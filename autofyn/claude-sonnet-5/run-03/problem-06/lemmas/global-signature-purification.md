## Status
certified (round 6, proof-reviewer)

## Source
`approaches/global-signature-purification.md` (round 6). Reviewer independently re-derived every
step and computationally checked all four pieces below (Correspondence: a_1 in 2..60, range
a_1+250; Purification: 16553 random trials; Signature Determinacy: a_1 in 2..60 range a_1+250,
plus a_1 in {15015,45045}; Periodic-Enumeration: hand-verified bijection argument, and numerically
confirmed T,L for a_1=9 (T=70,L=210) and a_1=15 (T=8008,L=30030, partial window)). No gap found.
This lemma set constitutes, together, a **complete independent proof of the whole theorem**
(imo-2026-06), for every a_1>=2 — see `current.md` Full proof.

## Statement

Fix k:=a_1>=2. A prime p is **small** if p<=k, **big** if p>k. For x>=k, π(x):={p prime<=k : p|x}
(the small-prime signature). Two integers x,x'>=k are **similar** if π(x)=π(x').

Define good:{k,k+1,...}->{T,F} by well-founded recursion: good(x) := [every m with k<=m<x and
gcd(m,x)=1 satisfies good(m)=False]. (good(k)=True vacuously.) Call x good/bad accordingly.

1. **Correspondence Lemma.** For the greedy sequence (a_n) of the problem (a_1=k), {x>=k : x good}
   = {a_1,a_2,a_3,...}.
2. **Purification Lemma.** If b>=k has a small prime factor, there exists x with k<=x<=b,
   π(x)=π(b), and x k-smooth (every prime factor of x is <=k).
3. **Signature Determinacy Theorem.** If a,b>=k are similar (π(a)=π(b)), then good(a)=good(b).
4. **Periodic-Enumeration Lemma.** If G⊆Z_{>=k} satisfies x∈G ⟺ x+L∈G for all x>=k (fixed L>=1),
   and G is infinite with increasing enumeration a_1<a_2<..., then with T:=#(G∩[k,k+L)),
   a_{n+T}=a_n+L for every n>=1.

## Proofs
See `approaches/global-signature-purification.md`, Sections 0-4, verified line by line by the
reviewer (round 6); all four proofs reproduced independently by the reviewer and found correct,
with no circularity (Theorem A's minimal-counterexample induction on max(a,b) uses only Fact 1 and
the Purification Lemma, never its own conclusion for a smaller pair before it is established).
