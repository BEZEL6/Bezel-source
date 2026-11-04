#!/usr/bin/env python3
"""Static Kodi skin geometry resolver (horizontal only).
Expands includes/params/constants per window and reports every control's
absolute x box, with the source file:line of the element that holds it.
usage: geom.py <skin>/xml out.json
"""
import sys, os, re, json, copy
from lxml import etree

XD = sys.argv[1]
P = etree.XMLParser(remove_comments=True, huge_tree=True)

def load(fn):
    t = etree.parse(os.path.join(XD, fn), P)
    cnt = {}; cc = 0
    for e in t.iter():
        if isinstance(e.tag, str):
            e.set('_src', '%s:%d' % (fn, e.sourceline or 0))
            k = cnt.get(e.tag, 0); cnt[e.tag] = k + 1
            e.set('_o', '%s#%s#%d' % (fn, e.tag, k))
            if 'center' in e.attrib:
                e.set('_co', '%s#c#%d' % (fn, cc)); cc += 1
    return t.getroot()

INC, CONST, PORG = {}, {}, {}
seen = set()
def load_inc(fn):
    if fn in seen or not os.path.exists(os.path.join(XD, fn)): return
    seen.add(fn)
    r = load(fn)
    for e in r:
        if not isinstance(e.tag, str): continue
        if e.tag == 'include' and e.get('name'):
            INC[e.get('name')] = e
        elif e.tag == 'include' and e.get('file'):
            load_inc(e.get('file'))
        elif e.tag == 'constant' and e.get('name'):
            CONST[e.get('name')] = (e.text or '').strip()
load_inc('Includes.xml')

PRE = re.compile(r'\$PARAM\[([^\]]+)\]')
def subst(el, params):
    for e in el.iter():
        if not isinstance(e.tag, str): continue
        if e.text and '$PARAM' in e.text:
            ms = PRE.findall(e.text)
            if len(ms) == 1 and ms[0] in PORG: e.set('_po', PORG[ms[0]])
            e.text = PRE.sub(lambda m: params.get(m.group(1), ''), e.text)
        for k, v in list(e.attrib.items()):
            if k.startswith('_'): continue
            if '$PARAM' in v:
                ms = PRE.findall(v)
                if e.tag == 'param' and len(ms) == 1 and ms[0] in PORG: e.set('_po', PORG[ms[0]])
                e.set(k, PRE.sub(lambda m: params.get(m.group(1), ''), v))

def expand(el, params, depth=0):
    if depth > 40: return
    i = 0
    while i < len(el):
        c = el[i]
        if not isinstance(c.tag, str): i += 1; continue
        if c.tag == 'include' and not c.get('file'):
            name = c.get('content') or (c.text or '').strip()
            name = PRE.sub(lambda m: params.get(m.group(1), ''), name)
            d = INC.get(name)
            if d is None: el.remove(c); continue
            p = {}; PORG.clear() if False else None
            porg = {}
            dd = d.find('definition')
            src = dd if dd is not None else d
            for pp in d.findall('param'):
                p[pp.get('name')] = pp.get('default', ''); porg[pp.get('name')] = pp.get('_o') + '@default'
            for pp in c.findall('param'):
                p[pp.get('name')] = pp.get('value', (pp.text or '')); porg[pp.get('name')] = pp.get('_po') or (pp.get('_o') + '@value')
            new = [copy.deepcopy(x) for x in src if isinstance(x.tag, str) and not (dd is None and x.tag == 'param')]
            holder = etree.Element('h'); holder.extend(new)
            PORG.clear(); PORG.update(porg)
            subst(holder, p)
            for x in list(holder): x.set('_via', (c.get('_via', '') + '>' if c.get('_via') else '') + name + '@' + c.get('_src', ''))
            expand(holder, p, depth + 1)
            kids = list(holder)
            el.remove(c)
            for j, k in enumerate(kids): el.insert(i + j, k)
            i += len(kids)
            continue
        expand(c, params, depth + 1)
        i += 1

def num(v):
    if v is None: return None
    v = v.strip()
    v = CONST.get(v, v)
    try: return float(v)
    except Exception: return None

OUT = []
CTRL = ('control',)
def walk(el, px, pw, path, win, pin=False, pid=-1):
    for c in el:
        if not isinstance(c.tag, str) or c.tag != 'control': continue
        typ = c.get('type')
        L = c.find('left'); R = c.find('right'); W = c.find('width'); CL = c.find('centerleft')
        l = num(L.text) if L is not None else None
        r = num(R.text) if R is not None else None
        w = num(W.text) if W is not None else None
        cl = num(CL.text) if CL is not None else None
        unk = any(t is not None and num(t.text) is None and (t.text or '').strip() not in ('', 'auto') for t in (L, R, W, CL))
        if w is None:
            if l is not None and r is not None: w = pw - l - r
            elif typ in ('group', 'grouplist') or W is None: w = pw - (l or 0) - (r or 0) if typ in ('group',) else (pw - (l or 0) if W is None else None)
        if l is None:
            if cl is not None and w is not None: l = cl - w / 2
            elif r is not None and w is not None: l = pw - r - w
            else: l = 0
        x0 = px + l
        cents = []
        for a in c.findall('animation'):
            for e in [a] + list(a):
                if isinstance(e.tag, str) and e.get('_co'):
                    cents.append((e.get('_co'), e.get('center'), e.get('effect') or a.get('effect'), (a.text or '').strip() or a.get('type')))
        anims = []
        for a in c.findall('animation'):
            if a.get('effect') in ('slide', 'zoom') and (a.text or '').strip() == 'Conditional' and a.get('time') in ('0', None) and a.get('condition') == 'true':
                anims.append('%s %s c%s' % (a.get('effect'), a.get('end'), a.get('center')))
        rec = dict(lpo=(L.get('_po') if L is not None else None), wpo=(W.get('_po') if W is not None else None), lo=(L.get('_o') if L is not None else None), wo=(W.get('_o') if W is not None else None), ro=(R.get('_o') if R is not None else None), lval=(L.text.strip() if L is not None and L.text else None), wval=(W.text.strip() if W is not None and W.text else None), cents=cents, id_=len(OUT), pid=pid, layout=(path[-1] if path and path[-1] in ('itemlayout','focusedlayout','content') else ''), win=win, o=c.get('_o'), pw=pw, px=px, src=c.get('_src'), via=c.get('_via', ''), type=typ, id=c.get('id'), x0=x0,
                   x1=(x0 + w) if w is not None else None, lsrc=(L.get('_src') if L is not None else None),
                   wsrc=(W.get('_src') if W is not None else None), unk=unk, anims=anims, path=path, pin=pin)
        OUT.append(rec)
        cw = w if w is not None else pw
        x1 = (x0 + w) if w is not None else x0
        me = pin or (x0 >= 569.5 and x0 < 1139.5 and x1 <= 1140.5)
        walk(c, x0, cw, path + [c.get('_src')], win, me, rec['id_'])
        for sub in c:  # itemlayout / focusedlayout / content
            if isinstance(sub.tag, str) and sub.tag in ('itemlayout', 'focusedlayout', 'content'):
                lw = num(sub.get('width')) or cw
                walk(sub, x0, lw, path + [c.get('_src'), sub.tag], win, me, rec['id_'])

for fn in sorted(os.listdir(XD)):
    if not fn.endswith('.xml') or fn.startswith('Includes') or fn in ('Font.xml', 'Variables.xml', 'Defaults.xml'): continue
    try: r = load(fn)
    except Exception as e: print('ERR', fn, e); continue
    if r.tag != 'window': continue
    expand(r, {})
    cs = r.find('controls')
    if cs is None: continue
    walk(cs, 0.0, 1920.0, [], fn)

json.dump(OUT, open(sys.argv[2], 'w'))
print(len(OUT), 'controls')
