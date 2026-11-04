#!/usr/bin/env python3
"""P1B: strip containers (groups at the old strip x 570) -> left bz_strip_x (660).
Every direct child is compensated by -90 (left, param origin, centerleft is refused,
missing left gets an explicit <left>-90</left>, animation centres -90), so nothing moves.
A shared source element is edited only if EVERY expanded occurrence needs the same delta.
usage: p1b.py geom.json <skin>/xml [--apply]
"""
import sys, json, re, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import xedit

G = json.load(open(sys.argv[1])); XD = sys.argv[2]; APPLY = '--apply' in sys.argv
BASE = float(sys.argv[sys.argv.index('--base') + 1]) if '--base' in sys.argv else 570.0
by = {r['id_']: r for r in G}
kids = collections.defaultdict(list)
for r in G: kids[r['pid']].append(r)
D = BASE - 660

def x1(r): return r['x1'] if r['x1'] is not None else r['x0']
def strip(r): return 659.5 <= r['x0'] < 1050.5 and x1(r) <= 1050.5 and x1(r) > r['x0']
def desc(r):
    for k in kids[r['id_']]:
        yield k; yield from desc(k)

def attached(r):
    a, b = r['x0'], x1(r)
    return (599.5 <= a and b <= 1110.5) or round(a, 2) in (0.0, 120.0)
def transp(r):
    return r['type'] == 'group' and not (r['lo'] or r['lpo'] or r['ro'] or r['wo']) and not r['cents'] and not r['layout']
# candidate containers
cand = {}
for r in G:
    if r['type'] != 'group' or round(r['x0'], 2) != BASE or r['layout'] or r['wo'] or r['ro']: continue
    if BASE == 570:
        if r['lval'] != '570' or not r['lo'] or round(r['px'], 2) != 0: continue
        if not any(strip(d) or 'BezelMMStripChrome@' in d['via'] for d in desc(r)): continue
    else:
        if r['pid'] == -1 or r['lpo']: continue                          # root controls: window can't move
        if r['lval'] not in (None, '0', '120', 'bz_stage_x'): continue
        if round(r['px'], 2) != 0: continue                                # bz_strip_x must be absolute
        if r['cents']: continue
        ok = True; nstrip = 0
        for k in kids[r['id_']]:
            if transp(k): ok = ok and all(attached(d) or transp(d) for d in kids[k['id_']]); continue
            if strip(k): nstrip += 1
            ok = ok and attached(k)
        if not ok or not nstrip: continue
    cand[r['id_']] = r

def shifted(C):
    T = set(C)
    for r in G:   # document order: parents come first
        if r['pid'] in T and transp(r): T.add(r['id_'])
    return T
def needs(C):
    """required edits per source key: key -> set of deltas (all occurrences)."""
    req = collections.defaultdict(set); why = collections.defaultdict(list)
    T = shifted(C)
    for r in G:
        conv = r['pid'] in T
        if transp(r) and r['id_'] not in C and r['id_'] in T: 
            for co, cen, eff, kind in r['cents']: pass
            continue
        lk = r['lpo'] or r['lo']
        if r['id_'] in C and not lk:
            req[('INS', r['o'])].add('S'); why[('INS', r['o'])].append(r['id_'])
        elif lk:
            req[('L', lk)].add('S' if r['id_'] in C else (D if conv else 0)); why[('L', lk)].append(r['id_'])
        else:
            # no left element at all
            if conv:
                if r['ro'] and r['wo']: pass               # right-anchored: invariant
                else: req[('INS', r['o'])].add(D); why[('INS', r['o'])].append(r['id_'])
            else:
                req[('INS', r['o'])].add(0)
        for co, cen, eff, kind in r['cents']:
            if cen.split(',')[0].strip() in ('auto', ''): continue
            req[('C', co)].add(D if conv else 0); why[('C', co)].append(r['id_'])
        # container itself
    return req, why

C = dict(cand)
for it in range(50):
    req, why = needs(C)
    bad = {k for k, v in req.items() if len(v) > 1}
    drop = set()
    for k in bad:
        for i in why[k]:
            p = by[i]['pid']
            if p in C: drop.add(p)
        # container's own left shared with a non-container occurrence
    for cid, c in C.items():
        k = ('L', c['lpo'] or c['lo']) if (c['lpo'] or c['lo']) else ('INS', c['o'])
        if len(req[k]) > 1: drop.add(cid)
    # params: a child left given by a non-numeric value cannot be shifted
    for cid in C:
        pass
    T = shifted(C)
    for r in G:
        if r['pid'] in T and (r['lpo'] or r['lo']) and r['lval'] is not None and r['id_'] not in C:
            try: float(r['lval'])
            except ValueError:
                p = r['pid']
                while p not in C: p = by[p]['pid']
                drop.add(p)
    for cid in C:
        p = by[cid]['pid']
        while p != -1:
            if p in C: drop.add(cid); break
            p = by[p]['pid']
    if not drop: break
    for d in drop: C.pop(d, None)

print('containers: cand %d kept %d' % (len(cand), len(C)))
dropped = sorted(set(c['src'] for i, c in cand.items() if i not in C))
print('dropped:', dropped)
kept = collections.Counter(c['src'] for c in C.values())
print('kept sources:', len(kept))
edits = collections.defaultdict(list)
for k, v in req.items():
    v = v - {0}
    if not v: continue
    (val,) = v
    kind, key = k
    if kind == 'L':
        if '@' in key:
            o, attr = key.split('@')
            fn, tag, n = o.split('#')
            edits[fn].append(('param@' + attr, int(n), (lambda s: 'bz_strip_x') if val == 'S' else (lambda s: xedit.fmt(float(s) + D))))
        else:
            fn, tag, n = key.split('#')
            edits[fn].append(('left', int(n), (lambda s: 'bz_strip_x') if val == 'S' else (lambda s: xedit.fmt(float(s) + D))))
    elif kind == 'C':
        fn, _, n = key.split('#')
        def cop(s):
            a = s.split(',')
            if a[0].strip() in ('auto', ''): raise Exception('auto centre ' + s)
            a[0] = xedit.fmt(float(a[0]) + D); return ','.join(a)
        edits[fn].append(('c', int(n), cop))
    elif kind == 'INS':
        fn, tag, n = key.split('#')
        edits[fn].append(('INS', int(n), '<left>%s</left>' % ('bz_strip_x' if val == 'S' else xedit.fmt(D))))
n = sum(len(v) for v in edits.values())
print('edits', n, {f: len(v) for f, v in edits.items()})

def apply(path, E):
    text = open(path, encoding='utf-8').read()
    by_, cen = xedit.index(text)
    reps = []
    for kind, k, op in E:
        if kind == 'INS':
            m = by_['control'][k]; reps.append((m.end(), m.end(), op))
        elif kind == 'c':
            m = cen[k]; a = re.search(r'(\scenter\s*=\s*")([^"]*)(")', m.group(0))
            s0 = m.start() + a.start(2); s1 = m.start() + a.end(2); reps.append((s0, s1, op(text[s0:s1])))
        elif '@' in kind:
            tag, attr = kind.split('@'); m = by_[tag][k]
            a = re.search(r'(\s%s\s*=\s*")([^"]*)(")' % attr, m.group(0))
            s0 = m.start() + a.start(2); s1 = m.start() + a.end(2); reps.append((s0, s1, op(text[s0:s1])))
        else:
            m = by_[kind][k]; close = text.index('</%s>' % kind, m.end())
            reps.append((m.end(), close, op(text[m.end():close].strip())))
    reps.sort()
    for a, b in zip(reps, reps[1:]):
        if a[1] > b[0]: raise Exception('overlap %s %s' % (a, b))
    for s0, s1, new in reversed(reps): text = text[:s0] + new + text[s1:]
    open(path, 'w', encoding='utf-8').write(text)

if APPLY:
    for fn, E in edits.items():
        bad, ok = xedit.check(XD + '/' + fn)
        assert not bad and ok, (fn, bad, ok)
    for fn, E in edits.items(): apply(XD + '/' + fn, E)
    print('applied')

if '--why' in sys.argv:
    # one pass with ALL candidates: show conflicting keys per dropped container
    req, why = needs(cand)
    for cid, c in cand.items():
        if cid in C: continue
        rs = []
        for k in kids[cid]:
            for kk in ([('L', k['lpo'] or k['lo'])] if (k['lpo'] or k['lo']) else [('INS', k['o'])]) + [('C', x[0]) for x in k['cents']]:
                if len(req[kk]) > 1:
                    others = set(by[i]['src'] + '|' + by[i]['win'] for i in why[kk] if by[i]['pid'] not in cand and by[i]['id_'] not in cand)
                    rs.append((kk, k['src'], k['lval'], sorted(req[kk], key=str), sorted(others)[:2]))
            if (k['lpo'] or k['lo']) and k['lval'] is not None:
                try: float(k['lval'])
                except ValueError: rs.append(('NONNUM', k['src'], k['lval']))
        print('##', c['src'], c['win']); [print('   ', x) for x in rs[:6]]
if '--who' in sys.argv:
    key = sys.argv[sys.argv.index('--who') + 1]
    T = shifted(cand)
    for r in G:
        if (r['lpo'] or r['lo']) == key and r['pid'] not in T:
            chain = []; p = r['pid']
            while p != -1: q = by[p]; chain.append('%s[%s l=%s w=%s r=%s c=%d]' % (q['src'], q['type'], q['lval'], q['wval'], bool(q['ro']), len(q['cents']))); p = q['pid']
            print(r['win'], ' < '.join(chain[:4]))
