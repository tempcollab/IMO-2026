# Circumcentre linear-certificate lemma

Let \(A=0\), let \(K,L\) have linearly independent position vectors \(k,l\), and let \(B,C\) have position vectors \(b,c\). If \(O\) is the circumcentre of \(AKL\), while \(M=b/2\) and \(N=c/2\), then \(OM=ON\) is equivalent to
\[
2((c-b)\times l)|k|^2+2(k\times(c-b))|l|^2
=(k\times l)(|c|^2-|b|^2).
\]

Write \(q=2O\). The circle through the origin has equation \(|x|^2-q\cdot x=0\), so
\[
q\cdot k=|k|^2,\qquad q\cdot l=|l|^2.
\]
Expanding squared distances gives
\[
OM^2-ON^2=\frac14\bigl(-2q\cdot b+|b|^2+2q\cdot c-|c|^2\bigr),
\]
so \(OM=ON\) is equivalent to
\[
q\cdot(c-b)=\frac{|c|^2-|b|^2}{2}.
\]
Because \(k\times l\ne0\), Cramer's rule gives
\[
c-b=\frac{(c-b)\times l}{k\times l}k+
\frac{k\times(c-b)}{k\times l}l.
\]
Dotting with \(q\), using the two circle equations, and clearing \(2(k\times l)\) yields the asserted identity. Every step is reversible.
