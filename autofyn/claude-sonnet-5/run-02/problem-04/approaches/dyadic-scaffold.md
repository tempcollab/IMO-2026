## Status
partial

## Approach: dyadic-scaffold

Target: the problem's actual claim — determine exactly the set S ⊆ (0°,180°) of θ for
which Mulan has a finite-step winning strategy against every Shan-Yu play (his choice
of initial triangle AND every subsequent discard choice).

Technique: direct algebraic bookkeeping of the two children produced by a cevian cut,
building two fully rigorous forcing primitives (bisection, transfer) into an explicit
constructive family, paired with the one clean necessity result that is airtight
(θ>90° impossible). This approach is the safe scaffold: it proves S∩(90°,180°)=∅ and
{180°/((2^k+1)·2^j) : k,j≥0} ⊆ S completely, and stops short of the exact upper
characterization of S∩(0°,90°], which is the open gap other approaches attack.

## Approaches tried
- Round 2 (this round): filled in the outline (round 2, `proof-outliner.md`) into a
  complete, fully rigorous proof. Every lemma below is derived from scratch (not
  cited from the outliner's report), every case is settled, and the transfer-move
  validity arithmetic (including the θ=90° boundary) is written out in full, per the
  outline-reviewer's request. Re-verified the core algebraic identities independently
  with sympy (identity ★, transfer-lemma output, bisection double-hit) — all confirmed.
  Outcome: WORKED — this yields a correct, gap-free partial result (necessity θ>90°
  impossible; sufficiency for the full dyadic-scaffold family). The exact
  characterization of S∩(0°,90°] beyond this family remains open and is honestly
  marked as a gap, not conjectured away.

## Current best

**Theorem (this approach).** Let S ⊆ (0°,180°) be the set of angles θ for which Mulan
has a finite-step winning strategy against every play of Shan-Yu. Then:

(a) S ∩ (90°,180°) = ∅ — proved in full below (Necessity Theorem).

(b) {180°/((2^k+1)·2^j) : k,j ∈ ℤ≥0} ⊆ S — proved in full below (Sufficiency Theorem),
by an explicit, finite, Shan-Yu-immune construction from any starting triangle.

The exact value of S ∩ (0°,90°] beyond this countable family is NOT determined by this
approach; see "Open gaps" below. This is a complete, gap-free `partial` result.

---

## Full proof of the partial result

### 0. Setup and notation

Label a triangle by its three (positive, summing to 180°) angles. When Mulan performs
a legal move, she designates one vertex — call its angle $p$ — and a point $X$ in the
open interior of the side opposite that vertex; call the other two vertices $Q,R$ with
angles $q,r$. (The problem phrases the move as "choose a point $P$ on the perimeter,
cut to the opposite vertex"; this is the same move with the point and the fixed vertex
relabeled — we use the fixed-vertex-first labeling throughout since it is more
convenient for angle bookkeeping.) So $p+q+r=180$.

As $X$ ranges over the open segment $QR$, let $x_1 = \angle QPX \in (0,p)$ (the part of
angle $p$ on the $Q$-side of the cut) and let $s = \angle PXQ$. Since $Q,X,R$ are
collinear, $\angle PXR = 180° - s$. In triangle $PXQ$: $x_1 + q + s = 180°$, so
$$s = 180° - x_1 - q.$$
In triangle $PXR$: the angle at $P$ is $p-x_1$, the angle at $R$ is $r$, and the angle
at $X$ is $180°-s = x_1+q$; as a check, $(p-x_1)+r+(x_1+q) = p+q+r = 180°$ ✓.

Using $r+p-x_1 = (180-q)-x_1 = 180-x_1-q = s$, the two children produced by this move
are exactly
$$A = \{q,\; x_1,\; r+p-x_1\} \qquad B = \{r,\; p-x_1,\; q+x_1\},$$
where $A$ is the triangle $PXQ$ and $B$ is the triangle $PXR$. As $X$ ranges
continuously and monotonically over $QR$ from $Q$ to $R$, $x_1$ ranges continuously
and strictly increasingly over the open interval $(0,p)$ by the Intermediate Value
Theorem applied to the (continuous, strictly monotonic in $X$-position) function
$x_1(X)$: $x_1\to 0$ as $X\to Q$, $x_1\to p$ as $X\to R$. Every $x_1\in(0,p)$ is
achieved by exactly one point $X$, so choosing a cut is exactly choosing $x_1\in(0,p)$.
This is the shared bookkeeping every lemma below is built on.

**Identity (★).** For every legal $x_1\in(0,p)$,
$$(r+p-x_1) + (q+x_1) = p+q+r = 180°.$$
*Proof.* Direct algebraic cancellation of $x_1$; re-verified symbolically:
$(r+p-x_1)+(q+x_1) - (p+q+r) = 0$ identically in $x_1$. ∎

(★) says: the two "new" (at-$X$) angles of $A$ and $B$ are always supplementary,
independent of where the cut is made — a restatement of $s + (180°-s) = 180°$.

---

### 1. Necessity: θ > 90° is not forceable

**Lemma 1 (non-obtuse invariant).** If a triangle has all three angles $\le 90°$
("non-obtuse"), then for every legal cut (every choice of apex vertex and every
$x_1\in(0,p)$), at least one of the two children $A,B$ is again non-obtuse (all three
of its angles $\le 90°$).

*Proof.* Suppose $p,q,r\le 90°$ and $x_1\in(0,p)$ is arbitrary. Consider child
$A=\{q,x_1,r+p-x_1\}$. Its first angle is $q\le 90°$ by hypothesis. Its second angle is
$x_1$, and since $x_1 < p \le 90°$, this angle is $<90°$. So the only angle of $A$ that
could exceed $90°$ is the third, $r+p-x_1$. Symmetrically, the only angle of $B$ that
could exceed $90°$ is its third angle, $q+x_1$. By Identity (★), $(r+p-x_1)+(q+x_1) =
180°$; if both exceeded $90°$ their sum would exceed $180°$, a contradiction. Hence at
most one of $\{r+p-x_1, q+x_1\}$ exceeds $90°$, so at least one of $A,B$ has all three
angles $\le 90°$, i.e. is non-obtuse. ∎

Note the argument is fully symmetric in which vertex Mulan designates as the apex
$p$ — it only used $p,q,r\le 90°$ and $x_1\in(0,p)$, both of which hold for *any*
legal move (any choice of vertex to cut opposite, and any cut point on that side).

**Theorem (Necessity).** For every $\theta > 90°$, $\theta \notin S$: Shan-Yu has a
strategy that prevents any angle from ever equaling $\theta$, no matter how Mulan
plays.

*Proof.* Shan-Yu's strategy: (i) start with the equilateral triangle $(60°,60°,60°)$,
which is non-obtuse; (ii) at every subsequent step, after Mulan cuts, keep a child that
is non-obtuse — such a child exists by Lemma 1 applied to the current (non-obtuse, by
induction) triangle, regardless of which vertex/point Mulan chose to cut. By induction
on the number of moves, the triangle is non-obtuse after every move: all its angles are
$\le 90°$. Since $\theta>90°$, no angle of the triangle ever equals $\theta$ (as every
angle present is $\le 90° < \theta$), so under this strategy the game never stops, and
Mulan never wins. Hence $\theta$ is not forceable. ∎

This proves $S \cap (90°,180°) = \varnothing$.

---

### 2. Sufficiency for θ = 90° (direct, one move)

**Lemma 2 (altitude-foot double hit).** From *any* triangle with no angle currently
equal to $90°$, Mulan can make one cut such that, whichever child Shan-Yu keeps, the
kept child has an angle exactly $90°$.

*Proof.* Let $p$ be any angle of the triangle that is $\ge$ the other two (a maximum,
possibly tied); let $q,r$ be the other two. We first show $q,r<90°$ strictly. If
$p\ge 90°$, then $q+r = 180°-p \le 90°$, and since $q,r>0$ each of $q,r$ is strictly
less than $90°$ (each is bounded by the sum $q+r\le 90°$, and cannot equal $90°$ itself
since the other would then be $0°$, impossible for a genuine triangle angle). If
instead $p<90°$, then since $p$ is a maximum, $q\le p <90°$ and $r\le p<90°$. Either
way, $q,r<90°$.

Now use the apex-$p$ parametrization of §0 with this $p,q,r$: $s(x_1) = 180°-x_1-q$ is
a strictly decreasing continuous (indeed affine) function of $x_1$ on $(0,p)$, with
$s\to 180°-q$ as $x_1\to 0^+$ and $s\to 180°-p-q = r$ as $x_1\to p^-$. Since $q<90°$ we
have $180°-q>90°$, and since $r<90°$ we have $r<90°$; so $90°$ lies strictly between
the two endpoint limits $r$ and $180°-q$ of the strictly monotonic continuous function
$s(x_1)$ on $(0,p)$. By the Intermediate Value Theorem there is a unique
$x_1^*\in(0,p)$ with $s(x_1^*)=90°$, i.e. child $A$ has its third angle
$s = r+p-x_1^* = 90°$ (recall $r+p-x_1=s$ from §0). By (★), child $B$'s third angle is
then $q+x_1^* = 180°-90°=90°$. So cutting at $x_1^*$ (the point $X$ = the foot of the
altitude from the max-angle vertex) makes BOTH children $A$ and $B$ contain a $90°$
angle. Whichever Shan-Yu keeps, the game ends with a $90°$ angle present. ∎

**Corollary.** $90° \in S$: from any starting triangle, if it does not already have a
$90°$ angle, Mulan wins in exactly one move by Lemma 2 (if it already has one, she has
already won, in zero moves).

---

### 3. Two adversary-immune forcing primitives

We now build the machinery for the constructive family. Call a target value $a$
**immune-forceable in $n$ moves from a triangle $T$** if Mulan has a specific,
predetermined sequence of $n$ legal cuts (each cut's parameters possibly depending on
which angle-values are already guaranteed present, but not on Shan-Yu's actual
discard history beyond that) such that, after these $n$ moves, for *every* sequence of
discard choices Shan-Yu could make, the surviving triangle has an angle exactly equal
to $a$ (or the game has already ended earlier because $a$ appeared sooner). We prove
below that every forcing step we use has this strong "immune" property — the target
angle appears in the kept triangle *regardless* of which child Shan-Yu keeps — which
is what lets us chain moves without needing to track Shan-Yu's choices at all.

**Lemma 3 (bisection double-hit).** If a triangle currently has an angle equal to $a$
(at some vertex, taken as apex $p=a$), then cutting at $x_1 = a/2$ produces
$A=\{q,a/2,r+a/2\}$ and $B=\{r,a/2,q+a/2\}$: the value $a/2$ appears in *both* children.
Hence $a/2$ is immune-forceable in one further move whenever $a$ is present.

*Proof.* Direct substitution $x_1=p/2=a/2$ into $A=\{q,x_1,r+p-x_1\}$,
$B=\{r,p-x_1,q+x_1\}$: the second entry of $A$ is $a/2$, and the second entry of $B$
is $p-x_1 = a-a/2=a/2$. Both children literally contain the entry $a/2$, independent
of Shan-Yu's choice. (Legality: $x_1=a/2\in(0,a)$ since $a>0$.) ∎

**Corollary (spectator creation).** From ANY starting triangle with angles
$a_0,b_0,c_0$, and any threshold $\eta>0$, Mulan can immune-force an angle value
$<\eta$ to appear, in finitely many moves.

*Proof.* Fix any one starting angle, say $a_0$. By the Archimedean property of the
reals, since $a_0>0,\eta>0$, there is an integer $n$ with $2^n > a_0/\eta$, i.e.
$a_0/2^n < \eta$. Apply Lemma 3 repeatedly to the same lineage: $a_0$ is present at
the start; by induction, if $a_0/2^k$ is present after $k$ applications (guaranteed
regardless of Shan-Yu's discards, since each bisection step is a double hit), one more
bisection (Lemma 3 applied with $a=a_0/2^k$) immune-forces $a_0/2^{k+1}$ after $k+1$
moves. After $n$ moves, $a_0/2^n<\eta$ is present. ∎

**Lemma 4 (transfer).** Fix $\theta_* \le 90°$. Suppose the current triangle has three
angles which we may label $r, u, v$ (with $u+v = 180°-r$) such that $r<\theta_*$ (call
$r$ the "spectator"). Then Mulan has a legal cut such that: one child contains
$\theta_*$ directly (an instant win if $\theta_*$ is the real game target), and the
other child is *exactly* $\{r,\ \theta_*-r,\ 180°-\theta_*\}$ — independent of the
value of the non-spectator, non-apex angle.

*Proof.* Set $p := \max(u,v)$ and $q$ := the other of $\{u,v\}$, and take the apex
vertex to be the one with angle $p$, so $q, r$ are the two "base" angles of the
$x_1$-parametrization of §0.

*Step (i): validity, i.e. $\theta_*-r < p$.* We show $p > \theta_*-r$. Since
$u+v = 180°-r$, we have $p=\max(u,v) \ge (u+v)/2 = (180°-r)/2 = 90° - r/2$. Since
$\theta_*\le 90°$ and $r>0$ strictly (a genuine triangle angle), $\theta_* \le 90° <
90°+r/2$, i.e. $90°-r/2 > \theta_*-r$. Combining, $p \ge 90°-r/2 > \theta_*-r$. So
$p>\theta_*-r$ strictly, for every $\theta_*\in(0°,90°]$ and every $r\in(0,\theta_*)$
— **including the boundary case $\theta_*=90°$ exactly**: there the required
inequality is $90°<90°+r/2$, which holds because $r>0$ strictly; no degeneracy.

*Step (ii): set $x_1 = r+p-\theta_*$.* By Step (i), $x_1 = r+p-\theta_* > r + (\theta_*
-r) - \theta_* = 0$, so $x_1>0$. Also $x_1 < p \iff r-\theta_*<0 \iff r<\theta_*$, which
is exactly the spectator hypothesis. So $x_1\in(0,p)$: this is a legal cut.

*Step (iii): compute the children.* Using the formulas of §0,
$$A = \{q,\ x_1,\ r+p-x_1\}, \qquad r+p-x_1 = r+p-(r+p-\theta_*) = \theta_*,$$
so $A = \{q,\ p+r-\theta_*,\ \theta_*\}$ contains $\theta_*$ exactly (re-verified
symbolically: substituting $x_1=r+p-\theta$ into $r+p-x_1$ gives $\theta$, confirmed by
independent computer-algebra check). And
$$B = \{r,\ p-x_1,\ q+x_1\}, \qquad p-x_1 = \theta_*-r,$$
$$q+x_1 = q + r+p-\theta_* = (p+q+r)-\theta_* = 180°-\theta_*,$$
using $p+q+r=180°$. So $B = \{r,\ \theta_*-r,\ 180°-\theta_*\}$, independent of $q$'s
actual value (also re-verified symbolically). Since $\theta_*\le 90°<180°$ and $r>0$
and $\theta_*-r>0$ (spectator condition) and $180°-\theta_*>0$ (as $\theta_*<180°$),
all three entries of $B$ are positive and sum to $r+(\theta_*-r)+(180°-\theta_*)=180°$,
so $B$ is a genuine triangle. ∎

Note Lemma 4's validity (Step (i)) used only $\theta_*\le90°$ and $r>0$ — it never
depended on the value of $q$ or on which of $u,v$ was picked as apex beyond
"the larger one", so it applies to *any* triangle carrying a spectator $r<\theta_*$,
regardless of its other two angles' actual values. This — combined with the fact that
$A$ is an instant win if reached — makes the move fully adversary-immune: if Shan-Yu
keeps $A$, $\theta_*$ is already present (win, if $\theta_*$ is the true target, or
otherwise irrelevant continuation); if he keeps $B$, the triangle is *exactly* known:
$\{r,\theta_*-r,180°-\theta_*\}$.

---

### 4. The constructive family

**Theorem (Sufficiency).** For every pair of integers $k,j\ge 0$,
$$\Theta_{k,j} := \frac{180°}{(2^k+1)\cdot 2^j} \in S,$$
via an explicit finite (adversary-immune) sequence of moves from any starting
triangle.

*Proof.* We build this in two stages.

**Stage A ($j=0$ case): $\theta_0 := 180°/(2^k+1) \in S$ for every $k\ge 0$.**

From any starting triangle, apply the spectator-creation corollary (with threshold
$\eta=\theta_0$) to immune-force some angle $r<\theta_0$ to appear, in finitely many
moves. (This uses only $\theta_0>0$; no further hypothesis.) Now apply Lemma 4 with
$\theta_* = \theta_0$: since $\theta_0\le 90°$ (as $2^k+1\ge 2$ for $k\ge0$... check
$k=0$: $2^0+1=2$, $\theta_0=90°$; for $k\ge1$, $2^k+1\ge3$, $\theta_0\le60°<90°$; in all
cases $\theta_0\le90°$), Lemma 4 applies. One further move either wins instantly
(child $A$ contains $\theta_0$) or forces the triangle to exactly
$B=\{r,\ \theta_0-r,\ 180°-\theta_0\}$.

We claim $180°-\theta_0 = \theta_0\cdot 2^k$: indeed $180°-\theta_0 =
180°-\tfrac{180°}{2^k+1} = 180°\cdot\tfrac{2^k}{2^k+1} = \theta_0\cdot2^k$. So the
triangle $B$ carries an angle equal to $\theta_0\cdot 2^k$. Apply Lemma 3 (bisection)
$k$ times in succession to this specific angle-lineage: after $i$ bisections
($0\le i\le k$) the value $\theta_0\cdot2^{k-i}$ is immune-forced present (base case
$i=0$: $\theta_0\cdot2^k$ present in $B$, by construction; inductive step: Lemma 3
applied to the present value $\theta_0\cdot2^{k-i}$ immune-forces
$\theta_0\cdot2^{k-i}/2 = \theta_0\cdot2^{k-i-1}$ next). After $k$ bisections
($i=k$), the value $\theta_0\cdot2^0=\theta_0$ is immune-forced present. (For $k=0$,
zero bisections are needed: $B$ already contains $\theta_0\cdot2^0=\theta_0$ directly —
this reproduces the direct one-move Lemma 2 construction as the $k=0$ special case,
consistent with it.)

Every step in this chain (spectator-creation bisections, the transfer move, and the
$k$ closing bisections) is immune to Shan-Yu's choices individually, so the composite
finite sequence guarantees $\theta_0$ appears regardless of all of Shan-Yu's discard
choices throughout. Hence $\theta_0 = 180°/(2^k+1) \in S$.

**Stage B (halving closure): if $\Theta\in S$ via an immune-forcing sequence, then
$\Theta/2\in S$ via an immune-forcing sequence one move longer.**

Let $\Theta$ be immune-forceable in $n$ moves by a sequence of moves $M_1,\dots,M_n$
(as in Stage A's construction, or in general any such sequence built from Lemmas 3–4).
Run exactly the same sequence of moves against Shan-Yu with the ACTUAL game target set
to $\Phi := \Theta/2$ instead of $\Theta$. Since $\Phi\ne\Theta$ (as $\Theta>0$), the
game does not stop merely because $\Theta$ appears (the game only stops when an angle
equal to the *true* target $\Phi$ appears; if $\Phi$ happens to appear earlier than
planned in the middle of the sequence, that is only an earlier win, not a problem).
By the immune-forcing property of $M_1,\dots,M_n$, after these $n$ moves the surviving
triangle has an angle exactly $\Theta$, regardless of Shan-Yu's discards (or the game
already ended earlier with $\Phi$ present, also a win). If the game has not already
ended, apply Lemma 3 once more to this present angle $\Theta$: this immune-forces
$\Theta/2=\Phi$ into the kept triangle, ending the game (since $\Phi$ is now the true
target). This is a valid $(n+1)$-move immune-forcing sequence for $\Phi$. ∎ (Stage B)

**Combining.** By Stage A, $\theta_0=\theta_{k,0} = 180°/(2^k+1) \in S$ for every
$k\ge0$. By Stage B applied $j$ times, $\Theta_{k,j} = \theta_0/2^j = 180°/((2^k+1)
2^j) \in S$ for every $j\ge0$. This proves the theorem for all $k,j\ge0$. ∎

**Concrete check.** For $k=1,j=1$: $\theta_0=180°/3=60°$, $180°-\theta_0=120°=60°\cdot2^1$
(one bisection closes it), giving $\Theta_{1,0}=60°\in S$; one further halving gives
$\Theta_{1,1}=30°\in S$. For $k=2,j=0$: $\theta_0=180°/5=36°$, $180°-36°=144°=36°\cdot4=
36°\cdot2^2$ (two bisections close it), giving $36°\in S$. Both re-verified by direct
symbolic substitution into the formulas of §0 and §3 (all algebraic identities used
above were independently checked with a computer-algebra system; the written proof
above is self-contained and does not rely on that check).

This proves $\{180°/((2^k+1)\cdot2^j) : k,j\ge0\} \subseteq S$, e.g.
$90°,45°,22.5°,\dots$ ($k=0$); $60°,30°,15°,\dots$ ($k=1$); $36°,18°,9°,\dots$ ($k=2$);
$20°,10°,5°,\dots$ ($k=3$); etc — a countably infinite family, all $\le90°$.

---

### 5. Conclusion of this approach

Combining §1 and §4: $S \cap (90°,180°) = \varnothing$ and
$\{180°/((2^k+1)\cdot2^j):k,j\ge0\} \subseteq S \subseteq (0°,90°]$. Both halves are
fully proved above with no remaining gap. The problem asks to determine $S$ exactly;
this approach has NOT determined whether $S\cap(0°,90°]$ equals this family or is
strictly larger (e.g. whether $180°/7°$ or other non-family values lie in $S$), so
Status remains `partial`.

## Open gaps

- **Exact characterization of $S\cap(0°,90°]$.** Is $S = \{180°/((2^k+1)2^j)\}$ exactly
  (the family proved above is then also an upper bound), or is $S$ strictly larger
  (possibly all of $(0°,90°]$, or a larger but still countable/arithmetic set)?
  Computational evidence from sibling approaches (not verified in this approach)
  suggests $180°/7°$ may also be forceable via a mechanism not captured by Lemmas 3–4
  alone (a "third generator" beyond bisection and transfer) — this is exactly the
  question the sibling approaches `corrected-genericity-bound` (attacking necessity),
  `full-interval-hypothesis` and `binary-word-invariant` (attacking sufficiency beyond
  the family) are chartered to resolve. This approach's role is to supply the
  fully-certified floor (both the impossibility bound $\theta\le90°$ and the
  constructive family) that those approaches build on or must not contradict.
- This approach does not address irrational $\theta$ separately (the constructive
  family only produces rational-multiple-of-$180°$ values; whether any irrational
  $\theta\le90°$ is in $S$ is untouched here — resolving it is not needed to establish
  the two inclusions proved above, but is needed for the final full characterization).

## Promotable lemmas

- **Identity (★)**: for a cevian cut of a triangle $(p,q,r)$ from the $p$-vertex at
  parameter $x_1\in(0,p)$, the two children are $A=\{q,x_1,r+p-x_1\}$,
  $B=\{r,p-x_1,q+x_1\}$, and $(r+p-x_1)+(q+x_1)=p+q+r=180°$ identically. Proved in §0.
- **Lemma 1 (non-obtuse invariant)**: if $p,q,r\le90°$ then for every legal cut, at
  least one child has all angles $\le90°$. Proved in §1. Directly gives the Necessity
  Theorem ($S\cap(90°,180°)=\varnothing$).
- **Lemma 2 (altitude-foot double hit)**: from any triangle with no $90°$ angle, one
  specific cut forces $90°$ into both children. Proved in §2. Gives $90°\in S$.
- **Lemma 3 (bisection double-hit)**: cutting the apex of angle $a$ at $x_1=a/2$ forces
  $a/2$ into both children. Proved in §3.
- **Lemma 4 (transfer)**: given a spectator $r<\theta_*\le90°$ among the triangle's
  angles, one specific cut either wins instantly ($\theta_*$ appears) or forces the
  triangle to exactly $\{r,\theta_*-r,180°-\theta_*\}$, for ANY value of the remaining
  angle. Proved in §3, including the boundary case $\theta_*=90°$ handled explicitly.
- **Sufficiency Theorem**: $\{180°/((2^k+1)2^j):k,j\ge0\}\subseteq S$, via the explicit
  Stage A + Stage B (halving-closure) construction in §4.

All five are fully proved with no forward references or unproven steps, and are ready
for the reviewer to certify into `results/imo-2026-04/lemmas/` for reuse by sibling
approaches (in particular `corrected-genericity-bound`, which needs to combine its own
necessity result with this sufficiency family to state a complete characterization).
