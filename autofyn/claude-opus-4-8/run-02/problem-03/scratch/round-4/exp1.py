from fractions import Fraction as Fr
import random, itertools
from functools import lru_cache

def u(k): return Fr(1, 2**(k+1)-1)
def c(k): return Fr(2**k, 2**(k+1)-1)

import sys
sys.setrecursionlimit(100000)

def eval_f(pieces, budget, memo):
    pieces = tuple(sorted(pieces, reverse=True))
    if budget<=0 or len(pieces)==0:
        return sum(pieces, Fr(0))
    key=(pieces,budget)
    if key in memo: return memo[key]
    best = sum(pieces, Fr(0))
    m=len(pieces)
    # free delete equal pair
    for i in range(m):
        for j in range(i+1,m):
            if pieces[i]==pieces[j]:
                newp=pieces[:i]+pieces[i+1:j]+pieces[j+1:]
                v=eval_f(newp,budget,memo)
                if v<best: best=v
                break
    # bisect
    for i in range(m):
        newp=pieces[:i]+pieces[i+1:]
        v=eval_f(newp,budget-1,memo)
        if v<best: best=v
    # pin j into i
    for i in range(m):
        for j in range(m):
            if i!=j and pieces[i]>pieces[j]:
                rem=pieces[i]-pieces[j]
                newp=tuple(pieces[x] for x in range(m) if x!=i and x!=j)+(rem,)
                v=eval_f(newp,budget-1,memo)
                if v<best: best=v
    memo[key]=best
    return best

def optf(pieces,k):
    return eval_f(tuple(pieces),k,{})

# random Case (iii) instances, verify residual <= u_k, split by beta
random.seed(1)
for k in range(2,5):
    uk=u(k); ck=c(k)
    viol=0; maxratio_lo=Fr(0); maxratio_hi=Fr(0); n_lo=0;n_hi=0
    for _ in range(300):
        # random partition into k+1 pieces
        cuts=sorted(Fr(random.randint(1,9999),10000) for _ in range(k))
        pts=[Fr(0)]+cuts+[Fr(1)]
        pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
        if any(p==0 for p in pieces): continue
        l1=pieces[0]; l2=pieces[1]
        if not (l1<ck and 2*l2<ck): continue  # only Case (iii)
        r=optf(pieces,k)
        ratio=r/uk
        if r>uk: viol+=1
        if l1<Fr(1,2):
            n_lo+=1; maxratio_lo=max(maxratio_lo,ratio)
        else:
            n_hi+=1; maxratio_hi=max(maxratio_hi,ratio)
    print(f"k={k} uk={float(uk):.5f} viol={viol}  beta<1/2: n={n_lo} maxratio={float(maxratio_lo):.4f}   beta>=1/2: n={n_hi} maxratio={float(maxratio_hi):.4f}")
