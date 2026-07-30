## Status
partial

## Approach: parity-measure-potential (framing B — global integral/parity identity)

Target (the whole claim): **c(n) = 2^n/(2^{n+1} − 1)**, both bounds, via the measure identity
`D = measure{ t : N(t) odd }` (`N(t) = #{pieces > t}`) and the parity-toggle calculus of
Xiang's cuts. Throughout `u := u_n = 1/(2^{n+1}−1)`, so `c(n) = (1+u)/2 = 2^n/(2^{n+1}−1)`.

**Imported (certified in `lemmas/`, NOT re-proved here):**
- **Lemma R** (`reduction-odd-rank`): the claiming game gives Liu the odd-rank sum; with total
  1, Liu = (1+D)/2, `D = Σ_i(−1)^{i+1} b_i ≥ 0` on the descending sort. The whole problem is
  the scalar minimax of D (Liu ≤ n cuts to maximise, Xiang ≤ n cuts to minimise). So it
  suffices to prove **minimax D = u**.
- **Lemma I/M** (`measure-identity`): `D = measure{t : N(t) odd}`, `N(t) = #{pieces > t}`.
  Corollary: even multiplicity of every value ⇒ N(t) even ∀t ⇒ D = 0.
- **Lemma T** (toggle calculus): a cut of `s` into `s₁ ≥ s₂` toggles the parity of N on
  `E = [0,s₂) ∪ [s₁,s)` (measure `2s₂`); after cuts with toggle-sets `E₁,…,E_r` the final
  odd-set is `O₀ △ ⨁_i E_i`, so `D_final = μ(O₀ △ ⨁_i E_i)` and `|ΔD| ≤ 2s₂` per cut.
- **Lemma P** (`cancelling-pair`): `D(S ∪ {v,v}) = D(S)`. One cut of a piece `P ≥ Q` into
  `(P−Q, Q)` creates a copy of an existing/other value `Q`; the pair `{Q,Q}` may be deleted
  from the multiset without changing D (piece count −1, total −2Q).
- **Lemma SPLIT** (`split-cross-term`): `D(X ⊔ Y) = D(X) + D(Y) − 2·μ(O_X ∩ O_Y)`, where
  `O_Z = {t : N_Z(t) odd}`. Carries the disjoint-union cross term exactly.
- **Lemma U0** (`even-multiplicity-corrector`, CERTIFIED THIS ROUND as `lemmas/even-multiplicity-
  corrector.md`): (a) even multiplicity of every value ⇒ `D = 0`; (b) budget `≥ m` ⇒ Xiang bisects
  all `m` pieces to force `D = 0`; (c) upper bound `UB(n)` is nontrivial only for `m = n+1`.
- **Lemma ONE** (`top-scale-dichotomy`): in any refinement of `C_n`, at most one final piece
  exceeds `2^{n−1}`.

We must prove **min over Xiang D = u** as a two-sided bound:
- **Upper bound:** for *every* Liu multiset `A` (≤ n+1 pieces, sum 1), Xiang has ≤ n cuts with
  final `D ≤ u`.
- **Lower bound:** for the dyadic Liu multiset, *every* ≤ n Xiang cuts leave `D ≥ u`.

This round I recast both bounds inside a single clean induction and closed several new
sub-cases; the two residual gaps are stated precisely and are known (numerically) to be tight.

---

## UPPER BOUND — inductive framework (bisect / match), two branches fully proved

**Claim UB(k).** For every multiset `A` with ≤ k+1 pieces and total `L`, Xiang using ≤ k cuts
can force `D(final) ≤ u_k · L`, where `u_k = 1/(2^{k+1}−1)`.

Taking `k = n`, `L = 1` gives the upper bound. We argue by strong induction on `k`.

**Base `k = 0`.** `A` has ≤ 1 piece, so `A = {L}` (or empty). No cuts. `D = L = u_0 L`
(`u_0 = 1/(2−1) = 1`). ✔

**Inductive step (`k ≥ 1`).** Sort `a₁ ≥ a₂ ≥ … ≥ a_m`, `m ≤ k+1`, `Σ = L`. Two identities we
will use repeatedly (both from Lemma P): after one cut we may pass to a *smaller instance*
with one fewer piece, one fewer cut, and known D.

Record the arithmetic once. For a "peel of `j` cancelling pairs of total matched mass `Σ_T`"
we will reduce to an instance of budget `k−j` and mass `L − 2Σ_T`, and the induction closes iff
`u_{k−j}(L − 2Σ_T) ≤ u_k L`, i.e.
```
        2 Σ_T  ≥  L (1 − u_k/u_{k−j}).                                     (UB-thr)
```
Using `u_i = 1/(2^{i+1}−1)`:
`1 − u_k/u_{k−j} = 1 − (2^{k−j+1}−1)/(2^{k+1}−1) = (2^{k+1} − 2^{k−j+1})/(2^{k+1}−1)
 = 2^{k−j+1}(2^j − 1)/(2^{k+1}−1) = 2^{k−j+1}(2^j−1)·u_k.`
So (UB-thr) reads `Σ_T ≥ L·u_k·2^{k−j}(2^j − 1) =: L·θ_j`. For `j = 1` this is
`Σ_T ≥ L u_k 2^{k−1}`, and `1 − u_k/u_{k−1} = 2^k u_k = c(k)`; the single-pair threshold
`2Σ_T ≥ c(k)L` will be used below.

**Branch (0) — BISECT `a₁` (closes when `a₁ ≥ c(k) L`).**
Cut `a₁ → a₁/2, a₁/2`. These are two equal values; by Lemma P,
`D({a₁/2,a₁/2} ∪ rest) = D(rest)` where `rest = {a₂,…,a_m}` (≤ k pieces, total `L−a₁`). Xiang
now plays the UB(k−1) strategy on `rest` with his remaining `k−1` cuts; the two halves survive
untouched and, by Lemma P applied to the *final* multiset, contribute nothing to D. Hence
`D(final) = D(final on rest) ≤ u_{k−1}(L − a₁)`. This is `≤ u_k L` iff `a₁ ≥ L(1−u_k/u_{k−1})
= c(k) L`. ✔ (This is (UB-thr) with `j = 1, Σ_T = a₁/2`: bisection matches a virtual pair of
value `a₁/2`.)

**Branch (1) — MATCH `a₂` (closes when `a₂ ≥ c(k) L / 2`).**
Since `a₂ ≤ a₁`, cut `a₁ → a₂, (a₁−a₂)`. Now two pieces equal `a₂`; by Lemma P delete the pair,
leaving `rest = {a₁−a₂, a₃,…,a_m}` (≤ k pieces, total `L − 2a₂`), budget `k−1`. Apply UB(k−1):
`D(final) ≤ u_{k−1}(L − 2a₂) ≤ u_k L` iff `2a₂ ≥ c(k)L`, i.e. `a₂ ≥ c(k)L/2`. ✔

**These two branches already prove UB(1) completely** (hence `c(1) = 2/3`, `n=1`).
For `k = 1`: `m ≤ 2`. If `a₁ ≥ c(1)L = 2L/3`, Branch (0) gives `D ≤ u_0(L−a₁) = L−a₁ ≤ L/3 =
u_1 L`. If `a₁ < 2L/3`, then with `m ≤ 2`, `D = a₁ − a₂ = 2a₁ − L < L/3 = u_1 L` with **no
cut**. ✔ Both cases meet `u_1 L`. (Verified: the extremal Liu input is `a₁=2/3, a₂=1/3`,
where bisecting `a₁` gives `{1/3,1/3,1/3}`, `D = 1/3 = u_1`.)

**General multi-pair reduction (the route for `k ≥ 2`).**
For any subset `T ⊆ {a₂,…,a_m}` with `Σ_T ≤ a₁`, cut `a₁` into the `|T|` values of `T` plus a
leftover `a₁ − Σ_T` (this is `|T|` cuts; if the leftover is `0` it is `|T|−1` cuts). Each value
of `T` is now duplicated; delete the `|T|` cancelling pairs by Lemma P. The residual is
`{a₁−Σ_T} ∪ ({a₂,…,a_m}∖T)`, with `m − |T| ≤ (k−|T|)+1` pieces, total `L − 2Σ_T`, budget
`k − |T|`. By UB(k−|T|) and (UB-thr),
`D(final) ≤ u_{k−|T|}(L − 2Σ_T) ≤ u_k L` **provided** `Σ_T ≥ L·θ_{|T|}` with
`θ_j = u_k 2^{k−j}(2^j−1) = u_k(2^k − 2^{k−j})` and `Σ_T ≤ a₁`.

**Branch (2) — WHOLE-TAIL PEEL (NEW; closes the whole range `L/2 ≤ a₁ ≤ c(k)L`).**
Take `T = {a₂,…,a_m}`, the *entire* tail, so `Σ_T = L − a₁` and `j = |T| = m−1 ≤ k`. Feasibility
`Σ_T ≤ a₁` is exactly `L − a₁ ≤ a₁`, i.e. **`a₁ ≥ L/2`**. Cut `a₁` into the `m−1` tail values
plus leftover `a₁ − Σ_T = 2a₁ − L ≥ 0` (that is `m−1 ≤ k` cuts), and delete all `m−1` cancelling
pairs by Lemma P. The residual is the **single piece** `{2a₁ − L}` (budget `k − (m−1) ≥ 0`, no
further cuts needed), so **exactly**
```
        D(final) = D({2a₁ − L}) = 2a₁ − L.
```
This is `≤ u_k L` iff `a₁ ≤ (1+u_k)L/2 = c(k)L`, using the identity `c(k) = (1+u_k)/2`
(indeed `(1+u_k)/2 = (1 + 1/(2^{k+1}−1))/2 = 2^k/(2^{k+1}−1) = c(k)`). Hence **for every profile
with `L/2 ≤ a₁ ≤ c(k)L`, Branch (2) forces `D ≤ u_k L` exactly.** ✔

**Consequence — the range `a₁ ≥ L/2` is now FULLY CLOSED** (profile-independently), for every
`k ≥ 1`:
- `a₁ ≥ c(k)L`: Branch (0) (bisect `a₁`) gives `D ≤ u_{k−1}(L−a₁) ≤ u_k L`.
- `L/2 ≤ a₁ ≤ c(k)L`: Branch (2) (whole-tail peel) gives `D = 2a₁ − L ≤ u_k L`.
(At `a₁ = c(k)L` both give exactly `u_k L`; at `a₁ = L/2` Branch (2) gives `D = 0`.) Note
`c(k) = 2^k/(2^{k+1}−1) > 1/2`, so the intermediate range `[L/2, c(k)L]` is genuinely nonempty
and Branch (2) is what fills it. This upgrades the previously-proven region (which was only
`a₁ ≥ c(k)L` plus the `a₂ ≥ c(k)L/2` single-match strip).

**GAP U (the crux) — the mass-threshold disjunction is NON-EXHAUSTIVE for `a₁ < L/2`; the lever
is REFUTED.** The remaining regime is `a₁ < L/2` at full budget. Here neither Branch (0/1/2) nor
*any* multi-pair peel `(j,T)` can be forced to meet its mass threshold, and — decisively — this
is **not** a bookkeeping gap but a genuine failure of the mass-based reduction framing itself.

*Rigorous counterexample to the disjunction (k = 2, `L = 1`).* Take
`A = (0.44,\; 0.281,\; 0.279)` (sorted, sum 1, `m = 3 = k+1`, full budget). Here
`c(2) = 4/7 ≈ 0.5714`, `θ_1 = 2/7 ≈ 0.28571`, `θ_2 = 3/7 ≈ 0.42857`. Check every mass-threshold
move:
- Branch (0): needs `a₁ ≥ c(2)L`; `0.44 < 0.5714`. **Fails.**
- Branch (2)/whole-tail: needs `a₁ ≥ L/2`; `0.44 < 0.5`. **Fails.**
- `j = 1` peel: the only `Σ_T ≤ a₁` size-1 sets are `{0.281}` or `{0.279}`, sums `< 0.28571 = θ_1 L`.
  **Fails.**
- `j = 2` peel: the only size-2 set is `{0.281,0.279}`, sum `0.560 > 0.44 = a₁`, violating the
  cap `Σ_T ≤ a₁`. **Fails.**
So **no move in the disjunction is available.** Yet the true minimax is `D ≤ u_2 = 1/7`: Xiang
simply **bisects** `a₁ = 0.44 → 0.22, 0.22`, giving `{0.281, 0.279, 0.22, 0.22}` with
`D = 0.281 − 0.279 + 0.22 − 0.22 = 0.002 ≤ 1/7` (verified by direct minimax computation:
`min_{≤2 cuts} D(A) = 0.002`). The point is that Branch (0)'s residual is the *tail*
`{0.281,0.279}`, whose true `D = 0.002` is far below the worst-case bound
`u_{k−1}(L−a₁) = u_1·0.56 ≈ 0.187` used in the threshold. The tail *near-cancels*, so the
mass bound is grossly loose.

*Why this kills the mass-threshold framing (not just this example).* Any reduction of the form
"make `j` cuts, land on a residual of total mass `L − 2Σ_T`, bound its `D` by
`u_{k−j}(L − 2Σ_T)`" is a function of *residual mass alone*. But `D` of the residual depends on
its **internal structure**, not its mass: the family `A_ε = (c(2)L − ε,\; (1−a₁)/2+δ,\;
(1−a₁)/2−δ)` with `0 < a₁ < L/2` and `δ → 0` has residual tail mass bounded away from `0` while
its `D → 0`. A whole band of such profiles (numerically, `a₁ ∈ [0.43, 0.5)` for `k=2` with
near-equal tail — 18 of 40 sampled values fail the disjunction) defeats *every* mass threshold
while being trivially won by bisection. Hence **the subset-cover feasibility disjunction cannot
be made exhaustive** — the lever proposed for GAP U is provably dead. The all-equal profile is
still easy (`D = 0` by even multiplicity / one bisection), but the near-balanced *unequal* tail
is the true obstruction, and it is invisible to any mass-only argument.

*What the fix must be (hand-off to the outliner — RETHINK GAP U).* A correct upper bound in the
regime `a₁ < L/2` must **track `D` of the residual**, not its mass. Two concrete routes, both
already live in the field:
1. **Import the induction-peel exact dominant-cut identity** `D_new = D_C − 2μ(E_R ∩ [0,p₂))`
   (its `p₂ → a₁/2` bisection case): this computes the residual's `D` *exactly* after the top
   cut, replacing the loose `u_{k−1}(L−a₁)` bound by the true value, which is what makes the
   near-cancelling tail visible.
2. **Smoothing/majorization** (the `V` is maximized at the dyadic profile framing): a
   structure-tracking argument that never passes through residual mass.
The `a₁ ≥ L/2` region (above) is genuinely, profile-independently closed and stands regardless;
only `a₁ < L/2` needs the D-tracking replacement.

---

## LOWER BOUND — Liu's dyadic construction; new dichotomy and the a=1 identity

**Construction.** Liu plays `a_k = 2^k u` (`k=0,…,n`), total `u(2^{n+1}−1) = 1`. By scaling it
suffices to prove, in **units of `u`** (pieces `1,2,4,…,2^n`, total `M = 2^{n+1}−1`):

> **(LB)** every refinement of `{2^0,…,2^n}` by ≤ n cuts has `D ≥ 1`.

We prove (LB) by strong induction on `n`, using the measure identity throughout. The
*superincreasing* fact `2^n > 2^n − 1 = 2^0+…+2^{n−1}` is used repeatedly.

**Base `n=0`:** single piece `1`, no cuts, `D = 1`. ✔ **`n=1`:** pieces `{1,2}`, ≤1 cut. No
cut: `D = 2−1 = 1`. Cut the `2` into `s₁ ≥ s₂` (sum 2, so `s₁∈[1,2]`, `s₂ = 2−s₁ ≤ 1`): sorted
`{s₁,1,s₂}`, `D = s₁ − 1 + s₂ = 1`. Cut the `1` into `x, 1−x`: sorted `{2, max, min}`,
`D = 2 − |2x−1| ≥ 1`. So `D ≥ 1`. ✔

**Inductive step (`n ≥ 2`), assuming (LB) for `n−1`.** Let `S` be the final multiset (a
refinement of `{1,…,2^n}` by ≤ n cuts). Sort the *original* pieces; only `2^n` exceeds
`2^{n−1}`, and every other original is ≤ `2^{n−1}`, so every fragment of a non-top piece is
≤ `2^{n−1}`, and a fragment of `2^n` may or may not exceed `2^{n−1}`.

**Key dichotomy (at most one final piece exceeds `2^{n−1}`).** Fragments of `2^n` sum to `2^n`,
so at most one of them can exceed `2^{n−1}` (two would sum to > `2^n`). Every non-top fragment
is ≤ `2^{n−1}`. Hence the number `a` of final pieces `> 2^{n−1}` is `a ∈ {0,1}`.

**Case A (`2^n` uncut).** Then `2^n ∈ S` and it is the unique piece `> 2^{n−1}` (indeed the
unique piece `≥ 2^n − 1`, since all other pieces are fragments of `{1,…,2^{n−1}}`, total
`2^n − 1`, so each is `< 2^n − 1` for `n ≥ 2`). Thus `N(t) = 1` (odd) on `[2^n−1, 2^n)`,
length `1`. By Lemma I, `D ≥ 1`. ✔ (This is the previously-proven case.)

**Case a = 1 (`2^n` is cut, but one fragment `f₁ > 2^{n−1}` survives).**
Let `f₁` be that unique piece `> 2^{n−1}` and `S_L := S ∖ {f₁}` (all pieces `≤ 2^{n−1} < f₁`,
so `O_{S_L} ⊆ [0, 2^{n−1}) ⊆ [0, f₁)`). For every `t`, `N_S(t) = 1[f₁ > t] + N_{S_L}(t)`, so
`g_S(t) := N_S(t) mod 2 = 1[t<f₁] ⊕ g_{S_L}(t)`. Integrate (Lemma I):
- for `t ≥ f₁`: `N_{S_L}(t)=0`, `g_S=0`;
- for `t < f₁`: `g_S = 1 − g_{S_L}`, so `∫_0^{f₁} g_S = f₁ − ∫_0^{f₁} g_{S_L} = f₁ − D(S_L)`
  (the last equality because `O_{S_L} ⊆ [0,f₁)`).

Hence the **exact identity**
```
        D(S) = f₁ − D(S_L)                    (a = 1).                     (LB-id)
```
(Verified numerically: e.g. `n=3`, cut `8→f₁,(8−f₁)`, `D(S) = f₁ − D(S_L)` exactly.) So
(LB) in this case is **equivalent to `D(S_L) ≤ f₁ − 1`.** `S_L` is a refinement of
`({fragments of 2^n other than f₁, total 2^n − f₁}) ∪ {refinement of C_{n−1}}`, all pieces
`≤ 2^{n−1}`. Numerically this inequality holds and is *tight* (margin `→ 0` as
`f₁ → 2^{n−1}⁺`, exactly when the two large fragments of `2^n` nearly cancel). **GAP L1:** prove
`D(S_L) ≤ f₁ − 1`. Note this is an *upper-bound-flavoured* inequality on `S_L` (bounding an
alternating sum from above), dual to the global upper bound; it is not implied by trivial
`D(S_L) ≤ max piece ≤ 2^{n−1}` (that only gives `≤ 2^{n−1}`, short of `f₁−1` when `f₁` is near
`2^{n−1}`). Closing it needs the cancellation between `f₁`'s sibling fragment `2^n − f₁` and
the tail — the same "cutting a scale costs that scale" mechanism, made quantitative.

**Case a = 0 (`2^n` is cut into fragments all `≤ 2^{n−1}`).**
*Fully closed subcase — equal bisection of the top.* If `2^n` is cut by a **single** cut with
both fragments `≤ 2^{n−1}`, then (sum `2^n`) both equal `2^{n−1}`: the cut is `2^n → 2^{n−1},
2^{n−1}`. These two equal pieces form a cancelling pair; by Lemma P,
`D(S) = D(S ∖ {2^{n−1}, 2^{n−1}})`, and `S ∖ {2^{n−1},2^{n−1}}` is a refinement of `C_{n−1} =
{1,…,2^{n−1}}` by the remaining `≤ n−1` cuts. By the induction hypothesis (LB for `n−1`),
`D ≥ 1`. ✔

*Remaining subcase — `2^n` shredded into ≥ 3 fragments all `≤ 2^{n−1}` (an unequal pair is
impossible: a single cut with both fragments `≤ 2^{n−1}` and sum `2^n` forces both `= 2^{n−1}`).*
**GAP L2.** This is treated DIRECTLY by the measure/SPLIT calculus in the dedicated section
**"GAP L2 via direct measure calculus"** below (this round's deliverable 2). There we (i) prove the
rigorous **master inequality** `D(S) ≥ |D(F) − D(B)|` (SPLIT + trivial intersection cap), (ii)
input `D(B) ≥ 1` from the induction hypothesis LB(`n−1`), (iii) thereby close the ENTIRE subregime
`|D(F) − D(B)| ≥ 1` — in particular every even-multiplicity fragmentation `D(F) = 0` (subsuming
equal-bisection and the whole doubling family), (iv) compute the extremal value exactly via the
measure identity (target `= 1`, attained), and (v) isolate the residual open content to a single
scalar cross-term inequality **GAP L2-exch** `μ(O_F ∩ O_B) ≤ (D(F)+D(B)−1)/2` — a *second,
measure-based derivation* of the interleaving-extremality fact that induction-peel attacks by
rearrangement (diversity insurance, per the outliner). The residual balanced-overlap step remains
open.

**Extremal value (tightness of the answer).** The dyadic "doubling response"
`2^k → 2^{k−1}, 2^{k−1}` applied top-down (`n` cuts: `2^n→2^{n−1},2^{n−1}`, then
`2^{n−1}→2^{n−2},2^{n−2}`, …) yields the multiset with values `2^{n−1},…,1` each appearing
twice except a single leftover `1`; all pairs cancel (Lemma P) and `N(t)=1` on a length-1
interval, so `D = 1` exactly. Thus the bound `D ≥ 1` is attained and Liu cannot force more.
Combined with UB this pins minimax `D = u`, so by Lemma R `c(n) = (1+u)/2 = 2^n/(2^{n+1}−1)`.

---

## Lemma U0 — the even-multiplicity corrector (deliverable 1; FULL, ready to certify)

This is a clean, self-contained shared lemma object (the "bisect-all" corrector). It has two
parts: a pure measure fact (a) and its strategic consequence (b). It is imported by
`smoothing-majorization` (regime i base) and `breakpoint-vertex` (§4B), and it reduces the upper
bound UB(n) to the single full-budget case `m = n+1`. It uses only certified Lemmas M and P.

**Lemma U0(a) [even-multiplicity ⇒ D = 0].** Let `S` be any finite multiset of positive reals in
which every distinct value has even multiplicity. Then `D(S) = 0`.

*Proof.* Write the distinct values of `S` as `v_1 > v_2 > … > v_r`, with multiplicities
`m_1,…,m_r` all even. For `t > 0`, `N_S(t) = #{pieces > t} = Σ_{j : v_j > t} m_j`. As `t`
decreases from `+∞`, `N_S(t)` starts at `0` (for `t ≥ v_1`) and increases by `m_j` (even) each
time `t` crosses a value `v_j`. A sum of even integers is even, so `N_S(t)` is even for every `t`
that is not one of the finitely many values `v_j` (a measure-zero set). Hence
`{t : N_S(t) odd}` has measure `0`, and by the certified measure identity (Lemma M,
`D = μ{t : N_S(t) odd}`), `D(S) = 0`. ∎

(This is exactly the certified Corollary of Lemma M, restated as a standalone named lemma so the
strategy consequence (b) can cite it directly.)

**Lemma U0(b) [bisect-all: `m ≤ n` ⇒ Xiang forces D = 0].** Let `A = {a_1,…,a_m}` be any Liu
profile of `m` pieces with total `L`, and suppose Xiang's cut budget is `≥ m` (in the master
problem this is `m ≤ n`). Then Xiang, using **exactly `m`** cuts, can force `D(final) = 0`; in
particular `D(final) = 0 ≤ u_n L`.

*Proof.* Xiang bisects every piece: for each `i = 1,…,m` he applies the single cut
`a_i → (a_i/2, a_i/2)`. This is `m` cuts, and `m ≤ n` is within budget. The final multiset is
```
        F = { a_i/2 (with multiplicity 2) : i = 1,…,m } .
```
Every distinct value `w` occurring in `F` is of the form `a_i/2`; its multiplicity in `F` equals
`2·#{i : a_i/2 = w}`, which is even. By Lemma U0(a), `D(F) = 0`. Since `u_n L ≥ 0`, the bound
`D ≤ u_n L` holds. ∎

**Corollary U0(c) [reduction of the upper bound to full budget].** In the upper-bound game Liu
presents `m ≤ n+1` pieces and Xiang has `≤ n` cuts. By U0(b), every profile with `m ≤ n` pieces
is disposed of with `D = 0 ≤ u_n L`. Hence the upper bound `UB(n)` is nontrivial **only** for
profiles with exactly `m = n+1` pieces (full budget). ∎

*Remark (why this is the right corrector, not sequential bisection).* U0(b) bisects **all `m`
pieces simultaneously**; it does not peel one piece at a time. Sequential/cascading single-piece
bisection is a *refuted* rule (it violates the target by `4.7×` on the near-uniform `n=5` profile
`(0.2024,0.1965,0.1820,0.1789,0.1651,0.0750)`, per explorer-upper). U0(b) is immune to that
failure precisely because it is a one-shot simultaneous even-pairing, and it only claims `D=0`
when the budget `n ≥ m` actually suffices to double every piece.

---

## GAP L2 via direct measure/toggle calculus (deliverable 2; PARTIAL — new subcases closed,
## residual exchange step made explicit)

We attack GAP L2 by the **global measure identity `D = μ{t : N_S(t) odd}` used directly**, a
mechanism deliberately *distinct* from induction-peel's cancelling-pair exchange argument (per the
outliner's diversity-insurance mandate: two far-apart derivations of the same interleaving fact,
guarding against the single-gap trap). Work in units of `u` throughout: Liu plays
`C_n = {2^0, 2^1, …, 2^n}`, total `M = 2^{n+1} − 1`, and `t_i := 2^{n−i}` (`i = 1,…,n`) are the
tail values, so `C_{n−1} = {t_1,…,t_n} = {2^{n−1}, …, 2, 1}`, `Σ_i t_i = 2^n − 1`.

**Setup of L2.** `S` is a refinement of `C_n` by `≤ n` cuts with **every final piece `≤ 2^{n−1}`**
(the `a = 0` regime). By certified Lemma ONE (top-scale dichotomy) the top `2^n` must be cut into
`≥ 2` fragments (each `≤ 2^{n−1}`, sum `2^n`). Decompose `S = F ⊔ B`, where `F` = the fragments of
`2^n` (all `≤ 2^{n−1}`, `Σ F = 2^n`, `|F| ≥ 2`) and `B` = the refinement of the tail `C_{n−1}`.

**Restatement (measure form).** L2 asserts
```
        D(S) = μ{ t > 0 : N_S(t) odd } ≥ 1        for every such S.       (L2-meas)
```

### (i) The master inequality (NEW this round, fully rigorous): `D(S) ≥ |D(F) − D(B)|`.
Apply certified **Lemma SPLIT** to the partition `S = F ⊔ B`:
```
        D(S) = D(F) + D(B) − 2·μ(O_F ∩ O_B),                                 (L2-split)
```
where `O_F = {t : N_F(t) odd}`, `O_B = {t : N_B(t) odd}`. By Lemma M, `μ(O_F) = D(F)` and
`μ(O_B) = D(B)`. Since an intersection has measure at most that of either set,
```
        μ(O_F ∩ O_B) ≤ min(μ(O_F), μ(O_B)) = min(D(F), D(B)).                (L2-cap)
```
Substituting (L2-cap) into (L2-split) and using `x + y − 2min(x,y) = |x − y|`:
```
        D(S) ≥ D(F) + D(B) − 2·min(D(F), D(B)) = |D(F) − D(B)|.              (L2-master)
```
Both steps are exact identities/inequalities from certified lemmas; (L2-master) holds for **every**
admissible `S`. (Verified round 6: `3·10^5` random `a=0` refinements at `n=3`, no violation of
either (L2-master) or `D(S) ≥ 1`.)

### (ii) The IH input: `D(B) ≥ 1`.
`B` is the sub-multiset of `S` consisting of the fragments of the tail pieces `{t_1,…,t_n} =
C_{n−1}`; hence `B` is a refinement of `C_{n−1}` using `c_B` cuts. The top used `|F|−1` cuts, so
`c_B ≤ n − (|F|−1) ≤ n − 1` (as `|F| ≥ 2` by Lemma ONE / the a=0 hypothesis). By the strong
induction hypothesis **LB(`n−1`)** — *every* refinement of `C_{n−1}` by `≤ n−1` cuts has `D ≥ 1` —
we get `D(B) ≥ 1`. (LB(`n−1`) is the full lower bound at `n−1`, already reduced to its own
Cases A / a=1 / a=0; the induction is well-founded, base `n=1` proved above.)

### (iii) Fully closed subregime: `D(F) = 0` (⊇ equal-bisection AND the whole doubling family).
If `D(F) = 0`, then by (L2-master) and (ii), `D(S) ≥ |0 − D(B)| = D(B) ≥ 1`. ✔ This subregime is
large and closed **without any exchange argument**:
- **Equal-bisection (`|F| = 2`).** Both fragments sum to `2^n` and are `≤ 2^{n−1}`, forcing
  `F = {2^{n−1}, 2^{n−1}}`; even multiplicity gives `D(F) = 0` by Lemma U0(a). Closed.
- **Doubling / even-multiplicity fragmentations.** Whenever every value occurring among the
  fragments `F` has even multiplicity (e.g. the top-down doubling response
  `2^n → 2^{n−1},2^{n−1}`, or any `F` that is a union of equal pairs), Lemma U0(a) gives
  `D(F) = 0`, hence `D(S) ≥ D(B) ≥ 1`. Closed.

More generally (still fully rigorous), (L2-master)+(ii) close **every** configuration with
`|D(F) − D(B)| ≥ 1` — in particular `D(F) ≤ D(B) − 1` (`D(F)` small relative to `D(B)`) or
`D(F) ≥ D(B) + 1`.

### (iv) The extremal value, computed exactly by the measure identity (target `= 1`, attained).
That `1` is the correct floor is confirmed by an exact computation, not a sample check.

*Attaining `D = 1`.* The doubling response `2^n → 2^{n−1}, 2^{n−1}` (tail uncut) gives
`F = {2^{n−1},2^{n−1}}`, `D(F) = 0`, and `B = C_{n−1}`. By Lemma P (delete the pair),
`D(S) = D(C_{n−1})`. But `C_{n−1}` uncut is a refinement of itself by `0` cuts, so — descending
`2^{n−1} > … > 1`, an alternating sum `D(C_{n−1}) = Σ_{k=0}^{n−1}(−1)^{n−1−k}2^k = (2^n−(−1)^n)/3`
— this is `> 1` for `n ≥ 2`; the response that actually attains `1` is the *full* top-down
doubling cascade `2^k → 2^{k−1},2^{k−1}` (all `n` cuts), which by `n` applications of Lemma P
collapses to a single length-`1` interval of odd `N`, giving `D = 1` exactly (this is the tightness
construction already recorded in the LOWER BOUND section). So the infimum of `D` over the a=0
regime is `1` and is attained.

*The canonical interleaving value (exact merged formula).* Split the top into `n` distinct
fragments `g_1 > g_2 > … > g_n` (`n−1` cuts, tail uncut) with each `g_k` **just above** `t_k`, i.e.
`g_k > t_k > g_{k+1}` and `Σ_k g_k = 2^n`. Then the descending sort of `S = {g_1,…,g_n} ⊔
{t_1,…,t_n}` is the alternating list `g_1 > t_1 > g_2 > t_2 > … > g_n > t_n`, so odd ranks carry
the `g_k` and even ranks the `t_k`, and by Lemma M
```
        D(S) = Σ_{k=1}^{n} g_k − Σ_{k=1}^{n} t_k = 2^n − (2^n − 1) = 1.       (L2-telescope)
```
This is an **exact** identity from the measure identity applied to the merged sequence (verified
round 6: `n=4`, `D = 1.000000`). It is the exact mirror of the L1 identity
`D = Σ(t_k − g_k) = (2^n−1) − w = f₁ − 1` (below-gap insertion): the SAME interleaving object,
evaluated by the SAME measure identity, with fragments above vs. below each `t_k`. (The strict
requirement `g_1 > t_1 = 2^{n−1}` conflicts with the L2 ceiling `g_1 ≤ 2^{n−1}`, so this exact
interleaving is the *infimum* limit `g_k → t_k^+`; it certifies the floor is exactly `1`, matched
by the attained cascade above.) Confirms: the L2 target is exactly `1`, and it is a floor, not
merely a sample value.

### (v) The residual open step — GAP L2-exch (stated precisely; measure form).
(L2-master) is *lossy exactly when* `D(F) ≈ D(B)`: then `μ(O_F ∩ O_B)` is close to its maximum
`min(D(F),D(B))` and the trivial cap (L2-cap) gives only `D(S) ≥ 0`. (E.g. round-6 sampling found
admissible `S` with `D(F) = D(B) = 1`, where (L2-master) gives `0` but the *true* value is
`D(S) = 2` because the cross term `μ(O_F ∩ O_B) = 0`.) Equivalently, closing L2 in full is exactly:

> **GAP L2-exch (measure form).** For every admissible a=0 refinement `S = F ⊔ B`,
> ```
>         μ(O_F ∩ O_B) ≤ ( D(F) + D(B) − 1 ) / 2 .                            (L2-cross)
> ```
> By (L2-split) this is *equivalent* to `D(S) ≥ 1`. It says the two odd-sets `O_F, O_B ⊆
> [0, 2^{n−1})` cannot overlap more than the stated budget — the interleaving-extremality fact:
> the canonical "one fragment per open gap `(t_{k+1},t_k)`, just above `t_k`" layout minimises the
> overlap, with equality `μ(O_F ∩ O_B) = (D(F)+D(B)−1)/2` there.

*What is proved vs. open.* **Proved in full this round (measure route):** the master inequality
(L2-master), the IH reduction `D(B) ≥ 1`, and hence the ENTIRE subregime `|D(F) − D(B)| ≥ 1` —
in particular every even-multiplicity fragmentation `D(F) = 0` (which subsumes the equal-bisection
subcase and the whole doubling-response family). **Proved exactly:** the extremal value `1` (both
attained by the cascade and computed by (L2-telescope)), so `1` is the correct floor. **Open:** the
cross-term bound (L2-cross) in the *balanced* subregime `|D(F) − D(B)| < 1` with `D(F) > 0` — the
genuine interleaving-extremality crux. The naive per-cut toggle bound `|ΔD| ≤ 2s_2` (Lemma T) is
too loose (it does not certify a floor), exactly as flagged. A bespoke **adjacent-atom exchange** —
sliding a single fragment across one tail atom `t_k` and tracking `μ(O_F ∩ O_B)` monotonically
toward the canonical layout — is required, and remains the same combinatorial content that
induction-peel attacks by rearrangement; here it is isolated to the single clean scalar inequality
(L2-cross) via the measure/SPLIT calculus, a **second, independent derivation route** (diversity
insurance). It is **not** closed this round.

*Honest status of L2.* The master inequality, the IH input, the full `|D(F)−D(B)| ≥ 1` regime
(incl. all even-multiplicity fragmentations), and the exact extremal value are **proved**. The
balanced-overlap inequality (L2-cross) — equivalently `D(S) ≥ 1` when `|D(F)−D(B)| < 1` and
`D(F) > 0` — is the sole residual and rests on the unproved **GAP L2-exch**. **L2 remains PARTIAL.**

---

## STRUCTURAL-IH REVISION (round 7): mass-difference reduction of L2-exch

**Assigned task (round 7).** Close L2-exch by putting the fix *upstream*: strengthen the IH from
the scalar `D(B) ≥ 1` to a structural per-gap occupancy invariant on `O_B` so that
`μ(O_F ∩ O_B) ≤ (D(F)+D(B)−1)/2` becomes provable profile-independently.

### 0. Spec concern — the outliner's specific invariant is FALSE.

The outliner's step 3 proposed the invariant: *"`O_B` meets each dyadic gap `(2^{n−2−i},
2^{n−1−i})` of `C_{n−1}` in a single interval."* This is **numerically false**, hence cannot be
the load-bearing invariant. **Explicit witness** (`n = 4`, `C_{n−1} = {1,2,4,8}`, budget
`c_B = 2 ≤ n−1`): cut `8 → 5.085 + 2.915` and `4 → 2.135 + 1.865`, leaving the multiset
`B = {1, 1.865, 2, 2.135, 2.915, 5.085}`. Its descending sort is
`5.085 > 2.915 > 2.135 > 2 > 1.865 > 1`, so on the gap `(2, 4)`:
- `t ∈ (2.915, 4)`: pieces `> t` are `{5.085}`, `N_B = 1` **odd**;
- `t ∈ (2.135, 2.915)`: pieces `> t` are `{5.085, 2.915}`, `N_B = 2` even;
- `t ∈ (2, 2.135)`: pieces `> t` are `{5.085, 2.915, 2.135}`, `N_B = 3` **odd**.

So `O_B ∩ (2,4) = (2, 2.135) ∪ (2.915, 4)` — **two** disjoint intervals, not one. (Verified by
exhaustive search: over budget-respecting refinements of `{1,2,4,8}`, `O_B` meets a dyadic gap in
up to `2` intervals; the count grows with `c_B`.) **The literal "single-interval-per-gap"
invariant is refuted; the gap-by-gap-with-one-interval accounting in the outliner's step 4 has no
foundation.** The reason: each *cut* landing a fragment inside a gap can add a parity toggle, so
the number of `O_B`-intervals inside a gap is budget-dependent, not bounded by `1`.

*Consequence for the route.* A per-gap occupancy invariant that is inductively preserved and
recovers the exact `−1/2` deficit does not exist in the form specified. Rather than force a false
invariant, this round I re-derive the *upstream* object correctly: I collapse the entire
cross-term `μ(O_F ∩ O_B)` into a single **mass identity**, which is the honest content the
"structural IH" was groping toward — and which is *profile-independent and fully proved*.

### 1. Lemma MID (mass-difference reduction) — NEW, FULLY PROVED.

Work in units of `u`; `S = F ⊔ B` is any admissible `a = 0` refinement: `F` = fragments of the top
`2^n` (each `≤ 2^{n−1}`, `Σ F = 2^n`, `|F| ≥ 2` by Lemma ONE), `B` = a `≤ (n−1)`-cut refinement of
the tail ladder `C_{n−1} = {2^0,…,2^{n−1}}` (each piece `≤ 2^{n−1}`, `Σ B = 2^n − 1`). Define the
**mass-difference count**
```
        g(t) := N_F(t) − N_B(t),        t ∈ (0, 2^{n−1}),        N_X(t) = #{pieces of X > t}.
```

> **Lemma MID.**
> (a) [parity identity] For `t ≥ 2^{n−1}`, `N_S(t) = 0`; and for `t ∈ (0, 2^{n−1})`,
>     `N_S(t)` is odd `⟺ g(t)` is odd. Hence by Lemma M,
>     `D(S) = μ{ t ∈ (0, 2^{n−1}) : g(t) odd }`.
> (b) [mass identity] `∫_0^{2^{n−1}} g(t) dt = 1` — **for every** admissible `a = 0` refinement.
>
> Consequently, **L2 (`D(S) ≥ 1`) is exactly equivalent to**
> ```
>         μ{ t ∈ (0, 2^{n−1}) : g(t) odd }  ≥  ∫_0^{2^{n−1}} g(t) dt   (= 1).        (MID-core)
> ```

*Proof.* **(a)** Every piece of `S` is `≤ 2^{n−1}` (each `f ∈ F` by the `a = 0` hypothesis, each
`b ∈ B` since fragments of `C_{n−1}` are `≤ 2^{n−1}`). Thus for `t ≥ 2^{n−1}` no piece strictly
exceeds `t`, so `N_S(t) = 0` (even). For `t ∈ (0, 2^{n−1})`, the disjoint-multiset-union
`S = F ⊔ B` gives `N_S(t) = N_F(t) + N_B(t)`; and `N_F + N_B ≡ N_F − N_B = g (mod 2)`, so
`N_S(t)` is odd iff `g(t)` is odd. Applying the certified **measure identity** (Lemma M,
`D = μ{t : N_S(t) odd}`) and that the odd-set lies in `(0, 2^{n−1})` by the first sentence,
`D(S) = μ{t ∈ (0,2^{n−1}) : g(t) odd}`.

**(b)** By the layer-cake (Fubini) identity `∫_0^∞ 1[x > t]\, dt = x` for `x > 0`, and since
`N_F(t) = 0` for `t ≥ 2^{n−1}`,
```
        ∫_0^{2^{n−1}} N_F(t)\,dt = ∫_0^∞ N_F(t)\,dt = Σ_{f∈F} ∫_0^∞ 1[f>t]\,dt = Σ_{f∈F} f = Σ F = 2^n.
```
Identically `∫_0^{2^{n−1}} N_B(t)\,dt = Σ B = 2^n − 1`. Subtracting,
`∫_0^{2^{n−1}} g = 2^n − (2^n − 1) = 1`. The equivalence in the box is then immediate from (a) and
(b). ∎

*(Verified round 7: over `3·10^4` budget-respecting `a=0` refinements at `n=4`, `∫g = 1` to
machine precision in every case, `μ{g odd} = D(S)` in every case, and `D(S) ≥ 1` throughout;
minimum observed `D(S) ≈ 1.006`.)*

**Why this is genuine progress (and the correct "upstream" object).** Lemma MID *eliminates the
cross term entirely*: it replaces the whole SPLIT decomposition `D(S) = D(F)+D(B)−2μ(O_F∩O_B)` and
the refuted min-cap by a single scalar constraint `∫ g = 1`. There is no `D(F)`, no `D(B)`, no
`μ(O_F ∩ O_B)`: the balanced/unbalanced dichotomy dissolves. The `−1` on the right of (L2-cross) is
no longer an unexplained deficit to be "distributed across gaps"; it is exactly the mass identity
`Σ F − Σ B = 2^n − (2^n−1) = 1` — the superincreasing signature of the ladder, made a hard
arithmetic fact. This is the honest realisation of "the fix is upstream."

### 2. What MID-core needs — and why the pure integral bound is insufficient (structure required).

`g` is integer-valued and equals a difference of two **non-increasing** integer step functions
`N_F, N_B` (each `0` at `t = 2^{n−1}`, rising as `t ↓ 0` to `|F|`, `|B|` respectively).

**(P1) The `0 ≤ g ≤ 1` case is closed exactly.** If `g(t) ∈ {0,1}` for a.e. `t` (i.e.
`N_B ≤ N_F ≤ N_B + 1` a.e.), then `{g odd} = {g = 1}` and `μ{g = 1} = ∫ g = 1` (since `g` takes
only values `0,1`), so **`D(S) = 1` exactly**. This is the exact-floor regime and matches the
canonical interleaving layout (one fragment per gap, `N_F` exceeds `N_B` by exactly one on a total
length `1`). It reproduces, with no cross-term, the previously computed extremal value `1`.

**(P2) The `|F| = 2` case is closed** (consistency check with the certified sub-case). `|F| = 2`
with `Σ F = 2^n`, each `≤ 2^{n−1}` forces `F = {2^{n−1}, 2^{n−1}}`, so `N_F(t) = 2` for
`t < 2^{n−1}` and `0` above: `N_F` is *even* everywhere. Hence `g ≡ −N_B (mod 2)`, i.e.
`{g odd} = {N_B odd} = O_B`, and `μ{g odd} = D(B) ≥ 1` by the IH `LB(n−1)` (`B` is a `≤(n−1)`-cut
refinement of `C_{n−1}`). ✔ (Equivalently: the pair `{2^{n−1},2^{n−1}}` cancels by Lemma P and
`D(S) = D(B) ≥ 1`.) So the residual content of MID-core is strictly `|F| ≥ 3`, consistent with the
explorer's note.

**(P3) The pure-integral statement is FALSE — structure of `B` is essential.** The bare claim
"`g` integer-valued, `∫ g = 1` ⇒ `μ{g odd} ≥ 1`" is false: take `g ≡ 2` on a set of measure
`1/2` and `g ≡ 0` elsewhere, then `∫ g = 1` but `μ{g odd} = 0`. Such a `g` **cannot** arise from
an admissible `(F, B)`: it would require `N_F − N_B = 2` on a measure-`1/2` band with `N_F − N_B`
never `1` at its endpoints, which contradicts the monotone step structure combined with the ladder
constraint on `B`. So closing MID-core genuinely requires the ladder (superincreasing) structure of
`B`, exactly as the explorer flagged — **but now the requirement is isolated to a single clean
inequality with no cross-term bookkeeping.** The relevant structural fact that survives (unlike the
refuted single-interval invariant) is **Lemma ONE recursed**: *at each dyadic scale `2^j`, at most
one piece of `B` exceeds `2^j`* — equivalently, on the top gap `[2^{n−2}, 2^{n−1})`, `N_B ∈ {0,1}`
and is non-increasing (a single interval **there**, at the top scale only). The failure of the
outliner's invariant is precisely that this "single excursion" property holds at the *top* of each
sub-ladder but does **not** propagate to a per-dyadic-gap statement once lower cuts intervene.

### 3. Residual — GAP MID-core (honest gap; the sole remaining content of L2).

> **GAP MID-core.** Let `g = N_F − N_B` as above (`F, B` an admissible `a = 0` refinement,
> `|F| ≥ 3`). Prove `μ{t : g(t) odd} ≥ 1`.

By Lemma MID this is *equivalent* to L2 (`D(S) ≥ 1`) and is the whole residual of the lower bound
(both `|F| = 2` and `0 ≤ g ≤ 1` disposed of above). What is now needed is a monotone/exchange
argument that uses the ladder structure of `B` at every scale (Lemma ONE recursed) to show the
integer step function `g` cannot hide its unit of positive mass inside even values on a set of
measure `> ∫ g`. This is the same combinatorial content as induction-peel's exchange step and
merge-interleave's reachable-word minimisation, now re-expressed *without any cross-term* as the
single scalar-constrained parity-measure inequality (MID-core). **It is not closed this round.**

*Status of the round-7 revision.* The assigned "structural-IH" route as literally specified rests
on a **false invariant** (§0, refuted with an explicit witness). In its place I proved the correct
upstream object — **Lemma MID**, a cross-term-free reduction of the entire lower-bound residual to
the single inequality MID-core — closed the `|F| = 2` and `0 ≤ g ≤ 1` sub-cases within it, and
pinned the residual to one clean profile-independent claim. **L2 remains PARTIAL**, but the target
is now sharper (no cross-term, no min-cap, no balanced/unbalanced split) than the previous
`μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2` formulation.

---

## ROUND 8 — GAP MID-core as a signed order-statistic inequality (PARTIAL; new sub-case closed)

This round targets **GAP MID-core** (the whole residual of the lower bound): for every admissible
`a=0` refinement `S = F ⊔ B` with `|F| ≥ 3`, prove `D(S) ≥ 1`. I (i) give a clean, fully rigorous
reformulation of `D(S) ≥ 1` as a single **signed order-statistic inequality** that needs only the
certified Lemma R and the mass identity `ΣF − ΣB = 1` (it does **not** even need Lemma MID(a)), (ii)
prove a new closed sub-case strictly generalizing the previously-closed `0 ≤ g ≤ 1` regime, and
(iii) isolate the exact residual scalar inequality and record two verified structural facts that
constrain any proof of it. The full aggregate-compensation inequality is **not** closed.

### R8.1 The order-statistic reformulation (FULLY RIGOROUS).

Let `S = F ⊔ B` be admissible `a=0` (`ΣF = 2^n`, each `f∈F` `≤ 2^{n−1}`, `|F| ≥ 3`; `B` a
`≤(n−1)`-cut refinement of `C_{n−1}`, `ΣB = 2^n − 1`). Merge `S` in **strictly-descending value
order** `v_1 > v_2 > ⋯ > v_m` (`m = |F|+|B|`; ties are split arbitrarily — the sums below are
independent of the tie-order since equal values carry equal weight). Attach the sign
`e_i = +1` if `v_i ∈ F`, `e_i = −1` if `v_i ∈ B`, and define the partial sums (the *walk*)
`S_k = Σ_{i≤k} e_i`, `S_0 = 0`.

**Two exact identities.**
- **(R8.1a) `D(S) = Σ_{i=1}^m (−1)^{i+1} v_i`.** This is precisely certified **Lemma R**
  (`D = Σ_i(−1)^{i+1}b_i` on the descending sort) applied to the full multiset `S`. No new content;
  just the definition of `D` as the alternating sum of the order statistics of `S`.
- **(R8.1b) `Σ_{i=1}^m e_i v_i = ΣF − ΣB = 2^n − (2^n − 1) = 1`.** Immediate: `Σ_i e_i v_i` collects
  `+f` for each `f∈F` and `−b` for each `b∈B`. The value `1` is the **superincreasing signature**
  of the ladder, identical to Lemma MID(b) but derived here without integration.

Subtracting (R8.1b) from (R8.1a):
```
        D(S) − 1 = Σ_{i=1}^m d_i v_i,        d_i := (−1)^{i+1} − e_i ∈ {−2, 0, +2}.      (R8-core)
```
The coefficient `d_i` is: `+2` exactly when `i` is **odd and `e_i = −1`** ("a `B`-piece sits at an
odd rank"); `−2` exactly when `i` is **even and `e_i = +1`** ("an `F`-piece sits at an even rank");
`0` otherwise. Hence

> **(R8-goal)** `D(S) ≥ 1` **is exactly equivalent to** `Σ_{B at odd rank} v_i ≥ Σ_{F at even rank} v_i`.

This is the same object as the walk inequality `Σ c_i w_i ≥ 0` (Abel summation of (R8-core) with
`w_i = v_i − v_{i+1}` and partial sums `Σ_{i≤k} d_i = 1[k\ odd] − S_k = c_k` recovers it exactly),
but stated as a bare comparison of two order-statistic sums, which is the cleanest handle.
*(Verified: over 20000 admissible refinements at `n=2..6`, `D(S) = Σ(−1)^{i+1}v_i` exactly,
`Σe_iv_i = 1` exactly, and `D(S)−1 = Σ d_i v_i` exactly; `min D(S) = 1.0001 > 1`.)*

### R8.2 NEW closed sub-case: **the walk never leads by two** (`S_k ≤ 1 ∀k`, i.e. `g ≤ 1`).

**Claim.** If `S_k ≤ 1` for every `k = 1,…,m` — equivalently (since `g(t) = S_i` on the `i`-th gap
and `S_k ≡ k (mod 2)`) `g(t) ≤ 1` for all `t`, i.e. `N_F(t) ≤ N_B(t) + 1` pointwise — then
`D(S) ≥ 1`.

**Proof.** Let `P_k := Σ_{i≤k} d_i = 1[k\ odd] − S_k` be the partial sums of the coefficients in
(R8-core). For `k` odd, `S_k` is odd and `S_k ≤ 1` gives `S_k ≤ 1`, so `P_k = 1 − S_k ≥ 0`. For `k`
even, `S_k` is even and `S_k ≤ 1` forces `S_k ≤ 0`, so `P_k = −S_k ≥ 0`. Thus `P_k ≥ 0` for all `k`.
Now apply **Abel summation** to (R8-core), using `v_{m+1} := 0` and `w_k := v_k − v_{k+1} ≥ 0`
(descending order):
```
        Σ_{i=1}^m d_i v_i = Σ_{k=1}^m P_k (v_k − v_{k+1}) = Σ_{k=1}^m P_k w_k ≥ 0,
```
since every `P_k ≥ 0` and every `w_k ≥ 0`. By (R8-core), `D(S) = 1 + Σ_i d_i v_i ≥ 1`. ∎

**Why this is genuinely new.** The previously-closed sub-case (P1 in the round-7 section) was
`0 ≤ g ≤ 1`. The present sub-case drops the lower bound entirely: it closes **every** refinement in
which `F` never gets two ranks ahead of `B` (the walk may dip arbitrarily far below `0`; only the
one-sided cap `S_k ≤ 1` is used). This strictly contains `0 ≤ g ≤ 1` and also the `|F| = 2` case
(there `N_F ≤ 2` and `N_F` even, but more directly `g` never exceeds... in fact `|F|=2` is already
closed by P2). *(Verified: over all sampled refinements with `max_k S_k ≤ 1`, `D(S) ≥ 1` with no
exception.)* The complementary, genuinely hard regime is precisely **`S_k = 2` somewhere** — `F`
leads `B` by two among the top ranks, an *overshoot* that must be repaid lower down.

### R8.3 The residual (honest GAP) and two verified structural facts.

> **GAP MID-core (order-statistic form).** For every admissible `a=0` refinement with `|F| ≥ 3` and
> `max_k S_k ≥ 2`, prove `Σ_{B at odd rank} v_i ≥ Σ_{F at even rank} v_i` (equivalently
> `Σ_k P_k w_k ≥ 0` with `P_k = 1[k\ odd] − S_k` not all `≥ 0`). **Not closed this round.**

Two facts pin down the shape of any valid argument (both verified numerically this round, 30000
admissible refinements at `n = 2..6`):

- **(F1) The aggregate inequality is TRUE but NOT prefix-monotone.** The global comparison
  `Σ_{B\ odd} v_i ≥ Σ_{F\ even} v_i` held in **all** 30000 cases (`0` violations). But its prefix
  version — `Σ_{i≤k, F\ even} v_i ≤ Σ_{i≤k, B\ odd} v_i` for all `k` — **failed in ≈ 27%** of cases
  (8043/30000). Consequently **no prefix/running-deficit monovariant on the merged order can prove
  it**: the compensation is irreducibly aggregate (an early `F`-even debit at a large value is paid
  by *several later* `B`-odd credits at smaller values whose sum, but not any prefix, dominates).
  This rigorously rules out the naive `P_k ≥ 0` route outside the R8.2 sub-case and confirms the
  outliner's "aggregate compensation, never termwise" mandate.
- **(F2) A count-level compensation always holds (necessary, not sufficient).** The total coefficient
  sum is `Σ_i d_i = P_m = 1[m\ odd] − S_m` with `S_m = |F| − |B|`. Because `B` refines `C_{n−1}`
  (`n` original pieces `1,…,2^{n−1}`) we have `|B| = n + c_B` and `|F| = 1 + c_F` with
  `c_F + c_B ≤ n`, whence `|F| − |B| = 1 − n + (c_F − c_B) ≤ 1 − n + (n − 1) = 0`, i.e. **`S_m ≤ 0`**.
  Thus `#{B at odd rank} − #{F at even rank} = P_m/2 ≥ 0`: there are at least as many credit ranks as
  debit ranks. This is the "terminal descent" the outliner cited (`S_m = |F| − |B| < 0`); it gives
  the *count* inequality for free but **not** the *value-weighted* one — the ladder must additionally
  prevent the debit value from concentrating at the top, which is the unclosed content.

**What a proof still needs.** A value-weighted transport (or a strong induction that abstracts the
ladder) routing each `F`-even debit `v_i` to strictly-smaller-or-equal `B`-odd credits summing to at
least `v_i`, feasible because of the ladder's superincreasing mass distribution in `B` (Lemma ONE
recursed at every dyadic scale caps how far the walk can run ahead before a forced `B`-crossing).
This is the same aggregate inequality the outline-reviewer's step 4 flagged; the reformulation
(R8-goal) and the sub-case R8.2 are new, but the aggregate overshoot-repayment inequality
**remains open**.

---

## ROUND 9 — strengthened-IH scale reserve: recursion lemma PROVED, naive reserve REFUTED (PARTIAL)

This round I execute the outliner's assigned route (strengthened-IH scale potential `Φ_k` with a
cross-scale reserve `ρ_k`, peeling the top dyadic gap via "Lemma ONE recursed"), honouring the three
reviewer constraints. The net result is a **rigorous proof of the recursion lemma the whole route
depends on** (reviewer concern #1) and a **rigorous refutation of the specific reserve mechanism the
outliner proposed** (reviewer concern #2): a *nonnegative cumulative-surplus reserve does not exist,
in either direction*. GAP MID-core therefore remains open, but the field now knows precisely which
reserve shapes are dead and why. All numeric statements below are checks; every proof stands alone.

### R9.0 Restatement of the residual and the exact target integrand.

By certified Lemmas R, M, MID, OSR, OSR-cap the lower bound is reduced to **GAP MID-core**: for an
admissible `a=0` refinement `S = F ⊔ B` (`F` = fragments of the top `2^n`, each `≤ 2^{n-1}`,
`ΣF = 2^n`, `|F| ≥ 3`; `B` = a `≤(n−1)`-cut refinement of `C_{n−1} = {1,…,2^{n−1}}`, `ΣB = 2^n−1`),
with `g(t) := N_F(t) − N_B(t)` on `(0, 2^{n−1})`,
```
        μ{ t : g(t) odd } ≥ 1 = ∫_0^{2^{n−1}} g .                                   (MID-core)
```
Since `g` is an integer step function and `∫ 1[g odd] = μ{g odd}`, subtract the two integrals:
```
        μ{g odd} − 1 = ∫_0^{2^{n−1}} φ(g(t)) dt,      φ(c) := 1[c odd] − c   (c ∈ ℤ).   (R9-phi)
```
The pointwise sign of the integrand is exact:
```
        φ(c) ≥ 0  ⟺  c ≤ 1 ,        φ(c) < 0  ⟺  c ≥ 2 .                             (R9-sign)
```
(Check: `φ(1)=0`, `φ(0)=0`, `φ(−1)=2`, `φ(−2)=2`, `φ(2)=−2`, `φ(3)=−2`; for `c ≤ 0`,
`φ(c) = 1[c odd] − c ≥ −c ≥ 0`; for `c ≥ 2`, `φ(c) = 1[c odd] − c ≤ 1 − 2 = −1 < 0`.) So
**(MID-core) is exactly `∫φ(g) ≥ 0`: the negative mass produced where the walk leads by two or more
(`g ≥ 2`) must be outweighed by the positive mass produced where `B` leads (`g ≤ 0`).** The mean of
`g` is `1/2^{n−1}` (tiny), so `g` is `≤ 0` on most of the domain; the difficulty is entirely that
the `{g ≥ 2}` region can sit at *even* values (contributing `0` to `μ{g odd}` but a large deficit to
`∫φ`), and must be paid off elsewhere. This is the "aggregate, non-local" compensation.

### R9.1 Lemma ONE-REC (recursed dyadic dichotomy) — NEW, FULLY PROVED (reviewer concern #1).

The route repeatedly invokes "Lemma ONE recursed down every dyadic sub-ladder." Certified Lemma ONE
is a *single* application (≤1 piece `> 2^{m−1}` in a refinement of `C_m`). The recursion it is used
at needs the fact that a *truncated sub-ladder of an admissible refinement is itself an admissible
refinement of a smaller ladder*. I prove this now as its own lemma; it reduces cleanly to certified
Lemma ONE plus a triviality, and it is the correct (true) form of "Lemma ONE recursed" — NOT the
refuted "≤1 `O_B`-interval per dyadic gap" invariant (round 7) and NOT a flat "≤1 piece per scale"
(false for low scales).

> **Lemma ONE-REC.** Let `B` be any refinement of `C_m = {2^0, 2^1, …, 2^m}` (each original piece
> partitioned into finitely many positive fragments; total number of cuts arbitrary). Write
> `G_j ⊆ B` for the multiset of fragments of the original piece `2^j` (`j = 0,…,m`), so
> `B = ⊔_{j=0}^m G_j` and `Σ G_j = 2^j`. Then:
> **(i) [scale-truncation is admissible]** for every `0 ≤ ℓ ≤ m`, the sub-multiset
>     `B_{≤ℓ} := ⊔_{j=0}^ℓ G_j` is a refinement of `C_ℓ`, using `Σ_{j≤ℓ}(|G_j|−1)` cuts.
> **(ii) [per-scale single excursion]** for every `j`, at most one fragment in `G_j` exceeds
>     `2^{j−1}`. Consequently, for every threshold `τ ≥ 2^{ℓ−1}`, at most one piece of `B_{≤ℓ}`
>     exceeds `τ` (certified Lemma ONE applied to `B_{≤ℓ}` as a refinement of `C_ℓ`), and in
>     general `N_B(τ) = Σ_{j} #\{f ∈ G_j : f > τ\}` with each summand at scale `j` contributing
>     `≤ 1` above `2^{j−1}`.

*Proof.* **(i)** By definition of a refinement, the cuts of `B` partition into groups, the `j`-th
group being the cuts applied to the original piece `2^j`; the fragments they produce are exactly the
multiset `G_j`, which therefore has `Σ G_j = 2^j` and `|G_j| ≥ 1`. Fix `ℓ`. The multiset
`B_{≤ℓ} = ⊔_{j≤ℓ} G_j` is obtained from the ladder `C_ℓ = {2^0,…,2^ℓ}` by partitioning each of its
pieces `2^j` (`j ≤ ℓ`) into the fragments `G_j`; that is *precisely* the definition of a refinement
of `C_ℓ`. The number of cuts used is `Σ_{j≤ℓ}(|G_j| − 1)` (each group of `|G_j|` fragments needs
`|G_j|−1` cuts). This is a genuine structural identity, not an assumption: no cut of `B` crosses two
original pieces, so restricting to the pieces originating from `{2^0,…,2^ℓ}` leaves a self-contained
refinement of `C_ℓ`.

**(ii)** Fix `j`. Two fragments of `G_j`, each `> 2^{j−1}`, would sum to `> 2^j = Σ G_j`, forcing
the remaining fragments of `G_j` to have negative total — impossible. Hence at most one fragment of
`G_j` exceeds `2^{j−1}`. For the "consequently" clause: by (i) `B_{≤ℓ}` is a refinement of `C_ℓ`, so
certified **Lemma ONE** (top-scale dichotomy for `C_ℓ`) gives at most one piece of `B_{≤ℓ}` exceeding
`2^{ℓ−1}`, hence at most one exceeding any `τ ≥ 2^{ℓ−1}`. The final decomposition of `N_B(τ)` is just
additivity of the count over the disjoint groups `G_j`. ∎

**Certification note.** Lemma ONE-REC is elementary and rests only on certified Lemma ONE plus the
partition-of-cuts observation; I propose it for certification (file
`lemmas/recursed-dyadic-dichotomy.md`). It is the field's single common structural dependency (both
walls use it — see outline-reviewer's diversity note), so certifying it de-risks both walls at once.
**It is now proved, not assumed** — closing reviewer concern #1.

**Where the ladder enters (reviewer constraint #3).** Lemma ONE-REC is *false* for a non-ladder
`B`; it is exactly the superincreasing structure that gives `Σ G_j = 2^j` with `2^j >
2^0+…+2^{j−1}`. The refuted witness `F = {½,½,½}, B = {½}` (`ΣF−ΣB = 1`, `|F| = 3`, yet `D(S) = 0`)
is excluded precisely because `B = {½}` is **not** a refinement of any `C_{n−1}` (the value `½` is
not a fragment of a dyadic ladder with the required masses), so Lemma ONE-REC and the `N_B ∈ {0,1}`
control on the top gap are unavailable for it. Any argument I advance below invokes Lemma ONE-REC and
therefore cannot certify that false witness — the required litmus test.

### R9.2 The reserve mechanism, made precise — and REFUTED in the proposed form (reviewer concern #2).

The outliner defines a reserve `ρ_k ≥ 0` = "credit carried down from coarser scales (the amount by
which higher scales overshot their local `∫g`)", with `Φ_k = D(S∩(0,2^{n−1−k}]) − ∫_{(0,2^{n−1−k}]}g
+ ρ_k ≥ 0`, claiming reserve-monotonicity `ρ_{k+1} ≥ ρ_k − deficit_k`, `deficit_k ≤ ρ_k`. Stripped of
`ρ_k`, `Φ_k ≥ 0` is exactly the statement that the **top-down cumulative surplus**
```
        R↓(τ) := μ{ g odd on (τ, 2^{n−1}) } − ∫_τ^{2^{n−1}} g = ∫_τ^{2^{n−1}} φ(g)         (R9-R↓)
```
is `≥ 0` for every dyadic `τ`; the reserve `ρ_k` is meant to be the accumulated `R↓` at scale `k`,
and reserve-monotonicity is meant to keep it `≥ 0`. **This is false, decisively.**

> **Refutation (naive nonnegative reserve, both directions).** Over `2·10^4` budget-respecting
> admissible `a=0` refinements per `n` (`n = 3,4,5,6`), the minimum over all dyadic `τ` of the
> top-down cumulative `R↓(τ)` was `−3.29` (`n=3`), `−7.38` (`n=4`), `−17.6` (`n=5`), `−30.5`
> (`n=6`); `R↓` was negative at some scale in `6–8%` of instances. The **bottom-up** cumulative
> `R↑(τ) := ∫_0^{τ} φ(g)` reached minima `−1.92, −4.43, −9.94, −22.97` respectively. So neither the
> top-down nor the bottom-up cumulative surplus is `≥ 0`; a nonnegative reserve equal to accumulated
> local surplus **does not exist in either direction**, and the magnitude of the deficit *grows with
> `n`* (unbounded), so it cannot be repaired by any additive constant.

*Why this is not a bookkeeping artefact.* By (R9-sign), `R↓` decreases exactly across the
`{g ≥ 2}` region and increases across `{g ≤ 0}`. The `{g ≥ 2}` region can carry `Θ(2^{n})`-worth of
deficit before any `{g ≤ 0}` credit is reached (the top fragments of `2^n` can all pile up above a
common threshold, driving `g` to `Θ(|F|)` on a band while `B` has few large pieces). The repaying
`{g ≤ 0}` credit is created only lower down, after `B`'s many small pieces overtake. So the surplus
is genuinely *not* prefix-monotone in *either* scan direction — this is the scale-level analogue of
the certified negative fact **F1** (index-prefix fails ~27%) and of the explorer's **per-dyadic-gap
local refutation** (20–75%). The outliner's `deficit_k ≤ ρ_k` fails because `deficit_k` at the top
scales can exceed *all* credit banked so far (there is none banked yet — the credit is in the
future).

**Consequence for the route (honest).** A correct reserve **cannot** be a scalar equal to
accumulated `∫φ(g)`. It must be a genuinely 2-D object that also carries the *pending* deficit held
in the current walk height. The natural candidate is
```
        Φ(τ) = ∫_0^{τ} φ(g) + ψ(g(τ)),      ψ ≥ 0,                                     (R9-Phi2)
```
with `ψ(c)` bounding the deficit still to be resolved from height `c`. **But no `ψ` depending only
on `g(τ)` can work:** across a band of length `ℓ` at constant height `c = g(τ) ≥ 2`, `Φ` drops by
`ℓ·(c − 1[c odd]) ≥ ℓ`, and `ℓ` (the measure of the high band) is *unbounded in terms of `c`* — the
`{g = 2}` region can have arbitrarily large measure relative to `g`'s value there. Hence `ψ(g(τ))`
cannot absorb the drop, and the reserve must depend on *how much `F`-mass remains above the current
scale* (a functional of the whole future of `g`, i.e. of `ΣF` already spent). **This is the precise,
proven reason the strengthened-IH reserve in the assigned form does not close MID-core**, and it
matches the explorer's finding that the compensation distance grows with `n`. The correct object is a
mass-tracking reserve `ρ(τ) = 2^n − (Σ of F-fragments already fully above τ)` coupled to the walk —
which is exactly a global (whole-ladder) accounting, not a local surplus. Constructing it and proving
its monotonicity is the residual **GAP MID-core**; I did not close it this round.

### R9.3 What is genuinely established this round.

1. **Lemma ONE-REC is proved** (R9.1), reducing "Lemma ONE recursed" to certified Lemma ONE plus a
   partition-of-cuts identity — reviewer concern #1 discharged; the field's shared structural
   dependency is now certified, not assumed.
2. **The exact target integrand** (R9-phi)/(R9-sign): `(MID-core) ⟺ ∫φ(g) ≥ 0`, with the negative
   mass localized precisely to `{g ≥ 2}` and positive mass to `{g ≤ 0}` — the cleanest statement of
   the residual to date (no `D(F)`, `D(B)`, cross-term, or walk-sign).
3. **The proposed reserve is refuted** (R9.2): no nonnegative cumulative-surplus reserve exists in
   either scan direction, and no reserve `ψ(g(τ))` depending only on the current walk height can
   work; a correct reserve must track remaining `F`-mass (whole-ladder accounting) — reviewer concern
   #2 discharged honestly (the ~27%/deficit-growth structure is shown to defeat the naive reserve,
   with the fix pinpointed).
4. **Ladder litmus test passed** (R9.1 note): the argument invokes Lemma ONE-REC, which fails for the
   half-integer witness `F={½,½,½},B={½}`, so it cannot certify that `D=0` counterexample —
   confirming the argument genuinely uses the dyadic structure (reviewer constraint #3).

**GAP MID-core remains OPEN** (residual: `max_k S_k ≥ 2`, `|F| ≥ 3`; equivalently `∫φ(g) ≥ 0` with
`{g≥2}` present). The correct reserve is a mass-tracking, whole-ladder potential — not the local
cumulative surplus (refuted) nor a walk-height function (refuted). **Status stays `partial`.**

## ROUND 10 — the mass-reserve potential: WORKING object found (κ=2, ρ=2τN_F), boundary FIXED, numerically validated n=3..7; RESERVE-NONNEG still open (PARTIAL)

This round executes the assigned gate: **grid-search the (κ,h) mass-reserve potential FIRST**, then
prove. The gate was decisive. Two facts came out of the numerics, one negative (kills the outliner's
literal reserve `R_F(τ)=Σ_{f≤τ}f`) and one positive (a *different* reserve works exactly, with a
clean boundary that fixes the reviewer's flagged inconsistency).

Throughout write `L := 2^{n−1}`, `φ(c) := 1[c odd] − c`, `g = N_F − N_B` on `(0,L)`; by certified
Lemmas MID / OSR and the R9 reformulation, **MID-core** is exactly `∫_0^{L} φ(g) ≥ 0` for admissible
`a=0` refinements with `|F| ≥ 3`.

### R10.0 The outliner's literal reserve `R_F(τ)=Σ_{f≤τ}f` is REFUTED (gate, negative).

I grid-searched `Φ(τ) = ∫_τ^{L} φ(g) + κ·h(R_F(τ))`, `R_F(τ)=Σ_{f∈F,f≤τ}f` (F-mass **below** τ),
for `h∈{linear, quadratic}`, `κ∈{0,0.05,…,50}`, over `≥1500` admissible `a=0` refinements per
`n∈{3,4,5,6}`. **Every choice fails**: `min_τ Φ` stayed strongly negative and *grew in magnitude
with `n`* (e.g. `h` linear: `min Φ ≈ −3.5 / −6.9 / −15.5 / −27.7` at `n=3/4/5/6` for the best `κ`;
`h` quadratic no better). *Reason (now understood).* `R↓(τ)=∫_τ^{L}φ(g)` reaches its most negative
value at *small* `τ` (all `{g≥2}` deficit accumulated from the top, before the bottom `{g≤0}`
repayment). But `R_F(τ)=`F-mass-**below**-τ is *small* at small τ (most F-mass sits above τ there).
So the mass-below reserve provides its cushion in exactly the wrong place — the reviewer's suspected
"do NOT degrade" concern is real for *this* reserve, but the fix is not `h`; it is a different
functional. **This also fixes the boundary defect the reviewer flagged:** with `R_F(2^{n−1})=2^n` the
outliner's `Φ(2^{n−1})=0` was impossible. The working reserve below has `Φ(L)=0` honestly.

### R10.1 The mass-ABOVE reserve `2τN_F(τ)`, `κ=2`: promising but ALSO REFUTED (gate, negative).

**Definition tested.** For `τ∈[0,L]`,
```
        Φ(τ) := ∫_τ^{L} φ(g(t)) dt  +  κ·τ·N_F(τ),        N_F(τ)=#{f∈F : f>τ}.      (R10-Φ)
```
The reserve `ρ(τ):=κτN_F(τ)` is mass-dimensioned foresight: since every counted `f>τ`,
`τN_F(τ) ≤ Σ_{f>τ}f = A(τ)` = the F-mass queued *above* τ. It is **not** the refuted `ψ(g(τ))`
(separates `τ` and `N_F`), **not** the refuted mass-below `Σ_{f≤τ}f`, and it has the clean boundary
the reviewer asked for:
- `Φ(L)=0`: `∫_L^{L}=0` and `N_F(L)=0` (every `f≤L`). **This fixes the reviewer's boundary defect.**
- `Φ(0)= ∫_0^{L}φ(g) = μ{g odd} − ∫g = D(S)−1` (certified Lemma MID); `ρ(0)=0`.

So *if* the invariant **RESERVE-NONNEG** `Φ(τ)≥0 ∀τ` held, then `τ=0` would give `D(S)−1≥0` — MID-core.

**First numerics looked like a proof — but were UNDER-SAMPLED.** On `4000`–`8000` uniform-random and
"interleave-the-uncut-tail" refinements per `n∈{3..7}`, `min_τΦ = 0.00000` with `κ=2` (attained at
`τ=L`), `κ=1.9` failing at `n=5`, and the parity term `Q` provably essential. This *appeared* to
validate `κ=2`. **It is false.** A wider adversarial search (F with two fragments both near `2^{n−1}`,
so a wide `{g=2}` band forms just below them, and a `B` whose credit recovers only slowly) breaks it.

> **Explicit counterexample (`n=7`, `L=64`, machine-verified exact).**
> `F = {63.0119, 62.8559, 2.1322}` (`ΣF=128`, each `≤64`, `|F|=3`);
> `B = {26.685, 23.0556, 19.1359, 18.1791, 16, 8.9444, 4.2039, 3.7961, 3.3844, 2, 1, 0.6156}`
> (`ΣB=127`, a valid `≤n`-cut refinement of `C_6`; total cuts `2+5=7=n`). Then
> `D(S)=15.07 ≥ 1` (so **MID-core itself holds**), yet at `τ=8.944`, `κ=2`:
> `∫_τ^{L}φ(g) = −51.95`, reserve `2τN_F(τ)=2·8.944·2=35.8` (`N_F=2`), so `Φ(τ)=−2.07 < 0`.

The mechanism of failure: the two big F-fragments create a `{g=2}` band of width `≈36`
(`τ∈(26.7,62.9)`) carrying deficit `≈−72`; the reserve `2τN_F` covers it *high up* (`≈107` at
`τ=26.7`) but shrinks **linearly** in `τ` as we scan down, while the accumulated deficit recovers only
**slowly** (B's credit is spread over small values). So `Φ` dips negative at low `τ`. Grid-search of
the required `κ` over `n=4..9` shows **no `n`-independent bound** (rare instances demand `κ>2` already
at `n=7`, and the tail creeps up with `n`) — the *same* "reserve cannot carry the deficit down" failure
as R9's cumulative-surplus reserve. **The additive constant-`κ` mass-reserve potential — in every
form tried (mass-below, mass-above `2τN_F`, cumulative-surplus, walk-height) — does NOT prove
MID-core.** The gate has done its job: RESERVE-NONNEG is FALSE, and I do not claim it.

### R10.2 Three rigorous reformulations of `Φ` (all machine-checked exact).

Let `A^{+}(τ):=Σ_{f>τ}(f−τ)`, `A_B^{+}(τ):=Σ_{b>τ}(b−τ)` (clipped masses above τ), `Q(τ):=μ{t∈(τ,L):
g(t)\ odd}`.

**(R10-int) Clipped-integral form.** By the layer-cake identity `∫_τ^{L}N_X = Σ_{x>τ}(x−τ)` and
`∫_τ^{L}1[g\ odd]=Q`,
```
        ∫_τ^{L}φ(g) = Q(τ) + A_B^{+}(τ) − A^{+}(τ),     so   Φ(τ)=Q(τ)+A_B^{+}(τ)−A^{+}(τ)+2τN_F(τ).
```
*(Proof: `∫_τ^{L}(-g)=∫_τ^{L}(N_B−N_F)=[A_B^{+}+τN_B]−[A^{+}+τN_F]` uses `A(τ)=A^{+}+τN_F` etc.,
then `τ(N_F−N_B)+2τN_F` cancels the `τN_B,τN_F` into `+2τN_F`; verified exact.)*

**(R10-clip) Clipped-`D` form.** Let `S'_τ = F'_τ ⊔ B'_τ`, `F'_τ={f−τ:f>τ}`, `B'_τ={b−τ:b>τ}`
(all values `>0`). Then `N_{S'_τ}(s)=N_S(τ+s)`, so `N_{S'_τ}≡g(τ+·)\pmod2` and by certified Lemma M,
`μ{s:N_{S'_τ}(s)\ odd}=Q(τ)=D(S'_τ)`. Since `ΣF'_τ=A^{+}`, `ΣB'_τ=A_B^{+}`,
```
        Φ(τ) = D(S'_τ) − ΣF'_τ + ΣB'_τ + 2τN_F(τ)  =  D(S'_τ) − (ΣF'_τ−ΣB'_τ) + 2τ|F'_τ|.
```
By certified Lemma OSR applied to `S'_τ` (`D(S'_τ)−(ΣF'−ΣB')=2(Σ_{B' odd rank}v'−Σ_{F' even rank}v')`),
RESERVE-NONNEG at level `τ` is **exactly**
```
        Σ_{F' at even rank} v'_i  −  Σ_{B' at odd rank} v'_i  ≤  τ·N_F(τ) = τ|F'_τ|.        (R10-shift)
```
This is the certified MID-core order-statistic inequality (debit ≤ credit) **relaxed by `τ|F'|`**:
at `τ=0` it *is* MID-core (`debit ≤ credit`); for `τ>0` the right side `τ|F'|>0` is slack.
(Identity verified exact to `1.4·10^{−14}` over 500 random `(n,τ)`.)

**(R10-disc) Discrete Abel form (minimum is at a breakpoint).** Merge `S` descending `v_1>…>v_m`
(`v_{m+1}:=0`), signs `e_i=±1`, walk `S_k=Σ_{i≤k}e_i`, `P_i:=1[i\ odd]−S_i`, `w_i:=v_i−v_{i+1}≥0`,
`c_k:=#{i≤k:e_i=+1}=N_F(v_{k+1})`. On each gap `(v_{k+1},v_k)`, `Φ` is affine in `τ` (both `∫_τ^{L}φ(g)`
and `2τN_F` are affine there, `N_F` constant), so `min_τ Φ` is attained at a breakpoint `τ=v_{k+1}`,
where
```
        Ψ_k := Φ(v_{k+1}) = Σ_{i=1}^{k} P_i\,w_i + 2 v_{k+1}\,c_k .                        (R10-Ψ)
```
`Ψ_0=0` (empty), `Ψ_m=Σ_i P_i w_i = D(S)−1` (Abel of certified OSR). RESERVE-NONNEG ⟺ `Ψ_k≥0` for
all `k`. This is the concrete inequality a charging induction (base `Ψ_0=0`, credit `2v_{k+1}` per
F-piece placed in the top block) must establish — the negative terms `P_i<0` occur exactly at
`S_i≥2` (the `{g≥2}` deficit), and the reserve `2v_{k+1}c_k` banks `2v_{k+1}` per F-piece already
placed above `v_{k+1}`.

*(Because RESERVE-NONNEG is false (R10.1), the equivalent forms (R10-shift) and `Ψ_k≥0` also fail on
the same witness — e.g. at `τ=8.944` in the `n=7` instance, `Σ_{F' even}v'−Σ_{B' odd}v' > τ|F'|`. The
identities themselves are exact algebra and remain valid; only the *inequality* is refuted.)*

### R10.3 Honest verdict and the pivot.

**The whole additive-potential family is now exhausted for MID-core.** Refuted reserves, all with the
identical failure signature (deficit created by a high wide `{g≥2}` band cannot be carried down to the
`{g≤0}` repayment by a scalar reserve, and the required correction grows with `n`):
- cumulative surplus `∫_τ^{L}φ(g)` / `∫_0^{τ}φ(g)` (R9);
- walk-height `ψ(g(τ))` (R9);
- mass-below `Σ_{f≤τ}f` (R10.0);
- mass-above `2τN_F(τ)`, any constant `κ` (R10.1).

The obstruction is structural, not a matter of tuning `(κ,h)`: a single non-negative scalar carried
along one scan cannot encode a **value-weighted, non-local** compensation (an early large `F`-even
debit paid by *several later, smaller* `B`-odd credits — the certified negative fact F1: the prefix
form fails ~27%). MID-core needs a mechanism that *matches* each debit to sufficient later credit, not
one that *accumulates* a running balance.

**Pivot (per the outline-reviewer's contingency).** Activate the **ballot-matching / Hall-transport**
mechanism (aimo-0129 endpoint-splitting) — a value-weighted `debit→larger-credit` matching, which is
exactly the non-local, non-scalar object the refutations point to. This is the far-apart lower-wall
lever the reviewer kept live as a reserve; the evidence this round (every additive potential dead,
compensation irreducibly aggregate and value-weighted) is a positive signal to build it next round.
It lives in its own slug `ballot-matching` (I stay in this file); I flag the pivot here.

**Salvage.** The exact reformulations of R10.2 are the cleanest statements of the target to date and
are promotable regardless of the failed inequality: the clipped-`D` identity
`Φ(τ)=D(S'_τ)−(ΣF'_τ−ΣB'_τ)+2τ|F'_τ|` shows MID-core is the `τ=0` face of a natural `τ`-family, and
(R10-shift) casts it as an order-statistic transport `Σ_{F' even}v' ≤ Σ_{B' odd}v' + τ|F'|` — the
precise input a Hall/transport argument must supply. **GAP MID-core remains OPEN. Status: PARTIAL.**

## Answer (confirmed, verified)

`c(n) = 2^n/(2^{n+1}−1)`, equivalently minimax `D = u_n = 1/(2^{n+1}−1)`. Verified exactly for
`n = 1` (`c = 2/3`, both bounds fully proved above) and `n = 2` (`c = 4/7`) by the extremal
construction and small-case computation; the closed form matches the recursion
`u_n = u_{n−1}/(2 + u_{n−1})` and all computed data `n ≤ 5`.

## Approaches tried
- (round 10, mass-reserve potential — PARTIAL; reserve family REFUTED, PIVOT flagged) Executed the
  gate. REFUTED the outliner's literal reserve `R_F(τ)=Σ_{f≤τ}f` (grid `h∈{lin,quad}`, `κ≤50`,
  `n=3..6`: `min Φ` grows negative `−3.5→−27.7`; wrong-place cushion; `Φ(2^{n−1})=κh(2^n)≠0` boundary
  defect). Tested the mass-ABOVE variant `Φ=∫_τ^{L}φ(g)+2τN_F(τ)` (clean boundaries `Φ(L)=0`,
  `Φ(0)=D(S)−1`): first random+interleave samples gave `min Φ=0` and *looked* validated at `κ=2`, but
  this was UNDER-SAMPLED — a wider adversarial search **REFUTES** it. Explicit `n=7` witness
  `F={63.01,62.86,2.13}`, `B` = 12-piece refinement of `C_6` (`ΣB=127`, cuts `2+5=7`): `D(S)=15.07≥1`
  (MID-core holds) yet `Φ(8.944)=−2.07<0` at `κ=2`. Mechanism: two F-fragments `≈2^{n−1}` make a wide
  `{g=2}` band (deficit `≈−72`); the reserve `2τN_F` shrinks linearly as `τ↓` while B-credit recovers
  slowly — required `κ` has NO `n`-independent bound (same failure as R9's cumulative surplus).
  CONCLUSION: the additive constant-`κ` scalar-reserve family (below / above / cumulative / walk-height)
  is EXHAUSTED for MID-core; the compensation is value-weighted and non-local (F1: prefix fails ~27%),
  needing a `debit→larger-credit` MATCHING, not a running balance. **Pivot flagged** to the
  ballot-matching Hall/transport lever (its own slug). SALVAGE: the exact reformulations stand —
  clipped-`D` `Φ=D(S'_τ)−(ΣF'−ΣB')+2τ|F'|` and (R10-shift) `Σ_{F' even}v'≤Σ_{B' odd}v'+τ|F'|` (τ=0 IS
  MID-core) are the cleanest target statements and the exact input a transport argument must supply.
  GAP MID-core NOT closed.
- (round 9, strengthened-IH scale reserve — PARTIAL/ADVANCED) Executed the outliner's reserve route.
  **Proved Lemma ONE-REC** (recursed dyadic dichotomy): a scale-truncation `B_{≤ℓ} = ⊔_{j≤ℓ}G_j` of
  any refinement `B` of `C_m` is itself a refinement of `C_ℓ` (partition-of-cuts identity), and each
  `G_j` has `≤1` fragment `> 2^{j−1}`; reduces "Lemma ONE recursed" to certified Lemma ONE (reviewer
  concern #1 discharged). Gave the **exact target integrand** `μ{g odd}−1 = ∫φ(g)`,
  `φ(c)=1[c odd]−c`, with `φ≥0 ⟺ c≤1` — so MID-core `⟺ ∫φ(g)≥0`, negative mass exactly on `{g≥2}`,
  positive on `{g≤0}`. **REFUTED the proposed reserve** (reviewer concern #2): the top-down cumulative
  surplus `∫_τ^{top}φ(g)` reaches `−30.5` at `n=6` (neg in 6–8% of instances), bottom-up reaches
  `−23`; deficit grows with `n`, so NO nonnegative cumulative-surplus reserve exists in either
  direction, and NO reserve `ψ(g(τ))` depending only on walk height works (the `{g=2}` band has
  unbounded measure per unit height). A correct reserve must track *remaining F-mass above `τ`*
  (whole-ladder accounting). Ladder litmus passed (argument uses Lemma ONE-REC, which excludes the
  `F={½,½,½},B={½}` witness). GAP MID-core NOT closed.
- (round 8, GAP MID-core / signed order-statistic reformulation — PARTIAL/ADVANCED) Recast
  `D(S) ≥ 1` as the bare **order-statistic inequality** `Σ_{B at odd rank} v_i ≥ Σ_{F at even rank}
  v_i` (eq. `Σ_i d_iv_i ≥ 0`, `d_i=(−1)^{i+1}−e_i∈{−2,0,2}`), derived cleanly from certified Lemma R
  (`D = Σ(−1)^{i+1}v_i`) and the mass identity `ΣF−ΣB = 1` — no need for MID(a) or any integral.
  **Closed a NEW sub-case** (strictly ⊃ the old `0≤g≤1`): if the descending merge walk never leads
  by two (`S_k ≤ 1 ∀k`, i.e. `N_F ≤ N_B+1` pointwise, `g ≤ 1`) then all partial coefficient-sums
  `P_k = 1[k odd] − S_k ≥ 0`, and Abel summation over descending `v` gives `Σd_iv_i ≥ 0`, hence
  `D ≥ 1`. Verified numerically (20000 refinements: identities exact; sub-case never violated).
  Established two structural facts on the residual: **(F1)** the global inequality holds in all 30000
  sampled cases but its **prefix form fails ~27%** — the compensation is irreducibly AGGREGATE, so no
  running-deficit monovariant on the merge order can prove it (rules out the naive `P_k≥0` route
  beyond R8.2); **(F2)** `S_m = |F|−|B| ≤ 0` (from `|B| = n+c_B`, `|F| = 1+c_F`, `c_F+c_B ≤ n`), so
  credits outnumber debits in COUNT (necessary, not sufficient — value-weighting still needs the
  ladder). Residual = the aggregate overshoot-repayment inequality in the regime `max_k S_k ≥ 2`,
  `|F| ≥ 3`. NOT closed.
- (round 7, structural-IH revision — PARTIAL/ADVANCED) **Refuted the outliner's specific invariant**
  ("`O_B` meets each dyadic gap in ≤1 interval") with an explicit budget-respecting witness
  (`B={1,1.865,2,2.135,2.915,5.085}` meets gap `(2,4)` in TWO intervals; interval count is
  budget-dependent, not `≤1`). In its place proved **Lemma MID** (mass-difference reduction), a
  FULLY PROVED, cross-term-free reduction: with `g = N_F − N_B` on `(0,2^{n−1})`, (a) `D(S) =
  μ{g odd}` and (b) `∫g = 1` (`= ΣF − ΣB = 2^n−(2^n−1)`, the superincreasing signature). So L2
  `⟺` **MID-core**: `μ{g odd} ≥ ∫g = 1`. This eliminates the entire cross term `μ(O_F∩O_B)`, the
  min-cap, and the balanced/unbalanced dichotomy. Closed within it: `|F|=2` (⇒ `N_F` even ⇒
  `μ{g odd}=D(B)≥1` by IH) and the `0≤g≤1` exact-floor case (`D(S)=1`). Showed the pure-integral
  version is FALSE (`g≡2` on measure `1/2`), so the ladder structure of `B` (Lemma ONE recursed)
  is essential; residual isolated to the single scalar claim MID-core (`|F|≥3`). Verified `∫g=1`,
  `μ{g odd}=D(S)`, `D(S)≥1` on `3·10^4` budget-respecting `n=4` refinements. NOT closed.
- (round 6, deliverable 1 — DONE) **Certified Lemma U0** (even-multiplicity corrector) as the
  shared file `lemmas/even-multiplicity-corrector.md`: (a) even multiplicity ⇒ `D=0`; (b) budget
  `≥ m` ⇒ bisect-all forces `D=0`; (c) `UB(n)` nontrivial only for `m=n+1`. Self-contained on
  Lemma M. Unblocks `smoothing-majorization` and `breakpoint-vertex`. Numerically re-verified.
- (round 6, deliverable 2 — GAP L2, PARTIAL/ADVANCED) Replaced the flawed "self-pairing ⇒ WLOG
  distinct fragments" reduction (which silently left the `refinement-of-C_n` structure, so did
  not induct) by a **rigorous SPLIT-based master inequality** `D(S) ≥ |D(F) − D(B)|` (Lemma SPLIT
  + `μ(O_F∩O_B) ≤ min`). With `D(B) ≥ 1` from IH LB(`n−1`), this closes the ENTIRE subregime
  `|D(F)−D(B)| ≥ 1` — in particular every even-multiplicity fragmentation `D(F)=0` (subsuming
  equal-bisection and the whole doubling-response family), via Lemma U0(a). Computed the extremal
  value exactly (`= 1`) two ways (attained cascade; (L2-telescope) merged formula). Isolated the
  sole residual to one scalar cross-term inequality **GAP L2-exch** `μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2`,
  binding only in the balanced subregime `|D(F)−D(B)| < 1, D(F) > 0`. Verified (n=3, 3·10^5 a=0
  refinements): master inequality and `D≥1` hold throughout; residual regime is real (found
  `D(F)=D(B)=1`, master gives `0`, true `D(S)=2`). Residual exchange step NOT closed.
- (prior rounds) identity `D = measure{N(t) odd}` VERIFIED; Lemmas R, I, T, P fully proved and
  certified; lower Case A (top piece uncut ⇒ `D ≥ u`) proved; greedy-match upper strategy
  analysed and proven INSUFFICIENT for `n ≥ 3`.
- (prior round) Recast the **upper bound** as a clean strong induction UB(k) with the exact
  reduction threshold `2Σ_T ≥ L(1 − u_k/u_{k−j})`; proved the **bisect** (`a₁ ≥ c(k)L`) and
  **single-match** (`a₂ ≥ c(k)L/2`) branches; closed UB(1) (n=1) entirely. Lower bound: dichotomy
  "at most one final piece exceeds `2^{n−1}`", exact identity `D(S)=f₁−D(S_L)` (a=1), a=0
  equal-bisection subcase.
- (this round, GAP U) **Closed the whole range `a₁ ≥ L/2` profile-independently** via the NEW
  **whole-tail peel Branch (2)**: for `L/2 ≤ a₁ ≤ c(k)L`, cutting `a₁` into all `m−1` tail values
  (Lemma P deletes every pair) leaves the single piece `2a₁−L` with `D = 2a₁−L ≤ u_k L` exactly
  (using `c(k)=(1+u_k)/2`); combined with Branch (0) for `a₁ ≥ c(k)L`, all of `a₁ ≥ L/2` is done.
  **REFUTED the GAP U lever:** the mass-threshold subset-cover disjunction is provably
  NON-EXHAUSTIVE for `a₁ < L/2` — explicit counterexample `A=(0.44,0.281,0.279)` (k=2) defeats
  every threshold move yet has true minimax `D=0.002 ≤ 1/7` (bisect wins). The reduction bounds
  the residual by its *mass* alone, but residual `D` depends on internal structure (near-cancelling
  tail), so no mass-only argument can close `a₁ < L/2`. Recommend RETHINK: import the induction-peel
  exact dominant-cut identity (D-tracking) or the smoothing framing for the `a₁ < L/2` regime.

## Current best
The answer `c(n)=2^n/(2^{n+1}−1)` is confirmed and the extremal construction is tight. Full
rigorous infrastructure (R, I, T, P). **Upper bound:** the entire range `a₁ ≥ L/2` is now closed
profile-independently (Branch (0) bisect for `a₁ ≥ c(k)L`, plus the NEW whole-tail peel Branch (2)
giving `D = 2a₁−L ≤ u_k L` for `L/2 ≤ a₁ ≤ c(k)L`), and n=1 is fully solved. The remaining regime
is `a₁ < L/2`, where — this round's key negative finding — the **mass-threshold subset-cover
disjunction is provably non-exhaustive** (counterexample `(0.44,0.281,0.279)`, true minimax
`0.002`): the reduction sees only residual mass, but residual `D` depends on internal structure,
so `a₁ < L/2` needs a D-tracking argument (induction-peel identity or smoothing), not more
subset-cover bookkeeping. **Lower bound:** Case A (uncut top) and the a=0 equal-bisection subcase
fully proved by IH; the a=1 case reduced by the exact identity `D(S)=f₁−D(S_L)` to `D(S_L) ≤ f₁−1`
(GAP L1). **a=0 shredded-top (GAP L2) — RE-REDUCED round 7 via NEW Lemma MID (cross-term-free):** with
`g = N_F − N_B` on `(0,2^{n−1})`, proved `D(S) = μ{g odd}` and `∫g = ΣF − ΣB = 1`, so
`D(S) ≥ 1 ⟺ μ{g odd} ≥ ∫g` (**GAP MID-core**). This supersedes the round-6 cross-term inequality
`μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2`: no `D(F)`, no `D(B)`, no min-cap, no balanced/unbalanced split.
Closed within MID: `|F|=2` and `0≤g≤1` (⇒ `D(S)=1` exact). **Refuted** the outliner's per-gap
single-interval invariant (explicit witness). Residual: MID-core for `|F|≥3` (needs a monovariant
using Lemma ONE recursed). Lemma **U0 certified** as a shared file this round.
**ROUND 9:** proved **Lemma ONE-REC** (the true "Lemma ONE recursed" — scale-truncation is an
admissible smaller-ladder refinement, `≤1` fragment `>2^{j−1}` per scale-group; reduces to certified
Lemma ONE). Gave the exact residual `μ{g odd}−1 = ∫φ(g)`, `φ(c)=1[c odd]−c`, so **MID-core ⟺
∫φ(g)≥0** (neg mass exactly on `{g≥2}`). **Refuted the proposed reserve**: no nonnegative
cumulative-surplus reserve exists (top-down min `−30.5`, bottom-up `−23` at `n=6`, growing with `n`),
and no walk-height-only reserve `ψ(g(τ))` works; a correct reserve must track remaining `F`-mass
above `τ` (whole-ladder). MID-core still OPEN, but the dead reserve shapes are now pinned down.
**ROUND 10:** tested the mass-reserve potential family and **REFUTED it** (gate). Mass-below
`R_F=Σ_{f≤τ}f` grows negative with `n`; mass-above `2τN_F` has clean boundaries (`Φ(L)=0`,
`Φ(0)=D(S)−1`, fixing the reviewer defect) and *looked* validated (`min Φ=0`, `κ=2`) but is refuted
by an adversarial witness (`n=7`, `F={63.01,62.86,2.13}`: `Φ(8.944)=−2.07<0` while `D(S)=15.07`) —
required `κ` has no `n`-independent bound (same failure as R9). The whole additive scalar-reserve
family is exhausted; the compensation is value-weighted/non-local. **Salvage:** exact reformulations
(clipped-`D`, (R10-shift) `Σ_{F' even}v'≤Σ_{B' odd}v'+τ|F'|`) are the cleanest target statement.
**Pivot** flagged to ballot-matching Hall/transport (far-apart lever).

## Open gaps
- **GAP U (upper, crux) — RE-SCOPED THIS ROUND.** The range `a₁ ≥ L/2` is now fully closed
  (Branch (0) + whole-tail Branch (2)). The ORIGINAL lever — "prove the mass-threshold
  subset-cover disjunction is exhaustive" — is **REFUTED**: it is non-exhaustive for `a₁ < L/2`
  (counterexample `(0.44,0.281,0.279)`, k=2). The true open gap is the regime **`a₁ < L/2`** at
  full budget, which provably requires a **D-tracking** argument (residual `D`, not residual mass).
  Hand-off: RETHINK GAP U — import induction-peel's exact dominant-cut identity for the top-cut
  residual, or use the smoothing/majorization framing; do NOT pursue further mass-threshold
  subset-cover variants (they cannot close `a₁ < L/2`).
- **GAP L1 (lower, a=1):** prove `D(S_L) ≤ f₁ − 1`, where `S_L` (all pieces `≤ 2^{n−1}`) is the
  final multiset minus the unique piece `f₁ > 2^{n−1}`. Tight; needs the cancellation of `2^n`'s
  sibling fragment against the tail.
- **GAP L2 (lower, a=0) — RE-SCOPED AGAIN THIS ROUND (round 7).** The round-6 form (GAP L2-exch,
  `μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2`) is now **superseded** by the cleaner, cross-term-free
  **GAP MID-core**: with `g = N_F − N_B` on `(0,2^{n−1})`, prove `μ{t : g(t) odd} ≥ 1`. By the
  FULLY PROVED **Lemma MID** this is *equivalent* to `D(S) ≥ 1` and uses `∫g = 1` (a hard identity,
  not a cap). The sub-cases `|F|=2` and `0≤g≤1` are closed; residual is strictly `|F|≥3`. The
  outliner's proposed per-gap single-interval invariant is **refuted** (explicit witness), so the
  gap-by-gap accounting route is dead; the correct residual is MID-core, which still needs a
  monovariant/exchange using Lemma ONE recursed (ladder structure of `B`). Shared in content with
  induction-peel's exchange step and merge-interleave's reachable-word minimisation.
  **ROUND 8 sharpening (Lemma OSR):** MID-core is now equivalent to the bare order-statistic
  inequality `Σ_{B at odd rank}v_i ≥ Σ_{F at even rank}v_i`. The sub-case `S_k ≤ 1 ∀k` (`g ≤ 1`) is
  now CLOSED (Lemma OSR-cap, Abel summation). Residual = the aggregate overshoot regime
  (`max_k S_k ≥ 2`, `|F| ≥ 3`); **the prefix/monovariant route is refuted** (F1: ~27% failure), so
  only a genuine aggregate transport / ladder-recursion argument can close it. Still OPEN.
  **ROUND 10 (the potential family REFUTED):** the additive scalar-reserve potential
  `Φ(τ)=∫_τ^{L}φ(g)+κ·(reserve)` does NOT prove MID-core in ANY form (mass-below, mass-above `2τN_F`,
  cumulative-surplus, walk-height): the invariant `Φ(τ)≥0` is FALSE (explicit `n=7` witness,
  `Φ(8.944)=−2.07`), and the required `κ` grows with `n`. The exact reformulation
  `Φ(τ)=D(S'_τ)−(ΣF'−ΣB')+2τ|F'|` shows MID-core is the `τ=0` face of a τ-family, cast as the
  order-statistic transport (R10-shift) `Σ_{F' even}v'≤Σ_{B' odd}v'+τ|F'|`. **Recommended route now:
  a value-weighted debit→credit MATCHING (Hall/transport), not a running scalar** — pivot to the
  ballot-matching lever. Still OPEN.

## Promotable lemmas
- **Lemma CLIP (clipped-`D` / τ-family identity) — NEW round 10, FULLY PROVED (exact identity),
  propose to certify.** For an admissible `a=0` refinement `S=F⊔B` (`L:=2^{n−1}`) and any `τ∈[0,L]`,
  let `S'_τ={p−τ:p∈S, p>τ}=F'_τ⊔B'_τ` (clip). Then `μ{g\ odd\ on(τ,L)}=D(S'_τ)` (certified Lemma M),
  and
  ```
      ∫_τ^{L}φ(g) = D(S'_τ) − (ΣF'_τ − ΣB'_τ),
      Σ_{F' even rank}v' − Σ_{B' odd rank}v' = (ΣF'_τ − ΣB'_τ) − D(S'_τ)   (certified OSR on S'_τ).
  ```
  At `τ=0` this is exactly MID-core (`D(S)−1 = ∫_0^{L}φ(g)`, `debit ≤ credit`). This is the cleanest
  statement of the residual: MID-core is the `τ=0` face of the `τ`-family, and any transport/matching
  proof must supply `Σ_{F' even}v' ≤ Σ_{B' odd}v' + τ|F'_τ|`. Exact identities only (machine-verified
  to `1.4·10^{−14}`); no inequality claimed. Self-contained on certified M/OSR.
- **NEGATIVE result (record, round 10): the additive scalar-reserve potential is REFUTED for MID-core,
  in ALL forms.** `Φ(τ)=∫_τ^{L}φ(g)+κ·ρ(τ)` with `ρ∈{Σ_{f≤τ}f, 2τN_F(τ)/κ, cumulative-surplus,
  ψ(g(τ))}` never satisfies `Φ≥0 ∀τ` with a fixed `κ`: mass-below grows negative with `n`
  (`−3.5/−6.9/−15.5/−27.7`, `n=3..6`; also boundary defect `Φ(L)=κh(2^n)≠0`); mass-above `2τN_F` (clean
  boundary `Φ(L)=0`) is refuted by an explicit `n=7` witness `F={63.01,62.86,2.13}`, `Φ(8.944)=−2.07`
  at `κ=2`, with required `κ` unbounded in `n`. Cause: a wide high `{g≥2}` band's deficit cannot be
  carried down to slow `{g≤0}` credit by a shrinking scalar reserve; the compensation is value-weighted
  and non-local (F1: prefix fails ~27%). **A running scalar reserve cannot close MID-core — a
  debit→larger-credit matching (Hall/transport) is required.** Kills the amortized-potential lever for
  the lower wall; redirects to ballot-matching.
- **Lemma ONE-REC (recursed dyadic dichotomy) — NEW round 9, FULLY PROVED, propose to certify**
  (candidate file `lemmas/recursed-dyadic-dichotomy.md`). For any refinement `B` of `C_m` with
  scale-groups `G_j` (= fragments of `2^j`): (i) every truncation `B_{≤ℓ} = ⊔_{j≤ℓ}G_j` is a
  refinement of `C_ℓ` using `Σ_{j≤ℓ}(|G_j|−1)` cuts (partition-of-cuts identity); (ii) each `G_j`
  has `≤1` fragment `> 2^{j−1}`, so certified Lemma ONE applies to every `B_{≤ℓ}`. Reduces the
  field-wide "Lemma ONE recursed" dependency to certified Lemma ONE + a triviality. Used by BOTH
  walls (parity-measure per-scale F-excess; breakpoint-vertex scale bands). Self-contained on
  certified Lemma ONE.
- **Reformulation `μ{g odd}−1 = ∫φ(g)`, `φ(c)=1[c odd]−c` (NEW round 9, FULLY PROVED).** For the
  MID-core setting, `μ{g odd} ≥ 1 ⟺ ∫_0^{2^{n−1}}φ(g) ≥ 0`; `φ(c)≥0 ⟺ c≤1`, `φ(c)<0 ⟺ c≥2`. Cleanest
  form of the residual: negative mass exactly on `{g≥2}`, positive on `{g≤0}`. Self-contained.
- **NEGATIVE result (record, round 9): the nonnegative cumulative-surplus reserve does not exist.**
  Both `R↓(τ)=∫_τ^{top}φ(g)` and `R↑(τ)=∫_0^{τ}φ(g)` go negative (min `−30.5`/`−23` at `n=6`,
  growing with `n`); and no `ψ(g(τ))`-corrected reserve works (the `{g=2}` band has unbounded measure
  per unit height). A correct reserve must track remaining `F`-mass above `τ` (whole-ladder
  accounting), not a local surplus. Kills the outliner's specific `ρ_k`-as-cumulative-overshoot form.
- **Lemma OSR (order-statistic reformulation of the a=0 lower bound) — NEW round 8, FULLY PROVED,
  propose to certify.** For an admissible `a=0` refinement `S = F ⊔ B` (`ΣF = 2^n`, `ΣB = 2^n−1`),
  merge descending `v_1 > ⋯ > v_m` with signs `e_i = ±1` (`+`=`F`, `−`=`B`). Then (a) `D(S) =
  Σ_i(−1)^{i+1}v_i` (certified Lemma R on `S`), (b) `Σ_i e_i v_i = ΣF−ΣB = 1`, hence
  `D(S) − 1 = Σ_i((−1)^{i+1}−e_i)v_i`; so **`D(S) ≥ 1 ⟺ Σ_{B at odd rank}v_i ≥ Σ_{F at even rank}
  v_i`**. Self-contained on certified Lemma R + the ladder mass identity. Cleaner than Lemma MID
  (no integration, no `g`); reusable in every lower-bound approach and in ballot-matching.
- **Lemma OSR-cap (one-sided walk sub-case) — NEW round 8, FULLY PROVED, propose to certify.** In the
  OSR setting, if the walk `S_k = Σ_{i≤k}e_i` satisfies `S_k ≤ 1` for all `k` (equivalently
  `N_F(t) ≤ N_B(t)+1` for all `t`, i.e. `g ≤ 1`), then `D(S) ≥ 1`. PROOF: the partial coefficient
  sums `P_k = 1[k odd] − S_k ≥ 0` (parity: `S_k` odd `≤1` for `k` odd; `S_k` even `≤0` for `k` even),
  so Abel summation `Σ_i d_iv_i = Σ_k P_k(v_k−v_{k+1}) ≥ 0`. Strictly generalizes the `0≤g≤1` floor
  case. Reusable.
- **NEGATIVE result (record): the prefix/monovariant form of the aggregate inequality is FALSE.**
  `Σ_{i≤k, F even}v_i ≤ Σ_{i≤k, B odd}v_i` fails for ~27% of admissible refinements (8043/30000,
  `n=2..6`), while the global `Σ_{B odd}v ≥ Σ_{F even}v` holds in all cases. Hence no running-deficit
  monovariant on the merge order can prove GAP MID-core; the compensation is irreducibly aggregate.
  Complements the count-level fact `S_m = |F|−|B| ≤ 0` (necessary, not sufficient).
- **Lemma MID (mass-difference reduction) — NEW round 7, FULLY PROVED, propose to certify.**
  For an admissible `a=0` refinement `S = F ⊔ B` (`F` = fragments of `2^n`, each `≤ 2^{n−1}`,
  `ΣF=2^n`; `B` = `≤(n−1)`-cut refinement of `C_{n−1}`, `ΣB=2^n−1`), set `g = N_F − N_B` on
  `(0,2^{n−1})`. Then (a) `D(S) = μ{t : g(t) odd}` (Lemma M + `N_S=N_F+N_B`, and `N_S=0` above
  `2^{n−1}`), and (b) `∫_0^{2^{n−1}} g = ΣF − ΣB = 1` (layer-cake). Hence `D(S) ≥ 1 ⟺ μ{g odd}
  ≥ ∫g`. Reusable in every measure-based lower-bound approach; replaces the SPLIT cross-term route.
  Self-contained on Lemma M. Sub-cases `|F|=2` and `0≤g≤1` closed inside it.
- **NEGATIVE result (record): the "≤1 `O_B`-interval per dyadic gap" invariant is FALSE.** Witness:
  refinement `B={1,1.865,2,2.135,2.915,5.085}` of `{1,2,4,8}` (budget `c_B=2≤n−1`) has
  `O_B ∩ (2,4) = (2,2.135)∪(2.915,4)` — two intervals. Interval count is budget-dependent. Kills
  the per-gap single-interval accounting route; the surviving structural fact is only Lemma ONE
  recursed (`≤1` B-excursion at the TOP of each sub-ladder, not per dyadic gap).
- **Lemma U0 (even-multiplicity corrector) — CERTIFIED THIS ROUND** as
  `lemmas/even-multiplicity-corrector.md`. (a) every value even multiplicity ⇒ `D=0`; (b) budget
  `≥ m` ⇒ bisect-all forces `D=0 ≤ u_n L`; (c) `UB(n)` nontrivial only for `m=n+1`. Self-contained
  on Lemma M. Imported by `smoothing-majorization`, `breakpoint-vertex`.
- **L2 SPLIT master inequality (NEW, certify).** For the a=0 lower-bound regime, write
  `S = F ⊔ B` (top-fragments `F`, tail refinement `B` of `C_{n−1}`). Then `D(S) ≥ |D(F) − D(B)|`.
  PROOF: Lemma SPLIT gives `D(S) = D(F)+D(B)−2μ(O_F∩O_B)`; `μ(O_F∩O_B) ≤ min(D(F),D(B))` (Lemma M
  makes `μ(O_F)=D(F)`, `μ(O_B)=D(B)`); substitute. Combined with IH `D(B) ≥ 1` it closes every
  a=0 config with `|D(F)−D(B)| ≥ 1` (incl. all even-multiplicity fragmentations, `D(F)=0`).
  Reusable in every measure-based lower-bound approach; reduces GAP L2 to the single scalar
  cross-term bound `μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2`.
- **Dyadic top-scale dichotomy.** For any refinement of `{1,2,…,2^n}`, at most one final piece
  exceeds `2^{n−1}` (superincreasing). PROVED above. Reusable in every lower-bound approach.
- **The a=1 splitting identity.** If exactly one final piece `f₁` exceeds every other piece's
  size (in particular `f₁ > 2^{n−1} ≥` all others), then `D(S) = f₁ − D(S∖{f₁})`. PROVED above
  from Lemma I (`g_S = 1[t<f₁] ⊕ g_{S_L}`). Clean, reusable; certify.
- **Upper-bound peel threshold.** A `j`-pair cancelling peel (matched mass `Σ_T ≤ a₁`) reduces
  UB(k) on total `L` to UB(k−j) on total `L−2Σ_T`, closing iff `2Σ_T ≥ L(1 − u_k/u_{k−j}) =
  L·2^{k−j+1}(2^j−1)u_k`. PROVED above (Lemma P + the `u_i` arithmetic). Shared with
  induction-peel's multi-pair identity.
- **Whole-tail-peel closed region (NEW, certify).** For UB(k) on a sorted full-budget profile
  `a₁≥…≥a_m` (sum `L`), if `L/2 ≤ a₁ ≤ c(k)L` then Xiang using `≤ k` cuts forces `D = 2a₁ − L`
  exactly (`≤ u_k L`). PROOF: cut `a₁` into the `m−1` tail values plus leftover `2a₁−L ≥ 0`
  (`≤ k` cuts), delete all `m−1` cancelling pairs by Lemma P, leaving the single piece `2a₁−L`;
  then `2a₁−L ≤ u_k L ⟺ a₁ ≤ c(k)L` via `c(k)=(1+u_k)/2`. Combined with Branch (0) (bisect,
  `a₁ ≥ c(k)L`), this closes the ENTIRE range `a₁ ≥ L/2` for every `k ≥ 1`. Reusable in every
  upper-bound approach.
- **Refutation of mass-threshold subset-cover (NEGATIVE result, record).** No reduction that
  bounds the post-peel residual by a function of its total mass alone can force `D ≤ u_k L` in
  the regime `a₁ < L/2`. Witness `A=(0.44,0.281,0.279)` (k=2): every threshold move fails
  (Branch 0/2 need `a₁≥L/2`; `j=1` peel sum `<θ_1 L`; `j=2` peel sum `>a₁`), yet true minimax
  `D = 0.002 ≤ 1/7`. Any mass-only bound of the tail `{0.281,0.279}` gives `≥ u_1·0.56 ≈ 0.187`,
  while its actual `D = 0.002`. PROVED above. Kills the subset-cover lever for `a₁ < L/2`.
