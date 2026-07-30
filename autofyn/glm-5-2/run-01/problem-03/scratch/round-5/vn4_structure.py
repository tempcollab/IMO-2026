"""
Round 5: Structural probe — which n=4 configs give 0 < D* < 1/31?
And confirm: m<=4 => D*=0 (Xiang halves all pieces).
Also: characterize the winning strategy pattern for the hardest non-tower m=5 configs.
"""
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

def min_D_bp_trace(config, k):
    best = D_of(config); best_seq = []
    if k == 0: return best, best_seq
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]; rest = cs[:i] + cs[i+1:]
        for (q, r) in bp_splits(piece, cs):
            d, seq = min_D_bp_trace(rest + [q, r], k - 1)
            if d < best:
                best = d; best_seq = [(piece, q, r)] + seq
    return best, best_seq

n = 4; target = F(1, 31)

# ---- 1. Confirm m<=4 => D*=0 ----
print("="*60)
print("1. m<=4 configs: confirm D*=0 (Xiang halves all pieces)")
print("="*60)
rng = np.random.default_rng(7)
m4_nonzero = 0
for _ in range(300):
    for _ in range(50):
        raw = rng.dirichlet([1]*4)
        cfg = sorted(raw, reverse=True)
        break
    _MEMO.clear()
    cfgkey = [round(x,10) for x in cfg]
    d = min_D_bp(list(cfgkey), n)
    if float(d) > 1e-9:
        m4_nonzero += 1
        print(f"  m=4 nonzero! D*={float(d):.6f} cfg={[round(x,5) for x in cfg]}")
print(f"m=4: {m4_nonzero}/300 configs with D*>0")

# m=3
m3_nonzero = 0
for _ in range(300):
    raw = rng.dirichlet([1]*3)
    cfg = sorted(raw, reverse=True)
    _MEMO.clear()
    cfgkey = [round(x,10) for x in cfg]
    d = min_D_bp(list(cfgkey), n)
    if float(d) > 1e-9:
        m3_nonzero += 1
print(f"m=3: {m3_nonzero}/300 configs with D*>0")

# ---- 2. m=5 configs with 0 < D* < 1/31: characterize ----
print()
print("="*60)
print("2. m=5 configs with 0 < D* < 1/31 (the 'in-between' configs)")
print("="*60)
rng2 = np.random.default_rng(2024)
positive_cfgs = []
N = 3000
for _ in range(N):
    raw = rng2.dirichlet([1]*5)
    cfg = sorted(raw, reverse=True)
    _MEMO.clear()
    cfgkey = [round(x,10) for x in cfg]
    d = min_D_bp(list(cfgkey), n)
    if float(d) > 1e-7:
        positive_cfgs.append((cfg, float(d)))
print(f"m=5: {len(positive_cfgs)}/{N} configs with D*>0")
if positive_cfgs:
    positive_cfgs.sort(key=lambda x: -x[1])
    print("Top 10 hardest m=5 configs (D* > 0):")
    for cfg, d in positive_cfgs[:10]:
        M2 = sorted(cfg, reverse=True)[1]
        v4 = M2/8
        is_tower_like = all(abs(cfg[i] - cfg[i+1]*2 - 1e-3) < 0.01 for i in range(len(cfg)-1)) if len(cfg)>=5 else False
        print(f"  D*={d:.6f} ratio={d/float(target):.4f} V4={v4:.6f} cfg={[round(x,5) for x in cfg]}")
    # trace the hardest
    print()
    print("Tracing the hardest m=5 config:")
    cfg = positive_cfgs[0][0]
    _MEMO.clear()
    cfgkey = [round(x,10) for x in cfg]
    d, seq = min_D_bp_trace(list(cfgkey), n)
    cur = list(cfgkey)
    for mv in seq:
        piece, q, r = mv
        cur2 = list(cur); cur2.remove(piece)
        cur = sorted(cur2 + [q, r], reverse=True)
        print(f"  split {piece:.5f} -> {float(q):.5f} + {float(r):.5f}; cfg={[round(float(x),5) for x in cur]}")
    print(f"  final D = {d:.6f}")

# ---- 3. Test scaled towers and "tower-like" configs ----
print()
print("="*60)
print("3. Scaled/partial towers and tower-like configs")
print("="*60)
def norm(ic):
    s = sum(ic); return [F(p, s) for p in ic]
test_towers = [
    ("T_4", [16,8,4,2,1]),
    ("2*T_4", [32,16,8,4,2]),
    ("T_4+1 bottom", [16,8,4,2,1+1]),
    ("T_4 tail doubled", [16,8,4,2,2]),
    ("T_4 swap (16,8,4,1,2)", [16,8,4,1,2]),
    ("partial tower (16,8,4,2,0.5->int)", [32,16,8,4,1]),
    ("(16,8,4,2,1) exact", [16,8,4,2,1]),
    # near-tower with small perturbation
    ("(16,8,4,3,1)", [16,8,4,3,1]),
    ("(16,8,5,2,1)", [16,8,5,2,1]),
    ("(17,8,4,2,1)", [17,8,4,2,1]),
    ("(16,9,4,2,1)", [16,9,4,2,1]),
    ("(31,16,8,4,2)/61 T_5 trunc?", [31,16,8,4,2]),
]
for label, ic in test_towers:
    cfg = norm(ic)
    _MEMO.clear()
    d = min_D_bp(list(cfg), n)
    M2 = sorted(cfg, reverse=True)[1]
    print(f"  [{label}] cfg={ic} D*={d} ({float(d):.6f}) ratio={float(d/target):.4f} crux={cfg[0]<2*cfg[1] and (len(cfg)>=3 and cfg[2]>cfg[0]/2)}")
