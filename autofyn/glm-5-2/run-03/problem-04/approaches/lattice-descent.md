## Status
solved

## Approaches tried
- lattice-descent (round 1) — both directions proved: inclusion via the alignment move (M1) + tracked-vertex descent (M2) on the integer level m of a tainted angle mθ; exclusion via the 2×2 taint casework with explicit handling of irrational θ, p/q-rational θ (p>1), and θ>90°. Tracked-vertex invariant formalized as a single geometric vertex (the cut vertex), shown to persist in the kept child with its angle reduced by θ each step; no relocation needed. Bound ≤ n−1 moves. Status: solved.

## Current best
Complete characterization: Mulan guarantees victory in finitely many steps iff θ = 180°/n for some integer n ≥ 2. No open gap.

## Full proof

We prove the characterization in both directions. Write θ ∈ (0°, 180°) throughout. Recall an angle of a (non-degenerate) triangle lies in (0°, 180°), and the three angles sum to 180°.

### 0. The cut operation (infrastructure)

Let the current triangle be T = (A, B, C) with A + B + C = 180°, all in (0°, 180°). Mulan chooses a point P on the perimeter, different from the three vertices, and cuts from P to the opposite vertex. Suppose she cuts to the vertex carrying angle A, and let B, C be the other two angles. Let α ∈ (0°, A°) denote the part of angle A that lands on the B-side (so A − α lands on the C-side). The cut creates two triangles; a direct angle chase gives:

- **Child 1** (keeps vertex B): C₁ = (α, B, 180° − α − B).
- **Child 2** (keeps vertex C): C₂ = (A − α, C, B + α).

(Each triple sums to 180°: α + B + (180° − α − B) = 180° and (A − α) + C + (B + α) = A + B + C = 180°.) The two *fresh* angles at the new vertex P are (180° − α − B) and (B + α); their sum is exactly 180°, so **the two P-angles are supplementary**. Reparametrizing by β := B + α ∈ (B°, 180° − C°), the children are C₁ = (β − B, B, 180° − β) and C₂ = (180° − C − β, C, β), with P-angles β and 180° − β. Mulan controls α (equivalently β) freely in the open interval (0°, A°); Shan-Yu then discards one child.

This formula is the only geometric fact we use; it is verified by the sum check above.

### 1. The "reduce move" — a tainted angle forces a win (for any θ)

Define an angle x to be **tainted** (with respect to θ) if x = mθ for some positive integer m (m ≥ 1). We prove a θ-independent lemma:

> **Lemma 1 (Reduce move / descent).** Suppose the current triangle T has an angle equal to mθ at a geometric vertex V, for some integer m ≥ 1. Then Mulan forces a win. If m = 1 she has already won (the game check finds θ). If m ≥ 2, she wins in at most m − 1 further cuts, regardless of Shan-Yu's discards.

*Proof.* If m = 1 there is nothing to prove (T contains θ; the game stops). Assume m ≥ 2. Mulan cuts **to the vertex V** (the vertex carrying mθ) with parameter α = θ (placed on either side; say the B-side). By the cut operation with A = mθ:

- C₁ = (θ, B, 180° − θ − B) — **contains θ** (its angle at V is α = θ).
- C₂ = ((m − 1)θ, C, B + θ) — the angle at V is A − α = (m − 1)θ.

The cut is legal: α = θ ∈ (0°, A°) = (0°, mθ°) requires θ < mθ, which holds for m ≥ 2. Positivity of C₂'s three angles: (m − 1)θ > 0 (m ≥ 2); C > 0 (inherited from T); B + θ > 0 and, since the three angles of C₂ sum to 180° and the other two are positive, B + θ < 180°. So C₂ is a valid triangle.

Now Shan-Yu discards one child. **If he keeps C₁**, the new T contains θ, so the game check stops and Mulan wins. **If he keeps C₂**, the new T has angle (m − 1)θ at the *same geometric vertex V* (V is a vertex of C₂; its angle there is A − α = (m − 1)θ). Thus the tracked angle's level has decreased m → m − 1, at the same vertex, with no relocation.

Iterate. At step j (j = 0, 1, …, m − 2), before the cut the tracked angle at V is (m − j)θ ≥ 2θ, so the cut α = θ is legal (θ < (m − j)θ). After the cut, keeping C₂ reduces the level to (m − j − 1)θ at V; keeping C₁ ends the game (C₁ contains θ). After at most m − 1 cuts the tracked level reaches 1·θ = θ, at which point the game check stops and Mulan wins — unless she won earlier by Shan-Yu keeping a θ-bearing C₁. Either way Mulan wins in ≤ m − 1 cuts.

The **potential** is the integer level m of the tracked angle at V; it is a nonnegative integer that strictly decreases by 1 each time Shan-Yu chooses to delay (and the game ends the instant he does not). This is a natural-valued, strictly decreasing potential, so the descent terminates in at most m − 1 steps. ∎

> **Corollary (taint ⇒ loss for Shan-Yu).** For every θ, if any angle of T is a positive integer multiple of θ, Mulan wins. Consequently, in the exclusion direction Shan-Yu's invariant must forbid **all** positive multiples of θ, not only θ itself.

### 2. Inclusion: θ = 180°/n (n ≥ 2) ⇒ Mulan wins

Fix n ≥ 2 with nθ = 180°. Let T = (A, B, C) be Shan-Yu's initial triangle. If T already contains θ, Mulan has won. Assume not. We split on n.

#### 2a. The boundary n = 2 (θ = 90°) — one move

Let A be the largest angle (A ≥ 60°). Since T contains no 90° angle, A ≠ 90°.

- If A > 90° (obtuse), then B + C < 90°, so B, C < 90°.
- If A < 90° (acute), all angles are < 90°, so B, C < 90°.

In either sub-case B < 90° and C < 90°. Mulan cuts to the vertex carrying A with β = 90° (equivalently α = 90° − B). Legality: α = 90° − B ∈ (0°, A°) because α > 0 (B < 90°) and α < A ⟺ 90° < A + B = 180° − C ⟺ C < 90°, which holds. The two P-angles are β = 90° = θ and 180° − β = 90° = θ: **both children contain θ**. Whichever Shan-Yu keeps, the new T contains θ, and Mulan wins in one cut. (If A = 90° the game was already over before Mulan moved.)

#### 2b. The general case n ≥ 3 (θ ≤ 60°) — alignment move + descent

Let A be the largest angle, so A ≥ 60° ≥ θ = 180°/n, with equality A = 60° = θ only when T is equilateral (60°, 60°, 60°) — but then T already contains θ and Mulan has won. Hence, whenever Mulan needs to move, **A > θ**.

> **Lemma 2 (Alignment move, M1).** With nθ = 180° and n ≥ 3, if T contains no multiple of θ, Mulan can make a single cut such that **both** children contain a (positive integer) multiple of θ. Concretely, cutting to the largest angle's vertex with α = kθ − B for a suitable integer k ∈ {1, …, n − 1}, the two P-angles become kθ and (n − k)θ.

*Proof.* The open interval (B°, A° + B°) has length A > θ. The multiples of θ are spaced θ apart; by the **pigeonhole / extremal principle** (knowledge_base.md, *Pigeonhole / extremal*), an open interval of length strictly greater than θ contains a multiple of θ in its interior. Formally, let k = ⌈B/θ⌉ (the least integer with kθ ≥ B). If kθ = B, take k ← k + 1; then kθ = B + θ < B + A = A + B (since A > θ). Otherwise kθ > B already, and kθ < B + θ < B + A = A + B. In either sub-case kθ ∈ (B, A + B), strictly. Hence 1 ≤ k ≤ n − 1 (kθ > B > 0 forces k ≥ 1; kθ < A + B < 180° = nθ forces k ≤ n − 1).

Set α = kθ − B. Legality of the cut (α ∈ (0°, A°)): α > 0 because kθ > B; α < A because kθ < A + B. Now apply the cut operation. The two P-angles are:
- C₂'s P-angle = B + α = kθ;
- C₁'s P-angle = 180° − (B + α) = 180° − kθ = (n − k)θ (using nθ = 180°).

Both are positive integer multiples of θ, and both lie in (0°, 180°): 1 ≤ k ≤ n − 1 gives kθ ∈ (0°, nθ) = (0°, 180°) and (n − k)θ ∈ (0°, nθ) = (0°, 180°). The remaining four angles of the two children (the cut-vertex remainders and the preserved angles B, C) are all positive: α = kθ − B > 0; A − α = A + B − kθ = 180° − C − kθ > 0 because kθ < A + B = 180° − C; and B, C > 0 are inherited. Thus both children are valid triangles, each carrying a tainted angle at the new vertex P. ∎

After the alignment move, Shan-Yu keeps one child; the kept child carries a tainted angle mθ at vertex P, where m ∈ {k, n − k} ⊆ {1, …, n − 1}.

- If m = 1, the kept child already contains θ; the game check stops and Mulan wins (total: 1 cut).
- If m ≥ 2, apply Lemma 1 (the reduce move) to the tainted angle mθ at vertex P. Mulan wins in at most m − 1 ≤ n − 2 further cuts.

**Total bound.** At most 1 + (n − 2) = **n − 1 cuts**. This is finite and explicit. (For n = 2, §2a gives 1 = n − 1 cut, matching the bound.) Hence for every θ = 180°/n with n ≥ 2 integer, Mulan guarantees victory in finitely many steps. ∎ (inclusion)

### 3. Exclusion: θ ≠ 180°/n (any n ≥ 2) ⇒ Shan-Yu wins

Assume θ is not of the form 180°/n for any integer n ≥ 2. We exhibit a Shan-Yu strategy that keeps the game going forever (so Mulan never wins).

> **Invariant I.** *No angle of the current triangle is a positive integer multiple of θ.*

The forbidden set is F(θ) := {kθ : k ∈ ℤ_{≥1}, kθ < 180°}. This is finite for every θ ∈ (0°, 180°): it has exactly ⌈180°/θ⌉ − 1 elements (those k with 1 ≤ k < 180°/θ), which is finite since θ > 0. (For irrational θ the set is still finite — irrationality does not make ⌊180°/θ⌋ infinite.)

**Initial triangle.** Shan-Yu must pick a triangle whose three angles avoid F(θ). The angle-simplex Δ = {(A, B, C) : A, B, C > 0, A + B + C = 180°} is a (relatively) open 2-simplex. The forbidden conditions are the three families of lines A = kθ, B = kθ, C = kθ (finitely many lines). Removing finitely many closed lines from an open simplex leaves a nonempty (indeed dense) open set, so a taint-free triangle exists. Shan-Yu picks one; invariant I holds initially. (No assumption that the triangle lies on any lattice — the start is genuinely off-lattice.)

**Preservation.** Suppose T = (A, B, C) satisfies I, so A, B, C ∉ F(θ). Mulan cuts to the vertex carrying A with some parameter α ∈ (0°, A°). The children are C₁ = (α, B, 180° − α − B) and C₂ = (A − α, C, B + α). We prove that **at least one child satisfies I**; Shan-Yu keeps that child, preserving I.

Suppose for contradiction that **both** children fail I, i.e. each contains a tainted angle. In C₁ the angle B is untainted (inherited), so a tainted angle of C₁, if it exists, is either the α-slot (α = k₁θ for some integer k₁ ≥ 1) or the P-slot (180° − α − B = k₁θ). Similarly, in C₂ the angle C is untainted, so a tainted angle of C₂ is either the α-slot (A − α = k₂θ, k₂ ≥ 1) or the P-slot (B + α = k₂θ, k₂ ≥ 1). (The integers k₁, k₂ are ≥ 1 because each tainted angle is positive and equals (positive integer)·θ with θ > 0.) Pick one tainted slot in each child; the pair falls into one of four cases, and we show each is impossible:

**Case 1 (C₁ α-slot & C₂ α-slot):** α = k₁θ and A − α = k₂θ. Adding, A = (k₁ + k₂)θ. Since k₁ + k₂ ≥ 1 and A < 180°, this puts A ∈ F(θ), contradicting A untainted. (If (k₁ + k₂)θ ≥ 180° the equation A = (k₁ + k₂)θ has no solution with A < 180°, also a contradiction.) ✗

**Case 2 (C₁ α-slot & C₂ P-slot):** α = k₁θ and B + α = k₂θ. Subtracting, B = (k₂ − k₁)θ. Since B > 0, we have k₂ − k₁ ≥ 1 (if k₂ − k₁ ≤ 0 then B ≤ 0). Thus B = (k₂ − k₁)θ ∈ F(θ), contradicting B untainted. ✗

**Case 3 (C₁ P-slot & C₂ α-slot):** 180° − α − B = k₁θ (so α = 180° − B − k₁θ) and A − α = k₂θ. Then C = 180° − A − B = 180° − (α + k₂θ) − B = 180° − (180° − B − k₁θ + k₂θ) − B = (k₁ − k₂)θ. Since C > 0, k₁ − k₂ ≥ 1, so C ∈ F(θ), contradicting C untainted. ✗

**Case 4 (C₁ P-slot & C₂ P-slot):** 180° − α − B = k₁θ and B + α = k₂θ. Adding, 180° = (k₁ + k₂)θ, i.e. θ = 180°/(k₁ + k₂) with k₁ + k₂ ≥ 2 a positive integer — contradicting the hypothesis that θ is not of the form 180°/n (n ≥ 2). ✗

All four cases are impossible, so it cannot be that both children fail I. Hence at least one child satisfies I; Shan-Yu keeps it. The invariant I is preserved. We spell out the three sub-families of the hypothesis "θ ≠ 180°/n" to close the last case explicitly:

- **θ irrational.** Case 4 demands θ = 180°/(k₁ + k₂) ∈ ℚ, impossible for irrational θ. Cases 1–3 are the pure arithmetic above (no rationality of θ is used; they contradict taint-freedom directly, since a positive-integer multiple of θ that is < 180° lies in F(θ) regardless of whether θ is rational). So all four fail. The initial triangle exists because F(θ) is finite (⌊180°/θ⌋ elements) even for irrational θ.

- **θ = 180°·(p/q) in lowest terms with p > 1.** Then 180°/θ = q/p ∉ ℤ (since gcd(p, q) = 1 and p > 1, so p ∤ q), i.e. θ ≠ 180°/n for any integer n. Case 4 demands q/p = k₁ + k₂ ∈ ℤ, i.e. p | q, contradicting gcd(p, q) = 1 with p > 1. ✗. (Note θ < 180° forces p < q, so this family is nonempty, e.g. θ = 72° = 180°·(2/5).)

- **θ > 90°.** Then 2θ > 180°, so the only positive multiple of θ that can be an angle of a triangle is θ itself (F(θ) = {θ}). No θ = 180°/n exceeds 90° for n ≥ 2 (since 180°/n ≤ 90°), so θ > 90° lies outside the winning set. Case 4 forces θ = 180°/(k₁ + k₂) ≤ 90°, contradicting θ > 90°. Cases 1–3 force some angle to equal (positive integer)·θ; if that integer is 1 the angle is θ ∈ F(θ) (contradiction), and if it is ≥ 2 the value exceeds 180° (impossible for an angle). ✗.

In every sub-family, all four cases fail, so I is preserved.

**Conclusion of exclusion.** While I holds, no angle of T equals 1·θ = θ, so the game never stops. Since Shan-Yu can initialize I (taint-free triangle exists) and preserve I after every Mulan move (at least one taint-free child always exists), Mulan never wins. Hence θ ≠ 180°/n is a loss for Mulan. ∎ (exclusion)

### 4. Characterization

Combining §2 (inclusion) and §3 (exclusion), and noting that θ = 180°/n with n ≥ 2 is exactly the set of θ ∈ (0°, 180°) for which 180°/θ is an integer ≥ 2:

> **Mulan guarantees victory in finitely many steps, regardless of Shan-Yu's play, if and only if θ = 180°/n for some integer n ≥ 2** (equivalently, 180°/θ ∈ {2, 3, 4, …}).

The inclusion is constructive: Mulan wins in at most n − 1 cuts (one alignment cut creating a tainted angle in both children, then at most n − 2 reduce cuts descending the tracked level m → m − 1 → … → 1 at the same geometric vertex); for n = 2 a single cut suffices. The exclusion is the closed invariant "no angle is a positive integer multiple of θ," preserved by the 2×2 casework (Cases 1–3 contradict the parent's taint-freedom by pure linear arithmetic; Case 4 forces θ = 180°/n), with the initial taint-free triangle existing because the forbidden set F(θ) is finite for every θ > 0 (irrational or rational). ∎

## Promotable lemmas
- **Lemma 1 (Reduce move / taint descent).** *For every θ ∈ (0°, 180°), if the current triangle has an angle equal to mθ (m a positive integer) at a geometric vertex V, then Mulan forces a win in at most m − 1 further cuts: cut to V with α = θ; the θ-bearing child ends the game if kept, and the (m − 1)θ-bearing child (kept to delay) reduces the level m → m − 1 at the same vertex. The natural-valued potential m strictly decreases.* Proved in §1 of `results/imo-2026-04/approaches/lattice-descent.md`. Reusable by any approach needing "tainted angle ⇒ forced win."
- **Lemma 2 (Alignment move).** *If nθ = 180° (n ≥ 3) and T contains no multiple of θ, Mulan cuts to the largest angle's vertex (A > θ) with α = kθ − B for a pigeonhole-existing k ∈ {1, …, n − 1}; both children's P-angles become multiples kθ and (n − k)θ.* Proved in §2b of the same file.
- **Lemma 3 (Taint-free invariant closure).** *For θ ≠ 180°/n (n ≥ 2 integer), if a parent triangle has no angle in F(θ) = {kθ : k ≥ 1, kθ < 180°}, then not both children of any Mulan cut can be tainted: the four α-slot/P-slot pairings yield (Cases 1–3) A, B, or C ∈ F(θ) (contradicting taint-freedom), or (Case 4) θ = 180°/(k₁ + k₂) (contradicting the hypothesis). Hence Shan-Yu preserves "no angle is a positive multiple of θ" forever.* Proved in §3 of the same file; handles irrational θ, p/q-rational θ with p > 1, and θ > 90° explicitly.
