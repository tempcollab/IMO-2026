# Approach: even-rank-doublecount (scale-graded parity double-count / generating function on E(F)≤2^n−1)

## Status
partial

Honest note for the reviewer: the *specific* mechanism this slug was registered to test — a
**bivariate / scale-graded generating function producing a clean identity or per-scale defect bound
that closes `E(F)≤2^n−1`** — was put through the mandatory cheap-kill gate and **does not close the
bound** (see §3). The framing yields a genuinely new, fully-proved *reformulation* (the scale-parity
XOR identity `(⊞)`, §2), but the target inequality reduces to the SAME non-additive count-parity core
that has walled the field since R3. This is a **RETHINK signal for the genfn mechanism** (recorded
per the gate), delivered as a `partial` because the reformulation `(⊞)` is a reusable contribution.

## Approaches tried
- **(round 8 build — double-count / scale-graded genfn on `E(F)≤2^n−1`)** Ran the mandatory
  cheap-kill gate FIRST (n=2,3 exhaustive integer, n=3,4,5 real-random). Results:
  (1) **Target confirmed & tight.** `max E(F)=2^n−1` exactly, 0 violations; attained (e.g. n=2:
  scale-partition `(3,1),(2),(1)` → F=(3,2,1,1), E=2+1=3=2^2−1). Matches the certified §9 claim and
  the outline-reviewer's independent brute check.
  (2) **NEW fully-proved reformulation `(⊞)` (§2).** The even-rank sum has the level-set form
  `E(F)=∫_0^∞⌊N(t)/2⌋dt` and the discrepancy has the **scale-parity XOR form**
  `D̃(F)=O(F)−E(F)=∫_0^∞ ⊕_{j=0}^n 1[N_j(t)\text{ odd}]\,dt`, where `N_j` is the level function of
  scale `j` (fragments of `2^{n−j}`) and `⊕` is XOR. Verified `0/20000` mismatch, all `n≤5`, exact
  to `10^{−7}`. This is the "no measure language" restatement the slug promised.
  (3) **The genfn mechanism is refuted by the gate (§3).** The target `∫⊕_j s_j ≥ 1`
  (`s_j:=1[N_j\text{ odd}]`) is **non-additive**: `∫⊕s_j ≠ Σ_j∫s_j` and admits no clean per-scale
  bound. Concretely, the prefix-budget region `{Σ_{j≤k}a_j≤k ∀k}` has `min D̃ = 4.04 / 8.08 / 9.00`
  for `n=3/4/5` (huge slack), while **every** near-tight (`D̃→1`) config is *front-loaded* (budget
  concentrated on the top scales, `Σ_{j≤k}a_j>k` for some `k`). So the second (scale) grading does
  NOT recover the global bound via any pointwise/per-scale genfn identity; the `(♣)`-not-pointwise
  obstruction persists verbatim in the scale grading.
  (4) **Trivial half-bound (§2).** `⌊N/2⌋≤N/2` gives `E(F)≤Σ/2=2^n−1/2`, i.e. `D̃≥0` — free but
  the missing `1/2` (`⟺D̃≥1`) is the entire content, and it is exactly `∫(N/2−⌊N/2⌋)=½∫1[N\text{
  odd}]=D̃/2`, so the double-count reduces to the core with no gain.
  → **partial** (reformulation `(⊞)` proved and cached-worthy; genfn closing mechanism refuted by
  cheap-kill; front-loaded core is the honest open gap, coincident with the field's shared wall).

## Current best

Fully proved this round (game-free, no merged-order MEASURE language — pure level-set / scale
double-count):

- **`(⊞)` Scale-parity XOR identity + even-rank level form.** For any simultaneous refinement
  `F=⊎_{j=0}^n π_j`,
  ```
  E(F) = ∫_0^∞ ⌊N(t)/2⌋ dt ,      D̃(F) = O(F)−E(F) = ∫_0^∞ ⊕_{j=0}^n 1[N_j(t) odd] dt ,
  ```
  and equivalently (roots-of-unity form) `D̃(F)=½∫_{(0,W)}(1−∏_j σ_j)dt`, `σ_j:=(−1)^{N_j}`.
- **Trivial half-bound `E(F)≤2^n−½`** (`⟺ D̃≥0`), with the residual `½` = `D̃/2` identified as the
  whole content.
- **Sub-region delineation (empirical, §3):** the prefix-budget-ok region carries `D̃≫1`; the tight
  core is exactly the front-loaded-budget region — matching (and refining) the telescope slug's
  observation that all tight configs sit in the hard slice.

**Open gap (the whole content):** prove `∫_0^∞ ⊕_{j=0}^n s_j(t)\,dt ≥ 1` on the front-loaded-budget
core. The scale grading does not additively decompose this; the genfn route reduces to the same
non-additive count-parity inequality the field has been on since R3.

## Full proof
Not present — Status is `partial`.

---

## 1. Target (imported, certified equivalent)

By the certified §9 equivalence in `approaches/induction-recursion-telescope.md` (and the certified
Lemma G / level-measure spine), the entire open lower-bound residual (GAP L, Case B) is the
self-contained claim, with **no game and no measure/merged-order language**:

> **(Target).** Let `F=⊎_{j=0}^n π_j` be a simultaneous refinement of the dyadic multiset
> `{2^0,2^1,…,2^n}`, where `π_j` is a partition of the block `2^{n−j}` into `a_j+1` positive real
> parts and the total split budget is `Σ_{j=0}^n a_j ≤ n`. Sort `F` descending `w_1≥w_2≥…≥w_m`
> (`m=(n+1)+Σa_j`). Then the even-rank sum `E(F):=Σ_{i\text{ even}}w_i` satisfies
> ```
> E(F) ≤ 2^n − 1     ( equivalently O(F):=Σ_{i\text{ odd}}w_i ≥ 2^n,  equivalently D̃(F):=O−E ≥ 1 ).
> ```

Here `Σ F = Σ_{j=0}^n 2^{n−j} = 2^{n+1}−1`, so `O+E=2^{n+1}−1` and `E≤2^n−1 ⟺ D̃≥1`.

Write `N(t):=#\{i:w_i>t\}` for the level function of `F`, and for each scale `j`,
`N_j(t):=#\{p∈π_j:p>t\}`, so `N=Σ_{j=0}^n N_j`. Put `s_j(t):=1[N_j(t)\text{ odd}]∈\{0,1\}`.

**Cheap-kill confirmation of the target (gate, done first).** Exhaustive over all *integer*
refinements: n=2 (7 configs) `maxE=3=2^2−1`; n=3 (62 configs) `maxE=7=2^3−1`; both tight, 0
violations. Real-random (20000 configs each) for n=2,3,4,5: `maxE = 3, 7, 15, 30.74`, 0 violations,
tight up to n=4. The target is true and tight — the wall is a missing mechanism, not a false claim.

## 2. Two fully-proved double-count reformulations `(⊞)` (NEW)

These use only the definition of even-rank sum and the additivity `N=Σ_jN_j` — no game, no cutting,
no merged-order signed-sum. They are the "static double-count / generating-function" objects the slug
promised, and they are exact.

**Lemma 2.1 (even-rank level form).** `E(F)=∫_0^∞⌊N(t)/2⌋\,dt` and `O(F)=∫_0^∞⌈N(t)/2⌉\,dt`.

*Proof.* For each `k≥1`, the `(2k)`-th largest part satisfies `w_{2k}=λ\{t:N(t)≥2k\}` (indeed
`N(t)≥2k ⟺ t<w_{2k}`, using the descending sort; `w_{2k}=0` for `2k>m`). Summing,
`E(F)=Σ_{k≥1}w_{2k}=Σ_{k≥1}λ\{N≥2k\}=∫_0^∞Σ_{k≥1}1[N(t)≥2k]\,dt=∫_0^∞⌊N(t)/2⌋\,dt`, by
Tonelli (all terms `≥0`) and `Σ_{k≥1}1[N≥2k]=⌊N/2⌋`. Likewise `O(F)=Σ_{k≥0}w_{2k+1}
=∫⌈N/2⌉` since `Σ_{k≥0}1[N≥2k+1]=⌈N/2⌉`. ∎

**Lemma 2.2 (scale-parity XOR identity).**
`D̃(F)=O(F)−E(F)=∫_0^∞ 1[N(t)\text{ odd}]\,dt=∫_0^∞ \big(⊕_{j=0}^n s_j(t)\big)\,dt.`

*Proof.* `⌈N/2⌉−⌊N/2⌋=1[N\text{ odd}]`, so `D̃=∫1[N\text{ odd}]` by Lemma 2.1 (this also matches the
certified level-measure form `D̃=λ\{t:N(t)\text{ odd}\}`). For the XOR: `N=Σ_jN_j`, so
`N\bmod2=Σ_j(N_j\bmod2)\bmod2`, i.e. `1[N\text{ odd}]` is the XOR of the bits `1[N_j\text{ odd}]=s_j`.
Hence `1[N\text{ odd}]=⊕_j s_j` pointwise, and integrating gives the claim. ∎

*Verification.* `D̃(F)=∫⊕_js_j` was checked to `10^{−7}` on `20000` random real configs for each of
`n=2,3,4,5` — **0 mismatches**. The identity is exact.

**Roots-of-unity (generating-function) form.** Equivalently, with `σ_j:=(−1)^{N_j}∈\{±1\}` (a
per-scale sign that is `+1` where `N_j` is even, `−1` where odd),
`1[N\text{ odd}]=\tfrac12(1−∏_{j}σ_j(t))`, so on the support `(0,W)` (`W:=w_1≤2^n`, beyond which all
`N_j=0`),
```
D̃(F) = ½∫_0^{W}\big(1 − ∏_{j=0}^n σ_j(t)\big)\,dt .        (RUF)
```
`(RUF)` is exactly the `x=−1` roots-of-unity filter the outline named, with the **product over
scales** as its second (scale) grading. It is a correct identity; §3 shows it does not deliver a
closing bound.

**Corollary 2.3 (trivial half-bound).** `E(F)≤Σ/2=2^n−½`, i.e. `D̃≥0`.

*Proof.* `⌊N/2⌋≤N/2`, so `E=∫⌊N/2⌋≤½∫N=½ΣF=2^n−½` (using `∫_0^∞N=ΣF` by Tonelli). ∎

**The residual is the whole content.** `2^n−E=½∫(N−2⌊N/2⌋)=½∫1[N\text{ odd}]=D̃/2`. So
`E≤2^n−1 ⟺ D̃≥1 ⟺ ∫⊕_js_j≥1`, and Corollary 2.3 (the free part of the double count) only gives
`≥0`. **The double-count buys the sign but not the constant `1`.**

## 3. Why the genfn mechanism fails the cheap-kill (RETHINK signal, recorded)

The slug's intended engine was: express `E(F)−(2^n−1)` as a **sum over scales of a per-scale defect
controlled by `a_j`**, with `Σa_j≤n` forcing the total `≤0` — read via `(RUF)` plus a scale-grading
variable `q`. The gate refutes this engine.

**(i) The XOR target is non-additive across scales.** `∫⊕_js_j` is not `Σ_j∫s_j=Σ_jD̃_j`
(`D̃_j:=` alternating sum of `π_j`): for the reference (all uncut), `Σ_jD̃_j=Σ_j2^{n−j}=2^{n+1}−1`
while `∫⊕s_j=D̃=(2^{n+1}+(−1)^n)/3`. The `∏_jσ_j` in `(RUF)` is a genuine product; expanding it by
inclusion–exclusion produces `2^{n+1}` alternating-sign cross terms `∫∏_{j∈S}σ_j` over subsets `S`
of scales, with no sub-collection dominating — there is no clean per-scale identity. This is the
`(♣)`-not-pointwise obstruction (`1[N\text{ odd}]≤N` fails pointwise) reappearing verbatim under the
scale grading: the second grading does not linearize the parity.

**(ii) The tight cases are exactly where a per-scale bound would have to be sharp, and there the
budget is front-loaded.** Cheap-kill (60000 random real configs each):

| n | overall `min D̃` | `min D̃` on prefix-budget-ok `{Σ_{j≤k}a_j≤k ∀k}` | # front-loaded (prefix-bad) | `min D̃` on front-loaded |
|---|---|---|---|---|
| 3 | 1.0000 | **4.04** | 54675/60000 | 1.0000 |
| 4 | 1.0000 | **8.08** | 58118/60000 | 1.0000 |
| 5 | 1.0325 | **9.00** | 59354/60000 | 1.0325 |

So the prefix-budget-ok region (where a naive scale induction would apply the IH to each top prefix
`F^{≤k}`) carries margin `D̃≥4,8,9` — never close to `1`. **Every** near-tight configuration is
*front-loaded*: the budget is spent on the top scales, so `F^{≤k}` for small `k` is over-budget
(`Σ_{j≤k}a_j>k`) and the IH is unavailable there. A per-scale genfn defect controlled by `a_j` would
have to be exactly tight precisely where the budget accounting breaks — which is the same
front-loaded core the merged-order machinery already isolated. No clean generating-function identity
survives this.

**Conclusion.** The bivariate/scale-graded genfn does **not** close `E(F)≤2^n−1`. The reformulation
`(⊞)`/`(RUF)` is exact and reusable, but the target reduces to `∫⊕_js_j≥1` on the front-loaded core,
which is the field's shared wall (the non-additive count-parity inequality, refuted for scalar
summaries, top-down reserves, budget-count, and local injections in prior rounds). **This is the
RETHINK signal the gate asked for**: the genfn mechanism as set up cannot recover the global bound.

## 4. What is genuinely new and reusable

- The **scale-parity XOL identity `(⊞)`** `D̃(F)=∫⊕_j 1[N_j\text{ odd}]` (Lemma 2.2) is a clean,
  game-free, measure-free restatement that keeps *every scale's parts separate* (it does NOT summarize
  `Z` by a scalar — the refuted move). It expresses the whole lower bound as a **parity-covering
  problem across `n+1` interval-parity functions with a shared budget `Σa_j≤n`**. This may seed a
  genuinely different framing (e.g. a discrepancy/covering argument on the `s_j`), distinct from both
  the merged-order signed sum and the ordered-cut potential.
- The **front-loaded/prefix-budget dichotomy** (§3) sharpens the residual: the prefix-budget-ok slice
  is not the wall (huge margin); only the front-loaded slice is. This is a cleaner cut than the
  `maxc≥2` description and could focus the next mechanism.

## 5. Honest gap

The target `∫_0^∞⊕_{j=0}^n s_j(t)\,dt ≥ 1` on the front-loaded-budget core is **not proved**. The
double-count/generating-function framing reformulates it exactly `(⊞)/(RUF)` and secures the trivial
`D̃≥0`, but the constant `1` requires the same non-additive, bottom-inclusive count-parity
amortization across scales that is the shared open wall. The intended genfn closing mechanism is
refuted by the cheap-kill (§3). Recommendation: RETHINK this slug's mechanism (the reformulation
`(⊞)` should be preserved / certified and handed to a covering-style or amortized argument, not a
per-scale genfn identity).

## Promotable lemmas
- **Scale-parity XOR identity `(⊞)` (NEW round 8, fully proved, §2, verified `0/20000` mismatch,
  `n≤5`).** For any simultaneous refinement `F=⊎_{j=0}^n π_j` with scale-`j` level function `N_j`:
  `E(F)=∫⌊N/2⌋`, `O(F)=∫⌈N/2⌉`, and `D̃(F)=O−E=∫_0^∞ ⊕_{j=0}^n 1[N_j(t)\text{ odd}]\,dt
  =½∫_{(0,W)}(1−∏_jσ_j)dt`, `σ_j=(−1)^{N_j}`. Game-free, measure-language-free restatement of the
  lower-bound discrepancy that keeps each scale's parts separate. (Good `lemmas/` candidate; a clean
  reusable identity for GAP L.)
- **Trivial half-bound (NEW, §2).** `E(F)≤ΣF/2=2^n−½` (`⟺D̃≥0`), with `2^n−E=D̃/2`, isolating the
  missing constant `1` as exactly `∫1[N\text{ odd}]≥1`.
