from fractions import Fraction as F
import numpy as np
from scipy.optimize import differential_evolution

def c_float(k):
    return 2**k/(2**(k+1)-1)

def L2f(u,v):
    u,v = max(u,v), min(u,v)
    sigma=u+v
    if u >= c_float(1)*sigma:
        return u/2+v
    return u

def V3f(a,b,d):
    x1,x2,x3 = sorted([a,b,d], reverse=True)
    sigma=x1+x2+x3
    if sigma<=0: return 0
    if x1 >= c_float(2)*sigma:
        return x1/2+L2f(x2,x3)
    elif x1 >= sigma/2:
        return x1
    else:
        t1,t2=x2,x3
        tailsnip = x1+t2/2
        r = x1-t1
        blockrec = t1 + L2f(r,t2)
        return min(tailsnip,blockrec)

def full_min_f(p1,t1,t2,t3):
    r=p1-t1
    stratA = t1 + V3f(t2,t3,r)
    stratB = p1/2 + V3f(t1,t2,t3)
    tail=[t1,t2,t3]
    best=None
    for i in range(3):
        for j in range(3):
            if i==j: continue
            a,b=tail[i],tail[j]
            if a<b: continue
            others=[tail[k] for k in range(3) if k not in (i,j)]
            tk=others[0]
            rr=a-b
            val=b+V3f(p1,tk,rr)
            if best is None or val<best: best=val
    return min(stratA,stratB,best)

def margin(x):
    # x: 3 free params in (0,1), representing t1,t2,t3 proportions with p1 = 1-sum forced via sorting constraint p1<sum(tail)
    t1,t2,t3 = sorted(x, reverse=True)
    tailsum = t1+t2+t3
    if tailsum<=0: return 1e9
    # p1 must be < tailsum for Case C and p1>=t1 (sorted desc); pick p1 as separate param via scaling
    return None

def neg_margin(params):
    p1,t1,t2,t3 = params
    vals = sorted([p1,t1,t2,t3], reverse=True)
    p1,t1,t2,t3 = vals
    Sigma = p1+t1+t2+t3
    if Sigma<=1e-9: return 1e9
    if not (p1 < t1+t2+t3 - 1e-9):  # must be Case C
        return 1e9  # infeasible penalty (large, but DE minimizes so large is bad -> won't be chosen as worst)
    tgt = c_float(3)*Sigma
    val = full_min_f(p1,t1,t2,t3)
    return val - tgt  # want to MINIMIZE this to find most negative (violation) -- wait we want to find margin<0

bounds = [(0.001,2000)]*4
res = differential_evolution(neg_margin, bounds, seed=42, maxiter=300, popsize=40, tol=1e-12, polish=True)
print("best (most negative) neg_margin found:", res.x, res.fun)
