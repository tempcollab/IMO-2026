# Approach: vertex-integrality-parity (integral minimizer → parity of the odd dyadic total)

## Status
partial (round 10) — GAP-IMR NOT closed; this round establishes a rigorous *negative* that
the order-aware smoothing mechanism cannot close it, and that GAP-IMR is logically **equivalent**
(not a reduction) to the target. See Part 4.

## The whole claim this approach proves
GAP L (lower bound, Case B), which closes the entire problem: for every Xiang `≤n`-cut
response in the dyadic integer normalization, `D̃(F) ≥ 1` (equivalently `D* ≥ u_n`,
equivalently `c(n) ≥ 2^n/(2^{n+1}−1)`). Combined with the certified upper bound
(`lemmas/upper-bound.md`) this determines `c(n) = 2^n/(2^{n+1}−1)`.

## Route in one line (revised after the R9 outline review REFUTED the TU core)
`D̃` over the feasible set is minimized; if the minimum is attained at a config with **integer**
part-sizes, then — because the grand total `Σ F = 2^{n+1}−1` is **odd** — `D̃` is a nonnegative
**odd** integer there, hence `≥ 1`. So the whole problem reduces to the **Integer-Minimizer
Reduction**: `inf_F D̃(F)` is attained at (equals `D̃` of) an integer feasible configuration.
The **Parity Lemma** (integer parts + odd total ⇒ `D̃` odd ⇒ `D̃≥1`) is proven and bankable; the
Integer-Minimizer Reduction is the single remaining gap, stated honestly below with its obstruction.

## What the R9 outline review killed (do NOT resurrect)
The originally stated core — "vertices of the cell polytope `Q_{a,σ}` are integral by total
unimodularity (B2)" — is **FALSE** (computationally refuted, R9 review): minimizing vertices are
frequently fractional (`n=2,a=(0,0,1)`: min at `(4,2,½,½)`); per-cell LP minima are often
non-integer (`1.667`, `4.333`); the "round to an integer point of the cell" fallback **overshoots**
(cell `n=2,a=(0,0,1)`: LP min `2`, integer min of that cell `3`). **B2/TU and the cell-rounding
fallback are deleted.** Only the Parity Lemma and the reduction framing survive. Crucially the
reduction is a **GLOBAL** fact (min over the whole feasible union), not cell-local: individual
non-optimal cells have fractional minima with value `>1`, but the *global* optimum lands on integers.

## Imported (certified / proven, do not re-derive)
- **`D̃ = O(F) − E(F) = Σ_i(−1)^{i−1}w_i`** (descending alternating sum of the merged sorted
  multiset), and **`D̃ ≥ 0` always** (pair consecutive descending terms:
  `(w_1−w_2)+(w_3−w_4)+⋯ ≥ 0`), from `induction-recursion-telescope.md` §3, §9; verified `0/2·10⁵`.
- **Structure Lemma** (`induction-recursion-telescope.md` §5): every Case-A/B final multiset is a
  simultaneous refinement `F = ⊎_{j=0}^{n} π_j`, `π_j` a partition of the dyadic value `2^{n−j}`
  into `a_j+1` positive parts, with cut budget `Σ_{j=0}^n a_j ≤ n`. Grand total
  `Σ F = Σ_j 2^{n−j} = 2^{n+1}−1` (independent of the part-sizes).
- **Unified restatement** (`induction-recursion-telescope.md` §9): the whole lower bound is
  `D̃(F) ≥ 1` for every such refinement `F=⊎_{j=0}^n π_j` with `Σa_j≤n`.
- The certified **upper bound** `c(n) ≤ 2^n/(2^{n+1}−1)` (`lemmas/upper-bound.md`, R7): closing GAP L
  determines `c(n)` exactly.

Throughout, the **feasible set** `Φ_n` is the (finite, compact) union over admissible cut vectors
`a=(a_0,…,a_n)`, `Σa_j≤n`, of the polytopes
`P_a = { x ≥ 0 : the a_j+1 coordinates of block j sum to 2^{n−j}, each j }`, and `D̃ : Φ_n → ℝ`
is continuous and piecewise-linear (linear on each merged order-type cell).

---

## Part 1 — The Parity Lemma (FULLY PROVED; promotable)

> **Parity Lemma.** Let `F` be a finite multiset of **integers** `>0` whose total `Σ F` is **odd**.
> Then the descending alternating sum `D̃(F) := Σ_{i}(−1)^{i−1}w_i` (where `w_1≥w_2≥⋯≥w_m` is `F`
> sorted in nonincreasing order) is an **odd** integer. Consequently, since `D̃(F) ≥ 0`, we have
> `D̃(F) ≥ 1`.

**Proof.** Split the sorted list by rank parity: let `O(F)=Σ_{i \text{ odd}}w_i` (odd-rank sum) and
`E(F)=Σ_{i \text{ even}}w_i` (even-rank sum). All `w_i` are integers, so `O(F),E(F)∈ℤ` and
`D̃(F)=O(F)−E(F)∈ℤ`. Now
```
   D̃(F) = O − E = (O + E) − 2E = Σ F − 2E ≡ Σ F  (mod 2),
```
because `2E` is even. By hypothesis `Σ F` is odd, hence `D̃(F)` is odd.

For nonnegativity, pair consecutive descending terms:
```
   D̃(F) = (w_1−w_2) + (w_3−w_4) + ⋯ ,
```
where the last summand is `(w_{m−1}−w_m) ≥ 0` if `m` is even and `+w_m ≥ 0` if `m` is odd; every
summand is `≥ 0` because the list is nonincreasing and the parts are positive. Hence `D̃(F) ≥ 0`.
An odd integer that is `≥ 0` is `≥ 1`. ∎

**Remarks.**
- The two hypotheses are (i) integer parts and (ii) odd total. Both hold for **every** feasible
  `F∈Φ_n` **except** (i): the total is *always* `Σ F = 2^{n+1}−1` (odd, forced by the dyadic
  weights, Structure Lemma), regardless of fractionality. So for an *integer* feasible `F` the
  Parity Lemma fires immediately and gives `D̃(F)≥1`. The **only** missing ingredient for the full
  target is that some *minimizer* is integer — Part 3.
- This is the genuine non-local injection of the constant `1`: it is the **parity of the odd dyadic
  grand total `2^{n+1}−1`**. Every measure/merged-order/reserve/genfn framing (R8 meta) sees only
  `D̃ ≥ 0`; the Parity Lemma is exactly the `+1` upgrade those framings provably cannot supply,
  and it is *not* one of them (it is not a profile of the final multiset — it reads the integrality
  of the parts and the parity of the total).
- The hypothesis is odd **total**, NOT odd part-count (the R9 review flagged this distinction).
- Numerically verified: over `2·10⁵` random integer multisets of odd total, `0` had even `D̃`;
  over all integer feasible configs for `n≤5` (Part 2), the minimum `D̃` is exactly `1`, always odd.

---

## Part 2 — The integer minimum is exactly `1`, attained (construction)

> **Integer-value Lemma.** `min\{ D̃(F) : F∈Φ_n,\ F \text{ integer} \} = 1`.

**Proof.** *Lower bound.* Every integer `F∈Φ_n` has odd total `2^{n+1}−1` and integer parts, so
`D̃(F)≥1` by the Parity Lemma.

*Attainment — explicit integer family (`D̃=1`).* For `n=1` take `F=\{2,1\}` (cut vector `a=(0,0)`),
`D̃=2−1=1`. For `n≥2` take the cut vector `a` with `a_j=1` for `0≤j≤n−2` and `a_{n−1}=a_n=0`
(`Σa_j=n−1≤n`), and the splits
```
   π_j = \{2^{n−1−j}, 2^{n−1−j}\}   (each cut piece 2^{n−j} halved),  0 ≤ j ≤ n−3,
   π_{n−2} = \{3, 1\}   (the piece 2^2=4 cut as 3+1),
   π_{n−1} = \{2\},   π_n = \{1\}   (pieces 2 and 1 uncut).
```
The merged multiset is `\{2^{n−1},2^{n−1},\,2^{n−2},2^{n−2},\,…,\,4,4,\,3,2,1,1\}`: the `n−2` equal
pairs `\{2^{k},2^{k}\}` (`k=2,…,n−1`) occupy the top `2(n−2)` ranks and cancel in the alternating sum
(each pair sits at consecutive ranks `2t−1,2t` contributing `+2^k−2^k=0`), and the four-part tail
`3,2,1,1` (ranks `2n−3,…,2n`) contributes `3−2+1−1=1`. Hence `D̃=1`. Worked instances (exact
`Fraction`):
```
   n=1:  {2,1}                 D̃ = 2−1 = 1
   n=2:  {3,1, 2, 1}           D̃ = 3−2+1−1 = 1
   n=3:  {4,4, 3,1, 2, 1}      D̃ = 4−4+3−2+1−1 = 1
   n=4:  {8,8, 4,4, 3,1, 2, 1} D̃ = 8−8+4−4+3−2+1−1 = 1
```
(An alternative attaining integer config is the certified tie family, `n=4:` `Y=(8,3,3,2)`,
`Z=(8,2,2,2,1)`, merged `\{8,8,3,3,2,2,2,1\}`, `D̃=8−8+3−3+2−2+2−1=1`.) Combined with the lower bound,
`min` over integer feasible configs is exactly `1` — confirmed independently by exhaustive
enumeration for `n≤5` (`0` violations). ∎

This attainment also **verifies the final answer is tight**: `D̃ = 1` in integer units means
`D* = u_n`, whence `c(n) = (1+u_n)/2 = 2^n/(2^{n+1}−1)`, matching the certified upper bound.

---

## Part 3 — Reduction to an integer minimizer (the sole remaining gap)

> **Main Reduction.** *If* `inf_{F∈Φ_n} D̃(F)` is attained at some **integer** feasible
> configuration (equivalently: `min_{Φ_n} D̃ = min\{D̃(F):F\in Φ_n \text{ integer}\}`), *then*
> `D̃(F)≥1` for **every** `F∈Φ_n`, i.e. GAP L holds and the problem is solved.

**Proof of the reduction (the easy direction — FULLY RIGOROUS).** `Φ_n` is compact (a finite union
of compact polytopes) and `D̃` is continuous, so `μ := min_{Φ_n}D̃` is attained. By hypothesis it is
attained at an integer `F^*∈Φ_n`. Then `μ = D̃(F^*) ≥ 1` by Parts 1–2 (integer parts, odd total).
Since `μ` is the global minimum, `D̃(F)≥μ≥1` for all `F∈Φ_n`. ∎

So the whole problem is now the single statement:

> **(GAP-IMR) Integer-Minimizer Reduction.** `min_{Φ_n}D̃ = min\{D̃(F):F∈Φ_n \text{ integer}\}`.

Equivalently, the **Rounding Claim**: *for every `F∈Φ_n` there is an integer `F'∈Φ_n` with
`D̃(F')≤D̃(F)`.* (Rounding Claim ⇒ GAP-IMR trivially; and GAP-IMR ⇒ target via the Main Reduction.)

**This is NOT circular with the target.** GAP-IMR/Rounding Claim make no reference to the *value* `1`;
they assert only that the minimum is achieved on the integer sublattice. Proving GAP-IMR does not
presuppose `D̃≥1`. (This addresses the R8/R9 circularity trap: the reduction is a statement about
*where* the min lives, orthogonal to its value.)

### 3.1 What is established toward GAP-IMR

1. **The minimizer is rational and can be taken at a cell vertex.** On each merged order-type cell
   `Q_{a,σ}` (adjoin the ordering inequalities `w_{σ(i)}≥w_{σ(i+1)}` of the active cell to `P_a`),
   `D̃` is *linear*; `min_{P_a}D̃ = min_{σ}min_{Q_{a,σ}}D̃`, each inner min attained on a face of a
   rational polytope, hence at a rational vertex. So `μ` is rational and attained at a rational
   vertex `v^*` of some `Q_{a,σ}`. (Standard LP: a linear functional on a polytope attains its min
   on a face, whose vertices are vertices of the polytope; all data here is integral so vertices are
   rational. This is the salvaged, correct part of the old "B1".)

2. **If `v^*` is integer, done.** Then `μ=D̃(v^*)≥1` by Parts 1–2. So GAP-IMR fails only if *every*
   global minimizer vertex is fractional — the case to be excluded.

3. **The global optimum lands on integers (verified `n≤3`, exact).** By LP over *all* order-type
   cells (`scipy.optimize.linprog`, then re-examined with exact arithmetic): the continuum minimum
   `min_{Φ_n}D̃ = 1` for `n=1,2,3`, equal to the integer minimum (Part 2). Moreover **every**
   order-type cell whose LP minimum equals the global value `1` has an **integer** vertex minimizer
   (`0` optimal cells with a fractional vertex minimizer, `n=2,3`). Fractional vertices occur *only*
   in cells whose minimum is `>1` (e.g. `(4,2,½,½)` at value `2`). This is precisely the "GLOBAL, not
   cell-local" character of GAP-IMR: the coincidence `continuum-min = integer-min` holds even though
   it *fails* cell-by-cell. Certified R7 numerics independently give `0/2·10⁵` violations of `D̃≥1`
   for `n≤6`, consistent with `continuum-min = 1`.

### 3.2 The obstruction (why a naive rounding does not close GAP-IMR — honest gap)

The natural attempt "integralize one fractional tie-block at a time" **fails**, and understanding
why pins the exact difficulty:

- At a vertex `v^*`, the merged order splits into maximal **tie-blocks** (runs of equal consecutive
  values). A block `B` of size `r`, value `v`, occupying ranks `i,…,i+r−1`, contributes
  `Σ_{s=0}^{r−1}(−1)^{i−1+s}v = (−1)^{i−1}v·\mathbf 1[r\text{ odd}]` to `D̃` — so an **even** block
  contributes `0` (and is freely re-splittable without changing `D̃`), while an **odd** fractional
  block contributes a *fractional* value (this is the source of the reviewer's `1.667` cell-minima).
- To integralize block `B` while **preserving feasibility**, each group `g` contributing `n_g` parts
  to `B` must keep its block-sum `n_g·v` fixed (so the group total `2^{n−j}` is unchanged). If
  `n_g·v ∉ ℤ` for some group, the `n_g` integer values summing to `n_g·v` **cannot exist** — a
  single-block integralization is *impossible*. This is exactly the reviewer's "rounding overshoots":
  the only way to fix it is to move compensating mass **into other blocks of the same group**, which
  couples the blocks and makes the argument **global**.

So GAP-IMR requires a genuinely global mass-transfer / integral-flow argument on the *whole* config,
not a per-block or per-cell rounding. This is the same "the compensation is global, not local" wall
the R7 §10 / R8 meta identified, now surfacing as: *the integral structure lives across dyadic scales
simultaneously, tied together by the group-sum constraints `Σ(π_j)=2^{n−j}`.*

### 3.3 What a proof of GAP-IMR would need (for the next builder/outliner)

A correct closure must show: *the global minimum face of `D̃` over `Φ_n` contains an integer point.*
Two live shapes, neither yet rigorous:
- **(Even-block / flat-face rounding).** Prove that at a **global** minimizer vertex every fractional
  tie-block is *even* (hence contributes `0` to `D̃`), and that the union of even fractional blocks
  can be re-split into integers using cross-block mass transfer that stays on the optimal face
  (`D̃` unchanged). The `n≤3` data (all optimal vertices integer) is consistent with "no odd
  fractional block at a global optimum," but this is **unproven** and is the crux — odd fractional
  blocks *do* occur at non-optimal vertices, so the argument must use minimality (not just the cell
  geometry) to exclude them at the optimum.
- **(Integral polytope for the optimal cells only).** Identify a network/flow reformulation of
  `P_a ∩ \{D̃=μ\}` that is totally unimodular *for the optimal cells* (TU fails for general cells,
  R9 review, so this must exploit optimality). Not attempted.

**This is the honest open gap (GAP-IMR).** It is strictly the "does the global min sit on the
integer sublattice" question; the Parity Lemma then finishes. It is not equivalent to the target as a
proof obligation (§3, non-circularity), but I could not close it this round.

---

## Part 4 — Round-10 attempt at GAP-IMR via order-aware smoothing: a rigorous NEGATIVE

The Round-10 plan was: at a global minimizer `v*`, if fractional, kill odd fractional tie-blocks
by a joint same-group order-preserving perturbation that descends a fractionality monovariant while
keeping `D̃` non-increasing, terminating at an integer minimizer. I attempted this in full. It does
**not** close GAP-IMR, and I can now say **precisely why**, with exact-`Fraction` computation.

### 4.1 GAP-IMR is *logically equivalent* to the target (not a genuine reduction)

The approach file (§3, R9) claimed GAP-IMR is "non-circular / orthogonal to the value `1`." That is
false once Part 2 is used. Part 2 **proves** `min\{D̃(F):F∈Φ_n \text{ integer}\}=1`. Therefore:

> **Equivalence.** GAP-IMR `⟺` (Target `D̃(F)≥1 ∀F∈Φ_n`).

*Proof.* Write `μ=min_{Φ_n}D̃` (attained, `Φ_n` compact). Integer configs are feasible, so
`μ ≤ 1`. GAP-IMR says `μ = min_{integer}D̃ = 1` (Part 2). And Target says `μ ≥ 1`; combined with
`μ ≤ 1` this is `μ = 1`. Hence GAP-IMR `⟺ (μ=1) ⟺` Target. ∎

So GAP-IMR is a **reformulation** of the whole lower bound, not a strict sub-problem: proving it is
exactly as hard as proving `D̃≥1` on the continuum. The Parity Lemma supplies the `+1` **only at an
integer config**; *reaching* an integer config with `D̃≤μ` is the entire problem. This corrects the
R9 "non-circularity" note: the framing localizes the difficulty (it lives in the fractional-vs-integer
optimum question) but does not lower it.

### 4.2 Exact-computation structure of the optimum (new, exact `Fraction` / exact vertex enumeration)

- **Global continuum minimum is `1` for `n=1,2,3`** (LP over every order-type cell of every cut
  vector, `scipy.highs`): `n=1` min `1` at `(2,1)`; `n=2` min `1` at `(2,2,2,1)`; `n=3` min `1` at
  `(4,4,2,2,2,1)`. Matches the integer minimum (Part 2).
- **Every order-cell whose LP minimum equals the global value `1` returns an *integer* minimizer
  vertex.** Exact recount this round: `n=2`, **`0/90`** min-value LPs fractional; `n=3`,
  **`0/1134`** fractional. So for `n≤3` GAP-IMR is *true* and *proved* by exhaustive exact LP.
- **Fractional vertices with ODD fractional tie-blocks DO exist** — but *only off the optimum*.
  Exact vertex enumeration of all cells for `n=2` found `42` vertices carrying an odd-size fractional
  tie-block, e.g. `\{4,2,\tfrac13,\tfrac13,\tfrac13\}` (cut `(0,0,2)`, odd block of three `\tfrac13`,
  `D̃=7/3`) and `\{4,\tfrac32,\tfrac12,\tfrac12,\tfrac12\}` (cut `(0,1,1)`, odd singleton `\tfrac32`,
  `D̃=3`). **Every one has `D̃>1`.** So odd fractional blocks are not excluded by cell geometry
  (they occur), only by *minimality* — and excluding them at the optimum is precisely `μ=1`, i.e.
  the target (4.1).

### 4.3 Why the smoothing mechanism cannot descend (the load-bearing step provably fails)

The mechanism needs, at a **fractional global minimizer** `v*`, a feasibility-preserving perturbation
that is `D̃`-**non-increasing** in some direction while strictly reducing fractionality. Two fatal
facts:

1. **No fractional global minimizer is available to descend from (for the only `n` we can certify).**
   For `n≤3` *every* minimizer vertex is integer (4.2), so the mechanism's entire non-trivial case is
   **vacuous** and cannot even be exercised, let alone validated by the mandated exact-`Fraction`
   probe. There is no witness on which to test "`D̃` non-increasing," so the scheme is numerically
   ungroundable exactly where it must work.

2. **At an *isolated* fractional vertex, NO `D̃`-non-increasing feasible move exists.** A vertex `v*`
   of an order-cell is the unique solution of its `m` tight constraints (`n+1` integer group-sum
   equalities plus `Σa_j` tight ties/zeros). If `v*` is isolated on its `D̃`-level set inside `Φ_n`
   (0-dimensional optimal face there), then *every* feasible perturbation `d` has
   `D̃'(v*;d)>0` — because `μ=D̃(v*)` is a strict local min along every feasible ray (that is what
   "isolated on the level set" means). Hence there is **no** direction that keeps `D̃≤μ` while moving,
   so the monovariant cannot be decreased at all. The odd-fractional-block vertices of 4.2 (e.g.
   `\{4,2,\tfrac13,\tfrac13,\tfrac13\}`: the three `\tfrac13` are the *whole* group `2`, any feasible
   move splits their tie and strictly raises `D̃`) are exactly of this isolated, un-descendable type.
   So *if* a fractional minimizer ever occurred, the smoothing could not process it.

Combining 1–2: the order-aware smoothing is **not** a viable engine for GAP-IMR. It works only in the
regime where `v*` is already integer (nothing to do) or where the optimal face is positive-dimensional
with a fractional relative-interior point — but that case is trivial (a positive-dim optimal face is
the convex hull of its vertices, and the vertices are the very objects whose integrality is in
question, so "move to a vertex" begs the question unless the vertices are already known integer).

### 4.4 What survives, and where the difficulty truly sits

- The **reduction** (Part 3) and the **Parity Lemma** (Part 1, certified) are correct and remain the
  right *finishing device* for any route that reaches an integer optimum.
- **GAP-IMR is proved for `n≤3`** (exact LP, 4.2).
- For general `n`, GAP-IMR `=` target (4.1); the missing content is *value-based* — exclude
  fractional vertices of `D̃`-value `<1` — which is **not** obtainable by a local
  `D̃`-non-increasing descent (4.3). It requires either (i) a *global* argument that some integer
  config beats every fractional one (the Rounding Claim, itself `⟺` target by the same equivalence),
  or (ii) the direct real-valued induction of the **peel** route (`peel-scale-rank-induction`), which
  proves `D̃≥1` on the continuum without any integrality detour and is the field's only
  integrality-independent line. This confirms the imr-explorer's "merge GAP-IMR into the peel
  induction" recommendation and the outline-reviewer's WATCH: the two GAP-IMR slugs share this wall
  and the peel route is the one that does not hit it.

## Status of the pieces
- Parity Lemma (Part 1): **PROVED**, promotable/certifiable, independent of everything else.
- Integer-value Lemma + tightness/answer verification (Part 2): **PROVED** (Parity Lemma + explicit
  integer family with `D̃=1`).
- Main Reduction (Part 3, easy direction): **PROVED** — GAP-IMR ⇒ full target ⇒ problem solved.
- GAP-IMR (general `n`): **OPEN**, and now shown **logically equivalent to the target** (Part 4.1),
  so no easier than the whole lower bound. **Proved for `n≤3`** by exact LP (Part 4.2). The
  order-aware smoothing engine is **refuted** (Part 4.3): vacuous case for `n≤3`, and no
  `D̃`-non-increasing descent at isolated fractional vertices. Residual content is value-based and
  belongs to the peel real-valued induction, not to any integer-minimizer/rounding mechanism.

## Approaches tried
- **(round 10 build — GAP-IMR via order-aware smoothing)** Attempted the outliner's minimality-driven
  smoothing (kill odd fractional tie-blocks by joint same-group order-preserving perturbation,
  descend a fractionality monovariant with `D̃` non-increasing). **Refuted as an engine** by two
  rigorous facts (Part 4): (i) exact LP shows *every* min-value(=1) vertex is integer for `n≤3`
  (`0/90` at `n=2`, `0/1134` at `n=3`), so the mechanism's non-trivial case is **vacuous** and
  ungroundable; (ii) at an *isolated* fractional vertex (which is exactly the shape of the odd-frac
  vertices that exist, e.g. `\{4,2,\tfrac13,\tfrac13,\tfrac13\}`, `D̃=7/3`) *no* `D̃`-non-increasing
  feasible move exists, so the descent cannot start. Also proved (Part 4.1) GAP-IMR is **logically
  equivalent** to the target (`⟺ μ=1`) once Part 2's integer-min`=1` is used — a *reformulation*, not
  a reduction; the R9 "non-circularity" claim is thereby corrected. **Positive:** GAP-IMR is now
  *proved for `n≤3`* by exhaustive exact LP. → **partial** (mechanism refuted; framing shown
  equivalent-difficulty; the value-based exclusion of sub-`1` fractional vertices needs the peel
  route, not smoothing).
- **(round 9 build — GAP L)** Original TU core (B2: cell vertices integral) **REFUTED** by the R9
  outline review (fractional minimizing vertices; cell-min values `1.667`; rounding overshoots
  `2→3`). Salvaged and rigorized the **Parity Lemma** (integer multiset + odd total ⇒ `D̃` odd ⇒
  `D̃≥1`) as a standalone bankable lemma. Reframed the open wall honestly as the **Integer-Minimizer
  Reduction (GAP-IMR)**: `min_{Φ_n}D̃ = min` over integer configs; proved the **reduction direction**
  (GAP-IMR + Parity ⇒ full target) rigorously, and proved integer-min `=1` with an explicit
  attaining family (verifies the answer `c(n)=2^n/(2^{n+1}−1)` is tight). Established: minimizer is
  rational at a cell vertex; global optimum is integer-attained for `n≤3` (exact LP, all optimal
  cells have integer vertex minimizers — a GLOBAL, not cell-local, phenomenon). Identified the exact
  obstruction to naive rounding (odd fractional tie-blocks contribute fractional value; single-block
  integralization blocked by fractional group-block-sums `n_g·v∉ℤ`; requires cross-block global mass
  transfer). → **partial** (Parity Lemma banked; integer-minimizer reduction is the isolated open gap).
- (prior rounds recorded in run_state; TU/B2 skeleton is now retired.)

## Current best
Fully proved and bankable: the **Parity Lemma** (certified) and the **reduction**
GAP-IMR ⇒ target, plus **integer-min `=1`** with an explicit attaining family (verifies the answer
`c(n)=2^n/(2^{n+1}−1)` is tight), and **GAP-IMR itself proved for `n≤3`** by exhaustive exact LP
(every min-value vertex integer: `0/90`, `0/1134`). The genuine, sharpened finding this round: with
integer-min`=1` in hand, **GAP-IMR is logically equivalent to the target** (`⟺ μ=1`), so it is a
reformulation, not a difficulty-reducing sub-problem; and the proposed order-aware smoothing **cannot
close it** — its only non-trivial case (a fractional global minimizer) is vacuous for `n≤3` and, at
the isolated fractional vertices that do exist off the optimum (`\{4,2,\tfrac13,\tfrac13,\tfrac13\}`,
`D̃=7/3`), admits **no** `D̃`-non-increasing feasible move to descend along. The residual content is
value-based (exclude fractional vertices of value `<1`) and belongs to the **peel real-valued
induction**, not to any integer-minimizer/rounding mechanism. Recommendation: retire the GAP-IMR
mass-transfer line as an independent engine; fold the Parity Lemma in as the *base/finishing* device
of the peel induction (integer configs are closed for free), and route all remaining effort to
`peel-scale-rank-induction`.

## Promotable lemmas
- **Parity Lemma.** For any finite multiset `F` of positive integers with **odd** total `Σ F`, the
  descending alternating sum `D̃(F)=Σ_i(−1)^{i−1}w_i` is odd, and since `D̃(F)≥0` (pair consecutive
  descending terms) it satisfies `D̃(F)≥1`. Proof: `D̃=ΣF−2E≡ΣF≡1\ (\mathrm{mod}\ 2)` and `D̃≥0`.
  Proved in full in Part 1 above; verified `0` even over `2·10⁵` random odd-total integer multisets.
  Reusable by any GAP-L approach that reaches an integer configuration (it is the `+1` upgrade of the
  trivial `D̃≥0` that no measure/merged-order/sequential/genfn framing can supply). **Hypothesis is
  odd TOTAL, not odd part-count.** (Already certified: `lemmas/parity-odd-total.md`; imported, not
  re-promoted.)
- **GAP-IMR ⟺ Target (equivalence note, proved Part 4.1).** For the P3 feasible set,
  `min_{Φ_n}D̃ = min\{D̃(F):F\text{ integer}\}` holds **iff** `D̃(F)≥1` for all `F∈Φ_n`, because the
  integer minimum is `1` (Part 2) and integer configs are feasible (`min_{Φ_n}D̃≤1`). *Use:* warns
  any future approach that "reduce to an integer minimizer" is not a genuine reduction of this lower
  bound. Not a reusable positive lemma, but a reusable **caution** for the outliner.

## Spec concern (for the orchestrator/outliner)
**GAP-IMR is not a genuine reduction of the target — it is logically equivalent to it** (Part 4.1),
once integer-min`=1` (Part 2, proved) is used. Both GAP-IMR slugs (`vertex-integrality-parity`,
`peel-integral-exchange`) are therefore attacking the full lower bound in disguise, via mass-transfer
mechanisms that this round are shown insufficient (smoothing has no descent at isolated fractional
vertices; per-group rounding refuted R9; per-cell TU refuted R9). The field should **NOT** open a
fourth GAP-IMR/rounding variant. Concretely for R11:
- **Retire the integer-minimizer/rounding line as a standalone engine.** Keep the **Parity Lemma** and
  reduction only as the *finishing device folded into the peel induction* (integer configs closed for
  free — a clean base case), not as a separate approach.
- **Concentrate on `peel-scale-rank-induction`** — the only route that proves the real-valued
  `D̃≥1` directly, with no integrality detour, so it does not hit this wall.
- If the peel route also stalls, seed the reserved *far* framing that avoids the odd-total parity
  entirely: 2-adic valuation split `N=N_++N_-` (aimo-0917), or a monovariant descent transporting
  every feasible `F` to the canonical `D̃=1` family `\{2^{n−1},2^{n−1},…,3,2,1,1\}` by
  budget-preserving `D̃`-non-increasing moves — a *global-to-canonical* descent rather than a
  local integralization.
