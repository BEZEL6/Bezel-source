import json,collections,sys,os,shutil
sys.path.insert(0,'tools'); import xedit
G=json.load(open(sys.argv[1])); DST=sys.argv[2]; XCL=set(sys.argv[3].split(',')) if len(sys.argv)>3 and sys.argv[3] else set()
byid={r['id_']:r for r in G}
from rules import *
prep(G if "G" in dir() else A); fam=fam(G if "G" in dir() else A)
def anc(r):
    p=r['pid']
    while p!=-1:
        yield byid[p]; p=byid[p]['pid']
edits=collections.defaultdict(dict)   # file -> {(kind,k): (delta, why)}
manual=[]; conflicts=[]
def add(o, kind, delta, why, r, po=None):
    if po:
        o, where = po.split('@'); kind = 'param@' + where
    f,tag,k=o.split('#'); key=(kind,int(k))
    old=edits[f].get(key)
    if old and old[0]!=delta: conflicts.append((f,key,old,delta,why,r['win']))
    edits[f][key]=(delta,why)
def cen(r, delta, why):
    for co,cv,eff,_ in r['cents']:
        f,_,k=co.split('#'); key=('c',int(k))
        old=edits[f].get(key)
        if old and old[0]!=delta: conflicts.append((f,key,old,delta,why,r['win']))
        edits[f][key]=(delta,why)
for r in G:
    if r['win'] not in fam: continue
    if r['o'] and r['o'] in XCL: continue
    if S(r):
        A=list(anc(r))
        if any(S(a) for a in A): continue
        # inside layouts of a non-S list -> list content, skip
        if any(a['type'] in LISTS for a in A): 
            if not any(S(a) for a in A): continue
        if any((a['o'] or '') in XCL for a in A): continue
        if r['lo'] and r['lval'] and xedit_num(r['lval']) if False else (r['lo'] and r['lval'] and r['lval'].lstrip('-').replace('.','',1).isdigit()):
            add(r['lo'],'left',90,'S',r,r.get('lpo')); cen(r,90,'S')
        elif not r['lo'] and r['ro'] :
            add(r['ro'],'right',-90,'S',r); cen(r,90,'S')
        else: manual.append(('S',r['win'],r['src'],r['type'],round(r['x0']),round(box(r)[1]),r['lval'],r['o']))
    elif E(r):
        A=list(anc(r))
        if any(E(a) for a in A) and not r['wo']: continue
        if any((a['o'] or '') in XCL for a in A): continue
        if r['wo'] and r['wval'] and r['wval'].replace('.','',1).isdigit(): add(r['wo'],'width',90,'E',r,r.get('wpo'))
        elif r['ro'] and not r['wo']: add(r['ro'],'right',-90,'E',r)
        else: manual.append(('E',r['win'],r['src'],r['type'],round(r['x0']),round(box(r)[1]),r['wval'],r['o']))
json.dump({'manual':manual,'conflicts':[list(map(str,c)) for c in conflicts]},open('/tmp/plan_extra.json','w'),indent=0)
print('files',len(edits),'edits',sum(len(v) for v in edits.values()),'manual',len(manual),'conflicts',len(conflicts))
for c in conflicts[:30]: print('CONFLICT',c)
SKIP=[]
if DST:
    for f,ed in edits.items():
        p=os.path.join(DST,f)
        def op(d, f=f, kk=None):
            def g(s):
                h=s.strip().split(',')[0]
                try: v=float(h)
                except Exception:
                    SKIP.append((f,s)); return s
                return xedit.fmt(v+d)+(','+s.split(',',1)[1] if ',' in s else '')
            return g
        xedit.apply(p,[(kind,k,op(d)) for (kind,k),(d,why) in ed.items()])
    json.dump({f:{'%s:%d'%k:v for k,v in ed.items()} for f,ed in edits.items()},open('/tmp/plan_edits.json','w'))

print('skipped non-numeric', SKIP)
