"""
Verify the TELESCOPING conservation for split-larger and split-tower types,
and check the 'block' condition (fragments of each parent at same-sign positions).
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

# split-larger: 8->(8-q1)+q1, split (8-q1)->(8-q1-q2)+q2. fragments: a=8-q1-q2, b=q2, c=q1.
#   sum fragments = 8-q1-q2+q2+q1 = 8 = 2^n. TELESCOPE.
# split-tower: 8->(8-q1)+q1 (fragments a=8-q1, b=q1, sum=8); split tower 4->(4-q2)+q2 (fragments c=4-q2, d=q2, sum=4).
#   Two parent pieces: top (sum 8), tower-4 (sum 4).
# Check: at D=1 minimizers of split-larger, are fragments at + and towers at -?
print("="*70)
print("Split-larger: block condition at D=1 minimizers")
print("="*70)
def cfg_T3_split_larger(q1,q2):
    a=8-q1-q2; b=q2; c=q1
    return sorted([a,b,c,F(4),F(2),F(1)],reverse=True)
N=16
d1=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=(8-q1)/2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N)
        cfg=cfg_T3_split_larger(q1,q2)
        if alt_sum(cfg)==1: d1.append((q1,q2,cfg))
        k2+=1
# For each D=1, check: in the SPINE, are non-dyadics at + and towers at -?
nd_at_minus=0; nd_plus_only=0; block_ok=0
for (q1,q2,cfg) in d1:
    sp=spine(cfg)
    nd_pos=[i for i,v in enumerate(sp) if not is_pow2(v)]
    if any(i%2==1 for i in nd_pos): nd_at_minus+=1
    elif len(nd_pos)>0: nd_plus_only+=1
    # block condition: non-dyadics (fragments) all at + (i%2==0), towers at - (i%2==1) [except last + if odd length]
    if all(i%2==0 for i in nd_pos): block_ok+=1
print(f"  split-larger D=1: {len(d1)}; nd only at +: {nd_plus_only}; nd at -: {nd_at_minus}; block ok: {block_ok}")

# For block-ok cells, D = sum(fragments at +) - sum(towers at -) + (tower at last + if odd len)
# sum(fragments) = 8 (telescope). So D = 8 - sum(towers at -) + sum(towers at +).
# At dyadic, fragments = tower values, D=1. Check D=8-7=1? towers at - = {4,2,1} sum 7? 
print("  Check: D = 8 - (sum towers at -) + (sum towers at +) = 1?")
for (q1,q2,cfg) in d1[:3]:
    sp=spine(cfg)
    t_minus=sum(sp[i] for i in range(1,len(sp),2) if is_pow2(sp[i]))
    t_plus=sum(sp[i] for i in range(0,len(sp),2) if is_pow2(sp[i]))
    print(f"    spine={sp} towers-={t_minus} towers+={t_plus} 8-t-+t+={8-t_minus+t_plus}")

# ============================================================
# split-tower: two parent pieces (top sum 8, tower-4 sum 4).
# D = (fragments of top at +) - (fragments of top at -) + (fragments of tower-4 at +) - (...) + tower 2,1
# If top-fragments both at +: contribute +8. If tower-4 fragments both at -: contribute -4.
# D = 8 - 4 + (tower 2,1 signs) = 4 + (2,1 signs). 
# At dyadic (q1=4,q2=2): {4,4,2,2,1}? wait. 8->4+4, 4(tower)->2+2. cfg={4,4,2,2,2,1}? no, tower 2 and 1 remain.
#   {4,4,2,2,2,1}: D=4-4+2-2+2-1=1. Yes.
# ============================================================
print("\n"+"="*70)
print("Split-tower: block condition (top-fragments same sign, tower-4-fragments same sign)")
print("="*70)
def cfg_T3_split_tower(q1,q2):
    return sorted([8-q1,q1,4-q2,q2,F(2),F(1)],reverse=True)
d1t=[]
for q1n in range(1,4*N+1):
    q1=F(q1n,N)
    if q1<=0 or q1>4: continue
    q2max=2; k2=1
    while F(k2,N)<=q2max:
        q2=F(k2,N)
        cfg=cfg_T3_split_tower(q1,q2)
        if alt_sum(cfg)==1: d1t.append((q1,q2,cfg))
        k2+=1
print(f"  split-tower D=1: {len(d1t)}")
for (q1,q2,cfg) in d1t[:3]:
    sp=spine(cfg)
    print(f"    q1={float(q1)} q2={float(q2)} spine={sp} D(sp)={alt_sum(sp)}")
    # fragments: top {8-q1, q1} sum 8; tower-4 {4-q2, q2} sum 4.
    # In spine, identify which are top-fragments vs tower-4-fragments vs unsplit towers.
    nd=[v for v in sp if not is_pow2(v)]
    print(f"      non-dyadic spine: {nd}")

# ============================================================
# The GENERAL telescoping lemma:
# For ANY refinement, the fragments of each split piece sum to the parent value.
# If the sorted type places all fragments of each parent at positions of the same
# sign, their net contribution = ±(parent value), INDEPENDENT of cut positions.
# So D is constant on the cell = D at the dyadic endpoint (if reachable).
# ============================================================
print("\n"+"="*70)
print("GENERAL TELESCOPING LEMMA (the proof mechanism):")
print("  For each split piece of value V, its fragments sum to V (telescope).")
print("  If all fragments of V sit at same-sign positions (block), net = ±V.")
print("  D = sum over blocks of ±V + (unsplit tower contributions).")
print("  This is CONSTANT on the PL cell (independent of cut positions).")
print("  At a dyadic config in the cell, D = 1 (by dyadic-refinement-lower-bound).")
print("  => D = 1 on the whole cell. The min-level set is a union of such cells.")
print("="*70)
print("\nThe V-shape (8->5+3, rebalance 5->2.5+2.5) moves INTO a cell interior")
print("where the block condition FAILS (fragments of 5 at different signs).")
print("The transport moves ALONG cell boundaries (ties) where blocks hold => D=1.")
