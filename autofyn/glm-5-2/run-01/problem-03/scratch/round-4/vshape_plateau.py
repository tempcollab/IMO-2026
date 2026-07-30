"""
Probe the V-shape and plateau-connectivity GLOBAL exchange route for G1.

Lens: the plateau-connectivity / GLOBAL exchange / transport attack on the
odd-count non-dyadic leftover wall (G1).

Tower units: T_n = (2^n, ..., 1), total D_n = 2^{n+1}-1, target D >= 1.
D* = 1 (conjectured, verified n<=4).

Experiments:
1. Characterize the V-shape at odd-count minimizers of T_3.
   - From {4.75,4,2,2,1,1,0.25} (D=1), perturb EACH single cut and see D change.
   - Find a multi-cut direction along which D is non-increasing toward a dyadic config.
2. For T_2, T_3, T_4 odd-count minimizers, find a path to a dyadic config with D non-increasing.
3. Is the min-level set {D=1} connected (in the PL sense)? Does it touch a dyadic config?
4. The "1 is conserved" picture: do ALL odd-group minimizers share the SAME D as a nearby dyadic?
5. Tree-rewiring: can two splitting trees produce the same multiset? (D depends only on multiset,
   so the question is whether the min-level SET over multisets contains a dyadic config.)
"""
from fractions import Fraction as F
import numpy as np
from itertools import product

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

# ============================================================
# 1. V-shape at the T_3 odd-count minimizer {4.75,4,2,2,1,1,0.25}
# This comes from 3 cascading splits: 8->4.75+3.25->4.75+2+1.25->4.75+2+1+0.25
# (extract 2, then 1, from the non-4.75 side). The 4 cuts are pinned by the cascade.
# Parameterize: 8 -> x + (8-x); (8-x) -> x_2 + (8-x-x_2); etc.
# Actually the cascade is: 8 -> a + b, b -> c + d, d -> e + f (or c -> ...).
# The minimizer {4.75,4,2,2,1,1,0.25}: 8->4.75+3.25; 3.25->2+1.25; 1.25->1+0.25.
# So the cascade is on the "smaller fragment" each time. Cuts: q1=3.25 (smaller of 8-split),
#   then split 3.25 -> 2+1.25 (q2=1.25 smaller), then split 1.25 -> 1+0.25 (q3=0.25).
# Free params: q1 (in (0,4]), q2 (in (0, q1/2]), q3 (in (0, q2/2]).
# Config (sorted): {8-q1, q1-q2, q2-q3, q3, 4, 2, 1} (assuming all <= 4).
# Let me verify: q1=3.25,q2=1.25,q3=0.25: 8-3.25=4.75, 3.25-1.25=2, 1.25-0.25=1, 0.25, +4,2,1
#   = {4.75, 2, 1, 0.25, 4, 2, 1} sorted = {4.75,4,2,2,1,1,0.25}. Yes.
# ============================================================
print("="*70)
print("1. V-shape at T_3 odd-count minimizer {4.75,4,2,2,1,1,0.25}, D=1")
print("="*70)

def cfg_cascade_T3(q1, q2, q3):
    """3 cascading splits on smaller fragment. Returns sorted config."""
    a = F(8) - q1      # 4.75
    b = q1 - q2        # 2 (the piece kept from 2nd split larger frag)
    c = q2 - q3        # 1
    d = q3             # 0.25
    cfg = sorted([a, b, c, d, F(4), F(2), F(1)], reverse=True)
    return cfg

# Verify minimizer
q1m, q2m, q3m = F(19,4), F(5,4), F(1,4)  # 4.75? no. Let me recompute.
# 8 -> 4.75 + 3.25: q1=3.25=13/4 (smaller). a=4.75=19/4.
q1m = F(13,4); q2m = F(5,4); q3m = F(1,4)
cfg_m = cfg_cascade_T3(q1m, q2m, q3m)
D_m = alt_sum(cfg_m)
print(f"  minimizer: q1={q1m}={float(q1m)} q2={q2m}={float(q2m)} q3={q3m}={float(q3m)}")
print(f"  config={cfg_m}  D={D_m}={float(D_m)}")

# Dyadic target: balanced-pairs {4,4,2,2,1,1,1}, D=1. In cascade params:
#  8->4+4 (q1=4), 4->2+2 (q2=2), 2->1+1 (q3=1). So q1=4,q2=2,q3=1.
q1d, q2d, q3d = F(4), F(2), F(1)
cfg_d = cfg_cascade_T3(q1d, q2d, q3d)
D_d = alt_sum(cfg_d)
print(f"  dyadic target: q1={q1d} q2={q2d} q3={q3d} config={cfg_d} D={D_d}")

# Path: linear interpolate from minimizer to dyadic in (q1,q2,q3) space.
# q1: 13/4 -> 4, q2: 5/4 -> 2, q3: 1/4 -> 1.
print("\n  Linear path minimizer -> dyadic (cascade params):")
for t in [F(k,20) for k in range(0,21)]:
    q1 = (1-t)*q1m + t*q1d
    q2 = (1-t)*q2m + t*q2d
    q3 = (1-t)*q3m + t*q3d
    # check q2 <= q1/2 and q3 <= q2/2 (valid cascade)
    cfg = cfg_cascade_T3(q1, q2, q3)
    D = alt_sum(cfg)
    print(f"    t={float(t):.3f} q1={float(q1):.4f} q2={float(q2):.4f} q3={float(q3):.4f}  D={float(D):.4f}  cfg={[round(float(x),3) for x in sorted(cfg,reverse=True)]}")

# ============================================================
# 2. Single-cut perturbations at the minimizer (V-shape check)
# ============================================================
print("\n" + "="*70)
print("2. Single-cut perturbations at minimizer (each cut moved independently)")
print("="*70)
eps_vals = [F(-1,8), F(-1,16), F(0), F(1,16), F(1,8)]
for cut_name, qm, idx in [("q1", q1m, 1), ("q2", q2m, 2), ("q3", q3m, 3)]:
    print(f"  Perturb {cut_name} (minimizer value {qm}={float(qm)}):")
    for eps in eps_vals:
        q = qm + eps
        if idx == 1:
            q1, q2, q3 = q, q2m, q3m
        elif idx == 2:
            q1, q2, q3 = q1m, q, q3m
        else:
            q1, q2, q3 = q1m, q2m, q
        # validity: q1 in (0,4], q2 in (0,q1/2], q3 in (0,q2/2]
        if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
            print(f"    eps={float(eps):+.4f}: INVALID"); continue
        cfg = cfg_cascade_T3(q1, q2, q3)
        D = alt_sum(cfg)
        print(f"    eps={float(eps):+.4f} {cut_name}={float(q):.4f}: D={float(D):.4f}  dD={float(D-D_m):+.4f}")

# ============================================================
# 3. Find the min-level set {D=1} in the cascade 3-param space for T_3.
#    Is it connected? Does it contain the dyadic point (4,2,1)?
# ============================================================
print("\n" + "="*70)
print("3. Min-level set {D=1} in cascade (q1,q2,q3) space, T_3")
print("="*70)
# Grid of cascade params. q1 in (0,4], q2 in (0, q1/2], q3 in (0, q2/2].
# Use fine grid of Fractions with denominator 16.
N = 16
pts = []
for q1n in range(1, 4*N+1):       # q1 = q1n/(N) ... up to 4
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    # q2 in (0, q1/2]
    q2max = q1/2
    # iterate q2 = k/16 up to q2max
    k2 = 1
    while F(k2,N) <= q2max:
        q2 = F(k2,N)
        q3max = q2/2
        k3 = 1
        while F(k3,N) <= q3max:
            q3 = F(k3,N)
            cfg = cfg_cascade_T3(q1, q2, q3)
            D = alt_sum(cfg)
            pts.append((q1, q2, q3, D, cfg))
            k3 += 1
        k2 += 1

d1_pts = [(q1,q2,q3,cfg) for (q1,q2,q3,D,cfg) in pts if D == 1]
print(f"  total cascade configs (grid 1/{N}): {len(pts)}")
print(f"  # with D==1: {len(d1_pts)}")
dyadic_d1 = [(q1,q2,q3,cfg) for (q1,q2,q3,cfg) in d1_pts if all(is_pow2(v) for v in cfg)]
print(f"  # dyadic among D==1: {len(dyadic_d1)}")
for (q1,q2,q3,cfg) in dyadic_d1[:5]:
    print(f"    q1={float(q1)} q2={float(q2)} q3={float(q3)} cfg={cfg}")

# min D
minD = min(D for (_,_,_,D,_) in pts)
print(f"  min D over cascade grid = {float(minD)}")
# distribution of D values
from collections import Counter
Dcount = Counter(float(D) for (_,_,_,D,_) in pts)
print(f"  D distribution (top 10): {Dcount.most_common(10)}")

# ============================================================
# 4. Is {D=1} connected? Check by flood-fill in the grid (6-connectivity).
#    Does the dyadic point lie in the same component as the odd minimizer?
# ============================================================
print("\n" + "="*70)
print("4. Connectivity of {D=1} in cascade grid (T_3)")
print("="*70)
# build a set of D==1 points (q1,q2,q3) with grid coords
d1_set = set((q1,q2,q3) for (q1,q2,q3,cfg) in d1_pts)
# find component containing the odd minimizer (nearest grid pt)
def grid_near(q, N=16):
    return F(round(float(q)*N), N)
m_pt = (grid_near(q1m), grid_near(q2m), grid_near(q3m))
print(f"  odd minimizer grid pt: {m_pt} (in d1_set? {m_pt in d1_set})")
d_pt = (q1d, q2d, q3d)
print(f"  dyadic pt: {d_pt} (in d1_set? {d_pt in d1_set})")

# BFS flood fill on d1_set with 6-connectivity (neighbors differ by 1/16 in one coord)
if m_pt in d1_set and d_pt in d1_set:
    from collections import deque
    step = F(1, N)
    visited = set([m_pt])
    q = deque([m_pt])
    while q:
        c = q.popleft()
        for dc in [(step,0,0),(-step,0,0),(0,step,0),(0,-step,0),(0,0,step),(0,0,-step)]:
            nb = (c[0]+dc[0], c[1]+dc[1], c[2]+dc[2])
            if nb in d1_set and nb not in visited:
                visited.add(nb); q.append(nb)
    print(f"  component of odd minimizer: {len(visited)} pts")
    print(f"  dyadic pt in same component? {d_pt in visited}")

# ============================================================
# 5. The "1 is conserved" check: does EVERY D==1 config have a dyadic neighbor
#    within a small PL move? I.e. is the dyadic pt always reachable?
# ============================================================
print("\n" + "="*70)
print("5. '1 is conserved': for each D==1 cascade config, is a dyadic config reachable?")
print("="*70)
# Check: from each D==1 point, can we reach the dyadic by a monotone path (D never > 1)?
# Heuristic: greedy descent — move toward dyadic along the coord with most slack, stay in {D<=1}.
# Actually we want D non-INCREASING toward dyadic. Since both have D=1, we want a path in {D<=1} = {D==1}.
# That's the connectivity question above. Report: are there D==1 points NOT in the dyadic component?
if m_pt in d1_set and d_pt in d1_set:
    outside = [p for p in d1_set if p not in visited]
    print(f"  D==1 points NOT in dyadic's component: {len(outside)}")
    for p in outside[:5]:
        print(f"    {p}")

