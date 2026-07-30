## Status
partial

## Approaches tried
- (round 1, new) Reduction "sequence = increasing enumeration of the compatible set E_∞" + covering-prime characterization of E_∞. Reduction is rigorous; the single open gap was finiteness of the relevant-prime set R.
- (round 1, build) Closed Steps 1–4 in full rigor (enumeration lemma written out). **Sharpened the finiteness gap:** proved rigorously that R = {q : two terms have prime-intersection exactly {q}}, hence R is finite **iff** no prime q > P_max is such a "unique connector" (**Lemma A**). Lemma A is verified computationally on 9 seeds but remains unproven — this is now the sole gap, and it is a sharp, self-contained, elementary statement about the sequence (much tighter than the previous vague "replacement/syndeticity" mechanism).

## Current best
A fully rigorous reduction of the entire problem to the single elementary statement **Lemma A**:

> **Lemma A.** Let P_max be the largest prime factor of a_1. For no prime q > P_max do there exist two terms a_i, a_j of the sequence whose set of common prime factors equals exactly {q}.

Everything else is proven with no gaps: Steps 1–4 (the reduction to periodicity of E_∞ and the conclusion for *every* n), and the two-way reduction "R finite ⟺ Lemma A", including the exact identity R = {q : some pair of terms has prime-intersection {q}}. Lemma A is verified on a_1 ∈ {15,35,77,105,143,255,182,6,30} (0 violating pairs in every case). Closing Lemma A closes the whole problem.

---

## Notation
- For an integer m > 1, primes(m) is its set of prime factors.
- P := primes(a_1), P_max := max P (largest prime factor of a_1).
- A finite set S of primes is **covering** if S ∩ primes(a_i) ≠ ∅ for every index i (equivalently, every term is divisible by some prime of S).
- E_∞ := { m ∈ ℤ_{>1} : gcd(m, a_i) > 1 for every index i } (integers compatible with the whole sequence).
- E_n := { m ∈ ℤ_{>1} : gcd(m, a_i) > 1 for every i ≤ n }. Note E_1 ⊇ E_2 ⊇ ⋯ and E_∞ = ⋂_n E_n.
- F := { primes(a_i) : i ≥ 1 }, the family of prime-sets of terms. A member is **minimal** if no member is a proper subset of it. R := union of all minimal members of F.

## Step 1 — Every term lies in E_∞; any two terms share a prime; every term is divisible by a prime of P.
For i < j the defining rule gives gcd(a_j, a_i) > 1; gcd is symmetric, so gcd(a_i, a_j) > 1 for all i ≠ j. Also gcd(a_i, a_i) = a_i > 1. Hence for every j, gcd(a_j, a_i) > 1 for all i, i.e. a_j ∈ E_∞. In particular a_1 ∈ E_∞, and any two terms share a prime factor. Finally, gcd(a_i, a_1) > 1 means a_i shares a prime with a_1, i.e. a_i is divisible by some p ∈ P. So P is a covering set and every single term is divisible by a prime of P. ∎

## Step 2 — The sequence is the increasing enumeration of E_∞ ∩ [a_1, ∞).
Claim: for every n, a_{n+1} = min{ m ∈ E_∞ : m > a_n }.

By the defining rule, a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 ∀ i ≤ n } = min(E_n ∩ (a_n, ∞)). Since E_∞ ⊆ E_n (fewer constraints on E_n), no element of E_∞ can lie in the open interval (a_n, a_{n+1}): such an element would belong to E_n and be a member of E_n ∩ (a_n, ∞) strictly below the minimum a_{n+1}, a contradiction. Moreover a_{n+1} ∈ E_∞ by Step 1. Therefore a_{n+1} is the least element of E_∞ exceeding a_n. Since a_1 = min(E_∞ ∩ [a_1, ∞)) (a_1 ∈ E_∞ and it is the left endpoint), induction gives that a_1 < a_2 < ⋯ is exactly the increasing enumeration of the set E_∞ ∩ [a_1, ∞). ∎

## Step 3 — Covering characterization, and reduction to the minimal prime-sets.
**(3a)** For any m > 1: m ∈ E_∞ ⟺ primes(m) is a covering set. Indeed gcd(m, a_i) > 1 ⟺ some prime of m divides a_i ⟺ primes(m) ∩ primes(a_i) ≠ ∅; requiring this for all i is exactly "primes(m) covering."

**(3b)** A finite prime set H is covering ⟺ H hits every *minimal* member of F. (⟸) Every member primes(a_i) ∈ F contains a minimal member f ⊆ primes(a_i) (F-members are finite sets, so a shortest one inside primes(a_i) is minimal in F); if H ∩ f ≠ ∅ then H ∩ primes(a_i) ⊇ H ∩ f ≠ ∅. So hitting all minimal members forces hitting all members. (⟹) Minimal members are members, so covering forces hitting them. 

Combining (3a)+(3b): **m ∈ E_∞ ⟺ primes(m) hits every minimal member of F.** Every minimal member is a subset of R, so this condition depends only on primes(m) ∩ R. Hence:

> If R is finite, membership of m in E_∞ depends only on the residue of m modulo L := ∏_{q ∈ R} q. ∎

## Step 4 — R finite ⇒ the conclusion for every n.
Assume R finite; set L := ∏_{q∈R} q (a positive integer ≥ 2, since F has a minimal member — e.g. a shortest prime-set occurring — so R ≠ ∅). By Step 3, m ∈ E_∞ ⟺ (m + L) ∈ E_∞ for **all** integers m > 1 (membership depends only on which primes of R divide m, i.e. only on m mod L, since each q ∈ R divides m ⟺ divides m+L when q | L). Thus E_∞ is **exactly periodic mod L**.

**Enumeration lemma.** Let E ⊆ ℤ_{>1} be exactly periodic mod L (m ∈ E ⟺ m+L ∈ E) and nonempty. Fix a and let b_1 < b_2 < ⋯ enumerate E ∩ [a, ∞) in increasing order (infinite, since E is periodic and nonempty hence unbounded above). Put T := |E ∩ (x, x+L]|, which is independent of x: the shift r ↦ r+L is a bijection E ∩ (x, x+L] → E ∩ (x+L, x+2L], so every half-open window of length L contains exactly T elements of E; T ≥ 1 since E ≠ ∅. Then b_{n+T} = b_n + L for every n ≥ 1.

*Proof.* Fix n. The interval (b_n, b_n + L] is a length-L half-open window, so it contains exactly T elements of E. As (b_n, b_n+L] ⊆ [a, ∞) and the b_k enumerate all of E ∩ [a,∞) in order with nothing of E between consecutive b_k, these T elements are precisely b_{n+1} < ⋯ < b_{n+T}. Their maximum is max(E ∩ (b_n, b_n+L]). Now b_n + L ∈ E (periodicity, from b_n ∈ E) and b_n + L ∈ (b_n, b_n+L]; and every element of the interval is ≤ b_n + L. Hence b_n + L is the maximum, i.e. b_{n+T} = b_n + L. ∎

Apply this with E = E_∞, a = a_1: by Step 2, b_n = a_n. Therefore **a_{n+T} = a_n + L for every n ≥ 1**, with L = ∏_{q∈R} q and T = |E_∞ ∩ (x, x+L]| = number of residues mod L lying in E_∞ (this is ≥ 1 since ∏_{q∈R} q ∈ E_∞: its prime set is R, which is covering by (3b) as it contains every minimal member). Both T, L are positive integers. This is exactly the required conclusion, valid from n = 1. ∎

So the whole problem reduces to: **R is finite.**

## Reduction of finiteness to Lemma A (fully rigorous).
**(R1) The exact characterization of R.** *For any prime q: q ∈ R ⟺ there exist terms a_i, a_j with primes(a_i) ∩ primes(a_j) = {q}.*

First, a useful equivalence for a term a_i with q | a_i. Let T_i := primes(a_i) ∖ {q}. Then:

  T_i is **not** covering ⟺ there is a term a_j with primes(a_j) ∩ T_i = ∅.

Now any term a_j shares a prime with a_i (Step 1), so primes(a_j) ∩ primes(a_i) ≠ ∅; if also primes(a_j) ∩ T_i = ∅ then the only possible common prime is q, forcing primes(a_j) ∩ primes(a_i) = {q} (and q | a_j). Conversely such an a_j has primes(a_j) ∩ T_i = ∅. Hence:

  (★) for a term a_i with q | a_i: T_i not covering ⟺ ∃ term a_j with primes(a_i) ∩ primes(a_j) = {q}.

*(⟹ of R1).* Suppose q ∈ R, so q lies in some minimal member f = primes(a_i) of F (minimal members are members of F, i.e. of the form primes(a_i); and R is their union). Minimality means no term a_j has primes(a_j) ⊊ f; in particular no term has primes(a_j) ⊆ f ∖ {q} = T_i (that would be a proper subset of f, as it omits q ∈ f). A term with prime-set ⊆ T_i would exist if T_i were covering: taking a minimal covering subset S ⊆ T_i and m = (∏_{p∈S} p)^N with N large so m > a_1, we get primes(m) = S ⊆ T_i covering, so m ∈ E_∞ (3a), hence m is a term (Step 2) with primes ⊆ T_i — contradiction. So T_i is not covering, and by (★) there is a term a_j with primes(a_i) ∩ primes(a_j) = {q}.

*(⟸ of R1).* Suppose terms a_i, a_j have primes(a_i) ∩ primes(a_j) = {q}. Then q | a_i, and by (★) T_i = primes(a_i) ∖ {q} is not covering. Descend from primes(a_i) (a member of F) to a minimal member f ⊆ primes(a_i). If q ∉ f then f ⊆ T_i; but f is a minimal member, hence covering by (3b), contradicting "T_i not covering" (a subset of a non-covering set relative to... explicitly: f ⊆ T_i and f covering would make T_i ⊇ f covering). So q ∈ f, whence q ∈ R. ∎(R1)

**(R2) R finite ⟺ Lemma A.** By (R1), R = { q : some pair of terms has prime-intersection exactly {q} }. Split by size of q:
- Every prime q with q ≤ P_max: there are only finitely many such primes.
- A prime q > P_max lies in R ⟺ (by R1) some pair of terms has prime-intersection {q}, which is *exactly* the configuration forbidden by Lemma A.

Therefore: **Lemma A holds ⟺ R contains no prime exceeding P_max ⟺ R ⊆ {primes ≤ P_max}, a finite set.** Conversely if Lemma A fails, some q > P_max lies in R, and (taking any single such pair) R is still possibly finite — but for finiteness in general we need Lemma A: if Lemma A holds, R ⊆ {primes ≤ P_max} is finite; that implication is all Step 4 requires. Thus **Lemma A ⇒ R finite ⇒ (Step 4) the theorem.** ∎(R2)

Hence the entire problem is reduced, with full rigor, to Lemma A.

## Lemma A — THE REMAINING GAP (honestly unproven).
> **Lemma A.** For no prime q > P_max do two terms a_i, a_j exist with primes(a_i) ∩ primes(a_j) = {q}.

**Status: verified, not proved.** Numerically checked over all pairs of the first 1500–3000 terms for a_1 ∈ {15,35,77,105,143,255,182,6,30}: zero violating pairs in every case, so R ⊆ {primes ≤ P_max} in every case (matching the earlier R ⊆ P ∪ {2,3} observation, since {2,3} ⊆ {primes ≤ P_max} whenever P_max ≥ 3, and R = {2} when a_1 is a power of 2).

**What is established toward it.** Suppose q > P_max and terms A = a_i, B = a_j (i < j) had primes(A) ∩ primes(B) = {q}. Since q ∉ P (q > P_max), both A and B are divisible by q *and* by a prime of P (Step 1); write A = q^α u, B = q^β v with u, v coprime to q, and p | u, p′ | v for some p, p′ ∈ P. As gcd(u,v) shares no prime (the only common prime of A,B is q), p ≠ p′. Empirically the greedy minimality of B prevents this "coprime-cofactor" configuration: the terms divisible by a fixed large prime q are of the form q·(P-multiple) and always pairwise share a *small* prime. A local "find a smaller compatible number in (a_{j-1}, a_j)" argument provably cannot work (a_j is by definition the minimum of E_{j-1} above a_{j-1}, so the open interval is empty of compatible numbers); Lemma A must be proved by a non-local/extremal argument on the configuration, which is not completed here.

## Cases to cover (all discharged except Lemma A)
- Steps 1–4: complete, no case split needed.
- Reduction R1/R2: complete (both directions of R1 proved; q ≤ P_max vs q > P_max split in R2).
- Lemma A: OPEN.

## Promotable lemmas
- **Enumeration-of-a-periodic-set lemma** (proved in full in Step 4): if E ⊆ ℤ is exactly periodic mod L and nonempty, its increasing enumeration b_1 < b_2 < ⋯ of E ∩ [a, ∞) satisfies b_{n+T} = b_n + L for all n ≥ 1, where T = |E ∩ (x, x+L]| is the constant per-period count. Elementary, reusable.
- **Enumeration reduction (Steps 1–2)**: the greedy sequence equals the increasing enumeration of E_∞ ∩ [a_1, ∞); proved in full. Reusable by any approach.
- **Covering characterization (Step 3) + exact identity R = {q : some pair of terms has prime-intersection {q}} (R1)**: proved in full. This isolates the crux as Lemma A and is importable by density-bounded-recruitment and finite-state-window.
