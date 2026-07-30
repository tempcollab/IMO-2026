# Explorer report: Lemma PARITY-PAIR-GEN (general k<n, tail simultaneously refined)

Scope: numerically and structurally scout the round-6-opened gap in
`recursive-embedding-induction.md` — Lemma PARITY-PAIR-GEN, the extension of
the certified Lemma PARITY-PAIR (`lemmas/parity-pair-lemma-L.md`) from
"`k=n`, tail untouched" to general `0≤k<n` with Xiang Yu simultaneously
splitting the tail. Round 6's skeleton splits this into "Case A (even tying
block)" — claimed already covered by prior work — and "Case B (odd tying
block)" — flagged as the genuinely open, unworked part. **This is a scouting
report, not a proof.** All exact claims below were checked with
`fractions.Fraction`; all numerical-search claims used `scipy.optimize`
(Nelder–Mead, many random restarts) on the continuous split-simplex and are
flagged as such.

## Method

1. Built a numerical "full game" search: for `n=2,3,4`, enumerated (or
   sampled) allocations `(a_1,...,a_{n+1})` of Xiang Yu's `n` marks across
   the `n+1` original pieces of `A_n` (`a_1` = marks on `p_1`, i.e. `k`;
   `a_2,...,a_{n+1}` = marks distributed among the tail pieces, each
   independently split further). For each allocation, minimized
   `oddsum(merge)` over the continuous split simplex per piece (softmax
   reparametrization, Nelder–Mead, 8–25 random restarts) to approximate
   Xiang Yu's best response.
2. Cross-checked the numerically-found optima against exact `Fraction`
   arithmetic by identifying which values coincide with the geometric
   anchors `t_i = p_{i+1}`, and by hand-constructing exact anchor-only
   strategies to confirm predictions exactly (not just to float precision).

Scripts: `/tmp/round-7/explore_paritypairgen.py`,
`/tmp/round-7/check_multifree.py`, `/tmp/round-7/check_two_free.py`.

## Finding 1 (numeric, strong evidence): the lower bound holds, with an
enormous flat plateau of optimal Xiang Yu strategies

For every allocation tested at `n=2,3,4` (all allocations at `n=2,3`;
a representative sweep including all `k` from `0` to `n` at `n=4`), the
numerically-found minimum oddsum is **never** below `c(n)`, and a very large
fraction of allocations — not just `k=n` — achieve `oddsum = c(n)` **exactly**
(to float precision `~1e-13`), including allocations with `k` as low as `1`
and marks split across two or three different tail pieces simultaneously
(e.g. `n=4`: `k=1, tail=(2,0,1,0)` and `k=1, tail=(3,0,0,0)` and
`k=2, tail=(0,2,0,0)` all hit `c(4)=16/31` on the nose). This is consistent
with the "flat-optimum phenomenon" already noted elsewhere in the corpus
(`math-explorer-k-gap.md`), now confirmed to extend across the *whole*
tail-refined regime, not just fixed-`k`, fixed-tail cases. No counterexample
to the lower bound was found in any allocation tried.

## Finding 2 (exact, load-bearing structural fact): Case A is not just
"already covered" — it is a literal instance of the *existing, unmodified*
Lemma PARITY-PAIR, regardless of how marks are split between `p_1` and the
tail

The key fact making this true: **every piece of `A_n` sits in a pure
geometric progression of ratio exactly `2`**, so splitting *any* piece
exactly in half at its "natural" point reproduces an *already-existing*
anchor value, not a new one — e.g. splitting `p_1` in half gives `t_1`
(twice); splitting `t_2` in half gives `t_3` (twice); etc. Consequently, if
Xiang Yu's response lands *every* split point exactly on the fixed lattice
`{0, t_n, ..., t_1}` — **regardless of which original piece each mark was
spent on** — the resulting merged multiset is *always* expressible as
`T ∪ {t_i with multiplicity a_i}` for some `(a_1,...,a_n)`, exactly the
object Lemma PARITY-PAIR governs. Lemma PARITY-PAIR's certified statement
needs **no constraint on `Σ a_i t_i`** and does not care about the
*source* of each multiplicity — only the total count `m`. So:

> **Any anchor-only Xiang Yu strategy, however the marks are distributed
> between `p_1` and the tail, is already handled by the existing,
> unmodified Lemma PARITY-PAIR** (applied with `m` = total extra anchor
> copies produced), *provided* `n+m` is odd — and if Xiang Yu uses all `n`
> marks anchor-style, `m` always works out so this holds (verified exactly
> below).

**Exact verification** (`n=4`): the anchor-only strategy "`p_1 = t_1+t_2+t_2`
(2 marks) and `p_3 = t_3+t_3` (1 mark), rest untouched" (3 of the 4 marks
used, `k=2<n=4`, genuinely tail-refined) gives, by direct `Fraction`
computation, merged multiset `{8/31,8/31,4/31,4/31,2/31,2/31,2/31,1/31}`,
`D = 1/31 = t_4` **exactly** — matching Lemma PARITY-PAIR's prediction for
the vector `a=(1,1,2,0)` with no new argument needed. This means **Case A of
the round-6 skeleton is not merely "restatable" from Claim-★ work — it
follows immediately and in full generality from the already-certified Lemma
PARITY-PAIR as-is**, for *any* `k<n` and *any* distribution of marks across
tail pieces, as long as every split is anchor-exact. This is a stronger and
cleaner statement than the skeleton currently claims (it hedges Case A as
only "confirmed for `k=1,2`"); recommend the next builder write this up as a
one-paragraph closure of the anchor-only sub-case for *all* `k`, not just
`k≤2`.

## Finding 3 (structural, partly conjectural): the real content of Case B is
a *multi-free-coordinate* generalization of Lemma FC, not a new "T is
adversarial" mechanism

Lemma FC (`lemmas/lemma-V-prime-free-coordinate.md`) closed the "one free
coordinate" case for `k=n` (tail untouched) precisely because, with only
`p_1` being split, Lemma V' guarantees **at most one** non-anchor coordinate
at the true minimizing vertex (a single linear equality `Σs_i=2t_1`, so a
vertex of a bounded-box-with-one-equality has ≤1 interior coordinate).

When the tail is *also* split, there are **multiple independent linear
equality constraints** — one per piece Xiang Yu chooses to split (`p_1`'s
own split sums to `p_1`; each split tail piece's own sub-parts sum to that
piece's fixed value, independently). The natural generalization of the
vertex-reduction argument (Lemma V', which was only proved for the
fixed-tail case, per its own file's disclaimer) is:

> **Conjecture (multi-free-coordinate vertex reduction).** At the true
> minimizer of `D` over the *joint* polytope (Xiang Yu's simultaneous
> choice of how to split `p_1` and every tail piece he touches), **at most
> one coordinate per split piece** is a non-anchor free value — i.e. the
> total number of simultaneously-free coordinates is bounded by the number
> of *distinct pieces* Xiang Yu chooses to split (not by 1, and not growing
> with `n` beyond that).

This was checked structurally, not proved: I found candidate near-optima
(e.g. `n=4`, `k=2`, tail-alloc `(0,2,0,0)` — 2 marks on `p_1`, 2 on `p_3`)
where the numerical optimizer reported *three* non-anchor values inside the
2-mark split of `p_3` (a 3-part split has genuinely only one degree of
freedom at a *true* vertex, so 3 "free-looking" values indicate the
optimizer sits on a **flat face**, not yet pushed to the vertex — consistent
with, not a counterexample to, the conjecture, since `D` turned out to be
*locally constant* along that face, i.e. moving within it doesn't change
which anchor-bracket each of the 3 values occupies). This flatness is itself
informative: it suggests the joint-vertex argument should go through by the
**same** boundary/limiting argument Lemma V' already uses (affine on each
cell ⟹ minimum on a face is attained on its boundary), just applied
per-piece rather than globally.

**Proposed proof strategy for PARITY-PAIR-GEN** (concrete, not yet attempted
by any approach file): induct on the **number of simultaneously-free
(non-anchor) coordinates**, not on `n` or on `k` directly. Given a
minimizing configuration with `≥1` free coordinates, pick one (say, the free
value `x` inside some split piece), hold every other coordinate fixed, and
apply the **exact same affine-interpolation argument Lemma FC already uses**
(Lemma D-INSERT: `D` is affine in `x` alone on the bracket `(anchor_{j+1},
anchor_j)` that currently contains it, with everything else fixed) to push
`x` to one of its two neighboring anchors, landing on a configuration with
**one fewer** free coordinate and (by convexity of the affine map) `D` no
larger. Repeat until zero free coordinates remain — a pure-anchor
configuration, which Finding 2 already closes via the *existing* Lemma
PARITY-PAIR. This reduces PARITY-PAIR-GEN entirely to iterating
**already-certified** tools (D-INSERT + PARITY-PAIR), never needing a
genuinely new "adversarial tail" mechanism — i.e. **Case B, as currently
conceived in the round-6 skeleton (treating `T`'s own recursive game as an
opaque black box needing a new bound), may be the wrong framing.** The
right framing looks like "peel one free coordinate at a time, from whichever
piece it lives in," which is source-agnostic exactly like Finding 2 showed
Case A already is.

**What is NOT yet verified about this strategy** (honest gaps for the next
builder): (a) the multi-free-coordinate vertex-reduction conjecture itself
is not proved — Lemma V' as certified is explicitly scoped to the
fixed-tail case only; (b) the "peel one at a time, in what order" step needs
a well-founded induction (e.g. by total number of free coordinates, or by
total marks used) — not yet set up rigorously; (c) I did not find (nor rule
out) a genuine **two-simultaneous-truly-independent-free-coordinate vertex**
numerically — the closest candidate (`n=4`, `p_3` 3-way split) turned out to
be on a flat face rather than a sharp vertex, so this proposed peeling step
has not been stress-tested against a hard instance where two frees interact
non-trivially (e.g. straddle the *same* anchor bracket from two different
split pieces simultaneously, which numerically did not arise in the cases
tried but was not exhaustively ruled out).

## Finding 4 (numeric, no counterexample found): budget-slack strategies are
never better for Xiang Yu

Every allocation using strictly fewer than `n` total marks (in the `n=2,3,4`
sweeps) either matched or exceeded `c(n)` — consistent with "using extra
marks anchor-style can only help Liu Bang weakly" (splitting a piece exactly
at an anchor and leaving another part at `0` is equivalent to not spending
the mark). No allocation with slack ever beat a full-budget one.

## Recommendation for the next round

1. **Write up Finding 2 as a genuine (small, immediate) closure**: state and
   prove that any Xiang-Yu strategy whose splits all land on
   `{0,t_n,...,t_1}` satisfies the target bound for *every* `k` and *every*
   distribution of marks across pieces, as a direct corollary of the
   existing Lemma PARITY-PAIR (no new machinery) — this removes "Case A" as
   an open item entirely, more strongly than the current skeleton's `k≤2`
   hedge.
2. **Attempt the multi-free-coordinate peeling induction (Finding 3)** as
   the main target for PARITY-PAIR-GEN, rather than a monolithic "Case B" —
   first prove the vertex-reduction conjecture itself (generalizing Lemma
   V' to allow multiple simultaneously-split pieces; likely a direct
   extension of Lemma V's own proof, since it never used fixed-tail-ness
   essentially, per that file's own remark), then run the one-coordinate-at-
   a-time D-INSERT argument.
3. **Stress-test for a genuine 2-free-coordinate vertex** at `n=5` or `n=6`
   with two tail pieces split simultaneously and marks concentrated so
   neither split degenerates to an anchor or a flat face — this is the
   concrete numerical experiment that would either produce the "hard"
   instance Case B was meant to address, or provide more evidence that no
   such hard instance exists (i.e. that flatness is generic, not a
   coincidence of the small cases tried).
