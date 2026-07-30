"""Probe conjecture (C) for IMO 2026 P6.

(C): A_n ∩ (a_n, a_n+R] ⊆ B_n  for every n.
Equivalently: every m in the window with gcd(m,a_i)>1 for all i<=n is divisible
by some product-of-minimal-hitting-set m_h (small-prime-admissible).
"""
import math
from functools import lru_cache
from sympy import factorint

def primes_of(n):
    return set(factorint(n).keys())

def rad(n):
    r = 1
    for p in primes_of(n):
        r *= p
    return r

def small_support(n, R):
    """sigma(a_i) = supp(a_i) ∩ P_R, P_R = {primes p <= R}."""
    return {p for p in primes_of(n) if p <= R}

def minimal_hitting_sets(family):
    """Compute minimal hitting sets of a family of sets of small primes.
    family: list of sets; each set is subset of P_R.
    Returns list of frozensets, each minimal under inclusion, hitting every member.
    Brute force over subsets of the union (P_R is small: |P_R| ~ pi(R))."""
    if not family:
        return []  # no rows -> no hitting sets? define as empty family
    universe = sorted(set().union(*family))
    # We need minimal hitting sets. Brute force over subsets by increasing size.
    # universe size is small (e.g. for R=210, pi(210)=46). 2^46 too big.
    # Use a smarter incremental approach: start from each row pick one element -> hitting sets,
    # then minimize. Actually the standard way: greedy enumeration via the "transversal" recursion.
    # Use the recursive Berge algorithm for minimal transversals.
    family = [set(s) for s in family]
    # Berge-style: handle one element at a time.
    # We'll do: MHS(family) computed by recursion on |family|.
    # Simpler: since universe small in practice for our R (R=15 -> {2,3,5,7,11,13}, |U|=6),
    # brute force 2^|U| is fine. For R up to ~385, pi(385)=77, 2^77 too big.
    # Use the Berge algorithm.
    return _mhs_berge(family, universe)

def _mhs_berge(family, universe):
    """Berge algorithm for minimal transversals. family: list of sets."""
    # Start: no constraints -> one hitting set: the empty set? No, hitting set of empty family is {} (trivially).
    # Actually hitting set of empty family = any set; minimal = {}.
    if not family:
        return [frozenset()]
    # Process: we maintain a set of candidate minimal transversals incrementally.
    # Standard algorithm: T = { {} }; for each edge e in family:
    #   newT = []
    #   for tau in T:
    #     if tau ∩ e != empty: keep tau (still hits e)
    #     else: tau misses e -> branch: for x in e, tau ∪ {x}; add. Then minimize.
    #   then minimize newT (remove supersets) and add tau's that still hit.
    T = [frozenset()]
    for edge in family:
        newT = []
        for tau in T:
            if tau & edge:
                newT.append(tau)
            else:
                for x in edge:
                    cand = tau | {x}
                    # keep minimal later; just add
                    newT.append(cand)
        # minimize: remove any set that is a superset of another
        newT = _minimize(newT)
        T = newT
    return T

def _minimize(cands):
    """Remove supersets."""
    cands = [frozenset(c) for c in cands]
    # sort by size ascending
    cands.sort(key=lambda s: len(s))
    result = []
    for c in cands:
        if any(r <= c for r in result):
            continue
        result.append(c)
    return result

def m_h(h):
    r = 1
    for p in h:
        r *= p
    return r

def in_B(m, M_n):
    """m in B_n iff m_h | m for some h in M_n."""
    for h in M_n:
        if all(p_divides(p, m) for p in h):
            return True
    return False

def p_divides(p, m):
    return m % p == 0

def greedy_sequence(a1, N):
    """Compute a_1..a_N."""
    a = [a1]
    for n in range(1, N):
        cur = a[-1]
        m = cur + 1
        while True:
            ok = all(math.gcd(m, ai) > 1 for ai in a[:n+1]) if False else None
            # check admissibility
            admissible = True
            for ai in a:
                if math.gcd(m, ai) == 1:
                    admissible = False
                    break
            if admissible:
                a.append(m)
                break
            m += 1
    return a

def compute_Bn(a_list, n, R):
    """Compute M'_n and the small-prime-admissible predicate."""
    sigma_list = [small_support(ai, R) for ai in a_list[:n+1]]
    family = [s for s in sigma_list]  # may have duplicates; MHS of a family with dups = same as dedup
    # dedupe but keep as family
    family_dedup = []
    seen = set()
    for s in family:
        key = frozenset(s)
        if key not in seen:
            seen.add(key)
            family_dedup.append(s)
    Mn = minimal_hitting_sets(family_dedup)
    return Mn

def in_B_using_mh(m, Mn):
    for h in Mn:
        prod = 1
        for p in h:
            prod *= p
        if m % prod == 0:
            return True
    return False

def window_C_violations(a1, N):
    """For each n in 1..N-1, for each m in (a_n, a_n+R], check:
       m in A_n (gcd(m,a_i)>1 for all i<=n) but m NOT in B_n.
       Return violations list."""
    R = rad(a1)
    a = greedy_sequence(a1, N)
    violations = []
    # Precompute M_n incrementally is expensive; recompute each n.
    for n in range(len(a)-1):
        an = a[n]
        Mn = compute_Bn(a, n, R)
        for m in range(an+1, an+R+1):
            inA = True
            for ai in a[:n+1]:
                if math.gcd(m, ai) == 1:
                    inA = False
                    break
            if not inA:
                continue
            inB = in_B_using_mh(m, Mn)
            if not inB:
                violations.append((n, m, an))
    return a, violations

if __name__ == "__main__":
    import sys
    for a1 in [15, 35, 45, 77, 91, 105, 135, 175, 187, 221, 385]:
        N = 40 if a1 in (187, 221, 385) else 60
        try:
            a, v = window_C_violations(a1, N)
            print(f"a1={a1} R={rad(a1)} N={N} len(a)={len(a)} violations={len(v)} first_viol={v[:3] if v else None}")
        except Exception as e:
            print(f"a1={a1} ERROR {e}")
