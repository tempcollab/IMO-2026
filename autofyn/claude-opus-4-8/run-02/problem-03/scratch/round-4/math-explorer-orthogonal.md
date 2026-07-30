## imo-2026-03 — orthogonal-framing scouting report

**Task**: find a route to the WHOLE problem genuinely far from the D-level-measure /
concavity / separable-potential framing that both live approaches (dyadic-discrepancy,
induction-recursion) share, per the R2 outline-reviewer diversity flag.

### Candidate 1 — "scale-invariance / strategy-embedding recursion via 1/c(n)"

**Mechanism.** `1/c(n) = 2 - 2^{-n}` exactly (verified symbolically for n=1..7 with exact
fractions — see below), i.e. the "gap to 2" halves each round: `g(n):=2-1/c(n) = 2^{-n} =
g(n-1)/2`. This is clean enough to suggest a *direct* game-tree embedding: Liu marks a
single point splitting the stick into a top piece of length `c(n)` and a remainder `R` of
length `1-c(n)`; if Xiang never touches the top piece, global ranking puts the top piece
at rank 1 (Liu's), and *Xiang* becomes the effective first-mover on the remainder's own
internal ranking (rank-2-global = remainder's-own-rank-1). So Liu's guaranteed total
becomes `1 - V(R)` where `V(R)` is the (n-1)-cut subgame's value played on `R` with Xiang
moving first.

**Verdict: NOT orthogonal — I verified algebraically it is exactly the SAME recursion
`induction-recursion` already has.** Solving `1/c(n)=1+1/(2c(n-1))` gives
`c(n)=2c(n-1)/(2c(n-1)+1)`, and translating to the certified `u_n` normalization gives
`u_n = u_{n-1}/(2+u_{n-1})` — literally the recursion already recorded in `current.md` /
`induction-recursion`'s own derivation. The embedding argument I sketched IS the top/bottom
block decomposition already in play, and it hits the identical wall: it only closes when
Xiang doesn't cut the top piece (Case A, already done) or cuts it in a dominated way (Case
B, GAP L) — the "balanced regime" (top piece comparable to the rest) is exactly GAP L/GAP U
again, now just re-derived instead of re-solved. **Do not present this to the outliner as a
new approach — it is the same wall in different clothes.** (Numerically confirmed the
identity `g(n)=2^{-n}` is exact — this is a nice presentational fact for whichever approach
eventually closes the recursion, but it buys no new leverage on the balanced case.)

### Candidate 2 — surrogate-adversary domination (crux `aimo-0560`)

**Crux move found**: `aimo-0560` (gardener/lumberjack majestic-tree game) uses "replace the
adversary with a strictly stronger surrogate whose reply is pointwise at least as damaging,
so a win against the surrogate transfers down" — i.e., don't analyze the true optimal
adversary; construct an explicit, easier-to-analyze surrogate strategy that provably
dominates (is at least as good for the adversary, pointwise) and show the guarantee holds
against the surrogate.

**Assessment for GAP U**: this is *exactly* the shape of what dyadic-discrepancy is already
attempting (an explicit, non-optimal, hopefully-good-enough Xiang strategy: bisect / pin /
free-delete ops via the Residual-Total reduction) — the R3 build report already shows this
constructive-surrogate route is *insufficient in the balanced regime* (any "remove-max-total"
greedy surrogate telescopes to `2/((k+1)(k+2)) > u_k` for `k≥3`, and the true optimal beats
this by being non-greedy). So the surrogate-strategy idea is not new in kind; what's missing
is a smarter surrogate specifically calibrated to the balanced regime (a `β`-dependent
strengthened potential `ψ(k,β)`, as dyadic-discrepancy's own "spec concerns" section already
flags), not a different top-level framing. **Not independently orthogonal — same wall,
already-identified fix direction (the `ψ(k,β)` potential), which the outliner should treat
as advancing dyadic-discrepancy, not opening a new slug.**

### Candidate 3 — binary/2-adic combinatorial recasting (crux `aimo-0225`)

**Crux move found**: `aimo-0225` (triangle-area game on an n-gon) recasts a continuous
geometric monotonicity condition as *pure arithmetic on an integer arc-length multiset*
`(a,b,c)`, then determines the game's P/N value by recursing on `v_2` of a difference that
exactly halves at each step. This is a genuinely different STYLE (integer/2-adic recursion
on a finite invariant, not a continuous measure-theoretic discrepancy) from anything in the
live field.

**Why it's tempting here**: the dyadic extremal partition (piece ratios `1:2:4:...:2^n`) and
the clean `2^{-n}` gap strongly suggest an underlying binary/Zeckendorf structure. If the
game could be re-encoded so that "Liu's guarantee" reduces to a statement about `v_2` of some
integer quantity attached to the mark configuration (rather than a continuous Lebesgue
measure of an odd-level-set), the balanced-regime obstruction (which is fundamentally about
continuous interleaving of nearly-equal real-valued pieces) might dissolve into a parity
statement.

**Honest caveat — I did NOT find a concrete encoding.** The obstacle: Liu Bang's and Xiang
Yu's marks are arbitrary REALS, not confined to a dyadic grid a priori (the dyadic partition
is only the conjectured OPTIMAL Liu strategy, not a structural constraint on the game). So
unlike `aimo-0225` where the state space is intrinsically an integer arc-length triple, here
any binary recasting would have to first prove (not assume) that WLOG marks can be taken
dyadic — which is close to circular (proving optimality of the dyadic structure is most of
GAP U itself). I could not produce a discretization argument that doesn't smuggle in the
answer. **Rate this candidate as the most genuinely orthogonal in flavor, but currently
speculative / unconstructed — worth flagging to the outliner as a research direction, not a
ready mechanism.** A concrete sub-question worth assigning: can one show that Xiang's
optimal response to ANY Liu partition can be taken WLOG to only ever bisect or make "clean"
splits at a scale governed by `v_2` of a rank-count, i.e. is there a "rounding" argument
(perturb any Liu partition towards a dyadic one without decreasing Liu's guarantee, and
perturb any near-optimal Xiang response towards clean binary splits without increasing
Xiang's damage) that would justify reducing the continuous problem to the discrete one?
This is untested and NOT verified numerically this round (ran out of scope) — flag as an
open research question, not a result.

### Candidate 4 — quadratic-weighted discrepancy (my own probe, inconclusive)

I tested numerically (n=2, restricted to ≤2 total cuts across 3 Liu pieces, Nelder–Mead
inner search) whether a quadratic-weighted analogue `D_2 := Σ(-1)^{i+1}b_i^2` behaves more
tractably (e.g., convex/concave where linear `D` is not). Small numeric probe (`/tmp/round-4/
check2.py`) showed `D_2` at a midpoint of two random partitions was close to but not cleanly
above/below the average of the endpoints — **inconclusive, not pursued further**; more
importantly `D_2` is not the quantity the reduction was built on (Lemma G's odd-rank identity
is linear, specific to the actual claiming game), so even if `D_2` were nicely convex it
would not directly answer the problem. **Do not pursue; not promising, would need its own
reduction proof from scratch with no payoff shown.**

### Ranking of orthogonal candidates (most to least promising)

1. **Candidate 3 (binary/2-adic recasting)** — genuinely different in kind from D-language,
   matches the clean `2^{-n}` structure and the crux-corpus precedent (`aimo-0225`), but
   unconstructed; real risk it can't avoid re-proving dyadic-optimality first.
2. **Candidate 2 (surrogate-adversary)** — same wall as dyadic-discrepancy's current attack;
   useful only as a naming/reframing of the already-flagged `ψ(k,β)` fix, not a new slug.
3. **Candidate 1 (scale-invariance recursion)** — confirmed algebraically identical to
   induction-recursion's existing recursion; contributes nothing new (but the clean identity
   `1/c(n)=2-2^{-n}` is a nice fact to cite once a bound is proven).
4. **Candidate 4 (quadratic discrepancy)** — inconclusive numeric probe, no clear path.

### Cheap-kill / sanity notes
- `1/c(n) = 2 - 2^{-n}` exactly, for all n (proven trivially by algebra from the known
  closed form — not new information about the hard direction, just a clean restatement).
- Confirmed (again) that both live approaches' derived recursion `u_n=u_{n-1}/(2+u_{n-1})`
  is consistent with this identity — no contradiction, but no new leverage either.

### Recommendation to the outliner
Do not spend a build slot re-deriving Candidate 1 (it's proven identical to
induction-recursion's existing recursion) or Candidate 2 as a "new" slug (it's dyadic-
discrepancy's own flagged fix, i.e. an argument FOR advancing that approach with the
`ψ(k,β)` potential, not a rival). If a genuinely new slug is wanted this round, Candidate 3
(binary/2-adic recasting, inspired by `aimo-0225`'s v_2-recursion crux) is the only
candidate here that is structurally different from the D-level-measure framing — but flag
it honestly as unconstructed and carrying a real risk of circularity (it may need to assume
what it's trying to prove). An alternative, lower-risk recommendation: since neither wall
(GAP U's balanced regime, GAP L's joint interleaving) has a genuinely different framing that
avoids re-encountering the same combinatorial obstruction, it may be more productive to
accept that a fully orthogonal top-level framing does not exist for this problem, and
instead have the two live approaches attack the SAME identified sub-obstruction — the
balanced/near-equal-top-pieces case — with the specific new tool each currently lacks
(dyadic-discrepancy's own-flagged `ψ(k,β)` balance-crediting potential; induction-recursion's
own-flagged rank-interleaving/merged-order invariant) rather than opening a cosmetically
different but mechanically identical third approach.

## Analogous past problems (cruxes)
- `aimo-0225` — triangle-area game recast to integer arc-lengths, P/N determined by parity of
  a halving `v_2`. Analogous in FLAVOR (dyadic halving structure) but not in mechanism (no
  known reduction of our continuous marks to an integer state space yet).
- `aimo-0560` — surrogate-adversary domination for an upper-bound guarantee in a two-player
  alternating game. Analogous in GOAL (constructing a good-enough, easy-to-analyze Xiang
  strategy) but the mechanism dyadic-discrepancy is already using is essentially this same
  idea, already tried and found insufficient in the balanced regime.
- `aimo-0117` (from R1 memory) — "largest value exceeds sum of all others" dyadic/geometric
  claim-game crux, already exploited in R1 for the initial dyadic conjecture; not further
  useful here since it doesn't touch the balanced-regime obstruction.

## Prior progress (unchanged this round, confirmed)
Certified spine (Lemma G, level-measure identity, cut-flip/cut-budget/domination, reduction
`c(n)=(1+D*)/2`, `D*=u_n`), n=1 fully solved, lower-bound Case A done. GAP U (upper, general
n, balanced regime) and GAP L (lower, Case B doubly-balanced overlap) both open, both
numerically true but unproven, both traced by their respective builders (R3) to a SPECIFIC
missing tool (`ψ(k,β)` potential for GAP U; joint rank-interleaving invariant for GAP L) —
not to a wrong top-level framing.

## Dead ends (do not retry)
- Global concavity of `f=min_Xiang D` over the Liu simplex — REFUTED (R2 outline-reviewer,
  12/60 random midpoint violations, confirmed with 120-restart re-optimization).
- Separable per-piece potential certifying the odd-rank functional — REFUTED
  (potential-certificate, R1/R2, LP infeasibility).
- Bisection-only or myopic-greedy Xiang strategies — REFUTED (R1).
- Greedy "remove-max-total" (gap-greedy) as a complete GAP U mechanism — REFUTED this round
  by dyadic-discrepancy's own build (telescopes to `2/((k+1)(k+2))>u_k` for k≥3; true optimal
  is provably non-greedy in the balanced regime).
- Strict domination `W(n-1,b)>u_{n-1}` for GAP L — REFUTED (R2), only non-strict holds.
- "Confine `O_Z`/`O` to a high region" as a route to close GAP L — REFUTED this round
  (induction-recursion R3: already at n=1 the odd-set reaches arbitrarily close to 0, so no
  one-sided location confinement is possible; the missing fact is intrinsically joint).
- **NEW this round**: the "scale-invariance recursion via `1/c(n)=2-2^{-n}`" embedding —
  confirmed algebraically IDENTICAL to induction-recursion's `u_n=u_{n-1}/(2+u_{n-1})`
  recursion; not a new approach, do not open a slug for it.

## Small-case / intuition notes
- `1/c(n) = 2-2^{-n}` exactly for n=1..7 (exact-fraction verification, `/tmp/round-4/
  check1.py`) — a proven algebraic fact about the conjectured closed form, not new evidence
  about the unproven direction.
- Quadratic-weighted discrepancy probe (n=2, restricted cut budget) gave no clean
  convexity/concavity signal — labeled a conjecture-free, inconclusive numeric experiment,
  not pursued further (`/tmp/round-4/check2.py`).
