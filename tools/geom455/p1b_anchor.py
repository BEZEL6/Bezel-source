#!/usr/bin/env python3
"""P1B step 2: inside strip containers, full-screen (-660 -> bz_strip_nx) and stage (-540 -> bz_strip_tostage)
lefts become named constants. Only source elements whose EVERY occurrence is that anchor are edited.
usage: p1b_anchor.py g1.json g661.json <xml> [--apply]"""
import sys, json, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0]); import xedit
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); XD = sys.argv[3]
MAP = {('-660', 0.0): 'bz_strip_nx', ('-540', 120.0): 'bz_strip_tostage'}
occ = collections.defaultdict(set)
for a, b in zip(A, B):
    k = a['lpo'] or a['lo']
    if not k: continue
    moved = round(b['x0'] - a['x0'], 2) == 1
    occ[k].add(MAP.get((a['lval'], round(a['x0'], 2))) if moved else None)
E = collections.defaultdict(list); skip = []
for k, v in occ.items():
    hits = v - {None}
    if not hits: continue
    if len(v) != 1: skip.append((k, v)); continue
    (c,) = hits
    if '@' in k:
        o, attr = k.split('@'); fn, tag, n = o.split('#'); E[fn].append(('param@' + attr, int(n), lambda s, c=c: c))
    else:
        fn, tag, n = k.split('#'); E[fn].append(('left', int(n), lambda s, c=c: c))
print('edits', {f: len(v) for f, v in E.items()}, 'skipped(mixed)', skip)
if '--apply' in sys.argv:
    for fn, e in E.items(): xedit.apply(XD + '/' + fn, e)
    print('applied')
