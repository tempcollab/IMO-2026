# Lemma: Taint-free invariant closure

*For θ ∈ (0°, 180°) with θ ≠ 180°/n for every integer n ≥ 2, if a parent triangle T has no angle in the forbidden set F(θ) = {kθ : k ≥ 1, kθ < 180°}, then not both children of any Mulan cut can be tainted. Hence Shan-Yu preserves "no angle is a positive integer multiple of θ" forever, and Mulan never wins.*

## Proof

F(θ) is finite for every θ > 0 (it has ⌈180°/θ⌉ − 1 elements; for irrational θ, still finite). A taint-free initial triangle exists: the open angle-simplex {(A,B,C) : A,B,C > 0, A+B+C = 180°} minus finitely many closed line-segments {A = kθ}, {B = kθ}, {C = kθ} is nonempty (indeed dense).

For preservation, let T = (A,B,C) be taint-free, so A, B, C ∉ F. Mulan cuts to vertex A with α ∈ (0, A). The children are C₁ = (α, B, 180° − α − B) and C₂ = (A − α, C, B + α). Suppose for contradiction both children are tainted. Since B and C are untainted (inherited), a tainted angle of C₁ is either the α-slot α or the P-slot 180° − α − B; a tainted angle of C₂ is either the α-slot A − α or the P-slot B + α. Pick one witness slot per child (write k₁, k₂ ≥ 1 for the multipliers); the pair falls into one of four exhaustive cases:

1. **(α-slot, α-slot):** α = k₁θ and A − α = k₂θ. Adding: A = (k₁ + k₂)θ. Since k₁ + k₂ ≥ 1 and A < 180°, this puts A ∈ F (if (k₁ + k₂)θ ≥ 180° the equation has no solution with A < 180°, also a contradiction). Contradicts A untainted.
2. **(α-slot C₁, P-slot C₂):** α = k₁θ and B + α = k₂θ. Subtracting: B = (k₂ − k₁)θ. Since B > 0, k₂ − k₁ ≥ 1, so B ∈ F. Contradicts B untainted.
3. **(P-slot C₁, α-slot C₂):** 180° − α − B = k₁θ and A − α = k₂θ. Eliminating α: C = 180° − A − B = (k₁ − k₂)θ. Since C > 0, k₁ − k₂ ≥ 1, so C ∈ F. Contradicts C untainted.
4. **(P-slot, P-slot):** 180° − α − B = k₁θ and B + α = k₂θ. Adding: 180° = (k₁ + k₂)θ, i.e. θ = 180°/(k₁ + k₂) with k₁ + k₂ ≥ 2 an integer. Contradicts the hypothesis θ ≠ 180°/n.

All four cases contradict, so at least one child is taint-free; Shan-Yu keeps it. The invariant is preserved.

**Sub-families of the hypothesis:**
- *θ irrational:* Case 4 demands θ ∈ ℚ, impossible. Cases 1–3 use no rationality. Initial triangle exists (F finite).
- *θ = 180°·(p/q) in lowest terms with p > 1:* Then 180°/θ = q/p ∉ ℤ. Case 4 demands p | q, contradicting gcd(p, q) = 1 with p > 1.
- *θ > 90°:* Then 2θ > 180°, so F = {θ}; no θ = 180°/n exceeds 90°. Case 4 forces θ ≤ 90°, contradiction. Cases 1–3 force some angle = (positive integer)·θ; if the integer is 1, the angle is θ ∈ F; if ≥ 2, the value exceeds 180° (impossible for an angle).

## Source
Proved in §3 of `results/imo-2026-04/approaches/lattice-descent.md` (round 1); reviewer-certified. Also reproduced in `residue-monovariant.md` (§4) and `equilateral-witness.md` (Part B).
