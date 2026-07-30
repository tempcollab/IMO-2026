import numpy as np
from scipy.optimize import minimize
import itertools

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

T = [20.0, 15.0, 12.0, 8.0]  # tail, sum=55
n = len(T)
maxbudget = 3  # m-1 = 3

def compositions_le(total, parts):
    # all tuples of length parts with each >=0 summing to <= total
    if parts == 1:
        for i in range(total+1):
            yield (i,)
        return
    for i in range(total+1):
        for rest in compositions_le(total-i, parts-1):
            yield (i,) + rest

seen = set()
best_overall = None
for comp in compositions_le(maxbudget, n):
    if comp in seen: continue
    seen.add(comp)
    nvars = sum(comp)
    if nvars == 0:
        val = oddrank(T)
        if best_overall is None or val < best_overall[0]:
            best_overall = (val, comp, None)
        continue
    def negval(xs, comp=comp):
        vals = []
        idx = 0
        for i, c in enumerate(comp):
            if c == 0:
                vals.append(T[i])
            else:
                bp = xs[idx:idx+c]
                idx += c
                bp = np.sort(np.clip(bp, 1e-7, 1-1e-7))
                prev = 0.0
                parts = []
                for b in bp:
                    parts.append((b-prev)*T[i])
                    prev = b
                parts.append((1-prev)*T[i])
                vals.extend(parts)
        return oddrank(vals)
    best_local = None
    rng = np.random.default_rng(1)
    for _ in range(400):
        x0 = rng.uniform(0.01,0.99, nvars)
        r = minimize(negval, x0, method='Nelder-Mead', options={'xatol':1e-12,'fatol':1e-12,'maxiter':3000})
        if best_local is None or r.fun < best_local[0]:
            best_local = (r.fun, r.x)
    if best_local[0] < 27.6:
        print("comp", comp, "-> best", best_local[0], "x=", best_local[1])
    if best_overall is None or best_local[0] < best_overall[0]:
        best_overall = (best_local[0], comp, best_local[1])

print()
print("TRUE optimum over all <=3-mark strategies:", best_overall[0], "at comp", best_overall[1], best_overall[2])
print("Sigma(T)/2 =", 55/2)
