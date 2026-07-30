## imo-2026-03

Field for the ONE open wall, GAP L (lower bound, Case B). Target (all certified-equivalent):
`D̃(F) ≥ 1` ⇔ `E(F) ≤ 2^n−1` ⇔ `(△⋆) λ_(0,θ){M odd} ≥ 1−β`, for `F = ⊎_{j=0}^n π_j` a
refinement of the dyadic ladder `{1,…,2^n}` with `Σa_j ≤ n`, grand total `2^{n+1}−1`. Upper
bound is DONE/certified — untouched. Two far-apart NEW approaches; leader parked as machinery
home; two RETHINK slugs retired (lemmas banked).

---

vertex-integrality-parity: new  **(PRIMARY — dual of the certified upper bound)**
Target: `D̃(F) ≥ 1` for every feasible `F` (whole GAP L ⇒ whole problem).
Technique: extremal principle (piecewise-linear min at a vertex) + total-unimodular
integrality of the group-sum/ordering polytope + **parity of the odd dyadic total**. Imports
§9 restatement, `D̃ = Σ(−1)^{i−1}w_i ≥ 0`, Structure Lemma, Invisible-Pair Lemma.
Skeleton:
  1. `D̃` linear on each merged order-type cell ⇒ min over the feasible polytope `P_a` attained
     at a vertex of the refined polytope `Q_{a,σ}` — by piecewise-linear extremal principle.
  2. (B2) Vertices of `Q_{a,σ}` are INTEGRAL — group-sum rows (disjoint unit supports) stacked
     on ordering/nonneg difference rows (`±1`, network matrix) form a totally unimodular system
     with integer (dyadic) RHS.
  3. (C) At an integer config `D̃ = O−E ≡ O+E = Σ F = 2^{n+1}−1 ≡ 1 (mod 2)` is ODD; with
     `D̃ ≥ 0` (elementary, descending) an odd nonneg integer is `≥ 1`.
  4. Min over the finitely many cut-vectors `a` ⇒ `D̃ ≥ 1` universally.
Key lemmas (claim + mechanism):
  - Parity Lemma (heart): integer multiset + odd total ⇒ descending alternating sum is odd,
    so `D̃ ≥ 0` upgrades to `D̃ ≥ 1` — NON-LOCAL injection of the constant `1` via parity of
    `2^{n+1}−1`, invisible to every measure/profile framing (which only see `D̃≥0`, off by 1).
    VERIFIED: `0` bad over `1.7·10⁴` integer configs, `n≤4`, all cut vectors; min exactly 1.
  - Integral-vertex Lemma B2: TU of (partition rows) ⊕ (path network rows), integer RHS.
    Fallback: a fractional feasible point supports a cycle in the (groups × order-chain)
    constraint graph ⇒ not a vertex; so some integral vertex achieves the min value.
Open gaps: GAP-V1 = prove B2 (TU, or the cycle/exchange fallback) — THE ballgame; GAP-V2 =
  fully justify B1 (routine polyhedral geometry). (C) and `D̃≥0` proven.
Cases to cover: Case A (`a_0=0`) via C3; Case B (`a_0≥1`) via B2+C uniformly — no sub-cases.
Watch out for: optimum is a FLAT FACE (continuum), so claim integrality of ONE vertex of the
  optimal face, not uniqueness; parity needs ALL parts integral (B2 not optional); do NOT
  weaken (C) to `D̃≥0` (that is the trivial off-by-1 bound).
Numerics done: min over each `P_a` is an odd integer attained on an integer-containing face
  (e.g. `n=3, a=(1,0,1,0)`: min `D̃=3`); global min `1` (tie config n=4 (8,3,3,2)/(8,2,2,2,1)).

---

peel-scale-rank-induction: new  **(SECOND — far apart: induction on n, not extremal)**
Target: `O(F) ≥ 2^n` ⇔ `D̃(F) ≥ 1` (whole GAP L).
Technique: strong induction on `n` peeling the TOP dyadic scale `π_0`; rank-shift/insertion
accounting of `O` under inserting a total-`2^n` block into `F'` (refinement of `{1,…,2^{n−1}}`,
IH `O(F')≥2^{n−1}`); constant `+1` from dyadic dominance `2^n = 1+Σ_{k<n}2^k` spent once.
Skeleton:
  1. §9 target; IH `O(F')≥2^{n−1}` (`F'=⊎_{j≥1}π_j`, budget `≤n−1`).
  2. Case A (`a_0=0`): uncut `2^n` is rank-1 odd ⇒ C3.
  3. Case B: insert `π_0`'s `a_0+1` parts into sorted `F'`; each insertion at rank `r` toggles
     tail parity + adds `(−1)^{r−1}p`; Rank-Shift Key Lemma ⇒ `O(F)−O(F') ≥ 2^{n−1}`.
  4. `O(F)≥2^n` ⇒ done.
Key lemmas (claim + mechanism):
  - Rank-shift insertion identity: `D̃(F)−D̃(F')` as explicit function of insertion positions;
    each inserted part flips the sign of the straddled `F'`-tail (telescopes to partial sums) —
    the "whole-scale" analogue of the leader's `(♠)` Abel identity.
  - Dyadic dominance `2^n = 1+Σ_{k<n}2^k` (aimo-0117/0019): arithmetic origin of the `+1`.
  - Invariant I `M(0⁺)=(a_0+1)−|F'| ≤ 1` (joint, bottom-inclusive): seeds the near-0 band.
  - STRENGTHENED (loaded) IH: a shape invariant on `F'` (near-0 odd/even profile majorization,
    or prefix `Σ_{i≤2k}(−1)^{i−1}w_i≥0`) inherited by `F'` and forcing the insertion surplus.
Open gaps: GAP-P1 = Rank-Shift Key Lemma with the correct LOADED IH (main risk: plain IH too
  weak); GAP-P2 = Invariant I (one-line counting) wired to the near-0 base; GAP-P3 = Case A/base.
Cases to cover: Case A (`a_0=0`), Case B (`a_0≥1`); optionally split `y₁>θ` vs `y₁≤θ` via `(△)`.
Watch out for: plain IH under-powers the step — the loaded invariant MUST be stated and shown
  inherited; `π_0` parts can land deep in `F'` (handle any depth); NO monotone reserve /
  per-threshold domination (refuted both directions); NO scalar summary of `F'`.

---

induction-recursion-telescope: advance (park — machinery home, no new build this round)
Rationale: leader owns every certified reduction the two new slugs import — `(△)`, `(△⋆)`,
`(♠′)`, `(⊞)`, `(△△)`, Structure Lemma §5, §9 restatement, Lemma T. Its own route
(merged-order telescoping DOWN Z's tree, bounded-window tiling) is R8-exhausted (proven
circular). Do NOT rebuild it on the same wall. It stays LIVE and imported; no builder needed
until one new framing needs a banked lemma extracted.

cut-sequence-potential: retire (RETHINK, banked)
Reserve⇔Target Equivalence certified (`lemmas/reserve-target-equivalence.md`); sequential
family provably equivalent to target — no leverage. Note it does NOT prune static structural
insertion invariants (peel-scale slug is safe). Lemma banked; no re-plan.

even-rank-doublecount: retire (RETHINK, banked)
`(⊞)` scale-XOR reformulation certified (`lemmas/scale-parity-xor.md`); genfn engine refuted.
Retired for now; `(⊞)` available if a per-scale ledger is revisited later.

---

RECOMMENDED BUILD SET: vertex-integrality-parity, peel-scale-rank-induction

Both are complete rival attempts at the WHOLE GAP L (each closes the problem), far apart in
mechanism (extremal-integrality-parity vs peel-scale insertion induction), neither caught by
the R8 equivalence meta (both are non-local: parity of the odd total / static insertion
invariant — not measure/merged-order/sequential/genfn profiles of the final multiset). The
primary (vertex-integrality-parity) has a numerically confirmed, single, crisp remaining gap
(integral vertices, GAP-V1) whose closure ends the problem via a one-line parity step; prioritise
its builder. induction-recursion-telescope stays live as the machinery source both import.
