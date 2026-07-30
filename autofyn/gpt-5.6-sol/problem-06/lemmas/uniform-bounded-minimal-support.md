# Uniform bounded-minimal-support lemma

Let \(\mathcal U\) be the support upfamily of the greedy sequence in IMO 2026/6 and \(\mathcal M\) its inclusion-minimal members. There is a finite bound \(B\), depending only on \(a_1\), such that every prime in every member of \(\mathcal M\) is at most \(B\).

For each nonempty finite prime set \(S\), let \(\mu(S)\) be the least integer at least \(a_1\) having exact prime support \(S\). This exists because sufficiently large powers of \(\operatorname{rad}(S)\) are eligible. Define
\[
B=\max\left(\{a_1\}\cup
\{\mu(S):S\ne\varnothing,\ \operatorname{rad}(S)<a_1\}\right).
\]
The maximum exists because unique factorization injects the sets \(S\) in the second collection into the finitely many squarefree positive integers below \(a_1\).

Fix \(M\in\mathcal M\) and \(p\in M\). By the marked-prime radical-descent lemma, there is \(N\in\mathcal M\) containing \(p\) such that, for \(S=N\setminus\{p\}\), one has \(\operatorname{rad}(S)<a_1\). If \(S=\varnothing\), then \(N=\{p\}\in\mathcal U\). The occurring support \(E(a_1)\) also belongs to \(\mathcal U\), so exact-support self-duality implies \(\{p\}\cap E(a_1)\ne\varnothing\). Hence \(p\mid a_1\), and \(p\le a_1\le B\).

If \(S\ne\varnothing\), minimality of \(N\) gives \(S\notin\mathcal U\). The ordered disjoint-witness lemma yields \(W\in\mathcal U\) with
\[
W\cap S=\varnothing,
\qquad \operatorname{rad}(W)<\mu(S).
\]
Since \(W,N\in\mathcal U\), self-duality gives \(W\cap N\ne\varnothing\). As \(N=S\cup\{p\}\) and \(W\) avoids \(S\), it follows that \(p\in W\). Therefore
\[
p\le\operatorname{rad}(W)<\mu(S)\le B.
\]
Because \(M\) and \(p\) were arbitrary, the asserted uniform bound follows.