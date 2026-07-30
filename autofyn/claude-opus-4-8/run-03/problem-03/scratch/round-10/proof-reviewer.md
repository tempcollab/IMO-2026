# Proof-reviewer — Round 10 (imo-2026-03)

Two approaches built this round, one per wall. Both recorded Status `partial`; neither claims
`solved`. I re-derived the load-bearing steps independently. Both `partial` statuses are HONEST —
no overclaim on either wall. Verdict per slug: **CHANGES REQUESTED** for both. Overall problem
Status remains **partial** (no APPROVE).

---

## Approach 1 — parity-measure-potential (LOWER wall)  ·  Verdict: CHANGES REQUESTED

**Recorded Status: partial — CORRECT.**

**What R10 did.** Executed the assigned "grid-search-first" gate on the mass-reserve potential
`Φ(τ) = ∫_τ^L φ(g) + κ·ρ(τ)`, φ(c)=1[c odd]−c, MID-core ⟺ ∫_0^L φ(g) ≥ 0. Refuted every additive
scalar-reserve form (mass-below `Σ_{f≤τ}f`; mass-above `2τN_F(τ)`; cumulative-surplus and
walk-height from R9). Proposed one new promotable exact identity (Lemma CLIP).

**Independent verification of the load-bearing claims.**
- **RESERVE-NONNEG counterexample (the round's decisive negative result): CONFIRMED.** I rebuilt
  the `n=7` witness `F={63.0119,62.8559,2.1322}` (ΣF=128=2^7), `B` (12 pieces, ΣB=127=2^7−1) and
  computed `D(S)=15.073 ≥ 1` (so MID-core itself holds) yet **`Φ(8.944) = −2.07 < 0`** — the
  invariant `Φ(τ)≥0` is genuinely FALSE. Refutation is sound; the reserve lever is correctly killed.
- **MID/τ=0 identity: CONFIRMED.** `∫_0^L φ(g) = D(S)−1 = 14.0734` reproduced exactly.
- **Lemma CLIP (proposed for certification): CONFIRMED EXACT.** Independently checked
  `∫_τ^L φ(g) = D(S'_τ) − (ΣF'_τ − ΣB'_τ)` over 2000 random admissible a=0 refinements
  (n=2..6, random τ): max error `7.1·10^{−15}`. Derivation re-checked by hand
  (layer-cake + certified Lemma M on the clip + certified OSR). **CERTIFIED** as
  `lemmas/clipped-tau-family.md`.

**Minor blemish (not load-bearing).** In the writeup of the counterexample the builder states the
intermediate `∫_8.944^L φ(g) = −51.95`; the true value is `−37.85` (reserve `2·8.944·2 = 35.78`,
sum `−2.07`). The final `Φ=−2.07` — the load-bearing conclusion — is correct; only the stated
intermediate integral is a typo. Flag to fix, does not affect the refutation.

**What is genuinely established vs open.**
- Established (this round): the entire additive constant-κ scalar-reserve family is exhausted for
  MID-core (four forms refuted, all with the same "high wide {g≥2} band deficit can't be carried
  down by a shrinking scalar" signature; required κ has no n-independent bound). Lemma CLIP: the
  clean exact τ-family identity making MID-core the `τ=0` face of an order-statistic transport
  `Σ_{F' even}v' ≤ Σ_{B' odd}v' + τ|F'|`.
- **Open (GAP MID-core, unchanged):** prove `∫_0^L φ(g) ≥ 0` (equiv. `Σ_{F even rank}v ≤
  Σ_{B odd rank}v`) for |F|≥3. Builder correctly flags the pivot to a value-weighted
  debit→larger-credit **matching / Hall-transport** (ballot-matching slug), consistent with the
  certified negative fact F1 (prefix form fails ~27%): the compensation is irreducibly aggregate
  and non-local, so no running scalar can close it.

**Gap to attack next.** GAP MID-core via a value-weighted matching that supplies
`Σ_{F even}v ≤ Σ_{B odd}v` — the R10-shift input at τ=0. The additive-potential route is now
provably dead; do not re-attempt it.

---

## Approach 2 — breakpoint-vertex (UPPER wall)  ·  Verdict: CHANGES REQUESTED

**Recorded Status: partial — CORRECT.**

**What R10 did.** Executed the numeric-first gate on the outliner's two-case (generic/near-uniform)
skeleton. Refuted the "generic = fixed-depth two-level escape" lemma; recorded a new (unproven)
covering-radius invariant `ρ_i ≤ a_i/2`; kept GAP U-cover open and sharpened.

**Independent verification.**
- **Covering target `min 𝓡(A) ≤ u_n`: CONFIRMED.** Over 20000 random full-budget valley profiles
  (a₁<½, n=2..6), the descending include/skip reachable minimum was `≤ u_n` with **0 exceptions**.
  The target itself is correct; only a profile-independent proof is missing.
- **n=5 generic depth-2 failure witness: CONFIRMED.** For `A≈(0.2724,0.2067,0.1984,0.1800,0.1365,
  0.0060)` the full-depth reachable minimum is `0.0022 ≤ u_5=0.01587`, and this profile has a
  dominant adjacent ratio (22.7 at the small end), so it is unambiguously not near-uniform — a
  genuine generic profile whose escape depth exceeds 2. The refutation of the fixed-depth generic
  lemma is sound; the "generic/near-uniform with bounded-depth escape" partition provably does not
  localise the difficulty. Spec concern to the outliner is legitimate.
- **ρ_i ≤ a_i/2 invariant:** the builder explicitly does NOT claim it proven (natural induction
  yields only `ρ_i ≤ a_{i-1}/2`) and shows it is insufficient alone (saturates at `a_{n+1}/2 ≫ u_n`
  on near-uniform). Correctly recorded as a candidate, NOT promoted. I do not certify it. Good
  honesty — no overclaim.

**What is genuinely established vs open.**
- Established (this round): profile-independent refutation of the bounded-depth-escape class
  (prunes the outline's step-2 generic mechanism); a new validated structural candidate that
  narrows the search and, by its own saturation, pinpoints the residual as a density/pigeonhole
  among tree-realizable values. Prior certified content (PL1, VERT, TB, RL, VS, ESF-1/2, BL) stands.
- **Open (GAP U-cover, unchanged/sharpened):** prove `R_{n+1}` has an element in `(0,u_n]` (or 0 via
  even cancellation) — a restricted (tree-realizable, Lemma RL) EGZ/pigeonhole using Σa_i=1,
  a₁<½, a₂<β_n jointly. Both a bounded-depth move-search and a single-window covering-radius bound
  are provably insufficient.

**Gap to attack next.** GAP U-cover as a global density/pigeonhole invariant on the tree-realizable
reachable set (Lemma RL) telescoping to u_n; NOT a bounded-depth escape and NOT a single covering
radius (both refuted).

---

## Lemma certification
- **CERTIFIED:** Lemma CLIP → `results/imo-2026-03/lemmas/clipped-tau-family.md` (exact τ-family
  identity, reviewer-reproduced to 7·10^{−15}; self-contained on certified M/OSR; explicitly no
  inequality claimed — the associated RESERVE-NONNEG inequality is FALSE, verified).
- **NOT certified (correctly not promoted):** the upper wall's `ρ_i ≤ a_i/2` invariant — builder
  itself flags it unproven and insufficient.
- Both builders' recorded negative results (reserve family refuted; fixed-depth generic escape
  refuted) are reviewer-verified and worth keeping to prevent re-attempts.

## Scores (both approaches)
- Correctness: high — every asserted identity/refutation I checked reproduced exactly; the honest
  gaps are exactly where claimed.
- Completeness/rigor: incomplete — one clean residual gap per wall (MID-core / U-cover), both open.
- Progress vs prior best: moderate — no gap closed, but a whole lever-class refuted per wall (prunes
  the search) plus one new certified exact identity (CLIP). Correctly `partial`, not `advanced`.

## Routing
- parity-measure-potential: **CHANGES REQUESTED** (Status partial). Close GAP MID-core via the
  matching/Hall-transport pivot; additive-potential route is dead.
- breakpoint-vertex: **CHANGES REQUESTED** (Status partial). Close GAP U-cover via a global
  tree-realizable density/pigeonhole invariant; bounded-depth and covering-radius routes are dead.

Both spec concerns (lower: additive reserve refuted; upper: bounded-depth generic partition
refuted) are valid and should feed the next outliner: both walls now demand a genuinely global,
non-scalar / non-bounded-depth foresight object. The field has been on the same two walls for
several rounds — worth considering one genuinely different framing per the CLAUDE.md
shared-gap-plateau rule.
