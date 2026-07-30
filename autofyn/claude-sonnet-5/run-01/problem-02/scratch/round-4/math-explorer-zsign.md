## imo-2026-02 — sub-problem: prove Z ≠ 0 (a.k.a. D1 ≠ 0)

### Headline finding: Z > 0 outright, via a short direct positivity argument — no discriminant needed

Recall (from `coordinate-groebner-elimination.md` / `synthetic-angle-chase-aklastar.md`, both verified
identical up to the factor 2, `Z = D1/2`):
```
K = (tK*(p*ca+q*sa),  tK*(q*ca - p*sa)),   ca=cos α, sa=sin α,  tK > 0
X := q*ca - p*sa        (so K_y = tK * X, the y-coordinate of K)
Z := 2*(a*X + sa*(p²+q²))     [a = |BC| > 0,  p²+q² = |AB|²]
```
Claim: **Z > 0** whenever the actual position hypotheses hold (K strictly interior to triangle BMC,
tK > 0, and α = ∠KBA is a genuine non-degenerate angle). Proof sketch (each step elementary, no
discriminant / no root-selection argument required):

1. **X > 0.** K_y = tK·X is the y-coordinate of K. Since B=(0,0), C=(a,0) both lie on the x-axis and
   M = midpoint(AB) = (p/2, q/2) has q>0, the triangle BMC lies in the closed upper half-plane with
   y = 0 only on its edge BC. K strictly interior to triangle BMC forces **K_y > 0** strictly. Since
   tK > 0 (K ≠ B, already established in the current proof as a consequence of the position
   hypotheses), X = K_y/tK > 0. — This uses ONLY the K-side hypothesis (K interior to BMC), not L,
   not hypothesis (ii)/(iii), not any root-selection of g1/g2.
2. **sa = sin α > 0.** α = ∠KBA is by definition a genuine (non-degenerate, unsigned) angle of the
   configuration, hence α ∈ (0, π) (degenerate only if K were on line AB, excluded since K is a proper
   interior point of BMC, not on ray BA). So sin α > 0.
3. **a > 0, p²+q² = |AB|² > 0** trivially (orientation convention / A ≠ B).
4. Hence Z = 2·(a·X + sa·(p²+q²)) is **2× a sum of two strictly positive terms** (a·X > 0 from 1,3;
   sa·(p²+q²) > 0 from 2,3), so **Z > 0** unconditionally on the valid locus. In particular Z ≠ 0.

This is a strictly stronger and cleaner statement than "Z ≠ 0": Z has a **fixed sign** (positive),
established with no reference to the discriminant of g1, no case-split on which root of g1/g2 is
selected, and using only the single hypothesis "K strictly interior to triangle BMC" (plus the
elementary fact that α is a genuine angle in (0,π), and tK>0). It does not even need the L-side
interior-point hypothesis.

### Numeric verification (this round, from scratch)

- Re-derived Z at the concrete sample p=1.3,q=3.1,a=4,α=0.3 (matching `coordinate-groebner-
  elimination.md`'s example): X ≈ 2.577 > 0, Z ≈ 27.30 > 0. Matches.
- **200,000-sample Monte Carlo** over p∈(-5,5), q∈(0.01,5), a∈(0.01,5), with α drawn strictly inside
  (0, θ) where θ = ∠ABC = atan2(q,p) (i.e. simulating "K's ray-angle from BC is strictly between 0 and
  θ", the geometric consequence of K ∈ interior(∠ABC) ⊇ interior(triangle BMC)): **X>0 and Z>0 held in
  ALL 200,000 trials, zero counterexamples.** This is strong corroboration of the claim above (note:
  the constraint used here, α∈(0,θ), is implied by but slightly stronger than what's strictly needed —
  the proof above only needs K_y>0 directly, which is implied by, but doesn't require computing, θ).
- **Control experiment**: sampling α uniformly over the *full* unconstrained range (0,π) (i.e. dropping
  the "K interior to angle ABC" restriction) reproduces the reviewer's finding that Z's sign is NOT
  fixed — both signs occur — confirming that the geometric constraint (K really interior to triangle
  BMC ⟹ K_y>0) is exactly the load-bearing fact that pins the sign, and that this fact is not a pure
  algebraic identity independent of the hypotheses (as the current.md gap description already
  suspected). No accidental over-strength or error in reproducing the "sign changes in the ambient
  space" observation.

### Distinct openings
- **(Primary, recommended)** The direct positivity argument above: K_y>0 (from strict interiority of K
  in triangle BMC, which lies in the closed upper half-plane touching y=0 only along BC) + tK>0 ⟹ X>0;
  sin α>0 from α being a genuine angle in (0,π); conclude Z = 2(aX + sa|AB|²) is a sum of positive
  terms. This resolves the gap directly with no case-split and no discriminant machinery — the
  cleanest lever found.
- Alternative (not needed given the above, but noted for robustness): tie X to sin(θ-α) where θ=∠ABC
  (verified algebraically: with cosθ=p/|AB|, sinθ=q/|AB|, one gets X/|AB| = sin(θ-α)), giving a second,
  equivalent route via "K inside angle ABC ⟺ 0<θ-α<θ ⟹ sin(θ-α)>0" — this is a strictly weaker/more
  roundabout version of the same fact and can be dropped in favor of the direct K_y>0 argument.
- (Not investigated further, unnecessary): tying Z to the discriminant of g1 or to a power-of-a-point
  quantity — the direct sign argument above makes this unnecessary; do not spend more rounds on it.

### Candidate technique(s)
Elementary sign/positivity argument from the half-plane location of an interior point plus the
non-degeneracy of the angle α ∈ (0,π). No new knowledge-base theorem needed beyond basic triangle-
interior-point facts already implicit in the problem's hypotheses.

### Cheap-kill candidates
The Monte Carlo control experiment above is itself the cheap kill: confirms that dropping the
K-interior-to-triangle-BMC hypothesis (equivalently dropping "K_y>0") is exactly what makes Z change
sign in the ambient space — i.e. it's a clean necessary-and-apparently-sufficient condition, not a
red herring.

### Knowledge-base entries to use
None of `knowledge_base.md`'s named theorems are needed for this step — it's an elementary sign
argument from the coordinate setup already in place (half-plane containment of a triangle-interior
point). Worth checking `knowledge_base.md` for a directed-area / interior-point convexity lemma to
cite formally for "interior point of triangle has y-coordinate strictly between the y-coordinates
of its vertices when two vertices are collinear at y=0", but this is elementary enough to state and
prove inline (convex combination: K = λB+μM+νC with λ,μ,ν>0, λ+μ+ν=1 ⟹ K_y = μ·(q/2) > 0 since B_y=C_y=0,
M_y=q/2>0, μ>0).

### Analogous past problems (cruxes)
Did not query the crux corpus fresh this round (my lens was the Z-sign sub-problem specifically, and
the resolution found is elementary/self-contained, not requiring a borrowed crux move) — if the
outliner wants, a corpus check under domain=geometry, subtopic~"triangle interior point / convex
combination sign argument" could still be done, but the argument above is short enough to state and
prove from scratch without needing to hunt for an analogous case.

### Prior progress
Unchanged from `current.md` except this gap: the identity `myexpr·Z = 2(q−T_K·X)·A_1 + 2(T_L·X'−q)·B_1`
is already proven (independently, symbolically) — this round's contribution is closing the one
remaining piece, Z≠0 (in fact Z>0), via the argument above.

### Dead ends (do not retry)
- Trying to prove Z≠0 as a pure algebraic identity in (p,q,a,α) with no geometric input: confirmed
  again this round to be FALSE (Z changes sign over the ambient/unconstrained parameter space, 20,000-
  sample check) — do not look for an unconditional polynomial-identity proof of Z≠0; it must use the
  K-interior-to-BMC hypothesis (or equivalently tK>0 and K_y>0).
- Tying Z's sign to the discriminant of g1 (mentioned as a possible route in `coordinate-groebner-
  elimination.md`'s open gap) — not needed; the direct argument above bypasses this and requires no
  root-selection / discriminant reasoning about g1 at all. Recommend the outliner drop this heavier
  route in favor of the direct positivity argument.

### Small-case / intuition notes
Conjecture-turned-near-proof: Z>0 always on the valid locus (not just Z≠0). The 200k-sample Monte
Carlo (using the true geometric constraint α∈(0,θ)) found zero sign violations, and the elementary
argument (steps 1–4 above) gives a genuine proof modulo formalizing "interior point of triangle BMC
has positive y-coordinate" (trivial convex-combination fact) and "α=∠KBA is a genuine angle in (0,π)"
(standard angle-measure convention, needs only K∉line AB, guaranteed since K is a proper interior
point). This looks like a complete, short closing lemma for the shared gap — recommend the outliner
build this directly into both `synthetic-angle-chase-aklastar` and `coordinate-groebner-elimination`
approaches as the missing Z≠0 (in fact Z>0) step.
