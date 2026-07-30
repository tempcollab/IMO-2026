import numpy as np
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint
from itertools import product

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

# Witness 1
A1 = [0.4265,0.2536,0.1747,0.1014,0.0438]
# Witness 2
A2 = [0.3415,0.3023,0.1664,0.1404,0.0494]

def build_B(A, cuts_p1, cuts_p3, cuts_p4):
    # cuts_pi: fractions of piece i (list of split points in (0,1), sorted)
    B=[]
    p1,p2,p3,p4,p5 = A
    # p1 split into 2 pieces via cuts_p1 (one cut fraction x in (0,1))
    x = cuts_p1[0]
    B += [p1*x, p1*(1-x)]
    B += [p2]
    y = cuts_p3[0]
    B += [p3*y, p3*(1-y)]
    z1,z2 = cuts_p4  # two cuts on p4 -> 3 pieces, z1<z2 in (0,1)
    B += [p4*z1, p4*(z2-z1), p4*(1-z2)]
    B += [p5]
    return B

def objective(v, A):
    x = v[0]
    y = v[1]
    z1,z2 = v[2], v[3]
    if not (0<x<1 and 0<y<1 and 0<z1<z2<1):
        return 10
    B = build_B(A, [x],[y],[z1,z2])
    return oddrank(B)

from scipy.optimize import differential_evolution

for name,A in [("W1",A1),("W2",A2)]:
    bounds = [(0.001,0.999),(0.001,0.999),(0.001,0.999),(0.001,0.999)]
    def obj(v, A=A):
        x,y,z1,z2=v
        if not (0<z1<z2<1): return 10
        return objective(v,A)
    res = differential_evolution(obj, bounds, args=(), tol=1e-14, maxiter=3000, popsize=40, seed=1, polish=True)
    print(name, res.x, res.fun)

print("---detailed---")
A=A1
x,y,z1,z2 = 0.40650309,0.00464334,0.28402367,0.56804734
B = build_B(A,[x],[y],[z1,z2])
Bs = sorted(B, reverse=True)
for i,b in enumerate(Bs):
    print(i+1, b)
print("sum", sum(Bs))
print("oddrank", oddrank(B))
print("c4 = 16/31 =", 16/31)
