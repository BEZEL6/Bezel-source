# BEZEL 2.0 alpha 1: actions for the movie / TV info back (tap flip).
# RunScript(special://skin/scripts/bz_cmd.py,<action>,<dbtype>,<dbid>[,<tvshowid>,<season>])
# actions: play, resume, refresh, art, watched
import sys, os, json, xbmc, xbmcgui
def rpc(method, params):
    try:
        r = json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params})))
        return r.get('result')
    except Exception:
        return None
args = (sys.argv[1:] + ['', '', '', '', ''])[:5]
action, dbtype, dbid, showid, season = args
try: dbid = int(dbid)
except Exception: dbid = 0
home = xbmcgui.Window(10000)
if action in ('quit', 'exit'):   # BEZEL 3.1 item 8: 'exit,<Powerdown|Reboot|Shutdown|...>' runs the same stop first
    # BEZEL 3.0 exit fix: Kodi froze on Exit because the skin's background scripts never got Kodi's abort signal and Kodi waited on them
    # forever. Stop them ourselves first (each loop watches these flags), close the dust dialog, then quit.
    import time
    home.setProperty('bz_quit', 'true')
    for k in ('bz_flip_running', 'bz_dtap_running', 'bz_precache_running'): home.clearProperty(k)
    xbmc.executebuiltin('Dialog.Close(1114,true)')
    t0 = time.time()
    while time.time() - t0 < 1.5 and not home.getProperty('bz_quit_dtap'): xbmc.sleep(50)
    xbmc.sleep(400)
    fin = (sys.argv[2] if len(sys.argv) > 2 else 'Quit') if action == 'exit' else 'Quit'
    xbmc.executebuiltin(fin + '()')
    sys.exit()
if action == 'uadv':   # UNDERADV (Rob t3741/t3910): Tuner LOOK steps for underlay auto-advance (delay / hold), uadv,<delay|hold>,<1|-1>
    S = {'delay': [4, 6, 8, 10, 15, 20, 30], 'hold': [2, 3, 4, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50, 60]}; D = {'delay': 8, 'hold': 5}
    k = sys.argv[2] if len(sys.argv) > 2 else 'delay'; st = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    if k in S:
        try: cur = int(xbmc.getInfoLabel('Skin.String(bz_uadv_%s)' % k) or D[k])
        except Exception: cur = D[k]
        L = S[k]; i = L.index(cur) if cur in L else L.index(D[k])
        xbmc.executebuiltin('Skin.SetString(bz_uadv_%s,%d)' % (k, L[(i + st) % len(L)]))
    sys.exit(0)
if action == 'keymap_leave':   # 5.33.194: manual/test - remove all three BEZEL profile keymaps + reloadkeymaps
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_km; bz_km.leave()
    sys.exit(0)
if action == 'keymap':
    xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)
    # np3: install / refresh the BEZEL Tab keymap in the profile keymaps folder and reload keymaps at once (no Kodi restart). Run on every
    # music window load (MyMusicNav.xml onload) and when bz_flip.py starts; cheap when nothing changed. Logged in kodi.log either way.
    import xbmcvfs
    src = 'special://skin/resources/keymaps/bezel2_np_tab.xml'; dst = 'special://profile/keymaps/zz_bezel2_np_tab.xml'   # zz_: Kodi loads keymap files in name order, so this one wins over a user keyboard.xml
    try:
        f = xbmcvfs.File(src); new = f.readBytes(); f.close()
        old = b''
        if xbmcvfs.exists(dst):
            f = xbmcvfs.File(dst); old = f.readBytes(); f.close()
        if bytes(new) != bytes(old) or home.getProperty('bz_km_loaded') != 'np3':
            if not xbmcvfs.exists('special://profile/keymaps/'): xbmcvfs.mkdirs('special://profile/keymaps/')
            if bytes(new) != bytes(old):
                f = xbmcvfs.File(dst, 'w'); ok = f.write(bytes(new)); f.close()
            else: ok = True
            if xbmcvfs.exists('special://profile/keymaps/bezel2_np_tab.xml'): xbmcvfs.delete('special://profile/keymaps/bezel2_np_tab.xml')   # np2 name
            # report other keymap files that also bind Tab / Display (they can only win if they sort after zz_)
            try:
                for fn in xbmcvfs.listdir('special://profile/keymaps/')[1]:
                    if fn.lower().endswith('.xml') and fn != 'zz_bezel2_np_tab.xml':
                        f = xbmcvfs.File('special://profile/keymaps/' + fn); txt = f.read().lower(); f.close()
                        if '<tab' in txt or '<display' in txt: xbmc.log('BEZEL keymap: %s also maps Tab / Display (ours loads last and wins in the music window)' % fn, xbmc.LOGINFO)
            except Exception: pass
            xbmc.executebuiltin('Action(reloadkeymaps)')
            home.setProperty('bz_km_loaded', 'np3')
            xbmc.log('BEZEL keymap %s at %s (%s)' % ('installed/reloaded' if ok else 'WRITE FAILED', xbmcvfs.translatePath(dst), 'changed' if bytes(new) != bytes(old) else 'reload only'), xbmc.LOGINFO)
    except Exception as e:
        xbmc.log('BEZEL keymap install failed: %r (Tab keeps Kodi\'s FullScreen; restart Kodi or copy %s to %s)' % (e, src, dst), xbmc.LOGWARNING)
    if home.getProperty('bz_flip_running') == 'true' and home.getProperty('bz_flip_ver') != 'np3':
        xbmc.log('BEZEL: an older bz_flip.py is still running from before the skin update; restart Kodi to load the new one', xbmc.LOGWARNING)
    sys.exit(0)
if action == 'backdrop':
    # BETA 1.4 item 15: random backdrop image from special://skin/extras/backdrop/ (any image dropped there joins in) on every window load; no immediate repeat
    import xbmcvfs, random
    d = 'special://skin/extras/backdrop/'
    try: files = sorted(f for f in xbmcvfs.listdir(d)[1] if f.lower().rsplit('.', 1)[-1] in ('png', 'jpg', 'jpeg', 'webp', 'gif'))
    except Exception: files = []
    if not files: home.clearProperty('bz_backdrop'); sys.exit(0)
    # 4.7.4: Tuner LOOK > Backdrop image (skin string bz_bdimg: empty = Random, else a file name that sticks until changed)
    fix = xbmc.getInfoLabel('Skin.String(bz_bdimg)')
    if fix and fix in files: home.setProperty('bz_backdrop', d + fix); sys.exit(0)
    cur = home.getProperty('bz_backdrop') or home.getProperty('bz_backdrop_last')  # 4.7.5: cleared on window close
    pick = [f for f in files if d + f != cur] or files
    home.setProperty('bz_backdrop', d + random.choice(pick))
    sys.exit(0)
if action == 'bdimg':
    # 4.7.4: Tuner LOOK > Backdrop image LEFT / RIGHT: Random -> each file in extras/backdrop (sorted) -> Random
    import xbmcvfs
    d = 'special://skin/extras/backdrop/'
    try: files = sorted(f for f in xbmcvfs.listdir(d)[1] if f.lower().rsplit('.', 1)[-1] in ('png', 'jpg', 'jpeg', 'webp', 'gif'))
    except Exception: files = []
    opts = [''] + files
    cur = xbmc.getInfoLabel('Skin.String(bz_bdimg)')
    i = opts.index(cur) if cur in opts else 0
    step = -1 if (len(sys.argv) > 2 and sys.argv[2] == 'prev') else 1
    nxt = opts[(i + step) % len(opts)]
    if nxt:
        xbmc.executebuiltin('Skin.SetString(bz_bdimg,%s)' % nxt); home.setProperty('bz_backdrop', d + nxt)
        home.setProperty('bz_bdimg_lbl', nxt.rsplit('.', 1)[0].replace('_', ' ').title())
    else:
        xbmc.executebuiltin('Skin.Reset(bz_bdimg)'); home.setProperty('bz_bdimg_lbl', 'Random')
        if files: import random; home.setProperty('bz_backdrop', d + random.choice(files))
    home.setProperty('bz_tune_dirty', '1')
    sys.exit(0)
if action == 'bdopacity':
    # BETA 1.4 item 15: Skin Settings > Backdrop Opacity: 0 -> 5 -> 10 -> 15 -> 20 -> 25 -> 0 (empty = 15)
    steps = ['0', '5', '10', '15', '20', '25']
    cur = xbmc.getInfoLabel('Skin.String(bz_bdop)') or '15'
    nxt = steps[(steps.index(cur) + 1) % len(steps)] if cur in steps else '15'
    xbmc.executebuiltin('Skin.SetString(bz_bdop,%s)' % nxt)
    sys.exit(0)
if action == 'tab':
    # np2 test: Tab / remote Display (FullScreen) from the BEZEL keymap (resources/keymaps/bezel2_np_tab.xml). Music playing in the music list
    # view: open / close the Now Playing dialog, so the music window is never replaced by Kodi's fullscreen window (that reload reset the sway).
    # Anything else (or another skin active): Kodi's own FullScreen, exactly as before.
    if xbmc.getSkinDir() == 'skin.bezel2':
        if xbmc.getCondVisibility('Window.IsActive(1112)'):
            home.clearProperty('bz_np'); xbmc.executebuiltin('Dialog.Close(1112)'); sys.exit(0)
        if home.getProperty('bz_audio_latch') == 'true' and home.getProperty('bz_np') != 'true' and xbmc.getCondVisibility('Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + Control.IsVisible(60) + ![Skin.HasSetting(bz_grid_music) + [Container(60).Content(albums) | Container(60).Content(artists)]] + !System.HasModalDialog'):
            home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.clearProperty('bz_np_was')
            if not xbmc.getCondVisibility('Control.HasFocus(60)'): xbmc.executebuiltin('SetFocus(60)')
            home.setProperty('bz_npdlg', 'true'); home.setProperty('bz_np', 'true')
            xbmc.executebuiltin('ActivateWindow(1112)'); sys.exit(0)
    xbmc.executebuiltin('Action(FullScreen)'); sys.exit(0)
if action in ('xinfo', 'xclose'):
    # 3.5.6: in-place extended info (ext_info_inplace): I / long-press on a poster. The list + colour block region crossfades to the info
    # (bz_xinfo, 550 ms sine), focus starts on PLAY; Back closes; no input for 15 s closes it with the same fade.
    L = xbmc.getInfoLabel
    def close():
        home.clearProperty('bz_xinfo'); xbmc.executebuiltin('Dialog.Close(1111)'); xbmc.executebuiltin('SetFocus(60)')
    if action == 'xclose':
        close(); sys.exit(0)
    if home.getProperty('bz_xinfo') == 'true': close(); sys.exit(0)
    for _ in range(40):   # 3.5.7: called from the context menu's onload: wait until it has closed
        if not xbmc.getCondVisibility('Window.IsVisible(contextmenu)'): break
        xbmc.sleep(25)
    dt, di = L('Container(60).ListItem.DBType'), L('Container(60).ListItem.DBID')
    if dt not in ('movie', 'tvshow', 'episode') or not di: sys.exit(0)
    di = int(di)
    props = ['title', 'tagline', 'year', 'mpaa', 'runtime', 'rating', 'genre', 'plot', 'cast', 'director', 'studio', 'streamdetails', 'resume', 'trailer', 'fanart']
    if dt == 'tvshow': props = ['title', 'year', 'mpaa', 'rating', 'genre', 'plot', 'cast', 'studio', 'premiered', 'episode', 'fanart']
    if dt == 'episode': props = ['title', 'showtitle', 'season', 'episode', 'runtime', 'rating', 'plot', 'cast', 'director', 'streamdetails', 'resume', 'firstaired', 'fanart']
    m = {'movie': ('VideoLibrary.GetMovieDetails', 'movieid', 'moviedetails'), 'tvshow': ('VideoLibrary.GetTVShowDetails', 'tvshowid', 'tvshowdetails'),
         'episode': ('VideoLibrary.GetEpisodeDetails', 'episodeid', 'episodedetails')}[dt]
    d = (rpc(m[0], {m[1]: di, 'properties': props}) or {}).get(m[2]) or {}
    def hms(t):
        t = int(t or 0); h, r = divmod(t, 3600); mi, se = divmod(r, 60)
        return '%d:%02d:%02d' % (h, mi, se) if h else '%d:%02d' % (mi, se)
    P = lambda k, v: home.setProperty('bz_xi_' + k, v or '')
    P('title', d.get('title')); P('dbtype', dt); P('dbid', str(di))
    P('tagline', d.get('tagline') or ('%s · S%02dE%02d' % (d.get('showtitle', ''), d.get('season', 0), d.get('episode', 0)) if dt == 'episode' else ''))
    P('year', str(d.get('year') or (d.get('firstaired') or '')[:4] or '')); P('mpaa', (d.get('mpaa') or '').replace('Rated ', ''))
    rt = int(d.get('runtime') or 0); P('runtime', '%d MIN' % (rt // 60) if rt >= 60 else '')
    rg = d.get('rating') or 0; P('rating', 'RATED %.1f' % rg if rg else '')
    P('genre', ' / '.join(d.get('genre') or [])); P('plot', d.get('plot'))
    sd = d.get('streamdetails') or {}; v = (sd.get('video') or [{}])[0] if sd.get('video') else {}; a = (sd.get('audio') or [{}])[0] if sd.get('audio') else {}
    res = ''
    w = v.get('width') or 0
    if w: res = '4K' if w >= 3200 else '1080P' if w >= 1800 else '720P' if w >= 1200 else '%dP' % (v.get('height') or 0)
    tech = [res, (v.get('codec') or '').upper(), ('%.2f:1' % v['aspect']) if v.get('aspect') else '',
            ('%s %dCH' % ((a.get('codec') or '').upper(), a.get('channels') or 0)) if a else '',
            ('DIRECTOR ' + ', '.join(d.get('director'))) if d.get('director') else '', (d.get('studio') or [''])[0] if d.get('studio') else '']
    P('tech', '  ·  '.join(t for t in tech if t))
    # 4.3 item 15: fanart, real media flags, details line, up to 12 cast
    P('fanart', d.get('fanart') or L('Container(60).ListItem.Art(fanart)'))
    vr = '4K' if w >= 3200 else '1080' if w >= 1800 else '720' if w >= 1200 else ('480' if w else '')
    P('f_res', vr); P('f_hdr', (v.get('hdrtype') or '').lower()); P('f_ac', (a.get('codec') or '').lower()); P('f_ch', str(a.get('channels') or '') if a else '')
    P('details', '  ·  '.join(x for x in [' / '.join(d.get('genre') or []).upper(), '%d MIN' % (rt // 60) if rt >= 60 else '', ('RATING %.1f' % rg) if rg else '', (d.get('mpaa') or '').replace('Rated ', '')] if x))
    cast = (d.get('cast') or [])[:12]
    for k in range(6, 12):
        c = cast[k] if k < len(cast) else {}
        P('cast%d_name' % k, c.get('name')); P('cast%d_role' % k, c.get('role')); P('cast%d_thumb' % k, c.get('thumbnail'))
    for k in range(6):
        c = cast[k] if k < len(cast) else {}
        P('cast%d_name' % k, c.get('name')); P('cast%d_role' % k, c.get('role')); P('cast%d_thumb' % k, c.get('thumbnail'))
    r = d.get('resume') or {}; pos, tot = r.get('position') or 0, r.get('total') or 0
    P('resume', ('RESUME ' + hms(pos)) if pos > 0 else ''); P('respct', str(int(100 * pos / tot)) if pos and tot else '0')
    P('trailer', d.get('trailer'))
    home.setProperty('bz_xinfo', 'true'); xbmc.executebuiltin('ActivateWindow(1111)')
    mon = xbmc.Monitor(); import time; t0 = time.time()
    while not mon.abortRequested() and time.time() - t0 < 3 and not xbmc.getCondVisibility('Window.IsVisible(1111)'): mon.waitForAbort(0.05)
    while not mon.abortRequested() and xbmc.getCondVisibility('Window.IsVisible(1111)'):
        if time.time() - t0 >= 15 and xbmc.getCondVisibility('System.IdleTime(15)'):
            close(); break
        mon.waitForAbort(0.25)
    home.clearProperty('bz_xinfo')
    sys.exit(0)
if action == 'xplay':
    mode = dbtype   # play / resume / trailer / more
    t, i = home.getProperty('bz_xi_dbtype'), home.getProperty('bz_xi_dbid')
    home.clearProperty('bz_xinfo'); xbmc.executebuiltin('Dialog.Close(1111,true)'); xbmc.executebuiltin('SetFocus(60)')
    if mode == 'trailer' and home.getProperty('bz_xi_trailer'): xbmc.executebuiltin('PlayMedia(%s)' % home.getProperty('bz_xi_trailer'))
    elif mode == 'fav' and t and i:   # 4.3 item 15: Favourite pill
        path = {'movie': 'videodb://movies/titles/%s', 'tvshow': 'videodb://tvshows/titles/%s/', 'episode': 'videodb://tvshows/titles/-1/-1/%s'}.get(t, '') % i
        if path: rpc('Favourites.AddFavourite', {'title': home.getProperty('bz_xi_title'), 'type': 'media', 'path': path, 'thumbnail': home.getProperty('bz_xi_fanart')})
    elif mode == 'more': xbmc.Monitor().waitForAbort(0.6); xbmc.executebuiltin('SendClick(6280)')
    elif mode in ('play', 'resume') and t and i:
        K = {'movie': 'movieid', 'episode': 'episodeid'}
        if t in K: rpc('Player.Open', {'item': {K[t]: int(i)}, 'options': {'resume': mode == 'resume'}})
        else: xbmc.executebuiltin('RunScript(special://skin/scripts/bz_cmd.py,play,%s,%s)' % (t, i))
    sys.exit(0)
if action == 'gstyle_removed_beta11':   # beta1 item 1: Grid Style cycle per section (skin string bz_gstyle_music / bz_gstyle_video): all grid -> focused poster -> all poster -> none
    sec = dbtype if dbtype in ('music', 'video') else 'music'
    cur = xbmc.getInfoLabel('Skin.String(bz_gstyle_%s)' % sec) or 'all'
    nxt = {'all': 'focused', 'focused': 'poster', 'poster': 'none'}.get(cur, 'all')
    xbmc.executebuiltin('Skin.SetString(bz_gstyle_%s,%s)' % (sec, nxt))
    sys.exit()
if action == 'npmode':   # 3.5.6: Now Playing colour block: 1 visualisation -> 2 artist bio -> 3 artist fanart -> 1
    cur = xbmc.getInfoLabel('Skin.String(bz_npmode)') or 'vis'
    nxt = {'vis': 'bio', 'bio': 'fanart', 'fanart': 'lyrics', 'lyrics': 'upnext'}.get(cur, 'vis')   # 4.1: + lyrics; beta1: + up next
    xbmc.executebuiltin('Skin.SetString(bz_npmode,%s)' % nxt)
    sys.exit()   # 4.1: the mode-name label timing is in the XML (AlarmClock), so taps never wait on this script
if action == 'getmoreviz':   # 3.5.5: Get more in the visualisation picker: the modal select must close before the add-on browser can open
    xbmc.executebuiltin('Dialog.Close(selectdialog,true)')
    for _ in range(40):
        if not xbmc.getCondVisibility('Window.IsActive(selectdialog)'): break
        xbmc.sleep(25)
    xbmc.executebuiltin('ActivateWindow(AddonBrowser,addons://repository.xbmc.org/xbmc.player.musicviz/,return)')
    sys.exit()
if action == 'gridfocus':
    # BEZEL 3.2.0 item 2: switching to grid view gives the grid (6600) the focus first, once it is drawn (the list follows it via bz_flip.py)
    mon = xbmc.Monitor()
    mon.waitForAbort(0.15)
    if not xbmc.getCondVisibility('[Window.IsActive(music) + Skin.HasSetting(bz_grid_music)] | [Window.IsActive(videos) + Skin.HasSetting(bz_grid_video)]'): sys.exit(0)
    for _ in range(40):
        if xbmc.getCondVisibility('Control.IsVisible(6600) + Integer.IsGreater(Container(6600).NumItems,0) + !Container(6600).IsUpdating'):
            xbmc.executebuiltin('SetFocus(6600)')
            if mon.waitForAbort(0.05) or xbmc.getCondVisibility('Control.HasFocus(6600)'): break
        elif mon.waitForAbort(0.05): break
    sys.exit(0)
if action == 'fsexit':
    # 2.0a3: leave fullscreen Now Playing. Closing the window plays its WindowClose animations (the block slides back, the text fades),
    # exactly as with Back, then the list window returns.
    if xbmc.getCondVisibility('Window.IsActive(visualisation)'): xbmc.executebuiltin('ActivateWindow(Music)')
    sys.exit(0)
if action == 'blockcolor':
    # 2.0a3.1: colour block colour presets + custom hex (skin strings bz_blockcol = RRGGBB, bz_blockcol_name)
    P = [('BEZEL blue', ''), ('Black', '000000'), ('Charcoal', '2B2B2B'), ('Red', '8E1B1B'), ('Green', '1E6B3A'), ('Purple', '5B2A86'),
         ('Orange', 'B5561A'), ('Teal', '0F6E6E'), ('Custom hex...', None)]
    i = xbmcgui.Dialog().select('Colour block colour', [p[0] for p in P])
    if i < 0: sys.exit(0)
    name, hx = P[i]
    if hx is None:
        hx = xbmcgui.Dialog().input('Colour (RRGGBB)', xbmc.getInfoLabel('Skin.String(bz_blockcol)') or '0B5F86').strip().lstrip('#').upper()
        if len(hx) == 8: hx = hx[2:]
        if len(hx) != 6 or any(c not in '0123456789ABCDEF' for c in hx): xbmcgui.Dialog().notification('BEZEL', 'Not a colour: use RRGGBB', xbmcgui.NOTIFICATION_INFO, 2500); sys.exit(0)
        name = '#' + hx
    if hx: xbmc.executebuiltin('Skin.SetString(bz_blockcol,%s)' % hx); xbmc.executebuiltin('Skin.SetString(bz_blockcol_name,%s)' % name)
    else: xbmc.executebuiltin('Skin.Reset(bz_blockcol)'); xbmc.executebuiltin('Skin.Reset(bz_blockcol_name)')
    sys.exit(0)
if action == 'vistoggle':
    # 3.5.2: from Kodi's fullscreen music window (Tab / FullScreen). MusicVisualisation.xml has already gone back to the music screen.
    import time
    now = time.time()
    try: last = float(home.getProperty('bz_vistoggle_t') or 0)
    except Exception: last = 0
    if now - last < 1.0: sys.exit(0)   # same key press, second onload
    home.setProperty('bz_vistoggle_t', str(now))
    if home.getProperty('bz_audio_latch') != 'true' or xbmc.getCondVisibility('Player.HasVideo'): sys.exit(0)
    for i in range(40):
        if xbmc.getCondVisibility('Window.IsActive(music) + !Window.IsActive(visualisation)'): break
        xbmc.Monitor().waitForAbort(0.05)
    if home.getProperty('bz_np') == 'true':
        home.clearProperty('bz_np'); xbmc.executebuiltin('SetFocus(60)')
    else:
        home.setProperty('bz_np', 'true')
        for i in range(20):
            if xbmc.getCondVisibility('Control.IsVisible(6390)'): break
            xbmc.Monitor().waitForAbort(0.05)
        xbmc.Monitor().waitForAbort(1.2)   # 4.2 item 12: the list bar fades out with the list instead of popping off
        xbmc.executebuiltin('SetFocus(6390)')
    sys.exit(0)
if action in ('np', 'nptoggle'):
    # 2.0a3.1: in-place Now Playing (music only). From anywhere (mini player, menu, Kodi's fullscreen music window): back to BEZEL MUSIC LIST with bz_np set
    # 2.0a3.4: 'nptoggle' (Tab / FullScreen, via MusicVisualisation.xml): a second press leaves Now Playing again. bz_np is changed only once the
    # music window is back, so its slide-in / slide-back animations play.
    if home.getProperty('bz_audio_latch') != 'true' or xbmc.getCondVisibility('Player.HasVideo'): sys.exit(0)
    # 3.5.1: Tab / FullScreen opens Kodi's visualisation window, now an empty dialog over the music window: close it (the music window
    # was never unloaded, so the sway carries on) and toggle the panel. From another window: open the music window first.
    # np1 test: music playing + already in the music library list view (view 60, not the grid): Now Playing opens as a dialog over the
    # music window (Custom_1112_NowPlaying.xml), so the album sway underneath never resets. Every other route keeps the in-place panel below.
    if action == 'np' and home.getProperty('bz_np') != 'true' and xbmc.getCondVisibility('Window.IsActive(music) + !Window.IsActive(visualisation) + Control.IsVisible(60) + ![Skin.HasSetting(bz_grid_music) + [Container(60).Content(albums) | Container(60).Content(artists)]] + !Window.IsActive(1112)'):
        home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.clearProperty('bz_np_was')
        # np2: hand the music window's focus back to the list first (the slide-menu card / A-Z bar / art are hidden once the dialog is up),
        # so after the dialog closes the keys move the list and Left opens the slide menu again
        if not xbmc.getCondVisibility('Control.HasFocus(60)'): xbmc.executebuiltin('SetFocus(60)')
        home.setProperty('bz_npdlg', 'true'); home.setProperty('bz_np', 'true')
        xbmc.executebuiltin('ActivateWindow(1112)')
        sys.exit(0)
    vis = xbmc.getCondVisibility('Window.IsActive(visualisation)')
    if vis:
        xbmc.executebuiltin('Dialog.Close(visualisation,true)')
        for i in range(20):
            if not xbmc.getCondVisibility('Window.IsActive(visualisation)'): break
            xbmc.Monitor().waitForAbort(0.05)
    leaving = action == 'nptoggle' and home.getProperty('bz_np') == 'true' and xbmc.getCondVisibility('Window.IsActive(music)')
    home.clearProperty('bz_np_was')
    home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez')
    if not xbmc.getCondVisibility('Window.IsActive(music)') or xbmc.getCondVisibility('Window.IsActive(visualisation)'):
        # 4.2 item 12: open the music window straight into Now Playing (no list frame first, no pop)
        if not leaving: home.setProperty('bz_np', 'true')
        xbmc.executebuiltin('ActivateWindow(Music)')
        for i in range(60):
            if xbmc.getCondVisibility('Window.IsActive(music) + !Window.IsActive(visualisation)'): break
            xbmc.Monitor().waitForAbort(0.05)
        xbmc.Monitor().waitForAbort(0.15)
    if leaving:
        home.clearProperty('bz_np'); xbmc.executebuiltin('SetFocus(60)'); sys.exit(0)
    home.setProperty('bz_np', 'true')
    for i in range(20):
        if xbmc.getCondVisibility('Control.IsVisible(6390)'): break
        xbmc.Monitor().waitForAbort(0.05)
    xbmc.Monitor().waitForAbort(1.2)   # 4.2 item 12
    xbmc.executebuiltin('SetFocus(6390)')
    sys.exit(0)
# BETA 2 item 20: card 2 values wider than 260 px are abbreviated (VISUALIZATION -> VISUAL.): every word longer than 7 letters is cut to
# 6 letters + '.', longest first, until it fits; short values are unchanged. Widths = Ubuntu Regular advances (34 px uppercase bz_list / 21 px bz_r21).
W34 = {' ': 7.9, '!': 9.4, '"': 14.2, '#': 22.7, '$': 19.2, '%': 29.2, '&': 22.6, "'": 8.2, '(': 11.0, ')': 11.0, '*': 16.3, '+': 19.2, ',': 8.4, '-': 10.2, '.': 8.4, '/': 13.1, '0': 19.2, '1': 19.2, '2': 19.2, '3': 19.2, '4': 19.2, '5': 19.2, '6': 19.2, '7': 19.2, '8': 19.2, '9': 19.2, ':': 8.4, ';': 8.4, '<': 19.2, '=': 19.2, '>': 19.2, '?': 13.7, '@': 32.3, 'A': 22.5, 'B': 21.9, 'C': 21.1, 'D': 24.2, 'E': 19.4, 'F': 18.3, 'G': 22.8, 'H': 24.0, 'I': 9.1, 'J': 17.0, 'K': 21.4, 'L': 17.6, 'M': 29.6, 'N': 24.8, 'O': 26.5, 'P': 20.7, 'Q': 26.5, 'R': 21.4, 'S': 18.1, 'T': 19.2, 'U': 23.4, 'V': 22.3, 'W': 31.6, 'X': 21.5, 'Y': 20.3, 'Z': 19.5, '[': 11.2, '\\': 13.1, ']': 11.2, '^': 19.2, '_': 16.7, '`': 12.8, '{': 11.3, '|': 9.5, '}': 11.3, '~': 19.2}
W21 = {' ': 4.8, '!': 5.8, '"': 8.8, '#': 14.0, '$': 11.8, '%': 18.0, '&': 14.0, "'": 5.1, '(': 6.8, ')': 6.8, '*': 10.1, '+': 11.8, ',': 5.2, '-': 6.3, '.': 5.2, '/': 8.1, '0': 11.8, '1': 11.8, '2': 11.8, '3': 11.8, '4': 11.8, '5': 11.8, '6': 11.8, '7': 11.8, '8': 11.8, '9': 11.8, ':': 5.2, ';': 5.2, '<': 11.8, '=': 11.8, '>': 11.8, '?': 8.5, '@': 20.0, 'A': 13.9, 'B': 13.5, 'C': 13.0, 'D': 15.0, 'E': 12.0, 'F': 11.3, 'G': 14.1, 'H': 14.8, 'I': 5.7, 'J': 10.5, 'K': 13.2, 'L': 10.9, 'M': 18.3, 'N': 15.3, 'O': 16.3, 'P': 12.8, 'Q': 16.3, 'R': 13.2, 'S': 11.2, 'T': 11.9, 'U': 14.5, 'V': 13.8, 'W': 19.5, 'X': 13.2, 'Y': 12.6, 'Z': 12.0, '[': 6.9, '\\': 8.1, ']': 6.9, '^': 11.8, '_': 10.3, '`': 7.9, 'a': 11.0, 'b': 12.4, 'c': 9.8, 'd': 12.4, 'e': 11.7, 'f': 8.1, 'g': 12.1, 'h': 12.0, 'i': 5.3, 'j': 5.3, 'k': 11.0, 'l': 5.7, 'm': 18.1, 'n': 12.0, 'o': 12.4, 'p': 12.4, 'q': 12.4, 'r': 8.1, 's': 9.4, 't': 8.4, 'u': 12.0, 'v': 10.5, 'w': 16.3, 'x': 10.7, 'y': 10.4, 'z': 9.9, '{': 7.0, '|': 5.9, '}': 7.0, '~': 11.8}
def bz_abbr(s, W, up, mx=260):
    import re
    def wd(x): return sum(W.get((c.upper() if up else c), 20) for c in x)
    if not s or wd(s) <= mx: return s
    t = re.split(r'([^A-Za-z]+)', s)
    while wd(''.join(t)) > mx:
        c = [i for i, x in enumerate(t) if x.isalpha() and len(x) > 7]
        if not c: break
        i = max(c, key=lambda i: len(t[i])); nxt = t[i + 1] if i + 1 < len(t) else ''
        t[i] = t[i][:6] + ('' if nxt.startswith('.') else '.')
    s = ''.join(t)
    while wd(s) > mx and len(s) > 2: s = s[:-2] + '.'
    return s
if action == 'abbr':
    v = xbmc.getInfoLabel('Visualisation.Name')
    home.setProperty('bz_ab_vis_src', v); home.setProperty('bz_ab_vis', bz_abbr(v, W34, True))
    sys.exit(0)
# BETA 1.1: KODI SETTINGS quick rows on the back card. qsync fills Window(Home).Property(bz_qs_<key>) with the current value labels;
# qset,<key> steps that setting to its next option (Kodi's own option list, via JSON-RPC) and refreshes the labels.
QS = {'audio': 'audiooutput.audiodevice', 'subs': 'locale.subtitlelanguage', 'resume': 'myvideos.selectaction', 'power': 'powermanagement.shutdownstate'}
def _rpc(method, params):
    try: return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}))).get('result') or {}
    except Exception: return {}
QS_CAT = {'audiooutput.audiodevice': ('system', 'audio'), 'locale.subtitlelanguage': ('player', 'language'), 'myvideos.selectaction': ('media', 'video'), 'powermanagement.shutdownstate': ('system', 'powermanagement')}
def _qs_all(only=None):
    out = {}
    # the audio category enumerates the output devices (slow, and it crashed a box without an audio server), so it is only read
    # when the audio row is actually stepped (qset,audio); qsync leaves the audio label as last set
    for cat in sorted(set(QS_CAT[i] for i in QS.values() if (only is None and i != 'audiooutput.audiodevice') or i == only)):
        for st in _rpc('Settings.GetSettings', {'level': 'expert', 'filter': {'section': cat[0], 'category': cat[1]}}).get('settings', []):
            if st.get('id') in QS.values():
                if st['id'] == 'locale.subtitlelanguage':   # only the short list (None / Forced / Original / UI language), not every language
                    st['options'] = [o for o in (st.get('options') or []) if o.get('value') in ('none', 'forced_only', 'original', 'default')]
                out[st['id']] = st
    return out
def _qs_label(st):
    v = st.get('value')
    for o in st.get('options', []) or []:
        if o.get('value') == v: return o.get('label', str(v))
    return str(v)
# BETA 2.1: Kodi card quick rows. qput,<setting>,<value> sets one Kodi setting; qstart steps the startup window; _qs2 refreshes
# bz_qs_sounds / bz_qs_saver (true when on) and bz_qs_startup (label) for the toggles / label2
def _qs2():
    g = lambda sid: _rpc('Settings.GetSettingValue', {'setting': sid}).get('value')
    home.setProperty('bz_qs_sounds', 'true' if g('lookandfeel.soundskin') else '')
    home.setProperty('bz_qs_saver', 'true' if g('screensaver.mode') else '')
    for st in _rpc('Settings.GetSettings', {'level': 'expert', 'filter': {'section': 'interface', 'category': 'other'}}).get('settings', []):
        if st.get('id') == 'lookandfeel.startupwindow': home.setProperty('bz_qs_startup', bz_abbr(_qs_label(st), W21, False)); return st
if action == 'qput':
    a = sys.argv[2:] if len(sys.argv) > 2 else []
    if len(a) >= 1: _rpc('Settings.SetSettingValue', {'setting': a[0], 'value': a[1] if len(a) > 1 else ''})
    _qs2(); sys.exit(0)
if action == 'qstart':
    st = _qs2() or {}; opts = [o.get('value') for o in (st.get('options') or [])]
    if opts:
        nv = opts[(opts.index(st.get('value')) + 1) % len(opts)] if st.get('value') in opts else opts[0]
        _rpc('Settings.SetSettingValue', {'setting': 'lookandfeel.startupwindow', 'value': nv}); _qs2()
    sys.exit(0)
if action in ('qsync', 'qset'):
    one = QS.get(dbtype) if action == 'qset' else None
    al = _qs_all(one)
    if one and one in al:
        st = al[one]; opts = [o.get('value') for o in (st.get('options') or [])]
        if opts:
            nv = opts[(opts.index(st.get('value')) + 1) % len(opts)] if st.get('value') in opts else opts[0]
            _rpc('Settings.SetSettingValue', {'setting': one, 'value': nv}); al = _qs_all(one)
    for k, sid in QS.items():
        if sid in al: home.setProperty('bz_qs_' + k, bz_abbr(_qs_label(al[sid]), W21, False))   # BETA 2 item 20
    if not home.getProperty('bz_qs_audio'): home.setProperty('bz_qs_audio', 'Change')
    _qs2()
    sys.exit(0)
if action == 'npalbum':   # BETA 2.2 item 3: slide menu mini player art: open the playing song's album (video: the Now Playing view as before)
    aid = 0
    if xbmc.getCondVisibility('Player.HasAudio'):
        try: aid = int((rpc('Player.GetItem', {'playerid': 0, 'properties': ['albumid']}).get('item') or {}).get('albumid') or 0)
        except Exception: aid = 0
    if not aid:
        home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); xbmc.executebuiltin('RunScript(special://skin/scripts/bz_cmd.py,np)'); sys.exit(0)
    action = 'tomusic'; args[1] = 'musicdb://albums/%d/' % aid
def _bz_load_then_close(win, path):
    # 3.2.1 item 5: open the new section behind the menu, wait until its list is loaded, then close the menu
    mon = xbmc.Monitor(); old = xbmc.getInfoLabel('Container.FolderPath')
    # 4.0.1 O25: the new section is held hidden (bz_secload) until its list AND the focused item's art are in, then the menu closes
    # and the section fades in once (bz_secfade, 400 ms). Hard cap 3 s so a slow box (Shield) never hangs on a missing image.
    # SPEED t3451: MM warm already put this exact list under the menu -> just close the menu (no reopen, no load/art waits)
    if path and xbmc.getCondVisibility('Window.IsActive(%s)' % win) and old.rstrip('/') == path.rstrip('/') and not xbmc.getCondVisibility('Container.IsUpdating'):
        home.clearProperty('bz_secload'); home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); return
    home.clearProperty('bz_secfade'); home.setProperty('bz_secload', 'true')
    _wasact = xbmc.getCondVisibility('Window.IsActive(%s)' % win)
    xbmc.executebuiltin('ActivateWindow(%s%s)' % (win, (',' + path) if path else ''))
    # artist-root fix: Kodi keeps a drilled subfolder when asked for its parent root (PathHasParent) -> force the root
    if path:
        for i in range(20):
            if xbmc.getCondVisibility('Window.IsActive(%s)' % win): break
            mon.waitForAbort(0.05)
        cur = xbmc.getInfoLabel('Container.FolderPath')
        if _wasact or (cur != path and cur.startswith(path.split('?')[0])):
            xbmc.executebuiltin('Container.Update(%s,replace)' % path)
    for i in range(60):
        mon.waitForAbort(0.05)
        if xbmc.getCondVisibility('Window.IsActive(%s)' % win) and xbmc.getInfoLabel('Container.FolderPath') != old and not xbmc.getCondVisibility('Container.IsUpdating'): break
    if path and xbmc.getInfoLabel('Container.FolderPath').rstrip('/') != path.rstrip('/') and not xbmc.getInfoLabel('Container.FolderPath').startswith(path.split('?')[0]):   # F2 batch2: same-window path switch ignored -> force it
        xbmc.executebuiltin('Container.Update(%s,replace)' % path)
        for i in range(40):
            mon.waitForAbort(0.05)
            if xbmc.getInfoLabel('Container.FolderPath').rstrip('/') == path.rstrip('/') and not xbmc.getCondVisibility('Container.IsUpdating'): break
    for i in range(30):   # art of the focused item known (poster / thumb / fanart) -> give the texture loader a moment
        if xbmc.getInfoLabel('Container(60).ListItem.Art(poster)') or xbmc.getInfoLabel('Container(60).ListItem.Art(thumb)') or xbmc.getInfoLabel('Container(60).ListItem.Icon'): break
        mon.waitForAbort(0.05)
    mon.waitForAbort(0.15)   # SPEED t3451: 0.35 -> 0.15
    home.setProperty('bz_secfade', 'true'); home.clearProperty('bz_secload')
    home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez')
    mon.waitForAbort(0.6); home.clearProperty('bz_secfade')
if action == 'tomusic':
    if xbmc.getCondVisibility('Window.IsActive(1112)'):   # BETA 1.1: picked from the slide menu over the Now Playing dialog
        home.clearProperty('bz_np'); xbmc.executebuiltin('Dialog.Close(1112,true)'); xbmc.sleep(150)
    # 3.5.1: video -> music with music playing: the mini player and the poster fade out together (1.25 s, bz_tomusic), a short gap,
    # then the music window opens and its album art fades in (1.5 s, bz_from_video); no flip, the art is already cached.
    path = args[1] or ''
    if xbmc.getCondVisibility('Window.IsActive(videos)') and home.getProperty('bz_audio_latch') == 'true' and not xbmc.getCondVisibility('Player.HasVideo'):
        home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez')
        home.setProperty('bz_tomusic', 'true')
        xbmc.Monitor().waitForAbort(1.45)
        home.setProperty('bz_from_video', 'true')
        xbmc.executebuiltin('ActivateWindow(Music%s)' % ((',' + path) if path else ''))
        if path:
            xbmc.Monitor().waitForAbort(0.3); cur = xbmc.getInfoLabel('Container.FolderPath')
            if cur != path and cur.startswith(path.split('?')[0]): xbmc.executebuiltin('Container.Update(%s,replace)' % path)
        xbmc.Monitor().waitForAbort(2.0)
        home.clearProperty('bz_tomusic'); home.clearProperty('bz_from_video')
    else:
        _bz_load_then_close('Music', path)
    sys.exit(0)
if action == 'go':
    if xbmc.getCondVisibility('Window.IsActive(1112)'):   # BETA 1.1: picked from the slide menu over the Now Playing dialog
        home.clearProperty('bz_np'); xbmc.executebuiltin('Dialog.Close(1112,true)'); xbmc.sleep(150)
    # 2.0a3.4: side menu -> video sections (dbtype slot = path). From BEZEL MUSIC LIST with music playing: the art turns, shrinks into the
    # mini player spot (2.3 s), then the video view opens (poster slides in). Without music the art fades out first. No 'return'.
    path = args[1]
    if xbmc.getCondVisibility('Window.IsActive(music) + !Window.IsActive(visualisation)'):
        if home.getProperty('bz_audio_latch') == 'true' and not xbmc.getCondVisibility('Player.HasVideo'):
            home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez')
            # 3.5.3 (music_to_video_v3, no flip): the mini player fades in over the top of the list (bz_m2v); the album keeps swaying
            # until it is next flat (0 deg), the sway is held there (no snap) and the art fades out (bz_m2v_flat); the video list opens with
            # its cascade while the mini player stays in place; the poster and the mini player buttons fade in (0.5 s delay, 1.5 s).
            import time
            mon = xbmc.Monitor()
            home.clearProperty('bz_np'); home.setProperty('bz_m2v', 'true')
            # 3.5.7: fast: no wait for flat. The art (with its glares, which live inside the cover layers) fades out from wherever
            # the sway is (0.5 s, the sway keeps running so nothing snaps), and the video list + cascade open at once.
            home.setProperty('bz_m2v_flat', 'true'); mon.waitForAbort(0.45)
            home.setProperty('bz_from_music', 'true'); home.setProperty('bz_casc_force', 'true')
            xbmc.executebuiltin('ActivateWindow(Videos,%s)' % path)
            mon.waitForAbort(1.0)
            for k in ('bz_m2v', 'bz_m2v_flat'): home.clearProperty(k)
            sys.exit(0)
        else:
            home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.setProperty('bz_tovideo', 'fade'); xbmc.Monitor().waitForAbort(0.6)
    _bz_load_then_close('Videos', path)
    sys.exit(0)
if action == 'gridenter':
    # 3.5.4: Right from the list: the grid takes focus on the list's item (bz_grid_target from bz_flip.py; an unfocused panel ignores Control.Move)
    mon = xbmc.Monitor()
    t = home.getProperty('bz_grid_target')
    xbmc.executebuiltin('SetFocus(6600)')
    for i in range(20):
        if xbmc.getCondVisibility('Control.HasFocus(6600)'): break
        mon.waitForAbort(0.03)
    if t:
        # read the grid position once it is steady (the readback lags a frame or two), then one move
        last = None
        for i in range(12):
            mon.waitForAbort(0.06)
            try: c = int(xbmc.getInfoLabel('Container(6600).CurrentItem')) - 1
            except Exception: c = None
            if c is not None and c == last: break
            last = c
        if c is not None and int(t) != c:
            # Control.Move steps a vertical panel by rows (4 tiles): rows by Move, then the column by Left / Right
            t = int(t); dr = t // 4 - c // 4; dc = t % 4 - c % 4
            if dr: xbmc.executebuiltin('Control.Move(6600,%d)' % dr)
            for i in range(abs(dc)): xbmc.executebuiltin('Action(%s)' % ('Right' if dc > 0 else 'Left'))
    sys.exit(0)
if action == 'gridclick':
    # 3.5.4: a grid tile opens / plays the same item as the list. A tap on an unfocused grid focuses and clicks in one go, so the
    # list is put on the tapped item here first (DBID / label match), then selected.
    mon = xbmc.Monitor()
    L = xbmc.getInfoLabel
    def key(c, i): return L('Container(%d).ListItemAbsolute(%d).DBID' % (c, i)) or L('Container(%d).ListItemAbsolute(%d).Label' % (c, i))
    last = None
    for i in range(12):
        mon.waitForAbort(0.05)
        try: c = int(L('Container(6600).CurrentItem')) - 1
        except Exception: c = None
        if c is not None and c == last: break
        last = c
    if c is not None and c >= 0:
        k = key(6600, c)
        n = int(L('Container(60).NumAllItems') or 0)
        m = {key(60, i): i for i in range(n)}
        j = m.get(k); p = m.get(L('Container(60).ListItem.DBID') or L('Container(60).ListItem.Label'))
        if j is not None and p is not None and j != p:
            xbmc.executebuiltin('Control.Move(60,%d)' % (j - p))
            for i in range(20):
                mon.waitForAbort(0.05)
                if (L('Container(60).ListItem.DBID') or L('Container(60).ListItem.Label')) == k: break
    xbmc.executebuiltin('SetFocus(60)'); mon.waitForAbort(0.1); xbmc.executebuiltin('Action(Select)')
    sys.exit(0)
if action == 'vidsel':
    # BETA 2.6 item 5: Select in fullscreen video = pause / resume + show the OSD
    xbmc.executebuiltin('PlayerControl(Play)'); xbmc.executebuiltin('ActivateWindow(videoosd)'); sys.exit(0)
if action == 'vidback':
    # BETA 2.7 item 3: Back in fullscreen video: the first Back hides the controls (OSD, info, seek bar), the second Back stops
    if xbmc.getCondVisibility('Window.IsVisible(videoosd)'):
        import time; home.setProperty('bz_vosdc', str(time.time()))
        xbmc.executebuiltin('Dialog.Close(videoosd)'); sys.exit(0)
    if xbmc.getCondVisibility('Window.IsVisible(fullscreeninfo)'):
        xbmc.executebuiltin('Dialog.Close(fullscreeninfo)'); sys.exit(0)
    if xbmc.getCondVisibility('Player.ShowInfo'):
        xbmc.executebuiltin('Action(Info)'); sys.exit(0)
    import time
    try: recent = time.time() - float(home.getProperty('bz_vosdc') or 0) < 6   # the OSD was just closed by Back: the seek bar it leaves is not a second 'controls' step
    except ValueError: recent = False
    if xbmc.getCondVisibility('Player.DisplayAfterSeek | Player.Seeking') and not recent:
        home.setProperty('bz_vosdc', str(time.time())); sys.exit(0)
    xbmc.executebuiltin('PlayerControl(Stop)'); sys.exit(0)
if action == 'npctl':
    # BEZEL 3.2.1 item 1: the old under-the-art controls are gone; every path (M via PlayerControls.xml, taps) opens the colour-block list
    if xbmc.getCondVisibility('Window.IsActive(fullscreenvideo)'): xbmc.executebuiltin('ActivateWindow(videoosd)')
    elif xbmc.getCondVisibility('Window.IsActive(1115)'): xbmc.executebuiltin('Dialog.Close(1115)')
    else: xbmc.executebuiltin('ActivateWindow(1115)')
    sys.exit(0)
if action == 'upnext_goto':   # BETA 2.8 item 5: Up Next Select = jump to that entry of the current music playlist
    try: n = int(dbtype)
    except Exception: n = 0
    if n > 0: rpc('Player.GoTo', {'playerid': 0, 'to': n - 1})
    sys.exit(0)
if action == 'allrow':   # ALLROW (Rob t3729/t3730): bottom "All" row opens the stock All node (<path>-1/), query kept
    fp = xbmc.getInfoLabel('Container.FolderPath')
    base, _, q = fp.partition('?')
    xbmcgui.Window(10000).setProperty('bz_allret', fp)  # 5.33.95: Back from All lands on the ALL row, not the parked Disc 2
    if not base.endswith('/'): base += '/'
    xbmc.executebuiltin('Container.Update(%s-1/%s,return)' % (base, ('?' + q) if q else ''))
    sys.exit(0)
def _bz_showall_sync(only=None):
    import json as _json
    for _k, _b, _sid in (('seasons','bz_allseasons','videolibrary.showallitems'), ('albums','bz_allalbums','musiclibrary.showallitems')):
        if only and only != _k: continue
        try:
            _want = bool(xbmc.getCondVisibility('Skin.HasSetting(%s)' % _b))
            _r = xbmc.executeJSONRPC(_json.dumps({"jsonrpc":"2.0","id":1,"method":"Settings.GetSettingValue","params":{"setting":_sid}}))
            if _json.loads(_r).get('result',{}).get('value') != _want:
                xbmc.executeJSONRPC(_json.dumps({"jsonrpc":"2.0","id":1,"method":"Settings.SetSettingValue","params":{"setting":_sid,"value":_want}}))
        except Exception as _e:
            xbmc.log('BEZEL showall %s: %s' % (_k, _e), xbmc.LOGWARNING)
if action == 'lookcycle':   # t5146 Bezel Look Options: one global button style (bz_at_hishape) for MM + every list
    _c = xbmc.getInfoLabel('Skin.String(bz_at_hishape)') or '5'
    _n = {'1': '2', '2': '3', '3': '4', '4': '5'}.get(_c, '1')
    xbmc.executebuiltin('Skin.SetString(bz_at_hishape,%s)' % _n)
    sys.exit(0)
if action == 'showall':
    xbmc.sleep(100)
    _sa = sys.argv[2] if len(sys.argv) > 2 else None
    _bz_showall_sync(_sa)
    # 5.24 soft: refresh the open underlay list so the stock All entry shows/hides live (MM / bz_navbez untouched)
    try:
        import re as _re
        _ct = xbmc.getInfoLabel('Container(60).Content') or xbmc.getInfoLabel('Container.Content')
        _fp = xbmc.getInfoLabel('Container(60).FolderPath') or xbmc.getInfoLabel('Container.FolderPath')
        _base = _fp.split('?')[0]
        _ok = (_sa == 'seasons' and (_ct == 'seasons' or bool(_re.match(r'videodb://tvshows/[^?]*/\d+/$', _base)))) or \
              (_sa == 'albums' and (_ct == 'albums' or (_base.startswith('musicdb://') and ('albums' in _base or bool(_re.search(r'/\d+/$', _base))))))
        if _ok:
            xbmc.executebuiltin('Container.Update(%s,replace)' % _fp if _fp else 'Container.Refresh')
            xbmc.executebuiltin('AlarmClock(bz_safoc,SetFocus(6968),00:00,silent)')
    except Exception as _e:
        xbmc.log('BEZEL showall refresh: %s' % _e, xbmc.LOGWARNING)
if action == 'start' and xbmc.getInfoLabel('Skin.String(bz_tunever)') != '401':
    # 4.0.1 O24: the speed / timing rows got 15-17 finer steps. Saved 4.0.0 step numbers are moved to the step with the same value
    # once (bz_tunever=401), then the fixed-time steps are re-patched into the skin files so nothing shifts for existing users.
    _MIG = {"swaypause": [2, 4, 5, 6, 8, 10, 12, 14], "flip": [7, 9, 11, 12, 13, 15, 17], "pingspeed": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13], "rowscroll": [7, 9, 11, 12, 13, 15, 17], "zoomtime": [1, 3, 5, 7, 9, 11, 13], "fanart": [1, 3, 5, 7, 9, 11], "cascspeed": [7, 9, 11, 12, 13, 15, 17], "cascstag": [1, 4, 6, 8, 10, 12, 14], "menuopen": [7, 9, 11, 12, 13, 15, 17], "menuclose": [7, 9, 11, 12, 13, 15, 17], "dtapwin": [3, 5, 7, 9, 11, 12, 13], "mctrl": [7, 9, 11, 12, 13, 15, 17], "d3speed": [2, 4, 6, 8, 11, 13, 15], "phold": [2, 4, 5, 6, 8, 10, 12, 14]}
    _ch = False
    for _i, _m in _MIG.items():
        _v = xbmc.getInfoLabel('Skin.String(bz_at_%s)' % _i)
        if _v.isdigit() and 1 <= int(_v) <= len(_m):
            xbmc.executebuiltin('Skin.SetString(bz_at_%s,%d)' % (_i, _m[int(_v) - 1])); _ch = True
    xbmc.executebuiltin('Skin.SetString(bz_tunever,401)')
    if _ch:
        xbmc.sleep(300)
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_tune_patch
            if bz_tune_patch.patch(xbmc.getInfoLabel): xbmc.executebuiltin('ReloadSkin()')
        except Exception as _e: xbmc.log('BEZEL O24 migrate: %s' % _e, xbmc.LOGWARNING)
if action == 'start':
    # 5.28: View All Seasons / View All Albums default ON on fresh userdata (Rob voice Oct 29).
    # Skin.HasSetting is false both when unset and when user turned Off, so only apply once per userdata via bz_showall_inited.
    if not xbmc.getInfoLabel('Skin.String(bz_showall_inited)'):
        xbmc.executebuiltin('Skin.SetBool(bz_allalbums)')
        xbmc.executebuiltin('Skin.SetBool(bz_allseasons)')
        xbmc.executebuiltin('Skin.SetString(bz_showall_inited,1)')
    # Tuner toggles drive Kodi showallitems; sync every start/ReloadSkin
    _bz_showall_sync()

    for _k in ('music', 'movies', 'tv'):   # t4075: restore MM pill last-used after ReloadSkin / cold start
        _v = xbmc.getInfoLabel('Skin.String(bz_last_mmsub_%s)' % _k)
        if _v and not home.getProperty('bz_mmsub_' + _k): home.setProperty('bz_mmsub_' + _k, _v)
    if not xbmc.getInfoLabel('Skin.String(bz_attn_outline)'):   # attnqueue #9: global outline bar default once (Tuner LOOK > bar shape still changes it)
        xbmc.executebuiltin('Skin.SetString(bz_at_hishape,5)'); xbmc.executebuiltin('Skin.SetString(bz_attn_outline,1)')
    # 2.0a2: startup / Home redirect. The very first entry after Kodi starts sets bz_startfade (slow fade in from black, art a little later).
    # t5011: MM-on-load Music underlay = Artists (was recentlyplayed/albums/recent songs).
    first = not home.getProperty('bz_started')
    if first: home.setProperty('bz_started', 'true'); home.setProperty('bz_startfade', 'true')
    path = 'musicdb://artists/'
    if first:
        # t5012: pill defaults on cold start — Artists / Titles / Shows (index 1). Tuner Startup highlight (bz_at_mmdef) untouched.
        for _pk in ('music', 'movies', 'tv'):
            home.setProperty('bz_mmsub_' + _pk, '1')
            xbmc.executebuiltin('Skin.SetString(bz_last_mmsub_%s,1)' % _pk)
    # BETA 2.4 item 4: open the library root first, then the list, so Back steps up one level (musicdb://) instead of to the sources root ("")
    if first and not xbmc.getCondVisibility('Skin.HasSetting(bz_nomenustart)'):
        # 4.7.11 MM-first: arm the start menu BEFORE Music opens (Shield: the music window can take > 3 s, so bz_nav was never set under the splash)
        # MMDEF t4014: Tuner MAIN MENU > Default section on start (Skin.String bz_at_mmdef 1-13, empty = 1 Music)
        # t4315/t4316: Startup highlight (Skin.String bz_at_mmdef 1 Music / 2 Movies / 3 TV Shows; empty = 3 TV Shows)
        _secs = ['music', 'movies', 'tv']
        try: _r = min(max(int(xbmc.getInfoLabel('Skin.String(bz_at_mmdef)') or '3'), 1), 3) - 1
        except Exception: _r = 2
        home.setProperty('bz_mmstartrow', str(_r)); home.setProperty('bz_mmstartsec', _secs[_r])
        home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')
    if xbmc.getCondVisibility('Window.IsActive(music)') and xbmc.getInfoLabel('Container.FolderPath') == path: pass
    else:
        xbmc.executebuiltin('ActivateWindow(Music,musicdb://)')
        for _ in range(60):
            if xbmc.getCondVisibility('Window.IsActive(music)') and xbmc.getInfoLabel('Container.FolderPath') == 'musicdb://': break
            xbmc.Monitor().waitForAbort(0.05)
        xbmc.executebuiltin('Container.Update(%s)' % path)
    if first:
        # 4.7 Music-start: Kodi start = the default section (Music) with the Main menu open over it (section parent group dimmed, BezelSecDim).
        # Opened once the splash is done so the menu fade is seen; bz_flip moves the focus to the strip (6996, current section row).
        # 4.7.6 (Rob): Main menu must show before Music. bz_nav is now set as soon as the music window is up (under the splash),
        # not after bz_splash_done, so the splash fades straight onto the Main menu instead of Music first, menu ~later.
        for _ in range(300):
            if xbmc.getCondVisibility('Window.IsActive(music)') or xbmc.Monitor().abortRequested(): break
            xbmc.Monitor().waitForAbort(0.05)
        if xbmc.getCondVisibility('!Skin.HasSetting(bz_nomenustart) + Window.IsActive(music)') and not home.getProperty('bz_nav'):
            home.setProperty('bz_nav', 'true')
        for _ in range(240):
            if home.getProperty('bz_splash_done') == '1' or xbmc.Monitor().abortRequested(): break
            xbmc.Monitor().waitForAbort(0.05)
        # 4.7.8+ MM-start: re-assert the menu once the splash is done (an early close under the splash left Music showing)
        if xbmc.getCondVisibility('!Skin.HasSetting(bz_nomenustart) + Window.IsActive(music)') and not home.getProperty('bz_nav'):
            home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')
        xbmc.Monitor().waitForAbort(6); home.clearProperty('bz_startfade')
    sys.exit(0)
# 5.0.2 Choose art (Rob t3826): art types IN the colour strip, shaped thumbnail grid over the fanart (DialogSelect via bz_artsel)
if action == 'chooseart':
    CAK = {'movie': 'movieid', 'episode': 'episodeid', 'tvshow': 'tvshowid', 'musicvideo': 'musicvideoid', 'season': 'seasonid',
           'album': 'albumid', 'artist': 'artistid', 'song': 'songid'}
    CAS = {'movie': 'VideoLibrary.SetMovieDetails', 'episode': 'VideoLibrary.SetEpisodeDetails', 'tvshow': 'VideoLibrary.SetTVShowDetails',
           'musicvideo': 'VideoLibrary.SetMusicVideoDetails', 'season': 'VideoLibrary.SetSeasonDetails',
           'album': 'AudioLibrary.SetAlbumDetails', 'artist': 'AudioLibrary.SetArtistDetails', 'song': 'AudioLibrary.SetSongDetails'}
    def _shape(t):
        t = t.split('.')[-1]
        if t in ('fanart', 'banner', 'clearlogo', 'landscape', 'logo'): return 'wide'
        if t in ('poster', 'keyart'): return 'tall'
        return 'sq'
    if not dbid or dbtype not in CAK:
        xbmcgui.Dialog().notification('BEZEL', 'Not a library item', xbmcgui.NOTIFICATION_INFO, 2500); sys.exit(0)
    lib = 'AudioLibrary' if dbtype in ('album', 'artist', 'song') else 'VideoLibrary'
    item = {CAK[dbtype]: dbid}
    got = (rpc(lib + '.GetAvailableArtTypes', {'item': item}) or {}).get('availablearttypes') or []
    order = ['poster', 'fanart', 'thumb', 'clearlogo', 'landscape', 'banner', 'clearart', 'keyart', 'discart', 'cutout']
    types = [a for a in order if a in got] + [a for a in got if a not in order]
    if not types: types = ['thumb', 'fanart'] if lib == 'AudioLibrary' else (['poster', 'fanart'] if dbtype != 'episode' else ['thumb'])
    _gm = {'movie': 'Movie', 'episode': 'Episode', 'tvshow': 'TVShow', 'musicvideo': 'MusicVideo', 'season': 'Season', 'album': 'Album', 'artist': 'Artist', 'song': 'Song'}[dbtype]
    _d = rpc('%s.Get%sDetails' % (lib, _gm), dict(item, properties=['art'])) or {}
    _sa = (((list(_d.values())[0] if _d else {}) or {}).get('art') or {})  # t4251: freeze section art for the grid's right side (no focus preview)
    home.setProperty('bz_artsec', _sa.get('poster') or _sa.get('tvshow.poster') or _sa.get('thumb') or _sa.get('fanart') or '')
    home.setProperty('bz_arttitle', ((list(_d.values())[0] if _d else {}) or {}).get('label', '') or xbmc.getInfoLabel('ListItem.Label'))
    try:
        while True:
            home.setProperty('bz_artsel', 'types')
            i = xbmcgui.Dialog().select('Choose art', [t.capitalize() for t in types])
            if i < 0: break                     # Back on the type rows = leave Choose art
            t = types[i]
            av = (rpc(lib + '.GetAvailableArt', {'item': item, 'arttype': t}) or {}).get('availableart') or []
            if not av:
                xbmcgui.Dialog().notification('BEZEL', 'No %s artwork found' % t, xbmcgui.NOTIFICATION_INFO, 2000); continue
            items = []
            for a in av:
                li = xbmcgui.ListItem(a.get('arttype', t)); li.setArt({'thumb': a.get('previewurl') or a.get('url'), 'icon': a.get('previewurl') or a.get('url')}); items.append(li)
            home.setProperty('bz_artsel', _shape(t)); home.setProperty('bz_arttype', t.capitalize())
            home.clearProperty('bz_artback')
            j = xbmcgui.Dialog().select(t.capitalize(), items, useDetails=True)
            if home.getProperty('bz_artback'): j = -1   # Back always steps to the types, never applies
            if j < 0: continue                  # Back on the grid = step back to the type rows
            rpc(CAS[dbtype], {CAK[dbtype]: dbid, 'art': {t: av[j]['url']}})
            xbmc.executebuiltin('Container.Refresh')
            xbmcgui.Dialog().notification('BEZEL', '%s updated' % t.capitalize(), xbmcgui.NOTIFICATION_INFO, 2000)
            break
    finally:
        for k in ('bz_artsel', 'bz_arttype', 'bz_arttitle', 'bz_artback', 'bz_artsec'): home.clearProperty(k)
    sys.exit(0)
KEY = {'movie': 'movieid', 'episode': 'episodeid', 'tvshow': 'tvshowid', 'musicvideo': 'musicvideoid', 'season': 'seasonid'}
SETTER = {'movie': 'VideoLibrary.SetMovieDetails', 'episode': 'VideoLibrary.SetEpisodeDetails', 'tvshow': 'VideoLibrary.SetTVShowDetails',
          'musicvideo': 'VideoLibrary.SetMusicVideoDetails', 'season': 'VideoLibrary.SetSeasonDetails'}
def note(msg): xbmcgui.Dialog().notification('BEZEL', msg, xbmcgui.NOTIFICATION_INFO, 2500)
def episodes():
    p = {'properties': ['playcount']}
    if dbtype == 'tvshow': p['tvshowid'] = dbid
    elif dbtype == 'season':
        d = (rpc('VideoLibrary.GetSeasonDetails', {'seasonid': dbid, 'properties': ['tvshowid', 'season']}) or {}).get('seasondetails') or {}
        p['tvshowid'] = d.get('tvshowid', 0); p['season'] = d.get('season', 0)
    return (rpc('VideoLibrary.GetEpisodes', p) or {}).get('episodes') or []
if not dbid or dbtype not in KEY:
    note('Not a library item')
elif action in ('play', 'resume'):
    if dbtype in ('movie', 'episode', 'musicvideo'):
        rpc('Player.Open', {'item': {KEY[dbtype]: dbid}, 'options': {'resume': action == 'resume'}})
    else:  # show / season: play the first unwatched episode (or the first)
        eps = episodes()
        ep = next((e for e in eps if not e.get('playcount')), eps[0] if eps else None)
        if ep: rpc('Player.Open', {'item': {'episodeid': ep['episodeid']}, 'options': {'resume': True}})
elif action == 'refresh':
    m = {'movie': 'VideoLibrary.RefreshMovie', 'episode': 'VideoLibrary.RefreshEpisode', 'tvshow': 'VideoLibrary.RefreshTVShow',
         'musicvideo': 'VideoLibrary.RefreshMusicVideo'}
    if dbtype == 'season':
        d = (rpc('VideoLibrary.GetSeasonDetails', {'seasonid': dbid, 'properties': ['tvshowid']}) or {}).get('seasondetails') or {}
        r = rpc('VideoLibrary.RefreshTVShow', {'tvshowid': d.get('tvshowid', 0)})
    else:
        r = rpc(m[dbtype], {KEY[dbtype]: dbid, 'ignorenfo': False})
    note('Refreshing info' if r == 'OK' else 'Refresh failed')
elif action == 'art':
    art = (rpc('VideoLibrary.GetAvailableArtTypes', {'item': {KEY[dbtype]: dbid}}) or {}).get('availablearttypes') or []
    types = [a for a in ['poster', 'fanart', 'clearlogo', 'landscape', 'banner', 'thumb', 'clearart', 'keyart', 'discart'] if a in art] + [a for a in art if a not in
             ['poster', 'fanart', 'clearlogo', 'landscape', 'banner', 'thumb', 'clearart', 'keyart', 'discart']]
    if not types: types = ['poster', 'fanart'] if dbtype != 'episode' else ['thumb']
    i = xbmcgui.Dialog().select('Choose art type', [t.capitalize() for t in types])
    if i >= 0:
        t = types[i]
        av = (rpc('VideoLibrary.GetAvailableArt', {'item': {KEY[dbtype]: dbid}, 'arttype': t}) or {}).get('availableart') or []
        items = []
        for a in av:
            li = xbmcgui.ListItem(a.get('arttype', t)); li.setArt({'thumb': a.get('previewurl') or a.get('url')}); items.append(li)
        if not items:
            note('No %s artwork found' % t)
        else:
            j = xbmcgui.Dialog().select('Choose %s' % t, items, useDetails=True)
            if j >= 0:
                rpc(SETTER[dbtype], {KEY[dbtype]: dbid, 'art': {t: av[j]['url']}})
                xbmc.executebuiltin('Container.Refresh'); note('%s updated' % t.capitalize())
elif action == 'watched':
    if dbtype in ('movie', 'episode', 'musicvideo'):
        d = (rpc('VideoLibrary.Get%sDetails' % {'movie': 'Movie', 'episode': 'Episode', 'musicvideo': 'MusicVideo'}[dbtype],
                 {KEY[dbtype]: dbid, 'properties': ['playcount']}) or {})
        pc = (list(d.values())[0] if d else {}).get('playcount', 0)
        rpc(SETTER[dbtype], {KEY[dbtype]: dbid, 'playcount': 0 if pc else 1})
        note('Marked unwatched' if pc else 'Marked watched')
    else:
        eps = episodes(); allw = eps and all(e.get('playcount') for e in eps)
        for e in eps: rpc('VideoLibrary.SetEpisodeDetails', {'episodeid': e['episodeid'], 'playcount': 0 if allw else 1})
        note('Marked unwatched' if allw else 'Marked watched')
    xbmc.executebuiltin('Container.Refresh')
