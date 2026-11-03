# BEZEL 3.0: per-section presets preset,<sec>,<name>; 2.10/2.9: Animation Tuner actions. RunScript(special://skin/scripts/bz_tune.py,preset|reset|export[,arg])
# Settings live in Skin.String(bz_at_<id>) (step index, empty = default); the step tables are in bz_tune.json (written by gen_tuner.py).
import sys, json, os, time, xbmc, xbmcgui, xbmcvfs
here = os.path.dirname(os.path.abspath(__file__))
_J = json.load(open(os.path.join(here, 'bz_tune.json'))); P = _J['P']; TOG = _J.get('TOG', [])
LOOK = set(['hishape'] + [p[0] for p in P if p[1] == 'look'])
# BEZEL 3.0 tuner v2: per-section presets {section: {preset: {id: step}}}. Rows not named = default (4.0.1 O24: 17-step speed rows, step 7 = 1x = default).
PN = ['default', 'subtle', 'mid', 'high', 'extreme']
# 4.7.1 A1: presets from bezel_presets_all_categories.xlsx (Default = Subtle). Every row a preset names is written; rows not named = slider default.
PRESETS = {
    'art': {'subtle': {'swaypause': 14, 'phold': 14, 'flip': 7}, 'mid': {'swaypause': 12, 'phold': 12, 'flip': 7}, 'high': {'swaypause': 8, 'phold': 8, 'flip': 9}, 'extreme': {'swaypause': 5, 'phold': 5, 'flip': 12}, 'default': {'swaypause': 14, 'phold': 14, 'flip': 7}},
    'list': {'subtle': {'rowscroll': 7, 'rowsoft': 2, 'zoomtime': 7, 'zoomsize': 3, 'fanart': 7, 'cascspeed': 7, 'cascstag': 6, 'pingspeed': 8}, 'mid': {'rowscroll': 7, 'rowsoft': 4, 'zoomtime': 5, 'zoomsize': 4, 'fanart': 5, 'cascspeed': 7, 'cascstag': 8, 'pingspeed': 10}, 'high': {'rowscroll': 11, 'rowsoft': 5, 'zoomtime': 3, 'zoomsize': 5, 'fanart': 3, 'cascspeed': 11, 'cascstag': 10, 'pingspeed': 12}, 'extreme': {'rowscroll': 17, 'rowsoft': 6, 'zoomtime': 1, 'zoomsize': 7, 'fanart': 1, 'cascspeed': 17, 'cascstag': 14, 'pingspeed': 14}, 'default': {'rowscroll': 7, 'rowsoft': 2, 'zoomtime': 7, 'zoomsize': 3, 'fanart': 7, 'cascspeed': 7, 'cascstag': 6, 'pingspeed': 8}},
    'menu': {'subtle': {'menuopen': 7, 'menuclose': 7, 'mmbar': 10}, 'mid': {'menuopen': 9, 'menuclose': 9, 'mmbar': 10}, 'high': {'menuopen': 12, 'menuclose': 12, 'mmbar': 10}, 'extreme': {'menuopen': 17, 'menuclose': 17, 'mmbar': 10}, 'default': {'menuopen': 7, 'menuclose': 7, 'mmbar': 5}},
    'music': {'subtle': {'mctrl': 7}, 'mid': {'mctrl': 9}, 'high': {'mctrl': 12}, 'extreme': {'mctrl': 17}, 'default': {'mctrl': 7}},
    'dust': {'subtle': {'d20fdens': 1, 'd20mdens': 1, 'd20sdens': 1, 'd20fsize': 2, 'd20msize': 2, 'd20ssize': 2, 'mmdsize': 2, 'd20fbri': 3, 'd20mbri': 3, 'd20sbri': 3, 'd20ffade': 2, 'd20mfade': 2, 'd20sfade': 2, 'mmdfade': 2, 'd20fslide': 2, 'd20mslide': 2, 'mmdslide': 2, 'd3lsize': 1, 'pd3lsize': 1, 'd3lit': 4, 'pd3lit': 4, 'lspinspd': 22, 'plspinspd': 22}, 'mid': {'d20fdens': 2, 'd20mdens': 2, 'd20sdens': 2, 'd20fsize': 2, 'd20msize': 2, 'd20ssize': 2, 'mmdsize': 2, 'd20fbri': 5, 'd20mbri': 5, 'd20sbri': 5, 'd20ffade': 3, 'd20mfade': 3, 'd20sfade': 3, 'mmdfade': 3, 'd20fslide': 3, 'd20mslide': 3, 'mmdslide': 3, 'd3lsize': 2, 'pd3lsize': 2, 'd3lit': 6, 'pd3lit': 6, 'lspinspd': 18, 'plspinspd': 18}, 'high': {'d20fdens': 3, 'd20mdens': 3, 'd20sdens': 3, 'd20fsize': 2, 'd20msize': 2, 'd20ssize': 2, 'mmdsize': 2, 'd20fbri': 7, 'd20mbri': 7, 'd20sbri': 7, 'd20ffade': 3, 'd20mfade': 3, 'd20sfade': 3, 'mmdfade': 3, 'd20fslide': 4, 'd20mslide': 4, 'mmdslide': 4, 'd3lsize': 2, 'pd3lsize': 2, 'd3lit': 7, 'pd3lit': 7, 'lspinspd': 18, 'plspinspd': 18}, 'extreme': {'d20fdens': 3, 'd20mdens': 3, 'd20sdens': 3, 'd20fsize': 3, 'd20msize': 3, 'd20ssize': 3, 'mmdsize': 3, 'd20fbri': 9, 'd20mbri': 9, 'd20sbri': 9, 'd20ffade': 4, 'd20mfade': 4, 'd20sfade': 4, 'mmdfade': 4, 'd20fslide': 4, 'd20mslide': 4, 'mmdslide': 4, 'd3lsize': 3, 'pd3lsize': 3, 'd3lit': 9, 'pd3lit': 9, 'lspinspd': 10, 'plspinspd': 10}, 'default': {'d20fdens': 1, 'd20mdens': 1, 'd20sdens': 1, 'd20fsize': 2, 'd20msize': 2, 'd20ssize': 2, 'mmdsize': 2, 'd20fbri': 3, 'd20mbri': 3, 'd20sbri': 3, 'd20ffade': 2, 'd20mfade': 2, 'd20sfade': 2, 'mmdfade': 2, 'd20fslide': 2, 'd20mslide': 2, 'mmdslide': 2, 'd3lsize': 1, 'pd3lsize': 1, 'd3lit': 4, 'pd3lit': 4, 'lspinspd': 22, 'plspinspd': 22}},
}
def setv(i, v): xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1'); xbmc.executebuiltin('Skin.SetString(bz_at_%s,%s)' % (i, v)) if v else xbmc.executebuiltin('Skin.Reset(bz_at_%s)' % i)
DEF = _J.get('DEF', {})
def apply_defs(scope):   # t4691: Rob's Tuner default picks (bz_tune.json DEF). scope = section name, 'all' (look kept) or 'everything'
    lk = ('look', 'block')
    ok = lambda sc: scope == 'everything' or sc == scope or (scope == 'all' and sc not in lk)
    for k, (v, sc) in DEF.get('str', {}).items():
        if ok(sc): xbmc.executebuiltin('Skin.SetString(%s,%s)' % (k, v) if v else 'Skin.Reset(%s)' % k)
    for k, sc in DEF.get('on', {}).items():
        if ok(sc): xbmc.executebuiltin('Skin.SetBool(%s)' % k)
    for k, sc in DEF.get('off', {}).items():
        if ok(sc): xbmc.executebuiltin('Skin.Reset(%s)' % k)
    xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1')
def note(m): xbmcgui.Dialog().notification('BEZEL tuner', m, xbmcgui.NOTIFICATION_INFO, 2000)
a = (sys.argv[1:] + ['', '', ''])[:3]
if a[0] == 'preset':   # preset,<section>,<subtle|mid|high|extreme|next>
    sec, nm = a[1], a[2].lower()
    if sec not in PRESETS: sys.exit(0)
    if nm == 'next':
        cur = xbmc.getInfoLabel('Skin.String(bz_ps_%s)' % sec).lower()
        nm = PN[(PN.index(cur) + 1) % len(PN)] if cur in PN else 'default'
    pr = PRESETS[sec].get(nm, {})
    for i, s_, d, n, vals in P:
        if s_ == sec: setv(i, str(pr[i]) if i in pr else '')
    xbmc.executebuiltin('Skin.SetString(bz_ps_%s,%s)' % (sec, nm.capitalize()))
    note('%s preset: %s' % (sec.upper(), nm.capitalize()))
elif a[0] == 'reset':
    what = {'all': 'all timing (look kept)', 'everything': 'EVERYTHING (timing, look, double-tap)'}.get(a[1], 'the %s section' % a[1].upper())
    # t5022: force = in-Tuner Yes (no Dialog.yesno popup)
    if a[2] != 'force' and not xbmcgui.Dialog().yesno('BEZEL tuner', 'Reset %s to the defaults?' % what): sys.exit(0)
    for i, sec, d, n, vals in P:
        if a[1] in ('all', 'everything') or sec == a[1]:
            if a[1] == 'all' and i in LOOK: continue
            setv(i, '')
    if a[1] == 'everything' or a[1] == 'menu': xbmc.executebuiltin('Skin.Reset(bz_dtap_off)'); xbmc.executebuiltin('Skin.Reset(bz_at_mmdim)'); xbmc.executebuiltin('Skin.Reset(bz_at_mmwarm)'); xbmc.executebuiltin('Skin.Reset(bz_at_mmdef)')
    if a[1] == 'everything' or a[1] == 'dust':
        for b in ('bz_dust_off', 'bz_adust_off', 'bz_spin_off', 'bz_spin_ccw', 'bz_lspin_off', 'bz_lspin_cw', 'bz_sdust_off', 'bz_fib_off', 'bz_flk_off', 'bz_d3l0_off', 'bz_d3l1_off', 'bz_d3l2_off', 'bz_amb_off', 'bz_alit20', 'bz_plit20', 'bz_mmdust_off'): xbmc.executebuiltin('Skin.Reset(%s)' % b)
    if a[1] in ('everything', 'art'): xbmc.executebuiltin('Skin.Reset(bz_bigalb_off)'); xbmc.executebuiltin('Skin.Reset(bz_at_a2pfade)'); xbmc.executebuiltin('Skin.Reset(bz_at_midlefade)')  # 5.33.403 A2PFADE -> 800 ms (empty|7)
    if a[1] in ('everything', 'ashadow'): xbmc.executebuiltin('Skin.Reset(bz_acast_static)')
    if a[1] in ('everything', 'pshadow'): xbmc.executebuiltin('Skin.Reset(bz_pcast_static)')   # 4.1.0 O39
    for sec in PRESETS:
        if a[1] in ('all', 'everything', sec): xbmc.executebuiltin('Skin.Reset(bz_ps_%s)' % sec)
    if a[1] in ('everything', 'fschrome'):   # t4504 FULLSCREEN MUSIC chrome
        for b in ('Skin.Reset(bz_at_fschromeop)', 'Skin.Reset(bz_at_fschromecol)', 'Skin.Reset(bz_fschrome_fan)', 'Skin.Reset(bz_at_fsvizop)', 'Skin.Reset(bz_at_fsslide)'): xbmc.executebuiltin(b)
    if a[1] in ('everything', 'block'): xbmc.executebuiltin('Skin.Reset(bz_blockcol)'); xbmc.executebuiltin('Skin.Reset(bz_blockcol_name)')
    apply_defs(a[1])
    note('Reset ' + a[1])
elif a[0] == 'resetui':  # t5022: in-Tuner Yes/No mode (list visibility needs ReloadSkin)
    home = xbmcgui.Window(10000)
    mode = a[1]
    key = 'bz_topen_' + 'reset' + 'sys'
    if mode == 'open':
        xbmc.executebuiltin('Skin.SetBool(%s)' % key)
    else:
        xbmc.executebuiltin('Skin.Reset(%s)' % key)
    xbmc.executebuiltin('ReloadSkin()')
    xbmc.sleep(800)
    home.setProperty('bz_navtune', 'true')
    xbmc.sleep(200)
    xbmc.executebuiltin('SetFocus(6970)')
elif a[0] == 'seed':   # t4691: first start on a new defaults version -> write Rob's picks once, bake timings, reload if a file changed
    if DEF and xbmc.getInfoLabel('Skin.String(bz_defseed)') != DEF.get('ver'):
        apply_defs('everything'); xbmc.executebuiltin('Skin.SetString(bz_defseed,%s)' % DEF.get('ver')); xbmc.sleep(300)
        sys.path.insert(0, here); import bz_tune_patch
        if bz_tune_patch.patch(xbmc.getInfoLabel): xbmc.executebuiltin('ReloadSkin()')
elif a[0] == 'alldust':   # 4.1.0 O37: master All dust toggle (on / off / toggle)
    B = ('bz_dust_off', 'bz_sdust_off', 'bz_adust_off')
    off = all(xbmc.getCondVisibility('Skin.HasSetting(%s)' % b) for b in B)
    want_off = {'on': False, 'off': True}.get(a[1], not off)
    for b in B: xbmc.executebuiltin(('Skin.SetBool(%s)' if want_off else 'Skin.Reset(%s)') % b)
    xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1')
elif a[0] == 'import':   # 4.0.1: load an exported tuning file; 4.0.0 files are moved to the 4.0.1 finer steps (same table as the O24 start migration)
    MIG = {"swaypause": [2, 4, 5, 6, 8, 10, 12, 14], "flip": [7, 9, 11, 12, 13, 15, 17], "pingspeed": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13], "rowscroll": [7, 9, 11, 12, 13, 15, 17], "zoomtime": [1, 3, 5, 7, 9, 11, 13], "fanart": [1, 3, 5, 7, 9, 11], "cascspeed": [7, 9, 11, 12, 13, 15, 17], "cascstag": [1, 4, 6, 8, 10, 12, 14], "menuopen": [7, 9, 11, 12, 13, 15, 17], "menuclose": [7, 9, 11, 12, 13, 15, 17], "dtapwin": [3, 5, 7, 9, 11, 12, 13], "mctrl": [7, 9, 11, 12, 13, 15, 17], "d3speed": [2, 4, 6, 8, 11, 13, 15], "phold": [2, 4, 5, 6, 8, 10, 12, 14]}
    src = a[1] if len(a) > 1 and a[1] else ''
    if not src:
        dflt = 'special://profile/addon_data/skin.bezel2/'
        src = xbmcgui.Dialog().browse(1, 'Import BEZEL tuning', 'files', '.json', False, False, dflt)
    if src:
        try:
            f = xbmcvfs.File(src); d = json.loads(f.read()); f.close()
            ver = str(d.get('version', '0'))
            def vt(v):
                try: return tuple(int(x) for x in v.split('.')[:3])
                except Exception: return (0, 0, 0)
            old = vt(ver) < (4, 0, 1)
            st = d.get('settings', {}); n = 0
            for i, sec, dd, cnt, vals in P:
                e = st.get(i)
                if not isinstance(e, dict) or 'step' not in e: continue
                k = int(e['step'])
                if old and i in MIG:
                    k = MIG[i][k - 1] if 1 <= k <= len(MIG[i]) else dd
                if not 1 <= k <= cnt: continue
                setv(i, '' if k == dd else str(k)); n += 1
            if 'dtap' in st: xbmc.executebuiltin('Skin.SetBool(bz_dtap_off)' if st['dtap'].get('value') == 'OFF' else 'Skin.Reset(bz_dtap_off)')
            for t, lab, b, inv in TOG:
                if t in st:
                    on = st[t].get('value') == 'ON'
                    xbmc.executebuiltin(('Skin.SetBool(%s)' if on == bool(inv) else 'Skin.Reset(%s)') % b)
            for sec, nm in (d.get('presets') or {}).items():
                if sec in PRESETS: xbmc.executebuiltin('Skin.SetString(bz_ps_%s,%s)' % (sec, nm) if nm != 'Custom' else 'Skin.Reset(bz_ps_%s)' % sec)
            xbmc.sleep(300)
            sys.path.insert(0, here); import bz_tune_patch
            bz_tune_patch.patch(xbmc.getInfoLabel)
            note('Imported %d settings%s' % (n, ' (moved from %s)' % ver if old else ''))
            xbmc.executebuiltin('ReloadSkin()')
        except Exception as e:
            xbmc.log('BEZEL tuner import: %s' % e, xbmc.LOGWARNING); note('Import failed')
elif a[0] == 'export':
    out = {'skin': 'skin.bezel2', 'version': xbmc.getInfoLabel('System.AddonVersion(skin.bezel2)'), 'exported': time.strftime('%Y-%m-%d %H:%M:%S'), 'settings': {}}
    for i, sec, d, n, vals in P:
        s = xbmc.getInfoLabel('Skin.String(bz_at_%s)' % i)
        k = int(s) if s.isdigit() and 1 <= int(s) <= n else d
        out['settings'][i] = {'section': sec, 'step': k, 'value': vals[k - 1], 'default': k == d}
    out['settings']['dtap'] = {'section': 'menu', 'value': 'OFF' if xbmc.getCondVisibility('Skin.HasSetting(bz_dtap_off)') else 'ON', 'default': not xbmc.getCondVisibility('Skin.HasSetting(bz_dtap_off)')}
    for t, lab, b, inv in TOG:
        on = xbmc.getCondVisibility('Skin.HasSetting(%s)' % b) == bool(inv)
        out['settings'][t] = {'value': 'ON' if on else 'OFF', 'default': on != bool(inv)}
    out['presets'] = {sec: (xbmc.getInfoLabel('Skin.String(bz_ps_%s)' % sec) or 'Custom') for sec in PRESETS}
    out['preset_tables'] = PRESETS
    txt = json.dumps(out, indent=2)
    dst = 'special://profile/addon_data/skin.bezel2/'
    if not xbmcvfs.exists(dst): xbmcvfs.mkdirs(dst)
    f = xbmcvfs.File(dst + 'bezel_tuning.json', 'w'); f.write(txt.encode()); f.close()
    where = ['userdata/addon_data/skin.bezel2/bezel_tuning.json']
    if xbmc.getCondVisibility('System.Platform.Android'):   # Shield: also a copy the user can reach from a file manager / PC
        try:
            p = '/storage/emulated/0/Download/bezel_tuning.json'
            open(p, 'w').write(txt); where.append(p)
        except Exception as e:
            xbmc.log('BEZEL tuner export: Download copy failed: %s' % e, xbmc.LOGWARNING)
    xbmc.log('BEZEL tuner export:\n' + txt, xbmc.LOGINFO)
    xbmcgui.Dialog().textviewer('BEZEL tuning saved to: ' + ' + '.join(where), txt)
