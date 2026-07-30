import sys, numpy as np
sys.path.insert(0,'/tmp/round-2')
from brute import xiang_min_D, D_of
from scipy.optimize import minimize

def top_cut_only_minD(liu, n_budget, restarts=15, seed=0):
    # only allocate all cuts to the single largest piece (index 0 after sort)
    liu = sorted(liu, reverse=True)
    rest = liu[1:]
    L = liu[0]
    k = n_budget
    rng = np.random.default_rng(seed)
    def unpack(x):
        w = np.exp(x); w/=w.sum()
        return (w*L).tolist() + rest
    def obj(x):
        return D_of(unpack(x))
    best=None
    for r in range(restarts):
        x0 = rng.normal(size=k+1)
        res = minimize(obj,x0, method='Nelder-Mead', options={'maxiter':3000,'xatol':1e-9,'fatol':1e-12})
        if best is None or res.fun<best: best=res.fun
    return best

rng=np.random.default_rng(11)
u2=1/7
print("n=2 top-cut-only strategy test:")
worst=-1
for i in range(25):
    w = rng.dirichlet([1,1,1])
    liu = sorted(w.tolist(), reverse=True)
    v = top_cut_only_minD(liu, 2, restarts=8, seed=i)
    if v>worst: worst=v; worstliu=liu
print("worst (top-cut-only) over random Liu:", worst, "at", worstliu, "vs u2=",u2)

print("n=2 dyadic via top-cut-only:", top_cut_only_minD([4/7,2/7,1/7],2,restarts=15))
