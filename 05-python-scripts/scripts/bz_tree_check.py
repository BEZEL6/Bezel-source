# 5.33.389 dev-only: asserts Includes_Bezel Settings-tree branches == bz_flip SETTINGS_TREE. Run: python3 scripts/bz_tree_check.py
import re, os, ast, sys
d = os.path.dirname(os.path.abspath(__file__)); x = open(os.path.join(d, '..', 'xml', 'Includes_Bezel.xml')).read()
py = open(os.path.join(d, 'bz_flip.py')).read()
tree = ast.literal_eval(re.search(r'SETTINGS_TREE = (\(.*?\n    \))', py, re.S).group(1))
ok = True
for b, ws in tree:
    m = re.search(r'<expression name="bz_set_%s">(.*?)</expression>' % b, x)
    xs = tuple(re.findall(r'Window\.IsActive\(([^)]+)\)', m.group(1))) if m else None
    if xs != ws: ok = False; print('MISMATCH', b, xs, ws)
root = re.search(r'<expression name="bz_setkids">(.*?)</expression>', x).group(1)
if sorted(re.findall(r'bz_set_(\w+)', root)) != sorted(b for b, _ in tree): ok = False; print('ROOT MISMATCH', root)
# 5.33.390 ART_TREE: every registered prop must be used by bz_flip outside the registry
art = ast.literal_eval(re.search(r'ART_TREE = (\(.*?\n    \))', py, re.S).group(1))
body = py.replace(re.search(r'ART_TREE = \(.*?\n    \)', py, re.S).group(0), '')
for b, ks in art:
    for k in ks:
        if "'%s'" % k not in body and k[:-1] not in body: ok = False; print('ART UNUSED', b, k)
print('OK' if ok else 'FAIL'); sys.exit(0 if ok else 1)
