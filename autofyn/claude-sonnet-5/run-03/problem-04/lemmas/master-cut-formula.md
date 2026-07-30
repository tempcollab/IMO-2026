## Master Cut Formula

**Statement.** Let a triangle have vertex angles a (at A), b (at B), c (at C), a+b+c=180°.
Let P be a point on side BC, and let x = ∠BAP ∈ (0,a), so ∠CAP = a-x. Cutting from P to A
splits the triangle into two children:

  Child₁ = (b, x, a+c-x)   (the triangle ABP; keeps vertex B's angle b unchanged)
  Child₂ = (c, a-x, b+x)   (the triangle ACP; keeps vertex C's angle c unchanged)

**Proof.** In triangle ABP the angles are: at B, b (unchanged); at A, x (by definition);
at P, 180° - b - x by the triangle angle sum. Since a+b+c=180° gives 180°-b = a+c, the angle
at P equals a+c-x. In triangle ACP the angles are: at C, c (unchanged); at A, a-x; at P,
180° - c - (a-x) = 180°-c-a+x = b+x (using a+b+c=180° ⟹ 180°-c-a = b). ∎

**Verification.** Re-derived independently by the reviewer from the triangle angle-sum
theorem; also checked numerically against random triangles.

**Source.** Certified from `results/imo-2026-04/approaches/chip-double-force.md`
(round 2), independently re-derived by budget-partition-dimension.md as well.
