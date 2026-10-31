# BEZEL 2.0 BETA 2.8: double-tap Select = context menu (Rob, Samsung Frame CEC remote: a held button arrives as repeats, so long-press never fires).
# Service (one instance, guard bz_dtap_running). While it runs and Skin setting bz_dtap_off is NOT set it installs
# special://profile/keymaps/zz_bezel2_dtap.xml, which sends Select in Home / Music / Videos (windows only, never dialogs, keyboard, OSD or
# fullscreen video) as NotifyAll(bz,bz_sel). One tap -> Action(Select) once the window (tuner bz_at_dtapwin, 200-500 ms, default 300) has passed;
# a second tap inside the window -> Action(Info) = BEZEL Options+Info (t4004: old ContextMenu path removed). The keymap is removed when the setting is off or Kodi exits, so Select can never go dead.
import xbmc, xbmcgui, xbmcvfs, time, threading, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bz_km   # 5.33.194 keymap quarantine
home = xbmcgui.Window(10000)
SECW = ('pictures', 'programs', 'games', 'addonbrowser', 'musicplaylist', 'videoplaylist', 'tvchannels', 'radiochannels', 'tvguide', 'radioguide', 'tvrecordings', 'radiorecordings', 'tvtimers', 'radiotimers', 'tvtimerrules', 'radiotimerrules', 'tvsearch', 'radiosearch')   # 5.33.18 t203
DST = 'special://profile/keymaps/zz_bezel2_dtap.xml'
SEL = 'NotifyAll(bz,bz_sel)'
KM = ('<?xml version="1.0" encoding="UTF-8"?>\n<!-- written by BEZEL bz_dtap.py (double-tap Select = context menu); deleted when off -->\n<keymap>\n' +
      ''.join('\t<%s>\n\t\t<keyboard><return>%s</return><enter>%s</enter><return mod="longpress">%s</return><enter mod="longpress">%s</enter></keyboard>\n\t\t<remote><select>%s</select><select mod="longpress">%s</select></remote>\n\t</%s>\n' % (w, SEL, SEL, SEL, SEL, SEL, SEL, w)
              for w in (('home', 'music', 'videos', 'filebrowser', 'filemanager') + SECW)) + '</keymap>\n')   # 5.33.144: filemanager dtap -> ContextMenu (match filebrowser 5.33.99). 5.33.99 t625: filebrowser. 5.33.17 t196: Pictures = section Info
# 5.33.18 t203: section info/context menu (Custom 1119) for the other content sections
SECW = ('pictures', 'programs', 'games', 'addonbrowser', 'musicplaylist', 'videoplaylist', 'tvchannels', 'radiochannels', 'tvguide', 'radioguide',
        'tvrecordings', 'radiorecordings', 'tvtimers', 'radiotimers', 'tvtimerrules', 'radiotimerrules', 'tvsearch', 'radiosearch')
SECC = ' | '.join('Window.IsActive(%s)' % w for w in SECW)
def info():
    # Movies/TV/Music/Pics -> Action(Info) (Options+Info); other sections -> their section menu 1119
    if xbmc.getCondVisibility('Window.IsActive(filebrowser) | Window.IsActive(filemanager)'): xbmc.executebuiltin('Action(ContextMenu)'); return   # 5.33.144: filemanager + filebrowser dtap -> context popup
    if xbmc.getCondVisibility('[%s] + !Window.IsActive(1119)' % SECC): xbmc.executebuiltin('ActivateWindow(1119)')
    else: xbmc.executebuiltin('Action(Info)')
NOCTX = 'special://profile/keymaps/zz_bezel2_noctx.xml'   # t4005: old Kodi context menu can never open in library windows (dtap ON or OFF)
NK = ('<?xml version="1.0" encoding="UTF-8"?>\n<!-- written by BEZEL bz_dtap.py: context menu keys -> Options+Info -->\n<keymap>\n' +
      ''.join('\t<%s>\n\t\t<keyboard><c>NotifyAll(bz,bz_ctx)</c><menu>NotifyAll(bz,bz_ctx)</menu></keyboard>\n\t\t<remote><title>NotifyAll(bz,bz_ctx)</title><contextmenu>NotifyAll(bz,bz_ctx)</contextmenu><menu>NotifyAll(bz,bz_ctx)</menu></remote>\n\t\t<mouse><rightclick>NotifyAll(bz,bz_ctx)</rightclick><longclick>NotifyAll(bz,bz_ctx)</longclick></mouse>\n\t</%s>\n' % (w, w)
              for w in (('home', 'music', 'videos') + SECW)) +   # 5.33.17: C/menu/rightclick -> Info in Pictures too
      # 5.33.11: Settings sub-list Back -> parent category list (bz_dtap service decides; Kodi ignores onback on grouplist children)
      ''.join('\t<%s>\n\t\t<keyboard><backspace>NotifyAll(bz,bz_setback)</backspace></keyboard>\n\t\t<remote><back>NotifyAll(bz,bz_setback)</back></remote>\n\t</%s>\n' % (w, w)
              for w in ('systemsettings', 'servicesettings', 'pvrsettings', 'playersettings', 'mediasettings', 'interfacesettings', 'gamesettings')) + '</keymap>\n')
def noctx():
    try:
        f = xbmcvfs.File(NOCTX); cur = f.read(); f.close()
    except Exception: cur = ''
    if cur != NK:
        if not xbmcvfs.exists('special://profile/keymaps/'): xbmcvfs.mkdirs('special://profile/keymaps/')
        f = xbmcvfs.File(NOCTX, 'w'); f.write(NK.encode()); f.close(); xbmc.executebuiltin('Action(reloadkeymaps)')
STEPS = [150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600]
def win():
    try: return STEPS[int(xbmc.getInfoLabel('Skin.String(bz_at_dtapwin)')) - 1] / 1000.0
    except Exception: return 0.3
def install(on):
    have = xbmcvfs.exists(DST)
    if on and have and not st.get('fresh'):
        st['fresh'] = True; xbmcvfs.delete(DST); have = False   # t4004: always rewrite once (longpress select -> ContextMenu override)
    if on and not have:
        if not xbmcvfs.exists('special://profile/keymaps/'): xbmcvfs.mkdirs('special://profile/keymaps/')
        f = xbmcvfs.File(DST, 'w'); f.write(KM.encode()); f.close(); xbmc.executebuiltin('Action(reloadkeymaps)')
        xbmc.log('BEZEL dtap: keymap installed', xbmc.LOGINFO)
    elif not on and have:
        xbmcvfs.delete(DST); xbmc.executebuiltin('Action(reloadkeymaps)'); xbmc.log('BEZEL dtap: keymap removed', xbmc.LOGINFO)
def reload_tuned(force=False):
    # BETA 2.9: write the fixed-time tuner steps into the skin files (bz_tune_patch), reload, then put the music / video window back on
    # the folder it showed (ReloadSkin re-opens the window at its root)
    try:
        import bz_tune_patch; ch = bz_tune_patch.patch(xbmc.getInfoLabel)
    except Exception as e:
        ch = False; xbmc.log('BEZEL tuner patch error: %s' % e, xbmc.LOGWARNING)
    if not ch:
        # 3.0.2 slide-menu freeze fix: nothing on disk changed (Slide menu / Music / look rows are live skin-string conditions),
        # so no ReloadSkin. A reload here re-built the window while keys were still arriving and could leave bz_nav=true
        # with the slide menu invisible and holding focus (screen looks frozen, music plays on).
        if not force: pass  # t4644 Rob: no Tuner popup   # t4226 applied card A + logo spin
        return
    mmst = home.getProperty('bz_mmstart') or force   # t4064: no splash -> startup reload must keep MM-first bz_nav. 4.7.12 K23: startup patch+ReloadSkin under the splash wiped the MM-first bz_nav (Music showed first)
    for pr in (() if mmst else ('bz_nav',)) + ('bz_navtune', 'bz_navset', 'bz_navset2', 'bz_navsub', 'bz_navnp', 'bz_navcard2', 'bz_navlock', 'bz_kset'):
        home.clearProperty(pr)   # 3.0.2: the reloaded skin always starts with the slide menu closed
    w = 'music' if xbmc.getCondVisibility('Window.IsActive(music)') else 'videos' if xbmc.getCondVisibility('Window.IsActive(videos)') else ''
    path = xbmc.getInfoLabel('Container.FolderPath') if w else ''
    pos = xbmc.getInfoLabel('Container(60).CurrentItem') if w else ''
    xbmc.executebuiltin('ReloadSkin()')
    if not force: pass  # t4644 Rob: no Tuner popup   # t4226 applied card A + logo spin   # BEZEL 3.0 toast
    if w and path:
        for _ in range(40):
            xbmc.sleep(100)
            if xbmc.getCondVisibility('Window.IsActive(%s) + !Window.IsActive(1113)' % w): break
        xbmc.sleep(300)
        if xbmc.getInfoLabel('Container.FolderPath') != path:
            xbmc.executebuiltin('Container.Update(%s)' % path)
            if pos.isdigit() and int(pos) > 1:
                for _ in range(30):
                    xbmc.sleep(100)
                    if xbmc.getInfoLabel('Container.FolderPath') == path: break
                xbmc.executebuiltin('SetFocus(60,%d,absolute)' % (int(pos) - 1))
st = {'t0': 0.0, 'pend': False, 'ctx': ''}
def ctx():
    # BEZEL 3.0: focus fingerprint; a pending Select is only sent if nothing moved / opened meanwhile (no stray delayed Select)
    return '%s|%s|%s' % (xbmcgui.getCurrentWindowId(), xbmcgui.getCurrentWindowDialogId(), xbmc.getInfoLabel('System.CurrentControlId'))
lock = threading.Lock()
class M(xbmc.Monitor):
    def onNotification(self, sender, method, data):
        if method.endswith('bz_setback'):   # 5.33.11: Settings Back - sub-list (grouplist 5) -> parent category list 3, else normal Back
            xbmc.executebuiltin('SetFocus(3)' if xbmc.getCondVisibility('ControlGroup(5).HasFocus()') else 'Action(Back)'); return
        if method.endswith('bz_ctx'):   # t4005: context key -> Options+Info (never old ContextMenu / xinfo)
            # oct27d: old context may already be open (RPC action / longpress): close it first (onload Dialog.Close is ignored by Kodi), then Info
            for i in range(40):
                if not xbmc.getCondVisibility('Window.IsActive(contextmenu)'): break
                xbmc.executebuiltin('Dialog.Close(contextmenu,true)'); xbmc.sleep(25)
            home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start(); return
        if not method.endswith('bz_sel'): return
        with lock:
            t = time.time()
            if st['pend'] and t - st['t0'] < win():
                st['pend'] = False; home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start()   # 5.0.3 #5: double tap -> new combined Info+Context (skips xinfo), not old ContextMenu
            elif xbmc.getCondVisibility('Skin.HasSetting(bz_dtap_off)'):
                xbmc.executebuiltin('Action(Select)')
            else:
                st['pend'] = True; st['t0'] = t; st['ctx'] = ctx()   # BEZEL 3.0: remember where the tap landed
if home.getProperty('bz_dtap_running') != 'true':
    home.setProperty('bz_dtap_running', 'true')
    mon = M()
    noctx()
    reload_tuned(force=True)   # BETA 2.9: a skin update restores the stock files; re-apply the saved tuner steps (no reload when nothing changed)
    try:
        n = 0
        while not mon.abortRequested() and not home.getProperty('bz_quit'):   # BEZEL 3.0 exit fix
            with lock:
                if st['pend'] and time.time() - st['t0'] >= win():
                    st['pend'] = False
                    late = time.time() - st['t0'] > win() + 0.6
                    if not late and ctx() == st['ctx'] and not home.getProperty('bz_navlock'): xbmc.executebuiltin('Action(Select)')
                    else: xbmc.log('BEZEL dtap: pending Select dropped (focus/window changed)', xbmc.LOGINFO)
            n += 1
            if n % 5 == 0 and home.getProperty('bz_navtune') and home.getProperty('bz_nav') != 'true': home.clearProperty('bz_navtune')   # tuner card closes with the menu
            if n % 10 == 0 and home.getProperty('bz_tune_dirty') and home.getProperty('bz_nav') != 'true':   # BETA 2.8: apply tuner steps cleanly
                if st.get('dirty_t') is None: st['dirty_t'] = time.time()
                elif time.time() - st['dirty_t'] > 1.2:
                    st['dirty_t'] = None; home.clearProperty('bz_tune_dirty'); reload_tuned()
            if xbmc.getCondVisibility('Window.IsActive(contextmenu) + [Window.IsActive(home) | Window.IsActive(music) | Window.IsActive(videos) | Window.IsActive(pictures) | ' + SECC + '] + !Window.IsActive(1111) + !Window.IsActive(1112) + !Window.IsActive(1115)'):   # oct27d fix1: old context opened by a raw action (RPC/remote) -> Options+Info
                xbmc.executebuiltin('Dialog.Close(contextmenu,true)'); xbmc.sleep(40)
                if not xbmc.getCondVisibility('Window.IsActive(contextmenu)'):
                    home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start()
            if n % 5 == 0 and not xbmc.getCondVisibility('Window.IsVisible(movieinformation) | Window.IsVisible(musicinformation) | Window.IsVisible(songinformation) | Window.IsVisible(1111)'):   # 5.33.31 t265: mirror section stage fanart (9880 rotation) so Info stage draws the SAME image, not a second one
                f = xbmc.getInfoLabel('Control.GetLabel(9880)'); l = xbmc.getInfoLabel('ListItem.Label')
                if home.getProperty('bz_secfan') != f: home.setProperty('bz_secfan', f)
                if home.getProperty('bz_secfanlbl') != l: home.setProperty('bz_secfanlbl', l)
            if n % 25 == 1: install(not xbmc.getCondVisibility('Skin.HasSetting(bz_dtap_off)'))
            if n % 50 == 0 and not bz_km.on_bezel():   # 5.33.194 keymap quarantine: skin switched away -> remove all BEZEL keymaps
                bz_km.leave(); break
            if mon.waitForAbort(0.02): break
    finally:
        if not bz_km.on_bezel():   # 5.33.194: left Bezel (switch may also abort) -> remove all three keymaps
            try: bz_km.leave()
            except Exception: pass
            home.clearProperty('bz_dtap_running')
        elif not mon.abortRequested():   # BEZEL 3.0 exit fix: no Kodi calls while Kodi is shutting down (still on Bezel)
            try: install(False)
            except Exception: pass
            home.clearProperty('bz_dtap_running')
        if home.getProperty('bz_quit'): home.setProperty('bz_quit_dtap', 'true')
