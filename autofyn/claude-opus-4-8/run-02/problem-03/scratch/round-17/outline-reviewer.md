# Outline review — round 17 (imo-2026-03)

Sole live approach on the open wall (the b-lift, GAP-P1′-b), advanced as a revise. I independently
re-verified the round's load-bearing claims with exact `Fraction` (`/tmp/verify_r17.py`,
`/tmp/witness.py`, `/tmp/cuttop_endpoint.py`).

## ladder-length-deficient-induction — CHANGES REQUESTED (partial; real advance, honest open core)

The round-17 ENDPOINT COLLAPSE is a genuine, non-circular sharpening. It correctly retires the
refuted R16 TEETH lever and strips the wall to a measure-zero endpoint slice. Verdict CHANGES
REQUESTED: build it (banking S1+S2+anchor-uncut as SOLID, endpoint core reported open), with the
fixes below.

### What is SOLID (verified, may be banked)
- **(S1) `ΣR ≤ 2^m−1` trivial.** From `Δ≥0 ⟺ D̃(R⊎F') ≥ ΣR−2^m+1` (exact algebra, `ΣF'=2^m−1`),
  the RHS is `≤ 0` on this band, so `(NN) D̃≥0` closes it — for EVERY case (I, IIa, IIb). I confirmed
  the equivalence holds identically and 0 violations on the band (6687 configs, m=3), and that this
  legitimately SUBSUMES the entire R16 cut-top-rung `θ<ΣR≤2^m−1` machinery (`(L̂B-inherit)`,
  `I_S≤D̃(ρ₁)`) — those were never needed there. This is the real content of the round: R16's whole
  "ΣR>θ TEETH residual" was mostly trivial; only `ΣR=2^m` is hard.
- **(S2) band `2^m−1<ΣR<2^m` → endpoint.** Fill reds to `ΣR'=2^m` (feasible: `≥2` reds `≤θ`,
  capacity `(a₀+1)θ≥2θ`, count+budget preserved), then certified `(I4)` gives
  `D̃(R⊎F') ≥ D̃(R'⊎F')−ε ≥ 1−ε = ΣR−2^m+1`. Correct `(I4)` application, correct feasibility. NOTE:
  (S2) does NOT "inject the ½" — it DEFERS the +1 to the endpoint; that is fine and honestly stated.
- **Anchor, uncut-top-rung branch.** `D̃(F')=θ−D̃(F'')`, `D̃(F'')≤ΣF''=θ−1 ⇒ D̃(F')≥1`. Trivial via
  MAXPEEL; verified min=1 for `≤m−1` cuts, min drops to 0 at `m` cuts (m=2,3,4). The spare budget
  unit is genuinely load-bearing.
- **Anchor, cut-top-rung branch is a STRICTLY SMALLER b-lift instance, not circular.**
  `D̃(ρ₁⊎F'')` with `Σρ₁=θ=2^{m−1}`, `F''` a refinement of `L_{m−1}`, budget `a₁+b''≤m−1` is EXACTLY
  `(P̂_{m−1})` at its endpoint `ΣR=2^{m−1}`. Descends in `m` (base m=1 proven). Legitimate induction.

### What is OPEN (must be reported as gap, not closed)
- **Endpoint (S3) `ΣR=2^m` is equivalent to the target** — correctly labelled the sole irreducible
  core; report `partial`, do NOT claim it closed.
- **Gap 4b (the true residual):** the θ-red-peel upper bound `D̃(R₀⊎F') ≤ θ−1` at `ΣR₀=θ` for a
  GENERAL red `R₀` (only the `R={θ,θ}` tail is discharged, via the anchor). The existing `(Q̂_m)` is
  `2^m` too weak (do not cite it); this needs a genuinely new upper bound. This is now the honest wall.
- **Gap 4a (slack sub-case):** on the cut-top-rung endpoint with no red `=θ`, my check gives
  `min D̃ ≈ 1.12 > 1` (m=3,4) — slack, admits a crude bound. OK as a gap.

### Required fixes (fixable while building — the reason for CHANGES REQUESTED not APPROVE)
1. **The literal claim "endpoint configs with no red `=θ` satisfy `D̃≥13/12`" is FALSE as written.**
   Counterexample (`/tmp/witness.py`, m=3): `R={927/625, 2833/1250, 5313/1250}` (ΣR=8=2^m),
   `F'={4,2,1}` (uncut ladder), no red `=θ=4`, yet `D̃=1`. The `θ` there is a BLUE uncut top rung.
   The builder MUST restrict the "no-red-θ ⇒ slack" claim to the **cut-top-rung endpoint**
   (a₁≥1, all F' parts `<θ`), where it does hold (min ≈1.12, `/tmp/cuttop_endpoint.py`), and route
   the **uncut-top-rung endpoint** through the existing Case I `(A1)/(A2)` reduction to the smaller
   `(Q̂_{m−1})/(P̂_{m−1})` — NOT through the θ-red argument. As written, the θ-red-forcing step would
   silently mis-handle the uncut-top-rung endpoint.
2. **Do NOT re-assume the banned forms.** The `(†)`/`(‡)` teeth/parity-mismatch inequality is the
   target restated by `(C)` (R16, banned); the all-or-nothing tooth capture is REFUTED this round
   (6481/8000). The endpoint core must be closed by the θ-red/anchor route + a new 4b upper bound,
   NOT by any comb/merged-order/scalar-`I_S` charge.
3. Keep the `partial` verdict: the round's deliverable is the SOLID S1+S2+anchor-uncut collapse; the
   endpoint core (4a slack + 4b upper bound) stays open.

### Diversity note (for the orchestrator)
Field is (correctly) lean: both R17 speculative directions were cheap-killed with exact witnesses
(`math-explorer-cheapkill.md`: run-length recast reproduces the R8 meta, spread up to 2.99 within a
count-class; generalized red-peel re-routes to the vacuous `(Q̂)` wall). The `math-explorer-teeth.md`
file was not produced (the TEETH capture claim was refuted before it could be written). Every orthogonal
framing remains dead-or-equivalent, so a single well-aimed revision is the right call, not a filler slug.
The b-lift plateau continues (R11–R17) BUT the wall is now materially smaller than R16: from "ΣR>θ comb
charge" to "one upper bound (4b) on the integer-rigid endpoint `ΣR=2^m`". If gap 4b stalls next round,
the orchestrator should seed one genuinely-far framing for that endpoint upper bound (the θ-red-peel
`Q̂`-direction) per the shared-gap rule.

### Ranking (stale cleared; Elo folded)
ladder-length-deficient-induction 1736 (live leader, advanced again — S1+S2 collapse is real
progress) now edges past the parked peel-scale-rank 1715 (milestone done, no new closure). Dead-ends
(split-rung, absorb, coupled-cut, bottom-band, vertex-parity, cut-sequence) ranked below the live
lines. induction-recursion-telescope / ladder-abel-pairing kept as live hedges (~1568) below the
progressing leader.

build set: ladder-length-deficient-induction
