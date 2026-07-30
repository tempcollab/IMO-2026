"""
Two final checks for the G1 route assessment:

(E) Can an ODD-count non-dyadic group config be a MINIMIZER (D = D*)?
   If NO, then Route A (pair-cancellation at minimizers) is viable:
   minimizers have even non-dyadic groups (or are dyadic) -> spine of distinct
   powers of 2 -> D >= 1.
   Search 3-split configs of T_3 with an odd non-dyadic group and D = 1.

(F) Correct the 2-split min: it is D(T_{n-2}) (dyadic cascade), not D(T_{n-1}).
   Verify 2-split min = D(T_{n-2}) for n=3,4,5,6.
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
    s = sorted(config, reverse=True)
    c = Counter(s)
    kept = []
    for v in sorted(c.keys(), reverse=True):
        kept.extend([v] * (c[v] % 2))
    return sorted(kept, reverse=True)


# ================================================================
# (E) Search 3-split configs of T_3 with odd non-dyadic group AND D=1.
# T_3 = (8,4,2,1), total 15. D* = 1 (balanced-pairs).
# Enumerate 3-split refinements (split top, then split a piece, then split a piece)
# on a grid, look for: has an odd-count non-dyadic group AND D == 1.
# ================================================================
print("=" * 70)
print("(E) Can odd-count non-dyadic configs achieve D = D* = 1 (T_3, 3-split)?")
print("=" * 70)

T3 = tower(3)
top = 8.0
T3f = [float(x) for x in T3]
step = 0.25
odd_at_min = []
total = 0
q1s = np.arange(step, top / 2, step)
for q1 in q1s:
    a1, b1 = top - q1, q1
    base1 = sorted([a1, b1] + T3f[1:], reverse=True)
    for i2 in range(len(base1)):
        L2 = base1[i2]
        if L2 < step:
            continue
        q2s = np.arange(step, L2 / 2, step)
        for q2 in q2s:
            c2, d2 = L2 - q2, q2
            base2 = base1[:i2] + [c2, d2] + base1[i2 + 1:]
            for i3 in range(len(base2)):
                L3 = base2[i3]
                if L3 < step:
                    continue
                q3s = np.arange(step, L3 / 2, step)
                for q3 in q3s:
                    c3, d3 = L3 - q3, q3
                    cfg = base2[:i3] + [c3, d3] + base2[i3 + 1:]
                    D = sum(((-1) ** i) * sorted(cfg, reverse=True)[i]
                             for i in range(len(cfg)))
                    total += 1
                    if abs(D - 1.0) < 1e-9:
                        g = nondyadic_groups([F(x).limit_denominator(10**9) for x in cfg])
                        has_odd = any(cnt % 2 == 1 for cnt in g.values())
                        if has_odd:
                            odd_at_min.append((cfg, D, g))
print(f"  3-split configs tested: {total}")
print(f"  #configs with D=1 AND an odd non-dyadic group: {len(odd_at_min)}")
for cfg, D, g in odd_at_min[:5]:
    print(f"    D={D} groups={g} cfg={[round(x,3) for x in sorted(cfg,reverse=True)]}")

# Also check n=4, D*=3 (2-split) and D*=1 (3-split) for odd groups at min
print("\n" + "=" * 70)
print("(F) 2-split min = D(T_{n-2}) verification")
print("=" * 70)
for n in [3, 4, 5, 6]:
    T = tower(n)
    top = float(T[0])
    Tf = [float(x) for x in T]
    target = alt_sum(tower(n - 2))  # D(T_{n-2})
    step = top / 80.0
    minD = float("inf")
    for q1 in np.arange(step, top / 2, step):
        a, b = top - q1, q1
        # split b
        if b > step:
            for q2 in np.arange(step, b / 2, step):
                c, d = b - q2, q2
                cfg = sorted([a, c, d] + Tf[1:], reverse=True)
                D = sum(((-1) ** i) * cfg[i] for i in range(len(cfg)))
                minD = min(minD, D)
        # split a
        for q2 in np.arange(step, a / 2, step):
            c, d = a - q2, q2
            cfg = sorted([c, d, b] + Tf[1:], reverse=True)
            D = sum(((-1) ** i) * cfg[i] for i in range(len(cfg)))
            minD = min(minD, D)
    print(f"  n={n}: 2-split grid min D = {minD:.4f}  D(T_{{n-2}})={target}={float(target):.4f}  match={abs(minD-float(target))<0.05}")

# ================================================================
# (G) For the spine-geometry argument: when an odd non-dyadic leftover x
# is in the spine, where does it sit relative to tower pieces, and is the
# local contribution D_piece >= 1?
# ================================================================
print("\n" + "=" * 70)
print("(G) Spine geometry for odd-group leftovers")
print("=" * 70)

# Construct a family: T_n, 3 cascading splits producing 3x, leftover = 2^k.
# x = (2^n - 2^k)/3. Spine = tower pieces (excluding the paired ones) + x.
# The leftover 2^k pairs with tower 2^k (removed). The 3 x's -> 1 leftover in spine.
# Spine = {2^n, 2^{n-1}, ..., 2^{k+1}, x, 2^{k-1}, ..., 2, 1} minus those that paired.
# Actually the tower piece 2^k is paired with the leftover fragment 2^k -> both removed.
# And tower pieces that didn't get split remain. Let me just compute for several (n,k).

for n in [3, 4, 5]:
    for k in range(0, n + 1):
        x = (F(2 ** n) - F(2 ** k)) / 3
        if x <= 0 or is_pow2(x):
            continue
        if 3 * x != 2 ** n - 2 ** k:
            continue
        leftover = 2 ** n - 3 * x  # = 2^k
        # config: 3 copies of x, leftover-frag (=2^k), tower pieces
        # tower pieces: 2^n (split, gone), 2^{n-1},...,2^k(ties leftover-frag),...,1
        # The leftover-frag = 2^k ties tower 2^k -> pair removed.
        cfg = [x, x, x, F(leftover)] + [F(2 ** j) for j in range(n - 1, -1, -1)]
        # 2^n was split, not in cfg. tower pieces 2^{n-1}..1 present.
        sp = spine(cfg)
        Dsp = alt_sum(sp)
        g = nondyadic_groups(cfg)
        Dfull = alt_sum(cfg)
        print(f"  n={n} k={k}: x={x}={float(x):.3f} leftover=2^{k}={leftover}")
        print(f"    cfg has odd group? {any(c%2==1 for c in g.values())}  groups={g}")
        print(f"    spine={sp}  D(spine)={Dsp}={float(Dsp):.4f}  D(full)={Dfull}={float(Dfull):.4f}")
        # check: is x between 2^{k+1} and 2^{k-1}? (it replaced 2^k in the tower)
        if k + 1 <= n and k - 1 >= 0:
            print(f"    x between 2^{k+1}={2**(k+1)} and 2^{k-1}={2**(k-1)}? {2**(k+1) > float(x) > 2**(k-1)}")
