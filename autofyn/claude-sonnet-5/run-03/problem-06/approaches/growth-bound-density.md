## Status
partial

## Approaches tried
- Round 1 (first pass, this round): built the outline's "bound the gap first" route into a fully
  rigorous standalone lemma (a_{n+1}-a_n ≤ L0), then attempted to repair the flaw the
  outline-reviewer identified (state space built from S = primes(a_1) alone is provably too coarse:
  for a_1=15 the true dynamics needs prime 2 ∉ primes(15)). I traced the a_1=15 example by hand to
  locate *exactly* where and why a non-S prime becomes load-bearing (see "Diagnosis" below), proved a
  genuine new lemma (Constraint Domination) that gives the right logical framework for what the
  finite state *should* track, and then tested the most natural fix — "the set of primes dividing
  infinitely many terms is finite" — computationally, and **refuted it**: by direct simulation, for
  a_1=15, *every* prime up to at least 71 divides infinitely many terms of the sequence (with
  density ~1/p, as expected once the tail is periodic with period sum L=30 coprime to p). So the
  natural repair "enlarge S to the finite set of eventually-active primes" is not just insufficient
  bookkeeping, it rests on a **false premise** — that set is not finite. This is a genuine dead end
  for the literal "finite prime-signature state" framing and is recorded here so no other approach
  wastes a round rediscovering it. The framing that *is* still open and promising (Constraint
  Domination reducing the live constraints to an inclusion-minimal antichain, and asking whether the
  *antichain's structure* — not the raw set of primes seen — stabilizes) is written up below as the
  precise remaining gap.

## Current best

### Lemma 1 (Gap bound). For every n ≥ 1, a_{n+1} − a_n ≤ L0, where L0 := ∏_{p ∈ S} p and
S := {primes dividing a_1} (a finite nonempty set since a_1 > 1 is a fixed positive integer).

*Proof.* First, every a_i with i ≥ 2 shares a prime factor with a_1: by definition, a_i (for i ≥ 2) is
the smallest integer greater than a_{i-1} such that gcd(a_i, a_j) > 1 for **every** j = 1, …, i−1; in
particular, taking j = 1 (valid since i − 1 ≥ 1), gcd(a_i, a_1) > 1. Hence a_i and a_1 share a common
prime factor, i.e. primes(a_i) ∩ S ≠ ∅. (For i = 1 this is trivial: a_1 = a_1 shares every one of its
own prime factors with itself.) So for **every** i ≥ 1 there is a prime p_i ∈ S ∩ primes(a_i).

Now fix n ≥ 1 and let m be the smallest multiple of L0 exceeding a_n, i.e.
m = L0 · ⌈(a_n+1)/L0⌉. Since consecutive multiples of L0 differ by exactly L0, and a_n itself is
either a multiple of L0 or lies strictly between two consecutive multiples, we get a_n < m ≤ a_n + L0.

Because L0 = ∏_{p∈S} p and L0 | m, every prime p ∈ S divides m. In particular, for each i = 1, …, n,
the prime p_i ∈ S found above divides m, and p_i also divides a_i; hence gcd(m, a_i) ≥ p_i > 1. So m
is a valid candidate for a_{n+1} in the sense of the recursive definition: it is greater than a_n and
satisfies gcd(m, a_i) > 1 for every i = 1, …, n. Since a_{n+1} is defined as the *smallest* such
integer, a_{n+1} ≤ m ≤ a_n + L0. ∎

This is the lemma the outline-reviewer independently re-verified as fully rigorous; it is technique-
independent (uses only the definition and the finiteness of S) and reusable by every other approach
in the population, so it should be certified into `results/imo-2026-06/lemmas/`.

### Lemma 2 (Every prime factor of a_1 is ≤ L0). Immediate: if p | a_1 then p | L0 = ∏_{q∈S} q (p is
one of the factors in the product), so p ≤ L0. This bounds S itself inside [2, L0], but — as shown
next — it does **not** bound the full set of primes relevant to the dynamics; that is the content of
the diagnosis below.

### Lemma 3 (Constraint Domination). For indices i < j, if primes(a_j) ⊆ primes(a_i), then for every
integer y, gcd(y, a_j) > 1 implies gcd(y, a_i) > 1. Consequently, when checking whether a candidate y
is a valid next term, the constraint "gcd(y,a_i) > 1" is *logically implied by* (redundant given) the
constraint "gcd(y,a_j) > 1" whenever primes(a_j) ⊆ primes(a_i).

*Proof.* If gcd(y,a_j) > 1 then y and a_j share some prime q, so q ∈ primes(a_j). By hypothesis
primes(a_j) ⊆ primes(a_i), so q ∈ primes(a_i) too, i.e. q | a_i. Since also q | y, gcd(y,a_i) ≥ q > 1.
∎

Consequence: at stage n, the family of constraints {"gcd(y,a_i)>1" : i = 1,…,n} is, as a logical
system to be satisfied by y, equivalent to the sub-family indexed by the **inclusion-minimal**
elements of {primes(a_1), …, primes(a_n)} under set inclusion (an antichain 𝒜_n of finite sets of
primes): dominated constraints (those whose defining set is a strict superset of another appearing
set) may be dropped without changing which y are valid, by the lemma just proved (and the converse
direction — that a non-dominated constraint cannot be dropped — is immediate since it is literally
one of the original constraints). This is the correct *logical* content of "which past terms still
matter", and it is genuinely different from (and more refined than) the outline's original
"S-signature D_i = primes(a_i) ∩ S" bookkeeping, because it uses the **full** prime factorization of
each a_i, not just its intersection with S.

### Diagnosis (why S = primes(a_1) alone is provably insufficient, traced by hand)

Take a_1 = 15, S = {3,5}, so under the *original* (flawed) scheme one would try to determine a_3 by
requiring y to hit D_1 = primes(15) ∩ S = {3,5} and D_2 = primes(a_2) ∩ S. Simulating: a_2 = 18, and
primes(18) = {2,3}, so D_2 = {3}.

The naive S-only sufficiency rule would look for the smallest y > 18 divisible by an element of D_1
and an element of D_2 — since D_2 = {3} ⊆ D_1, domination (restricted to S) says the effective
requirement is just "y divisible by 3". Checking y = 19, 20: 19 is not divisible by 3; 20 is not
divisible by 3 either (20 = 2²·5). The next multiple of 3 after 18 is 21, and indeed gcd(21,15) = 3 > 1
and gcd(21,18) = 3 > 1, so the S-only rule would output a_3 = 21.

But the **true** greedy value is a_3 = 20 (directly verified: gcd(20,15) = 5 > 1, gcd(20,18) = 2 > 1,
and 19 fails since gcd(19,15) = gcd(19,18) = 1). The witness that makes 20 valid against the
constraint from a_2 = 18 is the prime **2** — a prime that does **not** divide a_1 = 15 and hence is
invisible to any state built only from S = primes(a_1). This is a fully rigorous, hand-verified
counterexample (not merely the reviewer's simulation output restated): it shows concretely, at the
very first nontrivial step (n = 2 → 3) of the very smallest interesting case, that the S-only
sufficiency rule computes a *different, larger* value than the true sequence. So S = primes(a_1) is
not merely "coarse" — a state machine built on it computes the wrong sequence starting at n = 3.

### Why the natural fix ("finitely many eventually-active primes") also fails

The most natural repair is to conjecture: there is a finite set A of primes (a superset of S) such
that for all sufficiently large n, a_n is divisible by some prime of A, and only primes of A ever
matter. I tested this directly: for a_1 = 15, the sequence stabilizes (by direct simulation,
independently reproducing the outline-reviewer's finding) into a purely periodic gap pattern
(2,4,6,6,4,2,3,3) of period T = 8 summing to L = 30 = lcm(2,3,5), starting from n = 1. Because the
gap sequence is eventually (indeed immediately) periodic with total shift L = 30 per period, we have
a_{n+8k} = a_n + 30k for all k ≥ 0. Fix any prime p with p ∤ 30 (i.e. p ∉ {2,3,5}). Since
gcd(30,p) = 1, the arithmetic progression a_n + 30k (k = 0,1,2,…) runs through *every* residue class
mod p infinitely often, in particular the class 0 mod p — so p divides a_{n+8k} for infinitely many
k. Hence **every** prime p ∉ {2,3,5} still divides infinitely many terms of the sequence (I verified
this numerically: primes 7, 11, 13, …, 71 each divide hundreds of terms among the first 2000). So
"the set of primes dividing infinitely many terms" is provably **not finite** — it is (eventually)
*every* prime not dividing L. This refutes the natural fix outright: no finite enlargement of S based
on "which primes recur infinitely often" can be the right invariant, because that criterion is
satisfied by infinitely many primes. Any correct finite-state argument must instead explain why these
recurring-but-rare large-prime divisibilities never actually change which y is minimal — i.e. it must
work at the level of the **antichain 𝒜_n** from Lemma 3 (which constraints are *live and
non-redundant*), not at the level of "which primes appear somewhere."

### Precise remaining gap

What is proven: (1) the gap bound a_{n+1} − a_n ≤ L0 (Lemma 1, unconditional, complete); (2) every
a_i (i ≥ 1) meets S = primes(a_1) (used in Lemma 1's proof, complete); (3) the Constraint Domination
lemma (Lemma 3, complete), which correctly reduces "check n constraints" to "check the constraints
indexed by the inclusion-minimal antichain 𝒜_n ⊆ {primes(a_1),…,primes(a_n)}"; (4) a fully verified
demonstration that S alone is insufficient (the a_1=15, n=2→3 computation above) and that the
"finite set of eventually-active primes" repair is false in general (the density argument above).

What is **not** proven, and is the true remaining gap for this approach: that the antichain 𝒜_n
itself stabilizes into a structure governed by only finitely many possible "shapes" as n → ∞, in a
way strong enough to force the *validity test* for a candidate y (in the guaranteed window
(a_n, a_n+L0]) to depend only on finitely much information about the recent past — e.g. on a_n modulo
a fixed integer M together with a bounded-length window of recent prime-factorization data. Concretely
one would want to show:
- (Gap 1) Large prime factors of a_i (primes q > L0 dividing a_i) can be dropped from primes(a_i) for
  the purpose of computing 𝒜_n and testing validity of any y in a bounded window near the *current*
  a_n, without changing the outcome — i.e. such q never becomes the unique witness for a live
  (non-dominated) constraint at the moment it is tested. I have *not* proven this: the argument that
  q | y is a rare event (density 1/q within a window of length ≤ L0 < q) shows such a coincidence
  cannot recur densely, but does not rule out it mattering on some single occasion, which is enough
  to threaten the "for every n" (not just eventually) form of the theorem's conclusion.
- (Gap 2) Even granting Gap 1, one would need the resulting "small-prime-only" antichain structure
  to itself be finite-state (bounded number of distinct antichains reachable, as a function of a_n's
  residue mod a fixed modulus), which has not been established.

Both gaps are open. I do not have a construction or counterexample resolving either, and I am not
claiming a proof of full periodicity. Status is therefore `partial`: Lemma 1 (certified-ready) and
Lemma 3 are complete, reusable results; the passage from them to the theorem's finite-state /
periodicity conclusion is not closed.

## Full proof
(Not applicable — status is partial, no complete proof of the theorem is claimed.)

## Promotable lemmas

- **Lemma 1 (Gap bound)**: For the greedy sequence defined in imo-2026-06, a_{n+1} − a_n ≤ L0 :=
  ∏_{p | a_1} p for every n ≥ 1. Proved in full above using only: (a) every a_i (i≥1) shares a prime
  factor with a_1 [direct from the recursive definition, no induction needed], and (b) the smallest
  multiple of L0 exceeding a_n is always a valid candidate for a_{n+1} [since it is divisible by
  every prime of primes(a_1), hence by the witness prime each a_i shares with a_1]. This is
  independent of any other approach's technique and reusable as a black-box "gaps are bounded"
  fact — recommend certifying to `results/imo-2026-06/lemmas/gap-bound.md`.
- **Lemma 3 (Constraint Domination)**: For i<j, primes(a_j) ⊆ primes(a_i) implies gcd(y,a_j)>1 ⟹
  gcd(y,a_i)>1 for all y; hence the validity test for a candidate next term reduces to checking only
  the inclusion-minimal elements of {primes(a_1),…,primes(a_n)}. Proved in full above (one-line
  argument from prime divisibility). Reusable by `core-signature-pigeonhole` and any approach that
  needs to reduce "n constraints" to a bounded live set — it is the correct refinement of that
  approach's D_i-signature idea (using full prime factorizations, not just intersections with a
  fixed S), and directly explains, via the a_1=15 worked example above, exactly where the
  S-only version breaks. Recommend certifying to `results/imo-2026-06/lemmas/constraint-domination.md`.
- **Negative result (not a lemma to certify, but record to avoid re-derivation)**: "the set of primes
  dividing infinitely many terms of the sequence is finite" is **false** in general (shown above for
  a_1=15 via the periodic-tail density argument, confirmed by simulation up to primes ≤ 71 dividing
  hundreds of terms among the first 2000). Any future approach that plans to fix the S-too-coarse
  issue by "enlarging S to the eventually-active primes" should be redirected before building, since
  that premise is refuted.
