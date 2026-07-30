## imo-2026-06

finite-support-maximal-linked: revise
Target: Prove that there exist positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Prime-support reformulation followed by marked-prime infinite descent on the integer radical; this adapts the terminating quantitative descent of `aimo-0030` (and the warning from `aimo-0060` that mere strict change is insufficient), then imports the certified finite-control-to-global-periodicity lemma.
Skeleton:
  1. Import the certified static gcd-polar enumeration, exact-support self-duality, ordered disjoint-witness, and global periodic-enumeration lemmas. Thus it remains only to prove that the self-dual upfamily \(\mathcal U\) is controlled by finitely many primes.
  2. Let \(\mathcal M\) be the inclusion-minimal members of \(\mathcal U\). Every \(H\in\mathcal U\) contains a member of \(\mathcal M\) — by repeatedly deleting primes while positivity remains, which terminates because \(H\) is finite.
  3. Fix arbitrary \(M\in\mathcal M\) and arbitrary marked \(p\in M\). If \(\operatorname{rad}(M\setminus\{p\})\ge a_1\), apply the ordered disjoint-witness lemma to the negative set \(M\setminus\{p\}\). Obtain \(K\in\mathcal U\), disjoint from that set, with \(\operatorname{rad}(K)<\mu(M\setminus\{p\})=\operatorname{rad}(M\setminus\{p\})\). Linkedness with \(M\) forces \(p\in K\).
  4. Choose an inclusion-minimal positive subset \(N\subseteq K\). Since \(N\) must meet \(M\), while \(K\cap M\subseteq\{p\}\), it follows that \(p\in N\). Moreover \(\operatorname{rad}(N)<\operatorname{rad}(M)\). Repeat this operation while the cofactor support after deleting \(p\) has radical at least \(a_1\); the positive integer radical strictly decreases, so the process terminates at a minimal member \(N\ni p\) with \(S=N\setminus\{p\}\) satisfying \(\operatorname{rad}(S)<a_1\).
  5. Bound the marked prime at a terminal state. If \(S=\varnothing\), then \(\{p\}\in\mathcal U\) meets \(\operatorname{supp}(a_1)\), so \(p\mid a_1\). If \(S\ne\varnothing\), minimality makes \(S\notin\mathcal U\); its ordered disjoint witness \(W\in\mathcal U\) has \(W\cap S=\varnothing\) and \(\operatorname{rad}(W)<\mu(S)\). Linkedness of \(W\) and \(N=S\cup\{p\}\) forces \(p\in W\), hence \(p<\mu(S)\).
  6. There are only finitely many finite prime sets \(S\) with \(\operatorname{rad}(S)<a_1\): their radicals are squarefree integers below \(a_1\). Therefore one uniform constant \(B\), the maximum of \(a_1\) and the finitely many \(\mu(S)\), bounds every marked \(p\) in every \(M\in\mathcal M\). Since \(p\) was arbitrary, every minimal member lies in the finite prime set \(P=\{p:p\le B\}\).
  7. Prove finite control: if \(H\in\mathcal U\), a minimal member \(M\subseteq H\) also satisfies \(M\subseteq P\), so \(M\subseteq H\cap P\) and upward closure gives \(H\cap P\in\mathcal U\); conversely, \(H\cap P\in\mathcal U\) implies \(H\in\mathcal U\). This establishes the certified finite-control hypothesis.
  8. Invoke the certified global periodic-enumeration lemma with \(L=\prod_{p\in P}p\) and \(T=|A\cap[a_1,a_1+L)|\), where \(A\) is the static admitted set, to conclude \(a_{n+T}=a_n+L\) for every \(n\ge1\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Marked-prime descent: every prime in a minimal positive support survives into a smaller-radical minimal positive support unless its complementary support already has radical below \(a_1\) — because the ordered witness is disjoint from the complement but linked with the original support, so their only possible common prime is the mark.
  - Exact threshold identity: \(\mu(H)=\operatorname{rad}(H)\) whenever \(\operatorname{rad}(H)\ge a_1\) — because the squarefree radical is the least positive integer with exact support \(H\), and it already lies above the threshold.
  - Terminal bound: for nonempty \(S=N\setminus\{p\}\), one has \(p<\mu(S)\) — because a lower ordered witness disjoint from \(S\) must meet the positive set \(N\), hence must contain \(p\).
  - Finite-controller criterion: if all minimal positive members are subsets of finite \(P\), then \(H\in\mathcal U\iff H\cap P\in\mathcal U\) — because each positive finite \(H\) contains a minimal positive subset.
Open gaps: Steps 3–7 must be written rigorously and checked edge-by-edge; the central mechanism is supplied above, so no conjectural lemma remains. Step 8 should quote, not re-prove, the certified lemma.
Cases to cover: At the terminal state, \(S=\varnothing\) and \(S\ne\varnothing\); during descent, cofactor radical below versus at least \(a_1\).
Watch out for: Do not reuse the failed anchor inference. In particular, never infer disjointness from a trace after enlarging its universe. Also justify that the minimal positive subset of \(K\) still contains \(p\), and do not apply \(\mu\) to the empty set.

bounded-prime-bad-pair: new
Target: Prove that there exist positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Direct arithmetic contradiction using the uniform gap bound, a minimal-span bad pair, and bridge-interval divisibility packing; inspired by the bounded-small-prime upgrade in `aimo-0030`, but avoiding the maximal-linked finite-anchor construction entirely.
Skeleton:
  1. Prove the cheap uniform bound \(a_{n+1}-a_n\le a_1\): the least multiple of \(a_1\) exceeding \(a_n\) is at distance at most \(a_1\) and has nontrivial gcd with every earlier term because each earlier term has nontrivial gcd with \(a_1\).
  2. Set \(P_0=\{p\text{ prime}:p\le a_1\}\). Assume there are two terms with no common prime in \(P_0\), and choose such a pair \(a_i<a_j\) with \(j-i\) minimal, then with \(a_j-a_i\) minimal. Their gcd has a prime divisor \(q>a_1\), so \(a_j-a_i\ge q>a_1\) and the interval contains an intermediate term.
  3. For every \(i<k<j\), minimality of the index span implies that \(a_k\) shares a prime \(p\in P_0\) with \(a_i\) and a prime \(r\in P_0\) with \(a_j\). The endpoint trace sets are disjoint, so \(p\ne r\), and every bridge term is divisible by some product \(pr\) with \(p\mid a_i\), \(r\mid a_j\), \(p,r\le a_1\).
  4. Establish the bridge-packing lemma: under the extra facts that consecutive selected terms are at distance at most \(a_1\), the endpoints are congruent modulo a common \(q>a_1\), and the pair is minimal-span/minimal-distance, an interval cannot have every selected interior integer in the finite union of progressions \(pr\mid m\) with disjoint endpoint prime sets. The intended mechanism is to split the bridge by its first changes of endpoint labels, use that a fixed pair \((p,r)\) has spacing \(pr\), and pigeonhole an adjacent label transition that yields a shorter pair with no common prime in \(P_0\).
  5. The bridge-packing contradiction proves that every two terms share a prime in \(P_0\).
  6. Translate this stronger statement to finite control. For \(H\in\mathcal U\), exact-support realization makes \(H\) a term support, so \(H\cap P_0\) meets every positive support in a prime from \(P_0\); self-duality gives \(H\cap P_0\in\mathcal U\). The converse follows by upward closure.
  7. Invoke the certified global periodic-enumeration lemma with \(P=P_0\) to obtain the required \(T,L\) for every positive index.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Uniform gap bound \(a_{n+1}-a_n\le a_1\) — because the next multiple of \(a_1\) is admissible at every stage.
  - Bridge trace forcing — because each interior-endpoint pair has smaller index span than the extremal bad pair and therefore must share a bounded prime.
  - Bridge-packing lemma — proposed mechanism: label each bridge term by one divisor from each of the disjoint endpoint traces and use spacing of multiples plus extremality to manufacture a shorter bad pair; this is the load-bearing unproved claim and must be tested for counterexamples before use.
  - Bounded pairwise intersection implies finite control — because exact-support realization turns every positive support into an occurring term support.
Open gaps: Step 4 is substantial and presently unproved; the builder must either prove the stated packing lemma with all label-switching cases or record a counterexample and stop. Steps 5–7 are conditional on it.
Cases to cover: Repeated versus changing label pairs \((p,r)\); bridge of one interior term versus at least two; endpoint gcd may have several primes, all exceeding \(a_1\).
Watch out for: A naive density union bound for multiples of \(pr\) is too weak. An intermediate term existing is not itself a contradiction. Do not assume a finite-state description before proving large-prime constraints redundant.

rank-compact-isolation: new
Target: Prove that there exist positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Well-founded induction on the exact-support rank \(\mu\), converted into a Cantor-cube isolation theorem for the positive finite points; this pursues uniform finite character rather than an explicit marked-prime radical bound.
Skeleton:
  1. Import exact-support self-duality and ordered witnesses, and strengthen them to the rank recursion: for every nonempty finite \(H\),
     \[H\notin\mathcal U\iff \exists K\in\mathcal U\ (K\cap H=\varnothing\text{ and }\mu(K)<\mu(H)).\]
     The forward direction uses the ordered term witness and \(\mu(K)\le\operatorname{rad}(a_j)^{e}\) only after choosing the least exact-support realization carefully; the builder should instead use the occurring term support itself and verify directly that its exact-support minimum is below \(\mu(H)\). The reverse direction is linkedness.
  2. For fixed \(H\), only finitely many supports \(K\) satisfy \(\mu(K)<\mu(H)\), since each is the support of an integer in \([a_1,\mu(H))\). Thus membership at each rank is decided by finitely many lower-rank positive supports.
  3. In the Cantor cube \(2^{\mathbb P}\), define \(\mathcal C=\{X:X\cap K\ne\varnothing\text{ for every }K\in\mathcal U\}\). It is closed, and its finite points are exactly \(\mathcal U\).
  4. Prove a uniform isolation lemma from the rank recursion: there is a rank \(R\) such that every finite point of \(\mathcal C\) contains a minimal finite point of rank at most \(R\). The proposed mechanism is a minimal-counterexample chain of new minimal positive supports: each new support has private lower-rank crossing witnesses for all deleted primes; pigeonholing their traces on \(\operatorname{supp}(a_1)\) should either produce an earlier contained positive support or a strict decrease in the maximal private-witness rank.
  5. The finitely many minimal positive supports of rank at most \(R\) have finite union \(P\). The isolation lemma implies every positive finite set contains one of them, hence \(H\in\mathcal U\iff H\cap P\in\mathcal U\).
  6. Apply the certified global periodic-enumeration lemma to this finite \(P\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Pointwise finite-rank recursion — because every negative support is skipped before its least exact-support realization, while supports realized below a fixed integer form a finite set.
  - Uniform isolation lemma — proposed mechanism: private crossing witnesses for every element of a minimal edge create a well-founded rank profile; an infinite sequence of genuinely new minimal edges must force a lexicographic decrease in that profile.
  - Finite isolated basis gives a controller — because an upward-closed family is generated by its inclusion-minimal members.
Open gaps: Step 4 is the entire load-bearing gap and is not supplied by compactness alone. The builder must define the rank profile precisely and prove strict decrease; if pigeonholing only gives pointwise bounds depending on the support, the approach has not advanced.
Cases to cover: Singleton minimal supports; repeated versus new traces on \(\operatorname{supp}(a_1)\); empty deleted support is excluded from \(\mu\) and handled separately.
Watch out for: Closed does not mean clopen, and compactness cannot extract finitely many defining clauses without a proved open cover. Finite subsets of the primes are not well-quasi-ordered by inclusion. Do not reproduce the failed anchor inference or claim that pairwise linkedness gives a triple intersection.
