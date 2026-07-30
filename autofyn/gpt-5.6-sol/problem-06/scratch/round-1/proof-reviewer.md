## finite-support-maximal-linked

**Verdict:** CHANGES REQUESTED  
**True Status:** partial  
**Builder-recorded Status:** partial — the status is correct, but the account of what the finite-anchor construction proves contains an additional logical error.

### Scores
- **Correctness:** 7/10. The four stated reductions are essentially valid, but the discussion at lines 46–50 wrongly claims a selected witness is disjoint from the truncated set.
- **Completeness / rigor:** 5/10. The theorem's load-bearing finite-control lemma (3) is explicitly unproved, so this is not a solution.
- **Progress:** 7/10. It gives a useful static reformulation, self-duality, an ordered numerical witness, and a complete conditional route from finite control to the required global identity.

### Adversarial verification

The actual problem asks for positive integers \(T,L\) such that \(a_{n+T}=a_n+L\) for **every** positive integer \(n\). The candidate does not prove their existence because it assumes the central finite-control statement
\[
H\in\mathcal U\iff H\cap P\in\mathcal U
\]
for some finite prime set \(P\).

I independently re-derived the load-bearing established reduction. If \(m\ge a_1\) is skipped, choose \(n\) with \(a_n<m<a_{n+1}\). Minimality of \(a_{n+1}\) forces \(\gcd(m,a_i)=1\) for some \(i\le n\); conversely every term has nontrivial gcd with every term. Thus the terms are exactly the increasing enumeration of the static gcd-polar. Direct computation for starts \(2\le a_1\le15\), through 40 generated terms, found no mismatch between generated membership and this static criterion on the tested range.

From this static identity, exact-support realization is valid: if finite \(H\) meets every term support, sufficiently large powers of \(\prod_{p\in H}p\) lie in the static polar and become terms. This gives the stated self-duality. The ordered witness argument is also valid: the least integer \(\mu(H)\) with a negative exact support is skipped and therefore has a coprime earlier term. Finally, assuming finite control, divisibility by each \(p\in P\) is invariant modulo \(L=\prod_{p\in P}p\), and the half-open interval count correctly proves the indexed identity from \(n=1\), not merely eventually.

### Precise gap and error

The exact missing step is existence of a finite controlling prime set \(P\). Self-duality of an arbitrary family of finite sets does not supply this.

There is also a concrete false implication in the candidate's attempted finite-anchor analysis. It chooses \(B_A\in\mathcal U\) disjoint from \(A\subseteq E\), defines
\[
P=E\cup\bigcup B_A,
\]
and, for negative \(H\), sets \(A=H\cap E\). From \(B_A\cap A=\varnothing\) one cannot conclude that \(B_A\cap(H\cap P)=\varnothing\): \(H\) may contain primes of \(B_A\setminus E\). Therefore even the claimed negative-direction implication of this one-stage construction has not been proved. The next revision must either choose witnesses guaranteed disjoint from the whole \(H\)-trace relevant to \(P\), or replace this construction and use the ordered bound \(\operatorname{rad}(a_j)<\mu(H)\) in a genuine terminating argument.

### Promotable lemmas

Certified and admitted into `results/imo-2026-06/lemmas/`:
- `static-gcd-polar.md`
- `exact-support-self-duality.md`
- `ordered-disjoint-witness.md`
- `global-periodic-enumeration.md` (explicitly conditional on finite control)

Each certified statement is no stronger than what was proved. None resolves the finite-control gap.

### Raw Goal Progress

`imo-2026-06`: **partial**. Verified static gcd-polar enumeration, exact-support realization/self-duality, an ordered disjoint witness below \(\mu(H)\), and finite-control \(\Rightarrow\) global periodic indexing. Remaining load-bearing gap: prove a finite controlling prime set exists. The proposed finite-anchor construction additionally fails in its alleged negative direction because \(B_A\cap A=\varnothing\) does not imply \(B_A\cap(H\cap P)=\varnothing\). Round-1 outcome recorded as `partial`; verdict `CHANGES REQUESTED`.
