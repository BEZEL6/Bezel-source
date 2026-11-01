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
                if not sway.get('busy') and sway['t0'] is not None and not home.getProperty('bz_backanim'):
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
    # v0.1.32: tap-to-flip back face (track list). The skin sets bz_back + bz_backanim on tap; this thread moves focus to
    # the list, closes it after 15 s (2.0a1) without input (System.IdleTime), plays a picked song, and clears bz_backanim 2.8 s
    # after the back has flipped away, so song-change flips (queued meanwhile) and glares wait for the whole turn.
    import json
    def rpc(method, params):
        try: return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}))).get('result')
        except Exception: return None
    def play_pick(sid):
        try: sid = int(sid)
        except Exception: return
        items = (rpc('Playlist.GetItems', {'playlistid': 0}) or {}).get('items') or []
        # BETA 1.1 item 8: after "Play next" the playlist can hold the same song twice; pick the copy at / after the
        # playing position (was: the first copy, which jumped back and played the wrong next songs)
        try: cur = int(xbmc.getInfoLabel('Playlist.Position')) - 1
        except Exception: cur = 0
        order = list(range(max(cur, 0), len(items))) + list(range(0, max(cur, 0)))
        for i in order:
            it = items[i]
            if it.get('id') == sid and it.get('type') == 'song':
                rpc('Player.Open', {'item': {'playlistid': 0, 'position': i}}); return
        aid = home.getProperty('bz_albumid')
        if not aid: rpc('Player.Open', {'item': {'songid': sid}}); return
        rpc('Playlist.Clear', {'playlistid': 0}); rpc('Playlist.Add', {'playlistid': 0, 'item': {'albumid': int(aid)}})
        items = (rpc('Playlist.GetItems', {'playlistid': 0}) or {}).get('items') or []
        pos = next((i for i, it in enumerate(items) if it.get('id') == sid), 0)
        rpc('Player.Open', {'item': {'playlistid': 0, 'position': pos}})
    def back_face():
        was = False; closed_at = None; aid_song = None; opened_m = 0
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
            on = bool(home.getProperty('bz_back'))
            if on and not was:
                xbmc.executebuiltin('SetFocus(6185)'); closed_at = None; home.clearProperty('bz_back_close'); opened_m = time.time()
            if on and time.time() - opened_m < 3.0 and not xbmc.getCondVisibility('Control.HasFocus(6185)'):
                xbmc.executebuiltin('SetFocus(6185)')
            pick = home.getProperty('bz_back_pick')
            if pick:
                home.clearProperty('bz_back_pick'); play_pick(pick)
            # 2.0a1: closes after 15 s without input (was 6), on Back (bz_back_close) or when the music stops;
            # it first fades the list to black (bz_back_fade, 0.5 s), then the black side turns away and the art turns in
            if on and not home.getProperty('bz_back_fade') and (home.getProperty('bz_back_close') or xbmc.getCondVisibility('System.IdleTime(15)') or not xbmc.getCondVisibility('Player.HasAudio')
                       and home.getProperty('bz_audio_latch') != 'true'):
                home.clearProperty('bz_back_close')
                ret = home.getProperty('bz_back_ret')
                if ret and xbmc.getCondVisibility('Control.HasFocus(6185)'): xbmc.executebuiltin('SetFocus(%s)' % ret)
                home.setProperty('bz_back_fade', 'true')
                if mon.waitForAbort(1.25): break   # 2.0a3: 1.2 s fade to black
                home.clearProperty('bz_back'); on = False
            if was and not on: closed_at = time.time()
            if not on and home.getProperty('bz_backanim'):
                if closed_at is None: closed_at = time.time()
                if time.time() - closed_at >= 2.8:
                    home.clearProperty('bz_backanim'); home.clearProperty('bz_back_fade'); closed_at = None
            elif not on and home.getProperty('bz_back_fade'): home.clearProperty('bz_back_fade')
            was = on
            if mon.waitForAbort(0.05 if (on or home.getProperty('bz_backanim')) else 0.15): break   # 2.0a3.3: slower when idle
    # 2.0a1: movies / TV poster (BEZEL list 60 in the video window). bz_psway is set after 5 s on one title (the poster eases
    # 0 -> 24 deg in 5 s), bz_ppulse 5 s later (the 20 s sway + glares, same as the album art). Both clear on a new title, so the
    # poster eases back to flat. The tap flip (bz_vback) shows the info back; it closes after 15 s without input (not while a
    # dialog is open), on Back (bz_vback_close), when the focused title changes or the list is focused again, fading to black first.
    def focus_back():   # 2.0a3: focus the first shown back button (SetFocus on the grouplist itself does not take)
        for c in ('6291', '6292', '6298', '6295', '6293'):
            if xbmc.getCondVisibility('Control.IsVisible(%s)' % c):
                xbmc.executebuiltin('SetFocus(%s)' % c); return
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
                            sw[0] = now_
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
    _bzstart(km_leave_watch)
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
        opened = None; last = 0.0
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            on = (home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmstart') and not home.getProperty('bz_mmwarm')
                  and not home.getProperty('bz_navtune') and not home.getProperty('bz_navset') and not home.getProperty('bz_navsub') and not home.getProperty('bz_kset')   # F10 batch2: pause while Tuner / settings card / submenu open
                  and not xbmc.getCondVisibility('Skin.HasSetting(bz_uadv_off)')
                  and xbmc.getCondVisibility('[Window.IsActive(videos) | Window.IsActive(music)] + Control.IsVisible(60) + !Container.IsUpdating + !System.HasModalDialog + !Window.IsVisible(1113) + !Window.IsVisible(1111) + !Window.IsVisible(1112) + !Player.HasVideo + Integer.IsGreater(Container(60).NumItems,1)'))
            if not on: opened = None
            else:
                now = time.time()
                try: hold = int(xbmc.getInfoLabel('Skin.String(bz_uadv_hold)') or 5); dly = int(xbmc.getInfoLabel('Skin.String(bz_uadv_delay)') or 8)
                except Exception: hold, dly = 5, 8
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
            if xbmc.getCondVisibility(_SECM[s2]) and not xbmc.getCondVisibility('Container.IsUpdating'):
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
        def _restore(s2, p2, spos):   # WARM 2.0 (1): after settle -> list row, then same-frame bounce back to strip 6996
            e = SS.get(s2) or {}; r = e.get('row')
            if r is None and not _pk() and xbmc.getInfoLabel('Container.FolderPath').rstrip('/') == p2.rstrip('/') and not xbmc.getCondVisibility('Container.IsUpdating'):
                r = _randrow()   # 5.33.204 RANDSTART: first visit (no session row) -> random list row, not top; seeded below
                if r is not None: e = SS.setdefault(s2, {}); e['row'] = r; e['path'] = p2; _dbgmm('warm2 randstart sec=%s row=%d' % (s2, r))
            if not r or _pk() or (e.get('path') or '').rstrip('/') != p2.rstrip('/'): return
            if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') != p2.rstrip('/') or xbmc.getCondVisibility('Container.IsUpdating'): return
            xbmc.executebuiltin('SetFocus(60,%d,absolute)' % r); _bzstrip(home, home.getProperty('bz_mmlive') or spos)
            _dbgmm('warm2 restore sec=%s row=%d' % (s2, r))
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
        big_t = [0]; fw_t = [0]; sj = [None, 0]; rp = [None, 0, None]; pl = [None, 0]; nav_was = [False, 0]; auto_spin = [time.time() + 30, 0]; biglogo_spin = [time.time() + 30, 0]; casc = [None, None]; casc_t = [0]; casc_pend = [None, 0, None]; dview = [None, 0]; fguard = [0]; autonp = [False]; autonp_t = [0]; autonp_np = [False]; autoinfo = [None]
        navlk = [0.0]; navgr = [0.0]; navop = [0.0, 0]; mmst = [0]; fs_was = [False, 0]; gfirst = ['', 0]
        setret = [False, 0.0]   # F8 batch2 (t3930): Settings family was active -> Back reopens MM on SETTINGS (not TV)
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            now = time.time()
            _sw = xbmc.getCondVisibility('Window.IsActive(settings) | Window.IsActive(systemsettings) | Window.IsActive(interfacesettings) | Window.IsActive(mediasettings) | Window.IsActive(playersettings) | Window.IsActive(servicesettings) | Window.IsActive(pvrsettings) | Window.IsActive(gamesettings) | Window.IsActive(skinsettings) | Window.IsActive(profiles) | Window.IsActive(systeminfo)')
            if setret[0] and not _sw: setret[1] = now   # F8: left Settings just now
            setret[0] = _sw
            # 3.2.1 item 14: leaving fullscreen music (Now Playing 1112, the in-place Now Playing, visualisation, controls 1115) -> focus the music list (60)
            fsm = home.getProperty('bz_np') == 'true' or xbmc.getCondVisibility('Window.IsActive(1112) | Window.IsActive(1115) | Window.IsActive(visualisation)')
            if fs_was[0] and not fsm: fs_was[1] = now + 1.2
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
                                        ('menu', bool(home.getProperty('bz_nav'))), ('flip back', bool(home.getProperty('bz_back') or home.getProperty('bz_backanim'))),
                                        ('dialog', xbmc.getCondVisibility('System.HasModalDialog | Window.IsActive(1111) | Window.IsActive(1112) | Window.IsActive(contextmenu) | Window.IsActive(musicinformation)'))) if bad]
                if not why and not _np_safe(): why = ['busy']   # 4.4.0 O86
                if not why:
                    autonp[0] = True
                    xbmc.log('BEZEL auto NP: open after %ss' % _ad, xbmc.LOGWARNING)
                    _np_open('auto')   # 4.6.0: guarded (cooldown + busy check right before the launch)
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
    _bzstart(back_face)
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
    def ab_clock():
        lanes = ((_ABLane('fan', 0.25, 0.5), _ab_fanart), (_ABLane('pos', 0.25, 0.5, True), _ab_poster),
                 (_ABLane('clr', 0.25, 0.5, True), _ab_clear))
        armed = False; open_t = 0.0
        home.clearProperty('bz_ab_live')
        while not mon.abortRequested() and home.getProperty('bz_flip_running') == 'true':
            if home.getProperty('bz_nav') == 'true':
                if not armed: armed = True; open_t = time.time()
                elif not home.getProperty('bz_ab_live') and time.time() - open_t >= 0.3: home.setProperty('bz_ab_live', '1')   # 5.33.207: side-flip fades armed only after MM is up (open = full opacity, same frame)
                if not xbmc.getCondVisibility('Container.IsUpdating | System.HasModalDialog'):
                    now = time.time()
                    for ln, rf in lanes: ln.tick(rf(), now)
            else:
                if armed:
                    armed = False; home.clearProperty('bz_ab_live')
                    for ln, rf in lanes: ln.stop()
                elif not xbmc.getCondVisibility('Container.IsUpdating | System.HasModalDialog') and xbmc.getCondVisibility('Window.IsActive(music) | Window.IsActive(videos)'):
                    now = time.time()   # 5.33.207 mirror-enter seed: lane front side tracks the section art while MM is closed
                    for ln, rf in lanes: ln.seed(rf(), now)
            if mon.waitForAbort(0.05): break
    _bzstart(ab_clock)
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
                if key and key != shown and home.getProperty('bz_backanim'):
                    pass   # v0.1.32: track list (back face) up or turning: the song-change flip is queued until it has flipped back
                elif key and not shown:
                    # 3.5.1: playback start never flips: the front layer simply takes the playing cover (the big art scales down,
                    # holds 2 s, then sways). Only an album change, the tap flip and the music -> video transition turn the art.
                    side = home.getProperty('bz_cov_side') or 'a'
                    home.setProperty('bz_cov_' + side, art); shown = key; shown_art[0] = art
                elif key and key != shown:
                    side = home.getProperty('bz_cov_side') or 'a'
                    other = 'b' if side == 'a' else 'a'
                    home.setProperty('bz_cov_next', art)       # hidden preload image
                    home.setProperty('bz_cov_' + other, art)   # hidden layer
                    if mon.waitForAbort(LOAD_WAIT): break
                    # v0.1.24: keep swaying until the art is next flat (either flat point), then hold the sway there
                    # (a newer track while waiting just retargets the hidden layer; it is first seen 1.3 s into the turn, time enough to load)
                    ab = False
                    while True:
                        flat = next_flat(time.time())   # v0.1.26: recomputed, the phase can be re-anchored by a window reload
                        cur = akey()
                        if cur != key and xbmc.getCondVisibility('Player.HasAudio'):
                            art = xbmc.getInfoLabel('Player.Art(thumb)'); key = cur
                            home.setProperty('bz_cov_next', art); home.setProperty('bz_cov_' + other, art)
                        if home.getProperty('bz_backanim'):   # v0.1.32: a tap flip started while waiting: queue behind it
                            if mon.waitForAbort(0.1): ab = True; break
                            continue
                        wait = flat - 0.2 - time.time()   # glares start fading 0.2 s early so the hold lands on flat
                        break   # BETA 2.2 item 2: no wait-for-flat swing (the bounce before the turn): the flip starts at once
                        if mon.waitForAbort(min(wait, 0.1)): ab = True; break
                    if ab: break
                    sway['busy'] = True
                    home.setProperty('bz_flipping', 'true')    # v0.1.23: glares fade out (150 ms) before the sway is held
                    if mon.waitForAbort(0.2): break
                    home.setProperty('bz_cov_side', other)     # -> flip (1.3 s + 1.3 s)
                    if mon.waitForAbort(_flip_s()): break            # BEZEL 3.0: flip time read live from the tuner (was patched); BETA 2.2 A: sway reset exactly edge-on (old face Hidden 1300 ms ends at 90 deg, new face starts at 1300 ms): no visible snap
                    home.setProperty('bz_sway_hold', 'true')
                    shown = key; shown_art[0] = art
                    # v0.1.24 flip lock: once started the full 2.6 s turn always completes (nothing touches the
                    # layers meanwhile). Newer track changes are queued: after the turn + a 0.3 s settle the loop
                    # flips straight to whatever is playing then (intermediate covers are skipped).
                    if mon.waitForAbort(_flip_s()): break            # BEZEL 3.0 live flip time; BETA 2.2 A: 0.2 + 1.3 + 1.3 = same 2.8 s lock
                    home.clearProperty('bz_cov_next')
                    home.clearProperty('bz_sway_hold')
                    # sway resumes from flat (1.2 s flat, then eases out); glare pulses restart at 0
                    sway['t0'] = time.time()
                    if mon.waitForAbort(0.3): break
                    home.clearProperty('bz_flipping')          # glares fade back in (400 ms), still locked to the sway
                    sway['busy'] = False
                    continue
            elif home.getProperty('bz_audio_latch') != 'true' and not xbmc.getCondVisibility('Player.HasMedia'):  # v0.1.24: only after the latch drops, never in a track gap
                for k in ('bz_cov_a', 'bz_cov_b', 'bz_cov_next'): home.clearProperty(k)
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
        for k in ('bz_back', 'bz_backanim', 'bz_back_pick', 'bz_albumid', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL', 'bz_castR'): home.clearProperty(k)
