#!/usr/bin/env python3
"""gaps-leftover sanity check: D = sum(gaps)+leftover >= 1 for random refinements of T_n.

Units: tower units (total D_n = 2^{n+1}-1). Target: D >= 1.

Verifies:
 (A) the gaps+leftover identity  D == sum(p_{2k-1}-p_{2k}) + [m odd]*p_m
     for both parities of m (pad even m with phantom 0 -> leftover 0).
 (B) D >= 1 for many random <=n-mark refinements of T_n, n=3,4.
 (C) reports min D seen and the pairing bound D >= p_m (m odd).
"""
import numpy as np
from fractions import Fraction


def alternating_sum(p):
    """p: sorted descending list. Returns D = p1 - p2 + p3 - ..."""
    s = 0.0
    for i, v in enumerate(p):
        s += v if i % 2 == 0 else -v
    return s


def gaps_leftover(p):
    """p sorted desc. Returns (sum_of_gaps, leftover) where
    D = sum_of_gaps + leftover; leftover = p_m if m odd else 0."""
    m = len(p)
    n_pairs = m // 2
    gaps = sum(p[2 * k] - p[2 * k + 1] for k in range(n_pairs))
    leftover = p[-1] if (m % 2 == 1) else 0.0
    return gaps, leftover


def refine_tower(n, rng, max_marks=None):
    """T_n = [2^n, 2^{n-1}, ..., 1]. Apply <=n marks (random split positions).
    Returns the refined sorted-desc list."""
    pieces = [2 ** (n - k) for k in range(n + 1)]  # 2^n, 2^{n-1}, ..., 1
    if max_marks is None:
        max_marks = n
    nmarks = rng.integers(0, max_marks + 1)
    # choose nmarks distinct pieces (with replacement ok? a piece can be split multiple times)
    # A mark splits ONE existing piece into two positive parts.
    for _ in range(nmarks):
        # pick a piece to split
        idx = rng.integers(0, len(pieces))
        v = pieces[idx]
        # split position q in (0, v); use random fraction, avoid exact halves bias
        frac = rng.uniform(0.01, 0.99)
        a = v * frac
        b = v - a
        pieces.pop(idx)
        pieces.extend([a, b])
    pieces.sort(reverse=True)
    return pieces


def check(n, N=20000, seed=0):
    rng = np.random.default_rng(seed)
    Dn = 2 ** (n + 1) - 1
    minD = None
    mincfg = None
    idfail = 0
    pairfail = 0
    for _ in range(N):
        p = refine_tower(n, rng)
        D = alternating_sum(p)
        g, l = gaps_leftover(p)
        if abs((g + l) - D) > 1e-9:
            idfail += 1
        # pairing bound: m odd -> D >= p_m (leftover); m even -> D >= 0
        if len(p) % 2 == 1 and D < p[-1] - 1e-9:
            pairfail += 1
        if minD is None or D < minD:
            minD = D
            mincfg = p
    print(f"n={n}: D_n={Dn}, trials={N}, min D seen = {minD:.6f} (target >=1)")
    print(f"   identity failures: {idfail}, pairing-bound failures: {pairfail}")
    print(f"   a minimizing cfg (approx): {[round(x,4) for x in mincfg]}")
    print(f"   m of mincfg = {len(mincfg)} (parity {'odd' if len(mincfg)%2 else 'even'})")
    print(f"   mincfg leftover p_m = {mincfg[-1]:.4f}")
    return minD


if __name__ == "__main__":
    for n in [3, 4]:
        m = check(n, N=30000, seed=42 + n)
        assert m >= 1.0 - 1e-6, f"D>=1 violated at n={n}: {m}"
        print()
    print("All checks passed: D >= 1 holds in every random trial; identity holds for both parities.")


def stress_small_leftover(n, N=60000, seed=1000):
    """Search for configs with D close to 1 AND smallest piece < 1
    (where the pairing bound D>=p_m is insufficient)."""
    rng = np.random.default_rng(seed)
    worst = None  # smallest D among configs with p_m < 1
    worstcfg = None
    count_small = 0
    for _ in range(N):
        # bias splits to create small fragments
        p = refine_tower(n, rng)
        # also try aggressive multi-split of small pieces
        if p[-1] < 1.0 - 1e-9:
            count_small += 1
            D = alternating_sum(p)
            if worst is None or D < worst:
                worst = D
                worstcfg = p
    print(f"n={n}: configs with smallest piece < 1: {count_small}/{N}")
    if worst is not None:
        print(f"   min D among those = {worst:.6f} (target >=1); p_m={worstcfg[-1]:.4f}, m={len(worstcfg)} ({'odd' if len(worstcfg)%2 else 'even'})")
        print(f"   pairing bound D>=p_m would give only D>={worstcfg[-1]:.4f} (insufficient by {1-worstcfg[-1]:.4f})")
        # check gaps carry the deficit
        g, l = gaps_leftover(worstcfg)
        print(f"   gaps={g:.4f}, leftover={l:.4f}, sum={g+l:.6f} (the gaps+leftover cover the deficit)")
    else:
        print("   (none found)")
    return worst


if __name__ == "__main__":
    print("--- stress: small-leftover configs ---")
    for n in [3, 4]:
        stress_small_leftover(n, N=80000, seed=900+n)
        print()
