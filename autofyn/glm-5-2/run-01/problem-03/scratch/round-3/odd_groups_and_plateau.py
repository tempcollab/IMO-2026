"""
Probe two subtle points for G1:

(A) ODD-count non-dyadic groups at STRONG breakpoints.
   The pair-cancellation argument (remove adjacent equal pairs -> spine of
   distinct values -> D >= 1) is clean ONLY when the spine is all powers of 2
   (even-count non-dyadic groups). If odd-count non-dyadic groups exist at
   strong breakpoints, the spine has non-dyadic leftovers and the bound is
   unclear. Check whether such configs exist AND whether D >= 1 there.

(B) PLATEAU CONNECTIVITY lead: does the min-level set {D = D*} always contain
   a DYADIC config? If yes, the dyadic lower bound (lemma 9) directly gives
   D* >= 1 and G1 closes. Test by: from sampled min-configs, try to slide
   toward a dyadic config keeping D = D*.
"""

from fractions import Fraction as F
from collections import Counter
import numpy as np


def alt_sum(pieces):
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
    import math
    lg = math.log2(x) if x > 0 else -1
    return abs(lg - round(lg)) < 1e-9 and round(lg) >= -20


def tower(n):
    return [F(2 ** (n - k)) for k in range(n + 1)]


def nondyadic_groups(config):
    c = Counter(config)
    return {v: cnt for v, cnt in c.items() if not is_pow2(v)}


def spine(config):
    """Remove ALL adjacent-equal pairs greedily, return remaining (strictly
    decreasing, all distinct) multiset."""
    s = sorted(config, reverse=True)
    from collections import Counter
    c = Counter(s)
    kept = []
    for v in sorted(c.keys(), reverse=True):
        kept.extend([v] * (c[v] % 2))
    return sorted(kept, reverse=True)


# ================================================================
# (A) ODD-COUNT NON-DYADIC STRONG BREAKPOINTS
# ================================================================
print("=" * 70)
print("(A) Strong breakpoints with ODD non-dyadic groups")
print("=" * 70)

# T_3 = (8,4,2,1). 3 splits cascading: 8 -> x+(8-x) -> ... producing 3 copies of x.
# 8 -> x + (8-x); (8-x) -> x + (8-2x); (8-2x) -> x + (8-3x).
# For strong bp: the leftover (8-3x) must tie a tower piece or be paired.
# 8-3x = 2^k (tower): x = (8-2^k)/3.
#   k=0: x=(8-1)/3=7/3.  k=1: x=(8-2)/3=2 (dyadic).  k=2: x=(8-4)/3=4/3.  k=3: x=(8-8)/3=0 (degenerate).
# So x in {7/3, 4/3} give strong breakpoints with 3 copies of non-dyadic x + a tower tie.

print("\nT_3, 3 cascading splits producing 3x, leftover ties tower:")
for x_label, x in [("7/3", F(7, 3)), ("4/3", F(4, 3))]:
    leftover = 8 - 3 * x
    # config: 3 copies of x, leftover (from split), tower pieces 4,2,1
    # but leftover IS a tower piece value (8-3x = 2^k), so it's a fragment tying the tower.
    # Wait: leftover = 8-3x is the final fragment from the 3rd split. It equals 2^k (tower value).
    # So config = {4(tower), 2(tower), 1(tower), 1(tower if k=0), x, x, x, leftover-frag}
    # Actually the leftover is a fragment = 2^k, ties tower 2^k.
    cfg = [F(4), F(2), F(1), x, x, x, leftover]
    # if leftover == 1, there are two 1's (tower + frag); else leftover is its own tower tie
    D = alt_sum(cfg)
    g = nondyadic_groups(cfg)
    sp = spine(cfg)
    Dsp = alt_sum(sp)
    print(f"  x={x_label}: leftover=8-3x={leftover} cfg={cfg}")
    print(f"    D={D}={float(D):.4f}  nondyadic_groups={g}  spine={sp}  D(spine)={Dsp}={float(Dsp):.4f}")

# More: 2 splits producing 3 copies is impossible (max 2 fragments/split-pair).
# 3 splits producing 5 copies of x: 5x <= 8, x<=8/5. cascade 4 deep needs 4 splits.
# With 3 splits, max 3 copies. So for T_3, odd non-dyadic groups have count exactly 3.

# T_4 = (16,8,4,2,1). 4 splits. Can get 3 copies of x (cascade 3 deep) + 1 extra split.
print("\nT_4, 3 cascading splits of 16 producing 3x, leftover ties tower, + 1 extra split:")
for x_num in range(1, 16):
    x = F(x_num, 3)  # x = m/3, leftover = 16-3x = 16-m, ties tower iff 16-m is pow2
    leftover = 16 - 3 * x
    if leftover <= 0 or not is_pow2(leftover):
        continue
    if is_pow2(x):
        continue  # want non-dyadic x
    # base config (3 splits): {8,4,2,1, x,x,x, leftover-frag}
    base = [F(8), F(4), F(2), F(1), x, x, x, leftover]
    D0 = alt_sum(base)
    g0 = nondyadic_groups(base)
    sp0 = spine(base)
    print(f"  x={x} leftover={leftover}: base D={D0}={float(D0):.3f} groups={g0} spine={sp0} D(spine)={alt_sum(sp0)}")
    # try a 4th split on the leftover-frag (split leftover -> y + (leftover-y)), need y to tie
    # skip detailed 4th-split; just note base is a 3-split strong bp already (uses 3 of 4 marks)

# Also: 3 copies with x = m/3 where leftover = 16-m is a tower, for T_4 with the
# leftover possibly > 8 (the top tower piece). E.g. x=1/3 -> leftover=15, not tower.
# Already filtered.

# ================================================================
# (B) PLATEAU CONNECTIVITY: does the min-level set contain a dyadic config?
# For n=3, min D=1. Sample min-configs and slide toward dyadic.
# ================================================================
print("\n" + "=" * 70)
print("(B) Plateau connectivity: min-level set -> dyadic?")
print("=" * 70)

# n=3, 2-split. Parametrize: 8->a+b (a=8-q1, b=q1), split b -> c+d (c=b-q2, d=q2).
# Config = {8-q1, b-q2, q2, 4, 2, 1} sorted (b=q1).
# D as function of (q1, q2). Find {D=1} region and check it touches dyadic.

def D_2split_T3(q1, q2):
    """8 -> (8-q1)+q1, then split q1 -> (q1-q2)+q2. Returns sorted config & D."""
    a, b = 8 - q1, q1
    c, d = q1 - q2, q2
    cfg = sorted([a, c, d, F(4), F(2), F(1)], reverse=True)
    return cfg, alt_sum(cfg)


print("\nn=3 2-split: D(q1,q2) on a grid, find D=1 region:")
# Use fractions on a grid
grid = [F(i, 12) for i in range(1, 49)]  # 1/12 .. 4
minD = None
d1_configs = []
for q1 in grid:
    if q1 <= 0 or q1 > 4:
        continue
    for q2 in grid:
        if q2 <= 0 or q2 > q1 / 2:
            continue
        cfg, D = D_2split_T3(q1, q2)
        if minD is None or D < minD:
            minD = D
        if D == 1:
            d1_configs.append((q1, q2, cfg))
print(f"  min D = {minD}")
print(f"  #configs with D=1: {len(d1_configs)}")
# check if any D=1 config is dyadic
dyadic_d1 = [(q1, q2, cfg) for (q1, q2, cfg) in d1_configs if all(is_pow2(v) for v in cfg)]
print(f"  #DYADIC D=1 configs: {len(dyadic_d1)}")
for (q1, q2, cfg) in dyadic_d1[:3]:
    print(f"    q1={float(q1):.3f} q2={float(q2):.3f} cfg={cfg}")

# Also check: also split a (the larger first fragment) case
def D_2split_T3_split_a(q1, q2):
    """8 -> (8-q1)+q1, then split a=(8-q1) -> (a-q2)+q2. Config & D."""
    a, b = 8 - q1, q1
    c, d = a - q2, q2
    cfg = sorted([c, d, b, F(4), F(2), F(1)], reverse=True)
    return cfg, alt_sum(cfg)


print("\nn=3 2-split (split larger fragment a):")
d1_b = []
for q1 in grid:
    if q1 <= 0 or q1 > 4:
        continue
    a = 8 - q1
    for q2 in grid:
        if q2 <= 0 or q2 > a / 2:
            continue
        cfg, D = D_2split_T3_split_a(q1, q2)
        if D == 1:
            d1_b.append((q1, q2, cfg))
print(f"  #D=1 configs: {len(d1_b)}")
dyad_b = [(q1, q2, cfg) for (q1, q2, cfg) in d1_b if all(is_pow2(v) for v in cfg)]
print(f"  #dyadic among them: {len(dyad_b)}")

# ================================================================
# (C) Does the min-level set for 2-split always touch a dyadic config?
# For general n: 2-split min = D(T_{n-1}). Dyadic config: expand top two levels.
# ================================================================
print("\n" + "=" * 70)
print("(C) 2-split min = D(T_{n-1}); dyadic attainer: expand top-2 levels")
print("=" * 70)
for n in [3, 4, 5, 6]:
    T = tower(n)
    # 2^n -> 2^{n-1}+2^{n-1}, then split one 2^{n-1} -> 2^{n-2}+2^{n-2}
    cfg = [F(2 ** (n - 1)), F(2 ** (n - 1)), F(2 ** (n - 2)), F(2 ** (n - 2))] + T[2:]
    # T[2:] = (2^{n-2},...,1) but we replaced the top two; actually T=(2^n,2^{n-1},2^{n-2},...,1)
    # after splitting top twice: pieces = {2^{n-1}, 2^{n-1}, 2^{n-2}, 2^{n-2}} ∪ {2^{n-2},...,1} (the rest of T)
    # but T[1:] had 2^{n-1} which got split. Let me rebuild.
    pieces = [F(2 ** (n - 1)), F(2 ** (n - 1))]  # from first split of 2^n
    # second split: split one 2^{n-1} -> 2^{n-2} + 2^{n-2}
    pieces = [F(2 ** (n - 1)), F(2 ** (n - 2)), F(2 ** (n - 2))]
    # plus the remaining tower pieces below 2^{n-1}: 2^{n-2}, 2^{n-3}, ..., 1
    pieces += [F(2 ** k) for k in range(n - 2, -1, -1)]
    pieces = sorted(pieces, reverse=True)
    D = alt_sum(pieces)
    print(f"  n={n}: dyadic 2-split config {pieces}  D={D}  D(T_{{n-1}})={alt_sum(tower(n-1))}  match={D==alt_sum(tower(n-1))}")

# ================================================================
# (D) Key check: for 2-split, is D ALWAYS >= D(T_{n-1})? (would close 2-split G1)
# Test on a grid for n=3,4,5.
# ================================================================
print("\n" + "=" * 70)
print("(D) Is 2-split D >= D(T_{n-1}) for ALL configs (not just min)?")
print("=" * 70)
for n in [3, 4, 5]:
    T = tower(n)
    target = alt_sum(tower(n - 1))
    top = 2 ** n
    # split top -> a+b (a=2^n-q1, b=q1), split b -> c+d OR split a -> c+d
    step = 2 ** (n - 1) / 24.0
    violations = 0
    tested = 0
    q1s = np.arange(step, top / 2, step)
    for q1f in q1s:
        q1 = float(q1f)
        a, b = top - q1, q1
        # split b
        if b > step:
            q2s = np.arange(step, b / 2, step)
            for q2 in q2s:
                c, d = b - q2, q2
                cfg = sorted([a, c, d] + [float(x) for x in T[1:]], reverse=True)
                D = sum(((-1) ** i) * cfg[i] for i in range(len(cfg)))
                tested += 1
                if D < target - 1e-9:
                    violations += 1
        # split a
        q2s = np.arange(step, a / 2, step)
        for q2 in q2s:
            c, d = a - q2, q2
            cfg = sorted([c, d, b] + [float(x) for x in T[1:]], reverse=True)
            D = sum(((-1) ** i) * cfg[i] for i in range(len(cfg)))
            tested += 1
            if D < target - 1e-9:
                violations += 1
    print(f"  n={n}: tested={tested} violations(D < D(T_{{n-1}})={target}): {violations}")
