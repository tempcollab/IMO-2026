## imo-2026-03 — LENS: game/reserve semantics, non-split handle for the b-lift (GAP-P1′-b)

### Terrain summary (honest negative + two fresh numeric NEGATIVES)

I searched specifically for a route to `I_n≤0` / `D̃(π_0⊎F')≥1` for general `b>0` that does **not**
form `π_0` vs `F'` as a split (i.e. does not invoke `D̃(A⊎B)=D̃(A)+D̃(B)−2λ(O_A∩O_B)` for ANY
bipartition of `F`), and does not reduce to the certified `I_n`/floor form. Conclusion: **no such
route exists as a separate engine** — every avenue collapses back into the same wall, for a
structural reason explained below, and I gathered two new pieces of numeric evidence that further
close off tempting "looser" relaxations. This is a genuine (not manufactured) negative result.

### Why the split/overlap wall is structurally unavoidable

`Lemma G` (certified `lemmas/greedy-claim.md`) already collapses the *entire* two-phase marking +
alternating-claim game into the single static formula `D̃(F)=Σ_i(−1)^{i−1}w_i` over the sorted final
piece multiset `F`. This is not a choice of framing — it is a *proof* that greedy claiming is
optimal, so the "game" content is entirely exhausted once `F` is fixed. Every subsequent
"game-theoretic" idea I could construct reduces to one of exactly three shapes, and all three are
already known dead or are just the split/overlap identity again:

1. **A potential over Xiang's cut-placement sequence** (the marking phase, one mark at a time) —
   this is `cut-sequence-potential`'s family: CERTIFIED equivalent to the target itself
   (`lemmas/reserve-target-equivalence.md`, R8): an admissible reserve exists **iff** GAP L holds.
   Dead, and this lens's "amortized argument over the actual pieces" instinct is exactly this
   family in disguise once you try to write it down.
2. **A potential over the alternating claim sequence** (the picking phase, turn by turn) — since
   greedy = sorted order (Lemma G), this is *identical* to the merged-order/window framing,
   CERTIFIED dead (`lemmas/merged-order-layer.md`, R8): any bounded/local window certificate is
   circular (tiling exists iff target holds).
3. **Any split `F=A⊎B` of the final multiset** (peel by scale, by rung, by value-threshold, or any
   other partition) — governed by the UNIVERSAL identity `D̃(A⊎B)=D̃(A)+D̃(B)−2λ(O_A∩O_B)`
   (`lemmas/peel-difference-bound.md`, item (1), proved for *any* disjoint split, not just
   `π_0`/`F'`). So "peel the bottom rung instead of the top scale," "peel piece-by-piece as Xiang's
   cuts land," or any other split you can name is *the same overlap mechanism* under a different
   name — banning "π_0-vs-F' comparison" specifically does not evade it, because the mechanism is
   split-agnostic. This matches the wall as already sharpened in R14.

I could not find a fourth shape. A genuine "strategy-stealing" (aimo-0560-style: replace the
adversary with a pointwise-stronger surrogate) or "pairing/injection directly on pieces" idea
*is* available in the crux corpus, but every concrete instantiation I tried for it (see below)
turned out to be exactly the co-varying b→b−1 descent already REFUTED (R12/R14), because "surrogate
= spend Xiang's lower-rung budget on the top piece instead" is precisely that banned move.

### Two fresh numeric NEGATIVES (new this round, worth recording)

1. **The exact per-rung sum constraint is load-bearing, confirming no "total mass only" bijective
   relaxation exists.** I tested dropping the requirement that each dyadic rung `j` splits into
   parts summing *exactly* to `2^{n-j}` (Xiang's cuts must land inside a specific rung), keeping only
   the aggregate constraints (total sum `2^n−1`, total part count `n+b`). Minimum `D̃` over such
   *relaxed* configs falls to **≈0.386** (n=4, exact `Fraction`, 2·10⁵ trials) — far below 1 — while
   the true (rung-respecting) minimum stays at `≈1` as expected. So any "bijection that changes n" or
   "combinatorial-game-sum" idea that forgets the exact per-rung sum `Σπ_j=2^{n−j}` is doomed; that
   hard equality is not a bookkeeping nicety, it supplies essentially all of the missing `+1`.
   (Consistent with, and sharpens, the R10 "hard equalities `Σπ_j=2^{n−j}`" finding — now confirmed
   quantitatively, not just qualitatively.)

2. **Cross-rung effects are strongly non-additive — no independent-subgame-sum decomposition.**
   Splitting two different ladder rungs `i≠j` independently and comparing `Δ(i,j)` (joint effect on
   `D̃`) to `Δ(i)+Δ(j)` (sum of isolated single-rung effects) gives gaps up to **6.5** (n=4, 2·10⁴
   trials, exact `Fraction`) — nowhere near additive. This rules out any "Sprague-Grundy / sum-of-
   games" style decomposition of the b-lift across rungs (an idea worth flagging because it's a
   genuinely different CGT tool nobody in the run has invoked by name) — it does not apply here
   because the "subgames" (rungs) are not independent once merged into one discrepancy functional;
   the interaction term is of the same order as the effects themselves.

### Distinct openings (for the record — all found to re-encode the banned wall, reported honestly)
- (i) Surrogate-adversary strategy-stealing (crux `aimo-0560`, "replace the adversary with a
  pointwise stronger surrogate") — collapses to the already-refuted co-varying b→b−1 descent.
- (ii) Claim-turn amortized credit scheme — collapses to merged-order/window tiling (dead, R8).
- (iii) Cut-placement amortized reserve — collapses to Reserve⇔Target Equivalence (dead, R8).
- (iv) Bijective "change n" relaxation dropping per-rung exact sums — REFUTED this round (min drops
  to 0.386, the per-rung constraint is essential).
- (v) Independent per-rung subgame-sum (CGT additivity) — REFUTED this round (non-additive, gap 6.5).

None of these survive as an independent engine. I recommend the outliner NOT open a "pure game
semantics" slug this round — it would immediately re-derive the certified overlap-term reduction and
die on the same wall (single-gap trap), OR (if it tries (i)) directly repeat the banned co-varying
descent. Given CLAUDE.md's shared-gap rule, the productive fresh framing has to inject something
outside both game-process framings AND all-split framings — i.e., it must be an argument that uses
the recursive dyadic cut-tree's exact-sum structure in a genuinely NEW combinatorial way (e.g. an
explicit invariant of the tree's branching pattern under Σa_j≤n, not a potential over any linear
order). That is consistent with, not contradicting, the existing R14 directive.

### Candidate technique(s)
None new to add beyond what's already banked. The only semi-promising untried tool: the
UB's own "distinct-subset-sum rigidity" (`{−1,0,1}` combinations of powers of two have `|sum|≥1`,
`lemmas/upper-bound.md`) has still never been imported into the LB side (flagged since R9, still
unused) — but this is a *sign-pattern* device, i.e. still fundamentally a split/measure argument
once instantiated, so it does not escape the wall identified above; it might still be useful as
a *finishing* tool once a genuinely non-split invariant narrows the search, not as the primary engine.

### Cheap-kill candidates
- Before any b-lift builder proposes a "bijection to a smaller-n instance," first check it against
  the two refutations above (per-rung sum drop, cross-rung non-additivity) — both are cheap
  (`Fraction`, a few thousand trials) and kill most naive relaxations in under a minute.

### Knowledge-base entries to use
- None beyond what's already imported (Lemma G / discrepancy game value, the certified SD/PEEL
  identity). `knowledge_base.md` combinatorics-games entries were already exhausted in prior rounds
  per `/tmp/memory/math-explorer.md` rules #2, #12, #18, #30.

### Analogous past problems (cruxes)
- `aimo-0560` (combinatorics/games-and-strategy) — "replace the adversary with a strictly stronger
  surrogate whose reply is pointwise at least as damaging." Genuinely relevant *idea* but every
  literal instantiation for this problem reduces to the already-refuted co-varying b→b−1 descent
  (R12/R14) — not usable as a fresh independent engine, report honestly rather than force it.
- `aimo-0117` (dyadic dominance, "largest exceeds sum of the rest") — already used (round 1/11), no
  new content for the b-lift specifically.
- `aimo-0596` (XOR/involution pairing for alternating card-taking) — structurally the closest
  "pairing strategy" crux in the corpus, but its mechanism (global XOR invariant that both players
  provably hold the same coset value) does not transplant: our game has a value function (weighted
  sum), not a parity/coset invariant beyond the already-exploited odd-total Parity Lemma
  (`lemmas/parity-odd-total.md`, R9), which is already banked and used only as a finisher, not an
  engine, for exactly the reasons GAP-IMR was ruled dead (R10).
- No crux in the corpus offers a genuinely new mechanism for THIS specific structure (alternating
  claim value collapsed to a static discrepancy functional over a two-level dyadic-refinement
  budget). Reporting this honestly rather than forcing a weak match.

### Prior progress
GAP L reduced (certified) to: UB done for all n (`lemmas/upper-bound.md`); LB Case A done
(`lemmas/peel-difference-bound.md` item 3); LB Case B base slice `b=0` FULLY proven
(`lemmas/base-slice-star.md`, `(★) Σ_blue-odd≥Σ_red-even`); the sole remaining wall is the
`b`-lift, now understood (R14) as the odd-set overlap term `λ(O_{π_0}∩O_{F'})`. This round adds no
positive progress on the wall itself — it is a scouting round confirming (with two new
quantitative numeric refutations) that no non-split/non-sequential shortcut exists, and that the
overlap term is genuinely unavoidable structurally (any split hits it; any process framing is
either equivalent-to-target or circular).

### Dead ends (do not retry — consolidating existing bans + this round's findings)
- All bans from `run_state.md` Rules stand (co-varying/single-cut b-descent, π_0-fixed multi-cut
  merge, ABSORB tautology, split-rung (I1′), scalar b-cutoff, (NEG) Q≥S_π, all measure/merged-
  order/sequential/genfn/GAP-IMR framings).
- NEW this round: dropping the exact per-rung sum constraint (`Σπ_j=2^{n−j}`) in favor of only
  total-sum/part-count REFUTED (min D̃ falls to 0.386, n=4, 2·10⁵ trials) — any "relaxed bijection to
  a smaller instance" idea must preserve every rung's exact sum, not just totals.
- NEW this round: independent per-rung (CGT sum-of-games) additivity REFUTED (cross-rung
  interaction gap up to 6.5, n=4, 2·10⁴ trials) — rules out decomposing the b-lift as independent
  subgames per rung.
- The "surrogate adversary" strategy-stealing idea (crux aimo-0560) is NOT independent of the
  banned co-varying descent — any literal instantiation reduces to it.

### Small-case / intuition notes (conjectural, numeric only)
- Confirms (again, exact Fraction) `min D̃(π_0⊎F')=1` over the true rung-respecting feasible set for
  n=4 across 2·10⁵ random Case-B trials (0 violations of `D̃≥1`), consistent with all prior rounds.
- The relaxed/non-rung-respecting minimum (0.386, n=4) quantifies just how much "slack" the exact
  dyadic rung-sum structure is buying — roughly 60% of the total gap between the trivial `D̃≥0` bound
  and the target `D̃≥1` comes from enforcing individual rung sums, not just the aggregate budget.
  This is a genuinely new number (not previously computed) that could usefully calibrate how "tight"
  any future non-scalar invariant on the cut-tree needs to be.
