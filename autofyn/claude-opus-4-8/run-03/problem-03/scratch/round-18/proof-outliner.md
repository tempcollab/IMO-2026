## imo-2026-03

SITUATION. Both R18 explorer directions died (UPPER two-anchor sliver REFUTED with growing-arity
signature; LOWER Abel-identity DOA + merge-to-|F|=2 = 11th dead lower lever). I ran fresh exact-Fraction
gates and reached a decisive re-localization of the UPPER wall plus an honest HOLD on LOWER. Field: one
ADVANCE (breakpoint-vertex, the leader, with a materially sharpened residual), one NEW gated UPPER slug
(reflected-walk-contraction — the dispatch's vector-balancing/prefix-discrepancy reframing, now on a
correct minimum-complete foundation), and LOWER HELD with a single gate-only probe offered.

NEW round-18 findings (exact Fraction; /tmp/gate_upper.py, /tmp/gate_upper2.py, /tmp/gate_cover.py):
1. **Caterpillar-min completeness (candidate lemma):** `Φ(A) = min_{∅≠T} descKK(T)` equals the min over
   ALL differencing trees and subsets — 0 counterexamples on random sliver, tight family A^{(n)}, and
   A^{(n)} perturbed into the sliver (full-tree enumeration, n≤5). ⇒ the caterpillar (reflected-walk)
   family is minimum-complete; the GAP-ACH factor-2 achievability deficit does NOT touch the minimum.
   This is the load-bearing simplification the dispatch's Steinitz framing needed (a pure signed-balancing
   bound over ALL signings is not required — the min already lives on tree-realizable caterpillars).
2. **Depth-margin structure of the sliver:** on the A^{(n)} family `Φ/u_n` = 0.88/0.94/0.97 at the
   boundary but DROPS to 0.38/0.44/0.47 one `u_n/4` deeper (n=3,4,5). The sup over the sliver is attained
   at the sliver/boundary interface as a continuous limit of the WTC-closed boundary and DECREASES with
   depth. ⇒ the correct object is a SHARPENED-WTC continuation (tight at the interface, slack growing
   with depth), not a margin argument and not a fresh tight problem.
3. **GUARDRAIL — single-target subset-sum density REFUTED as a closing lever:** `min_{S⊆tail}|a₁−Σ_S| ≤ u_n`
   is FALSE — fails 15–33% of sliver profiles (worst ratio 1.76/1.86/1.91/1.99 at n=3..6, growing with n).
   The R17 "single-target density Φ≤min_S|a₁−Σ_S|" was only ever an UPPER bound on Φ; it is not itself
   ≤ u_n, so it cannot close the sliver. The true Φ requires genuine differencing (≥2 tail pieces
   cancelling) — confirming the growing-arity (Steinitz-flavor) diagnosis with a fresh refutation.

---

breakpoint-vertex: advance
Target: Xiang forces `D ≤ u_nL` for every valley profile `a₁≥…≥a_{n+1}>0`, Σ=L, `a₁<L/2` (the whole
  UPPER bound; combined with the certified lower/base machinery this is the full problem's upper half).
Technique: LP-vertex finiteness → certified reduction to `Φ = min_{∅≠T} descKK(T) ≤ u_nL`; WTC closes
  the boundary layer; deep interior/sliver via the sharpened-WTC continuation.
Skeleton:
  1. Boundary layer `a₁≥(L−u_nL)/2` — CLOSED by certified WTC (`descKK(full) ≤ |2a₁−L| ≤ u_nL`). [done]
  2. Deep interior `a₁<(L−u_nL)/2` — target `Φ ≤ u_nL`. Adopt the corrected residual object:
     Φ = min_{∅≠T} descKK(T) (caterpillar-min complete, finding 1), NOT the loose `min_S|a₁−Σ_S|`
     (finding 3, refuted). [gap U-deep]
  3. Attack via the SHARPENED-WTC continuation: at the band-landing crossing index (certified BL) the
     residual is `P_{k*}−b₁`, and the post-crossing reflected steps contract under the tail's dyadic
     caps (ONE-REC). [gap U-deep, shared with reflected-walk-contraction]
Key lemmas (claim + mechanism):
  - Caterpillar-min completeness — because MATCH yields only differences (RL) and descending processing
    greedily minimizes the reflected residual; certify via an exchange (out-of-order steps do not lower
    the output). GATE-supported (0 counterexamples).
  - Sharpened-WTC continuation — because WTC's own two-sided invariant `b₁−P_k ≤ v_k ≤ |b₁−P_k|` gives,
    past the crossing, `v ≤ P−b₁`, and this overshoot telescopes down through the O(n) active dyadic
    scales rather than stopping at `|2a₁−L|`.
Open gaps: U-deep (the sliver/deep interior; caterpillar-min residual under the contraction). The two
  refuted sharpenings (per-subset WTC R16; single-target subset-sum density R18) are now BOTH on record
  so the builder does not retry them.
Cases to cover: spread regime (tail dyadically spread → walk contracts) vs collision regime (a big tail
  jump → even cancellation gives residual 0); must be handled uniformly (R11 dichotomy).
Watch out for: sliver has NO uniform margin near its top edge (sup Φ/u_n→1) — the continuation must be
  EXACT there (VALLEY-TIGHT). Do NOT regress to covering radius / density count / per-subset WTC /
  single-target subset-sum (all dead). MANDATORY exact-Fraction gate of the contraction constant before
  prose; if it does not telescope to ≤u_nL, report and STOP.

reflected-walk-contraction: new
Target: same whole UPPER bound (`D ≤ u_nL` in the valley) — a rival complete attempt, far from the
  LP-vertex/covering lineage.
Technique: view the caterpillar residue as a **reflected 1-D walk** `v_k=|v_{k−1}−b_k|` (the dispatch's
  1-D vector-balancing / prefix-discrepancy object), restricted to the minimum-complete caterpillar
  family, and prove `Φ ≤ u_nL` by a walk-contraction / telescoping argument under the dyadic caps.
Skeleton:
  1. R-COV'/ESF-2 reduction to `Φ ≤ u_nL`; caterpillar-min completeness (gate then certify). [gap C1]
  2. Two-sided invariant (I_k, WTC) + band-landing crossing (BL): residual `= P_{k*}−b₁` at crossing.
  3. **Contraction lemma (make-or-break):** post-crossing reflected steps, with decrements bounded by
     ONE-REC per-scale dyadic caps, halve the residual per active scale → telescopes to `≤ u_nL`. [gap C2]
  4. Cover all `a₁<L/2` with the WTC boundary closure. [gap C3]
Key lemmas (claim + mechanism):
  - Caterpillar-min completeness (shared, GATE-supported) — descending-order greedy minimizes the
    reflected residual; achievability (RL) is not lossy for the minimum.
  - Post-crossing contraction — once `P_k>b₁` the value is `P_k−b₁`; each further decrement either
    reflects (residual ≤ that decrement) or shrinks; superincreasing ONE-REC caps force per-scale
    halving, and the number of active scales (O(n)) is exactly the growing arity the sliver demands.
Open gaps: C1 (completeness — gate/certify), C2 (contraction constant — the whole difficulty; MANDATORY
  exact-Fraction gate on adversarial sliver profiles FIRST — refute-and-stop if it does not telescope),
  C3 (cover).
Cases to cover: spread vs collision (same dichotomy as breakpoint-vertex).
Watch out for: this shares the Φ OBJECT with breakpoint-vertex but attacks it with a genuinely different
  MECHANISM (reflected-walk contraction vs LP-vertex/first-gap pigeonhole) — the plateau-breaking
  diversity CLAUDE.md asks for on a field collapsed to one upper framing. If the reviewer judges it too
  close to breakpoint-vertex, fold C2 into breakpoint-vertex instead. Same VALLEY-TIGHT no-margin ban at
  the interface; same refuted-object dead list.

cross-scale-injection: new (GATE-ONLY PROBE — build = run the gate, or DEFER)
Target: whole LOWER bound (`D ≥ u_nL`, i.e. MID-core `μ{g odd}≥1`).
Technique: the SOLE remaining lower lead — aimo-0127 level-indexed cap × aimo-0009 self-referential
  scale index, made EXPLICITLY cross-scale (scale-SUFFIX cumulative transport), the one axis R17's
  same-scale refutation does not kill.
Skeleton (gate only): test SUFFIX-★ `Σ_{j≥J} Σ_i α_{i,j} ≤ Σ_{j≥J} Σ_i β_{i,j}` (and the finer-first
  mirror) in exact Fraction, n=4,5,6, adversarial `a=0` refinements, using R17's loss-free tagging.
Open gaps: everything downstream — DO NOT touch unless the gate passes.
Kill criteria: SUFFIX-★ fails on any exact witness → 12th dead lower lever, STOP; OR it holds but
  rearranges back to (★) with no scale-monotonicity input → repackaging, dead.
Watch out for: HOLD is the honest default. The R18 explorer PROVED (★) is a pure algebraic rewriting of
  `D≥1` (zero content beyond ∫g=1 + odd/even), and all 11 lower levers are dead. Recommend the reviewer
  either (a) include this as a cheap gate-only probe, or (b) HOLD LOWER entirely this round and defer the
  cross-scale synthesis to a future explorer scouting aimo-0127/aimo-0009 properly. Do NOT dispatch a
  builder to write LOWER prose.

---

RECOMMENDED BUILD SET: breakpoint-vertex (advance, primary), reflected-walk-contraction (new, gated —
mandatory contraction-constant gate FIRST). LOWER: HOLD (cross-scale-injection optional as a gate-only
probe; no LOWER prose this round). An UPPER-only build set is the honest call — LOWER has no
gate-passing vehicle after 11 dead levers and the explorer's algebraic-triviality proof of (★).
