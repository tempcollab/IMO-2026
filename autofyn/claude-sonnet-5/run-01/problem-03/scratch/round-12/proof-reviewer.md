# Proof review — round 12 — imo-2026-03

## Scope
One built slug this round: `universal-adversary-strategy`, "Round 12
build" section (Candidate 5: budget-capped TAIL-SNIP recursion). This is
the sole remaining gap for the entire problem (lower bound fully closed
since round 10; upper bound Cases A/B and m=1,2,3 fully closed; only
general-`m≥4` Case C is open).

## What was checked, and how

### 1. Lemma WF-C5 (well-foundedness of the Candidate-5 recursion)

Re-derived independently from the definitions (not from the builder's
proof text): defined `solve(A,budget)` exactly as specified (Move 1
halve, Move 2 partial-dom with budget-decremented leftover, Move 3
tail-snip gated on `|A|` odd and `budget>0`), and re-derived from
scratch why `(budget,|A|)` lexicographic with `budget` primary is the
correct well-founded measure:

- Move 1: budget ties, `|A|` strictly decreases. OK.
- Move 2: budget never increases; the `j*≥1` sub-claim (`A[0]≥A[1]=S_1`
  since `A` is sorted descending, so `j=1` always satisfies `p_1≥S_j`)
  guarantees `|leftover|<|A|`, covering the `budget=0` tie case. OK,
  independently reproduced.
- Move 3: budget strictly decreases regardless of `|A|` increasing —
  this is exactly why `budget` must be primary, not secondary; under an
  `|A|`-primary order (the outline's original, buggy statement) this
  move does not register as a decrease. The builder correctly diagnosed
  and fixed this.

I independently implemented `solve`/`solve_full` in Python with exact
`fractions.Fraction` arithmetic (from the spec, not from the builder's
script) and ran it on thousands of random instances (`m=2..12`,
`budget∈{0,1}`) with no non-termination and small, non-exploding call
counts, consistent with the measure argument. (Caught and fixed one bug
in my *own* test harness along the way: for `m=2`, Case C `p_1<Σ/2` is
vacuous since sorted-descending forces `p_1≥p_2≥Σ/2` — not a flaw in the
proof or recursion, just an artifact of my random-instance generator
that I corrected before drawing conclusions.)

**Verdict: Lemma WF-C5 is correct and gapless as proved.** Certified to
`results/imo-2026-03/lemmas/wf-c5.md`.

### 2. Mandatory adversarial gate

Independently re-implemented Candidate 5 in float form and ran my own
`scipy.optimize.differential_evolution` sweep for `m=4..12` (fresh
script, not the builder's), minimizing `c(m-1)Σ(A) - solve_full(A)` over
the Case-C simplex. Found strictly positive margins at every `m`,
matching the builder's claimed closed form `margin(m)=1/(2(2^m-1))`
essentially exactly at every tested `m` (e.g. `m=4`: `0.03333.. =
1/30`; `m=8`: `0.0019608 = 1/510`; `m=12`: `0.0001221 = 1/8190`). This
is strong independent corroboration — not a re-run of the builder's own
code, but an independent re-derivation from the spec that reproduces the
same extremal values.

Also independently ran the reviewer's own 3,000-trial exact-`Fraction`
random Case-C sweep (fresh implementation): zero violations of both
`solve_full(A)≤c(m-1)Σ(A)` and the sharper `solve_full(A)≤Σ(A)/2`.

Also independently checked the builder's flagged "tail locally dominant"
witness `A=(0.45,0.40,0.06,0.05,0.04)`: confirmed `solve_full(A)=1/2`
exactly (matches `Σ/2`), while a pure Move-1-only halving chain
overshoots to `13/25=0.52>1/2` — confirming Move 2/3 do genuine
load-bearing work here and that the flagged HALF-BOUND gap is real, not
a red herring or artifact.

**Verdict: gate genuinely passes, independently reproduced with a fresh
implementation and fresh optimizer run, not just re-trusted.**

### 3. Lemma HALF-BOUND — honesty check

The builder's own "Verdict for this round" explicitly states: "Status
remains `partial`... Case C for general `m≥4` is narrowed and sharpened
but still open." No overclaiming found anywhere in the round-12 section
— the file is explicit that HALF-BOUND is a conjecture strongly
evidenced numerically but not proved, and precisely isolates the one
open sub-case (a non-top-level tail piece becomes locally dominant
relative to its own remaining sum, so repeated Move-1 halving cannot
telescope to exactly `Σ/2`; Move 2/3 must do the work in that regime but
no inductive argument covering it exists yet). This isolation is
correct and matches my own independent reproduction of the overshoot
computation above — it is a genuine, precisely-scoped gap, not
hand-waving.

## Result

**Case C for general `m≥4` is NOT closed.** This round made real,
verified, honestly-reported progress (well-foundedness fully closed,
gate re-confirmed at a wider scope with a fresh independent
implementation, gap sharpened from "the whole induction" to "one precise
sub-case of a cleaner sufficient lemma") but did not close the gap. The
whole problem `imo-2026-03` therefore remains **`partial`**, not
`solved` — the round-12 build note in `current.md` (as I found it, prior
to my edits) was already accurately scoped as pending review with an
open gap; I've now finalized it as reviewed, unchanged in substance.

`current.md` updated: Status note replaced with the finalized round-12
review (Lemma WF-C5 confirmed and certified, gate confirmed, HALF-BOUND
gap confirmed real and precisely scoped), "Approaches tried" entry
added for round 12, open-gaps section (#2, general `m≥4` Case C)
extended with the round-12 sharpening and the concrete next target
(the tail-locally-dominant sub-case, possibly via
Hall-deficient-set-deletion / crux `aimo-0063`, not yet reached this
round).

## Promotable lemma certified

`results/imo-2026-03/lemmas/wf-c5.md` — Lemma WF-C5, well-foundedness of
the Candidate-5 recursion. Sorry-free, statement matches exactly what
was proved (termination only — explicitly scoped as NOT establishing any
value inequality), independently re-derived and re-verified by the
reviewer with a fresh implementation. Certified.

## Outcome recorded

`record_outcome(imo-2026-03, universal-adversary-strategy, round=12,
outcome=partial, note="WF-C5 closed+certified; gate re-confirmed
independently; HALF-BOUND gap (tail-locally-dominant sub-case) remains
open, Case C m>=4 still unsolved")`.

## Verdict

**CHANGES REQUESTED** for `universal-adversary-strategy` — real,
independently-verified progress (Lemma WF-C5 fully closed and certified,
the mandatory adversarial gate independently re-confirmed with a fresh
implementation matching exact claimed margins), but the load-bearing gap
(Lemma HALF-BOUND's tail-locally-dominant sub-case, equivalently Case C
for general `m≥4`) remains open. **Status: partial** — for both the
`universal-adversary-strategy` approach and the whole problem
`imo-2026-03` (this is still the sole remaining gap; nothing else in the
problem needs further work once this closes).
