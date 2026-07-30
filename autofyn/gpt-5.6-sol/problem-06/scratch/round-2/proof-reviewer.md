## `finite-support-maximal-linked`

**Verdict:** APPROVE  
**True Status:** solved  
**Builder's recorded Status:** correct

### Scores
- **Correctness:** 10/10
- **Completeness / rigor:** 10/10
- **Progress:** 10/10

### Review
The candidate proves the original statement for every permitted initial value \(a_1>1\), producing positive integers \(T,L\) with \(a_{n+T}=a_n+L\) for every positive integer \(n\). No case required by the statement is omitted.

The load-bearing new step is the marked-prime descent. I independently re-derived it as follows. For a minimal positive support \(C\) and marked \(p\in C\), if \(\operatorname{rad}(C\setminus\{p\})\ge a_1\), then minimality makes \(C\setminus\{p\}\) negative and its exact-support threshold is precisely its radical. The certified ordered-witness lemma gives positive \(K\) disjoint from \(C\setminus\{p\}\) with smaller radical. Self-duality applied to \(K,C\) forces \(p\in K\). Any minimal positive \(N\subseteq K\) still contains \(p\), because self-duality applied to \(N,C\) forces an intersection while \(N\cap C\subseteq\{p\}\). Finally,
\[
\operatorname{rad}(N)\le\operatorname{rad}(K)<\operatorname{rad}(C\setminus\{p\})<\operatorname{rad}(C),
\]
so well-ordering makes the iteration terminate. This reproduces equations (7)--(11), including preservation of the marked prime, without using the failed round-1 finite-trace inference.

At termination, the proof correctly separates \(S=N\setminus\{p\}=\varnothing\) from \(S\ne\varnothing\). In the first case self-duality with \(E(a_1)\) gives \(p\mid a_1\). In the second, another ordered witness forces \(p<\mu(S)\). There are only finitely many possible nonempty \(S\) with \(\operatorname{rad}(S)<a_1\), so the resulting uniform bound \(B\) is valid. Consequently every minimal member lies in the finite prime set \(P=\{p:p\le B\}\), and both directions of finite control follow from upward closure and finite minimization.

The final enumeration is also exact: divisibility by each prime of \(P\) is invariant under adding \(L=\prod_{p\in P}p\); translation by \(L\) is a bijection of the admitted tail onto the tail beginning at \(a_1+L\); and the half-open block \([a_1,a_1+L)\) contains exactly the positive number \(T\) of terms skipped. Thus translation advances every indexed term by exactly \(T\), including \(n=1\).

### Promotable lemmas
- **Marked-prime radical-descent lemma:** certified and admitted as `results/imo-2026-06/lemmas/marked-prime-radical-descent.md`.
- **Uniform bounded-minimal-support lemma:** certified and admitted as `results/imo-2026-06/lemmas/uniform-bounded-minimal-support.md`.
- **Minimal-basis finite-controller criterion:** certified and admitted as `results/imo-2026-06/lemmas/minimal-basis-finite-controller.md`.

Reviewer-owned `results/imo-2026-06/current.md` was updated to Status `solved` with the approved full proof.