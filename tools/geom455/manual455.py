import json,collections,sys,re,os
sys.path.insert(0,'tools'); import xedit
from rules import *
A=json.load(open(sys.argv[1])); D=sys.argv[2]
byid={r['id_']:r for r in A}
kids=collections.defaultdict(list)
for r in A: kids[r['pid']].append(r)
def desc(r):
    for k in kids[r['id_']]:
        yield k; yield from desc(k)
F=fam(A)
ED=collections.defaultdict(dict)  # file -> key -> delta (numeric add) or ('set',value)
LOG=[]
def addnum(o,delta,why):
    if '@' in o: base,where=o.split('@'); f,_,k=base.split('#'); key=('param@'+where,int(k))
    else: f,tag,k=o.split('#'); key=(tag,int(k))
    old=ED[f].get(key)
    if old is not None and old!=delta: raise SystemExit('conflict %s %s %s %s'%(f,key,old,delta))
    ED[f][key]=delta; LOG.append((why,f,key,delta))
def W(r,delta,why): addnum(r['wpo'] or r['wo'],delta,why)
def L(r,delta,why): addnum(r['lpo'] or r['lo'],delta,why)
ctl=lambda o: next(r for r in A if r['o']==o)
# ---- BLOCK fills widen 450 -> 540
for o in ['DialogPVRChannelsOSD.xml#control#2','EventLog.xml#control#2','FileManager.xml#control#1','Includes_Bezel.xml#control#108','Includes_Bezel.xml#control#115','Includes_Bezel.xml#control#152','Includes_Bezel.xml#control#380','Includes_BezelChooseArt.xml#control#12','Includes_BezelChooseArt.xml#control#35','Includes_BezelChooseArt.xml#control#58','Includes_BezelRefresh.xml#control#3','Includes_Tuner.xml#control#21','Includes_Tuner.xml#control#43','Includes_Tuner.xml#control#51','MyWeather.xml#control#13','SettingsProfile.xml#control#2','SettingsSystemInfo.xml#control#1','Includes_Bezel.xml#control#1483']:
    r=ctl(o); W(r,90,'BLOCK')
# 1486 shares param#740 with 1483 (listw default) -> covered
# ---- right panels: topmost gap controls
EXCL_SRC=('Includes.xml:',)
def gapc(r): return r['x1'] is not None and 959<=r['x0']<1139
tops=[]
for r in A:
    if r['win'] not in F or not gapc(r): continue
    if r['src'].startswith(EXCL_SRC): continue
    f,l=r['src'].split(':'); l=int(l)
    if f=='Includes_Bezel.xml' and (l==441 or 2615<=l<=2625 or 2715<=l<=2760 or 3300<=l<=3700 or 3778<=l<=3785): continue
    if f in ('Includes_BezelChooseArt.xml','SmartPlaylistEditor.xml','SmartPlaylistRule.xml','DialogPVRGuideSearch.xml'): continue
    p=r['pid']; top=True
    while p!=-1:
        if gapc(byid[p]): top=False;break
        p=byid[p]['pid']
    if top: tops.append(r)
done=set()
for r in tops:
    if r['o'] in done: continue
    done.add(r['o'])
    if not (r['lo'] or r['lpo']): print('NOLEFT',r['src'],r['type']); continue
    L(r,90,'PANEL')
    x1=r['x1']; w=r['x1']-r['x0']
    if (r['wo'] or r['wpo']) and w>=300 and x1>=1500: W(r,-90,'PANEL')
    for d in desc(r):
        if d['x1'] is None or not (d['wo'] or d['wpo']): continue
        dw=d['x1']-d['x0']
        if dw>=300 and abs(d['x1']-x1)<=45 and d['x0']<=r['x0']+60: W(d,-90,'PANEL')
# ---- explicit
X=[('Includes_Bezel.xml#left#457',45,'VIDBOX'),('Includes_Bezel.xml#left#458',45,'VIDBOX'),('Includes_Bezel.xml#width#546',-45,'VIDBOX'),
   ('Includes_Bezel.xml#left#459',90,'VIDBOX'),('Includes_Bezel.xml#width#547',-45,'VIDBOX'),
   ('Includes_Bezel.xml#width#1188',90,'FRAME'),('Includes_Bezel.xml#width#1189',90,'FRAME'),
   ('Includes_Bezel.xml#left#18',90,'ROOTHIDE'),('Includes_Bezel.xml#width#19',-90,'ROOTHIDE'),('Includes_Bezel.xml#left#19',90,'ROOTHIDE'),('Includes_Bezel.xml#width#20',-90,'ROOTHIDE'),('Includes_Bezel.xml#width#21',-90,'ROOTHIDE')]
for f in ('DialogPVRGuideSearch.xml','SmartPlaylistEditor.xml','SmartPlaylistRule.xml'):
    X+= [(f+'#width#1',90,'FRAME'),(f+'#width#2',90,'FRAME'),(f+'#left#4',90,'FRAME')]
for o,d,why in X: addnum(o,d,why)
json.dump({f:{'%s|%d'%k:v for k,v in e.items()} for f,e in ED.items()},open('/tmp/man_edits.json','w'))
for x in LOG: print(*x)
if D:
    for f,e in ED.items():
        def mk(d):
            return lambda s: xedit.fmt(float(s.strip())+d)
        xedit.apply(os.path.join(D,f),[(kind,k,mk(d)) for (kind,k),d in e.items()])

TXT=[('Includes_Bezel.xml','start="517,0" end="517,0"','start="620.84,0" end="620.84,0"',3),
     ('Includes_Bezel.xml','<param name="left" value="554"/>','<param name="left" value="644"/>',2),
     ('Includes_Bezel.xml','<param name="left" value="952"/>','<param name="left" value="1042"/>',1),
     ('Includes_Bezel.xml','start="-962,0" end="-962,0"','start="-1052,0" end="-1052,0"',1)]
if D:
    for f,a,b,n in TXT:
        p=os.path.join(D,f); t=open(p).read(); assert t.count(a)==n,(a,t.count(a)); open(p,'w').write(t.replace(a,b))
