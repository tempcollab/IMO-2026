import numpy as np
from scipy.optimize import minimize
import sys
sys.path.insert(0,'/tmp/round-2')
from brute import xiang_min_D, D_of

rng = np.random.default_rng(1)

def liu_from_x(x):
    w = np.exp(x); w/=w.sum()
    return sorted(w.tolist(), reverse=True)

def neg_inner(x):
    liu = liu_from_x(x)
    val,_ = xiang_min_D(liu, 2, restarts=4, seed=0)
    return -val

best=None
for trial in range(6):
    x0 = rng.normal(size=3)
    res = minimize(neg_inner, x0, method='Nelder-Mead', options={'maxiter':40,'xatol':1e-3,'fatol':1e-4})
    liu = liu_from_x(res.x)
    val = -res.fun
    print(trial, liu, val)
    if best is None or val>best:
        best=val; bestliu=liu
print("BEST", bestliu, best, "u2=1/7=",1/7)
