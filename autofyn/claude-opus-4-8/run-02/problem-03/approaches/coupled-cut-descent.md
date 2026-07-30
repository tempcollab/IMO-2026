# Approach: coupled-cut-descent (reduce general `b` to the base slice `b=0` by a budget-conserving co-varying monovariant, with a tie-family carve-out)

## Status
partial

The approach's structural machinery (the coupled move, its budget/feasibility bookkeeping, the
exact `ΔM` formula, and the tie handling) is proven rigorously below. **However, the central
mechanism — Step 3, "the specified coupled move is `D̃`-non-increasing" — is REFUTED at `n=5`:**
there are non-tie Case-B configs from which NO move of the specified class (one within-scale
`F'`-merge + free repartition of `π_0`) reaches a config of no-larger `D̃`. The single-cut coupled
descent therefore **cannot** close GAP-P1′-b as designed. This is recorded as a hard negative
result; the gap is left explicit and un-papered.

## Approaches tried
- **(round 12) Coupled-cut descent `b→b−1` (merge one `F'`-cut within a scale + repartition `π_0`
  into `a_0+2` parts, budget `a_0+b` conserved), aiming for a `D̃`-non-increasing monovariant to the
  base slice `b=0`.** Machinery proven; **Step 3 REFUTED at `n=5`** by exact enumeration (explicit
  counterexample below). The move works at `n=3` (0 failures over all `b≥1` configs) and `n=4`
  (the sole failure is a tie, which needs no move), but **fails on genuine non-tie configs at `n≥5`**
  (8 failures over the full `n=5` Case-B family, several with `D̃=3` yet best-reachable `D̃=5`). The
  co-varying single-cut descent is thus **not** a universal monovariant. Dead as specified.
- (prior rounds — inherited context) Pointwise `π_0`-fixed monovariant FALSE (~30%, R11); un-coupled
  `F'`-merge with `π_0` fixed can RAISE `D̃` (`{4,2,½,½}: 2→3`); scalar `b`-cutoff DEAD (ties at
  `b=2,3`); vertex/GAP-IMR route DEAD (R10). None re-seeded here.

## Current best
Rigorous, reusable partial results (all exact-`Fraction` verified):

1. **The coupled move is well-defined, feasibility- and budget-preserving** (Lemma CM below).
2. **Exact effect on `M`** (Lemma ΔM below): a within-scale merge of parts `x≤y` of `F'` plus a split
   of a part `u=u_1+u_2` (`u_1≤u_2`) of `π_0` gives
   `ΔM = 1_{(0,x)} − 1_{[y,x+y)} + 1_{(0,u_1)} − 1_{[u_2,u)}` on `(0,θ)` (0 mismatches / 117 000 checks).
3. **Tie configs need no move** (Lemma TIE below): if `D̃(F)=1` then `I_n=0≤0` already, by the
   certified `(FLOOR)` identity — so ties are *automatically* on the good side of the target and are
   never an obstruction to the *bound* (only to *strict* descent, which the induction does not need).
4. **The decisive negative result** (Prop REFUTE below): the specified single-cut coupled move is
   **not** `D̃`-non-increasing in general; explicit `n=5` non-tie counterexamples exhibited and
   verified exactly. Consequently **`b` is the wrong induction variable for a *local* monovariant**:
   the correct target `F^*` does live in the `(a_0+1, b−1)` slice (verified), but reaching it forces
   a *global* re-choice of `F'` that is equivalent to the slice-minimum comparison `min D̃ over the
   (a_0+1,b−1) slice ≤ D̃(F)`, whose `≥1` half is the theorem itself (circular). This confirms the
   slice-reduction explorer's meta-finding that the `b`-slice framing is a mirage for a local descent.

The open wall GAP-P1′-b is therefore **not** closed by this approach, and (given REFUTE) is unlikely
to be closable by any *single-cut* co-varying descent. The base slice `(★)` (GAP-P1′-a) remains the
sibling routes' responsibility and is untouched here.

## Setup and imported facts (certified)
Dyadic-integer normalization (Structure Lemma). `F = π_0 ⊎ F'`, `θ := 2^{n−1}`; `π_0` a partition of
`2^n` into `a_0+1` parts; `F'` a simultaneous refinement of the sub-ladder `{2^{n−1},…,2,1}`, namely
`F' = ⊎_{j=1}^{n} π_j` with `π_j` a partition of the rung `2^{n−j}` into `a_j+1` parts, all parts
`≤ θ`, `ΣF' = 2^n−1`. Budget `b := Σ_{j≥1} a_j`, feasibility `a_0 + b ≤ n`. `N_P(t)=#{p∈P:p>t}`,
`M(t) := N_{π_0}(t) − N_{F'}(t)` on `(0,θ)`.

- **(FLOOR)** [`lemmas/floor-half-reduction.md`, certified]: `D̃(F) = 1 − 2 I_n`, where
  `I_n := ∫_{(0,θ)} ⌊M/2⌋`. Hence `D̃(F)≥1 ⟺ I_n≤0`, and `D̃(F)=1 ⟺ I_n=0`.
- **(★-id)** [`lemmas/ladder-interleaving-identity.md`, certified, generalized here]: for the
  descending merge of `π_0` (red) and *any* `F'` (blue) with `Σπ_0 − ΣF' = 1`,
  `D̃(π_0⊎F') = 1 + 2(Σ_{blue at odd rank} − Σ_{red at even rank})`. (The certified proof uses only
  `Σred−Σblue = 2^n−(2^n−1) = 1`, which holds for every feasible `F'`, not just `F'=L`.)
- **Case A (`a_0=0`)** and **Invariant I** [`lemmas/peel-difference-bound.md`, certified]:
  `M(0⁺)=(a_0+1)−(n+b)=1−2b·` (with `a_0=n−b` on the extremal budget line) `≤ 1`; Case A closed.
- Upper bound `c(n)=2^n/(2^{n+1}−1)` certified [`lemmas/upper-bound.md`]. If GAP L closes, this is the
  final answer; **verification of the answer is deferred to whichever route closes GAP L** — this
  approach does not close it.

## Lemma CM (the coupled move is feasibility- and budget-preserving)
**Statement.** Fix a feasible Case-B config `F=π_0⊎F'` with `b≥1`. Choose a scale `j≥1` with
`a_j≥1` (so `π_j` has `≥2` parts) and two of its parts `x≤y`; replace them by the single part `x+y`
(a *within-scale merge*). Simultaneously replace `π_0` by any partition `π_0^{new}` of `2^n` into
`a_0+2` parts (*free repartition absorbing the freed cut*). Call the result `F^*`. Then `F^*` is a
feasible Case-B config with budget `b^*=b−1`, `a_0^*=a_0+1`, and `a_0^*+b^* = a_0+b` (budget conserved).

**Proof.** The merged scale `π_j^{new}` is still a partition of the rung `2^{n−j}` (its total is
unchanged), now into `a_j` parts, so `a_j^{new}=a_j−1` and `b^*=b−1`. Every merged part satisfies
`x+y ≤ Σπ_j = 2^{n−j} ≤ 2^{n−1}=θ`, so all `F^*`-parts remain `≤θ`; thus `F'^{*}=⊎π_i^{new}` is still
a valid simultaneous refinement of the sub-ladder. `π_0^{new}` is a partition of `2^n` into `a_0+2`
parts, so `a_0^*=a_0+1`. Budget: `a_0^*+b^* = (a_0+1)+(b−1)=a_0+b ≤ n`, so `F^*` is feasible. Since
`b^*=b−1≥0`, `F^*` is Case B (or the base slice `b=0`). ∎

## Lemma ΔM (exact effect on `M`)
**Statement.** With the notation of Lemma CM, choose the freed cut to split a part `u=u_1+u_2`
(`u_1≤u_2`) of `π_0` (any legal `π_0^{new}` differing from `π_0` by more than one split is handled by
composing single splits; the single-split case is the building block). Then on `(0,θ)`,
```
   M^*(t) − M(t) = 1_{(0,x)}(t) − 1_{[y,x+y)}(t) + 1_{(0,u_1)}(t) − 1_{[u_2,u)}(t).
```
**Proof.** `M = N_{π_0} − N_{F'}`. Merging `x≤y → x+y` in `F'` changes `N_{F'}` by `−1` on `(0,x)`
(two parts `>t` become one), `0` on `[x,y)` (one `>t` before: `y`; one after: `x+y`), and `+1` on
`[y,x+y)` (zero before, one `x+y>t` after); `0` on `[x+y,∞)`. Hence `−ΔN_{F'} = +1_{(0,x)} −
1_{[y,x+y)}`. Splitting `u→u_1,u_2` in `π_0` changes `N_{π_0}` by `+1` on `(0,u_1)`, `0` on
`[u_1,u_2)`, `−1` on `[u_2,u)`, `0` on `[u,∞)`. Hence `ΔN_{π_0} = +1_{(0,u_1)} − 1_{[u_2,u)}`. Adding
`ΔM = ΔN_{π_0} − ΔN_{F'}` gives the claim. ∎
*Verification.* 0 mismatches over 3 000 random merge+split instances × 39 test points (exact
`Fraction`, `/tmp/verify8.py`).

**Consequence (why the sign fight is genuine).** Near `t=0⁺`, `ΔM=+2` (both merge and split add a
part on the small end), which raises `⌊M/2⌋`, tending to *raise* `I_n` (good, the descent wants
`I_n` non-decreasing). But the two `−1` bands `[y,x+y)` and `[u_2,u)` lower `M` there, and where `M`
is even those cost `⌊M/2⌋`. The net sign of `ΔI_n` is a competition with no uniform winner — which
is exactly the phenomenon that Prop REFUTE makes fatal.

## Lemma TIE (ties are automatically on the good side; they are not an obstruction to the bound)
**Statement.** If `D̃(F)=1` then `I_n=0≤0`; the target inequality already holds, with equality.
**Proof.** Immediate from `(FLOOR)`: `D̃(F)=1 ⟹ 1=1−2I_n ⟹ I_n=0`. ∎
**Remark (the tie carve-out is vacuous for the bound).** The induction `P(b): "∀F` budget `b, D̃≥1"`
does not need a *strict* descent; a *non-strict* (`≤`) move suffices, and tie configs already satisfy
`D̃=1≥1` with no move at all. So the `n+1` "L-with-one-bumped-unit" tie family (verified equality by
`(★-id)`: red/blue alternate after the lead red, both sides of `(★)` vanish) is **not** the real
obstruction. The real obstruction is the *non-tie* failure of Step 3 below.

## Prop REFUTE (the specified coupled move is NOT `D̃`-non-increasing — the fatal gap)
**Statement.** There exist feasible non-tie Case-B configs `F` (`D̃(F)>1`, `b≥1`) such that **every**
config `F^*` obtained by one within-scale `F'`-merge plus a free repartition of `π_0` into `a_0+2`
parts has `D̃(F^*) > D̃(F)`. Hence the induction step `D̃(F)≥D̃(F^*)` fails: there is no coupled move
of the specified class that is `D̃`-non-increasing from `F`.

**Explicit witness (`n=5`, exact).**
```
   π_0 = {16, 16}                       (partition of 2^5=32, a_0=1)
   F' :  rung 2^4={16} → {10,4,2},  rung 2^3={8}→{8},
         rung 2^2={4}→{4},  rung 2^1={2}→{2},  rung 2^0={1}→{1}
   budget b = (3−1)+(1−1)+0+0+0 = 2,  a_0+b = 3 ≤ 5   (feasible)
   F = {16,16,10,8,4,4,2,2,1};  descending-alternating sum
     D̃(F) = 16−16+10−8+4−4+2−2+1 = 3   (> 1, a genuine non-tie config).
```
The only within-scale merges available are inside `π_1={10,4,2}` (the other rungs are single parts):
`{14,2}, {12,4}, {10,6}` — each yields `b^*=1`. Exhausting all three merges against all `171`
partitions of `32` into `a_0+2=3` parts (exact `Fraction`, `/tmp/verify6.py`) gives
```
   min over the specified move class  D̃(F^*) = 5   >   3 = D̃(F).
```
So no coupled move of the specified class descends from this `F`. The best move found is
`F'^*=(14,2,8,4,2,1)`, `π_0^{new}=(14,9,9)`, `D̃=5`.

**Scope of the failure.** Full exact enumeration of the entire Case-B family (`/tmp/verify4.py`):
- `n=3`: `0` failures over all `39` configs with `b≥1`.
- `n=4`: `1` failure, and it is a **tie** (`π_0={8,8}`, `F'={5,2,1}∪{4}∪{2}∪{1}`, `D̃=1`), which by
  Lemma TIE needs no move — so the move suffices at `n=4`.
- `n=5`: **8 failures**, of which several are **non-tie** (`D̃=3`, e.g. the witness above and
  `π_0={16,16}` with `π_1∈{ {11,3,2},{9,5,2},{9,4,3} }`). These are the fatal cases: `D̃(F)=3>1` but
  no specified move is non-increasing.
The failing configs share a signature: `π_0` has two (or more) **equal large parts**
(`{16,16}`, `{16,8,8}`) and the top rung `2^{n−1}` is finely cut. A single within-scale merge cannot
repair the discrepancy such a balanced-`π_0` creates against a finely-cut top rung, and `a_0+2` parts
of `π_0` are too few to re-match `F'`. **The refutation is therefore structural, not a boundary
artefact.** ∎

## Why the whole `b`-descent framing is a mirage for a *local* monovariant
For each failing `F` we verified (`/tmp/verify5.py`) that the target slice `(a_0+1,\,b−1)` *does*
contain a config `F^*` with `D̃(F^*)≤D̃(F)` — the descent target exists. But reaching it requires
re-choosing `F'` **globally** (rearranging cuts across scales), which is not a bounded-locality move
derived from `F`. The statement "some `F^*` in the `(a_0+1,b−1)` slice has `D̃(F^*)≤D̃(F)`" is
equivalent to `min_{slice} D̃ ≤ D̃(F)`, and its useful direction `min_{slice} D̃ ≥ 1` **is the theorem
itself**. Combined with the slice-reduction explorer's flat-slice-max fact (`min D̃ = 1` on *every*
slice `b<n`, so zero `b`-slack), this pins the conclusion:

> **The `b`-slice reduction cannot be driven by a single-cut co-varying descent.** `b` is the wrong
> reduction variable; the peel index `n` is the right one. GAP-P1′-b should be folded back into the
> pure `n`-peel / loaded-IH induction (peel §11.5), treating `b=0` only as a self-contained anchor,
> not as a slack-buying reduction target.

This is a firm recommendation for the next round's outliner, backed by the exact `n=5` refutation.

## Open gaps (precisely stated)
- **GAP-P1′-b (unchanged, this route dead):** prove `I_n≤0` for general `b` reduces to `b=0`. The
  single-cut coupled move is **refuted** (Prop REFUTE, `n=5`); no repair by broadening the freed cut
  to `a_0+1`-or-`a_0+2` parts (also fails at `n=5`, `/tmp/verify7.py`, 7 failures). A *multi-cut* or
  *cross-scale* descent might survive but was not found and is not obviously simpler than the theorem.
- **Base slice `(★)` / GAP-P1′-a:** imported, still open, owned by `peel-scale-rank-induction` /
  `ladder-abel-pairing`. Not attacked here.

## Cases covered
Case A (`a_0=0`) — certified closed (imported). Tie configs (`D̃=1`) — closed by Lemma TIE. Base
slice `b=0` — imported. Non-tie `b≥1` — **NOT closed**: Prop REFUTE shows the specified descent fails
at `n≥5`.

## Promotable lemmas
- **Lemma ΔM (exact `M`-effect of a within-scale merge + `π_0`-split):** the identity
  `ΔM = 1_{(0,x)} − 1_{[y,x+y)} + 1_{(0,u_1)} − 1_{[u_2,u)}` on `(0,θ)`. Proven in full above;
  exact-`Fraction` verified (0/117 000). Reusable for any deformation argument on the peel.
- **Lemma TIE:** `D̃(F)=1 ⟹ I_n=0`, so tie configs satisfy `I_n≤0` with equality and need no
  descent. One-line consequence of certified `(FLOOR)`.
- **Prop REFUTE (negative result):** the single-cut co-varying descent (within-scale `F'`-merge +
  free `π_0` repartition into `a_0+2`, or `a_0+1`-or-`a_0+2`, parts) is **not** `D̃`-non-increasing;
  explicit exact `n=5` non-tie counterexamples (`π_0={16,16}`, top rung finely cut, `D̃=3`,
  best-reachable `D̃=5`). This certifies the `b`-slice single-cut descent as a dead framing and
  should retire the co-varying single-cut monovariant family from the population.
