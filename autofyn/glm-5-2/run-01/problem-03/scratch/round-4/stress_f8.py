"""
Stress-test the candidate f8 = M_2 / 2^{n-1} (second-largest piece bound).
Also test f1=(M+M2)/2^n and f12=(2M-M2)/2^n which were also clean.
Check n=3,4 and the known Max-bound violators.
"""
import numpy as np
from fractions import Fraction as F

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits_f(piece, all_pieces):
    cs = {piece / 2.0}
    for p in all_pieces:
        if 0 < p < piece: cs.add(p); cs.add(piece-p)
    return [(q, piece-q) for q in cs if 0 < q < piece]

_MEMO = {}
def min_D_bp_f(config, k):
    key = (tuple(sorted(round(x,12) for x in sorted(config, reverse=True))), k)
    if key in _MEMO: return _MEMO[key]
    best = D_of(config)
    if k == 0: _MEMO[key]=best; return best
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece=cs[i]; rest=cs[:i]+cs[i+1:]
        for (q,r) in bp_splits_f(piece, cs):
            d = min_D_bp_f(rest+[q,r], k-1)
            if d < best: best = d
    _MEMO[key]=best; return best

def stress(n, n_trials, seed, bound_fn, name):
    rng = np.random.default_rng(seed)
    worst_r = 0; worst_cfg=None; viol=0
    for _ in range(n_trials):
        m = rng.integers(2, n+2)
        raw = rng.dirichlet([1]*m)
        cfg = sorted(raw, reverse=True)
        d = min_D_bp_f(list(cfg), n)
        M = max(cfg); M2 = sorted(cfg,reverse=True)[1] if len(cfg)>=2 else 0
        a3 = sorted(cfg,reverse=True)[2] if len(cfg)>=3 else 0
        b = bound_fn(M, M2, a3, n)
        if b <= 1e-15: continue
        if d > b + 1e-7:
            viol += 1
            if viol <= 5:
                print(f"  {name} VIOL n={n}: D*={d:.6f} > {name}={b:.6f}, cfg={[round(x,5) for x in cfg]}")
        r = d/b if b>1e-12 else 0
        if r > worst_r:
            worst_r = r; worst_cfg = cfg
    # tower
    tow = [2**k for k in range(n+1)][::-1]; s=sum(tow); tow=[x/s for x in tow]
    d = min_D_bp_f(list(tow), n)
    M, M2, a3 = max(tow), sorted(tow,reverse=True)[1], sorted(tow,reverse=True)[2]
    bt = bound_fn(M, M2, a3, n)
    print(f"  {name} n={n}: {n_trials} trials, viol={viol}, worst_ratio={worst_r:.5f}, "
          f"tower ratio={d/bt:.5f} (tower {name}={bt:.6f} target={1/(2**(n+1)-1):.6f})")
    if worst_cfg:
        print(f"    worst cfg={[round(x,5) for x in worst_cfg]}")
    return viol, worst_r

# crux-focused stress
def stress_crux(n, n_trials, seed, bound_fn, name):
    rng = np.random.default_rng(seed)
    worst_r = 0; worst_cfg=None; viol=0
    for _ in range(n_trials):
        for _ in range(40):
            m = rng.integers(3, n+2)
            raw = rng.dirichlet([1]*m)
            cfg = sorted(raw, reverse=True)
            if len(cfg)>=3 and cfg[0] < 2*cfg[1] and cfg[2] > cfg[0]/2:
                break
        else: continue
        d = min_D_bp_f(list(cfg), n)
        M = max(cfg); M2 = sorted(cfg,reverse=True)[1]; a3 = sorted(cfg,reverse=True)[2]
        b = bound_fn(M, M2, a3, n)
        if b <= 1e-15: continue
        if d > b + 1e-7:
            viol += 1
            if viol <= 5:
                print(f"  {name} CRUX VIOL n={n}: D*={d:.6f} > {name}={b:.6f}, cfg={[round(x,5) for x in cfg]}")
        r = d/b if b>1e-12 else 0
        if r > worst_r:
            worst_r = r; worst_cfg = cfg
    print(f"  {name} n={n} CRUX: {n_trials} trials, viol={viol}, worst_ratio={worst_r:.5f}")
    if worst_cfg:
        print(f"    worst crux cfg={[round(x,5) for x in worst_cfg]}")
    return viol, worst_r

def f8(M, M2, a3, n): return M2 / 2**(n-1) if n>=1 else M2
def f1(M, M2, a3, n): return (M + M2) / 2**n
def f12(M, M2, a3, n): return (2*M - M2) / 2**n
def f10(M, M2, a3, n): return max(M/2**n, M-M2)

# known Max-bound violators
print("=== Known Max-bound violators ===")
violators = [
    [7/21, 6/21, 5/21, 3/21],
    [22/67, 19/67, 16/67, 10/67],
    [15/45, 13/45, 11/45, 6/45],
]
n = 3
for cfg in violators:
    d = min_D_bp_f(list(cfg), n)
    M, M2, a3 = max(cfg), sorted(cfg,reverse=True)[1], sorted(cfg,reverse=True)[2]
    print(f"  cfg={[round(x,5) for x in cfg]}: D*={d:.6f} | "
          f"M/8={M/8:.6f}({'VIOL' if d>M/8+1e-7 else 'ok'}) "
          f"M2/4={M2/4:.6f}({'VIOL' if d>M2/4+1e-7 else 'ok'}) "
          f"f1={(M+M2)/8:.6f}({'VIOL' if d>(M+M2)/8+1e-7 else 'ok'})")

print()
for n in [3, 4]:
    _MEMO.clear()
    print(f"===== n={n} =====")
    stress(n, 300, 100+n, f8, "f8=M2/2^{n-1}")
    stress(n, 300, 200+n, f1, "f1=(M+M2)/2^n")
    stress(n, 300, 300+n, f12, "f12=(2M-M2)/2^n")
    stress(n, 200, 400+n, f10, "f10=max(M/2^n,M-M2)")
    _MEMO.clear()
    stress_crux(n, 200, 500+n, f8, "f8=M2/2^{n-1}")
    stress_crux(n, 200, 600+n, f1, "f1=(M+M2)/2^n")
    stress_crux(n, 200, 700+n, f12, "f12=(2M-M2)/2^n")
    stress_crux(n, 150, 800+n, f10, "f10=max(M/2^n,M-M2)")
    print()
