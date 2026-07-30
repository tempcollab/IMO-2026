# Proof-reviewer report — imo-2026-03, Round 14

Two builds reviewed. BOTH builders ran their mandatory numeric gates FIRST, both gates FAILED (the
proposed closing levers do not exist), and both correctly shipped NO prose proof — instead honest,
rigorous refutations plus positive structural deliverables. I adversarially re-verified every
load-bearing claim by independent computation. Neither wall is closed; Status stays `partial`.

---

## Approach 1: merge-interleave-pattern (LOWER wall) — VERDICT: RETHINK

### Recorded builder Status: PARTIAL. My judgement: the R14 lever is DEAD → RETHINK.

**Load-bearing refutations — independently verified (exact integer arithmetic):**

- **R14a (no ±1-equality Farkas certificate).** Witness `F={6,6,4}`, tail level-3 split `{3,3,2}`,
  sorted `{6,6,4,4,3,3,2,2,1}`. Verified: `L_T = 1`, `max = 6 < 8` (box-interior, so complementary
  slackness kills box multipliers and DUAL-CHAR applies). The signed-power equation
  `Σ ε_k·{16,8,4,2,1} = 1` has the UNIQUE `±1` solution `(+,−,−,−,−)` (my brute force confirms: only
  solution). That forces `Σ y_g|g| = +3 − 6 = −3 ≠ [9 odd] = 1`. Contradiction — airtight. ✓
- **R14b (odd-block collapse false).** Witness `{6,6,4,4,4,4,2,1}`: verified `L_T = 1`, box-free,
  block sizes `[2,4,1,1]` → two odd singleton blocks `{2},{1}`. ✓ One odd block has value 2, so the
  "odd residual pinned to value 1" conjecture is also dead.

**DUAL-CHAR** (box-free chain-certificate characterization) is a correct Farkas identity by
coefficient matching + telescoping; I re-derived it. But it is, by strong LP duality, **loss-free
equivalent to GAP-EXTR** — a reframing, not a reduction. The builder's diagnosis is correct and
honest (no overclaim).

**Why RETHINK, not CHANGES REQUESTED.** This is the SECOND lever to die inside the same
vertex-polytope framing (ONE-REC-tightness, R12; LP-dual/sparse-Farkas, R14), and the diagnosis is
structural: certificate-existence IS GAP-EXTR restated, so no lever *within this framing* can make
sub-progress — every candidate is the target reworded. This matches the ballot-matching precedent
(R11): when a slug's own distinct mechanism dies even though its imported reduction stands, route
RETHINK. The certified reduction VERT-LOW+BLK+ATT survives in the lemma cache regardless. The wall
needs a genuinely NEW lower mechanism from the outliner — NOT another restatement of "min L_T over
the vertex polytope." (Builder's own recommendation concurs.)

**Scores:** Correctness 5/5 (refutations verified exact), Rigor 5/5 (no fake prose, honest
diagnosis), Progress 2/5 (de-risked GAP-EXTR to n=5, killed a lever/sub-family, but no gap closed
and the framing is exhausted).

**True Status: unsolved-as-set-up (partial overall — GAP-EXTR remains the open true lower crux).**

---

## Approach 2: breakpoint-vertex (UPPER wall) — VERDICT: CHANGES REQUESTED

### Recorded builder Status: PARTIAL. My judgement: CONCUR — partial, real deliverable, gap open.

**Load-bearing claim — Lemma VALLEY-TIGHT — independently verified.** Family
`A^{(n)} = {2^n,…,4,3,2}/(2^{n+1}+1)`.

- Valley membership: `a_1 = 2^n/(2^{n+1}+1) < 1/2` ✓; `a_2 = 2^{n-1}/(2^{n+1}+1) < β_n =
  2^{n-1}/(2^{n+1}-1)` ✓.
- I computed the **FULL tree-realizable reachable set** (all differencing trees over all nonempty
  subsets, not just the descending caterpillar) at `n=3,4,5`: `0` is NOT reachable, and the minimum
  positive reachable value is exactly `1` (integer). So the true forced minimum is
  `Φ = 1/(2^{n+1}+1)`, giving `Φ/u_n = (2^{n+1}-1)/(2^{n+1}+1)` = `0.882, 0.939, 0.969, 0.985,
  0.992, 0.996` at `n=3..8`, monotone → 1. ✓ (I checked more than the descKK fold — the min over the
  entire reachable set is still 1, so the claim is not a caterpillar-only artifact.)

**Consequence is sound and important (a genuine NEGATIVE result):** `M*_valley/u_n → 1`, so the
valley residual is asymptotically as tight as the full upper bound. NO margin exists → every crude /
margin-based / non-tight valley bound is provably dead for large `n`, and the prior "worst 0.75"
figure was an under-sampling artifact. This also kills the valley-differencing-construction hedge's
robustness premise.

**Lemma DSUM (unsound) was correctly DROPPED** — not certified, not present. Good.

**Why CHANGES REQUESTED, not RETHINK.** Unlike the lower slug, the breakpoint-vertex framing's
core is a certified, TRUE reduction (R-UV / FGR / R-COV' sufficiency) to a genuinely distinct open
object — the first-gap / Subset-KK pigeonhole `min_{∅≠T} descKK(T) ≤ u_n`, a min-of-distances
discrepancy claim with its own attack surface. Only this round's specific closing lever
(extremal-tie margin bound) died; the reduction and residual stand and the residual is TRUE. The
approach stays live; it needs a genuinely TIGHT (not margin) lever. VALLEY-TIGHT is real forward
information constraining what can work.

**Scores:** Correctness 5/5 (VALLEY-TIGHT verified on the full reachable set), Rigor 5/5 (no fake
proof, unsound DSUM dropped), Progress 3/5 (decisive lever-family kill + certifiable near-extremal
family; residual open but sharper).

**True Status: partial (gap: prove the first-gap pigeonhole via a tight, non-margin argument).**

---

## Lemmas certified this round (→ 29 total)
- `lemmas/valley-tight.md` — VALLEY-TIGHT (verified on FULL reachable set n=3,4,5: 0 unreachable,
  Φ=1/(2^{n+1}+1), ratio→1).
- `lemmas/dual-char.md` — DUAL-CHAR (box-free chain-certificate characterization) + refutations
  R14a, R14b (both reproduced exact). Recorded as structural fact + dead-mechanism record.

## current.md
Updated: Status stays `partial`; R14 refuted levers under Approaches tried; confirmed facts (GAP-EXTR
at n=5, VALLEY-TIGHT tightness) and both verdicts under Current best. Neither wall claimed closed.

## Outcomes recorded (ranking tool)
- merge-interleave-pattern: `dead-end` (LP-dual lever dead, framing is a reframing → RETHINK).
- breakpoint-vertex: `partial` (extremal-tie lever refuted, VALLEY-TIGHT certified, residual open).
