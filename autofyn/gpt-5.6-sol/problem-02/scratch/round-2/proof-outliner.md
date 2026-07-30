## imo-2026-02

vector-perpendicular-bisector: advance
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Oriented ray coordinates plus the certified circumcentre linear-certificate lemma; derive the target from two scalar incidence residuals by one explicit linear identity.
Skeleton:
  1. Reflect if necessary so \(A,B,C\) are counterclockwise; set \(AB=c\), \(AC=b\), \(\angle BAC=A\), and \(x=\angle KBA=\angle ACL\) — by WLOG reflection and the first given angle equality.
  2. Write \(r=BK>0,s=CL>0\), \(h=\sin(A+x)\), and place
     \[
     B=(c,0),\ C=b(\cos A,\sin A),\ K=(c-r\cos x,r\sin x),
     \]
     \[
     L=C-s(\cos(A+x),\sin(A+x)).
     \]
     This incorporates the first angle equality with the correct rays, rather than using the false round-1 angle at \(K,L\).
  3. Establish \(0<x<B\), hence \(0<A+x<A+B<\pi\) and \(h>0\) — by the given interior/ray-order conditions.
  4. Translate \(\angle LBK=\angle LNC\), retaining the ordinary-angle branch, and expand dot-cross products to obtain
     \[
     F_2=(b^2+2s^2-2bs\cos x)h-bc\sin x-bs\sin A=0.
     \]
     Do this by cross-multiplying sine/cosine data or by positive rotation scales; cancel only the manifestly nonzero factor \(br/4\).
  5. Similarly translate \(\angle LCK=\angle BMK\) to
     \[
     F_3=(c^2+2r^2-2cr\cos x)h-bc\sin x-cr\sin A=0,
     \]
     cancelling only the manifestly nonzero factor \(cs/4\).
  6. Import the certified `circumcentre-linear-certificate` lemma: it is enough to prove
     \[
     T=2((C-B)\times L)|K|^2+2(K\times(C-B))|L|^2-(K\times L)(b^2-c^2)=0.
     \]
  7. Define
     \[
     P_3=bc\sin A+bs\sin x-cs\sin(A+x),
     \quad P_2=-bc\sin A+br\sin(A+x)-cr\sin x.
     \]
     Verify the hand-checkable certificate
     \[
     hT+P_3F_3+P_2F_2=0. \tag{*}
     \]
     Present the verification by substituting \(|K|^2=c^2+r^2-2cr\cos x\), \(|L|^2=b^2+s^2-2bs\cos x\), grouping coefficients in \(r,s\), and using only \(\sin(A+x)=\sin A\cos x+\cos A\sin x\) and the Pythagorean identities. Do not cite a CAS check.
  8. Since \(F_2=F_3=0\) and \(h>0\), (*) gives \(T=0\); the certified lemma then yields \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - The second and third angle hypotheses are exactly \(F_2=0,F_3=0\) in the chosen rays — because equality of ordinary angles preserves both oriented sine and cosine, and direct dot-cross expansion has positive removable factors \(br/4,cs/4\).
  - Explicit certificate (*) — because after inserting the displayed squared norms, its coefficients cancel under the angle-addition and Pythagorean identities; the builder must print a compact coefficient table or line-by-line grouping.
  - Target \(T=0\) is equivalent to \(OM=ON\) — by the already certified linear circle equation and Cramer's rule lemma.
Open gaps: Fully hand-check steps 4, 5, and especially the expansion certificate in step 7. This route is close to complete if that certificate is printed rather than asserted.
Cases to cover: The initial reflected orientation; right-angle values in the second or third angle equality (covered without dividing by dot products); nondegeneracy of \(AKL\), implicit in the stated circumcentre.
Watch out for: Never use the false common angle \(A+2x+y+z\). Do not divide by a dot product or tangent. Explicitly justify every cancelled factor and \(h>0\). A numerical or unpresented symbolic check of (*) is not acceptable.

four-circle-midpoint-web: new
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Far-from-analytic directed-angle circle web, Power of a Point, and an explicit midpoint/spiral-similarity lemma; this adapts the midpoint-doubling structural move of `aimo-0705` and the equal-power endpoint of `aimo-0266`.
Skeleton:
  1. Define \(D=BK\cap AC\) and \(E=CL\cap AB\) on the full lines — these are the concrete auxiliary points missing from the earlier synthetic sketches.
  2. Prove \(B,C,D,E\) cyclic from \(\angle DBE=\angle KBA=\angle ACL=\angle DCE\); prove \(B,D,L,N\) cyclic from \(\angle DBL=\angle KBL=\angle LNC=\angle DNL\); prove \(C,E,K,M\) cyclic analogously from the third angle equality — by the directed-angle concyclicity converse.
  3. From \((BCDE)\), obtain \(AB\cdot AE=AC\cdot AD\) — by Power of a Point at \(A\), with directed lengths.
  4. Since \(AM=AB/2\) and \(AN=AC/2\), rewrite step 3 as \(AE\cdot AM=AD\cdot AN\), and conclude \(D,E,M,N\) cyclic — by the directed power/concyclicity converse.
  5. Let \(P\) and \(Q\) be the midpoints of \(BE\) and \(CD\). Prove the midpoint-web lemma
     \[
     A,K,L,P,Q\text{ are concyclic}. \tag{W}
     \]
     The proof must explicitly compose the spiral similarities encoded by the four circles \((BCDE),(BDLN),(CEKM),(DEMN)\), tracking which rays and scale factors carry \(B,E\) to their midpoint \(P\) and \(C,D\) to \(Q\). Following `aimo-0705`, doubling about the relevant endpoint may remove each midpoint before applying the spiral-similarity lemma; unlike the old sketch, name every image and circle in the composition.
  6. Put \(\omega=(AKL)\). By (W), \(P,Q\) are the second intersections of \(AB,AC\) with \(\omega\). Using directed lengths,
     \[
     \operatorname{Pow}_\omega(M)=MA\cdot MP
       =\frac14\,AB\cdot AE,
     \quad
     \operatorname{Pow}_\omega(N)=NA\cdot NQ
       =\frac14\,AC\cdot AD,
     \]
     with a common sign according to the chosen directed convention.
  7. Step 3 makes the powers equal. As \(O\) is the centre of \(\omega\), \(OX^2-R^2=\operatorname{Pow}_\omega(X)\) gives \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Four-circle web: \((BCDE),(BDLN),(CEKM),(DEMN)\) are cyclic — because each of the first three is a direct concyclicity converse to one given angle equality, and the fourth follows from the midpoint-scaled power identity.
  - Midpoint-web lemma (W) — expected mechanism is a concrete composition of the four spiral similarities after factor-2 dilations remove \(P,Q\); this is the exact synthetic burden and must be supplied, not replaced by “Miquel theorem” vocabulary.
  - Equal powers imply equal centre distances — because \(\operatorname{Pow}_\omega(X)=OX^2-R^2\), the same endpoint used in the analogous `aimo-0266` solution.
Open gaps: Step 5 is unproved. The builder must either give a complete directed-angle/spiral-similarity proof of (W), or leave the approach partial; numerical evidence is not a certificate.
Cases to cover: Possible external positions/orderings of \(D,E,P,Q\) on the full side lines; directed-length signs; degenerate coincidences (if an auxiliary point coincides with a vertex, handle by the same directed identity or a limiting/direct argument).
Watch out for: Do not assert inversion exchanges \(K,L\) (it does not). Do not fall back to unnamed similar triangles or the analytic circle-equation gap. Check whether the five-point statement (W), rather than merely separate four-point concyclicities, is actually established.

trig-circle-factorization: revise
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Corrected Sine Law parametrization, cotangent substitution, and bounded-degree polynomial remainder certificate using the certified circle-value determinant lemma.
Skeleton:
  1. After reflection, let \(A,B,C\) be counterclockwise and put
     \[
     x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,\quad z=\angle LCK=\angle BMK,
     \]
     \(p=B-x-y\), \(q=C-x-z\). Record \(0<p<B-x\), \(0<q<C-x\).
  2. Recompute from the ray order
     \[
     \angle BKC=A+2x+z=\pi-B+x-q,
     \quad
     \angle BLC=A+2x+y=\pi-C+x-p.
     \]
     These angles are generally different; delete every use of the false round-1 common angle.
  3. Apply the Sine Law separately in \(BMK,BKC,CNL,BLC\), together with the triangle Sine Law, to derive
     \[
     F_p=\sin B\sin(B-x-p)\sin(C-x+p)-2\sin A\sin p\sin(B-p)=0,
     \]
     \[
     F_q=\sin C\sin(C-x-q)\sin(B-x+q)-2\sin A\sin q\sin(C-q)=0.
     \]
     Give the triangle-by-triangle derivation and positivity of every sine denominator.
  4. Substitute \(P=\cot p,Q=\cot q\). Divide only by \(\sin^2p,\sin^2q>0\) to obtain the two explicit quadratics
     \[
     \widehat F_p=\sin B[\sin(B-x)P-\cos(B-x)][\sin(C-x)P+\cos(C-x)]-2\sin A[\sin BP-\cos B],
     \]
     \[
     \widehat F_q=\sin C[\sin(C-x)Q-\cos(C-x)][\sin(B-x)Q+\cos(B-x)]-2\sin A[\sin CQ-\cos C].
     \]
  5. Normalize \(AB=1\), put \(b=AC=\sin B/\sin C\), and express
     \[
     R=BK=\frac{\sin(C-x)Q-\cos(C-x)}{2(\sin C Q-\cos C)},
     \quad
     S=CL/b=\frac{\sin(B-x)P-\cos(B-x)}{2(\sin B P-\cos B)},
     \]
     \[
     k=1-Re^{-ix},\qquad l=be^{iA}(1-Se^{ix}).
     \]
  6. Import the certified circle-value determinant lemma to write the desired condition as one rational numerator \(T(P,Q)=0\).
  7. Clear only denominators proved nonzero from the geometric intervals. Reduce \(\operatorname{num}T\) first modulo \(\widehat F_p\) in \(P\), then modulo \(\widehat F_q\) in \(Q\). Print the quotient terms and the final remainder of bidegree at most \((1,1)\), then simplify each of its four coefficients to zero using \(A+B+C=\pi\) and elementary trig identities. Equivalently print explicit \(U,V\) with \(\operatorname{num}T=U\widehat F_p+V\widehat F_q\).
  8. Since both residuals vanish, the certificate gives \(T=0\), hence \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Correct residuals \(F_p,F_q\) — because the two large-triangle angles are separately \(\pi-B+x-q\) and \(\pi-C+x-p\), after which the midpoint Sine Law equations decouple.
  - Cotangent quadratics — because every sine \(\sin(U\pm p)/\sin p\) is a linear expression in \(\cot p\), and similarly for \(q\).
  - Bounded-degree certificate — because division by the two univariate quadratics leaves only four bidegree coefficients to check, adapting the finite coefficient-matching move of `aimo-0903`; preserving linear sine brackets mirrors the compact constraint-substitution move of `aimo-0939`.
Open gaps: Step 7 remains unproved; the builder must provide the actual quotient/remainder identity. Steps 2–5 must also be rebuilt in the approach file because its current angle table is false.
Cases to cover: Reflected orientation; admissible cotangent roots selected by \(0<p<B-x\), \(0<q<C-x\); any zero denominator before clearing (show impossible or split it off explicitly); right angles \(p=\pi/2\) or \(q=\pi/2\), which are allowed by cotangent but not by divisions through cosine.
Watch out for: The current file's claimed common angle and coupled denominators are false. Do not use tangent equality alone, do not discard supplementary/right-angle branches, and do not call a CAS/ideal computation a proof without printing the identity.
