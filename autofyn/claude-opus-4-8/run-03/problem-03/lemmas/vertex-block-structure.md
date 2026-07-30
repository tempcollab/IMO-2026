# Lemma BLK (block-structure of MID-core vertices) — CERTIFIED (round 12)

**Certification (round 12).** Reviewer-verified. Standard vertex active-constraint rank count. The
`n+1` group-sum equalities (E) have pairwise-disjoint supports (each labelled piece lies in one
group), hence rank exactly `n+1`. At a vertex the `m` active independent constraints beyond (E) come
from tight order relations (O) and box faces (C): partitioning the `m` positions into `p` maximal
equal-value blocks makes exactly `m−p` order relations tight, and the box contributes at most two
more (top block `=2^{n-1}`, bottom block `=0`). Vertex ⇒ active rank `= m ≤ (n+1)+(m−p)+2`, i.e.
`p ≤ n+3`. Correct. Admitted.

**Statement.** At a vertex of `P_T` (notation as in Lemma VERT-LOW) the `m` piece-values take at most
`n+3` distinct values, hence at most `n+2` distinct **positive** values.

**Scope.** Makes GAP-EXTR a statement about a FINITE explicit family of block-structured extreme
points (each with `≤ n+2` distinct dyadic-group-summed positive values). Structural sharpening only;
does not close GAP-EXTR.
