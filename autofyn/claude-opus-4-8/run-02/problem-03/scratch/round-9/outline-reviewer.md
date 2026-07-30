# Outline Review — imo-2026-03 (Round 9), GAP L (lower bound)

Sole open wall: `D̃(F) ≥ 1` for every feasible refinement `F = ⊎_{j=0}^n π_j` of the dyadic
ladder with `Σa_j ≤ n`, grand total `2^{n+1}−1`. Upper bound is DONE/certified — untouched.
Field: two far-apart NEW approaches; leader `induction-recursion-telescope` parked as
machinery home (no build); `cut-sequence-potential` / `even-rank-doublecount` remain RETHINK.

I ran the numerics myself (scipy LP over cells + parity checks); findings below are computed,
not asserted.

---

## vertex-integrality-parity (PRIMARY) — CHANGES REQUESTED (stated crux REFUTED; core salvageable)

The route is B1 (min at a vertex) → B2 (vertices integral via TU) → C (integer config ⇒
`D̃ ≡ ΣF = 2^{n+1}−1` odd, and `D̃≥0` ⇒ `D̃≥1`) → assembly. I scrutinized the three pillars.

**(C) parity core — VALID and valuable.** For any integer multiset with ODD total,
`D̃ = O−E ≡ O+E = ΣF (mod 2)` is odd; with `D̃≥0` this gives `D̃≥1`. Verified `0` bad over
`2·10⁵` random integer multisets of odd total. This is a genuine, non-local injection of the
constant `1`, NOT caught by the R8 equivalence meta (measure/merged-order/sequential/genfn all
see only `D̃≥0`). It is worth extracting and certifying as a shared lemma regardless of the
approach's fate. NOTE the hypothesis is odd TOTAL (always true here), not odd part-count.

**(B2) integral-vertex / TU claim — FALSE (computationally refuted this round).** I enumerated
the cells `Q_{a,σ}` for `n=2,3` and minimized `D̃` (the fixed alternating functional) by LP:
- The minimizing vertex is FREQUENTLY FRACTIONAL. e.g. `n=2, a=(0,0,1)`: min at
  `(4, 2, 0.5, 0.5)` — the smallest group `π_2` (sum 1) splits into a tied pair `{½,½}`.
  Many such cells for `n=3` (`a=(0,0,1,1)`, `(1,0,0,1)`, …).
- So the constraint matrix (partition rows ⊕ order/difference rows) is NOT totally unimodular;
  "every vertex of `Q_{a,σ}` is integral" is false.

**The stated fallback is ALSO false.** The approach claims a fractional feasible point is
non-extreme and "some integral point achieves the same (minimal) value." Refuted: at
`n=2, a=(0,0,1)` the LP min is `2` (attained ONLY at the fractional vertex `(4,2,½,½)`); the
minimum over INTEGER points of that cell is `3`. No integer point of the cell reaches `2`. So
integral rounding within a cell strictly OVERSHOOTS — the fallback cannot recover the value.

**The weaker "cell-min value is integral" rescue — also FALSE.** Per-cell LP minima are often
non-integer: `n=3` gives cell minima `1.667`, `4.333`, `5.667`. So one cannot even argue "min
value is an integer, hence odd, hence ≥1." The parity step is inapplicable at the true
minimizers because they are fractional; the min VALUE there is not odd (or not integer).

**Consequence.** The stated skeleton does NOT prove the target. What is actually true and all
that survives: the GLOBAL min over all cells is `1`, attained at an INTEGER config (e.g. n=4
`(8,3,3,2)/(8,2,2,2,1)`), where the parity core fires. The real, unstated crux is therefore:
**prove the global infimum is attained at (equivalently: equals `D̃` of) an integer
configuration** — a much subtler claim than B2. This is precisely the explorer's Opening B
(Invisible-Pair collapse to the integer skeleton), and it carries a real R8-trap risk: the
optimum lives on a CONTINUUM (flat face), and Invisible-Pair removal of a tied `{v,v}` FLIPS
the total's parity (odd→even), destroying the very parity argument it is meant to feed. That
tension is why the reduction is hard and may be circular.

Verdict CHANGES REQUESTED (not RETHINK) only because the parity core is real, bankable
progress and the integer-minimizer reduction is a legitimate, not-yet-refuted direction — the
right target for the whole plateau. What the builder MUST do:
1. Extract and certify the **Parity Lemma** (integer multiset + odd total ⇒ `D̃` odd ⇒ `D̃≥1`)
   as a standalone shared lemma — valuable no matter what.
2. **DELETE B2/TU and the "some integral point achieves the minimal value" fallback** — both
   are refuted above; do not build on them.
3. Reframe the open gap honestly as: reduce `inf_F D̃(F) ≥ 1` to an INTEGER minimizer. Confront
   head-on (a) the continuum/flat-face optimum, and (b) the parity-flip tension of
   Invisible-Pair collapse. If this reduction turns out equivalent to the target (circular), say
   so and it becomes RETHINK next round; if it closes, it solves the problem.
Do NOT resubmit the vertex/TU skeleton as written.

---

## peel-scale-rank-induction (SECOND, genuinely far apart) — CHANGES REQUESTED

Strong induction on `n`: peel the top scale `π_0` (total `2^n`), `F=π_0⊎F'` with `F'` an
`(n−1)`-refinement of `{1,…,2^{n−1}}`, IH `O(F')≥2^{n−1}`; a rank-shift/insertion accounting
lifts to `O(F)≥2^n`. This is far from the vertex route (induction on `n`, not extremal
polytope) and, per both explorers, is a STATIC structural insertion invariant — NOT a
sequential reserve, so `reserve-target-equivalence.md` does not prune it, and it is not a
profile of the final multiset, so the R8 measure/merged-order/genfn meta does not catch it.
Technique is admissible and the skeleton is logically valid IF the key lemma holds.

Honestly-flagged main gap GAP-P1 (Rank-Shift Key Lemma + LOADED IH) is the true crux and is
correctly labelled as such (not hand-waved). Watch items the builder must respect:
- **Plain IH `O(F')≥2^{n−1}` is almost certainly too weak** (the outliner and both explorers
  say so). The loaded invariant must be EXPLICITLY stated and shown INHERITED by `F'`.
- **Circularity risk on the loaded IH.** A prefix bound `Σ_{i≤2k}(−1)^{i−1}w_i≥0` is trivially
  true (descending) and gives only `D̃≥0` — too weak to power the step. Any invariant strong
  enough to force `+2^{n−1}` under the worst interleave risks being equivalent to the target.
  The builder must show the chosen invariant is (i) inherited AND (ii) strictly stronger than
  `D̃≥0` without silently assuming the conclusion. If no such invariant separates the two, this
  collapses to RETHINK.
- Adversarial interleave: `π_0` fragments can be tiny and land deep in `F'`; the rank-shift
  identity must hold at ANY insertion depth, not just the top.
- Do NOT reintroduce any monotone reserve / per-threshold domination (both scan directions
  REFUTED — R7 §14, and this round's bottom-up `63496/10⁵`, mass-survival `28039/2e5`).

Base cases / Case A via C3 (GAP-P3) are routine. Cases are disjoint and covered.

---

## Parked / retired (no build)
- `induction-recursion-telescope` (advance/park): leader, owns all imported certified machinery
  `(△)/(△⋆)/(♠′)/(⊞)/(△△)`, Structure Lemma, Lemma T. Its own merged-order/tiling route is
  R8-exhausted (proven circular). Correctly kept LIVE as the machinery source both new slugs
  import; no rebuild on the same wall. Agreed.
- `cut-sequence-potential`, `even-rank-doublecount`: remain RETHINK; engines proven equivalent
  to target (lemmas banked). Agreed — do not build.

## Diversity check
The two build slugs share the SAME underlying target-equivalent inequality (unavoidable — one
wall) but attack it by genuinely different mechanisms: extremal-polytope + parity-of-odd-total
vs induction-on-n + insertion accounting. Neither is a static profile of the final multiset, so
neither is caught by the R8 meta. Field is far apart. Residual concern for the orchestrator:
BOTH new mechanisms ultimately lean on "the constant 1 comes from the odd dyadic total / dyadic
`+1` dominance" and both have a latent circularity risk at their crux (integer-minimizer
reduction; loaded-IH separation). If BOTH stall in R9 on that same "inject the ½ non-locally"
difficulty, that is the shared-wall signal — next round should seed a mechanism that does NOT
route the constant through the odd-total parity (e.g. the aimo-0917 2-adic-valuation invariant
carried through the ±-operation tree, or the aimo-0663 shadow/position-map coupling to the
zigzag `D̃=1` reference family), per the explorers' openings B/4.

build set: vertex-integrality-parity, peel-scale-rank-induction
