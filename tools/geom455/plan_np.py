# NP in-place / FS meta / Up Next panel: column 150..930 inside the 120..960 block -> 150..1020
import json,sys,collections
sys.path.insert(0,'tools')
A=json.load(open(sys.argv[1])); B=json.load(open(sys.argv[2]))
out={}
for a,b in zip(A,B):
    f,l=a['src'].split(':'); l=int(l)
    if f!='Includes_Bezel.xml' or not (3049<=l<=3280) or a['x1'] is None: continue
    if a['win'] not in ('MusicVisualisation.xml','Custom_1112_NowPlaying.xml','Custom_1121_MusicFanartFS.xml'): continue
    moved = round(b['x0']-a['x0'])!=0 or round(b['x1']-a['x1'])!=0
    if moved: continue
    x0,x1=a['x0'],a['x1']
    if x1-x0>1000 or x1<900 or x1>960.5: continue
    if 148<=x0<=156 and a['wo']:
        key=('W',a['wpo'] or a['wo'])
    elif x0>156 and a['lo']:
        key=('L',a['lpo'] or a['lo'])
    else:
        key=('?',a['o'])
    out.setdefault(key,set()).add((a['src'],a['type'],round(x0),round(x1)))
for k,v in sorted(out.items()): print(k,sorted(v))
json.dump([list(k) for k in out],open('/tmp/np_keys.json','w'))
