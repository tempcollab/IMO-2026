## Status
RETHINK (recommended for retirement, round 9)

## Approaches tried
- `minimax-mixed-duality` (round 6, new). Opened per the outline-reviewer's
  shared-gap-plateau rule: every live approach
  (`recursive-embedding-induction`, `universal-adversary-strategy`,
  `geometric-dominance-construction`) and both dead ones
  (`equalization-potential-bound`, `majorization-smoothing`) share one
  underlying mechanism — a **single deterministic local move** (peel one
  block / exchange one triple / split one or two pieces at hand-picked
  ratios) plus induction or vertex-reduction on the sorted composition.
  Every negative result on file (Claim ★ false for `s≥3`; bounded-width
  move-traps; TAIL-SNIP insufficient; the averaging-gate failure on
  `(1/3,1/3,1/3)`; the rank-weight-vector obstruction; the concavity-kink
  obstruction) is a negative result *about that one mechanism family*. This
  approach attacks the problem with a genuinely different proof *shape*:
  **minimax/LP duality over the full mixed (randomized) strategy space**,
  not a hand-picked deterministic rule or a 2–3-candidate average.
  **First build pass (round 6, this round):** followed the outline's
  instruction to do the cheap/exploratory work (Gap 1, Gap 2) before
  attempting the hard expectation inequality (Gap 3). **Result, honestly
  scoped:** the "mixed strategy" proof device did **not** turn up a
  shortcut avoiding casework — worked example shows that finding the right
  mixing weights is at least as hard as finding the true minimizer directly
  (see "Honest assessment of the mixed-strategy device" below), confirming
  the risk flagged in the round-6 skeleton. However, the *exploratory
  numeric search* over candidate response types (Gap 2) **did** surface a
  genuinely new, general, rigorously proved construction — **Lemma
  SANDWICH** — not previously in any approach's toolkit, which strictly
  beats Lemma TAIL-SNIP on the exact hard witness that
  `universal-adversary-strategy` used to prove TAIL-SNIP insufficient.
  Real, verified, novel progress; proof of the general upper bound remains
  open.

## Current best

**NEW this round (round 6), verified by the builder (30,000 exact-`Fraction`
trials, zero mismatches) but not yet independently re-derived by the
proof-reviewer — see `lemmas/sandwich-split.md`:**

**Lemma SANDWICH.** For any sorted `A=(p_1≥⋯≥p_m)` with `m` **odd**, if
`p_1 < p_2+p_m`, splitting `p_1` (1 mark) into `x∈(max(p_3,p_1-p_m),p_2)`
and `y=p_1-x` gives, exactly and independent of the choice of `x` in that
interval,
```
oddrank(B) = p_2 + p_3 + p_5 + ⋯ + p_m = oddrank(A) - (p_1-p_2).
```
Proved in full by rank-shift bookkeeping (same technique as Lemma DOM /
Lemma SPLIT): `x` lands at rank 2 (even, excluded), `y` lands at rank `m+1`
(even since `m` odd, excluded), every `p_i` (`i≥2`) keeps rank `i`.

**Concretely closes a previously-open witness.** On
`A=(4649,3042,2309)/10000` (`n=2`, the exact instance
`split-and-tail-snip.md` used to prove Lemma TAIL-SNIP alone insufficient,
and where DOM's and HALVE's hypotheses both fail), SANDWICH's hypothesis
`p_1<p_2+p_3` **does** hold (`0.4649 < 0.5351`), and it gives
`oddrank(B)=p_2+p_3=0.5351` exactly — strictly better than TAIL-SNIP's
`0.58035`, using only 1 of the 2 available marks. The round-5 file's
diagnosis that this witness "needs a coordinated simultaneous split of two
pieces at jointly-optimized non-half ratios" is **superseded**: a single
clean 1-mark move suffices after all (the two-piece move found there was a
real alternative optimum, not the *only* way to reach the bound).

**Honest scope limits (numerically established, not full proofs):**
- **Even `m` is not covered** by the SANDWICH construction as stated — an
  exploratory check (not a rigorous feasibility-respecting one) suggests
  the naive analogue degenerates to no improvement there; left open rather
  than claimed either way.
- **SANDWICH + DOM + HALVE + TAIL-SNIP together still do not cover the full
  `m=3` (`n=2`) configuration space.** A systematic sweep (684 sampled
  generic configurations on a fine grid) found this 4-candidate menu
  achieves `min ≤ c(2)` on 504/684 (~74%) and fails to on the remaining
  180 — but spot-checking 4 of those failures against the true unconstrained
  2-mark optimum (via numerical global search) confirms the true optimum
  **is** `≤ c(2)` in every spot-checked case (e.g. `A=(0.8,0.175,0.025)`:
  menu gives no candidate `≤ c(2)`, true optimum `≈0.5125 < c(2)`, achieved
  by splitting `p_1` alone into 3 parts — a construction not in the current
  menu). So the gap is in the **menu's coverage**, not in the theorem: more
  candidate constructions (multi-mark, single-piece splits; joint
  two-piece splits) are still needed for a complete casework proof, exactly
  the situation `universal-adversary-strategy` is independently working on.
  SANDWICH is a genuine, reusable *addition* to that shared toolkit, not a
  replacement for its casework.

**Honest assessment of the mixed-strategy device itself (Gap 2/3).** The
skeleton's hoped-for shortcut — find an explicit, `A`-dependent
distribution over a *small* candidate set whose *expectation* beats
`c(n)`, avoiding exact-minimizer casework — does not obviously pay off:
since only `min_B oddrank(B) ≤ c(n)` is actually needed (not an
expectation bound), the practical content of "find good mixing weights"
collapses to "find enough candidate pure constructions that their `min`
already beats `c(n)`," which is the *same* casework problem
`universal-adversary-strategy` is doing directly, just described in
probabilistic language. No LP-duality shortcut around this was found this
round. The value delivered this round came from the *exploratory numeric
search* step (Gap 2's instruction to search small witnesses for patterns),
which is a general problem-solving technique, not something specific to
the mixed-strategy framing — worth recording honestly rather than
overclaiming the minimax framing itself as the source of progress.

**Lower bound side (Gap 4):** not attempted this round, per the skeleton's
own scoping note that this approach is primarily an upper-bound tool;
unchanged from round 6's opening file.

## Setup (reusing the shared reformulation)

By the certified **claiming-phase value formula**
(`lemmas/claiming-phase-value.md`, imported, do not re-derive):
$$c(n) = \max_A \min_B \operatorname{oddrank}(B)$$
where $A$ ranges over Liu-Bang configurations (multisets of $\le n+1$
positive reals summing to $1$, reachable with $\le n$ marks) and $B$ ranges
over Xiang-Yu refinements of $A$ reachable with $\le n$ further marks;
$\operatorname{oddrank}(S) := a_1+a_3+a_5+\cdots$ for $S$ sorted descending.
The target is $c(n) = 2^n/(2^{n+1}-1)$, both directions:
- **Lower bound** ($\max_A\min_B \ge c(n)$): Liu Bang has *a* configuration
  forcing $\operatorname{oddrank}(B)\ge c(n)\cdot 1$ for every Xiang-Yu
  response — this is the geometric construction $A_n=\{2^{n-i}\}/D$,
  already fully proved (Lemma 1–3, Prop. 4). What is **open** (shared with
  `recursive-embedding-induction`) is that *this specific $A_n$* forces the
  bound against *every* response, for every $k<n$ tail-refined.
- **Upper bound** ($\max_A\min_B \le c(n)$): for *every* $A$, Xiang Yu has
  *some* response $B$ with $\operatorname{oddrank}(B)\le c(n)$ — open in
  general (shared with `universal-adversary-strategy`).

## The new idea: attack the upper bound via a mixed (randomized) Xiang-Yu strategy

**Key observation motivating this approach.** `potential-averaging-bound`
(round 5) tested whether $\min$ over 2–3 fixed, hand-picked deterministic
Xiang-Yu strategies, *averaged*, bounds $\operatorname{oddrank}$ — and it
failed, with a clean diagnosis: every tested candidate is "budget-blind"
(always spends a mark when a local rule fires, never stops early), so
*every* candidate individually already exceeds $c(n)$ on the witness
$A=(1/3,1/3,1/3)$, and averaging two numbers both above a bound cannot push
the average below it. The fix this approach proposes is not "add a third,
cleverer deterministic candidate" (which is what would collapse it into
duplicating `universal-adversary-strategy`'s casework, per the round-5
file's own warning) but to replace the finite, fixed candidate set with the
**full space of mixed strategies**, and derive the mixing *weights* from
$A$ itself via a duality/equalization argument, rather than guessing them.

**Formal statement to build toward (Lemma MIX).** For fixed $n$ and fixed
$A$ (sorted, $m\le n+1$ pieces), consider the *finite* set of "response
types" $\mathcal T(A)$ — combinatorial patterns of which pieces get split
into how many parts and in what relative order, each type $\tau$ a
polytope of continuous split ratios (this finite-type structure is already
established: it is exactly `universal-adversary-strategy`'s cell
decomposition, certified this round via Lemma TIE-NECESSARY, and
`recursive-embedding-induction`'s Lemma V'/vertex-reduction machinery).
Within each type $\tau$, $\operatorname{oddrank}$ is affine in the free
split parameters (shared fact, both sibling approaches already rely on
this). A **mixed Xiang-Yu strategy** is a probability distribution $\mu$
over (type, parameter-point-in-type) pairs. Claim:
$$\exists\, \mu_A \text{ (depending on } A\text{) such that } \mathbb E_{B\sim\mu_A}[\operatorname{oddrank}(B)] \le c(n)$$
for **every** $A$ simultaneously (in fact we only need existence of *some*
response with $\operatorname{oddrank}(B)\le c(n)$, i.e. $\min_B\le
\mathbb E_\mu$ trivially, so proving the *expectation* inequality for an
explicit $\mu_A$ **suffices** for the upper bound — the mixed strategy is a
proof device, not a claim that Xiang Yu must randomize).

**Why existence is not in question (von Neumann), only explicitness.**
Since each type $\tau$'s achievable $\operatorname{oddrank}$ values form a
polytope image and there are finitely many types, $\min_B
\operatorname{oddrank}(B)$ over all $B$ reachable from $A$ is a genuine
min over a finite union of compact convex images — it exists and equals
$\min_\tau \min_{\text{params}\in\tau}(\text{affine fn})$, a finite min of
linear-program optima. **We already know** (assuming the theorem) this
finite min is $\le c(n)$ for every $A$; the open content is a *proof*, and
the minimax/LP-duality reframing's value is that it suggests **which dual
object to exhibit**: not a single global rank-weight vector (already
proved impossible, `equalization-potential-bound`'s Lemma D/E — that
attacks the *lower* bound side's dual, a genuinely different LP), but a
**per-$A$, explicit convex combination of a small, structured family of
extreme responses** (DOM, HALVE, TAIL-SNIP, PARTIAL-DOM, and the
tie-matching responses `universal-adversary-strategy` is characterizing
this round) whose weights are given by a clean formula in $A$'s shape —
turning "prove the exact minimizer beats $c(n)$" into "prove a specific
weighted average beats $c(n)$," which is a strictly easier per-instance
computation **if** the right weight formula can be found, because it
avoids doing exact-minimizer casework on which cell/type is optimal.

## Proof skeleton (gaps to close, in dependency order)

1. **Gap 1 — Formalize the finite-type decomposition explicitly** (mostly
   shared infrastructure, likely importable rather than re-derived): state
   precisely what a "response type" is, that there are finitely many for
   fixed $n,m$, and that $\operatorname{oddrank}$ is affine on each type's
   parameter polytope. This should reuse `universal-adversary-strategy`'s
   Lemma TIE-NECESSARY (round 6) almost directly — TIE-NECESSARY already
   establishes that optima live on cell boundaries, which is the discrete
   structure this lemma needs. **Coordinate with that approach rather than
   re-deriving.**
2. **Gap 2 — Identify the candidate weighting family.** Rather than
   guessing, derive the weights from the *dual LP* at a few small, fully
   worked examples ($n=2$, both the $(1/3,1/3,1/3)$ witness that killed
   `potential-averaging-bound` and the $(4649,3042,2309)/10000$ witness
   from `universal-adversary-strategy`): solve the LP numerically
   (`scipy.optimize.linprog` or exact simplex via `sympy`/`fractions`) for
   the true dual variables at the optimum, and look for a closed-form
   pattern (e.g., weight $\propto$ distance-to-domination-threshold, or a
   softmax-like formula in prefix sums) — **this is empirical/exploratory
   work for the first builder pass**, not yet attempted.
3. **Gap 3 — Prove the expectation inequality for the identified weighting,
   in general.** This is the hard step and may be comparable in difficulty
   to the direct casework — honestly flagged as a real risk, not a
   shortcut, per the round-6 explorer's assessment. If the weighting turns
   out not to have a clean closed form, this approach should report that
   negative finding precisely (which weighting families were tried and why
   they failed) rather than force a fit.
4. **Gap 4 — Lower bound side.** The mixed-strategy device is naturally an
   *upper-bound* tool (Xiang Yu's problem). For the lower bound (Liu Bang's
   geometric construction forces the bound against *every* pure response),
   the dual/minimax framing suggests instead considering *Liu Bang's*
   choice of $A$ as also potentially "mixed" — but Liu Bang's choice is a
   single configuration (not repeated play), so this is less obviously
   applicable. Honest assessment: **this approach's primary target is the
   upper bound (Gap 1–3 above)**; for the lower bound it should first check
   whether the mixed-strategy view offers anything beyond what
   `recursive-embedding-induction`'s direct PARITY-PAIR-GEN induction
   already provides, and if not, explicitly scope this approach as
   upper-bound-only for now (still a valid whole-problem attempt in the
   CLAUDE.md sense, since the upper bound is genuinely half of the minimax
   claim, but should be stated honestly rather than silently dropped).

## Relation to existing dead ends (why this is not a repeat)

- **Not** `equalization-potential-bound`: that approach sought a single
  **rank-only linear functional** $w_i$ with $\operatorname{oddrank}(B)\le
  \sum w_i p_i$ for *every* $A,B$ simultaneously (a global, $A$-independent
  weight vector) — proved impossible (Lemma D/E, interior-point
  obstruction forces $w\equiv c(n)$, tautological). This approach's weights
  are **per-$A$** (a distribution over *responses* to a fixed $A$, not a
  functional on $A$-space itself) — a different mathematical object, not
  ruled out by that obstruction.
- **Not** `potential-averaging-bound`: that approach averaged **2–3 fixed,
  $A$-independent deterministic rules** with no dependence of the mixing
  weights on $A$'s shape — refuted because every candidate was individually
  budget-blind. This approach's mixture is **$A$-dependent** by
  construction (Gap 2), directly targeting that diagnosed weakness.
- **Not** a repeat of `universal-adversary-strategy`'s exact casework: that
  approach seeks the *exact* minimizer (pure strategy) for every $A$; this
  approach seeks an *explicit weighted average* that dominates the exact
  minimizer without identifying it — a different proof shape, though it
  will reuse that approach's Lemma TIE-NECESSARY, PARTIAL-DOM, and
  tie-matching characterization as raw material for the candidate family
  in Gap 2 (a form of coordination, not duplication: consuming certified
  lemmas from a sibling is expected and encouraged, not a diversity
  violation).

## Crux corpus note
No crux in the corpus matches this exact game type (per the round-6
`math-explorer-newframing` search of `combinatorics/games-and-strategy` and
broader keyword sweeps). Adjacent techniques flagged: `aimo-0117` (dyadic
domination sequence — same mechanism as this problem's own Lemma 2/S,
already in use); `aimo-0718` (pigeonhole bound against a bounded-size
blocking adversary — considered and judged likely too weak here, since
exact values, not just counts, are load-bearing — see the explorer's
Framing 3 discussion, not adopted). This approach's mixed-strategy idea is
genuinely adapted from general LP/minimax theory, not transplanted from a
specific crux.

## Round 7 update — gate check on the two hard `m=5` witnesses, and its honest outcome

**Assignment this round** (per the outliner): attempt a duality certificate
over the *full* discrete tie-structure search space implied by Lemma
TIE-NECESSARY (not the fixed named menu), targeting the retargeted theorem
"the TIE-NECESSARY-implied matching/assignment problem always has a
solution `≤c(n)`" — the same theorem `universal-adversary-strategy` is
attacking this round by matching-induction. Mandated gate: cheap numeric
check against the two recorded hard `m=5` witnesses
(`A=(0.4265,0.2536,0.1747,0.1014,0.0438)` and
`A=(0.3415,0.3023,0.1664,0.1404,0.0494)`, budget 4, target
`c(4)=16/31≈0.516129`) from `/tmp/round-7/math-explorer-menucoverage.md`,
which had flagged both as needing "genuine 3-piece simultaneous
coordination" beyond the current (extended) menu.

### What the gate check actually found

Rather than searching for an abstract dual weighting first, the cheapest
possible test of "is there a certificate at all" is to pin down the *exact*
winning tie-structure on the two witnesses and see whether it has a clean
form. Using `scipy.optimize.differential_evolution` + `Nelder-Mead` polish
(script: `/tmp/round-7/dual_probe5.py`), then verifying every candidate
**exactly** in `fractions.Fraction` arithmetic (script:
`/tmp/round-7/verify_exact.py`, both scripts left in place for reuse), both
witnesses' true optima resolve to **clean closed forms**, both **exactly**
verified:

- **Witness 1** (`A=(4265,2536,1747,1014,438)/10000`): the winning response
  splits `p_1` into two pieces landing at *even* sorted ranks (any split
  ratio `x∈(0.40539,0.40961)` works — this coordinate is a genuine flat
  direction, `oddrank` is provably constant on it, confirmed by testing
  three different values of `x` in that window and getting the identical
  exact value `5009/10000`), leaves `p_3` untouched, and splits `p_4` as
  `p_4 → (p_5, (p_4-p_5)/2, (p_4-p_5)/2)` — i.e. **one fragment tied exactly
  to the global minimum `p_5`, the residual `p_4-p_5` halved**. Exact value:
  $$\operatorname{oddrank}(B) = p_2+p_3+\tfrac{p_4+p_5}{2} = \tfrac{5009}{10000} = 0.5009 < \tfrac{16}{31}.$$
  Only 3 of the 4 marks are actually load-bearing (1 mark on `p_1` is
  needed only to push it off an odd rank, not to hit an exact target; the
  4th mark goes unused, matching Lemma TIE-NECESSARY's allowance for
  "fewer than budget" as a boundary case).
- **Witness 2** (`A=(3415,3023,1664,1404,494)/10000`): the winning response
  splits `p_1 → (p_5, (p_1-p_5)/2, (p_1-p_5)/2)` (the **same** "tie to
  global min, halve the residual" move, now applied to `p_1` instead of
  `p_4`) **and independently** splits `p_2 → (p_3, p_2-p_3)` (an ordinary
  Lemma PARTIAL-DOM tie of `p_2` down to `p_3`), leaving `p_4` untouched.
  Exact value:
  $$\operatorname{oddrank}(B) = \tfrac{p_1}{2}+p_3+p_4+\tfrac{p_5}{2} = \tfrac{2009}{4000} = 0.50225 < \tfrac{16}{31}.$$
  Again only 3 of 4 marks are load-bearing.

**This directly overturns the round-7 explorer's specific diagnosis on
these two witnesses.** What looked numerically like "irrational,
non-tie, non-half, jointly-tuned 3-piece coordination" (because a
gradient-free global optimizer converges slowly near a flat direction and
near-zero fragments) is, exactly, the **disjoint composition of two
already-essentially-certified moves**: (i) a new 2-mark composite —
call it **Lemma TIE-MIN-HALVE** — "tie one fragment of `p_i` to the global
minimum `p_m`, halve the residual `p_i-p_m`", applied to *one* piece, and
(ii) an ordinary already-certified Lemma PARTIAL-DOM tie applied to a
*different, disjoint* piece (Witness 2 only; Witness 1 needs no second
move at all). The "3 pieces touched" the explorer counted
(`p_1,p_3,p_4` for W1; `p_1,p_2,p_4` for W2) is real, but the touching is
**not jointly interacting** — each touched piece's fragments land at
ranks determined entirely by that piece's own local move, independent of
the other move, so the total value is simply the untouched pieces plus the
sum of each move's own (already-understood) local effect. There is no
genuine 3-way simultaneous ratio-tuning; the appearance of one was an
optimizer-precision artifact (the flat direction on `p_1`'s split in W1,
and a fragment converging to exactly `0` — a wasted mark — in both cases,
both of which a gradient-free numeric search approaches slowly without
ever landing exactly on).

### Lemma TIE-MIN-HALVE — proposed, NOT yet certified this round

**Proposed statement.** Let `A=(p_1≥...≥p_m)` sorted, `p_m>0` the global
minimum, and `i<m` with `p_i>p_m`. Suppose `r:=(p_i-p_m)/2` satisfies
`p_{i-1} ≥ r ≥ p_{i+1}` (reading `p_0:=+∞`, and `p_{i+1}` as whatever piece
is immediately after `p_i$ in the sorted list with `p_i` removed). Using 2
marks, split `p_i \to (r,r,p_m)` (three fragments: two copies of `r`, one
copy tied exactly to the value `p_m`). Then the two copies of `r` land at
the two consecutive ranks `p_i` used to occupy (one odd, one even — a
HALVE-style pair, contributing `r` once), and the new `p_m`-valued fragment
lands adjacent to the *existing* `p_m` entry at the bottom of the sorted
list (a DOM/PARTIAL-DOM-style exact tie, contributing `p_m` once between
the pair). Consequently
$$\operatorname{oddrank}(B) = \operatorname{oddrank}(A) - p_i + r + p_m = \operatorname{oddrank}(A) - \tfrac{p_i+p_m}{2}.$$

**Status of this lemma: proof sketch only, not certified.** The two
half-copies landing at *exactly* the two consecutive ranks `p_i` vacated,
and the new fragment tying cleanly at the bottom with no other piece
between it and the original `p_m`, both need the same kind of careful
rank-shift bookkeeping that Lemma DOM/HALVE/SANDWICH/PARTIAL-DOM's proofs
already carry out — I have **verified the formula exactly on the two
witnesses above** (both matched to the digit, `Fraction` arithmetic) but
have **not** written the general rank-shift proof this round, and have not
checked whether the stated hypothesis (`p_{i-1}≥r≥p_{i+1}`) is the weakest
correct one or whether edge cases (e.g. `i=m-1`, or `r` exactly equal to a
neighbor) need separate handling. This is honestly flagged as open, exactly
in the spirit of how Lemma SANDWICH was first found numerically (round 6)
and only proved rigorously afterward — the same should happen to this
lemma next round, ideally by whichever approach owns the menu
(`universal-adversary-strategy`) since it is a direct, mechanical
generalization of PARTIAL-DOM-RESIDUAL with target `p_m` instead of an
adjacent piece.

**Cross-check against Lemma SANDWICH (per the outliner's specific
request).** `m=5` is odd, so SANDWICH's hypothesis `p_1<p_2+p_m` was
checked on both witnesses exactly:
- Witness 1: `p_1=0.4265`, `p_2+p_5=0.2536+0.0438=0.2974`. `0.4265>0.2974`
  — **hypothesis fails**, SANDWICH does not apply at all.
- Witness 2: `p_1=0.3415`, `p_2+p_5=0.3023+0.0494=0.3517`. `0.3415<0.3517`
  — **hypothesis holds**, but applying SANDWICH alone (1 mark) gives
  `oddrank(B)=oddrank(A)-(p_1-p_2) = (p_1+p_3+p_5) - (p_1-p_2)
  = p_2+p_3+p_5 = 0.5181` exactly (`Fraction`-verified) — **`0.5181>c(4)`,
  so SANDWICH alone is insufficient here even though its hypothesis holds**,
  confirming the menu-coverage gap is real at `m=5` and SANDWICH alone
  cannot close it; the extra leverage came from spending the second mark on
  the residual, which is exactly Lemma TIE-MIN-HALVE (or, in retrospect,
  this witness's actual winning move used TIE-MIN-HALVE on `p_1` — with the
  *minimum* `p_5` as target, not `p_2` — plus a wholly separate PARTIAL-DOM
  move on `p_2`, not SANDWICH at all).

### Honest assessment: does this converge to `universal-adversary-strategy`'s argument?

**Yes, explicitly, and this should be said plainly rather than dressed up
as independent progress.** The exact winning constructions found by this
gate check are compositions of (a) an ordinary already-certified Lemma
PARTIAL-DOM application and (b) a mechanical generalization of the
PARTIAL-DOM-RESIDUAL composite (tie-then-halve-the-residual) that
`universal-adversary-strategy`'s own Step 1 is certifying this round —
merely with the tie target widened from "an adjacent piece" to "the global
minimum `p_m`". Searching for a genuine LP/minimax **duality certificate**
— an object that proves the bound *without* identifying which specific
tie-structure wins for each `A` — did **not** materialize from this gate
check: what I found instead is a *better, more explicit instance of the
same discrete search*, i.e. more evidence for, not an alternative to,
`universal-adversary-strategy`'s matching-induction target. Per this
round's explicit instruction: **this is the same argument, not an
independent one** — the value delivered is (i) a factual correction to
this round's explorer report (the "`m=5` needs genuinely growing
coordination degree" claim is not established; both witnesses decompose
into disjoint single/composite moves, no evidence of true multi-piece
joint-ratio tuning), and (ii) one new candidate composite move
(TIE-MIN-HALVE) for that approach's menu — not a new proof technique for
the retargeted theorem itself.

**What remains genuinely open for the mixed-strategy/duality framing.** No
closed-form, `A`-independent (or simply-parametrized, non-casework) dual
certificate was found or is evidenced to exist by this round's check —
if anything, the evidence points the other way: the winning move at each
witness is a *different* explicit combinatorial choice (which piece plays
the role of `i` in TIE-MIN-HALVE, whether a second disjoint move is needed),
selected by inequalities on `A`, which is precisely case analysis dressed
in different notation. Consistent with round 6's finding and now confirmed
on strictly harder witnesses: **the "mixed strategy" / duality proof
*shape* has not produced a shortcut around exact-minimizer casework in two
rounds of honest attempts.** Future rounds attempting this approach should
either (a) find a genuinely different dual object (e.g. one that bounds
`min_τ V(τ,A)` via a Positivstellensatz-style certificate valid on the
*whole* simplex without case-splitting on `A` — attempted informally this
round via the Farkas-certificate idea in the scratch scripts, but no such
global certificate was found for even the two witnesses' local cells), or
(b) be honestly retired/merged into `universal-adversary-strategy` as a
"contributes constructions, not a separate proof shape" role, per the
CLAUDE.md diversity rule, if a third round also fails to find independent
leverage.

## Full proof
(Not present — Status is `partial`. Round 7's gate check produced two
exact, `Fraction`-verified constructions closing both of this round's hard
`m=5` witnesses (`0.5009<16/31` and `0.50225<16/31`), correcting the
round-7 explorer's "growing coordination degree" diagnosis and yielding one
new candidate lemma (TIE-MIN-HALVE, proof sketched, not certified) — but,
honestly assessed per this round's explicit instruction, this **is** the
same underlying matching/casework argument `universal-adversary-strategy`
is pursuing, not an independent duality-certificate proof of the retargeted
theorem. No `A`-independent certificate was found. The general
arbitrary-configuration upper bound therefore remains open, and the
lower-bound side is still untouched by this approach.)

## Round 9 outliner note: recommend retirement

Per this file's own round-7 self-diagnosis (option (b) above) and
CLAUDE.md's diversity rule: this approach has produced **no independent
proof leverage for two consecutive rounds** (6 and 7) and was not revived
in round 8 (no build occurred; `current.md`'s round-8 record confirms no
new content). None of this round's three scouting reports (crosstie, ptbi,
altframing) surfaced a genuinely new dual object for it either. Recommend
the outline-reviewer **formally retire this slug from the active build
set** (not delete the file — its two certified contributions, Lemma
SANDWICH in `lemmas/sandwich-split.md` and the witness-value
cross-checks, remain in the shared lemma cache and stay available to
`universal-adversary-strategy`). If a future round finds a genuinely new
`A`-independent duality/certificate object (not a restatement of
`universal-adversary-strategy`'s casework), this slug can be revived by
the outliner at that time; until then it should not consume a build-set
slot each round.
