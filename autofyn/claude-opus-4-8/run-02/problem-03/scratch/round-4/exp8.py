from fractions import Fraction as Fr
import random
exec(open('exp4.py').read().split('for pieces')[0])
def strat_subsetsum(pieces):
    p=sorted(pieces,reverse=True); l1=p[0]; others=p[1:]
    sums={Fr(0)}
    for x in others:
        ns=set()
        for s in sums:
            ns.add(s)
            if s+x<=l1: ns.add(s+x)
        sums=ns
    return l1-max(sums)
random.seed(11)
k=3; uk=u(k); ck=c(k); worst=Fr(0); winst=None
for _ in range(20000):
    cuts=sorted(Fr(random.randint(1,999),1000) for _ in range(k))
    pts=[Fr(0)]+cuts+[Fr(1)]
    pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
    if any(p==0 for p in pieces):continue
    l1,l2=pieces[0],pieces[1]
    if not(l1<ck and 2*l2<ck):continue
    r=strat_subsetsum(pieces)
    if r/uk>worst: worst=r/uk; winst=pieces
print("worst subsetsum CaseIII k=3 ratio",float(worst),"inst",[float(x) for x in winst])
r,tr=eval_trace(tuple(winst),3,{})
print("optimal residual/u3=",float(r/uk))
for mv in tr: print("  ",mv)
print("subsetsum residual/u3=",float(strat_subsetsum(winst)/uk))
