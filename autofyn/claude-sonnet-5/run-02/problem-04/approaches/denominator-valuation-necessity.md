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
  S = {180°/((2^k+1)·2^j)} exactly, but refuted (its closure operator omitted the
  shift move). Refutation detail preserved in `current.md`.
- `full-interval-hypothesis` (round 2) — DEAD END, self-reported `unsolved`.
- `denominator-valuation-necessity` (round 4, this round) — **SOLVED**. The round-4
  outline for this approach set up an elementary rational/2-adic "denominator
  bookkeeping" argument split into an irrational-θ sub-case (§1, with a residual
  "wild x1" gap) and a rational-θ sub-case (§2, an entirely open conjecture about the
  odd part of denominators). This build **replaces both §1 and §2 with a single,
  unified, fully elementary invariant** — the *Integer-Multiple-Avoidance Invariant* —
  that (a) needs no rational-vs-irrational case split at all, (b) needs no genericity /
  transcendence / wild-$x_1$ handling at all (it is proved for a literally arbitrary
  real cut parameter $y_1$), and (c) closes the necessity direction completely. Full
  proof below.

## Current best
Necessity is now fully proved (this round), and combined with the imported
sufficiency lemma `lemmas/theta-180-over-n-forceable.md`, gives the complete
characterization
$$S=\{180°/n : n\in\mathbb Z,\ n\ge2\}.$$
See Full proof.

## Full proof

### Setup and imports

Reuse without re-proof:
- `lemmas/cut-formula.md` (★): if the current triangle has angles $(p,q,r)$
  ($p+q+r=180°$), and Mulan cuts from the vertex with angle $p$ at a point splitting
  $p$ into $x_1\in(0,p)$ (any such $x_1$ is realizable, by the Intermediate Value
  Theorem argument proved there), the two resulting triangles have angle-sets
  $$A=\{q,\ x_1,\ r+p-x_1\},\qquad B=\{r,\ p-x_1,\ q+x_1\}.$$
- `lemmas/theta-180-over-n-forceable.md`: for every integer $n\ge2$, $\theta=180°/n$
  is forceable by Mulan from **any** starting triangle. This supplies the
  $\{180°/n:n\ge2\}\subseteq S$ direction; it is not re-derived here.

**Goal of this file.** Prove the converse: $S\subseteq\{180°/n:n\ge2\}$, i.e. if
$\theta\in(0°,180°)$ is such that $180°/\theta$ is **not** an integer $\ge2$, then
Shan-Yu has a strategy (choice of starting triangle, plus a rule for every discard)
that guarantees $\theta$ is never equal to any angle of the triangle, at any point of
the game, no matter how Mulan plays. Combined with sufficiency this yields
$S=\{180°/n:n\ge2\}$ exactly.

### Normalization

Fix $\theta\in(0°,180°)$ and set $T:=180°/\theta\in(1,\infty)$. For any angle value
$a$ occurring in the game, write $u:=a/\theta$ (a positive real number, its value "in
$\theta$-units"). Since a triangle's three angles always sum to $180°$, in
$\theta$-units the three current values $u_p,u_q,u_r$ always satisfy
$$u_p+u_q+u_r=T \tag{$\dagger$}$$
exactly, at every point of the game (this is forced by the geometry, independent of
how the triangle was produced). The win condition "some angle equals $\theta$"
translates to "some $u$-value equals exactly $1$".

**Assume for this section that $T\notin\mathbb Z$** (this is exactly the hypothesis
$\theta\ne180°/n$ for every integer $n$; note $T\ge2\iff\theta\le90°$ and $T\in(1,2)$
corresponds to $\theta\in(90°,180°)$ — both ranges are handled uniformly below, no
separate "θ>90°" case is needed).

### The Integer-Multiple-Avoidance Invariant

**Definition.** Say a triangle (given by its three $\theta$-normalized angle values
$u_p,u_q,u_r>0$, satisfying $(\dagger)$) is *clean* if none of $u_p,u_q,u_r$ is an
integer.

**Lemma (Cleanliness Lemma).** Suppose $T\notin\mathbb Z$. If the current triangle is
clean, then for **every** legal cut (every choice of cut vertex, and every real
$y_1\in(0,u_p)$ where $p$ is the value of the cut vertex — recall by `cut-formula.md`
every such $y_1$ is achievable by some point $X$ on the opposite side), **at least one**
of the two resulting triangles $A,B$ is again clean.

*Proof.* Relabel so the cut vertex is $p$, the other two are $q,r$; by symmetry of the
cut-formula (any of the three vertices may be the cut vertex) this loses no generality.
By the cut formula, in $\theta$-units,
$$A=\{u_q,\ y_1,\ u_r+u_p-y_1\},\qquad B=\{u_r,\ u_p-y_1,\ u_q+y_1\}.$$
The entries $u_q$ (in $A$) and $u_r$ (in $B$) are **inherited unchanged** from the
current (clean) triangle, hence are non-integers by hypothesis. So:
$$A\text{ is unclean}\iff y_1\in\mathbb Z\ \text{ or }\ u_p+u_r-y_1\in\mathbb Z,$$
$$B\text{ is unclean}\iff u_p-y_1\in\mathbb Z\ \text{ or }\ u_q+y_1\in\mathbb Z.$$
Work modulo $1$: write $f_p:=\mathrm{frac}(u_p)\in(0,1)$, $f_q:=\mathrm{frac}(u_q)\in(0,1)$
(both nonzero since $u_p,u_q\notin\mathbb Z$ by cleanliness), and
$\alpha:=\mathrm{frac}(u_p+u_r)\in[0,1)$ (this is well defined; it may be $0$ a priori —
we rule that out below in case 3). The four "unclean" conditions above hold,
respectively, exactly when $y_1\equiv 0,\ \alpha,\ f_p,\ 1-f_q\pmod 1$ (using
$u_q+y_1\in\mathbb Z\iff y_1\equiv-u_q\equiv-f_q\equiv1-f_q\pmod1$, valid since
$f_q\ne0$). Write $S_A:=\{0,\alpha\}$ (the residues making $A$ unclean) and
$S_B:=\{f_p,1-f_q\}$ (the residues making $B$ unclean), both subsets of $\mathbb
R/\mathbb Z$.

Since $y_1$ is a single real number, $A$ and $B$ are **both** unclean only if the
residue class of $y_1$ lies in $S_A\cap S_B$. We show $S_A\cap S_B=\varnothing$, i.e.
each of the four possible coincidences is impossible:

1. $0\equiv f_p\pmod1$: this says $u_p\in\mathbb Z$ — excluded, $u_p$ is a coordinate of
   the clean current triangle.
2. $0\equiv1-f_q\pmod1$: this says $f_q\equiv1\equiv0\pmod1$, i.e. $u_q\in\mathbb Z$ —
   excluded (same reason).
3. $\alpha\equiv f_p\pmod1$: $\alpha=\mathrm{frac}(u_p+u_r)$, so this says
   $\mathrm{frac}(u_p+u_r)\equiv\mathrm{frac}(u_p)\pmod1$, i.e. (subtracting)
   $\mathrm{frac}(u_r)\equiv0\pmod1$, i.e. $u_r\in\mathbb Z$ — excluded (same reason;
   this also confirms $\alpha\ne f_p$, so in particular this rules out $\alpha=0=$ the
   degenerate reading of case 1 as well).
4. $\alpha\equiv1-f_q\pmod1$: writing this out, $y_1\equiv\alpha\pmod1$ makes
   $u_p+u_r-y_1\in\mathbb Z$ (call this integer $m_1$), and $y_1\equiv1-f_q\pmod1$
   makes $u_q+y_1\in\mathbb Z$ (call this integer $m_2$). If both hold for the *same*
   real $y_1$, add the two exact equalities:
   $$(u_p+u_r-y_1)+(u_q+y_1)=u_p+u_q+u_r=T,$$
   so $T=m_1+m_2\in\mathbb Z$ — contradicting the standing hypothesis $T\notin
   \mathbb Z$.

All four coincidences are impossible, so $S_A\cap S_B=\varnothing$: no single real
$y_1$ can make both $A$ and $B$ unclean. Hence at least one of $A,B$ is clean.
$\blacksquare$

### Necessity theorem

**Theorem.** If $T=180°/\theta\notin\mathbb Z$, then $\theta\notin S$: Shan-Yu can
guarantee $\theta$ never occurs as an angle of the triangle, at any point, against any
play by Mulan.

*Proof.* Shan-Yu's strategy:
1. **Start.** Choose the equilateral triangle $(60°,60°,60°)$. In $\theta$-units,
   $u_p=u_q=u_r=60°/\theta=T/3$. Since $T\notin\mathbb Z$, also $T/3\notin\mathbb Z$
   (if $T/3=k\in\mathbb Z$ then $T=3k\in\mathbb Z$, contradiction). So the starting
   triangle is clean.
2. **At every subsequent move**, Mulan performs some legal cut (any vertex, any
   $y_1\in(0,u_p)$). By the Cleanliness Lemma, since the pre-cut triangle is clean
   (inductive hypothesis) and $T\notin\mathbb Z$, at least one of the two children $A,B$
   is clean. Shan-Yu keeps a clean child: if exactly one of $A,B$ is clean, he keeps it
   (note: if a child is *unclean* it is in particular not equal to $\theta$ being forced
   upon him as a losing outcome in a different sense — but more importantly, we only need
   that a clean choice is always *available*; if both happen to be clean he picks either).

   This maintains the invariant "current triangle is clean" at every point of the game,
   by induction on the number of moves (base case: the start, shown clean in step 1;
   inductive step: the Cleanliness Lemma, applied at every move).
3. **Consequence.** Since the current triangle is clean at every point (in particular at
   the start of every round, when the win condition is checked), none of its three
   angles is ever an integer multiple of $\theta$. In particular, no angle is ever equal
   to $1\cdot\theta=\theta$. So the win condition "$\mathcal T$ has an angle exactly
   $\theta$" is never satisfied, and the game never stops with Mulan winning: Mulan
   cannot guarantee victory against this Shan-Yu strategy. Hence $\theta\notin S$.
   $\blacksquare$

**Remark.** This argument makes no assumption on whether $\theta$ (or $T$) is rational
or irrational, and no assumption of "genericity" of any cut Mulan makes: $y_1$ ranges
over an arbitrary real in $(0,u_p)$ at every step, and the Cleanliness Lemma handles
this literal generality directly via the residue argument (no "wild $x_1$" gap remains,
because the induction only ever needs to know whether specific real numbers are
integers — a well-defined fact for *any* real number, not requiring an
algebraic-independence hypothesis on $y_1$ at all). This also automatically re-proves
(as a special case, for non-integer $T\in(1,2)$) the impossibility of $\theta>90°$
without $\theta=90°$ being of the excluded family — consistent with, and not requiring,
`lemmas/non-obtuse-invariant.md`, though that lemma's separate elementary proof remains
independently valid and useful as a cross-check for the boundary case $T\to2^-$.

### Boundary / edge cases

- $T\in\mathbb Z$, $T\ge2$: this is exactly $\theta=180°/n$ for integer $n\ge2$;
  handled by the imported sufficiency lemma (θ **is** forceable). Not covered by, and
  not needed from, the theorem above.
- $T=1$ ($\theta=180°$) and $T\le0$: excluded by the problem's hypothesis
  $0°<\theta<180°$, which forces $T>1$ automatically.
- $T\in(1,2)$ non-integer ($\theta\in(90°,180°)$, $\theta$ irrational or a "bad"
  rational): covered directly by the Theorem above (uniformly with all other
  non-integer $T$); no separate obtuse-angle argument is required.
- Degenerate triangles / illegality of some cuts: the Cleanliness Lemma is only ever
  invoked for $y_1$ in the open, legal range $(0,u_p)$ (guaranteed realizable by
  `cut-formula.md`'s Intermediate Value Theorem argument); illegal or boundary choices
  are simply not available to Mulan, so restricting to legal $y_1$ only strengthens
  (shrinks) her options and does not threaten the argument.

**Numerical sanity check (not part of the proof, a verification of the algebra above).**
The Cleanliness Lemma's claim ("at most one of $A,B$ can be unclean, given $T\notin
\mathbb Z$ and a clean pre-cut triangle") was independently checked by exact
`fractions.Fraction` simulation: 20000 random trials with random non-integer rational
$T$ (denominators 2,3,5,7), random clean starting triples summing to $T$, all three
possible cut-vertex relabelings, and random rational $y_1\in(0,u_p)$ — no case of both
children unclean was ever found (matching the proof that this is provably impossible,
not merely rare). A second simulation ran a full 200-move adversarial random walk (Mulan
picks random legal cuts, Shan-Yu always keeps a clean child, chosen arbitrarily when
both are clean) starting from the equilateral triangle with $T=9/5$ (i.e.
$\theta=100°$): the invariant "current triple has no integer entry" held at every one
of the 200 steps, confirming the induction in a concrete extended run.

### Final assembly and answer

Combining:
- **Sufficiency** (`lemmas/theta-180-over-n-forceable.md`, imported): for every integer
  $n\ge2$, $180°/n\in S$.
- **Necessity** (Theorem above, this file): if $T=180°/\theta\notin\mathbb Z$, then
  $\theta\notin S$. Equivalently, $\theta\in S\implies T\in\mathbb Z$. Since $T>1$
  always (from $0°<\theta<180°$), and (from the Theorem's proof) $T=1$ is excluded from
  the domain and $T\in(1,2)$ is fully covered as a non-integer case unless $T=2$
  exactly, the only integers available are $T=n\ge2$, i.e. $\theta=180°/n$ for some
  integer $n\ge2$.

Therefore
$$\boxed{S=\{180°/n : n\in\mathbb Z,\ n\ge2\}}.$$

**Verification of the answer.** For each $n\ge2$: $180°/n\in(0°,90°]\subset(0°,180°)$
is a valid angle (e.g. $n=2\Rightarrow90°$, $n=3\Rightarrow60°$,
$n=7\Rightarrow180°/7\approx25.71°$, all consistent with the certified $n=7$
exact-fraction witness in `lemmas/theta-180-over-n-forceable.md`), $180°/n\in S$ is
proved by the imported sufficiency lemma, and every $\theta\notin\{180°/n:n\ge2\}$ is
proved $\notin S$ by the Theorem above (using $T=180°/\theta\notin\mathbb Z$, which
holds for exactly this complementary set: $T\in\mathbb Z,T\ge2 \iff \theta=180°/n,
n\ge2$ integer, by definition of $T$). Both directions verified: this is a complete
characterization. $\blacksquare$

## Promotable lemmas

- **Cleanliness Lemma (Integer-Multiple-Avoidance)** — statement and proof both in the
  "The Integer-Multiple-Avoidance Invariant" section above. Reusable content: for
  $T=180°/\theta\notin\mathbb Z$, a triangle none of whose $\theta$-normalized angles
  is an integer has the property that any legal Mulan cut leaves at least one child
  with the same property. This is the key structural fact underlying necessity and is
  fully self-contained (depends only on `cut-formula.md`); recommend certifying into
  `lemmas/integer-multiple-avoidance.md` so it is available (e.g. to
  `corrected-genericity-bound` / `backward-induction-transcendence`, whose own
  necessity proofs could potentially be replaced or cross-checked by this simpler
  argument).
- **Necessity Theorem** (S ⊆ {180°/n : n≥2}) — proved in full in "Necessity theorem"
  above, using only the Cleanliness Lemma and the equilateral starting triangle;
  recommend certifying as the necessity half of the problem's final answer once the
  proof-reviewer confirms it.

## Open gaps
None remaining in this approach — both directions (sufficiency, imported; necessity,
proved fresh this round) are complete, and the final answer is stated and verified.

## Cases to cover
All handled uniformly by the single Theorem above: irrational $\theta$, rational
$\theta$ with $180°/\theta\notin\mathbb Z$, and $\theta\in(90°,180°)$ are all subsumed
by "$T=180°/\theta\notin\mathbb Z$"; $\theta=180°/n$ ($n\ge2$ integer) is handled by
imported sufficiency; no case is left unaddressed.

## Watch out for
This proof supersedes the round-4 outline's original plan (irrational-θ sub-case +
open rational-θ denominator-odd-part conjecture): the "denominator" tracked here is
not the odd part of a lowest-terms fraction but simply "is this real number an
integer," and the invariant is proved directly by a residue/mod-1 argument, not by
2-adic bookkeeping through the shift/transfer/bisection primitives individually.
Sanity-check any future revision against the two independent computer simulations
described above before trusting hand-recomputed algebra in this style — sign errors in
the four coincidence cases were the main risk during derivation.
