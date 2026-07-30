# Lemma: Alignment move (M1)

*If nθ = 180° (n ≥ 3 integer) and the current triangle T contains no positive integer multiple of θ, then Mulan cuts to the largest angle's vertex with α = kθ − B for a pigeonhole-existing k ∈ {1, …, n − 1}; both children's fresh P-angles become positive multiples kθ and (n − k)θ.*

## Proof

Let A be the largest angle, so A ≥ 60° ≥ θ = 180°/n, with equality A = 60° = θ only when T is equilateral and n = 3 — but then T contains θ and Mulan has already won. Hence, under the hypothesis, A > θ.

The open interval (B, A + B) has length A > θ. Multiples of θ are spaced θ apart on the line; by the pigeonhole/extremal principle, an open interval of length strictly greater than θ contains a multiple of θ strictly in its interior. (Equivalently: take k = ⌈B/θ⌉; since B is not a multiple of θ, kθ > B, and kθ ≤ B + θ < B + A = A + B.) Hence there is an integer k with B < kθ < A + B. Then kθ > B > 0 forces k ≥ 1, and kθ < A + B = 180° − C < 180° = nθ forces k ≤ n − 1.

Set α = kθ − B. Legality of the cut (α ∈ (0, A)): α > 0 because kθ > B; α < A because kθ < A + B. Apply the cut operation. The two fresh P-angles are:
- C₂'s P-angle = B + α = kθ;
- C₁'s P-angle = 180° − (B + α) = 180° − kθ = (n − k)θ (using nθ = 180°).

Both are positive integer multiples of θ with 1 ≤ k ≤ n − 1 and 1 ≤ n − k ≤ n − 1, so each lies in (0, 180°). The remaining four child angles are positive: α = kθ − B > 0; A − α = 180° − C − kθ > 0 because kθ < 180° − C; and B, C > 0 are inherited. Thus both children are valid triangles, each carrying a tainted angle at the new vertex P. ∎

## Source
Proved in §2b of `results/imo-2026-04/approaches/lattice-descent.md` (round 1); reviewer-certified.
