## trig-circle-factorization

**Verdict:** CHANGES REQUESTED  
**True Status:** partial (the builder's recorded status is correct, but its claimed corrected angle equations are not)  
**Scores:** Correctness 4/10; Completeness/rigor 4/10; Progress 5/10.

The load-bearing trigonometric reduction fails at the angle sum in line 27. From the approach's own ray table,
\[
\angle KBC=B-x,\qquad \angle KCB=C-x-z,
\]
so
\[
\angle BKC=\pi-(B-x)-(C-x-z)=A+2x+z.
\]
Likewise,
\[
\angle LBC=B-x-y,\qquad \angle BCL=C-x,
\]
so
\[
\angle BLC=A+2x+y.
\]
They are not both \(A+2x+y+z\). Consequently (2) must have the distinct denominators
\[
BK=a\frac{\sin(C-x-z)}{\sin(A+2x+z)},\qquad
CL=a\frac{\sin(B-x-y)}{\sin(A+2x+y)}.
\]
Thus the sentence claiming the earlier distinct denominators were erroneous is itself erroneous, and the stated elimination system is not implied by the geometry. The formulas (1), the coordinate placement, and the independent circle determinant reduction (3)--(7) are valid, so there is real partial progress. Exact gap: repair (2) and then prove target (7) from the repaired incidence equations; currently no factorization or certificate is supplied.

The flagged Circle-value determinant lemma is certified and admitted as `results/imo-2026-02/lemmas/circle-value-determinant.md`.

**Raw Goal Progress:** status `partial`; ranking snapshot after outcome recording: `{"slug":"trig-circle-factorization","elo":1516.0,"expanded":1,"last_outcome":"partial","last_round":1,"stale":true}`.

## vector-perpendicular-bisector

**Verdict:** CHANGES REQUESTED  
**True Status:** partial (matching the builder's recorded status)  
**Scores:** Correctness 8/10; Completeness/rigor 5/10; Progress 6/10.

I independently re-derived the load-bearing circumcentre certificate. With \(q=2O\), the circle equations give \(q\cdot k=|k|^2\) and \(q\cdot l=|l|^2\), while direct expansion gives
\[
OM=ON\iff q\cdot(c-b)=\frac{|c|^2-|b|^2}{2}.
\]
Cramer's decomposition
\[
c-b=\frac{(c-b)\times l}{k\times l}k+
\frac{k\times(c-b)}{k\times l}l
\]
then reproduces (T), including all signs. The three ordered-vector pairs (E1)--(E3) also match the three ordinary angle hypotheses; retaining a common rotation with positive scale factors is necessary and handles the right-angle branches without division by a dot product.

However, the approach stops exactly before the theorem's substantive step: no proof derives (T) from (E1)--(E3). The assertion that an unpresented symbolic ideal calculation confirms it cannot serve as a proof. Exact gap: provide a hand-checkable algebraic certificate or another rigorous derivation using all three positive-scale/common-angle branch conditions. Until then, this is a correct reduction rather than a solution.

The flagged Circumcentre linear-certificate lemma is certified and admitted as `results/imo-2026-02/lemmas/circumcentre-linear-certificate.md`.

**Raw Goal Progress:** status `partial`; ranking snapshot after outcome recording: `{"slug":"vector-perpendicular-bisector","elo":1484.0,"expanded":1,"last_outcome":"partial","last_round":1,"stale":true}`.

## Overall Goal Progress

`imo-2026-02` remains `partial`. Canonical ranking snapshot: `{"trig-circle-factorization":{"elo":1516.0,"expanded":1,"last_outcome":"partial","stale":true},"vector-perpendicular-bisector":{"elo":1484.0,"expanded":1,"last_outcome":"partial","stale":true}}`.
