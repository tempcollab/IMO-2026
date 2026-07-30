import itertools, random
from functools import lru_cache

def u(k):
    return 1.0/(2**(k+1)-1)

def eval_f(pieces, budget, memo=None):
    # pieces: tuple sorted descending, positive floats, budget: int ops remaining
    # returns minimal achievable total (float)
    pieces = tuple(sorted(pieces, reverse=True))
    if budget<=0 or len(pieces)==0:
        return sum(pieces)
    key=(pieces,budget)
    if memo is not None and key in memo:
        return memo[key]
    best = sum(pieces)  # do-nothing baseline (not using budget) always an option (not forced to use all ops)
    m=len(pieces)
    # free-delete any equal pair (0 cost) -- generically won't fire except after pin creating duplicates,
    # but check anyway with tolerance
    for i in range(m):
        for j in range(i+1,m):
            if abs(pieces[i]-pieces[j])<1e-12:
                newp = pieces[:i]+pieces[i+1:j]+pieces[j+1:]
                val = eval_f(newp, budget, memo)
                if val<best: best=val
    # bisect each distinct piece (index-based to allow duplicates)
    for i in range(m):
        newp = pieces[:i]+pieces[i+1:]
        val = eval_f(newp, budget-1, memo)
        if val<best: best=val
    # pin j into i, ℓ_i>ℓ_j strictly
    for i in range(m):
        for j in range(m):
            if i==j: continue
            if pieces[i]>pieces[j]+1e-12:
                rem = pieces[i]-pieces[j]
                newp = [pieces[x] for x in range(m) if x!=i and x!=j] + [rem]
                val = eval_f(tuple(newp), budget-1, memo)
                if val<best: best=val
    if memo is not None:
        memo[key]=best
    return best

def f(ell, k):
    # ell: list of k+1 pieces summing to 1
    memo={}
    return eval_f(tuple(ell), k, memo)

if __name__=='__main__':
    for k in range(1,5):
        print("k=",k,"u_k=",u(k))

def dyadic(k):
    u_k = u(k)
    return [2**i*u_k for i in range(k,-1,-1)]

def c(k):
    return 1 - u(k)/u(k-1) if k>=1 else 1.0
