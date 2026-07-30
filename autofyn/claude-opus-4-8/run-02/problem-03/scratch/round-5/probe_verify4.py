import numpy as np
from scipy.optimize import minimize

def altsum(vals):
    s=sorted(vals, reverse=True)
    tot=0.0; sign=1
    for v in s:
        tot+=sign*v; sign=-sign
    return tot

def maxc_of(Y,Z):
    merged = sorted([(w,1) for w in Y]+[(w,-1) for w in Z], key=lambda x:-x[0])
    c=0; mx=0
    for w,s in merged:
        c+=s; mx=max(mx,c)
    return mx

# n=4, a=1: Y=(8,8), Z = response to dyadic {1,2,4,8} with budget b<=3 (a+b<=n=4)
n=4
Y=[8.0,8.0]
def softmax_split(x,total):
    e=np.exp(x-np.max(x)); w=e/e.sum(); return w*total

def build_Z(params, cutcounts):
    Z=[]; p=0
    for j,piece in enumerate([1,2,4,8]):
        k=cutcounts[j]
        if k==0: Z.append(float(piece))
        else:
            frags=softmax_split(params[p:p+k+1], piece); p+=k+1
            Z.extend(frags)
    return Z

trials_summary=[]
for cutcounts in [[0,0,0,3],[1,1,1,0],[3,0,0,0],[0,0,3,0],[1,0,2,0],[0,2,1,0]]:
    if sum(cutcounts)>3: continue
    nz = sum((k+1 if k>0 else 0) for k in cutcounts)
    if nz==0: continue
    def obj(x):
        Z=build_Z(x,cutcounts)
        return altsum(Y+Z)
    best=None
    rng=np.random.default_rng(1)
    for t in range(60):
        x0=rng.normal(size=nz)
        res=minimize(obj,x0,method='Nelder-Mead',options={'maxiter':4000,'xatol':1e-10,'fatol':1e-12})
        if best is None or res.fun<best[0]:
            best=(res.fun,x0copy:=res.x.copy())
    Z=build_Z(best[1],cutcounts)
    mc=maxc_of(Y,Z)
    print("cutcounts",cutcounts,"min D=",best[0],"maxc=",mc)
