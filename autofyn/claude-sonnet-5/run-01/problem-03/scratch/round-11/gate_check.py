import numpy as np
from scipy.optimize import differential_evolution, minimize
from fractions import Fraction

def split_piece(p, k, x):
    w = np.log1p(np.exp(np.clip(x, -30, 30))) + 1e-9
    w = w / w.sum()
    return w * p

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

def objective(x, A, ks, splits_idx):
    leaves = []
    for i, p in enumerate(A):
        k = ks[i]
        j = k+1
        xi = x[splits_idx[i]:splits_idx[i]+j]
        leaves.extend(split_piece(p, k, xi))
    return oddrank(leaves)

def best_for_alloc(A, ks, seed=0, popsize=40, maxiter=400, polish_iters=10):
    dims = []
    idx = []
    cur = 0
    for k in ks:
        j = k+1
        idx.append(cur)
        dims.append(j)
        cur += j
    total_dim = cur
    bounds = [(-6,6)]*total_dim
    res = differential_evolution(objective, bounds, args=(A, ks, idx),
                                  seed=seed, popsize=popsize, maxiter=maxiter,
                                  tol=1e-14, mutation=(0.4,1.5), recombination=0.9,
                                  polish=True, updating='deferred', workers=1)
    best_x = res.x
    best_val = res.fun
    for _ in range(polish_iters):
        r2 = minimize(objective, best_x, args=(A, ks, idx), method='Nelder-Mead',
                      options={'xatol':1e-14,'fatol':1e-16,'maxiter':40000,'maxfev':80000})
        if r2.fun < best_val:
            best_val = r2.fun
            best_x = r2.x
    return best_val, (best_x, idx, ks)

def reconstruct(A, sol):
    best_x, idx, ks = sol
    leaves = []
    origin = []
    for i, p in enumerate(A):
        k = ks[i]
        j = k+1
        xi = best_x[idx[i]:idx[i]+j]
        parts = split_piece(p, k, xi)
        leaves.extend(parts)
        origin.extend([i]*j)
    return leaves, origin

A = [1826/7188, 1563/7188, 1520/7188, 1514/7188, 765/7188]
budget = 4

# allocations that tied at ~0.50041736 in the earlier scan
tied_allocs = [(1,0,0,0,3),(1,0,0,1,2),(1,0,1,0,2),(1,1,0,0,2),(1,1,1,0,1),
               (1,2,0,0,1),(1,2,0,1,0),(1,2,1,0,0),(1,3,0,0,0),
               (2,0,0,0,2),(2,0,0,1,1),(2,0,1,0,1),(2,1,0,0,1),(2,1,1,0,0),
               (2,2,0,0,0),(3,0,0,0,1),(3,1,0,0,0)]

for ks in tied_allocs:
    val, sol = best_for_alloc(A, ks, seed=42)
    leaves, origin = reconstruct(A, sol)
    order = sorted(zip(leaves,origin), key=lambda t:-t[0])
    rounded = [round(v*7188,3) for v,o in order]
    print(ks, "val=%.10f"%val, rounded)
