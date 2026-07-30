## imo-2026-02

Common reformulation used by several approaches below (established, cite in each approach file):
Let A' = midpoint BC, A₀ = foot of altitude from A to BC, A* = A + (A' − A₀) (fourth vertex of
rectangle A,A₀,A',A*; equivalently: reflect A parallel to BC until its foot moves from A₀ to A').
Elementary fact (2-line coordinate check, not deep): midpoint(A,A') = midpoint(M,N) [midline
theorem], and AA* ⊥ ... is parallel to BC, so perp-bisector(AA*) = perp-bisector(MN) whenever A*≠A.
Hence for AB≠AC: **OM=ON ⟺ OA=OA* ⟺ A* lies on circle(AKL)** (O is circumcenter of AKL, so OA is
already a radius). For AB=AC, A*=A and this degenerates — must be handled separately (symmetry).

---

synthetic-angle-chase-aklastar: new
Target: OM = ON for every valid configuration (K,L satisfying the three angle/position hypotheses).
Technique: Directed-angle chase (mod 180°) proving A, K, L, A* concyclic directly from the three
given angle equalities plus the isosceles triangles ABM, ACN (M,N midpoints); then invoke the
common reformulation to conclude OM=ON. Fall back to explicit isosceles-case (AB=AC) symmetry
argument for the degenerate case where A*=A.
Skeleton:
  1. Set up directed angles mod 180° (∠(XY,XZ) notation) to avoid configuration casework — state
     this convention explicitly (KB "Synthetic toolkit": angle chasing).
  2. Record the two isosceles-triangle angle facts forced by M, N being midpoints: in triangle ABM
     (BM=MA), ∠MBA = ∠MAB =: β and ∠AMB = 180°−2β; in triangle ACN (CN=NA), ∠NCA = ∠NAC =: γ and
     ∠ANC = 180°−2γ. These give a base vocabulary of angles to substitute into ∠BMK and ∠LNC in the
     two mixed hypotheses.
  3. Translate the three hypotheses into directed-angle equalities:
     (i) ∠(BK,BA) = ∠(CA,CL) [given ∠KBA=∠ACL, matched with position hypotheses K inside ∠LBA,
         L inside ∠ACK to fix the sign/orientation],
     (ii) ∠(BL,BK) = ∠(NL,NC),
     (iii) ∠(CL,CK) = ∠(MB,MK).
  4. Introduce A* and express ∠(A*K,A*A) and ∠(A*A,A*L) — or equivalently the target
     ∠(AK,AL) = ∠(A*K,A*L) (mod 180°) — as the concyclicity criterion (inscribed-angle converse,
     KB "Circle/triangle configuration facts").
  5. Key lemma (the actual content, not yet closed by any explorer): show
     ∠(AK,AL) − ∠(A*K,A*L) ≡ 0 (mod 180°) by chaining (i)-(iii) through B and C: use that AA*∥BC
     and that A* is characterized by ∠(A*A₀,A*A')=90° / A*A=A'A₀=altitude length, converting
     "angle at A*" into "angle at A₀ or A' as seen from the rectangle," which are angles purely
     about the base triangle (no K,L) — then match against the K,L-side of the chase built from
     (i)-(iii). This is the step to hand to the builder to actually execute; the explorer reports
     supply the vocabulary (isosceles angles β,γ) but not yet the closing identity.
  6. Isosceles case AB=AC: A*=A degenerate; handle directly by the mirror symmetry B↔C, M↔N, K↔L
     across the perpendicular bisector of BC (which is also the axis of symmetry of the whole
     configuration since the three hypotheses are themselves symmetric under this swap) — O then
     lies on the axis automatically, giving OM=ON without invoking A* at all.
Key lemmas (claim + mechanism):
  - Perp-bisector(AA*) = perp-bisector(MN) when AB≠AC — because midpoint(A,A')=midpoint(M,N)
    (midline theorem: MN is the midline parallel to BC through midpoints, so its midpoint equals
    the midpoint of the median AA') and AA* ∥ BC ∥ MN so both segments AA*, MN have the same
    perpendicular direction and same midpoint, hence identical perpendicular bisector.
  - A,K,L,A* concyclic ⟺ ∠(AK,AL) ≡ ∠(A*K,A*L) (mod 180°) — inscribed angle theorem (directed form).
  - Isosceles case reduces to a symmetry argument, no concyclicity needed.
Open gaps: Step 5 (the actual angle-chase closing the concyclicity) is the whole open gap — the
explorers found the vocabulary and reformulation but did not close the chase. This is the hardest,
most load-bearing step; flag to builder that this may require introducing 1-2 auxiliary angles or a
second circle (e.g. circle(BMK) or circle(CNL) suggested by hypotheses (ii),(iii) individually).
Cases to cover: AB≠AC (main, via A*-concyclicity) and AB=AC (symmetry argument), both must appear.
Watch out for: sign/orientation of directed angles when substituting the position hypotheses ("K
inside angle LBA", "L inside angle ACK", K inside BMC, L inside BNC) — these fix which of the two
possible signs is correct and must be justified, not assumed. Also: do not assume K,L are uniquely
determined (there is a 1-parameter family) — the chase must work for a generic member of the family
using only the three hypotheses, not extra assumed relations (explorers confirmed several tempting
extra relations — e.g. AK,AL isogonal, spiral-similarity centers at K or L — are FALSE; do not use).

---

inversion-at-a-collinearity: new
Target: OM = ON for every valid configuration, via inversion.
Technique: Inversion centered at A (KB "Synthetic toolkit": inversion) converting the concyclicity
target A,K,L,A* concyclic into a collinearity of the images K*, L*, A*' (A*'=inv_A(A*) is a single
fixed point independent of the free parameter, since A, A* are both fixed independent of K,L),
then closing with a directed-angle collinearity chase (or a Menelaus/vector argument) using how
inversion at A acts on the two isosceles triangles ABM, ACN (M* lies on ray AB since M is on segment
AB and inversion fixes lines through the center setwise; likewise N*, and B*, C*).
Skeleton:
  1. State inversion ι centered at A, radius r (r=1 WLOG by scaling). Under ι: any point X on ray AB
     maps to X* on ray AB with AX·AX*=r²; lines through A map to themselves (as sets); circles
     through A map to lines not through A.
  2. Apply ι to circle(AKL): its image is exactly line K*L*. The target "A,K,L,A* concyclic"
     becomes "A*' ∈ line K*L*", i.e. K*, L*, A*' collinear, where A*'=ι(A*) is a single new fixed
     point (compute it in terms of A,B,C,r — or leave symbolic, it only depends on the base
     triangle, not on the free parameter of K,L).
  3. Compute how ι acts on the given hypotheses: B*∈ray AB with AB·AB*=r², similarly C*, M*, N*
     (all on rays AB, AC respectively). Since inversion preserves angles at the center A exactly
     (∠(AX,AY)=∠(AX*,AY*) trivially, same ray) but changes angles NOT at A via the standard
     inversion-angle-distortion rule (∠(X*Y*,X*Z*) relates to ∠(XY,XZ) plus terms from
     ∠(AX,XY) type contributions) — translate hypotheses (i),(ii),(iii) from the previous approach
     into statements about K*, L*, B*, C*, M*, N*.
  4. Key lemma: with M*, N* now at known fixed positions on rays AB, AC (since M, N are midpoints,
     M* is a specific fixed point: AM·AM*=r² and AM=AB/2 so AM*=2r²/AB, a determined length),
     the hypothesis-translated conditions constrain K*, L* enough to directly exhibit them as lying
     on a fixed line through A*' — this is the step to hand to the builder; likely provable by a
     Menelaus-type or vector computation exploiting that M*, N*, B*, C*, A*' are all completely
     fixed (independent of the free parameter) once the base triangle is fixed.
  5. Un-invert the collinearity back to concyclicity (mechanical, since ι is an involution), then
     invoke the common reformulation (OM=ON ⟺ A* ∈ circle(AKL)) to conclude.
  6. Handle AB=AC via the same symmetry fallback as the synthetic approach (A*=A degenerates the
     whole inversion picture too, since A*'=ι(A*)=ι(A) is undefined/at infinity).
Key lemmas (claim + mechanism):
  - ι(circle through A) = line not through A, and A,K,L,A* concyclic ⟺ K*,L*,A*' collinear —
    standard inversion fact (KB inversion entry): inversion sends circles through the center to
    lines, and preserves the incidence "point lies on circle" ⟺ "image lies on image line".
  - M*, N* (images of the midpoints) are fixed points depending only on the base triangle — because
    inversion is determined pointwise on ray AB by AM·AM*=r² and AM is fixed (=AB/2).
  - A*' is a single fixed point (not varying with the free parameter) — because A* itself doesn't
    depend on K, L (A* depends only on A,B,C).
Open gaps: Step 3 (translating hypotheses (i)-(iii) under inversion) and step 4 (closing the
collinearity from the translated hypotheses) are both open — this is a genuinely different
computational path from the synthetic approach even though it targets the same intermediate
concyclicity fact, since it works with the inverted picture (fixed points M*,N*,B*,C*,A*' and a
collinearity target) rather than direct angle chase in the original picture.
Cases to cover: AB≠AC (main) and AB=AC (degenerate, symmetry fallback — same as synthetic approach).
Watch out for: inversion distorts angles NOT centered at A in a length-dependent way (the standard
"inversion angle formula" involves the original angle plus correction terms depending on
AX,AY,AZ) — the builder must not assume angles are preserved except for angles literally at vertex
A (∠KAL, ∠BAC-type). This is the main way this approach could silently go wrong.

---

coordinate-groebner-elimination: new
Target: OM = ON for every valid configuration, via full symbolic/computational algebra with the
computation shown (no hand-waving), as the reviewer requires.
Technique: Coordinate bash (KB "Coordinates / complex / barycentric") with an explicit polynomial
system, closed either by direct symbolic substitution/simplification (preferred, human-checkable)
or, if that stalls, by Gröbner-basis / resultant elimination showing the target polynomial lies in
the ideal generated by the hypothesis polynomials — but written out step by step so a human can
verify it, not just "sympy says so".
Skeleton:
  1. Coordinates: B=(0,0), C=(a,0), A=(p,q) with q>0 (WLOG BC on x-axis). Then M=(p/2,q/2),
     N=((p+a)/2,q/2), A'=(a/2,0), A*=(a/2,q). Target reduces (established, elementary) to
     Re(O) = (2p+a)/4 =: target, where O is circumcenter of A,K,L — restate and re-derive this
     2-line reduction explicitly in the proof (don't just cite the explorer numerically; redo the
     algebra symbolically and show it, since the exact formula is short).
  2. Parametrize K, L using the first hypothesis directly built-in: K = B + tK·R(−α)·(A−B)/|A−B|,
     L = C + tL·R(α)·(A−C)/|A−C|, where α = ∠KBA = ∠ACL (one shared parameter, matching hypothesis
     (i) automatically by construction), tK,tL>0 the remaining two free parameters (3 total free
     params: α,tK,tL — matches the confirmed 1-parameter-family-after-3-conditions count once
     conditions (ii),(iii) below are imposed).
  3. Write hypotheses (ii) ∠LBK=∠LNC and (iii) ∠LCK=∠BMK as exact polynomial equations e1=0, e2=0
     in (cos α, sin α, tK, tL, p, q, a) using cross/dot bilinear forms (as the coordinate explorer
     derived — cite and re-derive the correct signed pairing, flagging the known sign pitfall:
     dot(B−M,K−M) not dot(K−M,B−M) for e2).
  4. Write the target myexpr := (p − a/2)·cross(K−A,L−A) + Im(L−A)|K−A|² − Im(K−A)|L−A|² (the exact
     formula the coordinate explorer derived for Re(O)−target up to the nonzero denominator D).
  5. Key computational step (the actual gap): show myexpr ∈ ideal(e1, e2) as polynomials in
     tK, tL (with α,p,q,a as parameters) — i.e. myexpr = f1·e1 + f2·e2 for explicit cofactors
     f1,f2, OR eliminate tK,tL via resultants from e1=e2=0 and substitute into myexpr to get 0
     identically in α,p,q,a. Do this computation with a CAS (sympy) but the proof must display the
     polynomials e1,e2,myexpr explicitly and the algebraic identity/cofactors found, not just
     assert "computer verified" — per rigor rules, show the computation.
  6. Conclude myexpr=0 ⟹ Re(O)=target ⟹ OM=ON, for ALL valid (α,tK,tL) simultaneously — no need to
     separately handle AB=AC, since this route never divides by (A'x−Ax) (myexpr is directly the
     OM=ON criterion, sidestepping the A* concyclicity degeneracy entirely, per the coordinate
     explorer's note).
Key lemmas (claim + mechanism):
  - Re(O) = target ⟺ OM=ON — because M,N have equal height q/2 above BC (midline theorem in
    coordinates), so perp-bisector(MN) is exactly the vertical line x=(Mx+Nx)/2.
  - myexpr=0 is algebraically equivalent to Re(O)=target — direct sympy-derivable circumcenter
    formula (must be re-derived and shown, not just cited).
  - myexpr lies in ideal(e1,e2) — the actual content of the problem, to be established by explicit
    polynomial division/cofactors (preferred) or resultant elimination (fallback), shown in full.
Open gaps: Step 5 entirely — this is a heavy but mechanical computation not yet performed by any
explorer (they derived e1, e2, myexpr but did NOT check myexpr ∈ ideal(e1,e2)). Risk: the
cofactors/resultant computation may be large; if so this approach should report partial progress
(e.g. verified numerically at high precision plus symbolic verification for degree-reduced special
sub-case) rather than claim solved without full display.
Cases to cover: none needed separately (this route naturally covers AB=AC, since a=2p ⟹ p−a/2=0
is just a substitution into myexpr, no special-casing of the derivation).
Watch out for: the sign pitfall in e2 already caught by the explorer (dot(B−M,K−M) vs
dot(K−M,B−M)); must double check with numeric substitution before trusting any symbolic
simplification chain. Also: showing "sympy simplify gives 0" is NOT sufficient for the rigor rules
— must exhibit the actual polynomial identity/division so a human can check it independently.

---

isosceles-locus-direct: new
Target: OM = ON for every valid configuration, without introducing A* or inversion at all —
directly characterize the locus of points equidistant from M and N in terms of K, L using the
isosceles structure at M (BM=MA) and N (CN=NA), then show O is forced onto that locus by the
hypotheses via power-of-a-point at M and N (not via a fourth concyclic point).
Skeleton:
  1. Note perp-bisector(MN) passes through the midpoint of AA' (A'=midpoint BC) and is parallel to
     the altitude from A (perpendicular to BC) — same elementary fact as other approaches, but here
     used only to set up a *power-of-a-point* criterion: for a point O, OM=ON iff pow(O, circle
     with diameter... ) — instead, use directly: OM²−ON² = 2·(N−M)·(O − midpoint(MN)) = 0 iff
     O·(N−M) = midpoint(MN)·(N−M) (a linear condition on O, since N−M ∥ BC is fixed direction) —
     i.e. OM=ON reduces to one linear (dot-product) equation in O's coordinates along the BC
     direction, matching the coordinate route's Re(O)=target but phrased vector-synthetically.
  2. Since O is circumcenter of AKL, O is equidistant from A and K, and from A and L — i.e. O lies
     on perp-bisector(AK) ∩ perp-bisector(AL). Use these two linear conditions plus the one from
     step 1 as three linear conditions O must satisfy; show the hypotheses (i)-(iii) force
     consistency (the three lines concurrent at a single valid O) by expressing everything as
     power-of-a-point computations at B, M, C, N using the isosceles triangles ABM, ACN directly
     (pow(B, circle(AKL))-type expressions, or the power of M and N w.r.t. circle(AKL)) rather than
     via the auxiliary point A*.
  3. Key lemma: express pow(M, circle(AKL)) and pow(N, circle(AKL)) each in closed form using
     MA·MB (=MA² since MA=MB, a fixed known quantity — the power of M w.r.t. any circle through A
     and B would be MA·MB, but circle(AKL) doesn't pass through B; need power via the actual chord
     MA extended, i.e. pow(M,circle(AKL)) = MO² − R² where R is the circumradius, or via a secant
     from M through A and a second intersection point — use the isosceles fact BM=MA to relate the
     secant-line power formula to the given angle hypotheses at M (∠BMK) directly, without ever
     defining A*).
  4. Show pow(M,circle(AKL)) = pow(N,circle(AKL)) directly from hypotheses (ii)/(iii) plus the
     isosceles angle facts (β=∠MAB=∠MBA, γ=∠NAC=∠NCA from step 2 of the synthetic approach) — this
     equality is exactly equivalent to OM=ON (since pow(M,ω)−pow(N,ω) = OM²−R²−(ON²−R²)=OM²−ON²
     for ω=circle(AKL) with center O, radius R), giving a one-step finish that never needs A* as an
     auxiliary point.
Key lemmas (claim + mechanism):
  - OM²−ON² = pow(M,circle(AKL)) − pow(N,circle(AKL)) — because pow(P,ω)=PO²−R² for any circle ω
    with center O radius R, so the R² and the circle cancel in the difference, leaving OM²−ON².
  - pow(M,circle(AKL)) computable via the secant through M, A (M,A,and the second intersection of
    line MA with circle(AKL)) — standard power-of-a-point identity, and the second intersection
    point's position is exactly what hypothesis (iii) (∠LCK=∠BMK) is designed to pin down (∠BMK is
    literally an angle at M, suggesting M's power w.r.t. circle(AKL) is the intended lever).
Open gaps: Steps 3-4 (making "pow(M,circle(AKL)) in closed form via the secant through A" precise
and matching it against hypothesis (iii), and the symmetric statement for N against hypothesis (ii))
are open — this is the least-derisked approach (most speculative of the four) but offers a genuinely
different mechanism (power of a point at M, N directly) than all three other approaches, none of
which use power-of-a-point as the finishing tool. Worth keeping in the population for diversity even
though higher risk.
Cases to cover: AB=AC should fall out automatically here too if it works (no A* dependency), but
verify pow(M,·)=pow(N,·) derivation doesn't secretly divide by (AB−AC) anywhere.
Watch out for: "power of a point" for a chord through M requires identifying the *second*
intersection of line AM (extended) with circle(AKL) — this second point is not obviously any of
K, L, or a named point; if it can't be identified cleanly this approach may dead-end at exactly this
step. Flag this as the first thing the builder should check before investing further.

---

build set: synthetic-angle-chase-aklastar, coordinate-groebner-elimination, inversion-at-a-collinearity
