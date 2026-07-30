import numpy as np
from scipy.optimize import differential_evolution, minimize
from fractions import Fraction
from itertools import product
import sys

def compositions(total, parts):
    # all ways to write total as sum of `parts` nonneg integers
    if parts == 1:
        yield (total,)
        return
    for i in range(total+1):
        for rest in compositions(total-i, parts-1):
            yield (i,) + rest

def split_piece(p, k, x):
    # split p into k+1 positive parts using k+1 raw params x (softplus then normalize)
    w = np.log1p(np.exp(np.clip(x, -30, 30))) + 1e-9  # softplus
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

def best_for_alloc(A, ks, seed=0, popsize=25, maxiter=200, polish_iters=6):
    dims = []
    idx = []
    cur = 0
    for k in ks:
        j = k+1
        idx.append(cur)
        dims.append(j)
        cur += j
    total_dim = cur
    bounds = [(-4,4)]*total_dim
    if total_dim == 0:
        return oddrank(list(A)), None
    res = differential_evolution(objective, bounds, args=(A, ks, idx),
                                  seed=seed, popsize=popsize, maxiter=maxiter,
                                  tol=1e-12, mutation=(0.4,1.5), recombination=0.8,
                                  polish=True, updating='deferred', workers=1)
    best_x = res.x
    best_val = res.fun
    # local polish with Nelder-Mead restarts
    for _ in range(polish_iters):
        r2 = minimize(objective, best_x, args=(A, ks, idx), method='Nelder-Mead',
                      options={'xatol':1e-12,'fatol':1e-14,'maxiter':20000,'maxfev':40000})
        if r2.fun < best_val:
            best_val = r2.fun
            best_x = r2.x
    return best_val, (best_x, idx, ks)

def reconstruct_leaves(A, sol):
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

def search_all_allocations(A, budget, verbose=True):
    m = len(A)
    best_overall = None
    best_alloc = None
    best_sol = None
    for ks in compositions(budget, m):
        val, sol = best_for_alloc(A, ks, seed=hash(ks) % 1000)
        if best_overall is None or val < best_overall - 1e-12:
            best_overall = val
            best_alloc = ks
            best_sol = sol
        if verbose:
            print(f"  alloc={ks} val={val:.8f}")
    return best_overall, best_alloc, best_sol

if __name__ == "__main__":
    # m=5 witness
    A = [1826/7188, 1563/7188, 1520/7188, 1514/7188, 765/7188]
    budget = 4
    print("=== m=5 witness A=(1826,1563,1520,1514,765)/7188, budget=4 ===")
    val, alloc, sol = search_all_allocations(A, budget)
    print("BEST:", val, "alloc:", alloc)
    leaves, origin = reconstruct_leaves(A, sol)
    order = sorted(zip(leaves, origin), key=lambda t: -t[0])
    for r,(v,o) in enumerate(order,1):
        print(f"  rank {r}: value={v:.8f} from piece {o+1} {'ODD' if r%2==1 else 'even'}")
    print("target c(4)=16/31=", 16/31)
