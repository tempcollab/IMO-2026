"""
Deep probes:
1. Star-shaped: from ANY D=1 cascade point, does the linear path to the dyadic stay at D=1?
2. The split-larger disconnected 17 points: real or grid artifacts?
3. Straddle structure for split-larger minimizers.
4. A THIRD type (split a tower piece, not top): does {D=1} reach dyadic?
5. General conservation law: D = (sum of non-dyadic spine leftovers at +) - (sum of tower pieces at -) = 1?
"""
from fractions import Fraction as F
import numpy as np
from collections import deque, Counter

def alt_sum(pieces):
    s=sorted(pieces,reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))
def is_pow2(x):
    if x<=0: return False
    if isinstance(x,F):
        if x.denominator==1:
            n=int(x); return n>0 and (n&(n-1))==0
        num,den=x.numerator,x.denominator
        return (num&(num-1))==0 and (den&(den-1))==0
    import math
    lg=math.log2(x) if x>0 else -1
    return abs(lg-round(lg))<1e-9 and round(lg)>=-20
def spine(cfg):
    s=sorted(cfg,reverse=True); c=Counter(s)
    return sorted([v for v in sorted(c,reverse=True) for _ in range(c[v]%2)],reverse=True)
def tower(n): return [F(2**(n-k)) for k in range(n+1)]

# ============================================================
# 1. STAR-SHAPED: from each D=1 cascade point, linear path to dyadic (4,2,1) stays D=1?
# ============================================================
print("="*70)
print("1. Star-shaped: linear path from D=1 cascade pt -> dyadic, stays D=1?")
print("="*70)
def cfg_T3_cascade(q1,q2,q3):
    a=8-q1; b=q1-q2; c=q2-q3; d=q3
    return sorted([a,b,c,d,F(4),F(2),F(1)],reverse=True)
q1d,q2d,q3d=F(4),F(2),F(1)  # dyadic
N=16
d1_cascade=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=q1/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N); q3max=q2/2; k3=1
        while F(k3,N)<=q3max:
            q3=F(k3,N)
            cfg=cfg_T3_cascade(q1,q2,q3); D=alt_sum(cfg)
            if D==1: d1_cascade.append((q1,q2,q3))
            k3+=1
        k2+=1

# Test star-shaped: from each D=1 pt, sample 10 pts along linear path to dyadic
star_ok=0; star_fail=0; fail_examples=[]
for (q1,q2,q3) in d1_cascade:
    ok=True
    for k in range(0,11):
        t=F(k,10)
        q1p=(1-t)*q1+t*q1d; q2p=(1-t)*q2+t*q2d; q3p=(1-t)*q3+t*q3d
        if q1p<=0 or q1p>4 or q2p<=0 or q2p>q1p/2 or q3p<=0 or q3p>q2p/2:
            continue  # invalid segment, skip (path leaves feasible region)
        Dp=alt_sum(cfg_T3_cascade(q1p,q2p,q3p))
        if Dp != 1: ok=False; break
    if ok: star_ok+=1
    else: star_fail+=1; fail_examples.append((q1,q2,q3))
print(f"  cascade D=1 pts: {len(d1_cascade)}")
print(f"  star-shaped to dyadic (path stays D=1): {star_ok}, fail: {star_fail}")
for ex in fail_examples[:5]:
    print(f"    FAIL pt: q1={float(ex[0])} q2={float(ex[1])} q3={float(ex[2])}")
    # show path
    for k in range(0,11):
        t=F(k,10)
        q1p=(1-t)*ex[0]+t*q1d; q2p=(1-t)*ex[1]+t*q2d; q3p=(1-t)*ex[2]+t*q3d
        if q1p<=0 or q1p>4 or q2p<=0 or q2p>q1p/2 or q3p<=0 or q3p>q2p/2:
            print(f"      t={float(t):.1f}: INVALID (out of cascade region)"); continue
        Dp=alt_sum(cfg_T3_cascade(q1p,q2p,q3p))
        print(f"      t={float(t):.1f}: D={float(Dp)}")

# ============================================================
# 2. Split-larger disconnected: what are the 17 isolated D=1 points?
# ============================================================
print("\n"+"="*70)
print("2. Split-larger type: the disconnected D=1 points")
print("="*70)
def cfg_T3_split_larger(q1,q2):
    a=8-q1-q2; b=q2; c=q1
    return sorted([a,b,c,F(4),F(2),F(1)],reverse=True)
d1_sl=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=(8-q1)/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N)
        cfg=cfg_T3_split_larger(q1,q2); D=alt_sum(cfg)
        if D==1: d1_sl.append((q1,q2,cfg))
        k2+=1
d1_set=set((q1,q2) for q1,q2,_ in d1_sl)
# find components
visited_all=set(); comps=[]
for pt in d1_set:
    if pt in visited_all: continue
    comp={pt}; dq=deque([pt]); step=F(1,N)
    while dq:
        c=dq.popleft()
        for dc in [(step,0),(-step,0),(0,step),(0,-step)]:
            nb=(c[0]+dc[0],c[1]+dc[1])
            if nb in d1_set and nb not in comp: comp.add(nb); dq.append(nb)
    visited_all|=comp; comps.append(comp)
comps.sort(key=len,reverse=True)
_sizes = [len(c) for c in comps[:10]]
print(f"  split-larger D=1 components: {len(comps)}, sizes: {_sizes}")
# show the isolated/small components
for i,c in enumerate(comps[1:6]):
    pts=list(c)
    print(f"  comp {i+1} (size {len(c)}): first pt {pts[0]}")
    q1,q2=pts[0]; cfg=cfg_T3_split_larger(q1,q2)
    print(f"    cfg={cfg} spine={spine(cfg)}")
    # check: is this point reachable from main comp via a NON-grid (continuous) path at D=1?
    # The isolated points are likely grid artifacts at the FEASIBLE-REGION BOUNDARY
    # (where the split-larger type transitions to another type). Check if q2 is at the boundary.
    print(f"    q2={q2} at boundary (q2=(8-q1)/2={F(8)-q1}/{2}={((8-q1)/2)})? {q2==(8-q1)/2}")

# ============================================================
# 3. Straddle structure in split-larger minimizers
# ============================================================
print("\n"+"="*70)
print("3. Straddle structure: split-larger D=1 minimizers")
print("="*70)
nd_sl=[(q1,q2,cfg) for q1,q2,cfg in d1_sl if not all(is_pow2(v) for v in cfg)]
for q1,q2,cfg in nd_sl[:5]:
    sp=spine(cfg); Dsp=alt_sum(sp)
    print(f"  q1={float(q1)} q2={float(q2)} cfg={[round(float(x),3) for x in cfg]}")
    print(f"    spine={sp} D(sp)={Dsp}={float(Dsp)}")
    # classify: which spine entries are non-dyadic?
    nd=[v for v in sp if not is_pow2(v)]
    dy=[v for v in sp if is_pow2(v)]
    print(f"    non-dyadic spine: {nd} dyadic spine: {dy}")
    if len(nd)==2:
        print(f"    nd sum={sum(nd)} straddle? tower pieces between: {[v for v in dy if nd[0]>v>nd[1]]}")

# ============================================================
# 4. THIRD type: split top, then split a TOWER piece (not a fragment of top).
# 8 -> (8-q1)+q1, then split tower piece 4 -> (4-q2)+q2.
# config = {(8-q1), q1, (4-q2), q2, 2, 1} sorted.
# ============================================================
print("\n"+"="*70)
print("4. Type: split top, then split TOWER piece (4)")
print("="*70)
def cfg_T3_split_tower(q1,q2):
    return sorted([8-q1,q1,4-q2,q2,F(2),F(1)],reverse=True)
d1_tower=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N)
        cfg=cfg_T3_split_tower(q1,q2); D=alt_sum(cfg)
        if D==1: d1_tower.append((q1,q2,cfg))
        k2+=1
print(f"  split-tower(4) D=1: {len(d1_tower)}")
dyad=[(q1,q2,cfg) for q1,q2,cfg in d1_tower if all(is_pow2(v) for v in cfg)]
print(f"  dyadic among them: {len(dyad)}: {[(float(q1),float(q2)) for q1,q2,_ in dyad[:3]]}")
# connectivity
if d1_tower:
    d1_set=set((q1,q2) for q1,q2,_ in d1_tower)
    start=next(iter(d1_set)); step=F(1,N); visited={start}; dq=deque([start])
    while dq:
        c=dq.popleft()
        for dc in [(step,0),(-step,0),(0,step),(0,-step)]:
            nb=(c[0]+dc[0],c[1]+dc[1])
            if nb in d1_set and nb not in visited: visited.add(nb); dq.append(nb)
    dyadic_in=any((q1,q2) in visited for q1,q2,_ in dyad)
    print(f"  D=1 component: {len(visited)} of {len(d1_set)}; dyadic reachable: {dyadic_in}")
# sample non-dyadic
nd_t=[(q1,q2,cfg) for q1,q2,cfg in d1_tower if not all(is_pow2(v) for v in cfg)][:3]
for q1,q2,cfg in nd_t:
    sp=spine(cfg)
    print(f"  nd: q1={float(q1)} q2={float(q2)} cfg={[round(float(x),3) for x in cfg]} spine={sp} D(sp)={alt_sum(sp)}")

# ============================================================
# 5. The conservation law: D(spine) = (sum of + non-dyadic) - (sum of - tower) ... 
# Test: for all D=1 cascade minimizers, is the straddle sum law exact?
# ============================================================
print("\n"+"="*70)
print("5. Conservation law across all T_3 cascade D=1 minimizers")
print("="*70)
violations=0
for (q1,q2,q3) in d1_cascade:
    cfg=cfg_T3_cascade(q1,q2,q3); sp=spine(cfg)
    if alt_sum(sp)!=1: continue
    nd=[(i,v) for i,v in enumerate(sp) if not is_pow2(v)]
    dy=[(i,v) for i,v in enumerate(sp) if is_pow2(v)]
    # spine is strictly decreasing, alternating signs starting +.
    # The "straddle" claim: non-dyadic leftovers pair up straddling tower pieces.
    # For spine length 3 with 2 non-dyadic: {a, t, d} a>t>d, a,d non-dyadic, t=tower.
    # D = a - t + d. a + d = t + 1 => D = 1.
    if len(sp)==3 and len(nd)==2:
        a,t,d=sp
        if a+d != t+1:
            violations+=1
            print(f"  VIOLATION: spine {sp} a+d={a+d} t+1={t+1}")
print(f"  spine-3 straddle law (a+d=t+1) violations: {violations} of {len(d1_cascade)}")
# Also count spine lengths
sp_lens=Counter(len(spine(cfg_T3_cascade(q1,q2,q3))) for q1,q2,q3 in d1_cascade)
print(f"  spine length distribution: {dict(sp_lens)}")
# For longer spines, check the general conservation
print("  Longer-spine minimizers (sample):")
for (q1,q2,q3) in d1_cascade[:5]:
    cfg=cfg_T3_cascade(q1,q2,q3); sp=spine(cfg)
    if len(sp)>=4:
        print(f"    q1={float(q1)} q2={float(q2)} q3={float(q3)} spine={sp} D={alt_sum(sp)}")
