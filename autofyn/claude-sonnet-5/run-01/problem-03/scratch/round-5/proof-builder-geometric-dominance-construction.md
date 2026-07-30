# Build report — geometric-dominance-construction, round 5

## Task
Attempt to prove the general doubling-family conjecture (all `k`, the `k≥2`
lower-bound gap) via a single-unit exchange/local-move argument on the
composition vector, as scoped by this round's outliner, with the
outline-reviewer's mandate to derisk numerically first (since the target,
Lemma L at `k=n`, is the same statement `recursive-embedding-induction` was
attacking in parallel via peel-induction).

## Outcome: Status remains `partial`. Genuine negative + methodological result on the exchange route; Lemma L closed by the sibling approach mid-round.

### What I did
1. Set up the exact finite-combinatorial framework for Lemma L (imported
   from `recursive-embedding-induction`'s Lemma V' reduction, not
   re-derived): integer vectors `a=(a_1,...,a_n)`, `Σa_i=n+1`,
   `Σa_it_i=2t_1`, `t_i=2^{n-i}`, target `D(a)≥t_n`.
2. Re-derived and independently verified (2000+ exact trials) the
   **block-parity formula** for `D`.
3. Derived the **minimal legal "single-unit exchange" move** exactly: since
   there are *two* linear constraints (count and value) to preserve, the
   null space forces a 3-index move, not a 2-index one — for consecutive
   indices `(i-1,i,i+1)` the unique primitive generator is `(+1,-3,+2)`
   (using `t_{i-1}=2t_i=4t_{i+1}`).
4. Proved **Lemma X** (fully, in closed form, after catching and fixing one
   algebra slip mid-derivation): the exact effect of this move on `D` is
   `ΔD=(-1)^{a_{i-1}+1}(-1)^{C_{i-2}}t_i`, and — a genuinely
   counter-intuitive fact — the *reverse* move (subtracting the same
   generator) changes `D` by the *same* signed amount, not the negative.
   Verified against 2000 exact-integer trials, zero mismatches.
5. **Exhaustively searched** (not sampled) for "move-traps": feasible
   vectors from which *no* single elementary move — at any index triple,
   consecutive or not, either direction — strictly decreases `D`. Found
   explicit, verified traps starting at `n=5` (e.g. `a=(0,2,4,0,0)`,
   `D=11≫t_5=1`), with more traps at `n=6,7,8`. This is a genuine
   falsification of the outline's literal "single-unit exchange, canonical
   is unique local⇒global min by connectivity" claim.
6. Tested whether **composed** (multi-generator) moves rescue the argument:
   yes for every tested trap, but the required composition width grows with
   `n` (width 2 at `n=5,6`; width 3–4 at `n=7,8`), so no bounded-width local
   exchange argument suffices — the mechanism is not actually simpler than
   a full recursive argument.
7. Mid-round, discovered that `recursive-embedding-induction` had
   **independently proved Lemma L in full** this same round (via peel
   induction / Lemma PARITY-PAIR, a strictly more general statement dropping
   the value constraint). Updated my approach file to import this by
   reference (per the coordination directive) rather than continue chasing
   the now-known-insufficient exchange route, and to correctly re-scope
   this approach's remaining unique contribution: extending from `k=n` to
   general `k<n` **with the tail simultaneously refined**, still open,
   gated on a not-yet-built generalization of Lemma V'.

### Why Status stays `partial`, not `solved` or `unsolved`
Real, rigorous progress this round: a new general lemma (Lemma X, fully
proved) and a real negative result (move-trap non-existence of a bounded
exchange proof), both reusable and both honestly scoped. But the round's
assigned target (closing `k≥2` via exchange) was not achieved by this
approach's own mechanism — it was achieved in parallel by
`recursive-embedding-induction`. The overall lower-bound theorem is still
not fully proved by any approach (general `k<n` with simultaneous tail
refinement remains open), so `partial` is the honest status.

## File updated
`/home/agentuser/repo/results/imo-2026-03/approaches/geometric-dominance-construction.md`
— new "Round 5" sections added (coordination update + full exchange-argument
attempt with Lemma X, the move-trap negative result, and the honest
conclusion), `Approaches tried` and `Current best` updated at the top,
`Promotable lemmas (round 5 additions)` appended at the end.

## Promotable lemmas proposed this round
- **Lemma X (elementary exchange move effect formula)** — fully proved,
  general-purpose for Lemma L's combinatorial lattice; reusable by any
  approach doing further local-move analysis there.
- **Move-trap negative result** — an explicit, exhaustively-verified
  falsification of the bounded single-move exchange mechanism for Lemma L;
  worth certifying to prevent any future round from re-attempting the same
  falsified strategy.

Both are documented in the approach file's new "Promotable lemmas (round 5
additions)" section for the reviewer to certify if judged reusable.
