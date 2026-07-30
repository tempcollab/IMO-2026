## imo-2026-03

### Setup / key structural reduction (used throughout)
Given the final multiset of pieces (after both players' marks and all cuts), the
alternating whole-piece-claiming subgame (Liu first) is a *zero-sum* game (total
length is fixed = 1), equivalent to "take turns picking one remaining number to
maximize your own running sum." I verified numerically (brute-force minimax vs.
greedy, 2000 random trials up to 6 pieces, all matched) that the optimal play for
BOTH players is: sort pieces descending, each player always takes the currently
largest remaining piece. So the claiming phase's outcome is deterministic once
the final piece multiset is fixed: sorting descending a_1≥a_2≥...≥a_m, Liu Bang
(first) gets the odd-indexed pieces a_1,a_3,a_5,..., Xiang Yu gets the even-indexed
ones. This reduces the whole problem to a two-stage *partition/subdivision* game:
Liu picks intervals (≤n+1 of them, lengths summing to 1), Xiang Yu then spends
≤n cuts subdividing those intervals (each cut always splits one existing piece
into two — total final piece count is exactly (n+1)+n = 2n+1 if both players use
all their marks) to minimize the sum of odd-ranked pieces.

### Distinct openings
1. **Direct minimax on the fixed-multiset reduction** (this report's core route):
   treat the problem as choosing x_1≥...≥x_{n+1} (Liu) then an adversarial
   re-subdivision by Xiang using n further cuts, and solve the resulting minimax
   exactly for small n, then generalize by pattern/induction.
2. **"Largest-piece-dominance" framing** (crux-inspired, see below): make Liu's
   configuration a two-sided-geometric-like (here one-sided geometric, ratio 1/2)
   sequence so that at every stage the current largest active piece dominates the
   rest — this is the mechanism that seems to force Xiang Yu's hand regardless of
   how he distributes his cuts.
3. **Recursive/self-similar framing**: numerically, Liu's optimal configuration for
   n cuts, restricted to its bottom n pieces (excluding the single largest), is
   *exactly* Liu's optimal configuration for n−1 cuts, rescaled to sum to 1−x_1.
   This suggests an inductive proof structure: c(n) in terms of c(n−1), rather than
   solving each n from scratch.

### Candidate technique(s)
- Exchange/greedy-optimality argument for the alternating claiming subgame (should
  be provable by a standard exchange argument / induction on number of pieces —
  a known folklore lemma, worth checking crux corpus induction-and-construction
  entries for the exact clean phrasing).
- Extremal/minimax argument + induction on n for the two-stage marking game.
- A "domination" invariant à la aimo-0117 below: if one piece exceeds the sum of
  several others it "locks in" for the player who can claim it first regardless of
  how the others are split.

### Cheap-kill candidates
- None found that fully resolve the problem, but a useful pruning fact: **the
  claiming order is fully determined by piece lengths alone** (see reduction
  above) — this collapses the "then alternately claim" phase to pure
  arithmetic, so all effort should go into the two marking stages, not simulating
  the claiming phase combinatorially.
- Symmetry/WLOG: Xiang Yu never benefits from leaving a cut budget unused, and
  never benefits from creating a piece equal in length to another existing piece
  that's already favorable to Liu (ties can be perturbed away without loss) —
  useful for cleaning up an eventual proof but not a full kill.

### Knowledge-base entries to use
- I grepped `knowledge_base.md` for stick/interval/game/greedy/partition-type
  entries; nothing specific to alternating-claim or interval-marking games is
  present (the file's game-adjacent content is generic: concavity-on-intervals,
  interval-intersection, multiset partition/power-sum matching). No direct KB
  entry matches this problem's core mechanism — flag this as a genuine gap; the
  outliner should not expect a named KB theorem to shortcut the game analysis.

### Analogous past problems (cruxes)
- **aimo-0117** (Jesse & Tjeerd stone game, `combinatorics`/`games-and-strategy`)
  — genuinely analogous and the single best match found. Crux: *"Assign the
  played values as a two-sided geometric (dyadic) sequence so that the single
  largest value strictly exceeds the sum of all the others"* — i.e. use powers of
  2 (or a 1/2-ratio geometric sequence) so `2^j > 2^{j-1}+...+2^{-i}`, meaning
  whichever "box" (here: whichever *player*) holds the current largest value
  wins regardless of how the rest is split. This is EXACTLY the phenomenon I
  found numerically: Liu Bang's optimal marks are (conjecturally) a geometric
  sequence with ratio 1/2, and the resulting game value seems to always reduce to
  "Liu Bang secures exactly his largest declared piece x_1, Xiang Yu gets exactly
  the rest 1−x_1," with Xiang Yu unable to do better by any split of that biggest
  piece, precisely because of a domination-type argument. Worth having the
  outliner read aimo-0117's full solution (the "defer committing the extreme
  value" invariant-maintenance strategy) as a template for how to write the
  induction that Liu Bang can maintain "dominant top piece" behavior against any
  Xiang Yu counter — though the games are not identical (that's simultaneous
  writing/moving stones between two boxes across n rounds; ours is two
  one-shot marking phases followed by an alternating claim), the "largest value
  beats the sum of the rest" style argument is the right shape of tool.
- Other games-and-strategy cruxes (aimo-0596 pairing/involution, aimo-0663
  pigeonhole-on-gaps, aimo-0445 double-threat/fork) do not resemble this
  problem's continuous-length-splitting structure — not recommended as
  analogies.

### Prior progress
None — this is round 1, no approaches file yet exists beyond the empty
`current.md` (Status: unsolved).

### Dead ends (do not retry)
None recorded yet (first round). One thing to flag as a **likely-wrong initial
guess**: equal pieces (x_i = 1/(n+1) for all i) is numerically suboptimal for
Liu Bang — e.g. for n=1, equal split (1/2,1/2) only guarantees ≈0.5 against
Xiang's best uneven counter-split, vs. ≈0.667 for the geometric split (2/3,1/3).
Do not let the outliner default to "equal division is optimal" — it is not.

### Small-case / intuition notes (all CONJECTURED, numerically verified, not yet proven)
- **n=1**: solved exactly by hand (not just numerically). Liu Bang splits the
  stick into (2/3, 1/3). For ANY way Xiang Yu splits either of the resulting
  pieces with his one cut, Liu Bang's guaranteed total is exactly 2/3 (checked
  algebraically: median-of-three analysis shows Xiang's best response value is
  g(x) = max(1−x, x/2) for a Liu split (x,1−x), x≥1/2; this is minimized over x
  at x=2/3, where g=1/3, giving Liu Bang total 1 − 1/3 = **2/3**). So **c(1) = 2/3**,
  confirmed both by direct calculus/case analysis and by a 2M-sample numeric
  search (Bash script /tmp/n1_analysis.py, /tmp/n1_check.py).
- **n=2**: numeric search (grid over Liu's 3-piece configurations, random search
  over Xiang's cut placements with up to 20000 trials per candidate; scripts
  /tmp/n2_search.py, /tmp/n2_refine.py, /tmp/n2_exact.py) strongly suggests the
  optimal Liu configuration is the geometric split **(4/7, 2/7, 1/7)**, against
  which Xiang Yu's best response is to put BOTH of his cuts inside Liu's single
  largest piece (4/7) — no other allocation of Xiang's 2 cuts (splitting two
  different pieces, or splitting the 2nd/3rd-largest piece) beat this in any
  configuration tested, including near-geometric perturbations, which all scored
  strictly worse for Liu than the exact geometric point. Resulting value:
  **c(2) = 4/7** (conjectured, ~0.5714).
- **n=3**: same geometric family generalizes: Liu's config (8/15, 4/15, 2/15,
  1/15) with Xiang concentrating all 3 cuts on the top piece gives Liu Bang
  total = 8/15 (matches conjecture below); perturbations again scored strictly
  worse. Script: /tmp/n3_test.py.
- **Conjectured closed form**: **c(n) = 2^n / (2^{n+1} − 1)** (equivalently
  1 − 1/(2^{n+1}−1)). Matches n=1 (2/3), n=2 (4/7), n=3 (8/15) exactly.
  Confidence: MEDIUM-HIGH for n=1 (rigorous), MEDIUM for n=2,3 (strong numeric
  evidence via random search + perturbation checks, but not a proof that no
  other Liu configuration or Xiang strategy family does better — the search
  is not exhaustive over the continuum).
- **Self-similar/recursive structure** (conjectured): in the optimal
  configuration, Liu's declared pieces are x_i = 2^{n+1−i}/(2^{n+1}−1) for
  i=1..n+1 (geometric, ratio 1/2, largest first). Crucially, the tail
  (x_2,...,x_{n+1}), when rescaled to sum to 1, is *exactly* the optimal
  (n−1)-cut configuration. This recursive self-similarity is strong evidence the
  true proof is an induction on n where the inductive step is: "Xiang Yu's
  dominant strategy is always to spend ALL his cuts on Liu's single largest
  declared piece" (never split across multiple pieces) — this dominance held in
  every simulated instance (including asymmetric non-geometric Liu
  configurations tested, e.g. (0.6,0.35,0.05) for n=2). If this dominance lemma
  can be proven directly (e.g. via an exchange/majorization argument: moving a
  cut from a smaller piece to the largest piece never hurts Xiang and can only
  help), the problem reduces to a clean one-piece recursive subproblem, closely
  paralleling the aimo-0117 "largest value beats the sum of the rest" mechanism.
- **What is NOT yet established**: (a) a proof that geometric-ratio-1/2 is
  optimal for Liu Bang among ALL configurations (only checked against finitely
  many alternatives numerically); (b) a proof that Xiang Yu's optimal reply is
  always to concentrate on the single largest piece (checked in several
  instances but not proven in general — e.g. near-tied largest pieces might
  behave differently, worth double-checking edge cases); (c) the exact
  mechanism by which "Liu Bang's total = his single largest declared piece x_1"
  holds as an *equality* at optimum (this exact equality, observed in n=1,2,3,
  is suspicious/clean enough to be the right invariant to prove, likely via
  showing x_1 exactly dominates when the tail is optimally geometric, similar to
  2^j > 2^{j-1}+...+2^0 in aimo-0117).
