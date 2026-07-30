# Static gcd-polar lemma

Let \((a_n)\) satisfy the greedy rule of IMO 2026/6. Then its terms are exactly, in increasing order, the integers
\[
S=\{m\ge a_1:\gcd(m,a_i)>1\text{ for every }i\ge1\}.
\]

Indeed, the terms are strictly increasing. Any two distinct terms have gcd greater than one by the rule at the later term, and each term has gcd greater than one with itself because it exceeds one; hence every term lies in \(S\). Conversely, if \(m\ge a_1\) is not a term, choose the unique \(n\) with \(a_n<m<a_{n+1}\). The minimality of \(a_{n+1}\) means that \(m\) failed the stage-\(n\) admissibility test, so \(\gcd(m,a_i)=1\) for some \(i\le n\). Thus \(m\notin S\).
