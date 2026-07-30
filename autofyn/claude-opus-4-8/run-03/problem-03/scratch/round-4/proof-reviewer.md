# Proof review — imo-2026-03, round 4

Answer treated CONFIRMED (reviewer brute force n=0,1,2): c(n)=2^n/(2^{n+1}−1),
minimax D = u_n = 1/(2^{n+1}−1). Neither built approach claims `solved`; both self-report
`partial`. I independently re-derived every new load-bearing claim.

---

## Approach 1: induction-peel — Verdict: CHANGES REQUESTED (Status: partial)

Builder's recorded Status `partial` is CORRECT.

**Independently verified new content (all correct):**
- **Lemma PEEL** `D(S)=f₁−D(S∖{f₁})` for a unique max: re-derived from Lemma M and checked
  on 5000 random multisets — max error 0. Proof (band split at the 2nd-largest value) is
  rigorous and self-contained. CERTIFIED → `lemmas/strict-max-peel.md`.
- **Lemma SPLIT** `D(X⊔Y)=D(X)+D(Y)−2μ(O_X∩O_Y)`: pointwise-XOR proof correct; checked on
  3000 random partitions — max error 1.1e-16 (round-off). CERTIFIED → `lemmas/split-cross-term.md`.
- **Lemma ONE** (≤1 final piece >2^{n-1}): elementary superincreasing argument, correct.
  CERTIFIED → `lemmas/top-scale-dichotomy.md`.
- **"No adaptivity" reformulation:** correct — D is a function of the final multiset and
  Xiang's play is a refinement, so LB(n) = min over refinements. Sound.
- **Correction of the round-3 "WLOG single top cut":** I confirm the round-3 premise was
  FALSE. The minimiser does put all n cuts on the top (allocation [n,0,…]), and
  budget-monotonicity points the opposite way. Good catch; correctly retracted.
- **Case (a)** (top uncut ⇒ D≥2^{n-1}≥1) and **exact reduction of Case (I) to (L⋆)
  D(S')≤f₁−1** via PEEL: both correct.

**Real gap remaining (GAP L):** (L⋆) `D(S')≤f₁−1` [Case I] and Case II (`D≥1` when every
piece ≤2^{n-1}). Numerically verified but not proved. GAP U (balanced upper, a₁<L/2) unchanged.

**Score:** Correctness 10/10 (nothing false; false premise correctly retracted).
Completeness 6/10 (two lower sub-inequalities + balanced upper open). Progress: real —
exact reduction + 3 certified lemmas.

---

## Approach 2: parity-measure-potential — Verdict: CHANGES REQUESTED (Status: partial)

Builder's recorded Status `partial` is CORRECT.

**Independently verified new content (all correct):**
- **Whole-tail-peel Branch (2):** for L/2 ≤ a₁ ≤ c(k)L, cutting a₁ into the m−1 tail values +
  leftover 2a₁−L (feasible iff a₁≥L/2; ≤k cuts since m≤k+1), deleting pairs by Lemma P, leaves
  the single piece 2a₁−L, so D = 2a₁−L, and 2a₁−L ≤ u_kL ⟺ a₁≤c(k)L via c(k)=(1+u_k)/2. I
  verified the algebra exactly and the bound on 200 random dominant profiles. CORRECT.
  CERTIFIED → `lemmas/whole-tail-peel.md`. NOTE: the *companion* bisect branch (a₁≥c(k)L) is
  conditional on the inductive hypothesis UB(k−1); only the whole-tail piece is unconditional.
  The lemma file records this — do not cite "entire a₁≥L/2 closed" as unconditional.
- **Refutation counterexample (0.44,0.281,0.279), k=2:** I re-checked with exact fractions.
  Bisecting a₁ gives {0.281,0.279,0.22,0.22}, D = 1/500 = 0.002 ≤ 1/7 = u_2. Every
  mass-threshold move is unavailable: Branch 0 / whole-tail need a₁≥1/2 (0.44 fails); j=1 peel
  size-1 sums 0.281,0.279 < θ₁=2/7; j=2 peel sum 0.560 > a₁=0.44 (cap violated). So the
  subset-cover disjunction is genuinely NON-EXHAUSTIVE for a₁<L/2. The negative result is
  SOUND and valuable — it kills the mass-only lever and correctly redirects GAP U to a
  D-tracking argument. Recorded in the whole-tail-peel lemma file as a negative companion.
- **Lower bound:** Case A + a=0 equal-bisection subcase correct; a=1 exact identity
  D(S)=f₁−D(S_L) (= Lemma PEEL) correct.

**Real gaps remaining:** GAP U (a₁<L/2, needs D-tracking); GAP L1 (D(S_L)≤f₁−1, = induction-peel's
(L⋆)); GAP L2 (a=0 shredded top, ≥3 fragments).

**Score:** Correctness 10/10 (whole-tail peel exact; refutation verified). Completeness 6/10
(a₁<L/2 upper + two lower gaps open). Progress: real — a whole upper region newly closed +
a decisive negative that stops a dead lever.

---

## Lemma certification summary
CERTIFIED this round (all independently verified):
`lemmas/strict-max-peel.md` (PEEL), `lemmas/split-cross-term.md` (SPLIT),
`lemmas/top-scale-dichotomy.md` (ONE), `lemmas/whole-tail-peel.md` (+ negative companion).
NOT certified as unconditional: "Lemma DOM / entire a₁≥L/2 closed" — its bisect branch depends
on the still-open upper-bound induction UB(k−1); only its whole-tail sub-branch is unconditional.

## Goal Progress
- **Ranking (post-round):** parity-measure-potential elo 1602.6 (advanced), induction-peel
  1561.8 (advanced) — both LIVE, both expanded=2. Dormant/unbuilt: two-box-balancing 1504.8,
  smoothing-majorization 1472.6, lp-dual-weight 1470.0, explicit-pairing-strategy 1388.1.
- **Gaps closed this round:** upper-bound region a₁≥L/2 fully closed (whole-tail peel, certified);
  lower Case I exactly reduced to a single inequality (L⋆); 3 new exact lemmas certified; the
  false round-3 "WLOG single top cut" retracted; the mass-threshold upper lever refuted.
- **Gaps open (now SHARED across both live approaches — a hardening shared wall):**
  1. **Lower (L⋆)/GAP L1:** D(S')≤f₁−1 with all pieces ≤2^{n-1}. Both approaches reduce Case I
     to this identical inequality. Needs the SPLIT cross term carried (crude bound short by −1).
  2. **Lower Case II / GAP L2:** D≥1 when the top is shredded into all-≤2^{n-1} fragments.
  3. **Upper GAP U (a₁<L/2):** provably NOT closable by mass-only bounds; needs D-tracking.
- **Orchestrator signal:** the two live approaches have now converged onto the SAME lower
  inequality (L⋆ = GAP L1) and the SAME upper obstruction (a₁<L/2 requiring D-tracking). This
  is a shared-wall collapse. Next round should either (a) put a builder squarely on (L⋆) using
  the now-certified PEEL/SPLIT machinery (it is a clean upper-type inequality on a
  ≤2^{n-1}-bounded refinement — attackable by induction on piece count), and (b) activate a
  genuinely different framing for the upper a₁<L/2 regime (smoothing-majorization or
  lp-dual-weight are dormant and are exactly the D-tracking framings the refutation calls for).
