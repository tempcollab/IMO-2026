# Build report — odd-block-counting (LOWER wall), round 16

## Verdict: PARTIAL — the assigned per-band/block-parity counting lever COLLAPSES to MID-core restated (G1 STOP triggered honestly), but with genuine, rigorous partial content extracted and the lever definitively pruned.

## Gate results (exact Fractions, n=3,4,5,6)
- **Reformulation confirmed exactly:** D = 1 − 2∫⌊g/2⌋ holds identically on all sampled configs
  (integer + random non-integer, n=3..5). MID-core ⟺ ∫₀^{2^{n-1}}⌊g/2⌋ ≤ 0.
- **[G1] non-integer / dyadic-alignment — FAILS both horns.**
  - Non-integer minimizers: random search min D ≈ 1.0005 / 1.14 / 1.43 (n=3/4/5), all > 1, attained
    by **non-dyadic** F over the unrefined ladder B. So the minimizer is NOT dyadic-aligned; the
    clean integer-vertex structure the reviewer found does not extend, and reducing to an integer
    vertex would require a forbidden enumeration ([G2]).
  - Band-count robustness: the per-band target ∫_{I_k}⌊g/2⌋ ≤ 0 is FALSE. Exact witness (n=3):
    **F={12/5,14/5,14/5}, B={1,2,2,2}** → band totals [I₀,I₁,I₂] = [−1, 0, +4/5]; top band
    I₂=(2,4) has ∫⌊g/2⌋ = +4/5 > 0. Total = −1/5 ≤ 0 only via cross-band cancellation. D = 7/5.
  - Prefix-from-bottom ∫₀^s⌊g/2⌋ ≤ 0 also FALSE (exact witnesses n=3..6; e.g. n=6 the running
    prefix reaches +10.99 in the middle bands and is only repaid by the wide g=−1 top band).
  ⇒ The required cancellation is irreducibly CROSS-BAND. Any scale-local counting/pigeonhole
  inequality (the assigned "band-parity count") collapses to the global ∫⌊g/2⌋≤0 = MID-core itself.
- **[G3] used integer-valuedness of g (counts), never block-value integrality.** The floor
  reformulation and the g≤1 sub-case use only that g is integer-valued; correct.

## Genuine rigorous progress this round (not a restatement)
1. **Lemma FLR (loss-free reformulation):** D = 1 − 2∫₀^{2^{n-1}}⌊g/2⌋. Crisp scalar target
   ∫⌊g/2⌋ ≤ 0; level-set form Σ_{i≥1}μ{g≥2i} ≤ Σ_{i≥1}μ{g≤1−2i}.
2. **Proven robust sub-case:** g ≤ 1 a.e. ⟹ D ≥ 1 (⌊g/2⌋≤0 pointwise). Strictly generalizes MID's
   certified 0≤g≤1 slice — now covers all g that never exceed 1, including negative g.
3. **Proven robust cap:** g(0⁺)=|F|−|B| ≤ 1 (budget: |B|≥n, |F|+|B|≤2n+1). ⇒ residual is exactly
   {sup g ≥ 2}.
4. **Decisive pruning:** the per-band / prefix / block-parity counting family is dead (exact
   witnesses). It is the 9th dead lower lever (a scale-local count). Recorded so no future round
   re-tries a per-scale counting inequality.

## Spec concerns
None with the certified stack (MID/BLK/VERT-LOW/ONE-REC/ATT all used correctly). The outline's
premise that a "band-parity count" pinned by fixed dyadic group sums 2^j could force μ{g odd}≥1 is
REFUTED: the group sums do not localize the odd mass (the top band can carry net-positive ⌊g/2⌋,
repaid elsewhere). This matches the reviewer's flagged G1 STOP condition — reported, not papered over.

## Recommendation to orchestrator
The LOWER wall again has NO live closing vehicle: the block/dyadic-band counting lever joins the 8
prior dead levers. The residual is crisply isolated (regime sup g ≥ 2; target
Σμ{g≥2i} ≤ Σμ{g≤1−2i}, irreducibly global/cross-scale). Next round should escalate to a genuinely
new GLOBAL cross-scale cancellation object (not scale-local, not a running scalar, not matching/LP/
transform), or a self-similar reduction in n that carries the cross-band cancellation intact.
Lemma FLR (with its two robust corollaries) is proposed for certification as the cleanest current
target statement.

## Files
- Approach file (updated): /home/agentuser/repo/results/imo-2026-03/approaches/odd-block-counting.md
- Probes: /tmp/probe.py, /tmp/probe2.py, /tmp/probe3.py, /tmp/probe4.py (exact-Fraction checks)
