# proof-builder report: inversion-at-a-collinearity (round 5)

File written: /home/agentuser/repo/results/imo-2026-02/approaches/inversion-at-a-collinearity.md
Status: partial (unchanged category, but real new progress this round)

## What was done
Dispatched to try closing the round-4-diagnosed gap: hypotheses (ii) angle-LBK=angle-LNC and (iii)
angle-LCK=angle-BMK resist translation via the file's Lemma 2 (SAS-similarity under inversion
centered at A) because neither leg of either angle passes through A.

- Checked inverting at B (for ii) or C (for iii) instead of A: ruled out and documented why — the
  "other" angle in each hypothesis (angle-LNC for (ii), angle-BMK for (iii)) still has neither leg
  through the new center, so no single fixed center among A,B,C,M,N works for both legs of both
  hypotheses simultaneously. This is a genuine structural fact, not just "didn't find it."
- Confirmed (citing this round's math-explorer-newframing2.md numerics, and reasoning about it) that
  a naive spiral similarity for (ii) alone fails (needs a second angle not implied by the hypotheses).
- Found and fully proved a new mechanism that DOES work: **Lemma 4** (vertex-swap angle-to-
  concyclicity translation), a short cross-ratio argument requiring no inversion and no distinguished
  center at all, building only on the file's own Lemma 3 (cross ratio real iff concyclic-or-collinear,
  already proved in prior rounds). Applied it to get:
  - hyp (ii) [on the shared branch] ⟺ B,N,L,W₂ concyclic-or-collinear, W₂ = line(BK) ∩ line(NC)
  - hyp (iii) [on the shared branch] ⟺ C,M,K,W₃ concyclic-or-collinear, W₃ = line(CL) ∩ line(MB)
  Both the general lemma and its two applications are proved symbolically from scratch, plus
  corroborated numerically (Python/cmath, 20 random configurations total, machine-precision matches).
- Honestly assessed why this still does not close the full collinearity chase: (1) W₂,W₃ are still
  coupled in K,L; (2) inverting the new facts at A does not give a clean closed form for W₂*,W₃* in
  terms of K*,L* (inversion doesn't commute with line-intersection); (3) the translation is contingent
  on the same directed-angle branch-selection question flagged elsewhere in the population (inherited,
  not new). Identified but did not execute a promising next step: a no-inversion, same-plane
  radical-axis/Miquel argument combining the three concyclic quadruples (target + two new ones from
  Lemma 4), which share points K, L pairwise.

## Status
Kept as `partial`. This is genuine, provable structural progress (Lemma 4 is fully proved and
reusable), but the approach's overall collinearity chase is still open.

## Promotable lemma flagged for the reviewer
Lemma 4 (vertex-swap angle-to-concyclicity translation) — general-purpose, self-contained (depends
only on the already-certifiable Lemma 3), proved in full in the file. Recommend certification into
results/imo-2026-02/lemmas/ if the reviewer confirms it.
