# Lemma X (elementary exchange move effect) and the move-trap negative result (certified, round 5)

Source: `geometric-dominance-construction.md`, "Round 5 — testing the
exchange argument." Independently re-verified by the proof-reviewer: Lemma X
against 10,000+ random exact-integer trials (zero mismatches); the specific
move-trap `n=5, a=(0,2,4,0,0)` against an exhaustive from-scratch
re-implementation (all `C(5,3)=10` index triples, both move directions —
confirmed a genuine trap, `D=11`, no legal single elementary move decreases
it); the width-2 escape `(0,2,4,0,0) → (1,0,3,2,0)` (`D: 11 → 7`) confirmed
by direct recomputation.

## Setting

Same as `lemmas/parity-pair-lemma-L.md`: `t_i = 2^{n-i}`, feasible integer
vectors `a` satisfy `Σa_i = n+1`, `Σ a_i t_i = 2t_1`.

## Lemma X (exact effect of the consecutive elementary move on `D`)

**Statement.** For the consecutive elementary move at indices `(i-1,i,i+1)`
(`2 ≤ i ≤ n-1`), i.e. `a_{i-1} += 1, a_i -= 3, a_{i+1} += 2` (the unique
primitive integer move on 3 consecutive coordinates preserving both linear
constraints, since `t_{i-1}=4t_{i+1}, t_i=2t_{i+1}`), applied to a feasible
`a` with `a_i ≥ 3`, the resulting `a'` satisfies
```
D(a') - D(a) = (-1)^{a_{i-1}+1} · (-1)^{C_{i-2}(a)} · t_i,
```
where `C_{i-2}(a) = (i-2) + Σ_{j<i-1} a_j`. In particular `|D(a')-D(a)| =
t_i` exactly, and the reverse move applied to the same `a` (when legal)
changes `D` by the identical signed amount as the forward move.

*Proof.* Direct case tracking of the three affected blocks' prefix-sum
parities and odd/even-multiplicity indicators; see the approach file for the
full derivation. Independently confirmed by 10,000+ random exact-integer
trials (`n` up to 12), zero mismatches.

## Move-trap negative result

**Fact.** `n=5`, `a=(0,2,4,0,0)` is feasible (`Σa_i=6=n+1`,
`Σa_i t_i = 2·8+4·4 = 32 = 2t_1`), `D(a)=11 ≫ t_5=1`, and is a **move-trap**:
exhaustively checking all `C(5,3)=10` index triples and both directions of
the primitive elementary move at each, every legal resulting vector has
`D ≥ 11` (no strict decrease). Further traps exist at `n=6,7,8` (see approach
file). A width-2 composed move escapes this specific trap:
`(0,2,4,0,0) → (1,0,3,2,0)`, `D: 11 → 7`; larger traps at `n=7,8` require
composed-move width 3 and 4 respectively (numeric only, not proved to be
bounded in general).

**Consequence (negative result, certified).** The natural conjecture "single
elementary exchange move, canonical vector is the unique local-hence-global
minimum by connectivity" is **false** as stated for the minimal notion of
local move — genuine local minima away from the canonical vector exist. Any
future exchange-argument proof of Lemma L must use unboundedly-wide composed
moves (width growing with `n` in the tested range), not a bounded local-move
argument. Do not re-attempt a bounded-width single-exchange-move proof of
Lemma L / the doubling-family conjecture without addressing this obstruction.
