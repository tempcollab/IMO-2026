from fractions import Fraction as Fr
from probe_star import ladder, partitions_of, Dtilde_from_merge
import random

def merged(reds,blues, tiebreak_blue_first=True):
    order = 0 if tiebreak_blue_first else 1
    elems=[(v,'b') for v in blues]+[(v,'r') for v in reds]
    # descending; tie: blue first if flag
    elems.sort(key=lambda x:(-x[0], 0 if x[1]=='b' else 1) if tiebreak_blue_first else (-x[0], 1 if x[1]=='b' else 0))
    return elems

def prefix_test(reds, blues, tb=True):
    elems=merged(reds,blues,tb)
    bo=Fr(0); re=Fr(0); minmargin=None
    for j,(v,c) in enumerate(elems):
        rank=j+1
        if c=='b' and rank%2==1: bo+=v
        if c=='r' and rank%2==0: re+=v
        m=bo-re
        if minmargin is None or m<minmargin: minmargin=m
    return minmargin  # want >=0 for ballot property

for n in range(1,7):
    L=ladder(n); tot=2**n
    worst_true=None; worst_false=None
    cntbad=0; total=0
    for pi in partitions_of(tot, n+1):
        total+=1
        mm_bf=prefix_test(pi,L,True)
        mm_rf=prefix_test(pi,L,False)
        # ballot holds if for SOME tiebreak min>=0
        if mm_bf<0 and mm_rf<0:
            cntbad+=1
            if worst_false is None or max(mm_bf,mm_rf)>worst_false[0]:
                worst_false=(max(mm_bf,mm_rf),pi)
    print(f"n={n}: total={total}, ballot-fails(both tiebreaks)={cntbad}, worst={worst_false}")
