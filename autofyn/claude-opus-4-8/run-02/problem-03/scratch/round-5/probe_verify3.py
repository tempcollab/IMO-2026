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

Y=[4.0,4.0]
def obj(x):
    e=np.exp(x-np.max(x)); w=e/e.sum()*4.0
    Z=[1.0,2.0]+list(w)
    return altsum(Y+Z)

best=None
rng=np.random.default_rng(5)
for trial in range(300):
    x0=rng.normal(size=3)
    res=minimize(obj,x0,method='Nelder-Mead',options={'maxiter':5000,'xatol':1e-10,'fatol':1e-12})
    if best is None or res.fun<best[0]:
        e=np.exp(res.x-np.max(res.x)); w=e/e.sum()*4.0
        best=(res.fun,list(w))
print("min D found for Y=(4,4),Z={1,2}+split(4):", best)
Z=[1.0,2.0]+best[1]
print("maxc at min:", maxc_of(Y,Z))
print("merged sorted:", sorted(Y+Z,reverse=True))
