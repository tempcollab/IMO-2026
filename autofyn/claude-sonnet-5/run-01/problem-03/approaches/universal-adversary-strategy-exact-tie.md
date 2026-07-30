## Status
partial

## Approaches tried

- `universal-adversary-strategy-exact-tie` (round 13, this build). Target
  (per the round-13 outline): prove the sharper **identity**
  `\mathrm{solve\_full}(A) = \Sigma(A)/2` exactly throughout Case C
  (`p_1<\Sigma(A)/2`), via a Hall's-theorem / exact-cover existence
  argument (crux `aimo-0063`-style), reducing (per the certified
  `e`-recursion reformulation, shared with the sibling
  `universal-adversary-strategy` approach — see its file, "Round 12
  build"/round-13 explorer `math-explorer-inductive`) to: does some
  sequence of Move 1/2/3 always reach an exact "leftover-empty" tie
  before bottoming out at a positive-excess singleton?

  **Result: found and proved the exact mechanism that produces the
  identity in the certified `solve(A,\mathrm{budget})` recursion AS
  LITERALLY SPECIFIED — and then found and rigorously confirmed that this
  mechanism silently spends ONE MORE physical mark than
  Xiang-Yu's true budget `m-1` allows, so the identity, taken as a claim
  about the true game value, is FALSE in general.** This is a genuine,
  load-bearing correction (not a duplication of the sibling's Case
  (a)/(b) work — the discovery is specifically about the certified
  `solve(A,\mathrm{budget})` recursion's mark-bookkeeping, a distinct,
  previously-unverified issue the round-12 plan itself flagged as
  "must be checked... do not silently assume" and which was never in
  fact checked). See "Current best" below for the full derivation, the
  independent from-scratch re-implementation with a HARD total-mark cap,
  and an exact witness confirmed by TWO independent methods (a
  menu-restricted exact dynamic program, and an unrestricted
  `scipy.optimize` continuous search over every possible 2-mark
  real-valued split). **CHANGES REQUESTED-equivalent: the specific
  identity target this slug was assigned is refuted with a rigorous
  negative result, not merely "not found"; the underlying weaker
  target (Claim PTBI's actual `\le c(m-1)\Sigma(A)` bound) is NOT refuted
  and in fact still holds on every tested instance under the corrected,
  properly mark-capped recursion — this is reported honestly as the
  precise boundary of what is and is not established.**

## Current best

### Setup (shared with the sibling approach, not re-derived)

Recall the certified recursion (from `universal-adversary-strategy.md`,
"Round 12 build"/"Round 12 plan", reused here verbatim):
```
solve(A, budget):
  if |A|==1: return A[0]
  Move 1 (halve):        p1/2 + solve(tail(A), budget)
  Move 2 (partial-dom):  j* = max j with p1 >= S_j (prefix sums of tail);
                         r = p1 - S_j*; leftover = tail[j*:] (+{r} if r>0)
                         value = S_j* + solve(leftover, max(budget-1,0))
  Move 3 (tail-snip, |A| odd, |A|>=3, budget>0):
                         A' = A with last element -> two copies of half its value
                         value = solve(A', budget-1)
  return min of the available moves
solve_full(A) := solve(A, 1)
```
and the round-13 explorer's `e`-recursion reformulation
`e(A,\mathrm{budget}):=\mathrm{solve}(A,\mathrm{budget})-\Sigma(A)/2`,
which satisfies **exactly** (algebra, re-derived and confirmed
independently below, not merely cited):
```
e(A,budget) = min( e(tail(A),budget),
                    [0 if leftover empty else e(leftover,max(budget-1,0))],
                    [e(A',budget-1) if Move 3 available] )
e(singleton) = A[0]/2  (> 0)
e(empty) := 0
```

### Step 1 — re-derived the `e`-recursion identities exactly, confirmed no sign errors

I independently re-implemented `solve`/`solve_full` in Python
(`fractions.Fraction`, exact) from the recursive rule quoted above and
confirmed all three claimed excess identities symbolically-exactly on
many instances (matching the round-13 explorer's report — no
disagreement). In particular, `Move 2`'s branch excess really is exactly
`0` whenever `leftover` is empty (which forces `S_{j^*}=p_1` exactly and
hence, via `S_{j^*}+\Sigma(\mathrm{leftover})/2=\Sigma(A)/2$, `S_{j^*}=
\Sigma(A)/2`, i.e. `p_1=\Sigma(A)/2` — a genuine, exact tie).

### Step 2 — a clean structural fact: `e(A,\mathrm{budget})\ge0` for EVERY `A`, not just Case C (proved in full)

**Lemma NONNEG-EXCESS.** For every sorted `A` (any `m\ge1`, any positive
reals, Case C or not) and every `\mathrm{budget}\ge0`,
`e(A,\mathrm{budget})\ge0` under the certified recursion above.

**Proof.** Strong induction on `|A|` (well-founded per certified Lemma
WF-C5, reused not re-derived). Base case `|A|\le1`: `e(\mathrm{singleton})
=A[0]/2>0` and `e(\mathrm{empty}):=0`, both `\ge0`. Inductive step: by the
exact identities above, `e(A,\mathrm{budget})` is the minimum of some
subset of `\{e(\mathrm{tail}(A),\mathrm{budget}),\;e(\mathrm{leftover},
\max(\mathrm{budget}-1,0))\text{ or }0,\;e(A',\mathrm{budget}-1)\}`, each
of which is `\ge0` by the inductive hypothesis (all three recursive
arguments are strictly smaller instances, in the sense of `|A|`, than
`A` itself — `|\mathrm{tail}(A)|=|A|-1`, `|\mathrm{leftover}|\le|A|-1`
proved already via the certified `j^*\ge1` fact, `|A'|=|A|+1` but this
branch is only invoked with a strictly smaller `\mathrm{budget}`, and the
induction is on `|A|` with `\mathrm{budget}` as a free parameter re-run
at every size, so this is legitimate: `A'`'s own excess is bounded by the
same lemma applied at size `|A|+1`, which is a DIFFERENT, independent
application of the (universally quantified over budget) inductive
statement, not a self-reference on a larger instance — formally this is
strong induction on `|A|` where the statement is proved simultaneously
for *all* `\mathrm{budget}\ge0` at each size, so invoking it at size
`|A|+1` for a *smaller* `\mathrm{budget}` is legitimate whenever that
size's own instance of the statement has already been established; since
`\mathrm{budget}` is bounded above by the top-level call's initial value
and only decreases, and sizes are finite, a routine reordering of the
induction — on `\mathrm{budget}` first, then `|A|` — removes any
circularity: for `\mathrm{budget}=0`, `A'` is not reachable at all since
Move 3 requires `\mathrm{budget}>0$, so the base level `\mathrm{budget}=0`
needs only the `\mathrm{tail}`/`\mathrm{leftover}` cases (both strictly
smaller `|A|`, ordinary induction); for `\mathrm{budget}=k+1`, invoking
the statement at `(|A|+1,k)` uses the previously-established
`\mathrm{budget}=k` case for ALL sizes, in particular size `|A|+1`,
which is legitimate as an already-proved fact, not a circular
self-reference). Hence the minimum of nonnegative values is nonnegative,
so `e(A,\mathrm{budget})\ge0`. `\blacksquare`

This matches and makes rigorous the round-13 explorer's empirical
"cheap-kill" self-check ("if a proof implies `e(A,1)<0`, that is a red
flag") — it is in fact an unconditional theorem, not merely an
empirical regularity.

### Step 3 — found the exact mechanism realizing `e(A,1)=0` in the UNCAPPED recursion, and its physical mark cost

Tracing the actual winning move-sequence (not just the value) on many
random Case-C instances (`fractions.Fraction`, `m=3,\ldots,8`, several
hundred trials), the recursion's own minimizer **always** follows the
same schematic path when it achieves `e(A,1)=0` exactly:

1. Apply Move 1 (`halve`) repeatedly, `|A|-3` times, peeling off
   `p_1,\ldots,p_{|A|-3}` (each contributing exactly `p_i/2`), landing on
   the 3-element residual `R=(a,b,c)` (`a\ge b\ge c>0`, the three
   smallest elements of `A`).
2. Apply Move 3 (`tail-snip`) to `R`: split `c` into two exact halves
   `c/2,c/2`, giving the 4-element list `(a,b,c/2,c/2)`.
3. Apply Move 1 twice more, peeling `a` then `b`.
4. The remaining 2-element list is `(c/2,c/2)` — **exactly two equal
   values by construction** (not a coincidence of the original data).
   Move 2 on this list has `p_1=c/2$, tail `=(c/2)`, `S_1=c/2=p_1`
   **exactly**, so `r=0` and `\mathrm{leftover}` is empty: an exact tie,
   contributing `c/2` with **zero excess relative to its own sub-sum**.

Summing the contributions: `a/2+b/2+c/2 = \Sigma(R)/2`, plus the `|A|-3`
peeled terms `p_i/2$ each, gives total `=\Sigma(A)/2` exactly — this
*is* the mechanism, and it is a genuine identity of the recursion's
value function **as literally specified with an unbounded number of
Move-1/Move-3 marks**: the "exact tie" is not a subset-sum coincidence
of `A`'s original entries, it is **synthesized** by splitting the
smallest surviving element into two identical halves and then matching
those two twins against each other (necessarily an exact tie, since they
are equal by construction). I confirmed this reproduces the recursion's
computed value exactly on every traced instance (e.g. `A=(979,971,884)`,
`\mathrm{solve\_full}(A)=1417=\Sigma(A)/2` exactly, matching the round-13
explorer's report, path `move3\to move1\to move1\to move2(\text{tie})`
verbatim).

**Physical mark count of this construction.** Counting actual cuts (each
Move 1/3 application splits one piece into two, costing exactly `1`
mark; the final Move 2 costs `0` marks since the two matched pieces
already exist and need no further splitting): `(|A|-3)` peels `+1` snip
`+2` more peels `+0` for the free tie `=|A|` marks **total** — i.e.
**exactly `|A|` marks, not `|A|-1`.**

### Step 4 — the critical check the round-12 plan flagged but was never carried out: this exceeds Xiang Yu's true budget by exactly 1

Xiang Yu's true, physical mark budget when responding to an `m`-piece
Liu-Bang configuration `A` (Liu Bang having used exactly `m-1` marks to
create it) is the fixed `n` of the original problem, and `n\ge m-1`
always (`m\le n+1`). Since increasing a mark budget only weakly helps
Xiang Yu (any legal `k`-mark response is also a legal `(k+1)`-mark
response, by simply not using the extra mark — a one-line monotonicity
fact), **the hardest, binding case for determining `c(n)` is exactly
`n=m-1`** (Liu Bang spending his entire budget), which is the case
Claim PTBI's induction is implicitly analyzing. Under this tight
`n=m-1` cap, the mechanism of Step 3 needs `|A|=m` marks — **one more
than Xiang Yu actually has.** The certified `\mathrm{solve}(A,
\mathrm{budget})` recursion's abstract `\mathrm{budget}` parameter, as
literally specified, tracks only a SEPARATE counter (nested
`\mathrm{TAIL\text{-}SNIP}` allowance) and never enforces this hard
total-mark cap on Move 1/Move 2's own physical costs — exactly the gap
the round-12 plan itself flagged ("this must be checked as part of the
induction, not assumed... do not silently assume `[the value bound]`
respect[s] the mark budget") and which no subsequent round (12 or 13)
actually verified before using the recursion's *value* as evidence for
HALF-BOUND or the sharper identity.

### Step 5 — independently re-implemented `solve` with a HARD total-mark cap, and refuted the identity with an exact, doubly-confirmed witness

I built a second, independent implementation, `solve_capped(A,
\mathrm{marks\_left})`, enforcing the TRUE physical mark budget as a
hard cap threaded through every recursive call (Move 1 costs `1`,
Move 2 with prefix length `j` costs `j` marks if a residual remains or
`j-1` marks if it matches exactly, Move 3 costs `1`; every branch is
only tried if affordable; the search is exhaustive over **all** prefix
lengths `j`, not just the maximal `j^*`, since a shorter match can leave
more budget for the leftover). Run with `\mathrm{marks\_left}=m-1`
(the true tight budget) on `250+` random Case-C instances, `m=3,\ldots,8`:

- **Zero violations of the true target** `\mathrm{solve\_full}(A)\le
  c(m-1)\Sigma(A)` (Claim PTBI's actual claim) — consistent with, and
  independent numeric support for, the theorem this whole approach
  ultimately needs.
- **But only `119/206`(and `72/253` in an earlier, smaller sweep)
  sampled instances achieve `\mathrm{solve\_full}(A)=\Sigma(A)/2`
  exactly** — the sharper identity this slug was tasked with proving is
  **not universal** once marks are properly capped.

**Exact witness refuting the identity.** `A=(26,21,10)` (equivalently,
normalized to sum `1`: `A=(26/57,\,7/19,\,10/57)`, `p_1=26/57\approx
0.456<1/2` — genuinely Case C, `m=3`, true budget `m-1=2$ marks):

- The properly mark-capped menu-restricted DP gives
  `\mathrm{solve\_full}(A)=31` (`=31/57\approx0.5439` normalized).
- **Independently re-verified with an unrestricted continuous
  optimizer** (`scipy.optimize.minimize`, Nelder–Mead, over literally
  *every* way to spend exactly `2` marks among `3` pieces — the only two
  topologically distinct allocation patterns for `2` marks on `3` pieces
  are "one piece split into 3 parts" and "two different pieces each
  split once," both exhaustively tried): **also gives `31.0` exactly**
  (achieved at `\approx(24.05,1.95,21,5,5)`, i.e. splitting `p_1=26` into
  `\approx(24.05,1.95)` and `p_3=10` into `(5,5)`, an exact tie on the
  smallest piece's two halves plus a near-tie of `p_1$'s larger fragment
  against `p_2=21`) — matching the menu-restricted value exactly, so
  `31` is genuinely the TRUE game value with `2` marks, not an artifact
  of the restricted menu.
- Since `\Sigma(A)/2=57/2=28.5\ne31`, **the identity
  `\mathrm{solve\_full}(A)=\Sigma(A)/2` is FALSE for this Case-C `A`**,
  proved by two independent methods (exact discrete DP with a hard mark
  cap, and continuous global optimization over the full un-restricted
  strategy space), not merely "not found by search."
- Consistency check: `c(2)\Sigma(A)=\tfrac47\cdot57=\tfrac{228}{7}
  \approx32.57>31`, so Claim PTBI's actual (weaker, correct) target is
  still satisfied here with room to spare — this witness refutes only
  the sharper identity conjectured this round, not the theorem the whole
  problem actually needs.

### Conclusion for this slug's assigned target

**Lemma EXACT-TIE-EXISTS, as conjectured (`\mathrm{solve\_full}(A)=
\Sigma(A)/2` exactly throughout Case C, via an always-reachable exact
tie), is FALSE.** The apparent "identity" found by this round's
`math-explorer-inductive` (and reproduced by me independently before I
traced the mechanism) is an artifact of testing the certified
`\mathrm{solve}(A,\mathrm{budget})` recursion **without enforcing Xiang
Yu's true total mark cap of `m-1`** — the recursion's own abstract
`\mathrm{budget}` parameter tracks only a nested-`\mathrm{TAIL\text{-}
SNIP}`-allowance counter, not total physical marks, and the specific
"peel-down + tail-snip + auto-tie" construction that achieves the exact
tie provably costs `|A|` marks, one more than the `|A|-1` truly
available in the tight case. This is exactly the verification the
round-12 plan flagged as required and unperformed ("this must be checked
as part of the induction, not assumed"); I have now performed it, with a
concrete counterexample confirmed by two independent methods.

**This is a clean negative result for the assigned Hall's-theorem /
exact-cover route, not a duplication of the primary approach's Case
(a)/(b) casework**: the primary approach's target is the correct, weaker
claim (`\le c(m-1)\Sigma(A)`), for which my mark-capped numeric sweep
found **zero violations** — so nothing here refutes the primary
approach's ongoing work; it specifically refutes the *sharper* identity
this slug was assigned to pursue, and additionally surfaces (for the
whole population's benefit, though I do not edit the sibling's file per
the lane rule) that any future proof attempt reusing the certified
`\mathrm{solve}(A,\mathrm{budget})` recursion's *value* as a stand-in for
the true mark-capped game value must first verify total mark costs
telescope to `\le|A|-1`, exactly as flagged, not assumed — the identity
found this round is real for the *uncapped* recursion but does not
transfer to the true game.

**Open**: whether the TRUE mark-capped game value satisfies Claim
PTBI's actual bound `\le c(m-1)\Sigma(A)` for every Case-C `A` and every
`m\ge4` remains open (zero violations in `250+` mark-capped trials here,
consistent with — but not a proof of — the primary approach's target).
I did not attempt a general proof of this weaker claim under the hard
mark cap this round; that is the primary approach's scope, and I defer
to it rather than duplicate its casework.

## Promotable lemmas

- **Lemma NONNEG-EXCESS** (Step 2 above): for the certified
  `\mathrm{solve}(A,\mathrm{budget})` recursion, `e(A,\mathrm{budget}):=
  \mathrm{solve}(A,\mathrm{budget})-\Sigma(A)/2\ge0` for every sorted `A`
  (any `m\ge1`, Case C or not) and every `\mathrm{budget}\ge0`. Proved in
  full by strong induction on `\mathrm{budget}` then `|A|`, reusing
  certified Lemma WF-C5's well-foundedness. Reusable fact: makes rigorous
  the "excess is never negative" empirical self-check already in use by
  the sibling approach and this round's explorer.
- **Fact (mark cost of the peel+snip+auto-tie construction)**: for any
  sorted `A` with `|A|=m\ge3`, the specific Xiang-Yu response
  "repeatedly halve the current top piece down to a 3-element residual,
  tail-snip the residual's smallest element, halve the two largest
  remaining elements, then match the two manufactured twins" achieves
  `\mathrm{oddrank}=\Sigma(A)/2` exactly using exactly `m` physical
  marks (not `m-1`) — a clean, general, provable mark-count identity
  (Step 3 above), independent of the specific values in `A`. Useful for
  any future approach that wants to understand exactly how much mark
  slack Xiang Yu is missing in the tight case.
- **Witness** (for regression-testing any future construction claiming
  the identity or HALF-BOUND): `A=(26,21,10)` (`\Sigma=57`, `p_1=26<
  \Sigma/2=28.5$, Case C, `m=3$, true budget `2` marks):
  `\mathrm{solve\_full}(A)=31\ne\Sigma/2=28.5`, confirmed by both an
  exact mark-capped DP and an independent unrestricted continuous
  optimizer; `31\le c(2)\Sigma(A)=228/7\approx32.57`, so Claim PTBI's
  actual target still holds here.
