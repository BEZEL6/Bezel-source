#!/usr/bin/env python3
"""Strip-move test: a.json (as is) vs b.json (bz_strip_x+1 with companions). Counts drawn controls."""
import json, sys, collections
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
def ins(r):
    x1 = r['x1'] if r['x1'] is not None else r['x0']
    return 659.5 <= r['x0'] < 1050.5 and x1 <= 1050.5 and x1 > r['x0']
c = collections.Counter(); oth = collections.Counter(); still = collections.Counter()
for a, b in zip(A, B):
    if a['type'] == 'group': continue
    d = round(b['x0'] - a['x0'], 2)
    c[('strip' if ins(a) else 'other', 'moves' if d == 1 else 'still' if d == 0 else str(d))] += 1
    if not ins(a) and d != 0: oth[(round(a['x0']), round(a['x1'] or a['x0']), a['src'])] += 1
    if ins(a) and d == 0: still[a['win']] += 1
print(dict(c))
if '-v' in sys.argv: print(oth.most_common(15)); print(still.most_common(20))
