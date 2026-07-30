from fractions import Fraction as F

def c(k):
    return F(2**k, 2**(k+1)-1)

def L1(x):
    return x

def L2(u,v):
    u,v = max(u,v), min(u,v)
    sigma = u+v
    if u >= c(1)*sigma:  # u>=2v
        return u/F(2) + L1(v)
    else:
        return u  # DOM

def V3(a,b,d):
    x1,x2,x3 = sorted([a,b,d], reverse=True)
    sigma = x1+x2+x3
    if x1 >= c(2)*sigma:
        # Case A: peel-half + IH(L2 on x2,x3)
        return x1/F(2) + L2(x2,x3)
    elif x1 >= sigma/F(2):
        # Case B: DOM
        return x1
    else:
        # Case C
        t1,t2 = x2,x3
        tailsnip = x1 + t2/F(2)
        r = x1 - t1
        leftover = L2(r,t2)
        blockrec = t1 + leftover
        return min(tailsnip, blockrec)

def target(m, Sigma):
    k = m-1
    return c(k)*Sigma

# sanity check extremal (3/7,2/7,2/7)
print(V3(F(3,7),F(2,7),F(2,7)), c(2))

A = [F(1859), F(931), F(619), F(611)]
Sigma = sum(A)
tgt = target(4, Sigma)
print("Sigma", Sigma, "target", tgt, float(tgt))
p1,t1,t2,t3 = A
tail=[t1,t2,t3]

best=None
records=[]
for i in range(3):
    for j in range(3):
        if i==j: continue
        a,b = tail[i], tail[j]
        if a<b: continue
        others=[tail[k] for k in range(3) if k not in (i,j)]
        tk = others[0]
        r = a-b
        val = b + V3(p1, tk, r)
        records.append((i,j,val))
        if best is None or val<best: best=val

for rec in records: print(rec, float(rec[2]))
print("best StrategyC:", best, float(best))

r = p1-t1
stratA = t1 + V3(t2,t3,r)
stratB = p1/F(2) + V3(t1,t2,t3)
print("StratA",stratA,float(stratA))
print("StratB",stratB,float(stratB))
print("overall min", min(stratA,stratB,best), "target", float(tgt), "OK?", min(stratA,stratB,best)<=tgt)

def stratC_all(p1,t1,t2,t3):
    tail=[t1,t2,t3]
    best=None
    for i in range(3):
        for j in range(3):
            if i==j: continue
            a,b=tail[i],tail[j]
            if a<b: continue
            others=[tail[k] for k in range(3) if k not in (i,j)]
            tk=others[0]
            r=a-b
            val = b + V3(p1, tk, r)
            if best is None or val<best: best=val
    return best

def full_min(p1,t1,t2,t3):
    r = p1-t1
    stratA = t1 + V3(t2,t3,r)
    stratB = p1/F(2) + V3(t1,t2,t3)
    stratC = stratC_all(p1,t1,t2,t3)
    return min(stratA,stratB,stratC)

# known extremal witness
A = [F(6),F(5),F(4),F(2)]
Sigma = sum(A)
tgt = target(4,Sigma)
print("extremal (6,5,4,2)/17:", full_min(*A), float(full_min(*A)), "target", tgt, float(tgt))

import random
random.seed(1)
worst_margin = None
worst_A = None
trials=20000
for _ in range(trials):
    vals = [random.randint(1,2000) for _ in range(4)]
    vals.sort(reverse=True)
    p1,t1,t2,t3 = [F(v) for v in vals]
    Sigma = p1+t1+t2+t3
    if not (p1 < t1+t2+t3):  # need Case C
        continue
    tgt = target(4,Sigma)
    val = full_min(p1,t1,t2,t3)
    margin = tgt - val
    if worst_margin is None or margin < worst_margin:
        worst_margin = margin
        worst_A = (p1,t1,t2,t3)

print("worst margin over", trials, "trials:", worst_margin, float(worst_margin), "at", worst_A)
