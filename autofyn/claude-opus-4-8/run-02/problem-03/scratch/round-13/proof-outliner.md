## imo-2026-03

Sole open wall: **GAP L** (lower bound, Case B) ⟺ certified `I_n ≤ 0` (`(FLOOR)`), split into
`(★)` base slice (`b=0`, `F'=L`) + the `b`-lift (general `F'`→ladder). Upper bound DONE/certified —
NOT touched. Two decisive R13 developments folded in: (1) `coupled-cut-descent`'s single-cut
co-varying `b→b−1` descent is RIGOROUSLY REFUTED (`n=5`, non-tie, min reachable `D̃=5>3`) → RETIRE;
salvage Lemma TIE (`D̃=1⟹I_n=0`) + Lemma ΔM for certification. (2) peel §11.5's full-WM-IH `b`-lift
is REFUTED (WM and dyadic-threshold HLP both fail off the ladder) → the `b`-lift is NOT subsumed by a
WM-IH; reassigned to a new specialist. NOTE: partial-sum majorization ON THE LADDER survived a fresh
adversarial search, so peel §11's WM route still stands as a standalone base-slice claim.

Field: 3 far-apart routes on the base slice `(★)` (value-domination / Abel-parity / ladder-length
role-swap) + 1 fresh independent `b`-lift specialist (numeric layer IH) that does NOT go through the
ladder — the hedge if all base-slice routes stall on the tail-charge. I verified the new (D) route's
two statements myself (0 failures over 95k + 188k exact-`Fraction` configs) before seeding it.

---

peel-scale-rank-induction: advance
Target: `D̃(F)≥1` for all dyadic-refinement `F` (whole problem, with certified UB ⇒ `c(n)`).
Technique: peel top scale + value-domination (weak majorization / HLP threshold form) on the ladder.
Skeleton:
  1. Reduce (certified peel + `(FLOOR)` + `(★-id)`) to base slice `(★) Σ_blue-odd ≥ Σ_red-even`. — imported
  2. Prove `(★)` via `(WM)`/`(HLP)`: `∀t Φ(t)=∫_t^∞(N_BO−N_RE)ds ≥ 0` (self-similar truncation, §11.2). — HLP/Karamata
  3. Tail-charge red-even mass onto blue-odd rungs of ≥ value using `(DOM) b_i=1+Σtail` (one odd rung dominates its whole tail) + `(m₀≤1)`. — §11.4, THE open step GAP-P1′-a
Key lemmas:
  - `(DOM)` `b_i=2^{n−i}=1+Σ_{i'>i}b_{i'}` — geometric; one odd-rank rung's gap absorbs its entire even-red tail (cross-block cancellation the per-block charge lacked).
  - `(m₀≤1)` at most one red `>θ` — two reds `>θ` sum `>2θ=2^n=Σπ_0`; lone top red at rank 1 contributes 0 to RE.
Open gaps: GAP-P1′-a (the uniform-in-`t` tail-charge, step 3). §11.5's WM-IH `b`-lift is DEAD — DROP it from this file; the `b`-lift is now owned by `qlayer-charge-induction`.
Cases to cover: base slice `b=0`; `n=1` (both sides of `(★)` are 0); Case A closed (certified).
Watch out for: use partial-sum (weak) majorization, NEVER termwise 1-1 (FALSE: `n=3` `π_0=(2,2,2,2)`, BO=[4,1] RE=[2,2]). Do NOT present the truncation reduction as if it closes the tail-charge. Do NOT reopen §11.5 WM-IH (refuted off the ladder this round).

ladder-abel-pairing: advance
Target: `D̃(F)≥1` (whole problem).
Technique: Abel summation / summation-by-parts on the merged alternating sum, PAIRED by ladder rung; global parity closer. Positional/parity dual to the value-domination route — targets `(★)` EXACTLY (survives if WM over-shoots).
Skeleton:
  1. Reduce to `(★)` (imported peel + `(FLOOR)` + `(★-id)`).
  2. `D̃=Σ_{j odd}(w_j−w_{j+1})`, each gap ≥0 (descending). — Lemma G
  3. Re-pair each odd-rank blue rung `b_i` against the even-reds in its `(DOM)`-dominated tail `(0,b_i)` — cross-`k` telescope. — the DISTINCT move
  4. Boundary = optional lone leading red (`(m₀≤1)`, rank 1, contributes 0); parity of `ΣL=2^n−1` odd forces residual ≥0 (aimo-0388 mechanism). — GLOBAL parity, not a running-margin scan
Key lemmas: `(DOM)`, `(m₀≤1)` (as above); parity closer — colour-sum `Σπ_0−ΣL=1` fixed integer offset + non-positive telescoped gaps force residual ≥0.
Open gaps: the rung-telescoped pairing inequality (step 3) — same status as peel §11.4, reached by a different mechanism (diversity). General-`b` delegated.
Cases to cover: base slice `b=0`; `n=1`; ties (red/blue alternate ⇒ both sides 0, must give equality).
Watch out for: must NOT collapse to a one-directional positional running-margin scan (refuted, margins `→−2^{n−1}`); parity closer must be GLOBAL. Do NOT use the per-block same-block charge (51% fail).

ladder-length-deficient-induction: new
Target: `D̃(F)≥1` (whole problem); deliverable = base slice `(★)` in its stronger deficient-total generalized form.
Technique: mutual induction on ladder length `m`, peeling the single top rung `θ=2^{m−1}`, with a deficient-total generalization `(P_m)` coupled to a complementary-parity partner `(Q_m)`. Genuinely FAR from value-domination and Abel-pairing — a two-branch case split with a parity role-swap, living entirely inside `π_0` vs. a ladder (no `F'` cut-tree).
Skeleton:
  1. Reduce base slice to `(★)=(P_n)|_{ΣR=2^n}` (imported).
  2. Base `m=1`: `L_1={1}`, `R` `≤2` parts `ΣR≤2` — elementary.
  3. `(P_m)` step (both branch identities PROVEN by explorer): Branch 1 (one red `y_1>θ`) removes pair `{y_1,θ}` (ranks 1,2, contribute 0/0) ⇒ exactly `(P_{m−1})`, gap-free; Branch 2 (no red `>θ`, `θ` top) role-swaps to `BO=θ+BE'`, `RE=RO'` ⇒ target becomes `BO'−RE' ≤ 2^m−1−ΣR` = exactly `(Q_{m−1})`.
  4. `(Q_m)` step — THE OPEN GAP: establish `(Q_m)` `BO−RE ≤ 2^{m+1}−1−ΣR` from `{(P_{m−1}),(Q_{m−1})}` by the same top-rung peel with its own two-branch split (now up to two reds `>θ`), tracking the constant.
  5. `(P_n)|_{ΣR=2^n}=(★)` ⇒ base slice; general `b` delegated.
Key lemmas:
  - `(P_m)` deficient generalized ladder: `#R≤m+1`, `ΣR≤2^m` ⇒ `BO≥RE`. Deficient total (`≤`, not `=`) is what lets Branch 1 land inside the IH. VERIFIED 0/95528 (`m≤6`; explorer 0/32000 `m≤8`).
  - `(Q_m)` complementary: `#R≤m+2`, parts `≤2^m`, `ΣR≤2^{m+1}` ⇒ `BO−RE ≤ 2^{m+1}−1−ΣR`. The matching upper direction Branch-2 needs. VERIFIED 0/188304 (`m≤6`); the per-part `≤2^m` cap is load-bearing (fails 8.6% without it — checked this round).
  - Branch-1 pair-removal identity (PROVEN probe3) + Branch-2 role-swap identity (PROVEN probe9).
Open gaps: the `(Q_m)` recursion (step 4) — the sole real content; the `(P_m)` side is already proven, so the base slice closes the moment `(Q_m)` is established.
Cases to cover: `m=1`; `(P_m)` Branch 1/2; `(Q_m)` Branch 1/2 (up to two reds `>θ`); ties (equality/slack check at every level).
Watch out for: carry BOTH caps (part-count AND total) at every level — dropping either breaks the lemma (explorer 40–60% / 3.4% failures); Branch reductions must re-satisfy both (they do — verified). Preserve the per-part `≤2^m` cap in the `(Q_m)` recursion. NOT a positional running-margin scan.

qlayer-charge-induction: new
Target: `D̃(F)≥1` (whole problem) — attacks `I_n≤0` for GENERAL `F'` directly, NOT via the ladder base slice; the independent `b`-lift specialist and hedge.
Technique: peel induction on `n` with a loaded IH that is an inherited NUMERIC lower bound on `F''s negative-layer sum `Q` — NO majorization, NO ladder reduction, NO `b`-slicing. Stays inside the certified `(POS)/(LAYER)` machinery.
Skeleton:
  1. Reduce (certified `(FLOOR)`): `D̃≥1 ⟺ I_n=P−Q≤0 ⟺ Q≥P`; by certified `(POS)` `P≤S_π` (π_0's even parts) ⇒ suffices `(NEG) Q(π_0,F') ≥ S_π` for every `π_0`.
  2. Identify a numeric functional `Φ(F')` of the staircase `g=N_{F'}` (an `∫h(N_{F'})` matching the `2k` vs `2k−1` threshold asymmetry) with (a) `Q≥Φ≥max_{π_0}S_π`, (b) inherited under one peel `F'=π_1⊎F''`. — THE open design object
  3. Inheritance: `N_{F'}=N_{π_1}+N_{F''}` (certified `(U2)`) ⇒ `Q`/`Φ` splits sub-additively; `π_1` (partition of `θ`) supplies the increment matching `S_π`'s level-`n` growth; the unit budget slack `n−(n−1)` (Invariant I `M(0⁺)≤1`) closes the `½`.
  4. Base `n=1`; conclude `(NEG)` ∀`(π_0,F')`.
Key lemmas:
  - `(NEG)` reduction: `D̃≥1 ⟺ Q≥P`, `P≤S_π` (both certified) ⇒ pure lower bound on the negative-layer sum.
  - loaded numeric IH `Φ(F')` inherited peel-by-peel (recursive, non-local — NOT a static aggregate).
  - peel sub-additivity of `Q` via level-set additivity `(U2)`.
Open gaps: identify `Φ` and prove (a)+(b) (steps 2–3) — the crux. Genuinely different object from the ladder routes; if `Φ` collapses to a static aggregate and (b) fails, RETHINK.
Cases to cover: `n=1`; peel step general `F'`; Case A closed (certified); tie family (`Q=S_π` equality gate).
Watch out for: the SCALAR-SUMMARY BAN (static aggregate of `F'` refuted, 3 CEs R3–R4) — `Φ` is admissible ONLY as a peel-inherited recursive functional; the inheritance step (b) is what makes it legitimate, not optional. `M(0⁺)≤1` alone insufficient (decoy `D̃=0.146`) — `Φ` must read the full staircase shape. NOT a top-down/bottom-up positional reserve (refuted). Filter any candidate `Φ` on the n=2 witness `π_0={4959/2500,5041/2500}`, `F'={3323/2500,1677/2500,1}` (breaks WM, satisfies `(★)`).

coupled-cut-descent: RETIRE
Single-cut co-varying `b→b−1` descent RIGOROUSLY REFUTED (Prop REFUTE, `n=5` non-tie witness `π_0={16,16}`, `D̃(F)=3` but min reachable `D̃=5`). Reaching `F*` needs a global re-choice of `F'` ⇒ circular (= the theorem). Salvage Lemma TIE + Lemma ΔM for certification; the mechanism is dead. Not built.

---

Proposed slugs for ranking:
- peel-scale-rank-induction — advance (base slice `(★)` via WM/HLP tail-charge; §11.5 WM-IH b-lift dropped)
- ladder-abel-pairing — advance (base slice `(★)` via Abel/parity, exact target)
- ladder-length-deficient-induction — new (base slice `(★)` via mutual ladder-length induction P_m/Q_m; far route, both statements de-risked 0/95528 + 0/188304)
- qlayer-charge-induction — new (independent b-lift specialist: numeric negative-layer loaded IH for general F', no ladder, no majorization)
- coupled-cut-descent — retire (single-cut descent dead R12)
