import numpy as np
from scipy.optimize import minimize
import itertools

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

T = [20.0, 15.0, 12.0, 8.0]  # tail, sum=55
n = len(T)
budget = 3  # m-1 = 3

# enumerate all ways to distribute `budget` cuts among n pieces (0..budget each, sum=budget)
def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for i in range(total+1):
        for rest in compositions(total-i, parts-1):
            yield (i,) + rest

best_overall = None
for comp in compositions(budget, n):
    # comp[i] = number of cuts on piece i -> comp[i]+1 parts
    nvars = sum(comp)  # each cut on a piece with c cuts needs c "free ratio" params (using cumulative sorted breakpoints)
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
                # c breakpoints in (0,1), sorted, giving c+1 parts
                bp = xs[idx:idx+c]
                idx += c
                bp = np.sort(np.clip(bp, 1e-6, 1-1e-6))
                prev = 0.0
                parts = []
                for b in bp:
                    parts.append((b-prev)*T[i])
                    prev = b
                parts.append((1-prev)*T[i])
                vals.extend(parts)
        return oddrank(vals)
    best_local = None
    rng = np.random.default_rng(42)
    for _ in range(300):
        x0 = rng.uniform(0.01,0.99, nvars)
        r = minimize(negval, x0, method='Nelder-Mead', options={'xatol':1e-11,'fatol':1e-11,'maxiter':2000})
        if best_local is None or r.fun < best_local[0]:
            best_local = (r.fun, r.x)
    print("comp", comp, "-> best", best_local[0])
    if best_overall is None or best_local[0] < best_overall[0]:
        best_overall = (best_local[0], comp, best_local[1])

print()
print("TRUE optimum over all <=3-mark strategies:", best_overall[0], "at comp", best_overall[1])
print("Sigma(T)/2 =", 55/2)
print("claimed solve2(T,3) = 7/25*55 =", 7/25*55, " (in original scaled units, since T sums to 55 here vs 0.55 normalized)")
