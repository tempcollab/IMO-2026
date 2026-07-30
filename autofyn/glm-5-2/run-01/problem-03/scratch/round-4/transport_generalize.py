"""
Probe whether the transport/conservation structure generalizes.

KEY FINDING from vshape_plateau.py (T_3 cascade):
  - The linear path (q1,q2,q3) = (1-t)*minimizer + t*dyadic keeps D=1 throughout.
  - Mechanism: along the path, the "middle pieces" q1-q2=2, q2-q3=1 are CONSTANT
    (pair with tower 2,1), and only the two leftovers move: a=8-q1 (4.75->4),
    d=q3 (0.25->1), keeping a+d=5 conserved. D=(a+d)-4 = 5-4 = 1.
  - D=1 in cascade grid is ONE connected component (816 pts) containing dyadic.

Here:
A. Verify the conservation law D = (leftover_top + leftover_bot) - (straddled tower)
   for T_3 minimizer, and check the transport reaches dyadic.
B. Generalize to T_2: find odd-count minimizers, check transport to dyadic.
C. Generalize to T_4: find odd-count minimizers, check transport.
D. Check NON-cascade combinatorial types (split larger fragment, split tower piece):
   is D=1 still connected and dyadic-touching across types?
E. The "straddle" structure: for a general odd-group minimizer, do the two
   non-dyadic leftovers always straddle a tower piece with sum = tower + 1?
"""
from fractions import Fraction as F
import numpy as np
from collections import deque, Counter

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))
def is_pow2(x):
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            n = int(x); return n>0 and (n&(n-1))==0
        num, den = x.numerator, x.denominator
        return (num&(num-1))==0 and (den&(den-1))==0
    import math
    lg = math.log2(x) if x>0 else -1
    return abs(lg-round(lg))<1e-9 and round(lg)>=-20
def tower(n): return [F(2**(n-k)) for k in range(n+1)]
def Dtower(n): return alt_sum(tower(n))
def spine(cfg):
    s = sorted(cfg, reverse=True); c = Counter(s)
    return sorted([v for v in sorted(c,reverse=True) for _ in range(c[v]%2)], reverse=True)

# ============================================================
# A. T_3: conservation law at the minimizer
# ============================================================
print("="*70)
print("A. T_3 conservation law: D = (leftover_top + leftover_bot) - straddled tower")
print("="*70)
# minimizer spine {4.75, 4, 0.25}, D = 4.75 - 4 + 0.25 = 1
# leftovers 4.75, 0.25 straddle tower 4. sum = 5 = 4 + 1.
sp_m = [F(19,4), F(4), F(1,4)]
print(f"  spine {sp_m}: D = {alt_sum(sp_m)} = {float(alt_sum(sp_m))}")
print(f"  leftovers {sp_m[0]} + {sp_m[2]} = {sp_m[0]+sp_m[2]} = tower {sp_m[1]} + 1 = {sp_m[1]+1}")
print(f"  D = (sum leftovers) - (straddled tower) = {sp_m[0]+sp_m[2]} - {sp_m[1]} = {sp_m[0]+sp_m[2]-sp_m[1]}")

# Transport: fix sum = 5, move mass from top to bot until both dyadic.
print("  Transport (fix a+d=5, move a: 4.75 -> 4, d: 0.25 -> 1):")
for a in [F(19,4), F(9,2), F(17,4), F(4)]:
    d = F(5) - a
    sp = sorted([a, F(4), d], reverse=True)
    print(f"    a={a} d={d} spine={sp} D={alt_sum(sp)} dyadic={all(is_pow2(x) for x in sp)}")

# ============================================================
# B. T_2 = (4,2,1), D(T_2)=3, D*=1 (balanced pairs {2,2,1,1,1}).
# Odd-count minimizers? 2 splits. Cascade: 4 -> a+b -> a+(b-c)+c.
# ============================================================
print("\n" + "="*70)
print("B. T_2: odd-count minimizers and transport to dyadic")
print("="*70)
# T_2, 2 cascade splits: 4->(4-q1)+q1, then q1->(q1-q2)+q2.
# config = {4-q1, q1-q2, q2, 2, 1} sorted. D = alt_sum.
# dyadic: q1=2, q2=1 -> {2,2,1,1,1} wait that's 5 pieces but T_2+2splits = 3+2=5. {2,1,1,2,1}->{2,2,1,1,1} D=2-2+1-1+1=1. yes.
N=16
d1_t2 = []
all_t2 = []
for q1n in range(1, 2*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 2: continue
    q2max = q1/2
    k2 = 1
    while F(k2,N) <= q2max:
        q2 = F(k2,N)
        a = F(4)-q1; b = q1-q2; c = q2
        cfg = sorted([a,b,c,F(2),F(1)], reverse=True)
        D = alt_sum(cfg)
        all_t2.append((q1,q2,cfg,D))
        if D == 1: d1_t2.append((q1,q2,cfg))
        k2 += 1
print(f"  T_2 cascade grid 1/{N}: {len(all_t2)} configs, {len(d1_t2)} with D=1")
minD = min(D for _,_,_,D in all_t2)
print(f"  min D = {float(minD)}")
# dyadic among D=1
dyad = [(q1,q2,cfg) for q1,q2,cfg in d1_t2 if all(is_pow2(v) for v in cfg)]
print(f"  dyadic D=1 configs: {len(dyad)}: {dyad[:3]}")
# connectivity of D=1
d1_set = set((q1,q2) for q1,q2,_ in d1_t2)
if d1_set:
    start = next(iter(d1_set))
    step = F(1,N); visited={start}; dq=deque([start])
    while dq:
        c = dq.popleft()
        for dc in [(step,0),(-step,0),(0,step),(0,-step)]:
            nb=(c[0]+dc[0],c[1]+dc[1])
            if nb in d1_set and nb not in visited: visited.add(nb); dq.append(nb)
    print(f"  D=1 component from {start}: {len(visited)} pts (of {len(d1_set)} total)")
# find an odd minimizer (non-dyadic D=1)
odd_min = [(q1,q2,cfg) for q1,q2,cfg in d1_t2 if not all(is_pow2(v) for v in cfg)]
print(f"  non-dyadic D=1 configs: {len(odd_min)}")
for q1,q2,cfg in odd_min[:3]:
    sp = spine(cfg)
    print(f"    q1={float(q1)} q2={float(q2)} cfg={cfg} spine={sp} D(spine)={alt_sum(sp)}")
    # check straddle
    if len(sp)==3:
        print(f"      leftovers {sp[0]},{sp[2]} sum={sp[0]+sp[2]} straddle tower {sp[1]}? {sp[0]+sp[2]==sp[1]+1}")

# ============================================================
# C. T_4 = (16,8,4,2,1), D(T_4)=11, D*=1.
# 3 cascade splits on top: 16->(16-q1)+q1->...->q3+(q3-q4) wait 3 splits.
# Actually need 4 splits for full cascade. Let's do 3 cascade + check D.
# ============================================================
print("\n" + "="*70)
print("C. T_4: 3-cascade-split minimizers and transport")
print("="*70)
# T_4, 3 cascade splits: 16->(16-q1)+q1, q1->(q1-q2)+q2, q2->(q2-q3)+q3.
# config = {16-q1, q1-q2, q2-q3, q3, 8, 4, 2, 1} sorted. 8 pieces.
def cfg_T4_3cascade(q1,q2,q3):
    a=16-q1; b=q1-q2; c=q2-q3; d=q3
    return sorted([a,b,c,d,F(8),F(4),F(2),F(1)], reverse=True)
# dyadic: q1=8,q2=4,q3=2 -> {8,8,4,4,2,2,1,1}? wait. a=8,b=4,c=2,d=2 ->{8,4,2,2,8,4,2,1}={8,8,4,4,2,2,2,1}
#  Hmm. Let me just compute.
cfg_d = cfg_T4_3cascade(F(8),F(4),F(2))
print(f"  dyadic cascade (q1=8,q2=4,q3=2): {cfg_d} D={alt_sum(cfg_d)}")
# Actually balanced-pairs for T_4 is {8,8,4,4,2,2,1,1,1} (9 pieces, 4 splits). 3 splits gives 8 pieces.
# Let's just find the min over a grid.
N=8
minD=None; mincfg=None; d1=[]
for q1n in range(1,8*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>8: continue
    q2max=q1/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N); q3max=q2/2; k3=1
        while F(k3,N)<=q3max:
            q3=F(k3,N)
            cfg=cfg_T4_3cascade(q1,q2,q3); D=alt_sum(cfg)
            if minD is None or D<minD: minD=D; mincfg=cfg
            if D==1: d1.append((q1,q2,q3,cfg))
            k3+=1
        k2+=1
print(f"  T_4 3-cascade grid 1/{N}: min D = {float(minD)}")
print(f"  # D==1: {len(d1)}")
dyad=[(q1,q2,q3,cfg) for q1,q2,q3,cfg in d1 if all(is_pow2(v) for v in cfg)]
print(f"  dyadic D==1: {len(dyad)}")
for q1,q2,q3,cfg in dyad[:3]: print(f"    q1={q1} q2={q2} q3={q3} cfg={cfg}")
# a non-dyadic D=1
nd=[x for x in d1 if not all(is_pow2(v) for v in x[3])]
print(f"  non-dyadic D==1: {len(nd)}")
for q1,q2,q3,cfg in nd[:3]:
    sp=spine(cfg)
    print(f"    q1={float(q1)} q2={float(q2)} q3={float(q3)} spine={sp} D(sp)={alt_sum(sp)}")

# connectivity
if d1:
    d1_set=set((q1,q2,q3) for q1,q2,q3,_ in d1)
    start=next(iter(d1_set)); step=F(1,N); visited={start}; dq=deque([start])
    while dq:
        c=dq.popleft()
        for dc in [(step,0,0),(-step,0,0),(0,step,0),(0,-step,0),(0,0,step),(0,0,-step)]:
            nb=(c[0]+dc[0],c[1]+dc[1],c[2]+dc[2])
            if nb in d1_set and nb not in visited: visited.add(nb); dq.append(nb)
    dyadic_in = any((q1,q2,q3) in visited for q1,q2,q3,_ in dyad)
    print(f"  D=1 component: {len(visited)} of {len(d1_set)} pts; dyadic reachable: {dyadic_in}")

# ============================================================
# D. NON-cascade type for T_3: split LARGER fragment.
# 8 -> (8-q1)+q1, then split (8-q1) -> (8-q1-q2)+q2. (split the larger piece)
# config = {8-q1-q2, q2, q1, 4, 2, 1} sorted.
# ============================================================
print("\n" + "="*70)
print("D. T_3 NON-cascade type (split larger fragment): D=1 connectivity")
print("="*70)
def cfg_T3_split_larger(q1,q2):
    a=8-q1-q2; b=q2; c=q1  # fragments
    return sorted([a,b,c,F(4),F(2),F(1)], reverse=True)
N=16
d1_sl=[]; all_sl=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    # split larger (8-q1): q2 in (0, (8-q1)/2]
    q2max=(8-q1)/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N)
        cfg=cfg_T3_split_larger(q1,q2); D=alt_sum(cfg)
        all_sl.append((q1,q2,cfg,D))
        if D==1: d1_sl.append((q1,q2,cfg))
        k2+=1
minD_sl=min(D for _,_,_,D in all_sl)
print(f"  split-larger grid 1/{N}: {len(all_sl)} configs, min D={float(minD_sl)}, #D=1: {len(d1_sl)}")
dyad_sl=[(q1,q2,cfg) for q1,q2,cfg in d1_sl if all(is_pow2(v) for v in cfg)]
print(f"  dyadic D=1: {len(dyad_sl)}: {[(float(q1),float(q2)) for q1,q2,_ in dyad_sl[:3]]}")
# connectivity
if d1_sl:
    d1_set=set((q1,q2) for q1,q2,_ in d1_sl)
    start=next(iter(d1_set)); step=F(1,N); visited={start}; dq=deque([start])
    while dq:
        c=dq.popleft()
        for dc in [(step,0),(-step,0),(0,step),(0,-step)]:
            nb=(c[0]+dc[0],c[1]+dc[1])
            if nb in d1_set and nb not in visited: visited.add(nb); dq.append(nb)
    print(f"  D=1 component (split-larger): {len(visited)} of {len(d1_set)}; dyadic in: {any((q1,q2) in visited for q1,q2,_ in dyad_sl)}")

# ============================================================
# E. Cross-type: is D=1 connected ACROSS combinatorial types?
# Merge cascade and split-larger D=1 points, check if they share a boundary
# (a config reachable from both types = a tie config).
# ============================================================
print("\n" + "="*70)
print("E. Cross-type connectivity: do cascade and split-larger D=1 share a config?")
print("="*70)
# A config is reachable from both types if the split structure overlaps.
# Easiest: collect the actual SORTED configs from both, intersect.
cascade_cfgs = set(tuple(cfg) for _,_,cfg in d1 if True) if False else set()  # placeholder
# Actually use the d1 from section 3 (cascade) — recompute small
# Cascade D=1 configs (sorted tuples):
d1_cascade_cfgs = set()
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=q1/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N); q3max=q2/2; k3=1
        while F(k3,N)<=q3max:
            q3=F(k3,N)
            a=8-q1; b=q1-q2; c=q2-q3; d=q3
            cfg=tuple(sorted([a,b,c,d,F(4),F(2),F(1)],reverse=True))
            if alt_sum(cfg)==1: d1_cascade_cfgs.add(cfg)
            k3+=1
        k2+=1
sl_cfgs = set(tuple(cfg) for _,_,cfg in d1_sl)
shared = d1_cascade_cfgs & sl_cfgs
print(f"  cascade D=1 configs: {len(d1_cascade_cfgs)}, split-larger D=1: {len(sl_cfgs)}")
print(f"  shared configs (D=1, both types): {len(shared)}")
for c in list(shared)[:3]: print(f"    {c}")

