## Status
solved

## Approaches tried
- lattice-descent (round 1) — APPROVED. Complete proof both directions: inclusion via M1 alignment (pigeonhole) + M2 taint descent (natural-valued potential, same-vertex invariant, bound ≤ n−1) + n=2 one-move boundary; exclusion via taint-free invariant + 2×2 casework (all four cases contradictory), with explicit irrational-θ, p/q-rational (p>1), and θ>90° arms. Anchor proof.
- residue-monovariant (round 1) — APPROVED. Distinct Φ-monovariant crux honestly refuted by builder (interval (θ−Φ,Φ) empty when Φ≤θ/2); proof stands on the M1+M2+casework fallback (complete, correct). Redundant with lattice-descent.
- equilateral-witness (round 1) — APPROVED. Inclusion via M1+M2. Exclusion: Part A (obtuse safe set S = {all angles ≤90°}, genuinely geometric, proven closed under the supplementary reflection for θ>90°) + Part B (shared taint casework for θ∈(0,90°]). Refuted E-alone crux honestly fixed by enlarging to S.

## Current best
Complete characterization: Mulan guarantees victory in finitely many steps, regardless of Shan-Yu's play, if and only if θ = 180°/n for some integer n ≥ 2 (equivalently, 180°/θ is an integer ≥ 2). Inclusion is constructive with explicit bound ≤ n−1 cuts (≤1 for n=2); exclusion is the closed "no angle is a positive integer multiple of θ" invariant (initiable for every non-divisor θ since the forbidden set F is finite) plus, for θ>90°, the independent geometric safe set S.

## Full proof

Write θ ∈ (0°, 180°) throughout. A triangle is identified with its angle triple (A,B,C), A+B+C=180°, all in (0°,180°).

### 0. The cut operation

Mulan chooses P on the perimeter (not a vertex) and cuts from P to the opposite vertex. Relabel so she cuts to the vertex carrying angle A; let α = ∠(BAP) ∈ (0,A) be the part of A on the B-side. A direct angle chase gives the two children:
- C₁ = (α, B, 180°−α−B) — preserves B;
- C₂ = (A−α, C, B+α) — preserves C.

Both sum to 180°. The two fresh angles at the new vertex P are (180°−α−B) and (B+α); their sum is exactly 180°, so **the two P-angles are supplementary**. Reparametrizing by β = B+α, the P-angles are 180°−β and β. All six child angles are positive exactly for α ∈ (0,A).

### 1. Inclusion: θ = 180°/n (n ≥ 2) ⇒ Mulan wins

**Lemma 1 (Reduce move / descent).** *If the current triangle has an angle mθ (m ≥ 2) at a vertex V, then Mulan forces a win in at most m−1 further cuts, regardless of Shan-Yu's discards.*

*Proof.* Mulan cuts to V with α = θ (legal: θ < mθ for m ≥ 2). The children are C₁ = (θ, B, 180°−θ−B) — which contains θ — and C₂ = ((m−1)θ, C, B+θ), carrying (m−1)θ at the *same geometric vertex* V (V is a vertex of both children). All angles of C₂ are positive: (m−1)θ > 0; C > 0; B+θ < 180° since B < 180°−mθ ≤ 180°−2θ. If Shan-Yu keeps C₁ the game stops (Mulan wins). If he keeps C₂ to delay, the tracked level decreases m → m−1 at V. Iterate: at level m−j (≥2) the cut α=θ is legal, and keeping C₂ reduces the level by 1; at level 2, C₂'s angle is (2−1)θ = θ, so both children contain θ and Mulan wins regardless. The level is a natural-valued potential strictly decreasing to 1; bound m−1. ∎ (Induction / infinite descent; Invariants & monovariants.)

**Lemma 2 (Alignment move).** *If nθ = 180° (n ≥ 3) and T contains no multiple of θ, Mulan cuts to the largest angle's vertex with α = kθ−B for a pigeonhole-existing k ∈ {1,…,n−1}; both children's P-angles become multiples kθ and (n−k)θ.*

*Proof.* Let A be the largest angle, so A ≥ 60° ≥ θ = 180°/n, with equality A = 60° = θ only when T is equilateral and n = 3 — but then T contains θ and Mulan has won. Hence, whenever Mulan needs to move, A > θ. The open interval (B, A+B) has length A > θ; multiples of θ are spaced θ apart, so by the pigeonhole/extremal principle there is an integer k with B < kθ < A+B. Then kθ > B > 0 forces k ≥ 1, and kθ < A+B = 180°−C < 180° = nθ forces k ≤ n−1. Set α = kθ−B ∈ (0,A). The two P-angles are B+α = kθ and 180°−kθ = (n−k)θ (using nθ = 180°). Both are positive multiples of θ with 1 ≤ k, n−k ≤ n−1, lying in (0,180°). All six child angles are positive (α>0, A−α = 180°−C−kθ > 0 since kθ < 180°−C, and B, C inherited). ∎ (Pigeonhole / extremal.)

**Putting inclusion together.** If T already contains θ, Mulan wins (0 moves). Else if some angle is mθ (m ≥ 2), apply Lemma 1 (win in ≤ m−1 ≤ n−2 cuts). Else (no angle a multiple of θ) apply Lemma 2 once: whichever child Shan-Yu keeps carries mθ for some m ∈ {k, n−k} ⊆ {1,…,n−1}; if m = 1 it already contains θ (1 cut), and if m ≥ 2 apply Lemma 1 (≤ m−1 ≤ n−2 further cuts). Total ≤ 1 + (n−2) = **n−1 cuts**.

**Boundary n = 2 (θ = 90°).** If T has a 90° angle, Mulan has won. Otherwise cut to the largest angle A. If A > 90° then B+C < 90°, so B,C < 90°; if A < 90° the triangle is acute, so B,C < 90°. Hence B < 90° and C < 90°. Set β = 90° (α = 90°−B): legality α > 0 (B<90°) and α < A ⟺ 90° < A+B = 180°−C ⟺ C < 90° ✓. Both P-angles equal 90° = θ; Mulan wins in one cut regardless of the discard.

So for every θ = 180°/n (n ≥ 2 integer), Mulan forces a win in at most n−1 cuts. ∎ (inclusion)

### 2. Exclusion: θ ≠ 180°/n (any n ≥ 2) ⇒ Shan-Yu wins

Assume θ is not of the form 180°/n for any integer n ≥ 2. Shan-Yu maintains:

> **(I)** No angle of the current triangle is a positive integer multiple of θ.

The forbidden set is F(θ) = {kθ : k ∈ ℤ≥1, kθ < 180°}, which is **finite** for every θ ∈ (0°,180°): it has ⌈180°/θ⌉−1 elements (finite since θ > 0; for irrational θ, still finite). Since θ = 1·θ ∈ F, invariant (I) in particular forbids θ, so Mulan never wins while (I) holds.

**Initial triangle.** The angle-simplex Δ = {(A,B,C) : A,B,C > 0, A+B+C = 180°} is an open 2-simplex. The forbidden conditions A = kθ, B = kθ, C = kθ are finitely many closed line-segments. Removing finitely many closed segments from an open simplex leaves a nonempty (indeed dense) open set, so a taint-free triangle exists; Shan-Yu picks one. (I) holds initially.

**Preservation.** Suppose T = (A,B,C) satisfies (I), so A,B,C ∉ F. Mulan cuts to vertex A with α ∈ (0,A). The children are C₁ = (α, B, 180°−α−B) and C₂ = (A−α, C, B+α). We prove at least one child satisfies (I). Suppose for contradiction that **both** children fail (I). Since B and C are untainted (inherited), a tainted angle of C₁ is either the α-slot α or the P-slot 180°−α−B; a tainted angle of C₂ is either the α-slot A−α or the P-slot B+α. Pick one witness slot per child; the pair falls into one of four cases (write k₁, k₂ ≥ 1 for the witness multipliers):

1. **(α-slot, α-slot):** α = k₁θ and A−α = k₂θ. Adding, A = (k₁+k₂)θ. Since k₁+k₂ ≥ 1 and A < 180°, this puts A ∈ F (if (k₁+k₂)θ ≥ 180° the equation has no solution with A < 180°, also a contradiction). Contradicts A untainted. ✗
2. **(α-slot C₁, P-slot C₂):** α = k₁θ and B+α = k₂θ. Subtracting, B = (k₂−k₁)θ. Since B > 0, k₂−k₁ ≥ 1, so B ∈ F. Contradicts B untainted. ✗
3. **(P-slot C₁, α-slot C₂):** 180°−α−B = k₁θ and A−α = k₂θ. Eliminating α: C = 180°−A−B = (k₁−k₂)θ. Since C > 0, k₁−k₂ ≥ 1, so C ∈ F. Contradicts C untainted. ✗
4. **(P-slot, P-slot):** 180°−α−B = k₁θ and B+α = k₂θ. Adding, 180° = (k₁+k₂)θ, i.e. θ = 180°/(k₁+k₂) with k₁+k₂ ≥ 2 an integer — contradicting the hypothesis θ ≠ 180°/n. ✗

All four cases are impossible, so at least one child satisfies (I); Shan-Yu keeps it. (I) is preserved. The three sub-families of the hypothesis:
- **θ irrational.** Case 4 demands θ = 180°/(k₁+k₂) ∈ ℚ, impossible. Cases 1–3 use no rationality of θ and contradict taint-freedom directly (a positive-integer multiple of θ that is < 180° lies in F regardless of rationality). The initial triangle exists because F is finite even for irrational θ.
- **θ = 180°·(p/q) in lowest terms with p > 1.** Then 180°/θ = q/p ∉ ℤ (since gcd(p,q)=1 and p > 1), i.e. θ ≠ 180°/n. Case 4 demands p | q, contradicting gcd(p,q)=1 with p > 1. ✗
- **θ > 90°.** Then 2θ > 180°, so F = {θ}; no θ = 180°/n exceeds 90° (since 180°/n ≤ 90° for n ≥ 2). Case 4 forces θ = 180°/(k₁+k₂) ≤ 90°, contradicting θ > 90°. Cases 1–3 force some angle = (positive integer)·θ; if the integer is 1 the angle is θ ∈ F (contradiction), and if ≥ 2 the value exceeds 180° (impossible for an angle). ✗

**Independent geometric exclusion for θ ∈ (90°, 180°).** Define S = {triangles with every angle ≤ 90°}. The equilateral E = (60°,60°,60°) lies in S, and no member of S has an angle equal to θ (all ≤ 90° < θ). S is closed under the game: for T = (A,B,C) ∈ S, Mulan cuts to vertex A; the non-P angles of each child are < A ≤ 90° (and B, C ≤ 90°), so the only angle that can exceed 90° in either child is its P-angle. The two P-angles P₁ = 180°−α−B and P₂ = B+α are supplementary (sum 180°), so at most one exceeds 90°. Hence at least one child lies in S; Shan-Yu keeps it. By induction the triangle stays in S forever; Mulan never wins. (This is a genuinely geometric safe set — a proper subset of the taint-free set, closed under the supplementary reflection — giving an independent route for the half-range (90°,180°).)

**Conclusion of exclusion.** While (I) holds (or, for θ > 90°, while T ∈ S), no angle equals θ, so the game never stops. Shan-Yu can initialize and preserve the safe state after every Mulan move. Mulan never wins. Hence θ ≠ 180°/n is a loss for Mulan. ∎ (exclusion)

### 3. Characterization

Combining §1 and §2: **Mulan guarantees victory in finitely many steps, regardless of Shan-Yu's play, if and only if θ = 180°/n for some integer n ≥ 2** (equivalently, 180°/θ ∈ {2, 3, 4, …}). The inclusion is constructive (≤ n−1 cuts via one alignment cut creating a tainted angle in both children, then at most n−2 reduce cuts descending the tracked level at the same geometric vertex; one cut for n = 2). The exclusion is the closed invariant "no angle is a positive integer multiple of θ," preserved by the 2×2 taint casework (Cases 1–3 contradict the parent's taint-freedom by linear arithmetic; Case 4 forces θ = 180°/n), with the initial taint-free triangle existing because F(θ) is finite for every θ > 0. ∎
