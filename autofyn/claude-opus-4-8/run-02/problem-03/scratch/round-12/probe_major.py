from fractions import Fraction as Fr
from probe_star import ladder, partitions_of
from probe_ballot import merged

def colored(reds,blues,tb=True):
    elems=merged(reds,blues,tb)
    bo=[]; re=[]
    for j,(v,c) in enumerate(elems):
        rank=j+1
        if c=='b' and rank%2==1: bo.append(v)
        if c=='r' and rank%2==0: re.append(v)
    return bo, re

def top_major(bo,re):
    # descending partial sums: does blue-odd dominate red-even from the top?
    bo=sorted(bo,reverse=True); re=sorted(re,reverse=True)
    ps_bo=0; ps_re=0; ok=True
    for k in range(len(re)):
        ps_re+=re[k]
        ps_bo=sum(bo[:k+1]) if k<len(bo) else sum(bo)
        if ps_bo<ps_re: ok=False
    return ok

for n in range(1,7):
    L=ladder(n); tot=2**n
    bad=0; ex=None
    for pi in partitions_of(tot,n+1):
        for tb in (True,False):
            bo,re=colored(pi,L,tb)
            if not top_major(bo,re):
                bad+=1
                if ex is None: ex=(pi,tb,sorted(bo,reverse=True),sorted(re,reverse=True))
                break
    print(f"n={n}: top-majorization fails={bad}, ex={ex}")
