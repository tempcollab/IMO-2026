# Proof-reviewer report — round 7 — imo-2026-03

Problem still `partial`. Answer c(n)=2^n/(2^{n+1}−1) remains CONFIRMED. No APPROVE this round;
all three built approaches advanced but each retains a real, precisely-localized gap. Three new
lemmas certified (MID, RL, VS → 13 total).

---

## 1. parity-measure-potential — CHANGES REQUESTED (Status: partial)

**Load-bearing deliverable: Lemma MID (mass-difference reduction). VERIFIED, CERTIFIED.**
Independently re-derived both parts:
- (a) parity identity: N_S=N_F+N_B and 2N_B≡0 ⇒ N_S≡g=N_F−N_B (mod 2); odd-set confined to
  (0,2^{n−1}) since all pieces ≤2^{n−1}. So D(S)=μ{t∈(0,2^{n−1}):g odd}. Correct.
- (b) mass identity: layer-cake gives ∫₀^{2^{n−1}}N_F=ΣF=2^n, ∫N_B=ΣB=2^n−1, so ∫g=1. Correct.
Numerically re-checked exact-piecewise at n=4 (e.g. F={7,6,3}, B={1,2,1.5,2.5,3,5}: D(S)=5=
μ{g odd}, ∫g=1). The reduction genuinely eliminates the SPLIT cross-term μ(O_F∩O_B) and the
balanced/unbalanced dichotomy — this is real, honest progress and the correct "upstream" object.
Certified as `lemmas/mass-difference-reduction.md`.

**§0 refutation of the outliner's invariant: SOUND.** The witness B={1,1.865,2,2.135,2.915,5.085}
gives O_B∩(2,4) = (2,2.135)∪(2.915,4), two intervals — re-checked by hand from the sorted list.
The "single-interval-per-gap" invariant is correctly refuted; good that the builder did not force a
false invariant.

**Gap (name the step): GAP MID-core.** L2 is now EXACTLY equivalent to μ{g odd} ≥ ∫g = 1 for
|F|≥3. The builder correctly closed |F|=2 (N_F even ⇒ μ{g odd}=D(B)≥1 by IH) and 0≤g≤1 (D=1), and
correctly showed the pure-integral version is FALSE (g≡2 on measure ½), so the ladder structure of
B (Lemma ONE recursed) is genuinely required. This step is NOT proved. Builder's recorded Status
(partial) is HONEST and matches reality. Outcome recorded: advanced.

Scores: Correctness 10/10 (MID and the refutation are exact) · Rigor/completeness 6/10 (one clean
gap remains, no hand-waving elsewhere) · Progress 8/10 (cross-term eliminated; residual is now a
single scalar parity-measure inequality — the sharpest form the lower bound has ever had).

## 2. induction-peel — CHANGES REQUESTED (Status: partial)

**Assigned mechanism (aimo-0298 split-and-average) REFUTED — refutation SOUND, status HONEST.**
Independently confirmed the core failure: the averaging inequality D(S)≥½(D(S_O)+D(S_E)) is not a
theorem for the parity-measure D — my own random-split check found it fails on ~45% of samples
(builder reports ~28% on the specific minimal-scale-run split over budget-enforced |F|≥3
refinements). Since D is a parity-measure, not an additive per-element sum, the termwise argument
that carries aimo-0298 (a dimensionless additive potential inducting on |S|) has no analogue here;
additionally S_O, S_E lose mass and ladder structure so they are not valid IH(n−1) instances. Both
independent obstructions are correct. This lever is a genuine dead-end and is correctly recorded as
such — no false progress claimed.

**Nothing is overclaimed.** All prior rigorous content (PEEL/SPLIT/ONE/TB/band-decomposition,
Case (a), trivial regime of L⋆, |F|=2 sub-case, both telescoping identities, entire upper dominant
case §4A) stands and is unchanged. GAP L2 (the exchange step) and GAP U remain open.

**Verdict rationale:** the *approach* is not fatally broken (its infrastructure is sound and GAP L2
is now better attacked via the certified MID route), so this is CHANGES REQUESTED, not RETHINK — but
the outliner MUST NOT re-assign the aimo-0298 monovariant to this slug. Outcome recorded: dead-end
(the round-7 lever), with a note that the slug itself stays partial/live.

Scores: Correctness 10/10 (the refutation is right) · Rigor 9/10 (honest negative result, well
documented) · Progress 3/10 (no gap closed; value is in ruling out a dead lever + confirming the
fix must be upstream, which MID now delivers).

## 3. breakpoint-vertex — CHANGES REQUESTED (Status: partial)

**Requested focus — is the uniform vertex boundedness profile-independent or a spot-check?**
Theorem VERT (optimal Xiang refinement has ≤n+1 distinct part-values) IS proved
profile-independently via the LP-vertex / hyperplane-arrangement rank count (Steps 1–4: fix a type,
D is affine on each sort chamber, min at a chamber∩polytope vertex, rank of active zero/tie
constraints ≤ N−d forces d≤M). This is a genuine structural argument, NOT a spot-check. Standing
and sound (certified-ready since round 5).

**New this round — Lemma RL and Lemma VS: both VERIFIED, CERTIFIED.**
- RL: re-derived the disjoint-support coefficient-vector invariant (each input leaf flows into one
  current piece ⇒ MATCH takes a sign-respecting difference ⇒ coefficients stay in {0,±1}); the
  budget count |T|−1+(m−|T|)=m−1≤n holds since m≤n+1; strictness (no sum of two positives) correct.
  Certified as `lemmas/leftover-realizability.md`. It correctly yields the *sufficient* Reduction
  R-UV (min 𝓡(A)≤u_nL ⇒ upper bound).
- VS: re-verified the algebra 1−u_n/u_{n−1}=c(n) and c(n)/2=β_n; both single-move certificates
  provably fail in the valley. Certified as `lemmas/valley-sharpness.md` (a limiting/adaptivity
  lemma). The round-6 "no-DELETE full-support tree" framing is correctly retracted (DELETE/subset
  selection is essential — overshoots on 214/516 valley profiles without it).

**Gap (name the step): Prop UV.** The upper bound in the valley is reduced EXACTLY to
min 𝓡(A) ≤ u_nL — the restricted signed-subset-sum discrepancy bound. This is UNPROVED: only
numerical evidence (387 valley profiles, budget enforced, worst ratio 0.56) plus the exact dyadic
extremal. So the upper bound is NOT closed; the "vertex bound covering the valley" the round-7 task
asked for is reduced-but-not-proved. Builder's recorded Status (partial) is HONEST.

Scores: Correctness 10/10 · Rigor 7/10 (VERT/RL/VS rigorous; Prop UV only reduced) · Progress 7/10
(upper valley now a single clean, correctly-framed discrepancy inequality; naive pigeonhole ruled
out rigorously).

---

## Certifications (round 7)
- **CERTIFIED** `lemmas/mass-difference-reduction.md` (Lemma MID) — exact, depends only on Lemma M
  + layer-cake.
- **CERTIFIED** `lemmas/leftover-realizability.md` (Lemma RL) — exact, depends only on Lemmas P/DM.
- **CERTIFIED** `lemmas/valley-sharpness.md` (Lemma VS) — exact algebra, adaptivity lemma.
No rejected lemmas.

## Shared-wall status (for the outliner)
Both walls are now cross-term-free scalar claims, on independent routes:
- LOWER = **GAP MID-core**: μ{g odd} ≥ ∫g = 1 for g=N_F−N_B, |F|≥3 (ladder structure of B
  essential). Attack this directly; it is the whole residual lower bound.
- UPPER = **Prop UV**: min 𝓡(A) ≤ u_nL over tree-realizable signed subset sums (Lemma RL), ≥2 cuts
  forced (Lemma VS). This is a restricted-discrepancy problem — a genuinely different object from
  the lower wall.
Do NOT re-assign aimo-0298 split-and-average to induction-peel (refuted this round).
