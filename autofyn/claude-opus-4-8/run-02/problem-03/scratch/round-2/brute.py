import numpy as np
from itertools import product
from scipy.optimize import minimize

def D_of(parts):
    b = sorted(parts, reverse=True)
    D = 0.0
    s = 1
    for x in b:
        D += s*x
        s = -s
    return D

def xiang_min_D(liu_parts, n_budget, restarts=8, seed=0):
    m = len(liu_parts)
    rng = np.random.default_rng(seed)
    best = None
    best_info = None
    # enumerate allocations k_1..k_m >=0 sum <= n_budget
    def allocs(m, budget):
        if m==1:
            for k in range(budget+1):
                yield (k,)
            return
        for k in range(budget+1):
            for rest in allocs(m-1, budget-k):
                yield (k,)+rest
    for alloc in allocs(m, n_budget):
        # total free params = sum(alloc) split points, each piece i has alloc[i] points in (0,L_i)
        total_params = sum(alloc)
        if total_params==0:
            val = D_of(liu_parts)
            if best is None or val<best:
                best=val; best_info=(alloc,None,val)
            continue
        # parametrize by unconstrained reals -> softmax-like normalized increments per piece
        def unpack(x):
            # x has total_params entries; for each piece with k_i cuts, we need k_i+1 positive fractions summing to L_i
            parts=[]
            idx=0
            for i,k in enumerate(alloc):
                L = liu_parts[i]
                if k==0:
                    parts.append(L)
                    continue
                raw = x[idx:idx+k+1]
                idx += k+1
                w = np.exp(raw)
                w = w/np.sum(w)
                parts.extend((w*L).tolist())
            return parts
        # count actual free variable length: for each piece with k cuts we use k+1 raw vars (softmax over k+1, one degree redundant but fine)
        nvar = sum((k+1) for k in alloc if k>0)
        def obj(x):
            parts = unpack(x)
            return D_of(parts)
        local_best=None
        for r in range(restarts):
            x0 = rng.normal(size=nvar)
            res = minimize(obj, x0, method='Nelder-Mead',
                            options={'maxiter':4000,'xatol':1e-9,'fatol':1e-12})
            if local_best is None or res.fun<local_best:
                local_best=res.fun
                local_x=res.x
        if best is None or local_best<best:
            best=local_best; best_info=(alloc, unpack(local_x), local_best)
    return best, best_info

# test n=2, dyadic Liu partition {4/7,2/7,1/7}
u2=1/7
liu=[4/7,2/7,1/7]
val,info = xiang_min_D(liu,2,restarts=10)
print("n=2 dyadic:", val, "target u=",u2, info[0])

# test some other Liu partitions n=2
tests = [
 [0.5,0.3,0.2],
 [0.6,0.25,0.15],
 [0.45,0.35,0.2],
 [0.7,0.2,0.1],
 [0.5,0.4,0.1],
 [0.55,0.3,0.15],
]
for t in tests:
    val,info = xiang_min_D(t,2,restarts=10)
    print(t, "-> minD=",val, "alloc=",info[0], "u2=",u2)

print("---dyadic n=2 detail---")
val,info = xiang_min_D([4/7,2/7,1/7],2,restarts=20)
print(val, info)
