## imo-2026-03 (LOWER WALL lens: GAP MID-core, foresight/whole-ladder reserve)

### Setting recap (verified against current files, not re-derived)
`S=F⊔B` admissible a=0 refinement of `C_n`; `F`=fragments of top `2^n` (`ΣF=2^n`, each `≤2^{n-1}`,
`|F|≥3`); `B`=`≤(n-1)`-cut refinement of `C_{n-1}={1,…,2^{n-1}}` (`ΣB=2^n-1`). `g=N_F-N_B` on
`(0,2^{n-1})`. Certified: Lemma MID (`D=μ{g odd}`, `∫g=1`), Lemma ONE-REC (scale-truncation
`B_{≤ℓ}=⊔_{j≤ℓ}G_j` is itself an admissible refinement of `C_ℓ`, each scale-group `G_j` has `≤1`
fragment `>2^{j-1}`), R9's `∫φ(g)≥0` reformulation (`φ(c)=1[c odd]-c`, sign flips exactly at `c=2`).
Confirmed by direct re-simulation this round (4000 random admissible a=0 refinements, n=3,4,5):
min `D` observed `1.0005/1.006/1.70` — consistent, no violation, nothing new numerically but
re-validates the setup before scouting further.

### Distinct openings (whole-ladder / foresight-potential family)

1. **"Remaining-F-mass-below-τ" reserve (the concrete object R9 pointed at but did not build).**
   Define, for `τ` scanning top-down, `R_F(τ) := Σ_{f∈F, f≤τ} f = 2^n - A(τ)` where
   `A(τ):=Σ_{f>τ}f`. This is *not* `N_F(τ)` (a count) but the **mass of F still waiting to cross**
   below `τ` — a genuine foresight quantity R9 called for but never wrote down. Candidate potential
   `Φ(τ) := R↓(τ) + κ·h(R_F(τ))` for some monotone `h` (linear or quadratic) and constant `κ`,
   where `R↓(τ)=∫_τ^{2^{n-1}}φ(g)`. Rationale: R9's refuted `ψ(g(τ))` failed because it depended
   only on the *current* walk height, blind to how much more F-mass is still queued below `τ` to
   create future overshoot; `R_F(τ)` is exactly "how much is still queued." **Untested this round**
   (I verified the setup numerically but did not have time to grid-search `κ`,`h`; flagging as the
   concrete next experiment, not a claim).
2. **Amortized-potential / "ink-game" mechanism (crux `aimo-0019` analogue).** That problem (paint
   pot with 4 units of ink, prove `[0,1]` fully blackened before the pot empties) is proved by an
   **amortized invariant**: "ink spent on `[0,x_r]` is `≤ 3x_r`", charged round-by-round against
   *progress* `x_r`, not against a raw resource count. This is the correct template-shape for a
   whole-ladder reserve here: a two-term potential (progress-so-far `∫φ(g)` + reserve) whose
   invariant is proved by an **amortized charging induction over the dyadic scale-groups `G_j`**
   (via certified Lemma ONE-REC), not by a running scalar bound alone. Concretely: charge every unit
   of `{g≥2}` deficit created while scanning through scale-group `G_j` against the *mass* `2^j` that
   `G_j` contributes (its scale budget), the way the ink problem charges ink spent against interval
   length covered. This is a genuinely different proof *shape* (amortized analysis, not integral
   inequality) from every reserve R9 tried and refuted (which were all pure scalar functions of `τ`
   or `g(τ)`).
3. **Hall-matching / bipartite feasibility (crux `aimo-0129` analogue) — endpoint-splitting Hall
   check.** `aimo-0129`'s Hall verification (for the horizontal/vertical maximal-stick bipartite
   graph) does **not** prove Hall's condition abstractly; it verifies it by **splitting any
   candidate violating set `S` by its extremal members** (leftmost/rightmost column) and bounding
   the neighborhood directly via two lengths `l,r`. This is a concrete template for closing
   `ballot-matching`'s open **GAP-HALL**: instead of trying to prove the debit↔credit Hall condition
   for a general candidate debit set, split any candidate violating set by its *coarsest dyadic
   scale* member and bound the reachable credit using Lemma ONE-REC's per-scale `≤1`-fragment cap —
   i.e. do the Hall check scale-by-scale with an explicit endpoint argument, exactly as in
   `aimo-0129`, rather than proving a general max-flow/min-cut style inequality.
4. **Ballot/reflection principle via running extremum, not integral (crux `aimo-0003` analogue).**
   `aimo-0003`'s invariant ("number of inverted arcs = `-x`, `x` = min value of a `±1` running tally")
   is proved by an induction that **deletes an innermost matched pair** (a chord whose arc contains
   no opposite-color point) — structurally this *is* already what certified Lemma P (cancelling
   pair) does here. The crux's genuinely different idea is stating the target as an **extremal
   statistic of the walk** (a min or max) rather than an integral/measure. Concretely: ask whether
   `D(S)` (or the residual `∫φ(g)`) can be re-expressed as a function of `min_k S_k` (the most
   negative excursion of the signed merge walk `S_k=Σ_{i≤k}e_i`, `e_i=±1`) via a reflection-type
   argument, since `S_m=|F|-|B|<0` is already known (certified fact F2 in round 8). This is
   speculative — **not verified**, offered as a genuinely different top-level target (extremal
   statistic vs. integral inequality) for the outliner to weigh against the amortized-potential
   route.

### Cheap-kill candidates
- Quick check: is `R_F(τ)` (or `A(τ)`) itself already implicit in existing failed reserves? No —
  R9's refuted objects (`ρ_k` cumulative surplus, `ψ(g(τ))`) are both functions of *count* data
  (`N_F,N_B,g`), never of the *mass* `R_F(τ)`. This is a genuine gap in what's been tried, not a
  re-hash — worth a dedicated numeric pass before any full construction.
- Parity/size cheap-kill: none obvious beyond what's already certified (Lemma ONE-REC, MID). No new
  one-move structural kill found this round.

### Candidate technique(s)
- Amortized potential / charging argument (two-term: progress + reserve, invariant proved by
  induction over dyadic scale-groups, cf. `aimo-0019`).
- Hall's marriage theorem verified by explicit endpoint-splitting of a candidate violating set
  (cf. `aimo-0129`), for `ballot-matching`'s GAP-HALL.
- Reflection-principle / extremal-statistic-of-a-walk restatement (cf. `aimo-0003`), as an
  alternative top-level target to the integral inequality `∫φ(g)≥0`.

### Knowledge-base entries to use
- **Hall's marriage theorem / SDR** (Combinatorics section) — directly named, for `ballot-matching`'s
  GAP-HALL.
- **Invariants & monovariants** (general) — the amortized-potential shape.
- **Constructive/incremental** and **Invariant/monovariant** (General Proof Methods) — for the
  scale-by-scale charging induction.
- No new KB entry (SOS, Cauchy-Schwarz, etc.) looks directly load-bearing here; the KB has no
  "amortized analysis" entry by name — this is imported purely from the crux corpus.

### Analogous past problems (cruxes)
- **`aimo-0019`** (paint/ink game, algebra/combinatorics-adjacent, `invariants-and-monovariants`):
  best analogue for the *mechanism* — a linear potential bounding cumulative resource by a constant
  times progress, proved by an amortized induction that charges each advance against what it
  absorbs. Directly maps onto "charge `{g≥2}` deficit created in scale-group `G_j` against `G_j`'s
  own mass budget `2^j`."
- **`aimo-0129`** (n×n sieve stick-partition, combinatorics, `graph-theory-and-connectivity` +
  `double-counting`): best analogue for **how to actually verify a Hall condition** — split any
  candidate violating set by its extremal (leftmost/rightmost, i.e. here coarsest/finest-scale)
  member and bound directly with two explicit lengths, rather than abstract max-flow reasoning.
  Directly actionable for `ballot-matching`'s GAP-HALL.
- **`aimo-0003`** (circle red/blue arc-matching invariant, combinatorics,
  `invariants-and-monovariants`): analogous *reduction move* (delete an innermost/adjacent matched
  pair) is already captured by certified Lemma P; its distinct contribution is recasting the target
  as an extremal statistic (`min` of a running tally) rather than an integral — offered as a
  speculative alternative top-level target, not verified against our setup's asymmetric walk
  (`aimo-0003`'s walk returns exactly to 0; ours ends at `S_m<0`, so the reflection argument would
  need to be re-derived, not transplanted).
- `aimo-0156` (frog-hop max-sum, NT/combinatorics, `telescoping-and-summation` — Abel summation of
  suffix bounds) is **not** a new analogue: its mechanism (bound each scale's count by a suffix cap,
  Abel-sum) is exactly the *prefix/suffix reserve* shape R9 already rigorously refuted (deficit grows
  with `n`). Do not re-import this move.

### Prior progress
See current.md: Lemma MID, ONE-REC, OSR, OSR-cap all certified; MID-core reduced to
`∫φ(g)≥0` with negative mass exactly on `{g≥2}`; `|F|=2` and `g≤1` sub-cases closed. Both
`parity-measure-potential` and `ballot-matching` target the same residual inequality from two
angles (induction/potential vs. Hall-matching transport); `merge-interleave-pattern` targets it as
a reachable-word extremal problem (also unclosed: GAP-REACH, GAP-EXTR).

### Dead ends (do not retry)
- Prefix-form / running-deficit monovariant on the merge order: **refuted**, fails ~27% (8043/30000).
- Per-dyadic-gap single-interval invariant for `O_B`: **refuted**, explicit 2-interval witness.
- Nonnegative cumulative-surplus reserve `ρ_k` (top-down `R↓` or bottom-up `R↑`, pure `∫φ(g)`
  accumulation with no mass term): **refuted**, deficit grows with `n` (−30.5/−23 at n=6).
- Walk-height-only reserve `ψ(g(τ))` (any function of current `g(τ)` alone, no lookahead): **refuted**
  — the `{g=2}` band can have unbounded measure per unit height, so no per-height correction absorbs
  the drop.
- `aimo-0156`-style Abel-summed suffix-cap bound: same shape as the refuted prefix/suffix reserve —
  do not re-attempt without a genuinely new ingredient.

### Small-case / intuition notes (conjecture, from this round's re-simulation)
- Confirms (conjecture, numeric only, n=3,4,5, 4000 samples each): `D(S)≥1` always holds, minimum
  observed grows slowly with `n` (`1.0005 → 1.006 → 1.70`), consistent with all prior rounds — no
  new counterexample structure found.
- The `R_F(τ)` mass-reserve idea (opening 1) is genuinely untested; it is the most concrete
  "whole-ladder, not local" object consistent with R9's own diagnosis ("must track remaining F-mass
  above/below `τ`") and should be the first numeric experiment next round: grid-search
  `Φ(τ)=R↓(τ)+κ·R_F(τ)^p` for `p∈{1,2}` against the same refinement generator used above, checking
  `min_τ Φ(τ)≥0` and the associated invariant-preservation step (does `Φ` decrease correctly across
  each scale-group `G_j`, chargeable to that scale's own mass budget as in the `aimo-0019` template).
