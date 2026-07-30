## imo-2026-06 — lens: reduced-process reverse-inequality (termwise coincidence a_n = b_n)

### Setup recap
`reduced-process-identity.md` reduces the whole theorem (rigorously, certified endgame) to
**(SL): every two terms of the sequence share a prime ≤ P_max** (equivalently the true greedy
sequence a_n coincides termwise with the "reduced" small-primes-only greedy sequence b_n).
Framed as strong induction, at step n the gap is the reverse inequality **β ≤ a_{n+1}**, where
β := min{m > a_n : m shares a prime ≤ P_max with each of a_1,…,a_n}. The easy direction
a_{n+1} ≤ β is proved (F2-type argument via the next multiple of a_1). The reverse direction is
the crux; the file itself proves (G3) that the interval (a_n, a_{n+1}) contains **no** element of
E_n at all — so no "exhibit a smaller compatible competitor" argument can work; a_{n+1} genuinely
is the minimal admissible integer, and (SL_n) is a property of its *value*, not of an
existence-of-competitor statement.

### Where exactly the induction breaks
The obstruction is precisely G3 in `reduced-process-identity.md`: minimality of a_{n+1} rules out
any classical "assume it fails, exhibit something smaller, contradiction" argument, because by
definition nothing smaller is even in E_n. Any successful induction step must instead be a
**direct structural argument about the value a_{n+1}** — e.g. show that IF a_{n+1} used a prime
q > P_max to connect to some predecessor a_k, THEN a_{n+1} could not actually be minimal (not by
producing a smaller *competitor number*, but by deriving a contradiction from a_{n+1}'s own
factorization / from the sole-connector-off-lattice constraint (Prop C) / from a parity or
valuation argument on a_{n+1} itself). No such argument is yet in hand.

### The reviewer's flagged subtlety — investigated, and it is REAL but the machinery generalizes
The concern: Lemma A (as stated in earlier rounds) forbids only the *sole*-connector case —
`primes(A) ∩ primes(B) = {q}` for a single prime q > P_max. But (SL) requires every pair to share
*some* prime ≤ P_max, which also forbids the case where two terms share **two or more** primes,
all > P_max, with **zero** shared small prime (e.g. `primes(A) ∩ primes(B) = {q1,q2}`, q1,q2 both
> P_max). Lemma A's statement, read literally, says nothing about this multi-prime case — so (SL)
is indeed formally stronger than the literal statement of Lemma A. I checked whether this gap is
real or vacuous:

- **It is a genuinely distinct logical case** (not automatically covered by the singleton
  argument) — Lemma A's hypothesis `= {q}` simply doesn't apply when the shared-prime set has size
  ≥ 2.
- **But the certified proof technique of Prop C (lemmas/sole-connector-off-lattice.md) generalizes
  verbatim, at no extra cost.** Re-reading the Prop C proof: it never uses that the intersection is
  a singleton. The argument is: if a_1 | A, then P (primes of a_1) ⊆ primes(A); every term B shares
  *some* prime p ∈ P with a_1 (certified F1); that same p then lies in primes(A) ∩ primes(B); if
  this intersection is disjoint from P (in particular if it is entirely primes > P_max), p ∈ P
  forces a contradiction — **regardless of how many primes are in the intersection**. So: *if A, B
  share no prime of P at all (in particular no small prime ≤ P_max), then a_1 divides neither A nor
  B* — for ANY size of the (all-large) shared-prime set, not just singletons. This is a genuine
  (easy, one-line) generalization of the certified lemma, not yet written up, worth promoting: it
  confines every hypothetical SL-violating pair (single- or multi-large-prime) to the same
  length-<a_1 window structure as before. It does not resolve (SL), but it kills the concern that
  the multi-large-prime case needs fundamentally new machinery — the existing lattice-avoidance
  argument already covers it.

### Numerical investigation (this round)
Wrote and ran a direct simulator (`/tmp/greedy_probe*.py`, sympy-based) computing the *true* greedy
sequence a_n (not the reduced b_n directly, but equivalently checking (SL) termwise, which is
exactly the coincidence a_n = b_n by the file's Step 3 equivalence) and searching explicitly for:
(a) any pair of terms with **zero** shared prime ≤ P_max (a genuine SL violation), and
(b) among those, any where the shared prime set has size ≥ 2 (the flagged multi-large-prime case).

Tested 25 seeds total, including "worst case" stress tests with very few small primes available
(a_1 = 6, 10, 14, 22, 26, 33, 34, 38, 46 — products of two primes with small P_max, giving the
*fewest* small primes to share and hence the most pressure toward a large-prime shortcut), with
term counts from 120 up to 500 (max term computed up to ~1900):

- **Zero SL violations in every single case** — the termwise coincidence a_n = b_n holds
  exactly and without exception on all seeds tested (conjectural but with essentially no
  counter-evidence after ~5000+ pair-checks across 25 seeds).
- Confirmed (as a sanity check, not a new fact) that pairs sharing **two or more large primes
  simultaneously** DO occur in the sequence (e.g. a_1=15: 462 = 2·3·7·11 and 770 = 2·5·7·11 share
  large primes {7,11}) — but in every observed instance such pairs *also* share a small prime (here
  2), so they are not SL violations. This shows multi-large-prime co-occurrence is a real
  phenomenon in the dynamics (not vacuous), reinforcing that the reviewer's flagged case is worth
  taking seriously in the induction, even though no violation has ever been observed.

### Assessment of this route
The strong-induction-on-termwise-coincidence framing is fully set up and cannot be pushed further
without a genuinely new idea for the reverse inequality. The one new piece of terrain this round
adds is: (1) the multi-large-prime case is logically distinct from the singleton case but the
certified Prop C machinery extends to it for free (a small promotable generalization, not a proof
of SL); (2) the "exhibit a smaller competitor" style of argument is provably unavailable (G3,
re-verified by re-reading the proof, it is correct) — any future attempt on (SL_n) MUST be a direct
argument about the factorization/value of a_{n+1}, e.g. via valuations, a smoothness/cost bound, or
an amortized/potential-function argument over the whole history, not a minimality-contradiction
argument. This rules out an entire natural family of approaches (repeat this warning to the
outliner so it isn't retried in a new guise).

## Distinct openings surfaced by this lens
1. **Value-property argument on a_{n+1}'s own factorization** (not competitor-based): try to show
   directly that if a_{n+1} carried a prime q > P_max as an essential connector to some a_k, some
   other predecessor a_j would then be *incompatible* with a_{n+1} unless a_{n+1} also carries a
   small prime — i.e., derive that "large-prime-only connection to a_k" is inconsistent with
   simultaneous compatibility with a *different* predecessor a_j, using the pairwise-intersecting
   but-no-common-element structure of {S_1,…,S_n} (G4) as leverage. Not attempted in detail; a
   genuinely different induction strengthening from anything on file.
2. **Promote the generalized Prop C** (multi-prime lattice-avoidance) as a cheap new lemma —
   strengthens the toolbox any live approach can cite, even though it alone doesn't close (SL).
3. **Amortized/potential argument**: instead of a per-step induction, bound the *total* "large-prime
   budget" used across all n (e.g., total number of distinct large primes ever recruited, or total
   excess size caused by large-prime connections) and show it must stay finite — a global rather
   than local induction, sidestepping the "no smaller competitor" trap by not trying to falsify a
   single step.

## Candidate technique(s)
Strong induction is structurally blocked in its naive (competitor/minimality) form; needs either a
direct factorization-based argument at each step, or a global/amortized invariant. KB entries: CRT
(already used for E* periodicity), no other KB entry directly attacks greedy minimality.

## Cheap-kill candidates
None new found this round — the generalized-Prop-C confinement (a_1 never divides an SL-violating
witness) is the only cheap structural fact available; it narrows the search window but does not by
itself kill the crux.

## Knowledge-base entries to use
Same as prior rounds: Chinese Remainder Theorem (for E* periodicity, already certified). No new KB
entry identified for the reverse inequality itself — this crux appears to need a bespoke argument,
consistent with round-2's finding that pure combinatorics/covering/capacity are insufficient.

## Analogous past problems (cruxes)
Not separately queried this round (out of scope for this lens per dispatch — focus was verification
of an existing framing); prior rounds' explorers should be consulted for corpus matches (none
reported as strongly analogous in round 2 reports, per current.md's silence on this).

## Prior progress
As in current.md: full reduction to (SL) is complete and certified (E* periodicity, reduction to
set inclusion). This round's net addition: (1) empirical strengthening — 25 seeds, including
small-P_max stress cases, zero SL violations; (2) resolved the reviewer's "is SL strictly stronger
than Lemma A" question — yes, formally, but the certified Prop C proof extends to the general case
for free (promotable generalization, one line, not yet written up as a lemma file); (3) reconfirmed
G3 (no-smaller-competitor) is correct, ruling out an entire class of future attempts.

## Dead ends (do not retry)
- Competitor/minimality argument on (SL_n) (G3, re-verified correct this round): the window
  (a_n, a_{n+1}) is provably empty of E_n-elements, so "exhibit a smaller compatible integer" can
  never contradict a_{n+1}'s minimality — any future approach that tries this will fail exactly as
  recorded.
- Helly-type "common small prime" arguments (G4): {S_1,…,S_n} is only pairwise-intersecting, not
  centrally intersecting (explicit witness: {2,3},{3,5},{2,5} realizable as small supports) — a
  single-universal-small-prime shortcut is unavailable.
- Global capacity/density counting (round 2, large-prime-capacity-counting): proven structurally
  incapable of isolating the finitely-many-large-primes claim.

## Small-case / intuition notes (conjecture, not proof)
- (SL) / termwise coincidence a_n = b_n holds exactly on all 25 tested seeds (a_1 up to several
  thousand, sequences up to ~500 terms / term values up to ~1900), including seeds engineered to
  minimize the number of available small primes (a_1 = product of two primes). This is strong
  empirical support but remains unproven.
- Multi-large-prime co-occurrence between two terms is a real, observed phenomenon (not a vacuous
  edge case) — but every observed instance is accompanied by a shared small prime, consistent with
  (SL) but not explaining why it must be.
