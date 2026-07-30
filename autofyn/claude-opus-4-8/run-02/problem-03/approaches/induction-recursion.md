# Approach: induction-recursion (self-similar minimax recursion on n)

## Status
partial

## Approaches tried
- **(round 7 build — GAP L, budget-count, pushed to wall + one negative result)** Drove the
  budget-count mechanism on `(GOAL)` `O_B≥E_A`. Re-verified `(B1)`–`(B3)` (identity error `3·10⁻¹⁵`;
  tie config `D̃=1`, `O_B=E_A=1`). New this round (§5E): **(E1)** the natural **termwise** closure
  `|A_{2j}|≤|B_{2j−1}|` is **FALSE** — explicit witness `n=4,a=2,b=2`, `Y=(7.936,7.174,0.890)`,
  `Z=(4,3.478,2.769,2,1.754,1)` has `|A_2|≈3.17>|B_1|≈2.77` yet `O_B≈4.52≥E_A≈3.17`; hundreds of such
  configs, aggregate always holds. So `(GOAL)` is irreducibly aggregate — no monotone super-level
  pairing can prove it (kills the most natural budget-count sub-route). **(E2)** the `b=0` slice
  (top budget only, `Z` uncut dyadic) has genuine slack (`min D̃(maxc≥2)≥1.029`, up to `1.486` at
  `n=5`), so the tight `maxc≥2` infimum-`1` boundary lives **only** at `b≥1` near-tie configs. A
  clean `b=0` closure was attempted but not completed (dyadic gives only upper bounds `a_ℓ≤y_ℓ`,
  `b_ℓ≤z_ℓ`; `O_B` needs a lower bound on `b_odd`). **(E3)** ESCALATION FLAG: the budget-count route
  is now at the same `(GOAL)` wall as telescope's Step-5, and the termwise variant is refuted — per
  the reviewer's short-leash note, GAP L needs a genuinely different framing next round, not a fourth
  attack on `O_B≥E_A`. → **partial** (no gap closed; one natural sub-route provably killed, tight
  slice isolated to `b≥1` near-tie, wall confirmed shared — recommend reframe).
- **(round 6 build — GAP L, budget-count REPOINT; exchange route retired)** Swapped the dead
  exchange/`|h|≤1` mechanism for a **global super-level count** on the certified merged-order signed
  sum `(♦)`. Three fully rigorous new results (§5D), all numerically confirmed (0 violations,
  10⁵–2·10⁵ configs, `n=2..6`, with the corrected `gen_Z` generator):
  (1) **Super-level reduction (NEW, fully proved).** Writing `M:=N_Y−N_Z`, `A_k:={M≥k}`,
  `B_k:={M≤−k}`, the exact identity `ψ(c)=−2⌊c⁺/2⌋+2⌈c⁻/2⌉` turns `(♦)` into
  `D̃−1 = 2( Σ_{j≥1}|B_{2j−1}| − Σ_{j≥1}|A_{2j}| )`. Hence the ENTIRE Case-B target `D̃≥1` is the
  single clean **super-level inequality** `O_B ≥ E_A`, where `O_B:=Σ_j|B_{2j−1}|` (odd negative
  super-levels = anchor surplus) and `E_A:=Σ_j|A_{2j}|` (even positive super-levels = T-run deficit).
  This is a structure-free restatement strictly cleaner than `(♦)` itself.
  (2) **Deficit budget + localization (NEW, fully proved).** `A_{2j}⊆{N_Y≥2j}`, so `|A_{2j}|≤y_{2j}`
  (the `2j`-th largest `Y`-fragment), giving `E_A ≤ y₂+y₄+y₆+⋯`. Moreover `y₂≤θ` (since
  `2θ=ΣY≥y₁+y₂≥2y₂`), so the **whole deficit is supported on `(0,y₂)⊆(0,θ)`** — no deficit above the
  half-threshold `θ=2^{n−1}`. This is the "run peak ≤ top budget" cap made exact and width-aware.
  (3) **Conservation identity (NEW, fully proved).** `∫_θ^∞ M = (y₁−θ)⁺=:δ` (at most one `Y`-part
  `>θ`, no `Z` above `θ`), and `∫_0^∞ M=1`, so `∫_0^θ M = 1−δ`: deficit and surplus both live below
  `θ` and their signed total there is pinned to `1−δ`.
  **What is NOT closed (honest):** the width-weighted domination `O_B ≥ E_A` itself — the deficit
  budget `E_A≤Σy_{2j}` is provably too weak (at the tie config `n=4,Y=(8,3,3,2),Z=(8,2,2,2,1)`,
  `E_A=1` but `Σy_{2j}=5`, while `O_B=1`), so the surplus must be lower-bounded through `Z`'s anchor
  placement (Structure Lemma), NOT a scalar/count of `Z`. As the outline-reviewer predicted, this
  target inequality **coincides** with the telescope twin's Step-5 wall — the two GAP-L mechanisms
  share it. The super-level reduction sharpens the wall to a pure width-count but does not breach it.
  → **partial** (clean super-level reduction + deficit budget/localization + conservation proved;
  the anchor-surplus lower bound is the isolated remaining gap, shared with telescope).
- **(round 4 build — GAP L, exchange/degenerate-boundary route)** Installed the **clean
  difference-function reformulation** of GAP-LB′ and proved two rigorous new results, but the
  exchange-to-`a−1` mechanism as specified is **provably obstructed** on part of the region, so the
  residual is sharpened, not closed. Concretely (integer units, `F=Y⊎Z`, `θ=2^{n−1}`,
  `ΣY=2^n=2θ`, `ΣZ=2θ−1`):
  (i) **Difference-function form.** With `h(t):=N_Y(t)−N_Z(t)` (`N_Y,N_Z`=count functions), the
  level-measure identity gives `D̃ = λ{t:h(t) odd}` and, since `∫₀^∞ h = ΣY−ΣZ = 1` **identically**,
  the target is `λ{h odd} ≥ ∫h = 1`. (ii) **Sufficient Lemma (proved, §5C):** if `|h(t)|≤1` a.e.
  then `D̃ = λ{|h|=1} ≥ ∫h = 1` — a clean, equality-robust closure whenever `Y` tracks `Z` within one
  level. Verified: 0 violations / 41814 `|h|≤1` configs. (iii) **Compactness + gradient (proved):**
  `min_Y D̃(Y⊎Z)` is attained (piecewise-linear on a compact simplex) and `∂D̃/∂y_j = 2·1[M_{−j}(y_j)
  even]−1 = ±1` where `M_{−j}(y_j)=#{other parts > y_j}`; at a minimizer, moving the smallest
  fragment down against a matched partner has directional derivative `0` (a value-preserving
  exchange). (iv) **The decisive obstruction (proved, and it kills the naive route):** when Xiang
  spends `b` bottom cuts, `Z` has `n+b` parts, so near `t=0`, `N_Z(0)=n+b` while `N_Y(0)=a+1≤n−b+1`;
  hence `h(0) ≤ −(2b−1)`, i.e. for **`b≥2` a negative excursion `|h|≥3` near `0` is FORCED** — `Y`
  simply lacks the fragments to track `Z` within one level. So `|h|≤1` is **unattainable** for `b≥2`,
  the `a→a−1` exchange **cannot** drive to a `|h|≤1`/Case-A config, and (matching the explorer's
  refutation) closing the residual genuinely requires `Z`'s **recursive cut-structure near `0`**, not
  any scalar or count summary. Numerics (build5): at min_Y, `max(N_Y−N_Z)=2` and `min(N_Y−N_Z)=−3`
  for `b≥1`, confirming both signs of `|h|≥2`. **Net:** the exchange route cleanly closes exactly the
  `|h|≤1`-attainable regime (all `b=0` configs empirically, and it is a per-config certificate) and
  reduces the rest to the same near-`0` `Z`-structure wall as the telescope twin. → **partial**
  (clean reformulation + Sufficient Lemma + exchange gradient proved; the doubly-balanced `b≥2`
  near-`0` excursion is the precise irreducible residual — NOT closable by the exchange alone).
- **(round 3 build — GAP L)** Added the **threshold-domination refinement** to Case B: in the
  integer-unit `n`-dyadic, since the top-descendants `Y` sum to exactly `2^n = 2θ` (`θ:=2^{n−1}`),
  **at most one** `Y`-part can exceed `θ`, so on `(θ,∞)` the level function `N=N_Y∈{0,1}` and the
  contribution is *exactly* `λ(O∩(θ,∞)) = (y₁−θ)⁺` (`y₁`=largest top-descendant). Hence
  `D̃ ≥ (y₁−θ)⁺`, which **closes the whole sub-region `y₁ ≥ 2^{n−1}+1`** cleanly — no cancellation
  term at all. Combined with the round-2 bound (★★), Case B is now closed on
  `{y₁ ≥ θ+1} ∪ {|D_top^< − D_bot| ≥ 1}`. Verified: 0 violations of "≤1 top part > θ",
  `λ(O∩(θ,∞))=(y₁−θ)⁺`, `D̃≥(y₁−θ)⁺`, and `D̃≥1` over 2·10⁵ random Case-B configs (n=2..6).
  **Also ruled out a tempting closing route:** the "confine `O` to a high region" strengthened IH is
  FALSE — already at n=1 (cut the `2` into `x,2−x`) the odd-set reaches `(0,x)` near 0, so `O` is not
  high-confined; only `λ(O)` is controlled, confirming the residual genuinely needs the *joint*
  overlap/interleaving bound, not a location-confinement invariant. **Residual GAP-LB′ unchanged and
  still open** (balanced region `y₁<θ+1` and `|D_top^<−D_bot|<1`): needs
  `2λ(O_Y^<∩O_Z) ≤ D_top^<+D_bot+D_top^>−1`. → **partial** (sub-region enlarged, residual sharpened
  and a dead route eliminated; the value `D̃=1` still verified tight n=2,3).
- (new, round 1) Prove the value by induction on n via a clean recursion, reducing the
  n-game to the (n−1)-game. No prior verdict.
- **(round 2 build — GAP L)** Replaced the REFUTED strict bound `W(n−1,b)>u_{n−1}` with an
  **exact-value recursion in integer units**. Rescaling by `1/u_n` turns Liu's dyadic into the
  integer weights `{1,2,4,…,2^n}` (total `2^{n+1}−1`), the bottom block into the *literal*
  `(n−1)`-dyadic `{1,…,2^{n−1}}` (no scaling factor), and the target `D≥u_n` into `D̃≥1`. In
  these units the minimax value `f(n,k):=min_{≤k cuts} D̃` obeys the clean **exact recursion
  `f(n,k)=f(n−1,k−1)` for `k≥1`**, hence `f(n,k)=f_{n−k}` with `f_m=(2^{m+1}+(−1)^m)/3`, and in
  particular `f(n,n)=f_0=1` (⇔ `D*=u_n`). Verified by exhaustive-allocation + Nelder–Mead:
  `f(n,k)` table matches for n≤3. **Proved rigorously this round:** base `n=0`; Case A (top
  uncut) `D̃≥1`; the **exact Case-B decomposition** `D̃ = D_top^> + D_top^< + D_bot − 2λ(O_Y^<∩O_Z)`
  at threshold `θ=2^{n−1}`, with `D_bot≥1` by IH; and the bound **`D̃ ≥ D_top^> + |D_top^< − D_bot|`
  (★★)**, which gives `D̃≥1` on the whole region `|D_top^< − D_bot| ≥ 1` (≈85% of random Case-B
  configs; includes the balanced-halves top-cut `a=1`, and every config with `D_top^<` small).
  **Residual GAP-LB′ (open, precisely stated):** the *balanced* region `|D_top^<−D_bot|<1` with
  near-complete overlap `λ(O_Y^<∩O_Z)`, where (★★) drops below 1 (true `D̃` still `=1`). Needs a
  joint structural bound on `λ(O_Y^<∩O_Z)` (the location of the bottom's odd-set inside the top's),
  not obtainable from `D_bot≥1` alone. → **partial** (real advance; strict-bound dead end removed,
  clean value-recursion installed, Case B ~85% closed).
- (round 1 build) Reformulated the whole game as a **discrepancy minimax** with a clean
  *level-measure formula* `D = λ{t : #(pieces>t) is odd}`, and a **cut-flip lemma**
  (each cut flips the parity of `N(t)` on `[0,x)∪(ℓ−x,ℓ)`). This turned the induction into
  a self-similar top/bottom split. Outcome: **Lemma G, the measure formula, the cut-flip
  lemma, the reduction to `minimax D = u`, and the lower-bound Case A are fully proved.**
  The naive bisection-only upper bound is **refuted** (Lemma SD is false for n≥2, verified
  numerically). Lower-bound Case B (parity cancellation between the top and bottom blocks
  under a shared cut budget) and the true upper bound remain open gaps. → **partial**.

## Current best

The problem is **exactly** reduced to a one-parameter discrepancy game, via three fully
proved lemmas (Lemma G, the Level-Measure Formula, the Cut-Flip Lemma). In the reduced
game Liu's payoff is `(1+D)/2` where
`D = λ{ t>0 : N(t):=#(final pieces of length > t) is odd }`,
and the target `c(n)=2^n/(2^{n+1}−1)` is equivalent to the discrepancy minimax `D* = u`,
with `u = u_n := 1/(2^{n+1}−1)`. Liu forces `D ≥ u` (lower), Xiang forces `D ≤ u` (upper).

- **Lower bound, Case A (top piece left uncut) — proved.** With Liu's dyadic partition
  `{2^k u}_{k=0}^n`, if Xiang never cuts the top piece `g=2^n u=(1+u)/2>1/2`, then the
  largest final piece equals `g`, so Liu's total `≥ g = (1+u)/2`, i.e. `D ≥ u`.
- **Lower bound, Case B (top piece cut) — enlarged closed region (round 3), one precise residual.**
  In the **integer-unit normalization** (Liu = `{1,2,…,2^n}`, bottom block = literal
  `(n−1)`-dyadic, target `D̃≥1`). Proved: base, Case A, the exact threshold decomposition
  `D̃ = D_top^> + D_top^< + D_bot − 2λ(O_Y^<∩O_Z)` with `D_bot≥1` (IH); the **threshold-domination
  refinement `D_top^> = λ(O∩(θ,∞)) = (y₁−θ)⁺`** (at most one top-descendant exceeds `θ=2^{n−1}` since
  `Y` sums to `2θ`), giving `D̃ ≥ (y₁−θ)⁺` and hence **`D̃≥1` on `{y₁ ≥ 2^{n−1}+1}`**; and the bound
  **`D̃ ≥ D_top^> + |D_top^< − D_bot|` (★★)**, giving `D̃≥1` on `{|D_top^<−D_bot| ≥ 1−D_top^>}`.
  **Residual GAP-LB′ (round-4 sharpening):** In the difference-function form (§5C) with
  `h:=N_Y−N_Z`, `∫h=1`, the target is `λ{h odd} ≥ 1`. The **Sufficient Lemma (R2)** closes it for
  every config with `|h|≤1` (proved, equality-robust). The **obstruction (R4)** proves `|h|≤1` is
  *unattainable* for `b≥2` (near-`0`, `h(0⁺) ≤ 1−2b ≤ −3`, forced by `Z` having `n+b` parts vs `Y`'s
  `≤n−b+1`), so no `Y`-exchange can finish — closing GAP-LB′ genuinely requires bounding
  `λ{h odd}` given `Z`'s **recursive dyadic cut-structure near `0`** (a scalar/count summary of `Z`
  provably fails — explorer probes 5–7). The residual is thus reduced to a near-`0` measure bound on
  the negative excursions of `h` supported on `Z`'s small cut-fragments.
- **Upper bound — reduced; naive strategy refuted.** Bisection-only Xiang forces exactly
  `D = min_{∅≠T} D(T)` over sub-multisets `T` of Liu's pieces (Cut-Flip corollary). This
  is **insufficient**: `min_T D(T) > u` for n≥2 (Lemma SD is FALSE — numerically the max
  over Liu partitions of `min_T D(T)` is `0.165>1/7` at n=2, `0.097>1/15` at n=3). Hence
  Xiang genuinely needs *unequal* cuts; the true upper bound is the open crux (GAP-UB).

The value/recursion algebra and n=1,2 are verified.

## Progress (full detail of the proved part)

Throughout, "piece" means a maximal sub-interval of the cut stick; the data of the game
after all marks is the **multiset of piece lengths**, summing to 1.

### 0. Position independence
The claiming phase depends only on the multiset of piece lengths, not on their positions:
a player's move is "claim an unclaimed piece", and both the set of available moves and each
piece's length are functions of the multiset alone. So the whole problem is the abstract
game: Liu chooses a multiset `P` of ≤ n+1 positive reals summing to 1 (n marks give ≤ n+1
pieces; using fewer marks gives fewer pieces, a special case); Xiang applies ≤ n *cuts*
(each replaces one current part `ℓ` by two positive parts `x, ℓ−x`); then the claiming
game is played on the resulting multiset.

### 1. Lemma G (greedy claiming) — PROVED
**Statement.** For a fixed multiset `a_1≥a_2≥…≥a_m` (sorted descending), in the alternating
claiming game (each player maximizes own total) the game value for the first player is the
**odd-rank sum** `a_1+a_3+a_5+…`. Equivalently, taking the currently-largest piece is
optimal for both players.

**Proof.** Since the grand total `T=Σa_i` is fixed, maximizing one's own total is the same
zero-sum objective as maximizing (own − opponent). Let `Δ(S)` be the value of
(current player's total − opponent's total) under optimal play from multiset `S`. Then
`Δ(∅)=0` and `Δ(S)=max_{a∈S}( a − Δ(S∖a) )`. We prove by induction on `|S|` that for
`S` sorted descending `a_1≥…≥a_m`,
`Δ(S) = a_1 − a_2 + a_3 − … =: A(S)`, and that the maximizer `a=a_1` attains it.

Base `|S|≤1` is immediate. Inductive step: for each index `i`, removing `a_i` and applying
the hypothesis to `S∖a_i` gives
`Δ(S∖a_i) = Σ_{j<i} s_j a_j − Σ_{j>i} s_j a_j`, where `s_j=(−1)^{j−1}` (the parts after
position `i` shift one place, flipping sign). Hence
`a_i − Δ(S∖a_i) = a_i − Σ_{j<i}s_j a_j + Σ_{j>i}s_j a_j`, and
`A(S) − (a_i − Δ(S∖a_i)) = 2Σ_{j<i}s_j a_j + (s_i−1)a_i`.
The partial alternating sum `Σ_{j<i}s_j a_j = (a_1−a_2)+(a_3−a_4)+…` is ≥ 0 (consecutive
terms non-increasing), and if `i` is even it is `≥ a_{i−1} ≥ a_i`. Thus:
if `i` odd, `s_i=1`, the expression `= 2Σ_{j<i}s_j a_j ≥ 0`;
if `i` even, `s_i=−1`, it `= 2(Σ_{j<i}s_j a_j − a_i) ≥ 0`.
So `a_i − Δ(S∖a_i) ≤ A(S)` for every `i`, with equality at `i=1`
(`a_1 − Δ(S∖a_1) = a_1 − (a_2−a_3+…) = A(S)`). Hence `Δ(S)=A(S)` and the greedy pick is
optimal. ∎

**Consequence.** The first player's total is `(T+Δ)/2 = (1+D)/2` with `T=1` and
`D := A(S) = a_1−a_2+a_3−…`. Also directly `(1+D)/2 = Σ_j \frac{1+s_j}{2} a_j =
Σ_{j odd} a_j`, the odd-rank sum. Both descriptions agree.
*(Numerically re-confirmed by the outline-reviewer on 3000 random multisets, 0 mismatches.)*

### 2. Level-Measure Formula for D — PROVED
**Statement.** For any multiset of positive parts with `N(t):=#{parts of length > t}`,
`D = a_1−a_2+a_3−… = λ( { t>0 : N(t) is odd } )` (Lebesgue measure).

**Proof.** `N(t)` is the number of parts exceeding `t`; since the parts sorted descending
are `a_1≥…≥a_m`, we have `N(t)=i` exactly on `t∈[a_{i+1},a_i)` (with `a_{m+1}:=0`).
Therefore `{t:N(t) odd} = ⋃_{i odd}[a_{i+1},a_i)`, a disjoint union, of measure
`Σ_{i odd}(a_i−a_{i+1}) = (a_1−a_2)+(a_3−a_4)+… = D`. ∎
*(Verified numerically: `alt` vs `meas` agree to 5 digits on random multisets.)*

Two immediate global facts used below:
- **(F1)** For `t>1/2`, at most one part exceeds `t` (two would sum to >1), so `N(t)∈{0,1}`
  and `{t>1/2:N odd} = {t>1/2 : a_max>t}`, of measure `(a_max−1/2)^+`. Hence
  `D ≥ (a_max−1/2)^+`.
- **(F2)** `λ{N≥j} = a_j` (since `N(t)≥j ⇔ a_j>t`).

### 3. Cut-Flip Lemma — PROVED
**Statement.** Replacing a part `ℓ` by two parts `x≤ℓ−x` changes the parity of `N(t)`
exactly on the set `[0,x) ∪ [ℓ−x,ℓ)` (measure `2x ≤ ℓ`), and nowhere else.

**Proof.** The change in `N(t)` from this single operation is
`ΔN(t)= (#new parts >t) − 1_{ℓ>t}`. For `t<x` both new parts exceed `t`: `ΔN=+1`.
For `x≤t<ℓ−x` only `ℓ−x>t`: `ΔN=0`. For `ℓ−x≤t<ℓ` neither new part exceeds `t` but `ℓ` did:
`ΔN=−1`. For `t≥ℓ`: `ΔN=0`. Parity flips iff `ΔN` is odd, i.e. on `[0,x)∪[ℓ−x,ℓ)`. ∎

After `≤n` cuts, `N(t) ≡ N_L(t) + Σ_j 1_{F_j}(t) (mod 2)`, where `N_L` is Liu's step
function and `F_j=[0,x_j)∪[ℓ_j−x_j,ℓ_j)` is the flip-set of cut `j` (on the *current* part
cut). Combined with §2 this makes `D` a purely parity-combinatorial functional.

**Bisection corollary — PROVED.** If Xiang *bisects* exactly the pieces in a set `S` of
Liu's pieces (each into two equal halves) and leaves `T=S^c` whole, then bisecting `ℓ`
flips parity on `[0,ℓ/2)∪[ℓ/2,ℓ)=[0,ℓ)`, i.e. on `{t<ℓ}`. Hence the final parity at `t`
is `N_L(t)+#{i∈S:b_i>t} ≡ #{i∈T:b_i>t} (mod 2)`, so by §2 the resulting discrepancy is
exactly `D(T)`, the discrepancy of the sub-multiset `T`. All bisection midpoints are
interior to Liu's pieces, hence automatically distinct from Liu's marks and from each other.
*(Verified: `D(final)=D(kept)` for all tested `S`.)*

### 4. Reduction of the answer to a discrepancy minimax — PROVED
By §1, Liu's payoff is `(1+D)/2`. Since `(1+u)/2 = (1 + 1/(2^{n+1}−1))/2 =
2^{n+1}/(2(2^{n+1}−1)) = 2^n/(2^{n+1}−1) = c(n)`, the target reduces to:

> **Lower:** Liu has a partition with `D ≥ u` for every Xiang response.
> **Upper:** for every Liu partition, Xiang has a response with `D ≤ u`.

Here `u=u_n=1/(2^{n+1}−1)`. If Liu uses `< n` marks (`m_0≤n` pieces), Xiang bisects all of
them (`m_0≤n` cuts) and by the Bisection corollary `D=D(∅)=0<u`, so such Liu play is
strictly worse; WLOG the extremal Liu uses `n` marks / `n+1` pieces.

### 5. Lower bound — Liu's dyadic partition. Case A PROVED, Case B open.
Liu uses `P={2^k u}_{k=0}^n` (sum `u(2^{n+1}−1)=1`). Write `g=2^n u`. Note
`g = 2^n/(2^{n+1}−1) = 1/2 + u/2 > 1/2`, and the remaining pieces
`R={2^k u}_{k=0}^{n−1}` have total `σ:=1−g=(2^n−1)u` and are a **scaled `(n−1)`-dyadic**:
scaling the `(n−1)`-dyadic `{2^k u_{n−1}}` by `σ` gives `2^k σ u_{n−1}=2^k u` since
`σ u_{n−1}=(2^n−1)u·\frac1{2^n−1}=u`. Because a stick can only be cut, pieces never merge,
so cuts inside the top piece `g` and cuts inside the block `R` act on disjoint sub-multisets;
the final multiset is (cuts of `g`) ⊎ (cuts of `R`). Let `a` = #cuts Xiang spends on the
top block, `b`= #cuts on `R`, `a+b≤n`.

**Induction on n.** Base `n=0`: single piece length 1, 0 cuts, `D=1=u_0`. Assume the lower
bound for `n−1` (and, by scale-invariance of `D` and the cut operation, for any scaled
`(n−1)`-dyadic: `≤ n−1` cuts give `D ≥ σ u_{n−1}=u`).

**Case A (`a=0`, top piece uncut).** Then the largest final piece is exactly `g` (every
other piece is a sub-part of some `2^k u ≤ 2^{n−1}u = g/2 < g`). By §1 Liu's total
`≥ a_max = g = (1+u)/2`, so `D ≥ u`. ✔ (Independently, (F1) gives the same on levels >1/2.)

**Case B (`a≥1`).** Then `b ≤ n−1`. This is proved below in the clean **integer-unit
normalization** (§5B); the round-1 strict-bound plan is retired (see the refutation note at the
end of this subsection). Case B is now ~85% closed, with a single precisely-stated residual
sub-claim GAP-LB′.

### 5B. Integer-unit normalization and the exact recursion `f(n,k)=f(n−1,k−1)`.

**Rescaling.** Multiply every length by `1/u_n`. Discrepancy `D` is homogeneous of degree 1 and
the cut operation is scale-covariant, so `D ≥ u_n` (original units) `⇔ D̃ ≥ 1` (rescaled), where
`D̃` is the discrepancy in the new units. Liu's dyadic partition becomes the **integer weights**
```
{ 2^0, 2^1, …, 2^n },   total  2^{n+1} − 1 ,
```
the top piece is `2^n`, and — crucially — the bottom block `R` becomes the **literal**
`(n−1)`-dyadic `{ 2^0, …, 2^{n−1} }` (total `2^n − 1`), with **no scaling factor**: in these
units the sub-problem is *identical in form* to the `n−1` problem. Define
```
f(n,k) := min over Xiang responses using ≤ k cuts of  D̃   (0 ≤ k ≤ n).
```
Our goal is `f(n,n) = 1`. Numerically (exhaustive allocation + multi-start Nelder–Mead, n≤3):
```
f(0,·)=1;  f(1,·)=[1,1];  f(2,·)=[3,1,1];  f(3,·)=[5,3,1,1].
```
These satisfy the **exact recursion `f(n,k) = f(n−1,k−1)` for `1 ≤ k ≤ n`**, and `f(n,0)` = the
uncut alternating sum `f_n := (2^{n+1}+(−1)^n)/3` (check: `f_1=1,f_2=3,f_3=5`). Unwinding,
`f(n,k) = f_{n−k}`, so in particular `f(n,n)=f_0=1 ⇔ D*=u_n`. **We prove the LOWER-bound half of
this recursion, `f(n,n) ≥ 1`, by strong induction on n; the strict-inequality mechanism is not
used.** *(This exact-value recursion is the round-2 replacement for the refuted `W(n−1,b)>u_{n−1}`
strict bound — it is equality-robust, matching that `D̃=1` is attained on a whole family of Xiang
allocations.)*

**Inductive claim `P(n)`.** *Any Xiang response with `≤ n` cuts to the integer-unit `n`-dyadic
`{1,…,2^n}` yields `D̃ ≥ 1`.*  Base `P(0)`: one piece of length 1, 0 cuts, `D̃ = 1`. ✓

**Inductive step.** Assume `P(n−1)`. Fix an `≤ n`-cut Xiang response; say `a` cuts fall on the
top piece `2^n` and `b` on the bottom block `{1,…,2^{n−1}}`, with `a+b ≤ n`. Because a stick only
cuts (never merges), the final multiset is `F = Y ⊎ Z`, where `Y` are the top-descendants (from
cutting `2^n` into `a+1` parts, total `2^n`, each `≤ 2^n`) and `Z` are the bottom-descendants
(total `2^n−1`, each `≤ 2^{n−1}`).

*Case A (`a=0`).* Top piece survives as `2^n`, the unique largest part. By the Domination
corollary (C3, `lemmas/cut-flip.md`) `D̃ ≥ 2·(2^n) − (2^{n+1}−1) = 1`. ✓

*Case B (`a≥1`).* Then `b ≤ n−1`, so `Z` is a `≤(n−1)`-cut response to the `(n−1)`-dyadic
`{1,…,2^{n−1}}`; by `P(n−1)`,
```
D_bot := λ(O_Z) ≥ 1 ,        O_Z := { t>0 : N_Z(t)=#{z∈Z:z>t} is odd }.
```
**Exact decomposition at the threshold `θ := 2^{n−1}`.** Every bottom part is `≤ θ`, so
`N_Z(t)=0` for `t ≥ θ` and `O_Z ⊆ (0,θ)`. Writing `O_Y := {N_Y odd}` for the top, the
level-measure identity (Lemma G, integral form) gives `D̃ = λ(O_Y △ O_Z)`. Split `O_Y` at `θ`:
`O_Y^> := O_Y∩[θ,∞)`, `O_Y^< := O_Y∩(0,θ)`, and set `D_top^> := λ(O_Y^>)`, `D_top^< := λ(O_Y^<)`.
On `[θ,∞)` we have `O_Z=∅`, so `O_Y△O_Z = O_Y^>`; on `(0,θ)`, `O_Y△O_Z = O_Y^< △ O_Z`. Hence
```
D̃ = D_top^> + λ(O_Y^< △ O_Z)
   = D_top^> + D_top^< + D_bot − 2 λ(O_Y^< ∩ O_Z).          (★)
```
(This is the round-1 identity `(★)`, now split by the threshold so that the cancellation term
`2λ(O_Y^<∩O_Z)` is confined to `(0,θ)`.)

**Threshold-domination refinement (round 3) — closes `y₁ ≥ θ+1`.** The top-descendants `Y`
partition the top piece, so `Σ_{y∈Y} y = 2^n = 2θ`. Two distinct parts each `> θ` would sum to
`> 2θ`, exceeding the total `2θ` — impossible. Hence **at most one `Y`-part exceeds `θ`**, so on
`(θ,∞)` we have `N_Y(t)∈{0,1}` (and `N_Z(t)=0` since every bottom part is `≤ 2^{n−1}=θ`), giving
`N(t)=N_Y(t)∈{0,1}` there. Writing `y₁:=max Y`, the level `N=1` holds exactly on `(θ, y₁)` (empty if
`y₁≤θ`), so
```
D_top^> = λ(O ∩ (θ,∞)) = (y₁ − θ)⁺ .          (◇)
```
Because all the summands in (★) are nonnegative and `D̃ ≥ D_top^>` (drop the `(0,θ)` part, whose net
contribution `λ(O_Y^< △ O_Z) ≥ 0`),
```
D̃ ≥ D_top^> = (y₁ − θ)⁺ .                     (◇◇)
```
**Therefore if `y₁ ≥ θ+1 = 2^{n−1}+1` then `D̃ ≥ 1`, and Case B is settled — with NO cancellation
term.** This is a strict enlargement of the region handled by (★★) below: it requires only that the
single largest top-descendant sit `≥ 1` above the half-threshold `θ`, whereas the domination
corollary (C3) would demand the far stronger `y₁ ≥ 2^n`. *(Verified: `λ(O∩(θ,∞))=(y₁−θ)⁺` and
`D̃≥(y₁−θ)⁺` hold with 0 violations over 2·10⁵ random Case-B configs, n=2..6.)*

In the remaining hard region we may therefore assume `y₁ < 2^{n−1}+1` (so `D_top^> = (y₁−θ)⁺ < 1`).

**Bound (★★).** Since `O_Y^<∩O_Z ⊆ O_Y^<` and `⊆ O_Z`, `λ(O_Y^<∩O_Z) ≤ min(D_top^<, D_bot)`, so
```
D̃ ≥ D_top^> + D_top^< + D_bot − 2 min(D_top^<, D_bot)
   = D_top^> + | D_top^< − D_bot | .                          (★★)
```
*(Numerically verified: 0 violations of (★★) over 3·10^5 random Case-B configs, n=2..6.)*

**Region closed by (★★).** If `| D_top^< − D_bot | ≥ 1`, then (★★) gives `D̃ ≥ 1` immediately
(using `D_top^> ≥ 0`). Because `D_bot ≥ 1`, this covers in particular:
- `D_top^< ≤ D_bot − 1` (e.g. `D_top^< = 0`, or the balanced top-cut `a=1` which forces the two
  top halves `2^{n−1},2^{n−1}`, giving `N_Y≡2` on `(0,θ)`, `O_Y^<=∅`, `D_top^<=0` ⇒ `D̃ ≥ D_bot ≥ 1`);
- `D_top^< ≥ D_bot + 1`.
This closes Case B on `≈85%` of random configs (measured). ✔

**Residual GAP-LB′ (open, precise).** After the round-3 refinement (◇◇) and (★★), the ONLY region
left open is the *doubly-balanced* one,
```
y₁ < 2^{n−1}+1   (so D_top^> < 1)   AND   | D_top^< − D_bot | < 1 − D_top^> ,
```
with near-complete overlap λ(O_Y^< ∩ O_Z) close to min(D_top^<,D_bot).
There (★★) can dip below 1 (e.g. n=2, a=2, b=0: `D_top^<≈0.593, D_bot=1, D_top^>≈0.561`, RHS of
(★★) `≈0.967<1`, yet the true `D̃ = 1`). To finish, one must show
```
2 λ(O_Y^< ∩ O_Z) ≤ D_top^< + D_bot + D_top^> − 1 ,          (GAP-LB′)
```
i.e. bound the overlap of the bottom's odd-set `O_Z` with the top's low odd-set `O_Y^<` away from
the trivial `min`. This is a *joint* structural fact about **where** `O_Z` sits inside `(0,θ)`
relative to `O_Y^<` — it does not follow from `D_bot ≥ 1` alone (which only controls `λ(O_Z)`, not
its location). The natural tools: (i) ~~strengthen the IH to *confine* `O_Z`~~ — **REFUTED this round
(do not retry):** even at `n=1`, cutting the `2` into `x,2−x` gives odd-set `(1,2−x)∪(0,x)` which
reaches arbitrarily close to `0`; so no "`O ⊆` high region" confinement invariant holds — only
`λ(O)=D̃` is controlled, never its location. Hence the residual is intrinsically a JOINT fact about
`O_Y^<` and `O_Z` together, not a one-sided containment. (ii) the rank-interleaving reformulation
(merge `Y` and `Z` into one sorted list, track the T/B label string, use Lemma G's signed sum on the
merged order) — this remains the recommended route: it works with `λ(O_Y^< △ O_Z)` directly rather
than through the opaque `2λ(∩)` term, and is the still-unclosed mechanism.
*(Numerics: in the residual region the true `min D̃` is exactly 1 over 3·10^5 samples — the theorem
holds; only this overlap bound is unproven.)*

**Retired (do NOT retry).** The round-1 STRICT bound `W(n−1,b) > u_{n−1}` for `b<n−1` is REFUTED
(`/tmp/round-2/math-explorer-lowerbound.md`): at n=3, `a=2,b=1` (`b=1<n−1=2`) attains `D=u`
EXACTLY when the bottom cut lands on the bottom's own dominant piece. Equality is attained on a
whole family, so any strict-domination argument is dead; the exact recursion above is the correct
equality-robust replacement.

### 5C. Difference-function reformulation, the Sufficient Lemma, and the exchange obstruction (round 4).

This subsection replaces the opaque `2λ(O_Y^<∩O_Z)` cancellation term of `(★)` by a single integer
function, proves a clean equality-robust closure of the residual whenever a two-sided tracking bound
holds, and then proves rigorously **why the exchange-to-`a−1` mechanism cannot close the whole
residual** — isolating the genuine remaining obstruction.

Throughout, `F = Y ⊎ Z` with `Y` the top-descendants (`ΣY = 2^n = 2θ`, `θ=2^{n−1}`, `a+1` parts,
`a≥1`) and `Z` the bottom-descendants (`ΣZ = 2^n−1 = 2θ−1`; `Z` is a `≤b`-cut response of the
literal `(n−1)`-dyadic `{1,…,2^{n−1}}`, so `Z` has exactly `n+b` parts). Budget: `a+b ≤ n`, `a≥1`.

**Count functions.** For a multiset `P` write `N_P(t) := #{p∈P : p>t}` (right-continuous,
non-increasing, integer). Then `N_F = N_Y + N_Z`, and by the Level-Measure Formula (§2, integral
form) `D̃ = λ{t>0 : N_F(t) odd}`.

**(R1) The difference function and its area identity.** Define
```
h(t) := N_Y(t) − N_Z(t)   (t>0).
```
Since `N_F = N_Y+N_Z ≡ N_Y−N_Z = h  (mod 2)`, we have `{N_F odd} = {h odd}`, so
```
D̃ = λ{ t>0 : h(t) odd }.                                    (R1a)
```
Moreover `∫₀^∞ N_P(t)dt = ∫₀^∞ #{p>t}dt = Σ_{p∈P} p = ΣP` for any multiset `P`. Hence
```
∫₀^∞ h(t) dt = ΣY − ΣZ = 2θ − (2θ−1) = 1     (identically, for every Case-B config).   (R1b)
```
Thus the entire residual GAP-LB′ is the single statement `λ{h odd} ≥ ∫h`, with the RHS pinned to `1`
by `(R1b)`. This is the exact, structure-free restatement of the target `D̃ ≥ 1`.

**(R2) Sufficient Lemma (proved).** *If `|h(t)| ≤ 1` for a.e. `t>0`, then `D̃ ≥ 1`, with equality
iff `λ{h=−1}=0`.*

*Proof.* Under `|h|≤1`, `h` takes values in `{−1,0,1}` a.e. Then `{h odd} = {h=1}∪{h=−1}` (disjoint),
so by `(R1a)`, `D̃ = λ{h=1} + λ{h=−1}`. Also, integrating the three-valued `h`,
`∫h = (+1)λ{h=1} + (−1)λ{h=−1} + 0 = λ{h=1} − λ{h=−1}`. Subtracting,
```
D̃ − ∫h = ( λ{h=1}+λ{h=−1} ) − ( λ{h=1}−λ{h=−1} ) = 2 λ{h=−1} ≥ 0 .
```
With `(R1b)` (`∫h=1`) this gives `D̃ = 1 + 2λ{h=−1} ≥ 1`, and `D̃=1 ⟺ λ{h=−1}=0`. ∎

`(R2)` is a genuine, reusable, equality-robust certificate: it closes GAP-LB′ for **every** Case-B
config whose difference function stays within one level (`|h|≤1`), and it explains the tight family
(`D̃=1` exactly when the bottom's odd-set is never “over-covered”, `λ{h=−1}=0` — the maximal-alternation
zigzag of the numerics, where `h∈{0,1}`). *Verified: 0 violations of `D̃ ≥ ∫h` over 41814 random
configs satisfying `|h|≤1`.*

**(R3) Compactness and the ±1 gradient (proved).** Fix `Z`. On the simplex
`Δ := {Y∈ℝ^{a+1} : y_j≥0, Σy_j=2θ}` (compact), `g(Y):=D̃(Y⊎Z)=λ{h odd}` is continuous and piecewise
linear, so `min_Δ g` is attained. Away from coincidences of part values, for each `j`,
```
∂D̃/∂y_j = 2·1[ M_{−j}(y_j) even ] − 1 ∈ {+1,−1},   M_{−j}(y_j) := #{ parts of F other than y_j that exceed y_j }.
```
*Proof of the gradient.* Increasing `y_j` by `dy` changes `N_F` only on the sliver `(y_j, y_j+dy)`,
where the single part `j` newly exceeds the level, so `N_F` there rises by `1` and its parity flips.
Writing `M=M_{−j}(y_j)` for the number of other parts exceeding `y_j`, the sliver's contribution to
`λ{N_F odd}` changes by `1[M+1 odd] − 1[M odd] = 1[M even] − 1[M odd] = 2·1[M even] − 1`. ∎

**Local exchange at a minimizer.** Let `Y*` minimize `g`, and let `y_s` be its smallest fragment.
For any other fragment `y'`, the mass-preserving direction `y_s↓, y'↑` is feasible, so its directional
derivative `∂D̃/∂y' − ∂D̃/∂y_s ≥ 0`. Combined with the reverse feasibility argument (as in the
round-3/4 build report), at a minimizer one always finds a partner `y'` with
`∂D̃/∂y' = ∂D̃/∂y_s`, i.e. a **value-preserving exchange** decreasing `y_s`. Following it drives `y_s`
down until it (a) reaches `0` — a genuine `a→a−1` reduction — or (b) coincides with a `Z`-value,
forming an *invisible pair* (§spine) that can be removed without changing `D̃`. This is the rigorous
core of the exchange move.

**(R4) The obstruction: the exchange cannot reach `|h|≤1`/Case A for `b≥2` (proved).** The route of
the outline hoped to iterate `(R3)` down to a `|h|≤1` config (then `(R2)` closes) or to Case A
(`a=0`). Both are **impossible** in general, for a hard structural reason:

At `t→0⁺` every positive part exceeds `t`, so `N_Y(0⁺)=a+1` and `N_Z(0⁺)= n+b` (the number of
`Z`-parts). Hence
```
h(0⁺) = (a+1) − (n+b).
```
Under the budget `a+b≤n` (so `a ≤ n−b`) we get `h(0⁺) ≤ (n−b+1)−(n+b) = 1 − 2b`. Therefore:
```
b ≥ 2  ⟹  h(0⁺) ≤ −3  on a right-neighbourhood of 0  ⟹  |h| ≥ 3 there,  irremovably.
```
No exchange on `Y` (which only redistributes `ΣY=2θ` among `a+1 ≤ n−b+1` fragments) can raise
`N_Y(0⁺)` above `a+1`; `Y` simply lacks the fragments to track `Z`'s `n+b` small parts near `0`. So
`|h|≤1` is **unattainable** when `b≥2`, the `(R2)` certificate does not apply there, and the
`a→a−1` exchange terminates not at a `|h|≤1` config but with these forced negative excursions intact.
*(Numerics, build5: at `min_Y`, `max(N_Y−N_Z)=2` and `min(N_Y−N_Z)=−3` for `b≥1`, so both a positive
`h=2` excursion and a deep negative excursion survive at the true minimizer; `D̃=1` still holds — via
the small measure of these excursions, not via `|h|≤1`.)*

**Consequence — the residual, precisely.** The negative excursions of `h` near `0` are (i) forced by
`Z`'s fragment count and (ii) supported on the tiny intervals occupied by `Z`'s small cut-fragments.
`D̃ = ∫h + 2λ{h<0, h odd} + (correction for |h|≥2 on the positive side)`; the bound `D̃ ≥ 1` holds
because these excursions carry small measure **and** are placed by `Z`'s recursive dyadic cutting —
which is exactly the ingredient a scalar/count summary of `Z` cannot supply (explorer probes 5–7).
Thus the exchange route **reduces GAP-LB′ to the same near-`0` `Z`-structure control** as the
telescope twin: bound `λ{h odd}` below `1` given that the sub-`θ` part of `Z` is itself a
`≤(b)`-cut response of the `(n−1)`-dyadic. This is the honest open step; it is **not** closed here.

**What is now rigorously closed (round 4).** (a) The reformulation `(R1)` and area identity `(R1b)`;
(b) the Sufficient Lemma `(R2)` — a complete, equality-robust **per-config certificate**: any Case-B
config whose difference function satisfies `|h(t)|≤1` a.e. has `D̃ ≥ 1`. This certificate is
verifiable directly and, empirically, is satisfied at every `b=0` minimizer (build5: `b=0` gives
`h∈{−1,0,1}`); (c) the gradient formula `(R3)` and the exchange's value-preserving local move at any
minimizer; (d) the impossibility `(R4)`: for `b≥2` a forced near-`0` excursion `|h|≥3` makes `(R2)`
inapplicable, so the exchange route **cannot** finish there.
**What is NOT yet proven (honest):** (i) that a `b=0` (or `b=1`) minimizer *provably* attains `|h|≤1`
— the positive-side plateau `h=2` seen in numerics would have to be flattened by a value-preserving
exchange, which `(R3)` makes plausible but I did **not** prove in general (fragment-count limits may
block the partner move); (ii) the `b≥2` near-`0` measure bound. Both reduce to controlling `Z`'s
recursive cut-structure near `0`, the shared wall with the telescope twin.

### 5D. Budget-count route (round 6): super-level reduction, deficit budget, conservation.

This subsection replaces the retired exchange mechanism of §5C by a **global combinatorial count** on
the certified merged-order signed sum `(♦)` of `lemmas/termwise-lattice.md`. We import verbatim: for
`F=Y⊎Z`, `M(t):=N_Y(t)−N_Z(t)`, `D̃=λ{t:M(t) odd}`, `∫₀^∞M=sum(Y)−sum(Z)=1` (integer Case-B units),
and along the merged descending order `w₁≥…≥w_m` with prefix imbalance `c_i` and `Δw_i=w_i−w_{i+1}≥0`,
```
D̃ − 1 = Σ_i ψ(c_i) Δw_i ,      ψ(c) := 1[c odd] − c .          (♦)
```
All statements below are for Case B (`a≥1`, so `Z` is a `≤b`-cut response to `S_{n−1}`, `b≤n−1`,
`sum(Z)=2^n−1`, every `Z`-part `≤θ:=2^{n−1}`; `Y` = `a+1` parts, `sum(Y)=2^n=2θ`, at most one `>θ`).

**(B1) Super-level reduction — PROVED.** For integers define the super-level sets
```
A_k := { t>0 : M(t) ≥ k } ,   B_k := { t>0 : M(t) ≤ −k }    (k≥1),
```
so `A_1⊇A_2⊇⋯`, `B_1⊇B_2⊇⋯`, `|A_k|=λ(A_k)`, `|B_k|=λ(B_k)`. Then
```
D̃ − 1 = 2( Σ_{j≥1} |B_{2j−1}|  −  Σ_{j≥1} |A_{2j}| )  =: 2( O_B − E_A ).      (B1)
```
so **the whole Case-B target `D̃≥1` is exactly the super-level inequality `O_B ≥ E_A`.**

*Proof.* `ψ` is evaluated at the integer `c=M(t)`. For `c≥0`: `c−1[c odd]=2⌊c/2⌋` (if `c=2q`, `=2q`;
if `c=2q+1`, `c−1=2q`), so `ψ(c)=−2⌊c/2⌋=−2Σ_{j≥1}1[c≥2j]`. For `c≤0`, put `d=−c≥0`:
`ψ(c)=1[d odd]+d=2⌈d/2⌉` (if `d=2q`, `=2q`; if `d=2q+1`, `d+1=2q+2`), so
`ψ(c)=2⌈d/2⌉=2Σ_{j≥1}1[d≥2j−1]=2Σ_{j≥1}1[c≤−(2j−1)]`. Exactly one of the two branches is nonzero
at any `t` (`c=0` gives `0` in both). Substituting into `(♦)` and using
`Σ_iΔw_i 1[c_i≥2j]=λ(A_{2j})` and `Σ_iΔw_i 1[c_i≤−(2j−1)]=λ(B_{2j−1})` (each interval `(w_{i+1},w_i)`
carries `M≡c_i`),
```
D̃−1 = Σ_i Δw_i( −2Σ_j1[c_i≥2j] + 2Σ_j1[c_i≤−(2j−1)] ) = −2Σ_j|A_{2j}| + 2Σ_j|B_{2j−1}|. ∎
```
*(Verified: `|D̃−1−2(O_B−E_A)|<10⁻⁶` over 3·10⁵ configs, 0 failures.)* Interpretation: `E_A`
(even positive super-levels) is the **T-run deficit**, `O_B` (odd negative super-levels) the
**anchor surplus** — `(B1)` is the exact, width-weighted form of the target `(GAP-LB′-run)`.

**(B2) Deficit budget and localization — PROVED.** Since `M=N_Y−N_Z≤N_Y`, we have
`A_{2j}={M≥2j}⊆{N_Y≥2j}`. By the order-statistic identity `λ{N_Y≥k}=y_k` (Level-Measure (F2), with
`y_k` the `k`-th largest `Y`-part, `y_k:=0` for `k>|Y|`), `|A_{2j}|≤y_{2j}`. Hence
```
E_A = Σ_{j≥1}|A_{2j}| ≤ y₂ + y₄ + y₆ + ⋯ .                     (B2a)
```
Furthermore `2θ=ΣY≥y₁+y₂≥2y₂` gives `y₂≤θ`, and `A_2⊆{N_Y≥2}=(0,y₂)`, so
```
the deficit is supported on (0,y₂) ⊆ (0,θ):  A_{2j}⊆(0,θ) for all j≥1.   (B2b)
```
*(Verified: 0 violations of both `E_A≤Σy_{2j}` and "no deficit above θ", 10⁵ configs.)* This is the
"each run peak consumes top-fragments, and no run rises above the half-threshold" bound, exact.

**(B3) Conservation below `θ` — PROVED.** For `t≥θ`, every `Z`-part is `≤θ` so `N_Z(t)=0`, and at
most one `Y`-part exceeds `θ` so `N_Y(t)∈{0,1}`; thus `M=N_Y∈{0,1}` on `[θ,∞)` and
`∫_θ^∞M = λ{t≥θ:y₁>t} = (y₁−θ)⁺ =: δ`. Combined with `∫_0^∞M=1`,
```
∫_0^θ M = 1 − δ ,     δ = (y₁−θ)⁺ ≥ 0 .                       (B3)
```
So deficit and surplus both live on `(0,θ)` (by (B2b) and: `B_k⊆{N_Z≥1}⊆(0,θ)`), with signed total
pinned to `1−δ`. (When `δ≥1`, i.e. `y₁≥θ+1`, `(◇◇)` already gives `D̃≥δ≥1`; so the open region has
`0≤δ<1`.)

**(B4) Status of the count — the isolated gap.** `(B1)`–`(B3)` reduce Case B to the single
width-weighted inequality
```
O_B = Σ_{j≥1}|B_{2j−1}|  ≥  Σ_{j≥1}|A_{2j}| = E_A ,   both supported on (0,θ).    (GOAL)
```
The deficit side is fully controlled — `E_A≤Σy_{2j}` and localized to `(0,y₂)`. The surplus side is
the residue: `(B2a)` alone is **too weak** (at the exact-tie config `n=4`, `Y=(8,3,3,2)`,
`Z=(8,2,2,2,1)`: `E_A=1`, `Σy_{2j}=y₂+y₄=3+2=5`, yet `O_B=1` — a pure `Y`-side bound cannot see that
the surplus is only `1`). So `O_B` must be **lower-bounded through `Z`'s anchor placement**, i.e. the
Structure Lemma geometry of where `Z`'s dyadic pieces sit inside `(0,θ)` — never a scalar/count
summary of `Z` (refuted, §5C R4 and telescope §6). Numerically `(GOAL)` holds with 0 violations over
2·10⁵ configs (`n≤6`), infimum of `D̃` exactly `1` attained only at tie boundaries continuous with the
closed region (matching Lemma T's equality-robustness; NO universal strict slack).

**This `(GOAL)` is precisely the width-weighted domination the outline flagged as Step 4, and — as the
outline-reviewer anticipated — it coincides with the telescope twin's Step-5 wall.** The budget-count
reframing contributes: (i) the exact super-level form `(B1)` (removes the opaque `2λ(∩)`/`ψ`-sum in
favour of a monotone super-level count); (ii) the sharp, `Y`-only deficit control `(B2)`; (iii) the
conservation `(B3)` localizing everything to `(0,θ)`. What remains open is the anchor lower bound on
`O_B`; it is genuinely a joint fact about `Z`'s cut-tree and is NOT closed here.

### 5E. Round 7 — refutation of the termwise super-level closure; `b=0` slack; wall assessment.

This round pushed the budget-count mechanism on `(GOAL)` and produced one rigorous **negative**
result that sharpens the wall, plus a numerical map of where the residual is tight. Nothing in
`(B1)`–`(B3)` changed (all re-verified: the `(B1)` identity `D̃−1=2(O_B−E_A)` holds to `3·10⁻¹⁵`
over `5·10⁴` configs `n=3..5`; `(B2)` `E_A≤Σy_{2j}` 0 violations; the tie config `n=4`,
`Y=(8,3,3,2)`, `Z=(8,2,2,2,1)` gives `D̃=1`, `O_B=E_A=1` exactly).

**(E1) The natural termwise closure of `(GOAL)` is FALSE — proved by explicit witness.** The
cleanest way a super-level count could prove `O_B=Σ_j|B_{2j−1}| ≥ Σ_j|A_{2j}|=E_A` would be the
**term-by-term domination** `|A_{2j}| ≤ |B_{2j−1}|` for every `j≥1` (pair the `2j`-th positive
super-level against the `(2j−1)`-th negative one). This is **refuted**: take the Case-B config
(`n=4`, `a=2`, `b=2`, so `a+b=4=n`)
```
Y = (7.9362, 7.1735, 0.8903)     (sum = 16 = 2⁴),
Z = (4, 3.4776, 2.7687, 2, 1.7536, 1)   (sum = 15 = 2⁴−1, a legitimate 2-cut of {1,2,4,8}).
```
Here `|A_2| = λ{M≥2} ≈ 3.1735` while `|B_1| = λ{M≤−1} ≈ 2.7687`, so `|A_2| > |B_1|` — the `j=1`
term-pairing **fails** — yet the aggregate holds: `E_A ≈ 3.1735`, `O_B ≈ 4.5224`, so `O_B ≥ E_A`
and `D̃ = 1+2(O_B−E_A) ≈ 3.70 ≥ 1`. (Verified directly; hundreds of such witnesses exist for
`b≥2`, e.g. `n=4,a=2,b=2`: 128 term-pairing failures per `2·10⁴` random draws, with `O_B≥E_A`
holding in **every** one.) *Consequence:* `(GOAL)` is **irreducibly aggregate** — it cannot be
proved by any monotone level-by-level or super-level pairing; the surplus at odd negative levels
must be summed against the deficit at even positive levels **globally**, not level-matched. This
closes off the most natural budget-count sub-route and matches why a scalar/count summary of `Z`
fails (§5C R4): the compensation is delocalized across levels.

**(E2) The `b=0` sub-region (top budget only, `Z` uncut dyadic) carries genuine slack.** For
`b=0`, `Z={2^0,…,2^{n−1}}` is the exact dyadic. Over the `maxc≥2` residual the discrepancy is
bounded strictly away from `1`:
```
min D̃ (maxc≥2, b=0):  n=3,a=2: 1.029;  n=3,a=3: 1.088;  n=4,a=3: 1.224;
                        n=4,a=4: 1.158;  n=5,a=5: 1.486   (8·10⁴ draws each, 0 violations).
```
So the tight `maxc≥2` boundary (infimum `=1`) lives **only** at `b≥1` tie configs (e.g. the
`n=4,b=1` tie `Y=(8,3,3,2)`, `Z=(8,2,2,2,1)`) — `b=0` is comfortably interior. This isolates the
genuinely hard slice as **`b≥1` with a near-tie between `y₁` and a `Z`-anchor**, and says the
budget-count difficulty is not about "many top fragments" but about the interleaving of `Z`'s
**cut**-fragments (which `b=0` lacks). A rigorous `b=0` closure via a clean `O_B` lower bound was
attempted but not completed this round (the dyadic `z_ℓ=2^{n−ℓ}` gives `a_ℓ≤y_ℓ` and
`b_ℓ≤z_ℓ`, both **upper** bounds, whereas `O_B` needs a **lower** bound on `b_{odd}` that couples
`N_Z` to where `N_Y` is small — the same coupling the wall demands).

**(E3) Honest wall assessment / escalation flag.** The budget-count mechanism has now been driven
to the identical target inequality `(GOAL)` as the telescope twin's Step-5, exactly as the
outline-reviewer predicted. Round 7 adds: (i) `(E1)` — the termwise/level-matched closure is
**provably impossible**, so a third "super-level pairing" variant would be dead on arrival;
(ii) `(E2)` — the tight slice is precisely `b≥1` near-tie, not `b=0`. Per the reviewer's short-leash
note ("if BOTH GAP-L mechanisms stall on the width-weighted domination, escalate: the field has
collapsed and GAP L needs a genuinely different framing, not a third mechanism for the same
inequality"), this is the trigger: both GAP-L slugs share `(GOAL)`, and the two most natural
mechanisms for it (recursive descent, global count) plus the termwise pairing are now all at or
past the wall. **Recommendation to the orchestrator:** next round GAP L needs a genuinely different
top-level framing (e.g. a direct minimax/LP-duality certificate on the reduced discrepancy game, or
an amortized potential over Xiang's cut *sequence* rather than the static final multiset), not a
fourth attack on `O_B ≥ E_A`.

### 6. Upper bound — reduction, and refutation of the naive strategy.
By §4 fix any Liu partition into `n+1` parts `b_1≥…≥b_{n+1}` (sum 1). Xiang wants a response
with `D ≤ u`.

**Bisection-only is INSUFFICIENT (refuted).** By the Bisection corollary Xiang can keep any
nonempty `T` (bisecting the other `≤ n` pieces) and reach `D=D(T)`, so bisection-only forces
exactly `min_{∅≠T} D(T)`. But this minimum can exceed `u`:
```
n=2: max over Liu partitions of  min_T D(T) ≈ 0.16495 > 1/7 ≈ 0.14286
n=3: … ≈ 0.09681 > 1/15 ≈ 0.06667
n=4: … ≈ 0.05987 > 1/31 ≈ 0.03226
```
(dyadic Liu attains exactly `min_T D(T)=u`, but other Liu partitions do worse for Xiang
under bisection). So the "bisect all but the smallest / bisect the n largest" family — and
any bisection-only rule — **cannot** cap Liu at `u`. Xiang must use *unequal* cuts. This
confirms the outline-reviewer's and explorers' refutation.

**General reduction.** By §2–§3 the upper bound is exactly: for any Liu step function
`N_L` (from `n+1` pieces) Xiang can choose `≤ n` flip-sets `F_j=[0,x_j)∪(ℓ_j−x_j,ℓ_j)`
(each `ℓ_j` a *current* piece length) so that
`λ{ t : N_L(t) ⊕ ⊕_j 1_{F_j}(t) = 1 } ≤ u`.
**GAP-UB (open).** No such general `≤n`-flip construction is yet proved. The n=1 optimum is
a *threshold* rule (bisect the long side if the mark `p≤1/3`, else pin the median), and the
correct general rule is non-myopic; producing it (or an equivalent parity-covering argument)
is the crux this approach has not closed.

### 7. Value / recursion algebra and small cases — verified
Closed form `c(n)=2^n/(2^{n+1}−1)` gives `u_n=2c_n−1=1/(2^{n+1}−1)`; then
`1/u_n = 2^{n+1}−1 = 2(2^n−1)+1 = 2/u_{n−1}+1`, i.e. `u_n = u_{n−1}/(2+u_{n−1})`, equivalently
`c_n = 2c_{n−1}/(2c_{n−1}+1)` (with `c_0=1`). Check `c_1=2/3, c_2=4/7, c_3=8/15`.

- **n=1 (fully by hand, both bounds).** Liu marks one point `p≤1/2` (WLOG), pieces
  `{1−p, p}`. Let `V(p)=min_{Xiang} D` be the discrepancy Xiang forces (Xiang has 1 cut).
  *(a) `p=1/3` gives `V=1/3`.* Pieces `{2/3,1/3}`. No cut: `D=2/3−1/3=1/3`. Cutting the
  `2/3` into `{x,2/3−x}` (`x≤1/3`) yields sorted `{2/3−x, 1/3, x}` (since `2/3−x≥1/3≥x`),
  `D=(2/3−x)−1/3+x=1/3`. Cutting the `1/3` into `{y,1/3−y}` yields `{2/3,1/3−y,y}`,
  `D=2/3−(1/3−y)+y=1/3+2y≥1/3`. So `V(1/3)=1/3=u_1`. *(b) No `p` beats it.* For any `p≤1/2`,
  Xiang may leave the stick uncut, forcing `D≤|(1−p)−p|=1−2p`; and by (F1) Xiang can also
  cut the long piece `1−p` in half. Concretely `V(p)≤min(1−2p, p)`:
  for `p≤1/3`, bisecting the long piece gives sorted `{(1−p)/2,(1−p)/2,p}`,
  `D=(1−p)/2−(1−p)/2+p=p`; for `1/3≤p≤1/2`, leaving uncut gives `D=1−2p≤1/3`. In both ranges
  `V(p)≤1/3`, with equality only at `p=1/3`. Hence `max_p V(p)=1/3`, so Liu's guaranteed
  payoff is `(1+1/3)/2=2/3`. `c(1)=2/3=2^1/(2^2−1)`. ✔ (This is Case A/B and the upper-bound
  threshold rule made fully explicit at n=1.)
- **n=2.** Dyadic `{1/7,2/7,4/7}`: exhaustive/local search over ≤2 arbitrary Xiang cuts
  gives `min D = 1/7`, so Liu ≥ 4/7; the reviewer's brute force of the full game gives
  `c(2)=4/7`. ✔ `4/7=2^2/(2^3−1)`.

## Cases to cover — status
- Base `n=0,1`: done. `n=1` both bounds explicit; `n=2,3` values verified numerically
  (min D̃ = 1 exactly, matching the explorer's brute force).
- Lower half: Case A proved; **Case B closed on `{y₁≥2^{n−1}+1} ∪ {|D_top^<−D_bot|≥1−D_top^>}`
  via (◇◇)+(★★); residual GAP-LB′ open** (doubly-balanced region, joint overlap bound
  `2λ(O_Y^<∩O_Z) ≤ D_top^<+D_bot+D_top^>−1`).
- Upper half: reduced; naive strategy refuted; **general Xiang strategy (GAP-UB) open**.
- Liu using `<n` marks: handled (Xiang bisects all, `D=0`).

## Full proof
Not present — Status is `partial`. Remaining gap (round-6 form): **`(GOAL)`** of §5D — the
width-weighted super-level inequality `O_B=Σ_j|B_{2j−1}| ≥ Σ_j|A_{2j}|=E_A`, equivalently `D̃≥1` in
Case B (`maxc≥2` residual). Fully proved this round: the exact super-level reduction `(B1)`
(`D̃−1=2(O_B−E_A)`), the deficit budget/localization `(B2)` (`E_A≤Σy_{2j}`, deficit `⊆(0,θ)`), and the
conservation `(B3)` (`∫_0^θM=1−δ`). The open residue is the **anchor lower bound on `O_B`** via `Z`'s
Structure-Lemma geometry — the same width-weighted domination that is the telescope twin's Step-5
wall (as flagged by the outline-reviewer). Round 7 (§5E) proved the **termwise** closure of `(GOAL)`
(`|A_{2j}|≤|B_{2j−1}|`) is FALSE (explicit witness), so `(GOAL)` is irreducibly aggregate; isolated
the tight `maxc≥2` slice to `b≥1` near-tie (the `b=0` slice has slack `≥1.029`); and flagged
escalation — GAP L now needs a genuinely different framing, not another attack on `O_B≥E_A`. Prior equivalent recasts still valid: the
difference-function `|h|≤1` Sufficient Lemma (R2, §5C) closes every `|h|≤1` config; the fragment-count
obstruction (R4) proves the exchange route cannot finish for `b≥2`. The lower bound is otherwise complete — base, Case A, Case B on
`{y₁≥2^{n−1}+1} ∪ {|D_top^<−D_bot|≥1−D_top^>}` are rigorous. **GAP-UB** (general non-bisection Xiang
upper-bound strategy) is owned by the dyadic-discrepancy approaches.

## Promotable lemmas
- **Super-level reduction of the merged-order signed sum (NEW, round 6 — fully proved, reusable).**
  For any `F=Y⊎Z`, set `M=N_Y−N_Z`, `A_k={M≥k}`, `B_k={M≤−k}`. Using `ψ(c)=−2⌊c⁺/2⌋+2⌈c⁻/2⌉` one has
  the exact identity `D(F)−(sum(Y)−sum(Z)) = 2( Σ_{j≥1}|B_{2j−1}| − Σ_{j≥1}|A_{2j}| )`. In particular,
  in integer Case-B units (`sum(Y)−sum(Z)=1`), `D̃≥1 ⟺ Σ_j|B_{2j−1}|≥Σ_j|A_{2j}|`. Also
  `A_{2j}⊆{N_Y≥2j}` gives `Σ_j|A_{2j}|≤Σ_j y_{2j}` (deficit budget), and `y₂≤θ` localizes the deficit
  to `(0,θ)`. *Proved in §5D (B1),(B2); 0 violations over 3·10⁵ configs.* Converts the `ψ`-weighted
  signed sum into a monotone super-level count. (Good `lemmas/` candidate: `super-level-reduction.md`.)
- **Lemma G (greedy claiming / odd-rank value).** For a fixed multiset sorted
  `a_1≥…≥a_m`, the alternating claim game value for the first player is the odd-rank sum
  `a_1+a_3+…=(1+D)/2`, `D=a_1−a_2+a_3−…`; greedy (take-largest) is optimal for both.
  *Proved in full in §1.* (Shared spine for all approaches → `lemmas/greedy-claim.md`.)
- **Level-Measure Formula.** `D = λ{ t>0 : #(parts > t) is odd }`. *Proved in §2.*
  Corollaries (F1) `D ≥ (a_max−1/2)^+`, (F2) `λ{N≥j}=a_j`.
- **Cut-Flip Lemma.** Replacing part `ℓ` by `x≤ℓ−x` flips the parity of `N(t)` exactly on
  `[0,x)∪[ℓ−x,ℓ)`; consequently bisecting a set `S` of Liu's pieces yields discrepancy
  `D(T)` for `T=S^c`. *Proved in §3.* (Basis of the refutation of bisection-only Xiang.)
- **Threshold block-decomposition + (★★) bound (round 2 — fully proved, reusable).**
  For a multiset `F = Y ⊎ Z` with all of `Z ⊆ (0,θ]` (so `O_Z ⊆ (0,θ)`), split `O_Y` at `θ`
  into `O_Y^>=O_Y∩[θ,∞)`, `O_Y^<=O_Y∩(0,θ)`. Then the discrepancy satisfies the **exact identity**
  `D(F) = λ(O_Y^>) + λ(O_Y^<) + λ(O_Z) − 2λ(O_Y^<∩O_Z)` and the **bound**
  `D(F) ≥ λ(O_Y^>) + | λ(O_Y^<) − λ(O_Z) |`. *Proved in §5B, verified numerically (0 violations,
  3·10^5 trials).* Reusable by any approach splitting a dyadic into a dominant top block and a
  low sub-block. (Good `lemmas/` candidate: `threshold-decomposition.md`.)
- **Difference-function reformulation + Sufficient Lemma (NEW, round 4 — fully proved, reusable).**
  For any `F = Y ⊎ Z`, set `h(t) := N_Y(t) − N_Z(t)`. Then `D̃(F) = λ{t : h(t) odd}` and
  `∫₀^∞ h = ΣY − ΣZ`. **Sufficient Lemma:** if `|h(t)| ≤ 1` a.e., then
  `D̃(F) = ∫h + 2λ{h=−1} ≥ ∫h`, with equality iff `λ{h=−1}=0`. *Proved in §5C (R1),(R2); 0 violations
  over 41814 `|h|≤1` configs.* A clean, equality-robust per-config lower-bound certificate whenever
  two multisets' count functions differ by at most one level. (Good `lemmas/` candidate:
  `difference-function-bound.md`.)
- **Fragment-count obstruction (NEW, round 4 — fully proved).** If `Y` has `≤ p` parts and `Z` has
  `q` parts, then `h(0⁺) = |Y|−q ≥ −q`, more precisely `N_Y(0⁺)−N_Z(0⁺) = |Y|−|Z|`; so `Y` cannot
  track `Z` within one level near `0` once `|Z| ≥ |Y|+2`. In the dyadic Case B this forces `|h|≥3`
  near `0` for `b≥2`, proving the `|h|≤1` route (and any `Y`-only exchange) cannot close GAP-LB′
  there. *Proved in §5C (R4).* Documents precisely why `Z`'s recursive structure is indispensable.
- **Half-total single-crosser identity (NEW, round 3 — fully proved, reusable).** If a multiset
  `Y` of positive parts has total `S` and `θ = S/2`, then at most one part of `Y` exceeds `θ`
  (two would sum to `> S`), so for any disjoint `Z ⊆ (0,θ]` the combined odd-set `O=O_Y△O_Z`
  satisfies `λ(O ∩ (θ,∞)) = (y₁ − θ)⁺` where `y₁=max Y`; consequently the discrepancy of `Y⊎Z`
  obeys `D(Y⊎Z) ≥ (y₁ − θ)⁺`. *Proved in §5B (◇),(◇◇); 0 violations over 2·10⁵ trials.* This is a
  sharp, cancellation-free lower bound whenever the dominant block's largest fragment clears its
  own half-total by ≥ the target. (Good `lemmas/` candidate.)
