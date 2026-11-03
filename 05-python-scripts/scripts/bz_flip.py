import re
# v0.1.20: album cover flip on track change.
# Holds the cover being shown in Home properties bz_cov_a / bz_cov_b; bz_cov_side says which layer is in front.
# On a track change the OLD cover stays up; the new cover is put on the hidden layer (and a hidden preload image)
# and only after it has had time to load do we switch sides, which plays the skin's flip animation.
import xbmc, xbmcgui, os, threading

def _dbgmm(msg):   # fork.2: Skin.HasSetting(bz_debug_mm) -> verbose MM warm log
    import time as _tq
    if xbmc.getCondVisibility('Skin.HasSetting(bz_debug_mm)'): xbmc.log('BEZEL DBGMM %.3f %s' % (_tq.time(), msg), xbmc.LOGWARNING)

def _np_safe():   # 4.4.0 O86: no Now Playing launch while Kodi is busy / mid track change
    try:
        return not xbmc.getCondVisibility('Window.IsActive(busydialog) | Window.IsActive(busydialognocancel) | Player.Caching | !Player.HasAudio | Window.IsActive(1112) | Window.IsActive(visualisation)')
    except Exception:
        return False
_np_last = [0.0]
def _np_open(src):   # 4.6.0 crash dig: one guarded launcher for every auto Now Playing (auto NP + tap on the playing song)
    import time as _tm
    try:
        if _tm.time() - _np_last[0] < 4.0: return False          # busy guard: never a second launch while the first is still opening
        if not _np_safe(): return False
        _np_last[0] = _tm.time()
        xbmc.log('BEZEL NP open (%s)' % src, xbmc.LOGINFO)
        xbmc.executebuiltin('RunScript(special://skin/scripts/bz_cmd.py,np)')
        return True
    except Exception as e:
        xbmc.log('BEZEL NP open failed (%s): %s' % (src, e), xbmc.LOGWARNING); return False
def _ptime():   # 4.6.0: play time from the info label (no xbmc.Player() object created 10x / s from a helper thread)
    try:
        v = xbmc.getInfoLabel('Player.Time(secs)').strip()
        if v.isdigit(): return float(v)
        hms = [int(x) for x in xbmc.getInfoLabel('Player.Time(hh:mm:ss)').split(':')]
        t = 0
        for x in hms: t = t * 60 + x
        return float(t)
    except Exception:
        return 0.0
def casc_len():   # 4.0.1 O21: full cascade length from the tuner (rows 1-15), plus a margin
    try:
        import json as _j, os as _o
        _d = _j.load(open(_o.path.join(_o.path.dirname(__file__), 'bz_tune.json')))
        def _v(i, dflt):
            s = xbmc.getInfoLabel('Skin.String(bz_at_%s)' % i); vals = _d['V'][i]
            k = int(s) if s.isdigit() and 1 <= int(s) <= len(vals) else dflt
            return vals[k - 1]
        _D = dict((p[0], p[2]) for p in _d['P']); cs, cg = _v('cascspeed', _D['cascspeed']), _v('cascstag', _D['cascstag'])
        return (14 * cg * cs / 400.0 + cs * 1.35) / 1000.0 + 0.25
    except Exception:
        return 1.6
def _flip_s():
    # BEZEL 3.0: flip time (s) from Skin.String(bz_at_flip) + bz_tune.json, read every flip (no file patch / reload needed for the script side)
    try:
        import json as _j
        _d = _j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bz_tune.json')))
        v = _d['V']['flip']; dflt = [p[2] for p in _d['P'] if p[0] == 'flip'][0]
        s_ = xbmc.getInfoLabel('Skin.String(bz_at_flip)')
        k = int(s_) if s_.isdigit() and 1 <= int(s_) <= len(v) else dflt
        return v[k - 1] / 1000.0
    except Exception:
        return 1.3

home = xbmcgui.Window(10000)
# BEZEL 3.1: Jumbo (900 px) album art is the default; set it once per profile, after that the tap / OK toggle and the tuner own it
xbmc.executebuiltin("Skin.Reset(bz_jumbo)"); xbmc.executebuiltin("Skin.Reset(bz_jumbo31)")   # 4.0.1 O36 (Rob): Jumbo / tap-to-enlarge removed; old saved strings cleared
import time as _t
def now0(): return _t.time()
def _bzstrip(home, row=None):
    # t4094c: hand focus to strip 6996 without rewinding it. A positional SetFocus is queued and can land AFTER keys already moved the
    # strip (late warm rewinds the row). Only force a row when the strip sits at 0 and the live row says otherwise (fresh window).
    # 5.33.190: never steal focus from Tuner 6970 / BEZEL Settings 6968
    if home.getProperty('bz_navtune') or home.getProperty('bz_navbez'): return
    live = row if row is not None else (home.getProperty('bz_mmlive') or home.getProperty('bz_mmpos') or '0')
    if xbmc.getCondVisibility('Control.HasFocus(6996)'): return   # 5.33.336 t2453: strip already focused = never re-SetFocus (re-focus flashed the row; Position 0 = MUSIC row was read as 'fresh' and yanked you back to Movies)
    cur = xbmc.getInfoLabel('Container(6996).Position') or '0'
    if cur == '0' and str(live) not in ('', '0'): xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % live)
    else: xbmc.executebuiltin('SetFocus(6996)')

def _bzfocus(cmd):
    # BETA 1.1: list / grid focus fixes must not steal the focus from the Now Playing dialog (or its slide menu) over the music window
    if not xbmc.getCondVisibility('Window.IsActive(1112)'): xbmc.executebuiltin(cmd)
if home.getProperty('bz_flip_running') != 'true':
    home.setProperty('bz_flip_running', 'true')
    # np3: the Tab keymap is installed by bz_cmd.py keymap (music window onload), so it also works when this script was already running
    home.setProperty('bz_flip_ver', 'np3')
    xbmc.executebuiltin('RunScript(special://skin/scripts/bz_cmd.py,keymap)')
    mon = xbmc.Monitor()
    LOAD_WAIT = 0.5  # seconds the new cover gets to load (preload image) before the flip
    import time
    # v0.1.24: sway phase. The sway (Includes_Bezel) runs while bz_audio_latch + no bz_sway_hold:
    # flat for 1.2 s, eases to -24 by 6.2 s, then a 20 s pulse -24..+24 -> flat at 11.2, 21.2, 31.2 ... s.
    sway = {'t0': None}
    def next_flat(now):
        t0 = sway['t0']
        if t0 is None: return now
        e = now - t0
        if xbmc.getCondVisibility('Skin.HasSetting(bz_swayright)'):
            # BETA 2 item 6: right sway: go at 2.4 s, then a 12 s cycle (1 s flat, 5 s out, 5 s back, 1 s flat): flat from 2.4 + 10 + 12k to 2.4 + 14 + 12k
            # 2.2 sway2fix: no flat hold; continuous 11 s cycle (5.5 s out, 5.5 s back), flat at 2.4 + 11k
            if e < 2.6: return now
            c = (e - 2.4) % 11.0
            if c < 0.2 or c > 10.9: return now
            return t0 + 2.4 + 11.0 * (int((e - 2.4) // 11.0) + 1)
        if e < 2.1: return now                      # still in the initial flat hold
        # BETA 2.3 item 13: 11.5 s half pulse (2 s still at +13): flat at 7.4 + 5.25 and 7.4 + 17.75 in every 23 s cycle
        if e <= 12.65: return t0 + 12.65
        n = int((e - 12.65) // 23.0)
        for f in (12.65 + 23.0 * n, 25.15 + 23.0 * n, 12.65 + 23.0 * (n + 1)):
            if f >= e: return t0 + f
        return t0 + 12.65 + 23.0 * (n + 1)
    # BETA 2.6 item 11: back-and-forth scroll of a long focused title. Kodi has no string-length condition, so the width of the focused row's
    # title is estimated here (Ubuntu Regular 28, uppercase, advance widths measured offline) and bucketed into bz_longt (shift in px) for the skin.
    _BZW = {'A': 18.6, 'B': 18.0, 'C': 17.4, 'D': 20.0, 'E': 16.0, 'F': 15.0, 'G': 18.8, 'H': 19.7, 'I': 7.5, 'J': 14.0, 'K': 17.6, 'L': 14.5, 'M': 24.4, 'N': 20.4, 'O': 21.8, 'P': 17.0, 'Q': 21.8, 'R': 17.6, 'S': 14.9, 'T': 15.8, 'U': 19.3, 'V': 18.4, 'W': 26.0, 'X': 17.7, 'Y': 16.8, 'Z': 16.0, '0': 15.8, '1': 15.8, '2': 15.8, '3': 15.8, '4': 15.8, '5': 15.8, '6': 15.8, '7': 15.8, '8': 15.8, '9': 15.8, ' ': 6.5, '.': 6.9, ',': 6.9, "'": 6.8, '-': 8.4, ':': 6.9, '&': 18.6, '(': 9.1, ')': 9.1, '!': 7.7, '?': 11.3, '/': 10.8}
    _bzlt = {'lbl': None}
    def _bz_longtitle():
        lbl = xbmc.getInfoLabel('$VAR[BezelListLabelF]') or xbmc.getInfoLabel('Container(60).ListItem.Label')
        music = xbmc.getCondVisibility('[Window.IsActive(music) | Window.IsActive(musicplaylist)] + [Container.Content(artists) | Container.Content(albums) | Container.Content(songs)]')
        key = (lbl, music)
        if key == _bzlt['lbl']: return
        _bzlt['lbl'] = key
        w = sum(_BZW.get(c, 17.0) for c in lbl.upper())
        over = w - (300 if music else 380)
        b = ''
        if over > 10:   # BETA 2.8 item 6: only titles clearly wider than the box scroll (estimate margin)
            for v in (20, 40, 60, 80, 110, 140, 180, 220, 280, 350, 420, 520, 640, 800, 960):
                if over <= v: b = str(v); break
            else: b = '960'
        if home.getProperty('bz_longt') != b: home.setProperty('bz_longt', b)
        _pp['t'] = time.time(); _pp['st'] = 0
        if home.getProperty('bz_lp'): home.clearProperty('bz_lp')
    # BETA 2.8 item 6: ping-pong timing (tuner: bz_at_pingspeed px/s, bz_at_pingpause s). bz_lp set = slid left (reversible Conditional slide)
    _pp = {'t': 0.0, 'st': 0}
    _PPS = (20, 25, 30, 35, 40, 50, 60, 70, 80, 89, 100, 120, 140, 160, 200); _PPP = (0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0)
    def _ppv(name, tab, d):
        v = xbmc.getInfoLabel('Skin.String(bz_at_%s)' % name)
        try: return tab[int(v) - 1]
        except Exception: return tab[d - 1]
    def _bz_pingpong():
        b = home.getProperty('bz_longt')
        if not b: return
        T = int(b) / float(_ppv('pingspeed', _PPS, 10)); P = _ppv('pingpause', _PPP, 5)
        e = time.time() - _pp['t']
        if _pp['st'] == 0 and e >= P: home.setProperty('bz_lp', '1'); _pp['st'] = 1; _pp['t'] = time.time()
        elif _pp['st'] == 1 and e >= T + P: home.clearProperty('bz_lp'); _pp['st'] = 2; _pp['t'] = time.time()
        elif _pp['st'] == 2 and e >= T: _pp['st'] = 0; _pp['t'] = time.time()
    # 5.33.170 BUG-021: Play Next stub cast shadows read ONE shared progress (sway['t0']) instead of their own Kodi timers,
    # so a stub/viz/Play Next load mid-cycle can't re-zero the cast out of step with the sway. Mirrors the sway timeline:
    # go 2.4 s (5 s lead-in 0 -> -13), pulse 7.4 s (hold D at -13, -13 -> +13 in 10 s, pulse reverses, T = D + 10250).
    # L bright at -13, R bright at +13 (same levels as the old 5.33.74 fades). Short sway: 0 -> -30, 5.5 s pulse from go.
    import math
    _cd = {'m': None, 'D': 2000}
    def _cast_D():
        try:
            import xbmcvfs
            f = xbmcvfs.translatePath('special://skin/xml/Includes_Bezel.xml'); m = os.path.getmtime(f)
            if m != _cd['m']:
                _cd['m'] = m
                import re as _re
                g = _re.search(r'<effect type="rotatey" start="0" end="0" center="1440" time="(\d+)"/><effect type="rotatey" start="-13" end="13" center="1440" time="10000"', open(f).read())
                if g and 0 <= int(g.group(1)) - 10250 <= 5000: _cd['D'] = int(g.group(1)) - 10250
        except Exception: pass
        return _cd['D'] / 1000.0
    def _sn(x):
        x = 0.0 if x < 0 else 1.0 if x > 1 else x
        return (1 - math.cos(math.pi * x)) / 2
    def _bz_cast(t0):
        L = R = None
        if t0 is not None and home.getProperty('bz_audio_latch') == 'true' and not home.getProperty('bz_sway_hold'):
            u = time.time() - t0
            if u >= 2.4 and xbmc.getCondVisibility('Skin.HasSetting(bz_swayright)'):
                w = (u - 2.4) % 11.0; q = _sn((w if w < 5.5 else 11.0 - w) / 5.5); L = 40 + 60 * q; R = 100 - 85 * q
            elif 2.4 <= u < 7.4:
                q = _sn((u - 2.4) / 5.0); L = 40 + 60 * q; R = 100 - 85 * q
            elif u >= 7.4:
                D = _cast_D(); T = D + 10.25; w = (u - 7.4) % (2 * T); f = w if w < T else 2 * T - w
                L = 100 - 85 * _sn((f - D) / 5.0); R = 15 + 85 * _sn((f - D - 5.0) / 5.0)
        # 5.33.171 BUG-021 follow-up: sway clock = cast timing/phase (above); overall level = Tuner Viz/stub opacity (bz_at_fsvizop) only. No art-brightness sampling.
        try: _vb = int(xbmc.getInfoLabel('Skin.String(bz_at_fsvizop)') or 11)
        except Exception: _vb = 11
        _vb = 1.0 if not 1 <= _vb <= 10 else (_vb - 1) / 10.0
        if _vb < 1.0:
            L = (100 if L is None else L) * _vb; R = (100 if R is None else R) * _vb
        for k, v in (('bz_castL', L), ('bz_castR', R)):
            v = '' if v is None else str(min(100, max(15 if _vb >= 1.0 else 0, int(round(v / 5.0)) * 5)))
            if v == '100': v = ''
            if home.getProperty(k) != v:
                if v: home.setProperty(k, v)
                else: home.clearProperty(k)
    import threading
    def sway_clock():   # v0.1.24: starts the sway / glare pulses 6.2 s after the sway (re)starts
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            # v0.1.26: a music window (list / fullscreen Now Playing / playlist) just (re)loaded: Kodi starts its sway at an arbitrary
            # state, so restart it from flat (glares hidden for the moment) and re-anchor the phase. Skipped while a flip owns the sway.
            if home.getProperty('bz_sway_restart'):
                home.clearProperty('bz_sway_restart')
                if not sway.get('busy') and sway['t0'] is not None:
                    home.setProperty('bz_flipping', 'true'); home.setProperty('bz_sway_hold', 'true')
                    if mon.waitForAbort(0.25): break
                    home.clearProperty('bz_sway_hold'); sway['t0'] = time.time()
                    if mon.waitForAbort(0.3): break
                    if not sway.get('busy'): home.clearProperty('bz_flipping')
            t0 = sway['t0']
            if home.getProperty('bz_sway_t0') != ('%.3f' % t0 if t0 is not None else ''): home.setProperty('bz_sway_t0', '%.3f' % t0 if t0 is not None else '')   # 3.5.3: for the music -> video wait-for-flat
            go = t0 is not None and not home.getProperty('bz_sway_hold') and time.time() - t0 >= 2.4   # 3.5.1: end of the still hold -> lead-in (5 s)
            if go and not home.getProperty('bz_sway_go'): home.setProperty('bz_sway_go', 'true')
            elif not go and home.getProperty('bz_sway_go'): home.clearProperty('bz_sway_go')
            on = t0 is not None and not home.getProperty('bz_sway_hold') and time.time() - t0 >= 7.4
            if on and not home.getProperty('bz_sway_pulse'): home.setProperty('bz_sway_pulse', 'true')
            elif not on and home.getProperty('bz_sway_pulse'): home.clearProperty('bz_sway_pulse')
            if home.getProperty('bz_audio_latch'): sway['bt0'] = None   # BETA 2.5: big album idle clock: runs only while no music plays (latch off)
            elif sway.get('bt0') is None: sway['bt0'] = time.time()
            bt0 = sway.get('bt0')   # big album one-shot (5 s) then pulse
            for k, d in (('bz_big_go', 2.5), ('bz_big_pulse', 7.5)):
                v = bt0 is not None and time.time() - bt0 >= d
                v = v and xbmc.getCondVisibility('Skin.HasSetting(bz_idlerock)')   # 5.33.231 HINGEFLIP: idle rock is a Tuner toggle, default Off
                if v and not home.getProperty(k): home.setProperty(k, 'true')
                elif not v and home.getProperty(k): home.clearProperty(k)
            on2 = on and time.time() - t0 >= 12.4   # 2.0a3.4: cross wobble, a quarter cycle after the swing, so the art keeps moving through the turns
            if on2 and not home.getProperty('bz_sway_pulse2'): home.setProperty('bz_sway_pulse2', 'true')
            elif not on2 and home.getProperty('bz_sway_pulse2'): home.clearProperty('bz_sway_pulse2')
            try: _bz_cast(t0)   # 5.33.170 BUG-021: stub cast opacity from this same sway clock
            except Exception: pass
            try: _bz_longtitle(); _bz_pingpong()   # BETA 2.6 item 11 / BETA 2.8 item 6
            except Exception: pass
            if mon.waitForAbort(0.05): break   # 2.0a3.3: was 0.02
    # 5.33.309: the tap-to-flip track list (back face) is deleted. This thread only keeps bz_albumid (album of the playing song) for the album content path.
    import json
    def rpc(method, params):
        try: return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}))).get('result')
        except Exception: return None
    def album_id():
        aid_song = None
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            song = xbmc.getInfoLabel('MusicPlayer.DbID')
            if song != aid_song:
                aid_song = song; aid = ''
                if song and xbmc.getCondVisibility('Player.HasAudio'):
                    d = (rpc('AudioLibrary.GetSongDetails', {'songid': int(song), 'properties': ['albumid']}) or {}).get('songdetails') or {}
                    aid = str(d.get('albumid') or '')
                    if aid == '0': aid = ''
                if aid: home.setProperty('bz_albumid', aid)
                else: home.clearProperty('bz_albumid')
            if mon.waitForAbort(0.5): break
    # 2.0a1: movies / TV poster (BEZEL list 60 in the video window). bz_psway is set after 5 s on one title (the poster eases
    # 0 -> 24 deg in 5 s), bz_ppulse 5 s later (the 20 s sway + glares, same as the album art). Both clear on a new title, so the
    # poster eases back to flat. The tap flip (bz_vback) shows the info back; it closes after 15 s without input (not while a
    # dialog is open), on Back (bz_vback_close), when the focused title changes or the list is focused again, fading to black first.
    def focus_back():   # 2.0a3: focus the first shown back button (SetFocus on the grouplist itself does not take)
        for c in ('6291', '6292', '6298', '6295', '6293'):
            if xbmc.getCondVisibility('Control.IsVisible(%s)' % c):
                xbmc.executebuiltin('SetFocus(%s)' % c); return
    # 5.33.367 Rob t2622: list-60 -> Home mirror for the 1122 poster stage (layer 6401). Dialog 1122 can't read Container(60)
    # (t4097), so every list-60 value BezelVPLPoster needs is copied here each poll. Frozen with the rest of poster_clock while a
    # modal / busy / info dialog is up (Container(60) reads empty from a script then), so the stage never blanks.
    # 5.33.389 Rob t2725 SETTINGS TREE: mirror of Includes_Bezel bz_set_hub/kodi/tools -> bz_setkids (verify: scripts/bz_tree_check.py)
    SETTINGS_TREE = (
        ('hub',   ('1130', '1131', '1117', 'addonbrowser')),
        ('kodi',  ('settings', 'systemsettings', 'servicesettings', 'playersettings', 'mediasettings', 'interfacesettings', 'profiles', 'skinsettings')),
        ('tools', ('systeminfo', 'eventlog', 'filemanager')),
    )
    # 5.33.390 Rob t2728 ART TREE: global artwork home (1122 / 6400) branched by STATE. Single registry of every Home prop each
    # state owns. Leave-clear reads it (no hand list to drift); scripts/bz_tree_check.py asserts every prop is real. Doc: behaviors/artwork-group.md
    ART_TREE = (
        ('poster.live',  ('bz_v60_next', 'bz_v60_art', 'bz_vpl_on')),          # 6401 poster layer: preload slot -> promoted shown poster, gate
        ('poster.hold',  ('bz_v60_mov', 'bz_v60_tv')),                          # held Movies / held TV (385 DUALHOLD)
        ('poster.meta',  ('bz_v60_lbl', 'bz_v60_parent', 'bz_v60_scroll', 'bz_v60_watched', 'bz_v60_resume', 'bz_v60_episodes', 'bz_m60_art')),
        ('album.idle',   ('bz_m_idle_a', 'bz_m_idle_b', 'bz_m_idle_side', 'bz_m_idle_art', 'bz_m_idle_lock')),   # 6402 idle random A/B + MMHOLD lock
        ('album.np',     ('bz_m_np_art',)),                                     # 6402 Now Playing (over idle while Player.HasAudio)
        ('gate.setkids', ('bz_setopen',)),
        ('gate.a2p',     ('bz_a2p_hold',)),                                     # 5.33.392 album->poster dissolve: album holds until poster gate rises                                      # SETTINGS latch -> poster opacity 0 over held art
    )
    _ART_CLEAR = tuple(k for b, ks in ART_TREE if b.startswith('poster.') for k in ks)   # poster.* cleared on Bezel leave (album.* holds, as before)
    _SETKIDS = '[' + ' | '.join('Window.IsActive(%s)' % w for _b, ws in SETTINGS_TREE for w in ws) + ']'   # = $EXP[bz_setkids]
    _V60_INFOWIN = '[Window.IsActive(music) | Window.IsActive(musicplaylist) | Window.IsActive(favourites) | Window.IsActive(favouritesbrowser) | Window.IsActive(programs) | Window.IsActive(games)]'
    _V60_GRIDV = 'Window.IsActive(videos) + Skin.HasSetting(bz_grid_video) + [Container(60).Content(movies) | Container(60).Content(tvshows) | Container(60).Content(seasons)]'
    def _v60_set(k, v):
        if home.getProperty(k) != v:
            if v: home.setProperty(k, v)
            else: home.clearProperty(k)
    _setopen_t = [0]
    _v60_pend = ['', 0.0]; _v60_gone = [0.0]   # 5.33.372 POSTERHOLD: staged art (preload slot bz_v60_next) + list-60 gap grace
    def _v60_art_stage(a):   # 5.33.372 Rob t2671-t2677: never overwrite bz_v60_art with an undecoded path. New art -> hidden preload slot first
        if not a or a == home.getProperty('bz_v60_art'): _v60_pend[0] = ''; _v60_set('bz_v60_next', ''); return   # empty = keep old (hold)
        now = _t.time()
        if a != _v60_pend[0]: _v60_pend[0] = a; _v60_pend[1] = now; _v60_set('bz_v60_next', a); return
        if now - _v60_pend[1] >= 0.6:   # preload slot had >= 0.6 s to decode -> promote; 6401's own image fades old->new from cache
            _v60_set('bz_v60_art', a); _v60_pend[0] = ''; _v60_set('bz_v60_next', '')
    # 5.33.385 DUALHOLD Rob t2700-t2702: split poster holds. bz_v60_mov = last Movies poster, bz_v60_tv = last TV poster (written
    # whenever list 60 promotes art in that content type). Target = MM highlighted row (Container(6996) sec) while MM is on the strip,
    # else the Videos list type. If the list isn't showing the target type yet, bz_v60_art is swapped to the matching hold (already
    # decoded earlier) so 6401 fades up a movie for Movies and a show for TV. Layer swap stays opacity-only; Music never feeds it.
    _V60_TYP = {'movies': 'Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets) | String.StartsWith(Container.FolderPath,videodb://movies/)]',
                'tv': 'Window.IsActive(videos) + [Container.Content(tvshows) | Container.Content(seasons) | Container.Content(episodes) | String.StartsWith(Container.FolderPath,videodb://tvshows/)]'}
    _V60_HK = {'movies': 'bz_v60_mov', 'tv': 'bz_v60_tv'}
    def _v60_ltype():
        for k, c in _V60_TYP.items():
            if xbmc.getCondVisibility(c): return k
        return ''
    def _v60_target(lt):
        if home.getProperty('bz_nav') == 'true' and xbmc.getCondVisibility('Control.HasFocus(6996)'):
            s2 = xbmc.getInfoLabel('Container(6996).ListItem.Property(sec)')
            return s2 if s2 in _V60_HK else ''
        return lt
    def _v60_dualpick():   # returns True when the list is NOT the target type (caller must not stage list-60 art over the hold)
        lt = _v60_ltype(); tg = _v60_target(lt)
        if not tg: return False
        if tg == lt and not xbmc.getCondVisibility('Container.IsUpdating'): return False
        h = home.getProperty(_V60_HK[tg])
        if h and home.getProperty('bz_v60_art') != h:
            _v60_pend[0] = ''; _v60_set('bz_v60_next', ''); _v60_set('bz_v60_art', h)
        return True
    def _v60_dualrec():
        lt = _v60_ltype(); a = home.getProperty('bz_v60_art')
        if lt and a and not xbmc.getCondVisibility('Container.IsUpdating') and _v60_target(lt) == lt: _v60_set(_V60_HK[lt], a)
    def v60_mirror():
        cv = xbmc.getCondVisibility; il = xbmc.getInfoLabel
        vid = cv('Window.IsActive(videos)'); oth = (not vid) and cv(_V60_INFOWIN)
        if home.getProperty('bz_setopen'):   # 5.33.370 Rob t2660: MM->Settings/Add-ons/Sources latch; keep 6401 gated through the nav-clear gap
            if cv('Window.IsActive(1130) | Window.IsActive(1131) | Window.IsActive(1117)'): home.clearProperty('bz_setopen')
            elif _t.time() - _setopen_t[0] > 2.0 and _setopen_t[0]: home.clearProperty('bz_setopen'); _setopen_t[0] = 0
            else:
                if not _setopen_t[0]: _setopen_t[0] = _t.time()
                _v60_set('bz_vpl_on', ''); return
        else: _setopen_t[0] = 0
        if cv(_SETKIDS):   # 5.33.388 Rob: every MM SETTINGS kid shows the global artwork group (poster 6401 from the held MM lane; album via bz_railvis)
            if home.getProperty('bz_pos_on') and not cv('Player.HasAudio + !Player.HasVideo'):
                pa = home.getProperty('bz_pos_b' if home.getProperty('bz_pos_side') == 'b' else 'bz_pos_a')
                if pa: _v60_art_stage(pa)
                _v60_set('bz_vpl_on', '1' if home.getProperty('bz_v60_art') or pa else '')
            else: _v60_set('bz_vpl_on', '')
            return
        if cv('Window.IsVisible(movieinformation) | Window.IsVisible(musicinformation) | Window.IsVisible(songinformation)'): return   # 5.33.379 Rob t2697: Info/Options on top -> list 60 unreadable from dialog; HOLD poster/art + bz_vpl_on (was cleared -> blank art)
        _dmis = _v60_dualpick()   # 5.33.385 DUALHOLD
        if not (vid or oth) or not cv('Control.IsVisible(60)'):
            # 5.33.372 POSTERHOLD: list 60 blinking out on a section swap / warm load no longer drops 6401 into an empty frame —
            # keep bz_vpl_on + the held art for a 1.5 s grace (or while the MM / a handoff is up), then clear as before.
            if vid and home.getProperty('bz_vpl_on'):
                if not _v60_gone[0]: _v60_gone[0] = _t.time()
                if (_t.time() - _v60_gone[0] < 1.5 or home.getProperty('bz_nav') == 'true' or home.getProperty('bz_tovideo') or home.getProperty('bz_m2v_flat')) and not home.getProperty('bz_setopen'):
                    return
            _v60_gone[0] = 0.0
            _v60_set('bz_vpl_on', ''); return
        _v60_gone[0] = 0.0
        par = cv('Container(60).ListItem.IsParentFolder')
        if vid:   # = $VAR[BezelPoster60V]
            a = ''
            if par: a = il('Container(60).ListItemNoWrap(1).Art(poster)') or il('Container(60).ListItemNoWrap(1).Art(tvshow.poster)')
            if not a: a = il('Container(60).ListItem.Art(poster)') or il('Container(60).ListItem.Art(tvshow.poster)')
            if not a and home.getProperty('bz_arthold'): a = home.getProperty('bz_hold_poster')
            if not a: a = il('Container(60).ListItem.Icon')
            if not _dmis: _v60_art_stage(a); _v60_dualrec()   # 5.33.385 DUALHOLD: list type == target -> stage + record per-type hold
            # 5.33.372: follows list 60 = the MM random idle row (UADVRAND / RANDSTART move it); staged, never blanked
            on = not cv(_V60_GRIDV) and not cv('Container.Content(episodes)') and not cv('Container.Content(actors)')
        else:     # = $VAR[BezelPoster60M] (music) ; other info-list windows have no art var
            a = ''
            if cv('Window.IsActive(music)'):
                if par: a = il('Container(60).ListItemNoWrap(1).Art(thumb)')
                if not a: a = il('Container(60).ListItem.Art(thumb)') or il('Container(60).ListItem.Icon')
            _v60_set('bz_m60_art', a)
            on = (not cv('[Window.IsActive(music) | Window.IsActive(musicplaylist)] + [Container.Content(artists) | Container.Content(albums) | Container.Content(songs)]')) and not cv('Container.Content(episodes)')
        _v60_set('bz_v60_lbl', '1' if il('Container(60).ListItem.Label') else '')
        _v60_set('bz_v60_parent', '1' if par else '')
        _v60_set('bz_v60_scroll', '1' if cv('Container(60).Scrolling') else '')
        _v60_set('bz_v60_watched', '1' if cv('Integer.IsGreater(Container(60).ListItem.PlayCount,0)') else '')
        _v60_set('bz_v60_resume', '1' if cv('Container(60).ListItem.IsResumable') else '')
        _v60_set('bz_v60_episodes', '1' if cv('Container.Content(episodes)') else '')
        _v60_set('bz_vpl_on', '1' if on else '')
    # 5.33.392 A2P (Rob t2746 GO): album->poster = ONE dissolve. 1122 drives both layers off $EXP[bz_artposter] (bz_vpl_on | handoff).
    # Gap fix: Music window leaves before list 60 / bz_vpl_on is ready -> bz_a2p_hold keeps the album up (railvis bypass) until the
    # poster gate rises (same frame -> album down + poster up together, 400 ms sine) or 1.5 s failsafe / non-Videos target.
    _a2p = [0.0, 0.0]   # [last time a Music window was active, hold start]
    def _a2p_tick():
        cv = xbmc.getCondVisibility; now = _t.time()
        if cv('Window.IsActive(music) | Window.IsActive(musicplaylist)'): _a2p[0] = now; _a2p[1] = 0.0; _v60_set('bz_a2p_hold', ''); return
        tov = cv('Window.IsActive(videos)') or home.getProperty('bz_tovideo') or home.getProperty('bz_m2v_flat')
        if tov and not home.getProperty('bz_vpl_on') and not home.getProperty('bz_setopen') and (_a2p[1] or now - _a2p[0] < 1.5):
            if not _a2p[1]: _a2p[1] = now
            if now - _a2p[1] < 1.5: _v60_set('bz_a2p_hold', '1'); return
        _a2p[0] = 0.0 if not tov else _a2p[0]; _a2p[1] = 0.0; _v60_set('bz_a2p_hold', '')
    # 5.33.384 IDLEAB (Rob parked 👍): idle Music album = two always-loaded 1122 slots bz_m_idle_a / bz_m_idle_b, bz_m_idle_side = shown slot.
    # New cover -> written into the HIDDEN slot only (preload), promoted after 0.6 s (= _v60_art_stage), then side flips -> 400 ms sine opacity A->B.
    # A slot is never rewritten while it is visible or still fading out (0.45 s guard) = no mid-fade texture swap. bz_m_idle_art = cover on screen (lock/hold logic).
    _mi = {'pend': '', 't': 0.0, 'flip': 0.0}
    def _m_idle_stage(a):
        now = _t.time(); side = home.getProperty('bz_m_idle_side') or 'a'
        if a is None:
            a = _mi['pend']
            if not a: return
        if a == home.getProperty('bz_m_idle_art'): _mi['pend'] = ''; return
        if not home.getProperty('bz_m_idle_art'):   # first cover (startup): straight into the shown slot
            _v60_set('bz_m_idle_' + side, a); _v60_set('bz_m_idle_side', side); _v60_set('bz_m_idle_art', a); _mi['pend'] = ''; return
        hid = 'b' if side == 'a' else 'a'
        if a != _mi['pend']:
            if now - _mi['flip'] < 0.45: _mi['pend'] = a; _mi['t'] = 0.0; return   # hidden slot still fading out -> wait
            _mi['pend'] = a; _mi['t'] = now; _v60_set('bz_m_idle_' + hid, a); return
        if not _mi['t']:
            if now - _mi['flip'] < 0.45: return
            _mi['t'] = now; _v60_set('bz_m_idle_' + hid, a); return
        if now - _mi['t'] >= 0.6:
            _v60_set('bz_m_idle_side', hid); _v60_set('bz_m_idle_art', a); _mi['flip'] = now; _mi['pend'] = ''
    def m_mirror():   # 5.33.368 Rob t2636: Music NP + idle list art mirrored into Home for the dual-preloaded 1122 big album (hold last when unseen)
        cv = xbmc.getCondVisibility; il = xbmc.getInfoLabel
        if cv('Player.HasAudio') and not cv('Window.IsActive(visualisation)'):
            a = il('Player.Art(thumb)')
            if a: _v60_set('bz_m_np_art', a)
        if cv('Window.IsActive(music)') and cv('Control.IsVisible(60)') and not home.getProperty('bz_m_idle_lock'):   # = BezelPoster60 music path; 5.33.369 MMHOLD: frozen on MM open until under_adv's first random step
            a = ''
            if cv('Container(60).ListItem.IsParentFolder'): a = il('Container(60).ListItemNoWrap(1).Art(thumb)')
            if not a: a = il('Container(60).ListItem.Art(thumb)') or il('Container(60).ListItem.Icon')
            if a: _m_idle_stage(a)
        if not home.getProperty('bz_m_idle_art') and home.getProperty('bz_cov_last'): _m_idle_stage(home.getProperty('bz_cov_last'))   # = bz_cov_last fallback
        _m_idle_stage(None)   # 5.33.384 IDLEAB: tick the pending promote
    ART_CYCLE = 24.5   # 5.33.391: Kodi pulse cycle of the album/poster sway (12250 ms anim, reversed) = 24.5 s
    def _art_epoch():
        # 5.33.391 Rob t2742 SHARED ART CLOCK: one sway clock for group 6400. Master = album t0 (music latch);
        # with no music a free-running epoch (set once) stands in. Published as Home bz_art_t0.
        t = sway['t0']
        if t is None:
            if sway.get('art0') is None: sway['art0'] = time.time()
            t = sway['art0']
        return t
    def _art_sw_anchor(now_):
        # Poster flags: pswayon at sw+4, ppulse at sw+9. Album: go at t0+2.4, pulse at t0+7.4.
        # Pick the earliest ppulse onset >= now+9 that sits on the album pulse grid (t0+7.4 + k*24.5).
        t0 = _art_epoch(); base = t0 + 7.4; want = now_ + 9.0
        k = max(0, int(math.ceil((want - base) / ART_CYCLE)))
        on = base + k * ART_CYCLE
        if on - want > ART_CYCLE: on -= ART_CYCLE
        home.setProperty('bz_art_t0', '%.3f' % t0)
        return on - 9.0
    def poster_clock():
        key = None; since = time.time(); was = False; closed_at = None; opened = 0; got = False; sw = [0]; pend = [None, 0.0]; sw_prev = [0]; sw_path = ['']; sw_top = [False]; sw_tchg = [0.0]
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            # t4465: remember the focused actor (dir) so the actor folder small art shows the actor thumb
            try:
                if xbmc.getCondVisibility('Window.IsActive(videos) + Container.Content(actors) + !Container(60).ListItem.IsParentFolder'):
                    _at = xbmc.getInfoLabel('Container(60).ListItem.Art(thumb)'); _ap = xbmc.getInfoLabel('Container(60).ListItem.FolderPath')
                    if _ap and home.getProperty('bz_actpath') != _ap: home.setProperty('bz_actthumb', _at); home.setProperty('bz_actpath', _ap)
            except Exception: pass
            # 3.5.1: a track change opens Kodi's busy dialog over the video window; while it (or any modal dialog) is up, Container(60) reads
            # empty from a script, which used to look like a new title and reset the poster hold / sway. Freeze the poster state until it closes.
            if key is not None and xbmc.getCondVisibility('Window.IsActive(videos) + [Window.IsVisible(busydialog) | Window.IsVisible(busydialognocancel) | System.HasModalDialog | Window.IsVisible(1111) | !String.IsEmpty(Window(Home).Property(bz_xinfo))]') and not home.getProperty('bz_vback'):  # 4.3 item 15: the poster stays while the info is up
                if mon.waitForAbort(0.1): break
                continue
            try: m_mirror()
            except Exception: pass
            try: v60_mirror(); _a2p_tick()   # 5.33.367: after the modal freeze, so a dialog never blanks the 1122 stage
            except Exception: pass
            # ALLBOTTOM2: hidden top *All never keeps focus (direction-aware), and Down-wrap off the last row goes to the bottom All row
            if xbmc.getCondVisibility('Control.HasFocus(60)'):
                try: _pos = int(xbmc.getInfoLabel('Container(60).CurrentItem') or 0); _n = int(xbmc.getInfoLabel('Container(60).NumItems') or 0)
                except Exception: _pos = 0; _n = 0
                _ab = 6097 if xbmc.getCondVisibility('Window.IsActive(music)') else 6098
                _fp = xbmc.getInfoLabel('Container.FolderPath')
                _ar = home.getProperty('bz_allret')
                if _ar and _fp == _ar and xbmc.getCondVisibility('Control.IsVisible(6097) | Control.IsVisible(6098)'):
                    home.clearProperty('bz_allret'); xbmc.executebuiltin('SetFocus(%d)' % _ab); sw_prev[0] = 0; sw_path[0] = _fp
                    if mon.waitForAbort(0.1): break
                    continue
                elif _ar and _fp != _ar and '/-1/' not in _fp: home.clearProperty('bz_allret')
                _fchg = sw_path[0] != _fp
                if _fchg: sw_tchg[0] = time.time()
                if _fchg and xbmc.getCondVisibility('Window.IsActive(videos) + Container.Content(seasons) + Container(60).ListItem.IsParentFolder + !Container(60).Scrolling') and _n > _pos:
                    xbmc.executebuiltin('Control.Move(60,1)'); sw_path[0] = _fp; sw_prev[0] = 0; mon.waitForAbort(0.15); continue  # 5.33.96: TV seasons open on the first real season, never '..'
                if sw_path[0] != _fp: sw_path[0] = _fp; sw_prev[0] = 0  # 5.33.95: folder change (open/Back) is never an Up-wrap — stale pos sent disc picker to Disc 2 + ALL
                _prev = sw_prev[0]; sw_prev[0] = _pos
                _tw = sw_top[0]; sw_top[0] = (time.time() - sw_tchg[0] > 0.8) and (_pos <= (0 if xbmc.getCondVisibility('String.IsEqual(Container(60).ListItemAbsolute(0).Label,..)') else 1)) and not _fchg  # 5.33.96: last poll sat on the top row ('..' or first)
                # t5111: Contains not EndsWith — TV *All is .../-1/?tvshowid=N; bounce every nav hit so Up/Down never stick on the invisible slot
                if xbmc.getCondVisibility('String.Contains(Container(60).ListItem.FolderPath,/-1/) + !String.Contains(Container.FolderPath,/-1/) + !Container(60).Scrolling'):  # t4112/t4113: only the hidden *All row itself, never items inside the All seasons folder (was auto-scrolling)
                    xbmc.executebuiltin('Control.Move(60,-1)' if (_prev and _prev > _pos) else ('Control.Move(60,1)' if _n > _pos else 'SetFocus(%d)' % _ab)); mon.waitForAbort(0.15)  # 5.33.95: let the bounce land before re-reading (double-move skipped Disc 1)
                # 5.33.91 t593: artist-albums cover column hides parent .. — never keep focus there (list-open shift / blank art); Up off first album wraps to ALL ALBUMS
                elif xbmc.getCondVisibility('Window.IsActive(music) + [Container.Content(albums) | Container.Content(songs)] + [String.StartsWith(Container.FolderPath,musicdb://artists/) | [String.StartsWith(Container.FolderPath,musicdb://albums/) + !String.IsEqual(Container.FolderPath,musicdb://albums/)]] + Container(60).ListItem.IsParentFolder + !Container(60).Scrolling') and _n > _pos:
                    if _prev and _prev > _pos and xbmc.getCondVisibility('Control.IsVisible(6097)'): home.setProperty('bz_allup', str(_n)); xbmc.executebuiltin('SetFocus(6097)')  # 5.33.109 t761: no visible jump to last; ALL onup restores; sw_prev[0] = 0  # last album remembered so Up off ALL lands on it
                    else: xbmc.executebuiltin('Control.Move(60,1)'); mon.waitForAbort(0.15)  # 5.33.95: let the bounce land before re-reading (double-move skipped Disc 1)
                # 5.33.96: TV seasons never rest on '..' — Up off the first season goes to ALL SEASONS (like discs), else back to the first season
                elif xbmc.getCondVisibility('Window.IsActive(videos) + Container.Content(seasons) + !String.Contains(Container.FolderPath,/-1/) + Container(60).ListItem.IsParentFolder + !Container(60).Scrolling') and _n > _pos:
                    if _prev and _prev > _pos and xbmc.getCondVisibility('Control.IsVisible(6098)'): home.setProperty('bz_allup', str(_n)); xbmc.executebuiltin('SetFocus(6098)')  # 5.33.109 t761: no visible jump to last; ALL onup restores; sw_prev[0] = 0; sw_top[0] = False
                    else: xbmc.executebuiltin('Control.Move(60,1)'); mon.waitForAbort(0.15)
                # t5111: inside All, ALLHIDE blanks parent .. — bounce to first real item so it is not selectable
                elif xbmc.getCondVisibility('String.Contains(Container.FolderPath,/-1/) + Container(60).ListItem.IsParentFolder + !Container(60).Scrolling'):
                    xbmc.executebuiltin('Control.Move(60,1)' if _n > _pos else 'noop'); mon.waitForAbort(0.15)  # 5.33.95: let the bounce land before re-reading (double-move skipped Disc 1)
                elif _tw and _n >= 2 and (_pos == _n or (_n > 6 and _pos >= _n - 3)) and not _fchg:  # 5.33.96: tolerate rapid taps past the wrap before the poll
                    # 5.33.96: Up-wrap off the top ('..' or first row) -> ALL row if shown, else stay put (no wrap to the last item)
                    if xbmc.getCondVisibility('Control.IsVisible(%d)' % _ab): xbmc.executebuiltin('SetFocus(%d)' % _ab)
                    else: xbmc.executebuiltin('SetFocus(60,0,absolute)')  # top row ('..' or first item)
                    sw_prev[0] = 0; sw_top[0] = True
                elif _prev and _n and _prev == _n and _pos <= 1 and xbmc.getCondVisibility('Control.IsVisible(%d)' % _ab):
                    xbmc.executebuiltin('SetFocus(%d)' % _ab); xbmc.executebuiltin('Control.Move(60,-1)'); sw_prev[0] = 0  # t4112: focus All first so the wrap-to-top never shows
            else: sw_prev[0] = 0; sw_top[0] = False
            vid = xbmc.getCondVisibility('Window.IsActive(videos) + Control.IsVisible(60)')
            # 2.0a3.5.1: keyed on the title and path only; the item index can shift when a refresh re-sorts the list
            k = (xbmc.getInfoLabel('Container(60).ListItem.DBID') + '|' + xbmc.getInfoLabel('Container(60).ListItem.Label') + '|' +
                 xbmc.getInfoLabel('Container.FolderPath')) if vid else None
            if xbmc.getCondVisibility('Container(60).ListItem.IsParentFolder'): k = None
            # 2.0a3.4: a new title hides the poster (blurred placeholder) and, once it has faded out (0.2 s), resets the sway to flat
            # while nobody sees it. 0.25 s after the list stops the poster fades in, holds still for 2 s (bz_pswayon then eases
            # into the sway over 5 s), bz_ppulse takes over the swing, bz_ppulse2 adds the cross wobble 5 s later.
            # A sway that is running is never reset while the focused title stays the same.
            lst = xbmc.getCondVisibility('Control.IsVisible(60)')
            kk = k if k is not None else (xbmc.getInfoLabel('Container(60).CurrentItem') + '|' + xbmc.getInfoLabel('Container(60).ListItem.Label') if lst else None)
            # 2.0a3.5: a list refresh (e.g. a track change updating play counts) briefly empties the focused item: keep the current poster
            if vid and key is not None and not xbmc.getInfoLabel('Container(60).ListItem.Label'): kk = key
            # t4097: Info / context / Choose art dialogs resolve Container(60) in the dialog (empty) -> keep the section poster + sway live
            if key is not None and xbmc.getCondVisibility('System.HasActiveModalDialog | System.HasVisibleModalDialog | Window.IsVisible(movieinformation) | Window.IsVisible(musicinformation) | Window.IsVisible(songinformation) | Window.IsVisible(selectdialog)'): kk = key
            # t4813 / 5.33.189: movies-only last poster+fanart hold — keep across TV/other sections (do NOT clear on !movies);
            # bridges empty Art(poster)/fanart when focusing Movies so the A/B lane never goes blank (TV unchanged: hold unused off movies)
            if xbmc.getCondVisibility('Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets) | String.StartsWith(Container.FolderPath,videodb://movies/)]'):
                _mp = xbmc.getInfoLabel('Container(60).ListItem.Art(poster)')
                if _mp and not os.path.basename(_mp.rstrip('/')).startswith('Default') and home.getProperty('bz_movposter_hold') != _mp:
                    home.setProperty('bz_movposter_hold', _mp)
                _mf = xbmc.getInfoLabel('Container(60).ListItem.Art(fanart)') or xbmc.getInfoLabel('Control.GetLabel(9880)')
                if _mf and home.getProperty('bz_movfanart_hold') != _mf:
                    home.setProperty('bz_movfanart_hold', _mf)
            now_ = time.time()
            # 2.0a3.5.1: debounce title key for fanart preload / tracking only (not for sway remount)
            if kk != key and key is not None and kk is not None and not xbmc.getCondVisibility('Container(60).Scrolling'):
                if pend[0] != kk: pend[0] = kk; pend[1] = now_
                if now_ - pend[1] < 0.4: kk = key
            if kk == key: pend[0] = None
            if kk != key:
                key = kk; since = now_; pend[0] = None
                # t4815: do NOT clear bz_pready / reset sway phase on title change (was remount hitch)
            # t4815 run-forever poster sway (Music sway_clock style): once armed, bz_pswayon/bz_ppulse/bz_ppulse2
            # advance from a phase timer and keep running until Videos is left. Title/focus changes never remount.
            # Texture still crossfades via existing fadetime on $VAR[BezelPoster60]. Movies + TV share this; Music untouched.
            alive = xbmc.getCondVisibility('Window.IsActive(videos)')
            scrolling = xbmc.getCondVisibility('Container(60).Scrolling')
            if alive and not home.getProperty('bz_vback') and not home.getProperty('bz_vbackanim'):
                if not home.getProperty('bz_pready'):
                    # first arm only: need a real item and a short quiet settle
                    if kk is not None and now_ - since >= 0.25 and not scrolling:
                        home.setProperty('bz_pready', 'true')
                        if not sw[0]:
                            sw[0] = _art_sw_anchor(now_)   # 5.33.391 Rob t2742: poster phase locked to the shared art clock
                if sw[0]:
                    e = now_ - sw[0]
                    for q, t_ in (('bz_pswayon', 4), ('bz_ppulse', 9), ('bz_ppulse2', 14)):   # 3.5.1: 0.5 s delay + 1.5 s fade + 2 s still hold
                        if e >= t_ and not home.getProperty(q): home.setProperty(q, 'true')
            elif not alive:
                if home.getProperty('bz_pready'): home.clearProperty('bz_pready')
                if sw[0]:
                    sw[0] = 0
                    for q in ('bz_pswayon', 'bz_ppulse', 'bz_ppulse2'):
                        if home.getProperty(q): home.clearProperty(q)
            if kk is not None and home.getProperty('bz_pfkey') != kk and time.time() - since >= 2.0:
                home.setProperty('bz_pfkey', kk); home.setProperty('bz_pfanart', xbmc.getInfoLabel('Container(60).ListItem.Art(fanart)'))   # info preload stays at 2 s
            # a tap before the poster / info was ready: flip now that it is (the request is never dropped)
            # BETA 2 item 23: the poster tap flip (bz_vreq -> bz_vback) is removed
            # 2.0a3.1: nothing focused after the window opens (Kodi's default control is not in this view): focus the list
            # t4085: never grab list 60 while the MM is open (Movies warm: empty focus mid-load -> SetFocus(60) flashed the list / left 6996)
            if vid and home.getProperty('bz_nav') != 'true' and not home.getProperty('bz_mmwarm') and not home.getProperty('bz_vback') and not home.getProperty('bz_vbackanim') and not xbmc.getInfoLabel('System.CurrentControlID') and not xbmc.getCondVisibility('System.HasModalDialog'): _bzfocus('SetFocus(60)')
            if home.getProperty('bz_vback') and was and time.time() - opened < 0.8 and k: home.setProperty('bz_vback_key', k)   # the tap moved off '..'
            on = bool(home.getProperty('bz_vback'))
            if on and not was:
                home.clearProperty('bz_vback_close'); home.setProperty('bz_vback_key', k or '')
                focus_back(); opened = time.time(); closed_at = None; got = False
            # 2.0a3.1: a slow device can take more than a second to show the back buttons; keep trying for 3 s, and only treat focus on the list
            # as 'left' once a back button really had focus (the first tap used to close the back again at once)
            if on and xbmc.getCondVisibility('ControlGroup(6290).HasFocus | ControlGroup(6297).HasFocus'): got = True
            if on and not got and time.time() - opened < 3.0:
                focus_back()   # the back buttons become focusable a frame after bz_vback is set
            if on and not home.getProperty('bz_vback_fade'):
                dialog = xbmc.getCondVisibility('System.HasModalDialog | Window.IsActive(selectdialog) | Window.IsActive(busydialog) | Window.IsActive(busydialognocancel)')
                left = got and xbmc.getCondVisibility('Control.HasFocus(60)')
                if (home.getProperty('bz_vback_close') or left or (k or '') != home.getProperty('bz_vback_key') or not vid
                        or xbmc.getCondVisibility('Player.HasVideo') or (not dialog and xbmc.getCondVisibility('System.IdleTime(15)'))):
                    home.clearProperty('bz_vback_close')
                    if vid and not xbmc.getCondVisibility('Control.HasFocus(60)'): _bzfocus('SetFocus(60)')
                    home.setProperty('bz_vback_fade', 'true')
                    if mon.waitForAbort(1.25): break
                    home.clearProperty('bz_vback'); on = False
            if was and not on: closed_at = time.time()
            if not on and home.getProperty('bz_vbackanim'):
                if closed_at is None: closed_at = time.time()
                if time.time() - closed_at >= 2.8:
                    home.clearProperty('bz_vbackanim'); home.clearProperty('bz_vback_fade'); closed_at = None
            was = on
            if mon.waitForAbort(0.1 if (vid or lst) else 0.5): break
    _bzth = []   # BEZEL 3.0 exit fix: helper threads are joined on shutdown (Kodi froze on Exit)
    def _bzstart(f):
        # 4.6.0 crash dig: a helper that raised used to die silently (thread exceptions do not reach kodi.log reliably) while
        # bz_flip_running stayed 'true', so a new bz_flip.py refused to start. Now the error is logged and the helper restarts
        # (max 5 times, 1 s apart); after that the whole script stops cleanly so the next RunScript can start fresh.
        def _guard():
            n = 0
            while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
                try:
                    f(); return
                except Exception:
                    import traceback
                    n += 1
                    xbmc.log('BEZEL bz_flip helper %s crashed (%d):\n%s' % (f.__name__, n, traceback.format_exc()), xbmc.LOGERROR)
                    if n >= 5:
                        home.setProperty('bz_flip_fail', f.__name__); home.clearProperty('bz_flip_running'); return
                    if mon.waitForAbort(1.0): return
        t = threading.Thread(target=_guard, daemon=True); _bzth.append(t); t.start()
    def km_leave_watch():   # 5.33.194 keymap quarantine: skin switched away from skin.bezel2 -> remove all BEZEL keymaps, stop helpers
        import sys as _s; _s.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_km
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            if not bz_km.on_bezel():
                bz_km.leave(); home.clearProperty('bz_flip_running'); return
            if mon.waitForAbort(1.0): return
    def albview_a():   # 5.33.237 t1843 view A: hold 3B album panel at album/disc level (bz_albva); D (default) = disc headers in list rows
        last = None
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            on = xbmc.getCondVisibility('Skin.HasSetting(bz_albview_a) + [Window.IsActive(music) | Window.IsActive(musicplaylist)] + Container.Content(songs) + String.StartsWith(Container.FolderPath,musicdb://) + !String.Contains(Container.FolderPath,songs/)')
            if on:
                dbid = xbmc.getInfoLabel('Container(60).ListItem.DBID'); disc = xbmc.getInfoLabel('Container(60).ListItem.DiscNumber')
                key = (xbmc.getInfoLabel('Container.FolderPath'), disc)
                if dbid and key != last and not xbmc.getCondVisibility('Container(60).Scrolling'):
                    last = key; home.setProperty('bz_albva', '1')
                    xbmc.executebuiltin('RunScript(special://skin/scripts/bz_artist.py,meta,song,%s,)' % dbid)
            elif last is not None or home.getProperty('bz_albva'):
                last = None; home.clearProperty('bz_albva')
            # 5.33.246 t1890 View D (default): right 3B = focused SONG (art, split title, DISC · TRACK · time, artist — album)
            d_on = (not on) and xbmc.getCondVisibility('!Skin.HasSetting(bz_albview_a) + Window.IsActive(music) + Container.Content(songs) + !Container(60).ListItem.IsParentFolder + !String.IsEmpty(Container(60).ListItem.Title) + [String.StartsWith(Container.FolderPath,musicdb://albums/) | String.StartsWith(Container.FolderPath,musicdb://artists/) | String.StartsWith(Container.FolderPath,musicdb://genres/) | String.StartsWith(Container.FolderPath,musicdb://years/) | String.Contains(Container.FolderPath,albums/)]')
            if d_on:
                g = lambda k: xbmc.getInfoLabel('Container(60).ListItem.' + k)
                t = g('Title'); w = t.split(' ', 1)
                bits = []
                if g('DiscNumber'): bits.append('Disc %s' % g('DiscNumber'))
                if g('TrackNumber'): bits.append('Track %s' % g('TrackNumber').lstrip('0'))
                if g('Duration'): bits.append(g('Duration'))
                aa = g('Artist'); al = g('Album')
                vals = {'bz_sd_n1': w[0], 'bz_sd_n2': w[1] if len(w) > 1 else '', 'bz_sd_meta': '  \u00b7  '.join(bits),
                        'bz_sd_alb': ' \u2014 '.join([x for x in (aa, al) if x]), 'bz_sd_thumb': g('Art(thumb)') or g('Icon')}
                for k, v in vals.items():
                    if home.getProperty(k) != v: home.setProperty(k, v)
                if home.getProperty('bz_albvd') != '1': home.setProperty('bz_albvd', '1')
            elif home.getProperty('bz_albvd'):
                home.clearProperty('bz_albvd')
            if mon.waitForAbort(0.1 if d_on else 0.25): return
    _bzstart(km_leave_watch)
    # 5.33.274 t2094: old music view types removed from options; clear leftover A/grid bools once so the 3-level list is the only view
    for _b in ('bz_albview_a','bz_grid_music'):
        if xbmc.getCondVisibility('Skin.HasSetting(%s)' % _b): xbmc.executebuiltin('Skin.Reset(%s)' % _b)
    _bzstart(albview_a)
    _bzstart(poster_clock)

    # 5.33.93: fanart_pop file check (FileExists($INFO[..]) is not valid in a skin condition -> parse error). Sets bz_fpop a/b/''.
    def fpop_clock():
        last = [None, '']
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            fp = xbmc.getInfoLabel('Player.FolderPath') if xbmc.getCondVisibility('Skin.HasSetting(bz_fs_fanartpop)') else ''
            if fp != last[0]:
                last[0] = fp; v = ''
                if fp:
                    import xbmcvfs
                    b = fp if fp.endswith('/') else fp + '/'
                    if xbmcvfs.exists(b + 'fanart_pop/bg.png') and xbmcvfs.exists(b + 'fanart_pop/fg.png'): v = 'a'
                    elif xbmcvfs.exists(b + '../fanart_pop/bg.png') and xbmcvfs.exists(b + '../fanart_pop/fg.png'): v = 'b'
                if v != last[1]:
                    last[1] = v
                    if v: home.setProperty('bz_fpop', v)
                    else: home.clearProperty('bz_fpop')
            if mon.waitForAbort(1.0): break
    _bzstart(fpop_clock)

    # UNDERADV (Rob t3741 / t3910): while the MM is open over a list (list text hidden), quietly step the underlay list 60 so the
    # fanart / poster changes. Hold N s after the MM opens, then one step every D s (wraps). Closing the MM / Select lands on the
    # advanced item (it IS the list position). K24: never during MM warm / Container.IsUpdating / dialogs; only Control.Move (no Container.Update).
    def under_adv():
        opened = None; last = 0.0; navwas = [False]; idwas = ['']
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            # 5.33.369 MMHOLD (Rob t2641-t2652): MM opens from Music -> lock bz_m_idle_art on the focused list-60 cover (warm/path churn can't swap it);
            # unlock on the first UADVRAND step (after hold) or MM close. Random never runs with MM closed (list browsing).
            _nv = home.getProperty('bz_nav') == 'true'
            if _nv and not navwas[0] and home.getProperty('bz_m_idle_art'): home.setProperty('bz_m_idle_lock', '1')
            if not _nv: home.clearProperty('bz_m_idle_lock')
            navwas[0] = _nv
            # 5.33.383 IDLERESET: MM auto-hide wake (bz_mmidle 1 -> clear) = fresh MM entry for idle art: re-lock the shown cover
            # and restart the UADVRAND hold (bz_uadv_hold, >=3 s) so no random step lands while the strip fades back in.
            _id = home.getProperty('bz_mmidle')
            if idwas[0] == '1' and not _id and _nv:
                opened = None
                if home.getProperty('bz_m_idle_art'): home.setProperty('bz_m_idle_lock', '1')
                xbmc.log('BEZEL IDLERESET: MM wake -> idle art hold restarted', xbmc.LOGINFO)
            idwas[0] = _id
            on = (home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmstart') and not home.getProperty('bz_mmwarm')
                  and not home.getProperty('bz_navtune') and not home.getProperty('bz_navset') and not home.getProperty('bz_navsub') and not home.getProperty('bz_kset')   # F10 batch2: pause while Tuner / settings card / submenu open
                  and not xbmc.getCondVisibility('Skin.HasSetting(bz_uadv_off)')
                  and xbmc.getCondVisibility('[Window.IsActive(videos) | Window.IsActive(music)] + Control.IsVisible(60) + !Container.IsUpdating + !System.HasModalDialog + !Window.IsVisible(1113) + !Window.IsVisible(1111) + !Window.IsVisible(1112) + !Player.HasVideo + Integer.IsGreater(Container(60).NumItems,1)'))
            if not on: opened = None
            else:
                now = time.time()
                try: hold = int(xbmc.getInfoLabel('Skin.String(bz_uadv_hold)') or 5); dly = int(xbmc.getInfoLabel('Skin.String(bz_uadv_delay)') or 8)
                except Exception: hold, dly = 5, 8
                hold = max(3, hold)   # 5.33.369 MMHOLD: focused art always holds >= 3 s on MM entry
                if opened is None: opened = now; last = now + hold - dly
                elif now - opened >= hold and now - last >= dly:
                    last = now
                    try: pos = int(xbmc.getInfoLabel('Container(60).CurrentItem') or 0); n = int(xbmc.getInfoLabel('Container(60).NumItems') or 0)
                    except Exception: pos = n = 0
                    lo = 2 if xbmc.getCondVisibility('String.Contains(Container(60).ListItemAbsolute(1).FolderPath,/-1/) | String.Contains(Container(60).ListItemNoWrap(1).FolderPath,/-1/)') else 1   # skip '..' (0) + ALLHIDE *All
                    # UADVRAND (Rob t3967/t3968/t3970): list hidden under MM -> random position (never same item); visible list keeps sequential (uadv only runs under MM)
                    import random as _rnd
                    nxt = _rnd.randint(lo, n) if n > lo else lo
                    if n > lo:
                        while nxt == pos: nxt = _rnd.randint(lo, n)
                    if n and nxt != pos: xbmc.executebuiltin('Control.Move(60,%d)' % (nxt - pos))
                    home.clearProperty('bz_m_idle_lock')   # 5.33.369 MMHOLD: hold over -> mirror follows the random steps
                    home.setProperty('bz_uadv_n', str(nxt))
            if mon.waitForAbort(0.25): break
    _bzstart(under_adv)

    # MMWARM TEST (t3400, reversible: delete this block + the bz_mmwarm guard in nav_menu). MM open on the strip (6996): the highlighted
    # Music / Movies / TV row loads its window UNDER the menu (debounced), menu stays up and focus returns to the same row.
    def mm_warm():
        WARM = {'music': ('Music', 'musicdb://artists/'),   # 5.33.164: MM Music underlay always Artists (art only); Select uses bz_lastmusic via bz_mm 'recent': ('Music', 'musicdb://recentlyplayedalbums/'),
                'movies': ('Videos', 'videodb://movies/titles/'), 'tv': ('Videos', 'videodb://tvshows/titles/')}
        last = [None, 0.0]; done = [None]; pk = [False]
        SS = {}   # 5.33.147 WARM 2.0: in-memory session store per section {row, path, backdrop, timer_on, parked_since}; cleared when MM closes
        BDW = 10.0   # WARM 2.0: backdrop dwell (s) while parked on a section — separate from bz_at_mmwarm park
        BDD = 'special://skin/extras/backdrop/'
        _SECM = {'music': 'Window.IsActive(music)', 'movies': 'Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets) | String.StartsWith(Container.FolderPath,videodb://movies/)]',
                 'tv': 'Window.IsActive(videos) + [Container.Content(tvshows) | Container.Content(seasons) | Container.Content(episodes)]'}
        def _snap(s2):   # WARM 2.0 (1)+(2): save leaving section row (0-based for SetFocus absolute) + path + backdrop
            if s2 not in WARM: return
            e = SS.setdefault(s2, {}); e['timer_on'] = False
            if 'row' in e and xbmc.getCondVisibility(_SECM[s2]) and not xbmc.getCondVisibility('Container.IsUpdating'):   # 5.33.218: only after a seeded/restored warm — an unseeded first pass (Music '..' row 0) no longer blocks RANDSTART
                try: e['row'] = max(0, int(xbmc.getInfoLabel('Container(60).CurrentItem') or 1) - (0 if xbmc.getInfoLabel('Container(60).ListItemAbsolute(0).Label') == '..' else 1))   # '..' row is absolute 0
                except ValueError: pass
                e['path'] = xbmc.getInfoLabel('Container.FolderPath')
            if home.getProperty('bz_backdrop'): e['backdrop'] = home.getProperty('bz_backdrop')
        def _randrow():   # 5.33.204 RANDSTART: random 0-based absolute row in list 60, skipping '..' and ALL/*All (like UADVRAND)
            import random as _rnd
            try: n = int(xbmc.getInfoLabel('Container(60).NumItems') or 0)
            except ValueError: n = 0
            if n <= 0: return None
            lo = 1 if xbmc.getInfoLabel('Container(60).ListItemAbsolute(0).Label') == '..' else 0
            hi = n - 1 + lo
            if '/-1/' in xbmc.getInfoLabel('Container(60).ListItemAbsolute(%d).FolderPath' % lo): lo += 1
            return _rnd.randint(lo, hi) if hi > lo else (lo if hi >= lo else None)
        def _cur0():   # 0-based absolute row of list 60 ('..' = 0), -1 unknown
            try: return int(xbmc.getInfoLabel('Container(60).CurrentItem') or 0) - (0 if xbmc.getInfoLabel('Container(60).ListItemAbsolute(0).Label') == '..' else 1)
            except ValueError: return -1
        def _defer(r, p2, spos):   # 5.33.219 RANDSTART path 2 (t1720u): SetFocus is ignored while list 60 is hidden under MM -> re-apply the row the moment 60 is visible
            def run():
                try: _run()
                finally: home.clearProperty('bz_randpend')   # 5.33.226 RANDFLASH: always release the list alpha
            def _run():
                stuck = None
                for i in range(12000):   # <=120 s, 10ms poll (5.33.230; was 20ms)
                    if mon.waitForAbort(0.01): return
                    if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') != p2.rstrip('/') or home.getProperty('bz_mmpick'): return
                    c = _cur0()
                    if c == r: _dbgmm('warm2 defer landed row=%d' % r); return
                    if not xbmc.getCondVisibility('Control.IsVisible(60)') or xbmc.getCondVisibility('Container.IsUpdating'): continue
                    mm = bool(home.getProperty('bz_nav'))
                    if not mm:
                        if stuck is None: stuck = c
                        elif c != stuck: return   # user moved the list themselves -> leave it
                    xbmc.executebuiltin('SetFocus(60,%d,absolute)' % r)
                    if mm: xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % (home.getProperty('bz_mmlive') or spos or '0'))   # 5.33.336 forced bounce (see _restore2)   # same-frame bounce: strip 6996 keeps focus
                    _dbgmm('warm2 defer apply row=%d mm=%d' % (r, mm)); mon.waitForAbort(0.03)
            home.setProperty('bz_randpend', '1')   # 5.33.226 RANDFLASH (t1796u): list 60 alpha 0 until the random row lands (no row-1 flash)
            threading.Thread(target=run, daemon=True).start()
        def _restore(s2, p2, spos):   # WARM 2.0 (1): after settle -> list row, then same-frame bounce back to strip 6996
            if s2 != 'music': return _restore2(s2, p2, spos)
            ok = [False]
            try: ok[0] = _restore2(s2, p2, spos)
            finally:
                if not ok[0]: home.clearProperty('bz_randpend')   # 5.33.230: no deferred apply -> release now
        def _restore2(s2, p2, spos):
            e = SS.get(s2) or {}; r = e.get('row')
            if r is None and not _pk() and xbmc.getInfoLabel('Container.FolderPath').rstrip('/') == p2.rstrip('/') and not xbmc.getCondVisibility('Container.IsUpdating'):
                r = _randrow()   # 5.33.204 RANDSTART: first visit (no session row) -> random list row, not top; seeded below
                if r is not None: e = SS.setdefault(s2, {}); e['row'] = r; e['path'] = p2; _dbgmm('warm2 randstart sec=%s row=%d' % (s2, r))
            if r is None or _pk() or (e.get('path') or '').rstrip('/') != p2.rstrip('/'): home.clearProperty('bz_randpend'); return   # 5.33.230: nothing to land -> release
            if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') != p2.rstrip('/') or xbmc.getCondVisibility('Container.IsUpdating'): home.clearProperty('bz_randpend'); return
            _lv = xbmc.getInfoLabel('Container(6996).Position') if xbmc.getCondVisibility('Control.HasFocus(6996)') else ''
            if _lv: home.setProperty('bz_mmlive', _lv)   # 5.33.336 t2453: live strip row at bounce time
            xbmc.executebuiltin('SetFocus(60,%d,absolute)' % r); xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % (_lv or home.getProperty('bz_mmlive') or spos or '0')) if not (home.getProperty('bz_navtune') or home.getProperty('bz_navbez')) else None   # 5.33.336: forced same-frame bounce (the HasFocus guard in _bzstrip would see 6996 still focused before SetFocus(60) lands)
            dfr = False
            if s2 == 'music': _defer(r, p2, spos); dfr = True   # 5.33.219 RANDSTART path 2: hidden Music list ignored SetFocus -> deferred apply when 60 is visible (MM close / list shown)
            home.setProperty('bz_warmrow', p2.rstrip('/'))   # 5.33.218: tell the grid sync this folder's list row is a WARM row (do not reset to item 0)
            _dbgmm('warm2 restore sec=%s row=%d' % (s2, r))
            return dfr
        def _bdpick():   # WARM 2.0 (3): new random backdrop (bz_cmd listing logic); honours a fixed Tuner image
            import xbmcvfs, random
            try: fs = sorted(f for f in xbmcvfs.listdir(BDD)[1] if f.lower().rsplit('.', 1)[-1] in ('png', 'jpg', 'jpeg', 'webp', 'gif'))
            except Exception: fs = []
            if len(fs) < 2 or xbmc.getInfoLabel('Skin.String(bz_bdimg)'): return None
            cur = home.getProperty('bz_backdrop'); return BDD + random.choice([f for f in fs if BDD + f != cur] or fs)
        def _pk():   # t5030: latch a Select made during this warm (bz_mmpick may be cleared by nav_menu before the warm ends)
            pk[0] = pk[0] or bool(home.getProperty('bz_mmpick')); return pk[0]
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            if mon.waitForAbort(0.05): return   # SPEED t3445: poll 100->50 ms
            if home.getProperty('bz_nav') != 'true' and not home.getProperty('bz_mmwarm') and xbmc.getCondVisibility('Window.IsActive(music) + !Container.IsUpdating'):
                _lp = xbmc.getInfoLabel('Container.FolderPath')   # MMQUEUE: keep last Music location for Select (bz_mm) — not for warm underlay
                _artists = _lp.rstrip('/') == 'musicdb://artists'
                if home.getProperty('bz_music_underlay') and _artists:
                    pass   # 5.33.164: MM Music underlay left artists up — do not overwrite real last browse
                elif _lp.startswith(('musicdb://', 'library://music/')) and _lp.rstrip('/') not in ('musicdb:', 'library://music') and 'recentlyplayed' not in _lp and _lp != home.getProperty('bz_lastmusic'):
                    if home.getProperty('bz_music_underlay'): home.clearProperty('bz_music_underlay')   # real browse after underlay
                    home.setProperty('bz_lastmusic', _lp)
            if not home.getProperty('bz_nav') and SS: SS.clear()   # WARM 2.0: session store lives only while MM is open
            if home.getProperty('bz_mmpick'): last[0] = None; done[0] = None; continue   # t5030: never start/continue a warm after a pick
            if home.getProperty('bz_nav') == 'true' and (home.getProperty('bz_mmidle') or xbmc.getCondVisibility('Control.HasFocus(6897)')):
                continue   # 5.33.374 IDLEWAKE (Rob t2682): MM auto-hide park 6897 is NOT leaving the strip - keep last/done so wake never re-arms a warm (list reload / RANDSTART reset the idle album)
            if home.getProperty('bz_nav') != 'true' or not xbmc.getCondVisibility('Control.HasFocus(6996)'):
                last[0] = None; done[0] = None; continue
            if home.getProperty('bz_mmstart') or home.getProperty('bz_secload') or home.getProperty('bz_navsub') or home.getProperty('bz_navset') or home.getProperty('bz_navtune') \
               or xbmc.getCondVisibility('Window.IsActive(1113) | Window.IsActive(1112) | System.HasModalDialog | Player.HasVideo + Window.IsActive(fullscreenvideo)'):
                continue   # K23: never during the start hold / splash
            sec = xbmc.getInfoLabel('Container(6996).ListItem.Property(sec)'); pos = xbmc.getInfoLabel('Container(6996).Position')
            now = time.time()
            if last[0] is None:   # the row the menu opened on is already the underlay: only a MOVE warms
                _m = {'music': 'Window.IsActive(music) + [String.IsEqual(Container.FolderPath,musicdb://artists/) | String.IsEqual(Container.FolderPath,musicdb://artists)]', 'movies': 'Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets) | String.StartsWith(Container.FolderPath,videodb://movies/)]',  # t4813 movies-only: as generous as TV (content flicker / sets / path)
                      'tv': 'Window.IsActive(videos) + [Container.Content(tvshows) | Container.Content(seasons) | Container.Content(episodes)]'}.get(sec)
                # 5.33.168 BUG-016: Music counts as already-warm only when artists root is up — album/other Music browse under MM re-warms to artists
                done[0] = sec if (not _m or xbmc.getCondVisibility(_m)) else None   # t4355: open row whose underlay does NOT match (start on TV over Music) warms it
            if sec != last[0]:
                if last[0] in SS: SS[last[0]]['timer_on'] = False; (home.getProperty('bz_backdrop') and SS[last[0]].__setitem__('backdrop', home.getProperty('bz_backdrop')))   # WARM 2.0 (3): scrolling away freezes the timer
                last[0] = sec; last[1] = now; continue
            try: park = 0.2 * int(xbmc.getInfoLabel('Skin.String(bz_at_mmwarm)') or 1)   # t4313: Tuner MAIN MENU park delay, step 1-10 = 0.2-2.0 s, default 0.2 (was 0.8)
            except ValueError: park = 0.2
            park = min(2.0, max(0.2, park))
            if sec in WARM and sec == done[0] and not home.getProperty('bz_mmwarm'):   # WARM 2.0 (3): focused + parked + warm done -> 10 s dwell cycles the backdrop
                e = SS.setdefault(sec, {})
                if not e.get('timer_on'): e['timer_on'] = True; e['parked_since'] = now; (home.getProperty('bz_backdrop') and e.__setitem__('backdrop', home.getProperty('bz_backdrop')))
                elif now - e['parked_since'] >= BDW and not xbmc.getCondVisibility('Container.IsUpdating'):
                    nb = _bdpick(); e['parked_since'] = now
                    if nb: home.setProperty('bz_backdrop', nb); e['backdrop'] = nb; _dbgmm('warm2 cycle sec=%s %s' % (sec, nb))
                continue
            if sec not in WARM or sec == done[0] or now - last[1] < park: continue   # t4313: wait until parked (was 200 ms)
            win, path = WARM[sec]
            try: _xf = (0, 0, 0.15, 0.25, 0.35, 0.5, 0.7, 1.0)[int(xbmc.getInfoLabel('Skin.String(bz_at_mmsecfade)') or 4)]   # t4339: Tuner MAIN MENU Section fade, 1=Off
            except (ValueError, IndexError): _xf = 0.35
            # 5.33.164: Music underlay path stays WARM artists only — never bz_lastmusic here (Select keeps last section in bz_mm)
            if sec == 'music': home.setProperty('bz_music_underlay', '1')   # mark artists load as underlay so tracking won't poison bz_lastmusic
            if xbmc.getCondVisibility('Container.IsUpdating'): continue   # FREEZE t3461: never stack a warm on a list still loading (TV->Movies while music played hung)
            if not xbmc.getCondVisibility('Window.IsActive(%s)' % win) and now - last[1] < max(park, 0.5): continue   # t4313 park (>=0.5); t3463: window switch only once you settle (500 ms); in-place stays 200 ms
            _snap(done[0] if done[0] in WARM else next((k for k in WARM if xbmc.getCondVisibility(_SECM[k])), None))   # WARM 2.0: snapshot the leaving underlay
            done[0] = sec; pk[0] = False
            if (SS.get(sec) or {}).get('backdrop'): home.setProperty('bz_backdrop', SS[sec]['backdrop'])   # WARM 2.0 (2): fade to cached image (onload picks only if empty)
            _dbgmm('warm-start sec=%s win=%s path=%s parked=%.3fs park=%.2f xf=%.2f' % (sec, win, path, now - last[1], park, _xf)); _t0 = time.time()   # fork.2 bz_debug_mm
            if xbmc.getCondVisibility('Window.IsActive(%s)' % win) and xbmc.getInfoLabel('Container.FolderPath').rstrip('/') == path.rstrip('/'):
                xbmc.log('BEZEL MMWARM: noop %s (already %s)' % (sec, path), xbmc.LOGWARNING); continue   # t3463: same window + same path -> nothing
            if sec == 'music' and (SS.get(sec) or {}).get('row') is None: (home.setProperty('bz_randpend', 'w'), threading.Thread(target=lambda: (mon.waitForAbort(15.0), home.getProperty('bz_randpend') == 'w' and home.clearProperty('bz_randpend')), daemon=True).start())   # 5.33.238 RANDFLASH3 (t1849u): set after the noop check; 15s fail-safe only (4s expired on the slow first cold Music DB load -> row 1 flashed); _restore always releases/defers
            def _clear_poster_lane():   # BUG-010: drop poster A/B + hold so Music never paints the poster frame (and vice versa)
                for k in ('bz_hold_poster', 'bz_pos_a', 'bz_pos_b', 'bz_pos_on', 'bz_pos_side', 'bz_pos_empty'):
                    home.clearProperty(k)
            def _xfade_out(enter_music):   # 5.33.204 mvidfade: Music<->video true fade — drop visibility now (1500 ms Hidden fade plays), drop textures after
                if enter_music: home.clearProperty('bz_pos_on'); home.clearProperty('bz_hold_poster')   # video poster A/B fades out over the new Music album
                else: home.clearProperty('bz_xalb_on')   # held Music album fades out under the incoming poster A/B
                def _late():
                    mon.waitForAbort(1.7)
                    if enter_music and not home.getProperty('bz_pos_on'):   # BUG-010: release poster lane once faded (skip if a video lane re-armed)
                        for k in ('bz_pos_a', 'bz_pos_b', 'bz_pos_side', 'bz_pos_empty'): home.clearProperty(k)
                    if not home.getProperty('bz_xalb_on'): home.clearProperty('bz_xalb')
                threading.Thread(target=_late, daemon=True).start()
            def _ahold():   # fork.5 SPEC 9.3 + BUG-010: same-family poster hold only; never Music→poster or poster→Music
                _gp = lambda *l: next((v for v in (xbmc.getInfoLabel(x) for x in l) if v), '')
                home.setProperty('bz_hold_fanart', _gp('Control.GetLabel(9880)', 'Container(60).ListItem.Art(fanart)', 'Window(Home).Property(script.grab.fanart.TV.FanArt)'))
                leave_music = xbmc.getCondVisibility('Window.IsActive(music)')
                leave_video = xbmc.getCondVisibility('Window.IsActive(videos)')
                enter_music = (sec == 'music')
                enter_video = (sec in ('movies', 'tv'))
                cross = (leave_music and enter_video) or (leave_video and enter_music)
                if leave_video and enter_music:   # 5.33.204 mvidfade: keep poster A/B textures + bz_pos_on so it can fade out in Music (_arel)
                    home.clearProperty('bz_hold_poster'); home.setProperty('bz_arthold', '1'); return
                if leave_music and enter_video:   # 5.33.204 mvidfade: hold the outgoing Music album so it fades out in Videos
                    _alb = _gp('Container(60).ListItem.Art(thumb)', 'Container(60).ListItem.Icon')
                    if _alb and not os.path.basename(_alb.rstrip('/')).startswith('Default'): home.setProperty('bz_xalb', _alb); home.setProperty('bz_xalb_on', '1')
                if cross or enter_music:
                    _clear_poster_lane()   # leaving frame cleared immediately across families; no poster hold into Music
                    home.setProperty('bz_arthold', '1')   # fanart hold only
                    return
                # Movies ↔ TV (same poster family): hold poster arts only — never Icon/thumb (Music bleed)
                hp = _gp('Container(60).ListItem.Art(poster)', 'Container(60).ListItem.Art(tvshow.poster)')
                if hp: home.setProperty('bz_hold_poster', hp)
                else: home.clearProperty('bz_hold_poster')
                home.setProperty('bz_arthold', '1')
            def _arel():   # release only once the new list has an item (max ~0.6 s), so no blank frame between swap and first art
                enter_music = (sec == 'music')
                arts = ('Container(60).ListItem.Art(thumb)', 'Container(60).ListItem.Art(icon)') if enter_music else ('Container(60).ListItem.Art(poster)', 'Container(60).ListItem.Art(tvshow.poster)')
                for i in range(45):   # 5.33.130 t948-950: also wait for the new item's art, so held art + section fade release together (no empty gap)
                    if xbmc.getInfoLabel('Container(60).ListItem.Label') and not xbmc.getCondVisibility('Container.IsUpdating') and (i >= 30 or any(xbmc.getInfoLabel(x) for x in arts)): break   # 5.33.131 / BUG-010: wait for family art
                    mon.waitForAbort(0.02)
                home.clearProperty('bz_xfade'); home.clearProperty('bz_xfin'); home.clearProperty('bz_arthold')   # 5.33.147: fade-in only
                if enter_music or home.getProperty('bz_xalb_on'): _xfade_out(enter_music)   # 5.33.204 mvidfade (BUG-010: poster lane released after the 1.5 s fade)
            _ahold()
            if xbmc.getCondVisibility('Window.IsActive(%s)' % win):   # MMWARM3 (t3420): that window is already under the menu -> no re-Activate (it closed MM ~1s later)
                # MMWARM4 (t3425): same window, different folder -> swap the list IN PLACE (no ActivateWindow reopen, menu stays up)
                home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)
                home.clearProperty('bz_xfin'); home.clearProperty('bz_xfade')   # 5.33.147: no section dim-out / no bz_xfin arm — fade-in only via art hold then release
                try:
                    xbmc.executebuiltin('Container.Update(%s,replace)' % path)
                    for i in range(40):
                        (_pk() or home.setProperty('bz_nav', 'true'))
                        if xbmc.getCondVisibility('Control.HasFocus(6996)'): pos = xbmc.getInfoLabel('Container(6996).Position') or pos; home.setProperty('bz_mmlive', pos)   # t4094c live from strip focus; oct27d walk: track live row, never restore a stale one
                        else: pos = home.getProperty('bz_mmlive') or pos; (_pk() or _bzstrip(home, pos))   # t4092 live row
                        mon.waitForAbort(0.025)
                        if i >= 12 and xbmc.getCondVisibility('Control.HasFocus(6996)') and not xbmc.getCondVisibility('Container.IsUpdating'): break   # SPEED: free the loop once loaded (was fixed 1s)
                    if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') != path.rstrip('/'):   # F2 batch2: path change in the same window must land (retry once)
                        xbmc.executebuiltin('Container.Update(%s,replace)' % path)
                        for i in range(40):
                            (_pk() or home.setProperty('bz_nav', 'true')); mon.waitForAbort(0.025)
                            if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') == path.rstrip('/') and not xbmc.getCondVisibility('Container.IsUpdating'): break
                    _restore(sec, path, pos)   # WARM 2.0 (1)
                    xbmc.log('BEZEL MMWARM: inplace %s in %s (%s) now=%s' % (sec, win, path, xbmc.getInfoLabel('Container.FolderPath')), xbmc.LOGWARNING)
                    _dbgmm('warm-done sec=%s took=%.3fs now=%s focus=%s' % (sec, time.time() - _t0, xbmc.getInfoLabel('Container.FolderPath'), xbmc.getInfoLabel('System.CurrentControlId')))   # fork.2
                finally:
                    _arel()   # fork.5 held art
                    home.clearProperty('bz_mmwarm'); home.clearProperty('bz_xfade')   # t4333: fade back in
                continue
            home.setProperty('bz_mmpos', home.getProperty('bz_mmlive') or pos or '0')   # t4094b live row first; FLASH t3430: new window's onload restores this row (was row 0 -> ~100ms previous-row flash)
            home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)
            home.clearProperty('bz_xfin'); home.clearProperty('bz_xfade')   # 5.33.147: no section dim-out / no bz_xfin arm — fade-in only via art hold then release
            try:
                xbmc.executebuiltin('ActivateWindow(%s,%s)' % (win, path))
                _pp = [pos]
                def _hold():   # MMWARM2 (t3407): keep focus locked on the strip for the whole warm
                    (_pk() or home.setProperty('bz_nav', 'true'))
                    if xbmc.getCondVisibility('Control.HasFocus(6996)'): _pp[0] = xbmc.getInfoLabel('Container(6996).Position') or _pp[0]; home.setProperty('bz_mmpos', _pp[0]); home.setProperty('bz_mmlive', _pp[0])   # t4094c   # oct27d walk: live row
                    else: _pp[0] = home.getProperty('bz_mmlive') or _pp[0]; home.setProperty('bz_mmpos', _pp[0] or '0'); (_pk() or _bzstrip(home, _pp[0]))   # t4092 live row
                for i in range(80):
                    _hold()
                    if i >= 4 and xbmc.getCondVisibility('Window.IsActive(%s)' % win): break
                    mon.waitForAbort(0.02)
                cur = xbmc.getInfoLabel('Container.FolderPath')
                if cur.rstrip('/') != path.rstrip('/'): xbmc.executebuiltin('Container.Update(%s,replace)' % path)
                for i in range(20):
                    (_pk() or home.setProperty('bz_nav', 'true'))
                    if xbmc.getCondVisibility('Control.HasFocus(6996)'): home.setProperty('bz_mmlive', xbmc.getInfoLabel('Container(6996).Position') or _pp[0]); break   # t4094c; JUMP t3450: never re-SetFocus a focused strip (yanked TV back to Movies when you moved on)
                    _pp[0] = home.getProperty('bz_mmlive') or _pp[0]; (_pk() or _bzstrip(home, _pp[0]))   # t4092 live row
                    mon.waitForAbort(0.05)
                for i in range(240 if sec == 'music' else 80):   # 5.33.238 RANDFLASH3: cold first Music load can exceed 4s -> wait <=12s; 5.33.218 RANDSTART: window-switch path waits (<=4s, Rob: solid wait OK under load screen) for the target list like the in-place path, so Music seeds a random row (was bailing on IsUpdating -> row 1)
                    if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') == path.rstrip('/') and not xbmc.getCondVisibility('Container.IsUpdating') and int(xbmc.getInfoLabel('Container(60).NumItems') or 0) > 0: break
                    (_pk() or home.setProperty('bz_nav', 'true')); mon.waitForAbort(0.05)
                _restore(sec, path, _pp[0])   # WARM 2.0 (1)
                xbmc.log('BEZEL MMWARM: %s under menu (%s)' % (sec, path), xbmc.LOGWARNING)
                _dbgmm('warm-done sec=%s took=%.3fs now=%s focus=%s' % (sec, time.time() - _t0, xbmc.getInfoLabel('Container.FolderPath'), xbmc.getInfoLabel('System.CurrentControlId')))   # fork.2
            finally:
                for i in range(15):
                    if _pk(): break   # t5030: Select during warm -> stop holding MM
                    _hold(); mon.waitForAbort(0.02)   # MMWARM2: hold through the list repaint
                _arel()   # fork.5 held art
                home.clearProperty('bz_mmwarm'); home.clearProperty('bz_mmpos'); home.clearProperty('bz_xfade')   # t4333
    _bzstart(mm_warm)
    # 2.0a1: slide-out section menu. The logo / Left set bz_nav (menu shown); focus it once visible, close it when focus leaves it
    ROOTS = ('', 'musicdb://', 'library://music/', 'videodb://', 'videodb://movies/', 'videodb://tvshows/', 'library://video/', 'sources://video/', 'sources://music/',
             'addons://sources/executable/', 'addons://sources/video/', 'addons://sources/audio/',
             'special://skin/playlists/bz_recent_songs.xsp')   # BETA 2 item 21: the startup / Recent Songs list is a top level: Back opens the slide menu (it fell back through Kodi's history)
    logo_t = [0.0]
    def nav_menu():
        stuck = [0, 0]; tabq = [0]
        had = False; t = 0
        big_t = [0]; fw_t = [0]; sj = [None, 0]; rp = [None, 0, None]; pl = [None, 0]; nav_was = [False, 0]; auto_spin = [time.time() + 30, 0]; biglogo_spin = [time.time() + 30, 0]; casc = [None, None]; casc_t = [0]; casc_pend = [None, 0, None]; dview = [None, 0]; fguard = [0]; autonp = [False]; autonp_t = [0]; autonp_np = [False]; autoinfo = [None]; fsauto = [False]
        navlk = [0.0]; navgr = [0.0]; navop = [0.0, 0]; mmst = [0]; fs_was = [False, 0]; gfirst = ['', 0]
        setret = [False, 0.0]   # F8 batch2 (t3930): Settings family was active -> Back reopens MM on SETTINGS (not TV)
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            now = time.time()
            _sw = xbmc.getCondVisibility('Window.IsActive(1130) | Window.IsActive(settings) | Window.IsActive(systemsettings) | Window.IsActive(interfacesettings) | Window.IsActive(mediasettings) | Window.IsActive(playersettings) | Window.IsActive(servicesettings) | Window.IsActive(pvrsettings) | Window.IsActive(gamesettings) | Window.IsActive(skinsettings) | Window.IsActive(profiles) | Window.IsActive(systeminfo)')
            if setret[0] and not _sw: setret[1] = now   # F8: left Settings just now
            setret[0] = _sw
            # 3.2.1 item 14: leaving fullscreen music (Now Playing 1112, the in-place Now Playing, visualisation, controls 1115) -> focus the music list (60)
            fsm = home.getProperty('bz_np') == 'true' or xbmc.getCondVisibility('Window.IsActive(1112) | Window.IsActive(1115) | Window.IsActive(visualisation)')
            # 5.33.378 Rob t2694u #2: FS opened while MM was open (or <0.8s after the opener cleared it) -> latch bz_fsmm; exit FS reopens MM, not the section list
            if home.getProperty('bz_nav') == 'true': fs_was.append(now) if len(fs_was) < 3 else fs_was.__setitem__(2, now)
            if fsm and not fs_was[0] and len(fs_was) > 2 and now - fs_was[2] < 0.8: home.setProperty('bz_fsmm', '1')
            if fs_was[0] and not fsm:
                fs_was[1] = now + 1.2
                if home.getProperty('bz_fsmm'):
                    home.clearProperty('bz_fsmm'); fs_was[1] = 0
                    if not xbmc.getCondVisibility('Player.HasVideo + Window.IsActive(fullscreenvideo)'):
                        home.clearProperty('bz_navgrace'); home.setProperty('bz_nav', 'true')
                        xbmc.log('BEZEL FSMM: left FS opened from MM -> MM', xbmc.LOGWARNING)
            fs_was[0] = fsm
            if fs_was[1]:
                if now > fs_was[1] or home.getProperty('bz_nav'): fs_was[1] = 0
                elif xbmc.getCondVisibility('Window.IsActive(music) + !System.HasModalDialog + Control.IsVisible(60) + !Control.HasFocus(60)'):
                    xbmc.executebuiltin('SetFocus(60)')
            # 3.2.1 item 11: the grid (6600) takes the focus first in every section / folder (music and video), like the AZR wall
            gp = xbmc.getInfoLabel('Container.FolderPath')
            if gp != gfirst[0]: gfirst[0] = gp; gfirst[1] = now + 2.5
            if gfirst[1]:
                if now > gfirst[1] or fs_was[1]: gfirst[1] = 0
                elif xbmc.getCondVisibility('Control.HasFocus(6600)'): gfirst[1] = 0
                elif not home.getProperty('bz_nav') and xbmc.getCondVisibility('[[Window.IsActive(music) + Skin.HasSetting(bz_grid_music) + [Container(60).Content(albums) | Container(60).Content(artists)]] | [Window.IsActive(videos) + Skin.HasSetting(bz_grid_video) + [Container(60).Content(movies) | Container(60).Content(tvshows) | Container(60).Content(seasons)]]] + Control.HasFocus(60) + !System.HasModalDialog + Control.IsVisible(6600) + Integer.IsGreater(Container(6600).NumItems,0) + !Container(6600).IsUpdating'):
                    xbmc.executebuiltin('SetFocus(6600)')
            # BETA 1.3: slide menu: Up / Down set bz_navlock (XML); further presses are ignored until the bar glide (280 ms) is done
            if home.getProperty('bz_navlock'):
                if not navlk[0]: navlk[0] = now
                elif now - navlk[0] >= 0.25: home.clearProperty('bz_navlock'); navlk[0] = 0.0
            else: navlk[0] = 0.0
            # BETA 1.4 item 7: an open drop-down closes once focus leaves its parent row and its sub rows
            ns = home.getProperty('bz_navsub')
            if ns and home.getProperty('bz_nav'):
                grp = {'music': (6901, 6941, 6942, 6943, 6944, 6945, 6946, 6947), 'movies': (6902, 6951, 6952, 6953, 6954, 6955, 6956), 'tv': (6903, 6961, 6962, 6963, 6964, 6965)}.get(ns)
                cid = xbmc.getInfoLabel('System.CurrentControlId')
                if grp and cid and cid.isdigit() and int(cid) not in grp: home.clearProperty('bz_navsub')
            # 3.5.1: the logo colour wipe is removed
            # 3.5.1: list cascade: a new folder in the music / video list toggles bz_casc a <-> b, which replays the rows' fade-in rise
            # 3.5.3: only for a folder change inside the same window; switching music <-> video no longer replays it (that 20 px rise read as a shift)
            fp = xbmc.getInfoLabel('Container.FolderPath') if xbmc.getCondVisibility('[Window.IsActive(music) | Window.IsActive(videos) | Control.IsVisible(60)] + !System.HasModalDialog + !Window.IsActive(visualisation) + !Window.IsActive(fullscreenvideo)') else None   # FS fade fix: Kodi's fullscreen music window has a hidden button 60, so its empty path was read as a folder change and the return replayed the cascade (list bar flicker)
            wid = xbmc.getInfoLabel('System.CurrentWindow')
            # 5.33.274 THREELEVEL (Rob t2073u): 270 MERGED13 Artists->all-songs hop removed; native Artists -> Albums (artists/ID/) -> album songs.
            if fp is not None and fp != casc[0]:
                # 3.5.7: direction: back = the new path is a parent of the old one (rows come from the left), else in (from the right)
                back = casc[0] is not None and len(fp) < len(casc[0]) and casc[0].startswith(fp)
                pair = ('c', 'd') if back else ('a', 'b')
                nxt = pair[1] if home.getProperty('bz_casc') == pair[0] else pair[0]
                entry = casc[0] is not None and (wid != casc[1] or not (fp.startswith(casc[0]) or casc[0].startswith(fp)))   # BETA 2 cascade fix: section entry (new window or unrelated path, not folder open/back) -> start 420 ms later, after the window switch + fade-in that hid the first rows
                if casc[0] is not None and (home.getProperty('bz_nav') or home.getProperty('bz_mmwarm')) and not home.getProperty('bz_casc_force'): home.setProperty('bz_casc_fp', fp); casc_pend[0] = None   # t3463: MM warm swaps under the menu never replay the list cascade
                elif casc[0] is not None and not home.getProperty('bz_casc_force'):
                    if entry: casc_pend[0] = nxt; casc_pend[1] = now + 0.6; casc_pend[2] = fp   # beta2.2: 0.6 s (was 0.42): old window 300 ms fade-out + new 300 ms fade-in, measured on :77; rows stay hidden (bz_casc_fp) until then
                    else: home.setProperty('bz_casc', nxt); home.setProperty('bz_casc_fp', fp)   # 4.2: switching sections (window change) also plays the row cascade
                elif home.getProperty('bz_casc_force'): home.clearProperty('bz_casc_force'); home.setProperty('bz_casc', nxt); home.setProperty('bz_casc_fp', fp)
                else: home.setProperty('bz_casc_fp', fp)   # beta2.2: first folder after start: show at once
                casc[0] = fp; casc[1] = wid
                casc_t[0] = now + (0.6 if casc_pend[0] else 0)
                fguard[0] = now   # 4.3 item 4: entering a list: the list owns the focus, not the player controls
                dview[0] = fp; dview[1] = now   # 4.3 item 13: default view per content, applied once per folder
            if dview[0] and now - dview[1] < 3:
                ct = xbmc.getInfoLabel('Container.Content')
                if ct:
                    dview[0] = None
                    # beta1 item 13: the main music Albums list defaults to BEZEL ALBUM LIST (grid off, bz_albumlist on)
                    if ct == 'albums' and xbmc.getInfoLabel('Container.FolderPath').startswith('musicdb://albums/') and not xbmc.getCondVisibility('Skin.HasSetting(bz_albumlist)'):
                        xbmc.executebuiltin('Skin.SetBool(bz_albumlist)')
                    want = {'albums': ('bz_grid_music', False), 'artists': ('bz_grid_music', False), 'songs': ('bz_grid_music', False),
                            'movies': ('bz_grid_video', False), 'tvshows': ('bz_grid_video', False), 'episodes': ('bz_grid_video', False)}.get(ct)
                    if want:
                        has = xbmc.getCondVisibility('Skin.HasSetting(%s)' % want[0])
                        if want[1] and not has: xbmc.executebuiltin('Skin.SetBool(%s)' % want[0])
                        # 3.2.1 item 11: the grid is a kept view choice (View options > View type); it is no longer reset on every folder, so the grid can take the focus first in every section
                        elif not want[1] and has and False: xbmc.executebuiltin('Skin.Reset(%s)' % want[0])
            if fguard[0] and now - fguard[0] < 2.5:
                if xbmc.getCondVisibility('Window.IsActive(music) + !String.IsEqual(Window(Home).Property(bz_np),true) + Control.IsVisible(60) + [Control.HasFocus(6161) | Control.HasFocus(6162) | Control.HasFocus(6163) | Control.HasFocus(6164) | Control.HasFocus(6165) | Control.HasFocus(6166) | ControlGroup(6389).HasFocus]'):
                    _bzfocus('SetFocus(60)')
            else: fguard[0] = 0
            # 4.3 item 19 (beta1 item 4: 60 s): music playing + music list idle 60 s -> Now Playing (same path as the menu / mini player)
            # beta1 item 3: the 15 s video info auto-open (4.3 item 14) is removed
            # np2 test: no longer needs the focus on the list (60) / 6600 exactly: any control of the music window counts (A-Z bar, grid, view pill,
            # focus left on the art after a tap), unless the slide menu, a flip back, the extended info or any dialog is up. Each idle period
            # logs once (kodi.log, 'BEZEL idle NP') whether it opened Now Playing or what blocked it.
            # 4.0.1 O30 (Rob): fullscreen music no longer opens by itself while music plays; it stays on the list (Tab / menu / tap on the playing song still open it)
            # 4.2.0 O57: auto fullscreen music, Tuner > Music > Auto fullscreen music (Off by default). The delay counts from play start; opens once per play session.
            _ad = {'2': 5, '3': 10, '4': 20, '5': 30, '6': 60}.get(xbmc.getInfoLabel('Skin.String(bz_at_autonp)'))
            _pl = xbmc.getCondVisibility('Player.HasAudio + !Player.HasVideo')
            # 4.3.0 O82: the delay is now idle time (no key press for N s) instead of time since play start, and it re-arms after Now Playing
            # closes or the track changes (was: once per play session, reset only when the music stopped)
            _np = bool(home.getProperty('bz_np')); _tk = xbmc.getInfoLabel('MusicPlayer.Title') + '|' + xbmc.getInfoLabel('Player.Filenameandpath')
            if not _pl: autonp[0] = False; autonp_t[0] = 0
            else:
                if autonp_t[0] != _tk or (autonp_np[0] and not _np): autonp[0] = False
                autonp_t[0] = _tk
            autonp_np[0] = _np
            if _ad and _pl and not autonp[0] and xbmc.getCondVisibility('System.IdleTime(%d)' % _ad) and not _np:
                why = [n for n, bad in (('not music window', not xbmc.getCondVisibility('Window.IsActive(music) + !Window.IsActive(visualisation)')),
                                        ('menu', bool(home.getProperty('bz_nav'))),
                                        ('dialog', xbmc.getCondVisibility('System.HasModalDialog | Window.IsActive(1111) | Window.IsActive(1112) | Window.IsActive(contextmenu) | Window.IsActive(musicinformation)'))) if bad]
                if not why and not _np_safe(): why = ['busy']   # 4.4.0 O86
                if not why:
                    autonp[0] = True
                    xbmc.log('BEZEL auto NP: open after %ss' % _ad, xbmc.LOGWARNING)
                    _np_open('auto')   # 4.6.0: guarded (cooldown + busy check right before the launch)
            # 5.33.325 t2420u/t2421u: Music section + music playing + 30 s no input -> Dialogue FS (1120). Once per idle period (any key re-arms).
            # Tuner > FULLSCREEN MUSIC > Open after 30 s idle in Music (bz_fsauto_off). Uses the same gate as the big-album tap (bz_pndlg_ok).
            if xbmc.getGlobalIdleTime() < 30: fsauto[0] = False
            elif not fsauto[0] and not xbmc.getCondVisibility('Skin.HasSetting(bz_fsauto_off)'):
                if xbmc.getCondVisibility('!Skin.HasSetting(bz_pndlg_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + !Window.IsActive(1120) + !Window.IsVisible(1121) + !System.HasModalDialog + !Window.IsActive(1111) + !Window.IsActive(1112) + !Window.IsActive(contextmenu) + !Window.IsActive(musicinformation) + !Window.IsActive(fullscreenvideo)') \
                        and not home.getProperty('bz_nav') and not home.getProperty('bz_np') and _np_safe():
                    fsauto[0] = True
                    xbmc.log('BEZEL auto Dialogue FS: open after 30s idle', xbmc.LOGWARNING)
                    home.setProperty('bz_rail', 'centre'); xbmc.executebuiltin('ActivateWindow(1120)')
            if casc_pend[0] and now >= casc_pend[1]: home.setProperty('bz_casc', casc_pend[0]); home.setProperty('bz_casc_fp', casc_pend[2]); casc_pend[0] = None   # beta2.2: unhide + cascade on the same tick
            if casc_t[0] and now - casc_t[0] > casc_len() and home.getProperty('bz_casc'):   # 4.0.1 O21 root cause: was a fixed 0.7 s, which cut rows 6-15 (still animating until ~1.25 s) and snapped them in at the end   # 3.5.7: rows created later (scroll / deep return) must not replay it
                home.clearProperty('bz_casc'); casc_t[0] = 0
            # 2.0a3: the grown mini player art shrinks back after 15 s without input, or when the music stops
            if home.getProperty('bz_minibig'):
                if not big_t[0]: big_t[0] = now
                if (now - big_t[0] >= 15 and xbmc.getCondVisibility('System.IdleTime(15)')) or home.getProperty('bz_audio_latch') != 'true':
                    home.clearProperty('bz_minibig'); big_t[0] = 0
            else: big_t[0] = 0
            # BEZEL 3.2.0: focus watchdog. Rob lost focus in the music lists (nothing focused, arrows dead until Esc): when the focused control in the
            # music / video library is gone or hidden (grid / art / Now Playing parts hidden while focused) for ~0.6 s, focus goes back to the list (60).
            if xbmc.getCondVisibility('[Window.IsActive(music) | Window.IsActive(videos)] + !System.HasModalDialog + !Window.IsActive(1112) + !Window.IsActive(musicosd) + !Window.IsActive(1115) + !Window.IsActive(contextmenu)'):
                _cid = xbmc.getInfoLabel('System.CurrentControlId')
                _trk = xbmc.getInfoLabel('MusicPlayer.Title') + '|' + xbmc.getInfoLabel('MusicPlayer.Album')   # SONGJUMP t3858: track change
                if _trk != sj[0]: sj[0] = _trk; sj[1] = now
                if _cid and _cid != '0' and xbmc.getCondVisibility('Control.IsVisible(%s)' % _cid): sj.append(_cid); del sj[2:-1]   # last good focus
                if home.getProperty('bz_nav') == 'true':
                    fw_t[0] = 0   # MM owns focus (hide-lists guard handles it)
                    if now - sj[1] < 2.5 and (not _cid or _cid == '0') and not xbmc.getCondVisibility('System.HasModalDialog') and not home.getProperty('bz_navtune') and not home.getProperty('bz_navbez'):
                        xbmc.executebuiltin('SetFocus(6996)')   # MM mini-player: song change dropped the strip focus; 5.33.190 skip while Tuner/Settings
                elif now - sj[1] < 2.5 and (not _cid or _cid == '0') and len(sj) > 2:
                    xbmc.executebuiltin('SetFocus(%s)' % sj[2]); fw_t[0] = 0   # SONGJUMP: song change dropped focus -> put it back on the SAME control (keeps grid + position)
                elif xbmc.getCondVisibility('Container.IsUpdating') and not (fw_t[0] and now - fw_t[0] >= 3.0):
                    pass   # 5.33.133 t962: updating holds the timer (was reset forever -> music list could stay unfocused); 3 s cap
                elif not _cid or _cid == '0' or not xbmc.getCondVisibility('Control.IsVisible(%s)' % _cid) or \
                        (_cid in ('6385', '9000') and xbmc.getCondVisibility('Window.IsActive(music)') and not home.getProperty('bz_np') and not home.getProperty('bz_npctl') and not home.getProperty('bz_lctl')):
                    # 5.33.133 t962: Music list losing focus -> also offscreen helper 6385 / hidden blade 9000 count as lost; music returns after 0.5 s (videos keep 1.0 s)
                    fw_t[0] = fw_t[0] or now
                    if now - fw_t[0] >= (0.5 if xbmc.getCondVisibility('Window.IsActive(music)') else 1.0):
                        xbmc.executebuiltin('SetFocus(6600)' if xbmc.getCondVisibility('Control.IsVisible(6600)') else 'SetFocus(60)'); fw_t[0] = 0
                else: fw_t[0] = 0
            else: fw_t[0] = 0
            # 2.0a3: fullscreen player controls (MusicOSD, opened with M) hide after 6 s without input
            if xbmc.getCondVisibility('Window.IsActive(1115) + System.IdleTime(6) + !System.HasModalDialog'):
                xbmc.executebuiltin('Dialog.Close(1115)')
            if xbmc.getCondVisibility('Window.IsActive(musicosd) + System.IdleTime(6) + !System.HasModalDialog + !Window.IsActive(1103) + !Window.IsActive(visualisationpresetlist)'):
                xbmc.executebuiltin('Dialog.Close(musicosd)')
            # 2.0a3.4: Now Playing controls hide after 5 s without input (focus back to the block) or when Now Playing ends
            if home.getProperty('bz_npctl') and (not home.getProperty('bz_np') or xbmc.getCondVisibility('System.IdleTime(10) + [!System.HasModalDialog | Window.IsTopMost(1112)]')):
                if xbmc.getCondVisibility('ControlGroup(6389).HasFocus | Control.HasFocus(6191) | Control.HasFocus(6192) | Control.HasFocus(6193) | Control.HasFocus(6171) | Control.HasFocus(6172) | Control.HasFocus(6173) | Control.HasFocus(6174) | Control.HasFocus(6175) | Control.HasFocus(6176) | Control.HasFocus(6177) | Control.HasFocus(6178) | Control.HasFocus(6179) | Control.HasFocus(6195) | Control.HasFocus(6196) | Control.HasFocus(6197) | Control.HasFocus(6198)') and home.getProperty('bz_np'):
                    xbmc.executebuiltin('SetFocus(6390)')
                home.clearProperty('bz_npctl')
            # BETA 1.1b: Tab pressed while Kodi's busy dialog was up (song opening): open Now Playing once it is gone (within 20 s)
            if home.getProperty('bz_tabq'):
                if not tabq[0]: tabq[0] = time.time()
                if time.time() - tabq[0] > 20: home.clearProperty('bz_tabq'); tabq[0] = 0
                elif not xbmc.getCondVisibility('Window.IsActive(busydialog) | Window.IsActive(busydialognocancel)'):
                    home.clearProperty('bz_tabq'); tabq[0] = 0
                    if xbmc.getCondVisibility('Window.IsActive(music) + !Window.IsActive(1112) + Player.HasAudio'): xbmc.executebuiltin('ActivateWindow(1112)')
            # BETA 1.1: music list full player controls (bz_lctl, opened from the compact bar): hide once the focus leaves them or after 10 s idle
            if home.getProperty('bz_lctl') == 'go':
                xbmc.sleep(40); xbmc.executebuiltin('SetFocus(6192)'); home.setProperty('bz_lctl', 'true')
            elif home.getProperty('bz_lctl'):
                onc = xbmc.getCondVisibility('Control.HasFocus(6191) | Control.HasFocus(6171) | Control.HasFocus(6192) | Control.HasFocus(6172) | Control.HasFocus(6173) | Control.HasFocus(6193) | Control.HasFocus(6196) | Control.HasFocus(6197) | Control.HasFocus(6174) | Control.HasFocus(6198) | Control.HasFocus(6177) | Control.HasFocus(6179) | Control.HasFocus(6195) | Control.HasFocus(6176) | Control.HasFocus(6160) | System.HasModalDialog') or not xbmc.getInfoLabel('System.CurrentControlId')   # a pointer over the panel background (no control) keeps it open
                if not onc or home.getProperty('bz_np') or xbmc.getCondVisibility('System.IdleTime(10) + !System.HasModalDialog'):
                    if onc and not xbmc.getCondVisibility('System.HasModalDialog'): _bzfocus('SetFocus(60)')
                    home.clearProperty('bz_lctl')
            # 2.0a3.1: the in-place Now Playing ends with the music
            if home.getProperty('bz_np') and home.getProperty('bz_audio_latch') != 'true': home.clearProperty('bz_np')
            # np1 test: the Now Playing dialog closes whenever bz_np is cleared (music stopped, logo, scripts)
            if not home.getProperty('bz_np') and xbmc.getCondVisibility('Window.IsActive(1112)'): xbmc.executebuiltin('Dialog.Close(1112)')
            # 2.0a3.1: Back at a section's top level opens the menu only on a separate press: the folder must have been shown for 0.6 s
            # (bz_rootarm = that path) before Back counts, so the Back that lands on the top level never opens it
            fp = xbmc.getInfoLabel('Container.FolderPath')
            if fp != rp[0]:
                _wid = xbmcgui.getCurrentWindowId()
                # 5.33.179 BUG-024: Favourites / Programs / Games freshly opened from MM arm the top level at once (no 0.6 s wait), so the first Back goes straight to MM
                _fresh = _wid != rp[2] and _wid in (10060, 10001, 10820)
                rp[0] = fp; rp[1] = now - (0.6 if _fresh else 0); rp[2] = _wid; home.clearProperty('bz_rootarm')
            elif rp[2] != xbmcgui.getCurrentWindowId(): rp[2] = xbmcgui.getCurrentWindowId()
            elif now - rp[1] >= 0.6 and (fp in ROOTS or (home.getProperty('bz_navroot') and fp.rstrip('/') == home.getProperty('bz_navroot').rstrip('/'))) and home.getProperty('bz_rootarm') != 'true':
                # 4.1: also the folder a side-menu submenu opened (bz_navroot): Back there opens the side menu
                home.setProperty('bz_rootarm', 'true')
                if fp not in ROOTS: home.setProperty('bz_atnavroot', 'true')
            if fp in ROOTS or not home.getProperty('bz_navroot') or fp.rstrip('/') != home.getProperty('bz_navroot').rstrip('/'):
                if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')
            # 2.0a3.1: a tap / Select on the playing song in the list (Kodi restarts it) opens the in-place Now Playing.
            # Kodi lists take no skin onclick, so this watches for the same file jumping back to its start while the list is focused.
            if xbmc.getCondVisibility('Player.HasAudio + !Player.HasVideo'):
                pf = xbmc.getInfoLabel('Player.Filenameandpath')
                pt = _ptime()   # 4.6.0: info label instead of xbmc.Player().getTime() (O86 crash dig)
                if pf == pl[0] and pl[1] > 2.0 and pt < 1.0 and not home.getProperty('bz_np') and _np_safe() and \
                        xbmc.getCondVisibility('Window.IsActive(music) + Control.HasFocus(60) + Container(60).ListItem.IsPlaying'):
                    _np_open('tap')
                pl[0] = pf; pl[1] = pt
            else: pl[0] = None; pl[1] = 0
            # 2.0a3.1: logo spin when the menu closes
            nv = bool(home.getProperty('bz_nav'))
            # 2.0a3.4: starts 0.75 s after the menu has closed
            if nav_was[0] and not nv: nav_was[1] = now
            # t4562: legacy bz_logospin (menu-close + old 30s) stays OFF — force-clear.
            if home.getProperty('bz_logospin'): home.clearProperty('bz_logospin')
            nav_was[1] = 0
            if nav_was[1] and now - nav_was[1] > 2.2: home.clearProperty('bz_logospin'); nav_was[1] = 0
            if auto_spin[1] and now - auto_spin[1] > 1.5: home.clearProperty('bz_logospin'); auto_spin[1] = 0
            if False and now >= auto_spin[0]:  # t4562: legacy 30s auto spin OFF
                if not home.getProperty('bz_logospin') and not nav_was[1] and not nv:
                    home.setProperty('bz_logospin', 'true'); auto_spin[1] = now; auto_spin[0] = now + 30
                else: auto_spin[0] = now + 2
            # t4908: Big Logo spin — pulse bz_biglogo_spin every 30s; clear after ~1.2s (1100ms anim + settle). Skip while MM open.
            if biglogo_spin[1] and now - biglogo_spin[1] > 1.2:
                home.clearProperty('bz_biglogo_spin'); biglogo_spin[1] = 0
            if now >= biglogo_spin[0]:
                if not home.getProperty('bz_biglogo_spin'):   # t4985: no MM gate — spin on every section/screen (bz_nav is set under MM-first)
                    home.setProperty('bz_biglogo_spin', 'true'); biglogo_spin[1] = now; biglogo_spin[0] = now + 30
                else:
                    biglogo_spin[0] = now + 2
            # 4.1: a closed menu reopens without the settings stack or a submenu
            # BEZEL 3.0: no offscreen menu control may ever hold focus: menu closed + focus inside 6898-6999 -> back to the list
            if not nv and not home.getProperty('bz_nav') and xbmc.getCondVisibility('[Window.IsActive(music) | Window.IsActive(videos)] + Integer.IsGreaterOrEqual(System.CurrentControlId,6898) + Integer.IsLess(System.CurrentControlId,7000)'):
                xbmc.log('bz_flip: stray focus in closed menu -> list', xbmc.LOGWARNING); xbmc.executebuiltin('SetFocus(60)')
            # BEZEL 3.0: M / Menu key lands in the hidden Estuary options blade (9000): route it to the slide menu, card 2 (view options)
            if xbmc.getCondVisibility('[Window.IsActive(music) | Window.IsActive(videos)] + !System.HasModalDialog + !Window.IsActive(musicinformation) + !Window.IsActive(movieinformation) + !Window.IsActive(songinformation) + [ControlGroup(9000).HasFocus | [Integer.IsGreaterOrEqual(System.CurrentControlId,6050) + Integer.IsLess(System.CurrentControlId,6090)]]'):
                xbmc.log('bz_flip: M -> slide menu card 2', xbmc.LOGWARNING)
                xbmc.executebuiltin('SetFocus(60)')
                if not nv and not home.getProperty('bz_navgrace') and not home.getProperty('bz_navlock'):
                    home.setProperty('bz_navcard2', 'true'); home.setProperty('bz_nav', 'true')
            # BEZEL 3.0: one close routine. Any close sets bz_navgrace (0.5 s lock + 0.3 s grace); every open path checks $EXP[bz_navok],
            # and an open that slips through during the grace is undone here, so Back / Left can never bounce the menu open again
            if nav_was[0] and not nv: home.setProperty('bz_navgrace', 'true'); navgr[0] = now
            elif nv and not nav_was[0] and home.getProperty('bz_navgrace') and now - navgr[0] < 0.8 and not home.getProperty('bz_mmstart'):
                home.clearProperty('bz_nav'); nv = False; xbmc.log('BEZEL menu: reopen inside the close grace ignored', xbmc.LOGWARNING)
            if home.getProperty('bz_navgrace') and now - navgr[0] >= 0.8: home.clearProperty('bz_navgrace')
            if nav_was[0] and not nv:
                home.clearProperty('bz_navset'); home.clearProperty('bz_navsub'); home.clearProperty('bz_navnp'); home.clearProperty('bz_navset2'); home.clearProperty('bz_kset'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navstrip'); home.clearProperty('bz_setret')   # 3.1
            if nv and not nav_was[0]: home.clearProperty('bz_setret') if not (setret[1] and now - setret[1] < 4.0) else None; had = False; t = 0; stuck[1] = 0; navop[0] = now   # 3.0.2: every open starts clean (a fast close + reopen kept 'had' and closed at once)
            if not nv: home.clearProperty('bz_mmlive')   # t4092
            nav_was[0] = nv
            # 2.0a3.4: logo long press. This Kodi has no <onlongclick>; a touch long press / mouse long click sends ContextMenu,
            # so a context menu that opens while the logo (6001) had focus is swapped for the side menu
            # BEZEL 3.0: the long-press ContextMenu -> menu swap is removed (CEC remote: a held key is repeats, it fired at random)
            if home.getProperty('bz_nav'):
                if xbmc.getCondVisibility('ControlGroup(6899).HasFocus'):
                    had = True; stuck[1] = 0; navop[1] = 0
                    if xbmc.getCondVisibility('Control.HasFocus(6996)') and not home.getProperty('bz_mmstart'): home.setProperty('bz_mmlive', xbmc.getInfoLabel('Container(6996).Position') or '0')   # 5.33.188 BUG-011: never latch the pre-start row as live   # t4092: live strip row (a late warm load never picks the row)
                    if home.getProperty('bz_mmstart'):
                        _sr = home.getProperty('bz_mmstartrow') or '0'   # t4315: Startup highlight - land on the chosen row before releasing MM-start
                        # 5.33.188 BUG-011 (restore 5.33.186): Tuner start row wins — hold MM-start (warm/MMHIDE parked) until strip REALLY sits on it;
                        # releasing same tick as SetFocus let warm read row 0 (Music) then jump; hold is startup-only (bz_mmstart)
                        home.setProperty('bz_navstrip', home.getProperty('bz_mmstartsec') or 'music'); home.setProperty('bz_mmlive', _sr); home.setProperty('bz_mmpos', _sr)
                        if not mmst[0]: mmst[0] = now
                        if xbmc.getInfoLabel('Container(6996).Position') != _sr and now - mmst[0] <= 6.0: xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % _sr)
                        else: home.clearProperty('bz_mmstart'); mmst[0] = 0; xbmc.log('BEZEL MM-start: menu focused row ' + _sr, xbmc.LOGWARNING)
                elif xbmc.getCondVisibility('Window.IsActive(1113)') or home.getProperty('bz_mmwarm'):
                    if home.getProperty('bz_mmwarm') and not home.getProperty('bz_mmpick') and xbmc.getInfoLabel('System.CurrentControlId') in ('60', '61', '62', '63', '64', '6600'): _bzstrip(home)   # t4094c: list took focus during warm swap -> strip at once
                    t = 0; navop[0] = now; navop[1] = 0; stuck[1] = 0   # MMWARM test: window swap under MM is not a close
                elif home.getProperty('bz_mmstart') and not had:
                    # 4.7.11 MM-first: after the splash, never auto-close the start menu; keep giving it the focus (slow Shield list load) up to 6 s
                    if not mmst[0]: mmst[0] = now
                    if now - mmst[0] > 6.0: home.clearProperty('bz_mmstart'); mmst[0] = 0; xbmc.log('BEZEL MM-start: focus timeout', xbmc.LOGWARNING)
                    else: xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % (home.getProperty('bz_mmstartrow') or '0')); home.setProperty('bz_navstrip', home.getProperty('bz_mmstartsec') or 'music');   # MMDEF t4014: Tuner Default section on start navop[0] = now; navop[1] = 0; stuck[1] = 0   # 4.7.8+ MM-start: hold the start menu open under the splash (focus can't land yet; it auto-closed before the splash faded)
                elif not had and t < 30:
                    # 4.1: open on the current section's row (or the first row)
                    if home.getProperty('bz_navcard2'):   # BEZEL 3.0: M / Menu key opens straight on card 2 (view options)
                        home.clearProperty('bz_navcard2'); vid = xbmc.getCondVisibility('Window.IsActive(videos)'); tgt = 6902 if vid else 6901   # t4142: music too -> Info > Section options; t4129: video section options live in Info > Section options
                    elif home.getProperty('bz_np') and xbmc.getCondVisibility('Player.HasMedia'): tgt = 6902 if xbmc.getCondVisibility('Player.HasVideo') else 6901   # 3.1: the current section
                    elif xbmc.getCondVisibility('Window.IsActive(settings) | Window.IsActive(systemsettings) | Window.IsActive(interfacesettings) | Window.IsActive(mediasettings) | Window.IsActive(playersettings) | Window.IsActive(servicesettings) | Window.IsActive(pvrsettings) | Window.IsActive(gamesettings) | Window.IsActive(skinsettings) | Window.IsActive(profiles) | Window.IsActive(systeminfo)'): tgt = 6909   # 4.7.8: Back from Settings lands on SETTINGS
                    elif home.getProperty('bz_setret') or (setret[1] and now - setret[1] < 4.0): tgt = 6909; setret[1] = 0; home.setProperty('bz_setret', '1'); home.setProperty('bz_mmpos', '10')   # F8 oct27f: latch SETTINGS for the whole open (tick 2+ fell to TV)   # F8 batch2: Back from Settings -> MM on SETTINGS
                    elif xbmc.getCondVisibility('Window.IsActive(music)'): tgt = 6901
                    elif xbmc.getCondVisibility('Window.IsActive(videos) + [Container.Content(tvshows) | Container.Content(seasons) | Container.Content(episodes)]'): tgt = 6903
                    elif xbmc.getCondVisibility('Window.IsActive(videos) + Container.Content(musicvideos)'): tgt = 6904
                    elif xbmc.getCondVisibility('Window.IsActive(videos)'): tgt = 6902
                    elif xbmc.getCondVisibility('Window.IsActive(pictures)'): tgt = 6908   # 5.33.16: Left from MyPics highlights PICTURES (was MUSIC)
                    elif xbmc.getCondVisibility('Window.IsActive(addonbrowser) | Window.IsActive(programs) | Window.IsActive(games)'): tgt = 6919   # 5.33.20: Left from Add-ons highlights ADD-ONS (was MUSIC)
                    else: tgt = 6901   # 3.1: the menu always opens on a section row
                    home.setProperty('bz_navstrip', {6902: 'movies', 6903: 'tv', 6909: 'settings'}.get(tgt, 'music'))   # 4.7.8: settings strip case (Back no longer shows Music)   # 3.1 right strip
                    home.clearProperty('bz_navdir')   # beta1 item 7: the bar shows on the row at once
                    if tgt in (6930, 6931): xbmc.executebuiltin('SetFocus(%d)' % tgt)
                    else: xbmc.executebuiltin('SetFocus(6996,%d,absolute)' % {6902: 1, 6903: 2, 6904: 3, 6908: 8, 6919: 9, 6909: 10}.get(tgt, 0))   # 4.1 O46: the strip list, on the current section
                    t += 1
                elif not xbmc.getInfoLabel('System.CurrentControlId') or (xbmc.getCondVisibility('Window.IsActive(1112)') and (not stuck[1] or now - stuck[1] < 0.3)):
                    # BETA 1.1: a blank focus for a moment (a list refresh / track change under the Now Playing dialog) is not the user leaving the menu
                    if not stuck[1]: stuck[1] = now
                elif (not home.getProperty('bz_mmpick') and not xbmc.getCondVisibility('System.HasModalDialog')
                      and xbmc.getInfoLabel('System.CurrentControlId') in ('60', '61', '62', '63', '64', '6600')
                      and xbmc.getCondVisibility('Window.IsActive(music) | Window.IsActive(videos)')):
                    # MMHIDE (Rob t3853/t3854): while MM is open the underlay list/grid may never hold the keys: hand focus straight back to the strip row
                    try: _p = int(home.getProperty('bz_mmlive') or (int(xbmc.getInfoLabel('Container(6996).CurrentItem') or 1) - 1))   # t4092: live row first
                    except Exception: _p = 0
                    _bzstrip(home, max(_p, 0)); navop[0] = now; navop[1] = 0; stuck[1] = 0
                    xbmc.log('BEZEL MMHIDE: underlay took focus under MM -> strip', xbmc.LOGWARNING)
                elif xbmc.getCondVisibility('Window.IsVisible(1118)'): navop[1] = 0   # t4623: Power list lives in the strip; MM stays open under it
                elif not navop[1]: navop[1] = now   # 3.0.2: focus must stay outside the menu 0.3 s before it auto-closes
                elif now - navop[0] < 1.0 and now - navop[1] < 0.3: pass
                elif now - navop[0] < 1.0 and not xbmc.getCondVisibility('System.HasModalDialog') and not home.getProperty('bz_mmpick'):   # t5031: a fast pick inside 1s of open is not a stolen focus (re-grab flashed the strip + jumped the list)
                    # 3.0.2: something (list refresh, stray SetFocus, mouse) took the focus right after opening: give it back instead of closing
                    if had and home.getProperty('bz_mmlive'): _bzstrip(home); navop[1] = 0; stuck[1] = 0   # t4092: re-grab on the LIVE row, never re-pick the section of the window that just loaded
                    else: had = False; t = 0; navop[1] = 0
                    xbmc.log('BEZEL menu: focus stolen just after open -> back to the menu', xbmc.LOGWARNING)
                elif now - navop[1] >= 0.3:
                    home.clearProperty('bz_nav'); had = False; t = 0; stuck[1] = 0; navop[1] = 0
            else:
                had = False; t = 0
                if home.getProperty('bz_mmpick'): home.clearProperty('bz_mmpick')
                # np2: never leave the keys on the hidden slide menu: if the menu closed while (or just before) its row took the focus
                # (fast Left / Back presses, or a dialog closing over it), hand the focus back to the list
                if xbmc.getCondVisibility('ControlGroup(6899).HasFocus + !System.HasModalDialog'):
                    if not stuck[0]: stuck[0] = time.time()
                    elif time.time() - stuck[0] > 0.3 and not home.getProperty('bz_nav'):
                        xbmc.executebuiltin('SetFocus(60)' if xbmc.getCondVisibility('Control.IsVisible(60)') else 'SetFocus(9000)'); stuck[0] = 0
                else: stuck[0] = 0
            if mon.waitForAbort(0.05 if (nv or nav_was[1]) else 0.1): break   # 2.0a3.3: slower when the menu is closed
    def grid_sync():
        # 3.5.5: joined scroll. The list (60) leads while it has focus: when its item crosses a grid row, the unfocused grid (6600) is
        # scrolled one row in the same instant (Control.Move steps a vertical panel by rows; the panel only scrolls when its cursor leaves
        # the view, so the cursor is first pushed one row past the edge, then brought back onto the item). The item stays on the anchor row
        # (row 1) except at the top / bottom. Both scroll with the same scrolltime / tween (quadratic 200). The lit slot (bz_gslot) and the
        # number of filled slots (bz_gn) drive the fixed overlay frames. When the grid has focus it leads and the list follows (DBID map).
        C = 4; A = 1
        st = {'sig': None, 'map': {}, 'm60': {}, 't': 0, 'cr': 0, 'j': None, 'g': None, 'gb': 'a'}
        def key(c, i):
            return xbmc.getInfoLabel('Container(%d).ListItemAbsolute(%d).DBID' % (c, i)) or xbmc.getInfoLabel('Container(%d).ListItemAbsolute(%d).Label' % (c, i))
        def cur(c):
            try: return int(xbmc.getInfoLabel('Container(%d).CurrentItem' % c)) - 1
            except Exception: return -1
        def amap(c):
            n = int(xbmc.getInfoLabel('Container(%d).NumAllItems' % c) or 0)
            return {key(c, i): i for i in range(n)}
        def lit(j, n, V):
            home.setProperty('bz_gslot', '' if j is None else str((j // C - st['t']) * C + j % C))
            home.setProperty('bz_gn', str(max(0, min(V * C, n - st['t'] * C))))
        def gscroll():
            st['gs'] = time.time(); home.setProperty('bz_gscroll', '1')
        def place(j, n, V):
            rows = (n + C - 1) // C; r = j // C
            t1 = max(0, min(r - A, rows - V)); mv = []
            if t1 > st['t']: mv.append(t1 + V - 1 - st['cr']); st['cr'] = t1 + V - 1
            elif t1 < st['t']: mv.append(t1 - st['cr']); st['cr'] = t1
            st['t'] = t1
            if r != st['cr']: mv.append(r - st['cr']); st['cr'] = r
            if any(mv): gscroll()   # 4.2 item 9: overlay frames off while the grid scrolls
            for m in mv:
                if m: xbmc.executebuiltin('Control.Move(6600,%d)' % m)
            lit(j, n, V)
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            try:
                if xbmc.getCondVisibility('Control.IsVisible(6600) + !Container(6600).IsUpdating + !Container(60).IsUpdating + Integer.IsGreater(Container(6600).NumItems,0)'):
                    V = 4 if xbmc.getCondVisibility('Window.IsActive(music)') else 3
                    n = int(xbmc.getInfoLabel('Container(6600).NumItems') or 0)
                    sig = (xbmc.getInfoLabel('Container(60).FolderPath'), n, xbmc.getInfoLabel('Container(60).NumAllItems'))
                    if sig != st['sig']:
                        # new folder: Kodi may restore an old grid selection / offset that the unfocused panel does not read back, so put the
                        # grid on item 0 (offset 0) once, then give the focus straight back (known start for the row tracking)
                        gf = xbmc.getCondVisibility('Control.HasFocus(6600)')
                        same = st.get('fp') == sig[0]
                        st['fp'] = sig[0]
                        mp = amap(6600); j0 = None
                        if same:
                            # 4.2 item 23: same folder refreshed (new song / library update): hold the grid on the current list item instead of item 0
                            j0 = mp.get(xbmc.getInfoLabel('Container(60).ListItem.DBID') or xbmc.getInfoLabel('Container(60).ListItem.Label'))
                        if j0 is None and home.getProperty('bz_warmrow') and home.getProperty('bz_warmrow') == (sig[0] or '').rstrip('/'):
                            # 5.33.218 RANDSTART: WARM just put list 60 on a random/saved row -> grid follows that item instead of resetting to 0
                            home.clearProperty('bz_warmrow'); j0 = mp.get(xbmc.getInfoLabel('Container(60).ListItem.DBID') or xbmc.getInfoLabel('Container(60).ListItem.Label'))
                        if j0 is None:
                            # 4.6.2 nav3: the colour block reads list 60, which Kodi restores to the OLD selection: put it on item 0 with the grid
                            if not gf: _bzfocus('SetFocus(60,0,absolute)')
                            _bzfocus('SetFocus(6600,0,absolute)')
                            # BEZEL 3.1 item 6: in grid view a new folder gives the grid the focus first (the list follows it)
                            gview = xbmc.getCondVisibility('[Window.IsActive(music) + Skin.HasSetting(bz_grid_music)] | [Window.IsActive(videos) + Skin.HasSetting(bz_grid_video)]') and not same
                            if not gf and not gview: _bzfocus('SetFocus(60)')
                            st.update(sig=sig, map=mp, m60=amap(60), t=0, cr=0, j=None, g=None, gfoc=None); home.clearProperty('bz_gtitle')
                        else:
                            if not gf: _bzfocus('SetFocus(6600,%d,absolute)' % j0)
                            if mon.waitForAbort(0.05): break
                            try: pos = int(xbmc.getInfoLabel('Container(6600).Position'))
                            except Exception: pos = j0 % C
                            if not gf:
                                for _ in range(25):
                                    _bzfocus('SetFocus(60)')
                                    if mon.waitForAbort(0.04) or xbmc.getCondVisibility('Control.HasFocus(60)'): break
                            st.update(sig=sig, map=mp, m60=amap(60), t=max(0, j0 // C - pos // C), cr=j0 // C, j=j0, g=None, gfoc=None)
                            lit(j0, n, V)
                        if mon.waitForAbort(0.1): break
                        home.clearProperty('bz_gpend')   # 4.6.2 nav3: list + grid agree now: show the section
                    if not xbmc.getCondVisibility('Control.HasFocus(60)') and home.getProperty('bz_grest'): home.clearProperty('bz_grest'); st['rk'] = None
                    if xbmc.getCondVisibility('Control.HasFocus(6600)'):
                        g = cur(6600)
                        if g >= 0 and g != st['g']:
                            st['g'] = g
                            st['gb'] = 'b' if st['gb'] == 'a' else 'a'; home.setProperty('bz_gb', st['gb'])
                            try:
                                pos = int(xbmc.getInfoLabel('Container(6600).Position'))
                                t2 = max(0, g // C - pos // C)
                                if t2 != st['t']: gscroll()
                                st['t'] = t2
                            except Exception: pass
                            st['cr'] = g // C; st['j'] = g; lit(g, n, V)
                        if g >= 0:
                            # 4.2: grid leads: the list follows with a smooth scroll
                            st['gfoc'] = g
                            k = key(6600, g); j = st['m60'].get(k)
                            p = st['m60'].get(xbmc.getInfoLabel('Container(60).ListItem.DBID') or xbmc.getInfoLabel('Container(60).ListItem.Label'))
                            # 4.3 item 6: the list no longer follows while the grid has focus (no block / fanart flicker); it jumps once on return
                            # BETA 1.1: ...but the colour block (title, year, fanart, details) reads the list item (media window ListItem = view 60), so the
                            # hidden list (faded out while the grid has focus) is moved in ONE jump to the focused grid item once the grid rests 0.15 s
                            if j is not None and p is not None and j != p:
                                if not st.get('gm') or st['gm'][0] != g: st['gm'] = (g, now0()); st['gmn'] = 0
                                elif now0() - st['gm'][1] >= 0.15:
                                    # 4.6.2 nav1: a dropped / partial move used to leave the list (colour block) on another item for good: re-check and retry up to 4x
                                    xbmc.executebuiltin('Control.Move(60,%d)' % (j - p)); st['gmn'] = st.get('gmn', 0) + 1
                                    st['gm'] = (g, now0() + 0.25 if st['gmn'] < 4 else 1e18)
                    elif xbmc.getCondVisibility('Control.HasFocus(60)') and st.get('gfoc') is not None:
                        # 3.5.7: focus back on the list: one move to the grid item (the list scrolls with its own smooth scrolltime);
                        # st['j'] is set to that grid item first, so the joined scroll does not pull the grid back to the old row
                        g = st['gfoc']; st['gfoc'] = None; st['g'] = None
                        g1 = cur(6600)   # BETA 1.2: the grid's real item (a quick last grid move before Left may not have been polled yet)
                        if g1 >= 0: g = g1
                        k = key(6600, g); j = st['m60'].get(k)
                        p = st['m60'].get(xbmc.getInfoLabel('Container(60).ListItem.DBID') or xbmc.getInfoLabel('Container(60).ListItem.Label'))
                        st['j'] = st['map'].get(k, g)
                        if j is not None and p is not None and j != p: xbmc.executebuiltin('Control.Move(60,%d)' % (j - p))
                        if mon.waitForAbort(0.25): break
                        home.clearProperty('bz_gtitle')
                    elif xbmc.getCondVisibility('Control.HasFocus(60)'):
                        st['g'] = None
                        # 4.3 item 7: the grid shrinks / sways only after the list has rested 2 s on one item
                        k0 = xbmc.getInfoLabel('Container(60).CurrentItem')
                        if k0 != st.get('rk'): st['rk'] = k0; st['rt'] = time.time()
                        # beta1 item 1: no grid sway work unless a grid is visible and its style is not None
                        gsec = 'music' if xbmc.getCondVisibility('Window.IsActive(music)') else 'video'
                        gsw = False   # BETA 1.1: grid styles removed, static grid only (no grid sway / poster work)
                        if not gsw:
                            if home.getProperty('bz_grest'): home.clearProperty('bz_grest')
                        elif time.time() - st.get('rt', 0) >= 2.0 and home.getProperty('bz_grest') != '1': home.setProperty('bz_grest', '1')
                        k = xbmc.getInfoLabel('Container(60).ListItem.DBID') or xbmc.getInfoLabel('Container(60).ListItem.Label')
                        j = st['map'].get(k)
                        if j != st['j']:
                            st['j'] = j
                            if j is None: lit(None, n, V)
                            else: place(j, n, V)
                        home.setProperty('bz_grid_target', '' if j is None else str(j))
                    if st.get('gs') and time.time() - st['gs'] > 0.3: st['gs'] = None; home.clearProperty('bz_gscroll')
                    if mon.waitForAbort(0.02): break
                else:
                    if st['sig'] is not None: home.clearProperty('bz_gslot')
                    if home.getProperty('bz_gpend') and not xbmc.getCondVisibility('Container(60).IsUpdating'): home.clearProperty('bz_gpend')   # 4.6.2 nav3: no grid -> nothing to wait for
                    st['sig'] = None
                    if mon.waitForAbort(0.3): break
            except Exception as e:
                xbmc.log('bz_flip grid_sync: %s' % e, xbmc.LOGWARNING)
                if mon.waitForAbort(0.5): break
    def _drsnap(face):
        for n, o in (('m', -1), ('0', 0), ('p', 1)):
            for f, a in (('s', 'Season'), ('e', 'Episode'), ('t', 'Title')):
                home.setProperty('bz_dr%s_%s%s' % (face, n, f), xbmc.getInfoLabel('Container(60).ListItem(%d).%s' % (o, a)))
        # t4137: freeze art per face too, so a face never repaints in place before the slide (all tiles move as one)
        for n, o in (('mm', -2), ('m', -1), ('0', 0), ('p', 1), ('pp', 2)):
            ok = n in ('m', '0', 'p') or (xbmc.getInfoLabel('Container(60).ListItem(%d).Label' % o) and not xbmc.getCondVisibility('Container(60).ListItem(%d).IsParentFolder' % o))
            home.setProperty('bz_dr%s_%sa' % (face, n), xbmc.getInfoLabel('Container(60).ListItem(%d).Art(thumb)' % o) if ok else '')
    def drum_dir():
        # BETA 2 item 16: replaces strip_sync (no Control.Move any more). Only reports the direction of a list-60 move to the episode drum.
        last = None
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            try:
                if xbmc.getCondVisibility('Control.IsVisible(6706) + !Container(60).IsUpdating'):
                    try: cur = int(xbmc.getInfoLabel('Container(60).CurrentItem'))
                    except Exception: cur = None
                    if cur is not None and last is not None and cur != last:
                        nf = 'b' if home.getProperty('bz_drumk') == 'a' else 'a'
                        _drsnap(nf)   # 4.7.6: freeze this face's titles so the outgoing face keeps its own labels while it slides
                        home.setProperty('bz_drumdir', 'down' if cur > last else 'up')
                        home.setProperty('bz_drumk', nf)
                    elif cur is not None and last is None:
                        _drsnap('a'); _drsnap('b')
                    elif cur is not None and cur == last:
                        f0 = home.getProperty('bz_drumk')
                        if f0 in ('a', 'b') and home.getProperty('bz_dr%s_0t' % f0) != xbmc.getInfoLabel('Container(60).ListItem(0).Title'): _drsnap(f0)
                    last = cur
                    if mon.waitForAbort(0.05): break
                else:
                    last = None
                    if mon.waitForAbort(0.3): break
            except Exception as e:
                xbmc.log('bz_flip drum_dir: %s' % e, xbmc.LOGWARNING)
                if mon.waitForAbort(0.5): break
    _bzstart(drum_dir)
    _bzstart(grid_sync)
    _bzstart(nav_menu)
    _bzstart(sway_clock)
    _bzstart(album_id)
    # 4.0.1 O34 (Rob): TV Continue watching = in-progress episodes + next-up (the next unwatched episode of each show already
    # started). Kodi smart playlists cannot express next-up, so this writes a filename-matched xsp to addon_data on start and
    # after every video stop (plus every 10 min); the nav list (6913) reads it via bz_cwfile (two files alternate so the list reloads).
    def cw_clock():
        import xbmcvfs, time as _tm
        from xml.sax.saxutils import escape
        base = xbmcvfs.translatePath('special://profile/addon_data/skin.bezel2/'); flip = [0]
        def build():
            eps = []
            ip = rpc('VideoLibrary.GetEpisodes', {'filter': {'field': 'inprogress', 'operator': 'true', 'value': ''},
                     'properties': ['file', 'lastplayed', 'tvshowid'], 'sort': {'method': 'lastplayed', 'order': 'descending'}, 'limits': {'end': 20}}) or {}
            seen = set()
            for e in ip.get('episodes', []): eps.append(e['file']); seen.add(e.get('tvshowid'))
            sh = rpc('VideoLibrary.GetTVShows', {'filter': {'field': 'inprogress', 'operator': 'true', 'value': ''},
                     'properties': ['lastplayed'], 'sort': {'method': 'lastplayed', 'order': 'descending'}, 'limits': {'end': 20}}) or {}
            for t in sh.get('tvshows', []):
                if t['tvshowid'] in seen: continue
                n = rpc('VideoLibrary.GetEpisodes', {'tvshowid': t['tvshowid'], 'filter': {'field': 'playcount', 'operator': 'is', 'value': '0'},
                        'properties': ['file', 'season'], 'sort': {'method': 'episode'}, 'limits': {'end': 50}}) or {}
                l = [e for e in n.get('episodes', []) if e.get('season', 0) > 0] or n.get('episodes', [])
                l.sort(key=lambda e: (e.get('season', 0), e.get('episodeid', 0)))
                if l: eps.append(l[0]['file'])
            rules = ''.join('<rule field="path" operator="is"><value>%s</value></rule><rule field="filename" operator="is"><value>%s</value></rule>' % (escape(f.rsplit('/', 1)[0] + '/'), escape(f.rsplit('/', 1)[-1])) for f in eps[:20])
            if not eps: rules = '<rule field="inprogress" operator="true" />'
            # path AND filename per episode cannot be grouped in one xsp, so match on filename (rules are OR'ed); path rules dropped
            rules = ''.join('<rule field="filename" operator="is"><value>%s</value></rule>' % escape(f.rsplit('/', 1)[-1]) for f in eps[:20]) or rules
            xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<smartplaylist type="episodes"><name>BEZEL Continue watching</name>'
                   '<match>any</match>%s<limit>20</limit><order direction="descending">lastplayed</order></smartplaylist>' % rules)
            try:
                os.makedirs(base, exist_ok=True); flip[0] ^= 1; fn = 'bezel_cw_%s.xsp' % 'ab'[flip[0]]   # alternate files = list reload
                with open(os.path.join(base, fn), 'w', encoding='utf-8') as f: f.write(xml)
                home.setProperty('bz_cwfile', fn)
            except Exception as ex: xbmc.log('BEZEL cw: %s' % ex, xbmc.LOGWARNING)
        last = 0; had = False
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            v = xbmc.getCondVisibility('Player.HasVideo')
            if (had and not v) or now0() - last > 600:
                if had and not v: mon.waitForAbort(2)
                build(); last = now0()
            had = v
            if mon.waitForAbort(1): break
    _bzstart(cw_clock)
    # 5.33.148 WARM 2.0 MM-only A/B preload (Rob voice). Generic hold-until-ready lane, modelled on the bz_cov_a/b flip:
    # target settles SETTLE s -> staged into the hidden side (bz_<p>_a|b) -> LOAD_WAIT s -> bz_<p>_side flips -> XML
    # Visible/Hidden fades crossfade. bz_<p>_on = lane has art (MM A/B twins take over from the live twin).
    # Gate: only while bz_nav == 'true' (MM open). MM close: pending stage dropped, last shown art kept.
    # LOAD_WAIT is a fixed wait, NOT a texture-ready signal (Kodi exposes none to Python).
    class _ABLane(object):
        def __init__(self, p, settle=0.25, load_wait=0.5, empty_flag=False):
            self.p = p; self.settle = settle; self.load_wait = load_wait; self.empty_flag = empty_flag
            self.seen = None; self.seen_t = 0.0; self.shown = None; self.stage = None; self.stage_t = 0.0
        def seed(self, target, now):   # 5.33.207 mirror-enter: while MM is closed, keep the front side = art on screen now, so MM opens on it (no black)
            p = self.p; side = home.getProperty('bz_%s_side' % p) or 'a'
            if target:
                if home.getProperty('bz_%s_%s' % (p, side)) != target: home.setProperty('bz_%s_%s' % (p, side), target)
                if not home.getProperty('bz_%s_on' % p): home.setProperty('bz_%s_on' % p, 'true')
                if self.empty_flag and home.getProperty('bz_%s_empty' % p): home.clearProperty('bz_%s_empty' % p)
            elif self.empty_flag and not home.getProperty('bz_%s_empty' % p): home.setProperty('bz_%s_empty' % p, '1')
            self.shown = target; self.seen = target; self.seen_t = now; self.stage = None
        def stop(self):   # MM closed: drop pending, keep last shown
            if self.stage is not None:
                o = 'b' if (home.getProperty('bz_%s_side' % self.p) or 'a') == 'a' else 'a'
                home.setProperty('bz_%s_%s' % (self.p, o), self.shown or '')
            self.stage = None; self.seen = None
        def tick(self, target, now):
            p = self.p
            if target != self.seen: self.seen = target; self.seen_t = now
            if self.stage is not None:
                if now - self.stage_t >= self.load_wait:
                    side = home.getProperty('bz_%s_side' % p) or 'a'
                    home.setProperty('bz_%s_side' % p, 'b' if side == 'a' else 'a')
                    self.shown = self.stage; self.stage = None
                return
            if now - self.seen_t < self.settle or target == self.shown: return
            if not target:
                if self.empty_flag: home.setProperty('bz_%s_empty' % p, '1'); self.shown = ''
                return
            if self.empty_flag: home.clearProperty('bz_%s_empty' % p)
            side = home.getProperty('bz_%s_side' % p) or 'a'
            if not home.getProperty('bz_%s_on' % p) or not self.shown:   # first art: straight onto the front side
                home.setProperty('bz_%s_side' % p, side); home.setProperty('bz_%s_%s' % (p, side), target)
                home.setProperty('bz_%s_on' % p, 'true'); self.shown = target; return
            home.setProperty('bz_%s_%s' % (p, 'b' if side == 'a' else 'a'), target)
            self.stage = target; self.stage_t = now
    def _il(*labels):
        for l in labels:
            v = xbmc.getInfoLabel(l)
            if v: return v
        return ''
    def _ab_fanart():   # mirrors BezelFanart (MM/browse branches only)
        v = _il(*((() if xbmc.getCondVisibility('Skin.HasSetting(bezel_norotate)') else ('Control.GetLabel(9880)',)) + (
            'Container(60).ListItem.Art(fanart)', 'Container(60).ListItem.Art(artist.fanart)', 'Container(60).ListItem.Art(albumartist.fanart)',
            'Container(60).ListItem.Art(tvshow.fanart)', 'Window(Home).Property(script.grab.fanart.Global.FanArt)')))
        # 5.33.189: movies-only fanart bridge (same idea as bz_movposter_hold) — unused on TV/Music
        if not v and xbmc.getCondVisibility('Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets) | String.StartsWith(Container.FolderPath,videodb://movies/)]'):
            v = home.getProperty('bz_movfanart_hold')
        return v
    def _ab_poster():   # BUG-010: poster A/B lane is Videos-only — never Music thumb/Icon into bz_pos
        c = xbmc.getCondVisibility
        if c('Window.IsActive(music)') or not c('Window.IsActive(videos)'):
            return ''
        if c('Container(60).ListItem.IsParentFolder'):
            v = _il('Container(60).ListItemNoWrap(1).Art(poster)', 'Container(60).ListItemNoWrap(1).Art(tvshow.poster)')
            if v: return v
        v = xbmc.getInfoLabel('Container(60).ListItem.Art(poster)')
        # 5.33.189: use retained movies hold whenever under movies path/content (incl. empty frames after TV) — not on TV
        if not v and c('Container.Content(movies) | Container.Content(sets) | String.StartsWith(Container.FolderPath,videodb://movies/)'):
            v = home.getProperty('bz_movposter_hold')
        if not v: v = xbmc.getInfoLabel('Container(60).ListItem.Art(tvshow.poster)')
        if not v and home.getProperty('bz_arthold'): v = home.getProperty('bz_hold_poster')
        if v and os.path.basename(v.rstrip('/')).startswith('Default'): v = ''
        return v
    def _ab_mart():   # 5.33.216 Music A/B art lane: artist/album thumbs, Music window only (BUG-010: never feeds bz_pos)
        c = xbmc.getCondVisibility
        if not c('Window.IsActive(music)'):
            return ''
        if c('Container(60).ListItem.IsParentFolder'):
            v = _il('Container(60).ListItemNoWrap(1).Art(thumb)', 'Container(60).ListItemNoWrap(1).Icon')
        else:
            v = _il('Container(60).ListItem.Art(thumb)', 'Container(60).ListItem.Icon')
        if v and os.path.basename(v.rstrip('/')).startswith('Default'): v = ''
        return v
    def _ab_clear():   # TV clearlogo/clearart — same settle/load as fan/pos so strip logo crossfades with them
        c = xbmc.getCondVisibility
        if not c('Window.IsActive(videos)'):
            return ''
        if c('Skin.HasSetting(bz_tvclear_off)'):
            return ''
        if not c('Container.Content(tvshows) | Container.Content(seasons) | Container.Content(episodes)'):
            return ''
        if c('Container(60).ListItem.IsParentFolder'):
            return ''
        return _il('Container(60).ListItem.Art(clearlogo)', 'Container(60).ListItem.Art(tvshow.clearlogo)',
                   'Container(60).ListItem.Art(clearart)', 'Container(60).ListItem.Art(tvshow.clearart)')
    _WHWIN = ('Window.IsActive(favouritesbrowser) | Window.IsActive(pictures) | Window.IsActive(addonbrowser) | '
              'Window.IsActive(settings) | Window.IsActive(1107) | Window.IsActive(1117)')
    def _whold():   # 5.33.211 WARM HOLD kill switch (Tuner WARM 2.0 > Hold last art): Off = pre-.211 behaviour
        return xbmc.getInfoLabel('Skin.String(bz_at_warmhold)') != 'Off'
    def ab_clock():
        lanes = ((_ABLane('fan', 0.25, 0.5), _ab_fanart), (_ABLane('pos', 0.25, 0.5, True), _ab_poster),
                 (_ABLane('clr', 0.25, 0.5, True), _ab_clear),
                 (_ABLane('mart', 0.25, 0.5, True), _ab_mart))   # 5.33.216 Music A/B
        armed = False; open_t = 0.0
        home.clearProperty('bz_ab_live')
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            if home.getProperty('bz_nav') == 'true':
                if not armed: armed = True; open_t = time.time()
                elif not home.getProperty('bz_ab_live') and time.time() - open_t >= 0.3: home.setProperty('bz_ab_live', '1')   # 5.33.207: side-flip fades armed only after MM is up (open = full opacity, same frame)
                if _whold() and xbmc.getCondVisibility(_WHWIN):
                    pass   # 5.33.211 WARM HOLD: MM open over a non-M/M/TV section -> lanes keep the last WARM art (no re-target to that window's art)
                elif not xbmc.getCondVisibility('Container.IsUpdating | System.HasModalDialog'):
                    now = time.time()
                    for ln, rf in lanes: ln.tick(rf(), now)
            else:
                if armed:
                    armed = False; home.clearProperty('bz_ab_live')
                    for ln, rf in lanes: ln.stop()
                elif not xbmc.getCondVisibility('Container.IsUpdating | System.HasModalDialog') and xbmc.getCondVisibility('Window.IsActive(music) | Window.IsActive(videos)'):
                    now = time.time()   # 5.33.207 mirror-enter seed: lane front side tracks the section art while MM is closed
                    for ln, rf in lanes: ln.seed(rf(), now)
                elif not _whold() and not xbmc.getCondVisibility('Container.IsUpdating') and xbmc.getCondVisibility('Window.IsActive(1107) | Window.IsActive(1117)'):   # 5.33.211: WARM HOLD on -> no 1107/1117 seed (keeps last WARM); Off -> old .207 seed
                    # 5.33.207 mirror-enter ALL sections: Search (1107) / Media Sources (1117) draw BezelFanartLayer too —
                    # seed the fan lane with that on-screen fanart so MM opens on it (no 3000 ms unfed fade from black). Poster/clear N/A there.
                    lanes[0][0].seed(xbmc.getInfoLabel('$VAR[BezelFanart]'), time.time())
            if mon.waitForAbort(0.05): break
    _bzstart(ab_clock)
    def mm_idle():   # 5.33.216 MM idle fade: 30 s no input -> strip fades to 0 (veil/Warm stay), focus parked on 6897; any key wakes + SetFocus(6996)
        IDLE = 30
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            hid = home.getProperty('bz_mmidle')
            if hid == '1':
                if home.getProperty('bz_nav') != 'true':
                    home.clearProperty('bz_mmidle')
                elif xbmc.getGlobalIdleTime() < 1:
                    home.clearProperty('bz_mmidle')   # touch / mouse / key not routed to 6897
            elif (home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmidle_set')
                  and xbmc.getCondVisibility('Control.HasFocus(6897) + !System.HasModalDialog')):
                home.setProperty('bz_mmidle', '1'); home.setProperty('bz_mmidle_set', '1')   # 5.33.387: focus already parked (late SetFocus landed) -> finish the hide instead of stranding focus
            elif hid == 'w':   # woken by 6897 (ClearProperty) -> restore strip focus next frame
                pass
            elif home.getProperty('bz_mmidle_set'):
                home.clearProperty('bz_mmidle_set')
                # 5.33.380 WAKEGRACE (Rob t2694 #3): the wake key is eaten by 6897, but a fast 2nd press (Back/Select/L/R) used to land on the
                # freshly re-focused strip -> Back closed MM / Select opened a section. Park 0.5 s on the no-op 6897 (strip fades in), THEN hand to 6996.
                if mon.waitForAbort(0.5): break
                if home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmidle') and xbmc.getCondVisibility('Control.HasFocus(6897)'):
                    _bzstrip(home)
            elif (home.getProperty('bz_nav') == 'true' and xbmc.getInfoLabel('Skin.String(bz_at_mmidle)') != 'Off'
                  and not home.getProperty('bz_navtune') and not home.getProperty('bz_navbez')
                  and xbmc.getGlobalIdleTime() >= IDLE and xbmc.getCondVisibility('Control.HasFocus(6996) + !System.HasModalDialog')):
                xbmc.executebuiltin('SetFocus(6897)')
                # 5.33.380: only hide once the park really holds focus (hiding 6894 while 6996 focused let Kodi fall back to list 60)
                # 5.33.387 IDLEPARK (Rob t2714): 50 ms was too short on Shield -> focus sat on the invisible park with no bz_mmidle
                # (strip unfocused + never hid, and no retry since 6996 no longer focused). Poll up to 1 s; if the park never holds, give 6996 back.
                held = False
                for _ in range(20):
                    if mon.waitForAbort(0.05): break
                    if xbmc.getCondVisibility('Control.HasFocus(6897)'): held = True; break
                if mon.abortRequested(): break
                if held and home.getProperty('bz_nav') == 'true':
                    home.clearProperty('bz_mmtap')
                    home.setProperty('bz_mmidle', '1'); home.setProperty('bz_mmidle_set', '1')
                elif home.getProperty('bz_nav') == 'true' and not xbmc.getCondVisibility('Control.HasFocus(6996) | System.HasModalDialog'):
                    _bzstrip(home)
            if mon.waitForAbort(0.1): break
    _bzstart(mm_idle)
    def mm_tap():   # 5.33.386 MMTAP (Rob t2705): strip-wide quick-tap ignore. 6996 Select/Back/Left/Right set bz_mmtap as their last
        # action; every 6996 action is gated on !bz_mmtap, so a 2nd press inside 400 ms is swallowed. Clear 400 ms after first seen.
        LATCH = 0.4; t0 = 0
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            if home.getProperty('bz_mmtap'):
                if not t0: t0 = time.time()
                elif time.time() - t0 >= LATCH: home.clearProperty('bz_mmtap'); t0 = 0
            else: t0 = 0
            if mon.waitForAbort(0.05): break
        home.clearProperty('bz_mmtap')
    _bzstart(mm_tap)

    def idle_hinge():   # 5.33.231 HINGEFLIP (Rob pt1824u): idle big album AWAY centre-hinge flip. No audio, Music list 60 focused.
        # Artist row: cycles that artist's album covers (by year, wraps). Album row: album <-> artist face. 10 s hold; playback / focus change resets.
        HOLD = 10.0; K = ('bz_hf_a', 'bz_hf_b', 'bz_hf_ph')
        def clr():
            for k in K: home.clearProperty(k)
        def mmw():   # 5.33.279 MMLEAF (Rob pt2150u): Music warm under MM (strip 6996 or MM-idle park 6897), not mid-swap / submenu
            return (home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmwarm') and not home.getProperty('bz_navtune') and not home.getProperty('bz_navbez')
                    and xbmc.getCondVisibility('!Player.HasAudio + Window.IsActive(music) + [Control.HasFocus(6996) | Control.HasFocus(6897)] + !System.HasModalDialog'))
        def ok():
            if home.getProperty('bz_randpend'): return False
            if mmw(): return True
            return xbmc.getCondVisibility('!Player.HasAudio + Window.IsActive(music) + Control.HasFocus(60)') and not home.getProperty('bz_nav')
        def dim():   # 5.33.375 LEAFWAKE (Rob pt2688u): mirror XML bz_lfdim (MM open & not auto-hide, or gdim 1-6 MM closed) -> leaf groups hidden, so never step phases (was glare/shadow-only ghost flip)
            if home.getProperty('bz_nav') == 'true': return not home.getProperty('bz_mmidle')
            return xbmc.getInfoLabel('Skin.String(bz_at_gdim)') in ('1', '2', '3', '4', '5', '6')
        def keynow(): return xbmc.getInfoLabel('Container(60).ListItem.DBType') + ':' + xbmc.getInfoLabel('Container(60).ListItem.DBID')
        def covers():
            t = xbmc.getInfoLabel('Container(60).ListItem.DBType'); i = xbmc.getInfoLabel('Container(60).ListItem.DBID')
            cur = xbmc.getInfoLabel('Container(60).ListItem.Art(thumb)') or xbmc.getInfoLabel('Container(60).ListItem.Icon')
            out = [cur] if cur else []
            if t == 'artist' and i.isdigit():
                al = (rpc('AudioLibrary.GetAlbums', {'filter': {'artistid': int(i)}, 'properties': ['thumbnail', 'year'], 'sort': {'method': 'year'}}) or {}).get('albums') or []
                for x in al:
                    th = x.get('thumbnail') or ''
                    if th and th not in out: out.append(th)
            elif t == 'album':
                af = xbmc.getInfoLabel('Container(60).ListItem.Art(artist.thumb)')
                if af and af not in out: out.append(af)
            return [c for c in out if c and not os.path.basename(c.rstrip('/')).startswith('Default')]
        key = None; cv = []; idx = 0; t0 = 0.0; kt = 0.0
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            if mon.waitForAbort(0.1): break
            if not ok():
                if key is not None or home.getProperty('bz_hf_a'): clr(); key = None
                continue
            k = keynow()
            if not k.split(':')[-1]:   # 5.33.355 COLDLEAF (Rob pt2531u): list 60 not populated yet on cold start -> don't lock a key
                if key is not None or home.getProperty('bz_hf_a'): clr(); key = None
                continue
            if k != key:   # focus change resets
                clr(); key = k; cv = covers(); idx = 0; t0 = time.time(); kt = t0; continue
            if idx == 0 and not home.getProperty('bz_hf_ph') and time.time() - kt < 6.0 and int((time.time() - kt) * 10) % 10 == 0:
                c2 = covers()   # 5.33.355 COLDLEAF: on cold start / first MM open the item art + album RPC arrive late -> re-read covers for 6 s
                if c2 != cv and c2 and (not cv or c2[0] == cv[0] or not home.getProperty('bz_hf_a') or not cv[0]):
                    cv = c2; clr(); t0 = time.time()
            if len(cv) < 2: continue
            nxt = (idx + 1) % len(cv)
            if home.getProperty('bz_hf_b') != cv[nxt]:   # 5.33.245 PRELOAD: next cover set at hold start, drawn under A all hold -> loaded before fold
                home.setProperty('bz_hf_a', cv[idx]); home.setProperty('bz_hf_b', cv[nxt])
            if dim():   # 5.33.375 LEAFWAKE: hold paused while dimmed; A stays the shown cover; restart hold on undim (fresh flip with current art)
                t0 = time.time(); continue
            if time.time() - t0 < (5.0 if mmw() else HOLD): continue   # 5.33.279: MM warm 5 s, idle list 10 s
            aborted = False
            for ph in ('1', '2'):
                if not ok() or keynow() != key or dim(): aborted = True; break   # 5.33.375: dim mid-fold aborts + re-arms (no phase desync)
                home.setProperty('bz_hf_ph', ph)
                if mon.waitForAbort(1.4): return   # 5.33.254 Rob pt1922u: 1400 ms per phase (matches XML)
            if aborted: clr(); key = None; continue
            home.setProperty('bz_hf_a', cv[nxt]); home.clearProperty('bz_hf_ph'); idx = nxt; t0 = time.time()   # seamless: A := B (same pixels)
    _bzstart(idle_hinge)
    def akey():
        alb = xbmc.getInfoLabel('MusicPlayer.Album')
        if alb: return alb + '|' + xbmc.getInfoLabel('MusicPlayer.Property(Album_Artist)') + '|' + xbmc.getInfoLabel('MusicPlayer.AlbumArtist')
        return xbmc.getInfoLabel('Player.Filenameandpath') + '|' + xbmc.getInfoLabel('Player.Art(thumb)')
    try:
        gone = 0.0
        shown = ''; shown_art = ['']; aud_t = [0.0]; had = False
        while not mon.abortRequested() and not home.getProperty('bz_quit'):   # BEZEL 3.0 exit fix
            # v0.1.22: audio latch for Home: true while music plays, cleared only after audio has been gone for 1.5 s,
            # so a track change (HasAudio briefly false) never closes / re-opens the Now Playing row
            if xbmc.getCondVisibility('Player.HasAudio + !Player.HasVideo'):
                if not had: aud_t[0] = time.time(); had = True
                gone = 0.0
                if home.getProperty('bz_audio_latch') != 'true':
                    home.setProperty('bz_audio_latch', 'true'); sway['t0'] = time.time()   # sway (keyed on the latch) starts from flat
            elif home.getProperty('bz_audio_latch') == 'true':
                gone += 0.15   # t3378 minipop: no 0.45 s fast-drop on !HasMedia (track gap = player briefly empty -> mini player hid)
                if gone >= 2.5 or xbmc.getCondVisibility('Player.HasVideo'): home.clearProperty('bz_audio_latch'); gone = 0.0; sway['t0'] = None; had = False
            if xbmc.getCondVisibility('Player.HasAudio + !Player.HasVideo'):
                # 3.5.1: flips only when the album changes (akey); see playback start below. v0.1.24 note kept for history: full flip on EVERY song change (keyed on the file, so same-album tracks, skip/prev,
                # party mode and playback start all flip). The new cover only goes on the hidden layer; the
                # front layer rotates to 90 deg, then the hidden one rotates in from -90, so the swap happens edge-on.
                art = xbmc.getInfoLabel('Player.Art(thumb)')
                key = akey()   # 2.0a3.5: keyed on the album, so a new track from the same album leaves the art in place
                # 3.5.7: no false flips. MusicPlayer.Album reads empty for a moment at playback start / track changes, which gave a
                # filename key and then an album key (= a flip). Ignore album-less keys for ~1 s after audio starts (or while the album
                # label blinks), and treat a key change with the same cover art as no change (just adopt the key).
                if not xbmc.getInfoLabel('MusicPlayer.Album') and (time.time() - aud_t[0] < 1.2 or not art or (shown and art == shown_art[0])):
                    if mon.waitForAbort(0.15): break
                    continue
                if key and shown and key != shown and art and art == shown_art[0]:
                    shown = key
                if key and not shown:
                    # 3.5.1: playback start never flips: the front layer simply takes the playing cover (the big art scales down,
                    # holds 2 s, then sways). Only an album change, the tap flip and the music -> video transition turn the art.
                    side = home.getProperty('bz_cov_side') or 'a'
                    home.setProperty('bz_cov_' + side, art); shown = key; shown_art[0] = art
                elif key and key != shown:
                    # 5.33.301 ALBUM SWAY NEXT SONG FADE (Rob t2276u): album change while playing = in-place crossfade INSIDE the sway tree (stays tipped).
                    # No bz_cov_side flip, no sway hold, no flat wait. Old full-spin body parked in bak_5.33.300_tipfade.
                    home.setProperty('bz_cov_next', art); home.setProperty('bz_cov_x', art)   # preload (2 px + overlay texture)
                    if mon.waitForAbort(LOAD_WAIT): break
                    cur = akey()
                    if cur != key and xbmc.getCondVisibility('Player.HasAudio'):
                        art = xbmc.getInfoLabel('Player.Art(thumb)'); key = cur; home.setProperty('bz_cov_x', art)
                    home.setProperty('bz_cov_xf', 'true')                       # overlay fades in 900 ms over the front face
                    if mon.waitForAbort(1.0): break
                    side = home.getProperty('bz_cov_side') or 'a'
                    home.setProperty('bz_cov_' + side, art)                     # front face adopts the new cover under the overlay
                    shown = key; shown_art[0] = art
                    if mon.waitForAbort(0.4): break
                    home.clearProperty('bz_cov_xf'); home.clearProperty('bz_cov_next')   # overlay drops (instant; same art below)
                    continue
            elif home.getProperty('bz_audio_latch') != 'true' and not xbmc.getCondVisibility('Player.HasMedia'):  # v0.1.24: only after the latch drops, never in a track gap
                if shown_art[0]: home.setProperty('bz_cov_last', shown_art[0])   # 5.33.320 Rob t2402/t2403: keep last playing cover for the idle big album (1122) after stop
                for k in ('bz_cov_a', 'bz_cov_b', 'bz_cov_next', 'bz_cov_x', 'bz_cov_xf'): home.clearProperty(k)
                home.setProperty('bz_cov_side', 'a'); shown = ''
            if mon.waitForAbort(0.15): break
    finally:
      try:   # 5.33.194: left Bezel -> remove all BEZEL keymaps (safe if bz_dtap already did it)
        import sys as _s; _s.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_km
        if not bz_km.on_bezel(): bz_km.leave()
      except Exception: pass
      # BEZEL 3.0 exit fix: on Kodi exit, touch nothing (window properties need the GUI lock that Kodi holds while it waits for this script -> freeze)
      if not mon.abortRequested():
        home.clearProperty('bz_flip_running')   # every helper loop stops on this flag
        _dl = time.time() + 2.0
        for _t in _bzth: _t.join(max(0.0, _dl - time.time()))
        home.clearProperty('bz_audio_latch')
        home.clearProperty('bz_flipping')
        home.clearProperty('bz_sway_hold')
        home.clearProperty('bz_sway_pulse'); home.clearProperty('bz_sway_go'); home.clearProperty('bz_big_go'); home.clearProperty('bz_big_pulse')
        for k in ('bz_albumid', 'bz_art_t0', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL', 'bz_castR') + _ART_CLEAR: home.clearProperty(k)   # 5.33.390 ART_TREE
