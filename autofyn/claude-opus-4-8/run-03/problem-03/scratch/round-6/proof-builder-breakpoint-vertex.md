# Build report — breakpoint-vertex (imo-2026-03), round 6

## Status: partial

## What I closed this round
- **Lemma TB (top-band decomposition) — PROVEN in full and proposed for certification**
  (`results/imo-2026-03/lemmas/top-band-decomposition.md`). For any refinement $R$ of $C_n$,
  $$D(R)=(f_1-2^{n-1})^+ + D_{\mathrm{low}},\qquad D_{\mathrm{low}}=\mu\{t\in(0,2^{n-1}):N_R\text{ odd}\}.$$
  Proof = split the certified Lemma-M integral at the threshold $2^{n-1}$ + certified Lemma ONE
  ($\le1$ piece above threshold ⇒ $N\le1$ there, so the band contributes exactly $(f_1-2^{n-1})^+$).
  Depends only on certified Lemmas M and ONE. Numerically confirmed (3000 random multisets, exact).
- **Lower bound consequences now UNCONDITIONAL and profile-independent:** base case $n=0$; the
  **trivial regime** $f_1\ge2^{n-1}+1\Rightarrow D\ge1$; and **Case (a)** (top uncut) $\Rightarrow
  D\ge2^{n-1}\ge1$. These follow in one line each from Lemma TB (no exchange/interleaving needed).
- The whole lower bound is now **cleanly reduced** to a single scalar bound on $D_{\mathrm{low}}$ in
  exactly two small-excess sub-cases: (L1) critical band $2^{n-1}<f_1<2^{n-1}+1$ needs
  $D_{\mathrm{low}}\ge2^{n-1}+1-f_1$; (L2) top-shredded $f_1\le2^{n-1}$ needs $D_{\mathrm{low}}\ge1$.
  This recovers the induction-peel "trivial/critical band" split rigorously and independently, from
  a global measure identity rather than PEEL — and the critical band has width exactly 1 in $f_1$.
- **Standing proven (round 5, unchanged):** Lemma PL1 (single-cut PL, slopes $\{-2,0,2\}$),
  Theorem VERT (optimal refinement is a polytope vertex, $\le n+1$ distinct values; rank-count proof
  re-verified correct — restriction to $W_0$ decreases rank, giving $N-M\le N-d$, i.e. $d\le M$).

## What remains as explicit gaps
- **GAP L-fin** (lower): $D_{\mathrm{low}}\ge2^{n-1}+1-f_1$ (L1) and $D_{\mathrm{low}}\ge1$ (L2).
  Finite per $n$ by VERT, but the profile-independent proof still needs the one-per-gap
  exchange/telescoping argument with Lemma SPLIT's cross term carried (margin $\to0$ at
  $f_1\to2^{n-1}$). This is the SAME residual object as induction-peel's Gap-Interleaving Lemma and
  parity-measure's toggle route — a genuine shared wall.
- **GAP U-fin** (upper, $a_1<L/2$): simultaneous even-pairing vertex response + exact leftover bound
  $\rho\le u_nL$ via SPLIT. Shared endgame with smoothing-majorization regime (i). Untouched this
  round.

## Honesty / overclaim check
- I did NOT reuse greedy-merge, single-cancelling-pair-peel, or mass-threshold subset-cover as the
  Xiang upper strategy. Upper bound only imports the certified whole-tail-peel ($a_1\ge L/2$).
- Lower-bound target $\min_R D=1$ reconfirmed by exact brute force ($n\le4$, integer and $1/12$-grid
  refinements): min is exactly 1 (e.g. $\{3,2,1,1\}$ at $n=2$, $\{8,8,4,4,3,2,1,1\}$ at $n=4$). So
  Lemma TB and the residual gaps are aimed at a true statement.
- No sample-point "proof" of exhaustiveness anywhere; Lemma TB and the trivial-regime closure are
  fully general.

## Spec concerns
None. Reduction (Lemma R), answer $c(n)=2^n/(2^{n+1}-1)$, minimax $D=u_n$ all consistent with the
certified base cases.

## For the reviewer
- Please certify **Lemma TB** (`lemmas/top-band-decomposition.md`) — clean, depends only on certified
  M + ONE, importable by induction-peel and parity-measure (it gives their trivial/critical split for
  free and pins the residual to $D_{\mathrm{low}}$).
- The lower wall (GAP L-fin) and upper wall (GAP U-fin) remain the field's shared gaps; TB narrows
  the lower wall to the single scalar $D_{\mathrm{low}}$ in a width-1 band, which may help the
  next-round outliner target the exchange argument precisely.
