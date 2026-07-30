import itertools, numpy as np
from fractions import Fraction as F
from scipy.optimize import minimize

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def best_response_bruteforce(A, K, grid=200):
    """A: list of piece lengths (floats). K: total extra marks Xiang Yu may use.
    Enumerate all ways to distribute K marks among len(A) pieces (c_i cuts on piece i,
    sum c_i <= K), each piece split into c_i+1 parts. For each allocation, optimize
    the split ratios numerically to minimize oddrank(B). Return best value and the
    allocation/ratios achieving it."""
    m = len(A)
    best = (float('inf'), None, None)
    # enumerate allocations: c_i >=0, sum c_i <= K
    def allocs(m, K):
        if m == 1:
            for c in range(K+1):
                yield (c,)
            return
        for c in range(K+1):
            for rest in allocs(m-1, K-c):
                yield (c,) + rest
    for alloc in allocs(m, K):
        total_cuts = sum(alloc)
        if total_cuts == 0:
            val = oddrank(A)
            if val < best[0]:
                best = (val, alloc, [tuple(A)])
            continue
        # free params: for each piece i with c_i cuts, c_i free ratios in (0,1) determining
        # c_i+1 positive parts summing to A[i]. Use softmax-like parametrization via cumulative
        # sorted uniform variables scaled: parts_i = A[i]*diff(sorted([0,u_1,...,u_ci,1]))
        nparams = total_cuts
        if nparams == 0:
            continue
        def unpack(x):
            parts_all = []
            idx = 0
            for i, ci in enumerate(alloc):
                if ci == 0:
                    parts_all.append([A[i]])
                    continue
                us = x[idx:idx+ci]
                idx += ci
                # map to (0,1) via sigmoid then sort
                us = 1/(1+np.exp(-np.array(us)))
                cuts = sorted(us.tolist())
                bnds = [0.0]+cuts+[1.0]
                parts = [A[i]*(bnds[j+1]-bnds[j]) for j in range(len(bnds)-1)]
                parts_all.append(parts)
            return parts_all

        def objective(x):
            parts_all = unpack(x)
            allvals = [v for p in parts_all for v in p]
            return oddrank(allvals)

        x0 = np.zeros(nparams)
        res = minimize(objective, x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':20000,'maxfev':20000})
        # random restarts
        bestval = res.fun
        bestx = res.x
        rng = np.random.default_rng(0)
        for _ in range(30):
            x0r = rng.normal(0,3,size=nparams)
            r2 = minimize(objective, x0r, method='Nelder-Mead',
                           options={'xatol':1e-10,'fatol':1e-12,'maxiter':20000,'maxfev':20000})
            if r2.fun < bestval:
                bestval, bestx = r2.fun, r2.x
        if bestval < best[0]:
            best = (bestval, alloc, unpack(bestx))
    return best

if __name__ == "__main__":
    witnesses = {
        "third": [1/3,1/3,1/3],
        "hard1": [4649/10000, 3042/10000, 2309/10000],
    }
    for name, A in witnesses.items():
        A = sorted(A, reverse=True)
        val, alloc, parts = best_response_bruteforce(A, 2)
        print(name, A, "-> best oddrank:", val, "alloc:", alloc, "parts:", parts)

def scan_all_allocs(A, K):
    m = len(A)
    def allocs(m, K):
        if m == 1:
            for c in range(K+1):
                yield (c,)
            return
        for c in range(K+1):
            for rest in allocs(m-1, K-c):
                yield (c,) + rest
    results = []
    for alloc in allocs(m, K):
        total_cuts = sum(alloc)
        if total_cuts == 0:
            results.append((oddrank(A), alloc))
            continue
        nparams = total_cuts
        def unpack(x, alloc=alloc):
            parts_all = []
            idx = 0
            for i, ci in enumerate(alloc):
                if ci == 0:
                    parts_all.append([A[i]])
                    continue
                us = x[idx:idx+ci]
                idx += ci
                us = 1/(1+np.exp(-np.array(us)))
                cuts = sorted(us.tolist())
                bnds = [0.0]+cuts+[1.0]
                parts = [A[i]*(bnds[j+1]-bnds[j]) for j in range(len(bnds)-1)]
                parts_all.append(parts)
            return parts_all
        def objective(x, alloc=alloc):
            parts_all = unpack(x, alloc)
            allvals = [v for p in parts_all for v in p]
            return oddrank(allvals)
        rng = np.random.default_rng(42)
        bestval = float('inf')
        for _ in range(60):
            x0r = rng.normal(0,3,size=nparams)
            r2 = minimize(objective, x0r, method='Nelder-Mead',
                           options={'xatol':1e-12,'fatol':1e-14,'maxiter':30000,'maxfev':30000})
            if r2.fun < bestval:
                bestval = r2.fun
        results.append((bestval, alloc))
    results.sort()
    return results

A = sorted([4649/10000, 3042/10000, 2309/10000], reverse=True)
res = scan_all_allocs(A, 2)
for v, a in res:
    print(a, v)
