"""Key structural test: for each sigma*-class in F'_n, does it contain a term
a_j whose FULL support has NO large prime (all primes <= R)?
If YES for every class, then (C) follows: m not in B_n misses some sigma*;
that class has an all-small term a_j; m can't hit a_j via large primes (a_j has none);
m misses a_j; m not in A_n. QED.

Also test the STRONGER form: does every class contain a term with support = sigma*
(i.e. supp(a_j) ∩ {primes>R} = ∅)?
"""
import math
from sympy import factorint
from collections import defaultdict
import sys
sys.path.insert(0,'/tmp/round-3')
from probe_c import minimal_hitting_sets, small_support, primes_of, rad, greedy_sequence

def test(a1, N):
    R=rad(a1)
    a=greedy_sequence(a1,N)
    print(f"\n=== a1={a1} R={R} N={N} ===")
    # for each n, build classes, check each class has an all-small term
    all_ok=True
    worst=[]
    for n in range(len(a)):
        classes=defaultdict(list)
        for i in range(n+1):
            classes[frozenset(small_support(a[i],R))].append(i+1)
        for sig,idxs in classes.items():
            # does any term in this class have all primes <= R?
            has_allsmall=any(all(p<=R for p in primes_of(a[j-1])) for j in idxs)
            if not has_allsmall:
                all_ok=False
                if len(worst)<8:
                    worst.append((n,set(sig),idxs,[primes_of(a[j-1]) for j in idxs]))
    print(f"  every class has an all-small term (up to n={N}): {all_ok}")
    if worst:
        print(f"  classes WITHOUT an all-small term:")
        for n,sig,idxs,sups in worst:
            print(f"    n={n} sig={sig} idxs={idxs} supports={sups}")
    # also: which classes appear, and does the all-small term appear EARLY (small index)?
    # show class structure at n=N
    classes=defaultdict(list)
    for i in range(N):
        classes[frozenset(small_support(a[i],R))].append(i+1)
    print(f"  classes at n={N}: {len(classes)}")
    for sig,idxs in sorted(classes.items(), key=lambda x:-len(x[1])):
        allsmall_idx=[j for j in idxs if all(p<=R for p in primes_of(a[j-1]))]
        print(f"    sig={set(sig)} size={len(idxs)} #allsmall={len(allsmall_idx)} first_allsmall={allsmall_idx[:3]} first_idxs={idxs[:3]}")

for a1,N in [(15,80),(35,60),(77,45),(91,45),(105,40),(175,40),(385,30),(45,60),(135,40),(187,30),(221,30)]:
    test(a1,N)
