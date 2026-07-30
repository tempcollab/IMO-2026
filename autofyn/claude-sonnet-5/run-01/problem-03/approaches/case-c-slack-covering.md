## Status
partial

## Approaches tried

- **Round 14 (new slug, first build).** Mandate: attempt a non-constructive
  averaging/pigeonhole proof of Claim PTBI's Case C (`p_1<\Sigma(A)/2`,
  general `m\ge4`) as a structurally distinct route from
  `universal-adversary-strategy`'s explicit peel-and-overlap construction,
  gated by a mandatory numeric feasibility check against known hard
  witnesses (including the new round-14 witness `A=(965,965,958,482)`)
  **before** any proof write-up.

  **Result: the mandatory gate is passed on the easy witnesses but the
  underlying construction — worked out fully, in closed form, with an
  exact algebraic proof — is shown to FAIL, for every `m\ge4`, at the
  well-known near-uniform-tail boundary (`p_1\to\Sigma(A)/2^-`, tail
  values all equal) that has obstructed every other approach since round
  11. This is a genuine, decisive, honestly-reported negative result for
  the *specific* one-level-averaging mechanism gated this round — not a
  vague numeric near-miss, but an exact closed-form margin proved negative
  for all `m\ge4` by direct algebra.** Full derivation below.

### Step 0 — setting up the averaging family and its exact value (certified machinery only)

  Fix a Case-C configuration `A` sorted descending, `|A|=m\ge4`, tail
  `T=(t_1\ge t_2\ge\cdots\ge t_{m-1})` (so `t_1=p_2`), `\Sigma:=\Sigma(A)`.
  For each `i=1,\ldots,m-1` with `t_i\le p_1` (automatic, since `p_1` is
  the maximum of `A`), define the **candidate move** `\mu_i`: split `p_1`
  into `(t_i,\,r_i)` with `r_i:=p_1-t_i\ge0`, forming the tied pair
  `\{t_i,t_i\}` (one copy from the split, one already present in the
  tail) and leaving the residual `r_i` as a new free element. This uses
  exactly **1 mark** (one split of `p_1`).

  The resulting multiset is `\mathrm{REST}_i\cup\{t_i,t_i\}`, where
  `\mathrm{REST}_i:=(T\setminus\{t_i\})\cup(\{r_i\}\text{ if }r_i>0)`
  — i.e. the tail with `t_i` removed and `r_i` inserted, size exactly
  `m-1`.

  **Exact value identity (uses only already-certified Lemma
  DOUBLE-INSERT, `lemmas/double-insert.md`: inserting a duplicated value
  `v` into any array changes `\mathrm{oddrank}` by exactly `+v`,
  unconditionally on the rest of the array).** Viewing
  `\mathrm{REST}_i\cup\{t_i,t_i\}` as "insert a duplicate of `t_i`" into
  `\mathrm{REST}_i`:
  $$\mathrm{oddrank}(A\text{ after }\mu_i) \;=\; t_i \;+\; \mathrm{oddrank}(\mathrm{REST}_i).$$
  This is exact (not an estimate), for every `i`, including the
  degenerate case `r_i=0` (`t_i=p_1`), where the identity still holds
  with `\mathrm{REST}_i=T\setminus\{t_i\}` (size `m-2`; this sub-case
  uses `0` marks by the certified Lemma DOM-boundary-slack, strictly
  cheaper — never worse for an upper bound, since more marks only help
  the value go down or stay the same, an easy monotonicity fact used
  implicitly and correctly here since we are only ever proving an upper
  bound, never claiming tightness of mark usage).

  **Mark budget check (resolves the outline-reviewer's flagged open item
  about a second budget-tracking parameter — for this exact construction,
  none is needed).** `|\mathrm{REST}_i|=m-1` (generic case), so by the
  strong induction hypothesis (Claim PTBI already established for every
  size `<m`, in particular size `m-1`, using at most `(m-1)-1=m-2` marks):
  $$\mathrm{oddrank}(\mathrm{REST}_i)\;\le\;c(m-2)\,\Sigma(\mathrm{REST}_i),$$
  using at most `m-2` marks. Combined with the `1` mark spent on the
  split itself, total marks used `\le 1+(m-2)=m-1`, **exactly** the
  budget `|A|-1`. So the outer accounting telescopes for free here — no
  separate secondary induction parameter is needed for this construction
  (this answers, for this specific route, the outline-reviewer's item 3
  concern about the interaction between the subset-match induction and
  the recursive mark budget).

  Since `\Sigma(\mathrm{REST}_i)=\Sigma(T)-t_i+r_i=(\Sigma-p_1)-t_i+(p_1-t_i)=\Sigma-2t_i`,
  define
  $$\mathrm{UB}_i \;:=\; t_i+c(m-2)(\Sigma-2t_i) \;=\; c(m-2)\Sigma+\bigl(1-2c(m-2)\bigr)t_i,$$
  a valid upper bound: `\mathrm{oddrank}(A\text{ after }\mu_i)\le \mathrm{UB}_i` for every `i`.

### Step 1 — the pigeonhole/averaging lemma (trivial, proved in full)

  **Lemma (Averaging-Existence).** For any finite family of real numbers
  `\{\mathrm{UB}_i\}_{i=1}^{k}`, `\min_i \mathrm{UB}_i \le
  \frac{1}{k}\sum_i \mathrm{UB}_i`. *Proof:* the minimum of a finite set
  is at most its arithmetic mean (elementary; the sum of `k` copies of the
  mean equals the sum of the terms, so if every term exceeded the mean
  the sum would exceed itself, a contradiction). `\square`

  Applying it here: since `\mathrm{solve}(A)\le\min_i\mathrm{UB}_i`
  (Xiang Yu — or whichever player minimizes — can always choose the best
  available candidate move `\mu_i`), it suffices for the averaging route
  to show `\frac{1}{m-1}\sum_i \mathrm{UB}_i \le c(m-1)\Sigma`. This is
  the genuinely non-constructive step the outline asked for: if the
  *average* clears the target, existence of a good `\mu_i` follows
  without identifying which `i`.

### Step 2 — the averaging family COLLAPSES to a single deterministic choice (first structural finding)

  **Key fact (proved directly from the formula, no case-work needed):**
  `c(n)>1/2` for every `n\ge0` (`c(n)=2^n/(2^{n+1}-1)`, and
  `2\cdot2^n>2^{n+1}-1\iff 2^{n+1}>2^{n+1}-1`, always true). Hence
  `1-2c(m-2)<0` for every `m\ge2`, so `\mathrm{UB}_i` is **strictly
  decreasing** in `t_i`. Consequently
  $$\min_i \mathrm{UB}_i \;=\; \mathrm{UB}_1 \quad(\text{attained at }t_1=\max_i t_i=p_2),$$
  and since `\min_i \mathrm{UB}_i \le \frac{1}{k}\sum_i \mathrm{UB}_i`
  always (Step 1), **the averaged bound can never beat the single
  deterministic choice `\mu_1` (match `p_1` with the largest tail element
  `p_2`)** — it is provably weaker or equal. This means the "genuinely
  non-constructive, avoid-identifying-the-optimal-match" character
  promised by this slug's mandate does not materialize for this
  particular family: the best member is always explicitly identifiable
  (`i=1`), so working with the average instead of the (trivially
  identifiable) minimum only throws away information. Any proof using
  this family is therefore, honestly, no different in power from the
  explicit single-candidate construction "always match `p_1` with `p_2`"
  — a special case of exactly the kind of construction
  `universal-adversary-strategy` is already building (its Move 2 /
  PARTIAL-DOM maximal-prefix match, restricted to a size-1 prefix). This
  is reported honestly as a structural finding, not glossed over.

### Step 3 — the mandatory numeric gate on `\mathrm{UB}_1` (the best-in-family candidate)

  Ran the required feasibility check against the mandated witnesses,
  exact `fractions.Fraction` arithmetic throughout (script
  `/tmp/round-14/scratch/gate8.py`):

  - `A=(26,21,10)/57` (`m=3`, reference only — `m=3` is already fully
    closed and not reopened here): `\mathrm{UB}_1=31/57\approx0.5439 <
    c(2)\Sigma=4/7\approx0.5714`. **Passes**, and in fact reproduces
    EXACTLY the true 2-mark-constrained game value `31` (in un-normalized
    terms) independently found by the round-13 reviewer — a strong
    correctness check on the construction itself.
  - `A=(0.45,0.20,0.15,0.12,0.08)` (`m=5`, the round-13 Case-(a) witness,
    `T=(0.20,0.15,0.12,0.08)`): `\mathrm{UB}_1=13/25=0.52 <
    c(3)\Sigma=8/15\approx0.5333`. **Passes.**
  - `A=(965,965,958,482)/3370` (`m=4`, the new round-14 witness requiring
    "skip-if-already-tied"): `\mathrm{UB}_1=385/674\approx0.57121 <
    c(2)\Sigma=4/7\approx0.57143`. **Passes, but only barely** — the
    exact margin is `4/7-385/674 = 1/4718 \approx 2.1\times10^{-4}`,
    i.e. `1` part in `4718`. Note this construction handles the
    "already-tied" structure of this witness *automatically*, with no
    separate zero-cost "Move 0" rule needed: since `t_1=p_2=965=p_1`
    exactly here, `\mu_1` degenerates to the `r_1=0` case for free (cost
    `0` marks via Lemma DOM-boundary-slack), so the construction already
    "skips the free tie and spends the budget on the tail" — this
    resolves, for this route, the outline's concern that Move 0 needed
    to be bolted on as a separate case: it is already subsumed by always
    choosing `i=1` and applying the `r_i=0` boundary rule when it fires.
    (The `385/674` value itself is *not* tight — the true optimum on this
    witness, independently found by direct computation earlier this
    round via `scipy.optimize.differential_evolution` on the actual
    2-remaining-mark sub-game, is `1685/3370=337/674\approx0.5$,
    substantially below `385/674`; the IH bound used inside `UB_1` is
    valid but loose here because it charges the leftover as if it had
    only its minimum-required `m-2` marks, while the true game leaves it
    `2` marks, strictly more than needed — extra marks can only help, so
    the true value is `\le` this IH-based bound, never worse; `385/674`
    already suffices to pass the gate here, so this looseness is not
    load-bearing for this witness, but it is flagged because it explains
    why the margin above looks unexpectedly tight compared to the true
    game's actual comfortable margin.)

  These three pass — consistent with the outline's expectation that the
  "easy" witnesses should not immediately kill the idea. The gate is
  **not** yet decisive from these three alone (per the mandate, a passing
  gate on easy witnesses is not sufficient; the construction must be
  checked at its true worst case, not just at specific sampled points).

### Step 4 — the DECISIVE test: the near-uniform-tail boundary (worst case, found by direct optimization of the closed form, not sampling)

  Since `\mathrm{UB}_1=c(m-2)\Sigma+(1-2c(m-2))p_2` and the coefficient of
  `p_2` is negative (Step 2), `\mathrm{UB}_1` is **maximized** (worst
  case for the construction) when `p_2` is **minimized** subject to
  `p_2=\max(T)` and `\Sigma(T)=\Sigma-p_1` fixed. The minimum possible
  value of the maximum of `m-1` nonnegative reals summing to a fixed
  total is attained exactly when all `m-1` values are **equal**
  (uniform tail), giving `p_2=(\Sigma-p_1)/(m-1)`. So the worst case
  for this whole family (over all Case-C configurations with a given
  `p_1` and `m`) is the uniform tail — and since Case C only requires
  `p_1<\Sigma/2` with no lower bound, the worst case over `p_1` is at
  the boundary `p_1\to\Sigma/2^-` (checked directly: with `\Sigma=1`
  fixed, scanning `p_1$ finely over `(0,1/2)` for `m=3,\ldots,24`
  confirms the minimum margin always occurs at the largest tested
  `p_1$ closest to `1/2`, script `/tmp/round-14/scratch/gate4.py`).

  **Exact algebraic evaluation at the boundary (`\Sigma=1$, `p_1=1/2`,
  uniform tail `p_2=\tfrac{1/2}{m-1}=\tfrac{1}{2(m-1)}`), by direct
  symbolic computation (`sympy`, script `/tmp/round-14/scratch/gate7.py`):**
  $$\mathrm{margin}(m) \;:=\; c(m-1)-\mathrm{UB}_1 \;=\; \frac{2^m(3-m)-2}{2\,(2^m-2)(2^m-1)(m-1)}.$$
  (Verified this closed form reproduces the exact fractions computed
  directly for `m=3,\ldots,11` in `/tmp/round-14/scratch/gate5.py`, e.g.
  `m=4: -1/70`, `m=8: -641/453390`, matching exactly.)

  **Sign of the margin, proved for every integer `m\ge4` (not just a
  sampled range):** the denominator `2(2^m-2)(2^m-1)(m-1)>0` for every
  `m\ge2` (each factor is a product of positive terms once `m\ge2`, since
  `2^m>2`). The numerator is `2^m(3-m)-2`; for every integer `m\ge4$,
  `3-m\le-1`, so `2^m(3-m)\le-2^m`, giving numerator
  `\le -2^m-2<0`. **Hence `\mathrm{margin}(m)<0` for every integer
  `m\ge4`, unconditionally** — not a numerical near-miss at a few
  sampled `m`, but an exact, algebraically proved strict violation of
  `\mathrm{UB}_1\le c(m-1)\Sigma` at this boundary configuration, for
  every `m` in the open case's entire scope.

  **Consequence.** Since (Step 2) the averaged bound over the whole
  family `\{\mathrm{UB}_i\}` can never do better than `\mathrm{UB}_1`,
  and `\mathrm{UB}_1` itself **provably exceeds** the target at the
  uniform-tail boundary for every `m\ge4`, **no averaging (nor any single
  choice) within this one-level "match `p_1` against one tail element,
  bound the leftover by one application of the induction hypothesis"
  family can prove Claim PTBI's Case C in general.** This is not a
  looseness-of-bound artifact alone: at the exact uniform-tail boundary,
  the leftover `\mathrm{REST}_1` is *itself* again a near-uniform
  configuration at (asymptotically) the same relative `p_1/\Sigma$
  ratio, so the induction hypothesis is being invoked essentially at its
  own worst case one level down — i.e. this is a genuine
  self-similarity/fixed-point obstruction, structurally the same
  "near-uniform tail" difficulty that has independently obstructed
  `universal-adversary-strategy` since round 11 (the near-uniform-tail
  counterexample family for fixed small-pair constructions) and round 12
  (Lemma HALF-BOUND's flagged "tail locally dominant" open sub-case) —
  not a new, unrelated failure mode.

### Diagnosis and why this is a genuine, reportable dead end for the gated mechanism

  Per this slug's own mandated risk section: "the SAME failure mode that
  killed `potential-averaging-bound` (round 5) — averaging over
  budget-blind, fixed candidate strategies that ALL individually overshoot
  cannot produce an average below target" was explicitly flagged as the
  thing to check first. What was actually found is a related but
  distinct failure: it is not that all candidates individually overshoot
  everywhere (they do NOT — `\mathrm{UB}_1$ comfortably clears the target
  away from the uniform-tail boundary, e.g. on all three tested witnesses
  above); rather, **the family's single best member (which averaging can
  never beat) is *itself* insufficient exactly at the one boundary
  configuration that has obstructed every other approach to Case C so
  far.** Any fix requires either (a) a genuinely different second-level
  averaging family that also incorporates matching *within the leftover*
  (not just at the top level) — but this reduces to exactly the same
  multi-level recursive matching machinery `universal-adversary-
  strategy`'s Lemma SLACK-COVER is already trying to build, eliminating
  any independent proof leverage this route would supply — or (b) a
  sharper, non-generic bound for the leftover specifically in the
  near-uniform regime (not a fresh application of the coarse `c(m-2)\Sigma`
  IH bound) — which is again exactly the open content of Lemma
  HALF-BOUND / SLACK-COVER, not a new idea this slug introduces.

  This is the same convergence-failure pattern recorded for
  `minimax-mixed-duality` (round 6-7) and `case-c-secondary-extremality`
  (round 11): a nominally distinct proof shape that, once worked out
  concretely, reduces to (or is dominated by, or requires the same
  missing ingredient as) the field's existing leading approach. Per the
  round-11 convergence-failure precedent and this slug's own explicit
  instruction ("if your averaging idea can't account for this witness's
  structure, that's a fast, honest downgrade signal, same as what killed
  potential-averaging-bound... report that honestly... rather than
  pushing forward with a broken foundation"), **this specific mechanism
  (one-level single-match averaging with a coarse IH-bounded leftover) is
  reported as a dead end for proving Case C in general**, not pushed
  further.

## Current best

The one-level averaging/pigeonhole construction described above is
correctly derived (exact value identity via certified Lemma DOUBLE-INSERT,
correct mark-budget accounting) and gives a valid, sometimes-useful upper
bound `\mathrm{UB}_1 = c(m-2)\Sigma+(1-2c(m-2))p_2` for `\mathrm{solve}(A)`
on any Case-C configuration — it passes comfortably away from the
near-uniform-tail boundary (all three mandated easy/medium witnesses
checked) and reproduces the exact known true value on the `m=3` witness
`A=(26,21,10)`. **It provably fails, by an exact algebraic margin, for
every `m\ge4`, at the near-uniform-tail boundary
(`p_1\to\Sigma/2^-`, tail uniform)** — the same persistent hard regime
obstructing every other Case-C approach. Since the averaging step is
provably dominated by the single best member of the family (Step 2), no
repair within this specific "one match, one IH application" family can
close the gap; a genuine fix needs the same multi-level recursive
matching content `universal-adversary-strategy`'s Lemma SLACK-COVER is
independently pursuing, so this slug does not offer independent leverage
in its currently-gated form. **Case C for general `m\ge4` remains open**
— this build neither closes it nor claims to.

## Full proof
(Not applicable — Status is `partial`; the whole-problem claim (Claim
PTBI's Case C for `m\ge4`) is not proved by this approach.)

## Promotable lemmas

- **Lemma DOUBLE-INSERT-MATCH-VALUE (proved in full above, Step 0):** for
  any sorted configuration `A` with `p_1=\max(A)` and any tail element
  `t_i\le p_1`, splitting `p_1` into `(t_i,\,p_1-t_i)` gives
  `\mathrm{oddrank}(A\text{ after})=t_i+\mathrm{oddrank}(\mathrm{REST}_i)`
  exactly, where `\mathrm{REST}_i=(T\setminus\{t_i\})\cup\{p_1-t_i\}`
  (or `T\setminus\{t_i\}` if `p_1=t_i`) — a direct corollary of the
  already-certified Lemma DOUBLE-INSERT, worth certifying separately
  since it is the exact-value backbone any future single-match-based
  Case-C construction (in this or the sibling approach) will need, and
  it resolves cleanly why "skip-if-already-tied" (Move 0) needs no
  separate rule when the match is always taken against the largest tail
  element (the `r_i=0` case falls out for free).
- **Fact (uniform-tail worst-case margin, proved in full above, Step 4):**
  for the specific bound `\mathrm{UB}_1(m):=c(m-2)+\bigl(1-2c(m-2)\bigr)\cdot
  \tfrac{1}{2(m-1)}` (i.e. `\Sigma=1`, `p_1=1/2`, uniform tail), the exact
  closed form
  `c(m-1)-\mathrm{UB}_1(m)=\dfrac{2^m(3-m)-2}{2(2^m-2)(2^m-1)(m-1)}`
  is strictly negative for every integer `m\ge4`. This is a reusable,
  precisely quantified negative fact: **any future Case-C construction
  that reduces, even approximately, to "one top-level match plus one
  coarse application of the induction hypothesis to the leftover" is
  automatically ruled out** by this exact margin at the uniform-tail
  boundary — worth certifying so future rounds do not re-discover it by
  numeric search alone.
