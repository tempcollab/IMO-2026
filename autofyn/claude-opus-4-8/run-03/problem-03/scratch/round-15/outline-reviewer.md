# Outline review — imo-2026-03, Round 15 (ESCALATION)

Context: LOWER wall entered R15 with NO live vehicle (6 dead families incl. vertex-polytope R14).
UPPER = first-gap pigeonhole μ_{n+1}=min_i dist(a_i,R_{i-1})≤u_n, TRUE but (VALLEY-TIGHT)
asymptotically tight — no uniform margin allowed. The outliner ran the two mandated cheap-kills:
one LOWER lever (induction-peel merge) DIED; the UPPER boundary-continuation lever passed a
preliminary gate. Three nominations judged below.

---

## breakpoint-vertex (UPPER, advance) — APPROVE (build; exact gate mandatory before prose)

**Does the two-region split genuinely respect VALLEY-TIGHT?** Yes — I checked this adversarially,
it is the crux of the dispatch and it holds up:
- The margin is confined to the DEEP region a₁ ≤ L/2 − c·u_n, where L−2a₁ ≥ 2c·u_n gives
  provable slack. VALLEY-TIGHT's no-margin obstruction lives in the BOUNDARY layer: the tight
  family A^{(n)} has a₁ = 2^n/(2^{n+1}+1), i.e. L/2 − a₁ = 1/(2(2^{n+1}+1)) = Θ(u_n) below L/2,
  so it never enters the deep region. A margin argument used only where margin provably exists is
  legitimate — it is not the banned uniform/crude bound.
- The BOUNDARY-layer lemma (step 3) claims Φ ≤ (L−2a₁) + correction(a₂,a₃) ≤ u_n as an EXACT
  continuation of the certified dominant formula D=2a₁−L across a₁=L/2, tight AT the family. This
  is explicitly an exact/tight bound, NOT a disguised margin bound — it is the correct kind of
  step. Confirmed the file (lines 84–125) states it as exact-continuation, not slack.

So this is NOT a repackaged margin bound; the split is the right escape from VALLEY-TIGHT.

**Open gaps (CHANGES-REQUESTED-level, must be closed while building):**
1. Step 3 correction term. The R14 tied face is 14-dimensional at n=4 and n-varying; the
   tight-cert explorer (finding 3) confirmed the TRUE worst-case valley maximizer is NOT A^{(n)}
   but a multi-constraint tied face (whole-tail |2a₁−L| + several interior tree values binding
   simultaneously). The continuation MUST be tight on the whole face, not just A^{(n)}. The gate
   G2 correctly tests both A^{(n)} AND {16,8,4,3,2}/33 — keep that.
2. The self-consistent cutoff c (steps 2+4 overlap-cover). c must be n-independent or the split
   collapses.
3. Deep-region BOUNDED-MOVE lemma. Watch: the outliner's preliminary cheap-kill measured full
   exact Φ (worst Φ/u_n = 0.559/0.368 at n=4/5), but the PROOF mechanism is a bounded (1–2 move)
   reduction, whose value can be strictly larger than full Φ. On the ordinary deep valley
   {30,25,20,15,10}/100 the descending-caterpillar value is 0.05 > u_4≈0.032, and Φ=0 there only
   via a ≥4-element cancellation (tight-cert explorer). The FGR object (min over ALL i of
   dist(a_i,R_{i-1})) DOES reach 0 on that profile (I verified: μ_5=0), so the certified reduction
   is safe — but the deep lemma must be stated over the FULL FGR descending process, not a literal
   "one MATCH" move. The gate G1 must measure the actual mechanism's value, not full Φ.

**Binding precondition (per my R13 rule):** the exact sympy/Fraction gate G1/G2/G3 at n=3,4,5 is a
REQUIRED precondition to any prose. Structured + adversarial, not random (random misled R11). If
G1 fails (deep margin → 0 with n), the split collapses to the full tight problem — report and STOP,
no fake proof. Do NOT use the refuted mass-telescope (per-piece charge vs Σaᵢ) for the deep bound.

Verdict: APPROVE, build (advance). This is the field's strongest line and the only one with a
lever that is both new and VALLEY-TIGHT-compatible.

---

## gen-func-transform (LOWER, new) — APPROVE as a GATED probe (build; refute-and-stop if gate NO)

**Is it a dead-family re-entry?** No. Z(z)=∫₀^L z^{g(t)}dt at z=−1 is a genuinely new OBJECT — a
transform of the whole configuration, not a vertex, word, matching, or running scalar potential
Φ(τ). It is a fixed functional at a fixed point z=−1, so it does NOT fall under the banned
"additive scalar reserve over a moving threshold τ" (R9/R10). None of the 6 dead lower families
covers it. Registration is legitimate.

**Is it DOA repackaging?** The core identity Z(−1)=L−2μ{g odd} is honestly labelled as pure
MID-repackaging (closes nothing). The ENTIRE content is the step-3 two-band recursion, which the
genfunc explorer could not find and flagged as strong repackaging risk. I checked the mechanism
independently: splitting Z(−1) over top band (L/2,L) and bottom band (0,L/2), the bottom-band
integrand factors as (−1)^{N_F−N_{F_B}}·(−1)^{N_{B_B}} — this factors cleanly into a Z_{n−1}(−1)
recursion ONLY if h=N_F−N_{F_B} is trivial on the bottom band, which generically it is not. That
residual h IS the dead SPLIT cross-term μ(O_F∩O_B). So the repackaging risk is REAL and the most
likely gate outcome is NO.

**Why build it anyway (justification, since the dispatch demands one):** the LOWER wall has ZERO
live vehicles and escalation is mandatory. This is a fast, decisive, bounded gate — not open-ended
proof effort. It returns exactly one of two useful things: (a) a clean parity-controlled combining
rule → a genuinely new transform-based induction vehicle for the empty wall (big win); or (b) a
refutation → a cleanly-recorded 7th dead lower family (the transform object) that lets next round
definitively move to a new object class. Dropping it leaves LOWER with no builder AND no closure on
the transform object. A gated probe on an empty wall is worth one builder. It is NOT DOA in the
sense that matters (it is a decision, not a doomed proof). Build it strictly as a gate.

**Binding precondition:** run the exact sympy/Fraction gate FIRST on n=3,4,5 incl. tight
{8,8,4,4,3,2,1,1} and the non-canonical cross-group F={6,6,4} (the minimizing vertex need not be
one-fragment-per-scale — R14). If NO clean IH-carrying combining rule → report the refutation and
STOP, retire the slug, no fake proof. If the bound needs τ-derivative machinery it inherits the
dead scalar-reserve κ-unbounded failure — check early.

Verdict: APPROVE, build as a gated probe.

---

## induction-peel (LOWER, revise recording a refutation) — NOT BUILT (merge lever RETHINK)

The outliner correctly gated and KILLED the recursion-explorer's merge/budget-domination lever for
Case II: (1) per-config monotonicity is FALSE (9.2% failure n=3,4; 14.5% coarser n=3,4,5; freed
tail cut cannot reverse merge's D-increase — round-8 fact); (2) structurally, merging two
≤2^{n-1} fragments generically lands in Case (I), the still-OPEN critical band of (L⋆), not the
solved |F|=2 floor. This is a sound refutation (7th dead lower lever). The global fact
"min_{Case II} D = 1 only in the |F|=2 limit" stays TRUE but needs the same still-open
Gap-Interleaving exchange as the critical band — not a local merge.

Verdict: the merge lever is RETHINK (correctly not built). The slug STAYS LIVE — its certified
machinery (PEEL/SPLIT/ONE/TB/band-decomposition, base cases, |F|=2 sub-case) all stand; only this
one lever died. No builder this round. Ranking records the dead-end outcome.

---

## Field diversity note (for the orchestrator)

The two build slugs attack DIFFERENT walls with DIFFERENT objects (UPPER exact boundary-continuation
of D=2a₁−L; LOWER Z-transform character filter), so no single-gap-trap this round. BUT the LOWER
wall remains the field's structural risk: gen-func is a diversity bet with a likely-NO gate. If it
refutes, next round MUST seed a LOWER framing from a genuinely new object class — transform,
vertex-polytope, word, matching, and running-potential objects are ALL now exhausted. The remaining
untried directions flagged by explorers: the shared Gap-Interleaving exchange lemma (recursion
explorer opening 3 — same DNA as the upper L⋆/GAP-U wall, worth a unified attack), and a 2-scale
self-similar recursion D(n)=φ(D(n−2)) (recursion explorer opening 5). Neither is proposed this
round; flag for the outliner if gen-func dies.

## Ranking (updated this round)

breakpoint-vertex 1789 (leader, live UPPER, new VALLEY-TIGHT-compatible lever) >
parity-measure-potential 1639 (partial, scalar-reserve family dead) >
merge-interleave-pattern 1567 (dead-end, vertex-polytope exhausted) >
gen-func-transform 1530 (new LOWER probe, cold-anchored, gate unrun) >
induction-peel 1497 (dead-end this round, merge lever refuted; slug stays live).
Comparisons anchored to last outcomes: live/new-lever beats dead-ended; the newly-refuted merge
lever and the exhausted vertex-polytope framing sink; gen-func (fresh object) beats both dead-ended
LOWER lines but sits below the two established partials.

build set: breakpoint-vertex, gen-func-transform
