#!/usr/bin/env python3
"""P1B step 3: wrap absolute strip elements in <control type="group"><left>bz_strip_x</left> ... </control>
and subtract 660 from their left (or param origin) and own animation centres. Zero change in every use
(wrapper at P+660, element at l-660). Only elements that are strip-attached in EVERY use, whose parent is not a
grouplist / list layout, with numeric lefts and no % sizes; shared keys must agree across all uses.
usage: p1b_wrap.py geom.json sim.json <xml> [--apply]   (sim.json = geom with bz_strip_x+1 and companions)
"""
import sys, json, re, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0]); import xedit
A = json.load(open(sys.argv[1])); Bs = json.load(open(sys.argv[2])); XD = sys.argv[3]
by = {r['id_']: r for r in A}
mv = {a['id_']: round(b['x0'] - a['x0'], 2) for a, b in zip(A, Bs)}
D = -660
def x1(r): return r['x1'] if r['x1'] is not None else r['x0']
def ins(r): return 659.5 <= r['x0'] < 1050.5 and x1(r) <= 1050.5 and x1(r) > r['x0']
def att(r): return 599.5 <= r['x0'] and x1(r) <= 1110.5
def inlay(r):
    p = r
    while True:
        if p['layout']: return True
        if p['pid'] == -1: return False
        p = by[p['pid']]
# deciders
dec = set()
for r in A:
    if r['type'] == 'group' or not ins(r) or mv[r['id_']] != 0 or inlay(r): continue
    d = r
    while d['pid'] != -1:
        p = by[d['pid']]
        if att(p) and mv[p['id_']] == 0: d = p
        else: break
    dec.add(d['o'])
occ = collections.defaultdict(list)
for r in A: occ[r['o']].append(r)
lkey = collections.defaultdict(set); ckey = collections.defaultdict(set)
def isnum(v):
    try: float(v); return True
    except (TypeError, ValueError): return False
W = set(); why = {}
for o in dec:
    rs = occ[o]; ok = True
    for r in rs:
        p = by[r['pid']] if r['pid'] != -1 else None
        if p is not None and p['type'] in ('grouplist',) : ok = False; why[o] = 'parent grouplist'
        if inlay(r): ok = False; why[o] = 'in list layout'
        if not att(r) or mv[r['id_']] != 0: ok = False; why[o] = 'not strip in every use'
        if r['unk']: ok = False; why[o] = 'non-numeric position'
        if (r['lpo'] or r['lo']) and not isnum(r['lval']): ok = False; why[o] = 'left %s' % r['lval']
        if not (r['lpo'] or r['lo']) and (r['ro'] or r['wo'] is None): ok = False; why[o] = 'no left (right/fill)'
    if ok: W.add(o)
def keys(C):
    req = collections.defaultdict(set)
    for r in A:
        w = r['o'] in C
        k = r['lpo'] or r['lo']
        if k: req[('L', k)].add(D if w else 0)
        for co, cen, eff, kind in r['cents']:
            if cen.split(',')[0].strip() in ('auto', ''): continue
            req[('C', co)].add(D if w else 0)
    return req
for it in range(20):
    req = keys(W); drop = set()
    for o in W:
        for r in occ[o]:
            ks = ([('L', r['lpo'] or r['lo'])] if (r['lpo'] or r['lo']) else []) + [('C', c[0]) for c in r['cents'] if c[1].split(',')[0].strip() not in ('auto', '')]
            for k in ks:
                if len(req[k]) > 1: drop.add(o); why[o] = 'shared %s' % (k,)
    if not drop: break
    W -= drop
print('deciders', len(dec), 'wrap', len(W), 'uses', sum(len(occ[o]) for o in W))
rc = collections.Counter(v.split(' ')[0] + ' ' + v.split(' ')[1] if v.startswith('shared') else v for o, v in why.items() if o not in W)
print('skipped:', dict(rc))
if '-v' in sys.argv:
    for o, v in sorted(why.items()):
        if o not in W: r = occ[o][0]; print('  SKIP', o, r['src'], r['type'], r['lval'], round(r['x0']), v)
E = collections.defaultdict(list)
for o in W:
    fn, _, n = o.split('#')
    E[fn].append(('WRAP', int(n), None))
    for r in occ[o]:
        k = r['lpo'] or r['lo']
        if k:
            if '@' in k:
                oo, attr = k.split('@'); f2, tag, m = oo.split('#'); E[f2].append(('param@' + attr, int(m), lambda s: xedit.fmt(float(s) + D)))
            else:
                f2, tag, m = k.split('#'); E[f2].append(('left', int(m), lambda s: xedit.fmt(float(s) + D)))
        else:
            E[fn].append(('INS', int(n), '<left>%s</left>' % xedit.fmt(D)))
        for co, cen, eff, kind in r['cents']:
            if cen.split(',')[0].strip() in ('auto', ''): continue
            f2, _, m = co.split('#')
            def cop(s):
                a = s.split(','); a[0] = xedit.fmt(float(a[0]) + D); return ','.join(a)
            E[f2].append(('c', int(m), cop))
# dedupe (same key from several deciders cannot happen: keys are per source element)
for f in E:
    seen = set(); out = []
    for e in E[f]:
        if (e[0], e[1]) in seen: continue
        seen.add((e[0], e[1])); out.append(e)
    E[f] = out
print('edits', {f: len(v) for f, v in E.items()})

def close_of(text, toks, i):
    depth = 0
    for m in toks[i:]:
        if m.group(2) != 'control' or m.group(4): continue
        depth += -1 if m.group(1) else 1
        if depth == 0: return m
    raise Exception('unclosed')

def apply(path, edits):
    text = open(path, encoding='utf-8').read()
    toks = xedit.tokens(text); by_, cen = xedit.index(text)
    ctl = [i for i, m in enumerate(toks) if m.group(2) == 'control' and not m.group(1)]
    reps = []
    for kind, k, op in edits:
        if kind == 'WRAP':
            i = ctl[k]; m = toks[i]; c = close_of(text, toks, i)
            reps.append((m.start(), m.start(), '<control type="group"><left>bz_strip_x</left><!-- P1B -->', 0))
            reps.append((c.end(), c.end(), '</control>', 2))
        elif kind == 'INS':
            m = by_['control'][k]; reps.append((m.end(), m.end(), op, 1))
        elif kind == 'c':
            m = cen[k]; a = re.search(r'(\scenter\s*=\s*")([^"]*)(")', m.group(0))
            s0 = m.start() + a.start(2); s1 = m.start() + a.end(2); reps.append((s0, s1, op(text[s0:s1]), 1))
        elif '@' in kind:
            tag, attr = kind.split('@'); m = by_[tag][k]
            a = re.search(r'(\s%s\s*=\s*")([^"]*)(")' % attr, m.group(0))
            s0 = m.start() + a.start(2); s1 = m.start() + a.end(2); reps.append((s0, s1, op(text[s0:s1]), 1))
        else:
            m = by_[kind][k]; close = text.index('</%s>' % kind, m.end())
            reps.append((m.end(), close, op(text[m.end():close].strip()), 1))
    # apply from the end; at equal positions, keep a wrapper-close before a following wrapper-open
    reps.sort(key=lambda r: (r[0], r[1], -r[3]), reverse=True)
    last = None
    for s0, s1, new, pr in reps:
        if last is not None and s1 > last: raise Exception('overlap at %d' % s0)
        text = text[:s0] + new + text[s1:]; last = s0
    open(path, 'w', encoding='utf-8').write(text)

if '--apply' in sys.argv:
    for f, e in E.items():
        bad, ok = xedit.check(XD + '/' + f); assert not bad and ok, (f, bad)
    for f, e in E.items(): apply(XD + '/' + f, e)
    print('applied')
