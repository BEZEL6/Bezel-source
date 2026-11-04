import json,collections,sys
sys.path.insert(0,'tools')
A=json.load(open(sys.argv[1])); B=json.load(open(sys.argv[2]))
assert len(A)==len(B)
byid={r['id_']:r for r in A}
from rules import *
prep(G if "G" in dir() else A); fam=fam(G if "G" in dir() else A)
def anc(r):
    p=r['pid']
    while p!=-1:
        yield byid[p]; p=byid[p]['pid']
bad=collections.defaultdict(list); ok=collections.Counter()
for a,b in zip(A,B):
    d0=round(b['x0']-a['x0'],1); d1=round(box(b)[1]-box(a)[1],1)
    exp=(0,0)
    if a['win'] in fam:
        An=list(anc(a))
        inlist=any(x['type'] in LISTS and not S(x) for x in An)
        if S(a) and not inlist: exp=(90,90)
        elif any(S(x) for x in An) and not inlist: exp=(90,90)
        elif E(a): exp=(0,90)
    if (d0,d1)==exp: ok[exp]+=1; continue
    bad[(a['src'],a['type'],round(a['x0']),round(box(a)[1]),d0,d1,exp)].append(a['win'])
print(dict(ok))
for k,v in sorted(bad.items(), key=lambda kv:kv[0][0]): print(*k, len(v), sorted(set(v))[:3])
