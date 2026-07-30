## imo-2026-02
- Distinct openings:
  1. **Corrected residual factorization in the complementary angles.** Assume after reflection that \(A,B,C\) are counterclockwise and put
     \[
     x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,\quad z=\angle LCK=\angle BMK,
     \]
     then introduce the two remaining corner angles
     \[
     p:=B-x-y=\angle CBL,\qquad q:=C-x-z=\angle KCB.
     \]
     Thus \(0<p<B-x\), \(0<q<C-x\). Directly from the ray order, not from the erroneous round-1 table,
     \[
     \angle BKC=A+2x+z=\pi-B+x-q,
     \qquad
     \angle BLC=A+2x+y=\pi-C+x-p.
     \]
     In particular these are generally different. The midpoint triangles and the two large triangles give the corrected system
     \[
     BK={c\over2}{\sin(C-x-q)\over\sin(C-q)}
       =a{\sin q\over\sin(B-x+q)},                                    \tag{K}
     \]
     \[
     CL={b\over2}{\sin(B-x-p)\over\sin(B-p)}
       =a{\sin p\over\sin(C-x+p)}.                                    \tag{L}
     \]
     After the triangle sine law, these become two *decoupled quadratic residuals*
     \[
     F_p:=\sin B\sin(B-x-p)\sin(C-x+p)
       -2\sin A\sin p\sin(B-p)=0,                                     \tag{Fp}
     \]
     \[
     F_q:=\sin C\sin(C-x-q)\sin(B-x+q)
       -2\sin A\sin q\sin(C-q)=0.                                    \tag{Fq}
     \]
     This is substantially cleaner than the invalid coupled denominator \(A+2x+y+z\) in the old file.

     For a hand-checkable algebraic certificate, set \(P=\cot p,Q=\cot q\). Since \(p,q\in(0,\pi)\), division by \(\sin^2p,\sin^2q\) is branch-safe. The exact quadratic polynomials are
     \[
     \begin{aligned}
     \widehat F_p(P)={}&\sin B\,[\sin(B-x)P-\cos(B-x)]
       [\sin(C-x)P+\cos(C-x)]\\
       &-2\sin A\,[\sin B\,P-\cos B],
     \end{aligned}                                                     \tag{PFp}
     \]
     \[
     \begin{aligned}
     \widehat F_q(Q)={}&\sin C\,[\sin(C-x)Q-\cos(C-x)]
       [\sin(B-x)Q+\cos(B-x)]\\
       &-2\sin A\,[\sin C\,Q-\cos C].
     \end{aligned}                                                     \tag{PFq}
     \]
     Normalize \(AB=c=1\), so \(AC=b=\sin B/\sin C\), and define
     \[
     R={BK\over c}={\sin(C-x)Q-\cos(C-x)\over2(\sin C\,Q-\cos C)},
     \quad
     S={CL\over b}={\sin(B-x)P-\cos(B-x)\over2(\sin B\,P-\cos B)}.   \tag{RS}
     \]
     Then
     \[
     k=1-Re^{-ix},\qquad l={\sin B\over\sin C}e^{iA}(1-Se^{ix}).      \tag{Z}
     \]
     Substitution of (Z) into the certified circle determinant target produces a rational bidegree expression in \((P,Q)\). The concrete certificate to seek is ordinary two-variable polynomial division of its cleared numerator by the two displayed quadratics:
     \[
     \operatorname{num}(T)=U(P,Q)\widehat F_p(P)+V(P,Q)\widehat F_q(Q),\tag{Cert}
     \]
     with low-degree trigonometric coefficients. This is a finite hand-checkable target: expand the two sides and compare the at most nine bidegree coefficients, rather than citing an ideal/CAS computation. A useful way to keep coefficients readable is to leave the four linear brackets in (PFp),(PFq) unexpanded.

  2. **Complex circle-coefficient parametrization.** In the same normalization, retain (Z) and write the circle through \(0,k,l\) as \(|w|^2-2\Re(\bar o w)=0\). The desired perpendicular-bisector condition is the single real-linear equation
     \[
     2\Re(\bar o(be^{iA}-1))=b^2-1.
     \]
     Solving for \(o\) from \(2\Re(\bar o k)=|k|^2\) and \(2\Re(\bar o l)=|l|^2\) is exactly the certified determinant lemma, but (RS) may allow the resulting numerator to be grouped directly into the two bracketed residuals (PFp),(PFq), avoiding a full trigonometric expansion. This is a distinct presentation opening, though algebraically it reaches the same certificate.

  3. **Root-selection/parametrization opening.** Each of (PFp),(PFq) is quadratic, while geometry selects \(P=\cot p\) with \(0<p<B-x\) and \(Q=\cot q\) with \(0<q<C-x\). Numerically the second algebraic root lies outside the allowed interval. Factoring each quadratic using its two roots, then retaining the interval-selected root, may yield a short radical or Möbius parametrization for \(R,S\). This could simplify the circle equation more than direct bivariate reduction, but the root interval must be proved and no square-root cancellation has yet been found.

- Candidate technique(s): Corrected sine-law parametrization; cotangent substitution turning the two incidences into separate quadratics; low-bidegree polynomial remainder/factorization; complex/vector circle equation with a real-linear circumcentre condition. All ordinary-angle data should be carried as \(0<p<B-x\), \(0<q<C-x\), with \(y=B-x-p>0,z=C-x-q>0\).

- Cheap-kill candidates: Before any large expansion, reduce the cleared target modulo \(\widehat F_p\) in \(P\) and modulo \(\widehat F_q\) in \(Q\); the remainder has bidegree at most \((1,1)\), so only four coefficients need simplification. Also preserve the bracket factors in (PFp),(PFq), since they are exactly the sines \(\sin(B-x-p),\sin(C-x+p),\sin(C-x-q),\sin(B-x+q)\) divided by \(\sin p\) or \(\sin q\). This is preferable to expanding into many \(\sin(A+\cdots)\) terms.

- Knowledge-base entries to use: **Synthetic toolkit — angle chasing and Sine Law**; **Coordinates / complex / barycentric**; **Resultants / “transform the roots”** (the explicit identity (Cert), not an unpresented computation); **Introduce a substitution / change of variables** (\(P=\cot p,Q=\cot q\)); **Casework / exhaustion** for orientation/reflection and algebraic-root branches. The two certified local entries `circle-value-determinant.md` and `circumcentre-linear-certificate.md` are directly reusable.

- Analogous past problems (cruxes): The crux corpus has no geometry crux entries. The closest algebraic analogy is `aimo-0939`: multiply/complete an expression so the given constraint substitutes into a compact product; analogous only to preserving the linear sine brackets and grouping the target by (PFp),(PFq), not to the geometry itself. `aimo-0903`: truncate an ideal-membership question to bounded degree and match the finitely many coefficients; analogous to reducing the target to a \((1,1)\) remainder and checking four coefficients. Neither is genuinely configuration-analogous, so these are technique analogies only.

- Prior progress: Status is partial. The certified circle determinant and circumcentre linear-certificate lemmas correctly reduce the conclusion to
  \[
  2((C-B)\times l)|k|^2+2(k\times(C-B))|l|^2=(k\times l)(b^2-c^2).
  \]
  The ordered-vector translation in `vector-perpendicular-bisector` is also valid. The old trig approach’s ray coordinates \(k=c-re^{-ix}\), \(l=e^{iA}(b-se^{ix})\) remain valid, but its angle sum and incidence equations do not. The corrected equations are (K),(L)/(Fp),(Fq) above.

- Dead ends (do not retry): Do not use \(A+2x+y+z\) as a common angle at either \(K\) or \(L\); direct angle sums give \(A+2x+z\) and \(A+2x+y\). Do not rely on tangent equality alone, because it loses right-angle and supplementary-angle branches. Do not assert that a symbolic ideal calculation certifies the target without printing a checkable identity. Rotation-scale telescoping remains underdetermined because each angle equality introduces unrelated positive scales.

- Small-case / intuition notes: **Numerical evidence only.** For \((A,B,C,x)=(70^\circ,60^\circ,50^\circ,10^\circ)\), the allowed roots are approximately \(p=18.02924^\circ,q=15.73738^\circ\); for the equilateral case with \(x=10^\circ\), symmetry gives \(p=q\approx21.32843^\circ\). The other root of the \(p\)-quadratic in the first example is about \(68.607^\circ>B-x=50^\circ\), and similarly the equilateral second root is about \(68.672^\circ>50^\circ\). This supports, but does not prove, uniqueness of the geometrically admissible root. The symmetric case \(B=C\) also gives \(p=q\), hence \(R=S\), as expected from reflection symmetry.
