# Lemma ONE-REC (recursed dyadic dichotomy) — CERTIFIED (round 9)

**Certification (round 9).** Reviewer-verified. (i) is the partition-of-cuts identity: fragments of
pieces `2^0..2^ℓ` form a self-contained refinement of `C_ℓ`, cut count `Σ_{j≤ℓ}(|G_j|−1)` — correct.
(ii) two fragments of `G_j` each `>2^{j−1}` would sum to `>2^j=ΣG_j` — correct; applying certified
Lemma ONE to `B_{≤ℓ}` (a refinement of `C_ℓ` by (i)) gives ≤1 piece `>2^{ℓ−1}` — correct; `N_B(τ)`
additivity over disjoint `G_j` — correct. Claims nothing beyond (i),(ii); does NOT close GAP
MID-core (honestly noted). Ladder-litmus (excludes `F={½,½,½},B={½}`) valid. Admitted.


**Purpose.** The field-wide "Lemma ONE recursed down every dyadic sub-ladder" dependency (used by
BOTH walls: parity-measure caps per-scale F-excess; breakpoint-vertex the scale bands). This lemma
gives its correct, true form and reduces it to certified Lemma ONE (`top-scale-dichotomy`) plus an
elementary partition-of-cuts identity. It is NOT the refuted "≤1 O_B-interval per dyadic gap"
invariant (round 7) and NOT a flat "≤1 piece per scale" (false at low scales).

**Statement.** Let `B` be any refinement of `C_m = {2^0, 2^1, …, 2^m}` (each original piece
partitioned into finitely many positive fragments; the number of cuts is arbitrary). For
`j = 0,…,m` let `G_j ⊆ B` be the multiset of fragments of the original piece `2^j`, so
`B = ⊔_{j=0}^m G_j` and `Σ G_j = 2^j`. Then:

- **(i) [scale-truncation is admissible]** For every `0 ≤ ℓ ≤ m`, the sub-multiset
  `B_{≤ℓ} := ⊔_{j=0}^ℓ G_j` is a refinement of `C_ℓ`, using exactly `Σ_{j≤ℓ}(|G_j| − 1)` cuts.

- **(ii) [per-scale single excursion]** For every `j`, at most one fragment in `G_j` exceeds
  `2^{j−1}`. Consequently, for every `τ ≥ 2^{ℓ−1}`, at most one piece of `B_{≤ℓ}` exceeds `τ`
  (certified Lemma ONE applied to `B_{≤ℓ}` as a refinement of `C_ℓ`), and in general
  `N_B(τ) = Σ_j #{f ∈ G_j : f > τ}` with the scale-`j` summand contributing `≤ 1` above `2^{j−1}`.

**Proof.**
(i) By the definition of a refinement, the cuts of `B` partition according to which original piece
they subdivide; the `j`-th group of cuts produces exactly the fragments `G_j`, with `Σ G_j = 2^j`
and `|G_j| ≥ 1`. No cut crosses two original pieces. Restricting to the pieces originating from
`{2^0,…,2^ℓ}` therefore leaves a self-contained partition of each of those pieces into its `G_j`,
which is precisely a refinement of `C_ℓ`. The cut count is `Σ_{j≤ℓ}(|G_j| − 1)` (a group of `|G_j|`
fragments requires `|G_j| − 1` cuts).

(ii) Two fragments of `G_j`, each `> 2^{j−1}`, would sum to `> 2^j = Σ G_j`, leaving the remaining
fragments negative total — impossible. So `G_j` has at most one fragment `> 2^{j−1}`. For the
consequence: by (i), `B_{≤ℓ}` is a refinement of `C_ℓ`, so certified **Lemma ONE**
(`top-scale-dichotomy`) yields at most one piece of `B_{≤ℓ}` exceeding `2^{ℓ−1}`, hence at most one
exceeding any `τ ≥ 2^{ℓ−1}`. The `N_B(τ)` decomposition is additivity of the count over the disjoint
groups `G_j`. ∎

**Ladder is load-bearing.** The lemma is false for a non-ladder multiset; `Σ G_j = 2^j >
2^0+…+2^{j−1}` (superincreasing) is what forces (ii). The half-integer witness `F={½,½,½}, B={½}`
(`ΣF−ΣB = 1`, `|F|=3`, yet `D(S)=0`) is excluded because `B={½}` is not a refinement of any `C_m`,
so Lemma ONE-REC is unavailable for it — the required litmus test that a lower-bound argument
genuinely uses the dyadic structure.

**Dependencies.** Certified Lemma ONE (`top-scale-dichotomy`) + partition-of-cuts identity.
Self-contained; elementary. Proposed for certification.
