# Global periodic enumeration lemma

Let \(\mathcal U\) be the support family associated with the greedy sequence of IMO 2026/6. Suppose there is a finite prime set \(P\) such that, for every finite prime set \(H\),
\[
H\in\mathcal U\iff H\cap P\in\mathcal U.
\]
Then there are positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every \(n\ge1\).

Set \(L=\prod_{p\in P}p\). The hypothesis forces \(P\ne\varnothing\), since \(\varnothing\notin\mathcal U\), so \(L\) is positive. For each prime \(p\in P\), divisibility by \(p\) is unchanged upon adding \(L\). Hence membership of an integer \(m>1\) in
\[
A=\{m>1:\operatorname{supp}(m)\in\mathcal U\}
\]
is unchanged upon translation by \(L\), whenever both integers considered exceed one. Let
\[
T=|A\cap[a_1,a_1+L)|.
\]
This is positive because \(a_1\in A\). Translation by \(L\) is an order-preserving bijection from \(A\cap[a_1,\infty)\) to \(A\cap[a_1+L,\infty)\), and exactly the \(T\) elements in the displayed half-open interval precede its image. By the static gcd-polar lemma, \((a_n)\) is the increasing enumeration of \(A\cap[a_1,\infty)\). Therefore translation advances every term by exactly \(T\) positions: \(a_{n+T}=a_n+L\) for all \(n\ge1\).
