## imo-2026-03 (lens: open upper-bound gap — arbitrary-configuration strategy for Xiang Yu)

### Summary of the key finding
Numeric experiments (exact scripts below) show that **adding one more move —
a free "peeling" step — to the certified Lemma DOM + Lemma HALVE toolkit, used
recursively, empirically closes the general-`n` upper bound** for every `n`
tested (2, 3, 4), including all previously-recorded counterexamples to the
static-threshold rules. This is strong (but still numerical, not proved)
evidence for a genuinely new lemma the outliner should add to the induction.

### (a) Numeric experiments: what Xiang Yu's true optimal response looks like
Using a continuous optimizer (`scipy.optimize.minimize`, Nelder-Mead, over all
ways to distribute `n` marks among the `m` current pieces and all continuous
split positions, many random restarts) to find the **true** optimal Xiang-Yu
response for small adversarial 3-piece configurations at `n=2`:

- `A=(0.9862,0.0081,0.0057)`: optimal uses **1 mark, all on `p1`** (simple
  halving of the dominant piece), `oddrank≈0.5012 < c(2)=4/7≈0.5714`.
- `A=(0.5,0.3,0.2)`: optimal uses 2 marks both on `p1` (a 2-way split of
  `p1` matching Lemma DOM), `oddrank=0.5`.
- **`A=(0.398,0.398,0.204)` (near-tied top two pieces) — the pivotal case.**
  True optimum uses **only 1 mark, spent entirely on `p3` (halving the
  *smallest* piece), leaving `p1` and `p2` completely untouched** and one
  mark unused: `oddrank=0.5003 < c(2)`. Neither Lemma DOM nor Lemma HALVE
  (both of which only ever touch `p1`) can express this move — this is a
  genuinely different mechanism.

Diagnosing this: since `p1≈p2` and both exceed `p3`, ranks 1 (`p1`, odd) and
2 (`p2`, even) are **locked in regardless of what Xiang Yu does to the tail**
(as long as refinements of the tail stay `≤ p2`), so `oddrank(A) = p1 +
oddrank(tail)` for free — no marks needed to fix the top pair. Xiang Yu's
entire remaining budget should then be spent optimally **inside the tail**,
i.e. recursively solving the *same kind of sub-problem* on `tail` (a smaller
Liu-Bang-like instance of total mass `S=Σ(tail)`) with the leftover marks.
This "peel the dominant pair, recurse into the tail with full budget"
mechanism is the mechanism round 2's numerics were pointing at but had not
isolated.

### (b) Does a clean recursive rule reproduce the bound? Yes — a 3-move rule.
I formalized a **PEEL lemma** (new, not yet in `lemmas/`):

> **Lemma PEEL (candidate).** If `A=(p_1≥p_2≥⋯)` with `p_2 ≥ max(tail)`
> where `tail=(p_3,p_4,\ldots)`, then for *any* refinement `T'` of `tail`
> (using any number of marks, not touching `p_1,p_2`),
> `oddrank({p_1,p_2}∪T') = p_1 + oddrank(T')` — **using zero marks**.
> (Proof sketch, same rank-shift style as HALVE: `p_1,p_2` occupy global
> ranks 1,2 unconditionally since both dominate every element of `T'`; rank 1
> is odd → `p_1`; rank 2 is even → excluded; `T'`'s own ranks shift by 2,
> preserving parity.)

I then built a **discrete recursive search** over exactly three move types at
each step — (i) Lemma DOM with `k=1..budget` marks, (ii) Lemma HALVE (halve
`p_1`, 1 mark), (iii) Lemma PEEL (free, whenever `p_2≥max(tail)`, recurse into
`tail` with the *same* remaining budget) — computing, via memoized recursion,
the best achievable `oddrank` over all move sequences drawn from just these
three primitives (script: `/tmp/round-3/xy_experiment2.py`).

**Random testing:** 3000 random configurations each for `n=2` and `n=3`
(power-law-skewed random simplex points, sizes up to `n+2` pieces): worst
ratio found was `0.993` (`n=2`) and `0.985` (`n=3`) — i.e. **no violation of
`≤ c(n)` found**, and the three-move set clears every one of the concrete
adversarial configurations round 2 recorded as counterexamples to the
*static-threshold* rules (e.g. `(0.9862,0.0073,0.0163)`-type gives `0.5036 <
c(2)`, and the tied-top-pair case above gives `0.5003 < c(2)`).

**Adversarial search (stronger check):** running `scipy.optimize.minimize`
directly on Liu Bang's simplex point to *maximize* the value the discrete
DOM+HALVE+PEEL recursion achieves, for `n=2,3,4`, the adversarial optimizer
converges (from many random restarts, up to numerical precision ~1e-4) to
**exactly the certified geometric configuration `A_n`**, and the achieved
value equals `c(n)` almost exactly (ratios `1.0000001`, `0.9999999`,
`0.9998864` — within optimizer tolerance of exactly 1, never above):
```
n=2: A ≈ (0.5714, 0.2857, 0.1429) = (4/7,2/7,1/7) = A_2,  value ≈ c(2)
n=3: A ≈ (0.5333, 0.2667, 0.1333, 0.0667) = A_3,          value ≈ c(3)
n=4: A ≈ (0.5162, 0.2580, 0.1289, 0.0645, 0.0323) ≈ A_4,  value ≈ c(4)
```
This is exactly the expected tightness (the certified geometric lower-bound
witness), which is a strong consistency check: the three-move recursive
strategy appears to be **exactly tight**, not just sufficient with slack —
consistent with it being the *actual* optimal Xiang-Yu strategy, not merely
an adequate one.

**Conclusion (numeric/conjectural only):** DOM + HALVE + PEEL, applied
recursively (branch-and-take-min at each step), appears sufficient to prove
the general upper bound `max_A min_B oddrank(B) ≤ c(n)` for every `n`. This
has NOT been proved — only checked numerically to high confidence for
`n=2,3,4`.

### (c) Technique that fits proving this in general
The natural home for this is **strong induction, but on the wrong variable
for a naive n-only induction**: PEEL consumes **zero marks** but reduces the
**piece count** `m` by 2 (removing `p_1,p_2` from consideration, recursing
into `tail`), whereas DOM/HALVE consume marks but don't necessarily shrink
`m` by much. A proof will need **double induction / induction on a combined
measure** (e.g. on `m + budget`, or nested induction: outer on `n`, inner on
`m` for fixed budget, since PEEL can chain many times for free before any
marks are spent) — this is exactly `knowledge_base.md`'s **"Induction: pick
the right variable to induct on"** (`## General Proof Methods`) and
**"Invariants & monovariants"** entries, applied to a *game value* rather
than a single quantity — i.e. a **minimax/dynamic-programming induction**
where the state is `(configuration, remaining budget)` and the recursion is
exactly the one implemented numerically above. This is the same flavor as
the crux move in `aimo-0236` (a two-phase invariant, self-restoring because
one player's move fixes a valuation while the other's degrades a potential)
and the recursive-halving-by-valuation crux in `aimo-0225` — both are
"track a discrete measure that decreases under a forced recursive move"
patterns, structurally analogous to the `(m,budget)` recursion here, though
neither problem is a content-match.

### (d) A genuinely different top-level framing (not just this gap)
Worth flagging to the outliner as an alternative, further-out idea (not
pursued here): reformulate the whole minimax as a statement about **the
sorted vector of "weights" `2^{-i}` implicit in `oddrank`'s pairing
structure**, i.e. treat Xiang Yu's problem as **exactly the "sum of minima
over a pairing" problem** (already noted in `claiming-phase-value.md`'s Fact
0), and prove the upper bound by directly bounding, for *any* `A`, the
**best achievable pairing-with-refinement** value via a **greedy/matching
argument on the multiset of dyadic "slots"** `1, 1/2, 1/4, \ldots` rather
than via explicit case-by-case moves on `p_1`. This reframes "which piece to
split" as "which dyadic slot is under- or over-supplied," and might yield a
cleaner one-shot potential-function proof instead of the case-recursion
above — flagged as a direction, not attempted (would need its own approach
slug; overlaps with `equalization-potential-bound`, which the current.md
notes was a dead end for the wrong reason — its "impossibility" argument
assumed the still-open lower bound, so this direction is not actually
closed and could be revisited with the PEEL-based recursive structure in
mind).

### Candidate technique(s)
Minimax dynamic-programming induction on the combined state `(piece-count m,
remaining budget r)`, using three certified/near-certified moves (DOM,
HALVE, and the new candidate PEEL) as the only recursive steps, proved
sufficient via a two-index strong induction. Secondary: potential-function /
pairing (dyadic slot) reformulation as an alternative full framing.

### Cheap-kill candidates
- None new beyond what's certified. (Parity/size arguments don't obviously
  bound this LP-flavored minimax; already tried and shelved per
  `interior-point-linear-obstruction.md`.)

### Knowledge-base entries to use
- `## General Proof Methods` — **Induction** ("pick the right variable to
  induct on"; induction loading / strengthening the hypothesis) — directly
  relevant to the `(m, budget)` double-induction needed here.
- `## General Proof Methods` — **Invariants & monovariants** — the PEEL
  move's "locked-in top pair" is exactly an invariant-preservation argument.
- (Existing, already used) claiming-phase value formula, generalized
  domination/halving lemmas.

### Analogous past problems (cruxes)
- `aimo-0117` (`combinatorics`/`games-and-strategy`) — "assign played values
  as a two-sided geometric (dyadic) sequence so the largest value strictly
  exceeds the sum of all others" and "defer committing the extreme value,
  maintaining an invariant that the max sits in a fixed slot." Analogous in
  *spirit* (dyadic/geometric domination is the same mechanism behind Lemma
  DOM and the geometric witness `A_n`), but the underlying game (stone
  placement into two boxes) is structurally different — a hint for the
  domination mechanism, not a template for the recursion itself.
- `aimo-0236` (`number_theory`/`games-and-strategy`, listed under NT but
  game-theoretic in nature) — two-phase invariant, self-restoring because
  the first mover fixes a valuation while the opponent's forced move
  degrades a potential; structurally the closest analogue to the
  `(m,budget)` recursive-invariant proof shape needed here, though the
  content (2-adic valuation token game) does not transfer directly.
- `aimo-0225` — game value determined by recursion on a halving 2-adic
  valuation, flipping status each halving step — same "value determined by
  a halving recursion" shape as Lemma HALVE, worth a structural look if the
  outliner wants a valuation-style formalization of the recursion depth, but
  not a direct match.
- Overall: **no crux is a genuine content-match** for this specific minimax
  claiming-game problem; the above are technique analogues only, to be
  re-derived from scratch as the repo's rules require.

### Prior progress
- Lemma DOM and Lemma HALVE (both certified, `lemmas/generalized-domination-and-halving.md`)
  fully close `n=1` for every configuration and settle the `S≤p_1≤c(n)`
  sub-case for all `n`.
- **NEW this round (not yet certified — numeric only): Lemma PEEL**
  (see (b) above) — the missing third move; together with DOM+HALVE, a
  discrete recursive search using only these three moves finds **no
  violation of `oddrank≤c(n)` in 3000+ random trials for `n=2,3` and in
  adversarial (optimizer-driven) search for `n=2,3,4`**, with the
  adversarial optimum converging to the known geometric configuration `A_n`
  exactly. This is the most concrete positive lead surfaced so far for the
  general upper bound.

### Dead ends (do not retry)
- Confirmed (re-verified, not just trusted): all three dead ends recorded in
  `universal-adversary-strategy.md` (fixed-decrement Lemma J; repeated
  "halve the global max" with no tail-targeting; two-way `p_1≷2S` static
  switch) genuinely fail — I re-ran the tied-top-pair-style and
  small-third-piece adversarial configs from that file and confirmed the
  static-threshold rules cannot express the required "leave `p_1,p_2`
  untouched, spend the whole budget on the tail" move. However, **the
  general upper-bound gap is NOT a dead end** — the PEEL addition above
  appears (numerically) to resolve exactly the failure mode that killed the
  static-threshold rules; the outliner should treat "DOM+HALVE alone
  insufficient" as narrowing the mechanism, not as evidence the whole
  approach direction is wrong.

### Small-case / intuition notes (all labeled conjecture — numeric only)
- Conjecture: Lemma PEEL (`p_2≥max(tail) ⟹ oddrank(A)=p_1+oddrank(tail)`,
  zero marks) is a true, provable identity (same proof style as HALVE/DOM,
  likely a direct corollary of the same rank-shift argument — should be easy
  to prove rigorously, probably before HALVE/DOM in difficulty).
- Conjecture: the discrete recursive search over {DOM, HALVE, PEEL} exactly
  achieves `c(n)` at the geometric configuration and stays `≤c(n)` for every
  configuration tested at `n=2,3,4` (3000+ random trials + adversarial
  optimizer search, no counterexample found). If provable by induction on
  `(m,budget)`, this closes the entire remaining upper-bound gap.
- Conjecture (weaker, structural): the correct general induction variable is
  NOT `n` alone but a pair `(m, r)` — piece count and remaining budget —
  because PEEL changes `m` without consuming `r`. Any induction hypothesis
  the outliner writes should explicitly carry both.
