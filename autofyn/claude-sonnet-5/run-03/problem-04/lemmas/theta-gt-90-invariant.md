## θ>90° Survival Invariant (special-case cross-check, subsumed by residue-clean-invariant)

**Statement.** If a triangle has all three angles ≤90°, then for any cut (any vertex a with
others b,c≤90°, any x∈(0,a)) via the Master Cut Formula, at least one child again has all
three angles ≤90°.

**Proof.** The two "new" angles a+c-x and b+x sum to 180°, so at most one exceeds 90°.
If a+c-x≤90°: Child₁=(b,x,a+c-x) has b≤90°, x<a≤90°, a+c-x≤90° — all ≤90°.
If a+c-x>90°: then b+x<90° (strictly, from the 180° sum), so Child₂=(c,a-x,b+x) has c≤90°,
a-x<a≤90°, b+x<90° — all ≤90°. ∎

**Consequence.** For θ>90°, Shan-Yu starts from an all-≤90° triangle (e.g. equilateral) and
always keeps an all-≤90° child; since every angle he ever holds is ≤90°<θ, no angle is ever
equal to θ — he survives forever.

**Status.** This is a valid, self-contained special case; it is subsumed by the more general
residue-clean-invariant (Lemma A/B), which covers all θ with 180/θ∉ℤ uniformly, including
θ>90°.

**Source.** Certified from `results/imo-2026-04/approaches/chip-double-force.md` (round 2).
