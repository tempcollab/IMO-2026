from fractions import Fraction as Fr
from probe_star import ladder, partitions_of
from probe_major import colored
from probe_bottom import level_form
import random

# confirm HLP threshold form equivalent & robust; find which t are tight at ties
for n in range(1,7):
    L=ladder(n); tot=2**n; bad=0; ex=None
    for pi in partitions_of(tot,n+1):
        for tb in (True,False):
            bo,re=colored(pi,L,tb)
            ok,info=level_form(bo,re)
            if not ok:
                bad+=1
                if ex is None: ex=(pi,tb,info); 
    print(f"n={n}: HLP threshold-form fails={bad}, ex={ex}")
# fractional
print("--- frac ---")
for n in range(2,8):
    L=ladder(n); tot=2**n; bad=0; trials=20000
    for _ in range(trials):
        r=random.randint(1,n+1)
        cuts=sorted(random.randint(1,tot*8-1) for _ in range(r-1))
        pts=[0]+cuts+[tot*8]; pi=[Fr(pts[i+1]-pts[i],8) for i in range(r)]
        if any(p<=0 for p in pi): continue
        for tb in (True,False):
            bo,re=colored(pi,L,tb)
            ok,_=level_form(bo,re)
            if not ok: bad+=1; break
    print(f"n={n}: frac HLP fails={bad}/{trials}")
