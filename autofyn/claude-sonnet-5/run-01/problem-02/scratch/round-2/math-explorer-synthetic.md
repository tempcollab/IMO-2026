## imo-2026-02

### Key new finding (numerically verified, high confidence): equivalent concyclicity reformulation

Define the **fixed point A\*** (depends only on A, B, C — not on K, L):
let A₀ = foot of the altitude from A onto BC, A' = midpoint of BC.
A\* is the fourth vertex of the rectangle A, A₀, A', A\* (i.e. A\* = A + (A' − A₀); equivalently
AA\* ∥ BC, A'A\* ⊥ BC, and |A'A\*| = |A A₀|). Concretely: A\* is the point at the same height above
line BC as A, but positioned directly "above" the midpoint of BC (in the direction perpendicular to
BC), i.e. reflect A parallel to BC until its foot on BC becomes the midpoint of BC.

**Claim (verified numerically to ~1e-13 relative precision on two independent scalene triangles,
across the whole valid range of the free parameter):** A, K, L, A\* are concyclic.

This is *equivalent* to the problem's conclusion OM = ON: since O is already equidistant from A
and A\* iff A\* lies on circle(AKL) [because O is defined as circumcenter of AKL, so OA is a radius;
OA = OA\* ⟺ A\* on that circle], and O equidistant from A, A\* ⟺ O lies on the perpendicular
bisector of AA\*. A short computation shows the perpendicular bisector of segment AA\* is *the same
line* as the perpendicular bisector of MN (both are the line through the midpoint of AA' — which
equals the midpoint of MN, since midpoint(MN) = midpoint(A, A') always by the midline theorem —
perpendicular to BC). Hence: **O ∈ perp-bisector(MN) [i.e. OM=ON] ⟺ A\* ∈ circle(AKL)**.

This turns a metric distance-equality goal into a pure **concyclicity** goal with one new
completely fixed point A\*, which is exactly suited to synthetic angle chasing / power-of-a-point /
spiral-similarity techniques, and is a strictly more tractable-looking target than "prove OM=ON"
directly. I recommend the outliner build (at least) one approach around proving A, K, L, A\*
concyclic via an angle-chase using the three given angle equalities, since A₀ and A' (ingredients
of A\*) are both classical points (foot of altitude, midpoint of BC) with many known circle
relations (nine-point circle, circle with diameter AA', etc.) — although note: I checked whether
A\* itself lies on the nine-point circle of ABC and it does **not** (numerically the nine-point
circle passes through M, N, A', A₀ but not A\*), so don't waste time hunting for A\* as a
"named" triangle center — it appears to be a genuinely bespoke point tied to this problem,
defined only by the rectangle construction above.

### Structural observation: this is a moving-point / coaxial-pencil configuration

The three angle conditions (∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK) are 3 equations in the 4 degrees of
freedom of (K,L) (2 each), so K, L are **not uniquely determined** — there is a genuine 1-parameter
family of valid (K,L) pairs satisfying all constraints and the "inside" position requirements
(verified by numerically continuing a solution branch in the free parameter and checking the
"inside triangle BMC / BNC" and orientation conditions hold throughout an interval). OM=ON was
checked to hold (to numerical precision) across this *entire* family, on two different scalene
triangles — so the intended proof almost certainly must work "for the whole family at once" (i.e.
a single angle-chase valid for any K,L satisfying the hypotheses), not by pinning down K,L
uniquely first. This also explains why the fixed circle through A and A\* is the right target: as
the parameter varies, circle(AKL) is a genuine **pencil of circles through the two fixed points A,
A\*** — the coaxial-pencil viewpoint (radical axis = line AA\*) may be a second way to phrase the
same target for the outliner (e.g. show K, L always lie on some circle through A and A\*, perhaps
by identifying the pencil directly via power-of-a-point computations at B or C using the given
angle equalities, rather than chasing all 4 points concyclic head-on).

### Distinct synthetic openings to attack "A,K,L,A\* concyclic" (or directly OM=ON)

1. **Spiral similarity at A\* (or A) sending B-related data to C-related data.** The pattern
   ∠KBA = ∠ACL (angle at B equals angle at C) is the classic signature of a spiral similarity
   center that sees B and C at equal angles — worth checking whether A\* (or some other point on
   line AA\*) is the center of a spiral similarity taking ray BK to ray CL, or taking triangle
   related to B,K to one related to C,L. If such a center P has ∠PBK = ∠PCL type relations,
   standard spiral-similarity lemmas (center of spiral similarity taking segment to segment lies
   on the circle through the intersection of the lines and the two "other" points) could directly
   produce concyclic quadruples.
2. **Direct angle chase for the concyclicity A,K,L,A\*.** Show ∠KAL + ∠KA\*L = 180° (or ∠AKA\* =
   ∠ALA\*, etc.) by expressing every angle in the chain ∠KBA, ∠ACL, ∠LBK, ∠LNC, ∠LCK, ∠BMK in
   terms of the base triangle's angles plus the position of K, L, using that M, N are midpoints
   (so BM = MA, CN = NA — gives isosceles sub-triangles BMA, CNA, hence ∠MBA=∠MAB and
   ∠NCA=∠NAC as a starting set of equal angles to feed the chase).
3. **Use the midline MN directly.** MN ∥ BC and MN = BC/2. The conditions ∠LBK=∠LNC and
   ∠LCK=∠BMK pair an angle at B or C (near K/L) with an angle at N or M (on the midline) — this
   symmetric pairing (B↔M, C↔N in the second/third conditions vs the direct B↔C pairing in the
   first) suggests two "isosceles-triangle-driven" spiral similarities (one centered near M via
   BMA isosceles, one near N via CNA isosceles) that might compose to the same transformation
   that the first condition's B↔C spiral similarity gives — i.e. the three conditions may be
   forcing K and L to be corresponding points under *one* spiral similarity (center TBD, possibly
   A or A\*) applied twice (once directly B→C, once via the "reflected" isosceles triangles at
   M, N). Worth having the outliner explore whether K, L are images of each other under a single
   fixed-center spiral similarity, independent of the free parameter t — if so, the concyclicity
   of A, K, L, A\* might follow from a "center of spiral similarity lies on the circumcircle of
   the two initial and two final points" lemma (a standard configuration fact in the KB's
   "spiral similarity" toolkit entry).
4. **Isosceles sub-triangles from M, N as midpoints.** BM = AM (M midpoint of AB) makes triangle
   ABM isosceles at M — this converts "angle at M" (∠BMK in the third condition) into
   information about the apex angle of isosceles triangle ABM plus ∠KMA, potentially letting one
   replace ∠BMK by 180° − 2∠MAB − ∠(something with K) or similar identities. Likewise for N.

### Candidate technique(s)
Spiral similarity (KB "Synthetic toolkit" entry: similar triangles, spiral similarity, angle
chasing) combined with cyclic-quadrilateral / concyclicity criteria (equal angles subtending a
segment, or opposite angles summing to 180°), applied to the reformulated target "A, K, L, A\*
concyclic." The isosceles triangles from the midpoint definitions of M, N are the natural source
of the extra angle relations needed to close the chase.

### Cheap-kill candidates
None obvious as a full kill, but a useful cheap reduction is already found: replacing the metric
goal OM=ON with the purely angular/concyclicity goal "A,K,L,A\* concyclic" removes all need for
explicit distances or coordinates — a pure angle chase can in principle finish the problem without
any length computation. Also: since M,N,A₀,A' are all on the nine-point circle, if any approach
ends up needing "A\* on the nine-point circle" that is a dead end — numerically confirmed false;
don't pursue it.

### Knowledge-base entries to use
- "Synthetic toolkit" (angle chasing, power of a point, similar triangles, spiral similarity) —
  `knowledge_base.md` Geometry section, first bullet.
- "Circle/triangle configuration facts" (concyclicity converses, Miquel point of a complete
  quadrilateral) — same section, second bullet; the Miquel-point idea is a candidate if K, L, A\*
  arise as a complete-quadrilateral configuration.
- General "Direct proof" / "Casework" meta-methods for organizing the angle chase.

### Analogous past problems (cruxes)
The crux corpus currently has **no geometry cruxes at all** (`crux_moves_documentation.md`
explicitly states: "geometry — Not in the corpus yet; the problems DB includes geometry problems
with solutions, but no geometry cruxes have been extracted"). So there is nothing to query for
this domain — confirmed by reading the documentation, not guessed. No analogous crux available;
do not force a match from another domain.

### Prior progress
None — `results/imo-2026-02/current.md` is Status: unsolved, no approaches yet (this is round 2,
the workspace was just created). This report is first reconnaissance.

### Dead ends (do not retry)
- Treating K, L as uniquely determined by the three angle conditions — they are NOT; there's a
  genuine 1-parameter family (verified numerically). Any approach that tries to "solve for K, L"
  as if the system is square (4 unknowns, 4 equations) is missing that only 3 conditions are given
  and will either fail or silently assume an extra unstated constraint.
- Looking for A\* among named triangle centers (nine-point circle, symmedian point, etc.) — checked
  numerically, A\* is not the nine-point center's reflection or on the nine-point circle; it's a
  bespoke point from the rectangle construction above.

### Small-case / intuition notes (all labeled CONJECTURE, verified only numerically)
- Numerically verified on two independent scalene triangles (coordinates: A=(1.3,3.1), B=(0,0),
  C=(4,0); and A=(0.5,2.7), B=(-1,0), C=(3.5,0.3)), scanning a continuum of valid (K,L) pairs
  satisfying the three angle equalities and lying strictly inside the required triangles BMC, BNC:
  OM=ON holds to ~1e-12 relative precision throughout, confirming the problem statement.
  - The circumcenter O of AKL traces a *straight line segment* as the free parameter varies — this
    line is exactly the perpendicular bisector of MN (equivalently of A and A\*).
  - The circumcircle of AKL is a member of a pencil of circles all passing through the two fixed
    points A and A\* as the parameter varies (radical axis of the pencil = line AA\*).
  - Caution for future numeric checks: the angle conditions as literally written (unsigned angle
    equalities) admit spurious extra solution branches that do NOT satisfy the problem's "K inside
    angle LBA", "L inside angle ACK", "K inside triangle BMC", "L inside triangle BNC" side
    constraints — on the second (tilted) test triangle, a naive fsolve from one initial guess
    landed on such a spurious branch and OM≠ON there. Always filter numerical solutions by the
    inside-triangle / inside-angle conditions before trusting OM=ON as evidence; once filtered
    correctly, the equality held robustly on both triangles.
