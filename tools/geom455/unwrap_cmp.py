#!/usr/bin/env python3
"""zero-diff when B adds P1B wrapper groups: drop wrappers (source tag followed by <left>bz_strip_x</left><!-- P1B -->),
re-parent their children, then compare like zerodiff (ZD_GROUPS semantics). usage: unwrap_cmp.py a.json b.json <xmlB>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__)); import xedit
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); XD = sys.argv[3]
mark = {}
def iswrap(o):
    fn, tag, k = o.split('#')
    if fn not in mark:
        t = open(os.path.join(XD, fn), encoding='utf-8').read()
        st = [m for m in xedit.tokens(t) if m.group(2) == 'control' and not m.group(1)]
        mark[fn] = set(i for i, m in enumerate(st) if t.startswith('<left>bz_strip_x</left><!-- P1B -->', m.end()))
    return int(k) in mark[fn]
Bf = [r for r in B if not (r['type'] == 'group' and r['o'] and iswrap(r['o']))]
print('B', len(B), 'wrappers', len(B) - len(Bf), 'A', len(A))
assert len(Bf) == len(A)
def cabs(r):
    out = []
    for co, c, eff, k in r['cents']:
        a = c.split(',')
        try: out.append(round(r['px'] + float(a[0]), 2))
        except ValueError: out.append(c)
        out.append(a[1].strip() if len(a) > 1 else '')
    return out
bad = grp = 0
for a, b in zip(A, Bf):
    same = (a['win'], a['type'], a['src'].split(':')[0]) == (b['win'], b['type'], b['src'].split(':')[0])
    if not same: print('ORDER', a['win'], a['src'], b['src']); bad += 1; break
    if round(a['x0'], 2) != round(b['x0'], 2) or (a['x1'] is None) != (b['x1'] is None) or (a['x1'] is not None and round(a['x1'], 2) != round(b['x1'], 2)) or cabs(a) != cabs(b):
        if a['type'] == 'group' and cabs(a) == cabs(b): grp += 1; continue
        bad += 1
        if bad <= 12: print('DIFF', a['win'], a['src'], b['src'], a['x0'], b['x0'], a['x1'], b['x1'], cabs(a), cabs(b))
print('controls', len(A), 'changed', bad, 'groups moved', grp)
sys.exit(1 if bad else 0)
