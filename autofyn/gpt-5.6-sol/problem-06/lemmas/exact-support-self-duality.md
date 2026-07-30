# Exact-support self-duality lemma

For the greedy sequence of IMO 2026/6, write \(E_i=\operatorname{supp}(a_i)\) and
\[
\mathcal U=\{H:H\text{ is a finite prime set and }H\cap E_i\ne\varnothing\text{ for every }i\}.
\]
Then the supports occurring among the terms are exactly the members of \(\mathcal U\), and
\[
H\in\mathcal U\quad\Longleftrightarrow\quad H\cap K\ne\varnothing\text{ for every }K\in\mathcal U.
\]

Every occurring support is in \(\mathcal U\), because every two terms have gcd greater than one (including a term with itself). Conversely, if \(H\in\mathcal U\), then \(H\ne\varnothing\). Put \(r=\prod_{p\in H}p\). For all sufficiently large \(k\), \(r^k\ge a_1\), has support exactly \(H\), and has gcd greater than one with every term. The static gcd-polar lemma therefore makes \(r^k\) a term. Thus occurrence is equivalent to membership in \(\mathcal U\). The displayed equivalence now follows directly from the definition of \(\mathcal U\), with the quantified term supports replaced by all members of \(\mathcal U\).
