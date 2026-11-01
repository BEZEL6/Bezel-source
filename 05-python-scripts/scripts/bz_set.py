# 5.33.215 Settings (MM style, dialog 1130): expand toggle, sub-page, cycle pills via JSON-RPC, open stock pages.
import sys, json, xbmc, xbmcgui
home = xbmcgui.Window(10000)
ENUM = {'myvideos.selectaction': [(0, 'CHOOSE'), (1, 'PLAY'), (2, 'RESUME'), (3, 'INFO')],
        'general.addonupdates': [(0, 'AUTO'), (1, 'NOTIFY'), (2, 'NEVER')]}
BTXT = {'videolibrary.backgroundupdate': ('QUIET', 'SHOW')}   # 5.33.220 LIBRARY SCAN pill
ADP = ['general.addonupdates', 'general.addonnotifications', 'addons.unknownsources']
MSP = ['videolibrary.updateonstartup', 'musiclibrary.updateonstartup', 'videolibrary.backgroundupdate']
PILLS = ['filelists.showextensions', 'filelists.ignorethewhensorting', 'myvideos.selectaction', 'filelists.showhidden',
         'videolibrary.updateonstartup', 'musiclibrary.updateonstartup', 'lookandfeel.enablerssfeeds', 'screensaver.usedimonpause',
         'services.upnp', 'services.webserver', 'services.esenabled', 'services.airplay', 'services.zeroconf', 'services.devicename']
def rpc(m, p):
    r = json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': m, 'params': p})))
    return r.get('result')
def get(s):
    r = rpc('Settings.GetSettingValue', {'setting': s}); return None if r is None else r.get('value')
def show(s, v):
    if s in BTXT and isinstance(v, bool): t = BTXT[s][0 if v else 1]
    elif isinstance(v, bool): t = 'ON' if v else 'OFF'
    elif s in ENUM: t = dict(ENUM[s]).get(v, str(v))
    else: t = '' if v is None else str(v).upper()
    home.setProperty('bz_set_' + s.replace('.', '_'), t)
def load():
    for s in PILLS: show(s, get(s))
def cyc(s, d):
    v = get(s)
    if isinstance(v, bool): nv = not v
    elif s in ENUM:
        ks = [k for k, _ in ENUM[s]]; nv = ks[(ks.index(v) + d) % len(ks)] if v in ks else ks[0]
    else: return
    rpc('Settings.SetSettingValue', {'setting': s, 'value': nv}); show(s, get(s))
    if s == 'videolibrary.backgroundupdate': rpc('Settings.SetSettingValue', {'setting': 'musiclibrary.backgroundupdate', 'value': nv})
a = sys.argv[1:]
if not a or a[0] == 'load': load()
elif a[0] == 'x':
    home.setProperty('bz_setx', '' if home.getProperty('bz_setx') == a[1] else a[1])
elif a[0] == 'pg':
    home.setProperty('bz_setpg', a[1]); load()
    for _ in range(20):   # list 9131 only becomes focusable after the visibility flip renders
        xbmc.sleep(30); xbmc.executebuiltin('SetFocus(9131,0,absolute)')
        if xbmc.getCondVisibility('Control.HasFocus(9131)'): break
elif a[0] == 'pgback':   # Back on a sub-page: back to the home list on the opener row (SERVICES)
    home.setProperty('bz_setpg', '')
    for _ in range(20):
        xbmc.sleep(30); xbmc.executebuiltin('SetFocus(9130)')   # 9130 keeps its selected row (SERVICES) while hidden
        if xbmc.getCondVisibility('Control.HasFocus(9130)'): break
elif a[0] == 'cyc': cyc(a[1], int(a[2]) if len(a) > 2 else 1)
elif a[0] == 'go':
    # 1130 is a modal dialog: Kodi ignores ActivateWindow while it is open.
    # Close it, open the stock page, then reopen BEZEL Settings on Back
    # (section/Warm/poster stay loaded underneath the whole time).
    mon = xbmc.Monitor()
    xbmc.executebuiltin('Dialog.Close(1130,true)')
    xbmc.sleep(50)
    xbmc.executebuiltin('ActivateWindow(%s)' % a[1])
    w = a[1]
    for _ in range(40):
        if xbmc.getCondVisibility('Window.IsActive(%s)' % w): break
        xbmc.sleep(50)
    while not mon.abortRequested() and xbmc.getCondVisibility('Window.IsActive(%s)' % w):
        xbmc.sleep(150)
    # let the section finish its onload (it restores the MM / bz_nav) before reopening
    xbmc.sleep(600)
    if not mon.abortRequested() and not xbmc.getCondVisibility('Window.IsActive(fullscreenvideo) | System.HasActiveModalDialog'):
        xbmc.executebuiltin('ClearProperty(bz_nav,home)')
        xbmc.executebuiltin('ActivateWindow(1130)')

# ---- 5.33.220 Add-ons 1131 / Media Sources 1117 (Warm strip) ----
def _n(p):
    r = rpc('Addons.GetAddons', p) or {}
    return str(len(r.get('addons') or []))
def adload():
    for k in ADP: show(k, get(k))
    if not home.getProperty('bz_adx_seen'):
        home.setProperty('bz_adx_seen', '1'); home.setProperty('bz_adx', 'my')
    for k, p in (('video', {'content': 'video', 'enabled': 'all'}), ('audio', {'content': 'audio', 'enabled': 'all'}),
                 ('exec', {'content': 'executable', 'enabled': 'all'}), ('svc', {'type': 'xbmc.service', 'enabled': 'all'}),
                 ('skin', {'type': 'xbmc.gui.skin', 'enabled': 'all'}), ('all', {'enabled': 'all'})):
        home.setProperty('bz_ad_n_' + k, _n(p))
def msload():
    for k in MSP: show(k, get(k))
    if not home.getProperty('bz_msx_seen'):
        home.setProperty('bz_msx_seen', '1')
        if not home.getProperty('bz_msx'): home.setProperty('bz_msx', 'v')
    for m in ('video', 'music', 'pictures'):
        r = rpc('Files.GetSources', {'media': m}) or {}
        home.setProperty('bz_ms_n_' + m, str(len(r.get('sources') or [])))
def _reopen(under, dlg='1131'):
    # reopen the strip only when we came back to the same window and nothing else took over
    # (MM pick of another section, plugin launch, fullscreen, modal)
    xbmc.sleep(400)
    if xbmc.getCondVisibility('Window.IsActive(fullscreenvideo) | System.HasActiveModalDialog | String.StartsWith(Container.FolderPath,plugin://) | !String.IsEmpty(Window(Home).Property(bz_nav))'): return
    if xbmcgui.getCurrentWindowId() != under: return
    xbmc.executebuiltin('ActivateWindow(%s)' % dlg)
def ago(path):
    # » new strip menu: addonbrowser (Warm strip list 60) at path, Back at that path returns here
    mon = xbmc.Monitor(); under = xbmcgui.getCurrentWindowId()
    home.setProperty('bz_adgo', '1')
    xbmc.executebuiltin('Dialog.Close(1131,true)'); xbmc.sleep(50)
    xbmc.executebuiltin('ActivateWindow(addonbrowser,%s,return)' % path)
    for _ in range(40):
        if xbmc.getCondVisibility('Window.IsActive(addonbrowser)'): break
        xbmc.sleep(50)
    while not mon.abortRequested() and xbmc.getCondVisibility('Window.IsActive(addonbrowser)'):
        xbmc.sleep(150)
    home.clearProperty('bz_adgo')
    if not mon.abortRequested(): _reopen(under)
def azip():
    # FROM ZIP FILE: Kodi file browser picks the zip (File manager stays stock), then back to the strip
    mon = xbmc.Monitor(); under = xbmcgui.getCurrentWindowId()
    xbmc.executebuiltin('Dialog.Close(1131,true)'); xbmc.sleep(50)
    xbmc.executebuiltin('InstallFromZip')
    for _ in range(60):
        if xbmc.getCondVisibility('System.HasActiveModalDialog | Window.IsActive(filebrowser)'): break
        xbmc.sleep(50)
    n = 0
    while not mon.abortRequested() and n < 2400 and xbmc.getCondVisibility('System.HasActiveModalDialog | Window.IsActive(filebrowser) | Window.IsActive(busydialog)'):
        xbmc.sleep(150); n += 1
    if not mon.abortRequested(): _reopen(under)
if a and a[0] == 'adload': adload()
elif a and a[0] == 'msload': msload()
elif a and a[0] == 'x2':   # generic ▾ toggle: x2,<prop>,<grp>
    home.setProperty(a[1], '' if home.getProperty(a[1]) == a[2] else a[2])
elif a and a[0] == 'ago': ago(','.join(a[1:]))
elif a and a[0] == 'azip': azip()
