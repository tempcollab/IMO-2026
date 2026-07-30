# Outline review — imo-2026-03 round 14 (b-lift field)

Sole open wall: the b-lift (GAP-P1′-b) — prove general-`b` `I_n≤0` (Case B, arbitrary `F'`) from the
proven, certified base slice (★). UB, Case A, and (★) are all DONE/certified — no builder on them.

I numerically re-verified the two new tools that these approaches rest on, plus the disqualifying fact
for the third:
- **ABSORB** `Δ(R,Z)=θ+Δ(R⊎π_1,Z')`: **0/3000** exact-Fraction failures. Sound.
- **Split-rung correction** `D̃(partition)=Σ(−1)^{i−1}c_i` and `0≤` it `≤θ`: **0/2000**. Sound.
- **peel-scale's proposed Q-bound** at the n=4 b=2 tie (`π_0={8,8}`, `F'={5,4,2,2,1,1}`): `P=Q=3`
  (`I_n=0`), but `S_π=Σy_{2k}=8` ⇒ `Q=3 < 8`. The proposed sufficient step is FALSE.

---

## absorb-rescale-induction — NEW — CHANGES REQUESTED (build)
Sound technique, avoids every banned route, honest gaps. Strong induction on SCALE `n`, ONE exact
ABSORB step folding `F'`'s split top rung into red, closed by a rescaled deficient bound. It is NOT
π_0-fixed (transforms both sides via an exact identity), NOT the refuted naive ABSORB-iteration (uses
ABSORB once, then a rescaled — not verbatim `(LB_m)` — bound), NOT a monovariant, NOT WM/scalar-b.
The ABSORB foundation is verified exact.

Load-bearing issues the builder MUST close (both flagged honestly by the outliner):
- **GAP-A1 arithmetic deficit (concern I sharpened):** the bare rescaled bound at `ΣR̄=3·2^m` gives
  `min(0, 2^m−3·2^m)=−2·2^m`, which is WEAKER than the `−θ=−2^m` target by a full `2^m`. The `−θ`
  recovery (further (I2)/(I3) peel of the one absorbed red part `>θ`, OR proving the engine directly
  against the *deficient* refinement `F''` whose shorter ladder supplies the missing `2^m`) is
  UNRESOLVED and is the real content of GAP-A1 — not just "widen the mass cap." Do not hand-wave it.
- **GAP-A2 count-cap budget (make-or-break):** post-absorb `#R̄=a_0+a_1+2 ≤ m+3`, but the rescaled
  bound holds only at `#R≤m+1` (probe: `m+2` already fails). The 2-count overage must be closed by a
  real budget-accounting argument (`a_0+a_1≤n−2` on Case B) or by showing the `−θ` slack + refinement
  tolerates it. If neither closes, this route restates the wall.
Gate before writing the proof: re-run the rescaled probe at `m=5,6` with a *targeted adversarial*
(non-random) search to confirm the count cap is genuinely `m+1`.

## split-rung-mutual-induction — NEW — CHANGES REQUESTED (build) — strongest, most aligned
This is exactly the framing run_state Next(R14) calls for: a scale-by-scale peel that carries a
NON-WM loaded invariant and NEVER separates (★) from the lift (the `k=0` slice literally IS the
certified base-slice engine). Keeps red mass BOUNDED (no absorption), so it sidesteps the absorb
route's count-cap/mass-blowup difficulty entirely — a genuinely different mechanism, not a variation.
Avoids every banned route. The correction-term mechanism is verified sound (`D̃(partition)` = the
split parts' alternating sum, `≤θ`).
Builder MUST:
- **GAP-B1:** derive/prove the split-rung-peel identity (I1′) with the alternating-sum correction and
  show the correction is absorbed by the deficient bound. CHEAP-KILL the exact (I1′) form at
  `m=2, j=1` numerically BEFORE the full build (the outliner's own gate — enforce it).
- **GAP-B2:** verify the two-parameter dependency graph is non-circular, grounded at `(m=1 ∨ k=0)`.
- **GAP-B3:** pin the load-bearing caps of `(P_{m,k})/(Q_{m,k})` by a Fraction sweep first (the R13
  `(Q_m)` part-cap was false until pinned — same discipline with `k` added).
- Do NOT let the sub-level correction re-introduce FLOOR/level machinery recursively (circular unless
  it stays the closed alternating-sum term).

## peel-scale-rank-induction — ADVANCE — RETHINK (this round's proposed move is a banned dead route)
The slug's *banked, certified* machinery (FLOOR reduction, HLP, (POS)) is untouched and it remains
the leader/assembler. But the mechanism proposed for THIS round is dead: step 2 reduces `I_n=P−Q≤0`
to "it suffices to prove `Q ≥ Σ_{k=1}^{K_0} y_{2k}`." That RHS is exactly `S_π` from the certified
Positive-Layer Localization Lemma, so this is the **(NEG) `Q≥S_π` bound — explicitly BANNED**
(run_state Rules; FALSE 50–77%, fails the whole tie family; qlayer-charge-induction was KILLED R13 for
precisely this). I confirmed it false at the n=4 b=2 tie: `Q=3 < S_π=8`. The proposed "recursion on
F''s cut-tree" is a mechanism for proving a FALSE inequality — no recursion can establish a statement
that fails at every tie config. The `Q≥P` you need does NOT factor through `Q≥S_π`, because `P≤S_π`
is lossy (loose at ties). RETHINK: this line cannot be built. Send back to the outliner to re-plan
peel-scale's next move (its FLOOR/HLP machinery stays banked and it stays the assembly home once the
b-lift closes elsewhere). Do NOT re-seed any `Q≥S_π` / positive-layer-as-engine variant.

## Diversity note (for the orchestrator)
The intended 3rd approach (peel-scale) was the diversity hedge, and it is dead (banned bound). That
leaves two live routes. They both localize the difficulty to `F'`'s SPLIT top rung, but attack it by
OPPOSITE mechanisms — absorb-rescale FOLDS the rung into red (mass grows to `3·2^m`, crux = count-cap
budget) vs split-rung KEEPS it blue and peels in place (mass bounded, crux = the (I1′) alternating-sum
identity). Different load-bearing gaps ⇒ not the single-gap trap; a reasonable diverse pair for one
round. But note: if BOTH stall next round, the field will have collapsed onto "handle the split top
rung" with no live far-framing hedge — per the shared-gap rule, next round's outliner should then seed
one genuinely different b-lift framing (the surviving hedge is gone).

Ranking (folded this round): peel-scale-rank-induction 1739 (parked leader/assembler; Elo reflects its
certified achievements, not this round's dead move), ladder-length 1573 (base-slice reference, parked),
split-rung 1544, absorb-rescale 1511 (both new, live, cold-start moved up over dead siblings),
coupled-cut 1448, allocation-vertex 1417 (dead). Build set = the strongest LIVE slugs on the open wall
(NOT top-Elo, which are parked).

build set: split-rung-mutual-induction, absorb-rescale-induction
