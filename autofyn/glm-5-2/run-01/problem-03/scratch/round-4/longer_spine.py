"""
Probe the longer-spine (7-element) transport mechanism.
For spine-7 D=1 cascade points, what is conserved along the star-path?
The 2-leftover case has a+d=const. The 4-leftover case (spine 7) is subtler.
Hypothesis: along the linear path, D is affine per PL cell and the path direction
is in the kernel of the gradient (zero-slope direction) within each cell.
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

# A spine-7 minimizer: q1=51/16, q2=9/8, q3=1/16 (from prior analysis)
q1m,q2m,q3m = F(51,16), F(9,8), F(1,16)
cfg_m = cfg_T3_cascade(q1m,q2m,q3m)
sp_m = spine(cfg_m)
print(f"spine-7 minimizer: q1={q1m} q2={q2m} q3={q3m}")
print(f"  cfg={cfg_m} D={alt_sum(cfg_m)}")
print(f"  spine={sp_m} D(sp)={alt_sum(sp_m)}")
# fragments: a=8-q1=77/16, b=q1-q2=33/16, c=q2-q3=17/16, d=q3=1/16. ALL non-dyadic.

q1d,q2d,q3d = F(4),F(2),F(1)  # dyadic
print(f"\nStar-path from spine-7 minimizer to dyadic:")
for k in range(0,21):
    t=F(k,20)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    a=8-q1; b=q1-q2; c=q2-q3; d=q3
    print(f"  t={float(t):.2f}: a={float(a):.3f} b={float(b):.3f} c={float(c):.3f} d={float(d):.3f}  a+d={float(a+d):.3f} b+c={float(b+c):.3f}  D={float(alt_sum(cfg)):.4f}")

# The key: along the path, is a+d conserved? b+c? 
# a+d = 8-q1+q3. q1: 51/16->4 (decreases by 13/16), q3: 1/16->1 (increases by 15/16).
# a+d = 8 - q1 + q3. Change = -(q1 change) + (q3 change) = 13/16*t + 15/16*t = 28/16*t. NOT conserved!
# So for spine-7, a+d is NOT conserved. The mechanism must be different.
print("\n  a+d NOT conserved for spine-7. Mechanism is zero-gradient of affine D per cell.")
print("  Check: within a single PL cell (no type change), is D constant along the path direction?")

# Find a sub-interval of the path with NO type change, check D is affine (constant).
prev_type=None; segments=[]
for k in range(0,201):
    t=F(k,200)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    ty=tuple(cfg)
    if prev_type is not None and ty!=prev_type:
        segments.append(('change', float(t), float(alt_sum(cfg))))
    prev_type=ty
# Sample D within a fixed cell
print("  D at fine grid (1/200) along path — should be 1.0 everywhere if star-shaped:")
Dvals=set()
for k in range(0,201):
    t=F(k,200)
    q1=(1-t)*q1m+t*q1d; q2=(1-t)*q2m+t*q2d; q3=(1-t)*q3m+t*q3d
    cfg=cfg_T3_cascade(q1,q2,q3)
    Dvals.add(alt_sum(cfg))
print(f"  distinct D values along 201-pt path: {Dvals}")

# ============================================================
# The REAL mechanism: the path direction (q1d-q1m, q2d-q2m, q3d-q3m) = (13/16, 7/16, 15/16).
# Within each PL cell, D is affine in (q1,q2,q3). The gradient is zero along this direction
# <=> D is constant along the path within the cell.
# For the 2-leftover case (b=2,c=1 fixed), D = a+d-4 = (8-q1+q3)-4 = 4-q1+q3, 
#   gradient = (-1, 0, +1), and the path direction (13/16, 7/16, 15/16) has 
#   dot product = -13/16 + 0 + 15/16 = 2/16 != 0. WAIT that's not zero!
# But D WAS constant=1 along the 2-leftover path. Contradiction?
# Let me recheck: for the 2-leftover minimizer q1m=13/4,q2m=5/4,q3m=1/4:
#   b = q1-q2 = 13/4-5/4 = 2 (const along path since q1-q2 = (13/4+3t/4)-(5/4+3t/4)=2)
#   c = q2-q3 = 5/4-1/4 = 1 (const)
#   a = 8-q1, d = q3. D = a - 4 + b - 2 + c - 1 + d = a+d + b+c - 7 = (8-q1+q3)+3-7 = 4-q1+q3.
#   Along path: q1=13/4+3t/4, q3=1/4+3t/4. D = 4-(13/4+3t/4)+(1/4+3t/4) = 4-12/4 = 1. 
#   The 3t/4 terms CANCEL (q1 and q3 change at same rate). gradient dot direction = -1*(3/4) + 1*(3/4) = 0!
# So the path direction has EQUAL rates for q1 and q3: both increase by 3/4 over the path.
#   direction = (3/4, 3/4, 3/4) = uniform (1,1,1). gradient (-1,0,1) dot (1,1,1) = 0. YES.
# For the spine-7 minimizer: direction = (13/16, 7/16, 15/16) — NOT uniform. 
#   But D is still constant=1 along path. So the gradient must be different (different cell).
# ============================================================
print("\n"+"="*70)
print("Direction analysis: path direction dot gradient = 0 within each cell")
print("="*70)
# 2-leftover case: direction (1,1,1) uniform, gradient (-1,0,1), dot=0.
print("2-leftover: dir=(1,1,1) (q1,q2,q3 all +3/4), grad=(-1,0,+1), dot=0. D=4-q1+q3 const.")
# spine-7: direction (13,7,15) (over 16). Need to find the gradient in the spine-7 cell.
# In the spine-7 cell, the sorted order is {a, 4, b, 2, c, 1, d} with a=77/16>4>b=33/16>2>c=17/16>1>d=1/16.
# D = a - 4 + b - 2 + c - 1 + d = (a+b+c+d) - 7 = (8-q1 + q1-q2 + q2-q3 + q3) - 7 = 8 - 7 = 1.
# D = 1 ALWAYS (independent of q1,q2,q3!) as long as the sorted type is {a,4,b,2,c,1,d}.
# Because a+b+c+d = 8 (telescopes: (8-q1)+(q1-q2)+(q2-q3)+q3 = 8). So D = 8 - 7 = 1. CONSTANT.
print("spine-7 cell {a,4,b,2,c,1,d}: D = (a+b+c+d) - 7 = 8 - 7 = 1. INDEPENDENT of q's!")
print("  (a+b+c+d = (8-q1)+(q1-q2)+(q2-q3)+q3 = 8 telescopes). D=1 on the WHOLE cell.")
print("  => gradient = (0,0,0) in this cell. Any direction preserves D.")

# Generalize: in a cell where the sorted type interleaves {fragments} and {tower pieces}
# such that tower pieces are ALL at - positions and fragments at + positions,
# D = (sum of fragments) - (sum of tower at -) + (tower at + if any).
# Sum of fragments = 2^n (total top piece, since fragments partition 2^n).
# So D = 2^n - (tower pieces at - positions) + (tower pieces at + positions).
# This is an INTEGER (tower pieces are powers of 2), and it's CONSTANT on the cell.
# At the dyadic endpoint it equals 1, so it's 1 on the whole cell.
print("\nGENERAL: in a cell where fragments (+) interleave tower pieces (-),")
print("  sum(fragments) = 2^n (they partition the top piece).")
print("  D = 2^n - sum(tower at -) + sum(tower at +) = INTEGER, constant on cell.")
print("  At dyadic endpoint D=1, so D=1 on the whole cell (if the cell contains a dyadic pt).")
