# Proof review — round 16

## Approach: `odd-block-counting` (LOWER wall, GAP MID-core)

**Verdict: RETHINK**
**True Status: unsolved** (this slug's mechanism; the problem stays `partial` overall)
**Builder's recorded Status in approach file: `partial` — WRONG for the slug's own mechanism.** The
builder honestly reports a G1 STOP / collapse, but files it as `partial`. The distinct mechanism this
slug owns (scale-local block/dyadic-band parity counting) is *decisively refuted this round*, so the
correct routing is RETHINK (back to the outliner for a genuinely new global object), not
CHANGES REQUESTED. This matches the standing role rule (rounds 11, 14): do not keep a slug live on
CHANGES REQUESTED merely because it emitted lemmas, when its own vehicle died and the remaining
content is a loss-free reframing.

### Scores
- Correctness: 9/10 — everything written is arithmetically/logically correct (verified below). One
  overclaim: FLR is presented as new promotable content when it is a restatement of certified CLIP.
- Completeness / rigor: 2/10 — the target (μ{g odd} ≥ 1 for |F|≥3) is NOT proved; the assigned
  mechanism is proved *unable* to prove it.
- Progress vs prior best: 1/10 — no new ground closed. FLR = CLIP(τ=0); the g≤1 sub-case and the
  {sup g≥2} localization are direct corollaries of already-certified R9/CLIP content. The one genuine
  deliverable is the *negative* result (a dead lever recorded), which has value but is not progress
  toward closure.

### What I verified from scratch (exact Fractions, n=3 witness F={12/5,14/5,14/5}, B={1,2,2,2})
- **FLR is a correct, loss-free identity.** For integer c, ⌊c/2⌋ = c/2 − ½·𝟙[c odd]; integrating an
  integer-valued g over (0,2^{n−1}) with ∫g=1 (MID(b)) and D=μ{g odd} (MID(a)) gives
  ∫⌊g/2⌋ = ½ − ½D, i.e. D = 1 − 2∫⌊g/2⌋. Machine check: D = 7/5, ∫g = 1, ∫⌊g/2⌋ = −1/5, and
  1 − 2(−1/5) = 7/5 = D. Identity holds. ✓
- **The per-band target ∫_{I_k}⌊g/2⌋ ≤ 0 is FALSE (G1 STOP is legitimate).** Band totals on the
  witness are exactly [I₀,I₁,I₂] = [−1, 0, +4/5]; the top dyadic band I₂=(2,4) carries +4/5 > 0,
  offset only by I₀=−1, so the sum ≤ 0 only through cross-band cancellation. ✓ The scale-local /
  prefix-from-bottom counting family therefore cannot yield μ{g odd} ≥ 1; it collapses to the global
  inequality ∫⌊g/2⌋ ≤ 0, which *is* MID-core. The lever is correctly recorded dead (9th).
- **The cap g(0⁺) = |F|−|B| ≤ 1 is rigorous.** Cut budget: (|F|−1)+(|B|−n) ≤ n gives |F|+|B| ≤ 2n+1;
  |B| ≥ n; so |F|−|B| = (|F|+|B|)−2|B| ≤ 1. Witness saturates it: |F|+|B| = 3+4 = 7 = 2·3+1, and
  |F|−|B| = −1 ≤ 1. ✓ Genuinely localizes the residual to {sup g ≥ 2}.
- **The sub-case g ≤ 1 a.e. ⟹ D ≥ 1 is correct** (integer c ≤ 1 ⟹ ⌊c/2⌋ ≤ 0 ⟹ ∫⌊g/2⌋ ≤ 0). ✓

### Certification decision on Lemma FLR: REJECTED (do not add to lemmas/)
FLR is **exactly** the τ=0 face of the already-certified Lemma CLIP, rescaled by −½. CLIP identity 2
at τ=0 reads ∫₀^L φ(g) = D(S) − 1 with φ(c) = 1[c odd] − c; and ⌊c/2⌋ = (c − 1[c odd])/2 = −φ(c)/2,
so −2∫⌊g/2⌋ = ∫φ(g) = D − 1, i.e. D = 1 − 2∫⌊g/2⌋. Both corollaries are already established:
- "g ≤ 1 a.e. ⟹ D ≥ 1" is the R9 fact φ ≥ 0 ⟺ c ≤ 1 restated;
- "g(0⁺) = |F|−|B| ≤ 1, residual = {sup g ≥ 2}" reuses the R9 observation that negative mass sits on
  {g ≥ 2} plus the standard cut budget.
The task gate ("certify only if genuinely useful — not a trivial restatement of certified MID/CLIP")
is not met: FLR is a trivial re-expression of CLIP(τ=0). No new lemma file is created. The *negative*
result (scale-local ∫_{I_k}⌊g/2⌋ ≤ 0 is false, cross-band cancellation irreducible) is recorded in
the approach file's "do not re-attempt" note, which is the right place for it.

### Why RETHINK, not CHANGES REQUESTED
The mechanism this slug was set up to run — a per-band / block-parity / prefix counting inequality —
is proved *impossible* to close MID-core (the required cancellation is irreducibly global/cross-scale,
demonstrated by an exact witness). What remains (FLR + two corollaries) is loss-free reframing of
certified content, not sub-progress inside the mechanism. Per the established pattern for this problem
(gen-func-transform R15, merge-interleave R14, ballot-matching R11), a slug whose own vehicle collapses
to "= MID-core itself" and whose residual is a reframing must return to the outliner for a genuinely
new GLOBAL cross-scale cancellation object — not another scale-local count. The problem's `current.md`
Status stays `partial` (unchanged): the certified MID/CLIP/BLK stack stands and the UPPER
breakpoint-vertex line is the live leader; only this lower lever is dead.

### Recorded
- `record_outcome`: outcome **dead-end**, note naming the killed lever (per-band ∫⌊g/2⌋≤0 false,
  FLR = CLIP(τ=0)).
- No lemma certified. `current.md` Status unchanged (`partial`) — correctly reflects the field.
