## Status
unsolved

## Approaches tried
- **equalization-potential-bound (round 1, this round).** Directly resolved the
  outline-reviewer's circularity gate: *does a genuinely rank-only,
  configuration-independent linear weight vector `w_1,...,w_{n+1}` exist that
  turns the two-stage adversarial game into a one-shot LP `max_A Σ w_i p_i`,
  tight at the conjectured geometric optimum?* **Answer: no — proved
  impossible in general, with a complete argument (not just a suspicion).**
  The obstruction is structural (an interior-point-vs-vertex argument for
  linear functionals on the ordered simplex, Lemma D below), confirmed
  concretely by an exact computation at `n=1`. Every non-trivial way of
  trying to rescue the idea (fixed single strategy; strategy-independent
  inequality-only bound; case-adaptive strategy) is shown to either (a) give
  an invalid bound, or (b) collapse into either the same casework the other
  approaches already do, or (c) become a tautological restatement of the
  theorem itself. This is a genuine dead end for the "single global linear
  functional" mechanism as conceived in the outline. **Verdict: dead-end,
  reported honestly per the outline's own instruction; do not resurrect
  without a fundamentally different weighting mechanism than a fixed
  per-rank linear functional.**

## Current best
Nothing new towards the theorem's proof (the upper bound `c(n) ≤ 2^n/(2^{n+1}-1)`
is NOT established by this approach). What is established, in full rigor, is
the negative/structural result described below, which retires this approach's
central idea and explains precisely why. `geometric-dominance-construction`
and `recursive-embedding-induction` remain the two live approaches carrying
the actual proof forward; this file documents why their casework cannot be
shortcut by a global linear weighting.

## The setup, precisely

Fix `n`. By the shared claiming-phase reduction (Lemma 1, proved by strong
induction in `math-explorer-gamevalue.md` / imported by all approaches): once
the final multiset of pieces is fixed and sorted in decreasing order
`b_1 ≥ b_2 ≥ ... ≥ b_m`, the value Liu Bang obtains under optimal alternating
greedy play by both sides is `oddrank(B) := b_1 + b_3 + b_5 + ...` (the sum of
the odd-indexed pieces). So

`c(n) = max_A min_B oddrank(B)`,

where `A` ranges over Liu Bang's choices (equivalently, over the induced
sorted piece-list `p_1 ≥ p_2 ≥ ... ≥ p_{n+1} ≥ 0`, `Σp_i = 1`, coming from at
most `n` marks — WLOG exactly `n` marks and `n+1` positive pieces, since
using fewer marks can only be weakly worse for Liu Bang, a monotonicity fact
used identically in all approaches and not re-derived here), and `B` ranges
over all further refinements of `A` obtainable by Xiang Yu's ≤ n additional
marks.

Write `Δ_n := {p ∈ R^{n+1} : p_1 ≥ p_2 ≥ ... ≥ p_{n+1} ≥ 0, Σ p_i = 1}` for
the **ordered simplex** of feasible Liu Bang configurations, and
`V(A) := min_B oddrank(B)` for the *value function* Xiang Yu forces on
configuration `A`. Then `c(n) = max_{A ∈ Δ_n} V(A)`.

The approach's proposed mechanism was: find constants `w_1,...,w_{n+1}`
(depending only on rank `i`, not on the actual lengths `p_i`) such that
`Σ w_i p_i` is a valid, tight upper bound for `V(A)` uniformly over `Δ_n`,
turning the two-player game into a one-shot linear program over `Δ_n`. We now
resolve whether such `w` exists.

## Lemma D (interior maximum forces a linear functional to be constant)

**Statement.** Let `P` be a polytope of dimension `d ≥ 1` (i.e. with
nonempty relative interior in its affine hull), and let `f(x) = Σ w_i x_i`
be an affine-linear functional (restricted to the affine hull of `P`). If
`f` attains its maximum over `P` at a point `x^* ∈ relint(P)` (the relative
interior), then `f` is constant on all of `P`.

**Proof.** Work inside the affine hull `H` of `P` (dimension `d`), so `f`
restricted to `H` is an affine function of `d` free coordinates; write its
gradient (as a function on `H`) as `g ∈ R^d`. Suppose for contradiction
`g ≠ 0`. Since `x^* ∈ relint(P)`, there is `ε_0 > 0` such that the ball of
radius `ε_0` around `x^*` inside `H` is entirely contained in `P` (this is
the definition of relative interior for a polytope: every point of
`relint(P)` has a full-dimensional neighborhood, within the affine hull,
contained in `P`). Take `ε = ε_0 / (2\|g\|)` and set `x' = x^* + ε g ∈ P`
(valid since `\|x' - x^*\| = ε\|g\| < ε_0`). Then
`f(x') = f(x^*) + ε \|g\|^2 > f(x^*)`, since `\|g\|^2 > 0` and `ε > 0`,
contradicting that `x^*` is a maximizer of `f` over `P`. Hence `g = 0`, i.e.
`f` is constant on `H`, in particular on `P`. ∎

## Lemma E (the ordered simplex is full-dimensional and the geometric point is a strict interior point)

**Statement.** `Δ_n` is an `n`-dimensional polytope (inside the hyperplane
`Σp_i = 1` in `R^{n+1}`), and the conjectured optimal configuration
`p^*_i = 2^{n+1-i}/(2^{n+1}-1)` (`i = 1,...,n+1`) lies in its relative
interior.

**Proof.** `Δ_n` is cut out inside the hyperplane `H = \{Σp_i=1\}` (which has
dimension `n`) by the `n` inequalities `p_i \ge p_{i+1}` (`i=1,\dots,n`) and
the one inequality `p_{n+1}\ge 0`. It is a standard fact (and easy to check
directly) that `Δ_n` is the convex hull of the `n+1` points
`V_k = (1/k,\dots,1/k,0,\dots,0)` (`k` copies of `1/k` then zeros), for
`k=1,\dots,n+1`: any `p\in\Delta_n` can be written via its "sorted partial
sums" as a convex combination of the `V_k` (this is exactly the classical
description of the majorization/rearrangement polytope; concretely,
`p = Σ_{k=1}^{n+1} λ_k V_k` with `λ_k = k(p_k-p_{k+1}) \ge 0` for `k<n+1`
and `λ_{n+1}=(n+1)p_{n+1}\ge 0`, and one checks `Σλ_k=1` and the combination
reproduces `p` coordinate by coordinate by an Abel-summation identity). Since
these `n+1` points affinely span `H` (their pairwise differences
`V_k - V_{k+1}` are easily checked to be linearly independent for
`k=1,\dots,n`), `Δ_n` is full-dimensional in `H`, i.e. `dim(Δ_n) = n`.

For the geometric configuration `p^*`: since `2^{n+1-i}` is strictly
decreasing in `i`, we have `p^*_1 > p^*_2 > \dots > p^*_{n+1} > 0`, i.e.
**every** defining inequality of `Δ_n` is *strict* at `p^*`. For a polytope
cut out by finitely many linear inequalities inside its affine hull, a point
satisfying every defining inequality strictly is automatically in the
relative interior (a standard fact: near such a point, all the inequality
constraints have positive slack, so a whole ball around it, within `H`, stays
feasible). Hence `p^* \in relint(\Delta_n)`. ∎

## The obstruction: a valid, tight linear bound would be forced to be either invalid or tautological

Suppose, aiming for a contradiction with the approach's stated goal, that
there exist rank-only weights `w = (w_1,\dots,w_{n+1})` such that:

(i) **Validity:** `Σ w_i p_i \ge V(A)` for every `A = (p_1,\dots,p_{n+1}) \in \Delta_n`;

(ii) **Non-looseness at the optimum:** the resulting bound recovers
`c(n)` exactly, i.e. `max_{A\in\Delta_n} Σ w_i p_i = c(n)`.

(These are precisely the two properties the outline needs from `w` in order
for "one-shot LP over `w`" to be a genuine alternative route to proving
`c(n) \le 2^n/(2^{n+1}-1)`; weaker properties give a bound that is not tight,
hence useless for pinning down `c(n)` exactly.)

We already know, independently, from the matching lower-bound construction
(the explicit geometric configuration, whose value under optimal Xiang-Yu
play is computed directly and equals `c(n) = 2^n/(2^{n+1}-1)$ — this is the
content of the *other* approaches' Lemma 2/3, not re-derived here, and is not
in dispute) that `V(p^*) = c(n)`.

Combining with (i): `c(n) = V(p^*) \le Σ w_i p^*_i \le \max_{A} Σ w_i p_i`.
Combining with (ii): `\max_A Σ w_i p_i = c(n)`. Hence every inequality above
is forced to be an **equality**:
`Σ w_i p^*_i = c(n) = \max_{A\in\Delta_n} Σ w_i p_i`.

In particular, the linear functional `f(A) := Σ w_i p_i` **attains its own
maximum over `Δ_n` exactly at `A = p^*`.** By Lemma E, `p^*\in relint(\Delta_n)`.
By Lemma D, this forces `f` to be **constant** on all of `Δ_n`: `f(A) = c(n)`
for every `A \in \Delta_n`. Since `Δ_n` spans the hyperplane `Σp_i=1`
(dimension `n \ge 1$ for every $n\ge1$), a linear functional constant on this
full-dimensional slice of the hyperplane must have all its rank-coefficients
equal: `w_1 = w_2 = \dots = w_{n+1} = c(n)` (indeed `f(V_k)=(w_1+\dots+w_k)/k`
for the vertices `V_k` of Lemma E, and setting all these equal to `c(n)`
forces `w_1=c(n)$ from `k=1`, then inductively `w_k=c(n)` for all `k`).

So **the only weight vector satisfying (i) and (ii) is the trivial one,
`w_i \equiv c(n)`.** With this trivial choice, condition (i) reads
`c(n) \ge V(A)` for every `A \in \Delta_n` — but this is *exactly* the
upper-bound half of the theorem being sought (`c(n) = \max_A V(A)`,
restated), not a consequence of anything simpler. There is no independent
leverage gained: verifying (i) for the trivial weights requires already
knowing `V(A) \le c(n)` for every configuration `A`, which is precisely the
adversarial case analysis (over how Xiang Yu can respond to any `A`) that
the other approaches (`geometric-dominance-construction`,
`recursive-embedding-induction`) carry out directly. The "one-shot LP"
promised by the outline never materializes as a shortcut: it is either

- **not a valid bound** (any non-trivial `w` — see the concrete `n=1`
  witness below, the natural first candidate "always bisect the top piece,"
  which is invalid), or
- **the tautological constant `w_i \equiv c(n)`**, which encodes no new
  information and requires the full casework to verify anyway.

This is the rigorous form of the "circularity" the outline-reviewer flagged:
demanding a linear-in-`p_i` bound that is *tight at an interior point of the
feasible region* is, by Lemmas D–E, mathematically equivalent to assuming
the constant value `c(n)` is already known and simply repeating it — it
cannot be *derived* by a genuinely prior, independent linear-weighting
computation.

## Concrete confirmation at n = 1

To make the abstract obstruction completely explicit (and rule out any
doubt that some clever non-trivial `w` might sneak through), we compute
`V(A)` exactly for `n=1` and exhibit both failure modes.

Let `A = (p_1,p_2)`, `p_1\ge p_2\ge0`, `p_1+p_2=1`. Xiang Yu has one mark to
place, i.e. he chooses one of the two pieces and splits it into two
sub-pieces.

**Case split of one piece into $(a,p_1-a)$, $0<a<p_1/2$ WLOG $a\le p_1-a$.**
The final three pieces are $\{a,\,p_1-a,\,p_2\}$; write $M(a)$ for the median
of this triple, so $oddrank = 1 - M(a)$ (total $1$ minus the middle value,
since with three elements $oddrank$ = largest + smallest = total − middle).
Xiang Yu wants to **maximize** $M(a)$ over his two choices of which piece to
split and over the split point.

- Splitting $p_1$: writing $b = p_1-a\ge a$, the triple is $\{a,b,p_2\}$
  with $a+b=p_1$, $a\le b$. If $a \le p_2 \le b$ then $M=p_2$; achievable
  whenever $p_2\in[p_1/2,p_1]$, i.e. iff $p_1\le 2/3$ (since $p_2=1-p_1$ and
  $p_2\ge p_1/2 \iff p_1\le 2/3$); the best choice is any $a\le p_2\le b$,
  e.g. $a=p_1-p_2$ exactly, giving $M=p_2$ exactly (attained, not just a
  limit, since $a=p_1-p_2\in(0,p_1/2]$ is a valid interior split point
  whenever $p_1\le 2/3$ — one checks $p_1 - p_2 \ge 0$ automatically and
  $p_1-p_2 \le p_1/2$ iff $p_1 \le 2p_2 = 2(1-p_1)$ iff $p_1\le 2/3$, matching).
  If instead $p_1 > 2/3$ (so $p_2 < p_1/2$, i.e. $p_2 < b$ for every valid
  split with $a\le b$), then $p_2$ is never between $a$ and $b$ for splits
  with $a \le p_2$; the median is then $\max(a,p_2)$-vs-$b$ analysis reduces
  to $M=a$ maximized by the most even split $a=b=p_1/2$, giving $M=p_1/2$.
- Splitting $p_2$ instead (into $c\ge d$, $c+d=p_2$): the triple is
  $\{p_1,c,d\}$ with $p_1$ automatically the largest (since $p_1\ge p_2 \ge c$).
  $M=c$, maximized by $c\to p_2$ (i.e. $d\to0$), giving $M\to p_2$ (a supremum,
  approached but, for $d=0$ exactly, invalid since marks must be distinct —
  so this route gives, at best, values arbitrarily close to but not below
  $p_2$ from Xiang Yu's perspective, no better than splitting $p_1$ above
  which *attains* $M=p_2$ exactly when $p_1\le2/3$).

Combining: the true value function is
$$V(p_1,p_2) = 1 - \max(M) = \min(p_1,\; p_2 + p_1/2),$$
attained exactly (via splitting $p_1$) in both regimes — matching the
independently known closed form $c(1)=2/3$ at the crossover $p_1=2/3$ where
$p_1 = p_1/2+p_2$.

**This $V$ is not linear.** It is the pointwise minimum of the two distinct
linear functions $p_1$ and $p_1/2+p_2$, which genuinely disagree except at
$p_1=2/3$: e.g. at $p_1=1/2$, $p_1=0.5$ but $p_1/2+p_2=0.75$, so $V=0.5$; at
$p_1=9/10$, $p_1=0.9$ but $p_1/2+p_2=0.55$, so $V=0.55$. A single line cannot
equal a genuine min of two different lines on an interval containing the
crossing point in its interior (their difference changes sign there), so no
linear $w=(w_1,w_2)$ can equal $V$ identically on all of $\Delta_1$.

**Failure mode (a), invalid bound:** the natural single fixed strategy
"always bisect the top piece" gives $oddrank \equiv p_2+p_1/2$ — linear, with
$w=(1/2,1)$ — but at $A=(1/2,1/2)$ this evaluates to $3/4$, which exceeds
$V(1/2,1/2)=1/2$ (confirmed above) and, more importantly, exceeds
$c(1)=2/3$. So condition (ii) fails: $\max_{A} (p_2+p_1/2) = 3/4 \ne 2/3$ (in
fact the maximum of $p_2+p_1/2 = 1-p_1/2$ over $\Delta_1=\{p_1\in[1/2,1]\}$ is
at $p_1=1/2$, giving $3/4$). This is not a valid tight bound: it overshoots.
We verified this numerically as well (see build log): `bisect_top(1/2,1/2) =
3/4`, `bisect_top(2/3,1/3) = 2/3`, `bisect_top(9/10,1/10)=11/20`, matching
$1-p_1/2$ throughout, confirming it is genuinely linear but not $\le c(1)$
everywhere.

**Failure mode (b), tautological:** by Lemmas D–E applied directly to
$\Delta_1$ (a 1-dimensional segment with relative interior
$(1/2,2/3)\cup\{2/3\}\cup(2/3,1)$, i.e. the open segment strictly between its
two vertices $(1,0)$ and $(1/2,1/2)$ — and $p^*=(2/3,1/3)$ sits strictly
inside it), the only linear $w$ with $\max_A(w_1p_1+w_2p_2)$ attained at
$p^*$ and equal to $c(1)$ is $w_1=w_2=2/3$ (constant), which is the
tautology described above.

## Why the general-$n$ story is the same, structurally

The $n=1$ computation exhibits the general mechanism: Xiang Yu's optimal
response is genuinely **case-dependent** on the relative sizes of the
pieces (bisect the dominant piece vs. match it down to the runner-up),
producing a value function `V` that is a *minimum of several linear pieces*
on different sub-regions of `Δ_n` (a piecewise-linear, not linear,
function) — and this case-dependence recurses at every one of the `n`
levels of the construction (the same self-similar halving structure all
three math-explorers independently noted). Since the conjectured optimum
`p^*` is a strict interior point of the *entire* polytope `Δ_n` for every
`n` (Lemma E), Lemmas D–E apply verbatim for general `n`: any linear,
rank-only `w` satisfying the two conditions the outline needs is forced to
be the trivial constant `w_i \equiv c(n)`, which carries no independent
proof content. There is no way to patch this by choosing cleverer weights —
the obstruction is about the *geometry* of where the optimum sits relative
to the feasible polytope, not about a poor choice of specific numbers.

## Conclusion

The circularity flagged by the outline-reviewer is **real and unfixable**
for the mechanism as conceived: a single, rank-only, configuration-
independent linear weighting cannot give a valid *and* tight upper bound for
`V(A)` at the conjectured (interior) optimum, except via the tautological
constant weighting, which supplies no proof. This is confirmed both
abstractly (Lemmas D and E, general `n`) and concretely (exact computation
at `n=1`, exhibiting the genuine non-linearity of `V` and an explicit
invalid non-trivial attempt). Per the outline's own stated instruction, this
approach is reported as a **dead end** rather than patched around. The
proof of `c(n) = 2^n/(2^{n+1}-1)` should be carried by the case-based /
inductive approaches (`geometric-dominance-construction`,
`recursive-embedding-induction`), which do not attempt to avoid the
adversarial case analysis this file shows cannot be avoided.

## Promotable lemmas
- **Lemma D (interior maximum forces a linear functional constant)** — fully
  proved above, general polytope statement, reusable by any future approach
  on this problem (or others) that tries a linear/LP relaxation over the
  ordered simplex or a similar polytope with an interior conjectured optimum.
- **Lemma E (the ordered simplex `Δ_n` is `n`-dimensional with vertices
  `V_k=(1/k,...,1/k,0,...,0)`, and the geometric configuration is a strict
  interior point)** — fully proved above; useful background fact for any
  approach reasoning about the geometry of Liu Bang's configuration space.
- **Exact value function at n=1**: `V(p_1,p_2) = min(p_1,\, p_2+p_1/2)` on
  `Δ_1`, proved by full case analysis above (which piece Xiang Yu splits,
  and where) — reusable as a sanity-check base case for any inductive
  approach on this problem.
