"""Probe the REAL (C) obstruction: m in window with sigma(m) missing some class sigma*
(m NOT in B_n) but m in A_n (would be a (C) violation). Since (C) has 0 violations,
every m not in B_n also fails A_n. Find m NOT in B_n that is "closest" to A_n,
and identify which past a_i it misses and why.
"""
import math
from sympy import factorint
from collections import defaultdict
import sys
sys.path.insert(0,'/tmp/round-3')
from probe_c import minimal_hitting_sets, small_support, primes_of, rad, greedy_sequence, in_B_using_mh

def analyze_obstruction(a1, N, max_near=10):
    R=rad(a1)
    a=greedy_sequence(a1,N)
    print(f"\n=== a1={a1} R={R} N={N} ===")
    # For each n, for each m in window NOT in B_n, find # missed and the structure.
    # Focus on m NOT in B_n but missing few a_i (closest to admissible).
    best_per_n=[]
    violation_count=0
    for n in range(len(a)-1):
        an=a[n]
        Mn = minimal_hitting_sets(list({frozenset(small_support(ai,R)) for ai in a[:n+1]}))
        for m in range(an+1, an+R+1):
            inB = in_B_using_mh(m, Mn)
            if inB: continue
            # m not in B_n. Find missed a_i.
            missed=[(i+1,a[i]) for i in range(n+1) if math.gcd(m,a[i])==1]
            if len(missed)==0:
                violation_count+=1
                print(f"  VIOLATION n={n} m={m} an={an}")
            elif len(missed)<=2:
                best_per_n.append((n,m,an,len(missed),missed,sorted(primes_of(m))))
    print(f"  violations: {violation_count}")
    print(f"  #m-not-in-B missing <=2 past terms: {len(best_per_n)}")
    # Show samples
    for entry in best_per_n[:20]:
        n,m,an,nm,missed,ps=entry
        small_p=[p for p in ps if p<=R]
        large_p=[p for p in ps if p>R]
        print(f"  n={n} m={m} an={an} #missed={nm} missed={missed} small_primes={small_p} large_primes={large_p}")

# Run for several a_1
for a1,N in [(15,80),(35,60),(77,50),(91,50),(105,40),(175,40),(385,30)]:
    analyze_obstruction(a1,N)
