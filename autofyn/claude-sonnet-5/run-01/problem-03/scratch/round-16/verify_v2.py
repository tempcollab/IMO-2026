from fractions import Fraction as F
import itertools, random

def c(k):
    if k==0: return F(1)
    return F(2**k, 2**(k+1)-1)

def L2(u,v):
    # u>=v>0, m=2 exact theorem
    assert u>=v
    if u>=2*v:
        return u/2+v
    else:
        return u

def V3(x1,x2,x3):
    xs=sorted([x1,x2,x3], reverse=True)
    x1,x2,x3=xs
    sigma=x1+x2+x3
    if x1>=c(2)*sigma:
        return x1/2 + L2(x2,x3)
    elif x1>=sigma/2:
        return x1
    else:
        # Case C: min(TAIL-SNIP, BLOCK-RECURSE_1)
        tail_snip = x1 + x3/2
        r = x1-x2
        # BLOCK-RECURSE_1: L0 = {r, x3}, matched pair v=x2
        block_recurse = x2 + L2(*sorted([r,x3],reverse=True))
        return min(tail_snip, block_recurse)

def V4_case_C(p1,t1,t2,t3):
    # assume sorted desc p1>=t1>=t2>=t3>0, Case C: p1 < t1+t2+t3
    tail=[t1,t2,t3]
    assert p1<sum(tail)
    # Strategy A
    r = p1-t1
    stratA = t1 + V3(t2,t3,r)
    # Strategy B
    stratB = p1/2 + V3(t1,t2,t3)
    results = {'A':stratA,'B':stratB}
    # Strategy C_{ij}
    for (i,j) in [(0,1),(0,2),(1,2)]:
        a = tail[i]; b = tail[j]
        hi,lo = max(a,b), min(a,b)
        k_idx = [x for x in range(3) if x!=i and x!=j][0]
        tk = tail[k_idx]
        r2 = hi-lo
        val = lo + V3(p1, tk, r2)
        results[f'C_{i}{j}'] = val
    return results

# Witness check
A = (F(1859), F(931), F(619), F(611))
Sigma = sum(A)
target = c(3)*Sigma
print("Sigma=",Sigma,"target=",target, float(target))
res = V4_case_C(*A)
for k,v in res.items():
    print(k, v, float(v))
print("min=", min(res.values()), float(min(res.values())))
print("min<=target:", min(res.values())<=target)

print("\n--- random trials ---")
random.seed(12345)
viol=0
worst=None
worst_margin=None
for trial in range(30000):
    # generate random sorted A in Case C
    while True:
        vals = [random.randint(1,2000) for _ in range(4)]
        vals = sorted(vals, reverse=True)
        p1,t1,t2,t3 = [F(v) for v in vals]
        if t1>=t2>=t3>0 and p1>=t1:
            if p1 < t1+t2+t3:
                break
    Sigma = p1+t1+t2+t3
    target = c(3)*Sigma
    res = V4_case_C(p1,t1,t2,t3)
    m = min(res.values())
    margin = target - m
    if margin < 0:
        viol+=1
        print("VIOLATION", p1,t1,t2,t3, m, target)
    if worst_margin is None or margin<worst_margin:
        worst_margin=margin
        worst=(p1,t1,t2,t3,m,target)
print("violations:", viol, "of 30000")
print("worst margin:", worst_margin, float(worst_margin))
print("worst witness:", worst)

print("\n--- exact check candidate tight point (6,4,3,2) ---")
p1,t1,t2,t3 = F(6),F(4),F(3),F(2)
Sigma=p1+t1+t2+t3
target=c(3)*Sigma
res=V4_case_C(p1,t1,t2,t3)
for k,v in res.items():
    print(k,v,float(v))
print("min=",min(res.values()), "target=",target, float(target))
print("margin=", target-min(res.values()))
