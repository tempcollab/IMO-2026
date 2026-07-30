"""
Trace Xiang's optimal play and test the 'dyadic ratio 2:1 forces cascade' hypothesis.
Mechanism hypothesis (round 2): ratio b_k/b_{k+1}=2 (dyadic) forces the pairing
cascade to propagate fully, leaving residual 1/D_n; any deviation lets Xiang
terminate early, smaller residual.

We trace the optimal strategy tree and measure, for configs at n=3:
  - the consecutive ratios r_k = a_k/a_{k+1}
  - D* (min Xiang D)
  - how close ratios are to 2 vs D*
"""
import numpy as np
from fractions import Fraction as F
from xiang_optimizer import min_D, D_of, candidate_splits

def trace_optimal(config, k, depth=0, prefix=""):
    """Return (best_D, best_sequence) of split moves."""
    best_d = D_of(config)
    best_seq = []
    if k == 0:
        return best_d, best_seq
    for i in range(len(config)):
        piece = config[i]
        rest = config[:i] + config[i+1:]
        for (q, r) in candidate_splits(piece, config, 6):
            new = rest + [q, r]
            d, seq = trace_optimal(new, k-1, depth+1, prefix+f"[{piece:.4f}->{q:.4f}+{r:.4f}]")
            if d < best_d - 1e-12:
                best_d = d
                best_seq = [(i, piece, q, r)] + seq
    return best_d, best_seq

n = 3
configs = {
    "tower T_3 (8,4,2,1)/15":    [8/15, 4/15, 2/15, 1/15],
    "more-spread (0.6,.25,.1,.05)": [0.6, 0.25, 0.1, 0.05],
    "ratios all=2 except top (0.533,.267,.1,.0)": None,  # skip
    "exact-double-shifted (9,3,2,1)/15": [9/15,3/15,2/15,1/15],
    "(0.55,0.275,0.1,0.075) ratios~2,2,1.33": [0.55,0.275,0.1,0.075],
    "(8,4,1.5,1.5)/15 ratios 2,2.67,1": [8/15,4/15,1.5/15,1.5/15],
    "(8,5,1.5,0.5)/15": [8/15,5/15,1.5/15,0.5/15],
    "(7,5,2,1)/15": [7/15,5/15,2/15,1/15],
    "(8,4,2.5,0.5)/15": [8/15,4/15,2.5/15,0.5/15],
}

print(f"n={n}, target 1/D_n = {1/15:.6f}\n")
for name, cfg in configs.items():
    if cfg is None: continue
    ratios = [cfg[i]/cfg[i+1] for i in range(len(cfg)-1)]
    d, seq = trace_optimal(cfg, n)
    print(f"{name}")
    print(f"  pieces: {[round(x,4) for x in cfg]}")
    print(f"  ratios: {[round(r,3) for r in ratios]}")
    print(f"  D* = {d:.6f}  ({d/(1/15):.3f} x target)")
    print(f"  optimal splits: ", end="")
    for (i, piece, q, r) in seq:
        print(f"piece[{i}]={piece:.4f} -> {q:.4f}+{r:.4f}", end="  ")
    print()
    # show resulting multiset
    final = list(cfg)
    for (i, piece, q, r) in seq:
        # apply to current final (find piece)
        idx = final.index(piece)
        final = final[:idx] + final[idx+1:] + [q, r]
    sf = sorted(final, reverse=True)
    print(f"  final sorted: {[round(x,4) for x in sf]}")
    print(f"  D(final) = {D_of(sf):.6f}")
    print()
