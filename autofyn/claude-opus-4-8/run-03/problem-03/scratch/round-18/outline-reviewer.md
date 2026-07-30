# Outline review — imo-2026-03 (round 18)

Field: one ADVANCE (breakpoint-vertex, leader), two NEW slugs (reflected-walk-contraction UPPER,
cross-scale-injection LOWER gate-probe). I verified the two make-or-break gates independently and ruled
against the outliner on the build set: this is a single-builder UPPER-only round.

## Gate verification I ran

- **Caterpillar-min completeness (C1) — NUMERIC ONLY, confirmed but NOT proven.** Ran
  `/tmp/gate_upper.py`: `bestSubset-descKK == full-tree-min` exactly on every sliver sample (n=3,4,5:
  0.681=0.681, 0.557=0.557, 0.501=0.501). So `Φ = min_{∅≠T} descKK(T)` matches the true full-tree min
  numerically. This is a **candidate lemma, not a theorem** — the outliner honestly labels it C1
  ("gate then certify via RL + exchange"). It is load-bearing for BOTH new upper slugs. Flag: the
  builder must PROVE the descending-order exchange argument (out-of-order steps do not lower the
  output), not assume it from the gate. Note the balanced/KKgreedy pairings do NOT match full-tree min
  (n=4: balanced 0.961 vs full 0.557) — only the *descending caterpillar* min matches, so the proof
  must pin the minimum to the descending caterpillar specifically.
- **Post-crossing contraction constant (C2) — NOT GATED.** The outliner did NOT run this; both slugs
  leave it as the open make-or-break with a MANDATORY refute-and-stop gate. Per the dispatch, an
  ungated contraction gate means reflected-walk is HELD, not built as closed.
- **Object-overlap check (grep on breakpoint-vertex.md).** breakpoint-vertex's residual object is
  *literally* `Φ(A) = min_{∅≠T} descKK(T)` (lines 128, 242, 383, 1604, 1628), i.e. the reflected walk
  `v_k=|v_{k-1}-b_k|`. reflected-walk-contraction uses the SAME object and the SAME crux (post-crossing
  contraction under ONE-REC dyadic caps). The outliner itself labels breakpoint-vertex step 3's gap
  "shared with reflected-walk-contraction." **This is the single-gap trap** (CLAUDE.md): the two slugs
  die together on one wall.
- **Covering-radius collision risk.** breakpoint-vertex already REFUTED a covering-radius contraction
  (GAP TWO-CAP, R12; lines 440, 1349, 1494). The C2 "post-crossing contraction" is at real risk of
  collapsing back into that dead family — exactly the dispatch's warning ("if it can't contract to u_n
  it dies like covering-radius"). This is why C2 must be gated FIRST, hard, before any prose.

## breakpoint-vertex — CHANGES REQUESTED (advance; BUILD, leader)

Technique sound; certified reduction to `Φ = min_{∅≠T} descKK(T) ≤ u_nL` (R-COV'/FGR/ESF-2/WTC) stands;
boundary layer `a₁≥(L−u_nL)/2` closed exactly by WTC. Residual = deep interior / sliver via the
sharpened-WTC continuation (= post-crossing contraction). Build with two BINDING preconditions:
1. **C2 contraction-constant gate FIRST (mandatory, exact Fraction, adversarial sliver n=3..6):** show
   the post-crossing reflected residual telescopes to ≤ u_nL under ONE-REC per-scale caps. If the
   per-scale contraction constant is not ≤ the scale ratio — i.e. it does not reach u_n — **report the
   refutation and STOP** (it is then the covering-radius family in disguise, dead). No margin-dressed
   prose.
2. **C1 (caterpillar-min completeness) must be PROVEN, not cited from the gate** — the descending-order
   exchange (RL signings + largest-first greedily minimizes the reflected residual). It is currently
   numeric-only.
Do NOT regress to any dead upper mechanism: covering radius, density/COUNT, per-subset WTC,
single-target subset-sum density (`min_S|a₁−Σ_S|` REFUTED R18, fails 15–33%), full-tree 2nd moment,
margin/smoothing. VALLEY-TIGHT: the continuation must be exact at the sliver/boundary interface (sup
Φ/u_n→1), no uniform margin.

## reflected-walk-contraction — CHANGES REQUESTED as a population member; HELD from build

Registered (cold-start 1500) as a legitimate reframing kept in reserve. NOT built this round. Reason:
it shares BOTH the object (`Φ = min descKK`) AND the make-or-break gap (post-crossing contraction under
ONE-REC) with breakpoint-vertex — building both is the single-gap trap; they would die together on one
gate. The C2 gate is run ONCE, inside breakpoint-vertex step 3. The outliner explicitly offered this
fold ("if too close to breakpoint-vertex, fold C2 into breakpoint-vertex instead") — I take it.
It is NOT the genuine-diversity Steinitz route: the completeness gate deliberately drops the
all-signings/vector-balancing bound in favour of the caterpillar-min, which collapses back to descKK.
So it does not break the plateau — it is the same framing. Keep it live for a future round if the C2
gate passes and its distinct prefix-discrepancy prose is worth developing separately.

## cross-scale-injection — HELD (LOWER wall held, no builder)

Registered as a reserve axis; NOT built. This is a gate-only probe (SUFFIX-★, an Abel sum over the
scale index) that REUSES the R17-dead same-scale scale-of-origin tagging. Its only novel content is the
cumulative-in-scale variant, which the outliner's own kill criteria flag as likely rearranging back to
(★). The R18 lower explorer PROVED (★) is a pure algebraic rewriting of `D≥1` with zero content beyond
`∫g=1` + odd/even, and that cross-scale payment is non-monotone (deficit paid at BOTH finer and coarser
scales) — which is exactly the scale-monotone transport SUFFIX-★ would need. High probability it is a
disguised repackaging (kill criterion b/c). Per the dispatch, do not emit a doomed lower builder just to
have one. HOLD LOWER this round. The genuinely-untried lower lead is R17 direction (iii) — value-level ×
dyadic scale-of-origin self-referential cap (aimo-0009-style) — which needs a proper explorer, not this
thin SUFFIX gate.

## Field diagnosis for the orchestrator (plateau)

The UPPER field has collapsed to ONE object (`Φ = min descKK`) and ONE gap (post-crossing contraction
under ONE-REC). breakpoint-vertex and reflected-walk-contraction are the same framing. If the C2
contraction gate fails or stalls, next round needs a genuinely DIFFERENT upper object — the
**Steinitz / signed-subset-sum-discrepancy EXISTENCE** route both explorers flagged (the growing-arity
signature, ratios doubling ~2^{n-1} in n), NOT another caterpillar-descKK-contraction variant. The
LOWER wall has NO live vehicle after 11 dead levers; its only substantive lead is the aimo-0009
scale-of-origin self-referential synthesis (direction iii), which merits a dedicated explorer.

build set: breakpoint-vertex
