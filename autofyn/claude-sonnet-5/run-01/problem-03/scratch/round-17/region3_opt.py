import numpy as np
from scipy.optimize import differential_evolution
from fractions import Fraction as F

def L2f(u,v):
    M,m=(u,v) if u>=v else (v,u)
    return M if M<=2*m else M/2+m

def V3f(x,y,z):
    trip=sorted([x,y,z],reverse=True)
    x,y,z=trip
    sigma=x+y+z
    if sigma<=0: return 0
    if x>=4/7*sigma:
        return x/2+L2f(y,z)
    elif sigma/2<=x:
        return x
    else:
        return min(x+z/2, y+L2f(x-y,z))

def strategies(p1,t1,t2,t3):
    A = t1+V3f(*sorted([t2,t3,p1-t1],reverse=True))
    B = p1/2+V3f(t1,t2,t3)
    C12 = t2+V3f(*sorted([p1,t3,t1-t2],reverse=True))
    C13 = t3+V3f(*sorted([p1,t2,t1-t3],reverse=True))
    C23 = t3+V3f(*sorted([p1,t1,t2-t3],reverse=True))
    return A,B,C12,C13,C23

def region3_violation(x):
    # x = [t1,t2,t3,p1] with constraint p1>=t1>=t2>=t3>0, normalize Sigma=1 via p1=1-t1-t2-t3 forced externally
    t1f,t2f,t3f = x
    Sigma=1.0
    p1 = Sigma - t1f-t2f-t3f
    if not (p1>=t1f>=t2f>=t3f>1e-9):
        return 1000.0  # infeasible penalty
    if not (p1 < Sigma/2): return 1000.0
    if not (t1f < 4/15*Sigma): return 1000.0
    Stail = t1f+t2f+t3f
    if not (t1f < Stail/2): return 1000.0
    vals = strategies(p1,t1f,t2f,t3f)
    best = min(vals)
    target = 8/15*Sigma
    return best - target  # want >=0 always; minimize this -> find most negative

bounds = [(1e-6,0.3),(1e-6,0.3),(1e-6,0.3)]
result = differential_evolution(region3_violation, bounds, seed=42, maxiter=2000, tol=1e-14, popsize=40, polish=True)
print(result.x, result.fun)

# multiple restarts
best_overall = 0
best_x = None
for seed in range(20):
    r = differential_evolution(region3_violation, bounds, seed=seed, maxiter=1000, tol=1e-12, popsize=30)
    if r.fun < best_overall:
        best_overall = r.fun
        best_x = r.x
print("best overall margin (most negative found):", best_overall, best_x)
