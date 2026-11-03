import re,sys,collections
src=open(sys.argv[1]).read()
TR=['bz_sway_go','bz_sway_pulse','bz_sway_pulse2','bz_big_go','bz_big_pulse']
rows=[]
for m in re.finditer(r'<animation\b([^>]*)>(.*?)</animation>',src,re.S):
    a=m.group(1); c=re.search(r'condition="([^"]*)"',a)
    if not c: continue
    cond=c.group(1)
    if not any(t in cond for t in TR): continue
    line=src.count('\n',0,m.start())+1
    body=m.group(2)
    eff=re.findall(r'<effect ([^/]*)/>',body)
    times=[ (re.search(r'type="(\w+)"',e).group(1) if 'type=' in e else '?', re.search(r'time="(\d+)"',e).group(1) if 'time=' in e else '0', (re.search(r'delay="(\d+)"',e) or [0,'0'])[1]) for e in eff]
    if not eff:
        times=[(re.search(r'effect="(\w+)"',a).group(1) if 'effect=' in a else '?',(re.search(r'time="(\d+)"',a) or [0,'0'])[1],(re.search(r'delay="(\d+)"',a) or [0,'0'])[1])]
    pulse='pulse="true"' in a
    key=re.sub(r'\s+','',cond)
    rows.append((line,pulse,key,times))
g=collections.defaultdict(list)
for r in rows: g[r[2]].append(r)
for k,v in sorted(g.items(),key=lambda x:x[1][0][0]):
    print('COND',k[:230]); 
    for line,p,_,t in v: print('   L%-5d pulse=%d %s'%(line,p,t))
