import random
from fractions import Fraction as F

def dtilde(parts):
    w = sorted(parts, reverse=True)
    s = F(0)
    for i,x in enumerate(w):
        s += x if i%2==0 else -x
    return s

DENOM = 10000

def random_partition(total, k, rng):
    if k==1:
        return [F(total)]
    total_units = int(total*DENOM)
    if total_units < k:
        # degenerate, just pad
        pts = sorted(rng.sample(range(0, total_units+1), 1)*  (k-1)) if k-1>0 else []
    cuts = sorted(rng.sample(range(1, total_units), k-1))
    pts = [0]+cuts+[total_units]
    parts = [F(pts[i+1]-pts[i], DENOM) for i in range(k)]
    return parts

def gen_F_prime(n, b, rng):
    cuts_per_scale = [0]*n
    for _ in range(b):
        j = rng.randrange(n)
        cuts_per_scale[j]+=1
    F_parts = []
    a1_forced_zero = cuts_per_scale[0]==0
    for j in range(n):
        size = F(2)**(n-1-j)
        k = cuts_per_scale[j]+1
        F_parts += random_partition(size, k, rng)
    return F_parts, a1_forced_zero

def gen_pi0(n, a0, rng):
    return random_partition(F(2)**n, a0+1, rng)

rng = random.Random(2)
n = 3
trials = 300000
residual_all = 0
residual_a1zero = 0
viol_all = 0
viol_a1zero = 0
min_D_all = None
min_D_a1zero = None
worst_example = None
for t in range(trials):
    a0 = rng.randrange(1, n+1)  # skip Case A (a0=0), already closed
    remaining = n - a0
    b = rng.randrange(0, remaining+1)
    try:
        pi0 = gen_pi0(n, a0, rng)
        Fp, a1zero = gen_F_prime(n, b, rng)
    except ValueError:
        continue
    Dpi0 = dtilde(pi0)
    DFp = dtilde(Fp)
    diff = abs(Dpi0-DFp)
    DF = dtilde(pi0+Fp)
    if diff < 1:
        residual_all += 1
        if DF < 1:
            viol_all += 1
            if worst_example is None or DF < worst_example[0]:
                worst_example = (DF, pi0, Fp)
        if min_D_all is None or DF < min_D_all:
            min_D_all = DF
        if a1zero:
            residual_a1zero += 1
            if DF < 1:
                viol_a1zero += 1
            if min_D_a1zero is None or DF < min_D_a1zero:
                min_D_a1zero = DF

print("n=",n,"trials=",trials)
print("residual_all=",residual_all,"viol_all(DF<1)=",viol_all,"min_D_all=",float(min_D_all))
print("residual_a1zero=",residual_a1zero,"viol_a1zero=",viol_a1zero,"min_D_a1zero=",float(min_D_a1zero) if min_D_a1zero else None)
if worst_example:
    print("worst example DF=",float(worst_example[0]))
    print("pi0=",[float(x) for x in worst_example[1]])
    print("Fp=",[float(x) for x in worst_example[2]])
