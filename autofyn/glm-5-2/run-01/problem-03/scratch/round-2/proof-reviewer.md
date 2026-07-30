# imo-2026-03 — proof-reviewer report (round 2)

Reviewed three candidate proofs: `tail-count`, `tower-induction`, `majorization-upper`.
All three independently re-derived / brute-forced with exact `Fraction` arithmetic. **All
three are `partial` — real progress, gaps remain. No APPROVE.** Three CHANGES REQUESTED.

## Independent verification performed (all exact `Fraction`)

1. **Frontier recursion + closed form** (n=0..8): `D(T_n)+D(T_{n−1})=2^n` ✓, `D(T_n)=(2^{n+1}+(−1)^n)/3` ✓, integer ✓, `≥1` ✓ (equality at n=0,1).
2. **Single-split case (b-i)** (n=2,3,4, grid step 1/512, all cut positions dyadic AND non-dyadic): min `D = D(T_{n−1})` ✓, `D≥1` ✓, `D` non-increasing in `q` with slopes `{0,−2}` ✓ (0 violations). Min at the balanced end of the plateau `q=2^{n−1}` (value `D(T_{n−1})`).
3. **Dyadic multi-split (b-ii-dyadic) + F-block + F-min** (n=1..6): enumerated ALL balanced refinements (counts `2,4,10,28,79,224` matching tail-count's claim); min `D=1` ✓, all `D` odd ✓; F-block formula matches direct alternating-sum recomputation on every refinement ✓. F-min over ALL parity vectors `e∈{0,1}^n` (n=1..7): `1≤D_n(e)≤2^n−1` ✓, cascade `e=(1,…,1)` gives `D=1` ✓. **tail-count's frontier recursion and tower-induction's F-block/F-rec AGREE numerically** (cross-checked: both reduce to the same parity-staircase identity).
4. **U1 (parallel-halving → D=1/D_n)** (n=1..6, corrected balanced-pairs config `{2^{n−1},2^{n−1},…,2,2,1,1,1}`): `D=1` tower units ✓, total `=D_n` ✓.
5. **U2 identity** `(2^n−1)/D_{n−1}=1` (n=2..7): ✓ exact.
6. **n=2 complete upper bound** (exhaustive exact-Fraction search over all Liu configs with `m≤3` on a 1/28 grid, Xiang 2-mark optimum on a 1/20-per-piece grid): **0 exceedances of `D>1/7`**; max of `min_Xiang D` over all Liu configs `= 1/7`, attained **uniquely** at `T_2=(4/7,2/7,1/7)` ✓. Strongest claimed new result — CONFIRMED.

### Defects found

- **majorization-upper regime C1 (n=2) — vacuous case + sign-flipped inequality.** The proof's
  chain `a_3 ≤ (1−a_1)/3 < (3/7)/3 = 1/7` has the wrong direction: in regime C (`a_1<4/7`) one
  has `1−a_1>3/7`, so `(1−a_1)/3>1/7`. **However regime C1 (`a_1≥2a_2`, `a_1<4/7`, `a_2≥2a_3`)
  is VACUOUS**: `a_1+a_2+a_3 ≤ a_1+a_1/2+a_1/4 = 7a_1/4 < 1` (since `a_1<4/7`), contradicting
  `sum=1`. So C1 never occurs; the buggy inequality is on an empty set. Regime C always falls in
  C2 (`a_2<2a_3`), which is handled correctly (`D≤a_3/2`, `a_3≤a_2≤a_1/2<2/7` ⇒ `D<1/7`). **The
  n=2 upper bound is unaffected and correct** (exhaustive grid confirms). Cleanup: delete the
  vacuous C1 sub-case (or note it is empty); the displayed inequality should not appear as a
  proof step.
- **tail-count "rigorously established for n=2,3" — mild overclaim.** The non-dyadic
  multi-split sub-case (G1) is OPEN for all `n≥2`, including `n=2,3`. For `n=2,3` tail-count
  gives a **grid search** (1/1024 and 1/4 step), not a proof: a grid can miss breakpoints
  between grid points. The PL+breakpoint reduction (§6, proved) reduces the global min to
  breakpoint configs, but tail-count did NOT enumerate the (finite, exactly enumerable) breakpoint
  configs for `n=2,3` — it ran a grid. So the lower bound is rigorously proved for all `n` only
  in cases (a), (b-i), (b-ii-dyadic); the non-dyadic multi-split is open for every `n≥2`
  (grid-verified `n≤6`, not proved). The sentence "rigorously established for n=1,2,3" should
  read "rigorously established for n=1 (full); for n≥2 the non-dyadic multi-split sub-case
  remains open (grid-verified n≤6)".
- **tail-count §4 "p is the unique largest element"** — false at the balanced tie `q=2^{n−1}`
  (`p=2^{n−1}` ties the rest's `2^{n−1}`). Immaterial: `D` is tie-agnostic and the proof
  acknowledges this; the formula `D(M)=p−D(R)` holds at the tie by continuity. Cosmetic fix.

No circularity found: majorization-upper's n=2 proof uses only `W(1)` (certified n=1 base,
re-proved in-file with the unique-worst clause) and direct arithmetic for C/B2 — it does NOT
assume the general "tower-is-unique-worst" monotonicity (G1). The general-n Part IV regimes
A/B1 are conditional on `W(n−1)` (honest, labeled as reductions, not certifiable standalone).

---

## Per-slug review

### 1. `tail-count` — Status: partial. Verdict: CHANGES REQUESTED.

**Certified-here (correct, sorry-free, importable):**
- Per-split `ΔD` formula (§2) — load-bearing identity, re-derived independently, matches direct
  on T_3 ✓.
- Frontier recursion `D(T_n)+D(T_{n−1})=2^n`, closed form `D(T_n)=(2^{n+1}+(−1)^n)/3≥1` (§3) ✓.
- Balanced-split recursion: balanced top split of `T_n` ⇒ `D→D(T_{n−1})` (§3) ✓.
- **Single-split lower bound (b-i)** `D≥D(T_{n−1})≥1`, all `n` (§4) ✓ — the PL slope-`{0,−2}`
  analysis is clean and brute-force-confirmed.
- **Multi-split dyadic lower bound (b-ii-dyadic)** `D≥1`, all `n` (§5) ✓ — level-block
  dominance, verified on all 224 refinements of T_6.
- PL + breakpoint reduction (§6): global min of `D` over ≤n-mark refinements is at a
  breakpoint (tie) config ✓ (compactness + PL structure).

**Gaps (honest, explicit):**
- **G1 (non-dyadic multi-split)** — OPEN for all `n≥2`. The dyadic block-cancellation (§5) needs
  power-of-2 pieces; non-dyadic fragments don't group. The `ΔD` formula composes but its
  `O`-widths after the first split are functionals of the perturbed `N(t)` (parity coupling).
  Verified `n≤6` (grid); not proved. The plateau-connects-to-dyadic conjecture is the proposed
  route but is NOT proved.
- **(U) upper bound general n** — only `n=1` proved; parity coupling of `N(t) mod 2` across
  thresholds blocks the per-threshold cap.

**Overclaim to correct:** "rigorously established for n=2,3" → the non-dyadic sub-case is
grid-verified there, not proved. See Defects above.

**Scores:** Correctness 8/10 (proven parts all check out; the overclaim is scope-creep, not a
math error). Completeness 5/10 (G1 + U open). Progress 8/10 (closed single-split + dyadic
multi-split for all n, two genuinely new theorems). Outcome: `verified-milestone`.

### 2. `tower-induction` — Status: partial. Verdict: CHANGES REQUESTED.

**Certified-here:**
- **F-block** (block-contribution formula): `D(M)=Σ_k 2^k(−1)^{C_k}(n_k mod 2)` for dyadic
  refinements; `D` depends only on the split-parity vector `e` ✓ (matches direct on all
  refinements n≤6).
- **F-rec** (frontier recursion, general parity-vector form): `D_n(ē,0)=2^n−D_{n−1}(ē)`,
  `D_n(ē,1)=D_{n−1}(ē)`, `D_0=1` ✓ (the unsplit-tower identity is the `e≡0` special case;
  subsumes tail-count's balanced-split-frontier-recursion). Verified over all 2^n parity vectors
  n≤7.
- **F-min**: `1≤D_n(e)≤2^n−1` for every parity vector, all `n` ✓ (induction via F-rec). **Closes
  the all-balanced-splits sub-case of case (b) for all n** — a genuine new theorem, brute-force
  confirmed.

**Gaps (honest, explicit):**
- **G2 (unbalanced splits)** — OPEN for all `n≥2`. The block formula needs dyadic pieces;
  unbalanced `2^k→p+q` (`p≠q`) breaks it. The exchange "unbalanced ≥ balanced" is verified
  `n≤6` but unproved. Same wall as tail-count's G1 (opposite machinery — discrete frontier
  vs continuous PL; the outline-reviewer's diversity assessment holds).
- **U1, U2 (upper bound general n)** — dominant recurrence doesn't factor through `c(n−1)`;
  below-threshold regime open. Honestly deferred to `majorization-upper`.

**No overclaim:** the "closes the all-balanced-splits sub-case for all n" language is correctly
scoped to balanced splits; G2 (unbalanced) is flagged.

**Scores:** Correctness 9/10 (F-block/F-rec/F-min all check out cleanly). Completeness 5/10 (G2
+ upper bound open). Progress 8/10 (F-min closes balanced sub-case all n — the cleanest new
theorem this round). Outcome: `verified-milestone`.

### 3. `majorization-upper` — Status: partial. Verdict: CHANGES REQUESTED.

**Certified-here:**
- **U1** (parallel-halving saturates the tower): Xiang's n-mark parallel halving of `T_n` gives
  `D=1/D_n` exactly ✓ (the upper-bound witness against the tower, n=1..6).
- **U2** (dominant factorization): under `a_1≥2a_2` and `a_1≥2^n/D_n`, halving `a_1` factors
  `D(total)=D(rest)`, `R≤D_{n−1}/D_n`, closed by IH; tower is the unique equality case
  (conditional on `W(n−1)`) ✓. Identity `(2^n−1)/D_{n−1}=1` confirmed exact n=2..7. **Conditional
  on the IH — NOT certifiable standalone** (per round-1 rule); recorded as a reduction.
- **U3** (pairing-cancellation, non-dominant B1): under `a_1<2a_2`, `a_2≥2^{n−1}/D_n`, pairing
  `a_1→{a_2,a_1−a_2}` cancels positions 1,2; closed by IH, strict ✓. **Conditional on IH — NOT
  certifiable standalone.**
- **B1** (Xiang's optimum at a balanced/tie refinement): PL + compactness ⇒ the min of `D`
  over refinements is at a breakpoint (tie) config ✓. General (any Liu config); subsumes
  tail-count's §6 PL+breakpoint reduction. Sound, not circular (it constrains where the optimum
  lives; it does not assume the bound).
- **n=2 complete upper bound** (Part III): every Liu config with `m≤3` admits a ≤2-mark Xiang
  refinement with `D≤1/7`, tower `T_2` the **unique** equality case ✓ — **exhaustively verified
  (0 exceedances, unique max at T_2)**. The C1 sub-case is vacuous (see Defects); C2, A, B1, B2,
  m=1, m=2 all check out.

**Gaps (honest, explicit):**
- **G1 (tower-is-unique-worst exchange monotonicity)** — CONJECTURE, verified n=1..4, NOT
  proved for n≥3. The mechanism (ratio-toward-dyadic-2:1 increases `min_Xiang D`) is a research
  question. Correctly flagged; the B3-circularity trap (type enumeration = the bound) is
  avoided.
- **G2 (below-threshold regimes C, B2 for n≥3)** — `R/D_{n−1}` overshoots; a strengthened
  two-variable IH `D≤f(R,M,n)` is the candidate route; verified 0 exceedances n=2,3; open.

**Defect (benign):** the C1 sub-case of regime C (n=2) is vacuous and its displayed inequality
`(1−a_1)/3<1/7` has a sign error; harmless (C1 never occurs; C2 handles regime C correctly).

**No circularity:** n=2 proof uses only `W(1)` and direct arithmetic; does not assume G1.
General-n Part IV regimes A/B1 are conditional on `W(n−1)` (honestly labeled reductions).

**Scores:** Correctness 8/10 (n=2 complete and verified; C1 vacuous-case cleanup needed).
Completeness 4/10 (G1 + G2 open for general n — this is the upper-bound crux). Progress 9/10
(first real upper-bound progress: n=2 complete + mechanical scaffolding + the only upper-bound
approach in the field). Outcome: `verified-milestone`.

---

## Lemma certification summary

**Certified (admit to `results/imo-2026-03/lemmas/`)** — 7 new lemmas, deduplicated:

| Lemma (canonical name) | Source | Status |
|---|---|---|
| `frontier-recursion` | tower-induction F-rec (general parity-vector form) + tail-count §3 (closed form, special case) | CERTIFIED. Subsumes tail-count's `balanced-split-frontier-recursion`. |
| `block-contribution-formula` | tower-induction F-block | CERTIFIED. Distinct. |
| `dyadic-refinement-lower-bound` | tower-induction F-min (= `1≤D≤2^n−1` for every balanced refinement) + tail-count §5 (level-block dominance) | CERTIFIED (one canonical statement; both proofs equivalent). |
| `single-split-top-lower-bound` | tail-count §4 | CERTIFIED. |
| `parallel-halving-saturates-tower` | majorization-upper U1 | CERTIFIED. |
| `pl-breakpoint-minimum` | majorization-upper B1 (general, any Liu config) + tail-count §6 (specialized to T_n) | CERTIFIED (general B1 statement; tail-count §6 is the specialization). |
| `n2-upper-bound-complete` | majorization-upper Part III | CERTIFIED (with note: C1 sub-case is vacuous; the n=2 upper bound `c(2)≤4/7` is complete and exhaustively verified; tower T_2 unique equality). |

**Rejected (conditional on an unproved IH — not standalone, per round-1 rule):**
- `dominant-factorization` (majorization-upper U2) — conditional on `W(n−1)`; record as a
  conditional reduction inside the approach file, not a standalone lemma.
- `pairing-cancellation-non-dominant` (majorization-upper U3) — conditional on `W(n−1)`; same.

**Promotable but not submitted for certification this round** (left in the approach file):
tail-count's `per-split-delta-D` (§2) — proved, sorry-free, correct, but a tool internal to
tail-count rather than a reusable standalone; the builder did not submit it; I leave it
uncertified (it is available as the `ΔD` identity within tail-count).

The `lemmas/` directory now holds 13 lemmas (6 from round 1 + 7 new).

---

## Goal Progress

**Status: partial.** Best proven result:

- **Lower bound** `c(n)≥2^n/(2^{n+1}−1)`: rigorously proved for ALL `n` in cases (a) top-unsplit
  (certified), (b-i) single-split of top (§4 tail-count, all n), (b-ii-dyadic) all-balanced-splits
  (F-min / §5, all n). The non-dyadic multi-split sub-case (G1) is OPEN for all `n≥2`
  (grid-verified `n≤6`). `n=1` fully proved (both bounds). `c(2)=4/7`: lower bound proved (cases
  a, b-i, b-ii-dyadic cover n=2's reachable space EXCEPT non-dyadic 2-mark refinements, which are
  grid-verified only — NOT a proof for n=2; the n=2 lower bound is partial pending G1).
- **Upper bound** `c(n)≤2^n/(2^{n+1}−1)`: **n=2 COMPLETE** (exhaustively verified, tower T_2
  unique equality). n=1 complete (certified). General n: regimes A, B1 closed CONDITIONAL on
  `W(n−1)`; G1 (exchange monotonicity) and G2 (below-threshold C/B2) OPEN for n≥3.
- **Combined:** `c(1)=2/3` fully proved. `c(2)=4/7`: upper bound proved; lower bound pending G1
  (non-dyadic multi-split, grid-verified only). `c(n)` for n≥3: both bounds partial.

**#1 gap to attack next round (lower bound):** G1 — the non-dyadic multi-split breakpoint
  reduction. The PL+breakpoint reduction (now certified `pl-breakpoint-minimum`) LANDS the
  global min at a breakpoint config; the dyadic breakpoints are settled (`dyadic-refinement-
  lower-bound`); the open step is **prove `D≥1` at every non-dyadic breakpoint config** of `T_n`.
  Concretely: enumerate the (finite, exactly computable) breakpoint configs for small n via the
  PL structure, prove a structural "every non-dyadic breakpoint lies on a PL plateau whose
  closure contains a dyadic breakpoint" lemma (NOT a type-by-type check — that would be the B3
  trap), or find a direct `ΔD`-algebraic argument.

**#1 gap to attack next round (upper bound):** G1 — the exchange monotonicity "tower is the
  unique worst Liu config" for n≥3. The n=2 base is now proved (`n2-upper-bound-complete`);
  the general-n step needs a genuine structural monotonicity (ratio-toward-dyadic-2:1
  increases `min_Xiang D`), via the `D=∫(N mod 2)dt` residual language, NOT a type enumeration.

**Run-level state:** `c(n)=2^n/(2^{n+1}−1)` remains the conjectured answer (numerically exact
n=1..4). The balanced-splits sub-case of the lower bound is now CLOSED for all n (F-min), and
the n=2 upper bound is now CLOSED — both genuine advances. The two remaining cruxes (non-dyadic
multi-split lower-bound plateau; general-n upper-bound exchange monotonicity) are the
make-or-break steps for round 3.
