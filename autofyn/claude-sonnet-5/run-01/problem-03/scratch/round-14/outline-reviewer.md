## imo-2026-03 — round 14 outline review

Read: `/tmp/round-14/proof-outliner.md`, `results/imo-2026-03/current.md`,
`results/imo-2026-03/approaches/universal-adversary-strategy.md` (tail),
`results/imo-2026-03/approaches/universal-adversary-strategy-exact-tie.md`,
`.ranking.json`, `crux_moves_documentation.md` cross-check against
`past_crux_moves_database.json` for `aimo-0292`.

Context confirmed accurate: the entire lower bound and `m=3`'s upper bound
are closed and untouched this round (not re-litigated, correctly). The
sole remaining gap is Claim PTBI's Case C (`p_1<Σ(A)/2`) for `m≥4`, and
round 13's diagnosis (mark-bookkeeping bug in `solve(A,budget)`, real gap
re-sharpened to a Hall-type non-contiguous subset-matching existence
question) matches the outline's stated recap exactly — verified against
`current.md`'s round-13 status paragraph and the tail of
`universal-adversary-strategy.md`'s own round-13 build section. No drift
or overclaiming found.

### 1. universal-adversary-strategy (revise) — **APPROVE**, with mandatory pre-build checks

The technique is right and the plan is honest about what remains open
(Lemma SLACK-COVER is explicitly flagged as unproved, not asserted). Three
specific things checked and one item to fix before/during build:

- **`aimo-0292` cross-check (independent verification, not just name-match).**
  Pulled the actual crux entries from `past_crux_moves_database.json`: the
  real mechanism is "delete the largest block, split the achievable range
  into the sub-cases excluding/including it (the latter shifted by its
  weight), show the two shifted copies overlap using a per-element gap
  bound that follows from all blocks being ≥1." This is a real, applicable
  analog to "achieve a subset sum near a target by peeling the largest
  tail element and showing exclude/include ranges overlap" — the outline's
  characterization is accurate, not a superficial name-match.
- **Genuine disanalogy the outline does NOT flag and should:** `aimo-0292`'s
  overlap argument is load-bearing *because* every block weighs `≥1` (an
  integer lower bound), which bounds the largest element by the sum of the
  rest and controls the achievable-sum "mesh." Here tail elements are
  arbitrary positive reals with **no** uniform lower bound — the
  peel-the-largest overlap argument needs its own from-scratch proof of
  the analogous inequality (`t_1 ≤ Σ(rest) + slack`, or whatever the real
  analog is) from Case-C structure; it cannot be imported as-is. This is
  not fatal (the outline already scopes Lemma SLACK-COVER as "the open
  gap, do not claim proved, only give the reduction"), but the build
  should not silently assume the discreteness/mesh argument transfers —
  flag this explicitly as a CHANGES-REQUESTED item for the builder.
- **A second, more load-bearing gap not spelled out in the skeleton:**
  `aimo-0292` is a pure existence/covering question (no cost). Here there
  are TWO simultaneous constraints — subset-sum matching AND a real-mark
  budget that the recursion must respect. The outline states Move 2's
  cost (`|S|` or `|S|-1` if residual is exactly 0) but never shows how the
  "achievable target range" induction interacts with the recursive budget
  decrement — i.e., does the induction on `k=|T|` need its own secondary
  budget-tracking (a second induction parameter), or does Step 4's outer
  `(marks,|A|)` induction absorb this for free? This must be made
  concrete before the builder can claim SLACK-COVER even in a special
  case; treat as an explicit open item, not an oversight to silently
  paper over with "then it follows."
- **Well-foundedness with Move 0 added — independently re-checked, correct.**
  Move 0 recurses on the remainder at unchanged `marks`, strictly smaller
  `|A|` — consistent with `(marks,|A|)` lex, `marks` primary, exactly as
  WF-C5 already established for Move 3. The outline is right to flag this
  needs re-verifying rather than assuming zero-cost moves are automatically
  safe (per the round-12 WF-C5 precedent) — good instinct, and the check
  itself holds.
- **Move 0's scope is narrower than its own justification implies — flag
  for the builder.** The mechanism ("a pre-existing exact tie contributes
  its odd-rank value for free regardless of tie-break") is correct and
  trivial (`a_1=a_2 ⟹` whichever gets the odd rank contributes the same
  value). But the move as stated only checks for ties in the **top** `2k`
  elements (a prefix condition). If a tie exists lower in the sorted array
  (e.g. `p_3=p_4` with `p_1≠p_2`), the same free-contribution argument
  should still apply, but the move as written wouldn't detect/use it. This
  may or may not matter for the cases SLACK-COVER needs to cover — the
  builder should either generalize Move 0 to any tied pair (not just a
  top-prefix block) or explicitly justify why only top-prefix ties are
  ever relevant to the induction.

None of these are fatal — they're exactly the kind of "make the mechanism
concrete before claiming it" gaps CLAUDE.md's rigor rules require flagging
pre-build. **Verdict: APPROVE**, build with the above four items made
explicit gaps in the write-up (not glossed).

### 2. universal-adversary-strategy-exact-tie (retirement) — confirmed correct

Its assigned sharper target (`solve_full(A)=Σ(A)/2` exactly) is proved
false with a clean, reviewer-confirmed witness (`A=(26,21,10)`, true value
`31≠28.5`) — a complete negative result, not a stuck gap. Its only
remaining live content (the weaker existence question) is now textually
identical to `universal-adversary-strategy`'s own Step 3 (Lemma
SLACK-COVER) — continuing to build both would reproduce the exact
convergence-failure pattern already recorded twice (`minimax-mixed-
duality`, `case-c-secondary-extremality`). Its two certified
contributions (Lemma NONNEG-EXCESS, the mark-cost fact) correctly stay in
the shared lemma cache. **Retirement confirmed, no build.**

### 3. case-c-slack-covering (new) — **APPROVE, gated**

Genuinely distinct proof shape from approach 1 (non-constructive
averaging/pigeonhole vs. explicit peel-and-overlap construction), both
targeting the same lemma as competing whole-attempt routes to the same
end-to-end claim (Claim PTBI Case C) — this is the legitimate "two viable
ways to fill the same gap" pattern (per the standing memory rule #4/#10),
not the single-gap-trap CLAUDE.md warns against, since the rest of the
proof (recursion, Moves 0-3, base cases) is shared infrastructure, not a
disconnected slice.

Checked the outline's own safeguards: it correctly identifies the exact
failure mode that killed `potential-averaging-bound` (round 5) —
budget-blind fixed candidates that all individually overshoot cannot
average below target — and mandates a numeric feasibility gate against
three concrete hard witnesses, **explicitly including
`(965,965,958,482)`, which specifically requires Move 0** (this round's
own new finding) to be in the averaging family or the gate will fail
exactly as `potential-averaging-bound` did. This is the right gate,
correctly scoped, and per the standing rule ("ALWAYS verify a mandatory
numeric gate was actually run before trusting a candidate") — it has
**not** yet been run; this is appropriately assigned as the builder's
first task, not skipped or assumed passed. **Verdict: APPROVE**, but the
build set instruction below makes clear: if the gate fails on
`(965,965,958,482)` even with Move 0 included, downgrade/flag for likely
retirement next round per the round-11 convergence precedent — do not
sink further effort past a failed gate.

Note: no approach file yet exists at
`results/imo-2026-03/approaches/case-c-slack-covering.md` (the outliner
did not seed it this round). The builder should create it fresh from the
skeleton above; this is a process gap to note for future rounds (outliner
should seed new-approach files per the file contract), not grounds to
block the build — the outline text here is complete enough for the
builder to start from.

### Ranking

Registered `case-c-slack-covering` (cold start). Ranked:
- `universal-adversary-strategy` > `universal-adversary-strategy-exact-tie`
  (retiring, duplicative content absorbed into the winner).
- `case-c-slack-covering` > `case-c-secondary-extremality` (fresh live
  candidate vs. confirmed dead end with no independent leverage).
- `universal-adversary-strategy` draw `case-c-slack-covering` (anchor the
  newcomer against the field leader — neither has this round's concrete
  result yet).
- `universal-adversary-strategy-exact-tie` > `case-c-secondary-extremality`
  (real, if now-superseded, diagnostic progress beats a confirmed
  no-leverage dead end).

Post-update Elo: universal-adversary-strategy 1645 (top), recursive-
embedding-induction 1675 (untouched, lower bound fully closed, out of
scope this round), geometric-dominance-construction 1634 (untouched, same
status), case-c-slack-covering 1527, universal-adversary-strategy-exact-tie
1507 (retired), case-c-secondary-extremality 1422 (dead).

build set: universal-adversary-strategy, case-c-slack-covering
