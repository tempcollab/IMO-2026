# Marked-prime radical-descent lemma

Let \(\mathcal U\) be the support upfamily of the greedy sequence in IMO 2026/6, and let \(\mathcal M\) be its inclusion-minimal members. Fix \(C\in\mathcal M\) and \(p\in C\). There is \(N\in\mathcal M\) such that \(p\in N\) and
\[
\operatorname{rad}(N\setminus\{p\})<a_1.
\]
Moreover, \(N\) is reached by finitely many replacements that preserve \(p\) and strictly decrease the radical of the whole support.

Suppose a current \(C\in\mathcal M\), containing \(p\), satisfies \(\operatorname{rad}(C\setminus\{p\})\ge a_1\). Then \(H=C\setminus\{p\}\) is nonempty and is not in \(\mathcal U\), by the minimality of \(C\). Its least integer at least \(a_1\) with exact support \(H\) is \(\operatorname{rad}(H)\). The ordered disjoint-witness lemma therefore supplies \(K\in\mathcal U\) such that
\[
K\cap H=\varnothing,
\qquad \operatorname{rad}(K)<\operatorname{rad}(H).
\]
The exact-support self-duality lemma says that any two members of \(\mathcal U\) intersect. Thus \(K\cap C\ne\varnothing\), and because \(K\) avoids \(C\setminus\{p\}\), this forces \(p\in K\).

Delete elements from the finite set \(K\), while preserving membership in \(\mathcal U\), until obtaining an inclusion-minimal \(C'\in\mathcal M\) contained in \(K\). Again self-duality gives \(C'\cap C\ne\varnothing\), while \(C'\cap C\subseteq K\cap C\subseteq\{p\}\). Hence \(p\in C'\). Also
\[
\operatorname{rad}(C')\le\operatorname{rad}(K)
<\operatorname{rad}(C\setminus\{p\})
<\operatorname{rad}(C).
\]
Replace \(C\) by \(C'\) and repeat. The positive integer \(\operatorname{rad}(C)\) strictly decreases at every replacement, so the process terminates by well-ordering. At its terminal member \(N\), the replacement condition fails, giving \(\operatorname{rad}(N\setminus\{p\})<a_1\), while the marked prime \(p\) has been preserved throughout.