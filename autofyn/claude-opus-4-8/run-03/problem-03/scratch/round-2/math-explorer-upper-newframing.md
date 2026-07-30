## imo-2026-03 — lens: genuinely different framing for the adaptive Xiang-Yu upper bound (GAP B3 / GAP U)

### Setup recap (shared, both approaches agree)
Reduction Lemma R + measure identity (Lemma M/I, certified in `lemmas/`) collapse the whole
problem to: Liu picks a multiset `a_1≥…≥a_m` (m≤n+1) summing to 1; Xiang applies ≤n cuts;
`D = measure{t : N(t) odd}`, `N(t)=#{final pieces >t}`. Need: Xiang can always force
`D ≤ u_n = 1/(2^{n+1}-1)`. Both live approaches reduce the hard case to **m = n+1, full
budget, all cuts strict**, and both single-move peels (greedy-match; single
cancelling-pair/bisect) are proven (numerically + by counterexample) insufficient for n≥3
(and even the peel's *closing condition* `max(a_1,2a_2) ≥ L·c(n)` fails already at n=2).

### KEY NEW OBSERVATION (numerically verified this round, not previously reported)
The single-cancelling-pair peel is not just quantitatively weak — it is using the **wrong
combinatorial move**. Re-examined the induction-peel's own n=2 counterexample
`(a1,a2,a3)=(0.5,0.28,0.22)` (chosen because `max(a1,2a2)=0.56 < L·c(2)=0.571`, so the peel
"does not close"). Numerical optimization (scipy differential evolution over cut points)
shows the TRUE minimax value there is **D ≈ 0** (essentially 0, to 1e-9), far below
`u_2=1/7≈0.143` — achieved by a single cut of `a1=0.5` into exactly `(0.28, 0.22)`, i.e.
**splitting the top piece to exactly match the two smaller pieces `a2,a3` simultaneously**,
producing two perfectly cancelling pairs `{0.28,0.28},{0.22,0.22}` with ONE cut (this
example has `a1 = a2+a3` because `a1=1/2` forces it — a coincidence of this specific input,
but the *move* generalizes). Tested on generic (non-coincidental) inputs
`(0.45,0.30,0.25)`, `(0.4,0.35,0.25)`, `(0.6,0.25,0.15)`: optimal D = 0.05, 0.05, 0.10
respectively — all comfortably below `u_2=0.143`, achieved by cutting `a1` into fragments
that **partially match** `a2` and/or `a3` (a subset-sum style split), not by the "match top
two only" rule. This strongly suggests the peel-based inductions in both live approaches
are attacking gap U/B3 with an artificially weakened move set, and the real strategy space
is richer: **cut the top piece so its fragments align with an arbitrary subset of the
remaining pieces' values (or partial amounts thereof), not just the second-largest.**

### Distinct openings for the upper bound

1. **Subset-sum / exact-cover matching strategy (NEW, most promising given the numeric
   finding above).** Instead of one cancelling pair per cut, let Xiang look for a subset
   `T ⊆ {a_2,…,a_m}` (or partial amounts of them) with `Σ_T a_i ≤ a_1`, cut `a_1` into
   `|T|` fragments exactly equal to the elements of T plus one leftover `a_1 - Σ_T`, using
   `|T|` cuts to cancel `|T|` pairs at once (cancelling pair Lemma P applies to each pair
   independently — no new lemma needed, just a smarter choice of where to cut). This
   turns Xiang's problem into: choose a partition of `a_1` (his cut budget lets him realize
   any subdivision of `a_1` into ≤ (available cuts) pieces) that maximizes the total mass
   matched against `{a_2,…,a_m}`, a bin-covering/knapsack-flavored combinatorial
   optimization. Why it might work: because `a_1 ≥ a_2 ≥ …`, `a_1` is large enough to
   "absorb" much of the rest; the leftover after matching is the analogue of the residual
   `ℓ` in the peel approach but generically much smaller. Risk: turning "there exists a
   good subset/split" into a clean closed-form bound `≤ u_n` for ALL Liu profiles is itself
   a nontrivial combinatorial claim (a max-flow / greedy-fit argument), and cuts spent on
   matching several small pieces to fragments of `a_1` must still fit in budget `n` — needs
   a careful cut-count accounting (this is exactly the sort of profile-tracking the
   induction-peel's own GAP U note says is missing).

2. **LP-duality / weight-function certificate (structurally different from any
   "construct a strategy" approach).** Reformulate: for fixed cut budget, Xiang's minimum
   achievable D over all of his cut choices is itself an infimum of a linear (in piece
   lengths, for a fixed combinatorial cutting pattern) functional; view the overall
   two-player value as a minimax and seek a **dual certificate**: a function or weighting
   over thresholds t (or over "scales" 2^k u_n) that simultaneously (a) is achieved by
   Liu's dyadic config with value exactly u_n, and (b) upper-bounds D for every possible
   Xiang response to every possible Liu config — i.e., exhibit an explicit potential
   Φ(current multiset, cuts remaining) ≥ (achievable D) that telescopes/collapses via the
   toggle calculus (Lemma T is already fully proven and gives the exact effect of one cut
   on the odd-set — a natural base for a potential argument) to u_n after ≤n cuts,
   regardless of adversary choices. This avoids ever specifying "the" strategy explicitly;
   instead it's an amortized/monovariant argument (knowledge_base.md "Invariants &
   monovariants"). Risk: constructing the right potential is exactly as hard as finding the
   strategy — but such arguments are often more robust to case explosion than an explicit
   greedy rule, and might close both GAP L and GAP B3/U simultaneously since Lemma T's
   symmetric-difference bookkeeping is already the natural language for such a potential.

3. **Exchange/smoothing: dyadic partition is Liu's worst case, reduce arbitrary A to it.**
   Instead of building a strategy for every A, try to show V(A) := min_Xiang D(A) is
   *maximized* (over the simplex of Liu partitions with ≤ n+1 parts) exactly at the dyadic
   config already fully solved (upper bound proven THERE — see induction-peel §6, "dyadic
   extremal input", tight). A smoothing lemma of the form "if A' is obtained from A by an
   elementary move toward dyadic-shape (e.g. replacing two middle pieces (x,y) with
   (x+ε,y−ε) pushing the ratio toward 2:1) then V(A') ≥ V(A)" would let a finite chain of
   smoothing moves transfer the already-solved dyadic bound to every A. This is the
   "replace the adversary with a stronger surrogate" pattern (crux move from `aimo-0560`,
   see below) turned around: here Liu is the one being replaced by a worst-case surrogate.
   Risk: V(A) is itself a minimax (an infimum over Xiang's continuum of cut choices), so
   proving monotonicity under smoothing requires understanding how Xiang's OPTIMAL response
   changes under the perturbation — likely needs an envelope-theorem-style argument or an
   explicit coupling of the two games' optimal strategies. Not yet known whether the
   direction of monotonicity is even true in general (only checked at n=2 numerically that
   dyadic input attains the correct extremal value, consistent with but not proving
   maximality among ALL profiles — this needs a genuine argument, not just anecdote).

4. **Top-down "protected-tail" strategy pinned to dyadic scale intervals directly (global,
   non-adaptive-in-appearance but really an invariant argument).** Rather than induct on
   pieces, directly aim to show Xiang can force N(t) to be even for ALL t ≥ u_n (i.e. the
   entire odd-set of measure ≤ u_n sits in [0,u_n)). This is a stronger, cleaner target than
   "D ≤ u_n" (it upgrades a measure bound to a positional one) and might be provable by
   strong induction on scales: process Liu's pieces from largest to smallest, and whenever
   the current largest unprocessed piece exceeds the sum of the ones below AND the current
   remaining budget u_{k} threshold, cut it to exactly the "protected" size predicted by the
   dyadic model, recursing on the remainder — effectively enforcing the SAME accounting
   Case A (top-piece-uncut) used for the LOWER bound, but now as an upper-bound
   construction. This reuses Lemma T's exact toggle bookkeeping and may unify with opening
   2. Risk: same coupling difficulty flagged as GAP L for the lower bound (top-piece
   fragments interfering with sub-config parities) reappears here in mirrored form.

### Cheap-kill candidates
- None obvious as a pure parity/pigeonhole kill of gap B3 itself — but the subset-sum
  numeric finding (opening 1) is a cheap *test*: for any candidate general strategy
  proposed by the outliner, first check it beats "match top two only" on the induction-
  peel's own stated counterexample `(0.5,0.28,0.22)` and on the generic examples above
  `(0.45,0.30,0.25)`, `(0.6,0.25,0.15)` — any strategy failing to reach these numeric optima
  (0, 0.05, 0.10 respectively) is provably not tight and should be discarded quickly.
- Sanity bound: since `u_n < 1/2` always and `D=0` is achievable whenever some subset of
  pieces exactly sums to half the total (parity-cancellation is "free" in that case), any
  general strategy must specifically handle only the "irrational"/generic ratio profiles —
  a useful reduction: WLOG no exact subset-sum coincidences (perturb continuously, D is
  continuous in the piece lengths by Lemma I, so the sup over A is attained in the
  closure — this removes the trivial D=0 cases without loss, effectively normalizing the
  hard case to "generic ratios").

### Knowledge-base entries to use
- **Invariants & monovariants** (`knowledge_base.md` Combinatorics section) — direct
  match for opening 2's potential-function idea.
- **Hall's marriage theorem / SDR** — candidate tool for opening 1's subset-matching
  strategy (formalizing "which pieces can be simultaneously matched by fragments of a1"
  as a bipartite matching / covering problem with a Hall-type feasibility condition).
- **Multiset partitions & power-sum matching (Prouhet–Tarry–Escott flavor)** — directly
  named in `knowledge_base.md` Combinatorics; relevant vocabulary for "split a set into
  parts with matching sums," i.e. exactly opening 1's subset-sum matching.
- **Extremal principle / pigeonhole for the smoothing lemma** (opening 3) — "take the
  maximal/minimal element" is the natural start of an exchange argument.

### Analogous past problems (cruxes)
Filtered `combinatorics` + `games-and-strategy` (39 cruxes) and scanned all `how_used`
fields; also checked `sequences-and-recurrences`-adjacent items already used by the live
approaches. Best candidates:
- **`aimo-0117`** — "Assign the played values as a two-sided geometric (dyadic) sequence
  so that the single largest value strictly exceeds the sum of all the others," plus
  "defer committing the extreme value until the opponent's move vacates its target cell."
  Genuinely analogous: it is precisely the superincreasing/dyadic structural fact already
  used by both live approaches for the LOWER bound construction (Liu's `2^k` pieces); it
  does NOT directly solve the upper-bound adversarial-strategy gap, but confirms the
  dyadic superincreasing shape is the natural "hardest instance" pattern, supporting
  opening 3 (smoothing toward dyadic as worst case).
- **`aimo-0560`** — "Replace the adversary with a strictly stronger surrogate whose reply
  is pointwise at least as damaging, so a win against the surrogate transfers down." This
  is the crux move underlying opening 3 (reduce arbitrary Liu profiles to the dyadic
  surrogate by showing dyadic is pointwise worst for Xiang). Worth reading the full
  solution in `past_problems_database.json` for the technical machinery of "pointwise at
  least as damaging" — that's exactly the monotonicity condition opening 3 needs to
  establish.
- **`aimo-0653`** — "bound the requester by having the adversary commit every requested
  item to one orientation, then count disjoint lines each item must occupy" — a
  double-counting/pigeonhole bound on an adversarial resource-allocation game; only
  loosely analogous (different game shape) but the "count the commitment cost" idea is a
  weak analogue of the potential/credit idea in opening 2. Not a strong match — flagging
  for completeness, not recommending as primary.
None of the 39 games-and-strategy cruxes solve a "minimize an alternating-sign
sum via adaptive cuts against an adversarial partition" game directly — this problem's
game (claim-highest-piece game reduced to alternating sum of a cut multiset) does not
have a close structural twin in the sampled corpus; the closest structural fact
(superincreasing/dyadic sequences, `aimo-0117`) is already in use for the lower bound.

### Prior progress
See `current.md` — Lemmas R, I/M, T, P all fully proven and certified
(`lemmas/reduction-odd-rank.md`, `lemmas/measure-identity.md`,
`lemmas/cancelling-pair.md`). Lower bound Case A proven; upper bound proven exactly on the
dyadic extremal input. Both gaps (B2/L lower, B3/U upper) remain open and are the sole
blockers.

### Dead ends (do not retry)
- **Greedy-match (largest-two, 0/1/2-cut rules by ratio)** — proven insufficient
  numerically for n≥3 (parity-measure-potential's own computation).
- **Single cancelling-pair peel closing via `max(a_1,2a_2) ≥ L·c(n)`** — proven
  insufficient starting n=2 by explicit counterexample AND (new this round) shown to
  leave a large amount of achievable improvement on the table even where it "doesn't
  close" — the true minimax there is far below u_n, achieved by a smarter single cut. Do
  not re-propose either of these single-rule peels; any new approach must at minimum
  match the subset-sum-style cut found numerically above.

### Small-case / intuition notes (all conjectural, numerically checked only)
- On the induction-peel's own counterexample `(0.5,0.28,0.22)` for n=2: true minimax
  D ≈ 0 (not ≈0.003 as the approach file guessed), reached via ONE cut splitting `a1`
  into fragments matching `a2` and `a3` exactly (special because `a1=1/2`).
- On generic (non-special) 3-piece n=2 inputs `(0.45,.30,.25)`, `(0.4,.35,.25)`,
  `(0.6,.25,.15)`: true minimax D = 0.05, 0.05, 0.10 respectively (numeric, differential
  evolution over cut fractions), all comfortably `< u_2 = 1/7 ≈ 0.1429` — consistent with
  the conjecture that the DYADIC Liu profile `(4/7,2/7,1/7)` is the unique/near-unique
  worst case for n=2 (matches existing exact dyadic computation `D=1/7`).
- Attempted (and failed due to timeout, not disproof) a full bi-level numeric
  optimization (max over A of min over Xiang cuts) for n=2 to empirically confirm dyadic
  is the GLOBAL worst-case Liu profile among all 3-piece partitions — inconclusive this
  round; worth a faster/smarter numeric search (e.g. restrict to 1-D slices via a1
  parametrization with a2,a3 solved analytically) if the outliner wants independent
  numerical confirmation of opening 3's premise before investing proof effort in it.
