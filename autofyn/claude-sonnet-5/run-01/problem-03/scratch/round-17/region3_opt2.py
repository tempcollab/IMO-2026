import numpy as np
from scipy.optimize import differential_evolution

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

def neg_margin(x):
    # want to MAXIMIZE (best - target) i.e. find true violations (best>target)
    t1f,t2f,t3f = x
    Sigma=1.0
    p1 = Sigma - t1f-t2f-t3f
    if not (p1>=t1f>=t2f>=t3f>1e-9):
        return 1000.0
    if not (p1 < Sigma/2): return 1000.0
    if not (t1f < 4/15*Sigma): return 1000.0
    Stail = t1f+t2f+t3f
    if not (t1f < Stail/2): return 1000.0
    vals = strategies(p1,t1f,t2f,t3f)
    best = min(vals)
    target = 8/15*Sigma
    return -(best - target)   # minimize this -> maximize (best-target) -> find true violation if positive at minimum(-(..)) i.e we look for negative of this function

bounds = [(1e-6,0.3),(1e-6,0.3),(1e-6,0.3)]
best_overall = 1e9
best_x=None
for seed in range(30):
    r = differential_evolution(neg_margin, bounds, seed=seed, maxiter=1500, tol=1e-13, popsize=40, polish=True)
    if r.fun < best_overall:
        best_overall = r.fun
        best_x = r.x
print("min of -(best-target) i.e. -margin found:", best_overall, "=> margin(best-target)=", -best_overall)
print("x=",best_x)

print()
print("=== confirm interior (t1 <= 0.95*4/15 Sigma) worst margin, away from boundary ===")
def neg_margin_interior(x):
    t1f,t2f,t3f = x
    Sigma=1.0
    p1 = Sigma - t1f-t2f-t3f
    if not (p1>=t1f>=t2f>=t3f>1e-9):
        return 1000.0
    if not (p1 < Sigma/2): return 1000.0
    if not (t1f < 0.95*4/15*Sigma): return 1000.0
    Stail = t1f+t2f+t3f
    if not (t1f < Stail/2): return 1000.0
    vals = strategies(p1,t1f,t2f,t3f)
    best = min(vals)
    target = 8/15*Sigma
    return -(best - target)

best_overall = 1e9
best_x=None
for seed in range(30):
    r = differential_evolution(neg_margin_interior, bounds, seed=seed, maxiter=1500, tol=1e-13, popsize=40, polish=True)
    if r.fun < best_overall:
        best_overall = r.fun; best_x=r.x
print("interior worst margin:", -best_overall, "x=",best_x)
t1f,t2f,t3f = best_x
p1 = 1-t1f-t2f-t3f
print("p1,t1,t2,t3:", p1,t1f,t2f,t3f)
print("strategies:", strategies(p1,t1f,t2f,t3f))
