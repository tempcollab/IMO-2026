# Proof-reviewer — Round 13 (imo-2026-03, IMO 2026 P3)

Two built approaches reviewed adversarially. Upper bound NOT re-reviewed (certified R7).

---

## BUILD 1 — ladder-length-deficient-induction

**Verdict: CHANGES REQUESTED.  Status: partial (base slice `(★)` = solved; whole GAP L = partial).**
Builder's recorded Status (`partial`, base slice fully proven) is CORRECT and not overclaimed.

### What it claims
The extremal base slice `(★)`: `D̃(π_0 ⊎ L_n) ≥ 1` for any multiset `π_0` with `Σπ_0=2^n`, `≤n+1`
parts — a wall open since round 3. Proved via a mutual induction on ladder length `m`: deficient LB
`(P_m)` ⇄ complementary UB `(Q_m)`, with a D̃-Lipschitz collapse `(LB_m)` unlocking `(Q_m)`.

### Adversarial scrutiny — every load-bearing step re-derived independently (exact `Fraction`)
- **Peel identities (I1) rung-peel, (I2) Branch-1 pair-removal, (I3) red-peel**: recomputed
  `D̃(R⊎L_m)` from scratch and compared to each identity's RHS. **0 failures** over 40k/40k/38k
  random exact configs. Exact.
- **(I4) D̃ 1-Lipschitz** (crux tool): reduced element values by random total `ε`, checked
  `|ΔD̃|≤ε`. **0 failures / 40k.** True and correctly applied.
- **Lemma 0** `Δ_m(R)=BO−RE`: **0 failures / 20k.**
- **The crux collapse `(LB_m)` from `(P_m)`**: re-checked the algebra by hand —
  `Δ_m(R)−Δ_m(R̂)=½[(D̃-diff)−ε]≥½[−ε−ε]=−ε`, so `Δ_m(R)≥min(0,2^m−ΣR)`. It uses only `(P_m)` at the
  *tight* total `ΣR̂=2^m` plus continuity of `D̃`. **Not circular** (dependency is `(P_m)→(LB_m)→(Q_m)`,
  strictly downward/same-level, grounded at `m=1`) and **not hiding the missing ½** — the ½ appears
  explicitly and the arithmetic is honest.
- **Both branches / all cases**: verified `(P_m)`, `(Q_m)`, `(LB_m)` hold on their EXACT stated
  domains — **0 violations** over 30k/41k/45k configs (m≤7, caps enforced). The `(Q_m)` per-part
  cap `≤2^m` is genuinely load-bearing: **3230 violations when the cap is dropped**, matching the
  builder's "~9%". The uniform red-peel (I3) in `(Q_m)` handles ANY number of reds `>θ`, so the
  outline's "≤2/≤3 reds" undercount is correctly rendered moot.
- **Base case `m=1`**: `(P_1)`, `(Q_1)` checked by hand; the `(Q_1)⟺w_1+w_3≤3` reduction and its
  pigeonhole contradiction are correct.
- **Hypothesis chains** `#R≤m+1`, `#R≤m+2`, part caps, total caps traced through Branch 1/2 and both
  `(Q_m)` cases — all satisfied at each recursive call.
- **Target**: independently enumerated integer partitions — `min D̃(π_0⊎L_n)=1` exactly for
  n=1..6, tie at `{2^{n−1}+1,…,1}`. Matches.

**Conclusion: `(★)` is genuinely FULLY and rigorously proven, no gap, no circularity, no unproven
leap.** This is a real milestone (base slice open since round 3).

### Why NOT APPROVE
Per the routing rule: even a fully-proven `(★)` leaves the WHOLE problem `partial`, because the
general-`b` lift (GAP-P1′-b: arbitrary dyadic-cut `F'` in place of the uncut ladder `L`) has no live
route. Builder correctly delegates it and does not overclaim.

### Certified this round
- `lemmas/base-slice-star.md` — base-slice theorem `(★)` + `(P_m)/(Q_m)/(LB_m)` engine + reusable
  sub-lemmas Lemma 0 (generalized ladder identity), (I1)–(I3) peel identities, (I4) D̃-Lipschitz.
  All hold to the full bar (verified, statements no stronger than proved).

---

## BUILD 2 — peel-scale-rank-induction

**Verdict: CHANGES REQUESTED.  Status: partial.** Builder's recorded Status is CORRECT.

### What it claims (round-13 deliverable, §11.6)
Reduces the weak-majorization goal `(WM) BO ≻_w RE` for the base slice to a FINITE list of scalar
rung inequalities via a Hardy–Littlewood–Pólya breakpoint argument; closes the top rung; shows the
residual (`i≥2`) is the SAME deficient-ladder object Build 1 proves.

### Scrutiny (exact `Fraction`, independent)
- **(i) `(WM) ⟺ Φ≥0 at all breakpoints`**: 0 mismatches / 920 configs. The `⟸` ramp-form proof
  (choose `t=RE^↓_k`) is correct.
- **(ii) Min of `Φ` at `t=0` or a `BO`-value** (breakpoint reduction): 0 exceptions. The
  convex-kink-only-at-`BO`-values argument is a correct standard majorization fact.
- **(ii) `Φ(θ)=0` unconditionally** (top rung closed via `m₀≤1`): 0 exceptions. Correct.
- **(iii) Residual reduces to Build 1's object**: the shift identity
  `Φ(b_i)=[ΣBO(P_i)−ΣRE(P_i)]−b_i(|BO(P_i)|−|RE(P_i)|)` on the scaled ladder `2b_i·L_{i−1}` is a
  genuine restatement, correctly identified as the deficient self-similar `(★)` that Build 1's
  `(P_m)/(Q_m)` recursion proves. So Build 1 closing that wall discharges Build 2's residual.

**No overclaim**: Build 2 does NOT claim the `b`-lift is closed, and honestly labels its own
residual open (it did not independently close the base slice — it bridged its route to Build 1's).

### Certified this round
- `lemmas/hlp-breakpoint-reduction.md` — the general HLP breakpoint reduction of weak majorization
  (parts (a),(b)) + `Φ(θ)=0`. A clean, reusable, dyadic-free tool. Held to the full bar.

---

## Field status after round 13
- Upper bound: DONE/certified (R7). GAP L Case A: closed. GAP L Case B base slice `b=0`: **now
  CLOSED** (`base-slice-star.md`). **Sole open wall: GAP-P1′-b, the general-`b` lift** (`F'` a general
  dyadic cut, not the ladder) — no live route. Next round's outliner must seed a route for the
  `b`-lift; watch-outs (R10/R11): must ADD cuts to `F'` (never merge even tie-blocks — merging can
  RAISE `D̃`), must read the true staircase shape of `g=N_{F'}`, pointwise `π_0`-fixed monovariant is
  FALSE (~30%). Candidate: adopt `(WM)` / the deficient-ladder generalization as a LOADED IH inherited
  under one further peel `F'=π_1⊎F''` (Build 2 §11.5).

`current.md` Status updated to reflect the base-slice milestone; whole problem remains `partial`.
