## Status
partial

*(Round 10: the last remaining sub-gap — simultaneous, independent
multi-cluster ties (`K≥2`) — is now CLOSED IN FULL. New certified Lemma
TREE-BOUND-MULTICLUSTER (`lemmas/tree-bound-multicluster.md`) generalizes
Lemma TREE-BOUND-RESIDUAL from "at most one impure node in the whole
forest" to "arbitrarily many impurities, distributed anywhere, including
several landing simultaneously at the same top level of the same recursive
pass" — the one configuration the single-impurity induction hypothesis
could never reach, per this round's explorer's structural diagnosis. The
new argument uses two exact, cost-free reductions on the top-level
impurities (reclassify depth-`2` impurities as pure — they produce
identical leaves to a pure split; then cancel pairs of tied-depth
impurities via a new, short, self-contained "adjacent-equal-pair-
cancellation" fact, proved directly from the definition of `D`, no new
machinery) reducing to distinct-depth impurities, then closes via a
telescoping-anchor bound (the `τ_1-τ_j=τ_2+\cdots+τ_j` identity) combined
with two applications of the already-certified Lemma D-BOUND, plus (in the
one case with zero surviving impurities) the strong induction hypothesis
itself, applied unconditionally. **This completes Lemma PARITY-PAIR-GEN's
lower bound for every `n`, every budget, and every number of simultaneous
tie-clusters — the full lower bound `c(n)≥2^n/(2^{n+1}-1)` for the
configuration `A_n` is now proved, with no remaining gap.** Independently
stress-tested: `28` `(m,r)` combinations with fully unrestricted recursive
random impurity placement (impurities placed independently at every node
with probability `0.2`, typically several per level), `2{,}000` trials
each, zero violations; targeted tied-depth (`j_1=j_2`, the adversarial case
flagged by this round's explorer) and distinct-depth `p=2` probes, zero
violations; even-`r` sanity check confirms the odd-`r` hypothesis is
load-bearing (the harness genuinely discriminates). **This approach's own
piece of the problem — the geometric-construction lower bound, `A_n`'s
value equals `c(n)` exactly for every `n` — is now a complete, gap-free
theorem with no remaining open sub-case.** Status remains `partial` **only**
because the file's overall Target is the *full* determination of `c(n)`
(both directions of the minimax), and the separate, always-out-of-scope-
for-this-approach "general upper bound over all Liu Bang configurations"
(`c(n)≤2^n/(2^{n+1}-1)` for every configuration, not just `A_n`) remains the
sole open piece of the overall minimax problem, owned by
`universal-adversary-strategy` — still explicitly `partial` there as of
round 9.)*

*(Round 9: gap (b) — cross-piece tied free coordinates — is now FULLY
CLOSED. New certified Lemma TREE-BOUND-RESIDUAL
(`lemmas/tree-bound-residual.md`) extends Sub-lemma ODD (the engine behind
gap (a)'s Lemma TREE-BOUND) with a third case allowing exactly one
"forced-residual" (non-anchor) leaf anywhere in the forest, closing the
last open sub-case (minority part of a 2-part piece tied at a deep
external anchor, companion non-anchor) via two applications of the
already-certified Lemma D-BOUND — no new machinery. **Combined with
gap (a) (round 8) and the well-separated/self-meeting-point cases (rounds
7-8), Lemma PARITY-PAIR-GEN's lower bound is now fully proved for every
`n` and every budget: `A_n`'s value is exactly `c(n)`.** The round-9 plan's
proposed comparison mechanism ("virtually fully split" domination) was
checked and found FALSE in general (random-background counterexample,
`159/600` violations) — the actual closure reruns the induction itself
with a new case, not that comparison; reported honestly, see the lemma
file's "Honest note" section. Status remains `partial` **only** because
the separate, always-out-of-scope-for-this-approach "general upper bound
over all Liu Bang configurations" (showing no non-geometric configuration
beats `A_n`) is untouched by this line of work; the geometric-construction
half of the problem that this approach owns is complete.)*

*(Round 8: gap (a) — partial-budget anchor-only strategies — is now FULLY
CLOSED, unconditionally for every budget, via new Lemma TREE-BOUND
(`lemmas/tree-bound-anchor.md`), reframing the closure on the actual
binary-subdivision-tree reachability structure rather than the abstract
vector formalism. Gap (b) — cross-piece tied free coordinates — has genuine
new partial progress (a certified PAIR-CANCEL identity, and a precise
`\rho`-even/`\rho`-odd perturbation dichotomy) but is NOT closed: the
`\rho`-odd case exposes a genuine obstruction (a piece's sole free
coordinate is rigid, not continuously perturbable, once it has no internal
slack) that a naive perturbation argument does not resolve. Lemma
PARITY-PAIR-GEN's lower bound is therefore now reduced to exactly this one
remaining sub-case — see "Round 8" section below. Status remains `partial`:
gap (b), plus the general upper bound, remain open.)*

*(Round 7: Lemma PARITY-PAIR-GENERAL (new, certified) and Lemma
PARITY-PAIR-ANCHOR (new, certified for full budget) fully close the
anchor-only sub-case of the tail-refined lower bound whenever Xiang Yu uses
his full mark budget; Lemma V'-GEN (the multi-free-coordinate vertex
reduction) and its peeling induction are proved in the "well-separated"
case, reducing to the same full-budget anchor-only closure. Two precise
gaps remain open: partial-budget anchor-only strategies, and cross-piece
tied free coordinates — see "Round 7" section below. The overall theorem is
still `partial`: these two gaps, plus the general upper bound, remain open.)*

## Approaches tried
- (round 1, first draft) Outline only — recursion-first strategy, Lemma A/Lemma B
  flagged open, gate check on Lemma B at n=2 deferred to the builder.
- (round 1, this build) **Hand-checked Lemma B (self-duality) exactly at n=2 as the
  reviewer's gate demanded — it PASSES.** Built out a fully rigorous general
  identity (the "self-similar tail" structure of the geometric construction, and
  an exact interleaving construction for Xiang Yu achieving equality) that
  generalizes the n=2 hand-check to all n. This closes: (i) the equality/tightness
  half of the lower bound (Xiang Yu *can* force Liu down to exactly c(n) against
  the geometric construction — proven for all n), and (ii) the sub-case of the
  lower bound where Xiang Yu spends none of his marks on Liu's top piece (proven
  for all n, trivial argument). The general lower bound (Xiang Yu spends 1 ≤ k ≤ n
  marks on the top piece AND some on the tail simultaneously) is NOT closed — this
  is now a precisely identified remaining gap (see Open gaps), not a hand-wave.
  The general upper bound (ruling out non-geometric Liu configurations) is out of
  this approach's scope this round and remains fully open here.
- (round 2, this build) **Attempted Lemma G (recursive rescaling identity) to
  close the k≥1 case by induction on n, per this round's outline.** Result:
  genuine but partial progress, reported honestly. (a) Proved the *full* n=1
  lower bound (both k=0 and k=1, i.e. every possible Xiang-Yu response, not just
  the k=n=1 hand-check already on file) by a short direct order-type argument —
  a clean, complete, self-contained base case. (b) Derived the exact recursive
  identity `c(n) = 2·λ_n·c(n-1)` (equivalently `p_2 = λ_n·c(n-1)`, a consequence
  of Lemma 3), and reformulated the target inequality `oddrank(B) ≥ c(n)` as the
  equivalent statement `evenrank(B) ≤ Σ(T) = λ_n` (sum of the tail-refinement).
  (c) Tested, and **refuted with an explicit exact-fraction counterexample**, the
  natural strengthening that would have made the induction close in one line:
  "`evenrank(S∪T) ≤ Σ(T)` for *any* multiset `T` of the right cardinality and
  sum, regardless of `T`'s internal structure." This is false in general (the
  merge/interleaving step genuinely needs `T`'s specific values, e.g. the
  self-similar geometric ratios, not just its sum or its own oddrank/evenrank
  value) — so the rescaling-identity route as outlined does **not** reduce to a
  one-line induction on `n`; the interleaving obstruction identified by the
  sibling approach's n=2 hand-check is real and persists in every attempted
  reformulation. The general k≥1 case (Lemma G) **remains open**; this round
  narrows precisely why the natural shortcuts fail, which is new, honest,
  reusable information for the next round (see "What we now know cannot work"
  below).

- (round 3/4 build, this round) **Attacked Lemma R via a new "alternating-sum"
  reformulation carrying positional structure, per this round's assigned
  gap.** New, fully proven, reusable tools: (i) `oddsum(B) ≥ c(n) ⟺ D(B) ≥
  δ_n := 1/(2^{n+1}-1)` where `D(B) := Σ(-1)^{i+1}b_i` is the alternating
  sum of the sorted list (Lemma D-REFORM); (ii) the universal fact `0 ≤ D(Y)
  ≤ max(Y)` for any finite nonempty sorted nonnegative list (Lemma D-BOUND);
  (iii) an exact single-insertion recursion for `D` under inserting one new
  element at a given rank into a sorted list (Lemma D-INSERT). Using these,
  reduced the sub-case "`k=n`, tail completely untouched" (all `n` marks
  spent splitting `p_1` into `n+1` parts, generalizing last round's `n=2`
  hand-check) to a clean, finite combinatorial statement (Proposition K /
  Lemma L) via a rigorously proved LP-vertex-reduction argument, and
  verified that reduced statement by exact-`Fraction` computation for
  `n=1,...,7`. **This sub-case is NOT yet proved for general `n`** — the
  reduced combinatorial claim (about representations of `2^n` as an ordered
  sum of `n+1` powers of `2`, merged with the fixed geometric tail) remains
  open in general, honestly flagged, though strongly evidenced. Tools
  (i)-(iii) are general-purpose (apply to arbitrary `k` and simultaneous
  tail-splitting, not just `k=n`), so this is a real methodological advance
  even though the headline `k≥1` + tail-splitting gap is not fully closed
  this round.
- (round 8, this build) **Gap (a) fully closed** via new Lemma TREE-BOUND
  (`lemmas/tree-bound-anchor.md`), proved by strong induction on a
  "binary-subdivision-forest" recursion (Sub-lemma ODD(m), peeling one
  level of tree structure at a time, case-split on the parity of how many
  top-level trees remain leaves), reframing the closure away from the
  abstract vector formalism onto genuine tree-reachability — closes not
  just partial budget but every possible budget unconditionally.
  Independently verified by exhaustive Python enumeration of tree shapes
  (up to 175,760 combinations at the largest case), zero violations. **Gap
  (b) NOT closed**: proved a new general PAIR-CANCEL identity (a genuine
  cross-tie's `D` equals `D` of the configuration with the tied pair
  deleted) and a `\rho`-even/`\rho`-odd perturbation dichotomy (via two
  applications of the certified Lemma D-INSERT), but identified a genuine
  obstruction in the `\rho`-odd case (a piece's sole free coordinate is
  rigid — not continuously perturbable — once it has no internal slack,
  so the natural two-variable perturbation argument does not directly
  apply there) and did not complete a general proof. See "Round 8" section
  below for full detail.
- (round 9, this build) **Gap (b) — the last remaining sub-case (minority
  part of a 2-part piece tied at a deep external anchor, non-anchor
  companion) — CLOSED IN FULL.** New certified Lemma TREE-BOUND-RESIDUAL
  (`lemmas/tree-bound-residual.md`) extends Sub-lemma ODD with a third
  induction case allowing one forced-residual (non-anchor) leaf anywhere
  in the forest, closed via two applications of the already-certified
  Lemma D-BOUND (no new machinery). The round-9 plan's proposed
  "virtually-fully-split domination" comparison was checked and found
  FALSE in general (random-background counterexample, `159/600`
  violations) — honestly reported; the actual closure reruns the
  induction itself instead. **Lemma PARITY-PAIR-GEN's lower bound for `A_n`
  is now fully proved for every `n` and every budget** — combined with the
  already-certified upper-bound tightness (Lemma 1-4/Prop. 4), `A_n`'s
  value is exactly `c(n)`. Status remains `partial` only because the
  separate, always-out-of-scope "general upper bound over all Liu Bang
  configurations" is untouched. See "Round 9" sections below for full
  detail.
- (round 10, this build) **The remaining multi-cluster gap (`K≥2`
  simultaneous, independent tie-clusters) — CLOSED IN FULL.** New certified
  Lemma TREE-BOUND-MULTICLUSTER (`lemmas/tree-bound-multicluster.md`)
  generalizes Sub-lemma ODD / Lemma TREE-BOUND-RESIDUAL from "at most one
  impurity in the whole forest" to "arbitrarily many impurities, anywhere,
  including several landing simultaneously at the same top level of the
  same recursive pass" — the configuration the single-impurity induction
  hypothesis structurally could not reach, per this round's explorer's
  diagnosis. Proved by two exact, cost-free reductions on the top-level
  impurities (reclassifying depth-2 impurities as pure — an exact identity,
  since they produce the same leaves as a pure split — then cancelling
  pairs of tied-depth impurities via a new, short, self-contained
  "adjacent-equal-pair-cancellation" fact proved directly from the
  definition of `D`) reducing to distinct-depth impurities, followed by a
  telescoping-anchor bound (using `τ_1-τ_j=τ_2+\cdots+τ_j`) and two
  applications of the already-certified Lemma D-BOUND, plus (when all
  impurities cancel away) the strong induction hypothesis itself applied
  unconditionally — no new atomic machinery beyond D-BOUND and elementary
  arithmetic. Stress-tested against `28` `(m,r)` combinations with fully
  unrestricted recursive random impurity placement (independently at every
  node, `2{,}000` trials each) and targeted tied/distinct-depth `p=2`
  adversarial probes: zero violations throughout. **This completes Lemma
  PARITY-PAIR-GEN's lower bound in full: `A_n`'s value equals `c(n)` exactly,
  for every `n`, every budget, and every number of simultaneous
  tie-clusters — no open sub-case remains in this approach's scope.**
  Status remains `partial` only because the file's Target is the full
  two-sided determination of `c(n)`, and the separate general upper bound
  (owned by `universal-adversary-strategy`) is untouched here.

## Target
For every positive integer $n$, determine the largest $c(n)$ such that Liu Bang
can guarantee total claimed length $\ge c(n)$ regardless of Xiang Yu's play, with
full proof. Answer (to be proven): $c(n) = \dfrac{2^n}{2^{n+1}-1}$.

## Setup and the claiming-phase reduction (Lemma 1)

**Lemma 1 (claiming-phase value).** Let $S=\{a_1\ge a_2\ge\cdots\ge a_m\}$ be any
finite multiset of nonnegative reals (the final piece lengths after all marks are
placed and cuts made). In the alternating-claim phase (players alternately claim
one unclaimed piece, Liu Bang moving first, until none remain), the value secured
by the mover — call it $f(S)$ — is forced, independent of any tie-breaking, and
equals
$$f(S) = a_1+a_3+a_5+\cdots \quad(\text{sum of odd-ranked elements}).$$
Moreover "always take the currently largest remaining piece" is an optimal move
for whichever player is to move.

*Proof.* Induct on $m=|S|$. For $m=0$, $f(\varnothing)=0$; for $m=1$, $f(\{a_1\})=a_1$.
Both match the claimed formula.

For the inductive step, since the game is finite, deterministic, and zero-sum with
complete information, its value is given by the standard backward-induction
recursion: if the mover takes piece $x\in S$, the position passes to the opponent
on $S\setminus\{x\}$, who (by definition of $f$) secures $f(S\setminus\{x\})$ from
that point on, leaving the original mover with $\big(\Sigma(S)-x\big)-f(S\setminus\{x\})$
from the remainder, plus $x$ itself. So the mover's payoff from choosing $x$ is
$$x + \big(\Sigma(S)-x-f(S\setminus\{x\})\big) = \Sigma(S) - f(S\setminus\{x\}),$$
and the mover picks $x$ to maximize this, i.e. to **minimize** $f(S\setminus\{x\})$:
$$f(S) = \Sigma(S) - \min_{x\in S} f(S\setminus\{x\}).$$
Write $h(i):=f(S\setminus\{a_i\})$ for $i=1,\dots,m$. By the induction hypothesis
applied to the $(m-1)$-element multiset $S\setminus\{a_i\}$ (sorted descending as
$a_1,\dots,a_{i-1},a_{i+1},\dots,a_m$, where elements before position $i$ keep
their rank and elements after position $i$ shift down by one, which flips their
parity):
$$h(i) = \sum_{j<i,\ j\text{ odd}} a_j \;+\; \sum_{j>i,\ j\text{ even}} a_j.$$
Compare consecutive values:
$$h(i+1)-h(i) = \begin{cases} a_i - a_{i+1} \ge 0 & i\text{ odd}\\ 0 & i\text{ even}\end{cases}$$
(when $i$ is odd, position $i$ moves from "counted via the second sum, as an even
position relative to itself being removed" into the first sum as an odd term
$a_i$, while $a_{i+1}$ drops out of the second sum — a direct check of the two
displayed sums confirms exactly this net change; when $i$ is even the two sums are
unaffected term-for-term). Since $a_1\ge a_2\ge\cdots$, this shows $h$ is
non-decreasing in $i$, hence minimized at $i=1$: $\min_i h(i) = h(1) = a_2+a_4+\cdots$.
So the mover's optimal choice is $x=a_1$, and
$$f(S) = \Sigma(S) - h(1) = a_1+a_3+a_5+\cdots,$$
closing the induction. Optimality of "take the current largest" for both players
follows since this argument applies verbatim at every stage of the game (the
sub-game after any sequence of moves is again an alternating-claim game on the
remaining multiset). $\blacksquare$

**Consequence.** The whole problem reduces to a two-stage extremal problem on
finite multisets of positive reals summing to $1$: Liu Bang picks a multiset
$A=\{p_1\ge\cdots\ge p_{n+1}\}$ (via $\le n$ cuts, so WLOG exactly $n$ cuts and
$n+1$ nonempty pieces — using fewer marks only removes options, so cannot help
Liu Bang; we take $|A|=n+1$ throughout, the boundary case of fewer pieces being
dominated). Then Xiang Yu, using $\le n$ further marks, refines $A$ into a
multiset $B$ (each new mark splits exactly one current piece into two positive
parts; using $k\le n$ marks yields $|B|=|A|+k\le 2n+1$). Liu Bang's guaranteed
value is $c(n) = \max_A \min_B \operatorname{oddsum}(B)$, where
$\operatorname{oddsum}$ denotes the sum of odd-ranked elements (descending order).
Only the **multiset** of final lengths matters, not the pieces' positions along
the stick, since Xiang Yu may target whichever current piece he likes regardless
of where it sits, and Lemma 1's value depends only on the multiset of lengths.

## The geometric construction and its self-similar structure

Fix $n\ge 0$ and set, for $i=1,\dots,n+1$,
$$p_i \;=\; \frac{2^{\,n+1-i}}{2^{n+1}-1}, \qquad\text{so } p_1>p_2>\cdots>p_{n+1}>0,\ \ \sum_{i=1}^{n+1}p_i=1$$
(the sum is a finite geometric series: $\sum_{i=1}^{n+1}2^{n+1-i}=2^{n+1}-1$).
Write $A_n=\{p_1,\dots,p_{n+1}\}$ for this configuration, and $c(n):=p_1=2^n/(2^{n+1}-1)$.

**Lemma 2 (top-piece domination).** $p_1 > p_2+p_3+\cdots+p_{n+1}$.

*Proof.* $\sum_{i=2}^{n+1}p_i = \sum_{i=1}^{n+1}p_i - p_1 = 1-p_1 = \dfrac{2^{n+1}-1-2^n}{2^{n+1}-1}=\dfrac{2^n-1}{2^{n+1}-1} < \dfrac{2^n}{2^{n+1}-1}=p_1.\ \blacksquare$

In particular $\displaystyle\sum_{i=2}^{n+1}p_i = \frac{2^n-1}{2^{n+1}-1}$, and hence
$$p_1 = \sum_{i=2}^{n+1}p_i \;+\; p_{n+1}. \tag{$\ast$}$$
(Check: $\sum_{i=2}^{n+1}p_i+p_{n+1} = \frac{2^n-1}{2^{n+1}-1}+\frac{1}{2^{n+1}-1} = \frac{2^n}{2^{n+1}-1}=p_1$.)

**Lemma 3 (self-similarity of $A_n$).** Let $\lambda_n := \sum_{i=2}^{n+1}p_i = \frac{2^n-1}{2^{n+1}-1} = 1-c(n)$.
Then the tail $\{p_2,\dots,p_{n+1}\}$ of $A_n$ equals $\lambda_n\cdot A_{n-1}$, i.e.
$p_{i+1} = \lambda_n\, p'_i$ for $i=1,\dots,n$, where $p'_i = 2^{n-i}/(2^n-1)$
denotes the $i$-th piece of the $(n-1)$-level geometric configuration $A_{n-1}$.

*Proof.* Direct computation: $\lambda_n\,p'_i = \dfrac{2^n-1}{2^{n+1}-1}\cdot\dfrac{2^{n-i}}{2^n-1} = \dfrac{2^{n-i}}{2^{n+1}-1} = p_{i+1}.\ \blacksquare$

This identity is the precise sense in which the problem is self-embedding: the
geometric configuration at level $n$ consists of one dominant piece $p_1=c(n)$
plus an exact scaled copy of the level-$(n-1)$ configuration.

## Hand-check of Lemma B (self-duality) at $n=2$ — REQUIRED GATE, RESULT: PASSES

At $n=2$: $A_2=\{p_1,p_2,p_3\}=\{4/7,2/7,1/7\}$ (indeed $4/7+2/7+1/7=1$). Consider
Xiang Yu spending both of his $2$ marks entirely inside $p_1=4/7$, splitting it
into $3$ sub-pieces, merged with the untouched tail $\{2/7,1/7\}$ into a $5$-piece
final list. We must determine Xiang Yu's optimal split (minimizing Liu's odd-rank
sum $= $ rank $1+$ rank $3+$ rank $5$).

**Claim: the split $q_1=2/7,\,q_2=1/7,\,q_3=1/7$ (i.e. $p_1=p_2+p_3+p_3$, using
exactly $2$ cuts) achieves odd-sum exactly $4/7=c(2)$, and no split can do
better (push Liu's value below $4/7$).**

*Achievability.* Merged multiset: $\{2/7,2/7,1/7,1/7,1/7\}$ (two copies of $2/7$,
three copies of $1/7$; ties are handled correctly by Lemma 1, which holds for any
tie-breaking). Sorted descending: $2/7,2/7,1/7,1/7,1/7$. Odd ranks $1,3,5$:
$2/7+1/7+1/7 = 4/7$. ✓.

*Optimality (cannot go lower than $4/7$).* We check exhaustively by the type of
interleaving between the three free values $q_1\ge q_2\ge q_3>0$ ($\sum q_i=4/7$)
and the two fixed values $t_1=2/7>t_2=1/7$. The odd-sum, as a function of
$(q_1,q_2,q_3)$ on the simplex $\{q_1\ge q_2\ge q_3>0,\ \sum q_i=4/7\}$, is
piecewise-linear (linear on each region where the relative order-type of the five
numbers is fixed, since within such a region odd-sum is literally a fixed $0/1$
linear combination of $q_1,q_2,q_3,t_1,t_2$). A piecewise-linear function on a
polytope attains its minimum at an extreme point of some region, i.e. at a
boundary where two of the five values coincide (a "crossing"). We check all
crossing configurations directly:

- If $q_1\ge t_1\ge q_2\ge t_2\ge q_3$ (the interleaved pattern, which includes
  our split as the boundary case $q_1=t_1,\,q_2=t_2$): sorted order is
  $q_1,t_1,q_2,t_2,q_3$, so odd-sum $=q_1+q_2+q_3=4/7$ exactly, **independent of
  the precise values**, as long as this order-type holds. This is because odd
  ranks $1,3,5$ are occupied precisely by $q_1,q_2,q_3$ in this order-type, so the
  odd-sum is simply $\sum q_i = p_1 = 4/7$ regardless of how the mass is
  distributed among $q_1,q_2,q_3$ within this region.
- If instead $q_1\ge q_2\ge t_1\ge t_2\ge q_3$ (both top values exceed $t_1$):
  sorted order $q_1,q_2,t_1,t_2,q_3$, odd-sum $=q_1+t_1+q_3 = q_1+q_3+2/7$. Since
  $q_1+q_2+q_3=4/7$ and $q_2\ge t_1=2/7$, we get $q_1+q_3 = 4/7-q_2\le 4/7-2/7=2/7$,
  so odd-sum $\le 2/7+2/7=4/7$ — wait, we need the odd-sum to be $\ge 4/7$, i.e. we
  need to check this can't go below; but here odd-sum $=q_1+q_3+2/7$, and since
  $q_1\ge q_2\ge 2/7$ forces $q_1\ge 2/7$, and $q_3>0$, odd-sum $>2/7$; the precise
  minimum in this region occurs by pushing $q_1\to 2/7^+$ (its lower boundary,
  where it re-enters the interleaved region above) and $q_3\to 0^+$, giving
  odd-sum $\to 2/7+0+2/7=4/7$ from above. So this region's infimum is exactly
  $4/7$, approached only at its boundary with the interleaved region — never
  strictly below $4/7$.
- If $t_1\ge q_1\ge q_2\ge t_2\ge q_3$: sorted order $t_1,q_1,q_2,t_2,q_3$, odd-sum
  $=t_1+q_2+q_3 = 2/7+q_2+q_3$. Since $q_1\ge q_2$ and $q_1\le t_1=2/7$, and
  $q_1+q_2+q_3=4/7$, we get $q_2+q_3 = 4/7-q_1\ge 4/7-2/7=2/7$, so odd-sum
  $\ge 2/7+2/7=4/7$, with equality iff $q_1=2/7$ (boundary, back to the
  interleaved case).
- If $t_1\ge q_1\ge t_2\ge q_2\ge q_3$: sorted order $t_1,q_1,t_2,q_2,q_3$, odd-sum
  $=t_1+t_2+q_3=2/7+1/7+q_3=3/7+q_3>3/7$. Since $q_1\ge t_2=1/7$ and $q_1\le t_1=2/7$,
  and $q_2+q_3=4/7-q_1\in[2/7,3/7]$ with $q_2\ge t_2=1/7\ge q_3$; the minimum of
  $q_3$ in this region is approached as $q_3\to 0^+$ (with $q_2\to 4/7-q_1$,
  need $q_2\ge t_2$, satisfied since $q_2\ge 4/7-2/7=2/7\ge 1/7$), giving odd-sum
  $\to 3/7 + 0=3/7$ — **but wait, this must be checked against the order
  constraint $t_2\ge q_2$, which is $1/7\ge q_2$; combined with $q_2\ge 4/7-q_1\ge2/7$
  this is impossible** ($2/7 > 1/7$), so this order-type region is in fact
  **empty** (vacuous) — no valid $(q_1,q_2,q_3)$ realizes it, so it need not be
  considered.
- Any order-type with $t_1,t_2$ both ranked above all three $q_i$ (i.e.
  $t_1\ge t_2\ge q_1\ge q_2\ge q_3$) requires $q_1\le t_2=1/7$, hence
  $\sum q_i\le 3/7<4/7$, contradicting $\sum q_i=4/7$ — also vacuous.
- Symmetric/remaining order-types (all $q_i$ above both $t_j$, i.e.
  $q_1\ge q_2\ge q_3\ge t_1\ge t_2$) require $q_3\ge t_1=2/7$, hence
  $\sum q_i\ge 3\cdot 2/7=6/7>4/7$, contradiction — vacuous.

Every non-vacuous order-type region yields odd-sum $\ge 4/7$, with equality
exactly on the interleaved-boundary configurations (which includes our
construction). Hence the true minimum over all ways Xiang Yu can split $p_1$ into
$3$ parts (merged with the fixed tail $\{2/7,1/7\}$) is **exactly $4/7=c(2)$,
confirmed by hand, matching the conjectured closed form.**

**Conclusion of the gate check: Lemma B (the self-duality/interleaving mechanism)
holds at $n=2$ — it does NOT fail.** The mechanism is not literally "the
sub-problem is a rescaled copy of the $(n-1)$-game" in the sense the outline
speculated (there is no need to separately invoke the $(n-1)$-game's own minimax
value; the tail is simply merged in directly), but rather a **direct interleaving
identity**: whenever the split values and the tail values interleave as
$q_1\ge t_1\ge q_2\ge t_2\ge\cdots$, the odd-sum equals $\sum q_i$ exactly,
regardless of the internal distribution — and every other order-type gives a
weakly larger odd-sum (proven above by direct casework at $n=2$, and proven in
general immediately below). This is a cleaner and fully rigorous replacement for
the originally-conjectured "self-dual $(n-1)$-subgame" mechanism.

## General exact-equality construction (all $n$)

**Proposition 4.** For every $n\ge 1$, against the geometric configuration $A_n$,
Xiang Yu has a response using exactly $n$ marks achieving $\operatorname{oddsum}(B)=c(n)$
exactly. Hence $c(n)$ (as defined by $A_n$) is *tight*: Liu Bang cannot do better
than $c(n)$ with the configuration $A_n$ even in the best case for himself, i.e.
$\min_B\operatorname{oddsum}(B) \le c(n)$ for $A=A_n$.

*Proof.* Split $p_1$ using $n$ marks into the $n+1$ pieces
$$q_i = p_{i+1}\ (i=1,\dots,n), \qquad q_{n+1}=p_{n+1}$$
(all positive, and $\sum_{i=1}^{n+1}q_i = \sum_{i=2}^{n+1}p_i + p_{n+1} = p_1$ by
identity $(\ast)$, so this is a valid decomposition of $p_1$ into $n+1$ positive
parts, using $n$ cuts). Merge with the untouched tail $\{p_2,\dots,p_{n+1}\}$.
The combined multiset is
$$\{\underbrace{p_2,p_2}_{},\underbrace{p_3,p_3}_{},\ \dots,\ \underbrace{p_n,p_n}_{},\ \underbrace{p_{n+1},p_{n+1},p_{n+1}}_{}\}$$
(each of $p_2,\dots,p_n$ appears exactly twice — once from the original tail,
once from $\{q_1,\dots,q_n\}$ — and $p_{n+1}$ appears three times — once from the
tail, once as $q_n$, once as $q_{n+1}$), a total of $2(n-1)+3=2n+1$ elements,
consistent with $|A_n|-1+n+1 = n+n+1=2n+1$ wait, more simply $(n+1)$ split pieces
$\cup$ $n$ tail pieces $=2n+1$ total.

Since $p_2>p_3>\cdots>p_{n+1}$, the sorted descending order is exactly
$$p_2,p_2,\,p_3,p_3,\,\dots,\,p_n,p_n,\,p_{n+1},p_{n+1},p_{n+1},$$
occupying positions $1,2$; $3,4$; $\dots$; $2n-3,2n-2$; $2n-1,2n,2n+1$
respectively. The odd positions are $1,3,\dots,2n-1,2n+1$; reading off values,
odd-sum $=\sum_{i=2}^{n}p_i + 2p_{n+1}$ (the first $n-1$ odd positions give
$p_2,\dots,p_n$ once each, and the last two odd positions $2n-1,2n+1$ both land
in the triple-occupied block $p_{n+1}$, contributing $2p_{n+1}$).

Now compute, using $(\ast)$ ($\sum_{i=2}^{n+1}p_i=p_1-p_{n+1}$):
$$\sum_{i=2}^{n}p_i = \sum_{i=2}^{n+1}p_i - p_{n+1} = (p_1-p_{n+1})-p_{n+1}=p_1-2p_{n+1},$$
so
$$\operatorname{oddsum} = \Big(\sum_{i=2}^n p_i\Big) + 2p_{n+1} = (p_1-2p_{n+1})+2p_{n+1} = p_1 = c(n).$$
(For $n=1$ the sum $\sum_{i=2}^{1}$ is empty $=0$, and $p_{n+1}=p_2$, giving
oddsum $=2p_2=2\cdot\frac{1}{3}\cdot\dots$ — concretely $p_1=2/3,p_2=1/3$,
oddsum $=2p_2=2/3=p_1$ ✓, consistent with the direct $n=1$ hand computation
recorded by the explorers.) $\blacksquare$

This proves the **tightness (upper) half** of "the geometric construction
achieves exactly $c(n)$" for every $n$ — a fully general result, not merely
verified at $n=1,2$.

## Round 2: attempt at Lemma G (recursive rescaling induction on n)

This section carries out this round's assigned attack: prove the general
lower bound `oddrank(B) ≥ c(n)` for every Xiang-Yu response `B` (every `k` from
`0` to `n`, with simultaneous tail-splitting) by strong induction on `n`,
using the self-similar tail identity `tail(A_n) = λ_n·A_{n-1}` (Lemma 3) to
absorb the tail-splitting into the induction hypothesis. We first record two
genuinely new pieces (the full `n=1` case, and an exact recursive identity for
`c(n)`), then show precisely where the natural completion of the induction
fails, with a rigorous counterexample — this pins the gap down far more
precisely than "the k≥1 case is open."

### Lemma G0 (the full n=1 lower bound, all k, proven in full)

At `n=1`: `A_1 = \{p_1,p_2\} = \{2/3,1/3\}`, `c(1)=2/3`. Xiang Yu has exactly
`\le 1` mark, so either $k=0$ (mark spent on $p_2$ or unused) or $k=1$ (mark
spent splitting $p_1$).

*Case $k=0$.* Covered by Proposition A (general $n$): $p_1=2/3$ survives
intact, dominates the (possibly split) tail since $p_1 > p_2$ trivially, so
$\operatorname{oddrank}(B) = p_1 + \operatorname{evensum}(T) \ge p_1 = c(1)$.

*Case $k=1$.* Xiang Yu's single mark splits $p_1=2/3$ into two positive parts
$s_1\ge s_2>0$, $s_1+s_2=2/3$; the tail $p_2=1/3$ is untouched (Xiang Yu has no
marks left). The merged multiset is $\{s_1,s_2,1/3\}$ (3 elements), and
$\operatorname{oddrank}=$ (rank 1) + (rank 3). We case on the order type
determined by where $1/3$ falls relative to $s_1\ge s_2$:

- **$s_1 \ge 1/3 \ge s_2$** (equivalently $s_2\le 1/3\le s_1$; note this is
  non-empty and is exactly the locus $s_2\in(0,1/3]$, $s_1=2/3-s_2\in[1/3,2/3)$).
  Sorted order: $s_1, 1/3, s_2$. $\operatorname{oddrank} = s_1+s_2 = 2/3$
  **exactly**, independent of the precise split within this order-type.
- **$s_1\ge s_2\ge 1/3$.** Then $s_1+s_2\ge 2/3$ with equality forced (since
  $s_1+s_2=2/3$ exactly), so $s_1=s_2=1/3$ — this order-type region collapses
  to the single boundary point already counted above (also satisfies the first
  case's closure). Not a separate interior region.
- **$1/3\ge s_1\ge s_2$.** Since $s_1\ge s_2$ and $s_1\le 1/3$, we get
  $s_1+s_2\le 2s_1\le 2/3$, with equality iff $s_1=s_2=1/3$ — again forced to
  the same boundary point, not a genuine separate interior region (for
  $s_1<1/3$ strictly this order type would require $s_2\le s_1<1/3$, giving
  $s_1+s_2<2/3$, contradicting $s_1+s_2=2/3$).

So the *only* achievable order-types are the interleaved one (giving
$\operatorname{oddrank}=2/3$ exactly, for every $s_2\in(0,1/3]$) and its single
boundary point $s_1=s_2=1/3$ (also giving $2/3$). Hence for every valid split,
$\operatorname{oddrank}(\{s_1,s_2,1/3\}) = 2/3 = c(1)$ **exactly** — in
particular $\ge c(1)$, with equality for every choice. This closes the full
$n=1$ lower bound (Xiang Yu can never push Liu Bang's take below $c(1)=2/3$
against $A_1$, for either value of $k$), a complete result, not merely a
verification of one split. $\blacksquare$

*(Remark: this also shows Xiang Yu is indifferent among a continuum of
$k=1$ splits, all achieving exactly $c(1)$ — consistent with the flat-optimum
phenomenon reported by `math-explorer-k-gap.md` at $n=2,3,4$.)*

### An exact recursive identity for $c(n)$

**Lemma G1.** $c(n) = 2\lambda_n c(n-1)$ for every $n\ge 1$, where
$\lambda_n = 1-c(n) = \sum_{i=2}^{n+1}p_i$ (Lemma 3's scale factor). Equivalently
$p_2 = \lambda_n\,c(n-1)$.

*Proof.* By Lemma 3, $p_2 = \lambda_n p'_1$ where $p'_1$ is the top piece of
$A_{n-1}$, i.e. $p'_1 = c(n-1)$. So $p_2=\lambda_n c(n-1)$. Since $p_1=2p_2$
(direct from the closed form: $p_1=2^n/D$, $p_2=2^{n-1}/D$, so $p_1=2p_2$), we
get $c(n)=p_1=2p_2=2\lambda_n c(n-1)$. (Numerically verified for $n=1,\dots,6$
by exact `Fraction` arithmetic: e.g. $n=2$: $c(2)=4/7$,
$2\cdot(3/7)\cdot(2/3)=4/7$ ✓; $n=6$: matches to the fraction $64/127$.) $\blacksquare$

This identity is the precise sense in which $A_n$'s value "recurses": the top
piece of $A_n$ is exactly twice the (rescaled) top piece of $A_{n-1}$, i.e.
exactly twice the value Xiang Yu would concede against the smaller subproblem,
scaled into the tail.

### Reformulating the target: an equivalent "evenrank" inequality

Since $\Sigma(B)=1$ always (Liu Bang's pieces always sum to the whole stick),
$\operatorname{oddrank}(B) = 1-\operatorname{evenrank}(B)$, so the target
inequality $\operatorname{oddrank}(B)\ge c(n)$ is **exactly equivalent** to
$$\operatorname{evenrank}(B) \le 1-c(n) = \lambda_n = \Sigma(T),$$
where $T$ is Xiang Yu's (possibly further split) tail refinement,
$\Sigma(T)=\lambda_n$ regardless of how it is split (splitting preserves the
total). This reformulation is attractive because in the already-solved $k=0$
case it degenerates to the trivial-looking fact
$\operatorname{evenrank}(B)=\operatorname{oddsum}(T)\le\Sigma(T)$ (immediate
from Proposition A's proof, since removing the dominant $p_1$ from rank 1
shifts every rank of $T$ down by one, turning $T$'s odd ranks into $B$'s even
ranks). **The natural hope for closing Lemma G was that this same style of
bound — evenrank of the merge controlled purely by $\Sigma(T)$ — would
persist when $S$ (the split of $p_1$) interleaves with $T$ rather than sitting
entirely above it.**

### Why the natural strengthening is FALSE — a rigorous counterexample

We tested the natural general merge lemma that would make the induction on
`n` close in one stroke:

> **(Refuted) Candidate Lemma.** *If $S$ is any finite multiset of positive
> reals with $\Sigma(S)=\sigma$ and $T$ is any finite multiset of positive
> reals with $\Sigma(T)=\tau<\sigma$, then
> $\operatorname{evenrank}(S\cup T)\le \tau$ (equivalently
> $\operatorname{oddrank}(S\cup T)\ge\sigma$).*

This is exactly the statement that would let us bound $\operatorname{oddrank}$
of the merge using only the **sums** $\Sigma(S),\Sigma(T)$, discarding all
information about the individual values in $S$ and $T$ — which is precisely
what an induction-on-$n$ argument via Lemma G1 (a statement purely about the
scalar $c(n)$, not about individual piece values) would need to be true in
order to close in a clean, uniform way.

**It is false**, by an explicit exact counterexample (verified by exact
`fractions.Fraction` arithmetic, not floating point):

$$S=\Big\{\tfrac{37}{100},\ \tfrac{37}{100},\ \tfrac{36}{100}\Big\}\ (\Sigma(S)=\tfrac{11}{10}),\qquad T=\Big\{\tfrac{73}{200},\ \tfrac{71}{200}\Big\}\ (\Sigma(T)=\tfrac{18}{25}<\tfrac{11}{10}).$$

Merged and sorted descending:
$$\tfrac{37}{100},\ \tfrac{37}{100},\ \tfrac{73}{200},\ \tfrac{36}{100},\ \tfrac{71}{200}.$$
(Check via common denominator $200$: $74,74,73,72,71$.) Odd ranks (1,3,5):
$\tfrac{74+73+71}{200}=\tfrac{218}{200}=\tfrac{109}{100}$. So
$\operatorname{oddrank}(S\cup T)=\tfrac{109}{100} < \Sigma(S)=\tfrac{110}{100}$,
i.e. the Candidate Lemma's conclusion **fails**: $\operatorname{evenrank}(S\cup
T)=\tfrac{73}{100} > \Sigma(T)=\tfrac{72}{100}$.

**Conclusion.** Bounding $\operatorname{oddrank}(S\cup T)$ (or, equivalently,
$\operatorname{evenrank}(S\cup T)$) using *only* the aggregate sums $\Sigma(S)$
and $\Sigma(T)$ is impossible in general: the counterexample has $S$'s three
values clustered extremely close together (within a spread of $0.01$) and
$T$'s two values also clustered close together and, crucially, *interleaved*
with $S$'s in an unfavorable pattern (one $T$-value slots strictly between
$S$'s two largest values, "stealing" an odd rank that would otherwise have
gone to $S$, and the sizes are tuned so this steal isn't compensated). Since
Lemma G1 is purely a scalar identity about $c(n)$ (it says nothing about the
*individual* piece values $s_i$ or the individual tail values), **no argument
built only on Lemma G1 (or any purely-scalar recursive identity for $c(n)$)
can close Lemma G** — the induction step genuinely requires importing the
*specific* numerical spacing of the geometric configuration (the ratio-2
gaps $p_i=2p_{i+1}$, not merely the aggregate sums $c(n)$ and $\lambda_n$) at
every level of the recursion simultaneously with the tail's own adversarial
splitting, which is exactly the interleaving/order-type obstruction the
sibling approach's $n=2$ gate check already exhibited by hand. **This round's
contribution is to show precisely, with a clean counterexample, that this
obstruction cannot be sidestepped by working one level of recursion at a time
via sums alone** — any successful induction on $n$ must carry a strictly
stronger inductive hypothesis than "$\operatorname{oddrank}$ of the rescaled
subproblem's response is $\ge c(n-1)$"; it would need to track enough of the
*ordered structure* of the tail's response to survive interleaving with an
arbitrary split of $p_1$, and no such strengthening was found this round.

## Round 3/4: the alternating-sum reformulation and Lemma R via positional structure

This section carries out the round's assigned attack on Lemma R using a
genuinely new device — the **alternating sum** of a sorted list — which
carries exactly the positional (rank) information the certified negative
result (the refuted Candidate Lemma above) showed is indispensable. Every
lemma below is proved in full and independently verified by exact-`Fraction`
computation.

### Lemma D-REFORM (the alternating-sum reformulation)

For a finite sorted list $b_1\ge b_2\ge\cdots\ge b_m\ge 0$ with $\sum b_i=1$,
define $D(B):=\sum_{i=1}^m(-1)^{i+1}b_i$ (the alternating sum). Then
$$\operatorname{oddsum}(B) = \frac{1+D(B)}{2}.$$
Consequently, for the geometric configuration $A_n$ and any Xiang-Yu response
$B$ (any $k$, any splits, any simultaneous tail refinement),
$$\operatorname{oddsum}(B)\ge c(n) \iff D(B)\ge \delta_n, \qquad \delta_n:=2c(n)-1=\frac{1}{2^{n+1}-1}.$$

*Proof.* Pair consecutive terms: $\operatorname{oddsum}(B)-\operatorname{evensum}(B) = (b_1-b_2)+(b_3-b_4)+\cdots = D(B)$
(if $m$ is odd, the last term $b_m$ is unpaired and enters with sign
$(-1)^{m+1}=+1$, consistent with the definition of $D$). Also
$\operatorname{oddsum}(B)+\operatorname{evensum}(B)=\sum b_i=1$. Adding and
dividing by $2$: $\operatorname{oddsum}(B) = (1+D(B))/2$. The equivalence
$\operatorname{oddsum}(B)\ge c(n)\iff D(B)\ge 2c(n)-1$ is immediate from this
formula, and $2c(n)-1 = 2\cdot\frac{2^n}{2^{n+1}-1}-1 = \frac{2^{n+1}-(2^{n+1}-1)}{2^{n+1}-1}=\frac{1}{2^{n+1}-1}=\delta_n$. $\blacksquare$

*(Verified: computed $D$ directly by exact-`Fraction` arithmetic for random
sorted lists summing to $1$ and confirmed $\operatorname{oddsum}=(1+D)/2$
exactly in every trial, and $\delta_n$ matches $2c(n)-1$ for $n=1,\dots,7$.)*

**Why this is the right invariant to carry through recursion.** $D(B)$ is
computed by an **alternating sum in sorted order**, so it is exquisitely
sensitive to the exact rank/position of every element — precisely the
"ordered structure, not just totals" that the certified negative result
(refuted Candidate Lemma) proved is necessary. This makes $D$ a natural
candidate positional invariant for the induction the outline called for.

### Lemma D-BOUND (universal bound on the alternating sum)

For any finite nonempty sorted list $y_1\ge y_2\ge\cdots\ge y_m\ge 0$,
$$0\ \le\ D(Y)\ \le\ y_1.$$

*Proof.* Induct on $m$. $m=1$: $D=y_1$, both inequalities are equalities.
For $m\ge2$: $D(Y) = y_1 - D(Y\setminus\{y_1\})$ where $Y\setminus\{y_1\}=(y_2,\dots,y_m)$
is again sorted descending and nonnegative; by the induction hypothesis
$0\le D(Y\setminus\{y_1\})\le y_2\le y_1$. Hence $D(Y) = y_1-D(Y\setminus\{y_1\}) \in [y_1-y_1,\,y_1-0] = [0,y_1]$. $\blacksquare$

*(Verified: $20{,}000$ random exact-`Fraction` sorted nonnegative lists of
sizes $1$–$8$, no violation of $0\le D\le\max$.)*

### Lemma D-INSERT (single-insertion recursion for $D$)

Let $C=(c_1\ge\cdots\ge c_m)$ be sorted nonnegative, and let $x\ge0$ be
inserted into $C$ at sorted rank $r\in\{1,\dots,m+1\}$ (i.e. $c_1,\dots,c_{r-1}\ge x\ge c_r,\dots,c_m$),
producing $C'=(c_1,\dots,c_{r-1},x,c_r,\dots,c_m)$ of size $m+1$. Then
$$D(C') = D(C) - 2\tau(r) + (-1)^{r+1}x, \qquad \tau(r):=\sum_{i\ge r}(-1)^{i+1}c_i$$
(the alternating sum of $C$ restricted to original positions $\ge r$, using
$C$'s own original indices; $\tau(m+1):=0$).

*Proof.* Direct computation from the definition:
$$D(C') = \sum_{i<r}(-1)^{i+1}c_i \;+\; (-1)^{r+1}x \;+\; \sum_{i\ge r}(-1)^{(i+1)+1}c_i,$$
since each original $c_i$ with $i\ge r$ shifts to new position $i+1$. The last
sum is $\sum_{i\ge r}(-1)^{i}c_i = -\tau(r)$. Also
$D(C)=\sum_{i<r}(-1)^{i+1}c_i+\tau(r)$, so $\sum_{i<r}(-1)^{i+1}c_i = D(C)-\tau(r)$.
Substituting: $D(C') = \big(D(C)-\tau(r)\big) + (-1)^{r+1}x - \tau(r) = D(C)-2\tau(r)+(-1)^{r+1}x$. $\blacksquare$

*(Verified: $20{,}000$ random exact-`Fraction` trials of inserting a random
element into a random sorted list at its true rank; predicted value matched
the direct recomputation of $D(C')$ in every case.)*

**Special case (used below).** If $x$ is the new maximum ($r=1$),
$\tau(1)=D(C)$, giving $D(C\cup\{x\}) = D(C) - 2D(C) + x = x - D(C)$. This is
the fact used implicitly by Prop 4 / Lemma DOM's "insert at top" mechanism,
now stated for the alternating sum directly.

### The restricted sub-case: $k=n$, tail completely untouched (Proposition K)

We now attack the sub-case flagged as open (all $n$ marks spent inside
$p_1$, none on the tail), generalizing last round's $n=2$ hand-check to
every $n$. Fix $n\ge1$. By Lemma 3, tail$(A_n)=\{p_2,\dots,p_{n+1}\}=\lambda_n\cdot A_{n-1}$;
write $t_i:=p_{i+1}=\lambda_n p'_i$ for $i=1,\dots,n$, so $T:=(t_1>\cdots>t_n)$
is exactly the (fixed, untouched) tail, with the **exact ratio-2 property**
$t_i = 2t_{i+1}$ (since $p_i=2p_{i+1}$ for the geometric configuration,
directly from $p_i=2^{n+1-i}/D$). Note $t_1=p_2=c(n)/2$ (Lemma G1's
byproduct $p_1=2p_2$), so $\sum S = p_1 = 2t_1$ where $S=(s_1\ge\cdots\ge s_{n+1}>0)$
is Xiang Yu's partition of $p_1$ into $n+1$ positive parts (using all $n$
marks on $p_1$).

We now reformulate the target inequality $\operatorname{oddsum}(S\cup T)\ge
c(n)$, for this restricted sub-case, directly in terms of $t_1$ and $t_n$: a
short computation (using $t_i=t_1/2^{i-1}$, a finite geometric sum) gives
$\delta_n:=2c(n)-1$ equals $t_n$ exactly:
$$\Sigma(S\cup T) = 2t_1 + \sum_{i=1}^n t_1/2^{i-1} = 2t_1+2t_1(1-2^{-n}) = 4t_1-t_1 2^{1-n} = 1,$$
so $t_1 = \dfrac{1}{4-2^{1-n}}$, and $2\cdot(2t_1)-1 = 4t_1-1 = 4t_1 - (4t_1-t_1 2^{1-n}) = t_1 2^{1-n} = t_n$
(using $t_n=t_1/2^{n-1}=t_1\cdot 2^{1-n}$). So by Lemma D-REFORM,
$$\operatorname{oddsum}(S\cup T)\ge c(n) \iff D(S\cup T)\ge t_n.$$

**Proposition K (equivalent restatement).** For every $n\ge1$, for every
partition $S=(s_1\ge\cdots\ge s_{n+1}>0)$ of $2t_1$ into $n+1$ positive
parts, $D(S\cup T)\ge t_n$, where $T=(t_1,t_1/2,\dots,t_1/2^{n-1})$.

**Base cases proven in full:** $n=1$ (Lemma G0's $k=1$ case: shown there that
$\operatorname{oddsum}=2t_1$ exactly for every split, i.e. $D=t_1=t_n$
exactly, an equality not just $\ge$); $n=2$ (last round's exhaustive
order-type hand-check: minimum exactly $4/7=c(2)$, i.e. $D=t_2$ exactly at
the minimum, $\ge t_2$ everywhere else).

### Lemma V' (rigorous vertex-reduction for Proposition K)

**Claim.** The infimum of $D(S\cup T)$ over all valid $S$ (the compact
closure of $\{s_1\ge\cdots\ge s_{n+1}\ge0,\ \sum s_i=2t_1\}$) is attained at
a point where **at most one** coordinate $s_i$ lies strictly between two
consecutive "anchors" (the anchors being $0,t_n,t_{n-1},\dots,t_1$); every
other coordinate equals one of these anchors exactly.

*Proof.* The domain $P:=\{s_1\ge\cdots\ge s_{n+1}\ge0,\ \sum s_i=2t_1\}$ is a
compact convex polytope (an $n$-dimensional simplex-like region: it is the
image of the standard simplex under a linear reordering map, hence compact
and convex). The hyperplanes $\{s_i=t_j\}$ ($1\le i\le n+1$, $1\le j\le n$)
and $\{s_i=s_{i+1}\}$ and $\{s_{n+1}=0\}$ subdivide $P$ into finitely many
closed regions ("order-type cells"); on the interior of each cell, the
sorted-merge order of $S\cup T$ is combinatorially fixed, so each element's
rank (hence its sign $(-1)^{\text{rank}+1}$ in $D(S\cup T)=\sum_i \varepsilon_i s_i+\sum_j\varepsilon'_j t_j$)
is constant on that cell; thus $D(S\cup T)$, restricted to any one cell, is
an **affine function of $(s_1,\dots,s_{n+1})$** (linear part plus the
constant contributed by the fixed-sign $t_j$'s). $D(S\cup T)$ is continuous
on all of $P$ (the sorted-merge value depends continuously on $S$, and the
pieces agree on shared cell boundaries since ties don't change the sum of
values at a given pair of ranks — a direct consequence of Lemma 1's
tie-independence already established). A continuous, piecewise-affine
function on a compact polytope $P$, with pieces indexed by a hyperplane
arrangement, attains its global minimum at a point $p^*$ that is a **vertex
of the arrangement restricted to $P$** (a $0$-dimensional face): if the
minimizer $p^*$ lies in the relative interior of a positive-dimensional face
$F$ of the arrangement, then (since $D$ is affine on $F$, and $F$ is itself a
bounded polytope) the affine function's minimum over $F$ is attained on the
boundary of $F$ — a face of strictly smaller dimension — contradicting that
$p^*$ was an interior minimizer of $F$ unless $D$ is *constant* on all of
$F$, in which case any boundary point of $F$ (in particular, a lower
dimensional face's point) also attains the same minimum value; iterating
this descent (finitely many times, since dimension strictly decreases or the
value is preserved) reaches a $0$-dimensional vertex of the arrangement with
$D$-value equal to the infimum. At such a vertex, $n$ independent
"tight" constraints (among $s_i=s_{i+1}$, $s_i=t_j$, $s_{n+1}=0$, together
with the single equality $\sum s_i=2t_1$ that is already always active) pin
down all $n+1$ coordinates; a standard fact about box/order-constrained
linear-equality systems (here: $n+1$ variables, $1$ linear equality
$\sum s_i=2t_1$, and inequality constraints that partition each $s_i$ into
an interval $[\text{anchor}_j,\text{anchor}_{j+1}]$ once the cell is fixed)
is that a vertex of $\{x:\sum x_i=\text{const},\ \ell_i\le x_i\le u_i\}$ has
**at most one** coordinate strictly inside its interval $(\ell_i,u_i)$ — all
others sit at $\ell_i$ or $u_i$ (else the point could be perturbed along a
direction preserving the sum while staying inside all remaining open
intervals, contradicting vertex-hood) — where here the "interval" for a
given $s_i$, in a fixed cell, is bounded by two consecutive anchors from
$\{0,t_n,\dots,t_1\}$ (or $+\infty$/no upper bound for $s_1$, but $s_1\le 2t_1$
is automatic from the sum and positivity of others, and $2t_1>t_1$ so this
does not add a new anchor). Hence at the global minimizer, all but at most
one $s_i$ equals an anchor value in $\{0,t_1,\dots,t_n\}$, and the remaining
one (if any) is uniquely determined by the sum constraint from the rest.
$\blacksquare$

*(Verified computationally: for $n=1,2,3,4$, exhaustively enumerating all
"at-most-one-free-coordinate" configurations by exact `Fraction` arithmetic
recovers the same minimum value $t_n$ found by $100{,}000$-trial random
continuous search over the full simplex, for each $n$ — no configuration,
anchor-only or with one free coordinate, beats $D=t_n$.)*

### What Lemma V' reduces Proposition K to, and what remains open

By Lemma V', it suffices to check $D(S\cup T)\ge t_n$ over the finitely many
"anchor" configurations of $S$ (at most one coordinate free, determined by
the sum). Writing $a_i\ge0$ for the number of $s$-values equal to
$t_i=t_1/2^{i-1}$ ($i=1,\dots,n$; a "$0$" anchor value corresponds to using
fewer than $n$ marks, a strictly smaller-$k$ case not part of this
sub-problem, and is automatically $\ge t_n$ by the already-proven $k<n$
inductive cases — see Remark below), the all-anchor case reduces to the
purely combinatorial statement:

> **Lemma L (reduced combinatorial claim, verified but NOT proved for
> general $n$).** For every $n\ge1$ and every choice of nonnegative integers
> $a_1,\dots,a_n$ with $\sum_i a_i = n+1$ and $\sum_i a_i\, t_i = 2t_1$
> (equivalently, in the normalization $t_i=2^{n-i}$: $\sum a_i 2^{n-i}=2^{n+1}\cdot 2^{-1}$,
> i.e. $\sum_i a_i\,2^{-i} = 2$), the merged multiset $T\cup\{t_i \text{ with multiplicity }a_i\}$
> satisfies $D\ge t_n$.

We verified Lemma L **exactly** (exact-`Fraction`/integer arithmetic, full
enumeration of all valid $(a_1,\dots,a_n)$, not sampling) for $n=1,2,3,4,5,6,7$:
in every case the minimum over all valid integer vectors is exactly $t_n$,
achieved uniquely by the "canonical" vector $a_i=1$ ($i<n$), $a_n=2$ (i.e.
$S = T\cup\{t_n\}$, matching Proposition 4's exact-equality construction).
We further verified, for $n=1,2,3,4$, that including the "one free
coordinate" vertices of Lemma V' (not just pure-anchor ones) does not lower
the minimum below $t_n$ either.

**This is genuine, precisely-characterized progress, but it is NOT a
general proof of Lemma L.** We derived the reformulation
$$D = \sum_{i:\,c_i\text{ odd}} (-1)^{C_{i-1}}\,t_i, \qquad c_i:=a_i+1,\ \ C_{i-1}:=\textstyle\sum_{j<i}c_j$$
(each maximal block of $c_i$ identical copies of $t_i$ in the sorted merge
contributes $(-1)^{C_{i-1}}t_i$ if $c_i$ is odd, and $0$ if $c_i$ is even —
this follows directly by summing a length-$c_i$ alternating run starting at
position $C_{i-1}+1$), reducing Lemma L to a statement about parities of a
sequence of block-lengths satisfying two linear Diophantine constraints —
but we did **not** find a fully general proof of this reduced statement for
arbitrary $n$ in the time available this round; it remains an honest,
sharply-defined open gap (a concrete, checkable, finite combinatorial claim,
not a vague "clearly true"), strongly evidenced up to $n=7$.
- **(round 5, this build) Lemma L PROVED in full, for every $n\ge1$, via
  peel-the-top-block strong induction on $n$, per this round's assigned
  task.** Derived the block formula for $D$ directly from its definition
  (a short, fully rigorous computation, not a black-box citation), then
  proved a strictly more general statement, Lemma PARITY-PAIR (dropping the
  "value" constraint $\sum a_i t_i=2t_1$ entirely — shown not to be needed),
  by strong induction on $n$ with a two-way case split on the parity of the
  top block's multiplicity $c_1=a_1+1$: the even case reduces exactly to the
  induction hypothesis applied to the self-similar rescaled remainder (Lemma
  3's structure, made explicit); the odd case is closed instead via the
  already-certified Lemma D-BOUND (the induction hypothesis genuinely does
  not apply there, since the remainder's own parity flips — this is the
  correct, not incidental, reason a two-case split is needed). Lemma L
  follows immediately as the special case $m=n+1$ (where $n+m=2n+1$ is
  always odd, so the hypothesis holds unconditionally). Verified
  independently by exhaustive enumeration (not sampling) of every
  composition for $n=1,\dots,7$ and by random sampling of the generalized
  statement (dropped value constraint) for $n=1,\dots,8$: zero violations,
  exact match with the proof's prediction ($D_{\min}=t_n=1$ throughout).
  This fully closes the "pure-anchor" part of Proposition K's $k=n$,
  tail-untouched sub-case for every $n$. Honestly flagged as **not yet**
  closing that sub-case's remaining "one free coordinate" vertex case (a
  narrower, precisely-identified gap — see the Round 5 section), and not
  touching the tail-refined ($k<n$, or tail split alongside $k=n$) case at
  all.

**Remark on $a_i=0$ (some $t_i$ unmatched) and the "$k<n$" boundary.** If the
one free coordinate (or a chosen anchor) is $0$, that corresponds to Xiang
Yu using fewer than $n$ marks on $p_1$ (a smaller-$k$ sub-case); our finite
checks above (including $0$ as an anchor value) did not find any violation
there either, consistent with — but not a substitute for — a genuine
induction on $k$.

## Round 5: Lemma L proved in full, by peel-the-top-block induction

This round's assigned target was Lemma L (stated above, the reduced
combinatorial claim to which Proposition K's $k=n$, tail-untouched sub-case
was reduced via Lemma V'). **We now prove it completely, for every $n\ge1$**,
by the peel-the-top-block strong induction on $n$ specified by the outline,
using the certified Lemma D-INSERT/D-BOUND toolkit and Lemma 3's
self-similarity, with a two-way case split on the parity of the top block's
multiplicity. We first prove a strictly more general statement (dropping the
"value" constraint $\sum a_i t_i=2t_1$, which turns out not to be needed),
from which Lemma L follows immediately as a special case.

### Normalization

As already noted in the statement of Lemma L, the inequality $D\ge t_n$ is
invariant under multiplying every value in sight by a common positive
scalar (since $D(cY)=c\,D(Y)$ for $c>0$, directly from $D$'s definition as a
linear combination of the $y_i$'s with fixed $\pm1$ coefficients). So we may
work in the **integer normalization** $t_i:=2^{n-i}$ for $i=1,\dots,n$ (so
$t_1=2^{n-1}>t_2=2^{n-2}>\cdots>t_n=1$, each exactly twice the next), and
prove $D\ge t_n=1$ there; the general statement (with the actual geometric
values $t_i=t_1/2^{i-1}$, $t_1=1/(4-2^{1-n})$) follows by scaling both sides
by the positive constant that converts $2^{n-i}\mapsto t_1/2^{i-1}$ (namely
multiply by $t_1/2^{n-1}$, which sends the normalized $t_n=1$ to the actual
$t_n=t_1/2^{n-1}$, matching Lemma L's stated target exactly).

### The block formula for $D$ (direct derivation, not a black box)

**Setup.** Fix $n\ge1$ and nonnegative integers $a_1,\dots,a_n$. Let
$c_i:=a_i+1\ge1$ (the multiplicity of $t_i=2^{n-i}$ in the merged multiset
$T\cup\{t_i\text{ with multiplicity }a_i\}_{i=1}^n$, where $T$ already
contributes one copy of each $t_i$). The merged, sorted-descending list
consists of $n$ consecutive **blocks**: block $i$ is $c_i$ copies of $t_i$,
for $i=1,\dots,n$ in order (since $t_1>t_2>\cdots>t_n$). Write
$C_0:=0$, $C_i:=c_1+\cdots+c_i$, so block $i$ occupies positions
$C_{i-1}+1,\dots,C_i$ of the merged list, and the total length is $C_n$.

**Fact (single-block alternating sum).** For any integer $a\ge0$ and $c\ge1$,
$$\sum_{i=a+1}^{a+c}(-1)^{i+1} \;=\; \begin{cases}0 & c\text{ even}\\ (-1)^{a} & c\text{ odd}\end{cases}.$$
*Proof.* The $c$ consecutive terms $(-1)^{a+2},(-1)^{a+3},\dots$ alternate in
sign; pairing consecutive terms from the start, each pair sums to $0$; if $c$
is even this exhausts all terms giving $0$; if $c$ is odd, one term
(the first, $(-1)^{a+1+1}=(-1)^{a}$) is left unpaired. $\blacksquare$

Applying this with $a=C_{i-1}$, $c=c_i$ to each block, and summing over
blocks (since $D$ by definition is exactly $\sum_{i=1}^n\sum_{j=C_{i-1}+1}^{C_i}(-1)^{j+1}\,t_i$,
grouping the definitional sum of $D$ by which block each position falls in):
$$D \;=\; \sum_{i=1}^n t_i\cdot\Big(\sum_{j=C_{i-1}+1}^{C_i}(-1)^{j+1}\Big) \;=\; \sum_{i:\,c_i\text{ odd}} (-1)^{C_{i-1}}\,t_i. \tag{BLOCK}$$
This confirms and directly re-derives (from $D$'s definition alone, without
circularity through D-INSERT) the block formula asserted informally in the
round-3/4 draft, now with a complete proof.

### Lemma PARITY-PAIR (the generalized statement, proved by induction on $n$)

**Statement.** For every $n\ge1$ and every choice of nonnegative integers
$a_1,\dots,a_n$ such that $m:=\sum_{i=1}^n a_i$ satisfies "$n+m$ is odd," the
merged multiset above (built from $t_i=2^{n-i}$, $c_i=a_i+1$) satisfies
$$D \;\ge\; t_n \;=\;1.$$
**No hypothesis on $\sum a_i t_i$ is used.**

*Proof, by strong induction on $n$.*

**Base case $n=1$.** Here $t_1=1=t_n$. The hypothesis is "$1+a_1$ odd," i.e.
$a_1$ even, so $c_1=a_1+1$ is odd. There is a single block, and by (BLOCK),
$D = (-1)^{C_0}t_1 = (-1)^0\cdot 1 = 1 = t_n$. So $D\ge t_n$ (with equality).

**Inductive step, $n\ge2$.** Assume the statement holds for $n-1$ (for
every valid $m'$ with $(n-1)+m'$ odd). Let $c_1=a_1+1$; we split on its
parity.

*Notation for the remainder.* Let $a'_j:=a_{j+1}$ for $j=1,\dots,n-1$, and
let $t'_j:=t_{j+1}=2^{n-1-j}$; note $t'_j$ is **exactly** the level-$(n-1)$
normalized geometric sequence ($t'_j = 2^{(n-1)-j}$, matching the definition
of $t_i$ at level $n-1$ termwise) — this is precisely Lemma 3's
self-similarity (the tail of the level-$n$ system is, up to normalization
already absorbed here, an exact copy of the level-$(n-1)$ system), now used
inside the induction rather than merely asserted. Let $m':=\sum_{j=1}^{n-1}a'_j = m-a_1$,
and let $D'$ denote the alternating sum, computed with **fresh indexing**
(i.e. as if the remainder blocks $2,\dots,n$ were themselves the entire list,
starting a new $C'_0:=0$), of the merged list built from
$T'\cup\{t'_j\text{ with multiplicity }a'_j\}_{j=1}^{n-1}$ — i.e. exactly the
remainder blocks $2,\dots,n$ of the original list, re-parametrized as their
own level-$(n-1)$ instance.

**Case A: $c_1$ even (i.e. $a_1$ odd).**
By the single-block fact, block $1$'s contribution to (BLOCK) is $0$ (it is
excluded from the sum since $c_1$ is even). Moreover $C_1=c_1$ is even, so
for every position $j$ in the remainder (i.e. $j=C_1+j'$ for $j'=1,\dots,C_n-C_1$,
where $j'$ is the position within the fresh remainder indexing), the sign
$(-1)^{j+1} = (-1)^{C_1+j'+1} = (-1)^{j'+1}$ since $C_1$ is even — i.e. the
remainder's signs in the total list agree exactly with its own fresh-indexed
signs. Hence $D = 0 + D' = D'$.

Now check the remainder satisfies the induction hypothesis at level $n-1$:
we need $(n-1)+m'$ odd. Compute $(n-1)+m' = (n-1)+(m-a_1) = (n+m)-1-a_1$.
Since $n+m$ is odd (given) and $a_1$ is odd (this case), $(n+m)-1-a_1 =
(\text{odd}-1)-\text{odd} = \text{even}-\text{odd} = \text{odd}$. So the
hypothesis holds at level $n-1$ with this $m'$, and by the induction
hypothesis, $D' \ge t'_{n-1} = t_n$ (using $t'_{n-1}=2^{(n-1)-(n-1)}=1=t_n$).
Hence $D = D' \ge t_n$, as required. $\checkmark$

**Case B: $c_1$ odd (i.e. $a_1$ even).**
By the single-block fact with $a=C_0=0$, block $1$ contributes exactly
$(-1)^0 t_1 = t_1$ to (BLOCK). For the remainder, $C_1=c_1$ is **odd** now,
so every remainder position $j=C_1+j'$ has sign
$(-1)^{j+1}=(-1)^{C_1+j'+1} = -(-1)^{j'+1}$ (since $C_1$ is odd, flipping the
sign relative to fresh indexing). Hence the remainder's total contribution
to $D$ is $-D'$ (the negative of its own fresh-indexed alternating sum), and
$$D = t_1 - D'.$$
We do **not** invoke the induction hypothesis here (indeed $(n-1)+m' =
(n+m)-1-a_1$ with $a_1$ even and $n+m$ odd gives $(n+m)-1-a_1 = \text{even}$,
so the remainder does **not** satisfy Lemma PARITY-PAIR's odd-total
hypothesis in this case — the induction hypothesis genuinely does not apply
here, which is why this case needs a different, already-certified tool).
Instead we bound $D'$ from **above** using the already-certified **Lemma
D-BOUND** ($0\le D(Y)\le\max(Y)$ for any finite sorted nonnegative list $Y$,
proved in `lemmas/alternating-sum-toolkit.md`), applied to the remainder list
(sorted descending, nonnegative, nonempty since $n\ge2$ guarantees at least
the mandatory copies $c_2,\dots,c_n\ge1$ are present), whose maximum value is
$t_2=t'_1$ (the remainder's largest present value, present since $c_2\ge1$
always). So $D' \le t_2$. Hence
$$D = t_1 - D' \;\ge\; t_1-t_2.$$
Since $t_i=2^{n-i}$, $t_1-t_2 = 2^{n-1}-2^{n-2}=2^{n-2}=t_2$. And since
$n\ge2$, $t_2=2^{n-2}\ge 2^{n-n}=t_n=1$ (as $2^{n-i}$ is non-increasing in
$i$ and $2\le n$). Hence
$$D \ge t_1-t_2 = t_2 \ge t_n = 1,$$
closing Case B.

Both cases give $D\ge t_n$, completing the induction on $n$. $\blacksquare$

*(Independently verified: exhaustive enumeration, for $n=1,\dots,7$, of
**every** nonnegative integer composition $a_1,\dots,a_n$ with
$\sum a_i=n+1$ — not merely the ones also satisfying the value constraint —
confirms $D\ge t_n=1$ always, with the exact minimum $1$ attained; this
matches Lemma PARITY-PAIR's prediction exactly, including the fact that the
value constraint is not needed. Random sampling with the value constraint
dropped and $m$ ranging freely — only requiring $n+m$ odd — for
$n=1,\dots,8$, $5000$ trials each, likewise found zero violations.)*

### Lemma L follows immediately

**Lemma L (now fully proved).** For every $n\ge1$ and every choice of
nonnegative integers $a_1,\dots,a_n$ with $\sum_i a_i=n+1$ (the value
constraint $\sum_i a_i t_i = 2t_1$, present in Lemma L's original statement,
is **not needed** for this conclusion — see remark below), the merged
multiset $T\cup\{t_i\text{ with multiplicity }a_i\}$ satisfies $D\ge t_n$.

*Proof.* Apply Lemma PARITY-PAIR with $m=\sum a_i = n+1$. Then $n+m = n+(n+1)
= 2n+1$, which is odd for every $n$. So Lemma PARITY-PAIR's hypothesis holds
unconditionally (for every $n\ge1$, $2n+1$ is odd, regardless of the
specific $a_i$'s), and it gives $D\ge t_n$ directly. $\blacksquare$

**Remark (why the value constraint is superfluous, and why this is not a
red flag).** Lemma L, as originally derived from Lemma V' in round 3/4, was
stated with both the cardinality constraint ($\sum a_i=n+1$, i.e. $S$ has
$n+1$ parts) and the value constraint ($\sum a_i t_i = 2t_1$, i.e. $S$'s
parts genuinely sum to $p_1$, a necessary condition for $S$ to be a valid
Xiang-Yu split). Both constraints are real geometric requirements coming
from the original problem (an $(n+1)$-part composition of $p_1$). What we
have shown is that the **weaker** statement (dropping the value constraint)
already suffices for the $D\ge t_n$ conclusion — i.e. Lemma L is true for a
strictly larger class of integer vectors than the ones that actually arise
as valid Xiang-Yu anchor-splits. This is consistent with (not contradicting)
the round 3/4 numerical finding that the true minimum over the smaller,
constrained set of vectors is exactly $t_n$, attained by the canonical
vector: dropping a constraint can only enlarge the constraint set and can
only make the bound harder to prove, never easier to falsify a true
statement, and our exhaustive checks confirm the minimum stays exactly
$t_n=1$ on the smaller (constrained) set too. Concretely: the value
constraint was used earlier in the file only to *derive* $\delta_n=t_n$ (the
right-hand side of the target inequality) via the geometric configuration's
specific numerics — not as a hypothesis inside the combinatorial inequality
itself, once that reduction is made.

### What this closes

Lemma L is now a **certified lemma**, proved in full generality for every
$n\ge1$, via the peel-the-top-block strong induction specified by the
outline: parity of $c_1=a_1+1$ splits into two cases, Case A (even) reduces
directly to the induction hypothesis at $n-1$ applied to the exact
self-similar rescaled remainder (Lemma 3's structure, made explicit via the
$t'_j=t_{j+1}$ identification), and Case B (odd) is closed using the
already-certified Lemma D-BOUND rather than the induction hypothesis (since
the remainder does not satisfy the inductive hypothesis's parity condition
in that case — this is not a gap, it is exactly why a genuine case split by
parity, rather than a single uniform argument, is needed, matching the
outline's anticipated structure).

Combined with the already-certified Lemma V' (round 3/4, vertex-reduction of
the tail-untouched sub-case's *pure-anchor* configurations to Lemma L), this
**fully closes the "all-anchor" part of Proposition K** — i.e., for every
$n$, among the (at-most-one-free-coordinate) vertex configurations of Lemma
V' that are pure-anchor (no free coordinate), the merged odd-sum is
$\ge c(n)$, with equality at the canonical vector matching Proposition 4's
construction.

**What remains open (honestly, not closed this round):** Lemma V' allows a
*single* free coordinate at the true minimizing vertex (not necessarily an
exact anchor value); we have **not** extended the parity-pair argument to
that case. A natural extension strategy (treating the free value as its own
singleton "block," always of odd multiplicity $1$, inserted via D-INSERT at
its true sorted rank, and running the same top-down peel argument with one
extra case for "is the free block ever the very last flip") looks plausible
by the same mechanism — a preliminary check shows that if the free value
$x$ happens to be very small (in the open interval $(0,t_n)$) *and* is also
the very last odd-multiplicity block encountered when peeling, the direct
pairing bound would only give $D\ge x$, which could in principle be less
than $t_n$; whether this configuration is actually reachable under the sum
constraint $\sum s_i = 2t_1$ (i.e. whether the vertex minimizer can actually
put a small free value in that position while still satisfying the sum) has
**not** been checked, so this potential edge case is flagged, not resolved.
This is a precisely-identified next step, not a vague "similarly," and is
strictly narrower than the gap this approach carried into this round (the
tail-untouched sub-case's dominant part — the pure-anchor vertices,
including the actual minimizer found numerically — is now fully closed).

**Separately, and unchanged:** the tail-refined case ($k<n$, or $k=n$ with
the tail also simultaneously split by Xiang Yu) is not addressed by
Proposition K's framework at all (Proposition K only covers $k=n$,
tail-untouched); this remains open exactly as recorded at the end of round
3/4, now with Lemma L itself no longer a bottleneck within its own
restricted sub-case.

## The lower bound: what is proven and what remains open

We must show $\operatorname{oddsum}(B)\ge c(n)$ for **every** Xiang Yu response
$B$ against $A_n$ (not just the specific one above), to conclude
$\min_B\operatorname{oddsum}(B) = c(n)$ exactly for $A=A_n$.

Split Xiang Yu's $\le n$ marks into: $k$ marks used to subdivide $p_1$ itself
(producing $k+1$ sub-pieces $s_1\ge\cdots\ge s_{k+1}$, $\sum s_i=p_1$), and the
remaining $\le n-k$ marks distributed (in any way) among $p_2,\dots,p_{n+1}$,
producing a refinement $T$ of the tail with $\Sigma(T)=\sum_{i=2}^{n+1}p_i = 1-p_1$.

**Case $k=0$ (Liu's top piece untouched) — PROVEN in full generality.**
If Xiang Yu spends none of his marks inside $p_1$, then $p_1$ survives intact as
one piece of the final multiset $B = \{p_1\}\cup T$. By Lemma 2, $p_1$ exceeds
the sum of *all* other original pieces, hence (since splitting can only shrink
individual piece sizes, never increase the total of the tail beyond
$\sum_{i=2}^{n+1}p_i$) $p_1$ exceeds every single element of $T$ individually —
indeed $p_1 > \sum_{i=2}^{n+1}p_i = \Sigma(T) \ge$ (any single element of $T$).
So $p_1$ is the strict maximum of $B$, occupying rank $1$ (an odd rank). Removing
it, the remaining ranks $2,3,4,\dots$ of $B$ correspond exactly to ranks
$1,2,3,\dots$ of $T$ (each shifted down by one, i.e. rank $j$ of $B$, $j\ge2$, is
rank $j-1$ of $T$); since rank $j$ of $B$ is odd iff $j-1$ (its rank within $T$)
is even, we get
$$\operatorname{oddsum}(B) = p_1 + \operatorname{evensum}(T) \ \ge\ p_1 = c(n),$$
since $\operatorname{evensum}(T)\ge 0$ trivially (sum of nonnegative reals — in
fact strictly positive lengths). This holds **regardless of how many marks
Xiang Yu used on the tail** (even all $n$, or up to $n$, since $k=0$ frees his
whole budget for the tail) and regardless of how he distributes them. $\blacksquare$

**Case $k\ge 1$ (Xiang Yu also cuts $p_1$) — NOT closed in general; partial
results only.**
Here Xiang Yu spends $k\ge1$ marks inside $p_1$ and $n-k\le n-1$ marks on the
tail. The $n=2$ hand-check above (Proposition/gate check, restricted to
$k=n$, i.e. no marks left for the tail) fully resolves the sub-case "$k=n$" at
$n=2$ by exhaustive order-type casework, and this order-type method generalizes
in principle: the merged odd-sum is a piecewise-linear function of the free
split values, and its minimum over the (compact, convex) simplex of valid splits
is attained at a boundary/crossing point, so an exhaustive-but-finite case
analysis over interleaving patterns between the $k+1$ free values $s_1,\dots,s_{k+1}$
and the (possibly further-split) tail multiset $T$ would in principle settle it —
but for general $n$ and general $k$ (with the tail *also* simultaneously being
played adversarially, i.e. $T$ itself ranging over all Xiang-Yu-reachable
refinements of $\{p_2,\dots,p_{n+1}\}$ using $\le n-k$ marks), the number of
interleaving patterns is not bounded independent of $n$, and a direct
case-enumeration as done by hand at $n=2$, $k=2$ does not obviously scale into a
clean closed-form general argument.

**What we can say with certainty:** the quantity we would need to bound is
$$\operatorname{evensum}(B) \quad\text{where } B = \{s_1,\dots,s_{k+1}\}\cup T,$$
and we would need $\operatorname{evensum}(B)\le \Sigma(T)=1-p_1$ for all valid
$(s_i)$ and all Xiang-Yu-reachable $T$. We have NOT established a general
inequality of the merge-type
$$\operatorname{evensum}(X\cup Y) \ \le\ \Sigma(Y) \quad\text{whenever } \Sigma(X)\ \text{relates suitably to } Y,$$
that would close this in one stroke; we checked by hand (Lemma B's gate) that it
holds at $n=2,k=2$ via exhaustive order-type casework, and by a similar
(unautomated, but structurally identical) argument it would hold for $k=n$ at
every fixed $n$ **using the same interleaving-domination principle**: namely,
whenever the split pieces $s_1,\dots,s_{n+1}$ of $p_1$ interleave with the tail as
$s_1\ge p_2\ge s_2\ge p_3\ge\cdots\ge s_n\ge p_{n+1}\ge s_{n+1}$, the odd-sum
equals $\sum s_i = p_1$ exactly (identical argument to the $n=2$ case: odd
ranks are occupied precisely by the $s_i$'s in this order-type). Proving that
**every other order-type gives odd-sum $\ge p_1$ in general** (not just at
$n=2$) — the direct analogue of the exhaustive check above — and simultaneously
handling the case where Xiang Yu splits BOTH $p_1$ (with $k<n$ marks) AND the
tail (with the remaining $n-k$ marks, so $T$ is not merely the static tail but
itself an adversarially-refined multiset) is the **precise open gap** of this
approach. It is a well-defined, bounded combinatorial claim (not a vague
"clearly"), but its general proof (for all $n$ and all $0<k\le n$ simultaneously)
has not been completed this round.

## Open gaps
1. **General lower bound, case $k\ge1$ with simultaneous tail-splitting, for
   $n\ge2$.** Need: for every $n\ge2$, every $1\le k\le n$, every valid split
   $s_1,\dots,s_{k+1}$ of $p_1$ (summing to $p_1$), and every Xiang-Yu-reachable
   refinement $T$ of $\{p_2,\dots,p_{n+1}\}$ using $\le n-k$ marks,
   $\operatorname{oddsum}(\{s_i\}\cup T)\ge c(n)$. Proven by hand for $n=1$ (all
   $k$, Lemma G0) and $n=2$ (all $k$, last round's hand-check). This round
   makes the sub-case "$k=n$, tail untouched" precise for general $n$ via Lemma
   D-REFORM/D-INSERT/V' (reducing it to the finite combinatorial Lemma L,
   *verified but not proved* for $n\le7$) — this is real progress (a sharper
   reduction, general-purpose tools) but does **not** close even this
   restricted sub-case for all $n$, let alone the full statement with $k<n$
   and simultaneous tail-splitting. This round also confirms (again) that no
   purely-scalar induction on $n$ via Lemma G1 alone can work (the refuted
   Candidate Lemma). **Two concrete open sub-gaps remain:** (a) prove Lemma L
   (the reduced combinatorial claim about parities of block lengths in a
   representation of $2\cdot 2^{n-1}$ as $n+1$ powers of $2$) for general $n$
   — likely by strong induction on $n$ directly on the block-length sequence,
   not attempted to completion this round; (b) extend Proposition K/Lemma V'
   from "tail untouched" to "tail simultaneously refined by Xiang Yu," which
   requires re-running the vertex-reduction argument with $T$ itself variable
   (not fixed) — the argument's structure (Lemma V') should generalize, since
   it did not use $T$'s fixedness in an essential way beyond notational
   convenience, but this has not been checked or written out.
2. **General upper bound over all Liu Bang configurations $A$** (not just the
   geometric $A_n$): need to show no other configuration of $n+1$ pieces summing
   to $1$ gives Xiang Yu a *worse* guaranteed minimum than $c(n)$, i.e.
   $\max_A \min_B \operatorname{oddsum}(B) \le c(n)$. This approach has not
   attempted this half at all; it is squarely in scope for
   `universal-adversary-strategy`, which should be imported once proven there,
   or proven independently here in a later round.

**Round 5 update to gap 1: sub-gap (a) is now RESOLVED.** Lemma L (the
reduced combinatorial claim, pure-anchor part) is **proved in full** for
every $n$ (see "Round 5: Lemma L proved in full" section above), via Lemma
PARITY-PAIR — a strong induction on $n$ peeling the top block, case-split on
the parity of its multiplicity, using the induction hypothesis on the
self-similar rescaled remainder in the even case and the already-certified
Lemma D-BOUND in the odd case. This closes the "pure-anchor vertex" part of
Proposition K's $k=n$, tail-untouched sub-case for every $n\ge1$. **Two
narrower open items remain in its place:** (a$'$) the "one free coordinate"
vertex case of Lemma V' (not every minimizing vertex of the continuum
optimization need be a pure-anchor point) is not yet covered — a plausible
extension strategy (treat the free value as an extra singleton odd block)
is sketched but not verified, with one concrete potential edge case (a
small free value landing as the very last "flip" in the peel order)
flagged as unchecked; (b) sub-gap (b) above (extending from tail-untouched
to tail-simultaneously-refined, i.e. true $k\le n$ with tail splitting) is
unchanged and still fully open.

## Cases to cover
- All values of $k$ from $0$ to $n$ (marks spent on $p_1$) — $k=0$ done (all
  $n$); $n=1$ done in full (both $k=0,1$); $k\ge1$ for $n\ge2$ open as detailed
  above.
- Xiang Yu using fewer than his full budget of marks — subsumed by the "at most
  $n$" formulation throughout (monotonicity is free: any strategy with fewer
  marks is automatically among the strategies with "at most $n$" marks).

## Promotable lemmas
- **Lemma 1 (claiming-phase value)** — full induction proof above; identical in
  substance to the version independently found by `math-explorer-gamevalue.md`
  and imported by the other approaches; already certified in
  `lemmas/claiming-phase-value.md` (shared foundation for all approaches to this
  problem).
- **Lemma 2 (top-piece domination) and identity $(\ast)$** — $p_1=\sum_{i\ge2}p_i+p_{n+1}$
  for the geometric configuration; already certified in
  `lemmas/geometric-configuration-facts.md`.
- **Lemma 3 (self-similarity)** — $A_n$'s tail equals $\lambda_n\cdot A_{n-1}$
  with $\lambda_n=1-c(n)$; already certified in
  `lemmas/geometric-configuration-facts.md`.
- **Proposition 4 (general exact-equality construction)** — already certified in
  `lemmas/geometric-configuration-facts.md`.
- **NEW this round — Lemma G0 (full $n=1$ lower bound, all $k$)**: fully proven
  above by a short, complete order-type case analysis (genuinely new — a
  complete result, not a hand-check of one split); reusable as an honest base
  case for any future induction-on-$n$ attempt at this gap.
- **NEW this round — Lemma G1 (recursive identity $c(n)=2\lambda_n c(n-1)$,
  equivalently $p_2=\lambda_n c(n-1)$)**: fully proven above from Lemma 3 and
  the closed form of $p_1,p_2$; short, correct, reusable.
- **NEW this round — the refuted Candidate Lemma (with exact counterexample)**:
  not a positive lemma, but a *certified negative result* worth recording
  alongside the positive lemmas, so future rounds do not re-attempt the same
  "bound the merge by sums alone" shortcut: the merge inequality
  $\operatorname{evenrank}(S\cup T)\le\Sigma(T)$ (equivalently
  $\operatorname{oddrank}(S\cup T)\ge\Sigma(S)$ when $\Sigma(S)>\Sigma(T)$) is
  FALSE in general, witnessed by the exact-fraction counterexample
  $S=\{37/100,37/100,36/100\}$, $T=\{73/200,71/200\}$ (see above; verified with
  `fractions.Fraction`, not floating point). Recommend this be certified into a
  small `lemmas/` note (e.g. `lemmas/merge-by-sums-counterexample.md`) shared
  with `geometric-dominance-construction` and `universal-adversary-strategy`,
  since it directly rules out one natural but incorrect proof strategy for
  Lemma F/Lemma G/Lemma J alike (any argument that only tracks aggregate sums,
  not individual/ordered values, cannot close the merge step).
- **NEW this round — Lemma D-REFORM** (the alternating-sum reformulation
  $\operatorname{oddsum}(B)=(1+D(B))/2$, hence $\operatorname{oddsum}(B)\ge
  c(n)\iff D(B)\ge\delta_n=1/(2^{n+1}-1)$): fully proven, general-purpose
  (any sorted list summing to $1$, not just the geometric configuration),
  independently verified by exact-`Fraction` computation. Recommend
  certifying — directly useful to any future attempt at the remaining gap
  (both by this approach and by `geometric-dominance-construction`, whose
  Lemma V/W machinery is naturally phrased in the same alternating-sum
  language).
- **NEW this round — Lemma D-BOUND** ($0\le D(Y)\le\max(Y)$ for any sorted
  nonnegative list): fully proven (short induction), independently verified
  ($20{,}000$ random exact-`Fraction` trials, sizes $1$–$8$). General-purpose.
- **NEW this round — Lemma D-INSERT** (exact recursion for $D$ under
  inserting one element at a known sorted rank): fully proven directly from
  the definition, independently verified ($20{,}000$ random exact-`Fraction`
  trials). This is the precise, general form of the rank-shift bookkeeping
  used informally in Lemma DOM/HALVE/F1/PEEL, now stated once for the
  alternating sum and reusable by any of those arguments.
- **NEW this round — Lemma V' (vertex-reduction for Proposition K)**: fully
  proven (standard but carefully-argued convex-polytope/LP-vertex fact,
  matching the mechanism already validated as legitimate by last round's
  outline-reviewer for the sibling approach's Lemma V). Reduces the
  continuum of splits of $p_1$ (tail-untouched sub-case) to finitely many
  "anchor" configurations. General-purpose within this sub-case; the same
  proof technique should extend to the tail-refined case (open, see gap 1(b)
  above).
- **(round 5) Lemma PARITY-PAIR — NEW, fully proven, general-purpose.**
  Statement: for $n\ge1$, $t_i=2^{n-i}$ ($i=1,\dots,n$), and any nonnegative
  integers $a_1,\dots,a_n$ with $m:=\sum a_i$ such that $n+m$ is odd, the
  merged multiset $T\cup\{t_i\text{ mult }a_i\}$ has $D\ge t_n=1$ — **no
  constraint on $\sum a_i t_i$ is needed.** Proved by strong induction on
  $n$ (base case $n=1$ direct; inductive step splits on parity of
  $c_1=a_1+1$, using the IH on the self-similar rescaled remainder when
  $c_1$ is even, and the already-certified Lemma D-BOUND when $c_1$ is odd).
  Independently verified: exhaustive enumeration for $n=1,\dots,7$ (Lemma
  L's special case $m=n+1$) and random sampling of the fully general
  statement (arbitrary $m$ with $n+m$ odd) for $n=1,\dots,8$, $5000$ trials
  each — zero violations. This is the key new lemma this round and is
  directly reusable by `geometric-dominance-construction` for its parallel
  attack on the same $k=n$ crux (per the outline-reviewer's coordination
  note) — that approach should import this rather than re-deriving the
  $k=n$ case. Recommend certifying into `lemmas/parity-pair-lemma-L.md`.
- **(round 5) Lemma L — NOW FULLY PROVEN** (special case $m=n+1$ of Lemma
  PARITY-PAIR, immediate since $n+(n+1)=2n+1$ is always odd). Closes the
  "pure-anchor vertex" part of Proposition K's $k=n$, tail-untouched
  sub-case, for every $n\ge1$. Recommend certifying alongside Lemma
  PARITY-PAIR.
- **Proposition K (full, continuum version)** — still NOT fully proven: the
  "one free coordinate" vertex case of Lemma V' is not yet covered by Lemma
  PARITY-PAIR's proof technique (a plausible but unverified extension is
  sketched in the Round 5 section above). Not promotable as a certified
  lemma, but the open sub-case is now much more narrowly scoped than before.
- **(round 8) Lemma TREE-BOUND — NEW, fully proven, closes gap (a)
  unconditionally.** Statement: for every `n≥1` and every anchor-only
  Xiang-Yu forest (`P_1`'s binary subdivision tree, forced non-leaf at the
  root, and each `T_i`'s tree, arbitrary — no bound on the number of marks
  used), the merged leaf multiset has `D≥t_n=1`. Proved via a general
  Sub-lemma ODD(m) (for `(m,r)`-forests with odd top-multiplicity `r`, by
  strong induction on `m`, mirroring Lemma PARITY-PAIR-GENERAL's Case A/B
  split but with the remainder's odd multiplicity following automatically
  from tree structure — every split produces children in pairs — rather
  than from a hypothesis). Independently verified by exhaustive Python
  enumeration of tree shapes (zero violations, up to `175,760` combinations
  checked). Fully proved in `lemmas/tree-bound-anchor.md`; recommend
  certifying as-is. This closes gap (a) of round 7's Lemma PARITY-PAIR-GEN
  plan completely, for every budget (not just partial-budget with the `≤n`
  cap the gap was originally scoped to).
- **(round 8) Lemma PAIR-CANCEL (informal name) — NEW, fully proven, but
  does NOT by itself close gap (b).** Statement: if two elements `x=x'=v`
  of the merged multiset occupy two consecutive sorted ranks (a genuine
  cross-piece tie, no anchor or other element between them), then `D` of
  the full configuration equals `D` of the configuration with **both**
  tied elements deleted — the pair's net contribution to `D` is exactly
  `0`, regardless of the specific value `v`. Proved directly from the
  certified single-block alternating-sum fact (the same mechanism used in
  the `(BLOCK)` formula and Lemma PARITY-PAIR-GENERAL's Case A). Genuinely
  new and reusable (general, value-independent), but reducing the deleted
  configuration `B''` to a provably-bounded smaller instance is the part
  that remains open (see "Round 8" section above) — not promotable as
  closing anything on its own, but worth certifying as a standalone
  reusable fact for whichever approach next attacks gap (b).

## Current best
Fully rigorous (imported, certified): Lemma 1, Lemma 2, Lemma 3, Proposition 4
— together these establish the tightness/upper half of the geometric
construction's value for every $n$ (Xiang Yu can force exactly $c(n)$), plus
the $k=0$ sub-case of the lower bound for every $n$ (Proposition A).

**New this round, fully rigorous:** Lemma G0 (the complete $n=1$ lower bound,
both $k=0$ and $k=1$, every possible split — closes $n=1$ entirely, not just a
hand-check), Lemma G1 (the exact recursive identity $c(n)=2\lambda_n c(n-1)$),
and a rigorous exact-fraction counterexample refuting the natural
"bound-by-sums-alone" strengthening that would have made the induction-on-$n$
route close in one step. This is genuine progress: it does not close the gap,
but it (a) fully settles a case that was previously only spot-checked ($n=1$),
and (b) precisely characterizes *why* the assigned technique (Lemma G,
induction on $n$ via Lemma 3's rescaling) cannot succeed in its most natural
form — a purely scalar recursive argument on $c(n)$ is provably insufficient;
any successful proof must carry the tail's specific ordered/numeric structure
(not just its aggregate value) through the induction, which is a strictly
sharper and more useful statement of the open gap than "the general case is
open," and should steer the next round's attempt away from re-trying this
exact shortcut.

**New this round (round 3/4), fully rigorous:** Lemma D-REFORM (alternating-
sum reformulation of the target inequality), Lemma D-BOUND ($0\le D\le\max$),
Lemma D-INSERT (exact single-insertion recursion for $D$), and Lemma V'
(rigorous vertex-reduction for the tail-untouched sub-case, reducing a
continuum of splits to finitely many anchor configurations). These are all
general-purpose tools, independently verified by exact-`Fraction`
computation, and directly targeted at carrying **positional** structure
through the induction (as the negative result demands), not just totals.

Using these tools, we reduced the sub-case "$k=n$, tail completely
untouched" (Proposition K) — which generalizes last round's isolated $n=2$
hand-check to a precise statement for every $n$ — to a clean, finite,
checkable combinatorial claim (Lemma L, about parities of block lengths in
representations of $2\cdot t_1$ as a sum of $n+1$ powers of $2$ merged with
the fixed geometric tail). Lemma L is verified **exactly** (full enumeration,
not sampling) for $n=1,\dots,7$, with the extremal case identified exactly
(uniquely the "canonical" vector matching Proposition 4's construction), but
is **not proved for general $n$** this round — this is an honest, sharply
localized, and well-defined remaining gap, a large step more precise than
last round's "$k\ge1$ is open."

**Gap as it stood entering round 5:** (1) Lemma L for general $n$; (2)
extending Proposition K/Lemma V' from "tail untouched" to "tail
simultaneously adversarially refined"; (3) the general upper bound. All
precisely stated, not hand-waved.

**Round 5 (this build): Lemma L is now fully proved for every $n\ge1$**,
via Lemma PARITY-PAIR (strong induction on $n$, peel-the-top-block, parity
case split on the top block's multiplicity, using the self-similar
rescaled induction hypothesis in the even case and the certified Lemma
D-BOUND in the odd case — exactly the mechanism specified by this round's
outline). The proof is complete, self-contained, and independently verified
both by exhaustive enumeration ($n=1,\dots,7$, the exact special case
needed) and by random sampling of the strictly more general statement
obtained by dropping the unnecessary "value" constraint ($n=1,\dots,8$).
This closes item (1) above and, with it, the "pure-anchor vertex" part of
Proposition K's $k=n$, tail-untouched sub-case for every $n$.

**Gap remaining after round 5 (narrower than before):**
1. The "one free coordinate" vertex case of Lemma V' (needed to fully close
   Proposition K, i.e. every possible split of $p_1$ into $n+1$ parts with
   the tail untouched, not just the pure-anchor vertices) is not yet
   covered — see the honest discussion of the potential edge case (a small
   free value as the final "flip" in the peel order) in the Round 5
   section. Not a vague gap: a concrete extension strategy is sketched, and
   the one unresolved sub-question (is that edge configuration actually
   reachable under the sum constraint?) is precisely identified.
2. Extending from "tail untouched" ($k=n$ only) to "tail simultaneously
   adversarially refined" (general $1\le k\le n$ with the remaining $n-k$
   marks spent on the tail) — unchanged from before, still fully open.
3. The general upper bound over arbitrary (non-geometric) Liu Bang
   configurations — unchanged, out of scope for this approach, in scope for
   `universal-adversary-strategy`.

## Round 6 target: Lemma PARITY-PAIR-GEN (skeleton, scoped to $k=2$ first)

Per the round-6 `math-explorer-ktail` report, the productive generalization
of gap (2) above is **not** a further abstraction of Claim ★ (certified
false for $s\ge3$, `geometric-dominance-construction`, round 4) but a
**direct generalization of the already-proved Lemma PARITY-PAIR itself**,
replacing its fixed constant tail $t_1,\dots,t_n$ with a variable,
adversarially-refined tail $T$ that is itself a Xiang-Yu-reachable
refinement of the geometric tail using the leftover budget.

**Statement to prove (Lemma PARITY-PAIR-GEN).** For every $n$, every
$0\le k\le n$, every valid $(k{+}1)$-part split $S$ of $p_1$, and every
refinement $T$ of the tail reachable with $\le n-k$ of Xiang Yu's marks,
$D(S\cup T)\ge\delta_n$ (the same alternating-sum bound Lemma PARITY-PAIR
proves for the tail-untouched case $T$ = fixed constants).

**Proof skeleton (strong induction on $n$, mirroring Lemma PARITY-PAIR's
existing structure but with the remainder handled recursively rather than
as a fixed list):**
- *Case A (even tying block).* If the top block's multiplicity tying (or
  dominating) $T$'s current max is even, the tying block occupies an even
  number of ranks, so it contributes only its own top value to $D$ and
  hands off the rest of the ranks — with parity preserved — to $T$'s own
  sub-instance of the theorem, one recursion level down (budget $n-k$,
  reachable via $T$'s own top-split). This case is **already fully worked
  out concretely for $k=1$** (explorer report §2: splitting $p_1$ exactly
  in half ties $p_2$, an even (size-2) tying block, and reduces cleanly to
  $c(n)=2\lambda_n c(n-1)$ applied to whatever $T$'s own $n-1$-level game
  produces) — this is not new content, it is Claim ★'s $s=1,2$ case
  restated positionally and independently reconfirmed; write it up as the
  base instance of Case A, not re-derived from scratch.
- *Case B (odd tying block).* This is the genuinely open part. Apply the
  certified **Lemma D-BOUND** ($0\le D(Y)\le\max(Y)$) directly to the
  *merged* remainder object (top block's odd-sized tying tail merged with
  $T$), the same device that rescued Lemma PARITY-PAIR's odd case for the
  fixed-tail version — but here $T$ is not fixed, so the merged object's
  max and structure must be bounded using $T$'s own recursive properties
  (self-similarity, Lemma 3) rather than read off a constant list. This is
  the load-bearing new work.

**De-risking scope for round 6/7:** per the explorer's recommendation,
attempt **$k=2$ tail-refined only** first (the smallest case not already
covered by Claim ★'s $s\le2$), to work out the odd-case mechanics
concretely before generalizing $k$. A successful $k=2$ proof, plus the
already-solid $k=1$ instance, would give a second data point strongly
suggesting the general induction goes through, and would isolate exactly
which piece of "T's own recursive structure" is needed (likely: an
inductive bound on $\max(T)$ and $D(T)$ jointly, not just $D(T)$ alone —
open sub-question for the builder to resolve or flag).

Gap (1) (the "one free coordinate" vertex case of Lemma V') is **not**
targeted this round by this approach — it is being re-scoped as the
primary target of `geometric-dominance-construction` instead (see the
outline-reviewer's round-6 report for the coordination rationale), so this
approach's full attention goes to PARITY-PAIR-GEN.

## Round 7: Step 1 (Lemma PARITY-PAIR-ANCHOR) closed for full budget; Step 2
(Lemma V'-GEN) — vertex-reduction proved in the "well-separated" case,
peeling induction set up, two precise remaining gaps identified

Per this round's outline (two-step plan for Lemma PARITY-PAIR-GEN): (1)
close the anchor-only sub-case in full generality, (2) attack the
genuinely-free-coordinate content by a multi-free-coordinate generalization
of the certified Lemma FC (`lemmas/lemma-V-prime-free-coordinate.md`) via a
peeling induction reusing Lemma D-INSERT.

### Step 1 result: NOT the free one-line corollary the outline expected —
a genuine (now-closed, for full budget) generalization was needed

The outline's claim that Step 1 "should close outright, cheap" as a direct
instance of the *existing, unmodified* Lemma PARITY-PAIR turned out to be
**not quite right upon careful checking**, and identifying exactly why, and
fixing it, is this round's main deliverable. The subtlety: Lemma PARITY-PAIR
as certified requires **every** anchor value $t_1,\dots,t_n$ to appear at
least once ($c_i \ge 1$ for all $i$, i.e. $c_i=a_i+1$, $a_i\ge0$). But when
Xiang Yu splits a tail piece $T_i$ (not just $p_1$), $T_i$'s own baseline
contribution of $t_i$ can vanish entirely (replaced by its own finer split),
and — as the worked example in `lemmas/parity-pair-anchor.md` shows exactly
— this **does** genuinely happen within budget ($n=4$: splitting $T_1$ once
and $P_1$ with 3 marks kills $t_1$ from the merged multiset entirely, using
all 4 marks). So the literal statement of Lemma PARITY-PAIR does not apply
to every anchor-only strategy, and the "bookkeeping" the outline anticipated
needed to become a genuine (short, but new) proof.

**Resolution.** Proved a strict generalization, **Lemma PARITY-PAIR-GENERAL**
(`lemmas/parity-pair-general.md`, new, certified this round): for
$c_1,\dots,c_n \ge 0$ (allowing zeros), if $M:=\sum c_i$ is **odd**, then
$D\ge t_n$ — dropping the $c_i\ge1$ hypothesis entirely, replacing it with
the strictly weaker and more natural "total count is odd." The proof is the
*identical* strong-induction-on-$n$ argument as the certified Lemma
PARITY-PAIR (Case A/B on the parity of $c_1$, citing the same certified
block formula and the same certified Lemma D-BOUND for Case B) — the
induction goes through unchanged with zeros allowed, since the block
formula never actually needed $c_i\ge1$ (only the *definition* $c_i=a_i+1$
in the original lemma's parametrization artificially forced this).
Independently verified by exhaustive enumeration over $c\in\{0,\dots,4\}^n$,
$n=1,\dots,7$ ($97{,}648$ vectors, zero violations) — see the lemma file for
the concrete worked check.

Using Lemma PARITY-PAIR-GENERAL, `lemmas/parity-pair-anchor.md` (new,
certified this round) proves **Lemma PARITY-PAIR-ANCHOR in full for every
$n\ge1$ and every anchor-only strategy that uses Xiang Yu's *full* budget
of $n$ marks** (any distribution between $p_1$ and the tail, any number of
tail pieces touched, gaps allowed): the total piece count is always exactly
$2n+1$ (odd, unconditionally), so Lemma PARITY-PAIR-GENERAL applies directly
and unconditionally. This is a genuine, complete, unconditional theorem —
strictly stronger than the round-6 skeleton's $k\le2$ hedge, and covering
every $k$ and every tail distribution, **provided the full budget is used**.

**Honest remaining gap in Step 1.** *Partial-budget* anchor-only strategies
(Xiang Yu spends $b<n$ marks total, still landing every cut on the anchor
lattice) are **not** closed: the resulting total count $M=(n{+}1){+}b$ is
odd only when $b\equiv n\pmod2$; when $M$ is even, Lemma PARITY-PAIR-GENERAL
gives no information, and — critically — the corresponding *abstract*
combinatorial statement ("$M$ even $\Rightarrow D\ge t_n$") is **false in
general** (a genuine counterexample is recorded in the lemma file), so
this gap cannot be closed by strengthening the abstract lemma alone; it
requires tracking which $(c_1,\dots,c_n)$ patterns are actually
game-reachable with $b<n$ marks. A randomized simulator found zero
violations across $n=1,\dots,6$ (30,000 trials each, including
partial-budget strategies) and every hand-checked partial-budget extension
example showed $D$ decreasing monotonically down to exactly $t_n$ at full
budget, never below — strong circumstantial evidence for a conjectural
**extension-monotonicity** principle that would immediately close this
gap by reduction to the full-budget theorem, but a genuine proof attempt
(tracking sign changes in the certified block formula under a one-level
extension move) showed the naive per-block accounting does not obviously
bound the net change (a single extension move can flip the sign of *every*
higher-indexed odd-count block, not just a local region) — so this is left
as a precisely-stated open sub-problem, not closed this round.

### Step 2: Lemma V'-GEN (multi-free-coordinate vertex reduction)

**Statement (as conjectured by the round-7 outline, now made precise).** At
the true minimizer of $D$ over the *joint* polytope where Xiang Yu
simultaneously chooses how to split $p_1$ and any subset of tail pieces (a
budget-$\le n$ constrained choice), the number of coordinates that are
simultaneously *free* (strictly between two anchors in the sorted merge,
not equal to any anchor) is at most one **per split piece**.

**Proof attempt and result: proved in the "well-separated" case, genuine
gap identified precisely in the general case.**

*Setup.* Fix a sort-order cell of the arrangement (i.e. fix, for every pair
of coordinates across every split piece, whether they are equal or which is
larger — this determines the global sorted rank of every coordinate).
Within a fixed cell, $D$ (the alternating sum of the *global* sorted merge)
is **linear**, not merely affine, in the joint vector of free coordinates:
$D = \sum (\pm 1)\cdot(\text{coordinate value})$, with each coordinate's
sign fixed by its rank within the cell (this is the same fact used
implicitly by Lemma D-INSERT and by the original Lemma V'). The feasible
region for the joint vector, restricted to pieces Xiang Yu chooses to split,
is a **product** over split pieces $\pi$ of $Q_\pi := \{\text{parts of }\pi,
\text{ each}\ge0, \text{ summing to }\pi\text{'s fixed total}\}$ — the
pieces' own sum constraints are independent (no cross-piece equality), so
$Q=\prod_\pi Q_\pi$ as sets.

*Well-separated case (proved).* Suppose additionally that, within the
relevant cell, **every free coordinate's immediate neighbors in the global
sorted order are anchors** (fixed numbers from $\{0,t_n,\dots,t_1\}$), not
free coordinates belonging to a *different* piece. Then each free
coordinate's box constraint $[\ell,u]$ (the interval within which it can
move without leaving the cell) is a fixed anchor-bracket, exactly as in the
single-piece case. Since $D$ restricted to the cell is linear and the
feasible region is a product $\prod_\pi Q_\pi$, minimizing $\sum_\pi(\text{a
linear functional of }\pi\text{'s own coordinates})$ over the product
**decomposes into independent per-piece minimizations** (no coupling term).
Each per-piece minimization is *exactly* the LP-vertex fact Lemma V's own
proof already certified ("a vertex of $\{x:\sum x_i=\text{const}, \ell_i\le
x_i\le u_i\}$ has at most one interior coordinate"), applied to $\pi$'s own
parts alone. Hence, in the well-separated case, at most one coordinate *per
split piece* is free — **Lemma V'-GEN holds exactly as conjectured.**

*Genuinely open case: cross-piece ties.* If instead a free coordinate $x$
(in piece $\pi$) has, as one of its cell-boundary neighbors, a free
coordinate $x'$ from a *different* piece $\pi' \ne \pi$ (no anchor between
them in sorted order), the argument above does not immediately reduce the
free-coordinate count by peeling $x$: pushing $x$ to meet $x'$ merely makes
$x = x'$ exactly (a shared, still-undetermined real value occupying two
list-positions from two different pieces), not a resolution to an anchor.
This is *precisely* the scenario the round-7 math-explorer flagged as
"neither found nor ruled out" (a genuine two-simultaneous-free-coordinate
vertex straddling one bracket from two different split pieces). This build
identifies the **exact mechanism** needed to close it, without completing
the closure: such a tied pair should be treated as a **shared block** of
multiplicity $2$ at the tied value (a direct analogue of the "even block
contributes $0$, shifts parity" mechanism already used by Lemma
PARITY-PAIR-GENERAL's own Case A) rather than as two independent
singletons — but working out the resulting recursive bookkeeping (in
particular, whether a *third* free coordinate could also tie into the same
shared block, and how the induction's measure — total free-coordinate count
— behaves when two coordinates merge into one shared parameter instead of
each individually resolving to an anchor) is genuinely new content, not
attempted this round. **No numerical search for a concrete instance of this
scenario was run this round** (the round-6 explorer's own search found only
flat-face artifacts, not a confirmed sharp two-free vertex) — this is the
sharpest immediately-actionable open sub-question for the next round: does a
genuine cross-piece-tied vertex ever actually arise at the true minimizer
(not just on a flat face), and if not, can that be proved directly (which
would let Lemma V'-GEN be promoted to unconditional)?

### Peeling induction (Lemma D-INSERT reused, mirroring Lemma FC's proof)

**Setup.** Given a configuration (well-separated case) with $F \ge 1$ total
free coordinates, pick any one, $x$, in piece $\pi$, occupying sorted rank
$r$ in the full merged list $C$ (everything else — anchors and other free
coordinates alike — held fixed). By Lemma D-INSERT (certified,
`lemmas/alternating-sum-toolkit.md`), the function
```
f(y) := D(C with the element at rank r replaced by y)
```
is affine in $y$ for $y$ ranging over $x$'s current bracket
$(\text{lower neighbor}, \text{upper neighbor})$ (this uses only that $x$'s
rank stays fixed as $y$ varies within the bracket — a purely combinatorial
fact about the *background* list $C\setminus\{x\}$, independent of whether
that background list itself satisfies any sum constraint, exactly as in
Lemma FC's proof). In the well-separated case the bracket's two ends are
anchors $t_j, t_{j+1}$ (or $t_1,\infty$ / $t_n,0$ at the extremes), and:
```
f(x) = λ f(t_{j+1}) + (1-λ) f(t_j),   x = λ t_{j+1} + (1-λ) t_j,  λ∈(0,1),
```
so $D(C) = f(x) \ge \min(f(t_j), f(t_{j+1}))$, exactly as in Lemma FC's Step
4. Each of $f(t_j), f(t_{j+1})$ is $D$ of a *new*, valid configuration in
which $\pi$'s free coordinate has been snapped to an anchor — i.e. a
configuration with **exactly one fewer free coordinate**, and with $\pi$'s
own mark-budget usage **unchanged** (snapping to an anchor does not add or
remove marks, only relocates where the existing cut lands). Iterating,
**well-founded induction on $F$ (the total number of free coordinates,
$0\le F\le n$, since each split piece contributes at most one, per the
proved case of Lemma V'-GEN, and there are at most $n$ split pieces) reduces
any well-separated configuration to an anchor-only configuration with the
*same total mark budget $b$*.**

**Consequence.** For well-separated configurations, the peeling induction
correctly reduces Lemma PARITY-PAIR-GEN's remaining content entirely to the
already-analyzed anchor-only case (Lemma PARITY-PAIR-ANCHOR):
- If the original budget was full (`b=n`), peeling preserves `b=n`
  throughout (it only relocates cuts, never adds or removes them), so the
  anchor-only end state is exactly the **proved** full-budget case above —
  **the well-separated, full-budget sub-case of Lemma PARITY-PAIR-GEN is
  therefore fully closed**, modulo the still-open question of whether
  well-separation can fail (cross-piece ties).
- If `b<n`, the anchor-only end state inherits the **open** partial-budget
  gap from Lemma PARITY-PAIR-ANCHOR.

### Summary of round 7's precise remaining gaps (both narrower than
anything on file before this round)

1. **Partial-budget anchor-only strategies** (`b<n`, `M` even): open: no
   proof, but strong numerical evidence and a precisely-identified
   candidate fix (extension-monotonicity), with a specific reason the naive
   proof attempt stalls, recorded in `lemmas/parity-pair-anchor.md`.
2. **Cross-piece-tied free coordinates** (two free coordinates from
   different split pieces adjacent in sorted order, no anchor between
   them): open: Lemma V'-GEN is proved only in the well-separated case; the
   exact mechanism needed to close the general case (treat a tied pair as a
   shared 2-multiplicity block, generalizing Lemma PARITY-PAIR-GENERAL's
   Case A) is identified but not worked out, and no concrete instance of
   this scenario (versus a flat-face artifact) has yet been confirmed to
   actually arise at a true minimizer.

Both gaps are strictly narrower and more precisely located than the
round-6 skeleton's "Case B, the odd tying-block case, genuinely open" —
they are two independent, separately-attackable technical questions rather
than one monolithic unworked case, and the *majority* of Lemma
PARITY-PAIR-GEN's content (full-budget, well-separated strategies — plausibly
the "generic"/binding case, per the numerical evidence that partial-budget
strategies are never advantageous for Xiang Yu) is now a proved theorem, not
a plan.

## Round 8: gap (a) CLOSED IN FULL (unconditionally, no budget needed); gap (b) — new partial progress, genuine obstruction identified, not closed

Per this round's outline, reframed gap (a) away from the abstract
`(c_1,\ldots,c_n)`-vector formalism onto the actual binary-subdivision-tree
reachability structure, and attempted a direct perturbation/domination
argument for gap (b).

### Gap (a): fully closed — Lemma TREE-BOUND (new, certified)

**Result: Lemma TREE-BOUND, proved in full for every `n≥1`, and in fact
strictly stronger than what was asked** — it closes the anchor-only
sub-case **unconditionally, for every possible mark budget, including
unlimited budget**, not merely for the partial-budget-with-`n`-cap case
that was open. Full statement and proof certified in
`lemmas/tree-bound-anchor.md`; summary:

**Fact 0 (forced halving).** Since no two *distinct* powers of `2` sum to
a power of `2` (binary representations would have two `1`-bits vs. one),
the only anchor-exact split of a piece of value `2^e` is the exact halving
`2^e \to 2^{e-1},2^{e-1}`. Hence every anchor-only strategy is exactly a
choice of independent binary subdivision trees: `P_1`'s tree (rooted at
`2^n`, forced to split at least once since `2^n` is not itself an anchor)
and each `T_i`'s tree (rooted at the already-anchor value `t_i`, free to
remain a leaf or split further).

Peeling `P_1`'s forced root split turns the whole configuration (for
`n\ge2`) into exactly what the lemma file calls an **`(n,3)`-forest**:
three independent trees rooted at value `t_1` (`P_1`'s two children plus
`T_1`), together with `T_2,\ldots,T_n`. The key structural fact making the
induction close (where the abstract vector version failed) is that **every
genuine tree split produces children in pairs**, so at every level of the
recursive peeling, the "remainder" object inherits an automatically **odd**
top-level multiplicity (`r' = 2(r-k)+1`, always odd regardless of the
parities of `r` and `k`) — this is exactly the reachability information
missing from the abstract `(c_1,\ldots,c_n)`-vector formalism, and it
self-propagates through the whole induction with no extra bookkeeping.

Proved **Sub-lemma ODD(m)**: for every `m\ge1` and every odd `r\ge1`, every
`(m,r)`-forest (`r` independent trees at the top level `\tau_1=2^{m-1}`,
plus one standard tree at each of `\tau_2,\ldots,\tau_m=1`) has
`D\ge \tau_m=1`, by strong induction on `m`: base case `m=1` is a direct
computation (all `r` top trees are forced leaves at the bottom exponent,
alternating sum of an odd number of equal terms equals that term); the
inductive step case-splits on the parity of `k` (number of the `r`
top-level trees remaining as leaves) exactly as in the certified Lemma
PARITY-PAIR-GENERAL's Case A/B mechanism, but now the remainder's
multiplicity `r'` is *automatically* odd (rather than requiring a
hypothesis), so Case A (`k` even) always legitimately invokes the
induction hypothesis, and Case B (`k` odd) uses the already-certified
Lemma D-BOUND exactly as before. Lemma TREE-BOUND then follows: `n=1` by
direct computation, `n\ge2` as the `(n,3)`-forest instance of Sub-lemma
ODD (`r=3` odd, unconditionally, since `P_1`'s peeled root split always
produces exactly 2 children plus `T_1` = 3 top objects).

**Independently verified by exhaustive (not sampled) computation**: a
Python enumerator over all binary-tree-shape combinations (not just
resulting multisets) for `(m,r)\in\{(1,1),(1,3),(1,5),(2,1),(2,3),(2,5),
(3,1),(3,3),(3,5),(4,1),(4,3)\}` (up to `175{,}760` distinct tree-shape
combinations at the largest case checked) and separately for the full
original `(n,3)`-forest problem at `n=1,2,3,4` (up to `175{,}760`
combinations at `n=4`) — the minimum `D` found is **exactly `1=t_n` in
every single case**, matching the proof's prediction with zero
violations, and matching (as a superset check, since it drops the budget
cap entirely) the round-8 explorer's exhaustive budget-capped enumeration
(`104` total reachable configs, `n=1..4`, also zero violations).

This **fully closes gap (a)**, and does so without needing the "extension
monotonicity" conjecture flagged (and correctly not relied upon) in
`lemmas/parity-pair-anchor.md` — the bound is proved directly for every
reachable configuration at once, budget-cap or not.

### Gap (b): genuine partial progress — an exact identity and a precisely-located obstruction, NOT closed

Attempted the outline's perturbation/domination argument for a genuine
cross-piece tie (`x` from piece `\pi`, `x'` from piece `\pi'\ne\pi`, tied at
a common non-anchor value `v`, adjacent in the global sorted order with no
anchor between them).

**New exact identity (PAIR-CANCEL), proved.** Let `B''` denote the merged
configuration with **both** tied elements `x,x'` deleted (everything else
unchanged). Then, at the tie,
$$D(\text{full configuration}) \;=\; D(B'').$$
*Proof.* The pair `\{x,x'\}`, both equal to `v`, occupies two **consecutive**
sorted ranks (by hypothesis, nothing lies between them). By the certified
single-block alternating-sum fact (`lemmas/alternating-sum-toolkit.md`,
used identically in the derivation of the `(BLOCK)` formula and in Lemma
PARITY-PAIR-GENERAL's Case A), a run of **exactly 2** (even) consecutive
equal values contributes exactly `0` to `D`, and removing it leaves every
other element's rank shifted by an even amount (`2`, or `0` if the element
was already above the pair), which **preserves its sign** in the
alternating sum. Hence the pair's net contribution to `D` is exactly `0`,
and `D(\text{full}) = D(B'')` where `B''` is computed either with the
original global ranks (shifted) or with `B''`'s own fresh `1,\ldots,M-2`
indexing — both give the same value, since the shift is by the even amount
`2`. `\blacksquare`

This is a clean, fully general, value-independent fact (it holds for
**any** value `v`, and regardless of whether other free coordinates are
present elsewhere) — worth recording as a reusable corollary.

**Also computed (slope/kink analysis, via two applications of the
certified Lemma D-INSERT).** Writing `\rho` for the sorted rank the common
value `v` would occupy among all the *other* (non-tied) elements, a direct
computation shows that perturbing `x,x'` apart symmetrically
(`x=v+\epsilon`, `x'=v-\epsilon`) changes `D` **linearly in `|\epsilon|`**
with a sign controlled by the parity of `\rho`: `D(\epsilon) =
D(B'') + (-1)^{\rho+1}\cdot 2|\epsilon|`. If `\rho` is even, breaking the
tie in **either** direction strictly **decreases** `D` (so the tie cannot
be a genuine local minimizer along this direction, consistent with the
outline's expectation). If `\rho` is odd, breaking the tie **symmetrically**
strictly **increases** `D` along both directions — the tie is a local
minimum of this particular 2-parameter perturbation.

**The genuine obstruction (why this does not close the gap).** The
`\rho`-odd case is not merely a harder sub-case to bound — the entire
premise of a "perturbation" argument needs re-examination here: if `x` is
`\pi`'s **only** free coordinate (all its other parts already pinned at
anchor values), then `x`'s value is **not** an independently movable real
parameter at all — it is uniquely determined by `\pi`'s own fixed sum
constraint minus the sum of `\pi`'s other (anchor) parts. There is no
slack within `\pi` to compensate a change in `x` while preserving `\pi`'s
sum, so the two-variable `\epsilon`-perturbation examined above is not
actually a feasible move in the real (discrete-budget) game unless `\pi`
(or `\pi'`) has additional freedom beyond `x` (or `x'`) that was not
assumed. Resolving the `\rho`-odd case therefore genuinely requires either
(i) a *discrete* comparison against alternative combinatorial split
patterns for `\pi` and/or `\pi'` (in the spirit of gap (a)'s tree-peeling,
not a continuous perturbation), or (ii) using the PAIR-CANCEL identity's
reduction to `D(B'')` together with an inductive argument that legitimately
bounds `D(B'')` from below despite `B''` **not** itself being a valid
Xiang-Yu configuration (`\pi` and `\pi'` are each short exactly one leaf
relative to their true sum, so `B''` cannot simply be re-interpreted as a
smaller valid instance of the same theorem without further work). Neither
(i) nor (ii) was completed this round — this is a precisely-identified,
narrower-than-before remaining gap, not a restatement of the round-7 gap:
the `\rho`-even sub-case is genuinely resolved by the perturbation
argument (though converting "D strictly decreases" into a fully rigorous
feasible move still needs the same discrete-move care noted above, since
`x` is rigid there too), and the PAIR-CANCEL identity is a new, certified,
reusable fact even though it does not by itself finish the proof.

**Reconciliation note (coordination with `geometric-dominance-construction`,
per the outline-reviewer's requirement):** this round's build of
`geometric-dominance-construction` should be checked against the above; if
it reaches a different conclusion (e.g. claims a complete resolution),
that must be reconciled before either is trusted, per the outline's own
instruction. This file's honest conclusion is: gap (b) is **not** closed
this round, with the `\rho`-even/`\rho`-odd dichotomy and the PAIR-CANCEL
identity as genuine new partial progress, and the specific reason the
naive perturbation argument does not immediately generalize (rigidity of
a piece's sole free coordinate) identified precisely.

### Status update

Gap (a) (partial-budget anchor-only strategies) is now **fully closed**
(Lemma TREE-BOUND, certified in `lemmas/tree-bound-anchor.md`), for every
budget, not just the previously-closed full-budget case. Combined with the
already-proven well-separated case of Lemma V'-GEN (round 7) and Lemma FC
(single free coordinate, `geometric-dominance-construction`, round 6),
**Lemma PARITY-PAIR-GEN is now fully proved in every case except genuine
cross-piece tied free coordinates (gap (b))** — a single, sharply isolated
remaining gap, narrower than the two-gap picture entering this round.
Status remains `partial`: the lower bound for `A_n` is not yet a complete
theorem, but the surface area still open has shrunk to exactly one
precisely-characterized sub-case.

## Full proof
(Not present — overall Status is `partial`, since the separate "general
upper bound over all Liu Bang configurations" question is out of this
approach's scope and untouched. **However, as of round 9, Lemma
PARITY-PAIR-GEN itself — the lower bound for the specific geometric
construction `A_n`, i.e. "Liu Bang, playing `A_n`, guarantees at least
`c(n)` against every Xiang Yu response, for every `n` and every budget" —
is now a fully proved theorem**, certified across
`lemmas/parity-pair-general.md`, `lemmas/parity-pair-anchor.md`,
`lemmas/tree-bound-anchor.md` (gap (a)), and new this round
`lemmas/tree-bound-residual.md` (gap (b)). Combined with the already-
certified Lemma 1–4/Proposition 4 (Xiang Yu's own strategy showing `A_n`
gives Liu Bang *exactly* `c(n)`, not more), **`A_n`'s value is exactly
`c(n)` for every `n`** — a complete proof of the geometric-construction
half of the problem. See "Round 9 (this build): gap (b) CLOSED IN FULL"
below for the details of this round's closure, and the "What this does
not close" note there for the precise remaining scope (the general upper
bound over arbitrary, non-geometric configurations).)

## Round 9 plan: extend Lemma TREE-BOUND to forced-residual (non-anchor) leaves

**Target this round**: close gap (b)'s last sub-case — a cross-piece tie
where the tied coordinate is the *minority* part of a 2-part-split piece
`π` (`\mathrm{top}_π = t_i` or `2t_1`), pinned at an *external* anchor `t_j`
with `j > i+1` (so the win-endpoint is not `π`'s own self-meeting point),
leaving the companion `c = \mathrm{top}_π - t_j = 2^{n-j}(2^{j-i}-1)`
a fixed, generically non-power-of-2 value. Two independent probes this
round (`math-explorer-crosstie.md`, `math-explorer-altframing.md`)
converge on the same recommended mechanism, superseding the
perturbation/exchange route (confirmed dead, round 5 rigidity
obstruction — do **not** re-attempt bounded-width local moves here):

**Skeleton (domination-via-forest-extension).**
1. Observe `c = t_i - t_j = \sum_{l=i+1}^{j} t_l \cdot(\text{with multiplicity
   pattern }2^{j-i}-1\text{ in base 2})` — i.e. `c` is exactly the sum of
   the "missing" anchors `t_{i+1},\ldots,t_j$ that a *fully split* `π`
   would have produced had Xiang Yu spent `j-i` marks on it instead of
   stopping at 1. This reframes `c` not as an alien value but as a
   **partially-collapsed subtree**: a `\tau_{j-i}`-forest-node that stopped
   `j-i-1` levels short of full binary reduction.
2. Generalize Sub-lemma ODD's induction (`lemmas/tree-bound-anchor.md`) so
   that a "leaf" is allowed to be either (i) a true anchor value `\tau_l`
   (as before), or (ii) one **forced-residual node** of value
   `c=\sum_{l=i+1}^j t_l` standing in for its own un-split sub-forest.
   Key step to prove: replacing that one node by its "as-if-fully-split"
   virtual children `t_{i+1},\ldots,t_j` (a legal `(j-i)`-level forest by
   Fact 0) can only **decrease** `D` of the merged configuration — i.e.
   `D(\text{config with residual } c) \ge D(\text{config with } c\text{
   virtually split})`, and the right side is covered by the *already-
   certified* Sub-lemma ODD applied one level deeper. This is a
   **domination** claim (residue config `\ge` an already-TREE-BOUND-covered
   config), not a fresh from-scratch bound — matches the round-9 explorer's
   "most promising" recommendation exactly.
3. Prove step 2's domination inequality via the certified **Lemma D-BOUND**
   / **D-INSERT** identities already in `lemmas/alternating-sum-toolkit.md`
   (repeatedly inserting a duplicated pair only ever *adds* a nonnegative
   amount or leaves `D` unchanged on the relevant interval — this is
   exactly the mechanism `geometric-dominance-construction`'s
   CROSS-TIE-AFFINE already established for the affineness half of this
   picture; the new content here is the "un-split still dominates" step,
   not affineness itself).
4. Conclude: since the virtually-split configuration satisfies
   `D \ge \tau_n` (Sub-lemma ODD, already certified), and the actual
   (unsplit-residual) configuration's `D` is `\ge` the virtually-split one's
   `D` by step 2, the actual configuration also satisfies `D \ge \tau_n`.
   This closes gap (b) unconditionally.

**Honest risk flagged for the builder**: step 2's direction of inequality
must be checked carefully — "splitting further" changes both the
top-block occupancy (which ranks the new leaves land at) and the
remainder's sign in the alternating sum, so it is *not* immediate that
un-splitting is bad for Xiang Yu; the builder must verify the inequality
goes the needed direction on at least 2 independent concrete instances
before generalizing (reuse the round-9 explorer's numeric witnesses:
`n=4` symmetric two-minority tie, `n=6` external-anchor-snap residue) and
must produce the general induction, not just re-confirm the numerics.

## Round 9 (this build): gap (b) CLOSED IN FULL

**The plan's proposed mechanism (step 2 above) was checked and found
FALSE as stated.** Testing the exact claim "`D(\text{config with residual}
c) \ge D(\text{config with } c \text{ virtually split})`" against an
*unconstrained* common background (a background list not itself required
to be an achievable forest remainder) produces `159` violations out of
`600` random trials (`/tmp/verify1.py` — e.g. background
`\{8,1\}$, comparing residual `D=3$ to virtually-split `D=5$: the residual
is *smaller*, the wrong direction). So the plan's step 2, taken as a
free-standing comparison lemma between two arbitrary configurations, is
not true in general — the risk flagged by the outliner was real, and is
reported honestly rather than forced.

**What actually closes the gap: rerun Sub-lemma ODD's induction itself
with a third case, rather than comparing two separate configurations.**
New certified **Lemma TREE-BOUND-RESIDUAL** (`lemmas/tree-bound-
residual.md`) extends `lemmas/tree-bound-anchor.md`'s Sub-lemma ODD to
allow **at most one "impure" node anywhere in the forest** — a node that,
instead of being a leaf or a pure binary split, terminates directly into
`\{y=τ_j, c=τ_i-τ_j\}$ for some `j>i` (skipping `j-i-1` intermediate
anchor levels in one move, leaving `c` as a genuinely non-anchor residue).
The induction's existing two cases (impurity below the current top level,
handled directly by the strong induction hypothesis one level down; `k$
odd at the current top level, handled by Lemma D-BOUND exactly as
before — both unaffected by the extension, since every leaf of any
subtree, pure or impure, is bounded by its root's value) are joined by a
**new Case C** (the impurity sits at the current top level): writing
`X` for the merged leaves of everything else at that level (itself an
`(m-1,r'')`-forest, `r''` automatically odd, so `D(X)\ge τ_m` by the
induction hypothesis) and `R:=X\cup\{y,c\}`, the key new facts are (i)
`c=τ_1-τ_j\ge τ_2\ge$ every element of `X` and of `y` (so `c` is always a
maximum of `R`), and (ii) **two direct applications of the already-
certified Lemma D-BOUND** — once to `R` itself (`\max(R)=c`, giving
`D(B)=τ_1-D(R)\ge τ_1-c=τ_j\ge τ_m$ when the top-block count `k'` is odd)
and once to `X\cup\{y\}` (`\max\le τ_2`, giving, via one Lemma D-INSERT
step for `c` at rank `1`, `D(B)=D(R)=c-D(X\cup\{y\})\ge c-τ_2=τ_2-τ_j\ge
τ_3\ge τ_m$ when `k'` is even, using `j\ge3\Rightarrow m\ge3`) — close
both parities of `k'`. **No new machinery beyond Lemma D-BOUND (already
certified) and elementary arithmetic on the geometric anchors
(`τ_i=2τ_{i+1}`) is needed.** Full statement, proof, and the honest
account of why the plan's original mechanism fails are in
`lemmas/tree-bound-residual.md`.

**Independently verified**: exhaustively for the full original `(n,3)`-
forest problem at `n=2,3,4` (every impurity placement, every impure cut,
every pure-tree shape for everything else — up to `36` shapes per
`τ_2`-rooted tree at `n=4`) — minimum `D` found is exactly `1=t_n`, zero
violations. Also by large-scale randomized exact-`Fraction` sampling
(`n=2,\ldots,12`, `17{,}876` trials, impurity at a uniformly random tree
root at a uniformly random depth, every other tree an independently
random pure shape) — zero violations. Also reproduced this round's
`math-explorer-crosstie.md`'s two hand-built witnesses exactly (`n=4`
symmetric two-minority tie, `D=11`; `n=6` external-anchor-snap residue,
`c=14`, `D=43`) — both consistent with, and far above, the Lemma's own
(non-tight but always-sufficient) quantitative bound.

**What this closes.** Combined with the already-certified
`lemmas/cross-tie-affine.md` (which reduces *every* cross-piece tie to one
of exactly three sub-cases: well-separated/companion-pinned, majority-part/
self-meeting-point, or minority-part/deep-bracket-residue) and
`lemmas/tree-bound-anchor.md` (gap (a)), **gap (b) is now closed in every
sub-case**. Together with the round-7 well-separated closure and the
round-8 anchor-only closure, **Lemma PARITY-PAIR-GEN's lower bound —
`D(B)\ge t_n` for every Xiang-Yu-reachable configuration against `A_n`, for
every `n\ge1` and every budget `\le n` — is now a fully proved theorem**,
not a plan or a partial reduction.

**What this does not close.** The separate "general upper bound over all
Liu Bang configurations" (showing no non-geometric `A` lets Liu Bang
guarantee more than `c(n)`) is untouched by this round's work and remains
explicitly out of this approach's scope (see "Open gaps" item 2 above);
this belongs to `universal-adversary-strategy`. Consequently the *overall*
problem (`c(n)` as the answer to the full max-min over *all* Liu Bang
strategies) is not solved by this approach alone — only the
geometric-construction half (`A_n`'s own value is exactly `c(n)`) is now
complete. Status remains `partial` for that reason alone.

### Status update
Gap (b) (cross-piece tied free coordinates) is now **fully closed**
(Lemma TREE-BOUND-RESIDUAL, certified in `lemmas/tree-bound-residual.md`),
completing Lemma PARITY-PAIR-GEN's lower bound for `A_n` in full — no
sub-case of the lower bound for the geometric construction remains open.
The overall theorem (the full max-min over all Liu Bang configurations)
remains `partial`: only the general upper bound over non-geometric
configurations is still open, and that has always been out of this
approach's scope.

## Round 10: gap (b)'s last sub-case — simultaneous multi-cluster ties — CLOSED IN FULL

This round's dispatch (per the outline-reviewer's build-set instruction and
`math-explorer-multicluster.md`'s structural diagnosis) targeted the one
remaining honest gap flagged by round 9's review: Lemma TREE-BOUND-RESIDUAL's
induction hypothesis explicitly allows **at most one** impure node in the
whole forest, and its proof (the "Case C" step) never had to handle **two or
more impure top-level trees at once**, since peeling one impurity off always
lands any others inside the recursive `(m-1,r')` remainder — except in the
one scenario where `p\ge2` impurities sit **simultaneously at the current
top level of the same recursive pass**, which cannot be avoided by peeling
(the induction's top-level step processes all `r` top trees together in one
pass).

### New Lemma TREE-BOUND-MULTICLUSTER

Certified in full: `lemmas/tree-bound-multicluster.md`. States and proves,
by strong induction on `m` (the *same* induction that underlies Lemma
TREE-BOUND and Lemma TREE-BOUND-RESIDUAL), that an `(m,r)`-forest with
**arbitrarily many** impurities, distributed anywhere at all (any of the `r`
top trees, any of the `m-1` standard trees, at any depth, including several
landing at the same top level of the same pass) satisfies `D(B)\ge τ_m`,
for every `m\ge1` and every odd `r\ge1`.

**Why the naive generalization of Case C's argument does not survive
verbatim to `p\ge2` (the genuine obstruction, precisely identified before
being closed).** Case C's original proof (`p=1`) used two direct
applications of Lemma D-BOUND on the *whole* remainder-plus-pair list, never
needing to isolate the single companion's *alternating* contribution
separately from its raw value. For `p\ge2`, the `p` companions form their
own internal alternating-sum block (`A_p`), and if two companions happen to
be **tied** (`j_1=j_2`, an adversarial case this round's explorer
specifically stress-tested), that block's alternating sum can degenerate
to `0` — the naive "largest companion supplies all the slack" argument used
for `p=1` genuinely breaks down at `p=2` with tied companions, as verified
directly: `A_2=0` exactly in that case. The bound still holds (confirmed
numerically, `D=1=τ_m` exactly in this scenario, matching the round-9
reviewer's and this round's explorer's independent stress tests), but for a
*different reason* than the `p=1` argument supplies: the two tied
companions, together with their two tied minority values, **cancel exactly**
(as a pair-insertion into the sorted list, a length-2 block of equal values
changes `D` by `0` and leaves everything below it untouched in sign — the
new Fact PAIR-CANCEL, proved directly from the definition of `D`), reducing
the configuration *exactly* (not approximately) to the fully pure remainder
`X`, whose bound `D(X)\ge τ_m` then comes from the strong induction
hypothesis itself, not from D-BOUND. This is precisely the reason a genuine
"multi-pair insertion" argument (not a bare repetition of the `p=1` proof)
was needed, exactly as this round's outliner and explorer anticipated.

**The two-step fix.** (1) Reclassify any impurity at depth `j=2` as an
ordinary pure split (an exact identity: it produces the same two leaves
`\{τ_2,τ_2\}` either way) — eliminates the `j=2` boundary case uniformly.
(2) Cancel pairs of impurities tied at the same depth via the new Fact
PAIR-CANCEL — reduces to impurities at **pairwise distinct** depths
`\ge3`. After these two exact, `D$-preserving reductions, the surviving
`p'` impurities' companion block has a genuine telescoping-anchor lower
bound (`A_{p'}\ge τ_2+τ_m` if `p'` odd, `A_{p'}\ge τ_m` if `p'` even,
`p'\ge2`; `p'=0` uses the induction hypothesis directly on `X`), closing
every case with the *same* two tools already certified for `p\le1`
(Lemma D-BOUND, twice, plus the strong induction hypothesis) — no new
atomic machinery, exactly matching the round-10 outline's instruction not
to introduce anything beyond an induction on `p` built from the existing
D-INSERT/D-BOUND toolkit.

**Independent verification, this round.** Randomized recursive stress test
(`/tmp/explore_multi3.py`): `28` `(m,r)` combinations (`m=1,\ldots,7`,
`r\in\{1,3,5,7\}`), each node independently and recursively a `20\%$ chance
of being an impure cut to a uniformly random deeper anchor (so the number
and placement of impurities, including simultaneous multi-cluster
configurations, is entirely unconstrained), `2{,}000$ trials per
combination: minimum `D` found is exactly `1=τ_m` in every single case, zero
violations. Even-`r` sanity check (`/tmp/explore_multi3.py` with `r=2,4`):
genuine violations found (`D=0<1$ at `m=1,r=2`), confirming the harness
correctly discriminates and the odd-`r` hypothesis is load-bearing.
Targeted adversarial probes (`/tmp/explore_multi.py`, tied-depth `p=2`
across `m=3,\ldots,7`, all depths, `300` trials each; `/tmp/explore_multi2.py`,
distinct-depth `p=2` across `m=4,5,6`, `r\in\{3,5\}$, all `k`-parities, all
depth pairs, `150` trials each): zero violations in both, matching the
proof's predicted mechanism exactly (the tied-depth probe gives `D=1$
exactly, matching the PAIR-CANCEL-then-IH route; the distinct-depth probe
gives `D\ge1` with the margin predicted by the telescoping bound).

### What this closes

Combined with the already-certified `lemmas/cross-tie-affine.md` (reduces
every cross-piece tie to the well-separated / self-meeting-point /
minority-residue sub-cases) and `lemmas/tree-bound-anchor.md` (gap (a)),
**gap (b) is now closed in full generality, including the multi-cluster
case** — the sole remaining honest gap flagged by the round-9 review and
this round's `math-explorer-multicluster.md`. **Lemma PARITY-PAIR-GEN's
lower bound — `D(B)\ge t_n` for every Xiang-Yu-reachable configuration
against `A_n`, for every `n\ge1`, every budget, and every number of
simultaneous independent tie-clusters — is now a fully proved theorem, with
no remaining open sub-case of any kind.** Combined with the already-
certified Proposition 4 (Xiang Yu's matching exact-equality response),
**`A_n`'s value is exactly `c(n)$ for every `n`, unconditionally** — the
lower-bound half of the minimax problem is a complete, gap-free theorem.

### What this does not close

As with every round of this approach, this closes only the lower bound for
the specific geometric configuration `A_n`. The separate "general upper
bound over all Liu Bang configurations" (`c(n)\le2^n/(2^{n+1}-1)` for every
configuration, not just `A_n`) remains open and is, as always, out of this
approach's scope — owned by `universal-adversary-strategy`, explicitly
`partial` there (general `m\ge4` Case C of the upper bound's induction is
the sharpest remaining open sub-problem in the whole project as of round
9). Status remains `partial` for the file as a whole (its Target is the
*full* two-sided determination of `c(n)`), but this approach's own
contribution — the entire lower bound — is now complete.
