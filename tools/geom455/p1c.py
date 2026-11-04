#!/usr/bin/env python3
"""P1C: literal -> layout constant where EVERY use of the source element agrees (zero change by construction).
  width 540 on box 120..660          -> bz_fill_w
  left 120 at screen level (px 0)    -> bz_stage_x
  left 1140 at screen level (px 0)   -> bz_art_x
usage: p1c.py geom.json <xml> [--apply]"""
import sys, json, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0]); import xedit
A = json.load(open(sys.argv[1])); XD = sys.argv[2]
def x1(r): return r['x1'] if r['x1'] is not None else r['x0']
want = collections.defaultdict(set)
for r in A:
    lk = r['lpo'] or r['lo']; wk = r['wpo'] or r['wo']
    if wk:
        ok = r['wval'] == '540' and round(r['x0'], 2) == 120 and round(x1(r), 2) == 660
        want[('w', wk)].add('bz_fill_w' if ok else None)
    if lk:
        if r['lval'] == '120': want[('l', lk)].add('bz_stage_x' if round(r['px'], 2) == 0 else None)
        elif r['lval'] == '1140': want[('l', lk)].add('bz_art_x' if round(r['px'], 2) == 0 else None)
        else: want[('l', lk)].add(None)
E = collections.defaultdict(list); n = collections.Counter(); mixed = collections.Counter()
for (kind, k), v in want.items():
    hit = v - {None}
    if not hit: continue
    if len(v) > 1: mixed[tuple(sorted(hit))] += 1; continue
    (c,) = hit; n[c] += 1
    tag = 'width' if kind == 'w' else 'left'
    if '@' in k:
        o, attr = k.split('@'); fn, t, m = o.split('#'); E[fn].append(('param@' + attr, int(m), lambda s, c=c: c))
    else:
        fn, t, m = k.split('#'); assert t == tag, k; E[fn].append((tag, int(m), lambda s, c=c: c))
print('source edits', dict(n), 'skipped (also used elsewhere with another meaning)', dict(mixed))
if '--apply' in sys.argv:
    for fn, e in E.items(): xedit.apply(XD + '/' + fn, e)
    print('applied')
