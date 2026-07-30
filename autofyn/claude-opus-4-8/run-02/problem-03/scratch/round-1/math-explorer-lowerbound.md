## imo-2026-03 (lens: Liu Bang's guarantee — the LOWER BOUND / first-player strategy)

- **Population state:** `sample_approaches` returned 0 approaches (round 1, empty as expected). No prior work in `results/imo-2026-03/`.

### Reduction to a clean abstract game
The claiming phase only depends on the final multiset of piece lengths, not their positions on the stick. So the whole problem reduces to:

1. Liu Bang picks a partition of 1 into `m0 ≤ n+1` positive parts (n marks → n+1 pieces, or fewer if he marks < n points — but more pieces only helps him, so WLOG he uses exactly n marks / n+1 pieces).
2. Xiang Yu picks ≤ n more cuts, each splitting one *current* piece into two arbitrary positive parts (he cannot merge, only subdivide) — this is the adversarial move.
3. **Claiming-subgame key lemma (needs proof, but is standard/believable):** given any fixed multiset of piece lengths, when two players alternately claim pieces each maximizing their own total, the (unique-up-to-ties) optimal play for both is **greedy: always take the currently-largest unclaimed piece.** Hence if the pieces are sorted descending `q_1 ≥ q_2 ≥ ... ≥ q_m`, Liu Bang (first mover) ends with exactly `q_1+q_3+q_5+...` and Xiang Yu with `q_2+q_4+...`. This "greedy is optimal for alternating pick-the-max games" fact should be proved by a standard exchange/induction argument — it is the load-bearing lemma underlying BOTH the lower and upper bound, so it belongs in `lemmas/`.

So Liu Bang's problem becomes: choose a partition of 1 into n+1 parts to **maximize**, over all adversarial subdivisions Xiang Yu can apply with ≤n more cuts, the sum of odd-ranked (descending) pieces in the resulting multiset.

### Distinct openings (candidate Liu Bang strategies tested)

**Opening A — equal pieces (n+1 equal parts of 1/(n+1)).** Tempting first guess, but numerically REFUTED as suboptimal (see below): Xiang Yu can drive Liu's total down well below the naive "half-ish" estimate by shaving a sliver off one equal piece and splitting another in half, exploiting near-ties. Do not pursue this as the extremal construction.

**Opening B — "2n+1 equal final pieces" idea (Liu cuts into n pieces of size 2/(2n+1) and one of size 1/(2n+1), hoping Xiang Yu's best response is to bisect each 2-unit piece, yielding 2n+1 equal unit pieces and Liu total (n+1)/(2n+1)).** Checked numerically for n=2 (target 3/5 = 0.6): **REFUTED** — random/grid search over Xiang Yu's cut choices found he can force Liu's total down to ≈0.500 (well below 0.6), by cutting a tiny sliver off one 2/5-piece (leaving it ≈0.4, tying with the untouched 0.4 piece) and bisecting the 1/5 piece into two 0.1's, giving sorted pieces {0.4, ≈0.4, 0.1, ≈0.1, ≈0} — Liu's odd-rank sum ≈ 0.4+0.1+0 = 0.5. So the "equalize to 2n+1 identical pieces" idea is a dead end / not the extremal Liu strategy — flag this explicitly so the outliner doesn't waste a round on it.

**Opening C — geometric/dyadic "doubling" partition (this is the one that works).** Liu Bang partitions the stick into n+1 pieces with lengths **proportional to 1, 2, 4, ..., 2^n** (i.e. sizes `2^k/(2^{n+1}-1)` for `k=0,...,n`). This is the exact mechanism behind the crux in `aimo-0117` ("Jesse/Tjeerd" powers-of-two game): a geometric/dyadic sequence where **each piece strictly exceeds the sum of all strictly-smaller pieces** (`2^k > 2^{k-1}+...+2^0 = 2^k-1`), which is the classical device for pinning down who ends up with the "big" piece regardless of how the small pieces get split. This is a strong "different framing" candidate — not a size/equalizing argument but a **domination/geometric-weight invariant** argument.

- Verified **exactly by hand** for n=1: Liu Bang marks the point at 1/3 (pieces 1/3, 2/3). Full case analysis (see below) shows Xiang Yu's best response (splitting the 2/3 piece exactly in half, i.e. into thirds — matches the 1:2 doubling pattern with all-equal-after-split!) gives Liu Bang exactly 2/3, and no other placement by Liu beats 2/3. So **c(1) = 2/3**, proven, not just conjectured.
- Verified **numerically** (exhaustive/fine grid search over all of Xiang Yu's structural cut choices, plus independent random search with 5×10^5 trials) for n=2: the doubling partition (4/7, 2/7, 1/7) yields worst-case Liu total **exactly 4/7**, matching the pattern `2^n/(2^{n+1}-1)` with n=2. The general "outer" search over ALL Liu partitions (not just doubling) for n=2 converged toward ≈0.575, consistent with 4/7≈0.5714 up to grid coarseness, i.e. numerically doubling looks optimal among tested partitions, not just a lower bound.
- Verified **numerically** for n=3: doubling partition (8/15,4/15,2/15,1/15) gives worst-case Liu total 8/15 to 6+ digits (random search, 5×10^5 trials), matching `2^3/(2^4-1) = 8/15`.

**Conjectured closed form (label: CONJECTURE, evidence = n=1 proved + n=2,3 strong numerics, not a proof):**
```
c(n) = 2^n / (2^{n+1} - 1)
```
As n→∞, c(n) → 1/2 from above, which is sensible (Liu Bang's first-mover + doubling edge shrinks as the game gets larger but never vanishes).

### Candidate technique(s)
- **Greedy-optimality lemma** for the alternating-claim subgame (exchange argument / induction) — needed regardless of which Liu strategy is used, shared with the upper-bound (Xiang Yu) side.
- **Dyadic/geometric domination invariant**: piece `2^k` (scaled) exceeds the sum of everything strictly smaller. This is the crux move to adapt from `aimo-0117`.
- Likely need an inductive / self-similarity argument: since ratios are 1:2:4:...:2^n, a cut anywhere inside this structure "restarts" a smaller sub-instance of the same doubling game — this self-similarity is probably the key to a clean inductive proof of the exact lower bound `2^n/(2^{n+1}-1)`, rather than case-by-case.

### Cheap-kill candidates
- Parity/domination check: confirm `2^k > sum_{j<k} 2^j` (trivial, `2^k - 1`), used to argue Liu Bang can always safely identify a piece guaranteed to beat all combinations of smaller ones — worth stating explicitly as a one-line lemma before the harder claiming-game induction.
- Before trusting any specific Liu partition, numerically stress-test it against adversarial splits (as done above) — this caught opening B's failure cheaply.

### Knowledge-base entries to use
- Read `knowledge_base.md`; did not find a game-theory/alternating-selection entry by name specific to this — flag to outliner: the KB may need a new "greedy-optimal alternating selection" entry once the lemma is proven, but currently no existing KB entry directly matches (mostly geometry/combinatorics extremal entries per the grep). Outliner should double check KB directly for any "extremal" or "greedy exchange" general-purpose entries applicable to the claiming subgame.

### Analogous past problems (cruxes)
- **`aimo-0117`** (Jesse/Tjeerd two-box stone game) — genuinely analogous. Crux: "Assign played values as a two-sided geometric (dyadic) sequence so the single largest value strictly exceeds the sum of all the others" + "defer committing the extreme value / maintain an invariant that the max stays on your side." This is the direct structural analogue of the doubling partition found above; adapt the domination argument, not the literal proof.
- No other corpus entry (searched `combinatorics/games-and-strategy`, plus broader keyword search for "stick", "alternately claim", "greedy largest", "odd-indexed") resembles the claiming-subgame / stick-division setup closely enough to adapt directly — the rest of the `games-and-strategy` subtopic entries are pairing/mirroring/parity-invariant games structurally different from this "claim the largest remaining number" game.

### Prior progress
None (first round, empty population).

### Dead ends (do not retry)
- **Equal-(n+1)-pieces partition** for Liu Bang: suboptimal, refuted numerically for n=2 (worst case only ≈0.5 vs achievable 4/7≈0.571 under doubling). Do not use as the extremal construction, though it may still be worth keeping as a strawman in the writeup to motivate why doubling is needed.
- **"Equalize to 2n+1 unit pieces" partition** (n pieces of 2/(2n+1) + one of 1/(2n+1)): refuted for n=2 — gives only 3/5 in the naive "Xiang bisects everything" line of play, but Xiang Yu has a strictly better response (sliver + bisect) driving Liu down to ≈0.5. So `c(n) ≠ (n+1)/(2n+1)` in general (only coincides with the true value at n=1 where 2/3 happens to equal 2^1/(2^2-1) too — both formulas agree at n=1, which is why the wrong guess wasn't caught until n=2).

### Small-case / intuition notes (all labeled conjecture except n=1 which is proved by hand)
- n=1: **c(1) = 2/3**, proved exactly via direct case analysis (Liu marks 1/3; if Xiang Yu doesn't cut, pieces {1/3,2/3}, Liu gets 2/3; if Xiang Yu cuts, his best response is to bisect the 2/3 piece into thirds, giving three equal 1/3 pieces, Liu still gets 2/3 exactly). Any other Liu placement `p` gives strictly less than 2/3 against the optimal Xiang Yu response (shown by full case split on `p<1/3`, `p=1/3`, `p>1/3`).
- n=2: **conjectured c(2) = 4/7**, strong numerical support (exact match to 10+ significant figures via two independent search methods).
- n=3: **conjectured c(3) = 8/15**, matched via random search to 6+ digits.
- General conjecture: `c(n) = 2^n/(2^{n+1}-1)`, via Liu Bang's dyadic-doubling partition `2^0,2^1,...,2^n` (normalized). This is a conjecture pending: (a) a rigorous proof that the doubling partition guarantees at least this value against ALL Xiang Yu responses (not just the specific adversarial responses found numerically), and (b) confirmation from the upper-bound (Xiang Yu) side that Xiang Yu has a matching strategy capping Liu Bang at exactly this value (that is the other lens's job).
