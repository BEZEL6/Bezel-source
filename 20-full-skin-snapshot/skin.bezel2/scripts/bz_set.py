# 5.33.215 Settings (MM style, dialog 1130): expand toggle, sub-page, cycle pills via JSON-RPC, open stock pages.
import sys, json, xbmc, xbmcgui
home = xbmcgui.Window(10000)
ENUM = {'myvideos.selectaction': [(0, 'CHOOSE'), (1, 'PLAY'), (2, 'RESUME'), (3, 'INFO')],
        'general.addonupdates': [(0, 'AUTO'), (1, 'NOTIFY'), (2, 'NEVER')],
        # 5.33.241 SYSTEM Warm pages
        'videoplayer.adjustrefreshrate': [(0, 'OFF'), (1, 'START/STOP'), (2, 'ON START')],
        'audiooutput.guisoundmode': [(0, 'NEVER'), (1, 'IDLE'), (2, 'ALWAYS')],
        'audiooutput.streamsilence': [(0, 'OFF'), (1, '1 MIN'), (2, '2 MIN'), (5, '5 MIN'), (10, '10 MIN'), (-1, 'ALWAYS')]}
NUM = {'audiooutput.volumesteps': (10, 100, 10, ''), 'powermanagement.displaysoff': (0, 120, 5, ' MIN'),
       'powermanagement.shutdowntime': (0, 240, 15, ' MIN'),
       'lookandfeel.skinzoom': (-20, 20, 2, '%'), 'screensaver.time': (1, 60, 1, ' MIN')}   # 5.33.242   # (min, max, step, suffix) — 0 shows OFF
SYSP = ['videoplayer.adjustrefreshrate', 'videoplayer.usedisplayasclock', 'audiooutput.passthrough', 'audiooutput.guisoundmode',
        'audiooutput.streamsilence', 'audiooutput.volumesteps', 'input.enablemouse', 'input.enablejoystick',
        'powermanagement.displaysoff', 'powermanagement.shutdowntime', 'debug.showloginfo', 'eventlog.enabled',
        'lookandfeel.skinzoom', 'screensaver.time', 'gamesgeneral.enable', 'gamesgeneral.showosdhelp']   # 5.33.242 SKIN/SCREENSAVER/GAMES
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
    elif s in NUM and isinstance(v, int): t = 'OFF' if v == 0 and s.startswith('power') else '%d%s' % (v, NUM[s][3])
    else: t = '' if v is None else str(v).upper()
    home.setProperty('bz_set_' + s.replace('.', '_'), t)
# 5.33.331 generic pills: any Kodi setting cycles from its own definition (options / min-max-step)
try:
    from bz_set_pages import GENP
except Exception:
    GENP = []
_META = {}
def meta():
    if not _META:
        r = rpc('Settings.GetSettings', {'level': 'expert'}) or {}
        for d in r.get('settings') or []: _META[d['id']] = d
    return _META
def gshow(s, v):
    d = meta().get(s) or {}
    o = d.get('options')
    if isinstance(v, bool): t = 'ON' if v else 'OFF'
    elif isinstance(o, list) and o: t = next((str(x.get('label')) for x in o if x.get('value') == v), str(v))
    elif d.get('type') == 'addon': t = (v or 'NONE').split('.')[-1]
    else: t = '' if v is None else str(v)
    t = t.upper()
    home.setProperty('bz_set_' + s.replace('.', '_'), t if len(t) <= 10 else t[:9] + '…')
def gcyc(s, d):
    m = meta().get(s) or {}; v = m.get('value'); o = m.get('options')
    if isinstance(v, bool): nv = not v
    elif isinstance(o, list) and o:
        ks = [x.get('value') for x in o]; nv = ks[(ks.index(v) + d) % len(ks)] if v in ks else ks[0]
    elif m.get('type') == 'integer' and m.get('maximum', 0) > m.get('minimum', 0):
        lo, hi, st = m['minimum'], m['maximum'], m.get('step', 1) or 1; nv = v + d * st
        nv = lo if nv > hi else (hi if nv < lo else nv)
    else: return
    rpc('Settings.SetSettingValue', {'setting': s, 'value': nv}); _META.clear(); gshow(s, get(s))
def load():
    for s in PILLS + SYSP: show(s, get(s))
    for s in GENP:
        if s not in PILLS + SYSP: gshow(s, meta().get(s, {}).get('value'))
TXT = ['services.devicename']   # 5.33.340 text settings: never cycle (edit via keyboard)
def cyc(s, d):
    if s in TXT: return
    if s not in ENUM and s not in NUM and s not in BTXT and s in GENP and not isinstance(get(s), bool): return gcyc(s, d)
    v = get(s)
    if isinstance(v, bool): nv = not v
    elif s in ENUM:
        ks = [k for k, _ in ENUM[s]]; nv = ks[(ks.index(v) + d) % len(ks)] if v in ks else ks[0]
    elif s in NUM and isinstance(v, int):
        lo, hi, st, _ = NUM[s]; nv = v + d * st
        nv = lo if nv > hi else (hi if nv < lo else nv)
    else: return
    rpc('Settings.SetSettingValue', {'setting': s, 'value': nv}); show(s, get(s))
    if s == 'videolibrary.backgroundupdate': rpc('Settings.SetSettingValue', {'setting': 'musiclibrary.backgroundupdate', 'value': nv})
a = sys.argv[1:]
if not a or a[0] == 'load': load()
elif a[0] == 'x':
    home.setProperty('bz_setx', '' if home.getProperty('bz_setx') == a[1] else a[1])
elif a[0] == 'pg':
    home.setProperty('bz_setpg', a[1]); home.setProperty('bz_setpgt', a[2] if len(a) > 2 else a[1]); load()
    lid = 9131 if a[1] == 'services' else 9132   # 5.33.241/242: every other sub-page (SYSTEM subs, profiles, sysinfo, skin, screensaver, games) on 9132
    for _ in range(20):   # list only becomes focusable after the visibility flip renders
        xbmc.sleep(30); xbmc.executebuiltin('SetFocus(%d,0,absolute)' % lid)
        if xbmc.getCondVisibility('Control.HasFocus(%d)' % lid): break
elif a[0] == 'pgback':   # Back on a sub-page: back to the home list on the opener row (SERVICES)
    if home.getProperty('bz_setpg') in ('upnp', 'control', 'airplay', 'smb', 'weather', 'caching'):
        # 5.33.349 t2493: SERVICES sub-pages return to the SERVICES page (9131) on the opener row
        home.setProperty('bz_setpg', 'services'); home.setProperty('bz_setpgt', 'services')
        for _ in range(20):
            xbmc.sleep(30); xbmc.executebuiltin('SetFocus(9131)')
            if xbmc.getCondVisibility('Control.HasFocus(9131)'): break
        sys.exit()
    home.setProperty('bz_setpg', ''); home.setProperty('bz_setpgt', '')
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
# ---- 5.33.337 Rob t2458: ADD SOURCE straight from the strip ----
# Opens the section's sources:// list, selects its "Add …" item (path 'add') so Kodi's
# Add Source dialog comes up at once, then returns to Media Sources 1117 on ADD SOURCE.
def msadd(k):
    mon = xbmc.Monitor()
    win, path = {'m': ('Music', 'sources://music/'), 'p': ('Pictures', 'sources://pictures/')}.get(k, ('Videos', 'sources://video/'))
    home.setProperty('bz_msfocus', '7130'); home.setProperty('bz_msadd', '1')
    xbmc.executebuiltin('ActivateWindow(%s,%s,return)' % (win, path))
    for _ in range(60):
        if xbmc.getCondVisibility('Window.IsActive(%s) + String.IsEqual(Container.FolderPath,%s) + Integer.IsGreater(Container(60).NumItems,0)' % (win, path)): break
        xbmc.sleep(50)
    n = int(xbmc.getInfoLabel('Container(60).NumItems') or 0)
    hit = False
    for i in range(n, -1, -1):
        xbmc.executebuiltin('SetFocus(60,%d,absolute)' % i); xbmc.sleep(40)
        if xbmc.getInfoLabel('Container(60).ListItem.FolderPath') == 'add':
            xbmc.executebuiltin('Action(select)'); hit = True; break
    if hit:
        for _ in range(60):
            if xbmc.getCondVisibility('System.HasActiveModalDialog'): break
            xbmc.sleep(50)
        while not mon.abortRequested() and xbmc.getCondVisibility('System.HasActiveModalDialog | Window.IsActive(filebrowser)'):
            xbmc.sleep(150)
    home.clearProperty('bz_msadd')
    if mon.abortRequested() or home.getProperty('bz_nav'): return
    if xbmc.getCondVisibility('Window.IsActive(%s)' % win):
        home.clearProperty('bz_msret'); xbmc.executebuiltin('ActivateWindow(1117)')
if a and a[0] == 'msadd': msadd(a[1] if len(a) > 1 else 'v')
# 5.33.339 t2458: SERVICES DEVICE NAME — Warm text edit (Bezel strip keyboard) instead of stock Settings/Services
def dname():
    s = 'services.devicename'; v = get(s) or ''
    n = xbmcgui.Dialog().input('DEVICE NAME', v)
    if n and n != v:
        rpc('Settings.SetSettingValue', {'setting': s, 'value': n})
    show(s, get(s))
    xbmc.executebuiltin('SetFocus(9131)')
if a and a[0] == 'dname': dname()
