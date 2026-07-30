from fractions import Fraction as F
from itertools import product as iprod

def alt_sum(m):
    s=F(0)
    for i,x in enumerate(sorted(m,reverse=True)):
        s += (x if i%2==0 else -x)
    return s

def tower(n):
    return [F(2**(n-k)) for k in range(n+1)]

# Enumerate ALL balanced-split refinements of T_n with <= n marks.
# A balanced split replaces a 2^k (k>=1) by two 2^{k-1}.
# We do recursive enumeration of multisets (as sorted tuples).
def refinements(n):
    T=tuple(sorted(tower(n),reverse=True))
    results=set()
    def rec(multiset, marks_left):
        results.add(multiset)
        if marks_left==0:
            return
        # find distinct piece values that are splittable (>=2)
        from collections import Counter
        c=Counter(multiset)
        seen=set()
        for v in multiset:
            if v in seen: continue
            seen.add(v)
            if v>=2:
                half=v/2
                # remove one v, add two halves
                lst=list(multiset)
                lst.remove(v)
                lst=lst+[half,half]
                new=tuple(sorted(lst,reverse=True))
                rec(new, marks_left-1)
    rec(T, n)
    return results

print("== Balanced (dyadic) refinements, min D, F-block cross-check ==")
for n in range(1,7):
    refs=refinements(n)
    minD=None
    allvals=[]
    F_formula_ok=True
    for M in refs:
        D=alt_sum(M)
        allvals.append(D)
        if minD is None or D<minD: minD=D
        # F-block formula check: D = sum_k 2^k (-1)^{C_k} (n_k mod 2)
        from collections import Counter
        c=Counter(M)
        keys=sorted(c.keys(),reverse=True)
        # map value 2^k -> k
        # values are powers of 2 (dyadic); k = log2
        import math
        Dfb=F(0)
        # C_k = sum_{j>k} n_j; iterate k from high to low
        keys_sorted=sorted([int(math.log2(int(v))) for v in c.keys()], reverse=True)
        # build by k
        n_by_k={int(math.log2(int(v))):int(c[v]) for v in c.keys()}
        Ck=0
        Kmax=max(n_by_k.keys())
        for k in range(Kmax,-1,-1):
            nk=n_by_k.get(k,0)
            if nk%2==1:
                Dfb += F(2)**k * ((-1)**Ck)
            Ck += nk
        if Dfb!=D:
            F_formula_ok=False
    print(f"n={n}: #refs={len(refs)}, min D={minD}, all odd: {all(d%2==1 for d in allvals)}, min>=1: {minD>=1}, F-block formula matches direct: {F_formula_ok}")
