# Proof review — round 12, imo-2026-03

Two approaches reviewed independently. Neither claims `solved`; both builders reported `partial`
honestly. My adversarial checks confirm both are `partial` with real, verified progress. Both →
CHANGES REQUESTED. 5 lemmas certified (27 total).

---

## Slug 1 — merge-interleave-pattern (LOWER wall)

**Verdict: CHANGES REQUESTED. True Status: partial.** Builder's recorded status (partial) is correct;
no overclaim.

**What I verified independently.**
- **Cheap-kill actually done and PASSED.** The mandated vertex/LP cheap-kill was run: min D = 1 for
  n=3 (5 F-types), n=4 (21 F-types), NO vertex with L_w < 1. I independently reproduced min D = 1 on
  finer rational grids (n=2 den 6 → 199 refs; n=3 den 3 → 1166 refs) — no sub-1 vertex. The refutation
  branch did not trigger; the approach is NOT refuted.
- **GAP-EXTR correctly stated** as "min L_w ≥ 1 at every vertex," NOT the over-stated "every vertex
  canonical value 1." The builder explicitly refuted the constant-value reading (D varies across words;
  Case (a) gives D=2^{n-1}) and the integrality shortcut (non-integer vertices exist, all >1). Correct.
- **VERT-LOW reduction is sound.** I re-derived the load-bearing step: within a fixed type T the word
  σ is a valid descending order (enforced by (O)), so D = L_T on all of P_T (equal/zero coords sit at
  consecutive/bottom positions and contribute 0, so μ{N odd} agrees with the alternating sum including
  at ties/degenerate points). Enlarging to the closed polytope only lowers the min, so
  min-over-vertices ≥ 1 ⇒ every genuine refinement ≥ 1; the converse holds by continuity of D. The
  Fundamental-Theorem-of-LP step is standard. Sound and rigorous.
- **Tight attainment (Lemma ATT) verified exactly** for n=2..6: B=C_{n-1}, F={2^{n-1},…,2,1,1} gives
  merged multiset with cancelling pairs + triple-1 → D = 1. Confirms minimax D = u_n, lower bound tight.
  (n=1 excluded correctly — |F|≥3 needs n≥2.)

**The remaining gap (name the step).** GAP-EXTR for general n: every vertex of every P_T has L_T ≥ 1.
It is **loss-free equivalent to MID-core** — the vertex reduction reframes and sharpens (finite,
block-structured, ≤ n+2 distinct dyadic values per vertex) but does NOT close it. Moreover the builder
correctly flags that the outline's proposed *mechanism* to close GAP-EXTR ("ONE-REC tightness at a
vertex forces the spread") is UNSUPPORTED: ONE-REC is an automatic consequence of (E)+positivity, not
a binding facet whose tightness could force anything. So the closing lever is still missing.

**Certified:** VERT-LOW (`vertex-reduction-lower`), BLK (`vertex-block-structure`), ATT
(`midcore-attainment`). All three rigorous and reusable.

**Scores.** Correctness 9/10 (all written claims valid). Completeness 4/10 (reduction only; GAP-EXTR
open). Progress: modest — a sound finite reframing of MID-core + de-risking (n≤4) + tightness, but no
new closure. The LOWER wall still terminates at MID-core (convergence risk persists).

**Goal Progress (LOWER):** merge-interleave-pattern Elo 1454, Status partial (advanced). MOVED:
cheap-kill passed (min D=1, no sub-1 vertex n≤4); 3 lemmas certified (VERT-LOW/BLK/ATT); lower bound
proven tight for all n. STILL OPEN: GAP-EXTR (= MID-core), no closing lever — outline's ONE-REC
mechanism refuted as non-binding.

---

## Slug 2 — breakpoint-vertex (UPPER wall)

**Verdict: CHANGES REQUESTED. True Status: partial.** Builder's recorded status (partial) is correct.
The builder's own routing note recommends RETHINK *for the covering-radius mechanism* — I agree the
mechanism is dead, but the slug itself keeps a correctly-stated, verified next target, so the approach
stays live: CHANGES REQUESTED (not RETHINK).

**What I verified independently.**
- **GATE FAILED honestly.** GAP TWO-CAP (two-cap covering-radius contraction to u_n) is REFUTED:
  max-gap/u_n saturates at 3–5·u_n (worst 3.2×…24.6× for n=3..7), exactly the R10 one-cap saturation.
  The whole covering-radius family (one-cap R10 + two-cap R12) is now pruned. The builder did NOT ship
  a fake covering-radius proof.
- **Lemma FGR is correct.** I re-derived μ_i = min(μ_{i-1}, dist(a_i,R_{i-1})) from the reachable-set
  recursion and verified numerically (0 failures over 2000+ exact valley profiles, n=2..6). Clean and
  exact.
- **μ_{n+1} ≤ u_n (the sharpened residual) is robustly true.** Verified 0 fails over 1262 exact valley
  profiles, worst 0.75; tight at the dyadic boundary. The residual is correctly localised as the
  first-gap pigeonhole.
- **R-COV' — sufficiency direction rigorous; converse is NOT.** The USED direction (μ_{n+1} ≤ u_n ⟹
  Xiang forces D ≤ u_n, realized in exactly n cuts via ESF-2, T=∅ excluded) is correct and load-bearing.
  The converse ("upper bound ⟹ μ_{n+1} ≤ u_n") as written is loose — it conflates the full
  achievable-leftover set R(A) (all differencing trees, Lemma RL) with the descending include/skip
  family R_{n+1}, whose min positive value can exceed min R(A). I tested this: no valley counterexample
  arises only because μ_{n+1} ≤ u_n is always true there, so the biconditional holds vacuously-truly,
  not by proof. **I certified only the sufficiency direction** and explicitly flagged the converse as
  non-rigorous in the lemma file. This does not affect the proof program (only sufficiency is needed).

**The remaining gap (name the step).** The **first-gap pigeonhole**: prove μ_{n+1} = min_i
dist(a_i, R_{i-1}) ≤ u_n profile-independently. This is a global, adaptive discrepancy claim on the
coupled sequence (a_i, R_{i-1}) — NOT a covering radius, NOT a fixed-level bound (both dead). The
covering-radius vehicle is exhausted; the mechanism must pivot.

**Certified:** FGR (`first-gap-recursion`), R-COV' (`covering-value-reduction`, sufficiency only).

**Scores.** Correctness 9/10 (FGR exact; R-COV' sufficiency valid; converse correctly not relied on).
Completeness 4/10 (reduction only; first-gap pigeonhole open). Progress: real — the residual is
sharpened from a saturating covering radius to the correct first-gap target, plus a rigorous negative
retiring the covering-radius family, plus two verified lemmas.

**Goal Progress (UPPER):** breakpoint-vertex Elo 1719, Status partial (advanced). MOVED: GAP TWO-CAP
refuted (covering-radius family DEAD); 2 lemmas certified (FGR, R-COV'); residual correctly re-stated
as first-gap pigeonhole μ_{n+1} ≤ u_n (verified robustly true). STILL OPEN: the first-gap pigeonhole —
covering-radius vehicle exhausted, needs a genuinely new discrepancy lever (hand to outliner).

---

## Summary line for orchestrator

- merge-interleave-pattern: CHANGES REQUESTED / partial (advanced). 3 lemmas certified.
- breakpoint-vertex: CHANGES REQUESTED / partial (advanced). 2 lemmas certified; covering-radius
  mechanism dead — flag to outliner.
- 27 certified lemmas total. No APPROVE. Both walls still open; both this round's mechanisms exhausted
  but each leaves a correct sharper residual (LOWER: GAP-EXTR = MID-core; UPPER: first-gap pigeonhole).
