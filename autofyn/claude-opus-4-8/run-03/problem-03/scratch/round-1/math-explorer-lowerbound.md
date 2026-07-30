## imo-2026-03 — lens: Liu Bang's guarantee (lower bound c(n) ≥ ...)

### Verified reduction (the claiming sub-game)
Given the final multiset of pieces (fixed once all marks are placed), the alternating
"claim any unclaimed piece" game with both players maximizing their own total is a
classic *identical-valuation greedy* game: **both players' optimal strategy is to
always claim the currently-largest unclaimed piece.** Proof sketch (exchange
argument, not written out): by backward induction on the number of remaining pieces,
if the mover takes anything other than the current max, the opponent (playing
optimally) will take that max next turn regardless, so deviating cannot help and can
only cost the mover the chance to bank the max now. Hence with pieces sorted
descending L1 ≥ L2 ≥ … ≥ Lm, **Liu Bang's total = L1+L3+L5+…** (odd ranks),
Xiang Yu's = L2+L4+…. This reduction is safe to hand to the outliner as an
established lemma, not a conjecture — it only needs the standard exchange-argument
write-up, no new idea.

Consequence: the whole game reduces to a **pure sizing/adversarial-splitting
problem**: Liu Bang picks a partition of 1 into a+1 parts (a ≤ n marks — the
*order* of his pieces along the stick is irrelevant, only the multiset of lengths
matters, since Xiang Yu's marks act piece-locally). Xiang Yu then, seeing this
multiset, may perform ≤ n split operations (each op: pick a current piece, replace
it by two sub-pieces summing to the same length) to minimize the final odd-rank sum.
Xiang Yu need not use all n marks, and need not split a given piece only once (he
can mark k points inside one piece to shatter it into k+1 parts, "spending" k of
his marks there).

### Numerical determination of the answer (conjecture, computed not proved)
I brute-force computed the exact 2-player value (Liu Bang partition vs. Xiang Yu's
best splitting response, both searched numerically over all cut-allocations and
grid-refined split ratios) for n=1 and n=2, and a coarser check for n=3.

- **n=1:** optimal Liu Bang mark is at **1/3** (not 1/2!), giving pieces {1/3, 2/3}.
  Xiang Yu's best response (either not cutting, or bisecting the 2/3-piece into two
  1/3's) yields Liu Bang exactly **2/3**. Numerically confirmed as the max-min value
  to high precision (searched over all p, all Xiang Yu responses).
- **n=2:** optimal Liu Bang partition found numerically is **{1/7, 2/7, 4/7}**
  (ratio 1:2:4), giving value **4/7 ≈ 0.5714**, confirmed to be a local (and by
  broad grid search, global) max over partitions, robust to increasing the search
  resolution (coarser grids spuriously suggested higher values elsewhere but
  disappeared under refinement — a resolution artifact, not real).
- **n=3:** a coarse check of the **{1/15, 2/15, 4/15, 8/15}** partition (ratio
  1:2:4:8) gave a value ≥ 0.54 against a deliberately crude Xiang-Yu response
  search (insufficient resolution to pin down the true minimax exactly), consistent
  with but not confirming 8/15 ≈ 0.5333.

**Conjectured closed form: c(n) = 2ⁿ / (2ⁿ⁺¹ − 1).**
Matches n=1 (2/3) and n=2 (4/7) exactly; n=3 numeric is consistent (not yet a tight
confirmation). This is the number the outliner should target for the lower bound
(and check against whatever the upper-bound explorer's Xiang Yu construction gives —
they must match for the answer to be tight).

### Candidate mechanism (superincreasing partition) — sketch only, not a proof
Liu Bang's construction: mark points so his own n+1 pieces have sizes proportional
to **1, 2, 4, …, 2ⁿ** (i.e., length 2ⁱ/(2ⁿ⁺¹−1) for i=0,…,n). Key structural
property: this is a **superincreasing sequence** — each piece is strictly larger
than the sum of all strictly smaller original pieces (2ᵏ > 2⁰+…+2^{k−1} = 2ᵏ−1).
This is the same flavor of fact used in Zeckendorf/greedy-representation and
"weighing with binary weights" arguments — worth checking `knowledge_base.md`'s
general "constructive/incremental" and pigeonhole entries, though nothing there is
an exact match; this may need a fresh argument, likely by strong induction on n
(peel off the largest piece and reduce to the n−1 problem on the rest), or an
explicit adversary-argument potential function tracking the invariant "the sum of
all pieces at least as large as the current one, plus the current one, dominates
some target." I did NOT work out how superincreasing-ness forces the odd-rank sum
to be ≥ 2ⁿ/(2ⁿ⁺¹−1) against all of Xiang Yu's ≤ n splits — that derivation is the
real gap and is exactly the outliner's job to close (likely by induction on n,
peeling the top piece).

### Cheap-kill / structural observations
- **Order along the stick is irrelevant** — only the multiset of piece lengths from
  each player's marks matters (since claiming is by piece, and a split only affects
  the split piece). This collapses "choose n points on [0,1]" to "choose a partition
  of 1 into ≤ n+1 parts," a big simplification the outliner should state explicitly
  and use.
- **Parity / "does Xiang Yu want more or fewer total pieces?" is NOT a clean
  invariant** — I initially conjectured Xiang Yu always wants total piece count even
  (so ranks split exactly 50/50), but the n=1 exact computation refutes this: with
  m=2 (already even) Xiang Yu still can't beat 2/3, i.e. even parity does not
  force exactly 1/2 — a "dead end" worth flagging so nobody re-derives a false
  parity lemma. The real driver is the superincreasing-size structure, not parity.
- **Liu Bang should use all n marks** — in every case checked, partitions using
  fewer marks (bigger, fewer pieces) numerically underperformed using the full
  budget of n pieces with the geometric 1:2:4:… ratio (checked explicitly for
  n=2: a 2-piece partition capped out around 0.508, well below 4/7 ≈ 0.571).

### Knowledge-base entries to use
- No entry is a direct match; closest generic pointers: "Constructive / incremental"
  and "Pigeonhole / extremal principle" (Combinatorics section) for building the
  superincreasing construction and the induction; "Invariants & monovariants" if the
  outliner finds a potential-function argument for the adversary bound.
- The exchange-argument lemma for the claiming sub-game is standard game theory not
  explicitly in the KB — needs to be stated and proved from scratch (short,
  ~5-line induction), not cited.

### Analogous past problems (cruxes)
Searched crux corpus (`combinatorics` domain, subtopics `games-and-strategy`,
`extremal-principle`, `induction-and-construction`) for "stick / segment / interval /
piece / cut" combined with "alternately / take turns." None of the retrieved
problems (aimo-0019 paint game, aimo-0225 polygon counters, aimo-0445 hex Y-game,
aimo-0663 number-picking game, aimo-0854 grid orientation game) are genuinely
analogous — they are turn-based combinatorial games on discrete structures with
win/loss (or pairing-strategy) objectives, not a continuous-quantity
"claim-the-largest-remaining-share" allocation game preceded by adversarial
cutting. **No true analog found in the corpus; this looks like it needs a
from-scratch argument.**

### Prior progress
None (first round; results/imo-2026-03/ has no approaches yet).

### Dead ends (do not retry)
- Equal-spacing (n+1 equal pieces of 1/(n+1)) as Liu Bang's strategy: numerically
  weaker than the geometric 1:2:4:… partition (e.g. n=1: equal split gives only
  1/2, vs. 2/3 for the 1:3-ratio split).
- "Xiang Yu just wants total piece count even" as the driving principle: refuted by
  the n=1 exact computation (see above).
