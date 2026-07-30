# proof-reviewer — imo-2026-03 round 4

Review of three built approaches: `tail-count`, `majorization-upper`, `lp-dual-certificate`. All computations re-derived independently with exact `Fraction` arithmetic and scipy LP.

---

## 1. `tail-count` — CHANGES REQUESTED (Status: partial)

### What's proved this round

**GAP-B (telescoping zero-gradient block lemma, §11):** PROVED and rigorous. The argument is clean affine algebra:
- (a) On a fixed PL cell, each piece's position/sign is fixed, each length is affine in the cuts, so `D` is affine. ✓
- (b) Fragments of a split piece `V` satisfy `Σ f_j = V` (telescoping/partition identity). If all at same sign `s`, contribution `= s·V` (constant). If opposite signs, gradient `±2` per cut. ✓
- (c) Block condition (every split uniform-sign) ⇒ `D` = sum of constants = constant. ✓
- (d) All top-fragments at `+`, all below-tower at `−` ⇒ `D = 2^n − (2^n−1) = 1` directly, no dyadic endpoint needed. ✓

I independently verified the spine-7 cell `{a,4,b,2,c,1,d}`: `D = (a+b+c+d) − 7 = 8−7 = 1` (Fraction-exact), and the V-shape cell (`8→5+3, 5→4+1`): fragments `{4,1}` at positions 2(−),5(+) — opposite signs, block condition correctly FAILS. The load-bearing step (telescoping mass identity) is valid: split preserves partition sums, so top-fragment mass `= 2^n`, below-tower mass `= 2^n − 1`.

**GAP-A (two-leftover transport, §12):** PROVED as corollary of GAP-B(d). The mass identity `a+d = t+1` follows from: fragment mass `= 2^n`, paired fragment mass `= (2^n−1)−t` (each pair: fragment = tower piece), so `a+d = 2^n − ((2^n−1)−t) = t+1`. Then `D = a−t+d = 1`. Verified Fraction-exact (`a=9/2, d=1/2, t=4`: `D=1`). This is a genuine corollary — the D=1 conclusion is GAP-B(d) applied; the new content is the concrete mass identity. Standalone (depends only on certified `spine-pair-cancellation`, `strong-breakpoint-group-structure`, and GAP-B which is being certified).

**GAP-C (star-shaped transport, §13):** honestly OPEN. The builder correctly:
- Labels the 816/816, 322/322, 17/17, 165/165 numerics as "verification, NOT a proof" (per round-2 rule). ✓
- Identifies the two precise sub-gaps: (i) V-shape cell faces inherit the block condition; (ii) block-condition cells without the "all-top-+, all-below-−" sign pattern and without a dyadic endpoint. ✓
- Does NOT claim GAP-C is settled. ✓

The outline-reviewer's flagged concern ("the 'if' [cell contains dyadic endpoint] is load-bearing") is addressed for block-condition cells with the (d) sign pattern (D=1 computed directly, no dyadic endpoint needed), and honestly left open for cells without that sign pattern. This is the correct state.

### Verdict

Status: **partial**. GAP-B and GAP-A are real new proven results (certified as `telescoping-block-lemma` and `two-leftover-transport`). GAP-C (the G1-closer) remains open. The approach does not overclaim. The outline-reviewer's "APPROVE" is about the approach direction (the plateau NO-SADDLE mechanism is the strongest lower lead), not proof completeness — the proof is NOT complete.

**Scores:** Correctness 9/10, Completeness 6/10 (GAP-C open), Progress 8/10 (two new certified lemmas, block-condition cells settled).

---

## 2. `majorization-upper` — CHANGES REQUESTED (Status: partial)

### What's proved this round

**Max-bound refutation (Part I):** CORRECT. I verified `(7,6,5,3)/21`: the 3-mark refinement `{5/21, 5/21, 1/7, 1/7, 2/21, 2/21, 1/21}` (three canceling pairs + residual `1/21`) gives `D* = 1/21`. `M/8 = 1/24`. Ratio `8/7 > 1`. VIOLATION exact. The actual target `1/D_3 = 1/15` is NOT violated (`1/21 < 1/15`). ✓ The Max-bound conjecture is genuinely dead; the answer survives.

**n=2 Max-bound `D* ≤ max/4` (Part III):** PROVED. The per-regime derivation from `n2-upper-bound-complete` is sound. I verified the key algebraic step in regime B2: `b_1 ≥ 2b_2` forces `a_1 > 4/7` (via `a_2 + a_3 < (a_2+1)/3 < 3/7`), contradicting B2's `a_1 < 4/7`. I re-derived all four regimes independently. The averaging bound `min(b_1−b_2, 2b_2−b_1) ≤ b_2/2` (min ≤ average) is correctly applied. 0 violations over 157 integer configs (grid-12 search). ✓ Certified as `n2-max-bound`.

**V(3) `D* ≤ M_2/4` (Part IV):** PROVED. The two-case split correctly addresses the outline-reviewer's critical flag:
- **Case 1 (dominant, `a_1 ≥ 2a_2`):** HALVE `a_1`. I verified the pairing-witness `(8,3,2,2)/15`: pairing gives D=1/3 after 1 mark (the `a_1−a_2=5/15` fragment is largest, two `a_2`'s at positions 2,3 not 1,2). Pairing FAILS. Halving: `a_1/2 = 4/15 ≥ a_2 = 3/15`, halves at positions 1,2 cancel, rest max `= a_2 = M_2`, n=2 Max-bound gives `D ≤ M_2/4`. ✓
- **Case 2 (non-dominant, `a_1 < 2a_2`):** PAIR `a_1`. Two `a_2`'s at positions 1,2 cancel, rest' max `≤ M_2`, n=2 Max-bound. ✓

I checked the edge case `a_2 = a_3` (three `a_2` copies after pairing): tie-agnosticism + n=2 Max-bound (stated for arbitrary multisets) handles it — the rest' multiset has max `≤ M_2` regardless. ✓ 0 violations over 102 crux configs. Certified as `v3-upper-bound`.

**n=3 upper bound COMPLETE (Part VI):** All four regimes closed, UNCONDITIONAL:
- Regime A (dominant, `a_1 ≥ 8/15`): certified U2, `D* ≤ 1/15`. ✓
- Regime B1 (non-dom, `a_2 ≥ 4/15`): certified U3, `D* ≤ 1/15`. ✓
- Regime C (dominant, `a_1 < 8/15`): V(3) Case 1, `M_2 ≤ a_1/2 < 4/15`, `D* ≤ M_2/4 < 1/15`. Strict. ✓
- Regime B2 (non-dom, `a_2 < 4/15`): V(3) Case 2, `D* ≤ M_2/4 < 1/15`. Strict. ✓

I verified the counterexample `(7,6,5,3)/21` is correctly handled: `a_2 = 2/7 > 4/15`, so it's regime B1 (U3), NOT B2 (V(3)). U3 gives `D* ≤ R'/7 = (3/7)/7 = 3/49 < 1/15`. ✓ The four regimes are exhaustive and disjoint. **The n=3 upper bound `D* ≤ 1/15` is rigorously proved for every n=3 Liu config.**

### Overclaim found

The builder writes (Part VI): "Combined with the lower bound (`tower-top-unsplit` + `tail-count`/`tower-induction`/`gaps-leftover`), `D*(3) = 1/15`, hence `c(3) = 8/15`." This is an **overclaim**. The lower bound for n=3 is NOT complete: GAP-C (non-dyadic multi-split, k≥3) is OPEN even for n=3 (the tail-count approach verifies 816/816 + 322/322 + 17/17 for T_3 but does NOT prove it generally; the 2-split Type C sub-case is verified-only). The proved result is `c(3) ≤ 8/15` (upper bound); the equality `c(3) = 8/15` needs `c(3) ≥ 8/15` (lower bound), which is partial. The builder must state `c(3) ≤ 8/15` proved, not `c(3) = 8/15`.

### V(n≥4) and MB-Dom/MB-Pair

V(n≥4) is honestly labeled CONJECTURE (0 violations n=3,4,5, unproved in the crux). ✓ MB-Dom and MB-Pair are re-derived under V(n−1) IH as conditional reductions (Part V), correctly NOT submitted as standalone lemmas. The crux `a_1 < 2a_2 ∧ a_3 > a_1/2` is open. ✓

### Verdict

Status: **partial**. The n=3 upper bound is complete and correct (significant progress). The overclaim `c(3) = 8/15` must be downgraded to `c(3) ≤ 8/15`. Two new certified lemmas (`n2-max-bound`, `v3-upper-bound`).

**Scores:** Correctness 8/10 (overclaim on c(3)=8/15), Completeness 7/10 (n=3 upper complete, n≥4 open), Progress 9/10 (n=3 upper bound is the strongest certified upper-bound progress).

---

## 3. `lp-dual-certificate` — CHANGES REQUESTED (Status: partial)

### What's proved and valid

**LP-0 (per-type LP is exact):** Valid. Every LP-feasible `p` is realizable (any composition of `2^{n−t}` into `r ≥ 1` parts is a split tree), every realizable refinement is LP-feasible. The `p_k = 0` boundary (degenerate "no further mark") is correctly included as a breakpoint-type limit point. ✓

**LP-1 (`D ≥ 0`, boundedness):** Valid. By `gaps-leftover-identity`, `D = Σ(p_{2k}−p_{2k+1}) + [m \text{ odd}] p_{m−1} ≥ 0` for both parities (sorted descending, nonneg). ✓ Strong duality applies.

**LP-3 (clean-types certificate, GAP-LP1):** VALID and unaffected by the sign error (see below). For a clean type (each bin monochromatic in parity), `y_ub = 0`, `y_eq[t] = s_t` (bin parity). Stationarity: `y_eq[b(k)] = s_{b(k)} = (−1)^k` (bin clean). `y_ub = 0` is feasible for both `≥ 0` and `≤ 0` constraints, so the sign error in LP-2 is irrelevant. Top-bin-at-`+1`: if `s_0 = −1`, all top-fragments (mass `2^n`) at `−`, so `D ≤ (2^n−1) − 2^n = −1 < 0`, contradicting LP-1. ✓ Objective `Φ ≥ 1` (dyadic dominance `2^n > 2^n−1`). ✓ By strong duality, `min D ≥ 1` on clean-type cells. Certified as `lp-dual-clean-types`.

### Sign error found in LP-2 (the dual derivation)

The builder's dual derivation (LP-2) has a **sign error** in the mountain/stationarity. The builder writes:
```
y_eq[b(k)] = (−1)^k + y_ub[k] − y_ub[k−1],  y_ub ≥ 0  (nonneg mountain, prefix sums of d_k = y_eq[b(k)] − (−1)^k ≥ 0)
```
The **correct** dual (with sort constraints in `≥` form `p_k − p_{k+1} ≥ 0`, dual variable `y_ub ≥ 0`) has stationarity:
```
y_eq[b(k)] = (−1)^k − y_ub[k] + y_ub[k−1],  i.e. y_ub[k] = −Σ_{j=0}^k d_j  (NONPOS prefix sums of d_k = y_eq[b(k)] − (−1)^k)
```
The `y_ub` terms have the **opposite sign**. The builder's "nonneg mountain" should be "nonpos mountain" (or equivalently, `d_k` should be `(−1)^k − y_eq[b(k)]` for a nonneg mountain). I verified this with scipy: the correct dual of the interleaved T_2 cell has `max objective = 1.0` (matching primal `min = 1.0`), with optimal `y_eq = (1, −1, −1), y_ub = 0`.

### Consequences of the sign error

1. **The interleaved T_2 demonstrative example (§5) is INFEASIBLE.** The builder's cert `y_eq = (+1, −1, 0)`, mountain `y_ub = [0,0,0,1,0]` (objective 2) violates the correct stationarity at `k=3`: `y_eq[2] + y_ub[3] − y_ub[2] = 0 + 1 − 0 = 1`, but the constraint requires `≤ (−1)^3 = −1`. `1 ≤ −1` is FALSE. The cert is infeasible. The LP min is 1 (verified scipy); the builder's claimed objective 2 would violate strong duality. **This example must be removed or corrected.**

2. **The narrow provable interleaved sub-class (§5, "single adjacent 2-piece interleaving at an odd start") has the wrong parity.** With the corrected signs, the nonneg-mountain bump works for `k` EVEN (not odd). The builder's "k odd" is backwards.

3. **The mountain interpretation (LP-2) is stated with the wrong inequality direction.** This is the scaffold for GAP-LP2; it must be corrected before GAP-LP2 can be attacked.

### What survives

- LP-0, LP-1, LP-3 (clean types): valid. The clean-types sub-case of G1 is genuinely closed for all n. ✓
- The non-circularity claim: valid (refinement-min dual, not the round-3 claim-game dual). ✓
- GAP-LP2 equivalence to G1: conceptually correct (strong duality makes "dual objective ≥ 1 for every type" equivalent to "min D ≥ 1 for every type"), despite the mountain sign error. The builder correctly labels it G1-equivalent, not a shortcut (per the outline-reviewer's correction). ✓

### Verdict

Status: **partial**. The clean-types sub-result (LP-3) is valid and certified. But the dual derivation (LP-2) has a sign error that invalidates the interleaved T_2 example and the narrow interleaved sub-class. These must be corrected (flip the mountain direction, fix the parity, remove or redo the infeasible example). The approach is NOT dead — the clean-types result is real, the LP machinery is genuinely orthogonal, and the corrected dual may still yield a viable attack on GAP-LP2 — but the current write-up has a concrete algebraic error.

**Scores:** Correctness 5/10 (sign error in LP-2, infeasible example), Completeness 4/10 (clean types only; GAP-LP2 open and scaffold has sign error), Progress 6/10 (genuine 4th framing + one certified sub-result, but the dual machinery needs repair).

---

## Lemma certification summary

Certified this round (5 new, total 24):
1. `telescoping-block-lemma` (tail-count GAP-B) — standalone, proven. ✓
2. `two-leftover-transport` (tail-count GAP-A) — corollary of GAP-B(d), proven. ✓
3. `n2-max-bound` (majorization-upper Part III) — derived from `n2-upper-bound-complete`, proven. ✓
4. `v3-upper-bound` (majorization-upper Part IV) — two-case split, uses `n2-max-bound`, proven. ✓
5. `lp-dual-clean-types` (lp-dual-certificate LP-3) — LP strong duality, proven (unaffected by LP-2 sign error). ✓

Rejected: none this round (the prior REDUCTION files `max-bound-dominant`, `max-bound-pairing-small-third` remain conditional reductions, not standalone).

---

## Per-slug verdict block

- **tail-count**: CHANGES REQUESTED, Status partial. GAP-B and GAP-A proved and certified; GAP-C (the G1-closer) honestly open. No overclaim. Gap to close: GAP-C (star-shaped transport — prove every min-level-set cell face satisfies the block condition or contains a dyadic endpoint).

- **majorization-upper**: CHANGES REQUESTED, Status partial. Max-bound refuted, n=2 Max-bound proved, V(3) proved (two-case split), n=3 upper bound COMPLETE (`D* ≤ 1/15`). Overclaim: `c(3) = 8/15` must be downgraded to `c(3) ≤ 8/15` (lower bound partial). Gap to close: V(n≥4) crux `a_1 < 2a_2 ∧ a_3 > a_1/2`; and fix the c(3) overclaim.

- **lp-dual-certificate**: CHANGES REQUESTED, Status partial. Clean-types sub-result (LP-3) valid and certified. Sign error in LP-2 (mountain direction flipped); interleaved T_2 example infeasible (violates strong duality); narrow interleaved sub-class has wrong parity. Gaps to close: fix the LP-2 sign error, remove/correct the infeasible example, fix the sub-class parity, then attack GAP-LP2 with the corrected dual.
