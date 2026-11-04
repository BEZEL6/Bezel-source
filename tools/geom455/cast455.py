import sys,re
p=sys.argv[1]; L=open(p).read().split('\n')
def edit(i,pairs,expect):
    s=L[i-1]; n=0
    for a,b in pairs:
        c=s.count(a); n+=c; s=s.replace(a,b)
    assert n==expect,(i,n,expect); L[i-1]=s
# album cast (BezelAlbumCast) 1033..1063
s=L[1032]; assert '<left>570</left><top>0</top><width>390</width>' in s
L[1032]=s.replace('<left>570</left><top>0</top><width>390</width>','<left>660</left><top>0</top><width>390</width>',1)
assert L[1033].count('<left>-570</left>')==1; L[1033]=L[1033].replace('<left>-570</left>','<left>-660</left>')
tot=0
for i in range(1034,1063):
    a=L[i].count('center="960,520"')+L[i].count('<left>480</left>'); tot+=a
    L[i]=L[i].replace('center="960,520"','center="1050,520"').replace('<left>480</left>','<left>570</left>')
assert tot==58,tot
# poster cast 2794..2799
for i,exp in ((2794,7),(2797,1),(2798,1),(2799,7)):
    edit(i,[('center="960,570"','center="1050,570"'),('<left>480</left>','<left>570</left>')],exp)
open(p,'w').write('\n'.join(L)); print('ok')
