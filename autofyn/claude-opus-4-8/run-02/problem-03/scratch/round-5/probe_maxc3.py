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

# n=4: try a=2, Y = three equal parts 8/3 each -> forces T,T,T run at top if Z's max < 8/3
n=4
theta=8.0
Y=[theta/3]*3   # sum=8=2^n, three equal fragments (a=2 cuts)
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
for cutcounts in [[0,0,0,2],[0,0,2,0]]:
    nz=sum((k+1 if k>0 else 0) for k in cutcounts)
    def obj(x):
        Z=build_Z(x,cutcounts); return altsum(Y+Z)
    best=None
    rng=np.random.default_rng(2)
    for t in range(80):
        x0=rng.normal(size=nz)
        res=minimize(obj,x0,method='Nelder-Mead',options={'maxiter':4000,'xatol':1e-10,'fatol':1e-12})
        if best is None or res.fun<best[0]: best=(res.fun,res.x.copy())
    Z=build_Z(best[1],cutcounts)
    print(cutcounts,"minD",best[0],"maxc",maxc_of(Y,Z))
