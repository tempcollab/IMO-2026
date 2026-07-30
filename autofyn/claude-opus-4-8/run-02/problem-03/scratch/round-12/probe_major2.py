from fractions import Fraction as Fr
from probe_star import ladder
from probe_ballot import merged
from probe_major import colored, top_major
import random

# fractional stress test
for n in range(2,9):
    L=ladder(n); tot=2**n
    bad=0; ex=None
    trials=40000
    for _ in range(trials):
        r=random.randint(1,n+1)
        # random partition of 2^n into r positive fractional parts on grid /12
        cuts=sorted(random.randint(1,tot*12-1) for _ in range(r-1))
        pts=[0]+cuts+[tot*12]
        pi=[Fr(pts[i+1]-pts[i],12) for i in range(r)]
        if any(p<=0 for p in pi): continue
        for tb in (True,False):
            bo,re=colored(pi,L,tb)
            if not top_major(bo,re):
                bad+=1
                if ex is None: ex=(pi,tb,sorted(bo,reverse=True),sorted(re,reverse=True))
                break
    print(f"n={n}: fractional top-major fails={bad}/{trials}, ex={ex}")
