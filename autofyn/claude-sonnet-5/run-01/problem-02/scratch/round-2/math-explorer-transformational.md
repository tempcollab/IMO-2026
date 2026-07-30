## imo-2026-02

### Setup used for this exploration
Reproduced the prior explorer's 1-parameter family numerically on a fresh scalene
triangle (A=(1.3,3.1), B=(0,0), C=(4,0)), independently confirming both **OM=ON**
and **A, K, L, A\* concyclic** (A\* = rectangle-construction fixed point: reflect A
parallel to BC until its foot moves from the altitude-foot A₀ to the midpoint A′ of
BC) to ~1e-12 precision across the whole scanned parameter range. This corroborates
the synthetic-lens report; I did not just repeat it — I used this reproduction as a
harness to numerically test transformational (spiral similarity / rotation) hypotheses
about K, L directly, reported below.

### Distinct openings — with hypotheses tested and killed or surviving

1. **[KILLED, verified numerically] "K, L are the literal centers of the spiral
   similarities suggested by conditions 2 and 3."** The shape of `∠LBK = ∠LNC`
   looks like the base-angle equality that would hold if a spiral similarity
   centered at L sent B→N and K→C (similarly `∠LCK = ∠BMK` looks like it would
   hold if a spiral similarity centered at K sent C→M and L→B). I computed, for
   each parameter value, the *actual* unique spiral-similarity center S sending
   B→N, K→C (via the standard second-circle-intersection construction) and
   compared it to L: **S ≠ L**, off by O(1) throughout the family (not even
   converging). Same negative result for K vs. the spiral center sending C→M, L→B.
   **Conclusion: the given angle equalities are NOT full spiral-similarity data —
   they are single scalar constraints (base-angle-only, ratio unconstrained), so
   K and L each lie on a one-real-dimension locus compatible with condition 2 (or
   3) individually, not at a pinned "Miquel-type" point.** Do not have the
   outliner assume K or L is literally a spiral-similarity center of any of the
   given point 4-tuples — checked and false.
2. **[KILLED, verified numerically] "K and L are images of one another (or of
   B,C / M,N) under a single fixed-center spiral similarity independent of the
   free parameter."** Computed the spiral-similarity center taking K→L, B→C for
   each parameter value in the family: it is **not constant** (moves by ~O(1)
   across the family, from ≈(1.27,2.21) at one end to ≈(1.10,0.83) at the other).
   So there is no fixed "master" spiral center governing K↔L as the free
   parameter varies. Likewise tested full-triangle similarity KCL ~ KMB (would
   need `∠CKL = ∠MKB` in addition to the given `∠LCK=∠BMK`) and LBK ~ LNC (would
   need `∠BLK = ∠NLC` in addition to given `∠LBK=∠LNC`): **both extra angle
   equalities fail numerically** (off by full radians, not noise) — so these are
   genuinely NOT similar triangles, only the one prescribed angle matches. This
   rules out the "two composed spiral similarities" idea from the synthetic
   report's opening 3 in its literal form — worth telling the outliner this was
   checked and doesn't hold as a clean similar-triangle statement.
3. **[KILLED, cheap check] Isogonality of AK, AL w.r.t. angle A, and AA\* as
   bisector of ∠KAL.** Tested `∠BAK` vs `∠CAL` (isogonal-conjugate-line
   signature) — not equal, drifts by ~0.02 to ~0.09 rad across the family (not
   numerical noise, systematic). Tested whether line AA\* bisects ∠KAL — also
   false (the two sub-angles ∠KAA\* and ∠A\*AL differ by roughly a factor of ~2
   throughout, not equal). So AA\* is not an angle bisector at A and AK, AL are
   not isogonal w.r.t. ∠BAC. Rules out that entire family of "nice symmetric
   line through A" hypotheses.
4. **[SURVIVING — genuinely new opening] Inversion centered at A reduces the
   target to a fixed-point collinearity.** Since A ∈ circle(AKL) always (trivially)
   and (conjecturally/target) A\* ∈ circle(AKL), inverting the whole configuration
   at center A (any radius) sends circle(AKL) to a **line through K\*, L\***, and
   sends the fixed point A\* to a **single fixed point A\*′ = inv_A(A\*)**
   (independent of the free parameter, since A and A\* are both fixed). I verified
   numerically that K\*, L\*, A\*′ are collinear to ~1e-13 across the family — this
   is of course logically equivalent to the concyclicity (inversion preserves
   incidence), but it is a genuinely different *formal target* for a chase: **prove
   K\*, L\* both lie on one fixed line through A\*′**, where K\* = A + r²(K−A)/|K−A|²
   etc. This could be useful because inversion at A fixes the two lines AB and AC
   pointwise-as-sets, so B\* lands back on ray AB and M\* lands back on ray AB too
   (since M is on segment AB), similarly C\*, N\* stay on line AC — i.e. the
   "isosceles-at-M" and "isosceles-at-N" structure (AM=MB, AN=NC) survives
   inversion at A as a clean two-point-per-ray picture, which may make a directed
   angle chase for collinearity cleaner than the direct 4-point concyclicity chase.
   I did NOT push this further (outside my remit), but flag it as a distinct,
   verified-equivalent target the outliner could hand to a builder as an alternate
   route alongside the direct concyclicity chase.
5. **[Sanity check, consistent, not new information] Isosceles case degenerates
   correctly.** When AB=AC, the altitude foot A₀ coincides with the midpoint A′ of
   BC, so by the rectangle construction **A\* = A** exactly (verified: A=(2,3),
   A\*=(2,3) computed). In that case "A, K, L, A\* concyclic" is vacuous (A\*=A, and
   any 3 points A,K,L trivially have *some* circumcircle through A), consistent
   with OM=ON holding automatically by the mirror symmetry B↔C, M↔N, K↔L across
   the axis of symmetry in the isosceles case. This is a good boundary-case
   consistency check but does not by itself supply new structural leverage for the
   scalene case.

### Candidate technique(s)
Given findings 1–3 above are killed, a literal "spiral similarity with one of the
five named points as center" does **not** crack this directly — the three given
angle equalities are individually weaker than spiral-similarity data (single
angle, no ratio). The most promising **transformational** avenue left standing is
opening 4: **inversion centered at A**, converting the concyclicity target into a
fixed-point collinearity target (K\*, L\*, A\*′ collinear), potentially combined with
directed-angle-mod-180° bookkeeping (`∠(XY,XZ)` notation) to avoid configuration
casework, since directed angles are inversion-covariant in a controlled way for
angles subtended at the inversion center itself. A **pure directed-angle chase**
(not routed through inversion) remains the other live candidate, per the synthetic
report — my numerical work here doesn't privilege one over the other; it mainly
serves to prune away the "clean named spiral similarity" family of hypotheses so
the outliner doesn't spend a build cycle on them.

### Cheap-kill candidates
- Isosceles-triangle boundary check (AB=AC ⟹ A\*=A, statement trivializes) is a
  fast sanity test any approach's final chase should reduce to correctly — use it
  to catch sign/configuration errors in a directed-angle proof before trusting the
  general case.
- None of items 1–3 above are usable as "quick kills" of the *problem* (the
  problem is true), but they are quick kills of specific *sub-hypotheses* — don't
  let the outliner re-spend a round re-deriving them.

### Knowledge-base entries to use
- "Synthetic toolkit" (`knowledge_base.md`, Geometry section): angle chasing,
  power of a point / concyclicity converse, spiral similarity, inversion — the
  spiral-similarity and inversion sub-entries are the relevant ones for this lens,
  though spiral similarity itself is now down-weighted per findings 1–3 above;
  inversion is up-weighted per finding 4.
- "Circle/triangle configuration facts" (Miquel point of a complete
  quadrilateral) — still a candidate for *why* the angle conditions force
  concyclicity (Miquel-point machinery handles "angle at one vertex = angle at
  another" configurations more robustly than trying to force literal spiral
  centers, which is what I found doesn't work here).

### Analogous past problems (cruxes)
Confirmed independently (per `crux_moves_documentation.md`): **the crux corpus has
no geometry domain at all** (only number_theory / combinatorics / algebra). No
crux query is possible for this problem; do not force an analogy from another
domain. (Same conclusion as the synthetic-lens report — flagging so the outliner
doesn't re-check this.)

### Prior progress
`results/imo-2026-02/current.md` is still Status: unsolved, no approaches filed yet
(first real round). The synthetic-lens report's reformulation — OM=ON ⟺ A\*
(rectangle-construction fixed point) lies on circle(AKL) — is the strongest
established equivalence so far, and I independently re-verified it on a different
triangle. My contribution: (a) ruled out three specific transformational
hypotheses for *why* it's true, (b) supplied one new verified-equivalent
reformulation via inversion at A.

### Dead ends (do not retry)
- Spiral similarity centered at L sending B→N, K→C (or at K sending C→M, L→B) —
  checked exactly, the true spiral center for that map is a different point than
  L (resp. K), off by O(1) throughout the family. The given angle conditions are
  strictly weaker than "L/K is that spiral center."
- Similar triangles KCL ~ KMB or LBK ~ LNC (full AA similarity, not just the one
  given angle) — checked, the second angle needed for similarity does not match.
- A single fixed-center spiral similarity taking K→L (with B→C) valid for the
  whole family — checked, the center moves substantially as the parameter varies;
  no such fixed map exists.
- AA\* as the angle bisector of ∠KAL, or AK/AL isogonal w.r.t. ∠BAC — both
  checked and false.
- (Carried over from synthetic-lens report, re-confirmed) A\* is not a named
  triangle center (not on nine-point circle, not nine-point-center reflection).
- (Carried over) treating K, L as uniquely determined (they're a genuine
  1-parameter family) — confirmed again by my independent reconstruction of the
  family on a second triangle.

### Small-case / intuition notes (all CONJECTURE except where marked "verified")
- Re-verified (new triangle, new parametrization by θ=∠KBA solved via `fsolve` for
  the remaining 2 unknowns at each θ): OM=ON and A,K,L,A\* concyclic both hold to
  ~1e-12 across the family — strengthens confidence in the synthetic report's
  equivalence but this is still numerical evidence, not proof.
- New: under inversion at A, the fixed point A\*′ = inv_A(A\*) is a legitimate
  alternative "single point" for the outliner to try to characterize directly
  (e.g. maybe A\*′ has a clean description in terms of B\*, C\*, M\*, N\* — I did not
  compute this, flagging as an open sub-question for whoever picks up opening 4).
- The negative results (openings 1–3) suggest the real mechanism is more subtle
  than a single named transformation — likely a genuine multi-step directed-angle
  chase combining all three hypotheses plus the isosceles triangles ABM, ACN
  (BM=MA, CN=NA) is needed, not a one-line "spiral similarity kills it" shortcut.
  Flag this expectation to the outliner so the build doesn't underestimate the
  chase length.
