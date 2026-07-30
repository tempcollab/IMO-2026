"""For a_1=15, dig into large-only candidates in window that miss exactly 1 past term.
Identify which past term is missed and what large primes of m hit the others.
"""
import math
from sympy import factorint
from collections import defaultdict

def primes_of(n): return set(factorint(n).keys())
def rad(n):
    r=1
    for p in primes_of(n): r*=p
    return r

def greedy_sequence(a1, N):
    a=[a1]
    while len(a)<N:
        cur=a[-1]; m=cur+1
        while True:
            if all(math.gcd(m,ai)>1 for ai in a):
                a.append(m); break
            m+=1
    return a

a1=15; N=120
R=rad(a1)
a=greedy_sequence(a1,N)
print(f"a1={a1} R={R} N={N}")
print(f"first 20 terms: {a[:20]}")
print(f"terms 20-40: {a[20:40]}")

# Which a_i carry large primes?
large_in_a=[]
for i,ai in enumerate(a):
    ps=primes_of(ai)
    large=[p for p in ps if p>R]
    if large:
        large_in_a.append((i+1,ai,large))
print(f"\n#terms carrying a large prime: {len(large_in_a)} / {N}")
print(f"first 25: {large_in_a[:25]}")

# For each n, large-only m in window missing exactly 1
near_miss=[]
for n in range(len(a)-1):
    an=a[n]
    for m in range(an+1, an+R+1):
        ps=primes_of(m)
        if any(p<=R for p in ps): continue
        missed=[(i+1,a[i]) for i in range(n+1) if math.gcd(m,a[i])==1]
        if len(missed)==1:
            hit_primes_per_ai=[]
            for i in range(n+1):
                if math.gcd(m,a[i])>1:
                    qs=sorted([p for p in ps if a[i]%p==0])
                    hit_primes_per_ai.append((i+1,a[i],qs))
            near_miss.append((n,m,an,missed[0],hit_primes_per_ai))

print(f"\n#near-miss (miss exactly 1) large-only m: {len(near_miss)}")
for nm in near_miss[:15]:
    n,m,an,(mi,mai),hits = nm
    print(f"  n={n} m={m} an={an} missed=({mi},{mai}) primes(m)={sorted(primes_of(m))}")
    # show which large prime of m hits each past term
    prime_to_terms=defaultdict(list)
    for i,ai,qs in hits:
        for q in qs:
            prime_to_terms[q].append(i)
    for q,idxs in sorted(prime_to_terms.items()):
        print(f"      q={q} hits {len(idxs)} terms: {idxs[:8]}{'...' if len(idxs)>8 else ''}")
