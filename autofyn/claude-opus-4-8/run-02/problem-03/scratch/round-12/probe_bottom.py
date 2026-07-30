from fractions import Fraction as Fr
from probe_star import ladder, partitions_of
from probe_ballot import merged
import random

# bottom-up prefix scan (smallest first): running (blue_odd - red_even) over suffix from bottom
def bottomup_min(reds,blues,tb=True):
    elems=merged(reds,blues,tb)  # descending
    N=len(elems)
    bo=Fr(0); re=Fr(0); mn=Fr(0)
    for j in range(N-1,-1,-1):
        v,c=elems[j]; rank=j+1
        if c=='b' and rank%2==1: bo+=v
        if c=='r' and rank%2==0: re+=v
        if bo-re<mn: mn=bo-re
    return mn

# level-threshold form of weak-majorization: for all t, sum_bo (v-t)^+ >= sum_re (v-t)^+
def level_form(bo,re):
    vals=sorted(set(bo+re))
    for t in vals+[Fr(0)]:
        a=sum(v-t for v in bo if v>t)
        b=sum(v-t for v in re if v>t)
        if a<b: return False,(t,a,b)
    return True,None

from probe_major import colored
for n in range(1,7):
    L=ladder(n); tot=2**n
    bu_min=Fr(0); tightk_all=True
    for pi in partitions_of(tot,n+1):
        for tb in (True,False):
            m=bottomup_min(pi,L,tb)
            if m<bu_min: bu_min=m
    print(f"n={n}: bottom-up prefix min margin={bu_min}")
