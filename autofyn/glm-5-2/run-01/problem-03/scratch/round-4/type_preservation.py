"""
Re-run the type-preservation check with the CORRECT T_3 dyadic target.
Also: does the star-path cross combinatorial types (ties), and does D stay 1 at ties?
Also: reformulate the conservation law correctly.
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
def cfg_T3_cascade(q1,q2,q3):
    a=8-q1; b=q1-q2; c=q2-q3; d=q3
    return sorted([a,b,c,d,F(4),F(2),F(1)],reverse=True)

# T_3 correct dyadic
q1m,q2m,q3m=F(13,4),F(5,4),F(1,4)  # minimizer
q1d,q2d,q3d=F(4),F(2),F(1)          # dyadic (CORRECT)

print("="*70)
print("Type changes along star-path (T_3, correct dyadic target)")
print("="*70)
prev_type=None; type_changes=0; D_at_changes=[]
for k in range(0,101):
    t=F(k,100)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    ty=tuple(cfg)
    D=alt_sum(cfg)
    if prev_type is not None and ty!=prev_type:
        type_changes+=1
        D_at_changes.append((float(t),float(D)))
    prev_type=ty
print(f"  type changes: {type_changes}")
print(f"  D values at type changes: {D_at_changes[:10]}")
print(f"  all D at changes == 1? {all(abs(d-1.0)<1e-9 for _,d in D_at_changes)}")

# Show config at several t
for k in [0,25,50,75,100]:
    t=F(k,100)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    print(f"  t={float(t):.2f}: {[round(float(x),4) for x in cfg]} D={float(alt_sum(cfg))}")

# ============================================================
# The CORRECT conservation law:
# D(cfg) = 1 along the path. Decompose cfg into the 4 cascade fragments + tower.
# fragments: a=8-q1, b=q1-q2, c=q2-q3, d=q3. Tower: 4,2,1.
# Along the path a+d = 8-q1+q3. q1: 13/4->4, q3: 1/4->1. a+d = 8-q1+q3.
#   At t: q1=13/4+3/4*t, q3=1/4+3/4*t. a+d = 8-(13/4+3t/4)+(1/4+3t/4) = 8-12/4 = 5. CONSTANT=5.
# b+c = q1-q3 = (13/4+3t/4)-(1/4+3t/4) = 12/4 = 3. CONSTANT=3.
# So along the path: a+d=5 (const), b+c=3 (const). And a>=4 (since a=8-q1, q1<=4), d<=1.
# Tower pieces 4,2,1. b=q1-q2, c=q2-q3. Along path: b=(13/4-5/4)+3t/4*(1)=2+0=2? 
#   q1-q2 = (13/4+3t/4)-(5/4+3t/4) = 8/4 = 2. CONSTANT=2!
#   q2-q3 = (5/4+3t/4)-(1/4+3t/4) = 4/4 = 1. CONSTANT=1!
# So along the ENTIRE path: b=2, c=1, and only a,d vary with a+d=5.
# config = {a, 2, 1, d, 4, 2, 1} sorted. Since a in [4,4.75] and d in [0.25,1]:
#   a >= 4 (top), then 4, then 2 (b), then 2 (tower), then 1 (c), then 1 (tower), then d (bottom).
# D = a - 4 + 2 - 2 + 1 - 1 + d = (a+d) - 4 = 5 - 4 = 1. CONSTANT.
# ============================================================
print("\n"+"="*70)
print("The conservation law (CORRECT): along the path, b=2, c=1 fixed, a+d=5 fixed")
print("="*70)
for k in [0,25,50,75,100]:
    t=F(k,100)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    a=8-q1; b=q1-q2; c=q2-q3; d=q3
    print(f"  t={float(t):.2f}: a={float(a):.4f} b={float(b):.4f} c={float(c):.4f} d={float(d):.4f}  a+d={float(a+d)} b+c={float(b+c)}")

# ============================================================
# KEY: the path only moves a,d (the two straddling leftovers), keeping b,c
# (the middle pieces) FIXED at tower values 2,1. This is why D is constant:
# the middle pieces pair with tower pieces and cancel; only a,d contribute,
# and a+d is conserved (= tower_top + 1 = 4+1=5).
# This is the TRANSPORT: shift mass from a (top leftover) to d (bottom leftover),
# keeping their sum = straddled_tower + 1, until both hit tower values (dyadic).
# ============================================================
print("\n"+"="*70)
print("GENERAL TRANSPORT MECHANISM:")
print("  - The cascade produces fragments a (top), b,c (middle), d (bottom) + tower.")
print("  - At a minimizer, b,c are ALREADY at tower values (pair & cancel).")
print("  - Only a,d are non-dyadic, with a+d = (straddled tower) + 1 conserved.")
print("  - Transport: shift mass a->d keeping a+d const, until a=tower_top, d=tower_bot.")
print("  - D = (a+d) - (straddled tower) = 1 throughout (the '+1' is conserved).")
print("="*70)

# ============================================================
# Verify: for ALL 816 cascade D=1 points, are the middle fragments (b,c, or 
# whichever) at tower values, and only the straddling pair is non-dyadic?
# Check: the spine has non-dyadic values ONLY at + positions, and they pair-straddle.
# ============================================================
print("\n"+"="*70)
print("Verify: non-dyadic spine values are ALL at + positions (straddle pair)")
print("="*70)
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
nd_at_minus=0; nd_at_plus_only=0
for (q1,q2,q3,cfg) in d1:
    sp=spine(cfg)
    nd_pos=[i for i,v in enumerate(sp) if not is_pow2(v)]
    if any(i%2==1 for i in nd_pos):  # i%2==1 means minus position (0-indexed: pos 1,3,5 = minus)
        nd_at_minus+=1
    else:
        nd_at_plus_only+=1
print(f"  cascade D=1 minimizers: {len(d1)}")
print(f"  non-dyadic ONLY at + positions: {nd_at_plus_only}")
print(f"  non-dyadic at some - position: {nd_at_minus}")
# Note: 0-indexed, pos 0=+(odd index 1), pos 1=-(index 2), pos 2=+(index 3)...
# So i%2==0 is + position, i%2==1 is - position.
nd_at_minus2=0; nd_at_plus_only2=0
for (q1,q2,q3,cfg) in d1:
    sp=spine(cfg)
    nd_pos=[i for i,v in enumerate(sp) if not is_pow2(v)]
    if any(i%2==1 for i in nd_pos):
        nd_at_minus2+=1
    elif len(nd_pos)>0:
        nd_at_plus_only2+=1
print(f"  (0-indexed: i%2==1 is minus) nd at minus: {nd_at_minus2}, nd only at plus: {nd_at_plus_only2}, no nd: {len(d1)-nd_at_minus2-nd_at_plus_only2}")
