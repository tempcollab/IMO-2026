## imo-2026-03

Field this round: **one approach advanced/revised** (the cut-top-rung leaf, re-planned with the
newly-available `(L̂B_{m−1})` inheritance), plus an explicit **lean decision** on diversity
(no filler slug — reasoning at the end). Upper bound + (★) base slice are DONE/certified; nothing
opened on them.

---

ladder-length-deficient-induction: **revise** (re-plan the sole open gap — the cut-top-rung leaf —
folding in `(L̂B_{m−1})` admissibility to BANK the `ΣR≤θ` half, and installing the comb/teeth
skeleton for the `ΣR>θ` residual)

Target: `D̃(π₀ ⊎ F') ≥ 1` for every budgeted refinement `F'` of `L_n` with `a₀+Σaᵢ ≤ n`
(the b-lift, `GAP-P1′-b`). Closing it + certified UB (`lemmas/upper-bound.md`) + Case A gives
`c(n) = 2^n/(2^{n+1}−1)` — the whole problem, end to end.

Technique: the budget-aware mutual induction `(P̂_m)/(Q̂_m)/(L̂B_m)` on ladder length `m` (certified
machinery, already closes EVERY uncut-top-rung case). The distinct route for the open cut-top-rung
leaf: **spend the cut (`a₁≥1`) to inherit the FULL deficient lower bound `(L̂B_{m−1})` on `(R,F'')`**
(not just the `(Q̂_{m−1})` upper bound the file currently claims), then split the leaf by `ΣR` vs `θ`.

Skeleton:
  1. All uncut-top-rung cases of `(P̂_m)/(Q̂_m)/(L̂B_m)` — CLOSED & reviewer-verified (§3–§5 of the
     approach file; imports (A1)(A2)(A3) + correction (C) from `lemmas/cut-top-rung-correction.md`,
     the D̃-Lipschitz collapse (I4) from `lemmas/base-slice-star.md`). No change; advance verbatim.
  2. Cut top rung, exact peel — by correction (C) (certified):
     `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S`, `I_S := λ(O_{ρ₁} ∩ O_W)`, `W = R⊎F''`,
     `θ = 2^{m−1}`, `ρ₁` the cut top rung (`Σρ₁=θ`, `r:=|ρ₁|=a₁+1≥2`, all parts `<θ`).
  3. **NEW — `(L̂B_{m−1})` inheritance on the leaf** (corrects the file's §4/§6 "only `(Q̂_{m−1})`
     available"): `(L̂B_{m−1})` applies to `(R,F'')` and gives `Δ(R,F'') ≥ min(0, θ − ΣR)` — because
     a CUT top rung SPENDS a budget unit, so `a₀+b'' ≤ m−a₁ ≤ m−1` (its budget hypothesis), while
     reds `≤ θ = 2^{m−1}` and `ΣR ≤ 2^m = 2^{(m−1)+1}` are exactly `(L̂B_{m−1})`'s remaining
     hypotheses. Verified 0-fail / ~70k trials (explorer probe4).
  4. **NEW — sub-case `ΣR ≤ θ`: CLOSED (bank as sub-lemma).** Step 3 gives `Δ(R,F'') ≥ 0`
     (at `ΣR=θ`, `min(0,θ−ΣR)=0` — boundary safe). Then
     `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S ≥ ½θ + ½D̃(ρ₁) − I_S ≥ ½θ − ½D̃(ρ₁) ≥ 0`,
     using `I_S ≤ λ(O_{ρ₁}) = D̃(ρ₁)` and `D̃(ρ₁) ≤ θ` (`D̃` ≤ max part `< θ`). Two lines.
     Verified 0-fail / all `ΣR≤θ` configs, m=2..5 (outliner probe this round).
  5. **GAP — sub-case `ΣR > θ` (oversized reds).** Step-3 floor is now negative (`θ−ΣR<0`); the
     naive route `I_S ≤ D̃(ρ₁)` + floor fails ~31–37 % of oversized configs (this round's probe),
     though the true `Δ(R,F') ≥ 0` always. Need a JOINT bound on `I_S` sharper than both scalar
     ceilings — see key lemma (TEETH).
  6. **GAP (mirror) — Case IIa (some red `y>θ`).** By (A3), `Δ(R,F') = (2^m−1−ΣR₀) − Δ(R₀,F')`,
     `R₀=R∖y`, `ΣR₀ = ΣR−y < 2^m−θ = θ`. This needs the cut-top-rung `(Q̂_m)` UPPER bound
     `Δ(R₀,F') ≤ 2^m−1−ΣR₀`, which by (C) is a LOWER bound `I_S₀ ≥ Δ(R₀,F'')+½θ+½D̃(ρ₁)−(2^m−1−ΣR₀)`
     — the same overlap term, opposite direction. Same (TEETH) mechanism, lower-bound side.

Key lemmas (claim + the mechanism that makes it true):
  - **(L̂B-inherit)** `Δ(R,F'') ≥ min(0,θ−ΣR)` on the cut-top-rung leaf — because `a₁≥1` frees one
     budget unit (`a₀+b''≤m−1`), making `(L̂B_{m−1})` (from `(P̂_{m−1})` + the certified Lipschitz
     collapse (I4)) admissible on `(R,F'')` with no slack. This is the previously-unexploited
     resource; the file wrongly inherits only `(Q̂_{m−1})`.
  - **(ΣR≤θ closure)** `Δ(R,F')≥0` when `ΣR≤θ` — because the surplus `½θ+½D̃(ρ₁)` dominates the
     scalar ceiling `I_S≤D̃(ρ₁)` exactly when `D̃(ρ₁)≤θ`, once `(L̂B-inherit)` supplies `Δ(R,F'')≥0`.
     (Certifiable as a stand-alone sub-lemma — bank it even if the residual stays open.)
  - **(TEETH) [THE HARD STEP — GAP]** `I_S = λ(O_{ρ₁}∩O_W)` needs the JOINT bound
     `I_S ≤ Δ(R,F'') + ½θ + ½D̃(ρ₁)` (upper, for `(P̂)`) / the mirror lower bound (for `(Q̂)`), in the
     `ΣR>θ` regime. Mechanism to build: `O_{ρ₁}` is a **comb** of exactly `⌈r/2⌉` disjoint teeth
     `(p₂,p₁),(p₄,p₃),…` (+ `(0,p_r)` if `r` odd), `p₁>…>p_r` the sorted rung — so `a₁=r−1` controls
     tooth COUNT (NOT tooth measure: `D̃(ρ₁)` is NOT `a₁`-monotone, cheap-killed — do not assume it).
     `I_S = Σ_{teeth} λ(tooth ∩ O_W)`. `O_W` is itself a step-function odd-set with `≤ a₀+b''+1
     ≤ m` breakpoints (budget-limited). The joint charge: bound each tooth's overlap against `O_W`
     using the exact even-complement `λ(E∩O_W) = D̃(W) − I_S` (`E=(0,θ)∖O_{ρ₁}`) and the
     mass identity `D̃(W)=2Δ(R,F'')+ΣR−(θ−1)`; in the `ΣR>θ` regime the oversized red mass forces
     `O_W` to occupy the low band, where the teeth alternate — a pigeonhole/inclusion–exclusion
     across `⌈r/2⌉` teeth vs `≤ a₀+b''+1` `O_W`-breakpoints. **This is the unproved load-bearing
     step.** NB (proved this round): ANY purely scalar ceiling is vacuous — `I_S≤min(D̃(ρ₁),D̃(W))`
     combined with both inherited bounds telescopes to `Δ(R,F')≥−½θ+½D̃(ρ₁)≤0` (the R14 dead
     estimate). The bound MUST use the per-tooth geometry, not a scalar summary.

Open gaps: step 5 (`ΣR>θ` upper-bound `I_S` via TEETH) and step 6 (the `(Q̂)` mirror lower-bound
`I_S`, same mechanism). Everything else is closed/certified.

Cases to cover:
  - Case I (top rung uncut): DONE (certified, (A1)/(A2)).
  - Case IIb, `ΣR≤θ`: DONE this round (steps 3–4), bank as sub-lemma.
  - Case IIb, `ΣR>θ`: GAP (step 5).
  - Case IIa (`y>θ`, forces `ΣR>θ`): GAP-mirror (step 6).

Watch out for:
  - `ΣR=θ` boundary — folds into `≤θ`; `(L̂B-inherit)` floor is `min(0,0)=0` there, safe.
  - Do NOT assume `D̃(ρ₁)` (or `I_S`) shrinks with `a₁` — FALSE (one dominant part `θ−(r−1)ε` +
    tiny fragments pushes `D̃(ρ₁)→θ` for every `r`; cheap-killed, explorer). `a₁`'s ONLY leverage is
    (i) the budget it spends → `(L̂B-inherit)`, and (ii) the tooth COUNT `⌈r/2⌉`.
  - The `(Q̂)` mirror (step 6) is genuinely harder — a LOWER bound on `I_S` requires showing teeth
    actually MEET `O_W`, not just that they are few. Do not assume the upper-bound argument dualizes
    for free.
  - Do not re-inherit only `(Q̂_{m−1})` (the file's current wording) — `(L̂B_{m−1})` is the correct,
    stronger inheritance and is what makes step 4 close.

---

### Diversity decision (shared-gap rule, plateau R11–R15): NO new filler slug — deliberate, lean

Both explorer lenses converged this round on the same negative, so per the task's "if the only
candidate re-encodes a dead route, do NOT open a filler" I am keeping the field to one live approach:

- **per-rung-equality lens: DRY** (explorer verdict, explicit "do NOT open a slug"). Its recursive
  form IS the live `(P̂/Q̂)` engine; its additive/union/scalar-coefficient forms re-encode the R15
  union-bound cheap-kill (`Q` is inherently cross-rung) and the R11 scalar-`b` refutation.
- Every non-`(P̂/Q̂)` framing on the `ΣR>θ` residual is already a recorded dead end: π₀-fixed
  comparison / multi-cut merge (R14), ABSORB engine + split-rung (I1′) (R14), NEG-lemma value/layer
  forms + independent-subgame decomposition (R15), bottom-band/near-0 Parity peel (R15), all
  measure/merged-order/sequential/genfn/GAP-IMR framings (R8/R10). A second slug drawn from any of
  these would share the leaf's wall and die with it (the single-gap trap) — worse than none.
- The genuinely NEW lever this round (the comb/teeth geometry of `O_{ρ₁}`) is not a rival framing:
  it lives on the same leaf via correction (C) and IS the primary's next step. Splitting it into a
  separate slug would violate "one whole attempt = one slug."

Two speculative directions are logged as **cheap-kill candidates for next round's explorer** (NOT
slugs — neither is vetted, and opening either now would be a filler):
  (a) the discrete run-length / ±1-jump recast of `M` on the sorted breakpoint sequence
     (per-rung-equality lens, opening 3) — cheap-kill on the extremal ladder family + neighbors first;
  (b) a red-side peel of the largest red (≤θ) via MAXPEEL as an alternate reduction of the `ΣR>θ`
     leaf — cheap-kill whether it yields a non-circular recursion before committing.

If the TEETH step stalls next round, the explorer should vet (a)/(b) numerically; only a
cheap-kill survivor earns a slug. Until then the field stays lean at one live approach on the leaf.

build hint for outline-reviewer: build set should be {ladder-length-deficient-induction} — advance
the revised leaf plan (bank steps 3–4, attack steps 5–6 via TEETH).
