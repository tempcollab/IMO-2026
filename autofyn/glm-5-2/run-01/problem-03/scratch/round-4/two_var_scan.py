"""
Search for the correct two-variable bound f(M, M_2, n) >= D* for all configs.
We know:
  - D* <= M/2^n FAILS in crux (e.g. (7,6,5,3)/21).
  - D* = a1-a2 in some crux configs.
  - D* < 1/D_n always (the actual target).
Candidate forms to test on a broad scan (m=3,4,5; n=3,4):
  f1 = (M + M_2) / 2^n
  f2 = (a1 - a2) / 2^{n-2}  (residual-based)
  f3 = max(M, 2*(a1-a2)) / 2^n
  f4 = (M + M_2 + a3) / 2^{n+1}  (top-3 weighted)
  f5 = (a1 - a2) + M_2/2^n  (residual + small term)
  f6 = (2*M - M_2) / 2^{n+1}
  f7 = (M + a3) / 2^n  (max + third)
  f8 = M_2 / 2^{n-1}  (second-largest dominant)
  Also: the 'tower-saturating' bound. At tower T_n: M=2^n/D_n, M_2=2^{n-1}/D_n.
  f must give >= 1/D_n at tower. Check f(tower) >= 1/D_n for each.
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

def check_bound(n, configs, fname, f):
    """Check f(cfg) >= D* for all configs. Return (violations, worst_ratio)."""
    worst_r = 0; viol = 0
    for cfg in configs:
        _MEMO.clear()
        d = min_D_bp_f(list(cfg), n)
        M = max(cfg); M2 = sorted(cfg,reverse=True)[1] if len(cfg)>=2 else 0
        a3 = sorted(cfg,reverse=True)[2] if len(cfg)>=3 else 0
        bound = f(M, M2, a3, n, cfg)
        if bound <= 1e-15: continue
        if d > bound + 1e-7:
            viol += 1
            if viol <= 3:
                print(f"    {fname} VIOL n={n}: D*={d:.6f} > f={bound:.6f}, cfg={[round(x,4) for x in cfg]}")
        r = d/bound if bound > 1e-12 else 0
        if r > worst_r: worst_r = r
    return viol, worst_r

# Generate configs: random + crux-focused + tower
def gen_configs(n, n_rand, seed):
    rng = np.random.default_rng(seed)
    cfgs = []
    for _ in range(n_rand):
        m = rng.integers(2, n+2)
        raw = rng.dirichlet([1]*m)
        cfgs.append(sorted(raw, reverse=True))
    # add crux-focused m=4 configs
    for _ in range(n_rand//2):
        for _ in range(30):
            raw = rng.dirichlet([1]*4)
            c = sorted(raw, reverse=True)
            if c[0] < 2*c[1] and c[2] > c[0]/2:
                cfgs.append(c); break
    # tower
    tow = [2**k for k in range(n+1)][::-1]; s=sum(tow)
    cfgs.append([x/s for x in tow])
    # integer-partition configs (small D, up to 30)
    for D in range(n+2, 35):
        for p in range(1, D):
            for q in range(1, min(p, D-p)+1):
                rem = D-p-q
                if rem < 1: break
                if rem >= 2:
                    for r in range(1, min(q, rem)+1):
                        s_ = rem - r
                        if s_ < 1 or s_ > r: continue
                        cfgs.append([p/D, q/D, r/D, s_/D])
                else:
                    cfgs.append([p/D, q/D, rem/D])
    return cfgs

# candidate bounds
def f1(M, M2, a3, n, cfg): return (M + M2) / 2**n
def f2(M, M2, a3, n, cfg): return (M - M2) / 2**(n-2) if n>=2 else (M-M2)
def f3(M, M2, a3, n, cfg): return max(M, 2*(M-M2)) / 2**n
def f4(M, M2, a3, n, cfg): return (M + M2 + a3) / 2**(n+1)
def f5(M, M2, a3, n, cfg): return (M - M2) + M2/2**n
def f6(M, M2, a3, n, cfg): return (2*M - M2) / 2**(n+1)
def f7(M, M2, a3, n, cfg): return (M + a3) / 2**n
def f8(M, M2, a3, n, cfg): return M2 / 2**(n-1) if n>=1 else M2
def f9(M, M2, a3, n, cfg): return (M - M2) + a3/2**n
def f10(M, M2, a3, n, cfg): return max(M/2**n, (M-M2))  # max of max-bound and residual
def f11(M, M2, a3, n, cfg): return max(M/2**n, (M-M2)/2**(n-2)) if n>=2 else (M-M2)
def f12(M, M2, a3, n, cfg): return (M + (M - M2)) / 2**n  # (2M - M2)/2^n... = f6*2

candidates = [
    ("f1=(M+M2)/2^n", f1),
    ("f2=(M-M2)/2^{n-2}", f2),
    ("f3=max(M,2(M-M2))/2^n", f3),
    ("f4=(M+M2+a3)/2^{n+1}", f4),
    ("f5=(M-M2)+M2/2^n", f5),
    ("f6=(2M-M2)/2^{n+1}", f6),
    ("f7=(M+a3)/2^n", f7),
    ("f8=M2/2^{n-1}", f8),
    ("f9=(M-M2)+a3/2^n", f9),
    ("f10=max(M/2^n, M-M2)", f10),
    ("f11=max(M/2^n,(M-M2)/2^{n-2})", f11),
    ("f12=(2M-M2)/2^n", f12),
]

for n in [3]:
    cfgs = gen_configs(n, 300, seed=42+n)
    print(f"\n=== n={n}, {len(cfgs)} configs ===")
    # tower check
    tow = [2**k for k in range(n+1)][::-1]; s=sum(tow); tow=[x/s for x in tow]
    M = max(tow); M2 = sorted(tow,reverse=True)[1]; a3 = sorted(tow,reverse=True)[2]
    print(f"  tower: M={M:.5f} M2={M2:.5f} a3={a3:.5f} target 1/D_n={1/(2**(n+1)-1):.6f}")
    for name, f in candidates:
        ft = f(M, M2, a3, n, tow)
        print(f"    {name}: f(tower)={ft:.6f} {'>=target OK' if ft>=1/(2**(n+1)-1)-1e-9 else '<target FAIL'}")
    print()
    for name, f in candidates:
        v, r = check_bound(n, cfgs, name, f)
        print(f"  {name}: violations={v}, worst_ratio={r:.4f}")
