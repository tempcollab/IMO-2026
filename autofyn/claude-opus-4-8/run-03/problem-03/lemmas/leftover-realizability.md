# Lemma RL (leftover realizability) — CERTIFIED (round 7, breakpoint-vertex)

**Setting.** For a multiset $A=\{a_1,\dots,a_m\}$ of positive reals, a Xiang response is modelled by
the two certified DELETE/MATCH moves (Lemma DM, `elementary-reductions.md`), each costing one cut
and lowering the tracked piece-count by one:
- **DELETE $x$:** bisect $x$; the pair $\{x/2,x/2\}$ cancels (Lemma P), so $D(S)\mapsto
  D(S\setminus\{x\})$.
- **MATCH $(x,y)$, $x>y$:** cut $x$ into $\{y,x-y\}$; the new $y$ cancels the resident $y$ (Lemma P),
  so $D(S)\mapsto D((S\setminus\{x,y\})\cup\{x-y\})$.

Let $\mathcal R(A)=\{\rho\ge0:\rho$ is the single leftover of some $\le(m-1)$-move DM sequence on
$A\}$ (a sequence of $m-1$ non-degenerate moves ends at one piece $\rho$, with $D=\rho$).

**Statement.**
$$\mathcal R(A)=\Big\{\,\big|\textstyle\sum_{i\in T}\varepsilon_i a_i\big| : \varnothing\ne
T\subseteq[m],\ \varepsilon\text{ a nonnegative-differencing-tree sign pattern on }T\,\Big\},$$
a subset of $\{|\sum_i\varepsilon_i a_i|:\varepsilon\in\{0,\pm1\}^m\}$ (all signed subset sums),
**strict** in general: only tree-realizable patterns occur (MATCH produces only *differences*
$x-y$, never a sum of two positive pieces). The budget is $|T|-1$ MATCH moves plus $m-|T|$ DELETE
moves $=m-1$ cuts.

**Proof.** Track for each current piece its expansion as an integer combination $\sum_i c_i a_i$ of
the inputs. Initially each $a_i$ is $e_i$. Because each input leaf flows into exactly one current
piece, the coefficient vectors of the current pieces always have **pairwise disjoint supports**. A
DELETE zeroes the coordinates of the removed piece. A MATCH $(x,y)$ replaces $\mathbf v_x,\mathbf v_y$
(disjoint supports, entries in $\{0,1\}$ up to sign) by $\mathbf v_x-\mathbf v_y$, whose entries are
therefore in $\{0,\pm1\}$; its support is a binary tree over the leaves used, with the sign of each
leaf fixed by its depth-parity in the differencing tree (the value $x-y\ge0$ pins the root sign).
After $m-1$ moves the single surviving piece has value $\rho=|\sum_{i\in T}\varepsilon_i a_i|$ with
$T$ its support and $\varepsilon_i=c_i$ tree-realizable; and $D(\{\rho\})=\rho$. Conversely any
nonnegative differencing tree over any nonempty $T$ is executable: MATCH along its internal nodes
($|T|-1$ cuts) and DELETE the $m-|T|$ leaves outside $T$ ($m-|T|$ cuts), total $m-1$. Strictness:
for $m=3$ the value $a_1+a_2$ is a $\{0,\pm1\}$ signed sum but is unreachable (MATCH never sums two
positive pieces), so it is absent from $\mathcal R(A)$. $\blacksquare$

**Corollary (Reduction R-UV).** In the upper-bound game ($m=n+1$, $\le n$ cuts) Xiang forces
$D\le u_nL$ **as soon as** $\min\mathcal R(A)\le u_nL$. (Sufficiency: some DM sequence yields
$\rho\le u_nL$ with $D=\rho$; Xiang may also stop earlier at an even-multiplicity multiset for a
possibly smaller $D$, so this is a valid *sufficient* condition for the upper bound.)

**Depends only on** certified Lemmas P and DM. **Machine-checked** ($m\le5$, budget enforced):
$\mathcal R(A)$ is always a subset of the $\{0,\pm1\}$ signed sums, and strict (e.g. $|\mathcal R|=8
<13$ for $m=3$).

**Status:** CERTIFIED (round 7, proof-reviewer). Re-derived the disjoint-support invariant giving
$c_i\in\{0,\pm1\}$; the converse budget count $|T|-1+(m-|T|)=m-1\le n$ holds since $m\le n+1$; the
value $D(\{\rho\})=\rho$ is immediate. **Scope note:** RL characterizes the achievable-leftover
family and gives the *sufficient* reduction R-UV; it does **not** prove the upper bound. The
residual Prop UV ($\min\mathcal R(A)\le u_nL$ in the balanced valley) — a restricted
signed-subset-sum discrepancy bound — is open; a naive $2^{n+1}$-subset pigeonhole is invalid
because (by RL) not all $\{0,\pm1\}$ patterns are reachable.
