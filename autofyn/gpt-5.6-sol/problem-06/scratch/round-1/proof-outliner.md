## imo-2026-06

finite-support-maximal-linked: new
Target: Prove that there are positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Reformulate gcd incidence as intersection of finite prime supports, as in the transferable encoding move of `aimo-0224`; then prove finite generation of the resulting self-dual maximal linked family and finish by CRT periodicity.
Skeleton:
  1. Let \(E(m)\) be the finite set of prime divisors of \(m\), and let \(\mathcal F=\{E(a_n):n\ge1\}\) — by prime-support encoding, the hypothesis says \(\mathcal F\) is linked (pairwise intersecting).
  2. Prove the static-enumeration identity \(\{a_n:n\ge1\}=\{m\ge a_1:E(m)\text{ meets every member of }\mathcal F\}\) — a generated term meets all terms, while any skipped integer already failed a previous term.
  3. Deduce self-duality on all finite prime sets: \(H\in\mathcal F\) (in the upward-closed sense of being the support of some generated integer) iff \(H\) meets every member of \(\mathcal F\) — if \(H\) is a transversal, arbitrarily large integers with exact support \(H\) lie in the static set and hence are generated.
  4. Prove the finite-support lemma: any self-dual linked upfamily of finite subsets of an arbitrary ground set which contains one finite member \(E_1\) is determined by a finite set \(P\); equivalently, it has finitely many inclusion-minimal members, all contained in \(P\) — use a finite witness/decision-tree construction rooted at \(E_1\), where every negative finite set has a positive disjoint witness by self-duality.
  5. Let \(L=\prod_{p\in P}p\). Membership in the static set depends only on divisibility by primes in \(P\), hence only on the residue modulo \(L\), by modular arithmetic and CRT from the knowledge base.
  6. If exactly \(T\) residue classes modulo \(L\) are admitted, translation by \(L\) bijects the admitted integers at least \(a_1\) in order; conclude that the \(T\)-th successor of every \(a_n\) is \(a_n+L\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Static maximality: every integer \(m\ge a_1\) meeting all eventual terms is generated — because if it were skipped between consecutive generated terms, it would have met all terms then present and contradicted greedy minimality.
  - Self-duality: a finite support is positive exactly when it hits every positive support — because every transversal has arbitrarily large numerical realizations with exactly that support, and static maximality forces those realizations into the sequence.
  - Finite-support lemma — because the existing finite positive edge makes the positive/disjoint-witness decision tree finitely branching; the hard task is to show no infinite branch survives self-duality while every set is finite.
  - Periodic enumeration lemma — because a union of \(T\) residue classes modulo \(L\) has exactly \(T\) members in each translated period and translation preserves their order.
Open gaps: Step 4 is unproved and load-bearing. The builder must either close the finite-support theorem rigorously or find a counterexample; a bare compactness or abstract antichain assertion is not acceptable. Steps 2–3 also need careful notation distinguishing supports that literally occur from their upward closure.
Cases to cover: The finite-support lemma must cover all sizes of \(E_1\), including \(|E_1|=1\); the final enumeration must include the initial term, not merely a tail.
Watch out for: Abstract intersecting families such as \(\{p,q_i\}\) show that linkedness alone is insufficient. Do not claim the finite-stage lcm stabilizes. Verify that periodicity on \([a_1,\infty)\) yields the identity for every \(n\).

syndetic-sieve-descent: new
Target: Prove that there are positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Cheap uniform-gap bound followed by an extremal CRT contradiction: infinitely many essential divisibility clauses would create a forbidden interval longer than the allowed gap.
Skeleton:
  1. Put \(R=\operatorname{rad}(a_1)\). For each \(n\), \(a_n+R\) shares with every earlier \(a_i\) a prime dividing both \(a_i\) and \(a_1\); hence \(1\le a_{n+1}-a_n\le R\).
  2. Use the same skipped-integer argument to identify the generated set \(A\) with its static gcd-polar on \([a_1,\infty)\); in particular, \(A\) is \(R\)-syndetic and upward under divisibility (above \(a_1\)).
  3. Replace all terms by squarefree supports and retain only inclusion-minimal supports \(\mathcal C\), since a support containing another imposes no new hitting condition.
  4. Prove the syndetic-sieve termination lemma: an \(R\)-syndetic upward set equal to its gcd-polar has only finitely many essential minimal supports — argue contrapositively, using private witnesses to infinitely many essential supports to choose compatible avoidance congruences whose CRT solution gives \(R\) consecutive integers outside \(A\).
  5. Once \(\mathcal C\) is finite, set \(L\) equal to the product of all primes in its members; the defining finite sieve is periodic modulo \(L\).
  6. Count the admitted residue classes modulo \(L\) as \(T\) and apply ordered periodic enumeration to obtain \(a_{n+T}=a_n+L\) for all \(n\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Uniform gap \(R\) — because each earlier term shares some prime of \(a_1\), and adding \(R\) preserves divisibility by every such prime.
  - Private witnesses for a minimal edge \(E\): for every \(p\in E\), there is a positive support meeting \(E\) only at \(p\) — because \(E\setminus\{p\}\) is negative and self-duality supplies a positive support disjoint from it, while linkedness forces an intersection with \(E\).
  - Syndetic-sieve termination — because infinitely many independent essential clauses should permit CRT placement of a full length-\(R\) forbidden block; this compatibility is the central lemma to prove.
  - Finite sieve periodicity — because each divisibility predicate \(p\mid m\) depends only on \(m\bmod p\), and CRT combines the finitely many predicates.
Open gaps: Step 4, specifically the compatible interval-covering lemma. Avoidance is expressed by residue inequalities, so CRT is not automatic; the builder must produce actual compatible residues, not a density heuristic.
Cases to cover: Essential supports meeting \(E_1\) in different primes; repeated primes among private witnesses; \(R=2\) and singleton \(E_1\).
Watch out for: Syndeticity alone does not imply periodicity, and density zero does not by itself exhibit an interval of length \(R\). This approach is independent of the abstract finite-support theorem only if the interval contradiction is proved directly.

translated-first-disagreement: new
Target: Prove that there are positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Extremal comparison of translated bounded-length blocks, enlarging the proposed translation whenever the first disagreement reveals a new prime; this adapts the finite-state/least-obstruction philosophy of `aimo-0678` without assuming finite memory.
Skeleton:
  1. Establish \(a_{n+1}-a_n\le R=\operatorname{rad}(a_1)\); moreover any prime shared by consecutive terms divides their gap and is therefore at most \(R\).
  2. Encode each interval of length \(R\) by occupied positions together with a chosen small-prime witness for each consecutive adjacency; this supplies a finite local alphabet, though not yet a complete state.
  3. Choose a finite guard block and a translation \(L\) divisible by \(R\) and all primes appearing in that guard. Compare the generated/static membership patterns in blocks separated by \(L\), and take the least disagreement.
  4. Show that the rejected translated candidate has an earlier witness term sharing only a prime \(q\nmid L\) relevant to the disagreement; all witnesses dividing \(L\) would be translation-invariant and could not create the first disagreement.
  5. Enlarge \(L\) by \(q\), extend the guard minimally, and prove a monovariant termination lemma: charge \(q\) to a bounded local adjacency/type and show each charge either is unique or strictly decreases the first-disagreement datum.
  6. At termination, translation by \(L\) preserves the whole static set on \([a_1,\infty)\). Let \(T\) be the number of generated terms in one length-\(L\) block; ordered translation gives the desired identity for every index.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Finite adjacency alphabet — because a consecutive gcd witness divides the gap, and every gap is in \(\{1,\ldots,R\}\).
  - New-prime exposure at first disagreement — because translating by a multiple of a witness prime preserves divisibility of corresponding candidates.
  - Termination of translation enlargement — proposed mechanism: a new large witness must be connected through its earlier carrier to one of finitely many small-prime adjacencies; minimal disagreement must make this connection injective or monovariant.
  - Global translation implies indexed translation — because every interval of length \(L\) then has the same finite ordered pattern.
Open gaps: Steps 4–5. In particular, a rejection witness can be a large prime unrelated to the immediately adjacent gcd witness. The builder must prove the charging map and may not use transitivity of gcd.
Cases to cover: Disagreement caused by acceptance on the left/rejection on the right and the reverse; witnesses before the guard block; boundary positions between adjacent length-\(R\) blocks.
Watch out for: A finite gap alphabet is not finite memory. `aimo-0678` transfers only after its bounded-obstruction step; reproducing that missing step here is essential. Also prove translation from the initial block, not merely eventually.

initial-prime-branch-induction: new
Target: Prove that there are positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for every positive integer \(n\).
Technique: Structural induction on traces inside the finite initial prime support, decomposing the static admissible set into finitely many candidate types and proving each branch periodic.
Skeleton:
  1. Let \(P=E(a_1)\). Every generated support meets \(P\), and every candidate has one of the finitely many nonempty traces \(Q=E(m)\cap P\).
  2. For fixed \(Q\), all constraints whose \(P\)-trace meets \(Q\) are automatic; only supports disjoint from \(Q\) inside \(P\) impose outside-prime conditions, and each such residual support meets the strictly smaller set \(P\setminus Q\).
  3. Prove the base \(|P|=1\): if \(P=\{p\}\), every generated term is divisible by \(p\), and the smallest admissible successor is the next multiple of \(p\), so \((T,L)=(1,p)\).
  4. Establish a branch-normalization lemma: for each nonempty \(Q\subseteq P\), candidates of exact trace \(Q\) that survive all residual constraints can be represented as a normalized greedy process with control set contained in \(P\setminus Q\), or by an equivalent static maximal-linked family with a strictly smaller finite anchor.
  5. Apply induction to each nonempty branch; each branch is empty above some point or is a finite union of residue classes modulo a finite modulus.
  6. Take a common multiple \(L\) of the finitely many branch moduli and include any finite exceptional prefix into the translation analysis. Use static maximality to rule out a genuine exceptional prefix, then count admitted classes to get \(T\) and the identity for every \(n\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Finite trace decomposition — because every term must contain at least one prime from the fixed finite support of \(a_1\).
  - Residual-anchor decrease — because a constraint not automatically hit by \(Q\) must meet \(P\setminus Q\), which has fewer primes than \(P\).
  - Branch normalization — intended mechanism: pass to exact-trace candidates and delete automatic \(Q\)-divisibility clauses while preserving the static polar relation; this preservation must be proved.
  - Prefix removal — because the original greedy set is already a static polar on the entire half-line starting at \(a_1\), so any common branch period should act from that boundary.
Open gaps: Step 4 is unproved and may fail for the naive subsequence: fixed-trace terms are not automatically greedy among themselves, and deleting \(Q\) can destroy pairwise intersection. Step 6 must not hide a transient.
Cases to cover: Every nonempty \(Q\subseteq P\), including \(Q=P\); empty versus infinite branch; singleton base; branch moduli sharing primes.
Watch out for: Do not present induction until a genuinely smaller process satisfying the same hypotheses is defined. This route is farthest from the leading finite-clutter route but also the most speculative.
