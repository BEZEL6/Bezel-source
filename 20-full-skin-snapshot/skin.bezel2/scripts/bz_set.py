# 5.33.215 Settings (MM style, dialog 1130): expand toggle, sub-page, cycle pills via JSON-RPC, open stock pages.
import sys, json, xbmc, xbmcgui

# 5.33.432 CONFIRMFOCUS (Rob: "CONFIRM SKIN CHANGE POPUP HAS NO FOCUS ON THE LIST" - DialogConfirm is shared: keep-skin, remove, reset, sources...).
# Kodi sends SetFocus to the topmost MODAL dialog and UNFOCUSES its current control before looking up the id (GUIWindow GUI_MSG_SETFOCUS),
# so any SetFocus(60/6996/...) from a script while the Yes/No (or OK) is up left that dialog with no focus. Drop those while it is visible.
def _bz_fg_install(_x):
    if getattr(_x, '_bz_fg', False): return
    _eb = _x.executebuiltin
    def _safe(cmd, *a, **k):
        c = (cmd or '').lstrip().lower()
        if (c.startswith('setfocus(') or c.startswith('control.setfocus(')) and _x.getCondVisibility('Window.IsVisible(yesnodialog) | Window.IsVisible(okdialog)'):
            return None
        return _eb(cmd, *a, **k)
    try: _x.executebuiltin = _safe; _x._bz_fg = True
    except Exception: pass
_bz_fg_install(xbmc)
home = xbmcgui.Window(10000)
ENUM = {'myvideos.selectaction': [(0, 'CHOOSE'), (1, 'PLAY'), (2, 'RESUME'), (3, 'INFO')],
        'general.addonupdates': [(0, 'AUTO'), (1, 'NOTIFY'), (2, 'NEVER')],
        # 5.33.241 SYSTEM Warm pages
        'videoplayer.adjustrefreshrate': [(0, 'OFF'), (1, 'START/STOP'), (2, 'ON START')],
        'audiooutput.guisoundmode': [(0, 'NEVER'), (1, 'IDLE'), (2, 'ALWAYS')],
        'audiooutput.streamsilence': [(0, 'OFF'), (1, '1 MIN'), (2, '2 MIN'), (5, '5 MIN'), (10, '10 MIN'), (-1, 'ALWAYS')]}
NUM = {'audiooutput.volumesteps': (10, 100, 10, ''), 'powermanagement.displaysoff': (0, 120, 5, ' MIN'),
       'powermanagement.shutdowntime': (0, 240, 15, ' MIN'),
       'lookandfeel.skinzoom': (-20, 20, 2, '%'), 'screensaver.time': (1, 60, 1, ' MIN'),
       # 5.33.353 percent sliders (Kodi reports max 0 for these)
       'audiooutput.guisoundvolume': (0, 100, 10, '%'), 'subtitles.opacity': (0, 100, 10, '%'),
       'subtitles.bordersize': (0, 100, 5, '%'), 'subtitles.blur': (0, 100, 5, '%')}   # 5.33.242   # (min, max, step, suffix) — 0 shows OFF
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
    elif s in SECRET: t = '••••' if v else ''   # 5.33.353
    elif d.get('type') == 'list':
        lo = {x.get('value'): str(x.get('label')) for x in (d.get('definition') or {}).get('options') or []}
        t = ', '.join(lo.get(x, str(x)) for x in (v or [])) or 'NONE'
    elif d.get('type') == 'path': t = (v or 'NONE').rstrip('/\\').split('/')[-1].split('\\')[-1] or v
    elif 'dB' in str((d.get('control') or {}).get('formatlabel', '')) and isinstance(v, int): t = '%+d DB' % (v - 89)
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
    elif m.get('type') == 'addon' and m.get('addontype'):   # 5.33.351 addon pickers (navigation sounds) cycle installed add-ons
        r = rpc('Addons.GetAddons', {'type': m['addontype'], 'enabled': True}) or {}
        ks = ([''] if m.get('allowempty') else []) + [x['addonid'] for x in r.get('addons') or []]
        if not ks: return
        nv = ks[(ks.index(v) + d) % len(ks)] if v in ks else ks[0]
    else: return
    rpc('Settings.SetSettingValue', {'setting': s, 'value': nv}); _META.clear(); gshow(s, get(s))
def load():
    home.clearProperty('bz_skinpick')
    try: skinshow()
    except Exception: pass
    for s in PILLS + SYSP: show(s, get(s))
    for s in GENP:
        if s in NUM: show(s, get(s))   # 5.33.353
        elif s not in PILLS + SYSP: gshow(s, meta().get(s, {}).get('value'))
TXT = ['services.devicename']
SECRET = ['services.webserverpassword', 'services.airplaypassword', 'network.httpproxypassword', 'gamesachievements.password']   # 5.33.340 text settings: never cycle (edit via keyboard)
# 5.33.351 t2498 SKIN row: L/R picks among installed skins (label only), Select switches (Kodi asks keep/revert)
def _skins():
    r = rpc('Addons.GetAddons', {'type': 'xbmc.gui.skin', 'enabled': True, 'properties': ['name']}) or {}
    return [(x['addonid'], x.get('name') or x['addonid']) for x in r.get('addons') or []]
def skinshow():
    sk = _skins(); cur = home.getProperty('bz_skinpick') or get('lookandfeel.skin') or ''
    if cur not in [k for k, _ in sk]: cur = get('lookandfeel.skin') or ''
    home.setProperty('bz_skinpick', cur)
    n = dict(sk).get(cur, cur).upper(); n = n if len(n) <= 10 else n[:9] + '…'
    home.setProperty('bz_set_lookandfeel_skin', ('» ' if cur != get('lookandfeel.skin') else '') + n)
def skincyc(d):
    ks = [k for k, _ in _skins()]
    if not ks: return
    cur = home.getProperty('bz_skinpick') or get('lookandfeel.skin')
    home.setProperty('bz_skinpick', ks[(ks.index(cur) + d) % len(ks)] if cur in ks else ks[0]); skinshow()
def skinapply():
    pick = home.getProperty('bz_skinpick') or ''
    if not pick or pick == get('lookandfeel.skin'):
        ids = _skins()
        i = xbmcgui.Dialog().select('SKIN', [n for _, n in ids])
        if i < 0: return
        pick = ids[i][0]
        if pick == get('lookandfeel.skin'): return
    home.clearProperty('bz_skinpick')
    xbmc.executebuiltin('Dialog.Close(all,true)'); xbmc.sleep(150)
    rpc('Settings.SetSettingValue', {'setting': 'lookandfeel.skin', 'value': pick})
def cyc(s, d):
    if s in TXT: return
    if s == 'lookandfeel.skin': return skincyc(d)
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
elif a[0] == 'skinapply': skinapply()
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
def msadd(k, foc='7130'):
    mon = xbmc.Monitor()
    win, path = {'m': ('Music', 'sources://music/'), 'p': ('Pictures', 'sources://pictures/')}.get(k, ('Videos', 'sources://video/'))
    home.setProperty('bz_msfocus', foc); home.setProperty('bz_msadd', '1')
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
if a and a[0] == 'msadd': msadd(a[1] if len(a) > 1 and a[1] else 'v', a[2] if len(a) > 2 else '7130')
# 5.33.354 Rob t2513: CLEAN LIBRARY always asks Yes/No first (Videos + Music)
if a and a[0] == 'msclean':
    t = 'music' if len(a) > 1 and a[1] == 'music' else 'video'
    if xbmcgui.Dialog().yesno('CLEAN %s LIBRARY' % ('MUSIC' if t == 'music' else 'VIDEO'),
            'Removes library entries whose files or sources are missing.[CR]Continue?', nolabel='NO', yeslabel='YES'):
        xbmc.executebuiltin('CleanLibrary(%s)' % t)
# 5.33.339 t2458: SERVICES DEVICE NAME — Warm text edit (Bezel strip keyboard) instead of stock Settings/Services
def dname():
    s = 'services.devicename'; v = get(s) or ''
    n = xbmcgui.Dialog().input('DEVICE NAME', v)
    if n and n != v:
        rpc('Settings.SetSettingValue', {'setting': s, 'value': n})
    show(s, get(s))
    xbmc.executebuiltin('SetFocus(9131)')
if a and a[0] == 'dname': dname()

# ---- 5.33.353 t2505: MORE (KODI) rows pulled into Warm ----
# pick: Select on a text/path/multi-list/long-list setting -> Kodi keyboard / browser / select over 1130, write via RPC.
# act: Warm row that runs a Kodi tool (calibration, add-on settings, screensaver preview) and reopens 1130 after.
def _relist():
    lid = 9131 if home.getProperty('bz_setpg') == 'services' else 9132
    xbmc.executebuiltin('SetFocus(%d)' % lid)
def pick(s):
    m = meta().get(s) or {}; v = m.get('value'); t = m.get('type'); lab = str(m.get('label') or s).upper(); d = xbmcgui.Dialog(); nv = None
    if t == 'list':
        o = (m.get('definition') or {}).get('options') or []
        if o:
            r = d.multiselect(lab, [str(x.get('label')) for x in o], preselect=[i for i, x in enumerate(o) if x.get('value') in (v or [])])
            if r is not None: nv = [o[i].get('value') for i in r]
        else:
            r = d.input(lab, ', '.join(map(str, v or [])))
            if r is not None and r != '': nv = [x.strip() for x in r.split(',') if x.strip()]
    elif t == 'path':
        r = d.browse(0, lab, 'files', '', False, False, v or '')
        if r: nv = r
    elif t == 'addon':
        q = rpc('Addons.GetAddons', {'type': m.get('addontype'), 'enabled': True, 'properties': ['name']}) or {}
        ids = [(x['addonid'], x.get('name') or x['addonid']) for x in q.get('addons') or []]
        if ids:
            i = d.select(lab, [n for _, n in ids], preselect=[k for k, _ in ids].index(v) if v in [k for k, _ in ids] else -1)
            if i >= 0: nv = ids[i][0]
    elif isinstance(m.get('options'), list) and m['options']:
        o = m['options']; ks = [x.get('value') for x in o]
        i = d.select(lab, [str(x.get('label')) for x in o], preselect=ks.index(v) if v in ks else -1)
        if i >= 0: nv = ks[i]
    elif t in ('integer', 'number'):
        r = d.input(lab, str(v if v is not None else ''), type=xbmcgui.INPUT_ALPHANUM if t == 'number' else xbmcgui.INPUT_NUMERIC)
        try: nv = (float(r) if t == 'number' else int(r)) if r not in (None, '') else None
        except Exception: nv = None
    else:
        r = d.input(lab, '' if s in SECRET else (v or ''), option=xbmcgui.ALPHANUM_HIDE_INPUT if s in SECRET else 0)
        if r or (r == '' and s not in SECRET and v): nv = r
    if nv is not None and nv != v: rpc('Settings.SetSettingValue', {'setting': s, 'value': nv})
    _META.clear(); gshow(s, get(s)); _relist()
ACT = {'calib': ('ActivateWindow(screencalibration)', 'screencalibration'),
       'sspreview': ('ActivateScreensaver', 'screensaver'),
       'sssettings': ('Addon.OpenSettings(%s)', 'screensaver.mode'),
       'encsettings': ('Addon.OpenSettings(%s)', 'audiocds.encoder'),
       'wxsettings': ('Addon.OpenSettings(%s)', 'weather.addon')}
def act(k):
    if k not in ACT: return
    cmd, w = ACT[k]
    if '%s' in cmd:
        aid = get(w)
        if not aid: xbmcgui.Dialog().notification('BEZEL', 'NONE SELECTED', time=1500); return
        cmd = cmd % aid; w = 'addonsettings'
    mon = xbmc.Monitor()
    xbmc.executebuiltin('Dialog.Close(1130,true)'); xbmc.sleep(80)
    xbmc.executebuiltin(cmd)
    for _ in range(60):
        if xbmc.getCondVisibility('Window.IsActive(%s) | System.ScreenSaverActive' % w): break
        xbmc.sleep(50)
    while not mon.abortRequested() and xbmc.getCondVisibility('Window.IsActive(%s) | System.ScreenSaverActive | System.HasActiveModalDialog' % w):
        xbmc.sleep(150)
    xbmc.sleep(300)
    if not mon.abortRequested() and not xbmc.getCondVisibility('Window.IsActive(fullscreenvideo)'):
        xbmc.executebuiltin('ClearProperty(bz_nav,home)'); xbmc.executebuiltin('ActivateWindow(1130)')
if a and a[0] == 'pick': pick(a[1])
elif a and a[0] == 'act': act(a[1])

# ---- 5.33.364 Rob t2572: per-source dropdown in SOURCES 1132 (OPEN / RENAME / REMOVE / REFRESH) ----
def _srcctx(win, typ, path, want):
    # open <win> at sources://<typ>/, focus the source row, run Kodi's context entry whose label contains want
    xbmc.executebuiltin('ActivateWindow(%s,sources://%s/,return)' % (win, typ))
    for _ in range(60):
        if xbmc.getCondVisibility('Window.IsActive(%s) + String.IsEqual(Container.FolderPath,sources://%s/) + Integer.IsGreater(Container(60).NumItems,0)' % (win, typ)): break
        if _ == 30: xbmc.executebuiltin('Container.Update(sources://%s/)' % typ)
        xbmc.sleep(50)
    n = int(xbmc.getInfoLabel('Container(60).NumItems') or 0)
    for i in range(n + 1):
        xbmc.executebuiltin('SetFocus(60,%d,absolute)' % i); xbmc.sleep(40)
        if xbmc.getInfoLabel('Container(60).ListItem.FolderPath').rstrip('/') == path.rstrip('/'): break
    else:
        xbmc.log('BEZEL mssrc row not found %s' % path, xbmc.LOGWARNING); return False
    xbmc.executebuiltin('Action(ContextMenu)')
    xbmc.sleep(150)
    for _ in range(120):
        if xbmc.getCondVisibility('Window.IsActive(contextmenu)') and xbmc.getInfoLabel('Control.GetLabel(1000)') + xbmc.getInfoLabel('Control.GetLabel(1001)'): break
        xbmc.sleep(50)
    xbmc.log('BEZEL mssrc ctx open=%s labels=%s' % (xbmc.getCondVisibility('Window.IsActive(contextmenu)'), [xbmc.getInfoLabel('Control.GetLabel(%d)' % c) for c in range(996, 1012)]), xbmc.LOGWARNING)
    for cid in range(1000, 1040):
        if want in xbmc.getInfoLabel('Control.GetLabel(%d)' % cid).lower():
            xbmc.executebuiltin('SetFocus(%d)' % cid); xbmc.sleep(60); xbmc.executebuiltin('Action(select)'); return True
    xbmc.executebuiltin('Dialog.Close(contextmenu)'); return False
def _waitmodal(mon):
    for _ in range(40):
        if xbmc.getCondVisibility('System.HasActiveModalDialog'): break
        xbmc.sleep(50)
    while not mon.abortRequested() and xbmc.getCondVisibility('System.HasActiveModalDialog'): xbmc.sleep(150)
def _ctxpick(want):
    xbmc.sleep(150)
    for _ in range(80):
        if xbmc.getCondVisibility('Window.IsActive(contextmenu)'): break
        xbmc.sleep(50)
    xbmc.sleep(150)
    labs = [(c, xbmc.getInfoLabel('Control.GetLabel(%d)' % c)) for c in range(1000, 1040)]
    xbmc.log('BEZEL mssrc ctx %s' % [l for l in labs if l[1]], xbmc.LOGWARNING)
    for cid, l in labs:
        if want in l.lower():
            xbmc.executebuiltin('SetFocus(%d)' % cid); xbmc.sleep(60); xbmc.executebuiltin('Action(select)'); return True
    xbmc.executebuiltin('Dialog.Close(contextmenu)'); return False
def mssrc(act):
    mon = xbmc.Monitor()
    win = home.getProperty('bz_srcwin') or 'Videos'; path = home.getProperty('bz_srcsel'); name = home.getProperty('bz_srcname')
    typ = {'Music': 'music', 'Pictures': 'pictures'}.get(win, 'video')
    if act == 'refresh':
        if typ != 'pictures': xbmc.executebuiltin('UpdateLibrary(%s,%s)' % (typ, path))
        home.clearProperty('bz_srcdd'); xbmc.sleep(80); xbmc.executebuiltin('SetFocus(9150)'); return
    if act == 'open':
        home.clearProperty('bz_srcdd'); home.clearProperty('bz_msdd'); home.setProperty('bz_msret', '1')   # 5.33.388: dropdown is on 1117, no dialog to close
        xbmc.executebuiltin('ActivateWindow(%s,%s,return)' % (win, path)); return
    new = ''
    if act == 'rename':
        new = xbmcgui.Dialog().input('RENAME SOURCE', name)
        if not new or new == name: return
    # REMOVE / RENAME: Kodi's own source context entry, run on the 1117 source-list row 9150 (no window switch)
    home.clearProperty('bz_srcdd'); xbmc.sleep(80); xbmc.executebuiltin('SetFocus(9150)'); xbmc.sleep(80)
    xbmc.executebuiltin('Action(ContextMenu)')
    if act == 'remove':
        if _ctxpick('remove'): _waitmodal(mon)
    elif _ctxpick('edit'):
        for _ in range(80):
            if xbmc.getCondVisibility('Window.IsActive(mediasource)'): break
            xbmc.sleep(50)
        xbmc.sleep(200); xbmc.executebuiltin('SetFocus(12)'); xbmc.sleep(100); xbmc.executebuiltin('Action(select)')
        for _ in range(60):
            if xbmc.getCondVisibility('Window.IsActive(virtualkeyboard)'): break
            xbmc.sleep(50)
        xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'Input.SendText', 'params': {'text': new, 'done': True}}))
        xbmc.sleep(400); xbmc.executebuiltin('SetFocus(18)'); xbmc.sleep(100); xbmc.executebuiltin('Action(select)')
        _waitmodal(mon)
    msload(); home.setProperty('bz_msdd', '1'); xbmc.executebuiltin('SetFocus(9150)')
if a and a[0] == 'mssrc': mssrc(a[1] if len(a) > 1 else 'open')
# 5.33.364: Back in the per-source dropdown — Kodi closes 1132 on Back; reopen it on the list
if a and a[0] == 'ddback':
    xbmc.sleep(120)
    if not xbmc.getCondVisibility('Window.IsActive(1132)') and xbmc.getCondVisibility('Window.IsActive(1117)'):
        xbmc.executebuiltin('ActivateWindow(1132)')
