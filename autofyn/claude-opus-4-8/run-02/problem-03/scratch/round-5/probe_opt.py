import numpy as np
from scipy.optimize import minimize
import random

def softmax_split(x, total):
    e = np.exp(x - np.max(x))
    w = e/e.sum()
    return w*total

def build_Z_from_params(n, cut_assign, params, idx):
    # cut_assign[j] = number of cuts for piece 2^j, j=0..n-1
    Z=[]
    p=idx
    for j in range(n):
        k = cut_assign[j]
        piece = 2**j
        if k==0:
            Z.append(piece)
        else:
            frags = softmax_split(params[p:p+k+1], piece)
            p+=k+1
            Z.extend(frags)
    return Z, p

def altsum(vals):
    s=sorted(vals, reverse=True)
    tot=0; sign=1
    for v in s:
        tot+=sign*v; sign=-sign
    return tot

def Dtilde(Yparams, n, a, Zcuts, Zparams):
    Y = softmax_split(Yparams, 2**n)
    Z,_ = build_Z_from_params(n, Zcuts, Zparams, 0)
    return altsum(list(Y)+list(Z))

def maxc_of(Y,Z):
    merged = sorted([(w,1) for w in Y]+[(w,-1) for w in Z], key=lambda x:-x[0])
    c=0; mx=0
    for w,s in merged:
        c+=s; mx=max(mx,c)
    return mx

def objective_with_penalty(x, n, a, Zcuts, ny, nz):
    Yparams = x[:ny]
    Zparams = x[ny:ny+nz]
    Y = softmax_split(Yparams, 2**n)
    Z,_ = build_Z_from_params(n, Zcuts, Zparams, 0)
    D = altsum(list(Y)+list(Z))
    mc = maxc_of(Y,Z)
    pen = 0.0
    if mc < 2:
        pen = 100*(2-mc)  # not quite continuous but ok for exploration via restarts
    return D + pen

results=[]
rng=np.random.default_rng(0)
for n in [3,4]:
    for a in range(1, n):
        # try various Zcuts assignments (budget n-a)
        budget = n-a
        # enumerate simple assignments: all cuts on piece 0 (smallest), or spread
        assigns = []
        assigns.append([budget]+[0]*(n-1))  # all on smallest
        assigns.append([0]*(n-1)+[budget])  # all on largest (Z's top)
        if n>=3:
            half = budget//2
            assigns.append([half, budget-half]+[0]*(n-2))
        for Zcuts in assigns:
            if sum(Zcuts)!=budget: continue
            ny = a+1
            nz = sum(Zcuts)+ (n - sum(1 for c in Zcuts if c>0==False))  # rough; just count total frag params needed
            # recompute nz properly
            nz = sum((k+1 if k>0 else 0) for k in Zcuts)  # params only for cut pieces (softmax dims = k+1)
            if nz==0: nz=1
            best=None
            for trial in range(20):
                x0 = rng.normal(size=ny+nz)
                res = minimize(objective_with_penalty, x0, args=(n,a,Zcuts,ny,nz), method='Nelder-Mead',
                                options={'maxiter':3000,'xatol':1e-8,'fatol':1e-10})
                Yparams=res.x[:ny]; Zparams=res.x[ny:ny+nz]
                Y=softmax_split(Yparams,2**n)
                Z,_=build_Z_from_params(n,Zcuts,Zparams,0)
                mc=maxc_of(Y,Z)
                D=altsum(list(Y)+list(Z))
                if mc>=2 and (best is None or D<best[0]):
                    best=(D,Y,Z,mc)
            if best:
                results.append((n,a,Zcuts,best))
                print(f"n={n} a={a} Zcuts={Zcuts}: min D(maxc>=2)={best[0]:.5f} maxc={best[3]} Y={np.round(best[1],3)} Z={np.round(best[2],3)}")
