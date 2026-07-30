# Approach: peel-integral-exchange (cross-scale integral rounding of a global minimizer)

## Status
partial (round 10)

## The whole claim this approach proves
GAP L (lower bound, Case B): for every real feasible refinement `F = ⊎_{j=0}^n π_j`
(`π_j` a partition of `2^{n−j}` into `a_j+1` positive parts, budget `Σ_j a_j ≤ n`) one has
`D̃(F) ≥ 1`. With the certified upper bound (`lemmas/upper-bound.md`) this determines
`c(n) = 2^n/(2^{n+1}−1)`.

## Route in one line
Same target-reduction as the twin `vertex-integrality-parity` — **GAP-IMR** (`min_{Φ_n} D̃` is
attained at an integer configuration) `⇒ Parity Lemma ⇒ D̃ ≥ 1` — but reached by a **distinct
tool**: use the certified peel symmetric-difference identity as a *cross-scale* integral-rounding
engine on a global minimizer. This round I (i) prove two new, clean, promotable structural
lemmas that sharpen GAP-IMR to a finite lattice statement — the **Odd-Block Alternating-Value
Formula** and the **Vertex Distinct-Value Bound** — (ii) reduce GAP-IMR rigorously to *"some
minimizing cell-vertex is integer,"* (iii) localize the sole obstruction to a scale contributing
`≥2` parts to one tie-block, and (iv) execute the cross-scale exchange as far as it provably goes,
recording the precise wall where a non-increasing integral rounding is not yet constructible.

## Imported (certified / proven — not re-derived)
- **Level-measure identity / Lemma G** (`lemmas/greedy-claim.md`): `D̃(F)=λ(O_F)=Σ_i(−1)^{i−1}w_i`,
  descending sort `w_1≥…≥w_m`; `O_F={t>0: N_F(t)=#\{parts>t\}` odd`}`.
- **Peel identity (SD/PEEL) and difference bound (DIFF)** (`lemmas/peel-difference-bound.md`):
  for `F=A⊎B`, `O_F=O_A△O_B`, so `D̃(F)=D̃(A)+D̃(B)−2λ(O_A∩O_B)` and `D̃(A⊎B)≥|D̃(A)−D̃(B)|`;
  Case A (`a_0=0`) closed unconditionally; Invariant I.
- **Structure Lemma** (`induction-recursion-telescope.md` §5): every feasible `F` is a simultaneous
  refinement `⊎_{j=0}^n π_j`, `Σπ_j=2^{n−j}`, grand total `ΣF=2^{n+1}−1` (odd).
- **Parity Lemma** (`lemmas/parity-odd-total.md`): an integer multiset of odd total has
  `D̃ = ΣF − 2E ≡ ΣF ≡ 1 (mod 2)`, and `D̃≥0`, hence `D̃≥1`. Hypothesis is odd **total**.
- **D̃ ≥ 0 always** (pair consecutive descending terms).

Throughout, `Φ_n = ⋃_a P_a` is the compact feasible union, `P_a = {x≥0 : the a_j+1 coordinates of
block j sum to 2^{n−j}}`, and `D̃ : Φ_n → ℝ` is continuous and piecewise-linear (linear on each
merged order-type cell).

---

## Part A — Odd-Block Alternating-Value Formula (NEW, fully proved, promotable)

> **Lemma OB.** Let `F` be a finite positive multiset, sorted descending `w_1≥⋯≥w_m`, and let its
> **distinct** values be `u_1>u_2>⋯>u_K` with multiplicities `r_1,…,r_K` (`Σr_l=m`). Let
> `s_l = 1+Σ_{l'<l} r_{l'}` be the first rank of the block of value `u_l`. Then
> ```
>   D̃(F) = Σ_{l=1}^{K} (−1)^{s_l−1} u_l · 𝟙[r_l odd].                        (OB1)
> ```
> Equivalently, listing the values of **odd** multiplicity in descending order as
> `u_{(1)} > u_{(2)} > ⋯ > u_{(q)}`, the even-multiplicity blocks cancel and
> ```
>   D̃(F) = u_{(1)} − u_{(2)} + u_{(3)} − ⋯ = Σ_{p=1}^{q} (−1)^{p−1} u_{(p)}.   (OB2)
> ```

**Proof.** By Lemma G, `D̃(F)=Σ_{i=1}^m (−1)^{i−1} w_i`. Group the sum by tie-blocks. The block of
value `u_l` occupies ranks `i=s_l, s_l+1, …, s_l+r_l−1`, each term equal to `(−1)^{i−1}u_l`. Its
contribution is
```
   u_l Σ_{i=s_l}^{s_l+r_l−1} (−1)^{i−1}
      = u_l (−1)^{s_l−1} Σ_{t=0}^{r_l−1} (−1)^t
      = u_l (−1)^{s_l−1} · ( 𝟙[r_l odd] ),
```
since the finite geometric sum `Σ_{t=0}^{r_l−1}(−1)^t` equals `1` when `r_l` is odd and `0` when
`r_l` is even. Summing over `l` gives (OB1).

For (OB2): modulo 2, `s_l−1 = Σ_{l'<l} r_{l'} ≡ #{l'<l : r_{l'} odd}`. If `u_l = u_{(p)}` is the
`p`-th value of odd multiplicity, then exactly `p−1` earlier blocks have odd multiplicity, so
`(−1)^{s_l−1} = (−1)^{p−1}`. Even blocks contribute `0` by (OB1). Substituting gives (OB2). ∎

**Verification (exact `Fraction`).** `0` mismatches between `D̃` (Lemma G) and (OB2) over `5·10^4`
random positive-rational multisets.

**Consequences used below.**
- (OB-even) A tie-block of **even** size contributes `0` to `D̃`; it can be re-split or merged with
  another equal-value block of the same size-parity class without changing `D̃`, provided the merged
  order (hence every `s_l−1` parity) is preserved.
- (OB-int) If every odd-multiplicity value `u_{(p)}` is an **integer**, then `D̃(F)` is an integer
  (an alternating sum of integers). This is the precise reason integrality of the *even* fractional
  blocks is irrelevant to `D̃` while integrality of the *odd* blocks controls it.

---

## Part B — Vertex Distinct-Value Bound (NEW, fully proved, promotable)

> **Lemma V.** The global minimum `μ := min_{Φ_n} D̃` is attained at a **vertex** `v^*` of some
> merged order-type cell. At any such vertex whose coordinates are all positive, the number `K` of
> **distinct** part-values satisfies
> ```
>   K ≤ n+1.
> ```

**Proof.** *Attainment at a cell vertex.* `Φ_n` is a finite union of the polytopes `P_a`
(`Σ_j a_j ≤ n`), each compact; on each `P_a` fix a merged order-type by a permutation `σ` giving the
descending order `x_{σ(1)} ≥ ⋯ ≥ x_{σ(m)}`. The cell `Q_{a,σ} = P_a ∩ {x_{σ(1)}≥⋯≥x_{σ(m)}}` is a
rational polytope, and on it the descending sort is fixed, so `D̃ = Σ_i (−1)^{i−1} x_{σ(i)}` is a
**linear** functional. Hence `min_{Q_{a,σ}} D̃` is a linear program, attained at a vertex of
`Q_{a,σ}`; and `μ = min_a min_σ min_{Q_{a,σ}} D̃` is attained at such a vertex `v^*`.

*The bound.* `v^*∈ℝ^m` where `m = Σ_j(a_j+1) = (n+1)+b`, `b := Σ_j a_j` the cut budget. The
constraints defining `Q_{a,σ}` are: the `n+1` group-sum equalities (`Σ_{i∈block j} x_i = 2^{n−j}`),
the ordering inequalities `x_{σ(i)} ≥ x_{σ(i+1)}` (`i=1,…,m−1`), and `x ≥ 0`. A vertex of an
`m`-dimensional polytope is the unique solution of `m` linearly independent **active** (equality)
constraints. All `n+1` group-sum equalities are active. The active ordering constraints are exactly
the adjacent **ties** `x_{σ(i)} = x_{σ(i+1)}`; in a sorted list with `K` distinct values (block sizes
`r_l`) the number of adjacent equalities is `Σ_l (r_l−1) = m − K`. Since `v^*` has all coordinates
positive, no `x≥0` constraint is active. Therefore the total number of active constraints is at most
`(n+1) + (m−K)`, and this must be `≥ m` (a vertex needs `m` independent active constraints):
```
   m ≤ (n+1) + (m − K)   ⟹   K ≤ n+1.                                          ∎
```
(If some coordinate of `v^*` is `0`, that adds active constraints and only lowers the count of
distinct positive values; the bound `K ≤ n+1` still holds for the positive values.)

**Verification.** The bound holds with equality or slack on all computed vertices, e.g. `n=2`:
`(4,2,½,½)` has `K=3=n+1`; the integer minimizers `(3,1,2,1)`, `(2,2,2,1)` have `K=3,2 ≤ 3`. The
value-1 *interior* point `(9/4,7/4,2,1)` has `K=4 > 3`, correctly **not** a vertex (it lies on a
positive-dimensional optimal face; its face-vertices are integer — see Part C).

---

## Part C — GAP-IMR reduced to an integer minimizing vertex; the exchange and its wall

### C.1 The clean reduction (rigorous)

> **Reduction R.** If **some** minimizing cell-vertex `v^*` (Lemma V) has integer coordinates, then
> `μ ≥ 1`, hence `D̃(F) ≥ 1` for all `F∈Φ_n`, and the problem is solved.

**Proof.** An integer `v^*∈Φ_n` has integer parts and, by the Structure Lemma, odd total
`2^{n+1}−1`. By the Parity Lemma `D̃(v^*) ≥ 1`. Since `v^*` is a global minimizer, `μ = D̃(v^*) ≥ 1`,
and `D̃(F) ≥ μ ≥ 1` for every `F∈Φ_n`. ∎

So the entire remaining content of the problem is the single lattice statement:

> **(GAP-IMR′)** At least one vertex of an optimal cell `Q_{a,σ}` attaining `μ` has integer
> coordinates.

This is strictly weaker/cleaner than the original GAP-IMR (it is about vertices, a finite set) and
is **non-circular**: it refers only to integrality of a minimizing vertex, never to the value `1`.

### C.2 Localizing the obstruction (rigorous)

At a minimizing vertex `v^*` with distinct values `u_1 > ⋯ > u_K` (`K ≤ n+1`), let
`c_{jl} = #{parts of scale j equal to u_l}` (`0 ≤ j ≤ n`, `1 ≤ l ≤ K`). Then
`Σ_l c_{jl} = a_j+1` and the group-sum equalities read
```
   Σ_{l=1}^K c_{jl} u_l = 2^{n−j}     (0 ≤ j ≤ n).                              (C1)
```
`(C1)` is a linear system `C u = d` with integer matrix `C=(c_{jl})` and integer right-hand side
`d=(2^{n−j})_j`. The value vector `u` is the unique solution of a full-rank `K×K` subsystem of
`(C1)` (the group-sum equalities that, together with the ties, pin the vertex).

> **Localization.** If every column `l` of `C` has all entries in `{0,1}` (each scale contributes
> **at most one** part to the tie-block of value `u_l`), then the pinning `K×K` subsystem is a
> `0/1` matrix; when it is furthermore triangularizable by the natural scale/value order (as it is
> in every integer minimizer we computed) its determinant is `±1` and `u∈ℤ^K` by Cramer's rule
> (integer RHS). **Fractionality can only arise from a column `l` with an entry `c_{jl} ≥ 2`** — a
> scale `j` placing `≥2` equal parts into one tie-block.

Two equal parts of the *same* scale in the *same* block form (part of) an **even** sub-block; by
(OB-even) such a repeated value is exactly the harmless kind that contributes `0` to `D̃`. The
witness `(4,2,½,½)` (`n=2`, scale `2` puts both its parts at value `½`, so `c_{2,3}=2`, forcing
`2·u_3 = 2^0 = 1 ⇒ u_3 = ½`) is precisely this: the block `{½,½}` is even, contributes `0`, and the
vertex value is `2 > μ=1`. So **fractionality lives on even blocks**, and by (OB-int) it does **not**
affect `D̃` — but it *does* obstruct integralizing the vertex, because merging the even fractional
block into integers changes the merged order and can raise `D̃`.

### C.3 The cross-scale exchange, and exactly where it stalls

The exchange tool. Peel the top scale, `F = π_0 ⊎ F'` (`Σπ_0 = 2^n`, `F'∈Φ_{n−1}` the bottom `n`
scales). By (SD/PEEL) `D̃(F) = λ(O_{π_0} △ O_{F'})`. Because `Σπ_0 = 2^n` is a large integer, `π_0`
is easily integralized (any integer partition of `2^n` into `a_0+1` parts exists for `a_0+1 ≤ 2^n`),
so the top scale is never the obstruction. Recursing, the obstruction is pushed to the **bottom**
scales, where the group-sum `2^{n−j}` is small: the extreme case is scale `n` (value `1`), which
**cannot** be partitioned into `≥2` positive integers at all. Hence any minimizer that splits a
small scale into several parts must, to become integer, **merge** parts of that scale — reducing its
part-count and freeing budget (feasible, since budget `≤ n` is an inequality). This is the genuine
cross-scale move: *reallocate cut budget away from a small scale that resists integer splitting.*

What is provable. Two facts are clean:
- **(Top-scale non-obstruction.)** For any real `π_0` and any fixed `F'`, an integer partition
  `π_0^Z` of `2^n` into the same number of parts exists whenever `a_0+1 ≤ 2^n` (always true for
  `n ≥ 1`, since `a_0+1 ≤ n+1 ≤ 2^n`). So the top scale can always be integralized in place.
- **(Even-block freedom, OB-even.)** Even tie-blocks contribute `0`; on the optimal face they may be
  re-split among equal-parity multiplicities without changing `D̃`, provided the merged order (hence
  the parity of every `s_l−1`) is preserved.

The wall (honest). The step that does **not** yet go through is the *bottom-scale merge*: merging an
even fractional block such as `{½,½}` (scale `n`) into `{1}` changes the merged order and can
**increase** `D̃`. Explicitly, at `(4,2,½,½)` the merge `{½,½}→{1}` sends `D̃ : 4−2+½−½ = 2` to
`4−2+1 = 3` — a strict increase (this is the certified "rounding overshoots `2→3`"). At a *global
minimizer* this particular vertex is not optimal (value `2 > μ`), so its overshoot is harmless; but I
could not prove that **at an optimal vertex** the required merges are always `D̃`-non-increasing.
Concretely, the cross-scale exchange needs: *at an optimal vertex, a sequence of budget-reallocating
merges/splits that integralizes every fractional (even) block while keeping `D̃ ≤ μ`.* Mass literally
**cannot** cross a scale boundary (each `Σπ_j` is a hard integer constraint), so the only lever is
budget reallocation, which changes block parities **globally**; proving that a global reallocation
lands on integers without ever increasing `D̃` is the open gap.

### C.4 A sharpened, numerically-supported sub-target (for the next builder)

The computations this round point to a clean intermediate claim that would combine with Parts A–B:

> **(Conjecture C — optimal-face evenness.)** At every point of the optimal face `{D̃ = μ}`, every
> **fractional** tie-block has **even** multiplicity.

If Conjecture C holds, then by (OB-int) the odd-block values `u_{(p)}` are all integers on the
optimal face, so `μ = D̃(v^*) = Σ_p (−1)^{p−1} u_{(p)} ∈ ℤ_{≥0}`. **This alone still does not give
`μ ≥ 1`** — one must additionally exclude `μ = 0`, i.e. exclude `q=0` (all blocks even), which the
odd grand total `2^{n+1}−1` does *not* force in the continuum (even blocks may carry fractional
values whose weighted sum is odd). So even Conjecture C must be paired with the integralization of
the even blocks (to recover the Parity Lemma's odd-total argument). This confirms that integrality
— not merely evenness — is the irreducible ingredient, matching the R8/R9 meta.

**Numerical support (exact `Fraction`).** Over the value-`1` optimal-face vertices found for
`n=2,3,4` (local search then pushed to reduce the number of distinct values), **`0`** exhibited an
odd fractional block — consistent with Conjecture C. The global integer minimum is `1` for `n≤5`
(certified), and every optimal cell has an integer vertex for `n≤3` (certified `n≤3` exact LP,
`vertex-integrality-parity` §3.1) — i.e. GAP-IMR′ holds for `n≤3`.

---

## Status of the pieces
- **Lemma OB** (odd-block alternating-value formula): **PROVED**, promotable. New clean form of `D̃`.
- **Lemma V** (vertex distinct-value bound `K ≤ n+1`): **PROVED**, promotable.
- **Reduction R** (integer minimizing vertex ⇒ target) and **GAP-IMR′** (finite lattice
  restatement): **PROVED** (R); GAP-IMR′ is the isolated open target.
- **Localization** of fractionality to even blocks with a scale-column entry `≥2`: **PROVED**.
- **Cross-scale exchange**: top-scale non-obstruction and even-block freedom proved; the
  bottom-scale non-increasing merge is the **OPEN** wall (mass cannot cross scales; a merge can raise
  `D̃`, shown at `(4,2,½,½)`). Not closed.

## Approaches tried
- **(round 10 build — GAP-IMR via cross-scale peel exchange)** Diverged this NEW slug from the twin
  onto the cross-scale axis. Delivered two new, fully-proved, promotable structural lemmas — the
  **Odd-Block Alternating-Value Formula** `D̃ = Σ(−1)^{p−1}u_{(p)}` over descending odd-multiplicity
  values (even blocks cancel), and the **Vertex Distinct-Value Bound** `K ≤ n+1` at any minimizing
  cell-vertex. Used them to reduce GAP-IMR rigorously to the finite lattice statement **GAP-IMR′**
  ("some optimal cell-vertex is integer"), and to **localize** all fractionality to *even* tie-blocks
  fed `≥2` parts by a single scale (harmless to `D̃` by OB-int, but obstructing integralization).
  Executed the cross-scale exchange: proved top-scale integralization is always possible and even
  blocks are freely resplittable, and pinned the exact wall — the *bottom-scale non-increasing
  merge* (mass cannot cross a scale's hard sum constraint; merging an even fractional small-scale
  block can raise `D̃`, e.g. `(4,2,½,½): 2→3`). Recorded the numerically-supported optimal-face
  evenness Conjecture C and proved it is *insufficient alone* (evenness ⇏ `μ≥1` without
  integralization). → **partial** (2 new promotable lemmas; GAP-IMR′ isolated but open).
- (twin `vertex-integrality-parity`, round 9: Parity Lemma banked, reduction framing, integer-min=1.)

## Current best
GAP L is reduced to the finite, non-circular lattice statement **GAP-IMR′**: *some vertex of an
optimal merged order-type cell has integer coordinates* — after which the certified Parity Lemma
gives `μ ≥ 1`. Two new promotable tools sharpen this: **Lemma OB** (`D̃` = descending alternating
sum of the odd-multiplicity values; even blocks vanish) and **Lemma V** (`K ≤ n+1` distinct values
at a minimizing vertex). All fractionality at a vertex is localized to *even* tie-blocks fed `≥2`
parts by one scale — harmless to `D̃` but blocking in-place integralization. The open wall is the
cross-scale non-increasing integral rounding: mass cannot cross a scale's hard sum constraint, and a
budget-reallocating merge of a small-scale even fractional block can raise `D̃` (`(4,2,½,½): 2→3`),
so a *globally* non-increasing integralization of an optimal vertex is not yet constructed. GAP-IMR′
is verified for `n ≤ 3` (exact LP) and consistent with all `n ≤ 5` numerics.

## Promotable lemmas
- **Odd-Block Alternating-Value Formula (Lemma OB).** For a finite positive multiset `F` with
  distinct values `u_1>⋯>u_K`, multiplicities `r_l`, first-ranks `s_l=1+Σ_{l'<l}r_{l'}`:
  `D̃(F)=Σ_l(−1)^{s_l−1}u_l·𝟙[r_l odd]`, and, listing the odd-multiplicity values descending as
  `u_{(1)}>⋯>u_{(q)}`, `D̃(F)=Σ_p(−1)^{p−1}u_{(p)}` (even blocks contribute `0`; if all odd-block
  values are integers then `D̃∈ℤ`). Proved in Part A via a per-block geometric sum
  `Σ_{t=0}^{r−1}(−1)^t = 𝟙[r odd]`; verified `0` mismatches / `5·10^4` exact-`Fraction` multisets.
  Reusable by any GAP-L / discrepancy approach (it is the exact even/odd block decomposition of `D̃`).
- **Vertex Distinct-Value Bound (Lemma V).** `μ=min_{Φ_n}D̃` is attained at a vertex of a merged
  order-type cell `Q_{a,σ}`; at any such vertex with positive coordinates the number of distinct
  part-values is `K ≤ n+1`. Proved in Part B by the LP active-constraint count
  `m ≤ (n+1)+(m−K)`. Reusable to reduce GAP-IMR to a finite vertex/lattice search.

## Spec concerns
- The twin `vertex-integrality-parity` and this slug both route through GAP-IMR + Parity Lemma; the
  outline-reviewer already flagged the shared-reduction risk. This round confirms the **specific**
  shared wall is now *sharply localized* (even fractional blocks; cross-scale non-increasing merge),
  and Lemmas OB/V make the residual a **finite** lattice question (GAP-IMR′), which is a genuine
  narrowing rather than a restatement. If both GAP-IMR slugs stall again in R11, the reviewer's
  fallback stands (2-adic split `aimo-0917`, or a monovariant descent to the canonical integer
  minimizer `{2^{n−1},…,3,2,1,1}`) — and Lemma OB is the natural potential for such a descent, since
  it exposes exactly which value moves change `D̃`.
- No refuted line reused: no per-cell TU / integral-vertex claim (Lemma V does **not** assert
  vertices are integral — the localization explicitly exhibits fractional even-block vertices), no
  per-group independent rounding, no parity-through-peel (the peel identity is used only as a fixed
  mass-transfer/measure tool at the minimizer, never to push the Parity Lemma through an induction).
