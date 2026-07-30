from fractions import Fraction as Fr
from probe_star import ladder, partitions_of
from probe_ballot import merged

def prefix_margins(reds, blues, tb=True):
    elems=merged(reds,blues,tb)
    bo=Fr(0); re=Fr(0); mn=Fr(0)
    seq=[]
    for j,(v,c) in enumerate(elems):
        rank=j+1
        if c=='b' and rank%2==1: bo+=v
        if c=='r' and rank%2==0: re+=v
        m=bo-re
        seq.append(m)
        if m<mn: mn=m
    return mn, bo-re

for n in range(1,7):
    L=ladder(n); tot=2**n
    globalmin_bf=Fr(0); globalmin_rf=Fr(0)
    tightcfg=None
    for pi in partitions_of(tot, n+1):
        mn_bf,fin=prefix_margins(pi,L,True)
        mn_rf,_=prefix_margins(pi,L,False)
        if mn_bf<globalmin_bf: globalmin_bf=mn_bf
        if mn_rf<globalmin_rf: globalmin_rf=mn_rf
        if mn_bf<=Fr(-1) and tightcfg is None: tightcfg=pi
    print(f"n={n}: min prefix margin (blue-first)={globalmin_bf}, (red-first)={globalmin_rf}, sample tight={tightcfg}")
