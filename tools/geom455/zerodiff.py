#!/usr/bin/env python3
"""Zero-diff check: control x boxes and absolute animation centres identical. usage: zerodiff.py a.json b.json"""
import json, sys
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
if len(A) != len(B): print('COUNT', len(A), len(B)); sys.exit(1)
def cabs(r):
    out = []
    for co, c, eff, k in r['cents']:
        a = c.split(',')
        try: out.append(round(r['px'] + float(a[0]), 2))
        except ValueError: out.append(c)
        out.append(a[1].strip() if len(a) > 1 else '')
    return out
bad = 0; grp = 0
import os
IGN = os.environ.get('ZD_GROUPS') == '1'
for a, b in zip(A, B):
    if (a['win'], a['type']) != (b['win'], b['type']) or round(a['x0'], 2) != round(b['x0'], 2) or \
       (a['x1'] is None) != (b['x1'] is None) or (a['x1'] is not None and round(a['x1'], 2) != round(b['x1'], 2)) or cabs(a) != cabs(b):
        if IGN and a['type'] == 'group' and cabs(a) == cabs(b): grp += 1; continue
        bad += 1
        if bad <= 15: print('DIFF', a['win'], a['src'], b['src'], a['x0'], b['x0'], a['x1'], b['x1'], cabs(a), cabs(b))
print('controls', len(A), 'changed', bad, 'groups moved (draw nothing)', grp)
sys.exit(1 if bad else 0)
