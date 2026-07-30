## Status
partial

## Approaches tried
- (round 1, new) Finite-state / sliding-window pigeonhole route, deliberately avoiding any characterization of the compatible set E_∞. Framing set up; forward-propagation gap identified.
- (round 1, build) **Major advance.** Closed all the cheap facts rigorously and, crucially, turned the vague "finite state" idea into a *precise, fully-proved reduction*: the whole problem is equivalent to the existence of **one finite set of primes R** (a "sufficient set"), and I prove in full that a finite sufficient R forces a_{n+T}=a_n+L **for every n** (this closes the reviewer's G2 — the forward-propagation / determinism step — completely, conditional only on finiteness). The finite state is `x mod ∏R`. Remaining gap G1 is isolated to a single bounded statement: *no prime exceeding the largest prime factor of a_1 is relevant* (i.e. R₀ = {primes ≤ maxfactor(a_1)} is sufficient), verified computationally on 25+ seeds with **zero** counterexamples. Correctly note the earlier "R ⊆ P∪{2,3}" guess is FALSE (a_1=99 recruits 5).

## Current best
A complete, rigorous reduction of IMO 2026 P6 to a single finiteness statement, plus a full proof of the "for every n" conclusion from that statement. Explicitly:

1. Every term shares a prime with a_1; all terms are pairwise non-coprime; hence every term lies in the compatible set E_∞ = {x ≥ 1 : gcd(x, a_i) > 1 for all i}. **[proved]**
2. Bounded gaps: a_{n+1} − a_n ≤ a_1 for all n. **[proved]**
3. a_1·ℤ_{≥1} ⊆ E_∞ ⊆ ⋃_{p ∈ P} pℤ, where P = primes(a_1). **[proved]**
4. The sequence is exactly the increasing enumeration of E_∞ ∩ [a_1, ∞). **[proved]**
5. **Enumeration Lemma:** if E_∞ is *tail-periodic from a_1* (∃ L: for all x ≥ a_1, x ∈ E_∞ ⟺ x+L ∈ E_∞), then a_{n+T} = a_n + L for **every** n, with T = #(E_∞ ∩ [a_1, a_1+L)). **[proved]**
6. **Finite-State Reduction (closes G2):** if some **finite** set of primes R is *sufficient* (Def. below), then E_∞ is tail-periodic from a_1 with L = ∏R, so by (5) the conclusion holds for every n. The finite "state" is the residue x mod ∏R; the next-term rule is a deterministic function of that finite state. **[proved]**

**Open gap (G1, the genuine crux of P6):** existence of a finite sufficient R. Reduced to the clean bounded statement **R₀ = {primes ≤ maxfactor(a_1)} is sufficient** — i.e. no prime larger than the largest prime factor of a_1 is ever needed to certify eligibility. Verified with no counterexample on all tested seeds. Mechanism identified (large primes are overridden by accumulating small-prime covering constraints) but not yet a proof.

## Target
Prove there exist T, L with a_{n+T} = a_n + L for every positive integer n.

## Technique (spine)
Reduce eligibility to a **finite-state** description: identify a finite prime alphabet R so that membership in the eventual compatible set depends only on `x mod ∏R`; then the greedy rule becomes a deterministic finite-state process whose output is exactly periodic, giving the recurrence from n=1. This route never enumerates E_∞ by a covering predicate; it isolates the crux as a single finiteness fact and proves everything else in full.

## Notation and standing definitions
- P := set of primes dividing a_1 (finite; every p ∈ P satisfies p ≤ a_1).
- For a term a_i, S_i := set of primes dividing a_i. "x hits a set S of primes" means gcd(x, ∏S) > 1, i.e. some prime of S divides x.
- E_n := {x ≥ 1 : gcd(x, a_i) > 1 for all i ≤ n} = {x : x hits S_i for all i ≤ n}. These decrease: E_1 ⊇ E_2 ⊇ ⋯.
- E_∞ := ⋂_n E_n = {x ≥ 1 : gcd(x, a_i) > 1 for all i} = {x : x hits every S_i}.
- By definition of the sequence, for n ≥ 1: a_{n+1} = min( E_n ∩ (a_n, ∞) ).

---

## Full proof of everything except the single finiteness gap G1

### Lemma 1 (all terms are compatible; each shares a prime with a_1).
For all i, j: gcd(a_i, a_j) > 1. Consequently every term lies in E_∞, and every term shares a prime with a_1.

*Proof.* If i = j then gcd(a_i, a_i) = a_i > 1. If i < j, then a_j = a_{(j−1)+1} was chosen by the rule to satisfy gcd(a_j, a_k) > 1 for every k ≤ j−1; taking k = i (valid since i ≤ j−1) gives gcd(a_i, a_j) > 1. By symmetry the case i > j is the same. Thus any two terms are non-coprime. Fixing a term a_j: gcd(a_j, a_i) > 1 for all i, i.e. a_j hits every S_i, i.e. a_j ∈ E_∞. Taking i = 1 gives gcd(a_j, a_1) > 1, so a_j shares a prime with a_1, i.e. S_j ∩ P ≠ ∅. ∎

### Lemma 2 (bounded gaps). For every n, a_{n+1} − a_n ≤ a_1.
*Proof.* Let M be the least multiple of a_1 that exceeds a_n; since consecutive multiples of a_1 differ by a_1, M ≤ a_n + a_1. I claim M is an eligible candidate at step n, i.e. gcd(M, a_i) > 1 for all i ≤ n. By Lemma 1, a_i shares a prime p ∈ P with a_1; then p | a_1 | M and p | a_i, so gcd(M, a_i) ≥ p > 1. Hence M ∈ E_n ∩ (a_n, ∞). Since a_{n+1} is the least element of E_n ∩ (a_n, ∞), a_{n+1} ≤ M ≤ a_n + a_1. ∎

### Lemma 3 (envelopes). a_1·ℤ_{≥1} ⊆ E_∞ ⊆ ⋃_{p ∈ P} pℤ.
*Proof.* (Lower) Let x = c·a_1, c ≥ 1. For any i, a_i shares a prime p ∈ P with a_1 (Lemma 1); then p | a_1 | x and p | a_i, so gcd(x, a_i) ≥ p > 1. Hence x hits every S_i, so x ∈ E_∞.
(Upper) If x ∈ E_∞ then gcd(x, a_1) > 1, so some prime p | gcd(x, a_1); this p ∈ P divides x, so x ∈ pℤ. ∎

In particular E_∞ ⊇ {a_1, 2a_1, 3a_1, …} is infinite, and (with Lemma 2) the elements of E_∞ that are ≥ a_1 have consecutive gaps ≤ a_1.

### Lemma 4 (the sequence enumerates E_∞). {a_n : n ≥ 1} = E_∞ ∩ [a_1, ∞), and a_n is the n-th smallest element of E_∞ that is ≥ a_1.
*Proof.* By Lemma 1 every a_n ∈ E_∞, and a_1 < a_2 < ⋯ so a_n ≥ a_1; thus {a_n} ⊆ E_∞ ∩ [a_1, ∞). Conversely suppose y ∈ E_∞ with y ≥ a_1 but y ∉ {a_n}. Since a_1 is a term, y ≠ a_1, so y > a_1; since the terms strictly increase to ∞, there is a (unique) n with a_n < y < a_{n+1}. Now E_∞ ⊆ E_n (fewer constraints), so y ∈ E_n, i.e. y is eligible at step n, and a_n < y. But a_{n+1} = min(E_n ∩ (a_n, ∞)) ≤ y < a_{n+1}, a contradiction. Hence no element of E_∞ ∩ [a_1, ∞) is omitted, giving equality; the terms increase, so a_n is the n-th smallest. ∎

Lemma 4 is the key structural fact: it removes all dependence on the *order* in which constraints were imposed. The sequence is completely determined by the static set E_∞, and the recurrence a_{n+T} = a_n + L is now a statement purely about the arithmetic of E_∞.

### Lemma 5 (Enumeration Lemma — periodic set ⇒ recurrence for every n).
Suppose there is a positive integer L such that, for all integers x ≥ a_1,
  x ∈ E_∞ ⟺ x + L ∈ E_∞.   (†)
Let T := #( E_∞ ∩ [a_1, a_1 + L) ). Then T ≥ 1 and a_{n+T} = a_n + L for every n ≥ 1.

*Proof.* Write the increasing enumeration of E_∞ ∩ [a_1, ∞) as e_1 < e_2 < ⋯; by Lemma 4, e_n = a_n. Since a_1 ∈ E_∞ (Lemma 1), (†) gives a_1 + kL ∈ E_∞ for all k ≥ 0, so E_∞ ∩ [a_1, ∞) is nonempty in every window [a_1 + kL, a_1 + (k+1)L); thus T ≥ 1.

The map φ : x ↦ x + L restricts to a strictly-increasing bijection
  φ : E_∞ ∩ [a_1, ∞) → E_∞ ∩ [a_1 + L, ∞).
Indeed φ is injective and increasing; it lands in E_∞ ∩ [a_1+L, ∞) by (†) (x ≥ a_1, x ∈ E_∞ ⇒ x+L ∈ E_∞ and x+L ≥ a_1+L); and it is surjective onto that set because if z ∈ E_∞ with z ≥ a_1 + L, then z − L ≥ a_1 and, by (†), z − L ∈ E_∞, so z = φ(z − L).

Now the elements of E_∞ ∩ [a_1, ∞) that are < a_1 + L are exactly e_1, …, e_T (there are T of them, by definition of T, and they are the smallest T since [a_1, a_1+L) is an initial segment). Hence the elements that are ≥ a_1 + L are exactly e_{T+1}, e_{T+2}, …, i.e.
  E_∞ ∩ [a_1 + L, ∞) = {e_{T+1}, e_{T+2}, …}.
On the other hand, by the bijection above, E_∞ ∩ [a_1 + L, ∞) = φ(E_∞ ∩ [a_1, ∞)) = {e_1 + L, e_2 + L, …}. Both listings are strictly increasing enumerations of the same set, so they agree term by term:
  e_{T+i} = e_i + L for every i ≥ 1,
that is, a_{n+T} = a_n + L for every n ≥ 1. ∎

Lemma 5 reduces the entire problem to establishing the tail-periodicity (†). We now show (†) follows from a single finiteness statement.

### Definition (sufficient prime set — the finite state).
For a set of primes R, define the predicate on integers
  E_R(x) : "for every i, x hits S_i ∩ R"  ( equivalently, for every term a_i, some prime of R dividing a_i also divides x ).
Because divisibility of x by a fixed prime p depends only on x mod p, E_R(x) depends only on x mod ∏_{p∈R} p. Call R **sufficient** if, for all x ≥ a_1,
  x ∈ E_∞ ⟺ E_R(x).

Two remarks. (a) One direction is automatic and requires no hypothesis: since S_i ∩ R ⊆ S_i, "x hits S_i ∩ R" implies "x hits S_i"; hence E_R(x) ⟹ x ∈ E_∞ for **every** x. So sufficiency is really the assertion of the reverse implication for x ≥ a_1: every large compatible x can already be certified using only primes in R. (b) Sufficiency is monotone upward: if R is sufficient and R ⊆ R′, then R′ is sufficient (E_R(x) ⟹ E_{R′}(x) ⟹ x ∈ E_∞ ⟹ E_R(x) ⟹ E_{R′}(x)).

### Lemma 6 (Finite-State Reduction — closes G2).
If there exists a **finite** sufficient set of primes R, then (†) holds with L = ∏_{p∈R} p, and therefore a_{n+T} = a_n + L for every n.

*Proof.* Let L = ∏_{p∈R} p (finite since R is finite). Take any x ≥ a_1; then x + L ≥ a_1 as well. Because E_R depends only on the residue modulo ∏_{p∈R} p = L, and x ≡ x + L (mod L), we have E_R(x) = E_R(x + L). Using sufficiency at both x and x + L (both ≥ a_1):
  x ∈ E_∞ ⟺ E_R(x) ⟺ E_R(x + L) ⟺ x + L ∈ E_∞.
This is exactly (†). By Lemma 5, a_{n+T} = a_n + L for every n, with T = #(E_∞ ∩ [a_1, a_1 + L)). ∎

**Finite-state interpretation.** With a finite sufficient R fixed, define the *state* of position x ≥ a_1 to be σ(x) := x mod L ∈ ℤ/Lℤ (a finite alphabet of size L). Lemma 6 shows membership x ∈ E_∞ is a function of σ(x) alone, so the greedy rule "a_{n+1} = next element of E_∞ above a_n" is a **deterministic finite-state map**: from state σ(a_n) it advances to the nearest residue class in E_∞, and the gap a_{n+1} − a_n is a function of σ(a_n) only. The state sequence σ(a_1), σ(a_2), … lives in a finite set and its update is deterministic, so it is eventually periodic; and because E_∞ is a *union of complete residue classes mod L* (each class is entirely in or out of E_∞ by Lemma 6), the period is exact from n = 1. This is the finite-state-window mechanism the outline sought, now rigorous — the unbounded-memory objection is dissolved because Lemma 4 shows the entire history collapses to the static set E_∞, and sufficiency shows E_∞ is governed by the finite residue L.

---

## The remaining gap G1 (isolated, bounded, and the true crux of P6)

Everything above is complete. The single remaining step is:

> **(G1) There exists a finite sufficient set of primes R.**

I reduce G1 further to a clean bounded statement and record the mechanism and evidence.

### Reduction of G1 to a bounded statement.
Let R₀ := {primes p : p ≤ maxfactor(a_1)}, where maxfactor(a_1) is the largest prime factor of a_1. This set is finite. **Claim (G1′): R₀ is sufficient.** Equivalently: *no prime exceeding maxfactor(a_1) is ever needed to certify eligibility of a large integer* — whenever x ≥ a_1 hits every S_i, it already hits every S_i using only primes ≤ maxfactor(a_1). By upward monotonicity of sufficiency (remark (b)), G1′ ⇒ G1. Note R₀ contains P (all primes of a_1 are ≤ maxfactor(a_1)).

**Why this is the right target.** For every seed a_1 tested (25+ values, including 15, 35, 45, 55, 65, 77, 91, 95, 99, 105, 143, 165, and all semiprimes p·q with p<q up to 13·17), the true minimal sufficient set R (= the primes dividing the observed period L) satisfies max(R) ≤ maxfactor(a_1) with **no exception**. This *disproves the earlier guess R ⊆ P ∪ {2,3}* (e.g. a_1 = 99 = 3²·11 recruits the prime 5: R = {2,3,5,11}), which is why the finiteness must be argued through the bound maxfactor(a_1), not through a fixed small list.

### Mechanism (heuristic, not yet a proof).
Fix a prime q > maxfactor(a_1) and suppose, for contradiction, some x ≥ a_1 lies in E_∞ but hits some term a_i only through q (i.e. q ∈ S_i, q | x, and x is divisible by no prime of S_i ∩ R₀; in particular by no prime of S_i ∩ P). The mechanism to exploit is:

- By Lemma 3, x is divisible by some p ∈ P; but that p need not lie in S_i, so no immediate contradiction.
- The terms accumulate constraints. Concretely, the multiples of a_1 are all terms (Lemma 3), and more generally the term set is syndetic (gaps ≤ a_1). As the sequence proceeds, the family {S_i} contains, for the "winning" small prime(s), constraints of the form {p, q_1}, {p, q_2}, … with the q_j ranging over an infinite set of primes (each new term p·q_j of the winning class contributes one). Any x not divisible by the winning small prime p must then hit each {p, q_j} through q_j, i.e. be divisible by all q_j — impossible for x with finitely many prime factors. This is the exact phenomenon by which, e.g., a_1 = 33 forces E_∞ = 3ℤ and a_1 = 55 forces E_∞ = 5ℤ (verified): large-prime witnesses are overridden.

Turning this into a proof requires showing the winning small prime(s) really do generate an infinite family of constraints that pins down E_∞ modulo R₀ — this is where the argument becomes genuinely global and is not yet closed. It is the same finiteness crux that the two E_∞-based rival approaches face; here it is packaged as "R₀ sufficient," a single bounded number-theoretic statement.

### Honest status of G1.
Not proved. It is neither hand-waved nor assumed in any completed step above: Lemmas 1–6 are unconditional except that the final conclusion (†)⇒recurrence is invoked only through the hypothesis "finite sufficient R exists," which is exactly G1. Everything is rigorous up to this one clearly-marked gap.

## Open gaps
- **G1** (the crux): existence of a finite sufficient prime set R, reduced to the bounded claim **G1′: R₀ = {primes ≤ maxfactor(a_1)} is sufficient** (no prime beyond the largest prime factor of a_1 is relevant). Verified computationally with zero counterexamples; mechanism identified (accumulating small-prime covering constraints override large-prime witnesses); proof not completed.

## Cases to cover
- Within G1′: (i) primes q > maxfactor(a_1) are never needed; (ii) the winning small-prime class generates an infinite pinning family. Both currently open.

## Promotable lemmas
- **Lemma 1** (all terms pairwise non-coprime; every term ∈ E_∞; every term shares a prime with a_1). Fully proved above.
- **Lemma 2** (bounded gaps a_{n+1} − a_n ≤ a_1). Fully proved above.
- **Lemma 3** (envelopes a_1·ℤ_{≥1} ⊆ E_∞ ⊆ ⋃_{p∈P} pℤ). Fully proved above.
- **Lemma 4** (the sequence is exactly the increasing enumeration of E_∞ ∩ [a_1, ∞); removes all order/history dependence). Fully proved above.
- **Lemma 5** (Enumeration Lemma: tail-periodicity of E_∞ from a_1 with period L ⇒ a_{n+T} = a_n + L for **every** n, T = #(E_∞ ∩ [a_1, a_1+L))). Fully proved above — this is the mechanism delivering the "for every n" (not merely eventual) conclusion, reusable by any approach.
- **Lemma 6** (Finite-State Reduction: a finite sufficient prime set R ⇒ tail-periodicity with L = ∏R ⇒ conclusion for every n). Fully proved above — closes the forward-propagation/determinism step (G2) conditional on finiteness, reusable by every approach that establishes a finite relevant-prime set.
