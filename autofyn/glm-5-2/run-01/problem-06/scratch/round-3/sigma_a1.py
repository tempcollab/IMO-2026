"""Test the hypothesis: for m in window NOT in B_n, does sigma(m) ALWAYS miss
sigma(a_1)? If so, (C) follows trivially (a_1 has no large prime to compensate).
Also: characterize the cases where sigma(m) HITS sigma(a_1) but misses another class
— those need the deeper obstruction.
"""
import math
from sympy import factorint
from collections import defaultdict
import sys
sys.path.insert(0,'/tmp/round-3')
from probe_c import minimal_hitting_sets, small_support, primes_of, rad, greedy_sequence, in_B_using_mh

def test(a1, N):
    R=rad(a1)
    a=greedy_sequence(a1,N)
    sigma_a1=frozenset(small_support(a[0],R))
    print(f"\n=== a1={a1} R={R} N={N} sigma(a1)={set(sigma_a1)} ===")
    total_notB=0
    miss_sigma_a1=0
    hit_sigma_a1_miss_other=0
    other_escape_examples=[]
    for n in range(len(a)-1):
        an=a[n]
        classes=defaultdict(list)
        for i in range(n+1):
            classes[frozenset(small_support(a[i],R))].append(i+1)
        Mn=minimal_hitting_sets(list(classes.keys()))
        for m in range(an+1,an+R+1):
            if in_B_using_mh(m,Mn): continue
            total_notB+=1
            sm=frozenset(small_support(m,R))
            if not (sm & sigma_a1):
                miss_sigma_a1+=1
            else:
                # sigma(m) hits sigma(a_1) but misses some other class
                hit_sigma_a1_miss_other+=1
                missed=[sig for sig in classes if not(sm & sig)]
                # these missed classes are all != sigma_a1
                # find the escape (sigma*-term not hit by large primes of m)
                large=[p for p in primes_of(m) if p>R]
                for sig in missed:
                    idxs=classes[sig]
                    hitvia=[j for j in idxs if any(a[j-1]%q==0 for q in large)]
                    esc=[j for j in idxs if j not in hitvia]
                    if len(esc)<=2 and len(other_escape_examples)<10:
                        other_escape_examples.append((n,m,an,set(sig),idxs,large,esc,hitvia))
    print(f"  total m not in B_n: {total_notB}")
    print(f"  # where sigma(m) MISSES sigma(a1): {miss_sigma_a1}")
    print(f"  # where sigma(m) HITS sigma(a1) but misses another class: {hit_sigma_a1_miss_other}")
    print(f"  examples of 'hits sigma(a1), misses other':")
    for e in other_escape_examples:
        n,m,an,sig,idxs,large,esc,hitvia=e
        print(f"    n={n} m={m} an={an} sigma*={sig} class_idxs={idxs} large(m)={sorted(large)} escape={esc} hitvia={hitvia}")

for a1,N in [(15,60),(35,50),(77,40),(91,40),(105,35),(175,30),(385,25),(45,50),(135,40),(187,30),(221,30)]:
    test(a1,N)
