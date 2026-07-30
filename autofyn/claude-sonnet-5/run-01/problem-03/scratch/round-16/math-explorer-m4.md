## imo-2026-03 (Case C, m=4 specifically)

### Headline finding (new this round)

I independently re-implemented `solve2(A,marks)` from scratch (own bugs found
and fixed along the way — see "Implementation notes" below) and used it to
run an exhaustive/high-density numeric campaign on m=4 Case C. Main result:
**a concrete TWO-BRANCH candidate construction, built entirely from
already-certified machinery (Lemma HALVE / Lemma BLOCK-RECURSE `j=1`,
composed with the already-fully-proved general `m=3` theorem as a
subroutine), reproduces the exact known extremal margin `1/255` at
`A=(6,5,4,2)/17` and shows ZERO violations across 8000 random trials plus an
independent `differential_evolution` global search — this is a much
stronger and more actionable structural finding than the round-15 write-up's
"~9 empirically observed winning shapes"; it collapses the m=4 case-tree
down to exactly 2 algebraic branches.**

Concretely, for `A=(p_1,t_1,t_2,t_3)` sorted descending, Case C
(`p_1<\Sigma(A)/2`), define:
- **Strategy A** (peel `t_1`, `j^*=1` match): cost 1 mark on `p_1` matching
  `t_1` (Lemma BLOCK-RECURSE, `j=1`; legal always since `p_1\ge t_1`), value
  `= t_1 + V_3(t_2,t_3,r)` where `r=p_1-t_1\ge0` and `V_3(\cdot)` is the
  **exact value of the already-fully-certified general `m=3` theorem**
  (rounds 8–9, `min(\text{TAIL-SNIP},\text{BLOCK-RECURSE}_1)` in Case C,
  Lemma DOM otherwise — this is a *proved*, not conjectured, closed form,
  unconditionally `\le c(2)\Sigma$).
- **Strategy B** (halve `p_1`, Lemma HALVE): cost 1 mark, value
  `= p_1/2 + V_3(t_1,t_2,t_3)`.

Both branches use only 1 top-level mark plus whatever the `m=3` theorem
itself certifies to close its own 3-element leftover with `\le2` marks (so
budget `\le3` total, matching `m-1=3`) — **no non-contiguous subset
matching, no new lemma, no open existence question**: everything here is
either Lemma HALVE, Lemma BLOCK-RECURSE (`j=1`, i.e. matching one single
tail element — trivially contiguous), or a direct invocation of the
already-certified `m=3` theorem as a black box.

**Numeric verification (this round, independent, exact `Fraction` +
`scipy.optimize.differential_evolution`):**
- 8000 random Case-C `m=4` instances (`Fraction`, denominators up to 300):
  `min(A,B)` **never** exceeds `target = c(3)\Sigma(A)` — 0 violations
  (compare: the same random sample against the *loose* bound
  `c(2)\Sigma(\text{leftover})` in place of the *exact* `m=3` value gave
  4084/20000 violations — confirming it is specifically the tightness of
  reusing the exact `m=3` theorem, not merely "peel + generic bound," that
  matters; this is the round-15 gap's actual fix).
- `differential_evolution` global search (3 free params after normalizing
  `\Sigma=1`, seed 7, popsize 40, tol `1e-13`) on `min(A,B)`'s margin
  converges to `(p_1,t_1,t_2,t_3) = (0.352941,0.294118,0.235294,0.117647)
  \approx (6,5,4,2)/17` **exactly**, margin `\to 0.00392157\ldots = 1/255`
  **exactly** — i.e. the two-branch construction's own worst case coincides
  exactly with the true worst case of the full recursive `solve2(A,3)`
  (which the round-15 approach already established has margin `1/255>0`
  there). This is strong evidence the two-branch construction is not just
  "usually good enough" but **exactly optimal** at the hardest point.

**What remains to turn this into a complete proof (not yet done, this is
the recommended next-round target):** an explicit algebraic case split on
`V_3(\cdot)`'s own two regimes (Case C vs. non-Case-C for the 3-element
leftover/tail in each of Strategy A and B) — i.e. at most `2\times2=4`
algebraic sub-cases — proving `\min(A,B)\le c(3)\Sigma(A)` in each. This is
a bounded, mechanical (if tedious) algebra problem, not a new existence
question. The round-15 write-up's own attempted sufficient condition
(`t_1\ge\frac{4}{15}\Sigma$) was for a *cruder* one-branch version using the
generic `c(2)\Sigma` bound instead of the tight `V_3`; redoing that algebra
with the tight `V_3` closed form (available explicitly in the file, "Round
8" section, Lemma BLOCK-RECURSE `j=1` closed form) should close the gap —
I did not complete this algebra this round (ran out of budget after the
numeric campaign), but the numeric evidence that it *will* close is now
much stronger than round 15's (zero violations under the *tight* two-branch
construction, exact reproduction of the known extremal point, vs. round
15's cruder single-branch attempt which had a real, demonstrated failure
mode).

### Extremal point `A=(6,5,4,2)/17` — verified exactly, and characterized

- Re-verified independently: `solve2(A,3)=9/17`, `target=c(3)\Sigma=8/15`,
  margin `=1/255>0$ (my own from-scratch reimplementation, after fixing two
  bugs — see below — matches the round-15 claim exactly).
- **Winning move sequence traced exactly**: Move 1 (halve `p_1=6/17\to
  3/17,3/17`) → Move 0 (the two new `3/17`s tie for free, contributing
  `3/17`) → Move 2 `j=1` (match new top `5/17` against tail-prefix `4/17`,
  cost 1, residual `1/17`) → stop on leftover `(2,1)/17` (`oddrank=2/17$,
  further splitting does not help — checked by hand: halving `2/17` gives
  three equal `1/17`s, `oddrank=2/17` again, no improvement). Total:
  `3/17+4/17+2/17=9/17`. Only **2** of the 3 available marks are used
  (Move 1 + Move 2; Move 0 is free) — the third mark is provably useless
  here, consistent with the certified Lemma MARKS-MONO.
- **Local extremum check (this round, new)**: perturbed each of the 4
  coordinates by `\pm1/10000` (holding the others fixed, i.e. 8 directions)
  and recomputed the exact margin in each case — **all 8 perturbations give
  a strictly larger margin** than the base point's `1/255` (values found:
  `1267/318750\approx0.003975` and `3373/850000\approx0.003968`, both
  `>1/255\approx0.0039216`). Combined with the DE global search converging
  to this exact point from random restarts, this is strong evidence
  `A=(6,5,4,2)/17` is an **isolated local (and very likely global) minimum
  of the margin function**, not part of a continuous degenerate boundary
  family — i.e. there is no flat "ridge" of equally-bad configurations to
  worry about; a proof need only handle this one point (and nearby algebra)
  tightly.
- The point sits in the interior of the `j^*=1` region (`t_1=5/17\le
  p_1=6/17 < t_1+t_2=9/17`), **not** at a boundary of that sub-case
  (residual `r=1/17\ne0`), and not at `t_1=\frac{4}{15}\Sigma$ (the round-15
  sufficient-condition boundary — here `t_1/\Sigma=5/17\approx0.294>
  4/15\approx0.267`, so round 15's own cruder sufficient condition is
  actually satisfied at the true extremal point; its documented failure
  mode was a *different*, non-extremal limiting configuration).

### m=4 vs m=5 vs m=6 — sharpened size-threshold picture

- **m=4**: strong new evidence (this round) that the tight two-branch
  construction above suffices everywhere — 0 violations, 8000 trials + DE.
- **m=5**: quick independent DE check this round (4 free params, contiguous
  menu via `solve2`) also found **no violation**, minimum margin
  `\approx0.0033>0` at `\approx(0.410,0.308,0.205,0.051,0.026)` (not pinned
  down to an exact rational this round — lower priority, flagged for
  follow-up). Consistent with round 15's claim that `m=5` likely also
  avoids needing non-contiguous matching.
- **m=6**: round 15's exact counterexample `A=(14,12,10,9,8,4)`
  (`\Sigma=57`) is **not re-derived from scratch this round**, but I did
  not find any error in it either; it remains the standing proof that
  non-contiguous matching is *unavoidable* at `m=6` (contiguous value `29`
  vs. target `608/21\approx28.952`).
- **Recommendation**: the induction very likely needs a size split — a
  hand-closed small-`m` regime (`m=4`, probably `m=5`, via the tight
  two-branch-type construction using the previous size's already-proven
  theorem as a subroutine) feeding into a genuinely different mechanism
  (Lemma SLACK-COVER / Hall-type non-contiguous matching, or something else
  not yet found) for `m\ge6`. This is not new relative to round 15's
  recommendation, but is now backed by a much more concrete/promising `m=4`
  closure strategy.

### Implementation notes (bugs found and fixed in my own reimplementation —
useful for any future round writing solve2 from scratch)

While independently reimplementing `solve2`, I initially introduced (and
caught via the sanity check against the known `9/17` value) two bugs that
are worth flagging since they are easy to reintroduce:
1. **Move 0 must add back the removed tied run's own contribution**
   (`(runlen/2)*value`) before recursing on the reduced list — naively
   deleting the run and recursing on the rest (treating the run as if it
   simply vanished) silently sets its contribution to 0, which is wrong
   (Lemma FREE-TIE-REDUCTION says the *parity* of everything else is
   unaffected, not that the removed run contributes nothing) and, worse,
   creates a spurious zero-cost self-loop when applied right after Move 1
   (the two new `p_1/2` copies always form a length-2 tied run, so a naive
   Move 0 would let Xiang Yu delete all of `p_1`'s mass for free — this is
   exactly the bug that gave a nonsensical `1/17` value on my first buggy
   run).
2. **Move 2 (subset/prefix match) must add back `\Sigma(S)` (the matched
   tail-prefix sum)** before recursing on the leftover — this is precisely
   Lemma BLOCK-RECURSE's content (`oddrank(\text{block}\cup W) = S_j +
   oddrank(W)`); omitting it (recursing on the leftover alone) silently
   discards the matched block's value entirely, again giving a spuriously
   small answer.
Both bugs, once fixed, make my independent implementation match every
previously-reported witness exactly (`9/17` at the `m=4` extremal point,
and the general shape of the round-15 numbers) — recorded here so a future
round's from-scratch reimplementation doesn't waste time on the same two
mistakes.

### Candidate technique(s)
- For `m=4` (and likely `m=5`): the **two-branch composition** above
  (Lemma HALVE + `m=3`-theorem-as-subroutine, vs. Lemma BLOCK-RECURSE `j=1`
  + `m=3`-theorem-as-subroutine), closed by a bounded (`\le4`-way) algebraic
  case split on which regime of the `m=3` theorem each branch's leftover
  falls into. This is new structural content from this round, not present
  in the current `current.md`/approach file.
- For `m\ge6`: still the open Hall-type/subset-matching existence question
  (Lemma SLACK-COVER), per rounds 9–15; no new idea from this round on that
  side (out of scope for this dispatch).

### Cheap-kill candidates
- None new. (The perturbation check above is itself a cheap local-extremum
  sanity check, not a proof technique for the general case.)

### Knowledge-base entries to use
- Lemma HALVE, Lemma BLOCK-RECURSE (`j=1` case), Lemma DOM,
  Lemma TAIL-SNIP, Lemma MARKS-MONO, Lemma EXACT-TIE-SLACK — all already
  certified in `results/imo-2026-03/lemmas/` and
  `approaches/universal-adversary-strategy.md`. The general `m=3` theorem
  (`\min(\text{TAIL-SNIP},\text{BLOCK-RECURSE}_1)\le c(2)\Sigma$ in Case C,
  Lemma DOM otherwise — Round 8–9 content) is the key reusable subroutine
  this round's finding leans on.

### Analogous past problems (cruxes)
Did not query the crux corpus this round (dispatch was narrowly scoped to
numeric/algebraic verification of the m=4 sub-case using only
already-identified in-repo machinery); no new crux search performed. Prior
rounds' crux usage (if any) is not revisited here.

### Prior progress
See `results/imo-2026-03/current.md` Status (partial) and the round-15
build section for full context; this round's finding is additive to, and
sharper than, round 15's "strong evidence for m=4" claim — it supplies a
concrete, near-complete construction rather than only an empirical
observation.

### Dead ends (do not retry)
- Using the **loose** bound `c(2)\Sigma(\text{leftover})` in place of the
  exact `m=3` theorem value for either branch: confirmed this round to
  fail badly (4084/20000 violations) — the tightness of reusing the exact,
  already-proven `m=3` value (not just its existence) is load-bearing.
- Round 15's specific sufficient condition `t_1\ge\frac{4}{15}\Sigma$ for a
  single-branch (peel-only) strategy: confirmed (by inspection, not
  re-derived from scratch this round) to fail on a limiting family; this
  round's two-branch min avoids needing that condition at all (Strategy B
  covers the region where Strategy A's naive sufficient condition would
  fail).

### Small-case / intuition notes (conjectural unless stated as re-verified)
- **Re-verified exactly** (not conjecture): `A=(6,5,4,2)/17` gives
  `solve2=9/17`, target `8/15`, margin `1/255$.
- **Conjecture, strong numeric support** (DE + 8000 trials, zero
  violations, exact match at the extremal point): the two-branch
  construction above closes m=4 Case C in full.
- **Conjecture, lighter support** (one DE run, no exact witness pinned
  down): m=5 Case C is also closeable by an analogous (three-branch?)
  contiguous-only construction using the `m=4` theorem as a subroutine,
  once `m=4` itself is fully closed.
- **Established fact** (inherited from round 15, not re-derived this
  round): m=6 genuinely requires non-contiguous matching
  (`A=(14,12,10,9,8,4)`, exact violation `1/21`).
