# Lemma: Non-obtuse invariant (θ > 90° is never forceable)

**Statement.** If $\theta>90°$, then Shan-Yu has a strategy (choice of starting
triangle plus every subsequent discard) that prevents any angle from ever equaling
$\theta$, so $\theta\notin S$.

**Proof.**
*Step 1 (one-move invariance).* If a triangle $(p,q,r)$ has all angles $\le90°$, then
for every legal cut (every apex choice, every $x_1\in(0,p)$, using the cut formula from
`cut-formula.md`), at least one child $A=\{q,x_1,r+p-x_1\}$, $B=\{r,p-x_1,q+x_1\}$ has
all angles $\le90°$. Indeed $q\le90°$, $x_1<p\le90°$, so $A$'s only possibly-large angle
is $r+p-x_1$; symmetrically $B$'s only possibly-large angle is $q+x_1$. By identity (★),
$(r+p-x_1)+(q+x_1)=180°$, so they cannot both exceed $90°$; hence at least one of $A,B$
is non-obtuse.

*Step 2 (strategy).* Shan-Yu starts with the equilateral triangle $(60°,60°,60°)$
(non-obtuse) and at every step keeps a non-obtuse child, which exists by Step 1
regardless of Mulan's cut. By induction the triangle is non-obtuse forever, so every
angle ever present is $\le90°<\theta$. The game never stops. $\blacksquare$

**Source.** Proved identically (word-for-word up to notation) in `dyadic-scaffold`,
`corrected-genericity-bound`, `binary-word-invariant`. Certified by proof-reviewer round 2.
