## Status
partial

## Approaches tried
- Synthetic second-intersection and power-of-a-point route — live; it eliminates the circumcentre in one move, but the product identity still needs a concrete similarity or cyclicity proof.

## Current best
Let \(\omega=(AKL)\), and let \(P\ne A\), \(Q\ne A\) be the second intersections of \(AB,AC\) with \(\omega\), using directed lengths. Since \(O\) is the centre of \(\omega\),
\[
OM=ON\iff \operatorname{Pow}_\omega(M)=\operatorname{Pow}_\omega(N)
\iff MA\cdot MP=NA\cdot NQ.
\]
This is the cheap structural reduction, directly adapting the successful crux of `aimo-0266` (where an equal-distance-to-circumcentre target is converted to an equality of side products).

Planned completion: introduce the second intersections \(X\ne K\) of \(MK\) with \(\omega\) and \(Y\ne L\) of \(NL\) with \(\omega\). Use
\[
MK\cdot MX=MA\cdot MP,
\qquad NL\cdot NY=NA\cdot NQ.
\]
It is therefore enough to prove \(MK\cdot MX=NL\cdot NY\). The repeated angles \(\angle BMK=\angle LCK\) and \(\angle LNC=\angle LBK\), together with cyclic angle substitutions through \(A,K,L,X,Y\), should pair two triangles involving \((B,K,X)\) and \((C,L,Y)\). The desired similarity must have scale ratio \(MK/NL\), yielding \(MX/NY=NL/MK\), or equivalently two reciprocal similarities whose scale factors cancel.

A fallback within this synthetic route is to compute \(MP/MQ\) by the sine law in the cyclic quadrilaterals \(AKLP,AKLQ\), then use the midpoint identities \(MA=c/2,NA=b/2\); this remains synthetic trigonometry rather than solving coordinates.

**Open gap:** establish the actual pair of similar triangles (or the exact sine-product identity) and verify the directed-length signs. No unproved visual similarity may be asserted.
