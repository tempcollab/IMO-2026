# Approach: allocation-vertex-corner (non-recursive finite classification of the cut-allocation space)

## Status
partial (round 11 — the core engine `φ(b)` of this route is REFUTED by exact witnesses; the
positive-layer localization survives as a rigorous, verified lemma; base case imported)

## The whole claim this approach proves
GAP L (lower bound), closing the problem: for every simultaneous dyadic refinement
`F = ⊎_{j=0}^n π_j` of `{1,…,2^n}` with cut budget `Σ_j a_j ≤ n`, `D̃(F) ≥ 1`
(equivalently `I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`, `θ=2^{n−1}`, `M=N_{π_0}−N_{F'}`). With the certified
upper bound `lemmas/upper-bound.md` this gives `c(n)=2^n/(2^{n+1}−1)`.

## Approaches tried
- (round 11, this slug) NON-RECURSIVE finite classification of the allocation vector `a=(a_0,…,a_n)`
  via certified Lemma V, with an intended allocation-monotone pruning `φ(b)` to a low-`b` corner.
  **Outcome: the pruning engine (Step 2) is REFUTED.** The premise "the tie `I_n=0` is reached only
  at `b=0`, and `φ(b)<0` for `b≥1`" is FALSE: exact tie configurations exist at `b=2` and `b=3`
  (verified below, exact `Fraction`, `I_n=0` exactly). So the scalar `b` does not separate the tie
  set and cannot prune the allocation space to a finite low-`b` corner. What SURVIVES rigorously:
  (i) the reduction of `sup_positions I_n(a)` to a finite max over Lemma-V cell-vertices, and
  (ii) a fully proven, tight, verified **Positive-Layer Localization Lemma** bounding the positive
  layers of `I_n` by `π_0`'s even-ranked parts alone (`P ≤ Σ_k y_{2k}`), which shows positive
  contributions require `a_0` large — but the matching lower bound on the negative layers `Q`
  (needed for `I_n=P−Q≤0`) again requires `F'`'s recursive cut-tree, the shared wall.
- (prior) new slug seeded round 11; outline approved with CHANGES REQUESTED. See Route below.

## Route (as planned — STRUCTURE distinct from the leader)
Not an induction on `n` and no fixed comparison object: a **non-recursive finite classification of
the discrete allocation vector** `a=(a_0,…,a_n)`, `Σa_j≤n`, via the extremal/vertex principle. It
bounds `I_n` over each allocation cell and was to prune the tie set to a low-dimensional CORNER of
`a`-space (`a_0` large, `b:=Σ_{j≥1}a_j` small). Operates on the ALLOCATION, not a static profile of
the final multiset — so it is NOT the R8-dead measure/merged-order/sequential/genfn family; and
Lemma V bounds a corner, NOT an integer minimizer, so it is NOT the R10-dead GAP-IMR engine.

## What is rigorously established this round

### Step 1 (imported, certified). Reduction and finite-vertex structure.
By the certified FLOOR identity (`lemmas/floor-half-reduction.md`),
`D̃(F) = 1 − 2 I_n`, so GAP L Case B `⟺ I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`, `M=N_{π_0}−N_{F'}`, `θ=2^{n−1}`,
with the tie `D̃=1 ⟺ I_n=0`. For a FIXED allocation `a`, on the cell `P_a` (the coordinates are the
part-lengths of each `π_j`, subject to the hard scale-sums `Σπ_j=2^{n−j}`), `D̃` is piecewise-linear
in the positions, and by certified **Lemma V** (`lemmas/odd-block-vertex.md`) the infimum of `D̃`
over each merged order-type cell is attained at a vertex with `K ≤ n+1` distinct part-values. Hence
`sup_positions I_n(a) = (1 − inf_positions D̃(a))/2` is attained at such a cell-vertex, and
`sup_a I_n` is a finite maximum over the (finitely many) allocation cells' vertices. This part is
sound and imported.

### Step 3 (imported, shared). Base corner `b=0`.
When `b=0`, `F'` is the uncut dyadic ladder `L={2^{n−1},…,2,1}`, and `I_n≤0` becomes the fixed-object
statement `D̃(π_0⊎L) ≥ 1` for every partition `π_0` of `2^n` into `≤ n+1` parts. This is the shared
extremal base case being proven by `peel-scale-rank-induction` this round; **IMPORT it once certified**
(do not re-prove). Reviewer-verified numerically true, tie-attained, `n≤6`.

### NEW rigorous lemma (survives, verified): Positive-Layer Localization.
**Statement.** Let `M = N_{π_0} − N_{F'}` on `(0,θ)`, `θ=2^{n−1}`. Write the layer decomposition of
`I_n` (certified layer form) as `I_n = P − Q` with
```
   P := Σ_{k≥1} λ_{(0,θ)}{M ≥ 2k} = ∫_{(0,θ)} max(⌊M/2⌋, 0),
   Q := Σ_{k≥1} λ_{(0,θ)}{M ≤ −(2k−1)} = ∫_{(0,θ)} max(−⌊M/2⌋, 0).
```
Let `y_1 ≥ y_2 ≥ … ≥ y_{a_0+1}` be the parts of `π_0` in nonincreasing order and set
`K_0 := ⌊(a_0+1)/2⌋`. Then
```
   P ≤ Σ_{k=1}^{K_0} y_{2k}.                                              (POS)
```
In particular, if `a_0 = 0` then `K_0 = 0`, `P = 0` (this re-derives Case A on the positive side);
and every positive layer `k` requires `π_0` to have at least `2k` parts, i.e. requires `a_0` large.

**Proof.** Fix `k ≥ 1`. Since `N_{F'}(t) ≥ 0`, we have
`{t∈(0,θ): M(t) ≥ 2k} ⊆ {t∈(0,θ): N_{π_0}(t) ≥ 2k}`. Now `N_{π_0}(t) = #{parts of π_0 exceeding t}`,
so `N_{π_0}(t) ≥ 2k` holds iff at least `2k` parts of `π_0` exceed `t`, iff the `2k`-th largest part
`y_{2k} > t` (this requires `π_0` to have `≥ 2k` parts; otherwise the set is empty). Two distinct
parts each `≥ y_2` sum to at most `Σπ_0 = 2^n = 2θ`, so `y_2 ≤ θ`, whence `y_{2k} ≤ y_2 ≤ θ` for all
`k ≥ 1`. Therefore `{N_{π_0} ≥ 2k} ∩ (0,θ) = (0, y_{2k})`, a set of measure `y_{2k}`, and
`λ_{(0,θ)}{M ≥ 2k} ≤ y_{2k}`. The `k`-th term is nonzero only when `π_0` has `≥ 2k` parts, i.e.
`2k ≤ a_0+1`, i.e. `k ≤ K_0`. Summing over `k = 1,…,K_0` gives (POS). ∎

**Verification.** Exact `Fraction`, `n=4`, `20000` random feasible refinements across all budget
splits: `0` violations of (POS), and the bound is TIGHT (min slack `Σy_{2k} − P = 0` attained). Code
below (`check_layer.py`). This is the correct rigorous positive-side control for the allocation route;
it coincides in content with the banked round-6 deficit bound `E_A ≤ Σ y_{2j}` but is here derived
cleanly in the FLOOR/layer language and tied directly to `a_0` (a positive layer of index `k` exists
only if `a_0 ≥ 2k−1`). It is NOT a scalar summary of `F'`: it uses only `π_0`'s exact ordered parts.

## Spec concerns (HONEST NEGATIVE — the route's engine is refuted)

The engine of this route (Step 2, the "allocation-monotone bound `φ(b)`, non-increasing in `b`, with
`φ(b) < 0` for `b ≥ 1`, so only `b=0` reaches the tie") is **false**. Verified exactly:

1. **Tie at `b = 2`.** Take `n=4`, `a = (1,2,0,0,0)` (`b = a_1 = 2`, budget `Σa_j = 3 ≤ n`), with
   `π_0 = {8,8}`, `π_1 = {1,2,5}`, `π_2 = {4}`, `π_3 = {2}`, `π_4 = {1}`. Then
   `F = {8,8,5,4,2,2,1,1}`, `ΣF = 31 = 2^{n+1}−1`, descending alternating sum
   `8−8+5−4+2−2+1−1 = 1`, so `D̃(F) = 1` and `I_n = 0` EXACTLY. (Grid-search over positions of this
   allocation returns `max I_n = 0`, code `check_tie.py`.)
2. **Tie at `b = 3`.** `n=4`, `a = (1,2,1,0,0)` (`b = 3`, budget `4 = n`), with `π_0={8,8}`,
   `F'={3,3,2,2,2,2,1}` (`π_1={3,3,2}, π_2={2,2}, π_3={2}, π_4={1}`): `F={8,8,3,3,2,2,2,2,1}`,
   `D̃=1`, `I_n=0` EXACTLY (verified `check_tie.py`).

So the tie set `{I_n = 0}` is reached at `b ∈ {0, 2, 3}`, not concentrated at `b=0`. Consequences:

- The literal Step-2 claim `φ(b) < 0 for b ≥ 1` is refuted (equality at `b=2`).
- Even the weaker "prune to a fixed small finite corner `b ≤ b*`" fails: for `n=4` the tie already
  needs `b` up to `3 = n−1`, so no `b`-cutoff independent of `n` isolates the tie. The scalar `b`
  carries **no separating power** for the tie set.
- This is consistent with, and sharper than, the reviewer's cross-`k` caution: the witness
  `a=(1,2,0,0,0)` is not merely a cross-`k`-cancellation near-miss, it is an EXACT tie, so any
  `φ` that is a function of `b` alone and negative for `b≥1` is impossible.

**Why the route stalls at the same wall.** With (POS) we have `I_n = P − Q ≤ Σ_{k=1}^{K_0} y_{2k} − Q`.
Closing `I_n ≤ 0` therefore needs a matching LOWER bound `Q ≥ Σ_{k=1}^{K_0} y_{2k}` (or a joint bound
`Q ≥ P`). But `Q = Σ_k λ{M ≤ −(2k−1)}` is governed by `N_{F'}`, i.e. by `F'`'s recursive dyadic
cut-tree — exactly the quantity the whole run has been unable to lower-bound by any allocation-scalar
(refuted: scalar/aggregate-of-`Z` R3–R4, top-down reserve R7, bottom-up reserve R9). The allocation
classification does not escape this: the finite Lemma-V corner it reduces to is not carved out by `b`
(refuted above), and any correct carving must read `F'`'s cut-tree shape, which returns to the leader's
loaded-IH wall. So this route, as planned around a `b`-monotone `φ`, cannot close GAP L; it is a
genuine negative on the "prune by `b`" mechanism.

## Current best
Rigorously this round: (i) the finite-vertex reduction `sup_a I_n = max over Lemma-V cell-vertices`
(imported, certified); (ii) the fully-proven, tight, verified **Positive-Layer Localization Lemma**
`P ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}` — the positive layers of `I_n` are controlled by `π_0`'s
even-ranked parts, so positive contribution requires large `a_0` (re-proves Case A on the positive
side); (iii) base corner `b=0` imported from the leader. The route's intended pruning engine `φ(b)`
is REFUTED (exact ties at `b=2,3`), so the open gap is unchanged from the field's shared wall: a
lower bound `Q ≥ P` on the negative layers requires `F'`'s recursive cut-tree, not any `b`-scalar.

## Full proof
*(Not present — Status is `partial`; GAP L is not closed by this route.)*

## Promotable lemmas
- **Positive-Layer Localization Lemma.** With `M=N_{π_0}−N_{F'}` on `(0,θ)`, `θ=2^{n−1}`, and
  `y_1≥…≥y_{a_0+1}` the ordered parts of `π_0`:
  `Σ_{k≥1} λ_{(0,θ)}{M ≥ 2k} ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}`.
  Proved in full above (`{M≥2k}⊆{N_{π_0}≥2k}=(0,y_{2k})`, `y_{2k}≤y_2≤θ`); verified exact
  `Fraction` `0/20000`, tight. Reusable: it bounds the positive `⌊M/2⌋` layers of `I_n` purely by
  `π_0`'s even-ranked parts, localizing all positive contribution to `a_0 ≥ 2k−1`. (This is the
  clean FLOOR-language form of the banked round-6 deficit bound `E_A ≤ Σ y_{2j}`.)

## Appendix: code (exact `Fraction`, reproducible)
```
# check_tie.py — exact ties at b=2 and b=3 (I_n=0), and grid max over a=(1,2,0,0,0)=0
# check_layer.py — P <= sum y_{2k}: 0/20000 violations, tight (min slack 0)
# check_phi.py / check_b1.py — sup I_n per allocation: b=0 -> 0, b=1 -> slightly negative,
#   b=2 (a=(1,2,0,0,0)) reaches 0.  (all in /tmp of this session)
```
