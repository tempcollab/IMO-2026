# Four-circle midpoint-web radical-axis lemma

Let two nonparallel lines through \(A\) contain points \(B,E\) and \(C,D\), respectively, and suppose the directed products satisfy
\[
AB\cdot AE=AC\cdot AD.
\]
Suppose moreover that \(D\) and \(E\) lie on the positive rays \(AC\) and \(AB\). Let \(M,N,P,Q\) be the midpoints of \(AB,AC,BE,CD\), respectively. If \(K\in BD\cap(CEM)\) and \(L\in CE\cap(BDN)\), where when \(E=M\) the circle through \(C,M,K\) is tangent to \(AB\) at \(M\), and when \(D=N\) the circle through \(B,N,L\) is tangent to \(AC\) at \(N\), then
\[
A,K,L,P,Q
\]
are concyclic.

Take \(A\) as origin and write \(B=\mathbf u\), \(C=\mathbf v\), where \(\mathbf u,\mathbf v\) form a basis. Put \(U=|\mathbf u|^2\), \(W=|\mathbf v|^2\), \(E=e\mathbf u\), and \(D=d\mathbf v\). The product hypothesis is \(Ue=Wd\), and
\[
M=\tfrac12\mathbf u,\quad N=\tfrac12\mathbf v,\quad
P=\tfrac{1+e}{2}\mathbf u,\quad Q=\tfrac{1+d}{2}\mathbf v.
\]
Writing \(X=s\mathbf u+t\mathbf v\), the circle \(\Gamma=(APQ)\) has equation
\[
|X|^2-U\frac{1+e}{2}s-W\frac{1+d}{2}t=0. \tag{1}
\]
The circle through \(C,E,M,K\) has equation
\[
|X|^2-U\left(e+\frac12\right)s-\left(W+\frac{Ue}{2}\right)t+\frac{Ue}{2}=0. \tag{2}
\]
If \(e=1/2\), (2) follows instead from the tangent condition: its restriction to \(AB\) must be \(U(s-1/2)^2\). Subtracting (1) from (2) and using \(Ue=Wd\) gives
\[
\frac W2\bigl(d(1-s)-t\bigr),
\]
whose zero set is precisely \(BD\). Thus \(K\in\Gamma\).

Similarly, the circle through \(B,D,N,L\) has equation
\[
|X|^2-\left(U+\frac{Wd}{2}\right)s-W\left(d+\frac12\right)t+\frac{Wd}{2}=0. \tag{3}
\]
For \(d=1/2\), the same equation follows from tangency to \(AC\) at \(N\). Subtracting (1) from (3) gives
\[
\frac U2\bigl(e(1-t)-s\bigr),
\]
whose zero set is precisely \(CE\). Hence \(L\in\Gamma\), proving the claim.
