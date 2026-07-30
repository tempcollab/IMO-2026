# Round 15 adversarial review — imo-2026-03

Reviewed two built approaches: `universal-adversary-strategy` (round 15
build) and `defect-hall-deficiency` (round 15 build). All numeric/algebraic
claims re-derived and re-verified from scratch with independently-written
Python (`fractions.Fraction` exact arithmetic, plus `scipy` adversarial
search for the monotonicity check), not by trusting either builder's
scripts. Full detail of what was checked and how below; both verdicts are
recorded via `mcp__approach-ranker__record_outcome` and `current.md`'s
`## Status` section is updated accordingly.

## 1. `universal-adversary-strategy` — verdict: CHANGES REQUESTED

### Claim 1: Lemma MARKS-MONO (`solve2(A,k)` non-increasing in `k`)

The write-up's proof is a strong induction on the auxiliary well-founded
order `(k,|A|)` (lexicographic, `k` primary), using that every move legal
at budget `k` (cost `\le k`) remains legal at budget `k+1`, producing the
*same* resulting sub-instance with recursive budget bumped by exactly `1`,
and that the IH applies to that sub-call (either because the cost was
`\ge1`, dropping the first coordinate, or because the move was the
zero-cost Move 0, which strictly shrinks `|A|`). I re-read this argument
line by line — it is correct and does not conflate this induction with
`WF-C5`'s own termination argument (a point the write-up is careful to
flag, correctly).

I additionally reimplemented `solve2` under the contiguous-only menu and,
separately, the full non-contiguous-subset-match menu, from scratch, and
ran 260 random trials (`m=2..6`, random rational entries) checking
`solve2(A,k)` is non-increasing across `k=0,\dots,m+1` for each random `A`,
under both menus. Zero violations. This corroborates the proof; I found no
gap.

### Claim 2: Lemma EXACT-TIE-SLACK

Re-derived from the elementary fact "splitting a value into `j` positive
parts costs exactly `j-1` marks" (a general subdivision-counting fact,
independent of the specific values). The two cases (`r>0`: cost `=|S|`,
no slack at the recursive call; `r=0`: cost `=|S|-1`, `2`-mark slack)
follow by direct arithmetic on `m'` and `\mathrm{marks}-\mathrm{cost}(S)`.
I re-did this arithmetic independently and it matches exactly. Correct.

### Claim 3: the `m=4` extremal witness `A=(6,5,4,2)/17`

Reimplemented the contiguous-only `solve2` from scratch (own script, not
reusing the builder's) and ran it on `A=(6/17,5/17,4/17,2/17)` with
`marks=3`:
```
contiguous-only solve2(A,3) = 9/17
target c(3) = 8/15
margin = 8/15 - 9/17 = 1/255  (exactly, via Fraction, no floating point)
```
Matches the builder's claim exactly, including the exact fraction.

### Claim 4: the `m=6` counterexample `A=(14,12,10,9,8,4)`

Same independent solver (plus a second, independent implementation of the
full non-contiguous-subset menu):
```
Sigma = 57, p1 = 14 < 57/2 = 28.5  (Case C confirmed)
contiguous-only solve2(A,5) = 29
target c(5)*57 = 608/21 ≈ 28.952...
29 > 608/21   (violation, exactly 1/21)
full-menu solve2(A,5) = 57/2 = 28.5 <= 608/21   (target met, via genuine
   non-contiguous match — the contiguous-only solver, searching the same
   move types minus non-contiguous Move 2, cannot reach 28.5)
```
Matches the builder's claim exactly. This is a real, exact proof that
Lemma SLACK-COVER's general non-contiguous existence question cannot be
avoided for every `m` — it is provably needed at `m=6`.

### What is honestly NOT established

The builder does **not** claim a complete case-exhaustive proof that the
contiguous-only menu suffices at general `m=4`; the write-up's own algebra
(the `j^*=1` single-strategy sufficient condition `t_1\ge\frac4{15}\Sigma`)
is shown not to be implied by the sub-case's constraints, and the builder
explicitly says the full case tree was not completed. This is correctly
flagged as a gap, not smoothed over. I did not find any place where the
write-up asserts more than it has shown.

I also ran my own (much smaller, time-boxed) adversarial `scipy`
differential-evolution search for an `m=4` violation of the contiguous-only
menu against the real target `c(3)\Sigma`; it did not converge to a
meaningful violation in the time available (the search landed on a
degenerate near-zero configuration, not a genuine counterexample), which
is at least mildly consistent with — but far too weak to independently
confirm — the builder's own broader (400-trial + `scipy`) search claim.
I treat the `m=4` closure question as still genuinely open, exactly as the
builder reports it.

### Conclusion

Every specific numeric/algebraic claim independently checked reproduces
exactly. The two new lemmas (MARKS-MONO, EXACT-TIE-SLACK) are correctly
proved and add real, reusable structure. The `m=4` witness and `m=6`
counterexample are both exact, not near-misses, and together sharpen
(without closing) the gap: Lemma SLACK-COVER is now *proved* necessary at
`m\ge6`, and strong (not yet complete) evidence suggests it may be
avoidable at `m=4`. No overclaiming found anywhere. **Case C for general
`m\ge4` remains open.** Routed **CHANGES REQUESTED** — real, verified
progress; the approach stays live for a future round to either finish the
`m=4` case-exhaustive proof or attack the now precisely-located `m=6`+
existence question directly.

## 2. `defect-hall-deficiency` — verdict: RETHINK

### The central structural claim

Case C is defined by `p_1 < \Sigma(A)/2`. Hence
`\Sigma(\mathrm{tail}(A)) = \Sigma(A) - p_1 > \Sigma(A)/2 > p_1`, strictly,
unconditionally. I re-derived this myself directly from the definition —
it is a two-line algebraic fact, correct, and it does immediately imply
that a covering subset of the tail for `p_1` always exists (greedy
largest-first must reach or pass `p_1` before exhausting a tail whose sum
strictly exceeds `p_1`). I checked this holds on all three witnesses the
builder used (uniform-tail family, `T=(0.20,0.15,0.12,0.08)`,
`A=(1826,1563,1520,1514,765)/7188`) — trivially true in each case, exactly
as claimed.

### The dichotomy argument

The write-up argues both natural bipartite encodings fail to give useful
leverage:
- **Permissive graph** (any subset with `\Sigma(S)\le p_1`): Hall's
  condition holds trivially since existence is never in doubt (per the
  structural fact above) — deficiency identically `0`, giving no
  information about *which* covering subset achieves the required
  recursive value. This reasoning is sound: a Hall/König theorem's payoff
  is exactly "a saturating matching exists"; if that's already known
  unconditionally by a two-line argument, invoking Hall's theorem adds
  nothing.
- **Restrictive graph** (contiguous-prefix class only): I independently
  reproduced the concrete counterexample showing a Hall-witness in this
  restricted class can be exactly the *wrong* choice value-wise: tail
  `(0.20,0.15,0.12,0.08)`, contiguous match gives `oddrank=7/25=0.28`,
  strictly exceeding `\Sigma(T)/2=11/40=0.275` — reproduced exactly with
  `fractions.Fraction`, matching the value already independently certified
  in prior rounds (and re-confirmed in the sibling approach's round-15
  build above, `solve2(T,3)=7/25` under the contiguous-only menu).

Both horns are checked and both genuinely fail the "Hall-matching-exists
implies the needed value-good subset-match exists" requirement. I agree
with the builder's diagnosis: the underlying difficulty here is a
numeric/value optimization over which subset to pick (a subset-sum/
knapsack-value shape), not a cardinality/reachability question, and defect
Hall/König machinery is simply the wrong tool for this — not a case of
correct-tool-wrong-execution.

### Self-check on scope discipline

The builder correctly stopped at its own mandated Step-0 gate rather than
proceeding to Steps 1–2 (deficiency bound, value-adaptation) on an
unverified premise, per its own stated risk list and per CLAUDE.md's
"prove, don't conjecture" discipline. No overclaiming found; the `Status`
line ("unsolved (dead end...)") accurately reflects the content.

### Conclusion

This is a correct, honest, and now decisively confirmed negative result: I
found no flaw in either the structural fact or the dichotomy argument, and
independently reproduced the one concrete numeric counterexample it
depends on. The mechanism (defect-Hall/König deficiency) genuinely cannot
supply the missing value-optimization content for Lemma SLACK-COVER, in
either natural encoding. Per CLAUDE.md's diversity mandate, since the
approach's entire premise (a structurally different mechanism) is now
refuted with no repair path identified (the write-up itself does not
propose one — it explicitly says there is no encoding in between that
escapes the dichotomy), this should return to the outliner for a
genuinely different framing rather than being rebuilt as-is. Routed
**RETHINK**. The one reusable fact (`\Sigma(\mathrm{tail}(A))>p_1` always
in Case C, so covering existence is never the obstruction — only the
value of which cover to use) is worth keeping on file so no future round
re-derives it by numeric search.

## Overall problem status (for `current.md`)

**Status: partial**, unchanged from round 14. The lower bound, `m=1`,
`m=2`, `m=3` (fully general), and the well-foundedness/mark-accounting
machinery (`solve2`, Lemma WF-C5, Lemma MARKS-MONO, Lemma EXACT-TIE-SLACK)
are all correctly established and re-verified. **The sole remaining gap is
Case C's Lemma SLACK-COVER for general `m\ge4`** — proved genuinely
necessary (via non-contiguous subset matching) at `m=6` this round; not
yet proved either necessary or avoidable at `m=4` (strong exact evidence
for avoidable, no complete proof); and the defect-Hall/König-deficiency
mechanism is now ruled out as a route to proving it, in either natural
encoding. `current.md`'s `## Status` and `## Current best`... (the
relevant note) have been updated to reflect this precisely; nothing
previously closed is reopened.

## Outcomes recorded

- `universal-adversary-strategy`: `record_outcome(outcome="partial", ...)`
  — real, independently-verified progress (two new certified lemmas, one
  exact new witness proving SLACK-COVER's necessity at `m=6`, one strong
  but incomplete `m=4` witness), gap remains open. CHANGES REQUESTED.
- `defect-hall-deficiency`: `record_outcome(outcome="dead-end", ...)` — the
  defect-Hall/König-deficiency mechanism is decisively and correctly ruled
  out for this problem's actual open question, independently confirmed.
  RETHINK.
