## imo-2026-03

### Distinct openings
1. **Position-independence reduction (key structural insight).** The claiming subgame
   only depends on the *multiset* of final piece lengths, never on where they sit on
   the stick. So the whole problem reduces to a purely combinatorial game on multisets
   of positive reals summing to 1: Liu Bang picks an initial multiset `P0` of `≤ n+1`
   positive reals (via `≤n` cuts), then Xiang Yu performs `≤n` "split" moves (each
   move picks one current piece and divides it into two positive parts, summing to
   the original), and the payout is `Σ` of the odd-ranked (1st, 3rd, 5th, ... when
   sorted descending) values of the final multiset (this is the value of the alternating
   claiming game — see the greedy lemma below). This reframing turns a geometric game
   into a discrete-multiset game and is likely the right level to state lemmas at.
2. **The greedy-claiming lemma as the load-bearing fact.** In the "take turns picking
   an unclaimed item to maximize your own sum" subgame on a fixed finite multiset, it
   is a *classical* fact (provable by an exchange/induction argument, not yet proven
   here — flagged as a gap) that both players playing "always take the currently
   largest remaining piece" is optimal for both, and the resulting value for the first
   mover is exactly `a_1+a_3+a_5+...` for `a_1≥a_2≥...` the sorted-descending pieces.
   This collapses "who gets what" into a pure sorting statement and is the crux that
   should be proven early and then imported as a lemma by every approach.
3. **Median-collapse framing for small n.** Since total length is fixed at 1, for an
   *odd* total piece count `2n+1`, Liu's share = `1 − (median of a carefully-tracked
   quantity)` only works cleanly for n=1 (3 pieces: Liu's share = largest+smallest =
   `1 − median`). For n=1 this reduces Xiang Yu's optimization to "maximize the median
   of the 3-piece multiset," which is a 1-D optimization solvable by hand (see below).
   For n≥2 this collapse doesn't directly generalize (5+ pieces, Liu gets 3 of them,
   not simply "not-the-median"), so a genuinely different invariant/potential is needed
   for the general n proof — this is the real technical gap to attack.
4. **Extremal/equalizing-strategy framing.** Conjecture Liu Bang's optimal opening
   forces near-equal pieces in a *value* sense (not necessarily equal lengths — the
   n=1 optimum is the unequal split `{1/3, 2/3}`, not `{1/2,1/2}`!) such that no matter
   how Xiang Yu subdivides, a certain weighted quantity is pinned. This "pinned
   invariant despite Xiang's choice" phenomenon (seen concretely in n=1, see below) is
   probably the mechanism behind the general lower bound and is worth building the
   outline's Liu-Bang strategy around.

### Candidate technique(s)
- Reduce to the multiset-of-lengths game (opening 1), prove the greedy-claiming lemma
  (opening 2) as a standalone certified lemma, then attack the n-piece optimization via
  an explicit Liu Bang construction (lower bound) + an explicit Xiang Yu adversary
  argument (upper bound), likely via an exchange/smoothing argument (à la
  "Piecewise-concavity smoothing" or "Standard inequalities" entries in KB, adapted) or
  an induction on n reducing to the n=1 base case structurally.
- Induction on n is a strong candidate: Xiang Yu's best response to a big piece often
  looks like "cut it near a boundary to reproduce a smaller subinstance" (seen in the
  n=1 computation, where Xiang's optimal cut of the 2/3-piece is *not* the midpoint but
  near one end) — suggests a recursive/self-similar structure worth formalizing.

### Cheap-kill candidates
- **Trivial piece-count bound**: total pieces ≤ `2n+1` ⟹ Liu Bang gets at most `n+1`
  pieces in the claiming subgame (alternating claim of `≤2n+1` items, Liu first). This
  immediately gives the *shape* of the answer (`something/(2n+1)`-flavored) but is NOT
  by itself the value, since pieces are unequal — only a naive equal-partition heuristic
  gives literally `(n+1)/(2n+1)`; the true optimum need not equalize lengths (confirmed
  false for n=1, see below).
- **Symmetry check**: for n=1, Xiang Yu is indifferent between "don't mark" and marking
  optimally at Liu Bang's optimum `a=1/3` — both give exactly `2/3`. This equalization
  of Xiang Yu's options at Liu's optimum is a strong signature of a true minimax
  equilibrium and a good sanity check to demand of any n≥2 candidate construction.

### Knowledge-base entries to use
- `knowledge_base.md` **Combinatorics: Invariants & monovariants** — the "median stays
  pinned regardless of Xiang's split location" phenomenon at n=1 is exactly an
  invariant-under-adversary-move argument; likely generalizes.
- **Problem-Solving Heuristics: Solve a simpler/special case first / Specialize** — used
  directly here.
- **General Proof Methods: Constructive vs. existence** — the final "solved" write-up
  needs BOTH a Liu Bang strategy (lower bound, explicit) AND an explicit Xiang Yu
  counter-strategy (upper bound) for every n — this is a `compute_and_prove` with
  `answer_type: expression`, so both halves are mandatory per CLAUDE.md rigor rules.
- No entry in the KB directly addresses alternating-claim / greedy-optimal games; the
  greedy-claiming lemma (opening 2) will likely need to be proved from scratch inside
  the approach, citable as "greedy exchange argument" under **General Proof Methods**.

### Analogous past problems (cruxes)
- Searched `combinatorics` × `games-and-strategy` (39 cruxes) and searched
  `past_problems_database.json` for stick/segment/interval + cut/mark/claim
  combinations. **None of the 39 games-and-strategy cruxes, nor any problem in the
  corpus, closely resembles this "mark points then alternately claim resulting
  pieces to maximize length" structure.** The closest surface-level matches
  (aimo-0596, aimo-0854 — pairing/involution strategies for take-turns claiming games)
  are about *discrete item* claiming games with a fixed a-priori pairing structure
  (e.g. cards, cells), not a continuous stick where the "items" (piece lengths) are
  themselves chosen adversarially before claiming starts — the adversarial-partition
  layer here has no real analogue in the sampled corpus. I recommend treating this as
  a genuinely novel construction problem rather than forcing a corpus match.
- If useful as a distant structural echo only (not a real crux match): aimo-0461's
  "conflict-cycle capping" pattern (responder always neutralizes the mover's last move
  locally) has the same *flavor* as "Xiang Yu reacts locally to Liu Bang's split," but
  the payoff structure (independent-set counting vs. continuous length sums) is too
  different to adapt directly.

### Prior progress
None — `results/imo-2026-03/` has no approaches yet (round 1, first exploration);
`current.md` and `approaches/` are empty. `sample_approaches` was not needed since the
population is empty.

### Dead ends (do not retry)
- **Equal-partition-of-n+1-pieces strategy for Liu Bang** (splitting the stick into
  `n+1` equal segments up front): computed exactly for n=1 (`a=1/2`) and it gives Liu
  Bang only `0.5`, strictly worse than the true optimum `2/3` — Xiang Yu can always cut
  one equal piece near its boundary to reproduce a median exactly equal to `a`, which at
  `a=1/2` is worse than at the true optimal `a=1/3`. **Do not propose "Liu Bang marks
  equally-spaced points" as the lower-bound construction** — it is provably suboptimal
  at n=1 and likely at all n.
- Naive guess `c(n) = (n+1)/(2n+1)` from the piece-count bound alone: matches n=1
  exactly (`2/3`), but numerical search at n=2 (see below) suggests the true value is
  probably *below* `3/5 = 0.6`, so this formula should be treated as an unconfirmed,
  likely-wrong-for-n≥2 conjecture, not a target to prove.

### Small-case / intuition notes (conjecture, not proof)
**n=1 — solved by hand + verified numerically (high confidence, this is a rigorous
small-case computation, not just a guess):**
Liu Bang marks one point `a ≤ 1/2` (WLOG), creating pieces `{a, 1−a}`. Xiang Yu's best
response is to split the larger piece `1−a` at some point, creating 3 pieces
`{a, x, 1−a−x}`; Liu's payoff = largest+smallest = `1 − median`. Case analysis:
- For `a ≤ 1/3`: Xiang Yu's best is the midpoint split, giving median `(1−a)/2`, so
  Liu's payoff `= (1+a)/2`, increasing in `a`.
- For `a > 1/3`: Xiang Yu's best is to cut *near a boundary* of the big piece (any cut
  with `x ∈ [0, 1−a−a]`, i.e. keeping the middle value pinned at exactly `a`), giving
  median `= a` exactly (cutting the *other*, smaller piece `a` instead is strictly worse
  for Xiang Yu). So Liu's payoff `= 1 − a`, decreasing in `a`.
Both branches meet at `a = 1/3`, giving **`c(1) = 2/3`**, confirmed by a fine grid search
in Python (`best_a ≈ 0.3328`, `value ≈ 0.6671`, matching `1/3` and `2/3` to grid
resolution). Notably the optimal split is *unequal* (1/3, 2/3), and at the optimum
Xiang Yu is indifferent between marking and not marking — both give exactly `2/3`, a
strong equilibrium signature.

**n=2 — numerical only, low-to-medium confidence (a nested continuous optimization,
approximated by Nelder-Mead with random restarts over a grid of Liu Bang's 3-piece
partitions, checking all of Xiang Yu's cut-distributions among the 3 pieces up to 2
total cuts):** best found value climbed from `≈0.564` (coarse grid, few restarts) to
`≈0.58` as the search was refined (grid ≈ Liu's pieces `{0.11, 0.27, 0.62}`, Xiang Yu's
best response splits the two larger pieces once each, or the largest piece twice). This
is **strictly below `3/5 = 0.6`**, the value the naive `(n+1)/(2n+1)` formula would
predict, and the numerics were still trending upward with more restarts when I ran out
of budget, so `c(2)` is not pinned down — plausible candidates in the `0.57–0.60` range
include `4/7 ≈ 0.571`, `7/12 ≈ 0.583`, or the search may in fact be converging to `3/5`
with better optimization (my Nelder-Mead + sigmoid parametrization is known to struggle
near boundary/degenerate splits). **Treat `(n+1)/(2n+1)` as unconfirmed for n≥2** — the
outliner should either (a) design the n=2 lower/upper bound constructions directly and
see what value they force out (more reliable than my noisy numeric search), or (b)
budget a follow-up numeric probe with a more robust global optimizer (e.g. an LP-style
relaxation or exact case analysis generalizing the n=1 median argument) before
committing to a target formula. The n=1 exact structure (optimal split unequal, ratio
1:2, Xiang Yu indifferent at the optimum) is the strongest lead for guessing the general
construction — it suggests self-similar/recursive piece ratios rather than equal
spacing.
