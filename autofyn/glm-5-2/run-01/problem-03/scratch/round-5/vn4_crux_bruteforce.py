"""
Round 5: V(n>=4) crux investigation — n=4 optimal Xiang response brute force.

Crux regime: a_1 < 2*a_2 AND a_3 > a_1/2 (three near-equal large pieces).
n=4: Liu has <=5 pieces (m<=5), Xiang has <=4 marks.
Target: D* <= 1/D_4 = 1/31.
V(4) = M_2/8 conjecture.

We compute the EXACT optimal Xiang response (breakpoint-restricted, B1-justified)
using Fraction arithmetic, trace the winning move sequence, and check <= 1/31.

Also check the V(4) bound D* <= M_2/8.
"""
from fractions import Fraction as F
from itertools import product
import sys

sys.setrecursionlimit(200000)


def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] if i % 2 == 0 else -s[i] for i in range(len(s)))


def bp_splits(piece, all_pieces):
    """Breakpoint candidates: half + ties to each other piece (B1-justified).
    Returns list of (q, r) with q >= r > 0, q + r = piece."""
    cs = {piece / 2}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p)
            cs.add(piece - p)
    out = []
    for q in cs:
        if 0 < q < piece:
            r = piece - q
            out.append((max(q, r), min(q, r)))
    return out


_MEMO = {}


def min_D_bp(config, k):
    """Min D over <=k Xiang marks, breakpoint-only (B1-justified). Exact Fraction."""
    key = (tuple(sorted(config, reverse=True)), k)
    if key in _MEMO:
        return _MEMO[key]
    best = D_of(config)
    if k == 0:
        _MEMO[key] = best
        return best
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]
        rest = cs[:i] + cs[i + 1:]
        for (q, r) in bp_splits(piece, cs):
            d = min_D_bp(rest + [q, r], k - 1)
            if d < best:
                best = d
    _MEMO[key] = best
    return best


def min_D_bp_trace(config, k):
    """Min D with the move sequence traced (for understanding the strategy)."""
    best = D_of(config)
    best_seq = []
    if k == 0:
        return best, best_seq
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]
        rest = cs[:i] + cs[i + 1:]
        for (q, r) in bp_splits(piece, cs):
            d, seq = min_D_bp_trace(rest + [q, r], k - 1)
            if d < best:
                best = d
                best_seq = [(piece, q, r)] + seq
    return best, best_seq


def norm(intcfg):
    """Normalize integer config to sum 1 (scale-free D)."""
    s = sum(intcfg)
    return [F(p, s) for p in intcfg]


def is_crux(cfg):
    """a_1 < 2*a_2 AND a_3 > a_1/2."""
    s = sorted(cfg, reverse=True)
    if len(s) < 3:
        return False
    return s[0] < 2 * s[1] and s[2] > s[0] / 2


def report(label, intcfg, n=4):
    cfg = norm(intcfg)
    _MEMO.clear()
    d = min_D_bp(list(cfg), n)
    d_trace, seq = min_D_bp_trace(list(cfg), n)
    M2 = sorted(cfg, reverse=True)[1]
    target = F(1, 2 ** (n + 1) - 1)
    v4 = M2 / (2 ** (n - 1))
    ok_target = d <= target
    ok_v4 = d <= v4
    print(f"[{label}] cfg={intcfg} sum={sum(intcfg)}")
    print(f"  D* = {d} = {float(d):.6f}")
    print(f"  1/D_4 = 1/31 = {float(target):.6f}  -> D*<=1/31? {ok_target}")
    print(f"  V(4)=M_2/8 = {v4} = {float(v4):.6f}  -> D*<=V(4)? {ok_v4}")
    print(f"  crux regime? {is_crux(cfg)}")
    print(f"  winning strategy ({len(seq)} marks):")
    cur = list(cfg)
    for mv in seq:
        piece, q, r = mv
        # remove one copy of piece from cur
        cur2 = list(cur)
        cur2.remove(piece)
        cur = sorted(cur2 + [q, r], reverse=True)
        print(f"    split {float(piece):.5f} -> {float(q):.5f} + {float(r):.5f}; now cfg={[round(float(x),5) for x in cur]}")
    print(f"  final D = {d_trace}")
    print()
    return d, v4, target, ok_target, ok_v4, seq


print("=" * 70)
print("n=4 CRUX BRUTE FORCE — worst configs (three near-equal large pieces)")
print("Target: 1/D_4 = 1/31. V(4) = M_2/8.")
print("=" * 70)
print()

# ---- 1. The n=3 Max-bound violators, extended to n=4 (m=5) ----
# (7,6,5,3) was the n=3 violator. Extend with a small 5th piece.
configs_test = [
    ("T_4 tower", [16, 8, 4, 2, 1]),
    ("(7,6,5,3)+1", [7, 6, 5, 3, 1]),
    ("(7,6,5,3)+small", [7, 6, 5, 3, 2]),
    ("(7,6,5,3) n=3 reused m=4", [7, 6, 5, 3]),
    ("(22,19,16,10)+1", [22, 19, 16, 10, 1]),
    ("(15,13,11,6)+1", [15, 13, 11, 6, 1]),
    # balanced triple (three near-equal) + 2 small
    ("(5,5,5,1,1)", [5, 5, 5, 1, 1]),
    ("(6,5,5,1,1)", [6, 5, 5, 1, 1]),
    ("(7,6,6,1,1)", [7, 6, 6, 1, 1]),
    ("(8,7,6,1,1)", [8, 7, 6, 1, 1]),
    ("(8,7,6,2,1)", [8, 7, 6, 2, 1]),
    ("(9,8,7,1,1)", [9, 8, 7, 1, 1]),
    ("(10,9,8,1,1)", [10, 9, 8, 1, 1]),
    # near-tower but crux
    ("(15,8,8,1,1)", [15, 8, 8, 1, 1]),
    ("(14,8,7,1,1)", [14, 8, 7, 1, 1]),
    # three equal + tower tail
    ("(8,8,8,4,2)", [8, 8, 8, 4, 2]),
    ("(8,8,8,2,1)", [8, 8, 8, 2, 1]),
    # m=4 crux (Liu used only 3 marks)
    ("(8,7,6,1)", [8, 7, 6, 1]),
    ("(9,8,7,1)", [9, 8, 7, 1]),
]

results = []
for label, ic in configs_test:
    r = report(label, ic, n=4)
    results.append((label, ic, r))

print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print(f"{'label':30s} {'cfg':20s} {'D*':12s} {'1/31':8s} {'V(4)':12s} {'<=1/31':7s} {'<=V4':6s} {'crux':5s}")
for label, ic, r in results:
    d, v4, target, ok_t, ok_v, seq = r
    print(f"{label:30s} {str(ic):20s} {str(d):12s} {str(target):8s} {str(v4):12s} {str(ok_t):7s} {str(ok_v):6s} {str(is_crux(norm(ic))):5s}")
