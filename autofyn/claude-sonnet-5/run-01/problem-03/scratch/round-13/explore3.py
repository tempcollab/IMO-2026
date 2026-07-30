import sympy as sp

x, y, z = sp.symbols('x y z', positive=True)  # p1,p2,p3 fractions of Sigma=1, x+y+z=1
# We'll just work with p1=x, p2=y, p3=1-x-y (m=3)
p1, p2 = x, y
p3 = 1 - x - y

def solve_full_m3(p1,p2,p3,budget=1):
    # returns symbolic expression min(...) is hard symbolically; instead evaluate all branch expressions
    # tail = (p2,p3) sorted desc -- assume p2>=p3 always in our regime
    # Move1: p1/2 + solve((p2,p3),budget)
    # solve((p2,p3),budget): m=2 -> Move1: p2/2+p3 ; Move2: partial-dom on (p2,p3) with top p2: S1=p3(tail=(p3,)), if p2>=p3 jstar=1,leftover=[] -> val=p3... wait tail of (p2,p3) is (p3,). S_1=p3. p2>=p3 always true (sorted). So jstar=1, leftover=(), r=p2-p3
        # leftover would include r if r>0: leftover=(p2-p3,) if p2>p3 else empty
    # Let's just implement generally with sympy Min won't handle branching well symbolically; do case-based.
    pass

# Let's do purely numeric evaluation across grid using fractions, not symbolic Min.
from fractions import Fraction as F
import random

def solve(A, budget):
    A = tuple(sorted(A, reverse=True))
    if len(A) == 1:
        return A[0]
    p1 = A[0]; tail = A[1:]
    v1 = p1/2 + solve(tail, budget)
    S = F(0); jstar=0
    for j in range(1,len(tail)+1):
        Snew = S+tail[j-1]
        if p1>=Snew:
            jstar=j; S=Snew
        else: break
    r = p1-S
    leftover = list(tail[jstar:])
    if r>0: leftover.append(r)
    leftover = tuple(leftover)
    v2 = S if len(leftover)==0 else S+solve(leftover, max(budget-1,0))
    cands=[v1,v2]
    if len(A)%2==1 and len(A)>=3 and budget>0:
        last=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[last/2,last/2],reverse=True))
        cands.append(solve(Aprime,budget-1))
    return min(cands)

# scan m=3 grid: p1 in (0,0.5), p2 in (R2/2, p1], p3=1-p1-p2
worst=None; worstA=None
N=60
for i in range(1,N):
    p1f = 0.5*i/N
    for j in range(1,N):
        # p2 ranges over (R2/2,p1] where R2=1-p1
        R2 = 1-p1f
        lo = R2/2
        hi = p1f
        if lo>=hi: continue
        p2f = lo + (hi-lo)*j/N
        p3f = 1-p1f-p2f
        if p3f<0: continue
        if p2f < p3f: continue
        A=[F(p1f).limit_denominator(1000), F(p2f).limit_denominator(1000), F(p3f).limit_denominator(1000)]
        s=sum(A)
        A=[a/s for a in A]
        val=solve(A,1)
        margin = F(1,2)-val
        if worst is None or margin<worst:
            worst=margin; worstA=A
print("worst margin (m=3, tail-dominant region):", worst, float(worst))
print("worst A:", worstA, [float(a) for a in worstA])
