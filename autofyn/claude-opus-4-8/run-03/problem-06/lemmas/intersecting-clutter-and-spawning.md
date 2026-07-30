# Lemmas (Intersecting clutter; essential witnesses; large-prime spawning)

**Certified** (proof-reviewer, round 9). Source: `minimal-cover-small-only` Lemmas A, B, C
(= `covering-small-part-descent` Lemma 12 for the spawning clause; cross-checked, certified once).
Structural facts about the self-dual covering clutter ℰ obtained by the value (realizability) method.

Notation as in `csp-iff-E-small-only.md`. Uses certified `realizability-and-self-dual-clutter.md`
(Lemma 1 = 𝒞=𝒯 + clause (c); Lemma 2 = a prime set meets every edge ⟺ it is covering).

## Lemma A (intersecting clutter)
(i) Every covering set meets every edge of ℰ. (ii) Any two edges meet: C,C'∈ℰ ⟹ C∩C'≠∅. (iii) Every
edge meets P=primes(a_1); in particular every edge contains a small prime.
*Proof.* (i) is the forward direction of certified Lemma 2. (ii) Each edge is covering, apply (i). (iii)
P=primes(a_1)∈𝒯=𝒞 is covering, apply (i); P⊆[2,P_max]. ∎

## Lemma B (essential witnesses)
For any edge C∈ℰ and any r∈C there is a term B_r with primes(B_r)∩C={r}.
*Proof.* C minimal ⟹ C∖{r} non-covering ⟹ some term B_r has primes(B_r)∩(C∖{r})=∅. C covering ⟹
primes(B_r)∩C≠∅, and this shared prime lies in C∖(C∖{r})={r}. ∎

## Lemma C (large-prime spawning)
If an edge C∈ℰ contains a large prime q, then, with B_q its essential witness (Lemma B): (1) C∩[2,P_max]
is non-empty and non-covering; (2) B_q is a bad term; (3) q is essential in primes(B_q)
(primes(B_q)∖{q} non-covering); (4) there is an edge C'∈ℰ with C'≠C and C∩C'={q} (so q∈C').
*Proof.* Write C_s:=C∩[2,P_max], so q∉C_s. (1) C_s⊇C∩P≠∅ (Lemma A(iii)); if C_s covering it is a proper
covering subset of C (q∈C∖C_s), contradicting minimality. (2) primes(B_q) covering; S(B_q)∩C=∅ (since
primes(B_q)∩C={q}, q large); if S(B_q) covering it meets C (Lemma A(i)), contradiction; so B_q bad. (3)
if primes(B_q)∖{q} covering it meets C (Lemma A(i)), but (primes(B_q)∖{q})∩C⊆{q}∖{q}=∅, contradiction.
(4) primes(B_q) covering ⟹ contains an edge C'; C'∩C⊆primes(B_q)∩C={q} and C'∩C≠∅ (Lemma A(ii)) ⟹
C'∩C={q}; C'≠C since C'∩C_s⊆primes(B_q)∩C_s=∅ while C_s≠∅. ∎

## Reusability / scope
A minimal cover with a large prime never occurs in isolation: it forces a distinct edge sharing exactly
its large prime (Lemma C(4)). The partner map C↦C' is **horizontal** (q∈C', same large prime), so it
yields NO strictly-decreasing quantity on the large-prime data (max large prime, |Q_C|, ∏Q_C, min/max
large prime are all non-decreased). Certified as reusable structure + a recorded obstruction to
transversal monovariants; it does NOT close the crux. Gap-free.
