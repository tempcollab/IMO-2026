## imo-2026-03

Shared facts (import, do NOT re-prove — certified in `lemmas/`):
- **Lemma R** (`reduction-odd-rank`): claiming value = odd-rank sum; with total 1, Liu = (1+D)/2,
  `D = Σ(−1)^{i+1} b_i ≥ 0`. Whole problem = scalar minimax of D (Liu ≤n cuts to maximise, then Xiang ≤n cuts to minimise). Answer `c(n)=2^n/(2^{n+1}−1)`, target `minimax D = u_n = 1/(2^{n+1}−1)`.
- **Lemma M/I** (`measure-identity`): `D = measure{t : N(t) odd}`, `N(t)=#{pieces>t}`. Corollary: even multiplicity everywhere ⇒ D=0.
- **Lemma T** (toggle calculus): a cut of s into s₁≥s₂ toggles parity of N on `E=[0,s₂)∪[s₁,s)` (measure 2s₂); after cuts with toggle-sets E₁…E_r the final odd-set is `O₀ △ ⨁E_i`, so `D_final = μ(O₀ △ ⨁E_i)`.
- **Lemma P** (`cancelling-pair`): `D(S∪{v,v})=D(S)`; one cut duplicating a value v deletes a cancelling pair (piece count −1, total −2v, eventual D unchanged).

The field bottoms out on the SAME two coupling gaps in every live approach; the two ADVANCE slugs attack them with the *new* moves via **different mechanisms** (net-toggle measure vs. recursion) so they do not die together, and two NEW framings attack the shared wall from genuinely different top-level targets.

Verified this round (arithmetic, exact): multi-pair peel of j cuts closes iff `2r ≥ 1 − u_n/u_{n−j}` where r = matched mass; single-pair (j=1) recovers `2r≥c(n)` (the old (6.1)); dyadic single-match hits it with equality for all n. Also (re-derived, do NOT re-attempt): all-equal profile `a_i=1/(n+1)` is EASY (bisect one piece ⇒ D=0), NOT a hard case; the multiplicative worst-case IH over-estimates it — balanced profiles are the reason a pure "peel + apply worst-case IH" cannot close alone.

---

### parity-measure-potential: advance
Target: c(n)=2^n/(2^{n+1}−1), both bounds, via `D = measure{N(t) odd}` and the net-toggle bookkeeping `D_final = μ(O₀ △ ⨁E_i)` — no induction on n. (Elo 1532, strongest.)
Technique: global measure identity + net symmetric-difference of toggle sets (Lemma T cumulative form). Distinct from the recursion route: everything is a single measure computation on the final odd-set.
Skeleton (only the two open gaps remain; §R,I,T,LB-CaseA,greedy-reduction already proven):
  1. [done] Lemmas R, I, T; lower Case A (top piece uncut ⇒ N(t)=1 on length-u interval ⇒ D≥u).
  2. UPPER (gap B3), net-toggle subset matching: for Liu's a₁≥…≥a_m (m≤n+1), choose Xiang's cuts so `⨁E_i` erases all but ≤u of O₀. Realise this by cutting a₁ into fragments each EQUAL to a chosen subset T⊆{a₂,…,a_m} (plus leftover a₁−Σ_T): each matched fragment forms a cancelling pair, and in net-toggle terms `⨁E_i` cancels the odd-set contributions of the matched pieces. Residual odd-measure = measure{N odd} of {a₁−Σ_T}∪(tail∖T); bound it ≤ u.
  3. LOWER (gap B2), measure-charging: for dyadic O₀ (pieces 1,…,2ⁿ, units u), each of Xiang's ≤n cuts contributes a toggle set E_i of measure 2s₂^i; show the total measure that `⨁E_i` can remove from O₀ telescopes to ≤ (μ(O₀) − u). Track toggled MEASURE, not band count (a single cut's E_i spans several dyadic bands — the naive "1 cut kills 1 band" pigeonhole is FALSE, per Lemma T).
Key lemmas (claim + mechanism):
  - Subset-match cancellation — because a fragment of a₁ cut to exactly a_i's value creates {a_i,a_i}, whose net toggle over the pair is empty (Lemma P / two consecutive ranks cancel), so `⨁E_i` deletes exactly those pieces' parity contribution; the residual odd-set is that of the reduced multiset.
  - Charging bound — because by Lemma T the symmetric difference can shrink O₀ by at most μ(⨁E_i) ≤ Σ 2s₂^i, and for the superincreasing dyadic O₀ any cut large enough to erase the top length-u block must simultaneously CREATE a length-≥u odd block below it (the fragment s₂ re-toggles a lower band), so net erasure ≤ μ(O₀)−u.
Open gaps: B3 (choice of subset T for arbitrary profile — see subset-cover lemma below; note balanced profiles need bisection, not matching); B2 (make the "erase-top-creates-block-below" charging quantitative and telescoping).
Cases to cover: B2 — Xiang cuts top piece once / several times / cuts create fragments spanning multiple bands. B3 — a₁ dominant (a₁>Σ rest) vs a₁ balanced (a₁≤Σ rest).
Watch out for: net (not gross) toggling — overlapping E_i cancel; do not double-count. The charging must bound the SYMMETRIC-difference shrinkage, not Σ|ΔD| per cut.

### induction-peel: advance
Target: c(n)=2^n/(2^{n+1}−1) for every n, by strong induction on n via `u_n = u_{n−1}/(2+u_{n−1})`. (Elo 1499.)
Technique: recursive peeling. NEW this round: replace the single cancelling-pair peel (proven to stall when max(a₁,2a₂)<Lc(n)) by a **multi-pair subset peel** (reduce UB(n)→UB(n−j) in one shot), and close lower Case (b) by a **shadow-coupling map** (one-directional inequality, aimo-0663 crux) rather than forcing a clean recursion.
Skeleton (§1–4 base/recursion + LB Case (a) + UB dyadic already proven):
  1. [done] Lemmas R,M,P; recursion; base n=0,1 both directions; LB Case (a); UB single-peel on dyadic (tight).
  2. UPPER (gap U), multi-pair subset peel: given a₁≥…≥a_m (m≤n+1, sum L), pick j and T⊆{a₂,…,a_m}, |T|=j, Σ_T≤a₁; cut a₁ into the |T| values of T + leftover a₁−Σ_T; delete the j cancelling pairs (Lemma P). Residual: {a₁−Σ_T}∪(tail∖T), m−j ≤ (n−j)+1 pieces, total L−2Σ_T, budget n−j. Apply UB(n−j): D ≤ u_{n−j}(L−2Σ_T) ≤ u_n L iff `2Σ_T ≥ L(1−u_n/u_{n−j})` (verified: dyadic hits equality; the balanced case where matching cannot reach the threshold is handled by the BISECT branch — bisect a piece to D-collapse, see subset-cover lemma).
  3. LOWER (gap L), shadow coupling: define a value-level map φ from a Case-(b) residual (Xiang cut top piece P) to a clean order-(n−1) dyadic-tail configuration, and prove the one-directional transfer `D(actual residual) ≥ D(φ(residual))` via Lemma T net-toggle, then apply LB(n−1)/Case (a) to φ(residual). Only an inequality is needed (the extremal Xiang set is a flat family, so exact matching is unnecessary — confirmed numerically min D=1 for n≤3 even under forced non-bisecting top cuts).
Key lemmas (claim + mechanism):
  - **Subset-cover feasibility (KEY, gap):** for every sorted profile there is a legal choice — either (matching) j and T with `2Σ_T ≥ L(1−u_n/u_{n−j})`, Σ_T≤a₁, OR (bisection) a piece whose deletion drops residual mass enough — because a₁ is the largest so a₁≥L/(m)≥L/(n+1); when a₁≥Lc(n) bisect a₁ closes directly, when a₁ dominant (a₁>Σrest) matching the top-fitting tail subset closes, and when balanced (a₁≤Σrest, a_i comparable) a single bisection already even-pairs the count toward D→0. The gap is proving the disjunction is exhaustive.
  - **Shadow map φ (KEY, gap):** because cutting P into p₁,p₂ and re-sorting only permutes ranks below p₂ up by ≤2 and above p₁ down; the odd-set of the true residual dominates that of φ (the tail with one scale removed) since the top-fragment toggles cover a superset of the discarded scale's block — "cutting a scale costs that scale."
Open gaps: U (subset-cover feasibility disjunction is exhaustive); L (construct φ + prove one-directional D-inequality).
Cases to cover: U — a₁≥Lc(n) / a₁>Σrest (dominant) / a₁≤Σrest (balanced). L — top piece cut once / multiple times / descendant cut.
Watch out for: residual piece-count must stay ≤(n−j)+1 for UB(n−j) to apply (it does: m−j≤n+1−j). The multiplicative IH over-estimates balanced profiles — do NOT try to close balanced profiles by matching alone; use bisection/parity-collapse there.

### two-box-balancing: new
Target: c(n)=2^n/(2^{n+1}−1), BOTH bounds unified, as the exact value of a two-box balancing game (adapts crux **aimo-0117**).
Technique: reformulate `D = |O|−|E|` where O=odd-rank box, E=even-rank box, box membership fixed by sorted rank. Liu = constructor committing pieces, Xiang = corrector with ≤n cuts rebalancing the two boxes. Prove the game value by an invariant induction that tracks "who currently holds the top scale," with a two-case step (top scale touched / untouched) — structurally identical to the still-open Case A/Case B split, but now the SAME device settles both bounds. This is far from both live routes: neither a global measure integral nor a mass-peel recursion, but a scale-by-scale invariant on box balance.
Skeleton:
  1. [import] Lemma R gives D=|O|−|E|. Recast one Xiang cut as: split one committed value, re-sort, possibly moving the top scale between boxes.
  2. Invariant (LOWER, dyadic Liu): maintain "after Xiang's move the largest surviving scale contributes a net +u to |O|−|E| that Xiang cannot cancel without spending a cut that promotes an equally large protected scale below." Two-case induction on whether Xiang's cut touched the current top scale: if untouched, top scale stays in O (Case A, done); if touched, the fragment ≥u re-enters as a new protected top scale one level down — invariant re-established with budget −1. Bottoms out at the base scale u after ≤n cuts ⇒ D≥u.
  3. Invariant (UPPER, arbitrary Liu): corrector strategy — always cut the current top piece to hand the top scale to the box that is currently behind, so |O|−|E| never exceeds the running "top scale" which telescopes (geometric, ratio ≤1/2 by the dominance inequality) to ≤u after ≤n corrections.
Key lemmas (claim + mechanism):
  - Top-scale dominance — because `2ⁿ > 2ⁿ⁻¹+…+1` (superincreasing, (5.1)); the single largest scale outweighs everything below, so whoever holds it in their box controls the sign of |O|−|E| down to the residual ≤u. This is exactly aimo-0117's closing inequality `2^j > 2^{j−1}+…+2^{−i}`.
  - Two-case top-scale induction — because a corrector cut either leaves the top scale (invariant trivially holds) or splits it, and the larger fragment (≥ next scale by dominance) becomes the new top scale, so the invariant recurses with one fewer scale and one fewer budget.
Open gaps: formalise "box the top scale into the lagging box" as a legal ≤n-cut Xiang strategy for the upper bound; verify the invariant survives when a cut's fragment lands strictly between two existing scales (re-sort changes ranks of both boxes).
Cases to cover: corrector moves top scale / leaves it; constructor extends range up vs. down (aimo-0117 mirrors this — here it is Liu's fixed dyadic, so only the corrector branches).
Watch out for: rank re-sorting after a cut flips O/E membership of many pieces at once — the invariant must be stated on SCALES (dyadic bands), not on fixed ranks, or the two-case step breaks. Do not assume the top scale stays rank 1 after a mid-list fragment appears.

### lp-dual-weight: new
Target: c(n)=2^n/(2^{n+1}−1), both bounds from ONE dual object — a fixed threshold weighting / covering certificate.
Technique: LP primal–dual. The lower bound "min over Xiang of D ≥ u" and the upper bound "min over Xiang of D ≤ u for the worst Liu" are dual faces of one linear program in the toggle-set incidence. Exhibit a single certificate w (a fractional covering of thresholds, equivalently a distribution over "protected witness intervals") that certifies both. Genuinely different: no strategy is ever named; the certificate is a static object checked against Lemma T.
Skeleton:
  1. LOWER as covering: O₀ (dyadic odd-set) has measure Σ(−1)…; each Xiang cut i can flip parity only on its toggle set E_i (Lemma T). Dual certificate = a sub-family of disjoint protected intervals of total measure u inside O₀ such that no n toggle sets E_i can simultaneously flip all of them (a Hall/covering feasibility condition: each E_i, being two intervals of equal length pinned by s₂, can "hit" the protected family only at a cost that exhausts budget before reaching measure u).
  2. UPPER as majorization: show the SAME weight makes the dyadic profile the maximiser of V(A)=min_Xiang D over all Liu profiles A (dominant crux **aimo-0560**: replace Liu by the pointwise-strongest surrogate = dyadic). Then V(A) ≤ V(dyadic) = u (already proven tight). Smoothing move: replacing two middle pieces (x,y) by (x+ε,y−ε) toward the 2:1 dyadic ratio does not decrease V, so a finite chain transports the dyadic bound to every A.
  3. Both faces evaluate the same w to u ⇒ minimax D=u ⇒ c(n)=(1+u)/2.
Key lemmas (claim + mechanism):
  - Protected-family non-coverability (KEY, gap) — because each toggle set E_i=[0,s₂)∪[s₁,s) contributes measure 2s₂ but to erase a protected block of the dyadic odd-set it must place s₂ at that scale, which by superincreasingness forces s₁ high and re-creates an odd block of equal measure elsewhere; a fractional covering LP then shows n cuts cover < total−u.
  - Smoothing monotonicity (KEY, gap) — because pushing a profile toward the 2:1 dyadic ratio only enlarges the residual Xiang cannot cancel (dyadic is Liu's pointwise-worst surrogate, aimo-0560); needs an envelope/coupling argument on how Xiang's optimal response moves under the perturbation.
Open gaps: construct the explicit weight/covering w and prove non-coverability (lower); prove smoothing monotonicity toward dyadic (upper).
Cases to cover: lower — cut toggle sets overlapping the protected family partially vs. fully. upper — smoothing step feasible in one direction at every non-dyadic profile.
Watch out for: the LP dual may not have a clean closed form — if the covering certificate resists, fall back to the smoothing/majorization half alone (it already yields the whole upper bound from the proven dyadic case). Do NOT conflate μ(⨁E_i) with Σμ(E_i) — overlaps cancel.
