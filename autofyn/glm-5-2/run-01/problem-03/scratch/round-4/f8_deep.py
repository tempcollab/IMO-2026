"""
Deep dive on f8 = M_2 / 2^{n-1} (second-largest-piece bound).
1. Verify worst case (ratio 0.889) with exact fractions.
2. Check n=4 (small sample).
3. Understand the inductive move: does pairing a_1 reduce to an (n-1)-game
   where the second-largest becomes the relevant quantity?
4. Check: is f8 actually = M_2/2^{n-1}, or is the true bound tighter?
"""
import numpy as np
from fractions import Fraction as F

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))
def bp_splits_f(piece, all_pieces):
    cs = {piece / 2.0}
    for p in all_pieces:
        if 0 < p < piece: cs.add(p); cs.add(piece-p)
    return [(q, piece-q) for q in cs if 0 < q < piece]
_MEMO = {}
def min_D_bp_f(config, k):
    key = (tuple(sorted(round(x,12) for x in sorted(config, reverse=True))), k)
    if key in _MEMO: return _MEMO[key]
    best = D_of(config)
    if k == 0: _MEMO[key]=best; return best
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece=cs[i]; rest=cs[:i]+cs[i+1:]
        for (q,r) in bp_splits_f(piece, cs):
            d = min_D_bp_f(rest+[q,r], k-1)
            if d < best: best = d
    _MEMO[key]=best; return best

# The worst f8 config was [0.65825, 0.20347, 0.09306, 0.04523]
# Let's understand: M=0.658, M2=0.203, so M2/4 = 0.0509. D*=? Let me compute.
cfg = [0.65825, 0.20347, 0.09306, 0.04523]
_MEMO.clear()
d = min_D_bp_f(cfg, 3)
M,M2 = max(cfg), sorted(cfg,reverse=True)[1]
print(f"worst f8 cfg: {cfg}")
print(f"  D*={d:.6f} M2/4={M2/4:.6f} ratio={d/(M2/4):.5f}")
print(f"  M/8={M/8:.6f} ratio_max={d/(M/8):.5f}")
# This is dominant (M >= 2*M2: 0.658 >= 0.407). So Max-bound should hold.
# M2/4 is the f8 bound. D*/(M2/4) = 0.889 means f8 is loose here but holds.

# Now: WHY does f8 work in the crux? The (7,6,5,3)/21 case:
cfg2 = [7/21, 6/21, 5/21, 3/21]
_MEMO.clear()
d2 = min_D_bp_f(cfg2, 3)
M,M2 = max(cfg2), sorted(cfg2,reverse=True)[1]
print(f"\ncrux (7,6,5,3)/21:")
print(f"  D*={d2:.6f} M2/4={M2/4:.6f} ratio={d2/(M2/4):.5f}")
print(f"  M/8={M/8:.6f} ratio_max={d2/(M/8):.5f}")
# f8 holds: D*=1/21=0.0476 < M2/4 = (6/21)/4 = 6/84 = 1/14 = 0.0714. ratio 0.667.

# Check: what is the actual tightest simple bound?
# At tower: M2/2^{n-1} = (2^{n-1}/D_n)/2^{n-1} = 1/D_n. TIGHT.
# In crux (7,6,5,3)/21: D*=1/21, M2/4=1/14. Gap.
# What about (M-M2)? = 1/21 = D*. So (M-M2) is tight here but fails elsewhere.

# Let's check if f8 = M2/2^{n-1} is actually PROVABLE by the same halving induction:
# Claim: D* <= M2/2^{n-1}.
# Induction: pair a_1 -> {a_2, a_1-a_2} (two copies of a_2 at pos 1,2 cancel).
# rest' = {a_3, a_4, ..., a_1-a_2}. The new second-largest is max(a_3, a_1-a_2, a_4).
# By IH at level n-1: D(rest') <= M2'/2^{n-2} where M2' = second-largest of rest'.
# We need M2'/2^{n-2} <= M2/2^{n-1}, i.e. M2' <= M2/2.
# Is M2' <= M2/2? In the crux, a_3 > M/2 and M2 > M/2, so a_3 > M/2 >= M2/2 (since M2<=M).
# So M2' >= a_3 > M/2 >= M2/2. So M2' > M2/2. IH FAILS by the same logic!
print()
print("=== Inductive check for f8 ===")
print("After pairing a_1 -> {a_2, a_1-a_2}, rest' = {a_3,...,a_1-a_2}")
print("rest' second-largest M2' = max(a_3, a_1-a_2, a_4)")
print("Need M2' <= M2/2 = a_2/2 for the halving IH to close.")
print("But in crux: a_3 > a_1/2 and a_2 > a_1/2, so a_3 > a_1/2 >= a_2/2 (if a_2<=a_1)")
print("  => M2' >= a_3 > a_1/2. And a_2/2 < a_1/4 < a_1/2.")
print("  => M2' > a_1/2 > a_2/2 = M2/2. IH FAILS.")
print()
# So f8 also can't close by simple pairing+IH. But it's TRUE (verified).
# The inductive move must be different. Let's check what the actual optimal move is
# for the (7,6,5,3)/21 case under the f8 lens.

# Let's also verify f8 on n=4 (small)
print("=== n=4 small check of f8 ===")
n=4
_MEMO.clear()
rng = np.random.default_rng(42)
worst_r=0; viol=0; worst_cfg=None
for _ in range(60):
    m = rng.integers(2, 6)
    raw = rng.dirichlet([1]*m)
    cfg = sorted(raw, reverse=True)
    d = min_D_bp_f(list(cfg), n)
    M=max(cfg); M2=sorted(cfg,reverse=True)[1] if len(cfg)>=2 else 0
    b = M2/2**(n-1)
    if b<=1e-15: continue
    if d > b+1e-7:
        viol+=1
        print(f"  VIOL: D*={d:.6f} > M2/8={b:.6f} cfg={[round(x,4) for x in cfg]}")
    r=d/b if b>1e-12 else 0
    if r>worst_r: worst_r=r; worst_cfg=cfg
tow=[16/31,8/31,4/31,2/31,1/31]
_MEMO.clear()
d=min_D_bp_f(list(tow),n)
M,M2=max(tow),sorted(tow,reverse=True)[1]
print(f"  n=4: {60} trials viol={viol} worst_ratio={worst_r:.5f}")
print(f"  tower T_4: D*={d:.6f} M2/8={M2/8:.6f} ratio={d/(M2/8):.5f} target={1/31:.6f}")
if worst_cfg: print(f"  worst={[round(x,5) for x in worst_cfg]}")

# n=4 crux
print()
_MEMO.clear()
worst_r=0; viol=0; worst_cfg=None
for _ in range(40):
    for _ in range(40):
        raw = rng.dirichlet([1]*5)
        cfg = sorted(raw, reverse=True)
        if cfg[0]<2*cfg[1] and cfg[2]>cfg[0]/2: break
    else: continue
    d = min_D_bp_f(list(cfg), n)
    M=max(cfg); M2=sorted(cfg,reverse=True)[1]
    b = M2/2**(n-1)
    if b<=1e-15: continue
    if d > b+1e-7:
        viol+=1
        print(f"  CRUX VIOL: D*={d:.6f} > M2/8={b:.6f} cfg={[round(x,4) for x in cfg]}")
    r=d/b if b>1e-12 else 0
    if r>worst_r: worst_r=r; worst_cfg=cfg
print(f"  n=4 crux: viol={viol} worst_ratio={worst_r:.5f}")
if worst_cfg: print(f"  worst crux={[round(x,5) for x in worst_cfg]}")
