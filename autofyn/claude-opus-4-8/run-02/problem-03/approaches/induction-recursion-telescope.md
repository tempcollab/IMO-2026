# Approach: induction-recursion-telescope (merged-order signed-sum + lattice telescoping on Z's cut-tree)

## Status
partial

## Approaches tried
- **(round 8 build — GAP L, greedy bounded-window nonneg-block TILING (crux aimo-0626))** The
  assigned mechanism — tile the merged index set into consecutive blocks of nonnegative
  `ψ(c_i)Δw_i`-sum — is **REFUTED as a local (bounded-window / greedy) certificate** (NEW dead end,
  §15), together with two rigorous supporting results. (a) **No local certificate exists.** A
  greedy minimal-nonneg-window tiling fails in **both** directions on `222/2·10⁵` residual configs
  (forward alone fails `28298`, backward alone `10049`); the minimal such witness (`n=3`,
  `Y=(3.382,2.553,2.065)`, `Z=(4,1.042,1,0.958)`, `D̃=2.107`) has a single deficit term
  `s_4=−2.046` that **exceeds each adjacent surplus separately** (`s_1=+1.237<2.046` on the left,
  `s_7=+1.916<2.046` on the right) — so no one-sided or bounded window covers it; only the *whole
  list* (`1.237−2.046+1.916=1.107≥0`) works. Since a partition into consecutive nonneg blocks
  **always** exists iff the total is `≥0` (take the single block `[1,m]`), the tiling is
  **logically equivalent to the target** `Σs_i≥0` and carries **no independent content** — the
  crux-aimo-0626 adaptation is circular here. (b) **Budget-height lemma (NEW, PROVED, §15).**
  `max_i c_i ≤ a_0+1` where `a_0+1=|Y|`; proved (only `Y`-parts raise `c`, so `c_i≤#\{Y\text{-parts}\}`),
  verified `0/10⁵`. It bounds the *height* of excursions but **not** the window length or block sum,
  so it does not rescue the tiling. (c) **All measure/layer forms restate `D̃≥1` (NEW, PROVED §15).**
  The layer identity gives `∫(⌊M^+/2⌋−⌈M^-/2⌉)dt = ½−½D̃` exactly (verified `0/10⁵`), so the summed
  form `Σ_kλ(A_{2k})≤Σ_kλ(B_{2k-1})`, the `(♠≥0)` form, and `(△⋆)` are **all equivalent
  restatements** of `D̃≥1` obtained by pure measure algebra — none injects the dyadic/budget
  structure, confirming the content is irreducibly the dyadic parity-measure bound. → **partial**
  (assigned tiling mechanism refuted as a local certificate; the wall is sharpened — any tiling is
  global/circular, so the closure must inject the dyadic budget through a genuinely non-local
  argument, not a bounded-window block decomposition).
- **(round 7 build — GAP L, exact threshold-split identity + reserve search)** Three rigorous
  results and one refuted reserve, sharpening the residual but NOT closing it (honest partial):
  (1) **Threshold-split identity `(△)` (NEW, fully proved, §13).** Splitting the level integral at
  `θ=2^{n−1}` and using the half-total single-crosser fact (at most one `Y`-fragment exceeds `θ`),
  `D̃(F) = (y₁−θ)⁺ + λ_{(0,θ)}(O_Y △ O_Z)` **exactly** — the *symmetric-difference* refinement of the
  round-2 inequality `(★★)` (which only gave `≥`). Verified `0/2·10⁵` (all `n≤6`).
  (2) **Localized reduction (NEW).** With `β:=(y₁−θ)⁺`, `M:=N_Y−N_Z` on `(0,θ)`, one has
  `∫_{(0,θ)}M = 1−β ∈(0,1]`, so the ENTIRE Case-B target collapses to the single clean localized
  inequality `λ_{(0,θ)}{M odd} ≥ ∫_{(0,θ)}M` with total mass `≤1`. This is `(♣)` restricted to
  `(0,θ)` with the *bounded* right side `1−β`.
  (3) **LAYER identity re-confirmed (§8 memory).** `D̃−1 = 2(Σ_kλ(B_{2k−1}) − Σ_kλ(A_{2k}))`,
  `A_j={M≥j}`, `B_j={M≤−j}`; verified `0/1.5·10⁵`.
  (4) **Reserve candidate REFUTED (NEW dead end, §13).** "`Z`'s odd-level measure leads its even-level
  measure from the top" — i.e. `λ{t>τ:N_Z odd} ≥ λ{t>τ:N_Z even,N_Z>0}` for all `τ` — is FALSE
  (`7306/4·10⁵` violations, worst `−22.5`). So the compensating surplus is NOT a top-down reserve of
  `Z`; the tie config `n=4,Y=(8,3,3,2),Z=(8,2,2,2,1)` realizes its whole surplus in the **near-0
  band** `(0,1)` (there `N_Z=5` odd, `N_Y=4` even; the top anchor `8` sits in BOTH `O_Y,O_Z` and
  cancels in `△`). Confirms the compensation is a **global, bottom-inclusive** parity effect across
  scales, not a top-anchor reserve — killing the "reserve carried down from the top" IH shape. →
  **partial** (identity sharpened to a bounded-mass localized inequality; another reserve shape killed).
- **(round 6 build — GAP L, telescope route, anchor-domination attempt)** Four rigorous
  new results, and one refutation that redirects the field:
  (1) **Tie-normalization resolved (§7).** `D̃` is the value-only alternating sum of the sorted
  merged list, hence *tie-break invariant*; the (♦)/(♣) machinery may use any tie-break. With the
  canonical **Y-before-Z** tie-break, the exact-tie boundary `y₁=θ` (e.g. `n=4,Y=(8,3,3,2),
  Z=(8,2,2,2,1)`, `D̃=1`) sits in `maxc≥2` with `D̃=1` *attained* — so the target is the **non-strict**
  `D̃≥1`, equality tracked, and the round-4 "strict slack ≥1.017" is a finite-sampling artifact
  (confirmed refuted).
  (2) **Abel-summation increment identity `(♠)` (NEW, fully proved, §8).** Summation-by-parts on
  `(♦)` collapses `ψ` to its step-increments, giving the clean **position-parity identity**
  `D̃−1 = 2·(Σ_{z∈Z at odd merged-pos} z − Σ_{y∈Y at even merged-pos} y)`, because the running
  imbalance parity equals the merged-position parity (`c_{i−1}≡i−1 mod 2`). Verified to `10^{−14}`
  over `2·10⁴` splits.
  (3) **Self-contained restatement (NEW, §9).** The whole Case-B target is equivalent to the purely
  combinatorial **`even-rank sum(F) ≤ 2^n−1`** (equivalently `odd-rank sum ≥ 2^n`), for `F` any
  simultaneous refinement `F=⊎_{j=0}^n π_j` (`π_j` a partition of `2^{n−j}`, `Σa_j≤n`). Verified:
  max slack exactly `0`, attained (`2·10⁵` configs).
  (4) **The anchor-matching mechanism (outline Step 5) is REFUTED (NEW dead end, §10).** The
  proposed "match each T-run against `Z`'s anchor, width-weighted" is a *value/width-dominating
  injection* `{Y even-pos}→{Z odd-pos}`. Such an injection provably does **not** exist in general:
  the survival-function (measure) domination `#{Z odd-pos>τ} ≥ #{Y even-pos>τ}` **fails on `21%`**
  of Case-B configs (`4.3·10⁴/2·10⁵`), e.g. `n=5,a=1,b=1: Y=(17.9,14.1)`,
  `Z=(11.42,8,4.58,4,2,1)` gives `Z_odd=(11.42,4.58,2)`, `Y_even=(14.1)` — a single `Y`-part `14.1`
  exceeds every `Z`-odd part yet `ΣZ_odd=18>14.1`. **The compensation is genuinely GLOBAL (a sum
  across scales), not a per-anchor/per-run match.** So the residual cannot be closed by a local
  width-weighted domination; it requires a global argument on `Z`'s cut-tree. → **partial** (residual
  reformulated cleanly and sharpened; local-matching route killed; global gap isolated).
- **(round 4 build — GAP L, telescope route)** Installed the merged-order signed-sum
  reformulation of GAP-LB′ and closed its **tight core**. Three rigorous new results:
  (1) **Clean reformulation `(♣)`.** In Case B, in integer units, `sum(Y)−sum(Z)=2^n−(2^n−1)=1`
  *identically*, so with `M(t):=N_Y(t)−N_Z(t)` (integer step function, `∫M=1`) and using that
  `N_Y+N_Z ≡ N_Y−N_Z (mod 2)`, the target `D̃≥1` is **exactly** `∫1[M odd] ≥ ∫M`.
  (2) **Merged-order lattice form.** Merge `Y⊎Z` into one descending list `w_1≥…≥w_m` with T/B
  labels; the prefix imbalance `c_i:=#T−#B` in `w_1..w_i` equals `M` on `(w_{i+1},w_i)`, and
  `D̃−1 = Σ_i ψ(c_i)(w_i−w_{i+1})` with `ψ(c):=1[c odd]−c`. This is Lemma G's signed sum on the
  merged order, made exact.
  (3) **Termwise Lattice Lemma (NEW, fully proved).** Since `ψ(c)≥0 ⇔ c≤1`, if the merged order
  has `c_i≤1` for every prefix then `D̃−1=Σψ(c_i)(w_i−w_{i+1})≥0` **termwise** ⇒ `D̃≥1`. This
  closes the sub-region "no top-run gets `≥2` ahead," which — verified over `4·10⁵` residual
  configs, `n≤5` — contains **every tight (`D̃=1`) configuration**; the residual `maxc≥2` cases
  all carry strict slack (`min D̃≈1.017`). So the hardest, equality-attaining part of GAP-LB′ is
  now rigorously closed. → **partial** (tight core closed; `maxc≥2` residual isolated, see below).
- **(carried, round 3)** threshold-domination refinement `(◇◇) D̃≥(y₁−θ)⁺`; Case B closed on
  `{y₁≥2^{n−1}+1}∪{|D_top^<−D_bot|≥1−D_top^>}`; one-sided confinement of `O_Z` REFUTED.
- **(carried, round 2)** exact-value recursion in integer units; `(★)` threshold identity;
  `(★★) D̃≥D_top^>+|D_top^<−D_bot|`; Case B ~85% closed. Base `P(0)`, Case A done.
- **(carried, round 1)** reduction to discrepancy minimax via Lemma G, Level-Measure Formula,
  Cut-Flip Lemma (all certified); Case A of the lower bound.

## Current best

The lower bound is reduced (integer units, Liu `={1,2,…,2^n}`, target `D̃≥1`) to Case B, and Case B
is closed **except** on a precisely isolated residual. What is now proved for Case B:

- Base `P(0)`, Case A (`a=0`) — done (Domination corollary C3).
- Case B on `{y₁≥2^{n−1}+1}` by `(◇◇)`, and on `{|D_top^<−D_bot|≥1−D_top^>}` by `(★★)`.
- **Case B on the whole `maxc≤1` region — NEW this round, via the Termwise Lattice Lemma.**
  In particular this closes **every tight configuration** (`D̃=1` is attained only with `maxc≤1`).

**Open residual GAP-LB′-run.** The merged descending order of `Y⊎Z` has some prefix with `c_i≥2`
(a "T-run" where top-fragments get `≥2` ahead of Z-parts). Numerically these all satisfy `D̃>1`
but their infimum approaches `1` (min observed `1.017`), so no crude slack estimate closes them:
the required compensation is supplied by **Z's own dyadic anchors** (uncut/large dyadic pieces of
`Z` sitting above `Y`-fragments create negative-`c` excursions of definite width), which is exactly
the recursive cut-tree structure a scalar summary of `Z` cannot supply. This is the honest remaining
gap; it is strictly smaller than the round-3 residual (the tight core is now removed).

**Round-6 sharpening.** The residual `maxc≥2` is now reformulated in three equivalent clean forms
(§8–§9), the tie boundary is normalized away (§7, target is non-strict `D̃≥1` with equality
tracked), and the *local* anchor-matching mechanism the outline proposed for Step 5 is **refuted**
(§10): no value/width-dominating injection `{Y even-pos}→{Z odd-pos}` exists in general, so the
compensating surplus is supplied *globally by `Z`'s cut-tree*, not by any single matched anchor.
The honest open gap is the **global sum inequality** `(♠≥0)` of §8, restated combinatorially as
`even-rank sum(F) ≤ 2^n−1` in §9; it must be proved through `Z`'s recursive structure (§5) by a
global argument, not a matching or a scalar summary of `Z`.

**Round-7 sharpening.** The exact **threshold-split identity `(△)`** (§13),
`D̃(F)=(y₁−θ)^+ + λ_{(0,θ)}(O_Y△O_Z)`, replaces the round-2 inequality `(★★)` by an equality and
collapses the whole Case-B residual to the **bounded-mass localized inequality** `(△⋆)`:
`λ_{(0,θ)}\{M\text{ odd}\} ≥ ∫_{(0,θ)}M = 1−β` with total mass `≤1`, `M=N_Y−N_Z`. Separately, the
outline's **top-down reserve** IH shape is refuted (§14): "`Z`'s odd measure leads its even measure
from the top" fails on `7306/4·10⁵` configs, and in the tie config `n=4,Y=(8,3,3,2),Z=(8,2,2,2,1)`
the entire surplus sits in the **near-0 count-parity band** `(0,1)` (`|Z|=5` odd vs `|Y|=4` even)
while the top anchor `8` cancels in `O_Y△O_Z`. So the surplus is **bottom-inclusive and global**; the
residual must be closed by a joint count-parity amortization across all scales, not a top-anchor
reserve. Both a scalar summary and a top-down reserve of `Z` are now ruled out.

**Round-8 sharpening (this round).** The assigned **greedy bounded-window nonneg-block tiling**
(crux aimo-0626) is **refuted as a local certificate** (§15): (i) a consecutive-nonneg-block tiling
exists **iff** the total `Σψ(c_i)Δw_i≥0`, so the device is logically equivalent to the target and has
content only if blocks are certified *locally*; (ii) local certification is impossible — a single
deficit run can exceed **every** individual adjacent surplus, so its only nonneg window is the whole
list (minimal witness `n=3,Y=(3.382,2.553,2.065),Z=(4,1.042,1,0.958)`, `s_4=−2.046`, left `+1.237`,
right `+1.916`, both `<2.046`); both-directional greedy fails on `222/2·10⁵`; (iii) the budget bound
only caps excursion **height** `maxc≤a_0+1` (Lemma H), not window length; (iv) all layer/summed/
position-parity/`(△⋆)` forms are pure measure-algebra restatements of `D̃≥1` (identity `(△△)`
`∫(⌊M^+/2⌋−⌈M^-/2⌉)=½−½D̃`), and the trivial layer bound only gives `D̃≥0` (off by `½`). Net: the
bounded-window tiling family is eliminated; the missing `½` must be injected by the dyadic budget
`Σa_j≤n` **non-locally**, not by any block/window decomposition of the merged order.

## Progress (full detail of the proved part)

Throughout, we import verbatim the certified spine from `results/imo-2026-03/lemmas/`:
**Lemma G** (greedy claim = odd-rank sum, with the Level-Measure integral form
`D=λ{t>0:N(t) odd}` where `N(t)=#\{parts>t\}`) and the **Cut-Flip Lemma** (with the Domination
corollary **C3**: `D≥2b₁−1` for a multiset of total `1`, i.e. `D̃≥2b₁−T` for total `T`). We also
import from `approaches/induction-recursion.md` the certified reduction of the whole answer to the
discrepancy minimax `D*=u_n`, and the integer-unit normalization. We only re-derive what is new.

### 1. Setup: integer-unit Case B (imported, restated)

Rescale all lengths by `1/u_n`. Liu's dyadic partition becomes the integer weights
`{1,2,4,…,2^n}` of total `2^{n+1}−1`; the top piece is `2^n`, the bottom block is the **literal**
`(n−1)`-dyadic `{1,…,2^{n−1}}` of total `2^n−1`. Discrepancy is homogeneous of degree 1 and the cut
operation is scale-covariant, so the target `D≥u_n` becomes `D̃≥1` in these units.

Fix a Xiang response with `a` cuts on the top piece and `b` on the bottom block, `a+b≤n`. Because a
stick can only be cut (never merged), cuts inside `2^n` and cuts inside the bottom block act on
disjoint sub-multisets, and the final multiset is `F=Y⊎Z`, where:

- `Y` = the top-descendants: `a+1` positive parts summing to `2^n`, each `≤2^n`;
- `Z` = the bottom-descendants: a `≤b`-cut response to the `(n−1)`-dyadic `{1,…,2^{n−1}}`, of total
  `2^n−1`, with every part `≤2^{n−1}=:θ`.

**Case A** (`a=0`) is settled by C3 (`D̃≥2·2^n−(2^{n+1}−1)=1`). We treat **Case B** (`a≥1`, so
`b≤n−1`). By the inductive hypothesis `P(n−1)` applied to `Z`,
```
D_bot := λ(O_Z) = altsum(Z) ≥ 1 ,    O_Z:={t>0 : N_Z(t)=#{z∈Z:z>t} odd}.       (IH)
```

Write `N_Y(t)=#\{y∈Y:y>t\}`, `N_Z(t)=#\{z∈Z:z>t\}`, so `N_F=N_Y+N_Z`. By Lemma G (integral form),
`D̃=λ(O_F)=∫_0^∞ 1[N_F(t)\text{ odd}]\,dt`.

### 2. The exact-difference reformulation `(♣)` — PROVED

Define the integer step function
```
M(t) := N_Y(t) − N_Z(t).
```
Two elementary facts.

**(a) Parity.** `N_F=N_Y+N_Z` and `M=N_Y−N_Z` differ by `2N_Z`, hence have the same parity:
`1[N_F(t)\text{ odd}] = 1[M(t)\text{ odd}]` for every `t`. Therefore
```
D̃ = ∫_0^∞ 1[M(t)\text{ odd}]\,dt.
```

**(b) The integral of `M` is exactly 1.** By Fubini (each part `y=∫_0^∞ 1[y>t]dt`),
`∫_0^∞ N_Y\,dt=\sum_{y∈Y}y=2^n` and `∫_0^∞ N_Z\,dt=\sum_{z∈Z}z=2^n−1`, both finite. Hence
```
∫_0^∞ M(t)\,dt = \sum_{y∈Y}y − \sum_{z∈Z}z = 2^n − (2^n−1) = 1.       (⋆)
```
The value `1` is not an estimate — it is forced by the dyadic weights (`sum(Y)−sum(Z)=1` exactly).

Combining (a),(b), the Case-B goal `D̃≥1` is **equivalent** to
```
∫_0^∞ 1[M\text{ odd}]\,dt ≥ ∫_0^∞ M\,dt .                                (♣)
```
This is the promised clean restatement — it foregrounds the single integer profile `M`, replacing
the opaque cancellation term `2λ(O_Y^<∩O_Z)` of the round-2 identity `(★)`. (Consistency check: `(♣)`
combined with `(⋆)` is `D̃≥1`; and `∫1[M odd]−∫M = ∫(1[M odd]−M)`, which we bound next.)

*Note (`(♣)` is NOT pointwise).* At a `t` with `N_Y=3,N_Z=0` we have `M=3`, and `1[M odd]=1<3=M`;
so `(♣)` can only hold as an integral. This is exactly why a scalar summary of `Z` is insufficient
(three counterexamples on record, `/tmp/round-4/math-explorer-gapL-interleaving.md`, probes 5–7):
the balancing is global and needs `Z`'s structure.

### 3. Merged-order lattice form of `(♣)` — PROVED

Merge `Y⊎Z` into one **descending** sorted list of its `m:=|Y|+|Z|` parts,
`w_1≥w_2≥…≥w_m` (`w_{m+1}:=0`), and label each `w_i` by `T` if it is a top-fragment (from `Y`) or
`B` if a bottom-part (from `Z`). Define the **prefix imbalance**
```
c_i := #\{j≤i : w_j\text{ labelled }T\} − #\{j≤i : w_j\text{ labelled }B\},    c_0:=0.
```
`c_i−c_{i−1}=+1` if `w_i` is `T`, `−1` if `B`; so `(c_i)` is a `±1` lattice path from `c_0=0`.

**Claim.** For `t∈(w_{i+1},w_i)`, `M(t)=c_i`. *Proof.* The parts exceeding such a `t` are exactly
`w_1,…,w_i`; among them the `T`'s are the `Y`-parts `>t` (count `N_Y(t)`) and the `B`'s are the
`Z`-parts `>t` (count `N_Z(t)`). Hence `c_i=N_Y(t)−N_Z(t)=M(t)`. ∎

Because `M` is constant `=c_i` on each interval `(w_{i+1},w_i)` of length `Δw_i:=w_i−w_{i+1}≥0`,
```
∫_0^∞ M\,dt = \sum_{i=1}^m c_i\,Δw_i ,        ∫_0^∞ 1[M\text{ odd}]\,dt = \sum_{i=1}^m 1[c_i\text{ odd}]\,Δw_i .
```
(The first sum re-derives `(⋆)` by Abel summation: `\sum c_iΔw_i=\sum w_i(c_i−c_{i−1})=\sum_T w_i−\sum_B w_i`.)
Subtracting, with `ψ(c):=1[c\text{ odd}]−c`,
```
D̃ − 1 = ∫(1[M odd]−M)\,dt = \sum_{i=1}^m ψ(c_i)\,Δw_i .                    (♦)
```
This `(♦)` is the merged-order signed sum: the entire Case-B target is `\sum_i ψ(c_i)Δw_i≥0`.

*Values of `ψ`.* `ψ(1)=ψ(0)=0`; for `c≤0`, `ψ(c)=1[c odd]−c≥−c≥0`; for `c≥2`,
`ψ(c)=1[c odd]−c≤1−c≤−1<0`. Thus
```
ψ(c) ≥ 0  ⇔  c ≤ 1 ,    and   ψ(c) < 0  ⇔  c ≥ 2 .                        (♦♦)
```

### 4. Termwise Lattice Lemma — closes the `maxc≤1` region (NEW, PROVED)

> **Lemma T (Termwise Lattice Bound).** If the merged descending order of `Y⊎Z` satisfies
> `c_i ≤ 1` for **every** prefix `i` (equivalently: in no prefix do the top-fragments outnumber the
> bottom-parts by `≥2`), then `D̃ ≥ 1`.

**Proof.** By `(♦♦)`, `c_i≤1` gives `ψ(c_i)≥0` for every `i`; and `Δw_i≥0` because the list is
descending. Hence every term of `(♦)` is `≥0`, so `D̃−1=\sum_iψ(c_i)Δw_i≥0`. ∎

This is a genuine, fully rigorous closure of a sub-region of Case B, and it is **equality-robust**:
if the merged order strictly alternates `T,B,T,B,…` (so `c_i∈\{0,1\}`) every `ψ(c_i)=0` and `D̃=1`
exactly — the extremal "zigzag" family. Two consequences pinned down numerically (`4·10⁵` residual
configs, `n=2..5`, `/tmp/round-4/scratch/tight.py`):

- **Every tight (`D̃=1`) configuration lies in the `maxc≤1` region** (of the near-tight `D̃<1.02`
  residual configs, `23058` had `maxc≤1` and only `3` had `maxc=2`, those already at `D̃≥1.017`).
  So Lemma T dispatches the entire equality-attaining core of GAP-LB′ — the part every earlier
  round found hardest.
- Configs with `maxc≥2` all satisfy `D̃≥1` with a strict margin (`min D̃≈1.017`).

*Worked equality check (residual example, `n=2`, `a=2`, `b=0`).* `Y=(2.64,1.32,0.04)` (sum `4=2^n`),
`Z=(2,1)`. Merged: `2.64T,2B,1.32T,1B,0.04T`, so `c=(1,0,1,0,1)`, `maxc=1`. Every `ψ(c_i)=0`, hence
by `(♦)` `D̃=1` exactly — matching the direct alternating sum `2.64−2+1.32−1+0.04=1`. This is one of
the two extremal cases flagged by the outline (strict-alternation-then-tail); Lemma T settles it.

### 5. The fully-unrolled recursive structure of `Z` (structural lemma)

Lemma T is a general fact about any merged order; it does **not** yet use `Z`'s origin. The residual
(`§6`) does. We record here the recursive cut-tree of `Z`, needed for the residual attack.

> **Structure Lemma.** Every `≤k`-cut response `Z` to the dyadic `S_k=\{1,…,2^k\}` decomposes as
> `Z = ⊎_{j=0}^{k} Y^{(j)}`, where `Y^{(j)}` is the set of fragments of the dyadic piece `2^{k−j}`
> (a partition of `2^{k−j}` into `a_j+1` positive parts), and `\sum_{j=0}^{k} a_j ≤ k`. Moreover for
> each `p`, the union `⊎_{j≥p}Y^{(j)}` is a `≤(k−p)`-cut response to the dyadic `S_{k−p}` (rescaled
> is unnecessary: it is literally a response to `\{1,…,2^{k−p}\}`).

**Proof.** A cut acts on one current part and never merges parts across the original dyadic pieces,
so the fragments partition into the `k+1` groups by which dyadic piece `2^{k−j}` they descend from;
`a_j` = number of cuts spent inside `2^{k−j}` gives `a_j+1` fragments, and `\sum_j a_j≤k` is the cut
budget. The pieces `\{2^{k−j}:j≥p\}=\{1,…,2^{k−p}\}` with their fragments and their `\sum_{j≥p}a_j≤k−p`
cuts are, by definition, a `≤(k−p)`-cut response to `S_{k−p}`. ∎

Applied to our `Z` (a `≤(n−1)`-cut response to `S_{n−1}`): `Z=⊎_{j=0}^{n−1}Y'^{(j)}`, its own top
group `Y'^{(0)}` being the fragments of `Z`'s top piece `2^{n−1}=θ`, and `⊎_{j≥1}Y'^{(j)}` a
`≤(n−2)`-cut response to `S_{n−2}` living in `(0,θ/2]`. This is the two-level (indeed multi-level)
recursion the residual argument must climb — the full multiset is
`F=Y⊎Z=Y^{(0)}⊎Y'^{(0)}⊎Y'^{(1)}⊎⋯`, one fragment-group per dyadic scale, total budget `≤n`. In
particular `Z`'s **top anchor** — the largest `Z`-part `z₁` — satisfies `z₁≥` (size of the largest
uncut dyadic piece of `Z`); when `Z`'s top piece `θ` is left uncut, `z₁=θ`, sitting at a **fixed**
height, and it is precisely such anchors that create the compensating negative-`c` excursions.

### 6. Residual GAP-LB′-run (open, precisely stated)

After Lemma T, the only open Case-B configurations are those whose merged descending order has
```
maxc := \max_i c_i ≥ 2 .                                                (residual)
```
There `(♦)` has strictly-negative terms `ψ(c_i)Δw_i` (on the intervals with `c_i≥2`), and Lemma T's
termwise argument fails. The exact open sub-claim is:
```
\sum_{i:\,c_i≥2} \big(c_i − 1[c_i\text{ odd}]\big)Δw_i  ≤  \sum_{i:\,c_i≤0}\big(1[c_i\text{ odd}]−c_i\big)Δw_i .   (GAP-LB′-run)
```
i.e. the **T-run deficit** (mass where top-fragments run `≥2` ahead) is dominated by the
**anchor surplus** (mass where `Z`-parts run ahead, `c_i≤0`).

**Why this needs `Z`'s cut-tree, and the mechanism.** The surplus terms have `c_i≤0`, meaning at
that height there are at least as many `Z`-parts as `Y`-parts above `t`; these are exactly the
heights guarded by `Z`'s dyadic anchors (`§5`). Concretely, when the merged order opens with a `B`
(the largest overall part is a `Z`-anchor `z₁≥` some uncut dyadic value, `>y₁`), the prefix has
`c_1=−1` over width `z₁−y₁>0`, contributing `+2(z₁−y₁)` to `(♦)` — a surplus of definite size set by
`Z`'s dyadic geometry, not by any scalar of `Z`. Example (`§`, `n=3`, `a=2`, `b=0`):
`Y=(3.242,2.672,2.085)`, `Z=(4,2,1)`, merged `4B,3.242T,2.672T,2.085T,2B,1B`, `c=(−1,0,1,2,1,0)`;
the single `c=2` deficit `−2·(2.085−2)=−0.17` is dwarfed by the opening `c=−1` surplus
`+2·(4−3.242)=+1.516` from the uncut anchor `4`, giving `D̃−1=1.345`. The residual claim is that
this domination is **universal** across the recursive tree; the natural proof is a two-level joint
induction: descend into `Z=Y'^{(0)}⊎(\text{response to }S_{n−2})` at threshold `θ/2` and match each
top-run against the anchors of the corresponding `Z`-subtree.

**What is NOT available (recorded dead ends, reconfirmed).** `(GAP-LB′-run)` is FALSE if `Z` is
replaced by an arbitrary multiset with the same `sum(Z)` and `altsum(Z)≥1` (probes 5–7); a T-run of
near-equal top values contributes almost `0` internal alternating mass, so only `Z`'s actual anchor
placement supplies the surplus. One-sided confinement of `O_Z` is REFUTED (`O_Z` reaches near `0`
already at `n=1`). Hence the residual must be closed **through** the Structure Lemma, never as a
free-standing bounded-multiset inequality.

*Numerics.* Over `4·10⁵` residual configs (`n≤5`), `(GAP-LB′-run)` held with `0` violations; the
`maxc≥2` infimum of `D̃` is `≈1.017` but the samples suggest the true infimum is `1` (approached),
so no non-tight slack estimate can substitute for the anchor-domination argument.

### 7. Tie-normalization: `D̃` is tie-break invariant; target the non-strict `D̃≥1` (NEW, PROVED)

The prefix imbalance `c_i` (§3) is order-dependent only at **exact ties** between a `Y`-value and a
`Z`-value: swapping two equal-valued adjacent parts leaves the sorted *value* sequence `w_1≥…≥w_m`
unchanged but changes their `T/B` labels' order, hence changes some `c_i`. However the quantity we
bound is `D̃`, and by Lemma G (level-measure form, certified) `D̃ = λ(O_F) = \sum_i (−1)^{i−1} w_i`
is the **value-only** alternating sum of the sorted list; it does **not** depend on how equal values
are ordered. Therefore:

> **Tie-invariance.** `D̃` is independent of the tie-break. Consequently the (♣)/(♦) machinery, and
> the increment identity (♠) below, may be evaluated with **any** fixed tie-break without changing
> `D̃`; we adopt the canonical **Y-before-Z** rule (at a `Y`–`Z` tie, the `Y`-part is listed first,
> i.e. gets the smaller position).

**Consequence for the residual.** Under Y-before-Z, a `Y`-fragment tying `Z`'s top anchor `θ`
(`y₁=θ`) is placed *above* it, so `c_1=+1` and a run to `c=2` can occur at an exact tie. The boundary
config `n=4, Y=(8,3,3,2), Z=(8,2,2,2,1)` (both from a legitimate `≤4`-cut Case-B response,
`a=3,b=1,a+b=4=n`) has value-only alternating sum `8−8+3−3+2−2+2−2+1 = 1`, i.e. `D̃=1` *attained*
inside `maxc≥2`. Hence the round-4 numerical claim "every `maxc≥2` config has strict slack ≈1.017"
was a finite-sampling artifact: the true infimum over `maxc≥2` is exactly `1`. **The residual target
is the non-strict `D̃≥1`, with equality tracked** — matching Lemma T's own equality-robustness
(strict alternation ⇒ `D̃=1`). We never assert a uniform strict margin.

### 8. Abel-summation increment identity `(♠)` — position-parity form (NEW, PROVED)

Apply summation by parts to `(♦)`. With `f_i:=ψ(c_i)`, `f_0:=ψ(c_0)=ψ(0)=0`, and `w_{m+1}=0`,
```
D̃ − 1 = \sum_{i=1}^m ψ(c_i)(w_i−w_{i+1}) = \sum_{i=1}^m (ψ(c_i)−ψ(c_{i−1}))\,w_i .
```
(The Abel step: `\sum_i f_i(w_i−w_{i+1}) = \sum_i f_i w_i − \sum_i f_i w_{i+1}
= \sum_i f_i w_i − \sum_{i≥2} f_{i−1} w_i = f_1 w_1 + \sum_{i≥2}(f_i−f_{i−1})w_i`, and `f_0=0`.)

Each step is `±1`: `c_i=c_{i−1}+1` (a `T`, i.e. `w_i∈Y`) or `c_i=c_{i−1}−1` (a `B`, `w_i∈Z`). Using
`ψ(c)=1[c\text{ odd}]−c` we compute the increments exactly. Write `c=c_{i−1}`:
- **T step** (`c→c+1`): `ψ(c+1)−ψ(c) = (1[c+1\text{ odd}]−1[c\text{ odd}]) − 1`. The parity term is
  `+1` if `c` even, `−1` if `c` odd; so the increment is `0` if `c` even, `−2` if `c` odd.
- **B step** (`c→c−1`): `ψ(c−1)−ψ(c) = (1[c−1\text{ odd}]−1[c\text{ odd}]) + 1`. The parity term is
  `+1` if `c` even, `−1` if `c` odd; so the increment is `+2` if `c` even, `0` if `c` odd.

Hence only two kinds of step contribute:
```
D̃ − 1 = 2\Big(\ \textstyle\sum_{\text{B step from even height}} w_i \ −\ \sum_{\text{T step from odd height}} w_i\ \Big).   (♠)
```
Now the **parity of the height equals the parity of the position**: among the `i−1` parts strictly
above `w_i` there are `#T` and `#B` with `#T+#B=i−1` and `c_{i−1}=#T−#B`, so
`c_{i−1}≡ i−1 \pmod 2`. Thus `c_{i−1}` even `⇔` `i` odd, and `c_{i−1}` odd `⇔` `i` even. A B-step from
even height is a `Z`-part at an **odd** position; a T-step from odd height is a `Y`-fragment at an
**even** position. Therefore `(♠)` is the **position-parity identity**
```
D̃ − 1 = 2\Big(\ \textstyle\sum_{z∈Z\ \text{at odd merged-position}} z\ −\ \sum_{y∈Y\ \text{at even merged-position}} y\ \Big).   (♠′)
```
*Verification.* On the run example (§6) `4B,3.242T,2.672T,2.085T,2B,1B`, the B-from-even steps are
`4B` (`c_0=0`) and `2B` (`c_4=2`), the T-from-odd steps are `3.242T` (`c_1=−1`) and `2.085T`
(`c_3=1`); `(♠)` gives `2(4+2−3.242−2.085)=2(0.673)=1.346=D̃−1`. Numerically `(♠′)` matches `D̃−1`
to `10^{−14}` over `2·10⁴` random Case-B splits. The Case-B goal `D̃≥1` is thus **exactly**
```
\sum_{z∈Z\ \text{odd-pos}} z \ \ge\ \sum_{y∈Y\ \text{even-pos}} y .   (♠≥0)
```

### 9. Self-contained combinatorial restatement (NEW, PROVED equivalent)

`D̃ = \sum_i(−1)^{i−1}w_i = O(F) − E(F)`, where `O(F)=\sum_{i\ \text{odd}}w_i` (odd-rank sum) and
`E(F)=\sum_{i\ \text{even}}w_i` (even-rank sum), and `O(F)+E(F)=\sum F=2^{n+1}−1`. Hence
`D̃≥1 ⇔ E(F) ≤ (2^{n+1}−2)/2 = 2^n−1 ⇔ O(F)≥2^n`. By the **Structure Lemma (§5)** any Case-B (or
Case-A) final multiset is a simultaneous refinement
```
F = \biguplus_{j=0}^{n} π_j,\qquad π_j = \text{a partition of } 2^{\,n−j}\text{ into } a_j+1 \text{ parts},\qquad \sum_{j=0}^n a_j ≤ n .
```
(Here `π_0=Y` is the top piece's fragments and `⊎_{j≥1}π_j = Z`.) So the **entire lower bound** is
the clean self-contained claim:

> **(GAP-L, restated).** For every simultaneous refinement `F=⊎_{j=0}^n π_j` of the dyadic
> `{1,2,…,2^n}` with total cut budget `\sum_j a_j ≤ n`, the even-rank sum satisfies
> `E(F) ≤ 2^n−1` (equivalently the odd-rank sum `O(F) ≥ 2^n`, equivalently `D̃≥1`).

*Numerics.* `\max\big(E(F)−(2^n−1)\big)=0` exactly, **attained**, over `2·10⁵` random configs
(`n≤5`, all `a,b`); `0` violations. This is the sharpest, most transparent form of the residual and
subsumes Cases A–B uniformly: Case A (`a_0=0`, top uncut) gives `O(F)≥2^n` immediately since the
uncut `2^n` is the unique largest part (rank 1, odd) — recovering the C3 domination bound.

### 10. The local anchor-matching mechanism is REFUTED (NEW dead end)

The outline's Step-5 mechanism ("match each maximal T-run against `Z`'s top anchor / its fragments,
width-weighted") is, in the `(♠′)` form, the assertion of a **value-dominating injection**
`μ:\{Y\text{ at even-pos}\}\hookrightarrow\{Z\text{ at odd-pos}\}` with `z_{μ(y)}≥y` (from which
`\sum_{Y\text{ even}}y≤\sum_{Z\text{ odd}}z` would follow). Equivalently, its width-weighted
(measure) form is the **survival-function domination**
`#\{z∈Z\text{ odd-pos}: z>τ\} ≥ #\{y∈Y\text{ even-pos}: y>τ\}` for all `τ`.

> **This is FALSE in general.** The survival domination **fails on `21%`** of Case-B configs
> (`42807/200000`, `n∈[3,5]`). Explicit witness (`n=5, a=1, b=1`): `Y=(17.9,14.1)`,
> `Z=(11.418,8,4.582,4,2,1)` (a `1`-cut of `Z`'s top `2^4=16` into `11.418+4.582`). Merged
> (Y-before-Z): `17.9Y,14.1Y,11.418Z,8Z,4.582Z,4Z,2Z,1Z`; the odd-position `Z`-parts are
> `Z_{odd}=(11.418,4.582,2)` and the even-position `Y`-parts are `Y_{even}=(14.1)`. Here the single
> `Y`-part `14.1` **exceeds every** `Z`-odd part (`\max Z_{odd}=11.418<14.1`), so no value/width
> dominating injection exists — yet `\sum Z_{odd}=18 > 14.1=\sum Y_{even}`, so `(♠≥0)` still holds.

**Conclusion (redirects the field).** The compensating surplus is supplied **globally** — a single
large `Y`-part at an even position is dominated by the **sum of several smaller `Z`-odd parts across
different dyadic scales**, not by one matched anchor. Therefore `(GAP-LB′-run)` **cannot** be closed
by any local (per-run / per-anchor) width-weighted domination, nor by a scalar/count summary of `Z`
(already refuted, probes 5–7). It must be proved as a **global sum inequality** through `Z`'s
recursive cut-tree. This kills the outline's proposed Step-5 matching and the near-duplicate
"budget-count runs vs anchors" if that count is read as a matching — see Spec concerns.

### 11. The honest open gap

After §7–§10, the residual `maxc≥2` is the single global inequality `(♠≥0)`, equivalently
`E(F)≤2^n−1` (§9). It is verified (`0` violations, tight infimum `1`) but **not proved**. What is
established rigorously toward it: (i) it is a non-strict, equality-attained bound (§7); (ii) it is
`\sum_{Z\text{ odd}}z≥\sum_{Y\text{ even}}y`, a global sum across scales (§8); (iii) it is **not** a
local matching (§10); (iv) it must route through the Structure-Lemma decomposition
`F=⊎_jπ_j` (§9), with the IH `D(Z)≥1` available one scale down. The remaining task is a genuinely
global argument (e.g. a potential summed over all scales, or an amortized charge that lets one
`Y`-even part draw on `Z`-odd mass from several scales at once). This is THE remaining GAP-L gap; it
is now sharper (three equivalent clean forms) and one plausible mechanism (local matching) is
eliminated.

### 12. Base cases and value algebra (imported, verified)
`P(0)`: one part of length `1`, `0` cuts, `D̃=1`. `n=1,2` fully solved in
`approaches/induction-recursion.md` (both bounds); `n=2,3` values verified (min `D̃=1`).

### 13. Threshold-split identity `(△)` and localized reduction (NEW round 7, PROVED)

This section installs an **exact** (equality, not inequality) refinement of `(★★)` that isolates the
open residual as a single localized inequality of *total mass `≤1`*, and records a further refuted
reserve shape. Throughout Case B: `θ:=2^{n−1}`, `F=Y⊎Z`, `Y`=fragments of the top piece `2^n=2θ`
(so `sum(Y)=2θ`, each `y≤2θ`), `Z`= a `≤(n−1)`-cut response to `S_{n−1}` (so `sum(Z)=2^n−1=2θ−1`,
each `z≤θ`). Write `y₁:=max Y`, `O_P:={t>0:N_P(t)\text{ odd}}`.

> **Lemma (Threshold-split identity `(△)`).**
> `D̃(F) = (y₁−θ)^+ + λ_{(0,θ)}\big(O_Y △ O_Z\big)`,
> where `λ_{(0,θ)}(\cdot)` is Lebesgue measure restricted to `(0,θ)`.

**Proof.** By Lemma G (level-measure form, certified) and `N_F=N_Y+N_Z`, parity of a sum is the XOR
of parities, so `1[N_F(t)\text{ odd}] = 1[t∈O_Y]⊕1[t∈O_Z] = 1[t∈O_Y△O_Z]`, hence
`D̃(F)=λ(O_Y△O_Z)` over `(0,∞)`. Split the axis at `θ`.

*On `(θ,∞)`.* Every part of `Z` is `≤θ`, so `N_Z(t)=0` and `O_Z∩(θ,∞)=∅`; thus
`(O_Y△O_Z)∩(θ,∞)=O_Y∩(θ,∞)`. Since `sum(Y)=2θ` and each `y≤2θ`, **at most one** part of `Y` exceeds
`θ` (two parts `>θ` would sum `>2θ`). Hence for `t>θ`, `N_Y(t)=1[y₁>t]∈\{0,1\}`, so
`O_Y∩(θ,∞)=(θ,y₁)` when `y₁>θ` and `∅` otherwise; its measure is `(y₁−θ)^+`.

*On `(0,θ)`.* Contributes exactly `λ_{(0,θ)}(O_Y△O_Z)`. Adding the two pieces gives `(△)`. ∎

*(This is the exact form of the round-3 half-total single-crosser bound `D̃≥(y₁−θ)^+` together with
the round-2 threshold decomposition `(★★)`; `(★★)` bounded the second term below by
`|D̃(Y)^{<θ}−D̃(Z)|`, whereas `(△)` keeps it as the exact symmetric-difference measure.)*

> **Localized reduction.** Put `β:=(y₁−θ)^+` and `M(t):=N_Y(t)−N_Z(t)` on `(0,θ)`. Then
> `∫_{(0,θ)}M\,dt = 1−β`, and the Case-B target `D̃(F)≥1` is **equivalent** to
> `λ_{(0,θ)}\{M\text{ odd}\} ≥ 1−β = ∫_{(0,θ)}M`.  `(△⋆)`

**Proof.** `∫_{(0,θ)}N_Y = \sum_{y}\min(y,θ) = 2θ − (y₁−θ)^+` (only `y₁` can exceed `θ`, and its
truncation at `θ` removes exactly `(y₁−θ)^+`); `∫_{(0,θ)}N_Z = \sum_z z = 2θ−1` (all `z≤θ`). Subtract:
`∫_{(0,θ)}M = 1−β`. And `O_Y△O_Z = \{t:N_Y,N_Z\text{ opposite parity}\}=\{M\text{ odd}\}`. Substituting
into `(△)`: `D̃(F)=β+λ_{(0,θ)}\{M\text{ odd}\}`, so `D̃≥1 ⟺ λ_{(0,θ)}\{M\text{ odd}\}≥1−β`. Since
`1−β=∫_{(0,θ)}M`, this is `(△⋆)`. ∎

**What `(△⋆)` buys.** The residual is now a copy of `(♣)` on the *bounded* window `(0,θ)` whose
right-hand mass is `∫M=1−β∈(0,1]` — at most `1`, and small when `y₁` is near `θ`. The obstruction is
unchanged in kind (positive excursions `M≥2` can make `1[M\text{ odd}]<M`), but the required surplus
is now capped at `1`. Numerics (`0/2·10⁵`, `n≤6`) confirm both `(△)` and `(△⋆)`.

### 14. A further reserve shape is refuted; the surplus is bottom-inclusive (NEW round 7)

The outline's IH shape `P*(n)` carries a *top-down* reserve of `Z` (surplus banked **above** a
threshold `τ`, e.g. `R_Z(τ)=λ\{t>τ:c_i(Z)≤−1\}`). The cleanest such reserve — "`Z`'s odd-level
measure leads its even-level measure from the top,"
`λ\{t>τ:N_Z(t)\text{ odd}\} ≥ λ\{t>τ:N_Z(t)\text{ even},N_Z(t)>0\}` for all `τ≥0` — is **FALSE**:
`7306/4·10⁵` random dyadic responses `Z` violate it (worst deficit `−22.5`). So `Z` does **not** keep
its discrepancy surplus in a high tail that a descending induction could hand down.

**Where the surplus actually lives (worked tie config).** `n=4`, `θ=8`, `Y=(8,3,3,2)`
(`sum 16=2θ`, `β=0`), `Z=(8,2,2,2,1)` (`sum 15`; the `2^3=8` piece is **uncut**, so this is
"Case (a)"). By `(△)`, `D̃=0+λ_{(0,8)}(O_Y△O_Z)`. Compute: `N_Y`: `4` on `(0,2)`, `3` on `(2,3)`, `1`
on `(3,8)`; so `O_Y∩(0,8)=(2,8)`. `N_Z`: `5` on `(0,1)`, `4` on `(1,2)`, `1` on `(2,8)`; so
`O_Z∩(0,8)=(0,1)∪(2,8)`. Hence `O_Y△O_Z=(0,1)`, and `D̃=1` (matching the direct alternating sum).
The **entire** surplus is the near-`0` band `(0,1)`: there `N_Z=5` (odd) while `N_Y=4` (even), a pure
*parity-of-part-count* effect (`|Z|=5>|Y|=4`). The top anchor `z₁=8=θ` lies in **both** `O_Y` and
`O_Z` on `(2,8)` and **cancels** in the symmetric difference — it does *not* itself supply surplus.

**Consequence (redirects the residual attack).** The compensation for a T-run deficit is supplied
**globally and bottom-inclusively** — it can be entirely a near-`0` count-parity band — not by a
top-anchor reserve of `Z`. This refutes the specific top-down `R_Z(τ)` reserve shape the outline
proposed (Step 5 mechanism), consistent with §10's refutation of the local width-dominating
injection. The residual `(△⋆)`/`(♠≥0)`/`E(F)≤2^n−1` remains the honest open gap; both a *scalar
summary of `Z`* (refuted, §2 note) and a *top-down reserve of `Z`* (refuted here) are now ruled out.
The live candidate mechanism is a **joint count-parity / global amortization across all dyadic
scales** (the near-0 band shows the balancing part-count `|Y|` vs `|Z|` and its scale-by-scale
refinement is load-bearing), routed through the Structure Lemma (§5) — not a match, not a scalar, not
a one-sided reserve.

### 15. The greedy bounded-window nonneg-block TILING is refuted as a local certificate (NEW round 8)

The round-8 assignment was to close `(♦≥0)` `Σ_iψ(c_i)Δw_i≥0` by the crux-aimo-0626 device: partition
the merged index set `{1,…,m}` into consecutive blocks `B_1,…,B_r` with each block-sum
`Σ_{i∈B_t}ψ(c_i)Δw_i≥0`, and sum. We record the three findings that settle its status.

**(15a) A consecutive-nonneg-block tiling exists iff the total is `≥0` (so the device is circular).**
Write `s_i:=ψ(c_i)Δw_i` and `P_i:=s_1+⋯+s_i`, `P_0:=0`. A partition into consecutive blocks with cut
points `0=i_0<i_1<⋯<i_r=m` has all block-sums `≥0` iff `P_{i_0}≤P_{i_1}≤⋯≤P_{i_r}`. The single-block
choice `r=1`, `[1,m]`, has block-sum `P_m=Σs_i`, which is `≥0` **iff** `Σs_i≥0`. Hence "a nonneg
consecutive-block tiling exists" is **logically equivalent** to the target `Σs_i≥0`; producing such a
tiling proves nothing that the total does not already give. The device has content **only** if each
block's nonnegativity is certified **locally** (by a bounded window whose sign is forced without
knowing the global total), exactly the aimo-0626 setting (windows of length `≤m`, each certified in
isolation). We show that local certification is impossible here.

**(15b) No one-sided or bounded-window local certificate exists (both-directional greedy fails).**
Run the aimo-0626 greedy: at the leftmost uncovered index emit the *shortest* forward window of
nonneg sum (forward tiling), or symmetrically the shortest backward window (backward tiling). Over
`2·10⁵` residual (`maxc≥2`) Case-B configs (`n≤6`): forward greedy fails on `28298`, backward on
`10049`, and **both** fail simultaneously on `222`. The minimal both-fail witness is

> `n=3`, `Y=(3.382,2.553,2.065)` (partition of `2^3=8`, `a_0=2` cuts), `Z=(4,\;1.042,0.958,\;1)` (the
> `2^2` piece uncut, the `2^1` piece cut once into `1.042+0.958`, the `2^0` piece uncut; `Z`-budget
> `1`, total budget `3=n`), giving merged (Y-before-Z) list
> `4B,\,3.382T,\,2.553T,\,2.065T,\,1.042B,\,1B,\,0.958B` with `c=(−1,0,1,2,1,0,−1)` and
> `s=(+1.237,0,0,−2.046,0,0,+1.916)`, `D̃=2.107`.

Here the **sole** deficit term is `s_4=−2.046` (at `c_4=2`). Its only two nonzero neighbours are the
surpluses `s_1=+1.237` (left) and `s_7=+1.916` (right), and **each is strictly smaller than the
deficit** (`1.237<2.046` and `1.916<2.046`). Therefore **no** window lying entirely on one side of
index `4`, and **no** window omitting either surplus, can have nonneg sum containing the deficit; the
*only* nonneg window covering index `4` is the full `[1,7]` (`1.237−2.046+1.916=1.107≥0`). A bounded
or one-directional greedy can never assemble it. This is the direction trap in its sharpest form: the
compensating surplus for a single deficit is **split across both sides** and must be gathered
simultaneously, so the certifying "block" is the whole list — i.e. non-local. Combined with (15a),
the tiling device collapses to the global inequality and adds nothing.

**(15c) Budget-height lemma (bounds excursion height, not window length).**
> **Lemma H.** In the merged descending list of `F=Y⊎Z`, `max_i c_i ≤ |Y| = a_0+1`.

**Proof.** `c_i=#\{Y\text{-parts among }w_1,…,w_i\}−#\{Z\text{-parts among }w_1,…,w_i\}≤#\{Y\text{-parts}
\}=|Y|=a_0+1`, since the negative count is `≥0`. ∎ (Verified `0/10⁵`.) By the Structure Lemma (§5)
`a_0≤n`, so `maxc≤n+1`. This caps the *height* of the lattice path (hence the per-term deficit
magnitude `|ψ(c_i)|≤c_i≤n+1`), but it does **not** bound the *length* of the compensating window nor
force any block-sum sign — as (15b) shows, a single depth-`2` excursion already needs a full-list
window. So Lemma H does not localize the certificate; it is recorded as a true structural bound.

**(15d) All measure/layer/position-parity forms are pure restatements of `D̃≥1`.**
Using the layer decomposition of the integer profile `M` (`A_j:=\{M≥j\}`, `B_j:=\{M≤−j\}`): since
`Σ_{k≥1}1[M≥2k]=⌊M^+/2⌋` and `Σ_{k≥1}1[M≤−(2k−1)]=⌈M^-/2⌉`, and
`⌊M^+/2⌋=M^+/2−½·1[M^+\text{ odd}]`, `⌈M^-/2⌉=M^-/2+½·1[M^-\text{ odd}]`, we get exactly
```
∫\big(⌊M^+/2⌋−⌈M^-/2⌉\big)dt = ½∫M − ½∫1[M\text{ odd}] = ½·1 − ½·D̃ = ½ − ½D̃ .   (△△)
```
(Verified to `10^{−6}`, `0/10⁵`.) Hence the summed-layer form `Σ_kλ(A_{2k})≤Σ_kλ(B_{2k-1})`, the
position-parity `(♠≥0)`, and the localized `(△⋆)` are **all** algebraically equivalent to `D̃≥1`; each
is obtained from the level-measure identity by measure bookkeeping alone and **injects no dyadic or
budget hypothesis**. The trivial bound `⌊M^+/2⌋≤M^+/2`, `⌈M^-/2⌉≥M^-/2` gives only
`∫(⌊M^+/2⌋−⌈M^-/2⌉)≤½∫M=½`, i.e. `D̃≥0` — off by the same `½` as `O(F)≥S/2` (the sorted-multiset
`w_{2i-1}≥w_{2i}` fact). **Conclusion:** the residual `½` — precisely the equality-attaining content —
cannot be recovered by any manipulation of the profile `M` in isolation; it must come from the
**dyadic budget constraint** `Σa_j≤n` entering *non-locally*. The tiling device (a reshuffle of the
same profile) is therefore structurally incapable of supplying it. The honest gap stands; this round
**eliminates the bounded-window tiling family** and pins that the closure must be a non-local
argument that uses the dyadic structure, not a block/window certificate on the merged order.

## Cases to cover — status
- Base `n=0,1`, Case A: done.
- Case B on `{y₁≥2^{n−1}+1}` `(◇◇)`, on `{|D_top^<−D_bot|≥1−D_top^>}` `(★★)`, and on the whole
  `maxc≤1` region (**Lemma T, new**, incl. all tight configs): done.
- Case B tie boundary `y₁=θ` (exact ties): **done** (§7) — `D̃` tie-invariant, boundary folds into
  `maxc≥2` with `D̃=1` attained; target is non-strict `D̃≥1`.
- Case B residual `maxc≥2` (`(♠≥0)` ⇔ `E(F)≤2^n−1` ⇔ `(△⋆)` `λ_{(0,θ)}\{M\text{ odd}\}≥1−β`):
  **open**, now sharpened to a **bounded-mass localized** inequality on `(0,θ)` (§13). The *local*
  anchor-matching closure is **refuted** (§10), the *top-down reserve* IH shape is **refuted**
  (§14, surplus is bottom-inclusive/near-0), and the **greedy bounded-window nonneg-block tiling**
  (crux aimo-0626) is **refuted as a local certificate** (§15, round 8): the tiling is equivalent to
  the total and has no bounded-window local certificate (a single deficit needs both-sided surplus),
  and all measure forms are pure restatements of `D̃≥1`. Must route through `Z`'s cut-tree by a
  global argument that injects the dyadic budget `Σa_j≤n` **non-locally** (non-matching, non-scalar,
  non-top-reserve, non-tiling).
- Upper bound (GAP-UB): out of scope for this slug (owned by the dyadic-discrepancy twins).

## Spec concerns
The assigned outline's **Step 5** ("match each maximal T-run against `Z`'s top anchor / its
`Y'^{(0)}` fragments, **width-weighted**") is **refuted as stated** (§10): a value/width-dominating
injection `{Y even-pos}→{Z odd-pos}` does not exist — the survival-function (measure) domination
fails on `21%` of Case-B configs; the compensation is a **global sum across dyadic scales**, not a
per-anchor match. The outline's caveat "width-weighted, not count-weighted" does **not** rescue it —
the width/measure version is exactly what fails. This also flags a shared-wall risk for the sibling
`induction-recursion` (budget-count) slug: if its Step-4 "pair each T-run's width against the width
to the next `Z`-anchor above it" is read as a per-run pairing, it hits the same refutation. Both
GAP-L slugs must target the **global** inequality `(♠≥0)`/`E(F)≤2^n−1` (§8–§9), not a local pairing.
Recommendation to the outliner: next round, replace the "match each run to an anchor" phrasing with a
**global potential/amortized-charge** framing (one `Y`-even part may draw on `Z`-odd mass from
several scales), or seed a genuinely different framing for the residual per the plateau rule.

**Round-8 Spec concern (assigned tiling mechanism refuted).** The round-8 assignment — greedy
bounded-window nonneg-block **tiling** (crux aimo-0626) — does **not** close GAP L and cannot as a
local certificate (§15). Two structural reasons, both rigorous: (1) a consecutive-nonneg-block tiling
of `Σψ(c_i)Δw_i` exists **iff** the total is `≥0`, so producing a tiling is logically equivalent to
the target — the device is only non-trivial if blocks are certified by *bounded local windows*, and
(2) bounded local windows provably do not exist here (a single depth-`2` excursion can need a
full-list window; both-directional greedy fails `222/2·10⁵`). The budget bound `maxc≤a_0+1` (Lemma H)
caps excursion **height** but not window length, and every layer/summed/`(♠)`/`(△⋆)` form is a pure
measure-algebra restatement of `D̃≥1` (identity `(△△)`). So the tiling family joins matching (§10),
scalar-summary (§2), and top-reserve (§14) as refuted. **Recommendation:** retire the merged-order
block/window/matching family for this residual; the live routes are the *sequential exact-toggle
amortized monovariant* (sibling `cut-sequence-potential`) and the *static scale-graded double-count*
(sibling `even-rank-doublecount`), both of which can in principle inject `Σa_j≤n` non-locally, which
`(△△)`/§15 show is exactly what the merged-order measure forms cannot do.

## Full proof
Not present — Status is `partial`. The lower bound is complete except for the Case-B residual, now
reduced to the single global inequality `(♠≥0)` ⇔ `E(F)≤2^n−1` (§8–§9, §11); the tight/equality core
is closed by Lemma T (§4), the tie boundary is normalized (§7), and the local-matching closure is
refuted (§10).

## Promotable lemmas
- **Budget-height Lemma H (NEW round 8, fully proved, §15c).** In the merged descending list of
  `F=Y⊎Z`, `max_i c_i ≤ |Y|`. Trivial but useful structural cap on excursion height. Verified `0/10⁵`.
- **Layer-restatement identity `(△△)` (NEW round 8, fully proved, §15d).** For the integer profile
  `M=N_Y−N_Z`, `∫(⌊M^+/2⌋−⌈M^-/2⌉)dt = ½∫M − ½D(F)`. Shows every layer/summed/`(♠)`/`(△⋆)` form is a
  pure measure-algebra restatement of `D≥1`; the trivial layer bound gives only `D≥0` (off by the
  same `½` as `O≥S/2`). Verified `0/10⁵`. (Records that the dyadic budget must enter non-locally.)
- **(Refutation, worth caching) No local nonneg-block tiling certificate for `(♦≥0)` (NEW round 8,
  §15a–b).** A consecutive-nonneg-block tiling of `Σψ(c_i)Δw_i` exists **iff** the total is `≥0` (take
  `[1,m]`), so the tiling device is equivalent to the target; and it has **no** bounded/one-sided
  local certificate — a single deficit run can exceed every individual adjacent surplus, needing a
  full-list window (minimal witness `n=3,Y=(3.382,2.553,2.065),Z=(4,1.042,1,0.958)`; both-directional
  greedy fails `222/2·10⁵`). Future rounds must not attempt to close the residual by a merged-order
  block/window tiling (crux aimo-0626 is circular here).
- **Threshold-split identity `(△)` (NEW round 7, fully proved, §13).** For a split `F=Y⊎Z` where
  `sum(Y)=2θ`, every `y≤2θ`, every `z≤θ`: `D(F) = (max Y − θ)^+ + λ_{(0,θ)}(O_Y △ O_Z)`. Exact
  refinement of `(★★)`; reduces the lower-bound residual to the bounded-mass localized inequality
  `λ_{(0,θ)}\{N_Y−N_Z\text{ odd}\} ≥ ∫_{(0,θ)}(N_Y−N_Z)`. Verified `0/2·10⁵`. (Good `lemmas/` candidate.)
- **Abel increment / position-parity identity `(♠)`/`(♠′)` (NEW, fully proved, §8).** For any labelled
  split `F=Y⊎Z` sorted descending, `D(F) − (sum(Y)−sum(Z)) = 2\big(\sum_{z∈Z\text{ at odd merged-pos}}z
  − \sum_{y∈Y\text{ at even merged-pos}}y\big)`, because the running imbalance parity equals the merged
  position parity. Equivalently `D(F)=O(F)−E(F)` with `E(F)` the even-rank sum. Verified to `10^{−14}`.
  A clean, reusable restatement of the merged-order signed sum. (Good `lemmas/` candidate; pairs with
  certified `termwise-lattice.md`.)
- **Tie-invariance of `D` (NEW, §7).** `D(F)=\sum_i(−1)^{i−1}w_i` is the value-only alternating sum,
  independent of tie-break; the `(♣)/(♦)/(♠)` machinery may use any tie-break. Resolves the exact-tie
  precision issue; target is the non-strict `D̃≥1` with equality attained at ties.
- **(Refutation, worth caching) No local domination for `(♠≥0)` (NEW, §10).** The value/width-dominating
  injection `{Y even-pos}→{Z odd-pos}` does not exist in general (survival domination fails on 21% of
  Case-B configs; explicit witness `n=5,Y=(17.9,14.1),Z=(11.418,8,4.582,4,2,1)`). Future rounds must
  not attempt to close the residual by a per-run/per-anchor match.
- **Exact-difference reformulation `(♣)` + merged-order lattice identity `(♦)` (NEW, fully proved).**
  For `F=Y⊎Z` with `sum(Y)−sum(Z)=Δ`, setting `M=N_Y−N_Z`: `D(F)=∫1[M odd]`, `∫M=Δ`, and along the
  merged descending order with prefix imbalance `c_i`, `D(F)−Δ=\sum_iψ(c_i)Δw_i`, `ψ(c)=1[c odd]−c`.
  Proved in §2–§3. Reusable for any top/bottom split. (Good `lemmas/` candidate.)
- **Termwise Lattice Lemma T (NEW, fully proved).** If the merged descending order of `Y⊎Z` has
  `#T−#B ≤ 1` in every prefix, then `D(Y⊎Z) ≥ sum(Y)−sum(Z)`. Proved in §4; equality-robust
  (strict alternation ⇒ equality). Closes the tight core of GAP-LB′. (Good `lemmas/` candidate.)
- **Structure Lemma (recursive cut-tree of a dyadic response) (NEW, fully proved).** Every `≤k`-cut
  response to `S_k` decomposes as `⊎_j Y^{(j)}` (fragments of `2^{k−j}`, `\sum a_j≤k`), with each
  upper union `⊎_{j≥p}Y^{(j)}` a `≤(k−p)`-cut response to `S_{k−p}`. Proved in §5. Provides the
  anchors the residual argument needs. (Good `lemmas/` candidate.)
- (carried) Lemma G, Level-Measure Formula, Cut-Flip, threshold decomposition `(★)(★★)`,
  half-total single-crosser `(◇◇)` — already certified / in `induction-recursion.md`.
