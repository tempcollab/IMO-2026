## imo-2026-03

Situation: both walls narrowed to ONE residual sub-case each, and each residual now has
TWO genuinely-distinct closing mechanisms available (per the R6 explorer gates). The field
puts two rival mechanisms on EACH wall so neither wall plateaus on a single idea (per my
round-4 memory rule: when no orthogonal top-level route exists, install two distinct
MECHANISMS on the same residual). potential-certificate stays retired (near-duplicate,
separable-potential dead-end banked). The near-duplicate twins (dyadic-discrepancy-euclid,
induction-recursion) are REPOINTED to a distinct mechanism, not retired — each carries a
different closing idea from its live sibling.

GAP L residual = merged-order (♦) sum with a `maxc≥2` T-run; target NON-STRICT `D̃≥1`
(equality attained at exact ties — the round-4 "strict slack ≥1.017" was a finite-sampling
overclaim). GAP U residual = RT(k) sub-case (iii-b) `ℓ₁<Σ/2`.

---

induction-recursion-telescope: advance
Target: The full LOWER bound of P3 — Liu's dyadic partition forces `D̃≥1` (i.e. `D≥u_n`)
  against EVERY Xiang ≤n-cut response; closes Case B residual `maxc≥2`, completing GAP L.
Technique: Two-level strong induction on `n` with the IH on `Z` STRENGTHENED from the scalar
  `altsum(Z)≥1` to a per-scale ANCHOR-RESERVE certificate carried down `Z`'s dyadic cut-tree
  (reserve-buffer / disjunctive-invariant pattern; structural analogue = crux aimo-0493's
  per-dyadic-scale tag). Spine = the certified (♦) merged-order signed sum `D̃−1=Σψ(c_i)Δw_i`
  + the Structure Lemma (§5, promote to lemmas/).
Skeleton:
  1. Import (♦): `D̃−1 = Σ_i ψ(c_i)Δw_i`, `ψ(c)=1[c odd]−c`, `ψ(c)≥0⇔c≤1` — by Lemma T machinery (certified termwise-lattice.md).
  2. Residual is exactly `(GAP-LB′-run)`: `Σ_{c_i≥2}(c_i−1[odd])Δw_i ≤ Σ_{c_i≤0}(1[odd]−c_i)Δw_i` (T-run deficit ≤ anchor surplus) — by (♦) restricted to sign of `c_i`.
  3. Tie-normalization (PRECISION FIX, do first): define `c_i` with the canonical Y-before-Z tie-break; prove the (♦) sum is tie-break-INVARIANT (equal-value T/B pieces span a `Δw=0` interval, contribute 0) — by construction; then fold the exact-tie boundary `y₁=θ` into the ALREADY-CLOSED region `y₁≥2^{n−1}` (Half-total single-crosser (◇◇)), so the open residual is `maxc≥2` with strict `y₁<θ`. Target the non-strict `≥`, equality tracked.
  4. Structure Lemma split at `θ/2=2^{n−2}`: `Z = Y'^{(0)} ⊎ Z'`, where `Y'^{(0)}` = fragments of `Z`'s top piece `θ` and `Z'` = a ≤(n−2)-cut response to `S_{n−2}` living in `(0,θ/2]` — certified §5.
  5. Anchor-domination descent: match each maximal T-run above `θ/2` against `Z`'s top anchor (uncut `θ`, or its `Y'^{(0)}` fragments), and each T-run below `θ/2` against `Z'` by the strengthened IH one level down — by the reserve certificate (HARD step below).
  6. Base: uncut top anchor `z₁=θ>y₁` opens the merged order with `c_1=−1` over width `θ−y₁`, banking surplus `+2(θ−y₁)` (≥ any single-run deficit at that scale) — direct.
Key lemmas (claim + mechanism):
  - Reserve-carry IH `P*(n)` — because a scalar `altsum(Z)≥1` is provably insufficient (3 counterexamples on record), the IH must carry, for every threshold `τ`, a LOCAL reserve `R_Z(τ) := Σ_{i:c_i(Z)≤−1, w_i>τ} Δw_i` (the width `Z`'s own alternating structure banks above `τ`), and assert `R_Z(τ) ≥` the maximal T-run deficit any intruder set `Y` of ≤(remaining budget) fragments can create above `τ`. The descent at `θ/2` hands `Z'`'s reserve down one scale; the anchor `θ` supplies the top-scale reserve. This is the exact per-scale certificate that survives interleaving, unlike a scalar.
  - Equality-robustness — because `ψ(c_i)Δw_i=0` on strict-alternation prefixes, `D̃=1` is attained only at tie configs continuous with the closed boundary; the bound is `≥` with equality, NOT a universal strict margin.
Open gaps: Step 5 — proving the reserve IH `P*(n)` closes under the Structure-Lemma descent
  (that each T-run's width-weighted deficit is dominated by the matched anchor subtree's banked
  reserve). This is THE remaining lower-bound gap.
Cases to cover: (a) `Z`'s top piece `θ` uncut (base anchor, width `θ−y₁`); (b) `θ` cut into
  `Y'^{(0)}` (recurse the reserve into the fragment group); (c) exact-tie boundary `y₁=θ`
  (folded into closed region, step 3); (d) multiple disjoint T-runs (sum the per-run matches).
Watch out for: (1) do NOT assert a universal strict slack `>1` — infimum is exactly 1 (tie
  configs e.g. n=4, Y=(8,3,3,2), Z=(8,2,2,2,1), `D̃=1`); prove non-strict. (2) A T-run of
  near-EQUAL top values has tiny internal width (deficit ~0) — the reserve match must be
  width-weighted, not count-weighted. (3) Do NOT summarize `Z` by any aggregate — go through
  the Structure Lemma. (4) The old probe_runcase.py has the `gen_Z(n-1,·)` bug (drops `Z`'s
  top anchor `2^{n-1}`); use `gen_Z(n,·)` for any numeric check.

---

induction-recursion: revise (repoint — exchange route is dead; install the budget-count mechanism)
Target: SAME full lower bound / Case B residual `maxc≥2` (`D̃≥1`), by a DIFFERENT closing
  mechanism than telescope's recursive descent — a global combinatorial budget count.
Technique: Pigeonhole / extremal budget count on the (♦) merged-order form, NOT recursion.
  (The prior exchange/difference-function `h` route is PROVEN unable — fragment-count
  obstruction `h(0⁺)≤1−2b≤−3` for `b≥2`, R4; that framing is retired. This revise keeps the
  slug but swaps in the budget-count on (♦).)
Skeleton:
  1. Import (♦) + linear bounds: for `c≥2`, `ψ(c)=1[c odd]−c ∈ [1−c, −1]` (deficit grows only
     linearly in `c`); for `c≤0`, `ψ(c)=1[c odd]−c ≥ |c|` (surplus) — direct from `ψ`'s form.
  2. Deficit budget: every maximal T-run raising `c` from 1 to a peak `p` consumes `≥ p−1`
     top-fragments; total top-fragments `|Y|=a+1`, so `Σ (run peak−1) ≤ a`. Hence the TOTAL
     run-count/height is capped by the top cut budget `a` — by counting T's.
  3. Anchor budget: `Z` has the Structure-Lemma anchors; the number and heights of `Z`'s
     dyadic anchors above any level are fixed by `Z`'s cut budget `b` and `a+b≤n`.
  4. Width-weighted domination: `Σ_{c_i≥2}(c_i−1[odd])Δw_i ≤ Σ_{c_i≤0}(1[odd]−c_i)Δw_i` by
     pairing each T-run's width against the width to the next `Z`-anchor above it — HARD step.
Key lemmas (claim + mechanism):
  - Run-cost bound — because each excess `+1` of `c` beyond the alternating baseline is a T with
    no matching B before it, and the ≤n budget gives `|Y|=a+1`, `|Z|` counts with `a+b≤n`, the
    number of "unbalanced" T's is `≤ a` and every one must be capped above by a `Z`-anchor (else
    `c` never returns to ≤1, contradicting `∫M=1>0`, i.e. `c` ends at a bounded value).
  - Width-aware pigeonhole — because a near-equal T-run has near-0 deficit width, the deficit is
    `Σ (peak−1)·(run width)` and each run width `≤` the gap to the next `Z`-anchor, so the
    surplus `Σ|c_i|Δw_i` over the anchor excursions dominates term-by-term via the dyadic
    geometry of anchor heights (Structure Lemma).
Open gaps: Step 4 — the width-weighted counting inequality. Distinct from telescope's gap:
  here it is a ONE-SHOT global count (runs vs anchors bounded by `a+b≤n`), not a recursive
  descent, so the two slugs cannot die on the same wall together.
Cases to cover: single T-run; multiple disjoint T-runs; the `b=0` sub-case (all budget on top,
  `Z` = uncut `{1,…,2^{n−1}}` — pure anchors, easiest); `a+b=n` tight-budget boundary.
Watch out for: same non-strict/tie discipline as telescope (equality at ties). Do NOT let the
  count ignore widths (a pure count of runs vs anchors is FALSE — the explorer's near-equal-run
  counterexample-to-scalar shows widths are load-bearing). Must still invoke the Structure Lemma
  for anchor heights; a scalar/count summary of `Z` alone is refuted.

---

dyadic-discrepancy: advance
Target: The full UPPER bound of P3 — every Liu partition admits a ≤n-cut Xiang response with
  `D≤u_n`; closes RT(k) sub-case (iii-b) `ℓ₁<Σ/2`, completing GAP U.
Technique: Induction loading (strengthened IH) — pin-top-2 as the first reduction op, composed
  with a two-parameter potential `ψ(k,β)` (β=top fraction) that captures the post-merge
  remainder's own regime, NOT the naive `u_{k−1}·total` bound (which is PROVEN to reduce
  exactly to Case (ii) and fail 100% on the residual).
Skeleton:
  1. Pin-top-2 (op P): pin `ℓ₂` into `ℓ₁`, 1 cut. Effective multiset `R={|ℓ₁−ℓ₂|,ℓ₃,…,ℓ_{k+1}}`
     (`k` pieces), total `Σ'=Σ−2ℓ₂`, budget `k−1` — by IP/generalized-pin (certified).
  2. Show `R` lands in its OWN Case (i)/(ii)/(iii-a) at level `k−1`, so RT(k−1) on `R` gives
     effective total `≤ u_kΣ` — NOT merely `≤ u_{k−1}Σ'` — HARD step.
  3. Chain: (i),(ii),(iii-a) already certified ∀n (Pivot Lemma); only (iii-b) recurses, so the
     strengthened potential `ψ(k,β)` closes by induction on `k` down to the proven `n=1,2`.
Key lemmas (claim + mechanism):
  - Post-merge structural improvement — because the naive bound `u_{k−1}Σ'≤u_kΣ ⟺ 2ℓ₂≥c(k)Σ`
    is exactly Case (ii), the residual `2ℓ₂<c(k)Σ` gains NOTHING from the raw IH; the real
    content is that after merging, either the new top `|ℓ₁−ℓ₂|` or the new second `ℓ₃` is LARGE
    relative to `Σ'=Σ−2ℓ₂` (since `Σ'` shrank by `2ℓ₂`), pushing `R` into its own dominant/
    balanced-top regime where RT(k−1) beats the black-box `u_{k−1}Σ'`. Must be stated as a
    two-parameter potential `ψ(k,β)` with `ψ(k,c(k))=u_k`, `ψ` non-increasing on `β<1/2`, and a
    verified recursion `ψ(k,β) ≥` [pin-top-2 residual expressed in `ψ(k−1,β')`].
  - k=4 near-miss resolution — because a single pin-top-2 has an EXACT near-miss (ratio 1.039
    at `parts≈[0.483,0.168,0.151,0.117,0.081]`), the potential must either (α) add a pin-top-3
    escape branch for that thin region, or (β) split (iii-b) at a secondary threshold; the
    builder MUST reproduce the near-miss (gate2d_residual_region.py) and prove the chosen branch
    kills it — do NOT submit bare single-pin-top-2.
Open gaps: Step 2 — define and verify `ψ(k,β)` (the strengthened potential) closing the
  pin-top-2 recursion below `u_kΣ` on all of (iii-b), INCLUDING the k=4 near-miss branch.
Cases to cover: (iii-b) split by whether post-merge `R` is dominant / balanced-top / still
  balanced; the near-miss thin region as its own sub-case; `ℓ₁=ℓ₂` (free-pair delete, 0 ops).
Watch out for: (1) The naive `u_{k−1}·total` splice is REFUTED (100% fail on residual) — reviewer
  will reject it on sight. (2) "Exclude ℓ₁ only" (bisect largest + recurse) also REFUTED
  (fails even with true-optimal recursion, up to 1.37×). (3) Slack GROWS with `k` (min/u_k up to
  0.76 at k=3, 0.52 at k=5) — no need to chase equality, only a sufficient `ψ`; but `ψ` must be
  sharp at the (iii-a)/(iii-b) interface `ℓ₁↑Σ/2` where slack →0.

---

dyadic-discrepancy-euclid: revise (repoint — accumulator is a duplicate; install the difference-coin mechanism)
Target: SAME (iii-b) `ℓ₁<Σ/2` upper-bound residual, by a DIFFERENT mechanism than pin-top-2 —
  a CONSTRUCTIVE Euclidean descent on pin-created "difference coins."
Technique: Adaptive pivot with pin-created intermediate coins (option (α) named in
  dyadic-discrepancy §4.6): bisect all but a near-equal pair, pin one of the pair into the other,
  residual = their difference; iterate a Euclid-style reduction `ℓ_i mod ℓ_j` to drive the
  reachable effective total below `u_kΣ`. Distinct from pin-top-2's inductive potential — this
  is a direct constructive descent, so the two GAP-U slugs cannot plateau together.
Skeleton:
  1. Enriched coins: legal ops generate, besides `{ℓ_2,…,ℓ_{k+1}}`, the differences `ℓ_i−ℓ_j`
     (pin) and can zero any piece (bisect). Effective total after bisecting all but two pieces
     `P≥p` and pinning `p` into `P` is exactly `P−p` — by IP/pin (certified).
  2. Gap pigeonhole: in region B the `k` pieces below `ℓ₁` span `[ℓ_{k+1},ℓ_2]⊂(0,c(k)Σ/2)`;
     consecutive gaps `Σ(ℓ_i−ℓ_{i+1}) = ℓ_2−ℓ_{k+1} < c(k)Σ/2` — direct.
  3. Euclidean descent: HARD step — exhibit a legal op-sequence realizing a reachable effective
     total `≤ u_kΣ` (either a small consecutive gap, or a chained `mod` reduction of two coins).
Key lemmas (claim + mechanism):
  - Reachable-value existence — because Xiang needs only ONE reachable effective total `≤u_kΣ`
    (not a global mesh bound — the GLOBAL mesh is REFUTED, so do NOT claim it), a constructive
    Euclidean/gap descent suffices: repeatedly replace the two largest remaining coins `P≥p` by
    `P−p` (pin) or delete equal pairs, à la the subtractive Euclidean algorithm, which strictly
    decreases the max coin and terminates at a residual bounded by the finest gap; bound that
    gap `≤u_kΣ` using `k+1` balanced pieces in `(0,c(k)Σ/2)` (pigeonhole on `k` gaps summing to
    `<c(k)Σ/2`, giving a gap `<c(k)Σ/(2k)`; compare to `u_kΣ` — verify the constant).
  - Near-equal-pair base — because the explorer's (iii-b) optima are exactly near-equal-pair
    configs (e.g. `(0.492,0.253,0.252,0.003)` → bisect ℓ₁,ℓ₄, pin ℓ₂ into ℓ₃, residual 0.001),
    the descent's base case is a pair with difference `≤u_kΣ`, reached by the pigeonhole gap.
Open gaps: Step 3 — prove the Euclidean/gap descent always reaches an effective total `≤u_kΣ`
  within the `≤k` op budget (the constant in `c(k)Σ/(2k)` vs `u_kΣ`, and that the descent uses
  `≤k` ops). This is a genuinely different gap from pin-top-2's potential `ψ`.
Cases to cover: pieces with a near-equal pair (base, few ops); pieces with no near-equal pair
  (chained `mod` reduction — the hard case); `ℓ_{k+1}` tiny (bisect it away first).
Watch out for: (1) Do NOT invoke a global mesh-coverage bound — REFUTED (mesh not globally
  `≤u_kΣ`, gaps up to 2×u_k just outside the window). Only a CONSTRUCTIVE single reachable point
  is allowed. (2) Op-budget accounting: bisecting all-but-two costs `k−1` ops, pins cost 1 each
  — a multi-step Euclidean chain may overrun `k` ops; the builder must bound the chain length.
  (3) Region-restricted concavity/LP is DEAD (37–42% violations) — do not detour through it.

build set: induction-recursion-telescope, induction-recursion, dyadic-discrepancy, dyadic-discrepancy-euclid
