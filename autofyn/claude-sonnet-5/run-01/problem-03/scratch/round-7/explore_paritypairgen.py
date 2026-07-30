import itertools, random
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize

def geom_config(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p_1..p_{n+1}

def c_of(n):
    D = 2**(n+1) - 1
    return F(2**n, D)

def oddsum_from_sorted(vals_sorted_desc):
    return sum(vals_sorted_desc[0::2])

def oddsum(values):
    vs = sorted(values, reverse=True)
    return oddsum_from_sorted(vs)

# ---------- Continuous optimizer for a fixed allocation vector a=(a_1,...,a_{n+1}) ----------
# piece i (value p_i, float) is split into a_i+1 positive parts via softmax params.
def build_values(theta_flat, group_sizes, group_sums):
    vals = []
    idx = 0
    for r, s in zip(group_sizes, group_sums):
        th = theta_flat[idx:idx+r]
        idx += r
        e = np.exp(th - np.max(th))
        w = e / e.sum()
        vals.extend(list(w * s))
    return vals

def neg_objective(theta_flat, group_sizes, group_sums):
    vals = build_values(theta_flat, group_sizes, group_sums)
    vs = sorted(vals, reverse=True)
    return sum(vs[0::2])  # we MINIMIZE this (Xiang Yu wants to minimize Liu's oddsum)

def optimize_allocation(p_floats, alloc, restarts=25, seed=0):
    group_sizes = [a+1 for a in alloc]
    group_sums = p_floats
    ntot = sum(group_sizes)
    rng = np.random.default_rng(seed)
    best = None
    best_theta = None
    for trial in range(restarts):
        theta0 = rng.normal(scale=2.0, size=ntot)
        res = minimize(neg_objective, theta0, args=(group_sizes, group_sums),
                        method='Nelder-Mead',
                        options={'maxiter': 1200, 'xatol':1e-9, 'fatol':1e-11})
        if best is None or res.fun < best:
            best = res.fun
            best_theta = res.x
    vals = build_values(best_theta, group_sizes, group_sums)
    return best, sorted(vals, reverse=True)

def all_allocations(n):
    # a_1,...,a_{n+1} >=0 sum = n  (use full budget; using less is dominated)
    def rec(remaining, slots):
        if slots == 1:
            yield (remaining,)
            return
        for v in range(remaining+1):
            for rest in rec(remaining-v, slots-1):
                yield (v,) + rest
    yield from rec(n, n+1)

def scan(n, restarts=20):
    p = geom_config(n)
    p_floats = [float(x) for x in p]
    c = float(c_of(n))
    print(f"\n=== n={n}, c(n)={c_of(n)} ~ {c:.6f} ===")
    results = []
    for alloc in all_allocations(n):
        val, vs = optimize_allocation(p_floats, alloc, restarts=restarts)
        results.append((val, alloc, vs))
    results.sort(key=lambda t: t[0])
    print("Top 8 worst-for-Liu allocations (lowest oddsum found):")
    for val, alloc, vs in results[:8]:
        k = alloc[0]
        tailmarks = alloc[1:]
        print(f"  oddsum={val:.6f} (c(n)={c:.6f}, diff={val-c:+.2e})  k={k} tail_alloc={tailmarks}")
        print(f"    sorted vals: {[round(v,5) for v in vs]}")
    return results

if __name__ == "__main__":
    import sys
    ns = [int(x) for x in sys.argv[1:]] or [2,3]
    for n in ns:
        scan(n, restarts=8)
