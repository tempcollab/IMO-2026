"""For each m in window NOT in B_n (sigma(m) misses some class sigma*), and m HAS
at least one large prime: does every sigma*-term get hit by a large prime of m?
Since (C) has 0 violations, some sigma*-term must escape. Find the escape pattern.
"""
import math
from sympy import factorint
from collections import defaultdict
import sys
sys.path.insert(0,'/tmp/round-3')
from probe_c import minimal_hitting_sets, small_support, primes_of, rad, greedy_sequence, in_B_using_mh

def sigma_classes(a_list, n, R):
    """Return list of (sigma_frozenset, [indices i+1 with that sigma]) for i in 0..n."""
    classes=defaultdict(list)
    for i in range(n+1):
        s=frozenset(small_support(a_list[i],R))
        classes[s].append(i+1)
    return classes

def probe(a1, N, show=15):
    R=rad(a1)
    a=greedy_sequence(a1,N)
    print(f"\n=== a1={a1} R={R} N={N} ===")
    # collect m not in B_n with at least one large prime, missing some class
    interesting=[]
    for n in range(len(a)-1):
        an=a[n]
        classes=sigma_classes(a,n,R)
        Mn=minimal_hitting_sets(list(classes.keys()))
        for m in range(an+1, an+R+1):
            if in_B_using_mh(m,Mn): continue
            ps=primes_of(m)
            large=[p for p in ps if p>R]
            if not large: continue
            # m has large primes, not in B_n. Find the sigma* classes missed by sigma(m).
            sm={p for p in ps if p<=R}
            missed_classes=[sig for sig in classes if not (sm & sig)]
            for sig in missed_classes:
                idxs=classes[sig]
                # which sigma*-terms does m hit via large primes?
                hit_via_large=[j for j in idxs if any(a[j-1]%q==0 for q in large)]
                escape=[j for j in idxs if j not in hit_via_large]
                interesting.append((n,m,an,set(sig),idxs,large,escape,hit_via_large))
    print(f"  #interesting (m not in B, has large prime, misses a class): {len(interesting)}")
    # distribution of escape sizes
    from collections import Counter
    esc_sizes=Counter(len(e) for *_,e,_ in interesting) if interesting else Counter()
    hit_sizes=Counter(len(h) for *_,_,h in interesting) if interesting else Counter()
    print(f"  escape size distribution: {dict(esc_sizes)}")
    # show those with smallest escape
    interesting.sort(key=lambda t: (len(t[6]), t[0]))
    for entry in interesting[:show]:
        n,m,an,sig,idxs,large,escape,hitvia=entry
        print(f"  n={n} m={m} an={an} sigma*={set(sig)} #class={len(idxs)} large_primes(m)={sorted(large)} #escape={len(escape)} escape_idxs={escape[:6]} hit_idxs={hitvia[:6]}")
    return interesting

for a1,N in [(15,80),(35,60),(77,45),(91,45),(105,35),(175,35),(385,25)]:
    probe(a1,N)
