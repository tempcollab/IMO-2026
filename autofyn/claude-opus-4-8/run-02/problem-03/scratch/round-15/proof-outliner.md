## imo-2026-03

### Cheap-kill results this round (exact `Fraction`, ~30k valid feasible Case-B configs per n=2..6)
Ran the overlap-tree explorer's mandated discipline BEFORE committing any slug. All results decisive:
- **Q ≥ Σ z_{2k−1}** (odd-ranked values of F', the flagged "NEG dual to POS"): **FALSE 100%** of trials, all n. Worst deficit grows with n (−43 at n=6). Structural reason: `Q` is the negative part of `M=N_{π₀}−N_{F'}`; a lower bound on `Q` cannot drop `N_{π₀}` (dropping `N_{π₀}≥0` gives an UPPER bound on `Q`, the wrong direction). The pure "F' values alone" dual is dead.
- **Q ≥ Σ z_{2k}** (even-ranked values of F'): FALSE 66–89%.
- **Q ≥ Σ y_{2k}** (π₀'s even-ranked values, the POS values): FALSE ~70%.
- **Termwise `Q_k ≥ P_k`**: holds 99.7% but FAILS (88/64/73/236 of 30k) — not clean.
- **Tail-sum `Σ_{k≥j}Q_k ≥ Σ_{k≥j}P_k`**: holds n≤5, FAILS at n=6 (162), including on a **b=0 base config** (π₀=[8,7,8,5,5,17,14], F'=uncut ladder) — so even the PROVEN slice violates layer-tail domination.
- **Prefix-sum domination**: FAILS (50–101 per n).
- **`Q ≥ P` / `I_n ≤ 0` itself: 0 violations, all n** (target confirmed true).

**Verdict for the reviewer:** the flagged value-ranked NEG-lemma opening is a cheap-kill FAILURE, and this compounds the game-explorer's independent finding that any per-scale/per-rung additive NEG bound is dead (cross-rung non-additive, gap 6.5). No clean termwise / tail / prefix / value-ranked layer statement closes `Q≥P`: the wall is irreducibly GLOBAL cross-layer cancellation coupling π₀ and F'. Do NOT seed the raw NEG-lemma slug. The two productive routes are (1) the certified **BO−RE ladder engine** — the one mechanism that has ever injected the ½ — generalized from blue=L to blue=refinement-of-L, and (2) a genuinely different split (bottom-band). Field below.

---

ladder-length-deficient-induction: revise
Target: the whole b-lift — `D̃(π₀ ⊎ F') ≥ 1` for ANY π₀ (Σ=2^n, ≤n+1 parts) and ANY dyadic refinement F' of the ladder L_n (Σ F'=2^n−1, all parts ≤ θ=2^{n−1}). Closing this + certified UB + Case A + (★) = `solved`, c(n)=2^n/(2^{n+1}−1).
Technique: generalize the CERTIFIED mutual induction `(P_m)/(Q_m)/(LB_m)` (base-slice-star.md) — which proved (★) for blue = UNCUT ladder — to blue = an arbitrary refinement of the ladder. The spine is the ladder-interleaving accounting `Δ_m = BO − RE` (Lemma 0), which holds for ANY blue multiset, not just L; the b-lift is exactly `BO ≥ RE` in the descending merge of red π₀ against blue F'. Reuse the `(I4)` D̃-Lipschitz collapse (the ½-injector) unchanged.
Skeleton:
  1. Recolor: red = π₀, blue = F'. By Lemma 0 (generalized, blue-agnostic), `D̃(π₀⊎F') = 1 + 2(BO−RE)` where BO = blue(F')-odd-rank sum, RE = red(π₀)-even-rank sum in the descending merge. Target ⟺ `BO ≥ RE`. — by ladder-interleaving-identity.md + Lemma 0.
  2. Strong induction on ladder length m (=n) AND on the number of cut rungs. Peel the top blue rung of F'. Two cases:
     (a) top rung UNCUT (single part θ): apply certified `(I1)` `D̃(R⊎L_m)=θ−D̃(R⊎L_{m−1})` verbatim → reduces to blue = refinement of L_{m−1}, same reds. This is precisely the base engine's Branch-2 step.
     (b) top rung CUT into ρ={p_1≥…≥p_r}, Σρ=θ, r≥2, parts <θ: peel via certified top-peel-general `D̃(P)=max(P)−D̃(P∖max)` (top-peel-general.md) applied to the merged multiset, isolating ρ's parts as extra blue elements sitting below any π₀-part >θ. — by top-peel-general.md.
  3. Prove the generalized deficient-LB `(P_m^{cut})`: with a cut top rung, the correction to `BO−RE` versus the uncut case is a signed sum over the ranks between ρ's fragments; show it is ≥ the incurred deficit, closing via the `(LB_m)` Lipschitz collapse on the RESIDUAL ladder L_{m−1} (shrink its reds' total by the ε needed to hit a threshold — the certified crux move). — by (LB_m)/(I4).
  4. Ground at m=1 and at "all rungs cut" (blue fully atomized): the endpoint reduces to a finite BO−RE check; base m=1 casework as in base-slice-star.md.
Key lemmas (claim + mechanism):
  - Generalized Lemma 0 `Δ = BO−RE` holds for blue = F' (any refinement), not only L — because its proof only subtracts the colour-sign sum `Σ τ_j w_j = ΣR−ΣF'` from `D̃=Σ(−1)^{j−1}w_j`, using `s_j−τ_j∈{0,±2}`; nothing there requires blue to be the uncut ladder.
  - Cutting a blue rung ρ (Σρ=θ) shifts only the ranks of merge-elements lying strictly between p_1 and p_r; the parity-flip set is LOCAL to that value window — because inserting r−1 extra blue elements between p_1 and p_r shifts lower ranks by a fixed count, flipping odd/even only there. This gives an EXACT correction term, not a lossy Lipschitz merge.
  - The `(I4)` Lipschitz collapse still injects the ½: any deficient sub-total is pushed to its tight threshold by an ε-shrink, incurring only −ε — reusable verbatim on the residual ladder.
Open gaps: Step 3 — proving the cut-rung correction term ≥ incurred deficit uniformly (the generalized `(P_m^{cut})`), and confirming `(Q_m)`'s complementary UB survives a cut blue rung (the part-cap ≤2^m was load-bearing; check it under cutting). This is the real content the builder fills.
Cases to cover: (a) uncut top rung; (b) cut top rung r=2; (b′) cut top rung r≥3; plus a part of π₀ exceeding θ (use certified `(I2)/(I3)` red-peel first). Endpoint "all rungs atomized".
Watch out for: do NOT collapse to a single-rung Lipschitz MERGE of ρ→θ (value change 2(θ−p_1) is too big, loses the ½ — matches the R12/R14 refutations and the game-explorer's cross-rung non-additivity). The correction MUST be the exact local rank-parity term (Step-3 mechanism), not a continuity estimate over a whole rung. Do NOT hold π₀ fixed as a monovariant (banned) — here π₀ is inert "reds" inside a structural induction, which is different.

---

bottom-band-peel-induction: new
Target: the whole b-lift — `D̃(π₀⊎F') ≥ 1` for all feasible (π₀,F'), same as above.
Technique: a genuinely different SPLIT — peel the BOTTOM (smallest) scale instead of the top. Split `F = F_{≤τ} ⊎ F_{>τ}` at a small dyadic threshold τ. Motivation (R7/R8, reconfirmed by the game-explorer): the `+1` surplus provably CONCENTRATES in the near-0 count-parity band, and near t→0⁺ the odd-set indicator is governed by the TOTAL part count parity, which the certified odd-total Parity Lemma controls exactly. This is far from every banned route: all prior peels/comparisons were top-scale (π₀ fixed); the bottom split has never been tried and routes the `+1` through the Parity Lemma directly rather than a π₀-vs-F' overlap.
Skeleton:
  1. Certified peel identity for the bottom split: `D̃(F) = D̃(F_{>τ}) + D̃(F_{≤τ}) − 2λ(O_{F_{>τ}} ∩ O_{F_{≤τ}})` (peel-difference-bound.md, proven for ANY disjoint split). — by peel-difference-bound.md.
  2. Near-0 control: on `(0, z_min)` (below the smallest part), `N_F(t)=|F|` constant, so the near-0 contribution to D̃ is `z_min · 1[|F| odd]`; more generally the low-t band's odd-set is fixed by cumulative count parities, which the Parity Lemma pins (integer multiset, odd total 2^{n+1}−1 ⇒ D̃ odd). — by parity-odd-total.md.
  3. Choose τ so that `F_{>τ}` is again a feasible smaller instance (a refinement of a shorter ladder against a rescaled π₀), apply the induction hypothesis `D̃(F_{>τ}) ≥ 1`, and bound the bottom-band overlap `λ(O_{F_{>τ}} ∩ O_{F_{≤τ}})` above using that `F_{≤τ}` consists only of the smallest fragments (each < τ, so their odd-set lives in `(0,τ)` where `N_{F_{>τ}}` is at its MAXIMUM = fixed count). — induction + measure bound on a bounded band.
Key lemmas (claim + mechanism):
  - Bottom-band overlap is bounded by the count parity, not a free geometric overlap — because every part of `F_{≤τ}` is `<τ`, so `O_{F_{≤τ}} ⊆ (0,τ)`, and on `(0,τ)` `N_{F_{>τ}}` equals the fixed number of parts `>τ`; the intersection measure is then a parity-weighted length, controllable by the exact fragment count (uses the per-rung exact sums non-locally, not a scalar).
  - Parity Lemma supplies the `+1` in the band where it provably lives — because the surplus concentrates near 0 (R7/R8) and `D̃` is odd (odd total) ⇒ `D̃≥1` once `D̃≥0` locally.
Open gaps: Step 3 — showing `F_{>τ}` is a bona-fide smaller feasible instance (the rescaling), and the quantitative bottom-band overlap bound. CHEAP-KILL FIRST (builder, before proving): numerically test `λ(O_{F_{>τ}}∩O_{F_{≤τ}}) ≤ (D̃(F_{>τ})+D̃(F_{≤τ})−1)/2` for the bottom split at the natural τ (=1, or the smallest ladder scale) over a few thousand exact-`Fraction` configs; if it fails badly like the top-split union bound did, retarget τ or retire.
Cases to cover: τ chosen at the unit scale vs a higher small scale; |F| even vs odd; whether `F_{>τ}` keeps ≤ n+1 top parts.
Watch out for: the game-explorer proved ALL splits hit an overlap term — so this is NOT a free escape. It survives only if the bottom-band overlap is genuinely easier (bounded by fixed count parity on a short interval) than the top overlap. If the cheap-kill shows the same non-additive blowup, this collapses to the shared wall — retire promptly, do not force it.

---

peel-scale-rank-induction: advance
Target: the whole b-lift via `I_n = P − Q ≤ 0` (the leader's certified FLOOR/POS reduction).
Technique: keep the certified `I_n=P−Q` layer reduction (floor-half-reduction.md) with `P ≤ Σ_{k≤K₀} y_{2k}` (positive-layer-localization.md), but attack `Q ≥ P` with the ONLY shape my cheap-kills leave open: a GLOBAL cut-tree-guided matching, NOT termwise/tail/value (all refuted above). Advance = keep this slug live as the machinery home; lower build priority than the ladder revise.
Skeleton:
  1. Import certified `I_n=P−Q`, POS bound `P ≤ Σ_{k=1}^{K₀} y_{2k}` (tight). — floor-half-reduction.md + positive-layer-localization.md.
  2. Build an explicit injection from POS's tight witnesses (the `2k` parts of π₀ above each t forcing `M≥2k`) to DEEPER negative-layer mass of F', using that F' refines the ladder and each rung sums EXACTLY to 2^{n−j} (the game-explorer's finding: this exact-sum structure supplies ~60% of the +1). The matching must cross layers (termwise fails) and cannot be additive per rung (cross-rung gap 6.5). — global charge on F''s cut-tree.
Key lemmas (claim + mechanism):
  - When π₀ has `2k` parts above t (making `M(t)≥2k`, a POS-tight point), the complementary mass forces F' to carry compensating cut-fragments at deeper scales — because `Σπ₀=2^n=2θ` and `ΣF'=2^n−1` are pinned, so π₀ concentrating mass high forces F' mass low, i.e. more small parts ⇒ deeper negative layers. This is the coupling the naive F'-only NEG lemma missed.
Open gaps: the injection/matching itself (the shared wall). Fully open — this is the hardest of the three; keep live for machinery, but the ladder revise is the primary bet.
Cases to cover: none new (inherits the reduction).
Watch out for: do NOT re-propose any termwise / tail / prefix / value-ranked bound (ALL cheap-killed this round — cite the results above). Do NOT use the banned (NEG) `Q≥S_π`, scalar-b, π₀-fixed, merged-order, or ABSORB moves. Only a genuinely global cut-tree matching qualifies; if the builder cannot make the injection concrete, this stays partial (no forced RETHINK — it is honestly the shared wall).

---

### Retire / park
- split-rung-mutual-induction, absorb-rescale-induction: DEAD R14 (both re-encode the certified overlap wall; banked lemma top-peel-general.md). Do not rebuild.
- coupled-cut-descent: DEAD R12 (single-cut b-descent refuted n=5).
- allocation-vertex-corner: DEAD engine R11 (φ(b) pruning refuted; positive-layer lemma banked).
- ladder-abel-pairing: parked exact-(★) hedge, no longer needed ((★) certified) — retire.
- dyadic-discrepancy / dyadic-discrepancy-euclid: UB reference (certified), do NOT rebuild.

### Suggested build set
ladder-length-deficient-induction (primary), bottom-band-peel-induction (far-apart new), peel-scale-rank-induction (machinery/advance). Reviewer to prune to avoid single-gap redundancy — the three are on DIFFERENT reductions (BO−RE ladder vs bottom split vs P−Q layers) so they do not die together.
