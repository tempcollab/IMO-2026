# Circle-value determinant lemma

Let noncollinear vectors \(k,l\) define a circle through the origin by
\[
|w|^2-q\cdot w=0.
\]
Then, for every vector \(v\),
\[
q\cdot v=\frac{[v,l]|k|^2+[k,v]|l|^2}{[k,l]},
\]
where \([u,v]\) is the oriented determinant.

Indeed, substituting \(k,l\) in the circle equation gives \(q\cdot k=|k|^2\) and \(q\cdot l=|l|^2\). Since \([k,l]\ne0\), Cramer's rule gives
\[
v=\frac{[v,l]}{[k,l]}k+\frac{[k,v]}{[k,l]}l.
\]
Taking the dot product with \(q\) proves the formula.
