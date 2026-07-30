## imo-2026-03 (lens: GAP L — lower bound Case B, the shared-cut-budget cancellation)

### Key finding (numeric, this round): the "strict refinement" the leader approaches ask for is FALSE — pursue an exact-value recursion instead

`induction-recursion.md` and `current.md` both frame the remaining work as: prove a
**strict** cut-budget-refined bound `W(n−1,b) > u_{n−1}` for `b < n−1`, to beat the
cancellation term `2λ(O_top∩O_bot)` in the identity `D = λ(O_top)+λ(O_bot)−2λ(O_top∩O_bot)`.
I built a Nelder-Mead/grid optimizer (`/tmp/explore_gapL4.py`, `/tmp/explore_gapL3.py`,
`/tmp/explore_gapL2.py`) over the exact Case-B search space (Xiang: choose `a` cuts on the
top dyadic piece `g_n` producing any composition of `a+1` positive parts, and independently
choose `b=n−a` cuts distributed over the bottom block, each landing on some current bottom
sub-piece) and found:

- At **n=3**, allocation `a=2,b=1` (i.e. `b=1<n−1=2`) with the single bottom cut placed on
  the bottom's OWN largest piece (`4u`, i.e. bottom-block's "top" element) achieves
  `D = u` **exactly** (Nelder-Mead converges to `0.06666667` = `u` to machine precision,
  diff `~1e-16`), not `> u`. Likewise `a=1,b=1` cutting that same bottom-top piece also hits
  `D=u` exactly.
- But `a=1,b=1` cutting either of the *other two* (smaller) bottom pieces gives `D=0.1333`
  or `D=0.2`, both `≫ u` — so the specific piece cut matters enormously, not just the count.
- So **`W(n−1,b) = u_{n−1}` (scaled) can be attained with equality for `b` strictly less than
  `n−1`**, whenever the extra bottom cut lands on the bottom block's own dominant piece and
  is used "efficiently" (i.e. recursively mimics the same top/bottom self-similar split one
  level down). The strict inequality `W(n−1,b) > u_{n−1}` that the leader approaches propose
  as the missing lemma is **false as stated** — do not have the outliner chase it; a
  non-strict argument is needed that is robust to equality.
- This also means the Case A/B dichotomy is itself somewhat artificial: the *same* value
  `D = u` is realized by many distinct cut-allocations `(a,b)` and by many distinct "which
  sub-piece" choices — the discrepancy-minimax value is flat/tight along a whole family of
  near-optimal Xiang responses, not just at one boundary case. A clean proof should exploit
  this flatness (an exact recursive VALUE formula), not chase strict domination.

### Distinct openings

1. **(Recommended) Exact minimax-value recursion, not an inequality chase.** Define
   `V(n,k) := min_{Xiang, ≤k cuts} D` for the `n`-dyadic Liu partition (`0≤k≤n`). The goal
   `V(n,n)=u_n` should be provable by strong induction on `n` via an EXACT recursive formula
   for `V(n,k)` (not merely a lower bound), because the equality case is attained on a whole
   family of allocations — a clean value recursion (mirroring `u_n = u_{n-1}/(2+u_{n-1})`)
   is more likely to close cleanly than an inequality with slack that turns out to vanish.
   Concretely: guess `V(n,k) = u_n` for `k≥n` and `V(n,k) > u_n` for `k<n` (this needs
   checking at more points — see below), then set up the induction as "the top piece `g_n`,
   however split by `a≤n` cuts, combined with the bottom `(n−1)`-dyadic subjected to `≤ n−a`
   cuts, cannot beat `u_n`" using an EXACT decomposition of `D` (the `O_top△O_bot` identity
   already proved) plus a case analysis not on `a` alone but on how the top's largest
   sub-piece compares to the bottom's largest sub-piece (a merge/interleaving argument,
   since which piece is globally largest determines the greedy claim order — Lemma G already
   reduces everything to sorted order, so the real invariant is the RANK interleaving of
   top-descendants vs bottom-descendants, not just their separate discrepancies).

2. **Rank-interleaving framing (bypasses O_top/O_bot cancellation entirely).** Since Lemma G
   says `D` is exactly the alternating sum over the merged sorted order, and top-descendants
   all have length `≤ g_n` while bottom-descendants are `≤ g_n/2` (bottom total is `g_n − u`... 
   actually bottom total `σ=1−g_n`), track the *interleaving pattern* of top-pieces and
   bottom-pieces in the merged sorted list directly (a 0/1 string of "T" and "B" labels) and
   show that regardless of Xiang's cuts, the interleaving pattern's signed sum is `≥ u`. This
   avoids computing `λ(O_top)`, `λ(O_bot)` separately (where cancellation is confusing) and
   works with the merged order directly — a genuinely different sub-framing worth having a
   rival approach try, since it sidesteps the exact cancellation term the leader is stuck on.

3. **Potential/monovariant framing:** since equality is attained on a large family, look for
   an explicit *exchange argument*: show that any Case-B Xiang response can be transformed,
   without decreasing Xiang's payoff (i.e. without increasing `D`... wait Xiang minimizes
   `D`, so this direction should show D can only be pushed up by "undoing" any exotic cut),
   into the canonical self-similar response (recursively split the largest current piece by
   the same u_n/u_{n-1} ratio), and that THIS canonical response gives exactly `D=u`. This
   converts the open-ended optimization into a "WLOG canonical form" argument, which is often
   easier to make rigorous than bounding an arbitrary adversarial split.

### Cheap-kill candidates
- Check whether *any* Case-B allocation, at n=2,3,4 (finer, exact rational search), can push
  `D` strictly BELOW `u`. All optimization so far (random search to `~1e-4-1e-6` precision,
  and Nelder-Mead to `~1e-16`) finds minimum exactly `u`, never below. This is strong
  (numeric, not proof) confirmation that `D≥u` really is tight and true for Case B, so the
  target inequality itself is safe to keep pursuing — no need to weaken the conjectured bound.
- A parity/size check worth doing before further proof effort: confirm whether the "canonical"
  equality-achieving Xiang responses ALWAYS recursively split only the currently-largest
  piece (never a smaller one) — if that pattern holds up at n=4 too, it strongly supports
  opening 3 (the exchange/canonical-form argument) as the most tractable route.

### Knowledge-base entries to use
- No KB entry specifically matches (checked `knowledge_base.md`; only generic "casework"/
  "check the answer" entries near line 186, 236, 245 — nothing on discrepancy games or
  alternating-claim games). Flag to outliner: may eventually want a new KB entry once solved
  ("alternating greedy-claim ⇒ odd-rank sum", already captured as certified Lemma G — good
  candidate for a KB addition post-solve, not now).

### Analogous past problems (cruxes)
- Searched crux corpus `combinatorics/games-and-strategy` (full subtopic list confirmed via
  `crux_moves_documentation.md`: fields are `problem_id`, `domain`, `subtopic`, `technique`,
  `how_used`, `technique_tags`, `subtopics`, `retries`). Keyword-filtered for
  stick/interval/alternat/claim/discrepancy/split/divide: only 3 hits
  (`aimo-0196` boundary-freezing coin game, `aimo-0461` monochromatic-class counting,
  `aimo-0663` no-consecutive-picks pigeonhole) — **none are genuinely analogous**; they are
  combinatorial-game pairing/pigeonhole arguments on discrete structures, not a continuous
  stick-division discrepancy-minimax. `aimo-0117` (already flagged round 1, domination
  invariant `2^k > sum of smaller`) remains the best partial analogue but only for the
  *construction* (why dyadic weights are the right Liu partition), not for GAP L's
  cancellation-avoidance step — no corpus entry addresses that step. Report: **no strong
  crux match for GAP L specifically.**

### Prior progress
- Full spine already certified (Lemma G, Level-Measure Formula, Cut-Flip Lemma — see
  `lemmas/greedy-claim.md`, `lemmas/cut-flip.md`).
- Case A (top piece uncut) fully proved: `D ≥ 2b₁−1`, `b₁=g_n ⇒ D≥u`.
- Case B reduced to exact identity `D = λ(O_top)+λ(O_bot)−2λ(O_top∩O_bot)`, `λ(O_bot)≥u_{n-1}`
  by strong IH scaled — this much is solid and reusable regardless of which opening above is
  chosen.

### Dead ends (do not retry)
- **Chasing a strict inequality `W(n−1,b) > u_{n−1}` for `b<n−1`.** Refuted this round:
  numerically, `b=1 < n−1=2` (at n=3) attains EQUALITY `D=u_{n-1}` (scaled) when the single
  extra bottom cut lands on the bottom block's own dominant piece — so no strict gap exists
  to exploit in general. Any approach banking on strict domination from "fewer cuts ⇒
  strictly bigger bottom discrepancy" needs to be revised or abandoned; the correct fact is
  a tight, sometimes-equality bound, requiring an exact-value (not pure-inequality) argument.
- (Carried over from round 1, still valid) equal-`(n+1)`-pieces and "`2n+1`-equal-final-pieces"
  Liu constructions are refuted as extremal — irrelevant to GAP L since Liu's dyadic
  construction itself is not in question here, only Xiang's Case-B response to it.

### Small-case / intuition notes (all numeric, labeled conjecture except where noted CERTIFIED)
- CERTIFIED (proof-reviewer round 1): Lemma G, Level-Measure Formula, Cut-Flip Lemma, Case A.
- Conjecture (strong numeric support, n=2,3, multiple optimizers): Case B minimum is exactly
  `u`, attained by several distinct Xiang allocations, most cleanly when Xiang recursively
  splits whichever piece is *currently the largest remaining piece* using a self-similar
  dyadic-like ratio — never below `u` in any search performed (random, grid, Nelder-Mead).
- Conjecture: the canonical/extremal Xiang response has a recursive self-similar structure
  (split largest piece; recurse into the two/several resulting sub-problems) that likely
  mirrors the recursion `u_n=u_{n-1}/(2+u_{n-1})` piece-by-piece — this is the shape an
  exact-value induction (opening 1) should target, but is NOT yet derived in closed form;
  only the equality-value numerics support it.
