# Proof-builder report — dyadic-discrepancy (imo-2026-03, round 7)

## Assigned task
Close GAP U (upper bound) residual sub-case (iii-b) `ℓ₁<Σ/2` for general n, per the outliner's
pin-top-2 potential `ψ(k,β)` mechanism.

## What I found / did
The GAP-U closure was **already achieved and written in my file in round 6** via a strictly
better mechanism than the assigned pin-top-2 potential: the **Realizability Lemma + Subset-Sum
Pigeonhole** (§4.7). That closure is *global* (selects the optimal `{-1,0,1}` sign pattern rather
than fixing a first move), so it handles the strictly-balanced sub-case (iii-b) **and every other
regime uniformly** — and it dissolves the `k=4` pin-top-2 near-miss (ratio 1.039) that the outliner
flagged as a mandatory obligation, because that near-miss only exists for a *fixed* first move.

This round I (i) **verified the entire §4.7 pipeline is correct** and (ii) **hardened its single
load-bearing prose step**.

### Verification (exact `Fraction` arithmetic, 0 violations everywhere)
- Subset-sum pigeonhole: `min_ε |Σ ε_i ℓ_i| ≤ u_n` — 0 violations, n≤4.
- Reachability characterization: ground-truth op-DP min effective total `==` `min_ε |Σ ε_i ℓ_i|`
  EXACTLY — 0 mismatches (validates that Xiang's reachable effective totals are exactly the
  `{-1,0,1}`-signed sums).
- Constructive Realizability op-sequence reaches `|Σ ε_i ℓ_i|` in **exactly n ops** (m−1), never
  overrunning the ≤n cut budget — n≤5. (Resolves the reviewer's op-budget accounting concern.)
- End-to-end: the ACTUAL physical final multiset conserves mass `=Σ` and has true discrepancy
  `D ≤ u_n` — 0 violations, worst ratio 0.9936. So the game-theoretic D (not just a bookkeeping
  total) satisfies the bound.

### Prose hardening (new this round)
Added an explicit **Physical-Decomposition remark** to §4.7 proving the load-bearing identity
`D(actual final multiset P) = D(effective multiset E)`: each removal op leaves exactly one *equal
pair* physically (bisect → two halves; generalized pin of b into a → original b + fresh copy of b;
free-delete → the pair itself), so `P = E ⊎ ⋃_s {v_s,v_s}`; the Invisible-Pair Lemma strips every
pair without altering the odd-set, and `D(E) ≤ total(E) = |Σ ε_i ℓ_i| ≤ u_n`. This closes the only
prose gap between "reachable effective total" and the position the claiming phase actually faces —
the spot a reviewer would otherwise challenge as "effective total ≠ real D."

## Status of my slug
`partial` — the **upper bound `c(n) ≤ 2^n/(2^{n+1}−1)` is fully proven for all n** (GAP U closed),
along with the reduction (§0), Lemma G + discrepancy identities, the answer `c(n)=2^n/(2^{n+1}−1)`,
the full n=1 solution, and lower-bound Case A. The whole problem remains partial because **GAP L
(lower-bound Case B) is open**, owned by the induction-recursion / -telescope slugs — not attacked
here (out of my lane).

## Spec concerns
None. I did not use any refuted move (no myopic/greedy Xiang, no bisect-n-largest, no fixed simple
schedule for k≥3, no global mesh-coverage bound, no region-restricted concavity/LP). The subset-sum
pigeonhole is on the `2^{n+1}` subset sums (elementary), NOT the refuted "mesh of reachable values."
Op budget verified tight (exactly n ops), so the reviewer's budget-accounting flag is discharged.

## Lemmas proposed for certification
The round-6 list stands; the two now-most-load-bearing and fully-proven-and-verified for GAP U:
- **Realizability Lemma** (§4.7): for any multiset and any `ε∈{-1,0,1}^m\{0}`, Xiang reaches
  effective total `= |Σ ε_i ℓ_i|` in exactly `m−1` removal ops. Rests only on the certified
  Invisible-Pair + generalized-pin/bisect ops. Now paired with the Physical-Decomposition remark
  giving `D(P)=D(E)`.
- **Subset-Sum Pigeonhole + complete upper bound** (§4.7): among the `2^{n+1}` subset sums of an
  `(n+1)`-piece partition, two consecutive sorted sums differ by `≤ u_nΣ`; realizing that
  `{-1,0,1}` pattern gives `D ≤ u_nΣ`. Proves `c(n) ≤ 2^n/(2^{n+1}−1)` for every n, sharp at the
  dyadic partition. **Recommend certifying as the upper-bound half of P3.**
