import re,sys
p=sys.argv[1]; L=open(p).read().split('\n')
s=next(i for i,l in enumerate(L) if '<control type="group" id="6706">' in l)
e=next(i for i,l in enumerate(L) if 'strip_edge.png</texture></control><!-- BETA 2.4 item 10: flush with the bottom' in l)
X=lambda x: 1080+(x-990)*0.9
Y=lambda y: 570+(y-570)*0.9
def fmt(v): return str(int(round(v)))
cnt={'l':0,'t':0,'w':0,'h':0}
for i in range(s,e+1):
    line=L[i]
    edge='strip_edge.png' in line
    def ctl(m):
        c=m.group(0)
        isimg=c.startswith('<control type="image"')
        def sub(tag,f):
            nonlocal c
            def r(mm):
                cnt[tag[0]]+=1; return '<%s>%s</%s>'%(tag,f(float(mm.group(1))),tag)
            c=re.sub(r'<%s>(-?[0-9.]+)</%s>'%(tag,tag),r,c,count=1)
        sub('left',lambda v: fmt(X(v)))
        sub('width',lambda v: fmt(v*0.9))
        if not edge:
            sub('top',lambda v: fmt(Y(v)))
            if isimg: sub('height',lambda v: fmt(v*0.9))
        return c
    # operate per leaf control opening..first child-closing; controls here are single-line leaf images/labels
    L[i]=re.sub(r'<control type="(?:image|label)">.*?</control>',ctl,line)
open(p,'w').write('\n'.join(L)); print(s+1,e+1,cnt)
t=open(p.replace('Includes_Bezel','Includes_Tuner')).read()
a=t.index('<include name="BezelATEpSlideDown">'); b=t.index('</include>',t.index('<include name="BezelATEpSlideUp">'))
seg=t[a:b]; n1=seg.count('start="0,526"'); n2=seg.count('start="0,-526"')
seg=seg.replace('start="0,526"','start="0,473"').replace('start="0,-526"','start="0,-473"')
open(p.replace('Includes_Bezel','Includes_Tuner'),'w').write(t[:a]+seg+t[b:]); print('slides',n1,n2)
