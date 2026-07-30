import random
from fractions import Fraction as F

def dtilde(parts):
    w = sorted(parts, reverse=True)
    s = F(0)
    for i,x in enumerate(w):
        s += x if i%2==0 else -x
    return s

def random_partition(total, k, rng):
    # random composition of `total` into k positive parts (Fraction), via random cut points
    if k==1:
        return [F(total)]
    cuts = sorted(rng.sample(range(1, int(total*1000)), k-1)) if False else None
    # use continuous random cuts scaled
    pts = sorted([rng.random()*total for _ in range(k-1)])
    pts = [0]+pts+[total]
    parts = [F(pts[i+1]-pts[i]).limit_denominator(10**6) for i in range(k)]
    return parts

def gen_F_prime(n, b, rng):
    # F' refines ladder {2^0,...,2^{n-1}} with total budget b cuts across n pieces
    # distribute b cuts among the n scales j=1..n (piece sizes 2^{n-j})
    cuts_per_scale = [0]*n
    for _ in range(b):
        j = rng.randrange(n)
        cuts_per_scale[j]+=1
    F_parts = []
    a1_forced_zero = cuts_per_scale[0]==0  # scale j=1 corresponds to index0 here (top of F')
    for j in range(n):
        size = F(2)**(n-1-j)
        k = cuts_per_scale[j]+1
        F_parts += random_partition(size, k, rng)
    return F_parts, a1_forced_zero

def gen_pi0(n, a0, rng):
    return random_partition(F(2)**n, a0+1, rng)

rng = random.Random(1)
n = 3
trials = 200000
residual_all = 0
residual_a1zero = 0
viol_all = 0
viol_a1zero = 0
min_D_all = None
min_D_a1zero = None
for t in range(trials):
    a0 = rng.randrange(0, n+1)  # 0..n
    remaining = n - a0
    b = rng.randrange(0, remaining+1)
    if a0==0:
        continue  # Case A already closed, skip
    pi0 = gen_pi0(n, a0, rng)
    Fp, a1zero = gen_F_prime(n, b, rng)
    Dpi0 = dtilde(pi0)
    DFp = dtilde(Fp)
    diff = abs(Dpi0-DFp)
    DF = dtilde(pi0+Fp)
    if diff < 1:
        residual_all += 1
        if DF < 1:
            viol_all += 1
        if min_D_all is None or DF < min_D_all:
            min_D_all = DF
        if a1zero:
            residual_a1zero += 1
            if DF < 1:
                viol_a1zero += 1
            if min_D_a1zero is None or DF < min_D_a1zero:
                min_D_a1zero = DF

print("n=",n,"trials=",trials)
print("residual_all=",residual_all,"viol_all(DF<1)=",viol_all,"min_D_all=",min_D_all)
print("residual_a1zero=",residual_a1zero,"viol_a1zero=",viol_a1zero,"min_D_a1zero=",min_D_a1zero)
