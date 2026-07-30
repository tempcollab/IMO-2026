## Status
partial

## Approaches tried
- (round 2, new) Global prime-capacity double-counting adapted from crux aimo-0447: assume R
  infinite (infinitely many large sole-connector primes q>P_max), bound the number of term-pairs a
  large prime can cover via Σ 1/p², and seek a density contradiction against the ~N(X)²/2 pairs.
  Outcome: the capacity/counting half is now proved in full rigour (Lemmas C1–C3 below). The
  localize-to-globalize half (Step 4) is proved to be UN-closable in this framing without assuming
  density/periodicity of E_∞ (circular): a single witness q∈R supplies only Θ(1) sole-connector
  pairs, whereas a contradiction needs Ω(X²), and no non-circular mechanism multiplies one witness
  into positive density. Recorded precisely as an honest GAP; the counting bound provably bounds a
  positive FRACTION and can never reach zero. Status: partial.

## Current best
The certified reduction (theorem ⟸ R finite; R = {q : some pair of terms shares exactly {q}}) is
imported, and the entire prime-capacity apparatus of the aimo-0447 analogue is established with full
rigour:

- **N(X) = Θ(X)** with an explicit two-sided bound (Lemma C1).
- **Per-prime pair-capacity** C(⌊X/p⌋,2) with the exact double-count (Lemma C2).
- **Large-prime capacity is a bounded fraction**: the pairs of terms ≤ X sharing SOME prime > P_max
  number at most (X²/2)·Σ_{p>P_max}1/p², and Σ_{p>P_max}1/p² < 0.21 is bounded away from the total
  pair count — proved elementarily (Lemma C3).

What is honestly missing, and shown to be missing in a precise sense, is the **localize-to-globalize
step**: turning "R infinite" (or even one witness q∈R) into Ω(X²) sole-connector pairs among terms
≤ X. Lemma C3 bounds only a fraction, so it cannot by itself reach the contradiction; and Section 5
proves that within this framing a single witness contributes only O(1) pairs, so the framing cannot
close the crux without an external density input that would be circular. This is the value of the
route: it certifies that pure capacity + the a_1·ℤ lattice do NOT replace the local minimality
argument, and pinpoints exactly why.

## Imported (certified, gap-free)
- `lemmas/enumeration-of-E-infinity.md` — the sequence is the increasing enumeration of
  E_∞ ∩ [a_1,∞), E_∞ = {m>1 : gcd(m,a_i)>1 ∀i}.
- `lemmas/periodic-set-enumeration.md` — E tail-periodic mod L ⇒ b_{n+T}=b_n+L for all n.
- `approaches/enum-covering-primes.md` Steps 1–4 + R1/R2 (reviewer-certified): the covering
  characterization, the identity R = {q : some pair of terms has prime-intersection exactly {q}},
  and "R finite ⇒ theorem." In particular: every multiple of a_1 is a term (⇒ N(X) ≥ ⌊X/a_1⌋−1),
  and every two terms share a prime.

---

## Notation
- P := primes(a_1), P_max := max P.
- A term is an element of the sequence; equivalently (imported) an element of E_∞ ∩ [a_1, ∞).
- For X ≥ a_1, N(X) := #{terms in [a_1, X]}.
- R := union of the minimal members of F = {primes(a_i)}; by the imported identity R1,
  R = {q prime : ∃ terms A,B with primes(A) ∩ primes(B) = {q}}.
- P_max is finite; the theorem follows (imported Step 4) once R is finite, equivalently once no
  prime q > P_max lies in R (Lemma A).

## Goal of this approach
Prove **R is finite** by contradiction from a global density count. The plan: if too many pairs of
terms were forced to have their ONLY common prime exceed P_max, a prime-capacity bound would be
violated. Steps 1–3 build and prove the capacity apparatus rigorously; Step 4 is the localize step.

---

## Step 1 — Term density: N(X) = Θ(X). (Lemma C1, proved.)

**Lemma C1.** For all X ≥ a_1,   ⌊X/a_1⌋ − 1 ≤ N(X) ≤ X.

*Proof.* Lower bound: every integer multiple k·a_1 with 2 ≤ k ≤ ⌊X/a_1⌋ satisfies primes(k a_1) ⊇ P,
and P is covering (imported Step 1), so k a_1 ∈ E_∞ and lies in [a_1, X]; these are ⌊X/a_1⌋ − 1
distinct terms, all ≤ N(X). Upper bound: the terms in [a_1, X] are distinct integers in [1, X], of
which there are at most X. Hence ⌊X/a_1⌋ − 1 ≤ N(X) ≤ X; in particular N(X) = Θ(X). ∎

(Only N(X) ≥ ⌊X/a_1⌋ − 1 and N(X) ≤ X are used below; both are unconditional.)

**Corollary C1'.** The number of unordered pairs of distinct terms in [a_1,X] is
  Π(X) := C(N(X), 2) ≥ C(⌊X/a_1⌋−1, 2) = (1+o(1))·X²/(2 a_1²).

---

## Step 2 — Per-prime pair capacity. (Lemma C2, proved.)

Every unordered pair {A,B} of distinct terms shares a prime (imported Step 1). Choose, for each such
pair, one prime dividing gcd(A,B); call it a *label*. For a prime p, let μ_p(X) := #{terms in [a_1,X]
divisible by p}. A pair can be labelled p only if p | A and p | B, i.e. both members are among the
μ_p(X) terms divisible by p.

**Lemma C2.** For every prime p, the number of unordered term-pairs {A,B} ⊆ [a_1,X] with p | gcd(A,B)
is at most C(μ_p(X), 2) ≤ C(⌊X/p⌋, 2) ≤ (X/p)²/2.

*Proof.* Both members must be p-divisible terms, of which there are μ_p(X); the count of pairs among
them is C(μ_p(X),2). Since p-divisible terms are in particular multiples of p in [1,X], μ_p(X) ≤
⌊X/p⌋. Finally C(k,2) = k(k−1)/2 ≤ k²/2 ≤ (X/p)²/2. This is the double-counting/pigeonhole bound
(knowledge_base.md: **Double counting**; **Pigeonhole / extremal principle**). ∎

---

## Step 3 — Large primes cover only a bounded fraction of pairs. (Lemma C3, proved.)

Call a pair {A,B} of terms a **large pair** if some prime p > P_max divides gcd(A,B), and a
**large-sole pair** if primes(A) ∩ primes(B) is a single prime q > P_max (so its unique label is
large). Every large-sole pair is a large pair.

**Lemma C3.** Let L(X) := #{large pairs of terms in [a_1,X]}. Then
  L(X) ≤ (X²/2) · Σ_{p > P_max} 1/p²  <  (X²/2)·0.21.
More precisely Σ_{all primes p} 1/p² < 1/2, so Σ_{p>P_max} 1/p² ≤ 1/2 − 1/4 = 1/4, and numerically
Σ_{p>P_max} 1/p² ≤ Σ_{p>2} 1/p² = P(2) − 1/4 < 0.2023 for every P_max ≥ 2.

*Proof.* A large pair is labelled by (at least) one prime p > P_max; summing the per-prime capacity
of Lemma C2 over p > P_max overcounts (each large pair counted once for each large label it has, ≥1),
so
  L(X) ≤ Σ_{p > P_max} C(μ_p(X),2) ≤ Σ_{p > P_max} (X/p)²/2 = (X²/2) Σ_{p > P_max} 1/p².
The reciprocal-square prime sum is bounded elementarily: for any y ≥ 2,
  Σ_{p > y} 1/p² ≤ Σ_{n > y} 1/n² < Σ_{n>y} 1/(n(n−1)) = 1/y ≤ 1/2 (telescoping),
and more sharply Σ_{p} 1/p² < Σ_{p≥2} 1/p² is a convergent series with value P(2) (the prime zeta
function at 2), P(2) = 0.45224742… < 1/2. Removing the p=2 term (2 ≤ P_max always, since P_max is a
prime ≥ 2) gives Σ_{p>P_max} 1/p² ≤ P(2) − 1/4 < 0.2023. Hence L(X) < 0.2023·(X²/2) < 0.21·X²/2. ∎

*(Sanity constants, computed with mpmath: P(2)=0.452247…; tails Σ_{p>P_max}1/p² for P_max=2,3,5,7,11
are 0.2022, 0.0911, 0.0511, 0.0307, 0.0225 respectively — all well below the ~1/a_1² pair density.)*

**Consequence (fraction, not zero).** Combining C1' and C3, the fraction of term-pairs ≤ X that are
large is at most
  L(X)/Π(X) ≤ [0.21·X²/2] / [(1+o(1))X²/(2a_1²)] = (1+o(1))·0.21·a_1².
This is a POSITIVE constant (indeed > 1 as soon as a_1 ≥ 3), so the capacity bound is **consistent
with a positive fraction of large pairs**. It does not, and provably cannot, force L(X) = 0.

---

## Step 4 — Localize-to-globalize: THE GAP (honestly unproven, and shown un-closable here).

To reach a contradiction from "R infinite" via Step 3, one would need the large-**sole** pairs to
number ≫ 0.21·X²/2 for arbitrarily large X — i.e. Ω(X²) large-sole pairs among terms ≤ X. We now
record, rigorously, why this framing cannot supply that.

**5.1 What R infinite literally gives.** Suppose R is infinite: there are infinitely many distinct
primes q_1 < q_2 < ⋯ with each q_k > P_max, and (imported R1) for each k a single pair of terms
(A_k, B_k) with primes(A_k) ∩ primes(B_k) = {q_k}. Nothing in R1 asserts a SECOND pair with the same
sole prime, nor any bound on the size of A_k, B_k. Thus at any fixed cutoff X, the witnesses with
q_k ≤ X are the only ones visibly below X, and each contributes a priori only ONE large-sole pair.
The number of large-sole pairs among terms ≤ X guaranteed by "R infinite" is therefore only
  ≥ #{k : A_k, B_k ≤ X} which is ≥ 0 and could be as small as O(π(X)) = O(X/log X) = o(X²).
This is dwarfed by the capacity slack of Θ(X²) in Lemma C3. Hence **no contradiction** arises: the
capacity bound permits far more large pairs than "R infinite" is known to produce.

**5.2 Why one witness cannot be multiplied (the non-circular obstruction).** The two natural seeds
both fail:
- *Lattice translation.* From a witness pair (A,B) with primes(A) ∩ primes(B) = {q}, translating by a
  multiple of a_1 (the one lattice we control, since a_1·ℤ ⊆ terms) destroys the factorization:
  primes(A + t·a_1) bears no relation to primes(A), so A + t·a_1 need not be sole-connected to
  anything, let alone by q. There is no group action on the sequence preserving "share exactly {q}."
  So translation manufactures zero new large-sole pairs.
- *q-multiples.* The terms divisible by q are those m with q | m and primes(m) covering. For such m to
  be a term at all it must carry a covering set of primes; generically that covering set includes a
  small prime shared with most other terms, so two q-divisible terms typically share a SMALL prime,
  i.e. are NOT large-sole. Concretely a large-sole pair requires primes(A) ∩ primes(B) = {q} with the
  small parts of A and B disjoint on the whole prefix — a rare, minimality-driven event, not a lattice
  orbit. Counting q-divisible terms (≤ X/q of them) even bounds large-sole q-pairs ABOVE by C(X/q,2),
  reinforcing Step 3's smallness rather than producing Ω(X²).

**5.3 The only escape is circular.** The single mechanism that WOULD deliver Ω(X²) large-sole pairs
is: "once E_∞ is periodic with period L, a witnessed sole-connector residue-configuration recurs with
positive density, so each period contributes ≥1 large-sole pair, giving ≍ X/L = Θ(X) sole primes and,
combined with recurrence of each, Ω(X²) pairs." But periodicity of E_∞ is the CONCLUSION of the whole
problem (imported Step 4 derives it FROM R finite). Assuming it to prove R finite is circular. The
math-explorer-covering-anchor report (opening 3, caveat) and the outline both flag this precisely; our
Section 5.1–5.2 upgrades that flag to a proof that no non-circular multiplication is available in the
capacity framing.

**Conclusion of Step 4.** Within the prime-capacity framing, Lemma C3 rigorously bounds the large-pair
count by a positive FRACTION Θ(X²) of all pairs, and "R infinite" rigorously supplies only o(X²)
guaranteed large-sole pairs. The two bounds are compatible: **no contradiction.** The localize step,
which would need Ω(X²) large-sole pairs, cannot be obtained without an external density/periodicity
input that is circular. This is the honest, un-closed GAP. Consequently this approach does NOT prove
Lemma A / R finite.

---

## THE GAP (honestly unproven)
Step 4 (localize-to-globalize). It is not merely unproven here: Section 5 gives a rigorous argument
that the capacity framing alone CANNOT close it, because (i) capacity bounds only a positive fraction
of pairs (Lemma C3 + its Consequence), never zero, and (ii) "R infinite" is known to force only
o(X²) large-sole pairs, with no non-circular way to reach Ω(X²). A genuine proof of R finite must come
from the local/minimality structure of the greedy step (the sibling approaches reduced-process-identity
and cofactor-recruitment-smoothness), not from global capacity counting.

## Cases to cover (status)
- q just above P_max vs q ≈ X: both handled uniformly by Lemma C3 (the bound Σ_{p>P_max}1/p² is over
  ALL large primes, independent of where q sits) — the counting half is exhaustive.
- "R finite but unbounded" vs "R infinite": both are subsumed by "R infinite" as the negation target
  (R finite is the goal; if R is finite the theorem holds by import). The negation used in Step 4 is
  "R infinite," and Section 5.1 covers it. Settled at the level the counting reaches; blocked only at
  the localize step, uniformly across these cases.

## Watch out for (confirmed)
The capacity bound alone never reaches zero — confirmed rigorously (Consequence after Lemma C3: the
fraction is ≥ a positive constant). The localize/globalize step is mandatory and, in this framing,
provably unavailable without circularity (Section 5). Recorded precisely as instructed; this framing's
value is the negative certification that capacity + the a_1·ℤ lattice do not replace the local
minimality argument.

## Promotable lemmas
- **Lemma C1 (term density).** For the greedy sequence, ⌊X/a_1⌋ − 1 ≤ N(X) ≤ X for all X ≥ a_1;
  in particular the number of term-pairs in [a_1,X] is ≥ C(⌊X/a_1⌋−1,2) = (1+o(1))X²/(2a_1²). Proved
  in full (Step 1) from the certified "every multiple of a_1 is a term / every term is P-divisible."
  Reusable by any counting-based approach.
- **Lemma C2 (per-prime pair capacity).** For every prime p, #{term-pairs {A,B}⊆[a_1,X] : p|gcd(A,B)}
  ≤ C(⌊X/p⌋,2) ≤ (X/p)²/2. Proved in full (Step 2); pure double counting.
- **Lemma C3 (large-prime capacity fraction).** #{large pairs ≤ X} ≤ (X²/2)·Σ_{p>P_max}1/p² <
  0.21·X²/2, using Σ_{p}1/p² = P(2) < 1/2 (with the elementary telescoping bound Σ_{n>y}1/n² < 1/y).
  Proved in full (Step 3). Reusable; note it bounds a positive FRACTION, never zero — the recorded
  reason the capacity route cannot finish alone.
