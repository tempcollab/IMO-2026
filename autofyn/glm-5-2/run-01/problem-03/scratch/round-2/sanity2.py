from fractions import Fraction

def alt_sum(pieces):
    s = sorted([p for p in pieces if p > 0], reverse=True)
    D = Fraction(0)
    for i, x in enumerate(s):
        D += x if i % 2 == 0 else -x
    return D

# === PLATEAU claim for n=3 ===
# Tower T_3 = (8,4,2,1)/15, tower units. Xiang <= 3 marks, min D should be 1 (tower units).
# Claim: 121 configs at D=1, only 1 dyadic (the frontier {4,4,2,2,1,1,1}).
# We verify the frontier claim and that all frontiers give D>=1.

# Enumerate all balanced-split frontiers of T_3 (tower units): expand subset of levels {1,2,3}
# Level k piece = 2^k. Expanding level k: 2^k -> 2^{k-1}+2^{k-1}.
# A frontier = antichain of expansions.
from itertools import combinations
def frontiers(n):
    """All frontiers of T_n: start with {2^n,...,2,1}; choose subset S of levels {1..n} to expand.
    Expanding level k replaces 2^k with two 2^{k-1}. But expanding cascades? 
    Actually a 'frontier' here = a full expansion pattern: for each level 1..n, decide expand or not.
    If expand level k: 2^k -> 2^{k-1}, 2^{k-1}. Non-recursive single expansion per level."""
    # Simpler: each level k in 1..n: either keep 2^k, or split into 2^{k-1}+2^{k-1}.
    pieces_by_level = {}
    configs = []
    for mask in range(2**n):
        pieces = []
        # level 0 (piece 1) always kept
        pieces.append(1)
        for k in range(1, n+1):
            if mask & (1 << (k-1)):
                # split 2^k -> 2^{k-1} + 2^{k-1}
                pieces.append(2**(k-1))
                pieces.append(2**(k-1))
            else:
                pieces.append(2**k)
        configs.append(pieces)
    return configs

print("=== All frontiers of T_3 give D >= 1 (tower units) ===")
fr = frontiers(3)
Dvals = {}
for cfg in fr:
    D = alt_sum(cfg)
    Dvals.setdefault(D, []).append(cfg)
for D in sorted(Dvals):
    print(f"  D={D}: {len(Dvals[D])} configs, e.g. {sorted(Dvals[D][0],reverse=True)}")
print(f"  min frontier D = {min(Dvals)}, >=1? {min(Dvals)>=1}")

# The tight frontier {2,...,n} = all levels expanded except 0 and 1:
tight = frontiers(3)
# mask that splits levels 2,3 but not 1? "expand all above m=1" -> mask = split all levels >=2
mask_tight = 0
for k in range(2, 4):  # levels 2,3
    mask_tight |= (1 << (k-1))
for cfg in tight:
    pass
# Just construct directly
cfg_tight = [1, 2]  # level 0, level1 kept
for k in [2,3]:
    cfg_tight += [2**(k-1), 2**(k-1)]
print(f"  tight frontier (split levels 2,3) {sorted(cfg_tight,reverse=True)}: D = {alt_sum(cfg_tight)}")

# === Non-dyadic breakpoints on plateaus: n=3, check that D as function of a split position
# is piecewise-linear and the minimum lies on a plateau reaching a dyadic breakpoint.
# Take T_3 tower units = (8,4,2,1). Split the top 8 into p+q (p>=q). Vary q in [0,4].
print("\n=== T_3 single top-split: D as function of q (tower units) ===")
tower_rest = [4,2,1]
for q_num in range(0, 33):
    q = Fraction(q_num, 8)  # q in [0,4] step 1/8
    p = 8 - q
    D = alt_sum([p, q] + tower_rest)
    print(f"  q={q}: D={D}", end="")
    if q_num % 4 == 0:
        print("  <-- q=2^{n-1}=4 or multiple", end="")
    print()
