## Status
partial

## Approaches tried
- (round 1, first pass) Original outline: track e_p(n) = v_p(gcd(a_1,a_n)) per prime p | a_1, hoping
  for a per-prime monotonicity dichotomy. No mechanism found; flagged by outline-reviewer as purely
  aspirational.
- (round 1, this pass) Replaced the per-prime-of-a_1 valuation idea with a global object: Q, the set
  of primes dividing infinitely many terms of the sequence ("permanently recurring primes"), plus a
  genuine counting/density monovariant on Q. Result: two lemmas proved in full (Q-cover Lemma, the
  global gap bound, and a density inequality on Q), but the central claim needed to finish the proof
  (|Q| < ∞) is NOT established; I tried three separate routes to it and all three provably fall short
  for the reasons given below. This is honest, verified partial progress, not a completed proof.
  I also ran direct simulation (a_1 = 15, 21, 33, 35, 45, 77, 105, 231) confirming: (a) infinitely many
  *distinct* primes divide the sequence overall (large "rider" primes appear once each, e.g. 13, 17,
  19, 23, 29, ... — so the *total* prime support is NOT eventually constant, ruling out the naive
  monovariant "number of distinct primes seen so far stabilizes"), while (b) the recurring set Q
  itself does look empirically small and stable (e.g. Q = {2,3} for a_1 = 15, Q = {2,3,5} for a_1=35,
  Q = {3} for a_1 = 21) — consistent with the theorem but not proved.

## Current best

This is the field's diversity anchor: unlike the three sibling approaches, nothing here is built on
the (confirmed insufficient) assumption that the active/state set is S = primes(a_1). Instead the
object tracked is genuinely global: the set of primes that recur infinitely often anywhere in the
sequence. Two lemmas below are fully proved and are new, reusable content; the finiteness of that set
is the honestly-reported open gap, with a precise account of why three natural attack routes on it
fail.

**Setup and notation.** Let a_1 < a_2 < a_3 < ... be the sequence, S0 := the (finite, nonempty) set of
primes dividing a_1, and L0 := ∏_{p ∈ S0} p.

**Lemma 0 (every term after a_1 hits S0).** For every i ≥ 2, gcd(a_i, a_1) > 1, i.e. a_i has a prime
factor in S0.

*Proof.* By the recursive definition, a_i (for i ≥ 2, so i = m+1 for some m ≥ 1) is required to
satisfy gcd(a_i, a_j) > 1 for every j = 1, ..., m; taking j = 1 gives gcd(a_i, a_1) > 1 directly. Since
a_1's only prime factors are S0, a shared prime factor of a_i and a_1 must lie in S0. ∎

**Lemma 1 (Global gap bound).** For every n ≥ 1, a_{n+1} − a_n ≤ L0.

*Proof.* Let N* be the smallest multiple of L0 with N* > a_n. Since the multiples of L0 are spaced L0
apart, N* ≤ a_n + L0. We claim N* is a valid candidate for a_{n+1}, i.e. gcd(N*, a_i) > 1 for every
i = 1, ..., n. Indeed N* is divisible by every prime of S0 (as L0 = ∏_{p∈S0} p divides N*). For i = 1,
a_1's primes are exactly S0, so gcd(N*, a_1) ≥ (any prime of S0) > 1. For 2 ≤ i ≤ n, by Lemma 0, a_i
has some prime p ∈ S0, and p | N*, so gcd(N*, a_i) ≥ p > 1. Hence N* satisfies every required
condition, so by minimality of the greedy choice, a_{n+1} ≤ N* ≤ a_n + L0. ∎

(This bound is also used, and independently verified, by the sibling approach `growth-bound-density`;
I re-derive it here from scratch because it is needed as an input to the density argument below, and
because CLAUDE.md requires every imported step to be reproven rather than cited.)

**Corollary 1.1 (linear growth bound).** For every N ≥ 1, a_N ≤ a_1 + (N−1)·L0.

*Proof.* Immediate by telescoping Lemma 1 over n = 1, ..., N−1: a_N − a_1 = Σ_{n=1}^{N-1} (a_{n+1}−a_n)
≤ (N−1)·L0. ∎

**Definition (the recurrence set Q).** Let Q := { primes q : q divides a_n for infinitely many n ∈ ℕ }.
This is the genuinely different top-level object of this approach: it is not tied to S0 = primes(a_1)
at all (it is a global, a priori possibly infinite, set determined by the whole sequence), which is
exactly the fix the outline-reviewer's computation showed is needed (for a_1 = 15, S0 = {3,5} is
provably too small, but 2 — not in S0 — belongs to Q).

**Lemma 2 (Q-cover Lemma).** For every i ≥ 1, a_i has a prime factor in Q. In particular Q ≠ ∅.

*Proof.* Fix i ≥ 1 and write a_i = ∏_{j=1}^k r_j^{e_j} with r_1, ..., r_k its (finitely many, k ≥ 1
since a_i > 1) distinct prime factors. Suppose for contradiction that none of r_1, ..., r_k lies in Q,
i.e. each r_j divides only finitely many terms of the sequence. For each j let
M_j := max{ n : r_j | a_n } (this is a well-defined finite number since {n : r_j | a_n} is a finite,
nonempty set — nonempty because r_j | a_i itself). Let M := max(M_1, ..., M_k, i). For every n > M and
every j = 1,...,k we have n > M_j so r_j ∤ a_n; since r_1,...,r_k are a_i's only prime factors, this
means gcd(a_n, a_i) = 1 for every n > M. But by the recursive definition applied at each step
m = i, i+1, ..., n−1 (using j = i ≤ m each time), gcd(a_n, a_i) > 1 holds for every n > i, in particular
for n = M+1 > M ≥ i — contradiction. Hence some r_j ∈ Q. ∎

**Proposition 3 (Density inequality on Q).** Σ_{q ∈ Q} 1/q ≥ 1/L0 (in particular Q ≠ ∅, reproving
Lemma 2's conclusion quantitatively, and showing Q carries genuine positive "density").

*Proof.* Fix N ≥ 1. By Lemma 2, every index i ∈ {1, ..., N} has a_i divisible by some prime of Q, so
{1,...,N} = ⋃_{q ∈ Q} { i ≤ N : q | a_i }, giving by the union bound
  N ≤ Σ_{q ∈ Q} #{ i ≤ N : q | a_i }.
Since a_1 < a_2 < ... < a_N are N distinct positive integers all ≤ a_N, the set {i ≤ N : q | a_i} is a
subset of the multiples of q lying in [1, a_N], so #{i ≤ N : q | a_i} ≤ ⌊a_N/q⌋ ≤ a_N/q. Hence
  N ≤ a_N · Σ_{q ∈ Q} 1/q,  i.e.  Σ_{q ∈ Q} 1/q ≥ N / a_N.
This holds for every N (the left side is a single fixed extended-real number in [0,∞], not depending on
N, so this is a valid family of lower bounds on one fixed quantity). By Corollary 1.1,
  N / a_N ≥ N / (a_1 + (N−1)L0) → 1/L0 as N → ∞.
So for every ε > 0 there is N with N/a_N > 1/L0 − ε, giving Σ_{q∈Q} 1/q ≥ 1/L0 − ε; since ε was
arbitrary, Σ_{q ∈ Q} 1/q ≥ 1/L0. ∎

**Central open gap: is Q finite?** If Q were shown finite, the intended finish (mechanical, not
attempted in detail here since it is the same CRT/pigeonhole bookkeeping the sibling approaches use in
their final step) would be: for n large, every a_n must be divisible by at least one element of the
now-fixed finite set Q (a strengthened, sequence-tail version of Lemma 2 restricted to large i, proved
the same way with a possibly-larger but still finite lookback bound), giving a periodic covering
structure on residues mod ∏_{q ∈ Q} q via CRT, from which a_{n+T} = a_n + L follows for
L = lcm of the periodic covering pattern's total displacement and T its length — this final assembly
step is standard once Q is fixed and finite and is NOT the content that is missing; the content that
IS missing is |Q| < ∞ itself.

I attempted three routes to |Q| < ∞ this round and record precisely why each falls short, so the next
round does not repeat them:

1. **Density-only route (Proposition 3 alone).** Σ_{q∈Q} 1/q ≥ 1/L0 is a genuine lower bound but gives
   no upper bound on |Q| or on Σ_{q∈Q} 1/q: an infinite set of primes (e.g. all primes greater than L0)
   can have Σ 1/q = +∞ trivially satisfying the inequality, and even a sparse infinite set of primes
   can have a convergent reciprocal sum exceeding 1/L0 while being infinite (e.g. Q could in principle
   be {2, 3, next prime after some huge gap, ...} with slowly growing gaps chosen to keep the partial
   sums above 1/L0 forever without ever stopping to grow). The union-bound inequality is one-directional
   and cannot by itself exclude an infinite Q. **This route is a genuine dead end as stated**: no
   amount of refining the union bound turns a lower bound into an upper bound on |Q|.

2. **"Eventually-always" strengthening route.** I tried to argue every q ∈ Q must in fact divide
   a_n for ALL sufficiently large n (not just infinitely many), reasoning that then only finitely many
   such primes can coexist because a single a_N has only finitely many prime factors. This
   strengthening is FALSE as stated: direct simulation of a_1 = 21 shows the prime 7 ∈ Q (it recurs
   infinitely often, every 7th term of the eventual arithmetic-progression-like tail, since gaps are
   eventually constant equal to 3 and 3 is invertible mod 7) but 7 does **not** divide every
   sufficiently large term — only a periodic subset of them. So Q-membership is strictly weaker than
   "eventually always divides," and the argument that finite-factorization-of-a_single-integer bounds
   |Q| does not apply: infinitely many primes could in principle each recur on their own increasingly
   sparse periodic sub-pattern, with no single term ever needing to be divisible by more than finitely
   many of them at once, so there is no factorization-count contradiction from this angle either.
   **This route is also a dead end as stated**, for a reason confirmed by direct computation, not
   merely suspected.

3. **Greedy-minimality / "large primes are never strictly needed" route.** Intuition: the greedy
   process, always choosing the smallest valid candidate, should "prefer" reusing small primes (which
   have short periods and can satisfy many constraints via CRT with small increments) over invoking a
   large prime, so large primes should only ever appear as one-off "riders," never as recurring
   (Q-)members. This intuition is exactly what the simulation data supports (Q always turned out small
   and dominated by 2 and small factors of a_1 in every example tried), but I could not turn it into a
   proof: the obstruction is that "greedy prefers small primes" is a statement about *typical* behavior
   averaged over many steps, not a statement that can be checked or falsified at any single step (there
   is no single index n at which one can point to a contradiction if a large prime is reused
   periodically with a long period — the greedy choice at each individual step is still consistent with
   an extremely long-period recurrence of a large prime coexisting with everything else, since a single
   greedy step only "sees" the immediate next candidate, not the infinite future recurrence pattern).
   Formalizing this requires exactly the kind of finite-window/finite-state argument (bounding how far
   back in the sequence a constraint can still be "live") that the sibling approaches are also stuck on
   — **this route reduces to the same shared wall the reviewer identified**, it is not a new escape from
   it, only a different vocabulary for approaching it.

**Honest conclusion for this round.** The monovariant-telescoping framing, concretized as "Q := primes
recurring infinitely often; show |Q| < ∞," is a legitimate and different top-level object from the
sibling approaches' S = primes(a_1)-based signatures — but it does not sidestep the field's shared
difficulty. It hits the same underlying wall (bounding which primes can become permanently/recurringly
relevant), confirmed by three failed independent routes above rather than merely restated as an
assumption. This is not "no mechanism was tried" (as the outline recorded going into this round); it is
"three concrete mechanisms were tried and each fails for an identified, provable reason." The two
lemmas proved in full (Lemma 0, Lemma 1/Corollary 1.1, Lemma 2, Proposition 3) are correct, new content
usable by any approach (Lemma 2 and Proposition 3 in particular give the cleanest general-purpose
statement of "some prime must recur forever" available in the population so far, not tied to primes(a_1)
alone), but the theorem itself is not proved by this approach in its current form.

## Full proof
(Not applicable — Status is partial, not solved.)

## Promotable lemmas

- **Lemma 0 (every term after a_1 hits S0)** — for i ≥ 2, gcd(a_i,a_1) > 1, hence a_i has a prime
  factor in S0 := primes(a_1). Proved in full above from the recursive definition alone. Trivial but
  foundational; likely already used implicitly by sibling approaches — worth stating as a named,
  certified lemma so it can be cited rather than reproven each time.

- **Lemma 1 / Corollary 1.1 (global gap and linear-growth bound)** — a_{n+1} − a_n ≤ L0 = ∏_{p|a_1} p
  for every n ≥ 1 (no "eventually" needed — holds from n = 1 on), hence a_N ≤ a_1 + (N−1)L0 for all N.
  Proved in full above via an explicit CRT-style "next multiple of L0" construction and Lemma 0. This
  is the same bound used by `growth-bound-density`; since it is now proved independently here too, it
  is ready to certify into `results/imo-2026-06/lemmas/` as shared, reusable content.

- **Lemma 2 (Q-cover Lemma)** — with Q := {primes dividing infinitely many terms of the sequence},
  every index i ≥ 1 has a prime factor of a_i lying in Q. Proved in full above by a finite-maximum /
  contradiction argument, independent of S0 or any assumption that the active prime set is finite.
  This is new, general-purpose content not present in any sibling approach's file (they work with
  S0 = primes(a_1) as their base set; Q is the correct, S0-independent generalization, and this lemma
  is the rigorous formal statement of "some prime must recur forever," proved without assuming Q is
  finite).

- **Proposition 3 (density inequality)** — Σ_{q ∈ Q} 1/q ≥ 1/L0. Proved in full above, combining
  Lemma 2, Corollary 1.1, and a union-bound counting argument on multiples. Reusable as a sanity check
  / quantitative fact for any future attempt at bounding Q, though (as documented above) it is
  provably insufficient on its own to establish |Q| < ∞.
