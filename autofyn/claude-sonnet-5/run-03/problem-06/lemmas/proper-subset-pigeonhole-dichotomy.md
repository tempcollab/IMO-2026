## Status
certified (round 6, proof-reviewer)

## Source
`approaches/gcd-pigeonhole-omega-induction.md` (round 6, Item 2). Reviewer re-derived: trivial
finite pigeonhole, no gap.

## Statement
Let (a_n) be the greedy sequence with S:=primes(a_1), |S|>=2. Then either:
(I) a_1 | a_n for all sufficiently large n, or
(II) there is a nonempty proper subset R_0⊊S such that primes(gcd(a_1,a_n))=R_0 for infinitely
many n.

## Proof
For n>=2, gcd(a_1,a_n)>1 (forced by the recursion's constraint at i=1), so
R_n:=primes(gcd(a_1,a_n)) is a nonempty subset of S. If R_n=S for all sufficiently large n, (I)
holds. Otherwise R_n≠S for infinitely many n; since there are finitely many (2^|S|-1) proper
subsets of S, pigeonhole on this infinite index set gives a fixed R_0⊊S with R_n=R_0 for
infinitely many n, i.e. (II). The two cases are exhaustive and mutually stated correctly (I is the
negation's failure case for infinitude, II is the pigeonhole consequence when I fails). ∎

## Note
This lemma alone does not yield a workable "reduction" to a smaller-ω recursion (see the source
file's Item 4 for a documented negative finding on that direction) — it is a standalone fact,
reusable but not part of any completed reduction chain. Not needed by the now-complete proof in
`lemmas/global-signature-purification.md` / `current.md`.
