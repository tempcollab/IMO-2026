# Lemma: Reduce move / taint descent (M2)

*If the current triangle has an angle mθ (m a positive integer, m ≥ 2) at a geometric vertex V, then Mulan forces a win in at most m − 1 further cuts, regardless of Shan-Yu's discards.*

## Proof

Mulan cuts to V with α = θ (legal: θ < mθ for m ≥ 2). By the cut operation, the children are:
- C₁ = (θ, B, 180° − θ − B), which contains θ;
- C₂ = ((m−1)θ, C, B + θ), carrying (m−1)θ at the *same geometric vertex* V (V is a vertex of both children, since the cut is from the opposite side to V).

All angles of C₂ are positive: (m−1)θ > 0 (m ≥ 2); C > 0 (inherited); B + θ < 180° because B < 180° − mθ ≤ 180° − 2θ. Also 180° − θ − B > 0 since B < 180° − mθ ≤ 180° − 2θ < 180° − θ.

If Shan-Yu keeps C₁, the game stops and Mulan wins. If he keeps C₂ to delay, the tracked level decreases m → m−1 at the same vertex V (no relocation). Iterate: at level m − j (≥ 2) the cut α = θ is legal (θ < (m−j)θ); keeping C₂ reduces the level by 1; at level 2, C₂'s V-angle is (2−1)θ = θ, so both children contain θ and Mulan wins regardless of the discard.

The level is a natural-valued potential strictly decreasing by 1 each delaying move and terminating at 1 (= θ, a win). Bound: m − 1 cuts.

## Source
Proved in §1 of `results/imo-2026-04/approaches/lattice-descent.md` (round 1); reviewer-certified.
