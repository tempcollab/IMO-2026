## imo-2026-03

Round-17 field. The dispatched R17 "all-or-nothing tooth capture" finding was tested and is FALSE
(6481/8000 leaf configs have a W-part strictly inside a tooth, `/tmp/teeth_probe.py`); the surviving
rank/interleave form is the full merged-order alternating sum = the target itself (R8-banned). The
per-tooth comb charge is therefore DEAD in every form (count / all-or-nothing / magnitude-interleave).
Instead, a different, verified sharpening collapses almost the entire wall. Lean field: one revise
(the reframed leader) + advance. No far-apart new slug is opened — every orthogonal framing is
refuted (merged-order = target, sequential = target, genfn dead, integer-minimizer equivalent-
difficulty, bottom-band-peel dead, red-peel vacuous); per CLAUDE.md's lean principle a single
well-aimed revision is correct, and fabricating a slug would violate it.

---

ladder-length-deficient-induction: revise
Target: The full b-lift `D̃(π₀ ⊎ F') ≥ 1` for `π₀` (Σ=2^n) and `F'` a budgeted refinement of `L_n`
  with `a₀ + Σaᵢ ≤ n` — which, with the certified UB and Case A, gives `c(n) = 2^n/(2^{n+1}−1)`.
Technique: budget-aware ladder-length mutual induction `(P̂_m)/(Q̂_m)/(L̂B_m)`, now with the round-17
  ENDPOINT COLLAPSE replacing the round-16 `ΣR`-split. Spine = `(NN) D̃≥0` (trivial band) + certified
  `(I4)` Lipschitz ½-injector (reduce to endpoint) + `(A3)/(I3′)` red-peel (endpoint θ-red) + the new
  pure-blue anchor.
Skeleton:
  1. Restate `Δ(R,F') ≥ 0 ⟺ D̃(R⊎F') ≥ ΣR − 2^m + 1` (since `ΣF' = 2^m − 1`). — algebra.
  2. (S1) `ΣR ≤ 2^m − 1`: RHS `≤ 0`, so `D̃ ≥ 0` closes it — for EVERY case (I, IIa, IIb),
     subsuming all round-16 machinery in that band. — by `(NN)`.
  3. (S2) `2^m − 1 < ΣR < 2^m`: fill reds up to `ΣR' = 2^m` (≥2 reds, each ≤θ, capacity ≥2θ), same
     count/budget; `(I4)` gives `D̃(R⊎F') ≥ D̃(R'⊎F') − (2^m−ΣR) ≥ 1 − (2^m−ΣR) = ΣR−2^m+1`. Same
     fill for the IIa mirror. — by certified `(I4)`; endpoint `D̃(R'⊎F')≥1` is the only input.
  4. (S3) Endpoint `ΣR = 2^m`: prove `D̃(R⊎F') ≥ 1`. Split:
     4a. no red `= θ` ⇒ `D̃ ≥ 13/12 > 1` (SLACK — attack with a crude overlap/measure bound). — gap.
     4b. some red `y = θ` ⇒ `(A3)/(I3′)`: `D̃(R⊎F') = θ − D̃(R₀⊎F')`, `ΣR₀ = θ`; need
         `D̃(R₀⊎F') ≤ θ − 1`. Iterating a second θ-red gives `R={θ,θ}` ⇒ `D̃(R⊎F') = D̃(F')`. — gap
         (upper bound) + anchor.
  5. Anchor lemma `D̃(F') ≥ 1` for a budgeted refinement of `L_m` with `≤ m−1` cuts: uncut top rung
     trivial (`θ − D̃(F'')`, `D̃(F'')≤ΣF''=θ−1`); cut top rung = pure-blue `(C)` overlap with a spare
     budget unit. — closes 4b's `R={θ,θ}` tail; certifiable stand-alone.
  6. Import unchanged & do NOT re-derive: certified `(★)` base slice (`base-slice-star.md`), `(C)`
     + `(A1)/(A2)/(A3)` (`cut-top-rung-correction.md`), MAXPEEL/`(I3′)` (`top-peel-general.md`),
     `(I4)` Lipschitz. Case I / uncut-rung cases now fold into S1 for `ΣR≤2^m−1`.
Key lemmas (claim + mechanism):
  - (S1) trivial band — because `Δ≥0 ⟺ D̃ ≥ ΣR−2^m+1` and `ΣR≤2^m−1 ⇒ RHS≤0 ≤ D̃` by `(NN)`.
    Verified `Δ<0`=0, min 1/12 (`/tmp/sliver2.py`).
  - (S2) Lipschitz-to-endpoint — because filling reds by total `ε=2^m−ΣR<1` moves `D̃` by `≤ε`
    (`(I4)`), so `D̃ ≥ 1 − ε`, exactly the target. Verified 0 Lipschitz violations
    (`/tmp/verify_chain.py`); the IIa `(A3)` upper-bound mirror is a FALSE target (`/tmp/iia.py`),
    correctly bypassed.
  - Endpoint θ-red forcing — because endpoint configs with no red `=θ` have `D̃ ≥ 13/12`
    (`/tmp/endpoint.py`), so all razor-tight `D̃=1` configs carry a red `=θ`, which is peelable.
  - Anchor `D̃(F')≥1` (≤m−1 cuts) — because the spare budget unit forbids the `min=0` configs that
    a full-`m`-cut refinement admits; uncut-top-rung branch is `D̃(F'')≤ΣF''`. Verified min=1 at
    `≤m−1` cuts vs min=0 at `m` cuts (`/tmp/anchor.py`).
Open gaps (the builder fills; all on the measure-zero endpoint `ΣR=2^m`):
  - (S3-4a) the slack endpoint sub-case (no red `=θ`, `D̃≥13/12`): find a non-scalar bound using the
    spare `1/12` slack — NOT razor-tight, so a crude comb/measure charge is admissible here (this is
    the only place a partial-capture teeth bound may legitimately be attempted; it must NOT be the
    magnitude-interleave = target form).
  - (S3-4b) the upper bound `D̃(R₀⊎F') ≤ θ−1` at `ΣR₀=θ` after one θ-red peel.
  - (Anchor) the pure-blue cut-top-rung overlap `λ(O_{ρ₁}∩O_{F''}) ≤ ½(D̃(ρ₁)+D̃(F'')−1)` at budget
    `≤ m−1` (no oversized reds — the tractable residual of the whole problem).
Cases to cover: S1 (ΣR≤2^m−1, all top-rung cases); S2 (open band, both IIb and IIa mirror); S3
  endpoint {no θ-red; one θ-red; R={θ,θ}}. Certified UB + Case A already give the other half of the
  determination.
Watch out for:
  - Do NOT re-open the per-tooth all-or-nothing capture (REFUTED this round) or any magnitude-
    interleave / merged-order form (= target, R8-banned) for the RAZOR-TIGHT endpoint core. The teeth
    lever is admissible ONLY in the slack sub-case 4a where there is genuine `1/12` room.
  - S2 fill must keep every red `≤ θ` and the count `a₀` and budget unchanged; check feasibility
    (needs `≥2` reds, guaranteed since `ΣR > 2^m−1 > θ`).
  - Endpoint 4b needs an UPPER bound (Q̂-direction); the existing `(Q̂_m)` is 2^m too weak — do not
    cite it. Route 4b through the anchor for the `R={θ,θ}` tail and treat the single-θ-red upper
    bound as the honest open gap.
  - The endpoint `ΣR=2^m` is genuinely equivalent to the target (it IS the b-lift) — do NOT claim it
    closed. The round's deliverable is the SOLID collapse (S1+S2) + the verified anchor, which
    strip the wall to a measure-zero, integer-rigid slice; report `partial`.

build set: ladder-length-deficient-induction
