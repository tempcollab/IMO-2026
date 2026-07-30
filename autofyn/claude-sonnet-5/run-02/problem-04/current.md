## Status
solved

## Approaches tried
- `dyadic-scaffold` (round 2) — worked, but incomplete: proves θ>90° impossible and
  the dyadic family {180°/((2^k+1)·2^j)} ⊆ S. Correct and fully rigorous as far as it
  goes; superseded (not contradicted) by `binary-word-invariant`'s strictly larger
  family.
- `binary-word-invariant` (round 2) — worked, still incomplete: discovers the "shift
  move" primitive and proves the strictly larger family {180°/n : n≥2} ⊆ S, with a
  fully hand/computer-verified exact-fraction 8-move witness for θ=180°/7°. Necessity
  (S ⊆ {180°/n}) is explicitly left open and not claimed.
- `corrected-genericity-bound` (round 2) — DEAD END, claimed `solved` with
  S = {180°/((2^k+1)·2^j)} exactly (asserting θ=180°/7° is NOT forceable), but this is
  **refuted**: proof-reviewer independently reproduced `binary-word-invariant`'s
  180°/7° construction move-by-move with exact `sympy.Rational` arithmetic and
  confirmed it is a genuinely legal, Shan-Yu-immune sequence. The flaw in
  `corrected-genericity-bound`'s necessity proof is located precisely: its closure
  operator $C(V)$ (§3) is defined using only two operations, (halve) $a\mapsto a/2$ and
  (reflect) $a\mapsto V-a$, and is claimed to capture every way a "junk-free" (pure
  θ-affine) angle can evolve. This omits the **shift** operation $a\mapsto a-\theta$
  (subtracting the fixed target θ from a big junk-free angle) entirely — even though
  the paper's own §5 propagation lemma explicitly lists the shift's defining formula
  ($x_1=V$, forcing $B=\{r,p-V,q+V\}$) as one of the "messy single-hit" cases it claims
  to have accounted for, it never folds this operation into the §3 closure computation.
  Once (shift) is added to the closure, the reachable set becomes exactly {180°/n :
  n≥2} (matching `binary-word-invariant`), not the strictly smaller {180°/((2^k+1)2^j)}.
  The paper's other pieces (the exhaustive double-hit dichotomy of §2, the general
  "junk coefficients propagate without cancellation" fact of §5) are independently
  correct and have been certified into `lemmas/double-hit-primitives.md`, but the
  headline necessity theorem (S = F exactly) is **false as proved** — its case n=7
  counterexample is a real, exhibited construction, not a search artifact.
- `full-interval-hypothesis` (round 2) — DEAD END. Self-reported `unsolved`; correctly
  hedged that its "H1 very likely false" conclusion (driven by an order-of-2-mod-7
  obstruction) only applies within its own restricted "one pure quantity + bisection +
  cross-transfer" move family, not the full game. That hedge turned out to be exactly
  right: its restricted family omits the shift move (a fundamentally different affine
  map $P\mapsto P-\theta$, vs. its own $P\mapsto 2P-180$ "cross-transfer"), and once the
  shift move is included θ=180°/7° **is** reachable — refuting the round's headline
  suspicion that the earlier witness was a search artifact. The "cross-transfer"
  primitive it discovered is a real, legal move but is not needed for (and does not by
  itself explain) the 180°/7° witness. Approach abandoned; H1 (full interval (0°,90°])
  remains neither proved nor disproved, but is not this approach's finding either way.
- `denominator-valuation-necessity` (round 4) — **SOLVED, verified round 5.** Proves
  the necessity direction S ⊆ {180°/n : n≥2} via the Integer-Multiple-Avoidance
  ("Cleanliness") Invariant: if T=180°/θ is not an integer, a triangle with no
  θ-normalized angle equal to an integer ("clean") always has a clean child under any
  legal cut, so Shan-Yu can start clean (equilateral) and stay clean forever, so θ is
  never hit. Combined with the imported sufficiency lemma
  `theta-180-over-n-forceable.md`, this gives the full characterization
  S = {180°/n : n integer ≥ 2}. Independently re-verified by the proof-reviewer: the
  four-case residue/integer argument was re-derived from scratch and matches; a
  targeted exact-`Fraction` search over ~17500 clean triples with non-integer T found
  zero double-unclean events, while the same search with T forced integer found
  tens of thousands (confirming the T∉ℤ hypothesis is genuinely load-bearing, not
  vacuous). See `lemmas/integer-multiple-avoidance.md` (newly certified) and the Full
  proof below.

## Current best

The problem is fully solved. See Full proof below.

**Certified lemmas in `lemmas/`:**
- `non-obtuse-invariant.md`: θ ∈ S ⟹ θ ≤ 90° (subsumed as a special case by the
  necessity theorem below, kept as an independent cross-check).
- `theta-180-over-n-forceable.md`: θ = 180°/n ∈ S for every integer n ≥ 2 (sufficiency
  direction; via bisection double-hit, transfer move, and the shift move; includes a
  fully hand-verified exact-fraction 8-move witness for θ = 180°/7°, independently
  reproduced by the proof-reviewer in round 2).
- `double-hit-primitives.md`, `transfer-and-shift-moves.md`, `cut-formula.md`: the
  reusable move-primitive toolkit underlying sufficiency.
- `integer-multiple-avoidance.md`: the Cleanliness Lemma (necessity direction),
  certified round 5.

## Full proof

**Answer.** $S = \{180°/n : n \in \mathbb{Z},\ n \ge 2\}$.

### Sufficiency: {180°/n : n≥2} ⊆ S

Proved in full in `lemmas/theta-180-over-n-forceable.md` (imported, not re-derived
here): for every integer $n\ge2$, Mulan has a finite Shan-Yu-immune move sequence
(bisection double-hits to manufacture a spectator angle $<\theta$ alongside a
persistent angle $>\theta$; one transfer move; $n-2$ shift moves) forcing $\theta =
180°/n$ to appear, from any starting triangle. Includes an exact-fraction worked
witness for $n=7$, independently hand-verified.

### Necessity: S ⊆ {180°/n : n≥2}

Fix $\theta \in (0°,180°)$ and let $T := 180°/\theta$. For any angle value $a$ in the
game write $u := a/\theta$; the three current angles' $u$-values always sum to $T$
(angle-sum invariant). Call a triangle *clean* if none of its three $u$-values is an
integer (equivalently, none of its angles is an integer multiple of $\theta$).

**Cleanliness Lemma** (proved in full, and independently re-verified, in
`lemmas/integer-multiple-avoidance.md`): if $T \notin \mathbb{Z}$, then for every
legal cut of a clean triangle, at least one of the two resulting children is again
clean. Proof: label the cut vertex $p$, others $q,r$; children are
$A=\{u_q,y_1,u_r+u_p-y_1\}$, $B=\{u_r,u_p-y_1,u_q+y_1\}$ for $y_1\in(0,u_p)$. Since
$u_q,u_r$ are inherited non-integers, both children unclean forces one of four
conjunctions of integrality conditions on $y_1$; each of the four is shown impossible
(the first three directly contradict $u_p,u_q,u_r\notin\mathbb Z$; the fourth, adding
$u_p+u_r-y_1\in\mathbb Z$ and $u_q+y_1\in\mathbb Z$, would force
$u_p+u_q+u_r=T\in\mathbb Z$, contradicting the hypothesis).

**Theorem.** If $T\notin\mathbb Z$, then $\theta\notin S$. Proof: Shan-Yu starts with
the equilateral triangle $(60°,60°,60°)$, whose $u$-values are all $T/3$; this is
clean since $T/3\in\mathbb Z$ would force $T=3(T/3)\in\mathbb Z$. At every subsequent
move, whatever cut Mulan makes, the Cleanliness Lemma guarantees a clean child exists;
Shan-Yu always discards to keep a clean one. By induction the triangle is clean at
every check point of the game, so no angle is ever an integer multiple of $\theta$ —
in particular never equal to $\theta$ itself. The game never stops with a win for
Mulan, so $\theta\notin S$. This argument is uniform in $\theta$ rational or
irrational, and uniform over $\theta\le90°$ or $>90°$ — no case split is needed beyond
$T\in\mathbb Z$ vs. $T\notin\mathbb Z$.

### Assembly

$T\in\mathbb Z$, $T\ge2$ is exactly $\theta=180°/n$ for integer $n\ge2$ (note $T>1$
always since $0°<\theta<180°$, so $T=1$ cannot occur). Hence:
$$\theta\in S \iff T=180°/\theta\in\mathbb Z,\ T\ge2 \iff \theta=180°/n\text{ for some integer }n\ge2.$$
Sufficiency (imported) proves the forward-⊇ direction; the Theorem above proves the
contrapositive of ⊆ (if $T\notin\mathbb Z$ then $\theta\notin S$). Together:
$$\boxed{S = \{180°/n : n \in \mathbb{Z},\ n \ge 2\}}.$$

**Verification of the answer.** $n=2 \Rightarrow \theta=90°$ (matches
`non-obtuse-invariant.md`'s boundary), $n=3\Rightarrow60°$, $n=7\Rightarrow180°/7°\approx
25.71°$ (matches the certified exact-fraction 8-move construction). Every such $\theta$
is in $S$ by sufficiency; every other $\theta\in(0°,180°)$ is excluded by the necessity
theorem. Both directions hold; the characterization is complete.

### Full derivation credit
Sufficiency: `binary-word-invariant`/`theta-180-over-n-forceable.md` (round 2).
Necessity: `denominator-valuation-necessity` (round 4), verified by proof-reviewer
(round 5) via independent re-derivation of all four cases plus a targeted exact-
`Fraction` search (found zero double-unclean events across ~17500 clean, non-integer-T
instances; found tens of thousands when $T$ was forced integer, confirming the
hypothesis is load-bearing).
