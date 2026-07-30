# imo-2026-03 — approach `majorization-upper` (REVISED, round 6)

**Round-6 revision (per outline-reviewer round 6):** the O1 split-bottom +
exact-pair-rest strategy for the compressed case (a_{n+1} > 1/D_n) is **PROVABLY
DEAD** — the reviewer proved exact pairing into equal pairs is IMPOSSIBLE for
the compressed config (5,3,2)/10 (n=2) for ALL x ∈ (0, 1/D_n] and ALL 9 split/
pairing patterns; the "pairing feasibility as a PL function of x" is a category
error (a discrete 0/1 indicator, IVT cannot apply). O1 is NOT retried.

**Round-6 HEADLINE (certifiable milestone, this round):** the halving lemma is
**GENERALIZED** — `halving-always-a-nplus1`: for ANY strictly-decreasing
m = n+1 Liu config (a_1 > … > a_{n+1}), Xiang halving a_1,…,a_n (n marks,
leaving a_{n+1}) gives **D = a_{n+1}** — the bottom-dominance hypothesis of
`bottom-dominant-halving` is DROPPED. The proof is a clean parity/grouping
(block) argument that does not depend on the sorted order's specifics. **Corollary
(close the region):** D* ≤ a_{n+1} for ALL strictly-decreasing m = n+1 configs
(all n, no induction) ⟹ **the a_{n+1} ≤ 1/D_n region is CLOSED for all n**
(halving gives D = a_{n+1} ≤ 1/D_n directly). This collapses GAP-U2's
non-bottom-dominant sub-case (a) whenever a_{n+1} ≤ 1/D_n; the ONLY remaining
open case is the **compressed** case a_{n+1} > 1/D_n (strictly narrower than
GAP-U2 as originally stated). The compressed case is honestly left as
**GAP-U2-compressed** (verified, not proved).

**Round-5 revision (per explorer + outliner + reviewer):** the V(n) ← V(n−1)
inductive spine and the 3-mark pairing cascade are **DROPPED** — both refuted as
phantom-crux chasers (the crux regime gives D* = 0 or tiny; the IH overshoots
because V(n−1) is a worst-case bound blind to slack). The **NEW spine is the
direct adaptive strategy**: case-split on the Liu config by piece count and
bottom-dominance, with NO induction on n.

**What is PROVED this round (round 6, the certifiable milestone):**
- **`halving-always-a-nplus1` (NEW, generalized)** — for ANY strictly-decreasing
  m = n+1 Liu config (a_1 > … > a_{n+1}), Xiang halving a_1,…,a_n (n marks,
  leaving a_{n+1}) gives D = a_{n+1}. The bottom-dominance hypothesis of
  `bottom-dominant-halving` is DROPPED. **Fully proved** (Part IV-bis, parity/
  grouping argument). **Corollary: the a_{n+1} ≤ 1/D_n region is CLOSED for all n**
  (halving gives D = a_{n+1} ≤ 1/D_n directly, no induction). This subsumes the
  entire non-bottom-dominant sub-case (a) of GAP-U2 whenever a_{n+1} ≤ 1/D_n, and
  the bottom-dominant sub-case (b) with a_{n+1} ≤ 1/D_n.

**What is PROVED (rounds 2–5, all rigorous, no induction):**
1. **GAP-U3 (m ≤ n ⟹ D* = 0)** — Xiang halves every piece; the resulting multiset
   has every value appearing an even number of times; each even block contributes
   0 to D. **Fully proved** (Part III). Lemma `m-le-n-halving-D-zero`.
2. **Halving lemma (bottom-dominant)** — for m = n+1 with a_n ≥ 2 a_{n+1},
   halving the n largest pieces (leaving a_{n+1}) gives D = a_{n+1}. **Fully
   proved** (Part IV). Lemma `bottom-dominant-halving` (now a COROLLARY of
  `halving-always-a-nplus1`).
3. **Repeated-value lemma** — for m = n+1 with any repeated value (a_i = a_{i+1}),
   D* = 0 (spine-pair-cancellation + halving the spine, which has ≤ n−1 ≤ n
   pieces). **Fully proved** (Part V). Lemma `repeated-value-D-zero`.

**What remains OPEN (GAP-U2-compressed, strictly narrower than GAP-U2):**
for m = n+1, strictly decreasing, and **a_{n+1} > 1/D_n** (the "compressed"
case — the smallest piece exceeds the target 1/D_n), exhibit a ≤ n-mark Xiang
strategy with D ≤ 1/D_n. The halving bound D = a_{n+1} > 1/D_n does NOT close
this (it overshoots); D* may be much smaller via piece-matching strategies, but
no universal proof is known. The O1 exact-pairing strategy is PROVABLY DEAD
(outline-reviewer round 6: exact pairing impossible for compressed configs).
Candidate mechanisms: O2 (split LARGE pieces to match MEDIUM pieces — the
empirically-winning D-small move) and bounded-spread pigeonhole (a_{n+1} > 1/D_n
forces bounded spread a_1/a_{n+1} < D_n − n). Both are honest OPEN sub-steps;
verification (exact-Fraction n=2 exhaustive, n=3 grid, round-5 breakpoint
search 0 violations over 6000+ trials) supports the claim but is verification-
not-proof. Flagged as **GAP-U2-compressed**.

**Base cases n = 1, 2, 3 are CERTIFIED (imported):** `n1-base-both-bounds`,
`n2-upper-bound-complete`, `v3-upper-bound` + `n2-max-bound`. The direct
strategy recovers V(3) (the n=3 base) — the halving and pairing moves of V(3)
are exactly the direct strategy's P1/P2 at n=3.

---

## Status

partial

The upper bound is **proved unconditionally for n = 1, 2, 3** (certified base,
imported). For **general n**, the direct adaptive strategy closes:
- **m ≤ n** (D* = 0, GAP-U3 proved);
- **m = n+1 with a repeated value** (D* = 0, repeated-value lemma proved);
- **m = n+1, strictly decreasing, a_{n+1} ≤ 1/D_n** (D* ≤ a_{n+1} ≤ 1/D_n,
  `halving-always-a-nplus1` proved — the bottom-dominance hypothesis is
  DROPPED; the a_{n+1} ≤ 1/D_n region is CLOSED for all n, regardless of
  bottom-dominance).

The remaining open case is **GAP-U2-compressed**: m = n+1, strictly decreasing,
and **a_{n+1} > 1/D_n** (compressed). The halving bound D = a_{n+1} overshoots
1/D_n here; D* may be smaller via piece-matching (O2), but no universal proof
is known. O1 (exact pairing) is PROVABLY DEAD. Candidate mechanisms: O2
(split-LARGE-to-match-MEDIUM) and bounded-spread pigeonhole. Both honest OPEN
sub-steps; verification supports the claim but is verification-not-proof.
Flagged as GAP-U2-compressed.

## Approaches tried

- `majorization-upper` (round 2, NEW) — proved the mechanical scaffolding
  (parallel-halving-saturates-tower, dominant-factorization, pairing-cancellation,
  Lemma B1); proved the full n = 2 upper bound; set up the general-n induction
  (regimes A and B1 close cleanly); the general-n below-threshold regimes (C, B2
  for n ≥ 3) and "tower-is-unique-worst" exchange monotonicity were left as the
  explicit open crux (G1/G2).
- `majorization-upper` (round 3, REVISE) — DROPPED the
  majorization/Schur-convexity/Karamata route (D* is not Schur-convex). NEW
  spine: the Max-bound conjecture D* ≤ M/2^n. PROVED: (i) dominant case by
  halving induction; (ii) non-dominant a_3 ≤ a_1/2 by pairing + IH. OPEN: the
  crux a_1 < 2a_2 ∧ a_3 > a_1/2.
- `majorization-upper` (round 4, REVISE) — MAX-BOUND CONJECTURE FALSIFIED
  (exact-Fraction counterexample (7,6,5,3)/21, ratio 8/7; Part I). NEW spine:
  V(n) = M_2/2^{n−1}. PROVED V(3) from certified n=2 Max-bound. V(n≥4) OPEN:
  V(n) ← V(n−1) IH overshoots 37% of crux cases; mutual W/V recursion + 3-mark
  cascade are conjectures.
- `majorization-upper` (round 5, REVISE) — DROPPED the V(n) ← V(n−1) IH and the
  3-mark cascade (both refuted as phantom-crux chasers by the upper explorer:
  the crux regime gives D* = 0 or tiny; the IH is a worst-case bound blind to
  slack). NEW spine: the DIRECT ADAPTIVE STRATEGY (no induction on n).
  **PROVED this round:** GAP-U3 (m ≤ n ⟹ D* = 0, even-multiplicity argument);
  halving lemma (bottom-dominant m = n+1 ⟹ D = a_{n+1}); repeated-value lemma
  (m = n+1 with a repeat ⟹ D* = 0, spine-pair-cancellation + halving the spine).
  These close three sub-cases of the general-n upper bound unconditionally.
  **OPEN:** GAP-U2 (strictly-decreasing configs where halving exceeds target
  or doesn't apply — the pair-matching cascade, conjecture from 3000 trials).
- `majorization-upper` (round 6, REVISE) — **HEADLINE: generalized the halving
  lemma to `halving-always-a-nplus1`** (drops the bottom-dominance hypothesis:
  halving a_1,…,a_n gives D = a_{n+1} for ANY strictly-decreasing m = n+1 config,
  via a parity/block-grouping argument independent of the sorted order's
  specifics). **Corollary: the a_{n+1} ≤ 1/D_n region is CLOSED for all n**
  unconditionally — this collapses GAP-U2's non-bottom-dominant sub-case (a)
  whenever a_{n+1} ≤ 1/D_n, so GAP-U2 narrows to ONLY the compressed case
  a_{n+1} > 1/D_n (strictly narrower). O1 (split-bottom + exact-pair-rest) is
  **PROVABLY DEAD** (outline-reviewer: exact pairing impossible for (5,3,2)/10
  for all x ≤ 1/D_n and all split/pairing patterns; the "PL-pairing-feasibility"
  function is a category error — IVT cannot apply). NOT retried. The compressed
  case (O2 split-LARGE-to-match-MEDIUM + bounded-spread pigeonhole) is honestly
  left as GAP-U2-compressed: verified (exact-Fraction n=2 exhaustive, n=3 grid,
  round-5 breakpoint search 0/6000+ violations) but NOT proved. The parity
  obstruction (2n+1 odd ⟹ D ≠ 0 always with n marks) is noted: the compressed
  case can only yield D = small leftover ≤ 1/D_n, never D = 0 via n marks.

## Current best

Certified scaffolding (imported, stays): `parallel-halving-saturates-tower`
(the equality witness D(T_n) = 1/D_n); `pl-breakpoint-minimum` (B1); the full
n = 2 upper bound (`n2-upper-bound-complete`, `n2-max-bound`); n = 1 base
(`n1-base-both-bounds`); `closed-form-answer`; `spine-pair-cancellation` (S1);
`v3-upper-bound` (n=3 base); `bottom-dominant-halving` (now subsumed by
`halving-always-a-nplus1`).

PROVED this round (round 6, the certifiable milestone):

**`halving-always-a-nplus1` (NEW, generalized, fully proved — Part IV-bis).**
For ANY strictly-decreasing m = n+1 Liu config (a_1 > … > a_{n+1}), Xiang halves
a_1, …, a_n (n marks, leaving a_{n+1}). The refined multiset is
{a_1/2, a_1/2, …, a_n/2, a_n/2, a_{n+1}} (2n+1 pieces). The values a_1/2, …,
a_n/2 are pairwise distinct (strictly-decreasing ⟹). Sort non-increasingly and
group consecutive equal values into blocks. Every value v ≠ a_{n+1} appears
exactly twice (a size-2 block, contributing 0). The value a_{n+1} appears
1 + 2·#{i : a_i = 2 a_{n+1}} times — and strictly-decreasing ⟹ at most one i has
a_i = 2 a_{n+1}, so its multiplicity is 1 (k = 0) or 3 (k = 1), both ODD. All
blocks above the a_{n+1}-block have even size, so the total number of pieces
preceding it is even ⟹ the a_{n+1}-block starts at an ODD position. A block of
odd size 2k+1 starting at an odd position has (k+1) plus-signs and k minus-signs
(over 2k+1 consecutive alternating signs), so it contributes +a_{n+1}·1 = +a_{n+1}.
Every even block contributes 0 (k plus, k minus over 2k consecutive positions,
regardless of starting parity). Hence D = a_{n+1}. ✓ Mark budget n. This is
independent of the sorted order's specifics (only the even-block/odd-block
multiplicity structure matters). Verified 0/20000 exact-Fraction trials (n=2..6,
strictly-decreasing configs). Generalizes `bottom-dominant-halving` (drops the
a_n ≥ 2 a_{n+1} hypothesis).

**Corollary (region closure, all n).** D* ≤ a_{n+1} for ALL strictly-decreasing
m = n+1 configs ⟹ whenever a_{n+1} ≤ 1/D_n, halving gives D = a_{n+1} ≤ 1/D_n
directly. **The a_{n+1} ≤ 1/D_n region is CLOSED for all n, unconditionally.**
This subsumes: (i) the bottom-dominant sub-case (b) with a_{n+1} ≤ 1/D_n (Part IV
of round 5); (ii) the non-bottom-dominant sub-case (a) of GAP-U2 whenever
a_{n+1} ≤ 1/D_n (which is the generic situation, since a_{n+1} ≤ 1/(n+1) and
1/(n+1) ≤ 1/D_n iff D_n ≤ n+1 iff 2^{n+1}−1 ≤ n+1, which FAILS for n ≥ 2 — so the
non-bottom-dominant sub-case is NOT generically closed; the closure is exactly
a_{n+1} ≤ 1/D_n, a sharp threshold).

PROVED (rounds 2–5, all rigorous, no induction):

1. **GAP-U3: m ≤ n ⟹ D* = 0** (Lemma, Part III) — Xiang halves every piece
   (m ≤ n marks). The refined multiset {a_i/2, a_i/2 : i = 1..m} has every value
   appearing an even number of times (each value v = a_i/2 appears 2 ×
   multiplicity of a_i times). An even block of 2k equal values at consecutive
   positions contributes v·(k − k) = 0 to D (k pluses, k minuses). So D = 0.
   Mark budget m ≤ n. ✓ Closes the m ≤ n case for ALL n.
2. **Halving lemma (bottom-dominant): a_n ≥ 2 a_{n+1} ⟹ D(halving) =
   a_{n+1}** (Lemma, Part IV) — now a COROLLARY of `halving-always-a-nplus1`
   (the bottom-dominance hypothesis is unnecessary). Kept as the round-5
   statement for cross-reference. ✓
3. **Repeated-value lemma: m = n+1 with a_i = a_{i+1} ⟹ D* = 0** (Lemma, Part V)
   — By `spine-pair-cancellation` (S1), D(config) = D(spine), where the spine
   has ≤ n−1 pieces (at least one pair removed). Xiang halves all spine pieces
   (≤ n−1 ≤ n marks). In the refined multiset, every value appears an even
   number of times (spine halves give 2 copies each; paired pieces give 2 copies
   each; collisions merge into even groups). So D = 0. ✓

**Open gap (GAP-U2-compressed, strictly narrower than GAP-U2).** For m = n+1,
strictly decreasing (a_1 > … > a_{n+1}, all distinct), and **a_{n+1} > 1/D_n**
(the compressed case — the smallest piece exceeds the target 1/D_n), exhibit a
≤ n-mark Xiang strategy with D ≤ 1/D_n.

The halving bound D = a_{n+1} > 1/D_n OVERSHOOTS here (it does not close the
case); D* may be much smaller via piece-matching strategies. **O1 (split-bottom
+ exact-pair-rest) is PROVABLY DEAD** (outline-reviewer round 6: exact pairing
into equal pairs is IMPOSSIBLE for the compressed config (5,3,2)/10 (n=2) for
ALL x ∈ (0, 1/D_n] and ALL 9 split/pairing patterns; the "pairing feasibility as
a PL function of x" is a category error — a discrete 0/1 indicator, IVT cannot
apply). NOT retried.

**Candidate mechanisms (honest OPEN sub-steps):**
- **O2 (split-LARGE-to-match-MEDIUM):** split large pieces to create ties with
  medium pieces (the empirically-winning D-small move). Witness for the spread
  config (0.6, 0.2, 0.1, 0.055, 0.045)/1: split a_1=0.6 → {0.2, 0.2, 0.2}
  (matching a_2 = 0.2 → four 0.2's, even) AND a_3=0.1 → {0.055, 0.045}
  (matching a_4, a_5); all-even ⟹ D = 0. For n=2 compressed (5,3,2)/10: split
  a_1=1/2 → {a_3=1/5, a_1−a_3=3/10} (tie at a_3) and a_2=3/10 → {eps, 3/10−eps};
  the tie at a_3 cancels, the residual D = 2·eps → 0 (inf, not attained — parity
  forbids D = 0 with 2 marks; the inf D = 0 ≤ 1/7 holds). The universal existence
  (a matching of large pieces to medium pieces) is an unproved subset-sum core.
- **Bounded-spread pigeonhole (cheap-kill fallback):** a_{n+1} > 1/D_n forces
  compression — a_i ≥ a_{n+1} > 1/D_n for all i ⟹ a_1 ≤ 1 − n/D_n = (D_n − n)/D_n,
  so the spread a_1/a_{n+1} < D_n − n = 2^{n+1} − 1 − n. Bounded spread ⟹ all
  pieces within a factor < 2^{n+1} of each other ⟹ a pigeonhole/size-bucket
  argument may force a matchable structure. NOT proved (the matching existence
  is the same subset-sum core as O2).
- **Parity obstruction (negative, from the explorer):** with exactly n marks
  the refined count is 2n+1 (odd) ⟹ D ≠ 0 always (an odd-multiplicity value
  survives). So the compressed case CANNOT be closed by "D = 0 always" via n
  marks; the best one can hope is D = small leftover ≤ 1/D_n. Design the
  strategy to leave a leftover ≤ 1/D_n, not to fully cancel.

**Verification (verification-not-proof):**
- n=2 compressed: exact-Fraction exhaustive grid search (den up to 2100) over all
  split/pairing patterns, tested (5,3,2)/10, (4,3,2)/9, (6,3,2)/11, (5,4,3)/12,
  (25,16,8)/49 (a_2−a_3 > 1/7), (32,9,8)/49 (a_1 near 5/7). ALL give best
  D ≤ 1/7 (ratios 0.03–1.0; the worst, (32,9,8)/49, gives D = 1/49 < 1/7
  exactly). 0 violations.
- n=3 compressed: exact-Fraction grid search (den 142, split a_1,a_2,a_3 each
  into 2) on the round-5 "phantom-crux" config (29,47,22,15)/142 gives best
  D = 2/71 < 1/15 (ratio 0.42). Random-search-only configs that appeared to
  violate were resolved by the grid search (the random search was too weak).
- Round-5 breakpoint-restricted exact-Fraction search: 0 violations over 6000+
  trials (n=4, all-configs and crux configs), worst ratio 0.52.

The claim D* ≤ 1/D_n in the compressed case is strongly supported but NOT
proved. The open core is the universal piece-matching existence (a subset-sum/
multiset-equal-sums problem), where Xiang chooses the fragment values to create
ties that drive the residual ≤ 1/D_n.

**Sub-case closed via halving + condition:** m = n+1, strictly decreasing, with
a_{n+1} ≤ 1/D_n: halving gives D = a_{n+1} ≤ 1/D_n (by
`halving-always-a-nplus1`). ✓ This sub-case includes the **dominant tower-tail
family** (a_1, 2^{n−1}, …, 2, 1)/S with a_1 ≥ 2^n (S ≥ D_n, so a_{n+1} = 1/S ≤
1/D_n); the tower T_n (S = D_n) is the tight member (D* = 1/D_n, by
`parallel-halving-saturates-tower`).

---

## Full proof

Not complete (GAP-U2 open for general n ≥ 4). The proof below covers everything
that IS proved; every open step is marked **GAP** or **CONJECTURE**.

---

# Part I — The Max-bound counterexample (refutation, kept from round 4)

**Proposition.** *The Max-bound conjecture D* ≤ M/2^n is FALSE.*

**Proof by counterexample.** Consider the n=3 Liu config

$$L \;=\; \frac{1}{21}(7,\,6,\,5,\,3),\qquad a_1=\tfrac{7}{21},\; a_2=\tfrac{6}{21},\; a_3=\tfrac{5}{21},\; a_4=\tfrac{3}{21}.$$

This is a valid sorted config (7 ≥ 6 ≥ 5 ≥ 3, total 21, m = 4 ≤ n+1 = 4). By
Lemma B1 (`pl-breakpoint-minimum`), Xiang's optimal refinement is a breakpoint
(tie) config. The breakpoint-justified optimizer (exact Fraction arithmetic)
gives D*(L) = 1/21, attained by the 3-mark refinement producing three canceling
pairs and a residual 1/21 at position 7 (odd, +). Meanwhile M/8 = (7/21)/8 =
1/24. So D* = 1/21 > 1/24 = M/8 (ratio 8/7 > 1). VIOLATION. The actual target
1/D_3 = 1/15 is NOT violated (1/21 < 1/15). ∎

The Max-bound M/2^n is refuted as a universal conjecture. It is never used
below. The answer c(n) = 2^n/(2^{n+1}−1) survives (only the sufficient lemma
is wrong).

---

# Part II — Setup and imported facts

### The game and the reduction

Liu Bang marks ≤ n points, then Xiang Yu marks ≤ n distinct points; the stick is
cut at all marks; the players alternate claiming pieces (Liu first), each
maximizing their total. We find the largest c(n) Liu can guarantee.

**Lemma 0** (`claim-game-odd-index`, certified). *For a fixed sorted multiset
a_1 ≥ … ≥ a_m, the alternating-draft value is the odd-index sum
a_1 + a_3 + a_5 + … = (T + D)/2, where T = ∑ a_i and D = a_1 − a_2 + a_3 − ….
Greedy is optimal for both.*

By Lemma 0, Liu's guaranteed take is (1 + D)/2, so the game reduces to the
alternating sum D of the sorted multiset after both players mark. Liu (inner
maximizer) wants D large; Xiang (outer minimizer) wants D small. The game value
is c(n) = (1 + D*(n))/2 where D*(n) = max_L min_Xiang D. The conjecture is
D*(n) = 1/D_n with D_n = 2^{n+1} − 1. **This file owns the upper bound
D* ≤ 1/D_n**: exhibit Xiang's adaptive strategy.

### Imported lemmas

- `claim-game-odd-index` (Lemma 0) — game value = odd-index sum = (T+D)/2.
- `n1-base-both-bounds` — c(1) = 2/3 (both bounds, certified).
- `n2-upper-bound-complete` — c(2) ≤ 4/7, tower T_2 unique equality, certified.
- `n2-max-bound` — n=2 Max-bound D* ≤ max/4 (derived from the above, certified).
- `v3-upper-bound` — n=3 upper bound D* ≤ M_2/4 (certified).
- `parallel-halving-saturates-tower` (U1) — Xiang's parallel halving of T_n
  yields D = 1/D_n exactly (the upper-bound witness against the tower).
- `pl-breakpoint-minimum` (B1) — Xiang's min of D over refinements is at a
  breakpoint (tie) config.
- `spine-pair-cancellation` (S1) — for any sorted multiset, removing adjacent-
  equal pairs preserves D; D(M) = D(spine(M)).
- `closed-form-answer` — the closed form r_n = 2^n/(2^{n+1}−1).

### Notation

A **Liu config** is a sorted multiset a_1 ≥ a_2 ≥ … ≥ a_m with m ≤ n+1 and
∑ a_i = 1. Write M := a_1 (largest), M_2 := a_2 (second-largest). A **Xiang
refinement** (≤ n marks) replaces some a_i by a partition into ≥ 2 positive
parts; the result is re-sorted. **Homogeneity:** D(c·multiset) = c·D(multiset),
so bounds are scale-free. The upper-bound target is D ≤ 1/D_n = 1/(2^{n+1}−1)
(real units).

**Sign convention.** For a sorted (non-increasing) multiset (b_1 ≥ b_2 ≥ … ≥
b_N), the alternating sum is D = b_1 − b_2 + b_3 − … = ∑_{i} sign(i)·b_i where
sign(i) = + for odd i, − for even i. Note D ≥ 0 for any non-increasing
multiset (since b_{2k−1} ≥ b_{2k} for all k).

---

# Part III — GAP-U3: m ≤ n ⟹ D* = 0 (PROVED)

> **Lemma (m-le-n-halving-D-zero).** *For any Liu config L = (a_1 ≥ … ≥ a_m) with
> m ≤ n pieces, Xiang has ≤ n marks forcing D = 0. Hence D*(L) = 0 ≤ 1/D_n.*

**Proof.** Xiang halves every piece: for each i = 1, …, m, split a_i into
{a_i/2, a_i/2}. This uses m ≤ n marks. The refined multiset is

$$M' \;=\; \bigl\{\,\tfrac{a_1}{2}, \tfrac{a_1}{2},\; \tfrac{a_2}{2}, \tfrac{a_2}{2},\; \ldots,\; \tfrac{a_m}{2}, \tfrac{a_m}{2}\,\bigr\}.$$

**Claim (even-multiplicity lemma).** *If every distinct value in a sorted
multiset appears an even number of times, then D = 0.*

*Proof of claim.* Sort the multiset non-increasingly. Group consecutive equal
values into blocks. Each block has even size 2k (by hypothesis, every value
appears an even number of times). A block of 2k equal values v at positions
p, p+1, …, p+2k−1 contributes

$$v \cdot \sum_{j=0}^{2k-1} \mathrm{sign}(p+j) \;=\; v \cdot (\text{# of } + \text{ signs}) - v \cdot (\text{# of } - \text{ signs}).$$

Over 2k consecutive positions, the signs alternate (+, −, +, −, …), so there
are exactly k positions with + and k with − (regardless of the starting
parity, since 2k is even). The contribution is v·(k − k) = 0. Summing over all
blocks, D = 0. ∎ (claim)

**Application.** In M', each value v = a_i/2 appears exactly 2 × (multiplicity
of a_i in L) times — an even number. (If a_i = a_j for i ≠ j, their copies merge
into a group of size 2 × (combined multiplicity), still even.) Hence every value
in M' appears an even number of times. By the even-multiplicity lemma, D(M') = 0.

Since Xiang achieves D = 0 ≤ 1/D_n (as 1/D_n > 0), we have D*(L) ≤ 0. But D ≥ 0
for any non-increasing multiset (sign convention above), so D*(L) = 0. ∎

**Mark budget.** m marks, m ≤ n. ✓

**Numerical verification.** Exact-Fraction check, 10000 random trials (n=1..6,
random configs with m ≤ n), all give D = 0 after halving every piece. ✓

---

# Part IV — Halving lemma: bottom-dominant m = n+1 ⟹ D = a_{n+1} (PROVED)

> **Lemma (bottom-dominant-halving).** *For a Liu config L = (a_1 ≥ a_2 ≥ … ≥
> a_{n+1}) with m = n+1 and a_n ≥ 2·a_{n+1} ("bottom-dominant"), Xiang's strategy
> of halving the n largest pieces (a_1, …, a_n) and leaving a_{n+1} unsplit
> uses n marks and gives D = a_{n+1}.*

**Proof.** Xiang splits each a_i (i = 1, …, n) into {a_i/2, a_i/2}. This uses
n marks. The refined multiset is

$$M' \;=\; \bigl\{\,\tfrac{a_1}{2}, \tfrac{a_1}{2},\; \tfrac{a_2}{2}, \tfrac{a_2}{2},\; \ldots,\; \tfrac{a_n}{2}, \tfrac{a_n}{2},\; a_{n+1}\,\bigr\},$$

total 2n + 1 pieces.

**Sorted order.** Since a_1 ≥ a_2 ≥ … ≥ a_n (sorted), we have a_1/2 ≥ a_2/2 ≥
… ≥ a_n/2. The bottom-dominant condition a_n ≥ 2 a_{n+1} gives a_n/2 ≥
a_{n+1}. Hence the non-increasing sorted order of M' is exactly

$$\tfrac{a_1}{2},\; \tfrac{a_1}{2},\; \tfrac{a_2}{2},\; \tfrac{a_2}{2},\; \ldots,\; \tfrac{a_n}{2},\; \tfrac{a_n}{2},\; a_{n+1}.$$

(The two copies of each a_i/2 are adjacent — they are equal, and a_i/2 ≥
a_{i+1}/2 so no value interposes. And a_n/2 ≥ a_{n+1} places a_{n+1} last.)

**Alternating sum.** The pair (a_i/2, a_i/2) occupies positions (2i−1, 2i):
position 2i−1 is odd (sign +), position 2i is even (sign −). Contribution:
+a_i/2 − a_i/2 = 0. The residual a_{n+1} is at position 2n+1 (odd, sign +).
Contribution: +a_{n+1}.

$$D(M') \;=\; \sum_{i=1}^{n} 0 \;+\; a_{n+1} \;=\; a_{n+1}.$$

Since D* ≤ D(any Xiang strategy) = D(M') = a_{n+1}, we have D*(L) ≤ a_{n+1}. ∎

**Corollary (dominant tower-tail).** *For the tower-tail family
(a_1, 2^{n−1}, 2^{n−2}, …, 2, 1)/S (geometric ratio 2 in the bottom n pieces,
S = a_1 + D_n − 1 the total), if a_1 ≥ 2^n (dominant tower-tail, S ≥ D_n),
then D* ≤ a_{n+1} = 1/S ≤ 1/D_n. The tower T_n (a_1 = 2^n, S = D_n) is the
tight member: D* = 1/D_n (by `parallel-halving-saturates-tower`).*

*Proof of corollary.* The tower-tail family satisfies a_n = 2 ≥ 2·1 = 2 a_{n+1}
(bottom-dominant, with equality). By the halving lemma, D ≤ a_{n+1} = 1/S. For
dominant tower-tail (a_1 ≥ 2^n), S = a_1 + (2^n − 1) ≥ 2^n + (2^n − 1) = D_n,
so 1/S ≤ 1/D_n. ✓ For the tower itself (a_1 = 2^n, S = D_n), D* = 1/D_n
exactly (certified `parallel-halving-saturates-tower`). ∎

**When halving closes the case.** For general bottom-dominant m = n+1 configs,
the halving lemma gives D* ≤ a_{n+1}. This closes the case whenever
a_{n+1} ≤ 1/D_n. The condition a_{n+1} ≤ 1/D_n is equivalent to
∑_{i=1}^{n} a_i ≥ (D_n − 1)·a_{n+1} = 2(2^n − 1)·a_{n+1}: the top n pieces
are "spread enough" relative to the tail. The dominant tower-tail family
attains this with equality at the tower; any config with a larger top (for
given a_{n+1}) is strict.

**When halving does NOT close the case.** If a_{n+1} > 1/D_n (the tail is
"large" relative to the spread), the halving bound D = a_{n+1} exceeds the
target 1/D_n. This is sub-case (b) of GAP-U2 (Part VII). The halving bound is
an UPPER BOUND on D*; the actual D* may be smaller (the pair cascade, GAP-U2).

**Numerical verification.** Exact-Fraction check, 10000 random bottom-dominant
strictly-decreasing configs (n=1..6), all give D(halving) = a_{n+1}. ✓

---

# Part IV-bis — Generalized halving lemma: D = a_{n+1} for ANY strictly-decreasing m = n+1 config (PROVED, round 6)

> **Lemma (`halving-always-a-nplus1`, NEW round 6 — generalizes
> `bottom-dominant-halving`).** *For a strictly-decreasing Liu config
> L = (a_1 > a_2 > … > a_{n+1}) with m = n+1 (all pieces distinct), Xiang's
> strategy of halving the n largest pieces (a_1, …, a_n) and leaving a_{n+1}
> unsplit uses n marks and gives*
>
> $$D \;=\; a_{n+1}.$$
>
> *No bottom-dominance hypothesis is required. Hence D*(L) ≤ a_{n+1} for EVERY
> strictly-decreasing m = n+1 config.*

**Proof.** Xiang splits each a_i (i = 1, …, n) into {a_i/2, a_i/2}. This uses
n marks. The refined multiset is

$$M' \;=\; \bigl\{\,\tfrac{a_1}{2}, \tfrac{a_1}{2},\; \tfrac{a_2}{2}, \tfrac{a_2}{2},\; \ldots,\; \tfrac{a_n}{2}, \tfrac{a_n}{2},\; a_{n+1}\,\bigr\},$$

total 2n + 1 pieces.

**Step 1 — block decomposition.** Sort M' non-increasingly and group consecutive
equal values into maximal blocks. (Equivalently, the spine of M' by
`spine-pair-cancellation` S1, but we do not invoke S1; we reason directly on
blocks.) Each block is a maximal run of equal values.

**Step 2 — every value v ≠ a_{n+1} appears an even number of times.** The values
that can appear in M' are exactly {a_1/2, a_2/2, …, a_n/2, a_{n+1}}. Since L is
strictly decreasing (a_1 > a_2 > … > a_n), the values a_1/2 > a_2/2 > … >
a_n/2 are pairwise distinct. Each a_i/2 (i = 1, …, n) appears exactly twice
(the two halves of a_i), UNLESS a_i/2 = a_{n+1} for some i — i.e., unless
a_i = 2 a_{n+1}. So:
- For each i with a_i ≠ 2 a_{n+1}: the value a_i/2 appears exactly 2 times
  (an even number), and no other a_j/2 equals it (distinctness).
- For each i with a_i = 2 a_{n+1}: the value a_{n+1} = a_i/2 appears as
  2 (from the two halves of a_i) PLUS 1 (the unsplit a_{n+1}) = 3 times. But
  see Step 3.

So every value v ≠ a_{n+1} appears exactly 2 times — an even number. (No value
a_i/2 with a_i ≠ 2 a_{n+1} coincides with a_{n+1}, by definition; and the
a_i/2 are pairwise distinct, so no two different i's contribute to the same
v ≠ a_{n+1} block.) Hence every block whose value is ≠ a_{n+1} has even size
(exactly 2, but only evenness matters).

**Step 3 — the value a_{n+1} appears an odd number of times.** The value
a_{n+1} appears 1 (the unsplit tail) + 2·#{i ∈ {1,…,n} : a_i = 2 a_{n+1}} times.
Since L is strictly decreasing, the equation a_i = 2 a_{n+1} has at most one
solution i (at most one of the distinct values a_1 > … > a_n equals 2 a_{n+1}).
So the multiplicity of a_{n+1} is 1 (if no i has a_i = 2 a_{n+1}) or 3 (if
exactly one i has a_i = 2 a_{n+1}). Both are ODD.

**Step 4 — the a_{n+1}-block starts at an odd position.** In the sorted order,
the a_{n+1}-block is preceded by blocks whose values are ≠ a_{n+1} (all even
size, by Step 2). The total number of pieces preceding the a_{n+1}-block is the
sum of these even block sizes — an EVEN number. Adding 1 (positions are
1-indexed), the a_{n+1}-block starts at position 1 + (even) = ODD.

**Step 5 — block-contribution formula.** (This is the `block-contribution-formula`
lemma, certified.) A block of size s starting at position p contributes
v · (number of + signs − number of − signs over positions p, p+1, …, p+s−1).
The signs alternate (+, −, +, −, …) by position parity. Over s consecutive
positions:
- If s is even (= 2k): there are k plus-signs and k minus-signs (regardless of
  whether p is odd or even). Contribution = v·(k − k) = 0.
- If s is odd (= 2k+1) and p is odd: the signs are +, −, +, …, + (positions
  odd, even, …, odd). Number of + = k+1, number of − = k. Contribution =
  v·((k+1) − k) = +v.
- If s is odd and p is even: contribution = −v (k plus, k+1 minus).

**Step 6 — assemble.** Every block with value v ≠ a_{n+1} has even size ⟹
contributes 0 (Step 5, even case). The a_{n+1}-block has odd size and starts at
an odd position (Steps 3–4) ⟹ contributes +a_{n+1}·1 = +a_{n+1} (Step 5, odd-
at-odd case). Therefore

$$D(M') \;=\; 0 \;+\; a_{n+1} \;=\; a_{n+1}.$$

Since D* ≤ D(any Xiang strategy) = D(M') = a_{n+1}, we have D*(L) ≤ a_{n+1}. ∎

**Mark budget.** n marks. ✓

**Why the bottom-dominance hypothesis is unnecessary.** The round-5 proof
(`bottom-dominant-halving`, Part IV) relied on the sorted order being exactly
(a_1/2, a_1/2, a_2/2, a_2/2, …, a_n/2, a_n/2, a_{n+1}) — which requires
a_n/2 ≥ a_{n+1} (bottom-dominance) to place a_{n+1} last. The generalized proof
above does NOT use the sorted order's specifics: it uses only (a) the
a_i/2 are pairwise distinct (strictly-decreasing ⟹), (b) every v ≠ a_{n+1}
appears an even number of times, (c) a_{n+1} appears an odd number of times.
The block-contribution formula (Step 5) then forces the unique odd block to
contribute +a_{n+1} (because the even blocks above it force its starting
position to be odd), regardless of where in the sorted order the a_{n+1}-block
actually sits. The bottom-dominance condition was an artifact of the round-5
"adjacent-pair" presentation, not a real hypothesis.

**Edge case a_i = 2 a_{n+1} (handled explicitly).** When some a_i = 2 a_{n+1}
(necessarily a unique i by strict decrease), the value a_{n+1} appears 3 times
(odd, Step 3). The three copies form a single size-3 block (they are equal and
maximal). The blocks above it are all even-sized, so the size-3 block starts at
an odd position; its contribution is +a_{n+1} (Step 5, 2k+1 = 3, k = 1, at odd
start: 2 plus, 1 minus). So D = a_{n+1} still. Verified: (4,2,1)/7 with
a_2 = 2 = 2·1 gives D = 1/7; (6,2,1)/9 with a_2 = 2 = 2·1 gives D = 1/9. ✓

**Numerical verification.** Exact-`Fraction` check, 0 violations / 20000 random
strictly-decreasing configs (n=2..6, random integer configs normalized). All
give D(halving) = a_{n+1}, including configs with a_i = 2 a_{n+1} and configs
far from bottom-dominant (a_n < 2 a_{n+1}). ✓

**Corollary (region closure, all n).** *For every n and every strictly-decreasing
m = n+1 Liu config L with a_{n+1} ≤ 1/D_n, Xiang has ≤ n marks with D ≤ 1/D_n
(namely, halving a_1, …, a_n, giving D = a_{n+1} ≤ 1/D_n).*

*Proof.* By `halving-always-a-nplus1`, D(halving) = a_{n+1} ≤ 1/D_n by
hypothesis. Mark budget n. ✓

This closes the **a_{n+1} ≤ 1/D_n region for all n, unconditionally** — for
strictly-decreasing m = n+1 configs. Combined with GAP-U3 (m ≤ n, D* = 0) and
the repeated-value lemma (m = n+1 with a repeat, D* = 0), the ONLY remaining
open case for the general-n upper bound is the **compressed** case:
strictly-decreasing m = n+1 with a_{n+1} > 1/D_n (Part VII-bis).

---

# Part V — Repeated-value lemma: m = n+1 with a repeat ⟹ D* = 0 (PROVED)

> **Lemma (repeated-value-D-zero).** *For a Liu config L = (a_1 ≥ a_2 ≥ … ≥
> a_{n+1}) with m = n+1 and at least one repeated value (a_i = a_{i+1} for some
> i), Xiang has ≤ n marks forcing D = 0. Hence D*(L) = 0 ≤ 1/D_n.*

**Proof.** By `spine-pair-cancellation` (S1, certified), for any sorted
multiset M, removing all adjacent-equal pairs preserves D: D(M) = D(spine(M)),
where the spine is the strictly-decreasing subsequence (all adjacent-equal
pairs removed).

Since L has at least one repeated value (a_i = a_{i+1}), the spine of L has
m' ≤ n pieces (we removed at least one pair from n+1 pieces, leaving ≤ n−1;
further pairs may be removed, only reducing the count).

**Xiang's strategy: halve every spine piece.** Xiang identifies the spine
(strictly-decreasing subsequence) and halves each spine piece s_j → {s_j/2,
s_j/2}, using m' ≤ n−1 ≤ n marks. The paired pieces (the removed duplicates)
are left unsplit.

**Claim.** *In the refined multiset M', every value appears an even number of
times.*

*Proof of claim.* The refined multiset M' consists of:
- For each spine piece s_j: two copies of s_j/2 (the halves).
- For each pair-group value v (the removed adjacent-equal pairs): 2·p copies
  of v, where p ≥ 1 is the number of pairs removed with value v (even).

Consider any value w in M':
- If w = s_j/2 for some spine piece s_j (and w ≠ v for any pair-group value v):
  the group is {w} with 2 copies (from halving s_j). Since the spine is
  strictly decreasing, s_j are all distinct, so s_j/2 are all distinct: no
  other spine piece contributes w. Size 2 (even). ✓
- If w = v for some pair-group value v (and w ≠ s_j/2 for all j): the group has
  2p copies (even). ✓
- If w = s_j/2 = v for some j and some pair-group value v: the groups merge,
  giving 2 + 2p copies (even). ✓
- If w = s_j/2 = s_k/2 for j ≠ k: impossible, since s_j ≠ s_k (spine strictly
  decreasing) ⟹ s_j/2 ≠ s_k/2.

In all cases, the group size is even. ∎ (claim)

By the even-multiplicity lemma (Part III), D(M') = 0. Since D(M') = D(spine(M'))
by S1 (all pairs cancel), and D*(L) ≤ D(M') = 0, and D ≥ 0 always, we have
D*(L) = 0. ∎

**Mark budget.** m' ≤ n−1 ≤ n marks. ✓

**Numerical verification.** Exact-Fraction check, 10000 random configs with
m = n+1 and at least one repeat (n=2..6), all give D = 0 after halving the
spine. ✓

---

# Part VI — Base cases n = 1, 2, 3 (CERTIFIED, imported)

The direct adaptive strategy recovers the certified base cases; they are NOT
re-derived here.

**n = 1** (`n1-base-both-bounds`, certified): c(1) = 2/3, D* = 1/3 = 1/D_1.

**n = 2** (`n2-upper-bound-complete`, `n2-max-bound`, certified): c(2) ≤ 4/7,
D* ≤ 1/7 = 1/D_2 for every m ≤ 3 config. Tower T_2 unique equality.

**n = 3** (`v3-upper-bound`, certified): D* ≤ M_2/4 for every m ≤ 4 config.
Combined with the regime closure (Part VIII of round 4), D* ≤ 1/15 = 1/D_3 for
every n=3 config. The V(3) proof's two-case split (dominant → halve a_1;
non-dominant → pair a_1) IS the direct strategy's P1/P2 at n = 3:
- The halving move (V(3) Case 1) is the bottom-dominant halving (Part IV) at
  n = 3, but applied to the TOP (a_1 ≥ 2 a_2 is top-dominant, not bottom-
  dominant). The V(3) proof halves a_1 (the largest), not the n largest. This
  is a DIFFERENT halving from Part IV. The V(3) proof then applies the n=2
  Max-bound on the rest — an inductive reduction (which works at n=3 because
  the n=2 base is certified). The direct strategy (Part IV) halves ALL n largest
  at once — a non-inductive move that gives D = a_{n+1} directly. Both are
  valid halving strategies; V(3) uses the inductive one (certified), the direct
  strategy uses the non-inductive one (Part IV).

So n = 1, 2, 3 are CLOSED (certified). The direct strategy is the general-n
extension.

---

# Part VII-bis — GAP-U2-compressed: the remaining open case (round 6 narrowing)

> **GAP-U2-compressed (open, round 6 — strictly narrower than GAP-U2).**
> *For a strictly-decreasing Liu config L = (a_1 > a_2 > … > a_{n+1}) with
> m = n+1 (all distinct) and **a_{n+1} > 1/D_n** (the "compressed" case — the
> smallest piece exceeds the target 1/D_n), exhibit a ≤ n-mark Xiang strategy
> with D ≤ 1/D_n.*

**Why GAP-U2 has narrowed to GAP-U2-compressed.** The round-5 statement of
GAP-U2 had two sub-cases: (a) non-bottom-dominant (a_n < 2 a_{n+1}), and (b)
bottom-dominant with a_{n+1} > 1/D_n. The generalized halving lemma
(`halving-always-a-nplus1`, Part IV-bis) closes BOTH sub-cases whenever
a_{n+1} ≤ 1/D_n (halving gives D = a_{n+1} ≤ 1/D_n directly, regardless of
bottom-dominance). So the ONLY remaining open case is the compressed case
a_{n+1} > 1/D_n — which is strictly narrower than GAP-U2 (it excludes the
generic non-bottom-dominant regime with a_{n+1} ≤ 1/D_n).

**Why the proved lemmas don't close the compressed case.**
- GAP-U3 (Part III) needs m ≤ n; here m = n+1. ✗
- The halving lemma (`halving-always-a-nplus1`, Part IV-bis) gives D = a_{n+1},
  but here a_{n+1} > 1/D_n ⟹ the halving bound OVERSHOOTS the target. The
  halving bound is an UPPER bound on D*; the actual D* may be much smaller
  (via piece-matching strategies), but halving itself does not certify D* ≤
  1/D_n here. ✗
- The repeated-value lemma (Part V) needs a repeated value; here all distinct. ✗

**O1 (split-bottom + exact-pair-rest) is PROVABLY DEAD.** The round-6 outline-
reviewer proved that exact pairing of {a_1, …, a_n, a_{n+1} − x} into n equal
pairs (the O1 target) is IMPOSSIBLE for the compressed config (5,3,2)/10 (n=2)
for ALL x ∈ (0, 1/D_n] and ALL 9 split/pairing patterns — the obstruction is
structural (the rest has three distinct values; forming two equal pairs forces
x = 0 or x < 0 or x > 1/D_n in every case). Moreover, the "pairing feasibility
as a piecewise-linear function of x" is a category error: pairing feasibility
is a discrete 0/1 indicator, not a continuous PL function, so the IVT argument
(step 6 of the round-5 O1 outline) has no continuous function to apply IVT to.
O1 is NOT retried. (The bounded-spread pigeonhole fallback, which also bottoms
on the same subset-sum existence, is likewise not a viable close; see below.)

**Candidate mechanism 1 — O2 (split-LARGE-to-match-MEDIUM).** The empirically-
winning D-small move in the compressed case splits LARGE pieces to create ties
with MEDIUM pieces (not the bottom-up cascade). Witness (the spread config
(0.6, 0.2, 0.1, 0.055, 0.045)/1, m = 5 = n+1 with n = 4): split a_1 = 0.6 →
{0.2, 0.2, 0.2} (2 marks, creating three copies of 0.2 that, together with the
existing a_2 = 0.2, give four 0.2's — even) AND split a_3 = 0.1 → {0.055, 0.045}
(1 mark, matching a_4 = 0.055 and a_5 = 0.045 — two pairs). Result: every value
appears an even number of times ⟹ D = 0. Mark budget 2 + 1 = 3 ≤ n = 4. ✓

For n = 2 compressed (5,3,2)/10: split a_1 = 1/2 → {a_3 = 1/5, a_1 − a_3 =
3/10} (1 mark, tie at a_3) and a_2 = 3/10 → {eps, 3/10 − eps} (1 mark). Refined
= {3/10, 3/10 − eps, 1/5, 1/5, eps}; the two 1/5's cancel (a size-2 block), and
D = (3/10) − (3/10 − eps) + (1/5) − (1/5) + eps = 2·eps → 0 as eps → 0. So the
INFIMUM of D is 0 (not attained — parity: 2n+1 = 5 is odd ⟹ D ≠ 0 for any
positive-piece refinement; the inf is approached but not reached). Since
inf D = 0 ≤ 1/7, the upper bound holds for this config. The universal
existence — that for EVERY compressed config some O2-style matching drives the
residual ≤ 1/D_n — is an unproved subset-sum/multiset-equal-sums core (Xiang
chooses the fragment values to create ties; the freedom is large, but a
universal existence proof is not known).

**Candidate mechanism 2 — bounded-spread pigeonhole (cheap-kill fallback).**
The compressed hypothesis a_{n+1} > 1/D_n forces compression: since a_i ≥
a_{n+1} > 1/D_n for all i and ∑ a_i = 1, we have a_1 = 1 − ∑_{i=2}^{n+1} a_i
≤ 1 − n·a_{n+1} < 1 − n/D_n = (D_n − n)/D_n. Hence the spread
a_1 / a_{n+1} < D_n − n = 2^{n+1} − 1 − n: all pieces are within a factor
< 2^{n+1} of each other. A pigeonhole/size-bucket argument on this bounded
range MIGHT force a matchable structure (two pieces close enough in value that
a single split of the larger creates a tie). This is a candidate cheap-kill, but
the matching existence (the step from "bounded spread" to "a tie is creatable
within n marks driving D ≤ 1/D_n") is NOT proved — it bottoms on the same
subset-sum existence as O2. Recorded as a fallback, not a close.

**Parity obstruction (negative, from the explorer — designs the target).** With
exactly n marks on a strictly-decreasing m = n+1 config, the refined count is
at most 2n+1 (odd) ⟹ D ≠ 0 always (at least one odd-multiplicity value
survives, by the block-contribution formula). So the compressed case CANNOT be
closed by "D = 0 always via n marks" — parity forbids it. The correct target is
D = small leftover ≤ 1/D_n (a residual odd-multiplicity block whose value is
≤ 1/D_n), NOT full cancellation. The O2 strategy above achieves this for
(5,3,2)/10 (inf D = 0, approached via 2·eps → 0, well under 1/7). The proof
must exhibit, for each compressed config, an n-mark refinement whose unique
odd-multiplicity residual is ≤ 1/D_n.

**What IS verified (numerical, verification-NOT-proof).**
- n = 2 compressed: exact-`Fraction` exhaustive grid search (denominator up to
  2100) over all split/pairing patterns, on (5,3,2)/10, (4,3,2)/9, (6,3,2)/11,
  (5,4,3)/12, (25,16,8)/49 (a_2 − a_3 > 1/7), (32,9,8)/49 (a_1 near 5/7). ALL
  give best D ≤ 1/7 (ratios 0.03–1.0; the worst, (32,9,8)/49, gives
  D = 1/49 < 1/7 exactly). 0 violations.
- n = 3 compressed: exact-`Fraction` grid search (den 142, split a_1, a_2, a_3
  each into 2) on the round-5 "phantom-crux" config (29, 47, 22, 15)/142 gives
  best D = 2/71 < 1/15 (ratio 0.42). Configs that appeared to violate under a
  weak random search were RESOLVED by the grid search (the random search was
  too weak to find the optimum).
- Round-5 breakpoint-restricted exact-`Fraction` search (B1-justified): 0
  violations over 6000+ trials (n = 4, all-configs and crux configs), worst
  ratio 0.52; all integer configs with sum ≤ 28 (4037 configs) 0 violations;
  the 11 round-4 Max-bound violators extended to m = 5 all give D* = 0 or
  D* = 1/sum < 1/31; tower and near-tower configs (sum 31–65) T_4 unique max
  (ratio 1.000), every perturbation of the tower drops D* to 0.

The claim D* ≤ 1/D_n in the compressed case is strongly supported but NOT
proved. The open core is the universal piece-matching existence: for every
compressed strictly-decreasing m = n+1 config, an n-mark refinement whose
unique odd-multiplicity residual block has value ≤ 1/D_n.

**Status.** GAP-U2-compressed is the primary open hard step. O1 is dead; O2
and bounded-spread are honest candidate mechanisms. Numerics strongly support
the claim (0 violations over 6000+ trials n=4, exhaustive n=2); a proof is not
known. The halving lemma + region closure (Part IV-bis) is the certified
progress this round; the compressed case is the honest GAP.

---

# Part VIII — Closure: what is proved unconditionally for general n

**Theorem (partial upper bound, unconditional).** *For every n and every Liu
config L = (a_1 ≥ … ≥ a_m), m ≤ n+1, Xiang has ≤ n marks with D ≤ 1/D_n, in the
following cases:*

1. ***m ≤ n*** *(any config):* D* = 0 ≤ 1/D_n. *(GAP-U3, Part III, proved.)*
2. ***m = n+1 with a repeated value*** *(a_i = a_{i+1} for some i):*
   *D* = 0 ≤ 1/D_n. *(Repeated-value lemma, Part V, proved.)*
3. ***m = n+1, strictly decreasing, with a_{n+1} ≤ 1/D_n*** *(no bottom-
   dominance hypothesis):* D* ≤ a_{n+1} ≤ 1/D_n. *(Generalized halving lemma
   `halving-always-a-nplus1`, Part IV-bis + condition, proved round 6.)* This
   sub-case includes the dominant tower-tail family (a_1 ≥ 2^n a_{n+1},
   geometric bottom), with the tower T_n as the tight member (D* = 1/D_n, by
   `parallel-halving-saturates-tower`), AND the entire non-bottom-dominant
   regime whenever a_{n+1} ≤ 1/D_n.

*The remaining case (GAP-U2-compressed, Part VII-bis) is OPEN: m = n+1,
strictly decreasing, with **a_{n+1} > 1/D_n**.*

**Proof of the theorem.** Case 1: by GAP-U3 (Part III), Xiang halves all m ≤ n
pieces, getting D = 0 ≤ 1/D_n. Case 2: by the repeated-value lemma (Part V),
D* = 0 ≤ 1/D_n. Case 3: by `halving-always-a-nplus1` (Part IV-bis), D* ≤
a_{n+1}, and a_{n+1} ≤ 1/D_n by hypothesis. ✓

**Combined with the certified base (n = 1, 2, 3):**
- n = 1: c(1) ≤ 2/3 = 2^1/D_1. (Certified.)
- n = 2: c(2) ≤ 4/7 = 2^2/D_2. (Certified.)
- n = 3: c(3) ≤ 8/15 = 2^3/D_3. (Certified.)
- n ≥ 4: c(n) ≤ 2^n/D_n holds in cases 1–3 above (unconditional);
  GAP-U2-compressed (a_{n+1} > 1/D_n) open.

---

# Part IX — Conditional closure (if GAP-U2-compressed is resolved)

**Theorem (upper bound, conditional on GAP-U2-compressed).** *If
GAP-U2-compressed (Part VII-bis) is resolved — i.e., for every strictly-
decreasing m = n+1 config with a_{n+1} > 1/D_n, Xiang has ≤ n marks with
D ≤ 1/D_n — then D*(n) ≤ 1/D_n for all n, with equality iff the Liu config
is the tower T_n.*

**Proof (conditional).** For any Liu config L:
- m ≤ n: D* = 0 ≤ 1/D_n (GAP-U3). ✓
- m = n+1 with a repeat: D* = 0 ≤ 1/D_n (repeated-value lemma). ✓
- m = n+1, strictly decreasing, a_{n+1} ≤ 1/D_n: D* ≤ a_{n+1} ≤ 1/D_n
  (`halving-always-a-nplus1`). ✓
- m = n+1, strictly decreasing, a_{n+1} > 1/D_n: D* ≤ 1/D_n
  (GAP-U2-compressed, assumed). ✓

So D* ≤ 1/D_n for every Liu config. Equality D* = 1/D_n requires:
- Not cases 1, 2 (D* = 0 < 1/D_n).
- Case 3 with a_{n+1} = 1/D_n AND D* = a_{n+1} (halving tight). The halving
  is tight iff the config is the tower-tail family with S = D_n, i.e., the
  tower T_n itself (by `parallel-halving-saturates-tower`, D(T_n) = 1/D_n;
  any other tower-tail has S > D_n, strict). And in case 4 (compressed),
  a_{n+1} > 1/D_n ⟹ if GAP-U2-compressed holds, D* ≤ 1/D_n < a_{n+1}, strict.

So equality iff T_n. ∎ (conditional on GAP-U2-compressed)

---

# Part X — Answer and verification

**Candidate answer** (`closed-form-answer`): c(n) = 2^n/(2^{n+1} − 1) = 2^n/D_n.

**Verification by substitution.** c(n) = 2^n/D_n; the relation c(n) = (1 + D*)/2
with D* = 1/D_n gives (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) =
2^n/D_n = c(n). ✓ Checked exactly:

| n | D_n | 1/D_n | c(n) = 2^n/D_n | (1+1/D_n)/2 |
|---|-----|-------|----------------|-------------|
| 1 | 3   | 1/3   | 2/3            | 2/3 ✓       |
| 2 | 7   | 1/7   | 4/7            | 4/7 ✓       |
| 3 | 15  | 1/15  | 8/15           | 8/15 ✓      |
| 4 | 31  | 1/31  | 16/31          | 16/31 ✓     |

**Upper bound** (Xiang ≤ c(n)): this file.
- n = 1: PROVED (imported, `n1-base-both-bounds`).
- n = 2: COMPLETE (imported, `n2-upper-bound-complete`, certified).
- n = 3: PROVED (imported, `v3-upper-bound`, certified; all four regimes closed
  unconditionally).
- n ≥ 4: PARTIAL. Cases 1–3 (Part VIII) closed unconditionally:
  m ≤ n (D* = 0); m = n+1 with a repeat (D* = 0); m = n+1 strictly-decreasing
  bottom-dominant with a_{n+1} ≤ 1/D_n (D* ≤ a_{n+1} ≤ 1/D_n). GAP-U2 (Part VII)
  open: m = n+1 strictly-decreasing with **a_{n+1} > 1/D_n** (compressed).
  O1 (exact pairing) is PROVABLY DEAD; O2 (split-LARGE-to-match-MEDIUM) and
  bounded-spread pigeonhole are honest candidate mechanisms (verification-
  not-proof: 0 violations over 6000+ trials n=4, exhaustive n=2; NOT proved).

The proof is complete for n ≤ 3; partial for n ≥ 4 (one sub-case open:
GAP-U2-compressed, the strictly-decreasing m = n+1 config with a_{n+1} > 1/D_n,
where the halving bound overshoots and a piece-matching strategy is needed). ∎

---

## Promotable lemmas (candidates for `results/imo-2026-03/lemmas/`)

1. **`halving-always-a-nplus1`** (Lemma, Part IV-bis, NEW round 6) — *For ANY
   strictly-decreasing m = n+1 Liu config (a_1 > … > a_{n+1}), Xiang halves
   a_1, …, a_n (n marks, leaving a_{n+1}). The refined multiset
   {a_1/2, a_1/2, …, a_n/2, a_n/2, a_{n+1}} has: every value v ≠ a_{n+1}
   appearing exactly twice (the a_i/2 are pairwise distinct by strict decrease);
   a_{n+1} appearing 1 + 2·#{i : a_i = 2 a_{n+1}} times (odd — at most one such
   i by strict decrease). All blocks above the a_{n+1}-block are even-sized ⟹
   the a_{n+1}-block starts at an odd position ⟹ it contributes +a_{n+1}
   (block-contribution formula: odd size at odd start gives net +1); every even
   block contributes 0. Hence D = a_{n+1}.* Fully proved (Part IV-bis),
   unconditional, no bottom-dominance hypothesis. **Generalizes
   `bottom-dominant-halving` (drops a_n ≥ 2 a_{n+1}).** **Corollary: the
   a_{n+1} ≤ 1/D_n region is CLOSED for all n** (halving gives D = a_{n+1} ≤
   1/D_n directly). Verified 0/20000 exact-Fraction trials (n=2..6). NEW round 6.
   **Submit for certification.**

2. **`m-le-n-halving-D-zero`** (Lemma, Part III, round 5, already certified) —
   *For any Liu config with m ≤ n pieces, Xiang halves every piece; the refined
   multiset has every value appearing an even number of times; by the even-
   multiplicity lemma (each even block of 2k equal values contributes v·(k−k) =
   0 to D), D = 0. Hence D* = 0 ≤ 1/D_n.* Already certified. (Kept for
   cross-reference; the even-multiplicity lemma / block-contribution formula
   is the engine behind both `m-le-n-halving-D-zero` and
   `halving-always-a-nplus1`.)

3. **`bottom-dominant-halving`** (Lemma, Part IV, round 5, already certified) —
   *For m = n+1 with a_n ≥ 2 a_{n+1} (bottom-dominant), halving the n largest
   pieces gives D = a_{n+1}.* Already certified. **Now a COROLLARY of
   `halving-always-a-nplus1`** (the bottom-dominance hypothesis is unnecessary).
   No re-certification needed; the generalization supersedes it.

4. **`repeated-value-D-zero`** (Lemma, Part V, round 5, already certified) —
   *For m = n+1 with a repeat, D* = 0.* Already certified. (Kept for
   cross-reference.)

5. (Prior, kept certified: `v3-upper-bound`, `n2-max-bound`,
   `n2-upper-bound-complete`, `parallel-halving-saturates-tower`,
   `pl-breakpoint-minimum`, `spine-pair-cancellation` — already in
   `results/imo-2026-03/lemmas/`.)

6. (Prior REDUCTION files, kept as conditional: `max-bound-dominant`,
   `max-bound-pairing-small-third` — conditional reductions on the refuted
   Max-bound IH W(n−1); valid only for n ≤ 3 where W(≤2) is TRUE. NOT promoted.)
