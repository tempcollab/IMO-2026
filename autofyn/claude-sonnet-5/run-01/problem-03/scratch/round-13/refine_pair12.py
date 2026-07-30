import numpy as np
from scipy.optimize import minimize, differential_evolution

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

A = [26.0, 21.0, 10.0]

def negval(xs):
    x1,x2 = xs
    if not (0<x1<1 and 0<x2<1): return 1e9
    vals = [A[0], A[1]*x1, A[1]*(1-x1), A[2]*x2, A[2]*(1-x2)]
    return oddrank(vals)

res = differential_evolution(negval, [(0.001,0.999),(0.001,0.999)], tol=1e-14, seed=1, maxiter=2000, popsize=40)
print(res.x, res.fun)

# try many random restarts with Nelder-Mead
best=None
rng=np.random.default_rng(0)
for _ in range(2000):
    x0 = rng.uniform(0.01,0.99,2)
    r = minimize(negval, x0, method='Nelder-Mead', options={'xatol':1e-12,'fatol':1e-12})
    if best is None or r.fun<best[0]:
        best=(r.fun, r.x)
print("best found:", best)
