## imo-2026-03

Field for R12: GAP L (lower bound, Case B) is the SOLE open wall; upper bound certified — untouched.
GAP L is pinned to `I_n≤0`, split into GAP-P1′-a (prove `(★) Σ_{blue odd}≥Σ_{red even}` on the base
slice `b=0`, `F'=L`) and GAP-P1′-b (lift general `b` to `b=0`). Three approaches, diverse in framing:
value-domination induction, positional/parity pairing, and monovariant descent — TWO independent
routes to `(★)` and TWO independent routes to the `b`-lift, so the field does not collapse on either
gap (single-gap trap avoided). Verified this round (exact `Fraction`, `/tmp` probe): `(★-id)` exact,
`(★)` 0 fails, weak-majorization 0 fails (integer `n≤6`), colour-sum `(C)=Σπ_0−ΣF'=1` for ANY
feasible `F'` (not just `L`), `(DOM) b_i=1+Σtail` exact.

allocation-vertex-corner: RETIRE (b-pruning engine DEAD R11; Positive-Layer Localization Lemma banked
and imported by ladder-abel-pairing). Replaced by ladder-abel-pairing below.

---

peel-scale-rank-induction: advance
Target: GAP L — `D̃(F)≥1` for all feasible `F`, closing the problem (with certified UB ⇒ `c(n)=2^n/(2^{n+1}−1)`).
Technique: strong induction on `n` peeling the top dyadic scale; NEW closer = TOP WEAK-MAJORIZATION
(HLP value-domination) on the base slice, adopted as the LOADED IH for the peel step.
Skeleton (new §11):
  1. Base slice `b=0`, `F'=L`: reduce to `(★)` — imported `(★-id)`.
  2. Prove the stronger `(WM)`: `∀k, Σ_{top k BO} ≥ Σ_{top k RE}` (BO=blue-odd values, RE=red-even).
     `k=all` ⇒ `(★)`. Equivalent HLP threshold form `(HLP) ∀t, Σ_{BO}(v−t)^+ ≥ Σ_{RE}(v−t)^+`.
  3. Self-similar truncation: `(HLP) ⟺ ∀t, ∫_t^∞(N_BO−N_RE)≥0` — tail-integral domination over all
     top-truncations `P_t` (ranks preserved on `>t`); the HLP/Karamata toolkit applies.
  4. Charge red-even mass onto odd-rank rungs via `(DOM) b_i=1+Σtail` + `(m₀≤1)` — cross-block tail
     cancellation; rank-parity `rank(b_i)=i+P_i` selects odd rungs. [GAP-P1′-a]
  5. Loaded-IH continuation: `(★-id)` generalizes to any `F'` (colour-sum `=1` always); take `(WM)`
     as the IH, base `F'=L` via `(DOM)`, inductive step = `(WM)` inherited under one peel
     `F'=π_1⊎F''`. Unifies GAP-P1′-a + GAP-P1′-b. [GAP-P1′-b]
Key lemmas:
  - `(WM)`/`(HLP)` weak majorization of BO over RE — because red-even mass is charged to blue-odd mass
    of `≥` value (global value-domination), the tail-integral form makes it a Karamata statement.
  - `(DOM) b_i=2^{n−i}=1+Σ_{i'>i}b_{i'}` — geometric; one odd rung dominates its whole lower tail.
  - `(m₀≤1)` — two reds `>θ` sum `>2^n=Σπ_0`; lone top red at odd rank contributes `0` to RE.
Open gaps: step 4 (the uniform-in-`t` tail-charge = GAP-P1′-a); step 5 inheritance (= GAP-P1′-b).
Cases to cover: base slice `b=0` (deliverable); `n=1` imported; Case A certified; general `b` via §11.5.
Watch out for: `(WM)` is STRICTLY STRONGER than `(★)` — verify no over-shoot at large `n` (0 fails so
far); if it over-shoots, fall back to ladder-abel-pairing (targets `(★)` exactly). Do NOT use the
refuted per-block charge (51% fail) or any positional running-margin scan (margins → `−2^{n-1}`).

ladder-abel-pairing: new  (replaces retired allocation-vertex-corner)
Target: GAP L — `D̃(F)≥1` for all feasible `F`, closing the problem.
Technique: Abel summation / summation-by-parts on the merged alternating sum, telescoped by ladder
rung; parity of the leading red forces the residual `≥0`. Crux analogue aimo-0388 (baby-P3 coin
split, parity `⇒|diff|≥1`); dyadic dominance aimo-0298. This is the value-reordering + GLOBAL parity
dual of the weak-majorization route — FAR from it, and targets `(★)` EXACTLY (robust to WM over-shoot).
Skeleton:
  1. Reduce to `(★)` on base slice — imported peel + `(FLOOR)` + `(★-id)`.
  2. `D̃ = Σ_{j odd}(w_j−w_{j+1})`, each consecutive-pair gap `≥0`.
  3. Rung-telescoped re-pairing: charge each odd-rank rung `b_i` against the even-reds in its
     dominated tail `(0,b_i)` via `(DOM)` — the cross-block cancellation the per-block charge lacked.
  4. Boundary term = lone leading red (`(m₀≤1)`, odd rank, contributes `0`); parity of `ΣL=2^n−1`
     (odd) forces residual `≥0` ⇒ `Σ_{blue odd}≥Σ_{red even}` ⇒ `D̃≥1` (aimo-0388 mechanism).
  5. General `b`: import loaded-IH (peel §11.5) or coupled descent.
Key lemmas: `(DOM)`, `(m₀≤1)`, parity closer (colour-sum exactly `1`, integer offset forces `≥0`).
Open gaps: step 3 rung-telescoped pairing inequality (core); general-`b` lift (imported).
Cases to cover: base slice `b=0`; `n=1` imported; ties (`n+1` configs) give equality — correctness check.
Watch out for: must NOT be a one-directional positional running-margin scan (REFUTED, margins →
`−2^{n-1}`); pairing is value-reordering + GLOBAL parity. Not the per-block same-block charge (51% fail).

coupled-cut-descent: new
Target: GAP L — `D̃(F)≥1` for all feasible `F`; specifically OWNS the `b`-lift wall GAP-P1′-b from a
framing far from the two `(★)` routes (monovariant descent, not induction/value-domination).
Technique: budget-conserving CO-VARYING monovariant (invariants & monovariants) with explicit
tie-family carve-out. `π_0` absorbs the freed cut — NOT the refuted pointwise `π_0`-fixed monovariant.
Skeleton:
  1. Reduce to `I_n≤0` (imported `(FLOOR)`); Case A certified; handle `1≤b≤n−1`.
  2. Coupled move `b→b−1`: merge two parts of a scale `π_j` (j≥1), give the freed cut to `π_0`
     (`a_0→a_0+1`, repartition); budget `a_0+b` conserved.
  3. Descent claim: every non-tie config (`D̃>1`) admits such a `D̃`-non-increasing move
     (explorer: 1395/1396 `n=4`); iterate to `b=0`. [HARD OPEN STEP]
  4. Base `b=0`: `(★)` closes it — imported.
  5. Tie carve-out: `{D̃=1}` = the `n+1` "`L`+one bumped unit" configs; ladder-interleaving ⇒ both
     sides of `(★)` are `0`, `D̃=1` directly — handle the finite family explicitly.
Key lemmas: coupled-move `D̃`-non-increasing on non-ties (mechanism: lower-scale merge cuts local
discrepancy; freed cut to `π_0` can't out-raise it since budget enters `I_n` only via `M(0⁺)≤1`,
Invariant I certified — OPEN: a selection rule, not just per-config existence); tie family = `n+1`
explicit configs closed by ladder-interleaving; Invariant I `M(0⁺)=1−2b`.
Open gaps: step 3 descent lemma (general `n`, selection + monotonicity); tie set = `n+1` at all `n`.
Cases to cover: A certified; B `1≤b≤n−1` descend; base imported; tie family explicit; `n=1` imported.
Watch out for: slice-max is FLAT `=0` for `b<n` (zero `b`-slack) ⇒ descent is max-preserving,
tie carve-out MANDATORY. NOT pointwise `π_0`-fixed (30% fail), NOT vertex/GAP-IMR (dead), NOT scalar
`b`-cutoff (dead, ties at `b=2,3`). Un-coupled merge (π_0 fixed) can RAISE `D̃` (`{4,2,½,½}:2→3`).
