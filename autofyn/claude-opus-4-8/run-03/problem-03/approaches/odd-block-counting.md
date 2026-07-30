## Status
partial

## Approaches tried
- odd-block-counting (LOWER wall, GAP MID-core: μ{g odd} ≥ 1 for |F|≥3) — R16, NEW mechanism
  (pure counting/pigeonhole on the block/dyadic-band structure). OUTCOME: the assigned per-band /
  block-parity counting lever **COLLAPSES to MID-core restated** (the reviewer's G1 STOP condition
  is triggered, honestly). Rigorously established this round, and NOT a restatement:
  (i) the clean loss-free reformulation **D = 1 − 2∫⌊g/2⌋**, so MID-core ⟺ ∫₀^{2^{n-1}}⌊g/2⌋ ≤ 0;
  (ii) a **proven robust sub-case**: if g(t) ≤ 1 for a.e. t then D ≥ 1 (strictly generalizes MID's
  0≤g≤1 sub-case; covers all g that never exceed 1, including negative g);
  (iii) a **proven robust cap**: g(0⁺) = |F|−|B| ≤ 1 always (cut-budget), so g can exceed 1 only
  in the interior/top and only when sup g ≥ 2 — the residual regime is exactly {sup g ≥ 2}.
  DECISIVE NEGATIVE (kills the lever): the per-band and prefix-from-bottom versions of the target,
  ∫_{I_k}⌊g/2⌋ ≤ 0, both FAIL with exact witnesses (n=3: F={12/5,14/5,14/5}, B={1,2,2,2} has top-band
  ∫⌊g/2⌋ = +4/5, offset only by band I₀ = −1; the total is −1/5 ≤ 0 only via cross-band
  cancellation). So no scale-local counting/pigeonhole inequality yields μ{g odd}≥1; the required
  cancellation is irreducibly global, i.e. = the global inequality ∫⌊g/2⌋≤0 = MID-core itself. G1
  also fails on the other horn: the numerical minimizers are NOT dyadic-aligned (min D→1 attained by
  non-dyadic F over the unrefined ladder B), so the minimizer cannot be reduced to an integer vertex
  without a forbidden vertex enumeration (G2). Reported as collapse per mandate; no fake proof.

(Prior approaches / history for the problem live in `results/imo-2026-03/current.md`.)

## Current best
**Answer (whole problem):** c(n) = 2ⁿ/(2ⁿ⁺¹−1), minimax D = u_n = 1/(2ⁿ⁺¹−1) (established and
reviewer-verified; recorded in `current.md`). This slug owns the LOWER wall, i.e. GAP MID-core:
prove μ{g odd} ≥ 1 (in u-units) for every admissible a=0 refinement with |F|≥3, where
g = N_F − N_B on (0, 2^{n−1}), ∫g = 1 (certified Lemma MID).

Furthest rigorous progress this round (all profile-independent unless a witness is cited):

**1. Reformulation (loss-free; the crisp scalar target).**
For any integer c, ⌊c/2⌋ = c/2 − ½·𝟙[c odd]. Since g is integer-valued, integrating over
(0,2^{n−1}) and using ∫g = 1 (Lemma MID(b)) and D = μ{g odd} (Lemma MID(a)),
  ∫₀^{2^{n−1}} ⌊g/2⌋ dt = ½∫g − ½μ{g odd} = ½ − ½D,  i.e.  **D = 1 − 2∫₀^{2^{n−1}}⌊g/2⌋ dt.**
Hence MID-core (D ≥ 1) ⟺ ∫₀^{2^{n−1}}⌊g/2⌋ dt ≤ 0. Equivalently, with layer-cake on ⌊g/2⌋,
  ∫⌊g/2⌋ = Σ_{i≥1}( μ{g ≥ 2i} − μ{g ≤ 1−2i} ),
so MID-core ⟺ Σ_{i≥1}μ{g≥2i} ≤ Σ_{i≥1}μ{g≤1−2i}: the total "excess-even/positive" over-level mass
is dominated by the "negative" over-level mass. (This is loss-free, hence not itself a closure — it
is the crisp form on which the rest is stated. The pure-integral version is false, e.g. g≡2 on
measure ½: ∫⌊g/2⌋ = ½ > 0.)

**2. Proven robust sub-case (genuinely closes a slice, generalizing MID's 0≤g≤1).**
If g(t) ≤ 1 for a.e. t ∈ (0,2^{n−1}), then ⌊g(t)/2⌋ ≤ 0 pointwise (integer c ≤ 1 ⟹ ⌊c/2⌋ ≤ 0),
so ∫⌊g/2⌋ ≤ 0 and D ≥ 1. This subsumes and extends the certified 0≤g≤1 slice inside MID (which
gave D=1 exactly, ⌊g/2⌋≡0) by additionally covering every profile whose g dips negative but never
exceeds 1.

**3. Proven robust cap at 0 (localizes the residual).**
Cut budget: (|F|−1) + (|B|−n) ≤ n (F uses |F|−1 cuts; B refines the n-piece ladder C_{n−1} using
|B|−n cuts), so |F|+|B| ≤ 2n+1; and |B| ≥ n. Hence g(0⁺) = |F|−|B| = (|F|+|B|) − 2|B| ≤ (2n+1) − 2n
= 1. So g starts ≤ 1; combined with (2), **the entire residual is the regime sup g ≥ 2** (some
dyadic level carries ≥2 more F-fragments than B-fragments), which must be paid back by negative g.

**Open gap (the residual crux = MID-core for {sup g ≥ 2}).** Bound the positive over-level mass
Σ_{i≥1}μ{g≥2i} by the negative over-level mass Σ_{i≥1}μ{g≤1−2i}. This round PROVES that this
cancellation is **irreducibly cross-band**: the per-band and prefix-from-bottom localizations
∫_{I_k}⌊g/2⌋≤0 both FAIL (exact witness n=3: F={12/5,14/5,14/5}, B={1,2,2,2} gives band totals
[−1, 0, +4/5]; the top dyadic band I₂=(2,4) has ∫⌊g/2⌋ = +4/5 > 0, offset only by band I₀ = −1).
Therefore no scale-local counting/pigeonhole inequality (the assigned "band-parity count") can
close MID-core — it collapses to the global inequality, which is MID-core itself. A genuinely new
GLOBAL cross-scale cancellation object is still required; the block/dyadic-band count is now
definitively pruned (the 9th dead lower lever — a scale-local count).

## Full proof
Not present — Status is partial. The residual GAP MID-core (regime sup g ≥ 2) is open; the assigned
counting mechanism is shown to collapse to it and is pruned.

## Promotable lemmas
- **Lemma FLR (floor reformulation of MID-core).** With g = N_F − N_B on (0,2^{n−1}), ∫g = 1
  (Lemma MID), and D = μ{g odd} (Lemma MID): D = 1 − 2∫₀^{2^{n−1}}⌊g/2⌋ dt. Hence D ≥ 1 ⟺
  ∫⌊g/2⌋ ≤ 0. *Proof:* ⌊c/2⌋ = c/2 − ½𝟙[c odd] for integer c; integrate. *Corollaries (proven,
  robust):* (a) g ≤ 1 a.e. ⟹ D ≥ 1; (b) g(0⁺) = |F|−|B| ≤ 1 by the cut budget (|B|≥n, |F|+|B|≤2n+1),
  so the residual is exactly {sup g ≥ 2}. *Proved in full this round; loss-free reformulation plus
  two robust corollaries. Worth certifying as a crisp target for future lower-wall attempts.*
- **Negative result (record, do not re-attempt):** the scale-local target ∫_{I_k}⌊g/2⌋ ≤ 0 is FALSE
  per band (exact witness n=3: F={12/5,14/5,14/5}, B={1,2,2,2}, band totals [−1,0,+4/5]); likewise
  prefix-from-bottom ∫₀^s⌊g/2⌋ ≤ 0 is FALSE (exact witnesses n=3..6). Any per-band / block-parity /
  per-scale counting inequality therefore collapses to the global MID-core.
