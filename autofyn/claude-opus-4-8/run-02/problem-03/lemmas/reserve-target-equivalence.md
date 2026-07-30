# Lemma (Reserve⇔Target Equivalence — sequential-monovariant obstruction) — CERTIFIED round 8

**Source:** approaches/cut-sequence-potential.md §2.
**Reviewer status:** verified (standard value-function / amortized-potential argument;
re-derived independently; the DP recursion `minreach(P,b)=min(D̃(P), min_{P→P'} minreach(P',b−1))`
and the four admissibility checks are correct).

## Setup
Dyadic root `F_0={1,…,2^n}`. A cut replaces one part `L` by `(x,L−x)`. For a config `P` and
budget `b`, `minreach(P,b):=min{D̃(Q): Q reachable from P by ≤b cuts}`. An **admissible reserve**
is `R:(config,budget)→ℝ_{≥0}` with (R0) `R(·,0)=0`; (R1) `R(P,b)−R(P',b−1)≥D̃(P)−D̃(P')` for
every legal cut `P→P'`; (R2) `R(F_0,n)≤D̃(F_0)−1`; (R3) `R≥0`.

## Statement
An admissible reserve exists **iff** the GAP-L target `(T)` holds (`D̃(F)≥1` for every ≤n-cut
response). Moreover the value-function reserve `R^*(P,b):=D̃(P)−minreach(P,b)` is the canonical
admissible reserve, and every admissible reserve is forced root-tight `R(F_0,n)=D̃(F_0)−1`.

## Proof
(⇐) Given `(T)`: `R^*` satisfies (R0) (`b=0` ⇒ `minreach=D̃`), (R3) (`minreach≤D̃`),
(R1) (from `minreach(P,b)≤minreach(P',b−1)`), and (R2) (`minreach(F_0,n)≥1` is exactly `(T)`).
(⇒) Telescoping (R1) along any ≤n-cut sequence and applying (R2),(R3) gives `D̃(F)≥1`. ∎

## Reuse / consequence (obstruction)
The amortized monovariant over Xiang's ordered cut sequence is **logically equivalent** to the
theorem it aims to prove — it carries **no independent deductive leverage**. Any admissible
reserve is a root-tight upper bound on the maximal remaining drop `R^*`; the only way the program
yields a proof is an explicit closed-form reserve with a *locally* verifiable (R1). Concretely
`R^*` is NOT a function of `(D̃,b)` (same `(11,1)`→`{6,7,8}` at n=4) and `R^*(F_0,b)` is strictly
concave (`0,6,8,10,10` at n=4), so coarse and summed-magnitude/budget-count reserves fail. This
prunes the entire sequential-count/potential family (incl. the retired `induction-recursion`).
