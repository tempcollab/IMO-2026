## Status
solved

## Approaches tried
- Prime-support maximal-linked route — the static gcd-polar reduction, self-duality, and the eventual-to-global enumeration step were proved rigorously in round 1, but the proposed finite-anchor argument did not prove its load-bearing first implication.
- Finite-trace witness construction rooted at \(E(a_1)\) — choosing one positive set disjoint from every negative trace gives a finite set of witnesses, but does not show that intersecting those witnesses is sufficient to intersect every positive support; this route was abandoned rather than used.
- Marked-prime strict radical descent — worked: preserving an arbitrary marked prime while strictly decreasing the radical reaches a bounded terminal complement, uniformly bounds every prime in every minimal positive support, and hence supplies a finite controller.

## Current best
The problem is solved. The key new point is the marked-prime descent: if \(M\) is an inclusion-minimal member of the support upfamily and \(p\in M\), then, unless \(\operatorname{rad}(M\setminus\{p\})<a_1\), the ordered disjoint-witness lemma replaces \(M\) by another minimal positive support containing the same marked prime \(p\) and having strictly smaller radical. At termination the complementary support has radical below \(a_1\), which bounds \(p\) by one of finitely many exact-support thresholds. Thus all minimal positive supports lie in one finite set of primes, giving finite control and then global indexed periodicity.

## Full proof
For an integer \(m>1\), write
\[
E(m)=\{p:p\text{ is prime and }p\mid m\}.
\]
For a finite set \(H\) of primes, put
\[
\operatorname{rad}(H)=\prod_{p\in H}p,
\]
with the convention \(\operatorname{rad}(\varnothing)=1\). This convention will be used only in a stopping condition; no exact-support minimum will be assigned to the empty set.

Define the upfamily
\[
\mathcal U=\{H:H\text{ is a finite set of primes and }H\cap E(a_i)\ne\varnothing
\text{ for every }i\ge 1\}.
\]
We use the four certified lemmas established for this problem.

1. By the **Static gcd-polar lemma**, the terms \(a_i\) are exactly, in increasing order, the integers \(m\ge a_1\) satisfying \(\gcd(m,a_i)>1\) for every \(i\ge1\).
2. By the **Exact-support self-duality lemma**, the supports occurring among the terms are exactly the members of \(\mathcal U\), and, for every finite prime set \(H\),
   \[
   H\in\mathcal U\quad\Longleftrightarrow\quad
   H\cap K\ne\varnothing\text{ for every }K\in\mathcal U. \tag{1}
   \]
3. By the **Ordered disjoint-witness lemma**, if \(H\ne\varnothing\) and \(H\notin\mathcal U\), and if
   \[
   \mu(H)=\min\{m\ge a_1:E(m)=H\},
   \]
   then there is a term \(a_j<\mu(H)\) whose support is disjoint from \(H\). In particular, with \(K=E(a_j)\),
   \[
   K\in\mathcal U,\qquad K\cap H=\varnothing,
   \qquad \operatorname{rad}(K)\le a_j<\mu(H). \tag{2}
   \]
4. By the **Global periodic enumeration lemma**, it is enough to find a finite set \(P\) of primes such that
   \[
   H\in\mathcal U\quad\Longleftrightarrow\quad H\cap P\in\mathcal U
   \tag{3}
   \]
   for every finite prime set \(H\).

The prime-support reformulation behind these lemmas is the **Reformulate** method together with **Divisor analysis** from `knowledge_base.md`: two positive integers have gcd greater than \(1\) exactly when their prime supports intersect. We now prove the missing finite-control statement (3).

First observe that \(\mathcal U\) is upward closed: if \(H\in\mathcal U\) and \(H\subseteq H'\), then every term support meeting \(H\) also meets \(H'\), so \(H'\in\mathcal U\). Every \(H\in\mathcal U\) contains an inclusion-minimal member of \(\mathcal U\). Indeed, starting from \(H\), delete a prime whenever the resulting set is still in \(\mathcal U\). Since \(H\) is finite, after finitely many deletions the process stops at an inclusion-minimal member. Let \(\mathcal M\) denote the family of these inclusion-minimal members. Notice that \(\varnothing\notin\mathcal U\), since it does not meet \(E(a_1)\); hence every member of \(\mathcal M\) is nonempty.

We next establish a uniform bound for every prime appearing in a member of \(\mathcal M\). Fix an arbitrary \(M\in\mathcal M\) and mark an arbitrary prime \(p\in M\). We shall repeatedly replace the current minimal support by a smaller-radical minimal support while retaining this same marked prime.

Suppose the current support is \(C\in\mathcal M\), with \(p\in C\), and suppose
\[
\operatorname{rad}(C\setminus\{p\})\ge a_1. \tag{4}
\]
The set \(C\setminus\{p\}\) is a proper subset of the inclusion-minimal positive set \(C\), so
\[
C\setminus\{p\}\notin\mathcal U. \tag{5}
\]
It is nonempty under (4), because \(a_1>1\) whereas \(\operatorname{rad}(\varnothing)=1\).

We also have the exact threshold identity
\[
\mu(C\setminus\{p\})=
\operatorname{rad}(C\setminus\{p\}). \tag{6}
\]
To justify it, every positive integer having exact support \(C\setminus\{p\}\) is divisible by each prime in that set, hence is divisible by their product and is at least its radical. Conversely, the radical itself has exact support \(C\setminus\{p\}\), and by (4) it is at least \(a_1\). It is therefore the least eligible integer in the definition of \(\mu\).

Apply the Ordered disjoint-witness lemma to \(C\setminus\{p\}\). Equations (2) and (6) give a set \(K\in\mathcal U\) such that
\[
K\cap(C\setminus\{p\})=\varnothing,
\qquad
\operatorname{rad}(K)<
\operatorname{rad}(C\setminus\{p\}). \tag{7}
\]
Both \(K\) and \(C\) belong to \(\mathcal U\), so the forward implication of (1) says that they intersect. Because (7) excludes every element of \(C\) other than possibly \(p\), this intersection forces
\[
p\in K. \tag{8}
\]

Choose an inclusion-minimal member \(N\in\mathcal M\) contained in \(K\), using the finite deletion procedure above. We must check that minimization has not discarded the marked prime. Since \(N,C\in\mathcal U\), equation (1) gives \(N\cap C\ne\varnothing\). On the other hand,
\[
N\cap C\subseteq K\cap C\subseteq\{p\}
\]
by \(N\subseteq K\) and (7). Thus \(N\cap C=\{p\}\), and in particular
\[
p\in N. \tag{9}
\]
Furthermore, because \(N\subseteq K\),
\[
\operatorname{rad}(N)
\le \operatorname{rad}(K)
<\operatorname{rad}(C\setminus\{p\})
<\operatorname{rad}(C). \tag{10}
\]
The last strict inequality holds because
\(\operatorname{rad}(C)=p\operatorname{rad}(C\setminus\{p\})\) and \(p>1\).

We now replace \(C\) by \(N\), retaining the same marked prime \(p\), and repeat whenever (4) holds for the new current support. At every replacement, the radical of the current support is a strictly smaller positive integer by (10). The **Infinite descent / monovariant principle** from `knowledge_base.md` therefore ensures that this process terminates. More explicitly, an infinite iteration would produce an infinite strictly decreasing sequence of positive integers
\(\operatorname{rad}(C)\), which is impossible by well-ordering. Hence it ends at some \(N\in\mathcal M\), still containing the original marked prime \(p\), for which, on writing
\[
S=N\setminus\{p\},
\]
we have
\[
\operatorname{rad}(S)<a_1. \tag{11}
\]

We bound \(p\) at this terminal state, separating the two exhaustive cases.

If \(S=\varnothing\), then \(N=\{p\}\in\mathcal U\). Also \(E(a_1)\in\mathcal U\), because it is an occurring term support. By (1), \(\{p\}\cap E(a_1)\ne\varnothing\), so \(p\mid a_1\). In particular,
\[
p\le a_1. \tag{12}
\]

Now suppose \(S\ne\varnothing\). Since \(S\) is a proper subset of the minimal member \(N\), we have \(S\notin\mathcal U\). The number \(\mu(S)\) exists: powers of \(\operatorname{rad}(S)\) have exact support \(S\) and eventually exceed \(a_1\). Apply the Ordered disjoint-witness lemma to this nonempty negative set \(S\). It yields \(W\in\mathcal U\) satisfying
\[
W\cap S=\varnothing,
\qquad
\operatorname{rad}(W)<\mu(S). \tag{13}
\]
Because \(W,N\in\mathcal U\), equation (1) gives \(W\cap N\ne\varnothing\). But \(N=S\cup\{p\}\), and (13) excludes intersection with \(S\). Consequently \(p\in W\), and therefore
\[
p\le\operatorname{rad}(W)<\mu(S). \tag{14}
\]
This completes both terminal cases. In particular, we never invoke \(\mu(\varnothing)\).

There are only finitely many nonempty finite prime sets \(S\) satisfying \(\operatorname{rad}(S)<a_1\). Indeed, the map \(S\mapsto\operatorname{rad}(S)\) is injective by unique prime factorization, and its values are squarefree positive integers below \(a_1\), of which there are finitely many. For every such nonempty \(S\), the integer \(\mu(S)\) exists as shown above. Thus the integer
\[
B=
\max\Bigl(\{a_1\}\cup
\{\mu(S):S\ne\varnothing,\ S\text{ a finite prime set},\
\operatorname{rad}(S)<a_1\}\Bigr) \tag{15}
\]
is well-defined; the set in the maximum is finite and nonempty because it contains \(a_1\).

The original choices of \(M\in\mathcal M\) and \(p\in M\) were arbitrary. The descent preserved that same \(p\) all the way to the terminal support. Equation (12) in the empty-complement case and equation (14) together with (15) in the nonempty-complement case show in all cases that
\[
p\le B. \tag{16}
\]
Therefore every member of \(\mathcal M\) is contained in the finite prime set
\[
P=\{p:p\text{ is prime and }p\le B\}. \tag{17}
\]

We now verify both directions of finite control. Let \(H\) be any finite prime set. If \(H\in\mathcal U\), choose a minimal member \(M\in\mathcal M\) with \(M\subseteq H\). By (17), \(M\subseteq P\), and hence
\[
M\subseteq H\cap P.
\]
Since \(M\in\mathcal U\) and \(\mathcal U\) is upward closed, this implies \(H\cap P\in\mathcal U\). Conversely, if \(H\cap P\in\mathcal U\), then \(H\in\mathcal U\) by upward closure because \(H\cap P\subseteq H\). Thus (3) holds.

For completeness, apply the Global periodic enumeration lemma with this finite controller \(P\). It gives the explicit choices
\[
L=\prod_{p\in P}p,
\qquad
T=\left|A\cap[a_1,a_1+L)\right|,
\quad
A=\{m>1:E(m)\in\mathcal U\}. \tag{18}
\]
Here \(P\ne\varnothing\): otherwise (3) applied to \(E(a_1)\in\mathcal U\) would imply \(\varnothing\in\mathcal U\), which is false. Hence \(L\) is a positive integer, and \(T>0\) because \(a_1\in A\).

To spell out the final application, for each \(p\in P\), the congruence \(m+L\equiv m\pmod p\) shows that \(p\mid m+L\) exactly when \(p\mid m\). Therefore (3) makes membership in \(A\) invariant under translation by \(L\), whenever both integers are positive. Translation by \(L\) is consequently an order-preserving bijection
\[
A\cap[a_1,\infty)\longrightarrow A\cap[a_1+L,\infty).
\]
Exactly the \(T\) elements of \(A\cap[a_1,a_1+L)\) precede the image. By the Static gcd-polar lemma, \((a_n)\) is the increasing enumeration of \(A\cap[a_1,\infty)\), so translation advances each term by exactly \(T\) places. Hence
\[
a_{n+T}=a_n+L
\]
for every positive integer \(n\), as required. \(\square\)

## Promotable lemmas
- **Marked-prime radical-descent lemma.** Let \(\mathcal U\) be the support upfamily of this greedy sequence and \(\mathcal M\) its inclusion-minimal members. For every \(M\in\mathcal M\) and \(p\in M\), repeated use of the ordered disjoint-witness lemma produces a terminal \(N\in\mathcal M\) containing the same \(p\), with \(\operatorname{rad}(N\setminus\{p\})<a_1\); each nonterminal replacement strictly decreases the whole-support radical. Proved in the descent beginning after equation (4) and ending at equation (11).
- **Uniform bounded-minimal-support lemma.** Every prime in every inclusion-minimal member of \(\mathcal U\) is at most the finite constant \(B\) in (15). Proved by the two terminal cases (12) and (14), followed by the finiteness argument through (16).
- **Minimal-basis finite-controller criterion.** If every inclusion-minimal member of an upward-closed family of finite sets lies in one finite set \(P\), then \(H\) belongs to the family exactly when \(H\cap P\) does. Proved in the paragraph following (17).
