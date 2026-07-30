# residue-monovariant — IMO 2026 P4 (Mulan's triangle game)

## Status
solved

## Approaches tried
- **round 1 — residue-monovariant Φ = max(angle mod θ) crux (the original distinct contribution):** FAILED. Conjectured that Mulan could always cut so that BOTH children have strictly smaller Φ, giving a direct real-valued-then-naturalized potential bypassing the alignment-move detour. Computationally refuted (~15–30% of random non-tainted triangles have no such cut, for every tested θ = 180°/n with n ∈ {3,4,5,6,7,8,9,10,12,15,20,30}). The obstruction is structural, not a grid artifact: the two fresh P-residues are r(β) and r(180−β) = (θ − r(β)) mod θ (since 180 ≡ 0 mod θ); for both to be < Φ with r(β) ≠ 0 requires r(β) ∈ (θ−Φ, Φ), which is **empty whenever Φ ≤ θ/2**. In that regime the only β that decreases both P-residues is r(β) = 0 — i.e. the alignment move itself. So the Φ-monovariant does not bypass the alignment move; it collapses into it. Recorded honestly as a dead end; do NOT retry a "max-residue strictly decreases for both children" lemma.
- **round 1 — fallback (alignment move, approved by the gate):** Pivoted to the M1 alignment move + M2 reduce move + 2×2 taint casework (the lattice-descent inclusion, the approved fallback). This gives a complete, rigorous, end-to-end proof of both directions. The residue-sum identity is retained as the *conceptual* explanation of why θ | 180° is the threshold (the supplementary pair lands on complementary multiples iff 180 ≡ 0 mod θ), but it is no longer load-bearing for the inclusion — the alignment move carries that.

## Current best
Complete proof of the characterization (both directions) via the alignment move (M1), the reduce move (M2), and the 2×2 taint casework. The original residue-monovariant crux is refuted (negative result recorded); the proof stands on the fallback. No open gaps.

## Full proof

**Answer.** Mulan can guarantee victory in finitely many steps, regardless of Shan-Yu's play, **if and only if** θ = 180°/n for some integer n ≥ 2 (equivalently, 180°/θ is an integer ≥ 2).

Throughout, angles are measured in degrees; a triangle is identified with its unordered angle triple (A, B, C) with A + B + C = 180° and all in (0°, 180°). The game halts (Mulan wins) the instant some angle equals θ.

### 1. The cut operation and the supplementary pair

Let Mulan cut to a chosen vertex of angle V, letting B, C denote the other two angles, with parameter α = ∠(cut, side toward B) ∈ (0, V). The two children are (a direct angle chase, verified in `knowledge_base.md` → *Trig identities & interval intersection / supplementary angles*):

- **C₁** = (α, B, 180° − α − B)  — preserves B;
- **C₂** = (V − α, C, B + α)      — preserves C.

Both sum to 180°; all six angles are positive exactly for α ∈ (0, V). Reparametrize by β = B + α ∈ (B, 180° − C); then C₁ = (β − B, B, 180° − β) and C₂ = (180° − C − β, C, β). The two *fresh* angles at the cut point P are β and 180° − β: they are **supplementary** (sum to 180°). This is the load-bearing structural fact. Each child inherits exactly one of the two non-destroyed parent angles (B in C₁, C in C₂); the destroyed angle V survives in neither.

We will use two moves. The first works for every θ; the second is the gate that separates θ | 180° from θ ∤ 180°.

### 2. The reduce move (M2) — works for every θ; "any tainted angle is a forced win"

Call an angle **tainted** (with respect to θ) if it equals kθ for some integer k ≥ 1. Note θ itself is 1·θ, so a tainted angle of level 1 is exactly a win.

**Lemma (M2).** Suppose the current triangle has an angle mθ (m ≥ 2) at a vertex V (the *tracked vertex*). Then Mulan forces a win in at most m − 1 further moves, regardless of Shan-Yu.

*Proof.* Mulan cuts to V with α = θ. The children are
- C₁ = (θ, B, 180° − θ − B),  which contains θ ⇒ Mulan wins immediately if Shan-Yu keeps it;
- C₂ = ((m−1)θ, C, B + θ),   carrying the reduced multiple (m−1)θ at the *same* cut vertex V.

Shan-Yu must discard C₁ (otherwise Mulan has won); he keeps C₂. The tracked angle's level is now m − 1, at the same geometric vertex. Repeat. At level 1 the angle equals θ and Mulan wins.

*Positivity throughout.* For m ≥ 2: (m−1)θ > 0; B > 0, C > 0 by hypothesis; 180° − θ − B > 0 because B < 180° − mθ ≤ 180° − 2θ (since B + C = 180° − mθ and C > 0), so 180° − θ − B > θ > 0; B + θ < 180° because B < 180° − mθ ≤ 180° − 2θ, so B + θ < 180° − θ < 180°. All child angles stay positive at every step.

*Tracked-vertex invariant.* After a reduce cut at V with α = θ, the kept child C₂ has angle V − α = mθ − θ = (m−1)θ at the *same* point V. So Mulan simply re-cuts the same vertex each round; the "tracked vertex" needs no relocation — it is the geometric vertex V, fixed throughout the descent. Commit to descending this one vertex. Even if other multiples of θ appear elsewhere in the kept triangle, that only helps Mulan (any multiple descends by M2); the committed descent of V terminates in m − 1 steps. The potential is the natural number m (level of the tracked angle); it strictly decreases to 1; bound m − 1. ∎  (knowledge_base.md → *Invariants & monovariants*; *Induction / infinite descent*.)

**Corollary.** If the current triangle contains *any* tainted angle (any kθ, k ≥ 1), Mulan forces a win in finitely many steps (≤ k − 1 ≤ ⌊180/θ⌋ − 1 further moves). Hence, for the *exclusion* direction, Shan-Yu's safe invariant must forbid **every** multiple of θ, not only θ.

### 3. Inclusion (θ = 180°/n, n ≥ 2): Mulan wins

Assume θ = 180°/n with integer n ≥ 2. We give an explicit strategy with a uniform finite bound.

#### 3a. The alignment move (M1) for n ≥ 3

If the triangle already contains a multiple of θ, apply M2 and win. Otherwise no angle is a multiple of θ. Cut to the **largest** angle A.

*Existence of the alignment parameter.* Since A is the largest angle, A ≥ 60° (= 180°/3). For n ≥ 3, θ = 180°/n ≤ 60°, with equality only when n = 3 and A = 60° — but A = 60° = θ would be a multiple of θ, the excluded case. Hence **A > θ**. The open interval (B, A + B) has length A > θ; multiples of θ are spaced θ apart on the line, so by the pigeonhole/extremal principle (knowledge_base.md → *Pigeonhole / extremal*) the interval contains a multiple kθ with k ≥ 1. Also kθ < A + B = 180° − C < 180° = nθ, so k ≤ n − 1; and kθ > B > 0, so k ≥ 1. Thus 1 ≤ k ≤ n − 1.

Set α = kθ − B. Then 0 < α (since kθ > B) and α < A (since kθ < A + B). Compute the two fresh P-angles:
- C₂'s P-angle = B + α = **kθ**;
- C₁'s P-angle = 180° − B − α = 180° − kθ = **(n − k)θ**  (using 180° = nθ).

Both are positive multiples of θ (1 ≤ k ≤ n − 1 ⟹ both k, n − k ≥ 1). Whichever child Shan-Yu keeps carries a tainted angle (kθ in C₂, (n−k)θ in C₁); apply M2 to descend it to θ.

*Positivity of all six child angles.* α ∈ (0, A) ✓; B, C > 0 ✓; C₁'s third angle (n − k)θ > 0 ✓; C₂'s third angle kθ > 0 ✓; C₂'s α-slot remainder A − α = A + B − kθ = 180° − C − kθ > 0 because kθ < 180° − C (the interval upper bound) ✓.

*Bound.* One alignment move + at most (n − 2) reduce moves = **≤ n − 1** moves.

#### 3b. The boundary n = 2 (θ = 90°): one-move supplementary fork

If T already has a 90° angle, Mulan has won. Otherwise cut to the largest angle A. We claim both other angles B, C are < 90°. Indeed B + C = 180° − A ≤ 180° − 60° = 120°, and if either of B, C were ≥ 90°, say B ≥ 90°, then A ≥ B ≥ 90° and B ≥ 90°, so A + B ≥ 180°, forcing C ≤ 0°, impossible. (Equivalently: the largest angle is ≥ 60°; if A ≥ 90° then B + C ≤ 90° so both < 90°; if A < 90° the triangle is acute and both B, C < 90°.) Hence B < 90° and C < 90°.

Set α = 90° − B (equivalently β = 90°). Then 0 < α < A: α > 0 since B < 90°; α < A since α < A ⟺ 90° − B < A ⟺ 90° < A + B = 180° − C ⟺ C < 90° ✓. Both fresh P-angles equal β = 90° and 180° − β = 90°: both children contain θ = 90°. Mulan wins in **one** move.

This is the unique self-supplementary angle (θ = 180° − θ ⟺ θ = 90°), which is why n = 2 is the one-move boundary.

#### 3c. Inclusion summary

For every θ = 180°/n (n ≥ 2 integer), Mulan has an explicit strategy (M1 once, then M2 until level 1; for n = 2, M1 alone) forcing θ to appear in at most n − 1 moves, independent of Shan-Yu's discards. Finiteness is certified by the strictly decreasing natural-valued potential *level of the tracked angle* (M2) plus the one-shot alignment (M1). ∎

### 4. Exclusion (θ ≠ 180°/n): Shan-Yu wins

Now assume 180°/θ is **not** an integer ≥ 2 (this covers every θ ∈ (0°, 180°) \ {180°/n : n ≥ 2}, including all irrational θ, all rational θ = 180°·(p/q) with p > 1, and all θ > 90°).

#### 4a. Shan-Yu's invariant

Shan-Yu maintains:
> **(I)** No angle of the current triangle is an integer multiple of θ (no angle lies in the finite forbidden set F = {kθ : 1 ≤ k ≤ ⌊180°/θ⌋}).

Since θ = 1·θ ∈ F, invariant (I) in particular forbids θ from ever appearing, so Mulan never wins as long as (I) holds.

#### 4b. Initial triangle exists

The forbidden set F is finite (it has ⌊180°/θ⌋ elements; for θ > 90°, |F| = 1; for irrational θ, still finite). Pick ε > 0 small enough that ε ∉ F and 180° − 2ε ∉ F (only finitely many ε are excluded). The triangle (ε, ε, 180° − 2ε) is non-degenerate (all angles positive) and satisfies (I). So Shan-Yu has a legal starting triangle. (For θ > 90°, F = {θ}; any acute-enough needle avoids it.)

#### 4c. The invariant is preserved — the 2×2 taint casework

We show: from any (I)-triangle, for **every** Mulan cut, **at least one child is (I)**; Shan-Yu keeps that child.

Suppose for contradiction that both children are tainted. Relabel so Mulan cuts to vertex A; the other angles B, C are (by (I)) untainted. The children are
- C₁ = (α, B, 180° − B − α),  with preserved angle B (untainted);
- C₂ = (A − α, C, B + α),    with preserved angle C (untainted).

In each child, the tainted angle cannot be the preserved one (B, C are untainted), so it must lie in that child's **α-slot** (the angle α in C₁, the angle A − α in C₂) or its **P-slot** (the fresh P-angle 180° − B − α in C₁, the fresh P-angle B + α in C₂). Choose one witness slot per child; this gives four disjoint, exhaustive cases (knowledge_base.md → *Casework / exhaustion*). Write k₁, k₂ ≥ 1 for the witness multipliers.

1. **α-slot & α-slot:** α = k₁θ and A − α = k₂θ. Adding: **A = (k₁ + k₂)θ**, a multiple of θ — contradicting A untainted. ✗
2. **α-slot (C₁) & P-slot (C₂):** α = k₁θ and B + α = k₂θ. Subtracting: **B = (k₂ − k₁)θ**, a (signed) multiple of θ — contradicting B untainted. ✗
3. **P-slot (C₁) & α-slot (C₂):** 180° − B − α = k₁θ and A − α = k₂θ. Subtracting the second from the first: (180° − B − α) − (A − α) = 180° − A − B = **C = (k₁ − k₂)θ**, a multiple of θ — contradicting C untainted. ✗
4. **P-slot & P-slot:** 180° − B − α = k₁θ and B + α = k₂θ. Adding: **180° = (k₁ + k₂)θ**, i.e. θ = 180°/(k₁ + k₂). Since k₁, k₂ ≥ 1, the denominator k₁ + k₂ ≥ 2, so this exhibits θ = 180°/n for an integer n ≥ 2 — contradicting the exclusion hypothesis θ ≠ 180°/n. ✗  (For irrational θ, 180°/θ ∉ ℚ so no integer k₁ + k₂ satisfies the equation at all; for rational non-divisor θ = 180°·(p/q) with p > 1, 180°/θ = q/p ∉ ℤ, again no solution.)

All four cases contradict. Hence at least one child is taint-free — i.e. satisfies (I). Shan-Yu keeps it. Invariant (I) is preserved. ∎  (knowledge_base.md → *Invariants & monovariants*; *Casework / exhaustion*.)

#### 4d. θ > 90°

No θ = 180°/n (n ≥ 2) exceeds 90°. The casework's case 4 forces θ = 180°/(k₁ + k₂) ≤ 90° (as k₁ + k₂ ≥ 2), a contradiction, so the exclusion applies verbatim. The whole interval (90°, 180°) is losing for Mulan. ∎

### 5. The residue-sum obstruction (conceptual, recorded; not load-bearing)

Although the Φ-monovariant crux failed (§Approaches tried), the residue viewpoint cleanly *explains* why θ | 180° is the threshold. Define r(x) = x mod θ ∈ [0, θ). Then r(A) + r(B) + r(C) ≡ A + B + C = 180° (mod θ). When θ | 180°, the residue-sum is ≡ 0 mod θ (so the all-zero configuration, i.e. the θ-lattice, is residue-theoretically reachable, and the supplementary pair (β, 180° − β) has complementary residues r(β), θ − r(β) summing to θ); when θ ∤ 180°, the residue-sum ≡ δ := 180° mod θ ≠ 0, an obstruction to ever reaching the all-zero (lattice) state. This is a *necessary* condition for the inclusion and the *motivation* for the alignment gate, but it is not by itself sufficient for the exclusion (a single angle can be θ while the other two residues sum to δ), which is why the airtight exclusion rests on the 2×2 taint casework of §4c, not on the residue-sum alone.

### 6. Verification of the answer

- θ = 180°/n, n ≥ 2: inclusion §3 (M1 + M2, bound ≤ n − 1; n = 2 in one move).
- θ ≠ 180°/n (including irrational θ, θ = 180°·p/q with p > 1, all θ > 90°): exclusion §4 (taint-free invariant (I), closed by the 2×2 casework; θ = 1·θ forbidden).

Both directions are covered, the casework is exhaustive and the cases disjoint, every invoked tool is named (cut/angle-chase, supplementary angles, pigeonhole/extremal for the alignment interval, induction/infinite-descent for M2, invariants & monovariants and casework/exhaustion for the exclusion), and finiteness is certified by the strictly decreasing natural-valued potential (level m of the tracked tainted angle). ∎
