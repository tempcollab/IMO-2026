## imo-2026-02

trig-circle-factorization: new
Target: Prove for every configuration in the problem that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Three-angle sine-law parametrization followed by a complex circle equation and an explicit trigonometric factorization; this is the analytic whole-problem route.
Skeleton:
  1. Set \(a=BC,b=CA,c=AB\) and \(x=\angle KBA=\angle ACL\), \(y=\angle LBK=\angle LNC\), \(z=\angle LCK=\angle BMK\); derive the strict angle ranges and ray order from all four interior hypotheses — by directed-angle bookkeeping.
  2. Derive \(BK=\frac c2\frac{\sin z}{\sin(x+z)}\) and \(CL=\frac b2\frac{\sin y}{\sin(x+y)}\) — by the sine law in \(BMK\) and \(CNL\).
  3. Derive the two global incidence constraints
     \[\frac c2\frac{\sin z}{\sin(x+z)}=a\frac{\sin(C-x-z)}{\sin(A+2x+z)},\qquad
     \frac b2\frac{\sin y}{\sin(x+y)}=a\frac{\sin(B-x-y)}{\sin(A+2x+y)}\]
     — by the sine law in \(BKC\) and \(BLC\), with angles obtained from Step 1.
  4. Place \(A=0,B=c,C=be^{iA}\) and express \(k=c-r e^{-ix}\), \(l=e^{iA}(b-s e^{ix})\), where \(r,s\) are the lengths in Step 2 — by ray parametrization.
  5. Write \((AKL)\) as \(F(w)=|w|^2+uw+\bar u\bar w=0\); solve the two real equations \(F(k)=F(l)=0\), but retain determinant form rather than expanding \(u\) blindly — by the linear circle-equation method in the knowledge base's Coordinates entry.
  6. Show \(F(c/2)=F(be^{iA}/2)\) by clearing positive sine denominators and factoring the difference as a linear combination of the two Step-3 constraints — by product-to-sum identities.
  7. Conclude equal powers of \(M,N\) to \((AKL)\), hence \(OM^2-ON^2=0\) and \(OM=ON\) — by power of a point.
Key lemmas (claim + the one-line mechanism that makes it true):
  - The two displayed incidence equations are equivalent to the remaining global placements of \(K,L\) — because each is the second sine-law evaluation of the same length \(BK\) or \(CL\), with the interior conditions fixing the unsigned-angle branch.
  - The circle-value difference lies in the linear span of those two incidence residuals after denominator clearing — because the determinant solution for \(u\) is bilinear in \(k,l\), and substituting their ray forms reduces every exponential pair via product-to-sum. This is the load-bearing algebraic lemma to exhibit, not merely assert.
  - Equal circle-polynomial values at \(M,N\) imply the target — because \(F(X)=\operatorname{Pow}_{(AKL)}(X)=OX^2-R^2\).
Open gaps: Step 6's explicit factorization is unproved; the builder must present a checkable identity. Step 1's full angle ranges and Step 5's nonzero determinant also need written verification.
Cases to cover: acute/right/obtuse values of the constituent angles are handled uniformly with directed angles; separately note any zero cosine/dot-product cases are not divided out.
Watch out for: Do not square angle equations or use tangent quotients; both can introduce extraneous orientations. Do not claim the factorization based only on numerical checks.

midpoint-doubling-spiral: new
Target: Prove for every configuration in the problem that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Two midpoint dilations and a finite composition of oriented spiral similarities, adapting the midpoint-doubling crux of `aimo-0705`; this is a synthetic transformation framing.
Skeleton:
  1. Dilate by ratio \(2\) about \(B\), sending \(M\mapsto A,K\mapsto U\), and by ratio \(2\) about \(C\), sending \(N\mapsto A,L\mapsto V\) — by midpoint homothety.
  2. Translate the hypotheses exactly into
     \[\angle ABU=\angle ACL,\quad \angle UBL=\angle VAC,\quad \angle VCK=\angle BAU,\]
     while recording ray orientations — because the two dilations preserve directed angles.
  3. Dilate the whole configuration by ratio \(2\) about \(A\). Then \((AKL)\) maps to \(\Gamma=(A,X,Y)\), where \(X=B+U\), \(Y=C+V\), its centre maps to \(2O\), and \(M,N\) map to \(B,C\) — by homothety.
  4. Reframe the target as \(\operatorname{Pow}_\Gamma(B)=\operatorname{Pow}_\Gamma(C)\) — by equality of squared distances to the centre of \(\Gamma\).
  5. Construct the spiral centre/companion points dictated by the three angle equalities in Step 2, and compose the corresponding direct similarities so that the midpoint identities \(K=(B+U)/2,L=(C+V)/2\) produce either reciprocal similar triangles or a cyclic quadrilateral giving the power equality in Step 4 — by the spiral-similarity lemma and power of a point.
  6. Pull the equality back under the dilation at \(A\) to obtain \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - The transformed three-angle system in Step 2 is exact — because \(BU\parallel BK\), \(CV\parallel CL\), and the homotheties send the vertex pairs \((M,K)\) to \((A,U)\), \((N,L)\) to \((A,V)\).
  - The desired synthetic four-ray lemma is \(\operatorname{Pow}_{(A,B+U,C+V)}(B)=\operatorname{Pow}_{(A,B+U,C+V)}(C)\) under the Step-2 angle system — because this is precisely the doubled target; the builder must prove it by identifying the actual spiral composition.
  - The method transfer from `aimo-0705` is the doubling move, not a citation — there, doubling a midpoint converted a hidden similarity into spiral similarity; the same mechanism motivates \(X=B+U,Y=C+V\), but every cyclicity here still needs proof.
Open gaps: Step 5 is the central unproved gap: no valid spiral centre or companion cyclic quadrilateral has yet been found.
Cases to cover: orientations of all three direct similarities; possible intersections outside the original triangles should be treated with directed angles.
Watch out for: This route is high-diversity but speculative. Reject it if Step 5 only restates equal powers or relies on a diagram; a concrete construction and similarity scale calculation are mandatory.

second-intersection-power: new
Target: Prove for every configuration in the problem that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Synthetic power of a point with second intersections and reciprocal similarities, adapting the equal-power crux of `aimo-0266` and the auxiliary-circle pattern of `aimo-0245`.
Skeleton:
  1. Let \(\omega=(AKL)\), and let \(P\ne A,Q\ne A\) be its second intersections with lines \(AB,AC\) — by auxiliary construction.
  2. Reduce the target to \(MA\cdot MP=NA\cdot NQ\) in directed lengths — because \(OM^2-ON^2=\operatorname{Pow}_\omega(M)-\operatorname{Pow}_\omega(N)\).
  3. Let \(X\ne K\) and \(Y\ne L\) be the second intersections of \(MK\) and \(NL\) with \(\omega\); rewrite Step 2 as \(MK\cdot MX=NL\cdot NY\) — by power of a point at \(M,N\).
  4. Chase cyclic directed angles through \(A,K,L,X,Y\), substituting \(\angle BMK=\angle LCK\), \(\angle LNC=\angle LBK\), and \(\angle KBA=\angle ACL\), to identify two reciprocal similarities linking \((B,K,X)\) with \((C,L,Y)\) — by the inscribed-angle theorem.
  5. Multiply the two resulting side ratios so the intermediate \(BK,CL,BL,CK\) terms cancel and obtain \(MX/NY=NL/MK\) — by similarity.
  6. Apply Step 3 and then Step 2 to conclude equal powers and \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - The target is the directed product identity in Step 2 — because the radius term cancels in the difference of the two powers. This is exactly the transferable crux from `aimo-0266`.
  - The second-intersection products in Step 3 are valid even if \(X,Y,P,Q\) lie on extensions — because directed power of a point is invariant along every secant.
  - A successful similarity pair must have reciprocal total scale \(MX/NY=NL/MK\) — because that equality is algebraically equivalent to the desired product; this criterion prevents accepting an attractive but irrelevant angle match.
Open gaps: Steps 4-5 are unproved: the exact similar triangles have not been identified. The builder may replace them by an exact sine-product derivation in the cyclic quadrilaterals, but must still close the full product identity.
Cases to cover: relative positions of \(P,Q,X,Y\) on line extensions; directed lengths handle them, but the sign convention must be stated once and used consistently.
Watch out for: Angle matching alone does not establish the needed reciprocal scale. This route and the trig route share the equal-power endpoint but not the same mechanism; do not turn it into the full coordinate elimination of the first approach.

vector-perpendicular-bisector: new
Target: Prove for every configuration in the problem that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Vector circle equation plus dot/cross encoding of oriented angle equalities; this targets the fixed perpendicular bisector directly rather than introducing circle secants.
Skeleton:
  1. Put \(A=0\) and write the vectors of \(B,C,K,L\) as \(b,c,k,l\). Write \((AKL)\) as \(|x|^2-q\cdot x=0\), so \(q=2O\) and \(q\cdot k=|k|^2,q\cdot l=|l|^2\) — by the linear equation of a circle through the origin.
  2. Rewrite \(OM=ON\), with \(M=b/2,N=c/2\), as
     \[q\cdot(c-b)=\frac{|c|^2-|b|^2}{2}\]
     — by expanding squared distances.
  3. Encode each of the three angle equalities as a cross-multiplied dot/cross identity, with the correct sign chosen from the interior ray order — by oriented rotations, without tangent division or squaring.
  4. Express \(c-b=\lambda k+\mu l\) explicitly using the two-dimensional determinant formulas for the basis \((k,l)\) — by linear algebra.
  5. Use the three Step-3 identities to prove
     \[\lambda|k|^2+\mu|l|^2=\frac{|c|^2-|b|^2}{2}.
     \]
     The intended mechanism is to represent each angle equality as \(v=tR_\theta u\) with \(t>0\), compose the three rotations so their angles telescope, then compare the scalar coefficients along \(k,l\).
  6. Dot the Step-4 decomposition with \(q\), substitute \(q\cdot k=|k|^2,q\cdot l=|l|^2\), and invoke Step 5 to obtain Step 2 and hence \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Squared-distance equality is the one linear identity in Step 2 — because the common \(|q|^2/4\) term cancels.
  - The coefficients are \(\lambda=((c-b)\times l)/(k\times l)\), \(\mu=(k\times(c-b))/(k\times l)\) — because Cramer's rule in the oriented basis \((k,l)\) applies, with \(k\times l\ne0\) since \(A,K,L\) have a circumcircle.
  - Step 5 is the sole load-bearing angle-algebra lemma — because once it is known, the two circle equations immediately evaluate the left side of Step 2. The builder must provide the actual cancellation, not call it a routine computation.
Open gaps: Step 5's explicit derivation is unproved; Step 3's orientation signs must be derived carefully.
Cases to cover: right-angle cases where dot products vanish; use polynomial cross-multiplied identities. Both orientations of \(ABC\) may be reduced by reflection/WLOG, stated explicitly.
Watch out for: The existence of a circumcentre excludes collinear \(A,K,L\), but no other denominator may be assumed nonzero. Do not compute \(q\) fully; that loses the approach's linear endpoint advantage.
