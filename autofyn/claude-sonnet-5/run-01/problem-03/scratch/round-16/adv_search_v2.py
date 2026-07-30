import numpy as np
from scipy.optimize import differential_evolution
from fractions import Fraction as F

def c_float(k):
    return 2**k/(2**(k+1)-1)

def L2f(u,v):
    if u>=2*v:
        return u/2+v
    return u

def V3f(x1,x2,x3):
    xs=sorted([x1,x2,x3],reverse=True)
    x1,x2,x3=xs
    sigma=x1+x2+x3
    if sigma<=0: return 0
    if x1>=c_float(2)*sigma:
        return x1/2+L2f(x2,x3)
    elif x1>=sigma/2:
        return x1
    else:
        tail_snip=x1+x3/2
        r=x1-x2
        a,b=sorted([r,x3],reverse=True)
        block=x2+L2f(a,b)
        return min(tail_snip,block)

def V4_min(p1,t1,t2,t3):
    tail=[t1,t2,t3]
    r=p1-t1
    stratA=t1+V3f(t2,t3,r)
    stratB=p1/2+V3f(t1,t2,t3)
    vals=[stratA,stratB]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        a,b=tail[i],tail[j]
        hi,lo=max(a,b),min(a,b)
        k_idx=[x for x in range(3) if x!=i and x!=j][0]
        tk=tail[k_idx]
        r2=hi-lo
        val=lo+V3f(p1,tk,r2)
        vals.append(val)
    return min(vals)

def objective(x):
    # x in R^3 unconstrained -> map to sorted simplex t3<=t2<=t1<=p1, all positive, sum=1
    # use sigmoid-based fractions
    import math
    s = [1/(1+math.exp(-xx)) for xx in x]  # in (0,1)
    # cumulative construction: p1 = s0, t1 = s0*s1, t2=t1*s2*..., simpler: build decreasing sequence
    a,b,cc = s
    p1 = 1.0
    t1 = p1*a
    t2 = t1*b
    t3 = t2*cc
    Sigma = p1+t1+t2+t3
    # need Case C: p1 < Sigma/2  i.e. p1 < t1+t2+t3
    if p1 >= t1+t2+t3:
        return 1000.0  # infeasible penalty pushed away, not Case C
    target = c_float(3)*Sigma
    m = V4_min(p1,t1,t2,t3)
    return target - m  # want to minimize this; negative = violation

best = None
for seed in [1,2,3,4,5]:
    res = differential_evolution(objective, bounds=[(-8,8)]*3, seed=seed, popsize=60, maxiter=300, tol=1e-12, polish=True)
    print("seed",seed,"fun=",res.fun,"x=",res.x)
    if best is None or res.fun<best.fun:
        best=res

print("BEST margin found:", best.fun)
print("BEST x:", best.x)

print("\n--- second independent search: direct simplex parametrization ---")
from scipy.optimize import differential_evolution as de2
def objective2(x):
    # x = 3 values in (0,1) representing t1/p1, t2/t1, t3/t2 directly (not sigmoid)
    a,b,cc = x
    if not (0<a<1 and 0<b<1 and 0<cc<1):
        return 1000.0
    p1=1.0
    t1=p1*a
    t2=t1*b
    t3=t2*cc
    Sigma=p1+t1+t2+t3
    if p1>=t1+t2+t3:
        return 1000.0
    target=c_float(3)*Sigma
    m=V4_min(p1,t1,t2,t3)
    return target-m

best2=None
for seed in [11,22,33,44]:
    res=de2(objective2, bounds=[(0.001,0.999)]*3, seed=seed, popsize=80, maxiter=400, tol=1e-14)
    print("seed",seed,"fun=",res.fun,"x=",res.x)
    if best2 is None or res.fun<best2.fun:
        best2=res
print("BEST2:", best2.fun, best2.x)
