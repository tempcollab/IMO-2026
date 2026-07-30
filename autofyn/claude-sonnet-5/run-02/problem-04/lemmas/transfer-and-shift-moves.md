# Lemma: Transfer move and Shift move (single-hit forced transitions)

Using the cut formula (`cut-formula.md`): triangle $(p,q,r)$, cut vertex $p$, cut
parameter $x_1\in(0,p)$, children $A=\{q,x_1,r+p-x_1\}$, $B=\{r,p-x_1,q+x_1\}$. Fix a
target $\theta$ not currently present.

## Shift move

**Statement.** If $p>\theta$, setting $x_1=\theta$ gives $A=\{q,\theta,r+p-\theta\}$
(contains $\theta$: Shan-Yu discards it) and forces
$$B=\{p-\theta,\ q+\theta,\ r\}$$
— i.e. the cut angle drops by exactly $\theta$, the chosen "receiver" $q$ gains exactly
$\theta$, and the spectator $r$ is untouched. This is Shan-Yu-immune (he always avoids
$A$ since it contains $\theta$, unless $q=\theta$ or $r+p-\theta=\theta$ too, in which
case it is a double-hit and he loses immediately regardless).

**Proof.** Direct substitution $x_1=\theta$ into the cut formula: legality needs
$0<\theta<p$, i.e. $p>\theta$ (given, and $\theta>0$ always). $A=\{q,\theta,r+p-\theta\}$
contains $\theta$ literally as its second entry. $B=\{r,p-\theta,q+\theta\}$ by direct
substitution $p-x_1=p-\theta$, $q+x_1=q+\theta$. $\blacksquare$

## Transfer move

**Statement.** If $p>\theta$ and there is a "spectator" angle $r$ with $0<r<\theta$
present, setting $x_1=r+p-\theta$ gives $A=\{q,r+p-\theta,\theta\}$ (contains $\theta$:
Shan-Yu discards it) and forces
$$B=\{r,\ \theta-r,\ 180°-\theta\}$$
— independent of the value of $q$ entirely.

**Proof.** Legality: $x_1=r+p-\theta\in(0,p)$. Upper bound $x_1<p \iff r<\theta$ (the
spectator hypothesis). Lower bound $x_1>0$: since $p>\theta$, $r+p-\theta>r>0$. By
identity (★), $A$'s third entry $r+p-x_1=\theta$ (direct substitution), so
$A=\{q,x_1,\theta\}$ contains $\theta$. $B=\{r,p-x_1,q+x_1\}$: $p-x_1=\theta-r$, and
$q+x_1=q+r+p-\theta=(p+q+r)-\theta=180°-\theta$ (using $p+q+r=180°$), independent of
$q$'s specific value. $\blacksquare$

## Sufficient condition for existence of a spectator

By repeated bisection (`bisection-lemma`, see `dyadic-scaffold`'s Lemma 3: bisecting an
angle $a$ forces $a/2$ into both children unconditionally), starting from any angle
$a_0>0$ present in the starting triangle, $a_0/2^n<\theta$ for $n$ large enough
(Archimedean property); this is forced regardless of Shan-Yu. So a spectator $r<\theta$
can always be manufactured in finitely many Shan-Yu-immune moves, for any $\theta>0$.

**Source.** Both moves independently re-derived and hand-verified by the proof-reviewer
(round 2) against the raw cut formula, including a full exact-fraction numeric
re-verification of an 8-move chain realizing $\theta=180°/7$ (transfer + 5 shifts from
an equilateral start). First discovered (shift move) and proved in
`binary-word-invariant` (round 2); transfer move independently proved in
`dyadic-scaffold` (Lemma 4) and `corrected-genericity-bound` (§1) as well. Certified.
