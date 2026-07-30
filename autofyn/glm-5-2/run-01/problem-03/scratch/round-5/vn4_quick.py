"""Round 5: quick structural probe (reduced)."""
from fractions import Fraction as F
import numpy as np
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

n = 4; target = F(1, 31)
def norm(ic):
    s = sum(ic); return [F(p, s) for p in ic]

# 1. m<=4 confirm D*=0
print("=== m<=4: confirm D*=0 ===")
rng = np.random.default_rng(7)
m4nz = 0; m3nz = 0
for _ in range(120):
    raw = rng.dirichlet([1]*4); cfg = sorted(raw, reverse=True)
    _MEMO.clear(); d = min_D_bp([round(x,10) for x in cfg], n)
    if float(d) > 1e-9: m4nz += 1
for _ in range(120):
    raw = rng.dirichlet([1]*3); cfg = sorted(raw, reverse=True)
    _MEMO.clear(); d = min_D_bp([round(x,10) for x in cfg], n)
    if float(d) > 1e-9: m3nz += 1
print(f"m=4: {m4nz}/120 nonzero; m=3: {m3nz}/120 nonzero")

# 2. m=5 hardest configs (reduced N)
print()
print("=== m=5: configs with D*>0 ===")
rng2 = np.random.default_rng(2024)
pos = []
N = 600
for _ in range(N):
    raw = rng2.dirichlet([1]*5); cfg = sorted(raw, reverse=True)
    _MEMO.clear(); d = min_D_bp([round(x,10) for x in cfg], n)
    if float(d) > 1e-7: pos.append((cfg, float(d)))
print(f"m=5: {len(pos)}/{N} configs with D*>0")
pos.sort(key=lambda x: -x[1])
for cfg, d in pos[:8]:
    M2 = sorted(cfg, reverse=True)[1]
    print(f"  D*={d:.6f} ratio={d/float(target):.4f} V4={M2/8:.6f} cfg={[round(x,5) for x in cfg]}")

# trace hardest
if pos:
    print()
    print("Trace hardest m=5 config:")
    cfg = pos[0][0]
    _MEMO.clear(); d, seq = min_D_bp_trace([round(x,10) for x in cfg], n)
    cur = list([round(x,10) for x in cfg])
    for mv in seq:
        piece, q, r = mv
        cur2 = list(cur); cur2.remove(piece)
        cur = sorted(cur2 + [q, r], reverse=True)
        print(f"  split {float(piece):.5f} -> {float(q):.5f} + {float(r):.5f}; cfg={[round(float(x),5) for x in cur]}")
    print(f"  final D={float(d):.6f}")

# 3. tower-like configs
print()
print("=== tower-like configs ===")
towers = [
    ("T_4", [16,8,4,2,1]),
    ("2*T_4", [32,16,8,4,2]),
    ("(16,8,4,3,1)", [16,8,4,3,1]),
    ("(16,8,5,2,1)", [16,8,5,2,1]),
    ("(17,8,4,2,1)", [17,8,4,2,1]),
    ("(16,9,4,2,1)", [16,9,4,2,1]),
    ("(31,16,8,4,2)/61", [31,16,8,4,2]),
    ("(16,8,4,2,2)tail2", [16,8,4,2,2]),
]
for label, ic in towers:
    cfg = norm(ic)
    _MEMO.clear(); d = min_D_bp(list(cfg), n)
    M2 = sorted(cfg, reverse=True)[1]
    crux = cfg[0]<2*cfg[1] and (len(cfg)>=3 and cfg[2]>cfg[0]/2)
    print(f"  [{label}] D*={d} ({float(d):.6f}) ratio={float(d/target):.4f} crux={crux}")
