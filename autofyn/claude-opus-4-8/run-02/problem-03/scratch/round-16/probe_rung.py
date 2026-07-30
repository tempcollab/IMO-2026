import random
from fractions import Fraction as F

random.seed(1)

def rand_partition(total, k, rng):
    # random composition of total into k positive parts (exact Fraction)
    if k == 1:
        return [total]
    cuts = sorted(F(rng.randint(1, 10**6-1), 10**6) for _ in range(k-1))
    pts = [F(0)] + cuts + [F(1)]
    parts = [total*(pts[i+1]-pts[i]) for i in range(k)]
    return parts

def gen_feasible(n, rng, budget=None):
    # rungs j=0..n, sum(pi_j) = 2^(n-j), a_j cuts => a_j+1 parts
    # budget: sum a_j <= n  (global cut budget)
    if budget is None:
        budget = n
    # distribute budget among rungs 0..n randomly
    a = [0]*(n+1)
    remaining = rng.randint(0, budget)
    for _ in range(remaining):
        a[rng.randint(0,n)] += 1
    rungs = []
    for j in range(n+1):
        total = F(2)**(n-j)
        k = a[j]+1
        parts = rand_partition(total, k, rng)
        rungs.append(parts)
    return rungs

def N(parts, t):
    return sum(1 for p in parts if p > t)

def compute_I(n, rungs, sample_pts):
    # I_n = integral over (0,theta) of floor(M/2), M = N_pi0(t) - N_F'(t)
    theta = F(2)**(n-1)
    pi0 = rungs[0]
    Fprime = [p for j in range(1,n+1) for p in rungs[j]]
    # integrate exactly via breakpoints
    breakpoints = sorted(set([p for p in pi0 if p<theta] + [p for p in Fprime if p<theta] + [F(0), theta]))
    I = F(0)
    P = F(0)
    Q = F(0)
    for i in range(len(breakpoints)-1):
        a,b = breakpoints[i], breakpoints[i+1]
        if b<=0 or a>=theta: continue
        a = max(a, F(0)); b = min(b, theta)
        if b<=a: continue
        mid = (a+b)/2
        m = N(pi0, mid) - N(Fprime, mid)
        fl = m//2  # floor division works for Fraction? need proper floor
        import math
        fl = math.floor(m)
        fl = fl//2 if fl>=0 else -((-fl+1)//2)
        # actually floor(m/2) for integer m:
        fl = m//2 if m>=0 else -((-m+1)//2)
        length = b-a
        I += fl*length
        if fl>0: P += fl*length
        if fl<0: Q += -fl*length
    return I, P, Q, pi0, rungs[1:]

n=4
trials=3000
minI = None
worstcfg=None
for t in range(trials):
    rungs = gen_feasible(n, random)
    I,P,Q,pi0,frest = compute_I(n, rungs, None)
    if minI is None or I>minI:
        minI = I
        worstcfg = (rungs, I, P, Q)
print("n=",n,"max I over",trials,"trials:", float(minI))
print(worstcfg[0])
print("I,P,Q=", float(worstcfg[1]), float(worstcfg[2]), float(worstcfg[3]))

# Separating witness: aggregate-only (rung sums NOT forced individually, only total + budget)
# vs exact per-rung equality kept.
import math
def gen_aggregate_only(n, rng, budget=None):
    # total mass 2^{n+1}-1 split into (budget+1) parts arbitrarily (NOT forced per-rung sums)
    if budget is None: budget=n+ n # generous total pieces bound like sum(a_j+1) <= 2n+1 roughly
    total = F(2)**(n+1)-1
    k = rng.randint(n+1, 2*n+2)
    parts = rand_partition(total, k, rng)
    return parts

def compute_I_flat(n, allparts, top_count_hint=None):
    # split into "pi0-like" top and "F'-like" rest is ill-defined without rung structure;
    # instead just recompute D~ directly and compare to 1
    parts = sorted(allparts, reverse=True)
    D = F(0)
    for i,w in enumerate(parts):
        D += w if i%2==0 else -w
    return D

trials=20000
minD=None
for t in range(trials):
    parts = gen_aggregate_only(n, random)
    D = compute_I_flat(n, parts)
    if minD is None or D<minD:
        minD=D
        worst=parts
print("aggregate-only (no per-rung equality) min D~ over",trials,"trials, n=",n,":", float(minD))
print(worst)
