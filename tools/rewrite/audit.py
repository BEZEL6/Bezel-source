#!/usr/bin/env python3
"""Reference audit: include / expression / variable definitions vs uses (XML + Python strings).
usage: audit.py <skin>  -> prints unused names per kind; --json out.json"""
import sys, os, re, glob, json
from lxml import etree
S = sys.argv[1]; X = S + '/xml'
P = etree.XMLParser(remove_comments=True, huge_tree=True)
defs = {'include': {}, 'expression': {}, 'variable': {}}
texts = {}
for f in sorted(glob.glob(X + '/*.xml')):
    t = etree.parse(f, P); fn = os.path.basename(f)
    texts[fn] = etree.tostring(t, encoding='unicode')
    for e in t.iter('include', 'expression', 'variable'):
        n = e.get('name')
        if n and e.getparent() is not None and e.getparent().tag == 'includes':
            defs[e.tag].setdefault(n, []).append((fn, e.sourceline))
py = ''.join(open(f, encoding='utf-8', errors='replace').read() for f in glob.glob(S + '/scripts/*.py') + glob.glob(S + '/scripts/*.json'))
alltxt = '\n'.join(texts.values())
used = {k: set() for k in defs}
# includes: <include>NAME</include>, content="NAME", and any token appearing as a param value / text that names an include
for m in re.finditer(r'<include(?:\s[^>]*)?>([^<]+)</include>', alltxt): used['include'].add(m.group(1).strip())
for m in re.finditer(r'<include[^>]*\scontent="([^"]+)"', alltxt): used['include'].add(m.group(1).strip())
dyn = set(re.findall(r'[\w.]+', ' '.join(re.findall(r'(?:value|default)="([^"]*)"', alltxt))))
for m in re.finditer(r'\$EXP\[([^\]\s,]+)', alltxt + py): used['expression'].add(m.group(1))
for m in re.finditer(r'\$VAR\[([^\]\s,]+)', alltxt + py): used['variable'].add(m.group(1))
out = {}
for k, d in defs.items():
    un = []
    for n in sorted(d):
        if n in used[k]: continue
        if re.search(r'(?<![\w$])%s(?![\w])' % re.escape(n), py): continue          # named in Python / json
        if k == 'include' and n in dyn: continue                                      # passed as a param value (dynamic include)
        un.append(n)
    out[k] = {n: d[n] for n in un}
    print(k, 'defined', len(d), 'unused', len(un))
if '--json' in sys.argv: json.dump(out, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
if '-v' in sys.argv:
    for k in out: print(k, sorted(out[k])[:400])
