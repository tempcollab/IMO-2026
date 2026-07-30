"""
Final probes:
1. General conservation law for ALL T_3 D=1 minimizers (all spine lengths):
   D = (sum non-dyadic at +) - (sum tower at -) + (non-dyadic at -) - (tower at +)
   The CLAIM: sum(non-dyadic at +) - sum(tower at -) = 1 + [corrections].
   Test the clean form: sum of + - position non-dyadic values = sum of - position tower values + 1.
2. T_4 star-shaped (cascade): linear path from D=1 pt to dyadic stays D=1?
3. Cross-type boundary: does the isolated split-larger slice (q1=4) connect via CASCADE type?
"""
from fractions import Fraction as F
from collections import Counter
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

# ============================================================
# 1. General conservation law for T_3 cascade D=1 minimizers
# ============================================================
print("="*70)
print("1. General conservation law: T_3 cascade D=1, all spine lengths")
print("="*70)
def cfg_T3_cascade(q1,q2,q3):
    a=8-q1; b=q1-q2; c=q2-q3; d=q3
    return sorted([a,b,c,d,F(4),F(2),F(1)],reverse=True)
N=16
d1=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=q1/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N); q3max=q2/2; k3=1
        while F(k3,N)<=q3max:
            q3=F(k3,N)
            cfg=cfg_T3_cascade(q1,q2,q3)
            if alt_sum(cfg)==1: d1.append((q1,q2,q3,cfg))
            k3+=1
        k2+=1

# For each D=1 minimizer, decompose spine into + and - positions
# spine[0]=pos1(+), spine[1]=pos2(-), spine[2]=pos3(+), ...
viol_plus_minus=0
viol_straddle=0
for (q1,q2,q3,cfg) in d1:
    sp=spine(cfg)
    # + position values: sp[0], sp[2], sp[4], ...
    # - position values: sp[1], sp[3], sp[5], ...
    plus_nd=sum(sp[i] for i in range(0,len(sp),2) if not is_pow2(sp[i]))
    plus_t=sum(sp[i] for i in range(0,len(sp),2) if is_pow2(sp[i]))
    minus_nd=sum(sp[i] for i in range(1,len(sp),2) if not is_pow2(sp[i]))
    minus_t=sum(sp[i] for i in range(1,len(sp),2) if is_pow2(sp[i]))
    # D = (plus_nd + plus_t) - (minus_nd + minus_t) = 1
    # CLAIM: plus_nd - minus_t = 1 and plus_t - minus_nd = 0 (towers and nd cancel in pairs)
    if plus_nd - minus_t != 1: viol_plus_minus+=1
    if plus_t - minus_nd != 0: viol_straddle+=1
print(f"  cascade D=1 minimizers: {len(d1)}")
print(f"  violations of (plus_nd - minus_tower = 1): {viol_plus_minus}")
print(f"  violations of (plus_tower - minus_nd = 0): {viol_straddle}")
# Show a longer-spine example decomposition
for (q1,q2,q3,cfg) in d1:
    sp=spine(cfg)
    if len(sp)==7:
        plus_nd=[sp[i] for i in range(0,len(sp),2) if not is_pow2(sp[i])]
        minus_t=[sp[i] for i in range(1,len(sp),2) if is_pow2(sp[i])]
        print(f"  spine-7 example: {sp}")
        print(f"    plus non-dyadic: {plus_nd} sum={sum(plus_nd)}")
        print(f"    minus tower: {minus_t} sum={sum(minus_t)}")
        print(f"    plus_nd - minus_t = {sum(plus_nd)-sum(minus_t)}")
        break

# ============================================================
# 2. T_4 star-shaped: linear path from D=1 cascade pt -> dyadic stays D=1?
# ============================================================
print("\n"+"="*70)
print("2. T_4 star-shaped (cascade 3-split)")
print("="*70)
def cfg_T4_cascade(q1,q2,q3):
    a=16-q1; b=q1-q2; c=q2-q3; d=q3
    return sorted([a,b,c,d,F(8),F(4),F(2),F(1)],reverse=True)
q1d,q2d,q3d=F(8),F(4),F(2)
N=8
d1_t4=[]
for q1n in range(1,8*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>8: continue
    q2max=q1/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N); q3max=q2/2; k3=1
        while F(k3,N)<=q3max:
            q3=F(k3,N)
            cfg=cfg_T4_cascade(q1,q2,q3)
            if alt_sum(cfg)==1: d1_t4.append((q1,q2,q3))
            k3+=1
        k2+=1
star_ok=0; star_fail=0
for (q1,q2,q3) in d1_t4:
    ok=True
    for k in range(0,11):
        t=F(k,10)
        q1p=(1-t)*q1+t*q1d; q2p=(1-t)*q2+t*q2d; q3p=(1-t)*q3+t*q3d
        if q1p<=0 or q1p>8 or q2p<=0 or q2p>q1p/2 or q3p<=0 or q3p>q2p/2:
            continue
        Dp=alt_sum(cfg_T4_cascade(q1p,q2p,q3p))
        if Dp!=1: ok=False; break
    if ok: star_ok+=1
    else: star_fail+=1
print(f"  T_4 cascade D=1 pts: {len(d1_t4)}; star-shaped to dyadic: {star_ok}, fail: {star_fail}")

# ============================================================
# 3. Cross-type boundary: do the isolated split-larger (q1=4) points
#    appear in the CASCADE D=1 set? (same sorted multiset)
# ============================================================
print("\n"+"="*70)
print("3. Cross-type boundary: split-larger q1=4 slice vs cascade")
print("="*70)
def cfg_T3_split_larger(q1,q2):
    a=8-q1-q2; b=q2; c=q1
    return sorted([a,b,c,F(4),F(2),F(1)],reverse=True)
# cascade D=1 configs (sorted tuples)
cascade_cfgs=set()
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=q1/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N); q3max=q2/2; k3=1
        while F(k3,N)<=q3max:
            q3=F(k3,N)
            cfg=tuple(sorted(cfg_T3_cascade(q1,q2,q3),reverse=True))
            if alt_sum(cfg)==1: cascade_cfgs.add(cfg)
            k3+=1
        k2+=1
# split-larger q1=4 slice
sl_boundary=set()
for k2 in range(1,2*N+1):
    q2=F(k2,N)
    if q2<=0 or q2>(8-F(4))/2: continue
    cfg=tuple(sorted(cfg_T3_split_larger(F(4),q2),reverse=True))
    if alt_sum(cfg)==1: sl_boundary.add(cfg)
shared=cascade_cfgs & sl_boundary
print(f"  cascade D=1 configs: {len(cascade_cfgs)}")
print(f"  split-larger q1=4 D=1 configs: {len(sl_boundary)}")
print(f"  shared (cross-type): {len(shared)}")
for c in list(shared)[:3]: print(f"    {c}")

# Also: do ALL split-larger D=1 configs appear in cascade?
sl_all=set()
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=(8-q1)/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N)
        cfg=tuple(sorted(cfg_T3_split_larger(q1,q2),reverse=True))
        if alt_sum(cfg)==1: sl_all.add(cfg)
        k2+=1
print(f"  all split-larger D=1 configs: {len(sl_all)}; shared with cascade: {len(sl_all & cascade_cfgs)}")

# ============================================================
# 4. The conservation law: is it the TRANSPORT invariant?
#    Claim: along the linear path to dyadic, the SORTED TYPE is preserved
#    (same combinatorial type), and within a type D is affine, constant=1
#    because the straddle sum is conserved. Verify type preservation.
# ============================================================
print("\n"+"="*70)
print("4. Type preservation along the star-path (T_3 cascade)")
print("="*70)
# Take the odd minimizer and check the sorted order type is constant along the path.
q1m,q2m,q3m=F(13,4),F(5,4),F(1,4)
type_changes=0
prev_type=None
for k in range(0,21):
    t=F(k,20)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    ty=tuple(cfg)  # the sorted order
    D=alt_sum(cfg)
    if prev_type is not None and ty!=prev_type:
        type_changes+=1
        # find where the tie happens
        print(f"  t={float(t):.3f}: type CHANGE (tie). D={float(D)}")
    prev_type=ty
print(f"  type changes along path: {type_changes}")
# Show the config evolution
for k in [0,5,10,15,20]:
    t=F(k,20)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    print(f"  t={float(t):.2f}: {[round(float(x),3) for x in cfg]} D={float(alt_sum(cfg))}")
