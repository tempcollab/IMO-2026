# Proof-reviewer — Round 10 (imo-2026-03, GAP L / lower-bound Case B)

Upper bound already certified (`lemmas/upper-bound.md`) — not re-reviewed. Sole open wall: prove
`D̃(F) ≥ 1` for every feasible dyadic refinement (Case B). Three builds reviewed independently.

---

## 1. peel-scale-rank-induction — CHANGES REQUESTED (Status: partial)

**Load-bearing claim — FLOOR identity `D̃(F)=1−2∫_{(0,θ)}⌊M/2⌋`.** Re-derived independently and
correct:
- Certified peel identity gives `D̃(F)=λ(O_{π_0}△O_{F'})`. Split at `θ=2^{n−1}`. On `(θ,∞)`,
  `O_{F'}=∅` (all `F'` parts `≤θ`) and `Σπ_0=2θ` ⇒ at most one part of `π_0` exceeds `θ`, so the
  contribution is `β=(y_1−θ)^+`. Correct.
- On `(0,θ)`: `O_{π_0}△O_{F'}={M odd}` (parity of sum = parity of difference). The elementary
  `1[m odd]=m−2⌊m/2⌋` holds for all integers `m` (both `= m mod 2`). Integration ⇒
  `λ{M odd}=∫M−2∫⌊M/2⌋`. I re-checked `∫_{(0,θ)}M`: `∫N_{F'}=ΣF'=2^n−1`, `∫_{(0,θ)}N_{π_0}=2^n−β`,
  so `∫M=1−β`. Hence `D̃=β+(1−β)−2∫⌊M/2⌋=1−2∫⌊M/2⌋`. Airtight.

**Independent numerical check (mine, exact `Fraction`):** `0` mismatches of (FLOOR) over 3000 random
feasible refinements, `n≤5`. Lemma OB/G cross-check also `0`. The consequence
`Case B ⟺ I_n:=∫⌊M/2⌋≤0` is exact and unconditional — a genuine sharpening of R9's GAP-P1 and of the
`(△⋆)` measure form. The two structural findings (budget enters only via `M(0⁺)≤1`; `M(0⁺)≤1` alone
insufficient — the §7a decoy `D̃=0.146` witness) are honest and correctly interpreted.

**Gap (honestly stated, GAP-P1′):** prove `I_n ≤ 0`. The reduction is unconditional/exact; the
closing loaded dyadic-shape IH on `g=N_{F'}` is NOT constructed. The circularity risk (any IH strong
enough must not restate the target) is spelled out but unresolved. Builder's Status `partial` is
correct. Real progress: the wall is now a single explicit scalar inequality.

**Scores:** Correctness 10/10 · Rigor 9/10 (reduction airtight; closure open, honestly) · Progress
high (sharpest GAP-L form of the run). **Certified:** `lemmas/floor-half-reduction.md` (FLOOR + layer
form). **Verdict: CHANGES REQUESTED — close `I_n≤0` via the loaded shape-IH on `g=N_{F'}`.**

---

## 2. vertex-integrality-parity — RETHINK (Status: unsolved as a standalone engine)

**Equivalence claim `GAP-IMR ⟺ target` (Part 4.1) — verified correct.** With `μ=min_{Φ_n}D̃`
(attained, compact): integer configs are feasible so `μ≤1`; Part 2 PROVES integer-min`=1`; GAP-IMR
says `μ=min_{integer}D̃=1`; target says `μ≥1`. All three are `μ=1`. The R9 "non-circular / orthogonal
to value 1" note is genuinely WRONG once Part 2 is used, and the builder correctly retracts it. This
is a valid, important negative: the integer-minimizer framing is a *reformulation*, not a
difficulty-reducing reduction.

**Smoothing-engine refutation (Part 4.3) — verified.** (i) For `n≤3` every min-value(=1) vertex is
integer (exact LP `0/90`, `0/1134`), so the mechanism's non-trivial case is vacuous. (ii) At an
isolated fractional vertex (0-dim optimal face), every feasible ray strictly increases `D̃`, so no
`D̃`-non-increasing descent exists; the odd-fractional-block witnesses (`{4,2,⅓,⅓,⅓}`, `D̃=7/3`) are
exactly this type. The reasoning is sound. Part 1 Parity Lemma and Part 2 attainment family I
re-verified (integer family `{…,4,4,3,2,1,1}` gives `D̃=1` for all `n=1..6`).

**Why RETHINK, not CHANGES REQUESTED:** the approach's engine — reach an integer minimizer via
mass-transfer/rounding/smoothing and apply Parity — is now shown to have no viable mechanism: TU/cell
rounding refuted (R9), per-group rounding refuted (R9), smoothing has no descent (R10), and the target
GAP-IMR is equivalent-difficulty to the whole lower bound. The surviving assets (Parity Lemma,
reduction) are ALREADY certified and are a *finishing device*, not an engine. The builder itself
recommends retiring the standalone line and folding Parity into the peel route. This is precisely a
RETHINK: the approach as set up cannot close GAP L — send back to the outliner.

Builder's recorded Status `partial` is defensible for the file (real negative results), but the
approach's *engine* is dead; I route it RETHINK. **Nothing new to certify** (Parity Lemma already
banked; the `GAP-IMR⟺target` equivalence is recorded as a caution in the file, not a reusable positive
lemma). **Scores:** Correctness 9/10 · Rigor 8/10 · Progress: a clean rigorous negative (prunes the
integer-minimizer engine). **Verdict: RETHINK.**

---

## 3. peel-integral-exchange — CHANGES REQUESTED (Status: partial)

**Lemma OB (odd-block value formula) — verified.** Per-block geometric sum
`Σ_{t=0}^{r-1}(−1)^t=𝟙[r odd]` and the parity `(−1)^{s_l−1}=(−1)^{p−1}` are both correct; my exact
check gives `0` mismatches vs Lemma G over 20000 random multisets. Correct and cleanly promotable.

**Lemma V (`K≤n+1` at a minimizing vertex) — verified.** `D̃` linear on each order cell ⇒ min at a
vertex; a vertex needs `m` independent active constraints; available: `n+1` group-sums + `(m−K)`
adjacent ties (no `x≥0` active when all coords positive), so `m≤(n+1)+(m−K)`, giving `K≤n+1`. The
active-constraint count is standard and correct. Note (correctly stated) it does NOT assert vertices
are integral — no resurrection of the refuted TU claim.

**Reduction to GAP-IMR′ ("some optimal cell-vertex is integer") — valid but weaker than it looks.**
Reduction R (integer optimal vertex ⇒ `μ≥1` via Parity) is correct. But GAP-IMR′ ⇒ target while
target ⇏ GAP-IMR′ (an optimal vertex could be fractional even with `μ=1` attained at an interior
integer point). So GAP-IMR′ is *stronger* than the target and could conceivably be FALSE at some `n`
where all optimal vertices are fractional. It is verified only `n≤3`. This is a genuine caveat, not a
flaw in the round's proven content. The localization (fractionality lives on even blocks fed `≥2`
parts by one scale) is correct via OB-even.

**Wall (honest):** cross-scale non-increasing integral rounding — mass cannot cross a scale's hard
sum `Σπ_j=2^{n−j}`, and a small-scale even-block merge can raise `D̃` (`(4,2,½,½): 2→3`). Real, open.
Conjecture C is correctly shown insufficient alone. Builder Status `partial` correct.

**Why not RETHINK:** unlike the twin, this slug delivered two *new correct promotable lemmas* and a
finite-lattice narrowing (GAP-IMR′), so there is real round-10 progress and a live (if risky) target.
It is not refuted. But it shares the integer-minimizer wall the twin proved equivalent-difficulty —
flagged as caution; if it stalls again in R11 it should be retired in favor of the peel route.

**Scores:** Correctness 10/10 · Rigor 9/10 · Progress moderate (OB/V solid; GAP-IMR′ possibly
unattainable). **Certified:** `lemmas/odd-block-vertex.md` (Lemmas OB + V). **Verdict: CHANGES
REQUESTED — either prove GAP-IMR′ (some optimal vertex integer) or redeploy Lemma OB as a monovariant
potential for a global descent to the canonical integer `D̃=1` family.**

---

## Summary

| slug | Status | Verdict | certified this round |
|---|---|---|---|
| peel-scale-rank-induction | partial | CHANGES REQUESTED | floor-half-reduction.md |
| peel-integral-exchange | partial | CHANGES REQUESTED | odd-block-vertex.md (OB, V) |
| vertex-integrality-parity | unsolved (engine) | RETHINK | — (Parity already banked) |

GAP L remains OPEN; no APPROVE. Whole problem stays **partial** (UB certified, LB Case B open). The
cleanest live route is `peel-scale-rank-induction`: GAP L `⟺ I_n=∫⌊M/2⌋≤0`, a single explicit scalar
inequality. The integer-minimizer routing is now proven equivalent-difficulty to the target — the
field should NOT open a 4th GAP-IMR/rounding variant; fold the certified Parity Lemma into the peel
induction as its integer base/finishing device.
