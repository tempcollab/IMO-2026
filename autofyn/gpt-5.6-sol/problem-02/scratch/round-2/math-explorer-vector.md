## imo-2026-02
- Distinct openings:
  1. **Oriented ray coordinates absorb (E1), while (E2) and (E3) become two short scalar residuals.** After reflecting if necessary, take \(A,B,C\) counterclockwise and write \(AB=c,AC=b,\angle BAC=A\). Put \(x=\angle KBA=\angle ACL\), \(r=BK>0,s=CL>0\), and abbreviate \(h=\sin(A+x)\). The interior/ray-order data give
     \[
     B=(c,0),\quad C=b(\cos A,\sin A),
     \]
     \[
     K=(c-r\cos x,r\sin x),\quad
     L=b(\cos A,\sin A)-s(\cos(A+x),\sin(A+x)).
     \]
     Thus (E1) is built into the parametrization with the correct ordinary-angle branch and positive scales. Direct dot-cross expansion of (E2), with its nonzero positive prefactor \(br/4\), reduces to
     \[
     F_2:=(b^2+2s^2-2bs\cos x)h-bc\sin x-bs\sin A=0.
     \]
     Likewise (E3), with nonzero positive prefactor \(cs/4\), reduces to
     \[
     F_3:=(c^2+2r^2-2cr\cos x)h-bc\sin x-cr\sin A=0.
     \]
     These formulas are hand-checkable: the quadratic factors are \(|L|^2\) and \(|K|^2\), respectively. Also \(h>0\), since the ray order gives \(0<x<B\), hence \(0<A+x<A+B<\pi\).
  2. **A concrete linear certificate for target (T), apparently closing the shared algebraic gap without the erroneous sine-law system.** Let \(T\) denote exactly the left side minus right side of the certified target
     \[
     2((C-B)\times L)|K|^2+2(K\times(C-B))|L|^2-(K\times L)(b^2-c^2).
     \]
     With the above coordinates, the following compact identity is the promising certificate:
     \[
     hT+P_3F_3+P_2F_2=0,
     \]
     where
     \[
     P_3=bc\sin A+bs\sin x-cs\sin(A+x),
     \]
     \[
     P_2=-bc\sin A+br\sin(A+x)-cr\sin x.
     \]
     This was checked by direct polynomial expansion using only \(\sin(A+x)=\sin A\cos x+\cos A\sin x\) and the two Pythagorean identities; it does not require an ideal-membership assertion. It should be verified/presented as a line-by-line expansion or by grouping coefficients of \(r,s\), not cited as a symbolic computation. Because \(F_2=F_3=0\) and \(h>0\), it reaches (T). This is materially different from the prior attempted elimination: no angles at \(K,L\), no Sine Law in \(BKC/BLC\), and no tangent division are used.
  3. **Linear-geometric interpretation of the same certificate.** The certified circle functional \(q\cdot X-|X|^2\) converts the goal to equality of the powers of \(B/2,C/2\), or equivalently the affine condition \(q\cdot(C-B)=(b^2-c^2)/2\). The residuals \(F_2,F_3\) can be regarded as the two oriented-rotation incidence constraints after the common rotation by \(x\) is fixed. The displayed certificate says this affine circle functional lies in their two-dimensional linear span with explicit coefficients \(P_2/h,P_3/h\); this is a usable invariant framing rather than a black-box polynomial-ideal framing.
- Candidate technique(s): Oriented vector/dot-cross angle encoding; positive rotation-scale parametrization; linear circle equation and Cramer's rule; explicit residual factorization. The main candidate is the short certificate \(hT+P_3F_3+P_2F_2=0\), with branch control supplied before any cancellation.
- Cheap-kill candidates: Absorb (E1) into rays rather than retaining three bulky dot-cross equations; cancel only the manifestly positive factors \(b,c,r,s,h\). No case split at right angles is needed, since neither \(F_2,F_3\) nor the certificate divides by a dot product. Positivity also excludes the supplementary-angle/tangent branch. The factors \(b^2+2s^2-2bs\cos x\) and \(c^2+2r^2-2cr\cos x\) should be recognized as squared norms to shorten checking.
- Knowledge-base entries to use: **Coordinates / complex / barycentric** (oriented coordinates aligned with \(AB\)); **Circle/triangle configuration facts — power of a point** (equivalent circle-power endpoint); **Synthetic toolkit — angle chasing** (ray order and ordinary-angle branches); **Resultants / “transform the roots”** only in its explicit-identity sense (the displayed certificate, not an unreported resultant); **Introduce a substitution / change of variables** (the shared angle \(x\) as a rotation parameter); **Invariant / monovariant** (the affine circle functional as the linear-geometric invariant).
- Analogous past problems (cruxes): `aimo-0266` — genuinely analogous endpoint: an equal-distance-to-a-circumcentre claim is changed into equality of powers and then a product identity; its second solution also compares circumcentres through projections, closely matching the linear-functional viewpoint here. `aimo-0705` — weaker but relevant midpoint analogy: dilation by factor 2 removes a midpoint and exposes a spiral-similarity/cyclicity relation; useful for interpreting the \(1/2\) geometry, though not for the explicit vector certificate. The crux database has no geometry-domain crux entries (as the documentation warns), so these were read from the geometry records in the problems database rather than forced through a nonexistent geometry subtopic.
- Prior progress: Status is `partial`; task is `proof_only` with answer type `none`. The certified circumcentre-linear lemma reduces the theorem exactly to (T). The live vector approach has a correct ordered-pair translation (E1)–(E3), but previously lacked any derivation of (T). The live trig approach has useful ray parametrization but its reviewed incidence equations are unreliable because its angle bookkeeping at \(K,L\) was disputed. The new two-residual certificate above is the furthest promising vector progress and bypasses that disputed calculation entirely.
- Dead ends (do not retry): Bare rotation-scale telescoping introduces unrelated positive scale factors and gives no length relation. Do not divide tangent equations by dot products: right-angle cases are then silently lost. Do not invoke “symbolic ideal computation confirms it” without the explicit identity. Do not use the sine-law equations from the current trig file as settled: the review metadata says the claimed common angle/denominators are wrong, while that file contains a contradictory later correction; the vector certificate needs none of them. Pure midpoint-doubling and second-intersection sketches remain mechanism-free until an actual similarity/cyclicity is identified.
- Small-case / intuition notes: **Symbolically checked conjectural certificate:** expanding \(hT+P_3F_3+P_2F_2\) reduces identically to zero under only \(\sin(A+x)\)'s addition formula and \(\sin^2+\cos^2=1\). This is strong reconnaissance evidence, not yet a presented proof. It suggests (E2) and (E3), once (E1) fixes the common oriented rotation, already contain exactly the two scalar relations needed; there is no third hidden incidence equation and no exceptional right-angle branch. Orientation and positivity are essential: \(r,s>0\), \(0<x<B\), and \(h>0\).