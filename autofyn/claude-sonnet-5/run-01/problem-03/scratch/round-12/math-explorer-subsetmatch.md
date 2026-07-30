## imo-2026-03 (dispatch: scout the m=8 counterexample / non-contiguous subset match)

### Headline finding — the m=8 counterexample does NOT require non-contiguous subset matching

I reproduced the sibling explorer's `m=8` counterexample exactly (rational
approximation, `fractions.Fraction`, denominator 10000):
```
A = (2117,3970/25→wait see below,...)/10000 sorted desc:
A = (0.2117, 0.1588, 0.1410, 0.1319, 0.1232, 0.0881, 0.0748, 0.0705)   [Σ=1 exactly]
target = c(7)·Σ = 16384/32767 ≈ 0.50196078...
Candidate-3 value = 0.5021, margin ≈ -0.0001392   (my rational witness; slightly
different denominator from sibling's, same sign/order of magnitude as their
-1.53e-4 — same phenomenon, independently reproduced)
```
I then did an **exhaustive brute-force search over every subset `T` of the
7-element tail** as a donor-match for `p_1` (all `2^7-1=127` nonempty
subsets, exact `Fraction`, recursing on the residual `U` via Candidate 3's
own `solve_full`). Result:
```
Best subset found: T = {p_2} alone  (i.e. the ORDINARY length-1 PREFIX —
NOT a non-contiguous subset at all)
value = 0.5,  margin = target - 0.5 = +0.00196  (STRICTLY POSITIVE, closes the gap)
```
So **the winning donor/subset is exactly the maximal-prefix PARTIAL-DOM match
Strategy 2 already uses** (`p_1` dominates only `p_2`, since `p_2+p_3=0.2998
> p_1=0.2117`, so the maximal PARTIAL-DOM prefix length is `j=1={p_2}`,
identical to what SUBSET-DOM's brute force also picked as optimal). The
*subset* was never the problem.

**What actually differs:** Candidate 3's Strategy 2 recurses on the leftover
`U` (7 elements, odd) using `solve12` (peel+halve / prefix-match only, no
TAIL-SNIP available). I directly computed:
```
solve12(U)     = 0.3433   →  0.1588+0.3433 = 0.5021  (matches Candidate 3's
                                                        losing value exactly)
solve_full(U)  = 0.3412   →  0.1588+0.3412 = 0.5000  (beats target)
```
i.e. the *only* missing ingredient is letting the **7-element residual `U`
itself get access to a TAIL-SNIP move** (since `|U|=7` is odd, exactly the
regime TAIL-SNIP is designed for). Candidate 3 deliberately routes Strategy
2's leftover recursion through `solve12` (not `solve_full`) specifically to
avoid re-triggering TAIL-SNIP recursively — that design choice is precisely
what causes the `m=8` miss. **No Hall's-theorem-style non-contiguous
matching is needed for this specific witness.**

### Task 1 answer — exact coordinates and winning move
- Witness: `A = (2117,1588,1410,1319,1232,881,748,705)/10000` (Σ=1).
- Winning move: match `p_1` against **only `p_2`** (ordinary maximal
  PARTIAL-DOM prefix, `j=1`), 1 mark, residual `r=p_1-p_2=529/10000`;
  leftover `U = {p_3,...,p_8,r}` (7 elements). Then apply **TAIL-SNIP to
  `U`** (split its smallest element `p_8=705/10000` into two copies of
  `705/20000`, since `|U|=7` is odd) before continuing with the
  peel/prefix-match menu on the resulting 8-element list. Total value
  `= p_2 + solve_full(U) = 0.1588+0.3412 = 0.5 < target≈0.501961`.
  Margin ≈ `+0.00196`, exact-rational-verified.

### Task 2 — general principle, and a genuine obstruction found

The "general principle" is not subset-sum-near-a-threshold (Hall's theorem
was a red herring here) — it is **recursive availability of the
parity-fixing TAIL-SNIP move inside the recursion, not just at the top
level.** I tested the direct fix — reroute Strategy 2's (and only Strategy
2's) leftover recursion through `solve_full` instead of `solve12` — and it:
- **Closes the `m=8` witness** (value 0.5, margin +0.00196, exact).
- **BUT is not well-founded as an unrestricted recursive definition.**
  Concretely: `solve_full(A)` [n odd] can invoke TAIL-SNIP to get `newA`
  (size `n+1`), then `solve12(newA)`'s own Strategy-1 branch peels the new
  top element and calls `solve_full` again on a tail of size exactly `n`
  (the *same* size as the pre-snip instance, just a different composition)
  — which can again be odd and again invoke TAIL-SNIP, and so on. I
  verified this is a **genuine, not merely slow, non-termination**: on a
  random `m=9` Case-C instance, the unrestricted version exceeded 2,000,000
  recursive calls in 18s without terminating (and with memoization added,
  timed out at 120s with no termination) — this is exactly the "infinite
  recursion trap" the sibling explorer flagged as a risk, and I've now
  confirmed it is real, not hypothetical, for this specific fix.
- **A bounded version is safe and still closes m=8.** Threading an explicit
  integer `budget` parameter (decremented only when TAIL-SNIP fires, initial
  budget as small as **`budget=1`**, i.e. "the leftover from a Strategy-2
  match gets at most one extra TAIL-SNIP anywhere in its own recursion")
  terminates cleanly (memoized, `m` up to 12 in ~2s, `523` random Case-C
  trials, 0 violations) and **still closes the `m=8` witness exactly**
  (value 0.5, same as unbounded). Also re-verified 0 violations on the
  known hard-witness families: the `m=5` witness (`A=(1826,1563,1520,1514,
  765)/7188`, margin `+0.0161`) and the near-uniform-tail family `p_1=0.499`
  for `m=4..20` (all positive, decaying toward 0 as before, e.g. `m=20`:
  `+4.77e-7`, matching the sibling's Candidate 3 numbers almost exactly —
  budget-1 has essentially the same asymptotic behavior on this family).

This is only a **budget-1, single random-sample stress test**, not an
adversarial optimizer search (I did not have time this round to rerun
`differential_evolution` against budget-1 Candidate 3 the way the sibling
did against plain Candidate 3) — so it is **not yet certified free of its
own counterexample**, but it is a much stronger, still-cheap candidate than
plain Candidate 3, and the mechanism (bounded nested TAIL-SNIP budget, not
subset matching) is now precisely identified.

### Task 3 — tractability verdict

**Tractable, and simpler than the non-contiguous-subset-matching route the
dispatch was scouting.** The concrete recommendation for the outliner/
builder:
1. **Drop the "arbitrary non-contiguous subset match" idea as the fix for
   `m=8`** — brute-force search over all 127 subsets confirms the ordinary
   contiguous maximal PARTIAL-DOM prefix is already optimal there; a
   non-prefix subset gains nothing on this witness. (This directly
   contradicts the sibling's tentative diagnosis "the needed move is NOT
   contiguous-prefix matching" — that diagnosis was based on candidate-move
   testing that never tried "let the leftover itself use TAIL-SNIP", only
   "try more prefixes for the *top-level* match", which is a different
   knob.)
2. **The real 4th move is: let PARTIAL-DOM's leftover recurse via the full
   `solve_full` menu (peel/prefix/TAIL-SNIP), not the restricted `solve12`
   menu** — but this must be **budget-capped** (a small fixed integer, e.g.
   `budget=1` suffices on all tested witnesses) to avoid the genuine
   non-termination I demonstrated for the unrestricted version. A proof
   would need to formalize this as: "strong induction on `m`, where the
   induction hypothesis for the leftover sub-instance is invoked with one
   fewer unit of `TAIL-SNIP budget` than the parent, and budget `B=O(1)`
   (or `B` growing very slowly, e.g. `O(log m)`) suffices" — this converts
   the open question from "does a good subset/matching selection rule
   exist" (a hard existence/Hall's-theorem-flavored question) to "how much
   TAIL-SNIP budget is provably always enough" (a bounded, checkable
   question, much closer to what THRESHOLD-REDUCTION / BLOCK-RECURSE's
   existing budget-telescoping arguments already handle).
3. **Not yet proven that any fixed constant budget is universal** — this is
   the next honest gap: does `budget=1` (or `2`, or some `f(m)`) suffice for
   *every* Case-C configuration at every `m`, or does the adversarial search
   find a new counterexample requiring more nested snips? This needs the
   same `differential_evolution`-style adversarial search the sibling ran,
   applied to the budget-1 (and budget-2) menu, before it can be trusted as
   the closing move.

### Cheap-kill candidates
- The subset-search itself is a useful cheap kill: for any future
  candidate counterexample, brute-forcing all `2^{m-1}` subsets (feasible
  up to `m≈15`, exact `Fraction`) against `solve_full` is a fast way to
  distinguish "needs non-contiguous matching" from "needs deeper
  recursive access to an existing move" — worth automating as a standard
  diagnostic before proposing new move types.
- A simple structural sanity check for future budget-schemes: verify the
  measure `2·|leftover| + [uses-TAIL-SNIP-again]` (or equivalent) strictly
  decreases along any recursive chain before trusting a "let X recurse via
  the fuller menu" fix — the naive unrestricted version looks well-founded
  at first glance (leftover is always strictly smaller than its immediate
  parent) but is NOT globally well-founded once TAIL-SNIP's size-increasing
  step is allowed to re-enter the same recursive slot; this is a subtle,
  easy-to-miss trap and should be flagged explicitly to whichever builder
  attempts this route.

### Knowledge-base / lemma entries used
- `lemmas/pair-value.md` (Lemma PAIR-VALUE, SUBSET-DOM corollary) — used
  for the brute-force subset search (guarantees the value identity for any
  subset match, contiguous or not, so the brute force is exact and valid).
- `lemmas/block-recurse.md` (Lemma BLOCK-RECURSE) — the contiguous-prefix
  special case; confirms Strategy 2's own maximal-prefix match is what the
  brute force also finds optimal here, so BLOCK-RECURSE's own machinery
  (not a new SUBSET-DOM machinery) is the right lens.
- `lemmas/split-and-tail-snip.md` (Lemma TAIL-SNIP) — the move whose
  *recursive/nested availability*, not the subset-matching mechanism, is
  the actual missing ingredient.
- Hall's marriage theorem (knowledge_base.md) — **found NOT to be the
  relevant tool for this specific gap** after direct investigation; flag
  this to the outliner so effort isn't spent formalizing a Hall's-theorem
  argument that this witness doesn't actually need. (It may still be
  relevant for *other*, not-yet-found counterexamples that do need genuine
  simultaneous multi-donor non-contiguous matching — this round's evidence
  only rules it out for the one known witness.)

### Analogous past problems (crux corpus)
Not queried this round — dispatch scope was numerical/structural
diagnosis of the specific `m=8` counterexample rather than a fresh corpus
search, and the finding (bounded-budget recursive-move availability, not
subset-sum matching) does not obviously map to a "Hall's theorem" or
"subset-sum matching" corpus subtopic as originally hypothesized; a future
round should instead search the corpus for **"bounded resource / budget
threading through a strong induction to guarantee termination"**
(recursion-with-fuel arguments) if a crux analogue is wanted — this is a
different search target than what the dispatch specified, flagging for the
outliner rather than guessing.

### Prior progress
`universal-adversary-strategy`'s Candidate 3 (adaptive 3-way menu, per the
sibling report) is the best certified-numerically starting point but has
the exact, reproduced `m=8` counterexample above. This round's contribution:
(a) the `m=8` witness needs no non-contiguous subset match — a brute-force
check rules that out; (b) the actual fix is "let PARTIAL-DOM's leftover use
`solve_full` (with TAIL-SNIP) instead of `solve12`"; (c) this fix is
unsound without a budget cap — demonstrated genuine non-termination
(millions of calls, no termination) for the unrestricted version on an
`m=9` instance; (d) a `budget=1`-capped version is well-founded, terminates
fast, closes the `m=8` witness, and passes 523 random Case-C trials
(`m=4..12`), the near-uniform-tail family (`m=4..20`), and the `m=5` hard
witness — but has **not** been adversarially stress-tested
(`differential_evolution`-style) the way the sibling tested plain
Candidate 3, so it is not yet certified counterexample-free.

### Dead ends (do not retry without modification)
- "Non-contiguous subset match as the fix for the `m=8` witness" —
  exhaustively refuted for this specific witness: brute force over all 127
  tail subsets shows the ordinary contiguous maximal-prefix match is
  already optimal; the gap is a recursion-depth/move-availability issue,
  not a matching-selection issue. (Refines, does not contradict, the
  sibling's honest uncertainty — they had not yet isolated the true cause.)
- "Let Strategy 2's leftover recurse via `solve_full` unconditionally, no
  budget cap" — genuinely non-terminating (confirmed: 2,000,000+ calls,
  18s+, no termination, on a random `m=9` instance; also timed out with
  memoization added). Do not propose this as a proof mechanism without a
  budget/fuel parameter.

### Small-case / intuition notes (conjectural, not proven)
- Conjecture (not proven): a small, possibly `O(1)` (not growing with `m`)
  TAIL-SNIP budget threaded through the PARTIAL-DOM leftover recursion is
  universally sufficient for Case C. Evidence so far: `budget=1` suffices
  on every tested witness including the one genuine `m=8` counterexample to
  the budget-0 (plain Candidate 3) menu. This is evidence from a modest
  random sample plus 3 known hard witnesses, not an adversarial search —
  treat as a promising but unverified conjecture, the natural next thing
  for a builder or another explorer to stress-test with
  `differential_evolution` before writing a proof outline around it.
- If a constant/slowly-growing budget does turn out to be universal, the
  proof shape becomes a clean strong induction (paralleling
  THRESHOLD-REDUCTION / BLOCK-RECURSE's existing budget-telescoping
  arguments) rather than requiring new Hall's-theorem machinery — this
  would be a significantly easier proof target than the sibling's
  "non-contiguous subset selection rule" framing suggested.
