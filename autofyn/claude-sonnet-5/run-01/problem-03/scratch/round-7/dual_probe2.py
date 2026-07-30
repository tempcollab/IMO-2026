import numpy as np
from scipy.optimize import minimize, differential_evolution

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

A1 = [0.4265,0.2536,0.1747,0.1014,0.0438]
A2 = [0.3415,0.3023,0.1664,0.1404,0.0494]

def build_B(A, x, y, z1, z2):
    p1,p2,p3,p4,p5 = A
    return [p1*x, p1*(1-x), p2, p3*y, p3*(1-y), p4*z1, p4*(z2-z1), p4*(1-z2), p5]

def obj(v, A):
    x,y,z1,z2 = v
    if not (1e-6<x<1-1e-6 and 1e-6<y<1-1e-6 and 1e-6<z1<z2<1-1e-6):
        return 10
    return oddrank(build_B(A,x,y,z1,z2))

for name,A in [("W1",A1),("W2",A2)]:
    best=None
    for seed in range(10):
        res = differential_evolution(obj, [(1e-5,1-1e-5)]*4, args=(A,), tol=1e-16, maxiter=5000,
                                      popsize=60, seed=seed, polish=True, mutation=(0.3,1.7), recombination=0.9)
        # polish further with Nelder-Mead
        res2 = minimize(obj, res.x, args=(A,), method='Nelder-Mead',
                         options={'xatol':1e-14,'fatol':1e-16,'maxiter':20000,'maxfev':20000})
        cand = res2 if res2.fun<res.fun else res
        if best is None or cand.fun<best.fun:
            best=cand
    print(name, best.x, best.fun)
    x,y,z1,z2 = best.x
    B = build_B(A,x,y,z1,z2)
    Bs = sorted(B, reverse=True)
    for i,b in enumerate(Bs):
        print(" ", i+1, f"{b:.8f}")
