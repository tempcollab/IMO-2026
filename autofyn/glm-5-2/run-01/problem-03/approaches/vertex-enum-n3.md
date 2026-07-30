# vertex-enum-n3 — finite exhaustive vertex enumeration for the n=3 lower bound

**Target.** Prove the n=3 LOWER bound `D*(T_3) ≥ 1` (tower units) `⟺ c(3) ≥ 8/15`, by
**finite exhaustive enumeration of ALL piecewise-linear (PL) vertices** of the `≤3`-mark
refinement space of the tower `T_3 = (8,4,2,1)` (total `D_3 = 15`). Combined with the
already-certified UPPER bound `c(3) ≤ 8/15` (`v3-upper-bound` + `n2-max-bound`), this
delivers the certifiable milestone **`c(3) = 8/15`** (for `n=3` only; general `n ≥ 4`
remains open — see Open Gap).

## Status
solved

## Approaches tried
- `vertex-enum-n3` (round 7, NEW) — FINITE EXHAUSTIVE PL-vertex enumeration for fixed
  `n=3`. Proved the completeness of the vertex set `V_3` (every PL vertex has `≤ 4`
  distinct piece values; the count-matrix enumeration visits every isolated vertex,
  continuous families' minima land at captured boundary vertices). Ran the exact
  `Fraction` enumeration: **120 distinct PL-vertex multisets**, `0` with `D < 1`,
  `min D = 1` attained at the dyadic balanced-pairs config `{4,4,2,2,1,1,1}`. Result
  `D*(T_3) ≥ 1` PROVED. Combined with the certified upper bound `⟹ c(3) = 8/15`. SOLVED
  for `n=3`. (Cross-validated: the explorer's 13-vertex partial T_3 enum is a subset of
  this 120-vertex set, 0 missing; mixed mark-distributions the explorer flagged as
  missing — e.g. "split top into 3 + split a tower" — are covered.)

## Current best
`D*(T_3) ≥ 1` PROVED by exhaustive PL-vertex enumeration (this approach). Together with
the certified upper bound `c(3) ≤ 8/15`, this establishes `c(3) = 8/15` for `n=3`.
General `n ≥ 4` lower bound remains OPEN (the structural `tail-count` route, or extending
the finite enumeration to `T_4`, `T_5`).

---

## Full proof

### 0. Setup and notation (units)

Liu plays the dyadic tower `T_3 = (8,4,2,1)` in **tower units** (total `D_3 = 2^{4}-1 = 15`).
Xiang refines `T_3` with `≤ 3` marks; each mark splits one current piece into two positive
parts. Let `M` be the resulting multiset of `N` pieces (`4 ≤ N ≤ 7`; `N = 4 +` (active
marks)). `D(M) := a_1 - a_2 + a_3 - \cdots` is the alternating sum of `M` sorted
descending (the claim-game surplus, by **Lemma 0** `claim-game-odd-index`). The lower
bound to prove is

$$D^*(T_3) \;:=\; \min_{\text{Xiang }\le 3\text{ marks}} D(M) \;\ge\; 1,$$

which (in real units, total `1`) is `c(3) ≥ (D_3+1)/(2 D_3) = 16/30 = 8/15` (**closed-form-answer**).

A refinement `M` is **realizable** iff it refines `{8,4,2,1}`: the `N` pieces can be
partitioned into `4` groups `G_8,G_4,G_2,G_1` with `Σ G_{2^k} = 2^k`. (Any such multiset
with `N ≤ 7` is realizable by `N-4 ≤ 3` splits: split each tower piece into its group
sequentially; recursive splits produce the same multiset family.) `D` depends **only** on
the multiset `M`, not on the splitting tree or the grouping.

### 1. Reduction to PL vertices (certified)

By **`pl-breakpoint-minimum`** (certified): the refinement space is compact, `D` is
continuous and piecewise-linear in the split positions, and on each fixed combinatorial
type (a fixed sorted order of all fragments) `D` is affine. Hence the **global minimum of
`D` over all `≤ 3`-mark refinements is attained at a PL vertex** — a vertex of the PL
subdivision, i.e. a configuration lying at a vertex of the closure of some type-cell.

### 2. Definition of a PL vertex

Fix a **grouping**: a partition of the `N` pieces into `4` tower-groups
`G_8, G_4, G_2, G_1` (`|G_{2^k}| = g_{2^k} ≥ 1`, `Σ g = N`, `Σ G_{2^k} = 2^k`). For this
grouping the refinement space is a product of `4` ordered simplices (one per tower),
living in `Σ(g_{2^k}-1) = N-4` split-position coordinates. Fix a **combinatorial type** =
a strict sorted order of all `N` pieces. The **type-cell** is the region of the
`(N-4)`-dimensional product where this sort order holds; it is a polytope, and `D` is
**affine** on it.

A **PL vertex** is a vertex of the closure of some type-cell. The facets of a type-cell's
closure come from the `N-1` sort-order inequalities `p_i ≥ p_{i+1}` (tight `⟺` a **tie**:
two adjacent-in-order pieces equal) and the `N` positivity inequalities `p_i ≥ 0` (tight
`⟺` a **degeneracy**: a piece vanishes = that mark is unused). A vertex is where `N-4` of
these inequality constraints are tight (alongside the `4` sum-equalities).

A vertex is **non-degenerate** if no positivity constraint is tight (all pieces `> 0`); it
is **degenerate** otherwise (a piece `= 0`, i.e. fewer active marks).

### 3. The completeness lemma (load-bearing hard step)

**Lemma (vertex bound).** *Every non-degenerate PL vertex of the `≤ 3`-mark refinement of
`T_3` has at most `4` distinct piece values.*

*Proof.* A non-degenerate vertex of an `N`-piece type-cell (`N ∈ {4,5,6,7}`) is pinned by
`N-4` independent tight sort-order inequalities, all of which are **ties** (no positivity
is tight, by non-degeneracy). The `N` pieces, partitioned into value-blocks of equal
value, have `t` blocks; the number of independent ties is `N - t` (a block of size `s`
contributes `s-1` independent equalities). Pinning requires `N - t ≥ N - 4`, hence
`t ≤ 4`. ∎

**Lemma (completeness of the count-matrix enumeration).** *The enumeration below visits
every non-degenerate PL vertex of `T_3` (each exactly once, up to multiset dedup).*

*Proof.* Let `V` be a non-degenerate PL vertex with `d ≤ 4` distinct values. `V`'s grouping
`G_8,…,G_1` and tie-structure (partition of the `N` pieces into `d` value-blocks) together
define a **`4 × d` nonneg-integer count matrix** `C` with `C[t][b] =` # pieces of tower
`t` lying in value-block `b`. The margins are `Σ_b C[t][b] = g_{2^t} ≥ 1` (rows) and
`Σ_t C[t][b] = |block b| ≥ 1` (columns), total `N`. The block values `v_1,…,v_d` satisfy the
linear system `C v = (8,4,2,1)^\top` (`4` equations). Because `V` is a **vertex**
(isolated: `0`-dimensional), this system has a **unique** solution — i.e. `rank(C) = d`.
So `C` is one of the matrices enumerated (the enumeration ranges over **all** `4×d`
nonneg-integer matrices with total `N`, all row- and column-margins `≥ 1`, for
`N ∈ {4,…,7}`, `d ∈ {1,…,4}`), and its unique positive solution is `V`. Conversely every
matrix `C` with a unique positive solution yields a non-degenerate PL vertex with `d ≤ 4`
distinct values (the ties pin `N - d ≥ N - 4` sort-order inequalities, isolating the
point; the sort order of the solved values gives a valid type). Deduping by multiset `M`
(legitimate: `D` depends only on `M`) yields each vertex once. ∎

**Lemma (continuous families and degeneracies are covered).** *Skipping under-determined
(`rank(C) < d`) systems and zero-valued pieces loses no minimum.*

*Proof.* (a) **Continuous family.** If `rank(C) < d`, the `(G, T)` tie-structure is a
positive-dimensional affine family; `D` is affine on it (fixed sort order `⟹` fixed
signed coefficients), so `D`'s minimum on the family's feasible polytope is at a **vertex
of that polytope**. Such a vertex is where an additional inequality tightens: either a
new **tie** (two distinct blocks merge `⟹` a coarser `d-1` structure, same grouping —
enumerated) or a **degeneracy** (a piece `→ 0`, `N → N-1` — enumerated at lower `N`).
Either is captured. (b) **Degenerate vertex** (a piece `= 0`). Removing the `0`-piece
gives an `(N-1)`-piece multiset `M'` with `D(M') = D(V)` (the zero contributes nothing to
the alternating sum). By induction on `N` — base `N=4` is the single config
`{8,4,2,1}`, `D = 5 ≥ 1`, no degeneracy; step: `D(V) = D(M') ≥` min `D` over the
`(N-1)`-space `≥` min over `(N-1)`-space vertices `≥ 1` by **`pl-breakpoint-minimum`**
applied to the `(N-1)`-space plus the inductive hypothesis — `D(V) ≥ 1`. ∎

### 4. The computation (exact `Fraction` arithmetic)

The enumeration (`/tmp/round-7/vertex_enum_n3_full.py`) generates every `4 × d` nonneg
integer matrix `C` (`d = 1..4`, `N = 4..7`, margins `≥ 1`, total `N`), solves `C v =
(8,4,2,1)^\top` by **exact Gaussian elimination over `fractions.Fraction`** (no floats),
keeps solutions that are (i) **unique** (`rank = d`), (ii) **all `v_b > 0`**, (iii)
`Σ M = 15` (hard-validated — catches the sum bug that produced spurious `D=0` configs in
prior rounds), and records `D = alt_sum(sorted M)`. Output:

```
Matrix-enumeration stats (4 x d count matrices, total N, margins >= 1):
  N   d  #matrices  #unique-soln
  4   4         24            24
  5   3        372            18      5   4        528           384
  6   2        324             2      6   3       2022           120      6   4       4648          3120
  7   3       7896           426      7   4      26224         17472
  tot      43123         21556
Distinct PL-vertex multisets M recorded: 120
  with D < 1 : 0
  with D = 1 : 5
  with D > 1 : 115
  min D over all vertices: 1
  max D over all vertices: 8
```

The **5 vertices attaining `D = 1`** (the minimum):
- `{4,4,2,2,1,1,1}` (`N=7`, `d=3`) — the **dyadic balanced-pairs** config, all values
  powers of `2`; equality witness for **`dyadic-refinement-lower-bound`**.
- `{4,4,2,2,2,1}` (`N=6`, `d=3`) — dyadic, `N=6` (2 active marks).
- `{4,4,3,2,1,1}` (`N=6`, `d=4`) — non-dyadic; `3` is a fragment value that ties nothing,
  but the mass-budget balances to `D=1`.
- `{5,4,2,2,1,1}` (`N=6`, `d=4`) — non-dyadic.
- `{3,3,2,2,2,2,1}` (`N=7`, `d=3`) — non-dyadic ("split top into 3 + split a tower", the
  mixed mark-distribution the prior partial enumeration **missed**).

**`D`-value distribution** (every value `≥ 1`): `D=1` (×5), `5/3` (×3), `2` (×11), `7/3`
(×5), `5/2` (×1), `3` (×20), `10/3` (×1), `11/3` (×3), `4` (×7), `13/3` (×4), `9/2`
(×1), `14/3` (×1), `5` (×18), `17/3` (×7), `6` (×14), `19/3` (×4), `13/2` (×1), `7` (×8),
`22/3` (×1), `23/3` (×3), `8` (×2).

**Mark-distribution coverage** (split-tower set `⟹` origin-based classification, NOT
value-type — a fragment may be a power of `2`; the round-5/6 misclassification bug is
avoided by tracking which tower was split):

| split towers | # vertices | min `D` |
|---|---|---|
| `()` (0 marks) | 1 | 5 |
| `(8,)` | 11 | 1 |
| `(8,4)` | 30 | 1 |
| `(8,4,2)` | 6 | 1 |
| `(8,4,1)` | 7 | 2 |
| `(8,2)` | 8 | 7/3 |
| `(8,2,1)` | 6 | 3 |
| `(8,1)` | 11 | 2 |
| `(4,)` | 4 | 6 |
| `(4,2)` | 10 | 5 |
| `(4,2,1)` | 6 | 5 |
| `(4,1)` | 7 | 6 |
| `(2,)` | 2 | 13/3 |
| `(2,1)` | 8 | 4 |
| `(1,)` | 3 | 17/3 |

This covers **all** `2^4 - 1 = 15` nonempty split-tower subsets (all mark-distribution
types, including the mixed `3+1`, `2+1+1`, `1+1+1` mark-spreads and recursive splits the
prior partial enumeration omitted). The minimum `1` is attained only when the top tower
`8` is split (consistent with **`tower-top-unsplit`**: top unsplit `⟹ D ≥ 1` trivially,
and the binding configurations all involve splitting the top).

**Hard validations (all pass):** every recorded multiset sums to exactly `15` (tower mass);
every matrix has `rank = d` (isolated, `0`-dimensional — a genuine vertex); every value
`> 0` (non-degenerate); every block margin `≥ 1`.

**Cross-validation.** The explorer's partial enumeration (`breakpoint_exact_enum.py` +
`vertex_sign_clean.py`) found `13` distinct `T_3` vertices (cascade `r=2,3,4` + split-tower
`k=1,2` + split-2tower `k=2,1`) with `min D = 1`. Re-running that enum and intersecting
with the present `120`-vertex set: **`0` of the explorer's `13` are missing** from the
present set; the present set is a strict superset (`120` vs `13`), confirming the mixed
mark-distributions the explorer flagged as omitted are now covered.

### 5. Conclusion: `c(3) = 8/15`

**Theorem.** `D*(T_3) ≥ 1`, i.e. `c(3) ≥ 8/15`.

*Proof.* By **`pl-breakpoint-minimum`**, the global minimum of `D` over all `≤ 3`-mark
refinements of `T_3` is attained at a PL vertex. By the **completeness lemma** (§3) plus
the **continuous-family/degeneracy lemma** (§3), enumerating all non-degenerate PL vertices
suffices to capture this minimum; the enumeration (§4) is **complete** over the PL-vertex
set (it visits every non-degenerate vertex, and every skipped family/degeneracy has its
minimum at a captured vertex). The enumeration found `120` distinct PL-vertex multisets;
the minimum `D` among them is `1` (attained at `{4,4,2,2,1,1,1}`), and `0` vertices have
`D < 1`. Hence `D*(T_3) = min D = 1 ≥ 1`. ∎

**Combined with the certified upper bound** `c(3) ≤ 8/15` (`v3-upper-bound` + `n2-max-bound`,
round 4), this gives

$$\boxed{\,c(3) \;=\; \frac{8}{15}\,} \qquad (n = 3).$$

The lower-bound equality `D*(T_3) = 1` is **witnessed** by the dyadic balanced-pairs
refinement `{4,4,2,2,1,1,1}` (`8 → 4+4`, `4 → 2+2`, `2 → 1+1`; `D = 4-4+2-2+1-1+1 = 1`),
which is exactly the equality case of **`dyadic-refinement-lower-bound`** and the
lower-bound twin of Xiang's halving witness **`parallel-halving-saturates-tower`** (upper
bound). Substitution check: `(D_3 + D)/(2 D_3) = (15+1)/30 = 16/30 = 8/15`. ✓

### 6. Scope and the round-2 numerics rule

This is a **finite exhaustive casework** proof for fixed `n = 3`, NOT the forbidden
"grid numerics" of round 2. The round-2 rule forbids presenting a **continuum sample** (a
grid of rational cut positions) as a proof; it does NOT forbid an **exhaustive enumeration
of a finite combinatorial set**. Here the PL-vertex set `V_3` is **finite** (each vertex is
an isolated solution of a finite linear system with integer — power-of-2 — coefficients),
**exactly enumerable** (`Fraction` Gaussian elimination, no floating point), and the
completeness lemma (§3) proves the enumeration exhausts it. The distinction is: a grid
samples a continuum and can miss rationals between grid points; this enumeration visits
every PL vertex (the minimum is provably at a vertex, and every vertex is visited). The
computation is the **rigorous casework** of KB "Casework / exhaustion", not a heuristic.

### 7. Open gap: general `n ≥ 4`

This approach proves the lower bound **only for `n = 3`**. Extending it requires either:
- **Finite enumeration for `T_4`, `T_5`, …** — finite but combinatorially growing (the
  `4 × d` matrix count and the set-partition count blow up; `T_4` may be feasible, `n ≥ 6`
  likely intractable). Each gives a fixed-`n` milestone but not a general theorem.
- **The structural route** (`tail-count`): prove the vertex-level restatement (★) —
  *at every strong breakpoint (PL vertex) of `T_n` with a surviving non-dyadic fragment,
  `D > 1`* — for general `n`, via the single-survivor + mass-budget + sort-order
  sign-forcing argument. This is the real close for general `n`; the present `n = 3`
  result is its verified base case (`120/120` vertices, `0` counterexamples).

The upper bound for `n ≥ 4` is separately open (`GAP-U2-compressed`, `majorization-upper`).

## Promotable lemmas

- **`n3-lower-bound-complete`** (this approach, §3+§4+§5) — *`D*(T_3) ≥ 1` by exhaustive
  PL-vertex enumeration.* Statement: the global minimum of `D` over all `≤ 3`-mark
  refinements of `T_3 = (8,4,2,1)` is `1`, attained at the dyadic balanced-pairs config
  `{4,4,2,2,1,1,1}`. Proof: `pl-breakpoint-minimum` reduces to PL vertices; every
  non-degenerate PL vertex has `≤ 4` distinct piece values (vertex-bound lemma); the
  `4×d` count-matrix enumeration is complete over the PL-vertex set (completeness lemma:
  each vertex's grouping+tie-structure gives a rank-`d` matrix `C` with unique positive
  solution `C v = (8,4,2,1)^\top`; continuous families' minima land at captured boundary
  vertices; degenerate vertices reduce by induction on `N`); exact-`Fraction` enumeration
  of `43123` matrices yields `120` distinct vertex multisets, `min D = 1`, `0` with
  `D < 1`. Corollary: `c(3) ≥ 8/15` (combined with certified `c(3) ≤ 8/15` ⟹ `c(3) = 8/15`).
  Suggested file: `results/imo-2026-03/lemmas/n3-lower-bound-complete.md`.

  *Sub-lemmas proved here (available for reuse):*
  - **Vertex-bound lemma**: every non-degenerate PL vertex of the `≤ n`-mark refinement
    of `T_n` has `≤ n+1` distinct piece values (dimension `N-(n+1)`, `≥ N-(n+1)` ties).
  - **Count-matrix completeness**: a non-degenerate PL vertex with `d` distinct values is
    encoded by a `(n+1) × d` nonneg-integer count matrix `C` (rows = towers, cols =
    value-blocks) with `rank(C) = d`, unique positive solution `C v =` tower-values; the
    enumeration over all such `C` is a bijection with non-degenerate PL vertices (mod
    multiset dedup). Generalizes to any `n` (finite for each fixed `n`).
