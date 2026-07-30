"""Analyze large-only candidates in the window.
For each n, for each m in (a_n, a_n+R] with sigma(m)=empty (all primes>R):
  - check if m in A_n (shares a prime with every past a_i)
  - if not in A_n: which a_i does m miss? (the obstruction)
  - if in A_n: this would violate (C); record.
Also: for large primes q>R that divide some past a_i, tabulate inter-arrival gaps.
"""
import math
from sympy import factorint

def primes_of(n):
    return set(factorint(n).keys())
def rad(n):
    r=1
    for p in primes_of(n): r*=p
    return r
def small_support(n,R):
    return {p for p in primes_of(n) if p<=R}

def greedy_sequence(a1, N):
    a=[a1]
    while len(a)<N:
        cur=a[-1]; m=cur+1
        while True:
            if all(math.gcd(m,ai)>1 for ai in a):
                a.append(m); break
            m+=1
    return a

def analyze(a1, N):
    R=rad(a1)
    a=greedy_sequence(a1,N)
    print(f"\n=== a1={a1} R={R} N={N} ===")
    # For each n, enumerate large-only m in window
    large_only_total=0
    large_only_inA=0  # would be a (C) violation
    miss_pattern={}  # number of past terms missed -> count
    for n in range(len(a)-1):
        an=a[n]
        for m in range(an+1, an+R+1):
            ps=primes_of(m)
            if any(p<=R for p in ps):
                continue  # has a small prime, not large-only
            # large-only candidate
            large_only_total+=1
            # which past terms does m hit?
            missed=[i+1 for i,ai in enumerate(a[:n+1]) if math.gcd(m,ai)==1]
            if not missed:
                large_only_inA+=1
                print(f"  (C) VIOLATION n={n} m={m} an={an}")
            else:
                k=len(missed)
                miss_pattern[k]=miss_pattern.get(k,0)+1
    print(f"  large_only_total={large_only_total} inA(violations)={large_only_inA}")
    print(f"  miss_pattern(#missed -> count): {dict(sorted(miss_pattern.items()))}")
    return a

def large_prime_structure(a1, N):
    """For each large prime q>R dividing some a_i, list its appearances and inter-arrival gaps."""
    R=rad(a1)
    a=greedy_sequence(a1,N)
    from collections import defaultdict
    appearances=defaultdict(list)
    for i,ai in enumerate(a):
        for p in primes_of(ai):
            if p>R:
                appearances[p].append(i+1)
    # tabulate
    recurrences=[(p,idxs) for p,idxs in appearances.items()]
    recurrences.sort(key=lambda x: -len(x[1]))  # by frequency
    print(f"\n--- a1={a1} R={R}: large primes dividing some a_i (i<=N) ---")
    print(f"  #distinct large primes = {len(appearances)}")
    print(f"  top 12 by frequency:")
    for p,idxs in recurrences[:12]:
        gaps=[idxs[k+1]-idxs[k] for k in range(len(idxs)-1)]
        gmin=min(gaps) if gaps else None
        gmax=max(gaps) if gaps else None
        print(f"    q={p} freq={len(idxs)} indices(first5)={idxs[:5]} gaps(min,max)=({gmin},{gmax})")
    # inter-arrival distribution
    all_gaps=[]
    for p,idxs in appearances.items():
        for k in range(len(idxs)-1):
            all_gaps.append(idxs[k+1]-idxs[k])
    if all_gaps:
        from collections import Counter
        c=Counter(all_gaps)
        print(f"  inter-arrival gap distribution (top): {dict(c.most_common(8))}")
        print(f"  min gap={min(all_gaps)} max gap={max(all_gaps)}")
    return appearances

if __name__=="__main__":
    for a1,N in [(15,80),(35,80),(77,80),(91,80),(105,60),(175,60),(385,60)]:
        analyze(a1,N)
        large_prime_structure(a1,N)
