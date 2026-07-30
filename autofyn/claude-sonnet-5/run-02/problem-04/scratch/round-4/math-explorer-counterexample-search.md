## imo-2026-04

### Lens
Searched (by hand-derivation + sympy verification) for θ NOT of the form 180°/n that
could nonetheless be forced, and tried to sharpen/close the "necessity" gap flagged in
`current.md`. **No counterexample found; instead I found a clean, rigorous closed-form
argument that closes the necessity gap for the "primitive-move-only" sub-case**, which
is new content beyond what `binary-word-invariant` §5 (informal transcendence heuristic)
and `corrected-genericity-bound` (refuted) established.

### Key finding: exact closure computation (new, verified)

Every "clean" (junk-free, i.e. independent of the adversary's chosen starting angles)
quantity ever producible by the three certified primitives — shift ($a\mapsto a-\theta$),
transfer (resets the clean output to exactly $180°-\theta$, **erasing all history**,
independent of what was "big" beforehand — verified: transfer's third output is always
$(p+q+r)-\theta=180°-\theta$ regardless of $p,q,r$), and bisection ($a\mapsto a/2$) — is
of the closed form
$$x = \frac{180° - (k+1)\theta}{2^A}, \quad k,A \in \mathbb{Z}_{\ge0}.$$

**Proof sketch (verified with sympy, both symbolically and on random shift/halve
sequences for θ=180/7):** transfer always resets the "clean" branch to $y:=180°-\theta$
(re-derived independently: $q+x_1=(p+q+r)-\theta=180-\theta$, no dependence on $p,q,r$
individually — so re-applying transfer to *any* descendant of $y$ just gives $180-\theta$
again, a fixed point, not new information). So the full reachable clean set is exactly
the closure of $\{180-\theta\}$ under $x\mapsto x-\theta$ and $x\mapsto x/2$. Track: after
$A$ halvings (in any order interleaved with $b_i\ge0$ shifts at "level" $i$, i.e. between
the $i$-th and $(i{+}1)$-th halving), the accumulated shift contribution is
$\theta\cdot\sum_i b_i/2^i = \theta\cdot(k/2^A)$ for an **integer** $k=\sum_i b_i 2^{A-i}\ge0$
(each term is an integer since $i\le A$). So $x = y/2^A - \theta k/2^A = [180-(k+1)\theta]/2^A$.

**Setting $x=\theta$:** $180-(k+1)\theta = \theta\cdot2^A \iff 180 = \theta\,(k{+}1{+}2^A)$,
i.e. $\theta = 180°/n$ with $n:=k+1+2^A$, always a positive integer $\ge2$ (take
$k=0,A=0\Rightarrow n=2$). **Every** $n\ge2$ is already achieved at $A=0$ alone (pure
shift chain, $k=n-2$) — so **halving adds no new reachable $n$** beyond what pure
shift-chains already give (matches `binary-word-invariant`'s existing n≥2 construction
exactly, confirming no larger family is hiding in mixed shift/halve orders). The same
computation shows an angle can only equal $2\theta$ (needed for a bisection double-hit)
when $\theta=180/n$ too — so bisection-double-hit never opens a route to a non-$180/n$
target either.

**Conclusion:** *restricted to strategies built only from the three certified primitives
(shift, transfer, bisection)*, the set of forceable $\theta\le90°$ is **exactly**
$\{180°/n : n\ge2\}$ — not just "no example found," but a closed-form proof of this
sub-claim. This is a repaired, corrected version of what `corrected-genericity-bound`
was trying to do with its closure operator $C(V)$ (its bug was omitting shift; this
computation includes shift and gets the right, exactly-matching answer). I verified this
numerically (sympy, random shift/halve orderings, θ=180/7 test) — see commands below;
every path's value has the form $[180-(k{+}1)\theta]/2^A$, never anything else.

### What remains open (the real gap, unchanged in kind but now sharper)

The exhaustive-primitives argument (`binary-word-invariant` §2) proves shift, transfer,
and the two double-hits are the **only single-move mechanisms that force Shan-Yu's hand
directly**. But it does NOT yet rule out an **adaptive branching strategy**: Mulan plays
a "free-choice" cut $x_1$ that puts $\theta$ in neither child (Shan-Yu freely picks), but
she has a winning continuation from **both** possible resulting triangles. My argument
above only bounds the clean-value set reachable via a **fixed sequence** of primitive
moves; it says nothing about whether branching via free-choice cuts as *setup* could let
Mulan reach a wider effective clean set. I could not close this rigorously in this pass,
but I give a genericity heuristic (below) suggesting it doesn't help, matching
`binary-word-invariant`'s own informal argument — this is not new, but I convinced myself
it's not a cheap loophole: a free-choice cut's children are *still* affine-in-$(p_0,q_0,
\theta,180)$ with rational coefficients (the cut formula is affine in $x_1$ and the
current angles), so the *same* closure argument (only clean values reachable are
$180-k\theta$ chains, since transfer/shift/bisect are still the only forcing ops
available in each branch) applies recursively to each branch. A free-choice cut only
ever *adds* a new junk quantity (an arbitrary chosen $\varphi$), never removes the need
to eventually clean it via transfer (which erases whichever slot isn't $r$/spectator,
snapping back to $180-\theta$ regardless). I did not find a way for free-choice branching
to produce a clean value other than $180-k\theta$ in a few hand-worked small examples
(depth ≤3), but a fully rigorous proof of "free-choice cuts never help" (point (i) in
`binary-word-invariant`'s Section 5) is still missing.

### Cheap-kill search: no counterexample θ found

Tried explicit non-$180/n$ candidates: $\theta=72°=180\cdot\frac{2}{5}$,
$\theta=40°=180\cdot\frac29$, $\theta=180\cdot\frac37=\frac{540}7°$: for each, solving
$180=\theta(k+1+2^A)$ for nonneg integers $k,A$ has no solution (since $180/\theta=5/2,
9/2,7/3$ are not integers and $k+1+2^A$ is always a positive integer) — so **none of
these are reachable via primitives**, consistent with hypothesis (a). I did not find any
rational $p/q$ ($p>1$) example that breaks the pattern.

**On irrational θ:** the same closure computation shows every clean value producible is
$\mathbb{Q}(\theta)$-affine with the specific integer-parametrized form above; if
$\theta$ is irrational, $180/\theta\notin\mathbb{Q}$ so no $(k,A)$ ever solves the
equation — consistent with `binary-word-invariant`'s note that irrational θ should be
unreachable, now backed by the same closed-form rather than just "the mechanism only
produces rational-in-θ combinations."

### Candidate technique(s) for the outliner
- **Repair `corrected-genericity-bound` directly using the closed-form above** — this
  *is* the repair the current.md's "Next round should (1)" step asked for; I've done the
  computation, just need it written up rigorously (induction on move count, formalize the
  "$k=\sum b_i2^{A-i}$ is a nonneg integer" claim) and — critically — combined with an
  argument that free-choice (non-forcing) branching moves cannot escape this closure
  (the still-open gap).
- **Invariant/monovariant + closure-of-generators technique** (KB "Invariant /
  monovariant", KB Meta-Strategy "prune before you compute"): exactly the shape of this
  argument — an algebraic closure computation showing a generator set's reachable set is
  precisely characterized.
- For the remaining branching gap: consider a **potential/valuation argument** — e.g.
  track $v$ = "the coefficient vector of the present angles in the basis
  $\{p_0,q_0,1,\theta\}$, or more precisely whether ANY present angle is clean" as a
  monovariant across arbitrary (not just primitive) moves, and show a free-choice move
  can never *create* a second clean quantity beyond what transfer already gives — this
  would need the cut formula applied to a general (junk, junk) pair, not just to
  (clean, junk) pairs as classified in §2.

### Knowledge-base entries to use
- **Invariant / monovariant** (`knowledge_base.md` line ~191): directly the technique
  needed to finish necessity — find the quantity that never changes/only moves through a
  restricted set under every legal cut (not just the four primitives).
- **Meta-Strategy "prune before you compute"** (line ~244): a size/multiplicity argument
  (here: rational-coefficient-denominator tracking, i.e. a $v_2$-style argument on the
  power of 2 in the denominator) is exactly the cheap structural tool that produced the
  closed form above, before any heavy casework.

### Analogous past problems (cruxes)
- **`aimo-0564`** (combinatorics, `induction-and-construction` subtopic; ISL-style
  "Lucy's tuples" problem — smallest generating set under `+` and `∨` closure to reach
  every integer tuple). Crux move: *"To prove a closure process (generated from seeds by
  given operations) cannot reach every element, find a homogeneous pairwise inequality
  that every operation preserves."* This is genuinely analogous in **shape**: our problem
  is exactly "which θ are reachable under the closure of {shift, transfer, bisect}", and
  the technique that would close the gap here is the same kind of "find an invariant/
  inequality preserved by every legal operation" argument (not a specific formula import
  — the operations are unrelated — but the proof *strategy* is a direct match: identify a
  closure operator, then either exhibit generators for everything, or find an invariant
  no generator can escape). Worth reading in full for the *style* of a rigorous
  closure-invariant proof (`past_problems_database.json`, `problem_id=aimo-0564`).
- No other crux in `games-and-strategy` or elsewhere in the corpus closely resembles the
  triangle-cutting mechanic itself (checked all 39 `combinatorics/games-and-strategy`
  entries for geometric/angle/cutting keywords — only generic pairing/strategy-stealing
  ideas turned up, none analogous to the cevian-cut affine-closure structure here).

### Prior progress
{180°/n : n≥2} ⊆ S ⊆ (0°,90°] (certified, see `current.md`). This round's addition: the
upper bound S ⊆ {180°/n} is now **proved** for the restricted class of "primitive-only"
Mulan strategies (a genuinely new, verified sub-result, not previously written down in
closed form) — reduces the open gap strictly to ruling out free-choice/adaptive
branching, rather than leaving the entire necessity direction as an unformalized
heuristic.

### Dead ends (do not retry)
- `corrected-genericity-bound`'s original closure $C(V)$ using only {halve, reflect}
  (no shift) — refuted (misses shift move entirely, wrongly excludes 180/7°). Do NOT
  reintroduce a "reflect" ($a\mapsto V-a$) generator; the correct third generator is
  **shift** ($a\mapsto a-\theta$), not reflection — the reflect move doesn't correspond
  to any certified primitive in the actual game (transfer's role already subsumes what
  reflect was trying to model, and it resets to a fixed point, it doesn't generate a
  ladder).
- Searching for non-$180/n$ candidates like 72°, 40°, 540/7° as forceable via
  shift/transfer/bisect chains: refuted by the closed-form above — none are reachable,
  no need to re-search these numerically again.

### Small-case / intuition notes (labeled conjecture where unproved)
- **Proved this round:** within primitive-only play, reachable clean angles are exactly
  $\{[180-(k+1)\theta]/2^A : k,A\ge0\}$, and this hits $\theta$ itself iff $\theta=180/n$,
  $n\ge2$ integer.
- **Conjecture (unchanged from `binary-word-invariant`):** S = {180°/n : n≥2} exactly.
  Now resting on a narrower, better-isolated gap: whether adaptive branching through
  non-forcing cuts can escape the closure. All hand-explored small branching examples
  (depth ≤3) failed to produce anything new, consistent with the conjecture, but this is
  not a proof.
- Verification commands used (sympy, exact `Rational`/symbolic arithmetic): manual
  chaining of `transfer` then `shift`/`shift` symbolically confirmed
  `(180-2*theta, ...)`, `(180-3*theta, ...)` and never anything off the $180-k\theta$
  ladder; random 6-move shift/halve sequences on θ=180/7 always landed on values of the
  exact predicted closed form (including negative/invalid ones when validity constraints
  would be violated, which is expected and irrelevant to the algebraic closure claim).
