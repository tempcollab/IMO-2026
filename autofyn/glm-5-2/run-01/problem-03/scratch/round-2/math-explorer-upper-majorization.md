# math-explorer (upper-majorization lens) — IMO 2026 P3, round 2

**Route:** Upper bound via majorization / extremal / parity. Target: for EVERY Liu
config (≤n marks → ≤n+1 pieces, sum 1), Xiang adaptively marks ≤n points to force
`D ≤ 1/D_n` (`D_n = 2^{n+1}−1`). This route is genuinely different from the inductive
dominant-case-split (another explorer owns that). All claims below are backed by
exact-`Fraction` grid searches; scripts in `/tmp/round-2/explore_majorization*.py`.

---

## (a) Computational verdict: "tower is the worst Liu config" — STRONGLY CONFIRMED

I computed `min_Xiang(odd-index)` (Xiang's best response) for the tower and for
hundreds of random + perturbation configs, n = 1..4. Headline:

**The dyadic tower `T_n = (2^n,…,2,1)/D_n` is the UNIQUE config that ties at the
target `2^n/D_n`. Every other config gives strictly less.**

Concrete numbers (exact `Fraction` grid search, grid = halving + 1/k fractions):

| n | target `2^n/D_n` | tower Xiang-best | best non-tower found | perturbations |
|---|------------------|------------------|----------------------|---------------|
| 1 | 2/3 = 0.6667     | **2/3 (TIE)**    | 1/2 (e.g. (4,3)/7)   | strict <      |
| 2 | 4/7 = 0.5714     | **4/7 (TIE)**    | 1/2 = 0.5000         | strict <      |
| 3 | 8/15 = 0.5333    | **8/15 (TIE)**   | 1/2 = 0.5000         | strict <      |

**Striking structural fact for n = 2.** Among ALL `/7`-denominator configs
scanned, the tower `(4,2,1)/7` is the **only** 3-piece config with Xiang-best =
4/7. Every other `/7` config — `(5,1,1)/7`, `(3,3,1)/7`, `(3,2,2)/7`, `(5,2)/7`,
`(4,3)/7`, `(6,1)/7` — has Xiang-best = **1/2** (i.e. `D = 0`, not just `D < 1/7`).
Xiang can drive `D` to **zero** against every non-tower config; only the tower
resists, holding `D` at exactly `1/7`.

**Perturbation test (n = 2, 3).** Shifting mass `±ε` (ε = 1/1000) between the
tower's two largest pieces drops Xiang-best strictly below the target in ALL
directions:
- n=2, d = ±1..±5 eps: all give 0.566..0.571, strictly < 4/7 = 0.571429.
- n=3, d = ±1..±5 eps: all give 0.529..0.533, strictly < 8/15 = 0.533333.

**Random search.** 400 random configs (n=2), 150 (n=3): **0 exceedances** of the
target. Worst found ≈ target (rounding). The grid can only *over*-estimate
Xiang-best (missed good splits), so 0 exceedances is strong evidence.

**Verdict on sub-route 1:** the tower is a **strict local (and apparently global)
maximizer** of `min_Xiang(odd-index)`. The gap to the next config is huge (1/D_n
vs 0 for n=2). This makes the exchange argument "tower is the worst ⇒ upper bound
= lower bound" the most promising route — IF a real monotonicity proof exists.

---

## (b) Ranked candidate strategies

### Sub-route 1: "tower is the worst" exchange / smoothing — MOST PROMISING

**The mechanism (numerically observed).** Xiang's optimal play is a
**config-adaptive pairing**, NOT a fixed rule:
- Against the **tower**, Xiang splits each of the `n` largest pieces in half
  (**parallel halving**): `2^k → (2^{k-1}, 2^{k-1})`. Because the tower has exact
  dyadic ratios `2^k : 2^{k-1} = 2`, each halved piece lands adjacent to the next
  tower piece, creating the **balanced-pairs config**
  `{2^{n-1},2^{n-1},…,1,1,1}/D_n` whose `D = 1/D_n` (the unpaired residual `1`).
  This is the **unique** config where the pairing cascade bottoms out at exactly
  `1/D_n` — verified for n=1..5 (all give `D = 1/D_n` exactly).
- Against **any non-tower config**, Xiang uses a *different*, adaptive split and
  achieves strictly smaller `D` (often `D = 0` for n=2). Parallel halving fails
  on non-tower configs (e.g. `(3,2,2)/7` → `D = 2/7`), but Xiang's *optimal* play
  on the same config gives `D = 0`.

**The exchange to prove.** If `L ≠ T_n` (some ratio `b_k/b_{k+1} ≠ 2`), then
Xiang can exploit the mismatch: when `b_k/b_{k+1} > 2`, splitting `b_k`
asymmetrically (not at half) lets one fragment *match* `b_{k+1}`, creating a
cleaner pair; when `b_k/b_{k+1} < 2`, Xiang splits `b_{k+1}` instead. The dyadic
ratio `2` is the **hardest** because it forces the cascade to continue all the
way down, accumulating the maximal residual `1/D_n`.

**Where it gets stuck.** The exchange must be a REAL monotonicity, not a
type-by-type check (the `balanced-configs` B3 trap — "check every type ≤ bound"
IS the bound). The concrete difficulty: for general n with arbitrary
fragmentation, the "adaptive pairing" strategy must be specified and proven to
leave a residual ≤ `1/D_n` for EVERY non-tower config. For n=2 this is clean
(every non-tower config admits `D = 0`); for n ≥ 3 the residual is nonzero and
the cascade structure is more intricate. No proof yet — but the numerics are
strong enough to warrant a dedicated build.

### Sub-route 2: D-integral "make N(t) even" parity pairing — PROMISING MECHANISM

**The framing.** `D = ∫(N(t) mod 2) dt` (certified lemma
`D-equals-parity-integral.md`). Xiang wants `N(t)` even almost everywhere,
shrinking the odd-parity set to measure ≤ `1/D_n`.

**What works.** For the tower, after parallel halving, `N(t) mod 2 = 1` exactly
on `[0, 1/D_n]` — the unpaired smallest piece. So `D = 1/D_n` cleanly. This
confirms the "residual unpaired interval = 1/D_n" picture: Xiang's `n` marks
create `n` pairs (filling odd+even slots, canceling), leaving one piece
unpaired, and for the tower that piece is exactly `1/D_n`.

**What fails.** A FIXED pairing strategy (parallel halve, or halve-largest) fails
on random configs (59/500 exceed for n=2, 37/500 for n=3 with parallel halve).
The tail-count obstruction (from `tail-count.md` gap U) is real: a single Xiang
mark re-sorts the global order and flips parities on a long range of `t`. The
D-integral gives the right *language* (residual unpaired measure) but not a
*decoupling* — the thresholds remain coupled.

**Where it gets stuck.** To avoid the coupling, one needs a bookkeeping that
tracks the pairing without global resorting. The cleanest candidate: process
pieces in a FIXED descending order and define a "signed telescoping sum" that
cancels in pairs, leaving the residual. I could not construct this bookkeeping
in the scout, but the n=2 evidence (Xiang achieves `D = 0` for every non-tower
config — `N(t)` even everywhere) suggests it exists at least for small n.

### Sub-route 3: Majorization / doubly-stochastic / rearrangement — LEAST DEVELOPED

**The question.** Is `f(L) = min_Xiang V(refine(L))` monotone in a majorization
order on Liu configs, with the tower as maximal element?

**Finding.** The odd-index sum `V(a) = a_1 + a_3 + …` is **not** Schur-convex or
Schur-concave (it's a non-symmetric functional). But `f(L) = min_Xiang V` — the
min over refinements — might have better structure: a refinement makes `L` more
equal (less spread), and `f` measures the worst-case after equalization. The
tower is the most "spread" config (superincreasing), and it's the hardest to
equalize below `1/D_n`. This is consistent with a majorization-type monotonicity
("more spread ⇒ higher `f`"), but I could not identify the partial order or prove
the monotonicity lemma. The Karamata / majorization entry in `knowledge_base.md`
does not directly apply (no convex function is being summed). This sub-route
needs more scouting; it currently reduces to sub-route 1's exchange argument in
disguise.

---

## (c) Is Lemma B1 (balanced optimum) importable and helpful? — YES, PARTIALLY

`balanced-configs` has no built file (confirmed absent at
`results/imo-2026-03/approaches/balanced-configs.md`); its summary lives in
`.ranking.json` and the round-1 reviewer report. The reviewer certified Lemma B1
as sound: **piecewise-linearity ⇒ Xiang's optimum is attained at a
balanced/tie refinement** (a split where two resulting pieces are equal, or a
piece ties a neighbor).

**Importable?** Yes. My grid search relies on exactly this: including `1/2`
(halving) and `1/k` fractions in the split grid captures the tie points, and the
search finds Xiang-best at these. B1 is a genuine structural fact that would
let a builder restrict to balanced refinements.

**Helpful for this route?** Partially. B1 reduces Xiang's continuous
optimization to a discrete search over balanced-split *types*. Combined with the
exchange argument, it bounds the cases to check. BUT B1 alone does NOT close the
bound — that's the B3 circularity the reviewer flagged ("check every type ≤
bound" = the bound). B1 is a useful IMPORT (restricts the search space) but the
monotonicity/exchange is still the load-bearing missing piece. Recommend: import
B1 into the shared lemma cache if a builder is dispatched on this route, but do
NOT build `balanced-configs` as-is (it's the circular one).

---

## (d) New lemmas worth proposing

**Lemma (Tower-is-hardest-to-pair).** *Conjecture, verified n = 1..4.*
Among all Liu configs `L` with ≤ n+1 pieces summing to 1, the dyadic tower `T_n`
is the unique maximizer of `min_Xiang D` (= `min` over ≤n-mark refinements of the
alternating sum). Equivalently: for every `L ≠ T_n`, Xiang has ≤ n marks with
`D < 1/D_n`; for `L = T_n`, Xiang's best is `D = 1/D_n` (attained by parallel
halving).

**Evidence.** n=2: every non-tower `/7` config admits `D = 0` (not just `≤ 1/7`);
tower alone holds `D = 1/7`. n=3: tower holds `D = 1/15`; all scanned
non-towers give `D ≤ 0` (odd-index = 1/2) or strictly less. Perturbations strict.

**Lemma (Parallel-halving saturates the tower).** *Provable directly.*
Splitting each of the tower's `n` largest pieces in half (one mark each, in
parallel) yields the balanced-pairs config
`{2^{n-1},2^{n-1},…,1,1,1}/D_n` with `D = 1/D_n` exactly, for all n. This is
the UNIQUE balanced refinement of `T_n` attaining `D = 1/D_n`. (Verified n=1..5;
the proof is the dyadic identity `2^k = 2·2^{k-1}`.)

**Lemma (Pairing residual).** *Proposed.* After Xiang uses n marks to split n of
the (n+1) pieces into pairs, the alternating sum `D` equals the length of the
"unpaired median" piece IF all pairs cancel (each pair's two halves land in
adjacent odd/even slots). The tower's dyadic structure forces the unpaired
residual to be exactly `1/D_n`; any ratio deviation lets Xiang reduce the
residual strictly.

---

## (e) Recommendation to the outliner

**Open a new `majorization-upper` slug** attacking the upper bound via the
exchange argument "tower is the unique worst Liu config." The strategy is
**config-adaptive pairing** (formalized through the `D = ∫(N mod 2) dt` residual
language), NOT a fixed rule. This is genuinely different from the inductive
dominant-case-split route. The build should: (1) prove the "parallel-halving
saturates the tower" lemma (mechanical), (2) prove the "tower-is-hardest" exchange
(the crux — show any ratio deviation from dyadic lets Xiang pair better, leaving
residual < 1/D_n), (3) import Lemma B1 to restrict to balanced refinements.
Import `D-equals-parity-integral.md` and `layer-cake-odd-index.md` for the
residual-integral language. Do NOT revive `balanced-configs` as-is (B3 is
circular); harvest only Lemma B1 from it.

**Risk note.** The exchange argument risks the same B3 circularity if it just
checks "every type gives ≤ 1/D_n." The builder must produce a genuine
monotonicity — a smoothing/exchange step showing "moving any ratio toward the
dyadic 2:1 only increases `min_Xiang D`" — not a type enumeration.
