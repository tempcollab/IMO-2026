# Two-residual vector certificate

Let real numbers \(b,c,r,s,p,q,g,h\) be given, and define
\[
u=gp+hq,\qquad v=hp-gq,
\]
where \(p^2+q^2=g^2+h^2=1\). Put
\[
 B=(c,0),\quad C=(bu,bv),\quad K=(c-rp,rq),\quad L=(bu-sg,bv-sh).
\]
Using \(X\times Y\) for the oriented determinant, define
\[
\begin{aligned}
F_2&=(b^2+2s^2-2bsp)h-bcq-bsv,\\
F_3&=(c^2+2r^2-2crp)h-bcq-crv,\\
T&=2((C-B)\times L)|K|^2+2(K\times(C-B))|L|^2-(K\times L)(b^2-c^2),\\
P_3&=bcv+bsq-csh,\qquad P_2=-bcv+brh-crq.
\end{aligned}
\]
Then
\[
hT+P_3F_3+P_2F_2=0.
\]

For a direct verification, temporarily set
\[
\Delta=p^2+q^2-1,\qquad \Gamma=g^2+h^2-1.
\]
Substitute the coordinates and
\(|K|^2=c^2+r^2-2crp\), \(|L|^2=b^2+s^2-2bsp\) into the left side \(E\), and collect in \(r,s\). The complete list of nonzero formal coefficients is
\[
\begin{array}{c|l}
 r^is^j&[r^is^j]E\\ \hline
 r^2s&-2h(\Delta\Gamma bq+\Delta bq-\Delta ch+\Gamma bq)\\
 r^2&-2\Delta bch(-gq+hp)\\
 rs^2&2h(-\Delta\Gamma bh-\Delta bh-\Gamma bh+\Gamma cq)\\
 rs&4b^2h^2p(\Delta\Gamma+\Delta+\Gamma)\\
 r&-b\bigl(2\Delta^2\Gamma b^2h^2+2\Delta^2b^2h^2+4\Delta\Gamma b^2h^2-2\Delta\Gamma bchq\\
 &\qquad+3\Delta b^2h^2-2\Delta bchq+2\Gamma b^2h^2-2\Gamma bchq+\Gamma c^2q^2\bigr)\\
 s^2&2\Gamma bch(-gq+hp)\\
 s&bc\bigl(-4\Delta\Gamma bh^2-\Delta bh^2+4\Gamma bghpq+4\Gamma bh^2q^2-4\Gamma bh^2+\Gamma bq^2-2\Gamma chq\bigr)\\
 1&2b^3ch(-gq+hp)(\Delta\Gamma+\Delta+\Gamma).
\end{array}
\]
All omitted coefficients are zero by direct multiplication. Since \(\Delta=\Gamma=0\), every coefficient vanishes, proving the identity.
