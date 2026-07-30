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
    A,B,C12,C13,C23 = strategies(p1,t1f,t2f,t3f)
    return C12 - min(A,B,C13,C23)  # want to find negative (C12 strictly best) -> minimize

bounds = [(1e-6,0.49),(1e-6,0.49),(1e-6,0.49)]
best=1e9;bx=None
for seed in range(20):
    r=differential_evolution(obj,bounds,seed=seed,maxiter=1000,popsize=30,tol=1e-12)
    if r.fun<best: best=r.fun;bx=r.x
print("min(C12 - min(others)) over full Case C domain:", best, bx)

def obj13(x):
    t1f,t2f,t3f = x
    Sigma=1.0
    p1 = Sigma - t1f-t2f-t3f
    if not (p1>=t1f>=t2f>=t3f>1e-9): return 1000.0
    if not (p1 < Sigma/2): return 1000.0
    A,B,C12,C13,C23 = strategies(p1,t1f,t2f,t3f)
    return C13 - min(A,B,C12,C23)

best=1e9;bx=None
for seed in range(20):
    r=differential_evolution(obj13,bounds,seed=seed,maxiter=1000,popsize=30,tol=1e-12)
    if r.fun<best: best=r.fun;bx=r.x
print("min(C13 - min(others)) over full Case C domain:", best, bx)

print()
t1f,t2f,t3f = 0.294118059,0.235293647,0.000001
Sigma=1.0
p1=Sigma-t1f-t2f-t3f
print("p1,t1,t2,t3:",p1,t1f,t2f,t3f)
print("Case C p1<0.5:", p1<0.5)
print("t1<4/15:", t1f<4/15)
A,B,C12,C13,C23=strategies(p1,t1f,t2f,t3f)
print("A,B,C12,C13,C23:",A,B,C12,C13,C23)
print("target:", 8/15)
