LISTS=('list','fixedlist','wraplist','panel','epggrid')
SR={'DialogContextMenu.xml':1020}
NOAUTO={'Custom_1122_BigAlbum.xml'}
EXTRA_FAM=set()
def box(r): return r['x0'], (r['x1'] if r['x1'] is not None else r['x0'])
def S(r):
    x0,x1=box(r); e=SR.get(r['win'],960); return 569.5<=x0<e+0.5 and x1<=e+0.5 and x1>x0
def E(r):
    x0,x1=box(r); return 119.5<=x0<=120.5 and abs(x1-960)<0.6
def fam(G):
    f=set(r['win'] for r in G if abs(r['x0']-570)<0.6 and r['x1'] and abs(r['x1']-960)<0.6)
    return (f|EXTRA_FAM)-NOAUTO

GS=set()
def prep(G):
    import collections
    kids=collections.defaultdict(list)
    for r in G: kids[r['pid']].append(r)
    def desc(r):
        for k in kids[r['id_']]:
            yield k; yield from desc(k)
    for r in G:
        if r['type'] in ('group','grouplist') and not r['wo'] and r['lo'] and 569.5<=r['x0']<SR.get(r['win'],960):
            D=[d for d in desc(r) if d['x1'] is not None]
            if D and all(S(d) for d in D): GS.add(r['id_'])
_S=S
def S(r): return r['id_'] in GS or _S(r)
