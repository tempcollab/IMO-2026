# Approach: ladder-abel-pairing (prove (★) by Abel/summation-by-parts telescoping of the merged alternating sum, organized by ladder rungs)

## Status
new (round 12) — independent second attack on the base-slice inequality (★), FAR from the
weak-majorization route (value-domination). This route is *positional/parity* (rearrange the signed
alternating sum), targeting `(★)` EXACTLY (not the stronger weak majorization), so it survives even
if weak majorization over-shoots at large `n`. Replaces the retired `allocation-vertex-corner`
(b-pruning engine DEAD R11; its Positive-Layer Localization Lemma is banked and imported below).

## The whole claim this approach proves
GAP L (lower bound), closing the problem: `D̃(F) ≥ 1` for every dyadic-refinement final multiset `F`
under budget `Σa_j ≤ n`. With the certified upper bound this gives `c(n)=2^n/(2^{n+1}−1)`.

## Route (shared reduction, then the DISTINCT closer)
Imports the certified peel machinery to reduce the whole problem to the extremal base slice, then
proves the base-slice inequality `(★)` by a **summation-by-parts / value-dominance pairing** —
genuinely different from the sibling `peel-scale-rank-induction`'s weak-majorization closer.

- Import (certified): `lemmas/peel-difference-bound.md` (peel SD identity, difference bound, Case A
  closed), `lemmas/floor-half-reduction.md` (`D̃(F)=1−2∫⌊M/2⌋`, Case B `⟺ I_n≤0`),
  `lemmas/ladder-interleaving-identity.md` (`(★-id)`: `D̃(π_0⊎L)=1+2(Σ_{blue odd}−Σ_{red even})`,
  base slice `b=0` `⟺ (★) Σ_{blue odd} ≥ Σ_{red even}`), `lemmas/positive-layer-localization.md`
  (`Σ_k λ{M≥2k} ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}` — positive `I_n`-layers bounded by `π_0`'s even parts).

## Technique (the spine)
Abel summation (summation-by-parts) on the descending merged alternating sum, PAIRED by ladder rung
so each odd-rank rung telescopes against the even-red mass in its dominated tail; the leading-red
parity forces the residual `≥ 0`. Crux analogue: **aimo-0388** (coins split into two stacks
minimizing `|val(A)−val(B)|`: pair consecutive sorted elements into non-positive gaps, isolated
boundary terms, parity `2k−49` odd ⇒ `|diff|≥1`) — structurally a baby-P3, exact shape of
`D̃=1+2(Σ_{blue odd}−Σ_{red even})`. Also aimo-0298 (dyadic "two gaps ≥ next scale" dominance).

## Skeleton
1. **Reduce to `(★)`.** By the certified peel + `(FLOOR)`, `D̃(F)≥1 ⟺ I_n≤0`; on the base slice
   `b=0`, `F'=L={2^{n-1},…,1}` and by `(★-id)` this is `(★) Σ_{blue odd} ≥ Σ_{red even}` in the merge
   of `π_0` (red, `Σ=2^n`) and `L` (blue). — imported.
2. **Write `D̃` as a sum of consecutive-pair gaps.** With the descending merge `w_1≥w_2≥…≥w_N`,
   `D̃ = Σ_{j odd}(w_j − w_{j+1})`, each gap `≥ 0` (descending). — Lemma G / elementary.
3. **Rung-telescoped re-pairing (the DISTINCT move).** Re-organize the alternating sum so each
   **odd-rank blue rung `b_i`** is charged against the **even-rank reds lying in its dominated tail**
   `(0,b_i)`. By `(DOM) b_i = 1 + Σ_{i'>i} b_{i'}` a single odd-rank rung dominates the ENTIRE lower
   tail (all smaller rungs at once) — this is the cross-block (cross-`k`) tail cancellation the naive
   per-block charge `Σ⌈m_i/2⌉b_i` (§10.6, 51% fail) could not achieve, now supplied by the telescope.
4. **Boundary term + parity.** The only unpaired element is the optional leading red (`(m₀≤1)`: at
   most one red `>θ=b_1`, at odd rank `1`, contributing `0` to `RE`). The integer parity of
   `ΣL=2^n−1` (odd) forces the residual of the telescoped alternating sum to be `≥ 0`, i.e.
   `Σ_{blue odd} ≥ Σ_{red even}`, hence `D̃≥1` (aimo-0388 parity mechanism, adapted).
5. **General `b` lift.** `(★-id)` generalizes to any feasible `F'` (colour-sum `(C)=Σπ_0−ΣF'=1`
   always; verified). For `F'≠L` the rung-dominance `(DOM)` is replaced by `F'`'s recursive dyadic
   split; import the loaded-IH inheritance from `peel-scale-rank-induction` §11.5, OR the coupled
   descent from `coupled-cut-descent`. (Base slice is the standalone deliverable here.)

## Key lemmas (claim + mechanism)
- **(DOM)** `b_i = 2^{n−i} = 1 + Σ_{i'>i} b_{i'}` — geometric sum; each rung exceeds the sum of all
  lower rungs, so one odd-rung gap in the telescope absorbs its whole even-red tail (cross-block).
- **(m₀≤1)** at most one red `> θ` — two reds `>θ` would sum `>2θ=2^n=Σπ_0`; the lone top red sits at
  odd rank `1`, contributing `0` to `Σ_{red even}`, so it only helps.
- **Parity closer** — because `ΣL=2^n−1` is odd and `Σπ_0=2^n` even, the colour-sum is exactly `1`;
  the telescoped non-positive pair gaps plus this fixed integer offset force the residual `≥0`
  (aimo-0388: clustered leading extreme + odd count ⇒ `|diff|≥1`). This is a GLOBAL parity argument,
  NOT a bounded running-margin reserve.

## Open gaps
- **The rung-telescoped pairing inequality (step 3)** — that the odd-rank rungs' pair-gaps cover the
  even-red mass in their tails, made rigorous with the `(DOM)` cross-block cancellation and the
  parity boundary term. This is the core and only real difficulty of the base slice.
- **General-`b` lift (step 5)** — imported from the sibling routes, not re-derived here.

## Cases to cover
Base slice `b=0` (the deliverable). `n=1`: `D̃(π_0⊎{1})≡1` (imported, both sides of `(★)` are `0`).
General `b` via import. Case A (`a_0=0`) already closed (certified §4).

## Watch out for
- **Do NOT reduce this to a one-directional positional running-margin scan.** Top-down and bottom-up
  positional reserves are REFUTED (min margin grows to `−2^{n-1}`; R7/R9 + explorer R12). The pairing
  MUST be a value-reordering telescoped by rung + a GLOBAL parity closer, not a monotone prefix scan.
- **Do NOT use the per-block same-block charge** `Σ_{red even}≤Σ⌈m_i/2⌉b_i` (51% fail) — the whole
  point is that the telescope charges an even-red to a HIGHER odd-rung, not its own block.
- Ties (`D̃=1`) = the `n+1` "`L`+one unit bumped" configs; there red/blue alternate perfectly after
  the lead red, both sides of `(★)` are `0` — the pairing must give equality there, a correctness check.

## Imported (certified)
`lemmas/peel-difference-bound.md`, `lemmas/floor-half-reduction.md`,
`lemmas/ladder-interleaving-identity.md`, `lemmas/positive-layer-localization.md`, Lemma G, cut-flip,
upper-bound. Do not re-derive.
