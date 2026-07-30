"""Round 5: trace near-tower and dominant configs; assess cascade (B) and crux."""
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
def min_D_bp_trace(config, k):
    best = D_of(config); best_seq = []
    if k == 0: return best, best_seq
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]; rest = cs[:i] + cs[i+1:]
        for (q, r) in bp_splits(piece, cs):
            d, seq = min_D_bp_trace(rest + [q, r], k - 1)
            if d < best: best = d; best_seq = [(piece, q, r)] + seq
    return best, best_seq
n = 4
def norm(ic):
    s = sum(ic); return [F(p, s) for p in ic]

def trace(label, ic):
    cfg = norm(ic)
    _MEMO.clear()
    d, seq = min_D_bp_trace(list(cfg), n)
    print(f"[{label}] cfg={ic} sum={sum(ic)} D*={d} ({float(d):.6f}) 1/31={float(F(1,31)):.6f} ratio={float(d/F(1,31)):.4f}")
    cur = list(cfg)
    for mv in seq:
        piece, q, r = mv
        cur2 = list(cur); cur2.remove(piece)
        cur = sorted(cur2 + [q, r], reverse=True)
        print(f"  split {float(piece):.5f} -> {float(q):.5f} + {float(r):.5f}; cfg={[round(float(x),5) for x in cur]}")
    # final residual (uncanceled piece)
    final = sorted(cur, reverse=True)
    print(f"  final sorted: {[round(float(x),5) for x in final]}")
    print()

print("=== near-tower dominant configs (m=5) ===")
trace("(17,8,4,2,1) sum32", [17,8,4,2,1])
trace("(16,8,4,2,1) T_4", [16,8,4,2,1])
trace("(18,8,4,2,1) sum33", [18,8,4,2,1])
trace("(20,8,4,2,1) sum35", [20,8,4,2,1])
trace("(24,8,4,2,1) sum39", [24,8,4,2,1])
trace("(16,8,4,2,1)*2 = 2T_4", [32,16,8,4,2])

print("=== the 3-mark cascade (B) test: pair a1<->a3, pair a2<->a3 ===")
print("Testing the conjectured cascade on crux config (7,6,5,3) with n=4 marks")
trace("(7,6,5,3) m=4 n=4", [7,6,5,3])

print("=== dominant m=5 with a1>>a2 (halving) ===")
trace("(40,10,5,3,2) sum60", [40,10,5,3,2])
trace("(50,8,4,2,1) sum65", [50,8,4,2,1])
