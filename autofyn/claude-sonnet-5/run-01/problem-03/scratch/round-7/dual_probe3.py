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
    if not (1e-7<x<1-1e-7 and 1e-7<y<1-1e-7 and 1e-7<z1<z2<1-1e-7):
        return 10
    return oddrank(build_B(A,x,y,z1,z2))

for name,A,x0 in [("W1",A1,[0.40650309,0.00464334,0.28402367,0.56804734]),
                   ("W2",A2,[0.1426102,0.5,0.5,0.5])]:
    res = minimize(obj, x0, args=(A,), method='Nelder-Mead',
                    options={'xatol':1e-13,'fatol':1e-15,'maxiter':30000,'maxfev':30000})
    print(name, res.x, res.fun)
    x,y,z1,z2 = res.x
    B = build_B(A,x,y,z1,z2)
    Bs = sorted(B, reverse=True)
    for i,b in enumerate(Bs):
        print(" ", i+1, f"{b:.9f}")
