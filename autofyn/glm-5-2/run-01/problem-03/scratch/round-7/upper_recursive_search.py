#!/usr/bin/env python3
"""
Round-7 upper-bound recursive-search verification for GAP-U2-compressed
(majorization-upper approach, imo-2026-03).

Three exact-Fraction tests:
  (1) GREEDY CASCADE REPRODUCTION (falsified by (12,4,3,2)/21).
  (2) GAP-SubsetSum exact test: for each compressed config with a_1 <= 2^n/D_n,
      does a subset S of {a_2..a_{n+1}} exist with sum(S) in [a_1-1/D_n, a_1]?
      (O2 single-piece split-a_1 strategy.) Exact, finite (2^n subsets).
  (3) RECURSIVE MULTI-PIECE SEARCH: for every compressed config, a recursive
      depth-first search over tie-creating binary splits + halving, budget n
      marks, exact Fraction. Reports min D, worst non-tower ratio, and the
      winning strategy pattern (halving-only / match-from-a_1 / multi-piece).

All arithmetic uses fractions.Fraction (exact). No floats.
"""

from fractions import Fraction
from itertools import combinations
from functools import lru_cache

Dn_cache = {}
def Dn(n):  # 2^{n+1} - 1
    if n not in Dn_cache:
        Dn_cache[n] = 2**(n+1) - 1
    return Dn_cache[n]

def alt_sum(pieces):
    """D = alternating sum of sorted (non-increasing) multiset of Fraction values."""
    s = sorted(pieces, reverse=True)
    D = Fraction(0)
    for i, v in enumerate(s):
        if i % 2 == 0:
            D += v
        else:
            D -= v
    return D

# ----------------------------------------------------------------------
# (1) GREEDY CASCADE on (12,4,3,2)/21, n=3
# ----------------------------------------------------------------------
def greedy_cascade(config):
    """Greedy: split a_1 -> {a_2, a_1-a_2}, then remainder -> {a_3, r-a_3}, ...
    Returns the refined multiset (using marks) and marks used.
    config = list of Fractions (a_1 > ... > a_{n+1}), length n+1."""
    a = list(config)
    n = len(a) - 1   # n+1 pieces, indices 0..n
    marks = 0
    r = a[0]          # active remainder (from splitting a_1)
    idx = 1           # next piece to match: a_1, ..., a_n (i.e. a[1..n]); a[n]=a_{n+1} untouched
    while idx <= n and marks < n - 1 and r >= a[idx]:
        # split r -> {a[idx], r - a[idx]}; the matched a[idx] ties with the original a[idx]
        r = r - a[idx]
        marks += 1
        idx += 1
    # build final multiset:
    #   a[1..idx-1] are DOUBLED (tie): 2 copies each
    #   a[idx..n-1] (i.e. a_idx..a_n) untouched: 1 copy each
    #   a[n] = a_{n+1} untouched: 1 copy
    #   remainder r: 1 copy
    final = []
    for j in range(1, idx):
        final.append(a[j]); final.append(a[j])
    for j in range(idx, n):   # a_idx .. a_{n} (indices idx..n-1), i.e. a_{idx+1}..a_n in 1-based
        final.append(a[j])
    final.append(a[n])        # a_{n+1}
    final.append(r)           # remainder
    return final, marks

def test_greedy_counterexample():
    print("=" * 70)
    print("(1) GREEDY CASCADE reproduction (falsified by (12,4,3,2)/21, n=3)")
    print("=" * 70)
    n = 3
    S = 21
    config_real = [Fraction(x, S) for x in [12, 4, 3, 2]]
    target = Fraction(1, Dn(n))
    print(f"config = (12,4,3,2)/{S}, n={n}, target D <= 1/D_n = 1/{Dn(n)} = {float(target):.6f}")
    final, marks = greedy_cascade(config_real)
    D = alt_sum(final)
    print(f"greedy cascade: marks used = {marks}")
    print(f"  refined multiset (x{S}): {sorted([int(x*S) for x in final], reverse=True)}")
    print(f"  D = {D} = {float(D):.6f}   D*{S} = {D*S}")
    print(f"  D / target = {float(D/target):.4f}")
    if D > target:
        print(f"  VIOLATION: D = {D} > 1/D_n = {target}  (greedy FALSIFIED)")
    else:
        print(f"  no violation")
    # the achieving strategy: halve a_1 (12->6,6) and halve a_4 (2->1,1)
    print("\n  Achieving strategy 'halve a_1 and a_4':")
    ach = [Fraction(6,S), Fraction(6,S), Fraction(4,S), Fraction(3,S), Fraction(1,S), Fraction(1,S)]
    Da = alt_sum(ach)
    print(f"    refined (x{S}): {sorted([int(x*S) for x in ach], reverse=True)}")
    print(f"    D = {Da} = {float(Da):.6f}  (= a_2 - a_3 = {4-3}/{S} = {Fraction(4-3,S)})")
    print(f"    D / target = {float(Da/target):.4f}   <= 1: {Da <= target}")
    print()

# ----------------------------------------------------------------------
# (2) GAP-SubsetSum exact test
# ----------------------------------------------------------------------
def subset_sum_test(config_real, n):
    """For config (a_1..a_{n+1}) real Fractions summing to 1, compressed (a_{n+1}>1/D_n),
    a_1 <= 2^n/D_n regime: does S subset of {a_2..a_{n+1}} exist with
    sum(S) in [a_1 - 1/D_n, a_1]? Returns (hit, best_leftover, best_subset_ints)."""
    target = Fraction(1, Dn(n))
    a1 = config_real[0]
    rest = config_real[1:]
    lo = a1 - target
    hi = a1
    best_leftover = None
    best_sub = None
    for k in range(0, len(rest)+1):
        for sub in combinations(range(len(rest)), k):
            s = sum(rest[i] for i in sub)
            if lo <= s <= hi:
                leftover = a1 - s
                if best_leftover is None or leftover < best_leftover:
                    best_leftover = leftover
                    best_sub = tuple(rest[i] for i in sub)
    return (best_leftover is not None, best_leftover, best_sub)

# ----------------------------------------------------------------------
# (3) RECURSIVE MULTI-PIECE SEARCH
# ----------------------------------------------------------------------
def recursive_min_D(config_real, n, marks_budget):
    """Recursive DFS over tie-creating binary splits + halving.
    State: tuple of Fractions (sorted non-increasing). Budget = marks.
    Splits tried:
      A. halve a piece v -> {v/2, v/2} (tie at v/2)
      B. split v -> {t, v-t} where t is a value currently present (tie at t)
      C. split v -> {a_i, v-a_i} where a_i is an ORIGINAL config value (O2 reproduce)
         (captured even after a_i itself has been split, to allow reproducing from a_1)
    Returns (min_D, strategy_description, marks_used_min)."""
    init = tuple(sorted(config_real, reverse=True))
    original_vals = set(config_real)
    best = [alt_sum(init), "stop", 0]
    visited = set()
    node_cap = 400000
    nodes = 0
    stack = [(init, marks_budget, [], 0)]
    while stack:
        if nodes >= node_cap:
            break
        nodes += 1
        state, budget, moves, mu = stack.pop()
        key = (state, budget)
        if key in visited:
            continue
        visited.add(key)
        D = alt_sum(state)
        if D < best[0] or (D == best[0] and mu < best[2]):
            best = [D, moves_to_label(moves), mu]
        if best[0] == 0:
            break
        if budget == 0:
            continue
        vals = sorted(set(state), reverse=True)
        tried_splits = set()
        for v in vals:
            # option A: halve v
            w = v / 2
            k = (v, 'halve')
            if k not in tried_splits:
                tried_splits.add(k)
                new = list(state); new.remove(v); new.append(w); new.append(w)
                stack.append((tuple(sorted(new, reverse=True)), budget-1,
                              moves + [(v, 'halve')], mu+1))
            # option B: split v -> {t, v-t}, t currently present, t<v
            for t in vals:
                if t == v or t >= v:
                    continue
                c = v - t
                if c <= 0:
                    continue
                k = (v, t, 'match')
                if k in tried_splits:
                    continue
                tried_splits.add(k)
                new = list(state); new.remove(v); new.append(t); new.append(c)
                stack.append((tuple(sorted(new, reverse=True)), budget-1,
                              moves + [(v, f'match-{t}')], mu+1))
            # option C: O2 reproduce -- split v -> {a_i, v-a_i}, a_i original value, a_i<v
            for t in original_vals:
                if t == v or t >= v:
                    continue
                c = v - t
                if c <= 0:
                    continue
                k = (v, t, 'orig')
                if k in tried_splits:
                    continue
                tried_splits.add(k)
                new = list(state); new.remove(v); new.append(t); new.append(c)
                stack.append((tuple(sorted(new, reverse=True)), budget-1,
                              moves + [(v, f'orig-{t}')], mu+1))
        if len(stack) > 250000:
            stack.sort(key=lambda x: alt_sum(x[0]))
            stack = stack[:50000]
    return best

def moves_to_label(moves):
    if not moves:
        return "stop"
    halve_count = sum(1 for m in moves if m[1] == 'halve')
    match_count = sum(1 for m in moves if m[1].startswith('match'))
    comp_count = sum(1 for m in moves if m[1].startswith('comp'))
    orig_count = sum(1 for m in moves if m[1].startswith('orig'))
    parts = []
    if halve_count: parts.append(f"halve x{halve_count}")
    if match_count: parts.append(f"match x{match_count}")
    if comp_count: parts.append(f"comp x{comp_count}")
    if orig_count: parts.append(f"orig-reproduce x{orig_count}")
    return ", ".join(parts) if parts else "stop"

# ----------------------------------------------------------------------
# Generate compressed integer configs for given n, maxsum Smax
# ----------------------------------------------------------------------
def gen_compressed_configs(n, Smax):
    """Generate strictly-decreasing integer configs (A_1 > ... > A_{n+1})
    with sum S <= Smax and A_{n+1} > S/D_n (compressed, in real units)."""
    D = Dn(n)
    configs = []
    # recursive generation
    def rec(remaining, prev, depth, acc):
        if depth == n + 1:
            if remaining == 0:
                S = sum(acc)
                a_last_real = Fraction(acc[-1], S)
                if a_last_real > Fraction(1, D):
                    configs.append(tuple(acc))
            return
        # next value < prev, >= 1, and we need n+1-depth more strictly decreasing
        max_v = prev - 1
        # need remaining to be split into (n+1-depth) strictly decreasing positive ints each < prev
        # min sum for k more values = k(k+1)/2 (values 1..k) but must be < prev
        k = n + 1 - depth
        min_sum = k * (k + 1) // 2
        if remaining < min_sum:
            return
        for v in range(max_v, 0, -1):
            # also need v <= remaining - (min sum of k-1 below v) = remaining - (k-1)k/2
            if v > remaining - (k - 1) * k // 2:
                continue
            if v * k < remaining:  # too small to reach (rough)
                # but strictly decreasing so max sum is v + (v-1) + ...; check feasibility
                pass
            rec(remaining - v, v, depth + 1, acc + [v])
    # S ranges from Dn+1 (need a_{n+1} > 1/Dn, i.e. A_{n+1} > S/Dn, smallest S where possible)
    # smallest S with a_{n+1} > S/Dn: S/Dn < A_{n+1} <= S/(n+1) roughly; need S > ... just iterate
    Smin = Dn(n) + 1  # tower is at S = Dn(n); compressed needs S > Dn(n) so a_{n+1}=1 at S=Dn+1? Actually tower has S=Dn(n), a_{n+1}=1, 1/Dn = 1/Dn, equal (boundary). Compressed: a_{n+1} > 1/Dn.
    for S in range(Smin, Smax + 1):
        # A_{n+1} >= 1, and we need A_{n+1}/S > 1/Dn i.e. A_{n+1} > S/Dn
        rec(S, S + 1, 0, [])
    return configs

# ======================================================================
# MAIN
# ======================================================================
def main():
    test_greedy_counterexample()

    print("=" * 70)
    print("(2) GAP-SubsetSum exact test (a_1 <= 2^n/D_n regime)")
    print("=" * 70)
    for n in [2, 3, 4]:
        D = Dn(n)
        Smax = {2: 60, 3: 80, 4: 60}[n]
        configs = gen_compressed_configs(n, Smax)
        threshold_real = Fraction(2**n, D)  # a_1 <= 2^n/D_n
        subset_hits = 0
        subset_misses = 0
        miss_examples = []
        total = 0
        for cfg in configs:
            S = sum(cfg)
            reals = [Fraction(x, S) for x in cfg]
            a1 = reals[0]
            total += 1
            if a1 <= threshold_real:
                hit, lo, sub = subset_sum_test(reals, n)
                if hit:
                    subset_hits += 1
                else:
                    subset_misses += 1
                    if len(miss_examples) < 5:
                        miss_examples.append((cfg, S, float(a1), float(threshold_real)))
        print(f"n={n}, Smax={Smax}: {len(configs)} compressed configs; "
              f"a_1<=2^n/D_n regime: {subset_hits+subset_misses} configs; "
              f"subset-sum HIT {subset_hits}, MISS {subset_misses}")
        if miss_examples:
            print(f"  MISS examples (a_1, threshold={float(threshold_real):.4f}):")
            for cfg, S, a1f, tf in miss_examples:
                print(f"    {cfg} / {S}   a_1={a1f:.4f}")
        else:
            print(f"  ALL configs in a_1<=2^n/D_n regime have a hitting subset (0 misses)")
    print()

    print("=" * 70)
    print("(3) RECURSIVE MULTI-PIECE SEARCH (tie-creating splits + halving)")
    print("=" * 70)
    for n in [2, 3, 4]:
        D = Dn(n)
        target = Fraction(1, D)
        Smax = {2: 50, 3: 45, 4: 35}[n]
        configs = gen_compressed_configs(n, Smax)
        print(f"\n--- n={n}, Smax={Smax}: {len(configs)} compressed configs ---")
        violations = 0
        worst_ratio = Fraction(0)
        worst_cfg = None
        worst_D = None
        worst_strat = None
        tower_count = 0
        large_top_count = 0
        large_top_hits = 0
        for cfg in configs:
            S = sum(cfg)
            reals = [Fraction(x, S) for x in cfg]
            # is it the tower? tower = (2^n, 2^{n-1}, ..., 1)/D_n
            tower = tuple(2**(n-i) for i in range(n+1))
            is_tower = (cfg == tower)
            if is_tower:
                tower_count += 1
            # recursive search
            best = recursive_min_D(reals, n, n)
            Dval, strat, mu = best
            ratio = Dval / target
            # large-top?
            a1 = reals[0]
            threshold_real = Fraction(2**n, D)
            if a1 > threshold_real:
                large_top_count += 1
                if Dval <= target:
                    large_top_hits += 1
            if Dval > target and not is_tower:
                violations += 1
                if ratio > worst_ratio:
                    worst_ratio = ratio
                    worst_cfg = cfg
                    worst_D = Dval
                    worst_strat = strat
            elif not is_tower and ratio > worst_ratio:
                worst_ratio = ratio
                worst_cfg = cfg
                worst_D = Dval
                worst_strat = strat
        print(f"  violations (D > 1/D_n, non-tower): {violations}")
        print(f"  tower configs (boundary, D=1/D_n expected): {tower_count}")
        print(f"  worst non-tower ratio: {float(worst_ratio):.4f} at {worst_cfg} "
              f"(S={sum(worst_cfg) if worst_cfg else '-'})")
        if worst_cfg:
            print(f"    D = {worst_D} = {float(worst_D):.6f}, 1/D_n = {float(target):.6f}, "
                  f"strategy: {worst_strat}")
        print(f"  large-top (a_1>2^n/D_n) configs: {large_top_count}, "
              f"of which D<=1/D_n: {large_top_hits}")
    print()

    print("=" * 70)
    print("(4) LARGE-TOP REGIME: what multi-piece patterns win?")
    print("=" * 70)
    # for n=3,4 examine large-top configs and classify the winning strategy
    for n in [3, 4]:
        D = Dn(n)
        target = Fraction(1, D)
        Smax = {3: 60, 4: 50}[n]
        configs = gen_compressed_configs(n, Smax)
        threshold_real = Fraction(2**n, D)
        print(f"\n--- n={n} large-top (a_1 > 2^n/D_n) winning strategies ---")
        patterns = {}
        examples = {}
        for cfg in configs:
            S = sum(cfg)
            reals = [Fraction(x, S) for x in cfg]
            a1 = reals[0]
            if a1 <= threshold_real:
                continue
            best = recursive_min_D(reals, n, n)
            Dval, strat, mu = best
            # classify: count halve vs match vs comp
            halve_only = ('halve' in strat and 'match' not in strat and 'comp' not in strat)
            match_only = ('match' in strat and 'halve' not in strat and 'comp' not in strat)
            mixed = ('halve' in strat) and ('match' in strat or 'comp' in strat)
            if halve_only:
                key = "halve-only"
            elif match_only:
                key = "match/comp-only"
            elif mixed:
                key = "mixed(halve+match)"
            elif strat == "stop":
                key = "no-split(D=original altsum)"
            else:
                key = strat
            patterns[key] = patterns.get(key, 0) + 1
            if key not in examples:
                examples[key] = (cfg, S, Dval, strat, mu)
        print(f"  total large-top configs: {sum(patterns.values())}")
        for k, v in sorted(patterns.items(), key=lambda x: -x[1]):
            ex = examples[k]
            print(f"    {k}: {v} configs; example: {ex[0]}/S={ex[1]} D={ex[2]} "
                  f"(={float(ex[2]):.5f}) strat='{ex[3]}' marks={ex[4]}")
    print()

if __name__ == "__main__":
    main()
