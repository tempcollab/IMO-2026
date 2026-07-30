import numpy as np
from scipy.optimize import minimize, differential_evolution

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

A2 = [0.3415,0.3023,0.1664,0.1404,0.0494]
# allocation (2,1,0,1,0): p1 -> 3 parts (2 cuts a1<a2), p2 -> 2 parts (cut b), p4 -> 2 parts (cut c)
def build_B2(A, a1,a2,b,c):
    p1,p2,p3,p4,p5 = A
    return [p1*a1, p1*(a2-a1), p1*(1-a2), p2*b, p2*(1-b), p3, p4*c, p4*(1-c), p5]

def obj2(v, A):
    a1,a2,b,c = v
    if not (1e-7<a1<a2<1-1e-7 and 1e-7<b<1-1e-7 and 1e-7<c<1-1e-7):
        return 10
    return oddrank(build_B2(A,a1,a2,b,c))

res = differential_evolution(obj2, [(1e-6,1-1e-6)]*4, args=(A2,), tol=1e-16, maxiter=4000,
                              popsize=50, seed=3, polish=True)
res2 = minimize(obj2, res.x, args=(A2,), method='Nelder-Mead',
                 options={'xatol':1e-14,'fatol':1e-16,'maxiter':30000,'maxfev':30000})
best = res2 if res2.fun < res.fun else res
print(best.x, best.fun)
a1,a2,b,c = best.x
B = build_B2(A2,a1,a2,b,c)
Bs = sorted(B, reverse=True)
for i,bb in enumerate(Bs):
    print(" ", i+1, f"{bb:.9f}")
print("c4=16/31=", 16/31)
