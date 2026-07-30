## imo-2026-03

Context: SOLE open wall is the b-lift (GAP-P1′-b). Upper bound, lower-bound Case A, and the (★)
base slice (b=0) are ALL PROVEN & certified — NO builder on any of them. Certified machinery to
import: `lemmas/base-slice-star.md` (the `(P_m)/(Q_m)/(LB_m)` engine + peel identities (I1)-(I3) +
D̃-Lipschitz (I4)), `lemmas/floor-half-reduction.md` (FLOOR: Case B ⟺ `I_n=∫_(0,θ)⌊M/2⌋≤0`),
`lemmas/ladder-interleaving-identity.md` ((★-id): `D̃(π_0⊎L_n)=1+2Δ_n(π_0)`),
`lemmas/positive-layer-localization.md` ((POS): `P≤Σ_{k≤K_0}y_{2k}`), `lemmas/peel-difference-bound.md`.

THE fresh, exact new tool this round (both explorers): the **ABSORB identity**, an algebraic
identity for `Δ(A,B):=½(D̃(A⊎B)−ΣA+ΣB)` — verified by hand and 0/2000:
```
   Δ(R, Z) = θ + Δ(R⊎π_1, Z')      whenever   Z = π_1 ⊎ Z',  θ := Σπ_1   (ABSORB, exact, no hyp)
```
It is one level more general than certified (I1) (which assumed the peeled block is the singleton
`{θ}` and every red `≤θ`); here `π_1` may be a SPLIT top rung. This is the natural handle on the
b-lift's core difficulty: F′'s top rung being cut into several parts.

I opened a decisive numeric probe (rescaled deficient bound, exact Fraction, /tmp/probe_rescale.py):
`Δ_m(R)≥min(0,2^m−ΣR)` with parts `≤2^m` and mass `ΣR≤3·2^m` **holds under count cap `#R≤m+1`
(0 fails, m=1..4) and FAILS at `#R≤m+2` (fails at m=1,2,3)**. This pins the exact regime for Route A
and identifies its load-bearing gap (see below).

BANNED / DEAD — do NOT seed (per run_state + this round's multicut report): any π₀-fixed comparison
of two F′ configs (single-cut OR global multi-cut "merge F′ to ladder" — the WHOLE π₀-fixed family
is now REFUTED, 970–2073/3000); single-cut co-varying b→b−1 descent; full-WM/HLP-IH inheritance;
(NEG) Q≥S_π bound; scalar b-cutoff / φ(b); all measure/merged-order/sequential/genfn/GAP-IMR
framings; **naive ITERATION of ABSORB reusing (LB_m) verbatim** (REFUTED 28/10000 — accumulated red
mass outruns the certified domain; use ABSORB ONCE, not down every scale).

---

absorb-rescale-induction: new
Target: Full lower-bound Case B for all n and every dyadic-cut response F′ — i.e. `D̃(π_0⊎F′)≥1`
  (equivalently `Δ_n(π_0,F′)≥0`, `I_n≤0`), which together with the certified UB, Case A, and (★)
  completes the determination `c(n)=2^n/(2^{n+1}−1)`.
Technique: Strong induction on the SCALE n (not on b), using the exact ABSORB identity ONCE per
  step to fold F′'s (possibly split) top rung into the red side, closed by a RESCALED deficient-bound
  theorem at mass `3·2^m`. Distinct from every banned route: it never holds π₀ fixed while varying
  F′ (it transforms BOTH sides simultaneously via an exact identity), never iterates ABSORB, is not
  a monovariant guess.
Skeleton:
  1. Peel structure: `F=π_0⊎F′`, `Σπ_0=2^n`, F′ a dyadic refinement of `L_n`, `ΣF′=2^n−1`,
     `θ=2^{n−1}`. Target `Δ_n(π_0,F′)≥0` — by (★-id)/Lemma 0 generalized to blue = F′.
  2. Write `F′=π_1⊎F″` (Structure Lemma top-peel): `π_1` = the parts of F′ that refine the top rung
     `θ` (`Σπ_1=θ`, `a_1+1` parts if `a_1` cuts spent there), `F″` a refinement of `L_{n−1}`,
     `ΣF″=2^{n−1}−1` — by the certified dyadic Structure Lemma.
  3. ABSORB (once): `Δ_n(π_0,F′)=θ+Δ_{n−1}(π_0⊎π_1, F″)`. Hence target ⟺
     `Δ_{n−1}(R̄, F″) ≥ −θ`, where `R̄:=π_0⊎π_1`, `ΣR̄=2^n+θ=3θ=3·2^{n−1}` — by ABSORB (exact).
  4. This is a scale-`(n−1)` instance of the SAME shape as (★)/Case B but with (a) tripled red mass
     `3·2^m` (m=n−1) and (b) a `−θ` slack, against a ladder-refinement `F″`. Close it by the
     Rescaled Deficient-Bound Theorem (key lemma) — which at `ΣR̄=3·2^m` yields exactly
     `min(0, 2^m−ΣR̄)=2^m−3·2^m=−2·2^m`... [see Watch out: the slack bookkeeping is `−θ`, and the
     rescaled bound must be run against the refinement `F″`, not the full ladder — recover the `−θ`
     target either by (i) a further single (I2)/(I3)-style peel of the one red part `>θ` created by
     absorbing, or (ii) directly proving the rescaled engine for blue=refinement].
  5. Base n=1 by finite casework (as in base-slice §3). Conclude by induction on n.
Key lemmas (claim + mechanism):
  - ABSORB `Δ(R,Z)=θ+Δ(R⊎π_1,Z′)` — because `D̃(R⊎Z)=D̃(R⊎π_1⊎Z′)` (same multiset) and expanding
    `Δ(R⊎π_1,Z′)` with `Σ(R⊎π_1)=ΣR+θ`, `ΣZ′=ΣZ−θ` gives `Δ(R,Z)−θ`. Exact, no hypothesis on π_1's
    shape or dyadicity. (Ready to promote as a lemma; reviewer re-verifies.)
  - Rescaled Deficient-Bound Theorem: for red R with parts `≤2^m`, `ΣR≤3·2^m`, and **count cap
    `#R≤m+1`**, `Δ_m(R)≥min(0,2^m−ΣR)` against `L_m` (and, the version needed here, against any
    ladder-refinement F″) — because the certified `(P_m)/(Q_m)/(LB_m)` engine + D̃-Lipschitz collapse
    (I4) extend to the wider mass window PROVIDED the tight count cap holds. NUMERICALLY PINNED this
    round: 0 fails at `#R≤m+1`, FAILS at `#R≤m+2` — the count cap is load-bearing at rescaled mass.
Open gaps (builder fills):
  - GAP-A1 (the crux): prove the Rescaled Deficient-Bound Theorem at mass `3·2^m` for blue = a
    ladder-refinement F″, under the correct count cap. Re-run the (P_m)/(Q_m)/(LB_m) induction with
    the mass cap widened to `3·2^m`; the Lipschitz collapse (I4) still reduces deficient→tight.
  - GAP-A2 (COUNT-CAP BUDGET — make-or-break): the post-absorb red count is `#R̄=a_0+a_1+2`. Budget
    `a_0+b≤n`, `a_1≤b` give only `a_0+a_1+2≤n+2=m+3`, exceeding the safe cap `#R≤m+1` by up to 2 —
    and the probe shows `m+2` already fails. MUST close this gap: either (i) tighten the budget
    accounting to `a_0+a_1≤n−2` on Case B (Xiang cutting the top rung costs budget that cannot also
    fragment π_0), or (ii) show the `−θ` target slack + F″ being a strict refinement (`ΣF″<` full,
    fewer effective crossings) tolerates the 2-count overage. This is THE gap; flag prominently.
Cases to cover: base n=1; step split on whether the absorbed red part(s) exceed θ (handle via one
  (I2)/(I3) peel as in base-slice §4–§5).
Watch out: the `−θ` slack must be tracked exactly through step 4 (do NOT drop it — it is what makes
  the tripled mass admissible). Do NOT iterate ABSORB (REFUTED). Verify the rescaled engine against a
  ladder-REFINEMENT F″, not only the full ladder, before claiming closure. Re-run probe_rescale.py at
  m=5,6 with a targeted (non-random) adversarial search to confirm the count cap is really m+1 (the
  random sampler saw 0 fails at large m only from undersampling).

---

split-rung-mutual-induction: new
Target: Full lower-bound Case B `D̃(π_0⊎F′)≥1` for all n and every dyadic-cut F′ (same whole claim
  as above), completing `c(n)=2^n/(2^{n+1}−1)`.
Technique: ONE two-parameter mutual induction `(P_{m,k})/(Q_{m,k})/(LB_{m,k})` on (ladder length m,
  blue-split-budget k), whose `k=0` slice IS the CERTIFIED base-slice engine (`base-slice-star.md`) —
  so it never separates the base case from the lift; the whole GAP L is one induction anchored at the
  proven k=0. Distinct from Route A: it keeps the red mass BOUNDED (no absorption into R; the split
  rung stays blue and is peeled in place), carrying the split budget as an explicit parameter.
Skeleton:
  1. Generalize the blue object from the uncut ladder `L_m` to a k-cut ladder-refinement `Z` (top
     rung split into `≤k+1` parts, total budget k of blue cuts across all rungs). Define
     `Δ_m(R,Z)=½(D̃(R⊎Z)−ΣR+ΣZ)` (Route-B blue = Z). k=0 ⟹ Z=L_m ⟹ certified (P_m)/(Q_m).
  2. State `(P_{m,k})` (deficient LB), `(Q_{m,k})` (complementary UB), `(LB_{m,k})` (full deficient
     LB) with the SAME caps as certified plus the split budget k; verify the load-bearing caps
     numerically before building (per role-memory rule R13).
  3. Induction on m. Split on blue's TOP rung: (a) top rung NOT split (its k-budget is 0 there) —
     reduce to `(P_{m−1,k})/(Q_{m−1,k})` by the certified rung-peel (I1)/(I2)/(I3) verbatim; (b) top
     rung SPLIT into `c_1,…,c_{j+1}` (`Σc_i=θ`, `j≥1`) — apply the split-rung-peel identity (I1′)
     to reduce to `(·_{m−1,k−j})` plus a bounded cross-term.
  4. Anchor: `k=0` slice is the certified base-slice theorem (imported, not re-proven). Base m=1 by
     finite casework in k. Take `m=n`, `R=π_0`, k = F′'s cut budget: `(P_{n,k})` gives `Δ_n(π_0,F′)≥0`.
Key lemmas (claim + mechanism):
  - Split-rung-peel (I1′) — THE gap: when the blue top rung is split into `c_1≥…≥c_{j+1}` with
    `Σc_i=θ`, on `(0,θ)` the blue level function is `Σ_i 1[t<c_i]` (a descending STEP function), not
    the single flip `1[t<θ]` of (I1). Mechanism to establish: `D̃(R⊎Z)` relates to `D̃(R⊎Z_{−rung})`
    by toggling parity on the multi-interval set `{t:Σ_i 1[t<c_i] odd}`; the correction versus the
    single-flip (I1) is `Σ_i(−1)^{i−1}c_i = D̃({c_1,…,c_{j+1}}) ≤ θ` — an ALTERNATING sum of the
    split parts (this is exactly the sub-scale discrepancy of the split rung). So (I1′) should read
    `Δ_m(R,Z)=2^m−1−ΣR−Δ_{m−1}(R,Z′)+ (correction in the split parts)`, the correction being a clean
    alternating-sum term bounded by θ. Verify this exact form numerically FIRST (cheap-kill: m=2, j=1).
  - k=0 anchor = certified base-slice-star.md (P_m)/(Q_m). Import, do not re-prove.
Open gaps (builder fills):
  - GAP-B1 (crux): derive and prove the split-rung-peel identity (I1′) with the alternating-sum
    correction term, and prove that correction is absorbed by the deficient bound (the split rung's
    own discrepancy `≤θ` is exactly the slack a length-(m−1) ladder provides).
  - GAP-B2: verify the two-parameter dependency graph `(P_{m,k})←{(P_{m−1,·}),(Q_{m−1,·})}`,
    `(LB_{m,k})←(P_{m,k})`, `(Q_{m,k})←(LB_{m,k})` is non-circular and grounded at (m=1 ∨ k=0).
  - GAP-B3: pin the load-bearing caps of `(P_{m,k})/(Q_{m,k})` by a Fraction sweep before writing the
    proof (the R13 (Q_m) part-cap was false until pinned — same discipline here with k added).
Cases to cover: top-rung-split vs not; within split, number of split parts j; base m=1 and k=0.
Watch out: do NOT let the split-rung correction re-introduce the FLOOR/level machinery recursively at
  the sub-level (circular unless the correction is a closed alternating-sum term, which the mechanism
  above claims it is — this MUST be checked, cheap-kill m=2,j=1, before full build). Mass must stay
  `≤2^{m+1}` (no absorption into R) — that is the whole point vs Route A.

---

peel-scale-rank-induction: advance
Target: Full lower-bound Case B `I_n≤0` for all n / every F′ (this leader owns the FLOOR reduction
  and will ASSEMBLE the final proof once the b-lift closes).
Technique: Close `I_n=P−Q≤0` on the certified FLOOR/layer identity by pairing the certified
  positive-layer bound (POS) with a NEW **recursive intrinsic lower bound on the negative layers Q**,
  obtained by ONE top-peel of F′ and induction on n — never comparing two F′ configs, never a
  π₀-fixed move (both banned). This routes the missing ½ through F′'s recursive dyadic cut-tree
  ORIGIN exactly as the run_state meta prescribes. Genuinely different framing from Routes A/B
  (FLOOR/layer accounting, not the Δ_m ladder functional).
Skeleton:
  1. Certified FLOOR: `I_n=P−Q`, `P=Σ_k λ_(0,θ){M≥2k}`, `Q=Σ_k λ_(0,θ){M≤−(2k−1)}`,
     `M=N_{π_0}−N_{F′}` on `(0,θ)` — import `floor-half-reduction.md`.
  2. Certified (POS): `P≤Σ_{k=1}^{K_0}y_{2k}` (π₀'s even-ranked parts, `K_0=⌊(a_0+1)/2⌋`) — import
     `positive-layer-localization.md`. So it suffices to prove `Q≥Σ_{k=1}^{K_0}y_{2k}`.
  3. NEW recursive Q-bound (the gap): peel F′'s top rung, expressing `Q` at scale n as a contribution
     from the top rung's split parts PLUS `Q` of the scale-(n−1) sub-refinement; induct to bound
     `Q≥Σ y_{2k}` intrinsically. The negative layers are governed by `N_{F′}`; F′'s dyadic origin
     forces enough odd-count band below each y_{2k}.
Key lemmas (claim + mechanism):
  - `Q≥P` via a recursive intrinsic lower bound on Q — because `Q` counts, per even layer `2k−1`, the
    measure where `N_{F′}` exceeds `N_{π_0}` by an odd amount, and F′ refining the ladder forces
    `N_{F′}` to carry at least `y_{2k}` worth of such excess below each even π₀-part (the cut-tree
    origin injects the band non-locally, not via any static profile of F′).
Open gaps (builder fills):
  - GAP-C1 (crux, MEDIUM-HIGH RISK): prove `Q≥Σ_{k=1}^{K_0}y_{2k}` by the recursive top-peel of F′.
    run_state flags the plain positive-layer engine as "dead as engine" because it restated the wall;
    the NEW content that must escape that is the RECURSION on F′'s cut-tree (not a static Q bound).
    If the recursion cannot beat the trivial layer bound (off by ½), this route restates the wall —
    cheap-kill it early: check whether the recursive Q-bound is even TRUE (not just `Q≥0`) on the
    documented tie witnesses (n=4 `F={8,8,5,4,2,2,1,1}`, b=2 tie).
Cases to cover: none beyond the layer index k and the top-rung peel.
Watch out: this is the highest-risk of the three (the static positive-layer engine was already ruled
  dead-as-engine R11); keep it as the DIVERSITY hedge so Routes A/B (which share the ABSORB/split-rung
  wall) do not die together with it. If the recursive Q-bound is refuted on the tie witnesses in the
  first hour, retire and concentrate builder budget on Routes A/B.

---

Parked (certified reference — NO builder, do NOT rebuild): `ladder-length-deficient-induction`
(certified (★)/base-slice engine — Route B imports its (P_m)/(Q_m) as the k=0 anchor);
`dyadic-discrepancy` / euclid (certified upper bound). Retire `ladder-abel-pairing`, `coupled-cut-descent`
(exact-(★) hedge + refuted single-cut descent — no longer needed).

Build set: absorb-rescale-induction, split-rung-mutual-induction, peel-scale-rank-induction
