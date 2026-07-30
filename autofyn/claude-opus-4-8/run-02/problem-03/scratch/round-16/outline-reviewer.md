# Outline review — round 16 — imo-2026-03 (b-lift, cut-top-rung leaf)

## Field this round
One approach only: **ladder-length-deficient-induction** (revise). No new/diversity slug opened —
the outliner made a deliberate lean call. I judge both the revise and the lean call below.

---

## ladder-length-deficient-induction — CHANGES REQUESTED (advance; bank steps 3–4, build the TEETH residual)

Technique is sound and the engine is certified machinery. The revision makes two claims; I verified
both numerically with exact `Fraction` before letting them advance.

**1. (L̂B_{m−1})-inheritance banking — VERIFIED, sound.**
The logic is valid: in the induction step for `(P̂_m)` the outer hypotheses `(P̂_{m−1})`/`(Q̂_{m−1})`
are in hand, and `(L̂B_{m−1})` follows unconditionally from `(P̂_{m−1})` via the certified Lipschitz
collapse (§5), so it is legitimately available on the leaf. Its hypotheses are all met on IIb:
reds `≤θ=2^{m−1}` (case hyp), `ΣR≤2^m` (`(P̂_m)` hyp), `F''` a budgeted refinement of `L_{m−1}`, and
the budget `a₀+b'' ≤ m−a₁ ≤ m−1` — the last inequality is exactly `a₁≥1 ⇒ one budget unit spent`.
So `Δ(R,F'') ≥ min(0, θ−ΣR)` holds on the leaf. My probe: **0 fails / 31,227 leaf configs, m=2..5.**
The explorer's correction to the file's §4/§6 ("only `(Q̂_{m−1})` available") is right and must be
folded in — `(L̂B_{m−1})` is cleanly inheritable and is what makes the ΣR≤θ half close.

**2. ΣR≤θ closure (steps 3–4) — VERIFIED, genuinely bankable.**
At `ΣR≤θ`, `min(0,θ−ΣR)=0` ⇒ `Δ(R,F'')≥0`; then via (C),
`Δ(R,F') ≥ ½θ + ½D̃(ρ₁) − I_S ≥ ½θ − ½D̃(ρ₁) ≥ 0`, using `I_S ≤ λ(O_{ρ₁})=D̃(ρ₁)` and
`D̃(ρ₁) ≤ max part < θ` (alternating-sum ≤ largest part; parts `<θ` because the rung is cut).
The `ΣR=θ` boundary is safe (`min(0,0)=0`). My probe: **0 fails / 26,213 ΣR≤θ leaf configs.**
This is a real sub-lemma — bank it as a stand-alone even if the residual stays open.

**3. TEETH residual (steps 5–6, ΣR>θ) — the sole open gap; a REAL residual, not a banned bound.**
- It is genuinely open: on `ΣR>θ` the `(L̂B_{m−1})` floor goes negative and the naive scalar route
  (`floor + ½θ − ½D̃(ρ₁)`) is inconclusive on **62.4% of 15,221 oversized configs**, while the true
  `Δ(R,F')≥0` **always** (0 fails). So the gap is real and the scalar ceilings are provably vacuous
  here — consistent with the standing ban that any purely scalar `I_S`-ceiling telescopes to the R14
  dead estimate.
- It is NOT a restatement of a banned bound. Caveat for the builder: the (TEETH) inequality
  `I_S ≤ Δ(R,F'') + ½θ + ½D̃(ρ₁)` is, by (C), *literally equivalent* to the target `Δ(R,F')≥0` — so
  it must NOT be treated as a lemma one may assume; it is the thing to prove. What saves it from being
  a bare hand-off is (i) the ΣR≤θ half is now independently closed (real progress regardless of TEETH),
  and (ii) the proposed closer is a concrete geometric charging plan, not "a matching exists": `O_{ρ₁}`
  is a comb of `⌈r/2⌉` disjoint teeth, `O_W` a step-function odd set with `≤a₀+b''+1≤m` breakpoints,
  charged via the even-complement identity `λ(E∩O_W)=D̃(W)−I_S` and mass identity
  `D̃(W)=2Δ(R,F'')+ΣR−(θ−1)`, pigeonholed in the low band. This is a per-tooth (non-scalar) lever, off
  the banned list (not (NEG) Q≥S_π, not scalar-b, not π₀-fixed, not ABSORB/split-rung, etc.).

**What to change while building.** (a) Fix the file's §4/§6 wording — inherit `(L̂B_{m−1})`, not only
`(Q̂_{m−1})`. (b) Write the ΣR≤θ closure as an explicit sub-lemma with the `D̃(ρ₁)≤max<θ` and
`I_S≤D̃(ρ₁)` steps stated. (c) Do NOT assume `D̃(ρ₁)` or `I_S` shrinks with `a₁` (cheap-killed —
`a₁`'s only leverage is the spent budget unit and the tooth COUNT `⌈r/2⌉`, not tooth measure).
(d) The `(Q̂)` mirror (step 6) is genuinely harder — a LOWER bound on `I_S` needs the teeth to MEET
`O_W`, not merely be few; do not assume the upper-bound argument dualizes for free.

**Verdict: CHANGES REQUESTED.** Bank steps 3–4 (ΣR≤θ half closed), build steps 5–6 (TEETH). The
approach stays live.

---

## Diversity decision — I concur with the lean call (no filler slug), with a plateau flag

The outliner opened no second slug and justified it. I agree this round:
- Both explorer lenses converged on the same negative. per-rung-equality is DRY (its recursive form
  IS the live `(P̂/Q̂)` engine; its additive/union/scalar-coefficient forms re-encode the R15 union
  cheap-kill and the R11 scalar-`b` refutation). Every non-`(P̂/Q̂)` framing on the residual is a
  recorded dead end (π₀-fixed, ABSORB, split-rung, NEG-lemma, subgame decomposition, bottom-band).
  A filler drawn from any of these would share the leaf's wall — the single-gap trap, worse than none.
- Crucially, the lean call is justified *this round* only because there is genuine forward motion (the
  ΣR≤θ half is newly closed) AND the new lever (comb/teeth) is concrete, so it is not the round-15
  situation where the only closer was a bare injection onto the wall.

**Plateau flag for the orchestrator.** The b-lift is now on a plateau R11–R16. If the TEETH step
stalls next round, the field is at a single-wall single-approach state and the shared-gap rule bites:
next round's explorer should cheap-kill the two logged speculative directions (the discrete
run-length / ±1-jump recast of `M`; the red-side MAXPEEL peel of the largest red ≤θ) numerically on
the extremal ladder family + neighbors, and only a cheap-kill survivor earns a far-apart slug. Do not
seed either as a slug now (unvetted = filler).

## Ranking
Updated (K=32, anchored to this round's evidence): ladder-length-deficient-induction advanced its gap
(banked the ΣR≤θ half) and is the closest-to-solved live line on the sole open wall, so it beats the
parked/dead siblings and edged peel-scale-rank-induction (parked, no live move this round). Both stale
flags (ladder-length, bottom-band) cleared. Post-update: peel-scale 1714 (parked reference),
ladder-length 1679 (live primary), bottom-band 1502 (retired), split-rung 1502, absorb 1485,
coupled-cut 1435. No new slug to register; no branch requested.

build set: ladder-length-deficient-induction
