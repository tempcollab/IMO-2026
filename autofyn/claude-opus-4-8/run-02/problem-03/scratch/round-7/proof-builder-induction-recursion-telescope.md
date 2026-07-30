# Build report — induction-recursion-telescope (imo-2026-03, GAP L), round 7

**Status: partial** (residual `maxc≥2` T-run case NOT closed; sharpened, and two more IH shapes killed).

## What I closed / added (all rigorous, numerically pre-checked)

1. **Exact threshold-split identity `(△)` (NEW, fully proved, §13).**
   `D̃(F) = (y₁−θ)⁺ + λ_{(0,θ)}(O_Y △ O_Z)`, `θ=2^{n−1}`. This is the *equality* refinement of the
   round-2 inequality `(★★)` (which only gave `≥ (y₁−θ)⁺ + |D̃(Y)^{<θ}−D̃(Z)|`). Proof uses parity
   XOR + the half-total single-crosser fact (≤1 `Y`-fragment exceeds `θ` since `sum Y=2θ`). Verified
   `0/2·10⁵` over `n≤6`.

2. **Localized reduction `(△⋆)` (NEW, proved).** The entire Case-B target `D̃≥1` is equivalent to the
   single **bounded-mass** inequality `λ_{(0,θ)}{M odd} ≥ ∫_{(0,θ)}M = 1−β`, `M=N_Y−N_Z`,
   `β=(y₁−θ)⁺∈[0,1]`. RHS mass is `≤1` (small when `y₁≈θ`). This is `(♣)` restricted to the window
   `(0,θ)` with a capped right side — the cleanest statement of the residual so far.

3. **LAYER identity re-confirmed** (`D̃−1 = 2(Σλ(B_{2k−1})−Σλ(A_{2k}))`), 0 violations.

## What remains open (the residual)

The `maxc≥2` residual is unchanged in kind: `(△⋆)` still requires controlling positive excursions
`M≥2`, i.e. the T-run deficit vs anchor surplus. I did NOT close it. Both bounds (`D̃≥1`, min over
`2·10⁵` Case-B samples) sit at exactly `1.0` (non-strict, tie-attained), consistent with prior rounds.

## Reserve shapes now refuted (Spec concerns — redirect for next round)

- **§10 (round 6, standing):** no *local* value/width-dominating injection `{Y even-pos}→{Z odd-pos}`
  (survival-domination fails on 21% of configs).
- **§14 (NEW round 7):** the outline's **top-down reserve** `R_Z(τ)` IH shape is refuted. The clean
  version "`Z`'s odd-level measure leads its even-level measure from the top" fails on `7306/4·10⁵`
  configs (worst `−22.5`). Worked tie config `n=4, Y=(8,3,3,2), Z=(8,2,2,2,1)`: by `(△)` the ENTIRE
  surplus is the **near-0 band** `(0,1)` (there `N_Z=5` odd vs `N_Y=4` even — a pure part-count parity
  effect, `|Z|=5>|Y|=4`), while the top anchor `z₁=8=θ` sits in BOTH `O_Y,O_Z` and **cancels** in
  `O_Y△O_Z`. So the compensation is **bottom-inclusive and global**, NOT a top-anchor reserve.

**Implication for the outline's Step 5 (anchor-domination descent):** the mechanism as written
(match T-runs against `Z`'s top anchors / hand a reserve down from the top) is now doubly refuted —
neither a local match nor a top-down reserve captures the surplus. The live mechanism is a **joint
count-parity amortization across ALL dyadic scales** (the balancing `|Y|`-vs-`|Z|` part-counts and
their scale-by-scale refinement), routed through the Structure Lemma. Recommend the outliner reframe
the residual around `(△⋆)` (bounded-mass localized inequality) + count-parity, or seed a genuinely
different framing per the plateau rule (this is the 3rd+ round on the same wall).

## Lemma proposed for certification

- **Threshold-split identity `(△)`** (§13): for `F=Y⊎Z` with `sum(Y)=2θ`, all `y≤2θ`, all `z≤θ`:
  `D(F) = (max Y − θ)⁺ + λ_{(0,θ)}(O_Y △ O_Z)`. Fully proved, verified `0/2·10⁵`. Reusable exact
  refinement of `(★★)`; pairs with the certified `termwise-lattice.md` and Structure Lemma.

## Files
- Updated: `results/imo-2026-03/approaches/induction-recursion-telescope.md` (new §13, §14; Current
  best round-7 sharpening; Promotable lemmas; Cases-to-cover status). Status stays `partial`.
