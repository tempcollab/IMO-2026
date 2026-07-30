# Proof-reviewer report — imo-2026-03, Round 6

Answer treated as confirmed (not re-litigated): c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1).

All four built approaches remain **partial** with honestly-stated, precisely-localised gaps. No
approach claims `solved`; each recorded Status (`partial`) matches reality. No overclaim detected —
every "PROVED" sub-part I re-derived checks out, and every open gap is labelled as open. Verdict for
each: **CHANGES REQUESTED**.

Independent numeric re-derivation this round: Lemma TB identity D(R)=e+D_low held exactly on 20000
random ≤n-cut refinements of C_n (n≤4); the L2 master inequality D(S)≥|D(F)−D(B)| held on 20000
random partitions. The three threshold identities (3.1),(3.3),(3.1'/UB) verified by hand.

---

## breakpoint-vertex — CHANGES REQUESTED (Status: partial)

**New this round: Lemma TB (top-band decomposition), PROVEN and CERTIFIED.**
D(R)=e+D_low, e=(f₁−2^{n-1})⁺, D_low=μ{t<2^{n-1}:N_R odd}. I re-derived it independently: split the
Lemma-M integral at 2^{n-1}; certified Lemma ONE forces N_R(t)∈{0,1} for t≥2^{n-1} (two pieces
>2^{n-1} would sum to >2^n), so the top band contributes exactly (f₁−2^{n-1})⁺. Correct and rigorous.
Consequences closed **unconditionally, profile-independently**: base n=0, trivial regime
f₁≥2^{n-1}+1 (⇒D≥1), Case (a) top-uncut (⇒D≥2^{n-1}). Standing PL1 + Theorem VERT unchanged.

- Scores: Correctness 10/10 (TB is exact), Rigor 9/10, Progress: real — moved the whole lower
  bound to a single scalar bound on D_low in two thin residual cases.
- **Gaps remaining:** GAP L-fin = (L1) D_low≥2^{n-1}+1−f₁ in the width-1 critical band, and (L2)
  D_low≥1 top-shredded; GAP U-fin = a₁<L/2 vertex bound. §4A's closing paragraph ("the extremal
  interleavings give exactly the boundary values… both inequalities are tight and consistent") is
  a plausibility statement, NOT a proof of the universal lower bound — VERT finitizes the search
  per n but the profile-independent argument is not written. Correctly labelled open.

## induction-peel — CHANGES REQUESTED (Status: partial)

New this round, both re-checked and correct: (i) band decomposition (3.1) unifying Cases (I)/(II);
(ii) **trivial regime of (L⋆) closed** — for w≤2^{n-1}−1, D(S')≤max(S')≤2^{n-1}≤f₁−1 (f₁=2^n−w, so
f₁−1≥2^{n-1}); (iii) **|F|=2 sub-case of Case II closed** via Lemma HALF (F={2^{n-1},2^{n-1}} ⇒
D(S)=D(T)≥1 by IH). Exact telescoping identities for both canonical extremal layouts are correct
identities (verified), establishing tightness — the file correctly does NOT claim these are the
extremisers (the exchange step is explicitly open).

- Scores: Correctness 10/10, Rigor 9/10, Progress real.
- **Gaps remaining:** GAP L2 = the single adjacent-pair exchange step (critical band of L⋆ +
  |F|≥3 of Case II); GAP U = balanced upper (a₁<L/2). The "GAP L2" write-up is candid that the
  per-cut |ΔD|≤2s₂ bound is too loose and the monovariant exchange inequality is unwritten.

## smoothing-majorization — CHANGES REQUESTED (Status: partial)

Genuine reframe: the upper bound as a finite DELETE/MATCH D-tracking game (Lemma DM certified).
Four-case strong induction on n; I verified the three closing identities exactly:
u_{n-1}(1−c(n))=u_n (3.1); whole-tail-peel gives 2a₁−L≤u_nL for L/2≤a₁≤c(n)L (3.2);
u_{n-1}(1−2β_n)=u_n (3.3). Cases 3.1–3.4 are disjoint and exhaustive; residuals (piece counts,
budgets) are correct — Step 3.3's residual R has exactly n pieces, budget n−1, so UB(n−1) applies.

- Scores: Correctness 10/10 (the three closed cases), Rigor 9/10, Progress real (diversifies the
  upper bound away from the refuted mass-threshold framing).
- **Gap remaining:** GAP U-VALLEY = the sole uncovered case a₁<L/2 & a₂<β_nL. Honestly open; the
  §5 numerics (worst ratio 0.75; deterministic-rule refutations 4.2×–25.5×) corroborate the target
  and refute simple rules but are explicitly flagged "not a proof step." Correct.

## parity-measure-potential — CHANGES REQUESTED (Status: partial)

**L2 SPLIT master inequality D(S)≥|D(F)−D(B)| — PROVEN, re-verified.** From certified Lemma SPLIT
D(S)=D(F)+D(B)−2μ(O_F∩O_B) and μ(O_F∩O_B)≤min(D(F),D(B)); x+y−2min(x,y)=|x−y|. Rigorous. With IH
D(B)≥1 it closes the whole |D(F)−D(B)|≥1 subregime of GAP L2, including every even-multiplicity
fragmentation D(F)=0 (via certified U0(a)). Extremal value 1 computed two ways (attained cascade;
(L2-telescope) merged formula) — an exact identity, not a sample. Lemma U0 written cleanly and
**certified** this round. Whole a₁≥L/2 upper range remains closed (Branch 0 + whole-tail Branch 2).

- Scores: Correctness 10/10, Rigor 9/10, Progress real; strongest of the field (elo 1637).
- **Gaps remaining:** GAP L1 (a=1: D(S_L)≤f₁−1); GAP L2-exch (the cross-term bound
  μ(O_F∩O_B)≤(D(F)+D(B)−1)/2, binding only in the balanced |D(F)−D(B)|<1, D(F)>0 subregime — the
  interleaving-extremality crux); GAP U (a₁<L/2, mass-threshold refuted, needs D-tracking). All
  correctly labelled; the round-6 self-flag that master is lossy exactly when D(F)≈D(B) (found
  D(F)=D(B)=1 with true D(S)=2) is accurate.

---

## Lemmas certified this round (3 of 3 accepted)

- **top-band-decomposition.md (Lemma TB)** — CERTIFIED. Exact; depends only on certified M and ONE;
  statement no stronger than proved. Independently re-derived and numerically re-verified.
- **elementary-reductions.md (Lemma DM)** — CERTIFIED. DELETE/MATCH via certified Lemma P; a
  sufficiency (legal-response) claim, not an optimality claim — no extremality smuggled in. Legality
  uses the same mechanism as the already-certified whole-tail-peel.
- **even-multiplicity-corrector.md (Lemma U0)** — CERTIFIED. (a) direct from measure identity;
  (b) needs budget≥m and is simultaneous (sequential is refuted — caveat present); (c) reduces UB
  to full budget m=n+1. Self-contained on M/P.

No lemma rejected.

## Goal progress

- Field-wide: all four approaches **advanced** (recorded via approach-ranker). 3 new shared lemmas
  certified (10 total). Both lower-bound routes (rearrangement in induction-peel; measure/SPLIT in
  parity-measure) now isolate the SAME interleaving-extremality crux from independent angles —
  diversity insurance intact, but the field has again converged the lower bound onto one exchange
  inequality.
- Elo after round: parity-measure-potential 1637 (leader), induction-peel 1586,
  smoothing-majorization 1505, breakpoint-vertex 1500.
- **Shared walls persisting (3+ rounds):** LOWER interleaving-exchange (L1/L2-exch), UPPER a₁<L/2.
  breakpoint-vertex's VERT is the one lever that genuinely reframes the upper wall (finitization);
  next round should push a builder to convert VERT+U0 into the uniform vertex bound for a₁<L/2, and
  push one builder squarely on the single exchange inequality (it now closes BOTH lower gaps at
  once). No RETHINK warranted — every approach is on a live, correct line.
