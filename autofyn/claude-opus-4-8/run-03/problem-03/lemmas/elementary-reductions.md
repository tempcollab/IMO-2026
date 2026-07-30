# Lemma DM (elementary Xiang reductions) — PROPOSED (round 6, smoothing-majorization)

**Statement.** In the stick-cutting game, let `S` be the current multiset of pieces (before some
of Xiang's marks are placed). Then Xiang can, with **one** additional mark, realize either:

- **DELETE `x`** (bisection): mark the midpoint of a piece `x ∈ S`, splitting it into `{x/2, x/2}`.
  The pair cancels by Lemma P, giving `D(S) ↦ D(S ∖ {x})`.
- **MATCH `(x, y)`** for two distinct pieces `x > y > 0` of `S`: mark the piece `x` at distance `y`
  from one end, splitting it into `{y, x−y}`. The new fragment `y` cancels the already-present `y`
  by Lemma P, giving `D(S) ↦ D((S ∖ {x, y}) ∪ {x−y})`.

If `x = y` the two equal pieces cancel at **zero** cost (Lemma P). A sequence of `≤ n`
non-degenerate DELETE/MATCH moves is a legal Xiang response using `≤ n` marks, and `D` of the
result is the alternating sum of the reduced multiset.

**Proof.** Each move places a single interior mark on one current piece (offset chosen from an end
so the mark avoids any measure-zero coincidence), hence uses one Xiang mark and is legal. In each
case the resulting full multiset contains a repeated value; certified Lemma P
(`D(T ∪ {v,v}) = D(T)`) deletes that pair without changing `D`. The stated image multiset is
exactly the full multiset with that pair deleted. Composing legal moves keeps `D` tracked exactly.
∎

**Use.** Recasts the *upper bound* (Xiang's side) as a finite combinatorial reduction game on the
multiset — no subset enumeration, no mass threshold, no convexity of the value function. Note this
is a *sufficiency* statement (these moves are legal and give an upper bound on the forced `D`); it
does **not** assert optimality of DELETE/MATCH responses (that is the separate VERT statement).

**Corollary (short-profile corrector, subsumes Lemma U0).** If a profile has `m ≤ n` pieces, Xiang
DELETEs all `m` of them with `m ≤ n` marks; the reduced multiset is empty, so `D = 0`. Hence the
upper bound is nontrivial only at full budget `m = n+1`.

Self-contained given certified Lemma P (`cancelling-pair.md`).

**Status:** CERTIFIED (round 6, proof-reviewer). Both moves are single interior marks producing a
repeated value that Lemma P cancels, giving the stated exact $D$-image; the response is a
*sufficiency* claim (legal + gives an upper bound on forced $D$), not an optimality claim, so no
extremality is smuggled in. Legality (mark distinctness) follows the same mechanism as the
already-certified `whole-tail-peel.md`. Statement is no stronger than proved.
