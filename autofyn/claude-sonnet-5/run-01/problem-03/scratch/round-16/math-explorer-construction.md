## imo-2026-03

### 1. Exact reproduction of the m=6 witness's winning non-contiguous match

Reproduced with a from-scratch exact-`Fraction` memoized recursive solver
implementing the full menu (Move 0 free-tie-pair-removal, Move 1
halve-top, Move 2 arbitrary-subset match of ANY subset `S` of the current
tail against the current top piece — cost `|S|` if residual `r>0`, `|S|-1`
if `r=0` exactly, per certified Lemma EXACT-TIE-SLACK — Move 3
tail-snip), correctly value-tracking Move 0 (a caught bug in a first draft:
removing a tied pair must ADD its value `v` to the running total, not
silently discard it — the pair itself is a real contribution to Xiang
Yu's constructed multiset, not a deletion of mass).

On `A=(14,12,10,9,8,4)`, `Σ=57`, `marks=5`: solver value = `57/2 = 28.5`,
exactly matching the certified figure, `≤ target c(5)·57 = 608/21≈28.952`.

**Two independent winning move sequences found (both value 28.5, both
using only 5 marks):**

- **Sequence A** (the one the memoized min happened to return first):
  `14 → (7,7)` [Move 1, cost 1] then, on tail `(12,10,9,8,4)`,
  `12 → (8,4)` — an **exact (`r=0`) non-contiguous subset match**
  `12 = 8+4` against the array's own 5th- and 6th-largest pieces,
  **skipping the intervening pieces 10 and 9** — cost `|S|-1 = 1` mark
  (the boundary-slack case of Lemma EXACT-TIE-SLACK). Leftover `(10,9)`
  is then closed with the remaining 3 marks via ordinary Move 3
  (tail-snip `9→4.5,4.5`) + Move 1 (halve `10`).
- **Sequence B** (found by directly testing the alternative): `p_1=14`
  itself has an **exact non-contiguous subset match to `{10,4}`**
  (`14=10+4`, skipping `12,9,8`), cost `1` mark (`r=0` boundary again).
  Leftover `(12,9,8)` is then closed with the remaining 4 marks by the
  **already-fully-certified contiguous-only menu alone** (Move 1 halve
  `12`→6,6; Move 3 snip `8`→4,4; Move 1 halve `9`→4.5,4.5), reaching
  `14.5`; total `14+14.5=28.5`. No further non-contiguous matching is
  needed once the one top-level exact match is made.

**Characterization**: the m=6 witness's non-contiguous necessity boils
down to a single *exact* (residual-zero) subset-sum coincidence — either
`12=8+4` (a middle piece against the two smallest) or `14=10+4` (the top
piece against a non-adjacent pair) — both present in this specific
integer-valued witness. The exact match is what buys the `2`-mark slack
(Lemma EXACT-TIE-SLACK: `r=0` costs `|S|-1`, not `|S|`) that funds
closing the rest of the instance with the already-certified contiguous
menu. **This is a numerically fragile, coincidental feature of this
specific integer witness, not a structural law** — see stress test below.

### 2 & 3. Candidate constructive rule and stress test — REFUTED

Formalized the natural generalization suggested by the witness: **"Rule
Exact-Match-Or-Single-Greedy"** — at every recursion level, match the
current top piece `p_1` against the single largest element `t_1` of the
current tail (cost `0` if `r=t_1-p_1... ` wait, cost `0` if `r=0` exactly
[a lucky coincidence], else cost `1`, residual `p_1-t_1` reinserted);
recurse on the leftover with the reduced budget; fall back to Move 1
(halve) only if the tail is empty. This is a genuine attempt at turning
the witness's observed mechanism (match against a single well-chosen
element, exploiting the `r=0` cost-saving whenever it happens) into a
closed-form, non-exhaustive, `O(m)`-per-level rule.

**Stress test (exact-Fraction, `m=4..10`, 300 random Case-C configs each,
target = actual Claim PTBI target `c(m-1)Σ`, NOT the abandoned stronger
HALF-BOUND):**

```
m=4: fails 112/300   m=5: fails 151/300   m=6: fails 164/300
m=7: fails 173/300   m=8: fails 192/300   m=9: fails 202/300
m=10: fails 221/300
```

**Failure rate 35-74%, worsening with `m`.** Cross-checked one concrete
failing instance (`m=4`, `A=(388/509,412/571,420/943,1/475)`, `Σ=
1952767111125/... ` exact fraction, `marks=3`): the greedy rule computes
value `628336/538453 ≈ 1.1667`, strictly exceeding the target
`c(3)Σ ≈ 1.0300`. The independent full exhaustive-subset-match solver on
the *same* instance reaches exactly `125850484727/130184474075 ≈ 0.9667
≤ 1.0300` — the true minimum comfortably meets the target. **Confirms**:
the underlying Claim PTBI target is untouched on this witness — only the
greedy "single-largest-fitting-element" rule is refuted, reproducing
round 10's finding ("greedy largest-first subset-sum fails 74% of random
Case-C trials") under a genuinely different specific rule variant
(single-element match with residual reinsertion + `r=0` boundary-slack
awareness, not round 10's multi-element greedy subset-sum). **This rule
family is now dead by direct construction, not just by analogy to round
10's different rule.**

### 4. Why the rule fails, and what it means for the induction

The reason the exact-match coincidence works so cleanly at `m=6` is that
the witness is a **carefully tuned rational/integer point where an exact
subset-sum equality happens to hold** (`12=8+4` or `14=10+4`) — this is a
**measure-zero event** for generic real-valued configurations (confirmed
by re-running the same witness with a small perturbation `ε=1/100` or
`1/50` on various coordinates: the recursion still finds success, but
generally via a *different* single-element or few-element match with
`r>0`, at the normal, unsaved cost — the specific literal identity is not
load-bearing, the underlying SLACK-COVER existence question is). The
greedy single-element rule fails broadly because, exactly as round 10
found, **the correct subset choice sometimes must skip a larger-fitting
single element to leave a leftover that is itself easier to close
recursively** — a genuinely non-local trade-off between "match cost now"
and "value of the recursive leftover," which a one-step greedy cannot
see. This is not new mechanism, but it is a new, independently-derived
confirmation that **no simple closed-form single-element-or-exact-match
selection rule can replace the existence question** — the fix has to
either (a) prove existence abstractly (Hall/exact-cover style — already
tried and killed, round 15, `defect-hall-deficiency`) or (b) find a
genuinely multi-step/adaptive selection principle that looks ahead into
the recursive value of the leftover, not just the immediate match cost.

**If this rule had survived** (it did not), the natural induction branch
would have been: "if some subset `S⊆tail(A)` matches `p_1` (or any other
piece) exactly or near-exactly at low cost, use it; the trigger vs. the
existing Move 0-3 menu would be 'does a cheap subset match exist that
beats plain Move 1/Move 3' — same trigger as the still-open Lemma
SLACK-COVER, i.e. this rule would not have added new machinery, only a
priority ordering among already-known moves." Since it fails outright,
this sharpens (again) the standing conclusion: **the existence question
is genuinely global/adaptive, not reducible to any simple per-level
scoring rule tried so far** (greedy-largest-first: round 10, dead;
greedy-single-element-with-boundary-awareness: this round, dead).

### Recommendation for next round

Do not pursue further "simple constructive selection rule" attempts on
this specific family (single-element / exact-match-priority) — it is now
refuted by direct exact-Fraction construction, not just numerically
suspected. The `m=6` witness's "clean" non-contiguous match is a
coincidental integer-arithmetic feature, not evidence of an exploitable
general pattern. The productive next targets remain what round 15
already isolated: (1) finish the `m=4`-specific case-exhaustive proof
using only the already-certified **contiguous** menu (strong evidence,
not yet a full case tree); (2) attack the genuine `m≥6` non-contiguous
existence question directly via a genuinely different tool than
greedy/Hall (both now dead) — e.g. an amortized/potential argument over
the whole recursion (tracking total "slack budget" `c(k)Σ - value`
across levels) rather than a per-level selection rule, since this
round's evidence suggests the needed leverage is about how errors
telescope through the recursion depth, not about which single element to
match at the top.

## Distinct openings
- Reproduced exact winning matches for the m=6 witness (two independent
  minimal witnesses of the mechanism: `12=8+4` and `14=10+4`), both
  exact-residual (`r=0`) boundary matches — new, concrete artifacts for
  future rounds to test any candidate general lemma against.
- Refuted the natural "single-largest-fitting-element, boundary-aware"
  greedy rule as a general SLACK-COVER substitute (35-74% failure,
  worsening with `m`) — a genuinely different specific rule from round
  10's, independently confirming the same qualitative conclusion.
- Suggested (not attempted — out of scope per dispatch) a potential/
  amortized-slack framing as the most promising alternative to
  per-level greedy selection, motivated by observing that the m=6
  witness's success is really about *funding* (mark-budget accounting)
  more than about *which* element to pick.

## Candidate technique(s)
Amortized/potential-based accounting of the mark budget across recursion
depth (tracking `c(k)Σ(A) - value` as a monovariant, rather than
per-level greedy element selection) — flagged as the most promising
unexplored angle, not yet attempted.

## Cheap-kill candidates
None new beyond the two rule refutations documented above (both already
executed this round, not merely proposed).

## Knowledge-base entries to use
No new entries beyond what's already certified in this approach's own
lemma files (Lemma EXACT-TIE-SLACK, Lemma DOM-boundary-slack, Lemma
BLOCK-RECURSE, Lemma PAIR-VALUE) — this round's work is internal
construction/stress-testing, not a knowledge-base retrieval task.

## Analogous past problems (cruxes)
Not queried this round (dispatch scoped to internal reconstruction/
stress-testing of the m=6 witness and a specific rule family, not a
fresh corpus search) — round 15's `defect-hall-deficiency` already
explored the Hall/König matching-existence corpus angle and it is dead;
no new crux search performed here.

## Prior progress
Case C for general `m≥4` remains the sole open gap (unchanged). This
round's contribution: exact reconstruction of the m=6 non-contiguous
mechanism (two clean minimal witnesses, `12=8+4` and `14=10+4`) plus a
decisive refutation of the natural greedy-constructive-rule
generalization suggested by that mechanism.

## Dead ends (do not retry)
- Greedy largest-first subset-sum matching (round 10, 74% failure) —
  still dead.
- **NEW this round**: "Rule Exact-Match-Or-Single-Greedy" (match top
  piece against the single largest fitting tail element, prioritizing
  exact/`r=0` boundary-slack matches) — refuted by direct exact-Fraction
  construction, 35-74% failure rate across `m=4..10`, worsening with
  `m`; confirmed on a concrete `m=4` counterexample that the underlying
  Claim PTBI target is untouched (full exhaustive solver still meets it)
  — only this specific rule fails. Do not retry any single-element/
  boundary-slack-priority greedy variant without new evidence.
- Non-constructive averaging/pigeonhole (case-c-slack-covering, round
  14) — still dead, unrelated to this round's finding but reconfirmed
  not to overlap.
- Hall/König deficiency-based matching (defect-hall-deficiency, round
  15) — still dead, unrelated to this round's finding.

## Small-case / intuition notes
- Conjecture (evidence only, not proof): the m=6 witness's exact
  subset-sum coincidence is not load-bearing for the underlying theorem
  — small perturbations of the witness (breaking the exact `12=8+4` /
  `14=10+4` identities) still meet the target via a *different* concrete
  match (verified exactly for `ε=1/100, 1/50` on 3 different
  coordinates), consistent with the theorem being true generically, with
  the "exact-match funds cheaper recursion" phenomenon being one
  instance of a broader, still-unproven existence fact rather than the
  mechanism itself.
- Conjecture (evidence only): the true selection principle is likely
  genuinely non-local — greedy single-step scoring (by size, by
  exactness, or by boundary-slack availability) is refuted at a rate
  that *increases* with `m`, suggesting the number of "look-ahead" steps
  needed to correctly choose the subset grows with `m`, which is
  consistent with (but not proof of) the standing view that Lemma
  SLACK-COVER needs a genuine inductive/existence argument, not a
  formula.
