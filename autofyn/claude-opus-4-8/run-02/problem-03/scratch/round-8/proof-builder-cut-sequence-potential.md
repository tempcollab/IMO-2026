# Build report — cut-sequence-potential (imo-2026-03, GAP L) — R8

**Status: partial (RETHINK-leaning). The reserve did NOT collapse to summed-magnitude — it
failed for a deeper structural reason, which I proved.**

## What was built (rigorous)
- Framework over Xiang's ordered cut sequence using the EXACT Cut-Flip toggle set
  `S=[0,x)∪[L−x,L)`: per-cut law `ΔD̃ = λ(S) − 2λ(S∩O)` (certified geometry, not magnitude).
- Base value `D̃(F_0)=(2^{n+1}+(−1)^n)/3 ≥ 1` (verified n=1..5: 1,3,5,11,21).
- Amortized reduction: an "admissible" reserve `R` (nonneg, `R(·,0)=0`, `R(F_0,n)≤D̃_0−1`,
  one-cut charging `R(P,b)−R(P',b−1)≥drop`) ⇒ target `D̃(F)≥1`.

## The core finding — Equivalence Theorem (proved, promotable)
An admissible reserve exists **iff** the GAP-L target holds. Both directions proved:
- (⇐) the value-function reserve `R^*(P,b)=D̃(P)−minreach(P,b)` is admissible (one-cut inequality
  verified 0/200 random instances, `/tmp/exp5.py`);
- (⇒) telescoping the one-cut inequality gives `D̃(F)≥1`.
Consequence: the sequential monovariant carries **no independent leverage** — it is logically
equivalent to the theorem. Any admissible reserve is forced root-tight `R(F_0,n)=D̃_0−1`, i.e. a
root-tight upper bound on the maximal remaining drop. The value-function reserve is vacuous.

## Why the explicit reserve is dead (guardrail check)
- Coarse reserves fail: `R^*` is NOT a function of `(D̃,b)` — same `(11,1)` gives `R^*∈{6,7,8}`
  (`/tmp/exp3.py`). Must use full geometry.
- Summed-magnitude / linear-in-budget reserves fail (the REFUTED budget-count): `R^*(F_0,b)` is
  strictly concave — n=4: `0,6,8,10,10` (increments `6,2,2,0`), not `b·const` (`/tmp/exp4.py`).
  So the guardrail's collapse mode is confirmed dead, AND avoided (I used exact geometry).
- Max single-cut drop `= max(2λ(S∩O)−2x)` has no telescoping closed form; by the Equivalence
  Theorem any such form is as strong as the theorem itself.

## Recommendation
RETHINK / de-prioritize this slug. The Equivalence Theorem also explains why the retired
`induction-recursion` (sequential budget-count) died — the WHOLE sequential family is equivalent
to GAP L. Push the field onto the two framings that route through a DIFFERENT object:
`induction-recursion-telescope` (merged-order block-tiling `Σψ(c_i)Δw_i≥0`) and
`even-rank-doublecount` (static `E(F)≤2^n−1`). If both stall, the theorem says: open a genuinely
new framing (e.g. LP/entropy relaxation of `E(F)≤2^n−1`), not another sequential monovariant.

## Files
- Approach: /home/agentuser/repo/results/imo-2026-03/approaches/cut-sequence-potential.md
- Scripts: /tmp/exp1.py (base), /tmp/exp2.py (minreach DP), /tmp/exp3.py (coarse-reserve
  refutation), /tmp/exp4.py (concavity/budget-count refutation), /tmp/exp5.py (R* admissibility).
