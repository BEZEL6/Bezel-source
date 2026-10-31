# 5.33.27 t236: Viz settings page inside FS Player Controls (1115). load | step,<i>,<+1|-1>
import sys, json, os, xml.etree.ElementTree as ET
import xbmc, xbmcaddon, xbmcgui
MAX = 8
def win():
    return xbmcgui.Window(xbmcgui.getCurrentWindowDialogId())
def vizid():
    r = json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","id":1,"method":"Settings.GetSettingValue","params":{"setting":"musicplayer.visualisation"}}'))
    return r.get('result', {}).get('value', '')
def rows(aid):
    a = xbmcaddon.Addon(aid)
    p = os.path.join(xbmc.translatePath(a.getAddonInfo('path')) if hasattr(xbmc,'translatePath') else __import__('xbmcvfs').translatePath(a.getAddonInfo('path')), 'resources', 'settings.xml')
    out = []
    try: root = ET.parse(p).getroot()
    except Exception: return a, out
    L = lambda s: (a.getLocalizedString(int(s)) or xbmc.getLocalizedString(int(s))) if s and s.lstrip('-').isdigit() and int(s) else ''
    for s in root.iter('setting'):
        t = s.get('type'); sid = s.get('id')
        if not sid or t not in ('integer', 'boolean', 'number'): continue
        lab = L(s.get('label')) or sid
        opts = [(o.text, L(o.get('label')) or o.text) for o in s.iter('option')]
        c = s.find('constraints'); d = s.findtext('default') or '0'
        r = dict(id=sid, t=t, lab=lab, opts=opts, d=d)
        if c is not None and not opts:
            r['min'] = float(c.findtext('minimum') or 0); r['max'] = float(c.findtext('maximum') or 100); r['step'] = float(c.findtext('step') or 1)
        out.append(r)
    return a, out[:MAX]
def show(a, rs, w):
    w.setProperty('bz_vs_n', str(len(rs)))
    for i in range(MAX):
        if i < len(rs):
            r = rs[i]; v = a.getSetting(r['id']) or r['d']
            if r['t'] == 'boolean': txt = 'On' if v.lower() == 'true' else 'Off'
            elif r['opts']: txt = dict(r['opts']).get(v, v)
            else: txt = v
            w.setProperty('bz_vs%d_lab' % i, r['lab']); w.setProperty('bz_vs%d_val' % i, txt)
        else:
            w.clearProperty('bz_vs%d_lab' % i); w.clearProperty('bz_vs%d_val' % i)
def main():
    w = win(); aid = vizid()
    if not aid:
        w.setProperty('bz_vs_n', '0'); w.setProperty('bz_vs_name', 'None'); return
    a, rs = rows(aid)
    w.setProperty('bz_vs_name', a.getAddonInfo('name'))
    args = sys.argv[1:]
    if args and args[0] == 'step':
        i, dirn = int(args[1]), int(args[2])
        if i < len(rs):
            r = rs[i]; v = a.getSetting(r['id']) or r['d']
            if r['t'] == 'boolean': nv = 'false' if v.lower() == 'true' else 'true'
            elif r['opts']:
                ks = [k for k, _ in r['opts']]; nv = ks[(ks.index(v) + dirn) % len(ks)] if v in ks else ks[0]
            else:
                f = float(v) + dirn * r['step']; f = max(r['min'], min(r['max'], f)); nv = str(int(f)) if r['t'] == 'integer' else str(f)
            a.setSetting(r['id'], nv)
    show(a, rs, w)
main()
