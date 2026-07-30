# imo-2026-03 — outline-reviewer report (round 2)

## Preamble / independent sanity checks performed

All claims below were reproduced independently (exact `Fraction` arithmetic); I did NOT take
the outliner's or explorers' word. Findings:

- **Frontier recursion `D(T_m)=2^m−D(T_{m−1})`, `D(T_0)=D(T_1)=1`: CONFIRMED** for m=2..7
  (D(T_2)=3, D(T_3)=5, D(T_4)=11, …). The parity-flip identity holds exactly. This is solid
  scaffolding for `tower-induction`.
- **Parallel-halving saturates the tower: CONFIRMED** n=1..5 — splitting each of the tower's n
  largest pieces in half yields D=1 (tower units = 1/D_n) exactly. The mechanical lemma for
  `majorization-upper` is sound.
- **Tower is UNIQUE worst (n=2,3): CONFIRMED.** n=2: every non-tower /7 config (5,1,1; 3,3,1;
  3,2,2; 5,2; 4,3; 6,1) admits Xiang-best D=0 (not just <1/7); the tower alone holds D=1/7.
  n=3: tower Xiang-best (3 marks) = 1/15 exactly; every ±ε perturbation of the top two pieces
  gives strictly < 1/15 (tested d=±1,±3,±5 on a 1/1000 grid). The "tower is hardest" conjecture
  is strongly backed.
- **Dominant factorization identity `(2^n−1)/D_{n−1}=1` and `R/D_{n−1}≤1/D_n` at the
  threshold `L=2^n/D_n`: CONFIRMED** exact for n=2..7. The arithmetic closes perfectly.
- **Parity-rest-starts-at-position-3 under `L/2>a_2` (strict): 0 violations over 155 836 random
  dominant configs.** (The 1358 "violations" in a non-strict run are tie artifacts where `a_2=L/2`
  and `.index()` finds the L/2 pieces.) The parity-clean claim is sound.
- **Below-threshold regime (Case C) is NONEMPTY for n=2:** L=0.55<4/7, parity-clean, but
  R/D_1=0.15>1/7=0.143 — induction overshoots. Explorer B's "three regimes" correction is real;
  the outliner's `majorization-upper` step 6 handles it as a flagged gap.
- **Single-split PL plateau reaches a DYADIC breakpoint: CONFIRMED for T_3 single top-split.**
  D(q) is constant on the plateau q∈[2,4] (=3, tower units), and q=4 is the dyadic balanced
  split (8→4+4). Breakpoints occur only at tower-piece values q∈{1,2,4}. So for the SINGLE
  split, non-dyadic breakpoints genuinely lie on a plateau reaching a dyadic one. **BUT** the
  minimum over single splits is D=3 ≥ 1 (easy); the global minimum D=1 requires MULTI-splits,
  and the multi-split plateau claim (G1) is the open crux — verified for n=3 numerically (121
  configs at D=1, only 1 dyadic) but NOT proved in general. The outline flags this honestly as
  G1, the load-bearing hard step, and does NOT assume it. Good.

No false lemmas detected this round. The round-1 parity-interleaving bug and the dead
naive-halving end are explicitly avoided by all three build slugs.

---

## Approach 1: `tail-count` (ADVANCE) — APPROVE

**Technique sound.** The `N(t)`-integral / piecewise-linearity-in-split-position / breakpoint-
minimum / plateau framing is the right machinery for the lower-bound case (b), and it is the
ONLY approach whose lower-bound engine handles the continuous split parameter directly (vs
`tower-induction`'s discrete tree/frontier combinatorics). The PL-minimum-at-a-breakpoint lemma
is sound (compactness + PL structure, supported by knowledge_base "Piecewise-concavity
smoothing"). The frontier recursion (imported via `tower-induction` or proved here) gives the
dyadic-breakpoint base. The ΔD formula is verified.

**Issues the builder must close (in priority order):**

1. **G1 (THE crux) — multi-split plateau-connects-non-dyadic-to-dyadic.** This is the
   load-bearing hard step and is UNVERIFIED in general. The outline correctly flags it as open
   and tells the builder to ATTACK it, not assume it. The builder must produce a genuine
   structural/continuity argument (a combinatorial-type-invariance lemma showing that between a
   non-dyadic breakpoint and the nearest dyadic one no further breakpoint intervenes, so the ΔD
   slope is 0 on the plateau), NOT a type enumeration. The round-1 B3-circularity warning applies
   here in full force: "checking every type ≤ bound" IS the bound. Flag this as the make-or-break
   step; if it cannot be closed this round, the builder should at least formalize the PL lemma and
   close the single-split case rigorously as partial progress.

2. **G2 — multi-split compounding parity landscape.** After the first split `N(t)` is no longer
   the clean tower staircase, so `O([0,q])` for the second split is harder. The PL/breakpoint
   argument must handle ≥2 splits of the top AND splits of non-top pieces. The variational
   minimum is over ALL ≤n-mark refinements, not just single top-splits. This overlaps with
   `tower-induction`'s G2 (same wall, opposite machinery — see diversity assessment).

3. **Avoid the crude `D_rest ≤ largest rest piece` bound** — it degenerates exactly at the
   balanced minimum (round-1 dead end). The outline already warns this; the builder must use the
   ΔD parity structure, not the crude bound.

**Verdict:** APPROVE. Build. The PL route is the most promising lower-bound engine because it
attacks the continuous parameter directly; even partial progress (PL lemma + single-split rigor
+ multi-split n=3 verification) is solid certified output.

---

## Approach 2: `tower-induction` (REVISE) — APPROVE

**Technique sound.** Replacing the self-similar IH (which bottomed out on the unequal/multi-
split interleaving, per round 1) with the frontier recursion `D(T_m)=2^m−D(T_{m−1})` as the
lower-bound engine is a clean scaffold improvement. Absorbing the would-be `frontier-recursion`
slug here avoids the shared non-dyadic-breakpoint wall being split across two identical slugs
(the single-gap trap) — the fold is the right call. The upper bound stays a dominance-case-split
induction with the below-threshold gap OPEN and explicitly a FALLBACK (not a rival to
`majorization-upper`) — no second upper-bound slug. Good.

**Issues the builder must close:**

1. **Extract the frontier recursion as a standalone importable lemma.** Prove
   `D(T_m)=2^m−D(T_{m−1})`, `D(T_0)=D(T_1)=1`, rigorously for all m (verified m=2..7 here). This
   is concrete, certifiable progress even if G1/G2 fail — it closes the balanced-split sub-case
   (b-i) standalone (currently conditional on IH). This is this slug's main deliverable.

2. **G1 — frontier-minimum lemma ("expanding all levels above m is optimal").** The non-
   monotonicity blocker is real and honestly flagged: expanding level 3 alone INCREASES D for
   n=4 (explorer A). A naive monotone argument fails; needs a genuine exchange step. The
   outline flags this as a GAP. The builder must either prove the exchange or leave it open
   honestly (do NOT present the verified-n=3..6 numerics as a proof).

3. **G2 — unbalanced→frontier reduction.** The outline TRANSPARENTLY admits this is "the same
   wall viewed from the frontier side" as `tail-count`'s non-dyadic-breakpoint gap. This is
   honest and necessary. The two slugs converge on the non-dyadic↔dyadic reduction from opposite
   machinery (see diversity assessment for why I allow both).

4. **Upper bound** stays a fallback with the dominant recurrence + below-threshold gap open —
   held, not the primary upper-bound route (`majorization-upper` owns that). Do not build it out
   as a rival; keep the gap honest.

**Verdict:** APPROVE. Build. The frontier-recursion lemma extraction is the concrete
deliverable; the frontier-minimum exchange is the hard step.

---

## Approach 3: `majorization-upper` (NEW) — APPROVE

**Technique sound and genuinely different.** The extremal/exchange framing "tower is the UNIQUE
worst Liu config" + config-adaptive pairing is the ONLY upper-bound-first approach, and its
spine (exchange monotonicity of `min_Xiang D` with the tower as maximal element) is a different
wall from `d-potential`'s Φ-existence, `tail-count`'s parity-coupling, and
`tower-induction`'s induction. The proven scaffolding is solid: parallel-halving-saturates-
tower (confirmed n=1..5 here), dominant factorization (identity confirmed exact n=2..7), pairing
cancellation (parity confirmed 0 violations strict). These are mechanical lemmas ready to
certify.

**Issues the builder must close:**

1. **G1 (THE crux) — the exchange monotonicity.** "Moving any consecutive ratio toward dyadic
   2:1 increases `min_Xiang D`." This is a CONJECTURE (verified n=1..4, not proved) and is the
   research question. The outline correctly flags it and, crucially, warns against the B3
   circularity trap: the builder must produce a GENUINE monotonicity/smoothing argument (using
   the `D=∫(N mod 2)dt` residual language), NOT a type-by-type enumeration. If G1 cannot be
   closed this round, the builder should at least (a) certify the three mechanical lemmas, (b)
   prove the clean n=2 case (every non-tower config admits D=0, confirmed here) as a base, and
   (c) record G1 honestly as the open crux. Do NOT present the n=1..4 numerics as a proof.

2. **G2 — below-threshold regime n≥3 (cases C/B2).** The strengthened two-variable IH
   `D≤f(R,M,n)` or the max-reduction coincidence. Computationally verified (0 violations n=2,3);
   structurally easier than the dominant case but not proved. Flag honestly.

3. **G3 — adaptive-pairing specification for non-tower n≥3.** The cascade structure is more
   intricate than n=2 (where every non-tower admits D=0); the residual is nonzero and the pairing
   strategy must be explicitly specified and proven to leave residual ≤ 1/D_n.

4. **Circularity audit (performed).** The exchange step as FRAMED is NOT "check every type ≤
   bound" — it is a claimed monotonicity (ratio-smoothing). It is not circular AS FRAMED; it is
   an open conjecture. The risk is that the builder, unable to prove the monotonicity, falls back
   to a type enumeration — that WOULD be the B3 trap. The outline's warning is sufficient; enforce
   it. Harvesting Lemma B1 (Xiang's optimum at a balanced/tie refinement) is a LEGITIMATE import:
   it restricts Xiang's continuous optimization to balanced types, reducing the exchange's case
   space — it constrains, it does not assume the bound. Not circular.

5. **Single-gap audit (performed).** There is exactly ONE upper-bound slug
   (`majorization-upper`). The outliner did NOT re-introduce an `inductive-upper` rival —
   confirmed. Explorer B's strengthened-IH stays a FALLBACK within step 6, not a separate slug.
   Good.

**Verdict:** APPROVE. Build. Even if the exchange crux stalls, the three mechanical lemmas + the
n=2 base + the verified tower-saturation witness are genuine certified progress on the (harder)
upper-bound direction.

---

## Approach 4: `d-potential` — HOLD (do not build)

Confirmed. Φ=D is circular (witness T_1: D stays 1/3 under the optimal mark, but 2/D+1=7 —
verified the recursion is a game-value fact, not a per-config decay). No concrete Φ exhibited.
All certified outputs (Lemma 0, closed-form, n=1 base, case-A) already in the shared cache;
re-building gains nothing. The outline's pivot suggestion (game-value potential
`Φ(L)=min_Xiang D(refine(L))`) collapses toward the inductive route — a last resort, not this
round. HOLD is correct.

---

## Approach 5: `self-similar` — HOLD (do not build)

Confirmed. Subsumed by `tower-induction`'s frontier-recursion scaffold (the clean rescaling
identity is absorbed). A separate build duplicates `tower-induction`'s lower-bound work. HOLD.

---

## Approach 6: `balanced-configs` — RETIRE (harvest B1)

Confirmed. B3 (structural check every type ≤ bound) is circular. RETIRED as a build target; stays
registered (not built). Lemma B1 (piecewise-linearity ⇒ Xiang optimum at balanced/tie
refinement) is sound and genuinely useful — the `majorization-upper` builder certifies it as an
import to restrict the exchange to balanced types. Do NOT build B3-circular.

---

## Field diversity assessment — does NOT collapse to one framing

The three build slugs attack DIFFERENT walls:

- **`tail-count`** — lower bound, non-dyadic-breakpoint plateau, **integral/PL language**
  (continuous split parameter; parity via the ΔD formula's ceiling).
- **`tower-induction`** — lower bound, frontier monotonicity, **tree/frontier language**
  (discrete expansion patterns; parity via the flip recursion).
- **`majorization-upper`** — upper bound, exchange monotonicity, **extremal language**
  (tower as unique worst; config-adaptive pairing; residual-integral).

**Shared-wall audit (the one real overlap):** the two lower-bound slugs (`tail-count`,
`tower-induction`) CONVERGE on the non-dyadic↔dyadic reduction (tail-count G1 ≈ tower-induction
G2). The outline is transparent about this. I judge the machinery is GENUINELY DIFFERENT
(continuous-variational vs discrete-combinatorial), so building both is not the single-gap trap:
each produces a DIFFERENT certified lemma (PL-minimum/breakpoint lemma for tail-count; frontier-
recursion lemma for tower-induction), and each cracks a different sub-case cleanly (tail-count:
single-split plateau; tower-induction: balanced-split sub-case). If both fail on the multi-split
reduction, we learn the gap is genuinely hard from two angles — valuable signal, not waste. The
upper-bound slug's wall (exchange monotonicity) is far from both lower-bound walls. No two slugs
share a single wall as their only bottleneck.

The field's upper-bound walls are now genuinely far apart: exchange monotonicity
(`majorization-upper`), Φ-existence (`d-potential`, held), parity-coupling (`tail-count`,
held-open on the upper side), induction recurrence (`tower-induction`, fallback). Good diversity.

---

## Ranking

Pairwise comparisons, anchored to gap analysis + last outcomes (tail-count, d-potential,
tower-induction carry `verified-milestone` outcomes from round 1, now stale→cleared;
self-similar/balanced-configs have no outcome; majorization-upper is cold-start 1500).
Newcomer `majorization-upper` was compared against the established field so its rating anchors
to real opponents, not just its absence of outcomes.

- `tail-count` > `tower-induction` — tail-count's PL route handles the continuous split
  parameter directly (more likely to crack the multi-split plateau); tower-induction's frontier
  route hits the non-monotonicity blocker AND shares the non-dyadic wall (G2).
- `tail-count` > `majorization-upper` — tail-count has more proven groundwork (Lemma 0,
  layer-cake, D-integral, case-a, n=1 base ALL certified) and a concrete advancing gap (plateau,
  verified n=3); majorization-upper's exchange is an unproven conjecture (cold-start).
- `tail-count` > `d-potential` — tail-count active and advancing; d-potential Φ-stuck (circular).
- `majorization-upper` = `tower-induction` (draw) — majorization-upper owns the crux
  upper-bound direction with verified scaffolding (parallel-halving, dominant-factorization,
  pairing all confirmed) and strong n=1..4 numerics; tower-induction has a certified
  verified-milestone + the frontier-recursion lemma to extract. Both have genuine partial
  progress in DIFFERENT directions; neither clearly dominates.
- `majorization-upper` > `d-potential` — majorization-upper has a concrete mechanism + verified
  scaffolding for the upper bound; d-potential's Φ is circular with no candidate.
- `tower-induction` > `d-potential` — tower-induction advancing (frontier recursion);
  d-potential stuck.
- `tail-count` > `self-similar`; `majorization-upper` > `self-similar`;
  `tower-induction` > `self-similar`; `d-potential` > `self-similar` — self-similar is held,
  subsumed, no standalone outcome; the others are active or have certified outputs.
- `self-similar` > `balanced-configs` — self-similar has a clean rescaling identity (held, not
  circular); balanced-configs is retired (B3 circular).
- `tail-count`, `majorization-upper`, `tower-induction`, `d-potential` > `balanced-configs`
  (retired).

Resulting Elo order (best→worst) after the K=32 update:
**`tail-count` (≈1603) > `tower-induction` (≈1530) ≈ `majorization-upper` (≈1529) >
`d-potential` (≈1519) > `self-similar` (≈1438) > `balanced-configs` (≈1382, retired).**

---

## Registrations / copy actions

- **Registered (new):** `majorization-upper` — cold-start Elo 1500. (Confirmed new slug;
  `tail-count`/`tower-induction` already registered, revising — no re-register.)
- **Copy (branch):** none. The outliner said "branching requested: none"; confirmed — no
  existing approach needs twin branching this round.
- **Retired (stays registered, not built):** `balanced-configs` — B3 circular; Lemma B1
  harvested by `majorization-upper`.
- **Held (registered, not built):** `d-potential` (Φ-stuck), `self-similar` (subsumed).

---

## Build set

Three builders, one per slug — the three active lines, each closing a different gap:

build set: tail-count, tower-induction, majorization-upper

- `tail-count` — close lower-bound case (b) via the variational/breakpoint/plateau route; G1
  (multi-split plateau-connects-non-dyadic-to-dyadic) is the make-or-break step.
- `tower-induction` — extract the frontier recursion `D(T_m)=2^m−D(T_{m−1})` as a standalone
  importable lemma (closes balanced sub-case b-i standalone); attack the frontier-minimum
  exchange (G1) and the unbalanced→frontier reduction (G2, shared wall with tail-count).
- `majorization-upper` — certify the mechanical scaffolding (parallel-halving-saturates-tower,
  dominant-factorization, pairing-cancellation) + Lemma B1; attack the exchange monotonicity
  (G1, the upper-bound crux) and the below-threshold regime (G2) for n≥3.
