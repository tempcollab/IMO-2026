"""Dig into a_1=135: how does the all-small term for class {2,3} arrive?
The first term 138=2*3*23 has a large prime. When does an all-small {2,3} term appear?
Also test the proof idea: can we prove W by induction on classes?
"""
import math
from sympy import factorint
from collections import defaultdict
import sys
sys.path.insert(0,'/tmp/round-3')
from probe_c import small_support, primes_of, rad, greedy_sequence

a1=135; N=60
R=rad(a1)
a=greedy_sequence(a1,N)
print(f"a1={a1} R={R} (note R=rad(135)=15, since 135=3^3*5)")
print(f"first 30 terms: {a[:30]}")
# classes
classes=defaultdict(list)
for i,ai in enumerate(a):
    sig=frozenset(small_support(ai,R))
    classes[sig].append((i+1,ai))
print(f"\n#classes={len(classes)}")
for sig,terms in sorted(classes.items(), key=lambda x: x[1][0][0]):
    allsmall=[(idx,ai) for idx,ai in terms if all(p<=R for p in primes_of(ai))]
    print(f"  sig={set(sig)} first={terms[0]} first_smooth={all( p<=R for p in primes_of(terms[0][1]))} allsmall_terms={allsmall[:4]}")

# For the class {2,3} born at 138: when does all-small arrive?
sig23=frozenset({2,3})
print(f"\nclass {{2,3}} terms: {classes[sig23]}")
print(f"  all-small {2,3}-terms: {[(i,ai) for i,ai in classes[sig23] if all(p<=R for p in primes_of(ai))]}")
