## Status
unsolved

## Approach: backward-induction-transcendence (round 4, new)

Target: the problem's actual claim — S = {180°/n : n ∈ ℤ, n≥2} exactly (full
characterization; sufficiency imported from `lemmas/theta-180-over-n-forceable.md`,
necessity is this approach's job, attacked via a structurally different route from
`corrected-genericity-bound`).

Technique: finite backward induction on Mulan's assumed winning strategy tree, combined
with a transcendence-degree / field-extension argument. Unlike `corrected-genericity-bound`,
which forward-propagates a hand-classified "junk coefficient" through named move types,
this approach inducts **backward from the tree's leaves**, using only the raw affine
structure of the cut formula at each node — so it is structurally less likely to silently
omit a generator (the exact class of bug that killed two prior necessity attempts in this
workspace: `corrected-genericity-bound`'s round-2 version and `full-interval-hypothesis`,
both of which built a hand-enumerated move list that missed the shift primitive).

### 0. Setup (shared, imported as-is)

Reuse without re-proof: `lemmas/cut-formula.md`, `lemmas/non-obtuse-invariant.md`,
`lemmas/double-hit-primitives.md`, `lemmas/transfer-and-shift-moves.md`,
`lemmas/theta-180-over-n-forceable.md`.

### 1. The winning strategy tree

Suppose θ∈S. Since Mulan forces a win in finitely many steps against *every* Shan-Yu
reply (this is the problem's own definition of "forceable"), fix an actual finite
strategy tree $T$: a finite tree of depth $N$ where each internal node is a triangle with
a chosen cut $x_1$, its two children are the resulting triangles $A,B$ (Shan-Yu may
discard either, so both must be handled — either a leaf itself, or the root of a further
subtree of $T$), and every leaf's triangle contains θ.

### 2. Coefficient-∈{0,±1} fact (cheap, general — no hand-built list)

From `lemmas/cut-formula.md`'s children $A=\{q,x_1,r+p-x_1\}$, $B=\{r,p-x_1,q+x_1\}$:
every "new" entry (i.e. every entry that is not literally carried over unchanged from the
parent) is affine in $x_1$ with coefficient in $\{0,+1,-1\}$ ($x_1$ itself: coeff $+1$;
$r+p-x_1$: coeff $-1$; $p-x_1$: coeff $-1$; $q+x_1$: coeff $+1$). So at any leaf where θ
is the entry newly produced by that branch's final move, back-solving "entry $=\theta$"
forces $x_1$ into exactly one of $\{\theta,\ r+p-\theta,\ p-\theta,\ \theta-q\}$ —
**reproducing the same four primitive families as `lemmas/double-hit-primitives.md` /
`lemmas/transfer-and-shift-moves.md`, but derived fresh from the raw affine structure at
each leaf, not asserted from a hand-built list.** This is the structural safeguard: any
future necessity argument that tries to enumerate "the ways to win" by hand risks missing
a case (as happened twice already); this derivation instead falls straight out of reading
off the coefficients, at every leaf, mechanically.

### 3. Shan-Yu's adversarial start and the field tower

Fix Shan-Yu's start $(p_0,q_0,r_0)$ with $p_0,q_0>0$ algebraically independent
transcendentals over $\mathbb Q(\theta)$ (identical construction to
`corrected-genericity-bound` §1 — imported, not reproved independently, since it is not
itself in dispute). For each node $i$ of $T$ (in particular each node along a root-to-leaf
path), define
$$K_i := \mathbb Q(\theta,p_0,q_0)(\text{all angles present at node }i).$$
$K_0 = \mathbb Q(\theta,p_0,q_0)$ (root); $K_i$ grows (weakly) along any root-to-node path
as angles accumulate, since each new angle is built from previous ones and $x_1$.

### 4. WLOG-$x_1\in K_i$ lemma — the genuinely new, hard step

**Round-5 revision.** The lemma below is reformulated as a single, precisely-stated
strong induction (one IH, stated once, indexed by a well-founded integer measure — no
"minimality of $T$" needed anywhere). This closes exactly the two gaps the round-4
outline flagged: (a) the informal "no NEW transcendental introduced, chained across
levels" step is replaced by an explicit field-containment chain proved by strong
induction on subtree size; (b) the vague "minimality of $T$" contradiction is replaced
by an explicit **constructive bottom-up substitution**, so no minimality hypothesis on
$T$ is needed at all — the lemma is proved for *every* winning tree, not just a
minimal one. **One genuine sub-gap remains** (Case B below, "$x_1$ algebraic over
$K_i$ but not in $K_i$") — this is the same open technical point flagged in
`corrected-genericity-bound`, left as an open shared import, not attacked fresh here.

**Setup restated.** For a node $i$ of the finite tree $T$, let $n_i\in\mathbb Z_{\ge1}$
denote the number of internal (cut) nodes in the subtree of $T$ rooted at $i$,
including $i$ itself. This is a well-defined positive integer since $T$ is finite, and
$n_i>n_j$ for every child $j$ of $i$ (a subtree rooted at $i$ properly contains the
subtrees rooted at its children). We prove, by strong induction on $n_i$:

**IH($i$).** Either (i) $x_1$ used at node $i$ lies in $K_i$ — and moreover the whole
subtree rooted at $i$ can be taken (after possibly replacing $x_1$ at $i$, but keeping
the triangle *entering* $i$ from its parent unchanged) to be one in which $x_1\in K_j$
for **every** node $j$ in that subtree; or (ii) the construction below gets stuck at
some node $j$ in the subtree because $x_1$ at $j$ is algebraic over $K_j$ but not a
member of $K_j$ (Case B) — an honestly reported gap, not a contradiction.

*Base case, $n_i=1$ (both children of $i$ are already leaves — i.e. both $A$ and $B$
already contain θ without further cuts).* By §2's coefficient computation applied to
whichever of $A$'s or $B$'s new entries equals θ, $x_1\in\{\theta,\,r+p-\theta,\,
p-\theta,\,\theta-q\}$, and $\theta,p,q,r$ are all $\in K_i$ by definition of $K_i$
(the parent triangle's own angles, plus θ). So $x_1\in K_i$ automatically: case (i) of
IH($i$) holds with no substitution needed.

*Inductive step, $n_i=N>1$.* Node $i$ has children $A,B$; at least one is not already a
leaf (else $n_i=1$). For each non-leaf child, its own subtree has strictly smaller
$n$-value, so IH holds for every node in it by the strong induction hypothesis. We may
assume (working bottom-up, i.e. having *already* replaced each non-leaf child's subtree
by the case-(i) version supplied by IH, before treating node $i$) that in fact **every**
node $j$ properly below $i$ already satisfies $x_1$-at-$j$ $\in K_j$ literally (not just
"by IH" abstractly — this is the already-constructed object at this stage), unless the
construction got stuck at Case B somewhere below, in which case IH($i$) reports (ii)
and we stop.

Assume no Case B below $i$. Suppose, for contradiction of case (i), that $x_1$ at node
$i$ itself is $\notin K_i$.

*Field-containment chain.* Fix any leaf $L$ in the subtree rooted at $i$, reached via
the path $i=n_0,n_1,\dots,n_r=L$ with cut values $x_1=y_0$ (at $i$), $y_1,\dots,
y_{r-1}$ (at $n_1,\dots,n_{r-1}$; all already known $\in K_{n_1},\dots,K_{n_{r-1}}$
respectively, by the "already cleaned below $i$" assumption above). By
`lemmas/cut-formula.md`, the angles present at $n_{k+1}$ are, in every case, obtained
from the angles at $n_k$ by an affine map of $y_k$ with coefficient $\pm1$ (§2), so
$$K_{n_{k+1}}\subseteq K_{n_k}(y_k)\qquad(k=0,\dots,r-1).$$
Since $y_1\in K_{n_1}\subseteq K_{n_0}(y_0)=K_i(x_1)$, and inductively (finite
induction on $k=1,\dots,r-1$, using only already-established containments, no further
appeal to IH needed): if $K_{n_k}\subseteq K_i(x_1)$ then $y_k\in K_{n_k}\subseteq
K_i(x_1)$, so $K_{n_{k+1}}\subseteq K_{n_k}(y_k)\subseteq K_i(x_1)(y_k)=K_i(x_1)$ (as
$y_k$ is already an element of $K_i(x_1)$, adjoining it changes nothing). Hence
$$K_{n_k}\subseteq K_i(x_1)\text{ for every }k=0,\dots,r,$$
in particular $K_L\subseteq K_i(x_1)$: **every angle present at every node of the
subtree — not merely the designated θ-hit — is an element of $K_i(x_1)$.** This is the
precise, formal replacement for the informal "no new transcendental introduced,
chained across levels" step: it is a finite chain of field containments, each link
justified by the cut formula, with no appeal to anything beyond already-established
facts at each step.

*Case A: $x_1$ transcendental over $K_i$.* Then $K_i(x_1)\cong K_i(X)$, the rational
function field in a formal indeterminate $X$, via $x_1\leftrightarrow X$. For *every*
leaf $L'$ in the subtree rooted at $i$ (finitely many), pick a designated entry
$E_{L'}(X)\in K_i(X)$ (via the isomorphism, using that every angle at $L'$ lies in
$K_i(x_1)$, shown above) equal to θ at $X=x_1$. Write $E_{L'}=N_{L'}/D_{L'}$ in lowest
terms, $N_{L'},D_{L'}\in K_i[X]$. Then $N_{L'}(x_1)-\theta D_{L'}(x_1)=0$. If the
polynomial $N_{L'}(Y)-\theta D_{L'}(Y)\in K_i[Y]$ is **not** the zero polynomial, this
says $x_1$ is a root of a nonzero polynomial over $K_i$, i.e. $x_1$ is algebraic over
$K_i$ — contradicting the case-A hypothesis that $x_1$ is transcendental over $K_i$.
So the polynomial **must** be identically zero, i.e. $E_{L'}(X)\equiv\theta$
identically as an element of $K_i(X)$ (a rational-function identity, not merely an
equality at $X=x_1$). This holds for **every** leaf $L'$ of the subtree simultaneously
(the argument used nothing leaf-specific beyond the existence of $E_{L'}$, so it
applies to each of the finitely many leaves in turn).

*Constructive bottom-up substitution (replaces "minimality of $T$").* Every node $j$ in
the subtree rooted at $i$ has all its angles given by specific rational functions of
$X$ over $K_i$ (shown above), and the *combinatorial shape* of the subtree (which
vertex is cut at each node, and both children present at every non-leaf node so that
either of Shan-Yu's discards is covered) does not depend on the numeric value of $X$.
The finitely many rational functions involved (angle-values at every node, and the
$E_{L'}$'s) have finitely many poles in $K_i$'s algebraic closure, hence finitely many
real poles. Also, at $X=x_1$, every legality constraint "cut value $y_k(X)\in
(0,\,\text{cut-vertex-angle}(X))$" holds as a *strict* inequality (since the original
subtree was legal), and each such constraint, together with "$X$ avoids the finite pole
set", defines a finite intersection of open conditions in $X$ (near $x_1$, using
continuity of rational functions away from their poles) — hence there is an open real
interval $U\ni x_1$ on which **all** of these finitely many open conditions hold
simultaneously. Since $K_i$ contains the (nonzero, positive) cut-vertex angle $p$ at
node $i$, it contains $p\cdot\mathbb Q\subset K_i\cap(0,p)$, a set of rational
multiples of $p$ that is dense in $\mathbb R$ (as $\mathbb Q$ is dense in $\mathbb R$
and $p\ne0$); intersecting with the nonempty open set $U\cap(0,p)$ (nonempty since
$x_1\in(0,p)\cap U$) yields infinitely many elements of $K_i$, so in particular at
least one element $x_1'\in K_i\cap U\cap(0,p)$ exists.

Substituting $X=x_1'$ into every one of the (finitely many) rational functions
describing the subtree's node-angles produces a **new**, fully legal (all range
constraints hold, by choice of $U$), fully numeric assignment at every node of the
subtree, respecting the cut formula at each step (since substitution $X\mapsto x_1'$ is
a field homomorphism $K_i(X)\to K_i$ fixing $K_i$, and the cut-formula relations among
the node-angles are polynomial/rational identities in $K_i(X)$, hence preserved under
any such homomorphism) — and at every leaf $L'$, the designated entry
$E_{L'}(x_1')=\theta$ still holds (as $E_{L'}\equiv\theta$ identically). So this
substituted subtree is **still a winning subtree** (same combinatorial shape, every
leaf still shows θ), and now literally has $x_1'\in K_i$ at node $i$ (as $x_1'\in K_i$
by construction), with every deeper node $j$'s angle values now given by the same
rational functions evaluated at $x_1'$ instead of $x_1$ — in particular each such
node's own cut value $y_k(x_1')$ is manifestly an element of $K_i(x_1')=K_i$ (since
$x_1'\in K_i$), hence certainly of the correspondingly-updated $K_j$ (which now equals
$K_i$-generated-by-the-new-angles, all in $K_i$). So IH($i$) case (i) holds, with the
required subtree replacement exhibited explicitly.

*Case B: $x_1$ is algebraic over $K_i$ but $x_1\notin K_i$.* Here $K_i(x_1)$ is a
proper finite extension, not (via the argument above) isomorphic to a pure rational
function field, so the "evaluate at $X=x_1$ forces the polynomial to vanish identically"
argument does not apply verbatim (a nonzero polynomial over $K_i$ genuinely can vanish
at an algebraic-but-not-in-$K_i$ element). Resolving this sub-case requires a
minimal-polynomial / degree-counting argument along the lines attempted in
`corrected-genericity-bound` §4's tightened sub-case — that argument is not yet
established as fully rigorous there either. **This is the one honest remaining gap**:
IH($i$) records this as outcome (ii) and the induction reports the obstruction rather
than papering over it.

**Status of §4 after this round's revision.** The induction is now a clean, single,
formally-stated strong induction (measure $n_i$ = subtree size) with:
- Base case: fully rigorous (§2, unchanged).
- Case A (transcendental $x_1$): **now fully rigorous** — the field-containment chain,
  the simultaneous-leaf-constancy argument, and the constructive (not minimality-based)
  bottom-up substitution are all spelled out above with no informal step remaining.
- Case B (algebraic, not in $K_i$): **still open**, explicitly identified as the same
  gap `corrected-genericity-bound` has in its own §4 sub-case. Not attacked fresh here,
  per this round's instructions — it is an open shared import, and closing it would
  simultaneously close both approaches' §4.

So §4 is reduced, cleanly, to exactly one remaining open sub-case (Case B), with the
"minimality of $T$" issue eliminated entirely (replaced by direct construction) and the
"chaining across levels" issue eliminated entirely (replaced by an explicit finite
field-containment chain). This is real progress: the lemma's *hard part* — as
originally flagged — is now down to a single, precisely-isolated open sub-case shared
with `corrected-genericity-bound`, rather than a globally-informal argument.

### 5. Reduction to the shared closure computation

With $x_1\in K_i$ established at every used node (§4, once proved), run the SAME
junk-coefficient bookkeeping as `corrected-genericity-bound` §§2–3,5–6: represent every
angle as $A+B\theta+Cp_0+Dq_0$, track "clean" ($C=D=0$) vs "junk," show transfer is the
only clean-injecting move, and that the reachable clean set is exactly
$$C^*(\theta) := \text{closure of }\{180°-\theta\}\text{ under (halve) and (shift-by-θ)},$$
which — by `corrected-genericity-bound` §5's closed-form lemma (imported once proved
there, or re-derived independently here as a cross-check) — contains θ or $2\theta$ iff
$\theta=180°/n$, $n\ge2$.

### 6. Conclusion

Combining §§1–5 with `lemmas/non-obtuse-invariant.md` and imported sufficiency:
$$\theta\in S \implies \theta=180°/n,\ n\ge2 \implies S=\{180°/n:n\ge2\}.$$

## Key lemmas (claim + mechanism)

- **Coefficient-∈{0,±1} fact (§2)** — trivial from direct inspection of the cut formula,
  but load-bearing: it re-derives the four primitive families at any leaf mechanically,
  without relying on a hand-enumerated list (the exact bug class that broke two prior
  attempts).
- **WLOG-$x_1\in K_i$ lemma (§4)** — because a transcendental-over-$K_i$ (or non-$K_i$
  algebraic) choice of $x_1$ can only contribute a coefficient that must vanish in any
  identity forced to equal the fixed value θ (or $2^m\theta$), by the affine structure of
  the cut formula propagated through the subtree — **this is the crux of the whole
  approach and is currently only a proof sketch, not a fully rigorous induction.**
- Everything in §5 is imported/shared with `corrected-genericity-bound`, not re-derived
  independently by default (though the builder may re-derive as a cross-check if time
  permits).

## Open gaps

- §4 (the WLOG-$x_1\in K_i$ lemma) is the entire open content of this approach — currently
  a proof sketch with an informally-stated inductive step ("no new transcendental
  introduced below node $i$"), not a rigorous induction. This is the primary work for the
  builder.
- §5 inherits `corrected-genericity-bound`'s own open gap (the $C^*(\theta)$ closed-form
  induction) unless that lemma is proved and certified first, in which case it should be
  imported rather than re-derived.
- The "minimality of $T$" move used in §4's contradiction (a branch with a vanishing
  θ-coefficient means $x_1$ could be replaced by any $K_i$-value, contradicting
  minimality) needs to be stated more carefully — minimality of what, exactly (fewest
  moves? smallest tree by some other measure?) — and checked that such a replacement
  really produces a smaller/different tree that still wins (not just a change that
  happens not to break anything already proved).

## Cases to cover
θ=90° (handled directly by `lemmas/double-hit-primitives.md`'s D2, independent of the
closure computation); θ=180°/n rational general case (main content, §§4–5); θ irrational
(automatic once §5's closed form is established: no integer $n$ solves $180=\theta n$ for
irrational θ).

## Watch out for
This approach's §5 overlaps substantially with `corrected-genericity-bound` (same
clean/junk bookkeeping, same target closure $C^*(\theta)$). The genuine novelty is
entirely in §4's backward-induction organization of "which $x_1$ actually matter," a
different, potentially more robust route to the same fact that
`corrected-genericity-bound` §4 tries to establish by direct forward case-splitting. If
`corrected-genericity-bound` §4 is proved rigorously first, this approach's unique
contribution shrinks to a cross-check; if it stalls, this is the fallback route to the
same gap. Do not treat the two approaches' progress as fully independent evidence when
ranking — they share a wall (the "wild $x_1$" / non-affine-move exclusion) and could fail
together if that wall turns out to be genuinely hard.

## Current best

No new claim proved yet this round beyond what is imported. §2 (coefficient-∈{0,±1}
fact) is a trivial, essentially-certified re-derivation and can be promoted to a shared
lemma immediately once a builder writes it up formally (it doesn't depend on anything
open). §4 and §5 remain open.

## Full proof

(Not applicable — Status is `unsolved`: no complete, gap-free argument yet, only an
outline with one major open lemma (§4) and one imported open lemma (§5, shared with
`corrected-genericity-bound`).)
