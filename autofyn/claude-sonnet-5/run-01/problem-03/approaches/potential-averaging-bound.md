## Status
partial

## Approaches tried
- `potential-averaging-bound` (this round, first build). Per the outline
  reviewer's mandatory feasibility gate, I did **not** write an inductive
  proof first. I first formalized the two "cascading" candidate strategies
  precisely enough to be computed and checked whether
  `(cascading-DOM value + cascading-HALVE value)/2 ≤ c(n)·Σ(A)` actually
  holds, on the same class of configurations (including the near-tied-top-two
  region) that the round-5 explorer flagged. Result: **the gate fails.** The
  averaging bound is violated by several concrete, valid Liu Bang
  configurations under every reasonably natural definition of "cascading
  DOM"/"cascading HALVE" I could construct, including a clean exact-fraction
  counterexample (below) that needs no numerical approximation. I traced the
  failure to a structural reason (not a definitional accident): any
  candidate strategy that is required to be *always well-defined and
  concretely computable without further casework* is forced to make a
  context-blind decision about how much of its budget to spend, and the true
  optimal Xiang-Yu strategy sometimes needs to spend *less* than its full
  budget, or spend it on a different piece than either DOM or HALVE points
  to, precisely to avoid the harm that greedy full-budget cascading causes.
  Reported honestly below as a negative result on the averaging *shape* of
  proof for this problem, not a rejection of the crux move's syntax
  (`min(A,B) ≤ (A+B)/2`) — that inequality is of course true; what fails is
  the premise that two *simply defined, always-available* candidates can be
  chosen with average already meeting the bound.

## Current best

### Setup (imported, certified)

By Lemma 1 (claiming-phase value formula, `lemmas/claiming-phase-value.md`),
the whole problem reduces to
```
c(n) = max_A min_B oddrank(B),
```
where `A` ranges over Liu-Bang configurations (multisets of ≤ n+1 positive
reals summing to 1, obtainable with ≤ n marks) and `B` ranges over Xiang-Yu's
refinements of `A` using ≤ n further marks, and `oddrank(S)` is the sum of
the odd-ranked elements of `S` sorted descending. This approach targets the
**upper-bound half**: for every `A` (arbitrary, not necessarily geometric)
and every `n`, Xiang Yu has an explicit strategy forcing
`oddrank(B) ≤ c(n)·Σ(A)` where `c(n) = 2^n/(2^{n+1}-1)` is the conjectured
value.

I import, without re-proof, the two certified identities from
`lemmas/generalized-domination-and-halving.md`:

- **Lemma DOM.** If `A = (p_1 ≥ ⋯ ≥ p_m)`, tail `T = (p_2,...,p_m)`,
  `S = Σ(T)`, and `p_1 ≥ S`, then using exactly `k = m-1` marks Xiang Yu can
  force `oddrank(B) = p_1` exactly (split `p_1` to structurally match `T`).
- **Lemma HALVE.** If `p_1 ≥ 2p_2`, then using 1 mark (split `p_1` into two
  equal halves) Xiang Yu forces `oddrank(B) = p_1/2 + oddrank(T')` for any
  further refinement `T'` of the tail `T = (p_2,...,p_m)`.

### Step 1 — formalizing the two "cascading" candidates

Both lemmas above are **flat**: each applies once, at the top, and only
under a hypothesis (`p_1 ≥ S`, resp. `p_1 ≥ 2p_2`) that need not hold. The
outline's Step 4 caution already flags that the naive flat pair fails
exactly when neither hypothesis holds. To test the corrected/recursive
version demanded by the falsifiability gate, I built the most natural
recursive extensions of each:

**Candidate 1 — `cascade-DOM(A, budget)`** (DOM-priority cascade, uses full
budget greedily top-down): at the current level with top piece `p_1`, rest
`T`, `S = Σ(T)`, `k = |T|`:
- if `budget ≥ k` and `p_1 ≥ S`: apply Lemma DOM (terminates, contributes
  `p_1` to `oddrank`);
- else if `budget ≥ 1` and `p_1 ≥ 2·(\max T)`: apply Lemma HALVE (spend 1
  mark, contribute `p_1/2` plus recurse on `T` with `budget - 1`);
- else: **leave `p_1` untouched** and recurse into `T`.

The third branch requires care: because refining `T` only shrinks its
elements, `p_1` (already ≥ everything in `T`) remains the unique rank-1
element of the merged list `B`. Every element of the refined tail `T'`
therefore has its *internal* rank shifted by exactly `+1` in `B`. An
internal-odd-rank element of `T'` becomes an even-rank (excluded) element of
`B`, and an internal-even-rank element becomes odd-rank (included). Hence
```
oddrank(B) = p_1 + evenrank(T'),
```
**not** `p_1 + oddrank(T')`. So the recursion, when it falls through to the
third branch, must switch to a genuinely different, *dual* sub-problem:
minimizing `evenrank` of the tail via marks, not `oddrank`. I define the
mirrored recursion `evenmin-cascade(T, budget)` by the same two branches with
the target swapped: applying (the DOM identity for the sub-list forces
`oddrank(T)=p_1'`, hence `evenrank(T) = S(rest of T)`) or (Lemma HALVE
similarly, mirrored), else fall through with no marks spent
(`evenrank(T)` as-is). This asymmetry between "minimize oddrank" and
"minimize evenrank" mode, triggered every time a candidate cascades past an
untouched top piece, is a structural fact of this problem not previously
recorded in this approach's lemma set; it is the reason a *literal* recursive
analogue of DOM/HALVE cannot simply "recurse with the same objective."

**Candidate 2 — `cascade-HALVE(A, budget)`**: same two branches, tried in
the opposite priority order (HALVE first, then DOM), else falls through to
the same `evenmin-cascade` dual.

**Candidate 3 (added during testing) — `always-halve(A, budget)`**: at every
step, split the *current* largest remaining piece into two equal halves
(regardless of whether it dominates the second-largest by a factor of 2),
re-sort, and recurse with `budget - 1`, until `budget = 0`; the resulting
value is computed directly from the definition of `oddrank`, not via Lemma
HALVE's identity (which needs the `p_1 ≥ 2p_2` hypothesis to hold). This
candidate is always well-defined (it needs no case hypothesis at all) and
was added specifically to probe whether a "hypothesis-free" candidate could
rescue the averaging bound.

All three candidates are concretely computable, always-available (need no
case hypothesis to be *defined*, only to short-circuit early), and legally
achievable by Xiang Yu (every step is a legitimate mark placement).

### Step 2 — the falsifiability test (exact-fraction counterexample)

Test on `A = (1/3, 1/3, 1/3)`, `n = 2` (a valid Liu-Bang configuration: 3
pieces from ≤ 2 marks). Here `c(2) = 4/7`, so the target bound is
`c(2)·Σ(A) = 4/7 ≈ 0.5714`.

- **`always-halve`, budget 2.** Round 1: current max is `1/3` (any copy);
  halve it: `1/6, 1/6`; sorted list is now `(1/3, 1/3, 1/6, 1/6)`, with
  `oddrank = 1/3 + 1/6 = 1/2`. Round 2 (budget still `1`): current max is
  `1/3`; halve it: `1/6, 1/6`; sorted list is `(1/3, 1/6, 1/6, 1/6, 1/6)`,
  with `oddrank = 1/3 + 1/6 + 1/6 = 2/3`. So `always-halve(A, 2) = 2/3`.
- **`cascade-DOM(A, 2)`.** Level 0: `p_1 = 1/3`, `T = (1/3,1/3)`, `S = 2/3`,
  `k = 2`. DOM hypothesis `p_1 ≥ S` fails (`1/3 < 2/3`). HALVE hypothesis
  `p_1 ≥ 2\max T = 2/3` fails (`1/3 < 2/3`). Fall through: `p_1` untouched,
  recurse `evenmin-cascade((1/3,1/3), 2)`. Level 1: `p_1' = 1/3`,
  `T' = (1/3)`, `S' = 1/3`, `k' = 1`. DOM-boundary hypothesis
  `p_1' ≥ S'` holds (equality), so `evenrank = S' = 1/3`. Total:
  `cascade-DOM(A,2) = 1/3 + 1/3 = 2/3`.
- **`cascade-HALVE(A,2)`**: identical computation (neither hypothesis fires
  differently with priority swapped here), also `= 2/3`.

So every pairwise average among `{2/3, 2/3, 2/3}` is `2/3`, and
```
2/3 > 4/7  (since 2/3 = 14/21 > 12/21 = 4/7),
```
**violating** the target averaging inequality
`(candidate_1 + candidate_2)/2 ≤ c(n)·Σ(A)` for every pair of the three
constructed candidates. This is an exact computation (fractions throughout),
not a numerical artifact.

Crucially, this is **not** evidence that the true optimum fails the theorem:
using only **one** mark (not the full budget of 2), split a single `1/3`
into two `1/6`'s and stop: `(1/3, 1/3, 1/6, 1/6)` has `oddrank = 1/2 < 4/7`,
comfortably meeting the bound with slack to spare, and with an unused mark.
The true `min_B oddrank(B)` for this `A` at `n=2` is therefore `≤ 1/2 < 4/7`,
consistent with the (still only partially proven) full theorem. **The
counterexample is entirely a failure of the constructed *candidates*, which
were forced by their own definition to spend their full budget greedily,
not a failure of the bound `c(n)Σ(A)` itself.**

I additionally tested (numerically, `Fraction`/`float`, see build-session
scratch computation) several further configurations for `n = 2, 3`,
including the near-tied-top-two configuration `(0.45, 0.44, 0.11)` flagged
by the round-5 explorer and the DOM-boundary configuration
`(0.6, 0.2, 0.15, 0.05)`. Findings:
- On some configurations (the geometric extremal family, and the near-tied
  example) the average of two of the candidates does clear the bound.
- On several others (the flat/near-equal configuration above, and a
  DOM-boundary configuration at `n=3`) **every pairwise average among the
  three candidates fails**, and in the flat case even the **minimum** of all
  three candidates exceeds the bound (`min(2/3,2/3,2/3) = 2/3 > 4/7`) — i.e.
  none of the three constructed strategies individually meets the bound
  either, let alone their average.

### Step 3 — diagnosis: why this is a structural obstruction, not a fixable definition

The failure traces to a single root cause common to all three candidates:
each is a **greedy, budget-blind** rule — it always tries to spend a mark
(via DOM or HALVE) whenever the local hypothesis allows, and otherwise
spends nothing on the current piece but recurses without ever considering
*stopping early with an unused mark*. The exact-fraction example shows the
true optimal strategy for `(1/3,1/3,1/3)` at budget 2 **must leave one mark
unused** — using the second mark (on the natural greedy target, another
`1/3`) makes the outcome strictly *worse* (`2/3` vs. `1/2`). This is exactly
the phenomenon `universal-adversary-strategy`'s own round-5 explorer
independently found ("budget is sometimes left unused... the optimal move
skips straight past `p_1,p_2`"): the *decision of how much budget to commit
and where* is itself an optimization that cannot be made by a fixed,
context-free rule of the "always fire DOM, else HALVE, else recurse" form.

For the averaging technique specifically, this is fatal in the following
precise sense: the crux move `min(strategy_1, strategy_2) ≤ average` is
correct as an inequality, but it only transfers a bound on the *average* of
the two named strategies into a bound on Xiang Yu's true minimum. If **both**
named candidates are individually forced (by being simply/context-freely
defined) to sometimes overspend their budget and land above the target
bound — as the exact-fraction example shows happens **simultaneously** for
all three natural candidates tried here — then no linear combination of
their values can be `≤` the bound either, since averaging non-negative
excesses cannot produce a non-positive excess. **The only way to repair this
within the averaging framework is to build a candidate that already encodes
the "sometimes stop early / spend less than the full budget" decision** —
but that decision (which piece to act on, and whether to stop) is precisely
the case-by-case optimization that `universal-adversary-strategy`'s cascade
induction is undertaking directly, and that this approach was explicitly
tasked (Step 4 of the outline, and the outline-reviewer's directive) with
avoiding. Constructing such a "budget-aware" candidate is therefore not a
shortcut around the case analysis; it *is* the case analysis, dressed up as
a second named strategy.

### Conclusion of the feasibility probe

Per the outline reviewer's explicit instruction ("If it fails anywhere, do
not force a proof — report the counterexample and either construct the
needed third candidate strategy explicitly ... or report this framing as a
documented negative result. Do not silently fall back to exact-minimizer
casework"), I report this as a **documented negative result**, not a forced
proof:

- The naive flat DOM/HALVE average was already known (round 5 explorer) to
  fail.
- The natural recursive/cascading repairs (three distinct candidates tried,
  including a hypothesis-free "always halve current max" rule) **also
  fail**, on an exact-fraction, easily verifiable example, and in a way that
  is not an artifact of a poor choice of candidate but a structural
  consequence of every context-free/greedy candidate being unable to
  represent "stop early, leave budget unused."
- A genuine fix requires a *budget-aware* candidate strategy whose
  definition already resolves the same optimal-stopping/optimal-target
  decisions that the direct casework approach (`universal-adversary-
  strategy`) is built to make; building such a candidate here would collapse
  this approach into a duplicate of that one, which the outline explicitly
  warned against.

This approach therefore does **not** currently provide a working alternative
proof shape for the upper bound. It remains genuinely different in
technique from `universal-adversary-strategy` (which is why it was kept in
the population), but the specific mechanism proposed (averaging two simply
defined cascading candidates) is now falsified with a clean, exact
counterexample, not merely "not yet verified."

## Full proof
(Not present — Status is `partial`. No proof of the theorem is claimed by
this approach. The material above is a completed, honest feasibility
analysis: the averaging *shape* of argument, as concretely instantiated with
the candidates the outline proposed, is shown to fail by an exact
counterexample, and the reason is shown to be structural rather than a
fixable technicality — this is a negative result, recorded so future rounds
do not re-attempt the same "cascading-DOM/cascading-HALVE, budget-greedy"
candidate pair.)

## Round 6 note: recommend retirement

Per round 5's own flag ("if a further attempt at a budget-aware third
candidate also collapses into duplicating `universal-adversary-strategy`,
retire as duplicative"): no budget-aware third candidate was attempted this
round, and this approach's diagnosed fix (a candidate whose definition
already resolves the optimal-stopping decisions `universal-adversary-
strategy` makes by direct casework) is structurally the same content that
approach is now proving directly as Lemma TIE-NECESSARY / Lemma PARTIAL-DOM
(round 6). This approach's unique diversity role — a genuinely different
*proof shape* for the upper bound, not exact-minimizer casework — is now
better filled by the new `minimax-mixed-duality` approach opened this
round, which is an actual expectation/probabilistic argument (not 2-3
fixed deterministic candidates) and directly targets the failure mode
diagnosed here (too few, too rigid candidates). Recommend the
outline-reviewer retire this approach (RETHINK, not further build slots)
unless it proposes a genuinely new, non-duplicative averaging mechanism
this round — not attempted, since the outliner judges the minimax approach
already supersedes it.

## Promotable lemmas

**Dual-objective shift under an untouched dominant element.** *Statement:*
if `B = {p_1} ∪ T'` where `p_1 ≥` every element of `T'` (so `p_1` occupies
rank 1 of `B`), then `oddrank(B) = p_1 + evenrank(T')`. *Proof:* every
internal rank `i` of `T'` becomes global rank `i+1` in `B`; odd global rank
`⟺` even internal rank; summing the included (odd-global) terms plus `p_1`
itself gives the stated identity. This is a short, fully general, reusable
fact (needs no geometric or DOM/HALVE structure) that is likely useful to
any approach that recurses on "leave the top piece untouched" — recorded
here in full but not yet split into its own `lemmas/` file since no other
approach currently imports it; the reviewer may promote it if a future
approach needs the oddrank/evenrank duality under an untouched maximum.
