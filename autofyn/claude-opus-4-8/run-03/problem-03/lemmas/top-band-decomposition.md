# Lemma TB (top-band decomposition) — PROPOSED (round 6, breakpoint-vertex)

**Statement.** Let $R$ be any refinement of $C_n=\{2^n,2^{n-1},\dots,2,1\}$ ($n\ge1$), i.e. a
multiset obtained by partitioning each piece of $C_n$ into positive parts. Let $f_1:=\max R$ and set
the top excess $e:=(f_1-2^{n-1})^+$ and
$$D_{\mathrm{low}}:=\mu\{t\in(0,2^{n-1}):N_R(t)\text{ odd}\}\ \ge 0,\qquad N_R(t)=\#\{b\in R:b>t\}.$$
Then
$$D(R)=e+D_{\mathrm{low}}.$$

**Proof.** By certified Lemma M, $D(R)=\int_0^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt$. Split at
$t=2^{n-1}$:
$$D(R)=\int_0^{2^{n-1}}\mathbf 1[N_R(t)\text{ odd}]\,dt+\int_{2^{n-1}}^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt
=D_{\mathrm{low}}+\int_{2^{n-1}}^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt.$$
By certified Lemma ONE (dyadic top-scale dichotomy), at most one final piece of $R$ exceeds
$2^{n-1}$. Hence for every $t\ge2^{n-1}$, $N_R(t)\in\{0,1\}$, so $N_R(t)$ is odd iff $N_R(t)=1$ iff
$f_1>t$. Therefore
$$\int_{2^{n-1}}^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt=\int_{2^{n-1}}^\infty\mathbf 1[f_1>t]\,dt
=(f_1-2^{n-1})^+=e.\qquad\blacksquare$$

**Immediate corollaries (unconditional lower-bound facts for $C_n$).**
- If $f_1\ge2^{n-1}+1$ then $e\ge1$, so $D(R)=e+D_{\mathrm{low}}\ge1$.
- If the top piece $2^n$ is uncut then $f_1=2^n$ (its unique max, all other pieces $\le2^{n-1}$), so
  $e=2^{n-1}$ and $D(R)\ge2^{n-1}\ge1$.
- The residual lower bound $D(R)\ge1$ is equivalent to: (L1, critical band $2^{n-1}<f_1<2^{n-1}+1$)
  $D_{\mathrm{low}}\ge2^{n-1}+1-f_1$; and (L2, top-shredded $f_1\le2^{n-1}$) $D_{\mathrm{low}}\ge1$.

**Depends only on** certified Lemma M and Lemma ONE. **Numerically confirmed** (3000 random
multisets with at most one piece above the threshold: identity $D=e+D_{\mathrm{low}}$ exact).

**Status:** CERTIFIED (round 6, proof-reviewer). Proof re-derived independently: splitting the
Lemma-M integral at $2^{n-1}$ and applying certified Lemma ONE ($N_R(t)\in\{0,1\}$ for
$t\ge2^{n-1}$, since two pieces $>2^{n-1}$ would sum to $>2^n$) gives the top-band contribution
exactly $(f_1-2^{n-1})^+$. Identity re-verified on 20000 random $\le n$-cut refinements of $C_n$
($n\le4$): $D(R)=e+D_{\mathrm{low}}$ held exactly. Depends only on certified M and ONE; statement
is exactly what is proved. Proved in full in `approaches/breakpoint-vertex.md` §4A.
