## vector-perpendicular-bisector

**Verdict: APPROVE**  
**True Status: solved**  
**Builder-recorded Status: solved — correct.**

**Scores**
- Correctness: 10/10
- Completeness / rigor: 10/10
- Progress: 10/10

The proof answers the stated problem and covers the ordinary-angle branches, right-angle possibilities, positivity, and noncollinearity needed for the circumcentre lemma.

I independently re-derived the load-bearing algebra. From the displayed coordinates I recomputed all eight dot/cross factors in (10) and (15). Before imposing the Pythagorean identities, their differences from the printed factors are multiples of only \(p^2+q^2-1\) or \(g^2+h^2-1\), so (10) and (15) are exact under (7). Expanding the two cross-multiplied angle equations then reproduces exactly
\[
F_2=(b^2+2s^2-2bsp)h-bcq-bsv,
\qquad
F_3=(c^2+2r^2-2crp)h-bcq-crv.
\]
No tangent or dot-product division is used; the only cancelled quantities are positive.

Most importantly, I expanded from scratch
\[
E=hT+P_3F_3+P_2F_2
\]
using the coordinate definitions. Its support in \((r,s)\) is exactly the eight monomials printed in (23), and every one of the eight independently computed coefficients agrees term-for-term with the table after setting \(\Delta=p^2+q^2-1\), \(\Gamma=g^2+h^2-1\). Hence the certificate is valid and gives \(T=0\) because \(h>0\). The certified circumcentre linear-certificate lemma then gives precisely \(OM=ON\).

The ray-order argument is complete: strict interiority gives \(0<x<\angle LBA<B\), so \(q,h>0\), and the first ordinary-angle equality fixes the stated ray directions. Reflection preserves all relevant data. The phrase “circumcentre of triangle \(AKL\)” supplies the necessary noncollinearity.

**Promotable lemma:** admitted as `results/imo-2026-02/lemmas/two-residual-vector-certificate.md`. Its statement is no stronger than the verified polynomial identity and includes the full coefficient certificate.

## four-circle-midpoint-web

**Verdict: APPROVE**  
**True Status: solved**  
**Builder-recorded Status: solved — correct.**

**Scores**
- Correctness: 10/10
- Completeness / rigor: 10/10
- Progress: 10/10

This independent proof also answers the whole problem. I re-solved the two line intersections from the ray directions and obtained
\[
AD=\frac{c\sin x}{\sin(\alpha+x)},\qquad
AE=\frac{b\sin x}{\sin(\alpha+x)},
\]
so the load-bearing product relation \(AB\cdot AE=AC\cdot AD\) is correct, with both auxiliary points finite, nonzero, and on the positive rays. The directed-angle conversions to \((BDLN)\) and \((CEKM)\) are valid modulo \(\pi\).

I independently reconstructed the midpoint-web certificate. In the basis \((\mathbf u,\mathbf v)\), substitution of \(A,P,Q\) gives (8). Substitution of \(C,E,M\) gives (9), and subtracting (8) gives
\[
\frac W2(d(1-s)-t),
\]
whose zero set is exactly \(BD\). The symmetric calculation gives (11), whose difference from (8) is
\[
\frac U2(e(1-t)-s),
\]
with zero set exactly \(CE\). Thus \(K,L\in(APQ)\) and the hard midpoint-web claim is proved, not asserted.

The only possible degeneracies in defining those two circles are exactly \(E=M\) and \(D=N\). In each case the original ordinary-angle equality gives the stated tangent by the tangent–chord converse, and the double-root calculation reproduces the same circle equation. Other possible equalities such as \(E=B\) or \(D=C\) leave three distinct noncollinear defining points and cause no failure. The circle \((APQ)\) is genuine because \(e,d>0\) and the side lines are nonparallel. Finally, the directed-power calculations at \(M,N\) have the correct negative signs and, together with the product relation, imply \(OM^2=ON^2\), hence \(OM=ON\).

**Promotable lemma:** admitted as `results/imo-2026-02/lemmas/four-circle-midpoint-web.md`, with the positivity assumptions actually used and both tangent coincidence branches stated.

## Canonical status

`results/imo-2026-02/current.md` is correctly at **solved** and contains the complete four-circle midpoint-web proof. No downgrade or replacement is needed. Both approaches are independently complete.

## Goal Progress

`imo-2026-02` advanced from `partial` to `solved`. Two independent complete proofs received APPROVE. The vector proof closes the prior dot-cross gap via a fully verified two-residual coefficient identity; the synthetic proof closes the midpoint-web gap via explicit radical-axis equations with both tangent degeneracies handled. Certified lemmas added: `two-residual-vector-certificate` and `four-circle-midpoint-web`. Ranker outcomes for round 2: `vector-perpendicular-bisector = verified-milestone`; `four-circle-midpoint-web = verified-milestone`.
