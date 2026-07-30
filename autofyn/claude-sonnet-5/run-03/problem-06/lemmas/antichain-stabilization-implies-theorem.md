## Lemma (Antichain Stabilization $\Rightarrow$ full theorem, $P'$-enlargement Master Lemma)

**Statement.** Let $(a_n)_{n\ge1}$ be the greedy sequence of imo-2026-06, $S:=\mathrm{primes}(a_1)$,
$L_0:=\mathrm{rad}(a_1)$, $P:=\{p\text{ prime}:p\le L_0\}\supseteq S$, $D_i:=\mathrm{primes}(a_i)$,
and $\mathcal A_n$ the antichain of inclusion-minimal elements of $\{D_1,\dots,D_n\}$.

Suppose **Antichain Stabilization** holds: there exists $N^*$ with $\mathcal A_n=\mathcal
A_{N^*}=:\mathcal A^\infty$ (a finite antichain) for all $n\ge N^*$. Then there exist positive
integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge1$.

Note: this is **strictly weaker as a hypothesis** than "P-Confinement relative to the fixed
$P=\{p\le L_0\}$" (`lemmas/pc-implies-theorem.md`) — Antichain Stabilization alone, with no
constraint that $\mathcal A^\infty$'s primes stay inside the specific fixed $P$, already suffices.

**Proof.** Let $P':=P\cup\bigcup_{B\in\mathcal A^\infty}B$, finite (finite union of finite sets) and
$\supseteq P\supseteq S$. Apply `lemmas/signature-stabilization-and-crt-sufficiency.md` (Lemmas A/B,
generic in any finite prime set $\supseteq S$) with $P_0=P'$: obtain $N_1'$ and a fixed
$R'\subseteq2^{P'}\setminus\{\emptyset\}$ with $R_n^{P'}=R'$ for all $n\ge N_1'$, and
$G'\subseteq\mathbb Z/L_{P'}\mathbb Z$ (nonempty, $0\in G'$) such that for $n\ge N_1'$,
$y_{n+1}:=\min\{x>a_n:x\bmod L_{P'}\in G'\}$ satisfies $a_{n+1}\le y_{n+1}$.

Let $N^{**}:=\max(N^*,N_1')$. For $n\ge N^{**}$, $\mathcal A_n=\mathcal A^\infty$ and every
$B\in\mathcal A^\infty$ satisfies $B\subseteq P'$ by construction of $P'$ — i.e. **PC holds relative
to $P'$** for every generator index realizing $\mathcal A_n$, $n\ge N^{**}$.

Re-run Steps A–D of `lemmas/pc-implies-theorem.md` verbatim with $P$ replaced by $P'$ and $N_1$
replaced by $N^{**}$ (that proof is generic in the finite prime set, given PC and $N_1$-stabilization
relative to it — both hold here by construction):
- Step A: $\mathcal A_n=\min(R_n^{P'})$ for $n\ge N^{**}$ (truncation by $P'$ fixes every
  $B\in\mathcal A_n$ pointwise since $B\subseteq P'$).
- Step B: for $n\ge N^{**}$, $x\bmod L_{P'}\in G'\iff \pi'(x)\cap B\ne\emptyset\ \forall B\in\mathcal
  A_n$, where $\pi'(x):=P'\cap\mathrm{primes}(x)$.
- Step C: since $B\subseteq P'$ for every $B\in\mathcal A_n$, $\pi'(x)\cap B=\mathrm{primes}(x)\cap
  B$, so the residue condition is equivalent to true validity $\gcd(x,a_i)>1\ \forall i\le n$ (via
  Constraint Domination extending from generators to all indices).
- Step D (No-Escape relative to $P'$): for $a_n<x<y_{n+1}$, minimality of $y_{n+1}$ gives
  $x\bmod L_{P'}\notin G'$, hence $x$ invalid; combined with $a_{n+1}\le y_{n+1}$ and validity of
  $a_{n+1}$, $a_{n+1}=y_{n+1}$ for all $n\ge N^{**}$.

By `lemmas/periodicity-given-no-escape.md` (generic in any finite $P_0$; its proof body — verified
directly, not merely by hypothesis list — never uses $S\subseteq P_0$, only "$P_0$ finite, $G_0$
nonempty, $a_{n+1}=y_{n+1}$ for $n\ge N_1$"; here that also happens to hold with $P'\supseteq S$
automatically by construction), No-Escape relative to $P'$ for $n\ge N^{**}$ gives $T,L\ge1$ with
$a_{n+T}=a_n+L$ for every $n\ge1$. $\blacksquare$

## Status
Certified. Proved in full in `approaches/global-smooth-density-contradiction.md` (round 5, "Master
Lemma"), reviewed and re-derived step by step by the proof-reviewer (round 5): the construction
$P':=P\cup\bigcup\mathcal A^\infty$ is finite and automatically $\supseteq S$, so no unverified
hypothesis is used anywhere (independently re-checked against `lemmas/periodicity-given-no-escape.md`'s
actual proof body, confirmed generic). Supersedes the need to separately verify "$P^*\supseteq S$" for
any eventual-generator-based prime set (the specific citation-hygiene issue flagged in round 2 for
`antichain-signature-closure.md`, independently repaired there too via a different route this round —
both fixes agree).

## Reuse note
Shows Antichain Stabilization (no reference to the fixed truncation $P=\{p\le L_0\}$) is by itself a
sufficient target for the whole theorem; `lemmas/pc-implies-theorem.md`'s PC hypothesis is strictly
stronger, not needed. The sole remaining open content of the theorem (odd $a_1$ case) is: **Antichain
Stabilization holds for every $a_1$** — equivalently (`lemmas/growth-event-decomposition.md`), only
finitely many "growth events" (indices where the antichain of inclusion-minimal prime-sets genuinely
changes) occur.
