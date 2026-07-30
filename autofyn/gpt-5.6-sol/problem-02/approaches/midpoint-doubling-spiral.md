## Status
partial

## Approaches tried
- Midpoint doubling followed by composition of direct similarities — live; the hypotheses acquire a clean finite-geometric form, but the final spiral-similarity composition has not yet been identified rigorously.

## Current best
Let \(U\) be the image of \(K\) under the dilation of ratio \(2\) centered at \(B\), and let \(V\) be the image of \(L\) under the dilation of ratio \(2\) centered at \(C\). Then \(K\) and \(L\) are the midpoints of \(BU\) and \(CV\). Because those dilations send \(M,N\) to \(A\), the angle hypotheses become
\[
\angle ABU=\angle ACL,
\qquad \angle UBL=\angle VAC,
\qquad \angle VCK=\angle BAU.
\]
This is the finite midpoint symmetry suggested by the factor \(1/2\), and all orientations are fixed by the original interior conditions.

Next dilate the entire plane by ratio \(2\) centered at \(A\). The circle \((AKL)\) becomes the circle
\[
\Gamma=(A,X,Y),\qquad X=2K=B+U,\quad Y=2L=C+V,
\]
and its centre is \(2O\), while \(M,N\) go to \(B,C\). Hence the original conclusion is equivalent to saying that \(B\) and \(C\) have equal powers to \(\Gamma\).

Planned completion: regard the three displayed angle equalities as three oriented direct similarities between the ray pairs \((AB,BU)\), \((BU,BL)\), \((CL,CA)\), and \((CV,CK)\). Compose them, using \(K=(B+U)/2\) and \(L=(C+V)/2\), to obtain the four-ray lemma
\[
\operatorname{Pow}_{(A,B+U,C+V)}(B)=
\operatorname{Pow}_{(A,B+U,C+V)}(C).
\]
The precedent is the midpoint-dilation/spiral-similarity move in `aimo-0705`: doubling should expose a cyclicity or similarity hidden by the two midpoint averages.

**Open gap:** discover and prove the precise spiral centre or companion cyclic quadrilateral realizing the four-ray lemma. A mere restatement as equal powers is not enough; the builder must write the actual composition and track directed orientations.
