# Lemma VS (valley-sharpness) — CERTIFIED (round 7, breakpoint-vertex)

**Setting.** Upper-bound game at full budget $m=n+1$, total $L$, sorted $a_1\ge\dots\ge a_{n+1}$.
The **balanced valley** is $\{a_1<L/2,\ a_2<\beta_nL\}$ with $\beta_n:=2^{n-1}/(2^{n+1}-1)$. Recall
$u_n=1/(2^{n+1}-1)$, $c(n)=2^n/(2^{n+1}-1)=(1+u_n)/2>\tfrac12$, and $u_n/u_{n-1}=(2^n-1)/(2^{n+1}-1)$.

**Statement.** In the balanced valley, **no single DM move** (Lemma DM) produces an $n$-piece
instance on which the inductive hypothesis $\mathrm{UB}(n-1)$ (Xiang forces $D\le u_{n-1}\cdot$mass)
*alone* certifies $D\le u_nL$:
1. **Single DELETE $a_i$** $\to$ $n$ pieces, mass $L-a_i$; certificate $u_{n-1}(L-a_i)\le u_nL$
   holds iff $a_i\ge c(n)L$ — but $a_i\le a_1<L/2<c(n)L$, so it fails for every $i$.
2. **Single MATCH $(a_i,a_j)$**, smaller part $y$ $\to$ $n$ pieces, mass $L-2y$; certificate
   $u_{n-1}(L-2y)\le u_nL$ holds iff $y\ge\beta_nL$ — but the smaller of any pair is $\le a_2<
   \beta_nL$, so it fails for every pair.

Hence any correct upper-bound argument in the valley must spend $\ge2$ coordinated cuts before
invoking induction (rigorous adaptivity).

**Proof.** (1) $u_{n-1}(L-a_i)\le u_nL\iff L-a_i\le(u_n/u_{n-1})L=\tfrac{2^n-1}{2^{n+1}-1}L\iff
a_i\ge(1-\tfrac{2^n-1}{2^{n+1}-1})L=\tfrac{2^n}{2^{n+1}-1}L=c(n)L$. As $c(n)>\tfrac12$
($2^{n+1}>2^{n+1}-1$) and $a_i\le a_1<L/2$, the certificate fails. (2) $u_{n-1}(L-2y)\le u_nL\iff
2y\ge\tfrac{2^n}{2^{n+1}-1}L\iff y\ge\tfrac{2^{n-1}}{2^{n+1}-1}L=\beta_nL$. In any pair at most one
member is $a_1$, so the other is $\le a_2$ and the smaller $y\le a_2<\beta_nL$; the certificate
fails. $\blacksquare$

**Depends only on** the closed forms $u_n,c(n),\beta_n$ and certified Lemma DM. The two thresholds
$c(n)L$ (DELETE) and $\beta_nL$ (MATCH) meet the valley's two defining inequalities exactly, so the
valley boundary is sharp; this rigorously subsumes the numeric refutations of every deterministic
single-rule Xiang strategy (always-DELETE-$a_1$, always-MATCH-top-two, hybrid, cascading bisection).

**Status:** CERTIFIED (round 7, proof-reviewer). Algebra re-verified: $1-u_n/u_{n-1}=c(n)$ and
$c(n)/2=\beta_n$. **Scope note:** VS is a *limiting/adaptivity* lemma — it proves the insufficiency
of the single-move IH certificate, not a positive bound. It localizes the residual upper-bound work
to Prop UV (see `leftover-realizability.md`), which remains open.
