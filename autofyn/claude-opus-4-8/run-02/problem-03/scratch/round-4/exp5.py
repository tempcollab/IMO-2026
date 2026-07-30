from fractions import Fraction as Fr
import random, itertools
exec(open('exp1.py').read().split('# random')[0])

def strat_subsetsum(pieces):
    # residual = l1 - max{sum(S): S subset of others, sum<=l1}
    p=sorted(pieces,reverse=True)
    l1=p[0]; others=p[1:]
    best=Fr(0)
    # subset sums <= l1, maximize
    sums={Fr(0)}
    for x in others:
        newsums=set()
        for s in sums:
            newsums.add(s)
            if s+x<=l1: newsums.add(s+x)
        sums=newsums
    return l1-max(sums)

random.seed(11)
for k in range(2,7):
    uk=u(k);ck=c(k)
    worstall=Fr(0); worstc3=Fr(0); cnt=0; cntc3=0
    worstinst=None
    for _ in range(4000):
        cuts=sorted(Fr(random.randint(1,999),1000) for _ in range(k))
        pts=[Fr(0)]+cuts+[Fr(1)]
        pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
        if any(p==0 for p in pieces):continue
        cnt+=1
        r=strat_subsetsum(pieces)
        ratio=r/uk
        if ratio>worstall: worstall=ratio; worstinst=pieces
        l1,l2=pieces[0],pieces[1]
        if l1<ck and 2*l2<ck:
            cntc3+=1
            worstc3=max(worstc3,ratio)
    print(f"k={k}: ALL cnt={cnt} worstratio={float(worstall):.4f} | CaseIII cnt={cntc3} worst={float(worstc3):.4f}")
    if worstall>1: print("   VIOL inst:",[float(x) for x in worstinst])
