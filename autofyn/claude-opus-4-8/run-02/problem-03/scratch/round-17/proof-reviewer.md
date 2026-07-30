# Proof review — round 17 (imo-2026-03)

## ladder-length-deficient-induction

**Verdict: CHANGES REQUESTED. True Status: partial.** (Builder's recorded Status `partial` is CORRECT — no overclaim.)

Scores: Correctness 9/10 (every written step valid) · Completeness/rigor 5/10 (two
endpoint leaves genuinely open) · Progress 8/10 (the S1+S2 collapse strips the whole
`ΣR>θ` residual down to a measure-zero endpoint slice — a real sharpening over R16).

### Independent verification (exact `Fraction`, `/tmp/rev17.py`, `/tmp/rev17b.py`)

- **`D̃` formula.** `D̃(P)=Σ(−1)^{i−1}w_i` (descending) `= λ{t:N_P(t) odd}` cross-checked
  equal on 2000 random multisets, 0 mismatches. Load-bearing identity confirmed.
- **(S1) trivial band — SOLID, unconditional.** Re-derived the algebra myself:
  `Δ(R,F')=½(D̃(R⊎F')−ΣR+ΣF')` and `ΣF'=2^m−1` (def. of budgeted refinement) give
  `Δ≥0 ⟺ D̃≥ΣR−2^m+1`. On `ΣR≤2^m−1` the RHS `≤0`, closed by certified `(NN) D̃≥0`.
  0 violations over 240k configs (m=2,3). Genuinely trivial and genuinely subsumes the
  entire R16 cut-top-rung `θ<ΣR≤2^m−1` machinery. Correct.
- **(S2) Lipschitz fill — SOLID, conditional reduction.** Fill feasibility confirmed
  (`ΣR>2^m−1>θ`, reds `≤θ` ⇒ `≥2` reds ⇒ slack `(a₀+1)θ−ΣR ≥ 2θ−ΣR = ε`). Certified `(I4)`
  applied with total decrease `ε=2^m−ΣR ∈(0,1)` gives `D̃(R⊎F')≥D̃(R'⊎F')−ε`. 0 Lipschitz
  violations. Correctly DEFERS the +1 to the endpoint (does not inject it) — honestly stated,
  not a hidden closure.
- **Anchor `D̃(F')≥1` (`≤m−1` cuts) — verified, but CONDITIONAL on the open IH.** Uncut-branch
  (MAXPEEL `D̃(F')=θ−D̃(F'')`, `D̃(F'')≤ΣF''=θ−1`) is unconditional and correct. Cut-branch is
  `D̃(ρ₁⊎F'')=(P̂_{m−1})` at endpoint `ΣR̄=2^{m−1}`, budget `a₁+b''≤m−1` — a STRICTLY SMALLER
  b-lift instance (descent in m, base m=1 proven). Non-circular. Numerics: min `D̃=1` at `≤m−1`
  cuts, drops <1 at `m` cuts (m=2: 0, m=3: 0, m=4: 1/6) — the spare budget unit is genuinely
  load-bearing.
- **Retraction of the `θ`-red-forcing slack claim — CORRECT.** Confirmed the exact witness
  `R={3,3,2}` (ΣR=8=2^3, all reds <θ=4, no red =θ), `F'={2,2,2,1}` (top rung `{2,2}` cut,
  budget 3=m): `D̃=1` exactly. So "no red =θ ⟹ D̃≥13/12" is FALSE, and the builder's retraction
  (going further than the outline-reviewer's proposed cut-top-rung restriction) is right — the
  outline-reviewer's restricted claim (min≈1.12) is also refuted by this cut-top-rung witness.
- **Endpoint target real & razor-tight.** `D̃(R⊎F')≥1` on `ΣR=2^m`, min `D̃=1` exactly (m=2,3).
  The wall is a genuine equality core, not a false target.

### The two CLOSED leaves — legitimately closed as induction steps
- S3-U big-red: `(A2)` ⇒ `Δ(R,F')=Δ(R₀,F'')`, `ΣR₀<θ` interior ⇒ `(P̂_{m−1})` (IH). Genuine
  descent (`ΣR₀<θ`, not endpoint). Correct.
- pure-blue / `{θ,θ}` tail: via the anchor (IH `(P̂_{m−1})`). Correct.
Both use the inductive hypothesis `(P̂_{m−1})` — legitimate; the step is incomplete only because
the other two leaves are open (so `(P̂_m)` is not established for m≥2 — honestly the reason the
whole thing is partial, no false claim made).

### The two OPEN leaves — honestly open, not secretly closable, not circular
- (i) S3-U all-reds-`≤θ`: `(A1)` at `ΣR=2^m` ⇒ `Δ(R,F')=−1−Δ(R,F'')`, needs `Δ(R,F'')≤−1` =
  `(Q̂_{m−1})` at the TOP of its range (cut-top-rung `(Q̂)` branch). Per §5 that exact branch
  (`ΣR>2^m` cut-top-rung of `(Q̂_m)`) is the still-open one. Genuinely open.
- (ii) S3-C all-reds-`≤θ`: `(C)` ⇒ the overlap wall `I_S≤Δ(R,F'')+½θ+½D̃(ρ₁)`, which §6 shows is
  literally the target restated (identity, not a lemma) — `D̃=1` attained. Correctly NOT assumed.

### Bans / circularity audit — CLEAN
No scalar `I_S`-ceiling used to close; the `(†)/(‡)` teeth/parity-mismatch form is explicitly NOT
assumed (retained only as the exact algebraic form of the residual); the refuted all-or-nothing
tooth capture is retracted; no merged-order/measure/sequential/genfn closer; `(L̂B-inherit)` is the
certified deficient bound, not the refuted scalar fill; `θ`-red-forcing retracted. All banned
routes avoided.

### Certification decision
No new standalone lemma certified this round.
- **S1** is unconditional and correct but a one-line corollary of certified `(NN) D̃≥0` — inline,
  not lemma-worthy (declined to avoid clutter).
- **S2** is conditional on the open endpoint claim — not a theorem yet.
- **Anchor** cut-branch is conditional on the open IH `(P̂_{m−1})` — not a theorem yet.
This matches prior role guidance (do not certify results conditional on the open IH).

### Remaining gap (for next round)
Close the two measure-zero endpoint leaves at `ΣR=2^m`:
(i) the `(Q̂_{m−1})` cut-top-rung endpoint upper bound `Δ(R,F'')≤−1` (a genuinely NEW upper bound;
existing `(Q̂_m)` is `2^m` too weak), and
(ii) the `(C)` overlap wall (equivalent to the target on this slice; needs a non-scalar cut-tree
invariant on `O_{ρ₁}` vs the budget-limited breakpoints of `O_W`).

Both are honest, razor-tight, and correctly labelled open. Whole problem: **partial**.
