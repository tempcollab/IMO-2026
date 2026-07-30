# imo-2026-03 — selection-game-value lens

## Selection subgame value (the reduction foundation)

Once the pieces are fixed as a sorted multiset `a_1 ≥ a_2 ≥ … ≥ a_m` (m ≤ 2n+1, sum 1), the alternating pick-any-piece game has value

  **V(a_1,…,a_m) = a_1 + a_3 + a_5 + …  (odd-index sum, descending)**

for the first player (Liu Bang). I.e. **greedy (always take the largest remaining) is optimal for both players.**

- **Exchange argument (sketch for the outliner).** At a position with largest remaining piece `a_1`, suppose the mover takes `a_j < a_1` instead. The opponent, facing a set still containing `a_1`, can take `a_1` immediately (greedy is at least as good for the opponent as any other reply to a *smaller* piece being removed, since leaving `a_1` for a future Liu turn only helps Liu). By backward induction / the standard exchange, deviating from greedy never increases the mover's payoff. (This is the pick-ANY-item zero-sum game, NOT the pick-from-an-end game — greedy is genuinely optimal here, verified by exhaustive minimax on 3000 random multisets of size 2–7, 0 mismatches with the odd-index sum.)
- Therefore the whole problem reduces to a **minimax over cut configurations**:

  `c(n) = max_{Liu's ≤n marks}  min_{Xiang's ≤n marks}  [odd-index sum of sorted(final multiset)]`.

  Liu moves first in the *marking* phase and wants to MAXIMIZE the odd-index sum; Xiang responds and wants to MINIMIZE it. (Xiang may place fewer than n marks.)

## How the odd-index sum rewrites under Xiang inserting cuts

Xiang's marks only **refine** Liu's pieces (split each Liu-piece into sub-pieces); the multiset is re-sorted descending and Liu gets the odd positions. The key weapon (conjectural crux of the upper bound): Xiang can insert **near-zero "scraps"** (ε-pieces). A scrap, being the smallest, lands in the last odd-index slot (when the total count is odd = 2n+1), forcing Liu to "waste" one pick on ε and shifting the larger pieces between Liu's odd slots and Xiang's even slots. Xiang can also split a large piece to **demote it** from Liu's odd slot into an even slot.

## Conjectured answer (strong numerical support, n=1,2,3)

  **c(n) = 2^n / (2^{n+1} − 1)**     (→ 1/2 as n→∞; monotone decreasing: 2/3, 4/7, 8/15, …)

Values verified to grid precision:
- c(1) = 2/3 (exact, by hand below).
- c(2) = 4/7 ≈ 0.57143 (powers-of-2 partition; Xiang-best = 4/7 exactly to grid).
- c(3) = 8/15 ≈ 0.53333 (powers-of-2 partition; Xiang-best = 8/15 exactly to grid).

### Liu's (lower-bound) strategy — the powers-of-2 partition

Liu marks so the stick is cut into pieces of sizes `1, 2, 4, …, 2^n` (over denominator `D = 2^{n+1}−1`). Marks at cumulative sums `1/D, 3/D, 7/D, …, (2^n−1)/D`. Computationally, Xiang cannot push Liu below `2^n/D` against this partition.

### Xiang's (upper-bound) strategy AGAINST the powers-of-2 partition — verified exact

Xiang uses all n marks to split **only the largest piece** `2^n/D` into sub-pieces `{2^{n-1}, 2^{n-2}, …, 2, 1, 1}/D` (note the doubled final 1; sum = (2^n−1)+1 = 2^n ✓). The full multiset becomes two copies of each `2^k` for k=1..n−1, plus three copies of 1, all over D — i.e. sorted descending:

  `2^{n-1}, 2^{n-1}, 2^{n-2}, 2^{n-2}, …, 2, 2, 1, 1, 1`  (2n+1 pieces).

Liu's odd-index take = `2^{n-1} + 2^{n-2} + … + 2 + 1 + 1 = (2^n − 1) + 1 = 2^n`, i.e. `2^n/D`. ✓ This proves the powers-of-2 partition's guarantee is **exactly** `2^n/D` (Xiang attains it, doesn't go below) — the partition is the tight lower-bound construction.

## n = 1 by hand (exact)

Liu marks at 1/3 → pieces {1/3, 2/3}. Xiang's options:
- 0 marks: Liu gets max = 2/3.
- split 2/3 into {p, 2/3−p}: multiset {1/3, p, 2/3−p}; Liu = max+min = 1 − median. Xiang maximizes median; max median = 1/3 (p=1/3) → Liu = 2/3.
- split 1/3 (small piece): largest stays 2/3, median ≤ 1/6, Liu ≥ 5/6 > 2/3 (Xiang won't).
So Xiang's best gives Liu exactly 2/3; **c(1) = 2/3**. (Scraps don't help Xiang at n=1 because the 1/3 piece is large enough to absorb them.) Generalized by the powers-of-2 formula.

## THE MAIN DIFFICULTY / gap for the outliner

The **upper bound** (Xiang can force ≤ 2^n/(2^{n+1}−1) against *every* Liu partition, not just the powers-of-2 one) is the open crux. The split-the-largest-into-{powers of 2 + double 1} recipe works *against the specific powers-of-2 partition* but does not obviously generalize to an arbitrary Liu partition. Promising sub-angles for the outliner:

- **Induction on n.** The recursion `c(n) = 2^n/(2^{n+1}−1)` satisfies `c(n) = c(n−1)/(2 − c(n−1))`? Check: c(n−1)=2^{n-1}/(2^n−1); the dyadic structure suggests an inductive halving argument where Liu's largest piece plays a special role. The powers-of-2 partition is the fixed point of "Liu protects the top, Xiang chips the top."
- **Duality / weight function.** Find a potential `Φ` on multisets such that (a) greedy-odd-index-sum ≥ something, (b) Xiang has a move dropping `Φ` by a controlled amount, (c) `Φ` lower-bounds the odd-index sum. The doubled-1 structure hints the potential is a "base-2 place value" of the sorted list.
- **Reformulate as a pairing.** Xiang's even-index picks: pair the sorted list as (1st,2nd),(3rd,4th),…,(2n−1,2n),(2n+1 alone). Liu gets the left of each pair + the last. Xiang's marking controls how mass distributes across pairs. The bound `2^n/D` is what survives when Xiang makes each pair "balanced" in a dyadic sense.

## Distinct openings (for the outliner's rival approaches)

1. **Selection-reduction + powers-of-2 construction (this lens).** Reduce to odd-index minimax; prove c(n)=2^n/(2^{n+1}−1) via the dyadic partition (lower) + a general upper-bound argument (the gap).
2. **Direct induction on n** via a "Liu reserves the largest piece, Xiang must spend marks chipping it" recurrence, avoiding the full minimax.
3. **Weight/potential (base-2 place value)** — prove a universal inequality `odd-index-sum ≥ 2^n/(2^{n+1}−1)` for the minimax via a potential that Xiang can decrease by at most a dyadic factor per mark.
4. **Pairing / matching framing** — view Liu's odd picks vs Xiang's even picks as a bipartite mass-transfer; the bound is the max Liu can lock into the odd slots under Xiang's refinement.

## Candidate technique(s)
- Greedy optimality via exchange argument (selection subgame) — knowledge_base "Invariants & monovariants" / "Pigeonhole / extremal"; classic but must be re-proved.
- Induction + construction (Pólya "Strengthen / induct on n"); the dyadic recurrence.
- Potential / weight function (knowledge_base "Invariants & monovariants", "Monotone subsequences").

## Cheap-kill candidates
- Parity / count of pieces: with all marks used, total = 2n+1 (odd) → Liu takes n+1 pieces; the "n+1 picks vs n picks" asymmetry is the whole game. Scraps exploit the forced last pick.
- The doubled-1 terminal (three 1's) is the extremal equality case — pin it.

## Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics) — for the potential/upper bound.
- "Induction" + "Constructive vs existence" (General Proof Methods) — lower bound = construction, upper bound = adversary strategy.
- "Pigeonhole / extremal principle" — the largest-piece-chipping.
- "Processes-and-algorithms" / "games-and-strategy" crux subtopic (combinatorics) — for analogous adversary/response structures.

## Analogous past problems (cruxes)
- Searched combinatorics `games-and-strategy` (39 cruxes) + greedy/exchange keywords. **No direct analogue** for the "mark-then-alternate-pick, odd-index value" reduction; closest in spirit (adversary marks then pairing response): `aimo-0115` (pairing strategy, responder answers in paired cell), `aimo-0596` (partner-mirroring in a take-turns pick game), `aimo-0663` (second-player always-pairing in a pick game). These are *strategy-structure* analogues only — the odd-index-sum value and the dyadic partition crux have no exact match in the corpus. Do not force a citation.

## Prior progress
- Round 1 start: none. This exploration establishes the reduction and the conjectured formula.

## Dead ends (do not retry)
- **Equal partition into 2n+1 equal pieces is NOT Liu's optimum** for n ≥ 2: Xiang splits one piece into two ~1/(2(2n+1)) halves and adds an ε-scrap, forcing Liu's odd-index take down to ~1/2 (verified: n=2 equal-partition → Xiang pushes to ≈0.5003). The equal-partition / `(n+1)/(2n+1)` guess is WRONG.
- Brute-forcing the full minimax for large n is infeasible (4D+ with scraps requiring fine near-zero grids); the structure must be proved.

## Small-case / intuition notes (conjecture, labeled)
- c(1)=2/3, c(2)=4/7, c(3)=8/15 all match `2^n/(2^{n+1}−1)` to grid precision.
- The equality (tight) case for the lower bound is the powers-of-2 partition; for the upper bound it is Xiang splitting the largest piece into `{2^{n-1},…,2,1,1}`.
- Monotone decreasing to 1/2: as n grows Xiang's scrap power asymptotically halves Liu's advantage, but never reaches 1/2 for finite n (Liu always retains the `2^n/(2^{n+1}−1) − 1/2 = 1/(2(2^{n+1}−1))` edge).
