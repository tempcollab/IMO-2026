# Proof-reviewer — round 16 — imo-2026-03 (IMO 2026 P3)

Reviewed one built approach: **ladder-length-deficient-induction** (the sole live approach on the
sole open wall, the b-lift cut-top-rung leaf).

## Verdict: CHANGES REQUESTED — Status: partial

The builder's recorded Status (`partial`) is CORRECT. The two banked results this round are sound
and honestly reported; the oversized-red residual is honestly OPEN (not overclaimed). The whole
problem remains `partial` until the leaf closes.

## Scores
- Correctness: high. Every banked step independently re-derived and re-verified (0 fails).
- Completeness/rigor: honest. The single open leaf (ΣR>θ) is precisely stated and NOT assumed.
- Progress: real. Half the cut-top-rung leaf (ΣR≤θ) is closed with the intended budget-trade
  leverage; the residual is sharpened to an exact parity-mismatch statement.

## What I verified independently (exact `Fraction`, /tmp/rev.py)

**Claim 1 — (L̂B-inherit).** On the cut-top-rung leaf (a₁≥1, all reds ≤θ, ΣR≤2^m):
`Δ(R,F'')≥min(0,θ−ΣR)`.
- Budget accounting checked by assertion in every trial: global `a₀+a₁+b''≤m`, `a₁≥1` ⇒
  `a₀+b''≤m−a₁≤m−1`. This is exactly the hypothesis set of `(L̂B_{m−1})` (parts ≤θ=2^{m−1},
  ΣR≤2^m=2^{(m−1)+1}, budget ≤m−1). The relabelling of rungs ρ₂..ρ_m as a budgeted refinement of
  L_{m−1} (rung j sum = 2^{m−1−j}) is correct.
- Statement verified: 0 fails / 76,338 leaf configs (m=2..5).
- The derivation of `(L̂B_{m−1})` from `(P̂_{m−1})` via the certified 1-Lipschitz collapse (§5) is
  valid (I re-checked the ε-shrink: `Δ(R,F')≥−ε=2^{m−1}−ΣR`). The Lipschitz-collapse is the
  certified R13 ½-injector, applied one level down.

**Claim 2 — ΣR≤θ closure (IIb-1).** `Δ(R,F')≥½(θ−D̃(ρ₁))>0`.
- `(C)` identity `Δ(R,F')=Δ(R,F'')+½θ+½D̃(ρ₁)−I_S` re-derived numerically: 0 fails / 76k.
- With ΣR≤θ the floor is 0 ⇒ `Δ(R,F'')≥0`; `I_S≤λ(O_{ρ₁})=D̃(ρ₁)` ⇒ `Δ(R,F')≥½(θ−D̃(ρ₁))`.
- Alternating-sum bound `D̃(ρ₁)=p₁−(p₂−p₃)−…≤p₁` and `p₁<θ` (r≥2, Σρ₁=θ, all parts positive):
  verified 0 fails (my assert `p₁≥θ or D̃(ρ₁)>p₁` never triggered).
- Full chain `Δ(R,F')≥½(θ−D̃(ρ₁))>0`: 0 fails / 58,339 configs with ΣR≤θ. Boundary ΣR=θ safe
  (min(0,0)=0).

**The (†)=target observation (no circular progress).** I re-verified as identities (0 fails / 57k):
the mass identity `D̃(W)=2Δ(R,F'')+ΣR−(θ−1)`, the even-complement identity `λ(E∩O_W)=D̃(W)−I_S`,
and the parity-mismatch reformulation `D̃(R⊎F')=λ{parity mismatch on (0,θ)}+ (mass above θ)`.
The builder's rearrangement of `(†)` into `(‡)` and, at ΣR=2θ, into `D̃(R⊎F')≥1` is therefore a
correct identity. This means `(†)` is *literally equivalent to the target* and CANNOT be assumed as
a lemma — which is exactly how the builder treats it (marked OPEN, not assumed). No circular
reasoning is passed off as progress. The residual is razor-tight (builder's true min Δ→0.062).

## Banned-route audit — clean
- The `(L̂B)` inheritance is the certified R13 deficient-total form `min(0,θ−ΣR)`, NOT the refuted
  scalar fill `D̃≥ΣY−ΣZ`.
- The scalar ceiling `I_S≤D̃(ρ₁)` is used ONLY in ΣR≤θ (where it is valid and gives a strict
  margin) and is explicitly declared vacuous/banned on the oversized leaf (matches the R14 finding).
- No (NEG) Q≥S_π, no single-cut b-descent, no full-WM-IH, no π₀-fixed comparison, no ABSORB engine,
  no split-rung (I1′), no NEG-lemma value forms, no independent-subgame decomposition, no
  bottom-band/near-0 Parity peel. None smuggled.

## The one gap (why not solved)
Cut-top-rung, OVERSIZED-red leaf `ΣR>θ` (Case IIb-2) and its `(Q̂)`-mirror (Case IIa). Here the
`(L̂B-inherit)` floor is negative and the scalar `I_S`-ceiling is vacuous; closing requires the
per-tooth comb charge on `O_{ρ₁}` (⌈r/2⌉ teeth) against the ≤2m−a₁ budget-limited breakpoints of
`O_W`. The builder set this up but did NOT close it, and honestly says so. Because this leaf is open
at every scale, the mutual induction `(P̂_m)` is not completed for m≥2, so nothing beyond m=1 is
unconditionally established — consistent with `partial`.

## Certification of promotable lemmas — DECLINED (both), with reason
Both proposed lemmas — (L̂B-inherit) and (ΣR≤θ closure IIb-1) — are numerically true but their
proofs are CONDITIONAL on `(P̂_{m−1})` (the still-open inductive hypothesis; the induction has not
closed while IIb-2/IIa remain). They are valid inductive-step reductions, not standalone
unconditional theorems. Per the standing rule (certify only fully-proven unconditional identities,
not the (P̂)/(Q̂)-conditional statements — role memory R15), I do NOT add them to `lemmas/`. They
stay banked in the approach file and become certifiable once the leaf closes. The imported (C),
(A1)–(A3) remain certified (`lemmas/cut-top-rung-correction.md`); nothing to re-certify.

## Routing
CHANGES REQUESTED — re-dispatch this slug's builder next round to attack the ΣR>θ TEETH parity via
the per-tooth comb charge (the sole open leaf + its (Q̂)-mirror). Per the plateau flag, if TEETH
stalls again the explorer should first cheap-kill the two logged speculative directions
(run-length/±1-jump recast of M; red-side MAXPEEL of the largest red ≤θ) on the extremal ladder
family before seeding a new slug.

Outcome recorded via ranker: `advanced` (real sub-case closed with new budget-trade leverage).
current.md updated (Status still partial; Round-16 section added).
