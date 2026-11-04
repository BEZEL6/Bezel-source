#!/usr/bin/env python3
"""Remove named top-level definitions (<include name=..>, <expression name=..>, <variable name=..>) from skin XML text,
keeping everything else byte-identical. usage: rmdefs.py <xml dir> dead.json kind[,kind] [--apply]"""
import sys, re, json, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'geom455')); import xedit
XD, J, kinds = sys.argv[1], json.load(open(sys.argv[2])), sys.argv[3].split(',')
byfile = {}
for k in kinds:
    for n, locs in J[k].items():
        for fn, line in locs: byfile.setdefault(fn, []).append((k, n))
tot = 0
for fn, items in byfile.items():
    p = os.path.join(XD, fn); text = open(p, encoding='utf-8').read()
    toks = xedit.tokens(text); spans = []
    want = {(k, n) for k, n in items}
    for i, m in enumerate(toks):
        if m.group(1) or m.group(2) not in kinds: continue
        nm = re.search(r'\sname="([^"]+)"', m.group(3) or '')
        if not nm or (m.group(2), nm.group(1)) not in want: continue
        if m.group(4): spans.append((m.start(), m.end())); continue          # self-closing
        depth = 0
        for mm in toks[i:]:
            if mm.group(2) != m.group(2) or mm.group(4): continue
            depth += -1 if mm.group(1) else 1
            if depth == 0: spans.append((m.start(), mm.end())); break
    assert len(spans) == len(want), (fn, len(spans), len(want))
    # also swallow the whitespace / newline right after, when the definition sits on its own line
    out = text
    for a, b in sorted(spans, reverse=True):
        ls = out.rfind('\n', 0, a) + 1
        if out[ls:a].strip() == '' and out[b:out.find('\n', b) if out.find('\n', b) != -1 else len(out)].strip() == '':
            e = out.find('\n', b); e = len(out) if e == -1 else e + 1; a = ls; b = e
        out = out[:a] + out[b:]
    tot += len(spans)
    print(fn, len(spans), 'removed', len(text) - len(out), 'bytes')
    if '--apply' in sys.argv: open(p, 'w', encoding='utf-8').write(out)
print('total', tot)
