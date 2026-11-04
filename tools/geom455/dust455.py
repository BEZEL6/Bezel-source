import re,sys
p=sys.argv[1]; t=open(p).read()
EDGES=(930,950,960)
pat=re.compile(r'<control type="grouplist"><left>(-?\d+)</left><top>(-?\d+)</top><width>(\d+)</width><height>(\d+)</height>(<orientation>vertical</orientation><itemgap>0</itemgap><scrolltime>0</scrolltime><control type="group"><left>0</left><top>0</top>)<width>(\d+)</width><height>(\d+)</height><animation effect="slide" start="(-?\d+),(-?\d+)" end="(-?\d+),(-?\d+)"')
log=[]
def r(m):
    x,y,w,h=int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4))
    x1=x+w; nx,nw=x,w
    if x1 in EDGES: nw=w+90
    elif x in EDGES: nx=x+90; nw=w-90
    else: return m.group(0)
    vis=''
    if nw<=0: nw=1; vis='<visible>false</visible>'
    log.append((x,y,w,h,'->',nx,nw))
    assert int(m.group(8))==-x and int(m.group(10))==-x
    return ('<control type="grouplist">%s<left>%d</left><top>%d</top><width>%d</width><height>%d</height>%s<width>%d</width><height>%s</height><animation effect="slide" start="%d,%s" end="%d,%s"'
            %(vis,nx,y,nw,h,m.group(5),nw,m.group(7),-nx,m.group(9),-nx,m.group(11)))
n=len(pat.findall(t)); t2=pat.sub(r,t); open(p,'w').write(t2)
print('grouplists',n); [print(*l) for l in log]
