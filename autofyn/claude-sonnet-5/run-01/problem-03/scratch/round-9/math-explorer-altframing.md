# Explorer report (round 9): sanity-check + reformulation scouting — imo-2026-03

**Lens:** sanity-check the near-complete state; hunt for a reformulation of either
remaining gap that trivializes it; independent numeric check of `c(n)=2^n/(2^{n+1}-1)`.

## 1. Independent numeric verification of the formula — CONFIRMED, no problem found

Did **not** trust the approach files' internal `scipy` checks; wrote a fresh,
independent brute-force/grid script (`/tmp/verify3.py`, `/tmp/verify4.py`) from the raw
problem statement:
- Model: pieces = gaps between all marked points (Liu Bang's ≤n points ∪ Xiang Yu's
  ≤n points) plus 0 and 1. The take-turns claim game on a fixed multiset of piece
  lengths is well known to be solved by pure greedy (always take the largest remaining
  piece) — an exchange argument shows this is optimal for both players since pieces
  don't interact. So Liu Bang's guaranteed total = sum of the **odd-ranked** pieces
  (1st, 3rd, 5th, ... largest) when sorted descending — i.e. exactly the `oddrank`/`D`
  quantity the approach files use. Good, this matches the framing already in use across
  all approach files — no discrepancy here.
- **n=1, by hand:** Liu Bang marks `a`, Xiang Yu marks `b≠a`, 3 pieces. Worked the full
  case split (`b<a` vs `b>a`) analytically: for `a=2/3`, the median piece is *exactly*
  `1/3` for **every** `b<2/3` (not just at the symmetric point), and `≤1/3` for `b>2/3`
  (max `1/6` at `b=5/6`). So Xiang Yu's best is median `=1/3`, giving Liu Bang
  `1−1/3=2/3=c(1)`. Cross-checked by a 200,001-point grid search over `b`
  (`/tmp/verify3.py`): numerical min matches `2/3` to machine precision.
  A 200×2000 grid outer/inner search over `a` (`/tmp/verify4.py`) independently finds
  the same optimum. **n=1 fully confirmed**, matching the "n=1 fully closed" claim
  already in `current.md`.
- **n=2, coarse grid (15 outer points × 40 inner points, `O(10^5)` evals,
  `/tmp/verify4.py`):** found value `≈0.57141`, vs. formula `c(2)=4/7≈0.571429` — matches
  to grid resolution, with **no exact-brute-force violation** found. Liu Bang's optimal
  marks came out at `≈4/7, 5/7`, which is a clean, suggestive pair (consistent with a
  geometric-type construction already in `geometric-dominance-construction.md`).
- **Conclusion: no evidence whatsoever of a problem with the conjectured formula.**
  Both n=1 (exact/analytic) and n=2 (numeric, independent of the repo's own checks)
  confirm `c(n)=2^n/(2^{n+1}-1)`. This should retire any residual worry about the
  target itself — round 9 effort should go entirely into closing the two remaining
  proof gaps, not re-deriving the answer.

## 2. Reformulation attempts on the two remaining gaps

### Gap (b) — lower bound, cross-piece tie, minority-part/deep-bracket residue

Read the full round-8 analysis in `recursive-embedding-induction.md` (PAIR-CANCEL,
lines ~1597–1676) and `geometric-dominance-construction.md` (CROSS-TIE-AFFINE). The
obstruction is precisely stated: PAIR-CANCEL reduces the tied configuration's `D` to
`D(B'')` where `B''` deletes both tied elements — but `B''` is **not** a valid
Xiang-Yu-reachable configuration, because the piece `π` owning the tied coordinate `x`
has *no other freedom*: `x` is forced to equal `Σ(π) − (π's pinned anchor parts)`, so
"perturbing x" is not a legal discrete move at all. Three reframings tried:

1. **"Tied ⟹ rigid ⟹ not generic" reframing.** If `x` is π's sole free coordinate and
   is *forced* to be exactly `v` (matching another piece's coordinate `x'`), this is not
   a perturbation-stability question at all — it's a **numerical coincidence between
   two fully-determined quantities from independent pieces**. Reframing away from
   "perturb and compare" to "this configuration is already 100% pinned; just compute
   `D` directly by the *same tree-recursion machinery that closed gap (a)*" looks like
   the right move (this matches option (i) already flagged in the file, but is worth
   restating as the recommended framing, not the fallback: gap (a)'s Lemma TREE-BOUND
   succeeded precisely by treating "residual" values as forced tree-children rather
   than free parameters — gap (b)'s hard case has the exact same shape, a value forced
   by its siblings' sum, so it may already be *within* Lemma TREE-BOUND's structural
   framework if generalized from anchor-exact splits to "anchor-plus-one-forced-residual"
   splits.) **This is the most promising quick win**: don't invent a new argument for
   gap (b); check whether Lemma TREE-BOUND's forest induction already covers this case
   once "leaf" is redefined to include forced-residual children, not just anchor leaves.
2. **Dual-framing with the upper bound's Case C.** Both remaining gaps have an
   isomorphic shape: "a piece/element whose value is forced (not freely optimizable)
   by the sum-minus-siblings constraint, sitting in a narrow residual range." Gap (b)'s
   "minority-part deep-bracket residue" and Claim PTBI Case C's `p_1<Σ/2` region (where
   `TAIL-SNIP` vs `BLOCK-RECURSE j=1` compete and neither dominates) both hinge on a
   *residual/leftover* quantity that is a difference of pinned values rather than a free
   parameter. This suggests genuine structural kinship between the two open gaps — not
   just coincidence — worth flagging to the outliner: a single new lemma about
   "forced-residual" quantities in the alternating-sum recursion (generalizing both
   TREE-BOUND's forced-halving mechanism and BLOCK-RECURSE's peeling mechanism) might
   close *both* gaps at once, which would be a genuine high-leverage unification, not
   just routing around one wall.
3. **"Drop to n=1 on the residual" reframing** (already used partially in
   `recursive-embedding-induction.md`'s BLOCK-RECURSE `j=1` computation for `m=3`):
   confirmed by hand-checking the two worked numeric examples in that file
   (`(0.45,0.275,0.275)` and `(0.4,0.35,0.25)`) — recomputed both TAIL-SNIP and
   BLOCK-RECURSE values independently and got the same numbers reported
   (`0.5875`/`0.55` and `0.575`/`0.525` respectively), so no arithmetic error there.
   The remaining task is a genuine 2-parameter piecewise-affine min-max, not a
   conceptual gap — this looks mechanically closable (not a deep obstruction) if
   someone sets up the full case boundary `p_2/p_1 ≷ 2/3` jointly with `p_1<1/2` and
   optimizes `min(TAIL-SNIP, BLOCK-RECURSE)` over the 2D region explicitly. This is a
   **concrete, bounded, finishable sub-task** for `m=3` — recommend a builder be
   assigned exactly this closed 2-parameter optimization (not the general-`m` case) as
   a quick, isolable win, since `m=3`'s Case C is otherwise fully closed.

### Gap (a) — already closed (round 8), no action needed.

### PTBI Case C general `m≥4` — no shortcut found

The `m=3`-specific vacuousness argument (Lemma HALVE's hypothesis and Case C being
mutually exclusive) was checked and does **not** generalize past `m=4` (confirmed
already correctly recorded in the file: `2Σ/(m+1)<Σ/2` once `m≥4`). No alternative
quick reformulation found for general `m` in the time available; this remains the
harder, still-fully-open sub-case.

## 3. Knowledge base / crux corpus check

`knowledge_base.md` has no entry for "coordinate tie-breaking in combinatorial games"
or "adversary threshold induction" specifically — closest generic entries are the
Pólya heuristics (specialize/reformulate) and the piecewise-concavity smoothing
technique (algebra section), which is structurally close to what's needed for the
gap-(b) perturbation argument (a concave-piecewise argument over the tie point) but is
stated for trigonometric sums, not directly reusable as-is.

Searched the crux corpus (`past_crux_moves_database.json`, `games-and-strategy`
subtopic in both `combinatorics` and `number_theory`, 39 entries total) plus a keyword
sweep for alternating/greedy-pick/oddrank-style moves. **No crux directly matches**
this problem's specific structure (a continuous take-turns claiming game solved by
greedy-oddrank, with an adversarial two-stage marking phase before it). The closest
family are pairing/mirroring strategies and parity-invariant arguments for discrete
token games — not obviously transferable to the continuous-value tie/residual
obstruction here. No new technique found worth importing wholesale; the existing
in-house toolkit (TREE-BOUND, BLOCK-RECURSE, PAIR-CANCEL, CROSS-TIE-AFFINE) is already
more specific to this problem's structure than anything retrievable from the corpus.

## Recommendations for next round

1. **No formula concern** — stop allocating any effort to re-verifying `c(n)`; it's
   solid (n=1 exact, n=2 numeric-independent, both matching).
2. **Try generalizing Lemma TREE-BOUND's tree/forest framework to cover forced-residual
   (non-anchor, sibling-determined) leaves** — this is the single most promising
   concrete next step for gap (b), reframing it from "perturbation of a rigid
   coordinate" (a dead end, per round 8) to "another instance of forced-value tree
   recursion" (the mechanism that already worked for gap (a)).
3. **Flag structural kinship between gap (b) and PTBI Case C** to the outliner — both
   are "residual value forced by pinned siblings" obstructions; a unifying lemma could
   be worth an explorer/outliner slot even though it's a bigger ask than either gap
   alone.
4. **Assign one builder to just finish `m=3`'s Case C 2-parameter optimization**
   (`min(TAIL-SNIP, BLOCK-RECURSE j=1)` over `p_1<1/2, p_3>1/7`) — this is bounded,
   mechanical, and would fully close the upper bound for `n=2`, a concrete milestone
   even if general `m` stays open.
