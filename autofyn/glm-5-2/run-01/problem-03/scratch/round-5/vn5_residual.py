"""Round 5: verify the 'halve n largest leave smallest' bottom-up strategy
and characterize when D = a_{n+1} (bottom-dominant) vs when it breaks."""
from fractions import Fraction as F
import sys
sys.setrecursionlimit(300000)

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] if i % 2 == 0 else -s[i] for i in range(len(s)))
def bp_splits(piece, all_pieces):
    cs = {piece / 2}
    for p in all_pieces:
        if 0 < p < piece: cs.add(p); cs.add(piece - p)
    out = []
    for q in cs:
        if 0 < q < piece:
            r = piece - q; out.append((max(q, r), min(q, r)))
    return out
_MEMO = {}
def min_D_bp(config, k):
    key = (tuple(sorted(config, reverse=True)), k)
    if key in _MEMO: return _MEMO[key]
    best = D_of(config)
    if k == 0: _MEMO[key] = best; return best
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]; rest = cs[:i] + cs[i+1:]
        for (q, r) in bp_splits(piece, cs):
            d = min_D_bp(rest + [q, r], k - 1)
            if d < best: best = d
    _MEMO[key] = best; return best

n = 4
def norm(ic):
    s = sum(ic); return [F(p, s) for p in ic]

# Test: for m=5 configs, does "halve the 4 largest leave smallest" give D = a_5
# when a_4 >= 2*a_5 (bottom-dominant)?
print("=== bottom-up halving: D = a_5 when a_4 >= 2*a_5? ===")
# configs where a_4 >= 2*a_5 (bottom-dominant)
bottom_dom = [
    ("(16,8,4,2,1) a4=2>=2*1", [16,8,4,2,1]),
    ("(17,8,4,2,1) a4=2>=2*1", [17,8,4,2,1]),
    ("(20,8,4,2,1) a4=2>=2*1", [20,8,4,2,1]),
    ("(16,8,4,3,1) a4=3>=2*1", [16,8,4,3,1]),
    ("(16,8,6,2,1) a4=2>=2*1", [16,8,6,2,1]),
    ("(10,8,4,2,1) a4=2>=2*1", [10,8,4,2,1]),
    ("(8,8,4,2,1) a4=2>=2*1", [8,8,4,2,1]),
    # a4 < 2*a5 (NOT bottom-dominant)
    ("(16,8,4,3,2) a4=3<2*2=4", [16,8,4,3,2]),
    ("(16,8,4,2,2) a4=2>=2*2? no 2<4", [16,8,4,2,2]),
    ("(10,8,6,4,3) a4=4>=2*3?no", [10,8,6,4,3]),
    ("(8,7,6,5,4) a4=5>=2*4?no", [8,7,6,5,4]),
]
for label, ic in bottom_dom:
    cfg = norm(ic)
    _MEMO.clear()
    d = min_D_bp(list(cfg), n)
    a5 = sorted(cfg, reverse=True)[4]
    # also compute the bottom-up halving D directly
    s = sorted(cfg, reverse=True)
    halves = []
    for i in range(4):  # halve the 4 largest
        halves += [s[i]/2, s[i]/2]
    halves += [s[4]]  # leave smallest
    d_halve = D_of(halves)
    print(f"  [{label}] D*={float(d):.6f} D(halve4+leave)={float(d_halve):.6f} a5={float(a5):.6f} match_a5={abs(float(d_halve)-float(a5))<1e-9}")

# Key: is the OPTIMAL strategy always "halve some subset + leave one" for m=5?
# And is D* = min over which piece to leave unsplit?
print()
print("=== compare: leave each piece unsplit, halve the other 4 ===")
test_cfgs = [
    [16,8,4,2,1],
    [17,8,4,2,1],
    [20,8,4,2,1],
    [10,8,4,2,1],
    [8,7,6,5,4],
]
for ic in test_cfgs:
    cfg = norm(ic)
    s = sorted(cfg, reverse=True)
    _MEMO.clear()
    d_opt = min_D_bp(list(cfg), n)
    print(f"  cfg={ic} D*={float(d_opt):.6f}")
    for leave in range(5):
        halves = []
        for i in range(5):
            if i == leave:
                halves += [s[i]]
            else:
                halves += [s[i]/2, s[i]/2]
        d_h = D_of(halves)
        marker = " <-OPT" if abs(float(d_h)-float(d_opt))<1e-9 and float(d_h) <= float(d_opt)+1e-9 else ""
        print(f"    leave piece {leave} (val {float(s[leave]):.5f}): D(halve)={float(d_h):.6f}{marker}")
