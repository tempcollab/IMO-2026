"""Test: (1) Is the FIRST term of each sigma*-class always R-smooth?
(2) For the proof idea: if first term a_j of class sigma* has a large prime,
    let s = a_j with all large-prime factors removed (R-smooth part).
    Is s admissible for {a_1..a_{j-1}}? Is s > a_{j-1} (contradiction) or <= a_{j-1}?
    Does s appear as a prior term (contradiction via newness)?
"""
import math
from sympy import factorint
from collections import defaultdict
import sys
sys.path.insert(0,'/tmp/round-3')
from probe_c import small_support, primes_of, rad, greedy_sequence

def R_smooth_part(n, R):
    """Remove all prime factors > R from n."""
    s=1
    for p,e in factorint(n).items():
        if p<=R:
            s*=p**e
    return s

def test(a1, N):
    R=rad(a1)
    a=greedy_sequence(a1,N)
    print(f"\n=== a1={a1} R={R} N={N} ===")
    # first appearance of each sigma*
    first={}
    for i,ai in enumerate(a):
        sig=frozenset(small_support(ai,R))
        if sig not in first:
            first[sig]=(i+1,ai)
    # check: is first term R-smooth?
    all_first_smooth=all(all(p<=R for p in primes_of(ai)) for _,ai in first.values())
    print(f"  #classes={len(first)} all_first_terms_Rsmooth={all_first_smooth}")
    if not all_first_smooth:
        for sig,(idx,ai) in first.items():
            if any(p>R for p in primes_of(ai)):
                print(f"    FIRST NOT RSMOOTH: sig={set(sig)} idx={idx} a={ai} primes={primes_of(ai)}")
    # proof idea test: for first terms with large primes (if any), check s
    # Also: for ALL terms (not just first) with large primes, check s admissibility & position
    proof_gap_examples=[]
    for j in range(1,len(a)):
        aj=a[j]
        if not any(p>R for p in primes_of(aj)): continue
        sig=frozenset(small_support(aj,R))
        is_first = (first[sig][0]==j+1)
        s=R_smooth_part(aj,R)
        # is s admissible for a_0..a_{j-1}?
        admissible = all(math.gcd(s,a[i])>1 for i in range(j))
        gt_prev = s > a[j-1]
        # is s a prior term?
        s_in_seq = s in set(a[:j])
        proof_gap_examples.append((j+1,aj,is_first,s,admissible,gt_prev,s_in_seq,sorted(primes_of(aj))))
    # show first-term cases
    first_large=[e for e in proof_gap_examples if e[2]]
    print(f"  #terms with large prime: {len(proof_gap_examples)}; #first-of-class-with-large: {len(first_large)}")
    if first_large:
        print(f"  first-of-class-with-large examples:")
        for e in first_large[:10]:
            j,aj,isf,s,adm,gt,sin,ps=e
            print(f"    j={j} a_j={aj} primes={ps} s={s} s_admissible={adm} s>a_(j-1)={gt} s_in_prior_seq={sin}")
    # distribution: for terms-with-large-prime, is s always admissible? always > a_{j-1}?
    n_adm=sum(1 for e in proof_gap_examples if e[4])
    n_gt=sum(1 for e in proof_gap_examples if e[5])
    n_sin=sum(1 for e in proof_gap_examples if e[6])
    print(f"  among terms-with-large-prime: s_admissible={n_adm}/{len(proof_gap_examples)} s>a_(j-1)={n_gt} s_in_prior_seq={n_sin}")

for a1,N in [(15,80),(35,60),(77,45),(91,45),(105,40),(175,40),(385,30),(45,60),(135,40),(187,25),(221,25)]:
    test(a1,N)
