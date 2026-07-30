"""
Direct structural analysis of 2-split and 3-split breakpoints of T_n.

T_n = (2^n, ..., 2, 1), total D_n = 2^{n+1}-1, tower units. Target D >= 1.

A breakpoint config: every fragment (split product) ties an adjacent piece.
Equal adjacent pieces CANCEL in the alternating sum (a_i=a_{i+1} => contrib 0),
and removing such a pair preserves all other signs.

KEY STRUCTURAL CLAIM TO TEST:
  At a breakpoint, a NON-dyadic fragment (value != 2^k) cannot tie a tower
  piece (all tower pieces are powers of 2), so it must tie another fragment of
  the same value. Question: does the count of each non-dyadic value come out
  EVEN (so pairs fully cancel, D = D of dyadic skeleton)?
  If yes -> D is determined by the dyadic skeleton, and we just need
  D(dyadic skeleton) >= 1 (a much smaller problem).

We also test the CONVEXITY lead: from a non-dyadic breakpoint, deform toward
a dyadic breakpoint and check D is non-increasing along the path.
"""

from fractions import Fraction as F
from collections import Counter
import numpy as np


def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1) ** i) * s[i] for i in range(len(s)))


def alt_sum_float(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1) ** i) * s[i] for i in range(len(s)))


def is_pow2(x):
    if x <= 0:
        return False
    if isinstance(x, F):
        if x.denominator == 1:
            n = int(x)
            return n > 0 and (n & (n - 1)) == 0
        num, den = x.numerator, x.denominator
        return (num & (num - 1)) == 0 and (den & (den - 1)) == 0
    # float
    import math
    lg = math.log2(x) if x > 0 else -1
    return abs(lg - round(lg)) < 1e-9 and round(lg) >= -20


def tower(n):
    return [F(2 ** (n - k)) for k in range(n + 1)]


def Dn(n):
    return 2 ** (n + 1) - 1


def nondyadic_groups(config):
    c = Counter(config)
    g = {}
    for v, cnt in c.items():
        if not is_pow2(v):
            g[v] = cnt
    return g


def dyadic_skeleton_D(config):
    """Remove non-dyadic pairs (keep odd one-out), resort, recompute D.
    Tests: does D(full) == D(skeleton)?  (pair-cancellation check)"""
    c = Counter(config)
    kept = []
    for v, cnt in c.items():
        if is_pow2(v):
            kept.extend([v] * cnt)
        else:
            kept.extend([v] * (cnt % 2))
    return alt_sum(kept)


def breakpoint_check(config):
    """Strong breakpoint: every piece value either has count>=2 (ties a copy)
    or is a tower-piece value (power of 2). Returns list of lone-non-dyadic
    values (violations)."""
    c = Counter(config)
    viol = [v for v, cnt in c.items() if cnt == 1 and not is_pow2(v)]
    return viol


# ================================================================
# 2-SPLIT BREAKPOINT STRUCTURE for T_n
# Split top 2^n -> a+b (a>=b, a+b=2^n), then split piece X -> c+d (c>=d).
# X in {a, b, 2^{n-1}, 2^{n-2}, ...} (any current piece).
# We enumerate the STRUCTURAL breakpoint possibilities.
# ================================================================

def two_split_configs(n, q1, q2, split_idx):
    """q1 = first cut (b), split top 2^n -> (2^n - q1) + q1.
    split_idx: index (in sorted base) of piece to split second.
    q2 = second cut (d).
    Returns final config (list of Fractions)."""
    T = tower(n)
    top = T[0]
    a = top - q1
    b = q1
    base = sorted([a, b] + T[1:], reverse=True)
    L = base[split_idx]
    c = L - q2
    d = q2
    out = base[:split_idx] + [c, d] + base[split_idx + 1:]
    return sorted(out, reverse=True)


def two_split_D_function(n, q1, q2, split_idx):
    """D as function; returns (config, D)."""
    cfg = two_split_configs(n, q1, q2, split_idx)
    return cfg, alt_sum(cfg)


# ---- Enumerate 2-split breakpoints structurally ----
# At a breakpoint, each fragment ties. Fragments are a, b, c, d (the split
# products; but if X is a fragment from split 1, splitting it consumes it).
# Let's just do a moderately fine FLOAT grid but only over the relevant
# region and check breakpoint-ness + D.

def two_split_grid_float(n, steps=200):
    """Float grid over (q1, q2, split_idx). Returns list of (cfg, D, info)."""
    T = tower(n)
    top = float(T[0])
    res = []
    q1s = np.linspace(1e-6, top / 2 - 1e-6, steps)
    for q1 in q1s:
        a = top - q1
        b = q1
        base = sorted([a, b] + [float(x) for x in T[1:]], reverse=True)
        for split_idx in range(len(base)):
            L = base[split_idx]
            if L < 1e-6:
                continue
            q2s = np.linspace(1e-6, L / 2 - 1e-6, steps)
            for q2 in q2s:
                c = L - q2
                d = q2
                out = base[:split_idx] + [c, d] + base[split_idx + 1:]
                D = alt_sum_float(out)
                res.append((tuple(sorted(out, reverse=True)), D, (q1, q2, split_idx)))
    return res


print("=" * 70)
print("2-SPLIT GRID ANALYSIS")
print("=" * 70)

for n in [3, 4, 5]:
    T = tower(n)
    print(f"\n--- T_{n} = {T}, D(T_{n})={alt_sum(T)}, D(T_{{n-1}})={alt_sum(tower(n-1))} ---")
    steps = {3: 150, 4: 100, 5: 60}[n]
    res = two_split_grid_float(n, steps)
    minD = min(r[1] for r in res)
    print(f"  2-split float grid (steps={steps}): min D = {minD:.6f}")

    # find near-min configs
    nearmin = [r for r in res if r[1] < minD + 0.01]
    print(f"  #configs with D < min+0.01: {len(nearmin)}")

    # breakpoint check (tolerance: pieces within 1e-3 of each other count as ties)
    # Use a tolerance-based tie detection.
    def ties(cfg, tol=0.05):
        s = sorted(cfg, reverse=True)
        buckets = [round(float(x) / tol) * tol for x in s]
        c = Counter(buckets)
        viol = []
        for v, cnt in c.items():
            vreal = v
            is_tower = any(abs(vreal - float(x)) < tol for x in T)
            if cnt == 1 and not is_tower and not is_pow2(vreal):
                viol.append(vreal)
        return viol

    bp = [r for r in res if len(ties(r[0])) == 0]
    print(f"  #approx-breakpoints (tol 0.02): {len(bp)}")
    if bp:
        print(f"  breakpoint D range: [{min(b[1] for b in bp):.4f}, {max(b[1] for b in bp):.4f}]")
        # non-dyadic breakpoints (has a non-power-of-2 piece)
        ndbp = [b for b in bp if any(not is_pow2(v) for v in b[0])]
        print(f"  #non-dyadic approx-breakpoints: {len(ndbp)}")
        if ndbp:
            ndmin = min(b[1] for b in ndbp)
            print(f"  non-dyadic breakpoint min D = {ndmin:.6f}")
            # show 3 min
            ndbp.sort(key=lambda b: b[1])
            for b in ndbp[:3]:
                print(f"    D={b[1]:.4f} cfg={[round(x,3) for x in b[0]]}")

# ================================================================
# EXACT analysis of specific known non-dyadic breakpoints (Fraction)
# ================================================================
print("\n" + "=" * 70)
print("EXACT STRUCTURAL ANALYSIS (Fraction)")
print("=" * 70)


def show(name, pieces):
    D = alt_sum(pieces)
    g = nondyadic_groups(pieces)
    Dskel = dyadic_skeleton_D(pieces)
    viol = breakpoint_check(pieces)
    print(f"  {name}: cfg={pieces}")
    print(f"    D={D}  groups(nondyadic)={g}  D_skeleton={Dskel}  lone-violations={viol}")
    print(f"    pair-cancel matches: D==D_skel ? {D==Dskel}")


# T_3 = (8,4,2,1), total 15
print("\nT_3 exact breakpoints:")
# dyadic balanced-pairs
show("dyadic {4,4,2,2,1,1,1}", [F(4), F(4), F(2), F(2), F(1), F(1), F(1)])
# non-dyadic: 8->6+2, 6->3+3  => {4,3,3,2,2,1}
show("nondyadic {4,3,3,2,2,1}", [F(4), F(3), F(3), F(2), F(2), F(1)])
# non-dyadic: 8->5+3, 3->2+1 => {5,4,2,2,1,1} -- is this a breakpoint? 5 is lone
show("nondyadic {5,4,2,2,1,1}", [F(5), F(4), F(2), F(2), F(1), F(1)])
# 8->5+3, 5->3+2 => wait 5->? need 5 split: 5 -> 3+2 gives {4,3,3,2,2,1} same as above
# 8 -> 7+1, 7 -> 4+3 => {4,4,3,2,1,1}
show("nondyadic {4,4,3,2,1,1}", [F(4), F(4), F(3), F(2), F(1), F(1)])
# 8 -> 7+1, 7 -> 3+4 (same)
# 8 -> (9/2)+(7/2)? fractions. Let's try 8->(9/2)+(7/2), (9/2)->? need (9/2) to tie.
# 8 -> 9/2 + 7/2; 7/2 -> ? need tie. Try 7/2 paired: split another piece? only 1 second split.
# Try: 8 -> 9/2 + 7/2; (9/2) not tieable alone. skip.
# 8 -> 6+2, 2(tower)->1+1: {6,4,2,1,1,1}? 6 lone. Not breakpoint.
# 8 -> 6+2, 6 -> 4+2: {4,4,2,2,2,1} dyadic.
# 8 -> 6+2, 6 -> 5+1: {5,4,2,2,1,1} 5 lone
# 8 -> (13/2)+(3/2), (13/2)->? hard. skip fractions for now.
# 8 -> 7+1, 7 -> 5+2: {5,4,2,2,1,1} 5 lone. same.
# 8 -> 7+1, 7 -> (7/2)+(7/2): {4,(7/2),(7/2),2,1,1}? groups (7/2):2 even.
show("nondyadic {4,7/2,7/2,2,1,1}", [F(4), F(7, 2), F(7, 2), F(2), F(1), F(1)])
# 8 -> (15/2)+(1/2), (15/2)->? need tie. (15/2) lone unless paired. skip.

# T_4 = (16,8,4,2,1), total 31
print("\nT_4 exact breakpoints:")
# non-dyadic 2-split: 16 -> 12+4, 12 -> 6+6 => {8,6,6,4,4,2,1}
show("nondyadic {8,6,6,4,4,2,1}", [F(8), F(6), F(6), F(4), F(4), F(2), F(1)])
# 16 -> 10+6, 10 -> 5+5 => {8,6,5,5,4,2,1}
show("nondyadic {8,6,5,5,4,2,1}", [F(8), F(6), F(5), F(5), F(4), F(2), F(1)])
# 16 -> 10+6, 6 -> 3+3 => {10,8,4,3,3,2,1} -- 10 lone
show("nondyadic {10,8,4,3,3,2,1}", [F(10), F(8), F(4), F(3), F(3), F(2), F(1)])
# 16 -> 12+4, 4(tower)->2+2: {12,8,4,2,2,2,1} 12 lone
# 16 -> 9+7, 9 -> 5+4: {8,7,5,4,4,2,1} 7 lone,5 lone
# 16 -> 14+2, 14 -> 7+7 => {8,7,7,4,2,2,1}
show("nondyadic {8,7,7,4,2,2,1}", [F(8), F(7), F(7), F(4), F(2), F(2), F(1)])
# 16 -> 14+2, 14 -> 8+6: {8,8,6,4,2,2,1} 6 lone
# 16 -> (24/2)+(8/2)=12+4 done. fractions: 16 -> 9+7, 7 -> (7/2)+(7/2): {9,8,4,(7/2),(7/2),2,1} 9 lone
# 16 -> (17/2)+(15/2), (15/2)->? lone. skip.
# 3-split T_4: 16->8+8, 8->? , ... let's try 16->12+4, 12->8+4 (gives dyadic-ish), 4->2+2
# 16 -> 12+4, 12->6+6, 6->3+3: {8,4,3,3,3,3,2,1}? count 3:4 even, count 4:2... wait
# pieces: 12->6+6 (two 6's), one 6->3+3. Final: {8(tower), 4(tower), 6, 3, 3, 2,1,4(tower)} wait
# start {16,8,4,2,1}; split 16->12+4: {12,4,8,4,2,1}={12,8,4,4,2,1}; split 12->6+6: {8,6,6,4,4,2,1};
# split one 6 -> 3+3: {8,6,3,3,4,4,2,1}={8,6,4,4,3,3,2,1}
show("nondyadic 3split {8,6,4,4,3,3,2,1}", [F(8), F(6), F(4), F(4), F(3), F(3), F(2), F(1)])

# ================================================================
# CONVEXITY LEAD: deform a non-dyadic breakpoint toward a dyadic one,
# check D is non-increasing along the path.
# ================================================================
print("\n" + "=" * 70)
print("CONVEXITY LEAD TEST")
print("=" * 70)


def D_along_path_3_3_3():
    """T_3: 8->6+2, 6->c+(6-c). Path c: 3 (=3+3, nondyadic bp) -> 4 (=4+2, dyadic).
    D as function of c in [3,4]."""
    T = [F(8), F(4), F(2), F(1)]
    print("  Path: 8->6+2 (b=2 fixed ties tower 2), 6 -> c+(6-c), c: 3 -> 4")
    for k in range(0, 11):
        c = F(3) + F(k, 10)
        d = 6 - c
        cfg = sorted([6 - c, c, d, F(4), F(2), F(1)], reverse=True)  # 8->6+2 then 6->c+d
        # wait: 8->6+2 gives {6,2,4,2,1}; then split 6 -> c+d gives {c,d,2,4,2,1}
        cfg = sorted([c, d, F(4), F(2), F(2), F(1)], reverse=True)
        D = alt_sum(cfg)
        print(f"    c={float(c):.2f} d={float(d):.2f} cfg={[float(x) for x in cfg]} D={float(D):.4f}")


D_along_path_3_3_3()


def D_along_path_5_5():
    """T_4: 16->10+6, 10 -> c+(10-c). c: 5 (=5+5, nondyadic bp) -> 8 (=8+2, dyadic)."""
    print("  Path: 16->10+6 (6 fixed ties? no 6 not tower; hmm). Actually use 16->12+4, 12->c+(12-c). c:6->8")
    for k in range(0, 11):
        c = F(6) + F(k, 5)  # 6 -> 8
        d = 12 - c
        # 16->12+4: {12,4,8,4,2,1}={12,8,4,4,2,1}; split 12 -> c+d: {c,d,8,4,4,2,1}
        cfg = sorted([c, d, F(8), F(4), F(4), F(2), F(1)], reverse=True)
        D = alt_sum(cfg)
        print(f"    c={float(c):.2f} d={float(d):.2f} D={float(D):.4f}  dyadic?{is_pow2(c) and is_pow2(d)}")


D_along_path_5_5()
