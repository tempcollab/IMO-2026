# proof-builder report — case-c-slack-covering (round 14)

## Task
New slug (no prior file existed). Mandate: attempt a non-constructive
averaging/pigeonhole route to Claim PTBI's Case C (`p_1<Σ(A)/2`, general
`m≥4` — the sole remaining gap for the whole problem), run the mandatory
numeric feasibility gate against known hard witnesses FIRST (especially
the new round-14 witness `A=(965,965,958,482)`), and report honestly if
the gate/idea fails.

## What I did
1. Set up the averaging family precisely: for each tail element `t_i`,
   the candidate move "split `p_1` into `(t_i, p_1-t_i)`, tie with `t_i`,
   bound the leftover by the induction hypothesis at size `m-1`." Derived
   the exact value identity via the already-certified Lemma DOUBLE-INSERT
   (`oddrank(after) = t_i + oddrank(REST_i)`, exact, not an estimate),
   and checked the mark budget telescopes exactly (`1 + (m-2) = m-1`,
   matching `|A|-1`) — this resolves the outline-reviewer's flagged
   concern about a secondary budget-tracking parameter for this specific
   construction.
2. Proved (elementary) the pigeonhole/averaging lemma, then found a
   structural collapse: since `c(n)>1/2` always, the bound `UB_i` is
   monotonically decreasing in `t_i`, so the family's minimum is always
   `UB_1` (match with the largest tail element `p_2`) — meaning averaging
   can never beat this single explicit choice. This means the
   "genuinely non-constructive" character promised by the mandate does
   not materialize for this natural family; the best move is always
   explicitly identifiable.
3. Ran the mandatory numeric gate (exact `fractions.Fraction`) on
   `A=(26,21,10)/57`, `A=(0.45,0.20,0.15,0.12,0.08)` (round-13 witness),
   and `A=(965,965,958,482)/3370` (the new round-14 witness) — all three
   PASS (the last one only barely, margin `1/4718`), and the construction
   reproduces the exact known true game value on the `m=3` witness (`31`),
   a good correctness check.
4. Found the decisive worst case analytically (uniform tail, `p_1→Σ/2⁻`)
   and proved, by exact symbolic algebra (`sympy`), that the margin
   `c(m-1)-UB_1` has closed form `[2^m(3-m)-2]/[2(2^m-2)(2^m-1)(m-1)]`,
   which is **strictly negative for every integer `m≥4`** — not a
   numeric near-miss at sampled `m`, a proved-for-all-`m` algebraic fact.
5. Diagnosed why: the near-uniform-tail boundary is the same persistent
   hard regime that has obstructed every other Case-C approach since
   round 11 (self-similar fixed point — the leftover after one match is
   again near-uniform at the same ratio, so one application of the IH
   is provably insufficient there). Any fix needs the same multi-level
   recursive matching content `universal-adversary-strategy`'s Lemma
   SLACK-COVER already needs, so this route offers no independent
   leverage in its gated form.

## Verdict
Per the mandate's own instruction ("if your averaging idea can't account
for this witness's structure, that's a fast, honest downgrade signal...
report that honestly rather than pushing forward with a broken
foundation") — this is a genuine, decisive, precisely-quantified dead end
for the specific one-level-averaging mechanism, reported honestly.
**Status: partial** (not `solved`; Case C remains open). Two reusable
lemmas are proposed for certification (the exact match-value identity,
and the uniform-tail worst-case margin formula) since they rule out an
entire natural class of future "one match + one IH application" attempts
without needing fresh numeric search.

## File written
`/home/agentuser/repo/results/imo-2026-03/approaches/case-c-slack-covering.md`
(Status: partial)
