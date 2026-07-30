"""
Round 4 — focused n=3 crux investigation.
Crux: a_1 < 2*a_2 AND a_3 > a_1/2. n=3, m=3 or m=4.
"""
import numpy as np
from functools import lru_cache

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits(piece, all_pieces):
    cs = {piece / 2.0}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p)
            cs.add(piece - p)
    return [(q, piece - q) for q in cs if 0 < q < piece]

_MEMO = {}
def min_D_bp(config, k):
    key = (tuple(sorted(config, reverse=True)), k)
    if key in _MEMO:
        return _MEMO[key]
    best = D_of(config)
    if k == 0:
        _MEMO[key] = best
        return best
    cfg_sorted = sorted(config, reverse=True)
    for i in range(len(cfg_sorted)):
        piece = cfg_sorted[i]
        rest = cfg_sorted[:i] + cfg_sorted[i+1:]
        for (q, r) in bp_splits(piece, cfg_sorted):
            new = rest + [q, r]
            d = min_D_bp(new, k - 1)
            if d < best:
                best = d
    _MEMO[key] = best
    return best

# ----- 1. n=3 crux grid search, m=3 -----
# region: a1>=a2>=a3>0, a1<2a2, a3>a1/2, sum=1
# equivalently a1 >= a2 >= a3, a2 > a1/2, a3 > a1/2, so a2,a3 in (a1/2, a1]
# and a1+a2+a3=1 => a1 >= 1/3 (else a2>a1/2 => a1+a2+a3 > a1+a1/2+a1/2=2a1 < 1 only if a1<1/2; fine)
# Actually a1<1 obviously. Let's grid (a1, a2), a3=1-a1-a2.

print("="*70)
print("n=3 CRUX GRID m=3 (a1<2a2, a3>a1/2, sum=1)")
print("="*70)
n = 3
_MEMO.clear()
grid = 100
worst_r = 0; worst_cfg=None; worst_d=None; worst_b=None; viol=0
all_ratios = []
for i in range(1, grid):
    a1 = i/grid
    for j in range(1, grid):
        a2 = j/grid
        a3 = 1.0 - a1 - a2
        if a3 <= 1e-9: continue
        c = sorted([a1,a2,a3], reverse=True)
        if not (c[0] < 2*c[1] and c[2] > c[0]/2): continue
        d = min_D_bp(list(c), n)
        M = c[0]; b = M/2**n
        if d > b + 1e-7:
            viol += 1
            if viol <= 5:
                print(f"  VIOL: D*={d:.6f} > M/2^n={b:.6f}, c={[round(x,5) for x in c]}")
        r = d/b if b>1e-12 else 0
        all_ratios.append((r, c, d, b))
        if r > worst_r:
            worst_r = r; worst_cfg=c; worst_d=d; worst_b=b

print(f"n={n} m=3 grid-{grid}: worst ratio={worst_r:.5f}")
print(f"  worst cfg={[round(x,5) for x in worst_cfg]}")
print(f"  D*={worst_d:.6f}  M/2^n={worst_b:.6f}  target 1/D_n={1/15:.6f}")
print(f"  violations={viol}")
print(f"  top 5 worst ratios:")
all_ratios.sort(reverse=True)
for r,c,d,b in all_ratios[:5]:
    print(f"    ratio={r:.5f} cfg={[round(x,5) for x in c]} D*={d:.6f} M/2^n={b:.6f}")
print()

# ----- 2. n=3 crux m=4 random + grid -----
print("="*70)
print("n=3 CRUX m=4 (a1<2a2, a3>a1/2, sum=1, 4 pieces)")
print("="*70)
rng = np.random.default_rng(123)
worst_r4 = 0; worst_cfg4=None; worst_d4=None; worst_b4=None; viol4=0
all4 = []
for _ in range(300):
    for _ in range(50):
        raw = rng.dirichlet([1]*4)
        c = sorted(raw, reverse=True)
        if c[0] < 2*c[1] and c[2] > c[0]/2:
            break
    else:
        continue
    d = min_D_bp(list(c), n)
    M = c[0]; b = M/2**n
    if d > b + 1e-7:
        viol4 += 1
        if viol4 <= 5:
            print(f"  VIOL: D*={d:.6f} > M/2^n={b:.6f}, c={[round(x,5) for x in c]}")
    r = d/b if b>1e-12 else 0
    all4.append((r, c, d, b))
    if r > worst_r4:
        worst_r4 = r; worst_cfg4=c; worst_d4=d; worst_b4=b

print(f"n={n} m=4: worst ratio={worst_r4:.5f}")
print(f"  worst cfg={[round(x,5) for x in worst_cfg4]}")
print(f"  D*={worst_d4:.6f}  M/2^n={worst_b4:.6f}")
print(f"  violations={viol4}")
all4.sort(reverse=True)
print(f"  top 5 worst:")
for r,c,d,b in all4[:5]:
    print(f"    ratio={r:.5f} cfg={[round(x,5) for x in c]} D*={d:.6f} M/2^n={b:.6f}")
print()

# ----- 3. Tower comparison -----
print("="*70)
print("n=3 TOWER (sanity)")
print("="*70)
T3 = [8/15, 4/15, 2/15, 1/15]
_MEMO.clear()
dt = min_D_bp(list(T3), 3)
print(f"T_3: D*={dt:.6f} M/2^n={max(T3)/8:.6f} target={1/15:.6f} ratio={dt/(max(T3)/8):.6f}")
