from fractions import Fraction as F

def L2(u,v):
    # 2-element list optimal value under <=1 mark, u>=v
    u,v = max(u,v), min(u,v)
    if u >= 2*v:
        return u/2+v
    else:
        return u

def V3(p1,t1,t2):
    # sorted desc triple, tail (t1,t2)
    p1,t1,t2 = sorted([p1,t1,t2], reverse=True)
    S = t1+t2
    if p1 >= S:
        return p1  # Lemma DOM
    # Case C
    tailsnip = p1 + t2/F(2)
    r = p1 - t1
    leftover = L2(r, t2)
    blockrec = t1 + leftover
    return min(tailsnip, blockrec)

def target(m, Sigma):
    # c(m-1)*Sigma where c(k)=2^k/(2^{k+1}-1)
    k = m-1
    ck = F(2**k, 2**(k+1)-1)
    return ck*Sigma

def c(k):
    return F(2**k, 2**(k+1)-1)

# witness
A = [F(1859), F(931), F(619), F(611)]
Sigma = sum(A)
tgt = target(4, Sigma)
print("Sigma", Sigma, "target", tgt, float(tgt))

p1,t1,t2,t3 = A
tail = [t1,t2,t3]

# Strategy C: tie t_i,t_j among tail (i<j indices in tail list, 0-indexed), split larger into (smaller, remainder)
best = None
for i in range(3):
    for j in range(3):
        if i==j: continue
        a,b = tail[i], tail[j]
        if a < b: continue  # need a>=b to split a into (b, a-b)
        others = [tail[k] for k in range(3) if k not in (i,j)]
        tk = others[0]
        r = a - b
        # new multiset after split: p1, tk, b,b,r  -> value = b + V3(p1, tk, r)  [DOUBLE-INSERT]
        val = b + V3(p1, tk, r)
        print(f"tie tail[{i}]={a} -> tail[{j}]={b}, other tail={tk}, r={r}: value={val} = {float(val)}")
        if best is None or val < best:
            best = val

print("best StrategyC value:", best, float(best), "target", float(tgt), "beats target?", best<=tgt)

# also compute StratA and StratB (peel p1, halve p1) with correct V3
r = p1 - t1
stratA = t1 + V3(t2,t3,r)
stratB = p1/F(2) + V3(t1,t2,t3)
print("StratA", stratA, float(stratA))
print("StratB", stratB, float(stratB))
print("min(A,B,C)", min(stratA,stratB,best), "target", float(tgt))
