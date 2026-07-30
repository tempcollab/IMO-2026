import numpy as np
from scipy.optimize import minimize
import itertools, random

# n=2: Liu partition p=(p1,p2,p3) sorted desc, sum=1, Xiang picks cuts on pieces (<=2 total cuts)
# We'll brute force min D over discretized cut allocations using nested optimization,
# reusing simple model: Xiang can do up to 2 single-cuts total across the 3 pieces.
# For each piece cut at position x in (0,len), it splits into x, len-x.
# We enumerate cut-count allocation (a1,a2,a3) with sum<=2, ai in {0,1,2} bisect multiple times not needed (with n=2, max 2 cuts total).
# For simplicity here allow at most 1 cut per piece (since with only 2 cuts, putting 2 cuts on same piece means 3 pieces there).
import random

def D(vals):
    vals=sorted(vals, reverse=True)
    s=0
    sign=1
    for v in vals:
        s+=sign*v
        sign*=-1
    return s

def min_D_given_alloc(p, alloc, restarts=40):
    # alloc: tuple of cuts per piece index (0,1,2 max cuts total across pieces), each piece gets 0 or 1 cut (with n=2 budget, 
    # allow one piece 2 cuts -> creates 3 subpieces)
    idxs=[i for i in range(3) if alloc[i]>0]
    if not idxs:
        return D(p)
    best=1e9
    dim=sum(alloc)
    for _ in range(restarts):
        x0=np.random.rand(dim)
        def obj(x):
            vals=[]
            xi=0
            for i in range(3):
                if alloc[i]==0:
                    vals.append(p[i])
                elif alloc[i]==1:
                    t=np.clip(x[xi],1e-6,1-1e-6); xi+=1
                    vals.append(p[i]*t); vals.append(p[i]*(1-t))
                elif alloc[i]==2:
                    t1=np.clip(x[xi],1e-6,1-1e-6); t2=np.clip(x[xi+1],1e-6,1-1e-6); xi+=2
                    cuts=sorted([t1*t2,ambiguous:=0])
            return D(vals)
        res=minimize(obj, x0, method='Nelder-Mead')
        if res.fun<best: best=res.fun
    return best

def minD(p):
    best=1e9
    for alloc in itertools.product([0,1],repeat=3):
        if sum(alloc)<=2:
            v=min_D_given_alloc(p,alloc, restarts=25)
            if v<best: best=v
    # also allocation with 2 cuts on one piece
    for i in range(3):
        alloc=[0,0,0]; alloc[i]=2
        v=min_D_given_alloc(p,alloc, restarts=25)
        if v<best: best=v
    return best

random.seed(1)
p1=[0.5,0.3,0.2]
p2=[0.6,0.25,0.15]
mid=[(a+b)/2 for a,b in zip(p1,p2)]
f1=minD(p1); f2=minD(p2); fm=minD(mid)
print("f(p1)=",f1,"f(p2)=",f2,"f(mid)=",fm,"avg=",(f1+f2)/2)
print("quadratic-weighted D check (sum sign*v^2):")
def D2(vals):
    vals=sorted(vals,reverse=True)
    s=0;sign=1
    for v in vals:
        s+=sign*v*v; sign*=-1
    return s
print(D2(p1),D2(p2),D2(mid))
