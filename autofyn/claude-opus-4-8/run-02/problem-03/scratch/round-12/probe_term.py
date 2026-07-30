from fractions import Fraction as Fr
from probe_star import ladder, partitions_of
from probe_ballot import merged
from probe_major import colored
import random

def termwise(bo,re):
    bo=sorted(bo,reverse=True); re=sorted(re,reverse=True)
    if len(re)>len(bo): return False, ("count",len(bo),len(re))
    for k in range(len(re)):
        if bo[k]<re[k]: return False, (k,bo[k],re[k])
    return True, None

# integer exhaustive
for n in range(1,7):
    L=ladder(n); tot=2**n
    bad=0; ex=None
    for pi in partitions_of(tot,n+1):
        for tb in (True,False):
            bo,re=colored(pi,L,tb)
            ok,info=termwise(bo,re)
            if not ok:
                bad+=1
                if ex is None: ex=(pi,tb,sorted(bo,reverse=True),sorted(re,reverse=True),info)
                break
    print(f"n={n}: termwise fails={bad}, ex={ex}")

print("--- fractional ---")
for n in range(2,9):
    L=ladder(n); tot=2**n; bad=0; ex=None; trials=30000
    for _ in range(trials):
        r=random.randint(1,n+1)
        cuts=sorted(random.randint(1,tot*12-1) for _ in range(r-1))
        pts=[0]+cuts+[tot*12]
        pi=[Fr(pts[i+1]-pts[i],12) for i in range(r)]
        if any(p<=0 for p in pi): continue
        for tb in (True,False):
            bo,re=colored(pi,L,tb)
            ok,info=termwise(bo,re)
            if not ok:
                bad+=1
                if ex is None: ex=(pi,tb,info)
                break
    print(f"n={n}: frac termwise fails={bad}/{trials}, ex={ex}")
