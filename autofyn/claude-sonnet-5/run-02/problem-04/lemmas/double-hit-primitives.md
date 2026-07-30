# Lemma: Exhaustive classification of one-move "double hit" forcing cuts

**Statement.** Fix a target value $V\in(0,180°)$ and a triangle $(p,q,r)$ (cut vertex
$p$, others $q,r$) with $q\ne V\ne r$. Using the cut formula (`cut-formula.md`), a
**double hit** at $x_1$ (i.e. $V$ present in *both* children $A,B$) occurs only in
exactly two families:

- **(D1) Bisection double-hit.** $p=2V$, $x_1=V$: both children get $V$ as their
  second entry.
- **(D2) $V=90°$ altitude-foot double-hit.** For any triangle with a max angle $p\ge
  90°-$ish (more precisely: taking $p=\max(p,q,r)$, so $q,r<90°$), setting
  $x_1=r+p-90°$ (equivalently the foot of the altitude from the max vertex) is a valid
  cut in $(0,p)$ and forces $90°$ into both children. This double-hit type exists only
  for $V=90°$.

No other value of $x_1$ can hit both $A$ and $B$ with $V$.

**Proof.** $\theta$ can appear in $A=\{q,x_1,r+p-x_1\}$ only via $x_1=V$ or
$x_1=r+p-V$ (excluding the already-present cases $q=V$), and in $B=\{r,p-x_1,q+x_1\}$
only via $x_1=p-V$ or $x_1=V-q$ (excluding $r=V$). A double hit requires one of the
two $A$-conditions to coincide with one of the two $B$-conditions:
1. $x_1=V=p-x_1 \Rightarrow p=2V$ (case D1).
2. $x_1=V=V-q \Rightarrow q=0$: degenerate, impossible.
3. $x_1=r+p-V=p-x_1 \Rightarrow r=0$: degenerate, impossible.
4. $x_1=r+p-V=V-q \Rightarrow p+q+r=2V \Rightarrow V=90°$ (case D2), valid at
   $x_1=r+p-90°$ provided $0<r+p-90°<p$, i.e. $q,r<90°$ — achievable by cutting from
   the (unique, up to ties) angle $\ge90°$ if one exists, else from any vertex.

These are the only four pairings of the two $A$-conditions with the two $B$-conditions;
each is checked exhaustively above. $\blacksquare$

**Source.** Proved independently and identically (same case exhaustion) in
`dyadic-scaffold` (§2, Lemmas 2–3), `corrected-genericity-bound` (§2), and
`binary-word-invariant` (§2, "double hit" part). Certified by proof-reviewer round 2 —
hand re-derived and confirmed the four-case exhaustion is complete and correct.
