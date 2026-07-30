# Outline review — imo-2026-03, round 13

Two live vehicles, one per wall (single-gap trap respected). Both are `advance` on a certified
residual, each re-planned with a genuinely NEW binding lever. f-partition-majorization correctly
HELD. I confirmed each lever does not silently re-enter one of the FOUR exhausted families
(scalar-reserve, structured transport/matching, dispersion/density/COUNT, covering-radius).

---

## merge-interleave-pattern (LOWER, GAP-EXTR) — APPROVE (build), with mandatory gate

Verdict: APPROVE. The strategy is a vertex-restricted PEEL + minimal-counterexample induction over
the FINITE vertex family P_T, driven by BLK's box-face dichotomy and certified Lemma TB. This is a
GLOBAL vertex→smaller-vertex reduction, not a scalar/local monovariant — exactly the shape the R10/R11
lower-lever refutations said any survivor must have. Cross-checks:

- NOT scalar-reserve/potential (R10 dead) — no running Φ.
- NOT structured transport/matching (R11 dead) — no Hall/debit-credit certificate.
- NOT prefix/termwise monovariant (R8 dead) — the peel compares a whole vertex to a whole smaller-n
  vertex.
- NOT ONE-REC-tightness (R12 refuted non-binding) — explicitly avoided; the outline warns against
  reintroducing ONE-REC as a facet (correct: it is implied by (E)+positivity inside a fixed P_T).
- NOT f-partition single-gap localisation (R12 refuted) — different object (vertex peel, not B-cut
  support).
  So the lever is genuinely new. Good.

Sound-skeleton check:
- Step 1 (block-parity reduction, L_T = alternating sum of odd-multiplicity distinct values): correct
  mechanism — even-length equal-value blocks are certified Lemma-P cancelling pairs (net 0), odd-length
  blocks toggle running-position parity. This is provable now and should be certified as its own lemma.
  Caveat (explorer-flagged, agreed): it re-expresses MID-core's μ{g odd} content in vertex language —
  it is the target restated on a finite object, NOT itself a closure. The closure must come from the
  peel (step 3) + generic characterization (step 4). Do not let the builder mistake step 1 for progress.
- Step 3 (GAP-EXTR-PEEL, top-box case, load-bearing): mechanism stated with a reason (TB splits
  D=e+D_low at 2^{n-1}; a pinned top block is a cancelling pair δ=0 or an unpaired top value δ≥2^{n-1}≥1;
  residual coordinates still satisfy lower-scale group-sum equalities → a genuine smaller-n vertex).
  Plausible and non-circular. The real risk the outline itself names: the δ must be tracked EXACTLY —
  a crude δ≥0 that loses the "−1" is fatal (same failure mode as the old D(S')≤max bound). The builder
  MUST nail the type/budget re-indexing that P_{T'} is a valid MID-core type at n−1.
- Step 4 (GAP-EXTR-GEN, generic box-free vertex = canonical ATT layout, telescopes to 1): this is the
  weakest link — the "box-free ⇒ one-fragment-per-dyadic-scale" characterization is CONJECTURE. The
  explorer confirms worst vertices at n=3,4 are ATT permutations but n=5 is UNVERIFIED. Superincreasing
  argument (2^j > Σ_{i<j}2^i forbids cross-group straddle) is a reasonable mechanism but not yet a proof.

Required before prose (mandatory numeric gate, per standing rule that killed a bad recursion each of
R9–R12): machine-check at n=5 that every box-free (p=n+1) vertex is a canonical ATT-permutation layout
(the explorer's exact conjecture). If false, step 4 must be re-planned before building it.

Do NOT re-run: the cheap-kill (min L_T=1, no sub-1 vertex n=3,4 — already passed/reproduced) or the
VERT-LOW/BLK/ATT derivations (certified).

## breakpoint-vertex (UPPER, first-gap pigeonhole μ_{n+1}≤u_n) — APPROVE (build), with mandatory gate

Verdict: APPROVE. The residual μ_{n+1}=min_i dist(a_i,R_{i−1}) ≤ u_n L is certified-reduced (FGR +
R-COV' sufficiency) and I re-confirmed it numerically (0 fails, worst ratio 0.80 over ~15k exact valley
profiles n=2..6). The proposed lever is a seeded/existential strong induction SEED(p) + a mass-telescope
discrepancy that charges each "far" piece against Σa_i=L. Cross-checks:

- NOT a covering-radius / max-gap bound (one-cap R10, two-cap R12 — whole family dead): the telescope
  charges against the SUM, sees the FIRST (min) gap, never the max gap. Distinct. Good.
- NOT set-count/density pigeonhole on R_{n+1} (R11 dead — |R|=2 on all-equal): the density backup is
  explicitly LOCAL near 0 using small a_i as digits, not a global count.
- NOT a fixed deterministic greedy recursion (R9 dead, ≤11.4× overshoot): the IH is EXISTENTIAL (some
  2-move fold exists), consuming ≥2 moves before invoking IH (Lemma VS forces this). Distinct.
- NOT a bounded-depth escape skeleton (R10 dead, depth Θ(n)): SEED(p) recurses the full remaining budget.
  So the lever is genuinely new/incomparable to the four dead families. Good.

Concern to flag (not a rejection): the mass-telescope inequality "¬(some dist(a_i,R_{i−1}) ≤ u_n L) ⇒
Σa_i > L" is the make-or-break, and it is the LEAST obviously-true step — u_n L is exponentially small,
so "every a_i is > u_n L from R_{i−1}" is a weak hypothesis and it is not yet clear it forces Σ>L. The
exact charging constant against the two caps is the entire content. This is honestly labelled GAP-TELE.
Likewise SEED(p): the outline itself concedes "12 rounds of induction attempts failed on exactly this
parametrization" — the seed threshold + mass scaling + seed-domination invariant is unproven.

Required before prose (mandatory numeric gate — this is the same gate that killed R9–R12 recursions in
one round each): exact-fraction machine-check the SEED(p) statement (seed threshold, mass M, the
seed-domination invariant making SEED(p−2) a legal IH) AND the GAP-TELE inequality on hundreds of valley
profiles per n=2..7, and verify the budget arithmetic (BL's k moves + 2/level ≤ n total). If the SEED
scaling or TELE constant fails the check, the builder must report the refutation (not dress a fake
proof), exactly as prior rounds did.

The mechanism must be TIGHT at the dyadic ladder (equality μ_{n+1}=u_n) — any "generic +ε slack"
argument is automatically wrong. The outline states this correctly.

---

## f-partition-majorization — HELD (correct; do not build)

GAP B-MONO's single-gap localisation is still the refuted R12 premise, not repaired this round. c_B=0
is not WLOG (42.8% of B-cuts strictly lower D at n=5). Correctly kept in the population, out of the
build set.

## Diversity note (for the orchestrator)

The field is healthy on the "one vehicle per wall" axis but structurally fragile: both walls sit on a
SINGLE lever each, and FOUR families are already dead. The two new levers are genuinely distinct from
the dead families and from each other, so this is not a shared-wall collapse. BUT if BOTH numeric gates
this round refute the SEED/TELE scaling (upper) and the box-free characterization (lower), escalate: per
the standing WATCH, put ≥1 explorer on a potential-free/LP-duality extremal re-derivation of the minimax
attacking BOTH walls at once, rather than a fifth variant of the current objects. The LOWER opening-4
(explicit LP-dual certificate λ with Σλ·(constraint) ≤ L_T−1) is a cheap parallel probe worth having the
builder run computationally — a valid dual point would close GAP-EXTR outright without the induction.

## Ranking (folded)

Cleared stale flags on both live vehicles. Anchored to last outcomes: both live advancing vehicles beat
the dead-family stalled leader parity-measure (family dead R10, cannot advance) and the dead-end
ballot-matching / induction-peel-lever. breakpoint-vertex retains the top slot (more certified machinery,
cleaner residual reduction) over merge-interleave. Result: breakpoint-vertex 1748 (leader),
parity-measure 1677 (demoted, dead family), smoothing-majorization 1527, merge-interleave 1524,
induction-peel 1516, f-partition 1493, ballot-matching 1432, subset-sum-pigeonhole 1376. No new slug to
register (both keep existing slugs); no copy requested.

build set: merge-interleave-pattern, breakpoint-vertex
