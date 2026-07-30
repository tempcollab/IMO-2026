# Build report — induction-peel (imo-2026-03), round 4

Focus: close GAP L (lower bound) end to end per the round-3 revised skeleton.
Answer treated CONFIRMED: c(n)=2^n/(2^{n+1}-1), minimax D=u_n=1/(2^{n+1}-1).

## Outcome: partial. GAP L re-localised (and the outline's route corrected), not fully closed.

## What I proved rigorously this round (new)
- **Correct combinatorial formulation.** LB(n) is a *refinement* optimisation (each original
  piece partitioned, total added parts ≤ n) — D depends only on the final multiset, so there is
  no adaptivity subtlety. Clean statement: min D over refinements of C_n={2^n,…,1} with ≤n cuts is ≥1.
- **Lemma PEEL (promotable, fully proved via Lemma M):** unique max f_1 ⇒ D(S)=f_1−D(S\{f_1}).
  This is the round-3 "dominant-cut identity" in exact, cut-free form (their μ(E_R∩[0,p_2)) formula
  is the p_2→0 special case). Verified numerically (20k random multisets, exact).
- **Lemma SPLIT (promotable, fully proved):** D(X⊔Y)=D(X)+D(Y)−2μ(O_X∩O_Y). Carries the cross term
  exactly (the reviewer's mandate: do not bound it away).
- **Lemma ONE (proved):** at most one final piece exceeds 2^{n-1} (top mass 2^n admits ≤1 fragment
  >2^{n-1}; tail fragments ≤2^{n-1}). Verified numerically.
- **Case (a) (top uncut):** D≥2^{n-1}≥1. Full.
- **Case (I) reduced EXACTLY to (L⋆):** when one piece f_1∈(2^{n-1},2^n), PEEL gives D=f_1−D(S'),
  so LB(n) ⟺ D(S')≤f_1−1. Verified numerically true on 55,682 Case-I refinements (n≤6), zero fails.

## The remaining gap (honest)
GAP L now = two sub-inequalities on the dyadic refinement:
- **(L⋆)** D(S')≤f_1−1 in Case (I). This is an *upper* bound on D(S'); crude bounds give only
  D(S')<f_1 (short by the "−1"). It is identical to parity-measure-potential's GAP L1, so a proof
  there imports directly. The SPLIT cross term 2μ(O_A∩O_B) must be carried (dropping it is too lossy
  near f_1→2^{n-1}+).
- **(II)** Case II: all pieces ≤2^{n-1}, no dominant piece, PEEL inapplicable — D≥1 unproven.
Both verified numerically (min D=1 over 60k refinements).

## Spec concerns
- **The round-3 outline's load-bearing reduction is FALSE.** "Budget-monotonicity ⇒ WLOG Xiang
  spends exactly one cut on the top piece" does not hold. Random search shows the minimiser puts
  ALL n cuts on the top (allocation [n,0,…,0]), cutting 2^n into n+1 fragments that interleave the
  uncut tail and telescope to D=1 exactly. Budget-monotonicity says more cuts weakly *help* Xiang —
  the opposite of what "WLOG one cut" needs. Consequently the reviewer's mandated tasks premised on
  it ("tight-safe check at near-bisection p1=2^{n-1}", "commit to route (a) exact branching recursion
  on the single top cut") are attacking a configuration that is not the minimiser; I did not pursue
  them and instead re-derived the correct reduction. The exact identity itself is salvaged and
  strengthened (Lemma PEEL).
- The two lower-bound approaches (induction-peel, two-box-balancing) both premised GAP L on
  single-top-cut framing; both should be re-pointed at (L⋆)/Case II, or at a genuinely global lower
  bound. This is a shared-wall signal for the orchestrator: the lower wall has collapsed to one
  (mis-specified) framing.

## Suggested next step for the outliner
(L⋆) D(S')≤f_1−1 and Case II are the entire lower bound. (L⋆) is a clean upper-type inequality on
a refinement with all pieces ≤2^{n-1} — attack it with the upper-bound machinery (§4 / Lemma DOM /
parity-measure GAP L1), possibly a fresh induction on the number of pieces of S' using PEEL+SPLIT.
Certify Lemma PEEL and Lemma SPLIT into lemmas/ (both fully proved, approach-agnostic).
