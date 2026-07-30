"""
Round 5: Systematic search for the WORST n=4 crux config (maximizing D*).
Also search ALL n=4 integer configs to find the global max D* and confirm
the tower T_4 is the unique worst (D* = 1/31).
"""
from fractions import Fraction as F
import sys
sys.setrecursionlimit(300000)

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] if i % 2 == 0 else -s[i] for i in range(len(s)))

def bp_splits(piece, all_pieces):
    cs = {piece / 2}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p); cs.add(piece - p)
    out = []
    for q in cs:
        if 0 < q < piece:
            r = piece - q
            out.append((max(q, r), min(q, r)))
    return out

_MEMO = {}
def min_D_bp(config, k):
    key = (tuple(sorted(config, reverse=True)), k)
    if key in _MEMO: return _MEMO[key]
    best = D_of(config)
    if k == 0:
        _MEMO[key] = best; return best
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]; rest = cs[:i] + cs[i+1:]
        for (q, r) in bp_splits(piece, cs):
            d = min_D_bp(rest + [q, r], k - 1)
            if d < best: best = d
    _MEMO[key] = best; return best

def norm(intcfg):
    s = sum(intcfg)
    return [F(p, s) for p in intcfg]

def is_crux(cfg):
    s = sorted(cfg, reverse=True)
    if len(s) < 3: return False
    return s[0] < 2 * s[1] and s[2] > s[0] / 2

# Enumerate ALL integer partitions of D into m parts (sorted desc), m in {2,3,4,5}.
# D ranges up to some bound. For n=4, target 1/31.
def gen_partitions(D, m):
    """Generate all sorted-desc m-tuples of positive ints summing to D."""
    def rec(remaining, parts, max_val):
        if len(parts) == m:
            if remaining == 0:
                yield tuple(parts)
            return
        for v in range(min(remaining, max_val), 0, -1):
            if remaining - v >= (m - len(parts) - 1):  # enough left
                yield from rec(remaining - v, parts + [v], v)
    yield from rec(D, [], D)

n = 4
target = F(1, 31)
worst_d = F(0)
worst_cfg = None
worst_crux_d = F(0)
worst_crux_cfg = None
D_max = 28  # search denominators up to 28 (tower is 31, but we test that separately)

print(f"Searching all n=4 integer configs, D (sum) from {n+1} to {D_max}...")
total = 0
for D in range(n+1, D_max + 1):
    for m in range(1, n + 2):  # m = 1..5
        for parts in gen_partitions(D, m):
            total += 1
            cfg = [F(p, D) for p in parts]
            # do NOT clear memo — keyed by (config,k), reuse across configs
            d = min_D_bp(list(cfg), n)
            if d > worst_d:
                worst_d = d
                worst_cfg = parts
            if is_crux(cfg) and d > worst_crux_d:
                worst_crux_d = d
                worst_crux_cfg = parts
    if D % 5 == 0 or D == D_max:
        print(f"  D={D}: configs so far={total}, global worst D*={float(worst_d):.6f} ({worst_cfg}), worst crux D*={float(worst_crux_d):.6f} ({worst_crux_cfg})")

print()
print(f"Total configs searched: {total}")
print(f"GLOBAL WORST: D* = {worst_d} = {float(worst_d):.6f}, cfg={worst_cfg}")
print(f"  target 1/31 = {float(target):.6f}, ratio D*/target = {float(worst_d / target):.6f}")
print(f"WORST CRUX: D* = {worst_crux_d} = {float(worst_crux_d):.6f}, cfg={worst_crux_cfg}")
print(f"  ratio to target = {float(worst_crux_d / target):.6f}")
