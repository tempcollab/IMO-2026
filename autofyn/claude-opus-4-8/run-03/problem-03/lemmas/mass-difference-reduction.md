# Lemma MID (mass-difference reduction) — CERTIFIED (round 7, parity-measure-potential)

**Setting.** Work in units of $u$; Liu plays $C_n=\{2^0,\dots,2^n\}$. Let $S=F\sqcup B$ be any
admissible $a=0$ refinement of $C_n$ by $\le n$ cuts:
- $F$ = the fragments of the top piece $2^n$, each $\le 2^{n-1}$, $\Sigma F=2^n$, $|F|\ge2$ (by
  certified Lemma ONE, since two fragments $>2^{n-1}$ would sum to $>2^n$);
- $B$ = a $\le(n-1)$-cut refinement of the tail ladder $C_{n-1}=\{2^0,\dots,2^{n-1}\}$, each piece
  $\le 2^{n-1}$, $\Sigma B=2^n-1$.

Define, on $(0,2^{n-1})$, the **mass-difference count**
$$g(t):=N_F(t)-N_B(t),\qquad N_X(t)=\#\{\text{pieces of }X>t\}.$$

**Statement.**
- **(a) [parity identity]** For $t\ge 2^{n-1}$, $N_S(t)=0$; and for $t\in(0,2^{n-1})$, $N_S(t)$ is
  odd $\iff g(t)$ is odd. Hence by certified Lemma M,
  $$D(S)=\mu\{t\in(0,2^{n-1}):g(t)\text{ odd}\}.$$
- **(b) [mass identity]** $\displaystyle\int_0^{2^{n-1}} g(t)\,dt=1$ for **every** admissible $a=0$
  refinement.

Consequently $D(S)\ge1$ (i.e. the $a=0$ lower bound "L2") is **exactly equivalent** to
$$\mu\{t\in(0,2^{n-1}):g(t)\text{ odd}\}\ \ge\ \int_0^{2^{n-1}}g(t)\,dt\ (=1).\tag{MID-core}$$

**Proof.** **(a)** Every piece of $S$ is $\le 2^{n-1}$ (each $f\in F$ by the $a=0$ hypothesis; each
$b\in B$ as a fragment of $C_{n-1}$). Thus for $t\ge 2^{n-1}$ no piece strictly exceeds $t$, so
$N_S(t)=0$ (even). For $t\in(0,2^{n-1})$, the disjoint multiset union $S=F\sqcup B$ gives
$N_S(t)=N_F(t)+N_B(t)$; since $N_F+N_B\equiv N_F-N_B=g\pmod 2$, $N_S(t)$ is odd iff $g(t)$ is odd.
By certified Lemma M ($D=\mu\{t:N_S(t)\text{ odd}\}$) and the first sentence (odd-set confined to
$(0,2^{n-1})$), $D(S)=\mu\{t\in(0,2^{n-1}):g(t)\text{ odd}\}$.

**(b)** By the layer-cake identity $\int_0^\infty\mathbf 1[x>t]\,dt=x$ for $x>0$, and since
$N_F(t)=0$ for $t\ge 2^{n-1}$,
$$\int_0^{2^{n-1}}N_F(t)\,dt=\int_0^\infty N_F(t)\,dt=\sum_{f\in F}\int_0^\infty\mathbf 1[f>t]\,dt
=\sum_{f\in F}f=\Sigma F=2^n.$$
Identically $\int_0^{2^{n-1}}N_B(t)\,dt=\Sigma B=2^n-1$. Subtracting, $\int_0^{2^{n-1}}g=1$. The
boxed equivalence follows from (a) and (b). $\blacksquare$

**Depends only on** certified Lemma M and the layer-cake (Fubini) identity. **Numerically confirmed**
(round 7 reviewer, exact-piecewise evaluation): on hand-built and random admissible $a=0$
refinements at $n=4$, $\int g=\Sigma F-\Sigma B=1$ exactly and $\mu\{g\text{ odd}\}=D(S)$ exactly
(e.g. $F=\{7,6,3\},B=\{1,2,1.5,2.5,3,5\}$: $D(S)=5=\mu\{g\text{ odd}\}$, $\int g=1$).

**Status:** CERTIFIED (round 7, proof-reviewer). Re-derived independently: $N_S=N_F+N_B$ and
$2N_B\equiv0$ give the parity identity; the two layer-cake integrals give $\Sigma F-\Sigma B=1$.
Both steps are exact and use only certified Lemma M. **Scope note:** MID is an exact *reduction*
(it eliminates the SPLIT cross term $\mu(O_F\cap O_B)$ and the balanced/unbalanced dichotomy). It
does **not** by itself prove $D(S)\ge1$: the residual GAP MID-core ($\mu\{g\text{ odd}\}\ge\int g$
for $|F|\ge3$) remains open and genuinely requires the ladder structure of $B$ (the pure-integral
version "$\int g=1\Rightarrow\mu\{g\text{ odd}\}\ge1$" is false, e.g. $g\equiv2$ on measure $1/2$).
