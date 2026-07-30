from fractions import Fraction as Fr
import random, itertools
exec(open('exp1.py').read().split('# random')[0])

def min_signed(pieces):
    p=list(pieces); m=len(p)
    best=None
    for signs in itertools.product([1,-1],repeat=m-1):
        s=p[0]+sum(sg*p[i+1] for i,sg in enumerate(signs))
        a=abs(s)
        if best is None or a<best: best=a
    return best

random.seed(21)
for k in range(2,8):
    uk=u(k);ck=c(k)
    worst=Fr(0); worstlo=Fr(0); cntlo=0; worstinst=None
    for _ in range(3000):
        cuts=sorted(Fr(random.randint(1,999),1000) for _ in range(k))
        pts=[Fr(0)]+cuts+[Fr(1)]
        pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
        if any(p==0 for p in pieces):continue
        l1,l2=pieces[0],pieces[1]
        if not(l1<ck and 2*l2<ck):continue
        r=min_signed(pieces)
        ratio=r/uk
        if ratio>worst: worst=ratio; worstinst=pieces
        if l1<Fr(1,2):
            cntlo+=1; worstlo=max(worstlo,ratio)
    print(f"k={k}: CaseIII min|signed sum| worst={float(worst):.4f}  (beta<1/2 n={cntlo} worst={float(worstlo):.4f})")
    if worst>1: print("   inst:",[float(x) for x in worstinst])
