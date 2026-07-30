# Proof-reviewer — Round 15 (imo-2026-03, the b-lift GAP-P1′-b)

Two builds judged independently. No APPROVE; whole problem stays `partial`. All load-bearing
identities re-derived from scratch and reproduced with exact `Fraction` (my own scripts, not the
builders').

---

## 1. ladder-length-deficient-induction — CHANGES REQUESTED (Status: partial)

**Recorded Status in the approach file (`partial`) is CORRECT.** The builder does not overclaim; it
explicitly isolates one open leaf.

### What I verified independently
- **Exact cut-top-rung correction (C)** `D̃(R⊎F')=D̃(ρ₁)−D̃(W)+2λ(E∩O_W)` (equiv. Δ-form with
  `I_S=λ(O_{ρ₁}∩O_W)`): re-derived and tested **0 fails / 30000** exact-Fraction configs (cut rung
  `r∈[2,4]`, reds ≤ θ). The parity-split derivation (odd-`N_{ρ₁}` band unchanged, even-`N_{ρ₁}` band
  `E` flips by `2·1[N_W odd]−1`, `λ(E)=θ−D̃(ρ₁)`, `D̃(U)=θ−D̃(W)` via MAXPEEL) is correct. This is
  the genuine "carry the below-`p_r` tail exactly" term, not a lossy Lipschitz merge.
- **(A1),(A2),(A3) Δ-form reductions**: **0 fails / 15000 each**. (A1)=MAXPEEL, (A2)=general (I2),
  (A3)=(I3′) in Δ-form; all sound.
- **(P̂_m)/(Q̂_m) statements themselves are TRUE**: **0 fails / 44198 (P̂) and 49927 (Q̂)** under the
  stated budgets — so the framing is not broken; the induction targets are correct statements.
- **Spec-correction claim is CORRECT.** `π₀={2,2}, F'={3/2,3/2}` gives `D̃=0` (parts ≤ θ=2, Σ=3):
  the b-lift is genuinely FALSE without the budget. Note this particular witness is not even a
  structural rung-refinement, but the second witness (rung-sums + 7 cuts, `D̃=0`) is the real one
  and confirms the budget `Σa_i≤n` is load-bearing and non-local — consistent with rounds 6–14. The
  "spec correction" is really a re-emphasis that the game's budget was always part of the target; the
  outline's shorthand dropped it. No error, correct caution.

### The load-bearing logic (checked)
The mutual induction closes **every uncut-top-rung case**: Case Ia via (A2)+`(P̂_{m−1})`, Case Ib via
(A1)+`(Q̂_{m−1})`, `(L̂B_m)` via the certified D̃-Lipschitz collapse, `(Q̂_m)` `y>θ` branch via
`(L̂B_m)`. Base `m=1` is fully settled including the cut case (`a₀=0`, `F'={p,1−p}`, direct). The
sole open leaf is **Case II = cut top rung** (`a₁≥1`), which peels via (C) to exactly
`I_S=λ(O_{ρ₁}∩O_W)` = the certified **GAP-P1** overlap wall. Honestly stated as open in §4/§6.

### Verdict rationale
This is real forward progress, not a re-encoding of R14's dead-end: R14 had **no live route**; this
reduces the whole b-lift to a **single concrete case** and equips it with a genuinely new, unused
resource (the budget `a₀+Σa_i≤m` constrains `a₁` non-locally). But the wall (`I_S`) is not bounded —
the gap remains. **CHANGES REQUESTED / partial.** Next: bound `I_S≤½θ+½D̃(ρ₁)+Δ(R,F'')` using
`a₁≤m−a₀−Σ_{i≥2}a_i` with a non-scalar invariant on the cut rung's fragment structure (scalar
`0≤I_S≤D̃(ρ₁)` is vacuous, R14).

**Scores** — Correctness 5/5 (every proven step verified); Rigor 4.5/5 (open leaf honestly isolated,
no hand-waving; §3 (P̂_1)'s three-ordering check is terse but correct); Progress 4/5 (single-case
reduction + new resource + 2 exact identities where R14 had nothing live).

**Certified:** `lemmas/cut-top-rung-correction.md` — (C) + (A1)/(A2)/(A3), all re-derived + 0-fail.
NOT certified: the `(P̂_m)/(Q̂_m)/(L̂B_m)` STATEMENTS — true numerically but proved only for the
uncut-top-rung step (cut case open), so they fail the "no stronger than proved" bar as theorems.

---

## 2. bottom-band-peel-induction — RETHINK (Status: unsolved)

**Recorded Status (`unsolved`/RETHINK, retire) is CORRECT.** An honest structural negative; nothing
overclaimed (explicitly labels the framing dead).

### What I verified independently
- **Bottom-band overlap identity** `D̃(F)=D̃(F_{>τ})+(−1)^{|F_{>τ}|}D̃(F_{≤τ})`: re-derived from
  SD/PEEL + the constant-`N_{F_{>τ}}` argument on `(0,τ)`; tested **0 fails / 30000** exact-Fraction
  (integer and fractional). Correct.
- **Cheap-kill witnesses**: `F={2,2,1,1,1}` → `D̃=1`, scale peel `G={2,2,1,1}` → `D̃(G)=0` (so
  `D̃(G)≥2` fails); `F={4,4,2,2,1,1,1}` → `D̃=1`, `F_{>1}={4,4,2,2}` → `D̃=0` (surplus entirely on
  bottom fragments; `F_{>τ}` is not a feasible sub-instance). Both reproduced exactly.
- The odd branch is a difference = the certified DIFF/overlap term; the split is genuinely
  split-agnostic and does not escape GAP-P1. The near-0/parity injector needs integers and the
  integer route (GAP-IMR) is proven equivalent-difficulty (R10) — correctly cited.

**Verdict:** the framing cannot close the b-lift; retire. **RETHINK / unsolved.** The one exact gain
(the bottom-band identity) is worth banking.

**Scores** — Correctness 5/5 (identity + all witnesses verified); Rigor 5/5 (honest negative, gate
run first, no forced proof); Progress 1.5/5 (dead-end, but a clean certified identity banked).

**Certified:** `lemmas/bottom-band-overlap.md` — identity re-derived + 0-fail; flagged as an
accounting tool, NOT a closer.

---

## Summary
- ladder-length-deficient-induction: **CHANGES REQUESTED** (partial). advanced. 2 lemmas certified
  (cut-top-rung-correction.md).
- bottom-band-peel-induction: **RETHINK** (unsolved). dead-end/retire. 1 lemma certified
  (bottom-band-overlap.md).
- `current.md` Status updated (still `partial`; b-lift reduced to the single cut-top-rung case).
- No APPROVE this round; the sole open wall remains `I_S` (GAP-P1) on the cut top rung, now with the
  budget as a fresh unused resource.
