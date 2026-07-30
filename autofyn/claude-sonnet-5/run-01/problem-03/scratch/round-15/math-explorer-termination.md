# Scouting report: solve2/m=8 termination diagnosis (round 15)

## What was checked
Read `results/imo-2026-03/current.md` (round 14 review), the full
`approaches/universal-adversary-strategy.md` (round-12 through round-14
sections), `/tmp/round-14/proof-builder-universal-adversary-strategy.md`,
`/tmp/round-14/proof-reviewer.md`, and the round-14/round-13 scratch
scripts (`/tmp/round-14/scratch/gate*.py`, `/tmp/round-13/*.py`). No
`solve2` source script survives in `/tmp` (the builder's and reviewer's
own `/tmp/solve2.py` / independent reimplementation are not retained;
only their prose descriptions and the round-14 `case-c-slack-covering`
gate scripts, which solve a *different* sub-problem, are present). This
report is therefore based on the two independent written accounts (builder
+ reviewer, round 14) of what `solve2` does and where it stalled, not on
rerunning the code myself — flagged so it isn't mistaken for a fresh
empirical result.

## Diagnosis: combinatorial blow-up, not a bug, not simple missing memoization

**It is not infinite recursion.** Well-foundedness of `solve2` — the
`(marks,|A|)` lexicographic measure, `marks` primary — was independently
re-derived twice (builder and reviewer, round 14) after both hit and
correctly excluded the one identified non-terminating sub-case (Move 2 with
`|S|=1, r=0`, a literal no-op that must be routed through Move 0 instead).
Once that exclusion is in place, termination is proven, not just observed.
The `m=8` stall is a **runtime/complexity** failure, not a correctness
failure of the recursion's design.

**Root cause: Move 2 ("subset-match") is currently formalized as
"exhaustively try every nonempty subset `S` of the current tail as a
donor match for `p_1`."** This was forced by round 13/14's finding that
the earlier *contiguous-prefix-only* Move 2 is provably insufficient (the
`T=(0.20,0.15,0.12,0.08)` witness needs the non-contiguous match `{0.12,
0.08}`, skipping `0.15`). Fixing that correctness gap by widening to "all
`2^{|tail|}-1` subsets" reintroduces exactly the exponential blow-up
round 12's own explorer had already hit and deliberately avoided: recall
`math-explorer-subsetmatch` (round 12) found that letting a PARTIAL-DOM
leftover recurse through the *unrestricted* full menu is genuinely
non-terminating in reasonable time — "2M+ recursive calls / 18s+ ... even
with memoization added" on a random `m=9` instance — and it was only
budget-capping the *nested TAIL-SNIP* count (not the subset enumeration
itself) that made round 12's Candidate 5 fast. Round 14's `solve2`
re-widens the subset search (needed for correctness on the m=4
non-contiguous witness) without re-adding an analogous cap on subset
*enumeration cost*, so at `m=8` the top-level call alone considers up to
`2^7-1=127` Move-2 branches, each of which recurses into a smaller
instance that itself re-enumerates up to `2^{k}-1` subsets of its own
tail, compounding across up to `marks=7` recursion levels. This gives
roughly `2^{7}\cdot2^{6}\cdots` total leaf work in the worst case (well
into the 10^7–10^8+ range even before accounting for the `Fraction`
arithmetic overhead per node), which comfortably explains a >5 minute
stall in pure Python with no result — a genuine, expected complexity
class problem given the current move formalization, not a stack overflow
or off-by-one causing true divergence.

**Memoization is not the fix, and this matters for planning round 15's
effort.** The already-recorded evidence (round 12's "even with
memoization added" note) and the structure of the problem both point the
same way: on a witness with generic, pairwise-distinct real (or
high-denominator rational) values, different Move-2 subset choices at the
top level produce genuinely *different* leftover arrays with no shared
substructure — there is essentially no repeated subproblem for a
`(sorted-tuple, marks)`-keyed cache to catch. The blow-up is branching
factor, not redundant recomputation, so memoization alone would not
rescue `m=8` to a tractable runtime; a builder who tries adding an
`lru_cache` and reports "still doesn't terminate" should not be treated
as having found a new problem — that is the expected outcome given the
above.

## What would actually fix the numeric check (if it's still wanted)

Three concrete options, in order of how much they change what's being
verified:

1. **Branch-and-bound / early-exit, not exhaustive optimization.** The
   claim actually needed is an *upper bound* (`solve2(A,marks) ≤
   c(m-1)Σ(A)` on this witness), not the exact game value. A DFS that
   returns as soon as any branch's telescoped value is `≤` the known
   target — without exploring the other ~126 subsets at that level — turns
   a search for the true minimum into a search for *a* certificate, which
   is far cheaper if a good move is tried early (e.g. try the maximal
   contiguous prefix match first, since round 12 already showed a
   structured, non-exhaustive strategy closes `m=8` exactly).
2. **Reuse round 12's already-fast, already-verified concrete strategy
   for this one witness**, instead of routing it through the newly
   generalized any-subset `solve2`. Round 12's Candidate 5 (contiguous
   PARTIAL-DOM prefix + a `budget`-capped *nested* TAIL-SNIP allowance,
   *not* an exhaustive subset search) was independently confirmed to
   close this exact `m=8` witness (margin `\approx-1.53\times10^{-4}`
   fixed to `\le0`) and ran fast (523 random trials `m=4..12` completed).
   The round-14 blow-up comes specifically from the newer *general*
   Move-2 menu, which this witness does not actually need — the winning
   subset for `m=8` was already shown (`math-explorer-subsetmatch`,
   round 12) to be the ordinary contiguous prefix, not a non-contiguous
   one. So the m=8 regression check can be re-run cheaply by plugging the
   already-certified round-12 construction into this witness directly,
   without going through the newly-generalized (and here unnecessary)
   any-subset search.
3. Meet-in-the-middle subset-sum indexing (`O(2^{k/2})` instead of
   `O(2^k)` per level) would help genuinely, but is over-engineering for
   what's actually needed here — see recommendation below.

## Sanity check: does the *mathematical* claim need the full m=8 instance at all?

**No — and this is the more important finding.** The m=8 witness's
historical role was to refute the *older*, contiguous-prefix-only Move-2
menu (Candidate 3): it showed that menu alone is insufficient at `m=8`.
But round 13/14 already found and certified a **strictly smaller**
witness exhibiting the *same* underlying defect one level up the
severity scale — `T=(0.20,0.15,0.12,0.08)`, only `m=4`, tail size 3
(`2^3=8` subsets, trivially enumerable) — where even the *contiguous*
match is insufficient and a genuine **non-contiguous** subset match is
required (`{0.12,0.08}`, skipping `0.15`) to reach the true optimum
`Σ/2`. This is a strictly sharper structural counterexample than m=8 ever
was (m=8's winning move turned out to be the ordinary contiguous prefix,
per `math-explorer-subsetmatch`'s brute-force check over all 127 tail
subsets — the m=8 witness never actually needed non-contiguous matching
at all, only the nested-TAIL-SNIP-budget fix). So:

- The **general subset-match existence question (Lemma SLACK-COVER)** —
  the field's actual sole open gap — is already witnessed, in its
  sharpest known form, by the small, fully-tractable `m=4` instance. No
  additional information is gained by getting `solve2` to terminate on
  the `m=8` instance specifically; it would only reconfirm a fact (the
  nested-TAIL-SNIP-budget fix suffices there) that round 12 already
  established with a cheaper, structured, non-exhaustive strategy.
- Conversely, since Lemma SLACK-COVER is a **universally quantified**
  claim (existence of a good subset match for *every* `A`, every `m`),
  no finite computation — on `m=4`, `m=8`, or any other single witness —
  can substitute for a proof. Getting the brute-force `solve2` to run
  faster at `m=8` would be a nice-to-have regression check, not progress
  toward closing the actual gap.

## Recommendation for round 15

1. **Do not spend builder/reviewer effort making the exhaustive-subset
   `solve2` scale to `m=8`.** It is expected to be slow (branching, not a
   bug), memoization will not rescue it, and even a fast run would only
   re-confirm what round 12 already established by a cheaper route.
2. If a quick regression re-check is wanted for hygiene, plug round 12's
   already-certified structured strategy (contiguous-prefix PARTIAL-DOM +
   budget-1-capped nested TAIL-SNIP) directly into the `m=8` witness
   `A≈(0.2117,0.1588,0.1410,0.1319,0.1232,0.0881,0.0748,0.0705)` — this is
   cheap (no exhaustive subset search) and was already shown to close it
   exactly in round 12.
3. **Redirect all real effort to proving Lemma SLACK-COVER itself**
   (the joint covering+recursive-value existence statement, as the
   round-14 write-up correctly re-scoped it) using the small, tractable
   `m=4` witness (`T=(0.20,0.15,0.12,0.08)`) as the concrete test case to
   build and check any candidate existence argument against — it already
   contains the full structural difficulty (need for a genuine
   non-contiguous match) at a size small enough for exact hand
   computation, Hall's-theorem-style bipartite reasoning, or exhaustive
   `2^3`-subset checking, with no engineering barrier at all.

## Files referenced
- `/home/agentuser/repo/results/imo-2026-03/current.md`
- `/home/agentuser/repo/results/imo-2026-03/approaches/universal-adversary-strategy.md`
  (round-12 plan section ~line 2464 for the m=8 witness statement and
  `math-explorer-subsetmatch`'s diagnosis; round-13/14 sections for the
  `T=(0.20,0.15,0.12,0.08)` witness and the m=8-untested note)
- `/tmp/round-14/proof-builder-universal-adversary-strategy.md`
- `/tmp/round-14/proof-reviewer.md`
- `/tmp/round-14/scratch/gate*.py` (round-14 `case-c-slack-covering`
  scripts — a different sub-problem's gate, referenced only for context;
  none of these implement `solve2` itself)
