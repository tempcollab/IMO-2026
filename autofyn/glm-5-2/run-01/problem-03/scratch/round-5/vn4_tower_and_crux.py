"""
Round 5: Test the tower T_4 and sum-31 configs, plus random crux search.
Find if ANY n=4 config exceeds 1/31.
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

def norm(intcfg):
    s = sum(intcfg)
    return [F(p, s) for p in intcfg]

def is_crux(cfg):
    s = sorted(cfg, reverse=True)
    if len(s) < 3: return False
    return s[0] < 2 * s[1] and s[2] > s[0] / 2

n = 4
target = F(1, 31)

# ---- Test tower and near-tower configs ----
print("="*60)
print("Tower and near-tower configs (sum near 31)")
print("="*60)
near_tower = [
    ("T_4", [16,8,4,2,1]),
    ("(17,8,4,2,0..1)", [16,8,4,2,1]),  # same
    ("(16,8,4,2)+1mark", [16,8,4,2]),   # m=4
    ("(16,8,4,1,1,1) too many m=6", None),
    ("(15,8,5,2,1)", [15,8,5,2,1]),
    ("(15,8,4,3,1)", [15,8,4,3,1]),
    ("(14,8,6,2,1)", [14,8,6,2,1]),
    ("(14,9,4,2,1)", [14,9,4,2,1]),
    ("(13,10,4,2,1)", [13,10,4,2,1]),
    ("(12,11,4,2,1)", [12,11,4,2,1]),
    ("(16,7,4,2,1)", [16,7,4,2,1]),
    ("(16,8,3,2,2)", [16,8,3,2,2]),
    ("(16,9,3,2,1)", [16,9,3,2,1]),
    ("(16,10,2,2,1)", [16,10,2,2,1]),
    ("(20,6,3,1,1)", [20,6,3,1,1]),
    ("(24,4,2,1,0->m4)", [24,4,2,1]),
    # scaled towers
    ("T_3 scaled (16,8,4)/28", [16,8,4]),
    ("T_3*2 (8,4,2)*2 sum28", None),
]

worst = F(0); worst_cfg = None
for label, ic in [(l, c) for l, c in near_tower if c is not None]:
    cfg = norm(ic)
    _MEMO.clear()
    d = min_D_bp(list(cfg), n)
    M2 = sorted(cfg, reverse=True)[1]
    v4 = M2 / 8
    ratio = float(d / target) if target > 0 else 0
    print(f"[{label}] cfg={ic} D*={d} ({float(d):.6f}) 1/31={float(target):.6f} ratio={ratio:.4f} crux={is_crux(cfg)}")
    if d > worst: worst = d; worst_cfg = ic

print(f"\nWorst of near-tower set: D*={worst} ({float(worst):.6f}) cfg={worst_cfg}")

# ---- Random float crux search: is D* ever > 1/31? ----
print()
print("="*60)
print("Random float crux search (n=4, breakpoint-only)")
print("="*60)
rng = np.random.default_rng(12345)
worst_r = 0.0; worst_rcfg = None; worst_rd = None
violations = 0
N = 1500
for trial in range(N):
    m = int(rng.integers(3, 6))  # m = 3,4,5
    for _ in range(50):
        raw = rng.dirichlet([1]*m)
        cfg = sorted(raw, reverse=True)
        if cfg[0] < 2*cfg[1] and (m >= 3) and cfg[2] > cfg[0]/2:
            break
    else:
        continue
    # use float config (not Fraction) for speed
    _MEMO.clear()
    # convert to a hashable form for memo — use rounded floats
    cfgkey = [round(x, 10) for x in cfg]
    d = min_D_bp(list(cfgkey), n)
    r = float(d) / float(target)
    if r > worst_r:
        worst_r = r; worst_rcfg = cfg; worst_rd = float(d)
    if float(d) > float(target) + 1e-9:
        violations += 1
        if violations <= 5:
            print(f"  VIOLATION trial={trial}: D*={float(d):.6f} > 1/31={float(target):.6f} cfg={[round(x,5) for x in cfg]}")
print(f"Random crux search: {N} trials, violations={violations}")
print(f"  worst ratio D*/(1/31) = {worst_r:.5f}, D*={worst_rd:.6f}")
print(f"  worst cfg = {[round(x,5) for x in worst_rcfg] if worst_rcfg else None}")

# ---- Random float search over ALL configs (not just crux) ----
print()
print("="*60)
print("Random float search ALL configs (n=4)")
print("="*60)
rng2 = np.random.default_rng(99999)
worst_r2 = 0.0; worst_rcfg2 = None; worst_rd2 = None; viol2 = 0
N2 = 1500
for trial in range(N2):
    m = int(rng2.integers(2, 6))
    raw = rng2.dirichlet([1]*m)
    cfg = sorted(raw, reverse=True)
    _MEMO.clear()
    cfgkey = [round(x, 10) for x in cfg]
    d = min_D_bp(list(cfgkey), n)
    r = float(d) / float(target)
    if r > worst_r2:
        worst_r2 = r; worst_rcfg2 = cfg; worst_rd2 = float(d)
    if float(d) > float(target) + 1e-9:
        viol2 += 1
        if viol2 <= 5:
            print(f"  VIOLATION trial={trial}: D*={float(d):.6f} > 1/31 cfg={[round(x,5) for x in cfg]}")
print(f"Random all-config search: {N2} trials, violations={viol2}")
print(f"  worst ratio D*/(1/31) = {worst_r2:.5f}, D*={worst_rd2:.6f}")
print(f"  worst cfg = {[round(x,5) for x in worst_rcfg2] if worst_rcfg2 else None}")
