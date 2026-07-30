# Outline Review — Round 15 (imo-2026-03, b-lift / GAP-P1′-b)

Sole open wall: the b-lift, `D̃(π₀⊎F') ≥ 1` for arbitrary dyadic-cut `F'`, i.e. the odd-set
overlap term `λ(O_{π₀}∩O_{F'}) = GAP-P1`. UB, (★) base slice, Case A are DONE/certified — no
builder on them. Plateau R11–R14 ⇒ shared-gap rule in force: the field must carry ≥1 genuinely
far-apart framing. Both explorers this round confirmed (with fresh numerics) that the overlap term
is split-agnostic and every scalar/telescoping/sign/union route re-encodes it; the outliner's own
cheap-kills killed the raw NEG-lemma dual (`Q≥Σz_{2k−1}` FALSE 100%; termwise/tail/prefix/value all
fail). The field is judged against that.

## ladder-length-deficient-induction (revise) — CHANGES REQUESTED (build, PRIMARY)

Verdict: sound to build. This extends the ONLY mechanism that has ever injected the missing ½ — the
certified `(P_m)/(Q_m)/(LB_m)` ladder-length mutual induction + the `(I4)` D̃-Lipschitz collapse
(base-slice-star.md) — from blue = uncut ladder to blue = an arbitrary refinement `F'`. It stays on
certified TRUE identities (ladder-interleaving `Δ=BO−RE`, blue-agnostic; top-peel-general
`D̃(P)=max(P)−D̃(P∖max)`), so it is NOT a re-encoding of a refuted identity.

Not banned: this is NOT a π₀-fixed monovariant (banned R11/R14) — π₀ are inert reds inside a
structural downward induction on ladder length, and Step 3 shrinks the residual ladder's red total
by ε (π₀ is not held fixed while F'→L). It is NOT split-rung-mutual-induction reborn: split-rung
died because its closing identity `(I1′)` was FALSE and its honest form telescoped to the vacuous
overlap; here the closer is an EXACT rank-parity correction on the merged order plus the Lipschitz
collapse, a genuinely different closing device.

Issues to fix while building:
- **Step 3 Key Lemma "the parity-flip set is LOCAL to that value window (p₁,p_r)" is FALSE.**
  Verified numerically (red={5,3,2,1}, θ=8 cut into ρ={5,3}, r=2): cutting the rung shifts the ranks
  of EVERY element below p_r by r−1 (value 2: ranks 5,6→6,7; value 1: ranks 7,8→8,9), not just those
  strictly between p₁ and p_r. The correction is still EXACT (it is a rank computation), but it is
  GLOBAL below p_r (a parity flip of everything below by r−1). The builder must carry the below-p_r
  tail flip explicitly; do NOT rely on a local-window correction. This is the real content of the
  generalized `(P_m^{cut})` and is where the proof lives or dies.
- Confirm `(Q_m)`'s complementary bound survives a CUT blue rung — the per-part cap ≤2^m was
  load-bearing in base-slice-star.md (3230 fails when dropped); re-check it under cutting (outliner's
  own flagged gap).
- Heed the outliner's own warning: do NOT collapse ρ→θ via a single-rung Lipschitz MERGE (value
  change 2(θ−p₁) loses the ½ — matches R12/R14 refutations + the game-explorer's cross-rung
  non-additivity gap 6.5). Use the exact rank-parity correction, apply Lipschitz only on the residual
  ladder L_{m−1} as in the certified engine.

Cases: (a) uncut top rung [certified (I1)]; (b) cut r=2; (b′) cut r≥3; π₀-part >θ [red-peel (I2)/(I3)
first]; endpoint "all rungs atomized". All present.

## bottom-band-peel-induction (new) — APPROVE (build, FAR-APART diversity) — cheap-kill is a HARD gate

Verdict: register + build as the mandated genuinely-different framing (bottom-scale split, +1 routed
through the Parity Lemma near 0, distinct engine from the ladder revise's Lipschitz collapse). It is
on a DIFFERENT reduction than the primary (bottom split vs BO−RE ladder), so the two do not share one
wall. Uses only certified tools (peel-difference-bound SD identity; parity-odd-total).

The honest risk (both explorers): the overlap term is split-agnostic — a bottom split ALSO produces
`λ(O_{F_{>τ}}∩O_{F_{≤τ}})`, and every additive/union combination across scales was cheap-killed
(overlap-tree (a): 1125/3000 fail). This survives ONLY if the bottom-band overlap is genuinely easier
because it lives on `(0,τ)` where `N_{F_{>τ}}` is a fixed count (parity-controllable), NOT a free
geometric overlap.

Hard gate before any proof effort: run the outliner's mandated cheap-kill —
`λ(O_{F_{>τ}}∩O_{F_{≤τ}}) ≤ (D̃(F_{>τ})+D̃(F_{≤τ})−1)/2` at the natural τ over a few thousand
exact-`Fraction` Case-B configs. If it blows up non-additively like the top-split union bound, this
collapses to the shared wall — record the NEGATIVE and retire promptly; do NOT force it. Also verify
Step 3's `F_{>τ}` is a bona-fide smaller feasible instance (the rescaling) before leaning on the IH.

## peel-scale-rank-induction (advance) — KEEP LIVE, do NOT build this round

Verdict: park as the machinery home (owns the certified FLOOR/POS reductions; leader by Elo 1725).
It does NOT enter the build set. Its proposed closer — "a GLOBAL cut-tree-guided matching for `Q≥P`"
— has NO stated mechanism; every concrete termwise/tail/prefix/value-ranked form was cheap-killed
this round (outliner's own results) and it went RETHINK R14 on the banned `(NEG)` bound. A named
matching with no mechanism is an unverified hand-off onto the bare shared wall; building it would burn
a builder with no concrete route (the outliner itself ranks it lowest and honestly calls it "the
shared wall, fully open"). Leave live; re-plan only if a concrete non-scalar cut-tree invariant
appears. Its FLOOR/POS/ladder-interleaving lemmas remain the field's shared machinery.

## Retire / park (agree with outliner)
split-rung-mutual-induction, absorb-rescale-induction (DEAD R14, banked top-peel-general.md);
coupled-cut-descent (DEAD R12); allocation-vertex-corner (DEAD engine R11); ladder-abel-pairing
(parked (★) hedge, no longer needed); dyadic-discrepancy / -euclid (UB reference, certified).

## Diversity check
The two build slugs sit on DIFFERENT reductions with DIFFERENT +1-injectors: ladder revise = BO−RE
merged-order accounting closed by the Lipschitz ½-collapse; bottom-band = SD split closed by the
odd-total Parity Lemma near 0. They do not share the top-scale overlap wall and will not die together
— satisfying the shared-gap rule. Primary bet is the ladder revise (extends the one working engine);
bottom-band is the honest far-apart hedge, gated by its cheap-kill.

## Ranking (updated this round)
peel-scale-rank-induction 1726 (machinery home, parked) · ladder-length-deficient-induction 1621
(PRIMARY live route, verified-milestone base) · bottom-band-peel-induction 1522 (new far-apart) ·
split-rung 1513 / absorb 1494 / coupled-cut 1442 / induction-recursion 1343 (all dead).

build set: ladder-length-deficient-induction, bottom-band-peel-induction
