# Build report — induction-recursion (imo-2026-03 / IMO 2026 P3), Round 4

Slug: **induction-recursion**. Owns **GAP L** (lower bound, Case B). Target this round: close the
doubly-balanced residual GAP-LB′ via an **exchange / degenerate-boundary argument** (drive the
smallest top-fragment to 0, induct `a→a−1` down to Case A). No scalar-summary fill (that route is
proven false — probes 5–7).

Status remains **partial**. I did NOT close GAP-LB′. I proved that the exchange mechanism **as
specified cannot** close it, and I turned the residual into a clean, sharper form with two new fully
proved lemmas. Honest outcome, no overclaim.

## What I proved this round (all rigorous, all in §5C of the approach file)

Setup (integer units): `F=Y⊎Z`, `θ=2^{n−1}`, `ΣY=2^n=2θ` (top, `a+1` parts, `a≥1`), `ΣZ=2θ−1`
(`Z` a `≤b`-cut response of the `(n−1)`-dyadic, so `Z` has exactly `n+b` parts), budget `a+b≤n`.

1. **(R1) Difference-function reformulation.** With `h(t):=N_Y(t)−N_Z(t)`,
   `D̃ = λ{t:h(t) odd}` and `∫₀^∞ h = ΣY−ΣZ = 1` **identically**. So GAP-LB′ ⟺ `λ{h odd} ≥ ∫h = 1`.
   This is the exact, structure-free restatement (cleaner than the `2λ(O_Y^<∩O_Z)` term).
2. **(R2) Sufficient Lemma (proved, equality-robust).** If `|h(t)|≤1` a.e. then
   `D̃ = ∫h + 2λ{h=−1} ≥ ∫h = 1`, equality iff `λ{h=−1}=0`. A reusable **per-config certificate**
   closing every config where `Y` tracks `Z` within one level. Verified 0/41814.
3. **(R3) Compactness + ±1 gradient (proved).** `min_Y D̃(Y⊎Z)` attained (piecewise-linear on a
   compact simplex); `∂D̃/∂y_j = 2·1[M_{−j}(y_j) even]−1 = ±1`. At a minimizer, the smallest
   fragment admits a **value-preserving** mass-exchange (directional derivative 0) with a matched
   partner — driving it to `0` (a real `a→a−1` reduction) or into an invisible pair with a `Z`-value.
   This is the rigorous core of the exchange move.
4. **(R4) The obstruction (proved) — this is the decisive finding.** At `t→0⁺`,
   `h(0⁺)=(a+1)−(n+b) ≤ 1−2b` (using `a≤n−b`). Hence for **`b≥2`, `h(0⁺)≤−3`**: a negative excursion
   `|h|≥3` near `0` is **forced** because `Y` (only `a+1≤n−b+1` fragments) cannot match `Z`'s `n+b`
   small parts. So `|h|≤1` is unattainable for `b≥2`; the `(R2)` certificate fails there and **no
   `Y`-exchange can finish**. This is a clean, proved reason the exchange route bottoms out — and it
   pins the residual exactly onto `Z`'s near-`0` cut-structure (matching the explorer's scalar-fill
   refutation from a new, count-theoretic angle).

## Why the assigned mechanism does not fully close (honest)

The outline hoped: compactness minimizer ⟹ push smallest top-fragment to 0 ⟹ `a→a−1` ⟹ Case A.
Two independent obstructions, both now understood:
- **Interior minimizers exist.** e.g. `n=2`, `Z={1,2}`, `Y=[1.772,2.228]`: `D̃=1` is the true min,
  but pushing the smaller fragment to `0` gives `Y={4}` with `D̃=altsum(4,2,1)=3` — the reduction
  *increases* `D̃`. So "drive to 0" is not `D̃`-non-increasing in general; the minimizer need not sit
  on the `a−1` stratum. (The value-preserving exchange (R3) instead stops at a `Z`-tie / invisible
  pair, not at `0`.)
- **Fragment-count wall (R4).** For `b≥2` the minimizer *provably* has `|h|≥3` near `0`; the target
  `|h|≤1`/Case-A form is unreachable by any `Y`-only move. `min_Y` numerics (build5): at the true
  minimizer `max(N_Y−N_Z)=2` and `min(N_Y−N_Z)=−3` for `b≥1` — both an `h=2` positive plateau and a
  deep negative excursion survive, yet `D̃=1` (via the small measure of the excursions).

Net: the exchange cleanly closes exactly the `|h|≤1`-attainable regime and reduces the rest to the
**same near-`0` `Z`-structure bound** as the telescope twin. Not a full closure.

## Precise remaining gap (GAP-LB′, round-4 form)

Prove `λ{h odd} ≥ 1` (equiv. `D̃ ≥ 1`) for `b≥2`, where the negative excursions of `h=N_Y−N_Z` near
`0` are supported on the small fragments produced by cutting the `(n−1)`-dyadic. Equivalently: bound
`2λ{h<0, h odd}` (the deficit `D̃−∫h` when `|h|>1`) using that the sub-`θ` part of `Z` is itself a
`≤b`-cut response of the `(n−1)`-dyadic. A scalar/count summary of `Z` provably fails; `Z`'s recursive
cut-tree is required — i.e. a two-level joint induction (the telescope twin's target), OR a measure
bound on `Z`'s small cut-fragments. Numerics: true `min D̃ = 1` exactly in this region.

## Promotable lemmas (for reviewer certification)

- **Difference-function bound (R1)+(R2)** — for `F=Y⊎Z`, `h=N_Y−N_Z`: `D̃=λ{h odd}`,
  `∫h=ΣY−ΣZ`, and `|h|≤1 ⟹ D̃ = ∫h + 2λ{h=−1} ≥ ∫h` (equality iff `λ{h=−1}=0`). Fully proved §5C.
  Candidate `lemmas/difference-function-bound.md`.
- **Fragment-count obstruction (R4)** — `N_Y(0⁺)−N_Z(0⁺)=|Y|−|Z|`, so `|Z|≥|Y|+2` forces `|h|≥2`
  near `0`; in dyadic Case B this gives `|h|≥3` for `b≥2`, proving the `|h|≤1`/exchange route cannot
  close GAP-LB′ there. Fully proved §5C. Documents why `Z`'s structure is indispensable.
- (carried, still good candidates) Half-total single-crosser (◇◇); threshold block-decomposition +
  (★★).

## Spec concerns

- The outline's key lemma "at the `D̃`-minimum the smallest top-fragment can be driven to 0
  non-increasing" is **false as stated** (interior-minimizer counterexample above; and for `b≥2` the
  fragment-count wall (R4) blocks reaching Case A). The salvageable rigorous core is the
  *value-preserving* exchange (R3), which stops at a `Z`-tie, not at 0 — it does not reduce `a` in
  general. So the "induct `a→a−1` down to Case A" skeleton does not run; the field should treat the
  near-`0` `Z`-structure bound as the true, shared obstruction (same wall as the telescope twin).
- Equality-robustness respected throughout: (R2) is an identity `D̃=∫h+2λ{h=−1}` with the tight
  family characterized (`λ{h=−1}=0`, the maximal-alternation zigzag). No strict domination used.
