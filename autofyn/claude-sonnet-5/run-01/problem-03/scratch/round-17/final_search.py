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

def obj(x):
    t1f,t2f,t3f = x
    Sigma=1.0
    p1 = Sigma - t1f-t2f-t3f
    if not (p1>=t1f>=t2f>=t3f>1e-9): return 1000.0
    if not (p1 < Sigma/2): return 1000.0
    if not (t1f < 4/15*Sigma): return 1000.0
    Stail=t1f+t2f+t3f
    if not (t1f < Stail/2): return 1000.0
    A,B,C12,C13,C23 = strategies(p1,t1f,t2f,t3f)
    best=min(A,B,C12,C13,C23)
    target=8/15*Sigma
    return -(best-target)   # minimize -> most negative means best<<target(safe); we want MAX(best-target) i.e. look for positive at true violation -> so track max separately

bounds=[(1e-7,0.3),(1e-7,0.3),(1e-7,0.3)]
# We instead directly search for MAX(best-target); use objective = -(best-target) and minimize; report -fun as max(best-target)
worst_margin_found = -1e9
worst_x=None
for seed in range(60):
    r=differential_evolution(obj,bounds,seed=seed,maxiter=2000,popsize=50,tol=1e-14,polish=True)
    val = -r.fun  # = best-target
    if val > worst_margin_found:
        worst_margin_found = val
        worst_x = r.x
print("max(best-target) found over 60 restarts (positive would be violation):", worst_margin_found)
print("at x=",worst_x)
