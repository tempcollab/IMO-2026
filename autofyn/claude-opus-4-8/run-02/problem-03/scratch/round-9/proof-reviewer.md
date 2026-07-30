# Proof Review — imo-2026-03 (IMO 2026 P3), Round 9

Sole open wall: GAP L (lower bound), `D̃(F) ≥ 1` for every dyadic-feasible refinement
`F = ⊎_{j=0}^n π_j`, `Σa_j ≤ n`, total `2^{n+1}−1`. Upper bound is DONE/certified. I
re-derived every load-bearing claim below and reproduced all numerics with exact
`Fraction` arithmetic. Neither slug closes GAP L; the whole problem stays `partial`.

Independent checks (all passed, exact arithmetic):
- `D̃` descending-alt-sum ≡ level-measure `λ(O_F)`: `0` mismatches / 3·10³.
- Parity Lemma: `0` even and `0` negative over `2·10⁵` random odd-total integer multisets.
- Peel (SD) identity + difference bound (DIFF): `0` mismatches / `0` violations / 5·10³+1.2·10⁵.
- Integer feasible min `= 1` by exhaustive enumeration for `n ≤ 5`; attaining families in both
  slugs verified (`D̃=1`, correct total `2^{n+1}−1`).
- Continuum sampled min `≈ 1.0000` (`n=3,4`, 2·10⁵ each) — target numerically true.
- Slug-2 §7a witness reproduced exactly: `D̃(F')=2.506`, `D̃(π_0⊎F')=0.146<1`.

---

## Slug 1 — vertex-integrality-parity

**Verdict: CHANGES REQUESTED. Status: partial.**

**Parity Lemma (Part 1) — CORRECT, airtight, CERTIFIED.** For an integer multiset of odd
total, `D̃ = O − E = ΣF − 2E ≡ ΣF ≡ 1 (mod 2)`, and `D̃ ≥ 0` by pairing consecutive
descending terms ⇒ `D̃ ≥ 1`. Both steps are valid; the hypothesis is odd *total* (always true
here, `2^{n+1}−1`), not odd part-count. This is a genuine non-local `+1` injection not caught
by the R8 equivalence meta. Certified → `lemmas/parity-odd-total.md`.

**Part 2 (integer min = 1, attaining family) — CORRECT.** Lower bound is the Parity Lemma;
the explicit family `{2^{n−1},2^{n−1},…,4,4,3,2,1,1}` gives `D̃=1` (verified), and enumeration
confirms integer min `= 1` for `n ≤ 5`. Also correctly verifies the answer `c(n)=2^n/(2^{n+1}−1)`
is tight.

**Part 3 Main Reduction (easy direction) — CORRECT.** `Φ_n` compact, `D̃` continuous ⇒ min
attained; if attained at an integer config, `μ ≥ 1` by Parts 1–2, so `D̃ ≥ μ ≥ 1` everywhere.
Valid.

**Sole gap GAP-IMR — genuinely open, non-circular.** The claim "`inf_{Φ_n} D̃` is attained at
an integer configuration" makes no reference to the value `1`, so it is not circular as a proof
obligation (this correctly answers the R8-trap concern). It is verified `n ≤ 3` (exact) but
UNPROVEN in general: the optimum can sit on a fractional flat face, and single-block rounding is
blocked because a group's block-sum `n_g·v` may be non-integer, so closure needs a *global*
integral mass-transfer / optimal-cell-TU argument. The builder honestly located this obstruction.
Not closed.

**Overclaim check:** the recorded Status `partial` is accurate. The deleted TU/B2 core was
correctly retired (I did not re-litigate it). No overclaim.

Outcome recorded: **advanced** (Parity Lemma is real, certified, bankable progress).

---

## Slug 2 — peel-scale-rank-induction

**Verdict: CHANGES REQUESTED. Status: partial.**

**(SD)/(PEEL) identity — CORRECT.** `O_{A⊎B}=O_A△O_B` from parity-XOR of `N`, giving
`D̃(F)=D̃(A)+D̃(B)−2λ(O_A∩O_B)=λ(O_A△O_B)`. Verified `0` mismatches. Certified.

**Case A (`a_0=0`) closed UNCONDITIONALLY — CORRECT and clean.** `O_{π_0}=(0,2^n)⊇O_{F'}` ⇒
`λ(∩)=D̃(F')` ⇒ `D̃(F)=2^n−D̃(F')`; with `D̃(F') ≤ ΣF' = 2^n−1`, `D̃(F) ≥ 1`. Uses only the
universal `D̃ ≤ Σ`, no value-IH. Re-derived and correct — a genuine new unconditional closure of
the `a_0=0` branch.

**Difference bound (DIFF) — CORRECT.** `λ(∩) ≤ min(D̃(A),D̃(B))` ⇒ `D̃(F) ≥ |D̃(π_0)−D̃(F')|`.
Verified `0` violations. Closes Case B on `{|·|≥1}`. The "80.8%" figure is a non-load-bearing
coverage statistic; fine.

**Invariant I — CORRECT.** `M(0⁺)=(a_0+1)−|F'|`, `|F'|=n+b`, budget `a_0+b≤n` ⇒
`M(0⁺)≤1−2b≤1`, equality iff `b=0,a_0=n`. Re-derived, correct.

Certified the bundle → `lemmas/peel-difference-bound.md`.

**Sole gap GAP-P1 — genuinely open.** Case B residual `{|D̃(π_0)−D̃(F')|<1}` (near-balance).
The builder proves rigorously (verified witness `D̃(F')=2.506`, `D̃(π_0⊎F')=0.146`) that the
plain value-IH is insufficient, so a *loaded dyadic-shape* invariant on `F'` is required. No such
invariant is yet shown both inherited by `F'` and sufficient to force (RESID); the circularity
risk (must be strictly stronger than `D̃≥0` yet not the target) is honestly flagged, not resolved.
Not closed.

**Overclaim check:** recorded Status `partial` is accurate. The cases are disjoint and exhaustive
(A `a_0=0`; B split by (DIFF)). No overclaim.

Outcome recorded: **advanced** (Case A unconditional + certified machinery).

---

## Certified this round
- `lemmas/parity-odd-total.md` — Parity Lemma (integer multiset + odd total ⇒ `D̃` odd ⇒ `≥1`).
- `lemmas/peel-difference-bound.md` — (SD)/(PEEL) identity, difference bound (DIFF), Case-A
  unconditional closure, Invariant I.

## Bottom line
No APPROVE: GAP L (hence P3) is not solved. Both mechanisms are genuine, non-profile advances
(certified) that bottom out on the same residual — injecting the constant `1` requires a GLOBAL
argument (integer-minimizer reduction / loaded dyadic-shape IH). `current.md` updated to reflect
this true state. Both slugs stay live: CHANGES REQUESTED, re-dispatch to close GAP-IMR / GAP-P1.
If both stall again, the shared-wall signal says seed a mechanism routing the `+1` WITHOUT the
odd-total parity (2-adic valuation through the ±-operation tree; shadow/position-map to the
`D̃=1` zigzag family).
