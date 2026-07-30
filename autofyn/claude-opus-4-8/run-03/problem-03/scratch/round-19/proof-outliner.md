## imo-2026-03

FIELD DIRECTIVE: UPPER-only this round. LOWER is HELD — both explorers confirm no gate-passing
lower vehicle (12th dead lower lever this round: SUFFIX-★ cross-scale Abel, fails 33–42% growing
with n; g-level-crossing pairing structurally refuted). No lower slug is put up.

STRATEGIC PIVOT (the key move): the CERTIFIED Reduction R-UV makes `min R(A) ≤ u_nL` an EXACT iff
for the upper bound, where `R(A)` = tree-realizable values (Lemma RL). The caterpillar object
`μ_{n+1}` that breakpoint-vertex has fought since R7 is a strictly HARDER sub-target
(`min R(A) ≤ μ_{n+1}` trivially, since caterpillars ⊆ trees). The R19 explorer's headline —
`μ_{n+1} = min R(A)` is FALSE (n=4: FGR μ=1 but tree-min=0) — is therefore NOT a wall but a signal:
STOP targeting the caterpillar and target `min R(A)` directly. This dissolves the false-completeness
problem entirely and is the far framing the field has needed. Both new approaches target `min R(A)`
by two genuinely different mechanisms; breakpoint-vertex advances by officially re-targeting.

---

tree-min-divide-conquer: new
Target: whole P3 upper bound — valley profile forces `D ≤ u_nL`, `u_n=1/(2^{n+1}−1)`; with certified
lower bound ⇒ `c(n)=2^n/(2^{n+1}−1)`. Deep interior `a₁ < L/2 − u_nL/2` (only open region).
Technique: divide-and-conquer / disjoint-block differencing over `R(A)`, telescoped by the exact
dyadic recursion `1/u_n = 2/u_{n-1}+1` and ONE-REC. Route (A) — non-anchored global existence.
Skeleton:
  1. Reduce to `min R(A) ≤ u_nL` — by certified R-UV; boundary layer closed by WTC.
  2. Disjoint-difference primitive: disjoint `P,Q`, `x∈T(P), y∈T(Q)` ⇒ `|x−y| ∈ R(A)` — Lemma RL.
  3. Balanced binary scale-split of the pieces into two mass-straddling groups — ONE-REC + induction.
  4. Window-overlap at each level contracts `w ↦ (w − u_kL)/2`, telescoping to `u_nL` — induction (GAP).
  5. Two disjoint blocks within `u_nL` ⇒ tree value ≤ u_nL ⇒ `D ≤ u_nL` — step 2 + R-UV.
Key lemmas (claim + mechanism):
  - Disjoint-difference legality — `|x−y|` of disjoint-support sub-tree values is a genuine tree
    value (each piece used once, the only RL constraint). THIS is the fix to dead MD2 (which
    differenced overlapping subsets — illegal). This is why the counting is not the dead density.
  - Balanced-split existence (GAP) — a disjoint mass-balanced split with overlapping reachable
    windows exists BECAUSE the deep gap `L/2−a₁ > u_nL/2` forbids any single piece exceeding the
    complementary group's whole span (no "unmatched giant" — exactly what the anchored walk missed).
  - Dyadic telescope — window contracts by `w↦(w−u_kL)/2`, whose fixed point is `1/u_n=2/u_{n-1}+1`,
    landing EXACTLY at u_nL (VALLEY-TIGHT no-margin met by exactness, not a bounded multiple).
Open gaps: step-4 window-overlap induction (balanced-split-existence + exact contraction) — the whole
difficulty; step-3 confirm ONE-REC yields n independent split levels for arbitrary deep profiles.
Cases to cover: deep interior only; base n=1; exact-zero even cancellation (helps, 0≤u_nL).
Watch out for: (a) VALLEY-TIGHT — a window bound `≤ C·u_nL` with C>1 is DEAD; telescope must land
EXACTLY. (b) Do NOT degenerate into the dead greedy recursion (pair a₁,a₂, recurse on tail with
target `u_{n-1}(L−a₁)`, R9-dead) — both groups must carry ~half the mass. (c) R-UV realizability:
confirm a GENERAL tree value (not just caterpillar) is n-cut-realizable — cite the exact R-UV/RL
clause (ESF-2 was caterpillar-only); if only caterpillars realize, revert to μ_{n+1} via the bridge.

---

signed-tree-invariant: new
Target: same whole P3 upper bound; deep interior `a₁ < L/2 − u_nL/2`.
Technique: EXACT two-sided interval-nesting invariant, generalising certified WTC from one
caterpillar to an adaptively-chosen fold with a DISJOINT RESTART after band-landing. Analytic
(interval nesting), not counting — deliberately far from the D&C route while probing the same
`min R(A)` target. Route (A) variant.
Skeleton:
  1. Reduce to a nonempty tree value ≤ u_nL — R-UV/R-COV'; boundary closed by WTC.
  2. Track reachable interval `[a₁−P_k, |a₁−P_k|]` for the fold value — extend WTC's invariant `(I_k)`.
  3. Band-landing (BL) lands crossing subset `T`, residual `r=Σ_T−a₁∈[0,a_{k*})`; RESTART the
     invariant on the DISJOINT sub-instance `{r} ∪ {pieces below scale k*}` (a₁ consumed, never
     re-folded), telescoping via `1/u_n=2/u_{n-1}+1` — BL + IH (GAP).
  4. Terminal residual ≤ u_nL is a tree value ⇒ `D ≤ u_nL`; matches lower bound ⇒ answer.
Key lemmas (claim + mechanism):
  - WTC two-sided invariant (certified, imported) — `a₁−P_k ≤ v_k ≤ |a₁−P_k|`; its d≥0 branch is
    EQUALITY, the source of tightness/no-margin.
  - Nested residual (GAP) — the restart does NOT re-inflate (contrast R18 dead anchored walk)
    BECAUSE a₁ is consumed into `r` and the restart is on a DISJOINT support; the R18 re-inflation
    came from re-folding the same anchor into later pieces.
  - Deep-gap absorption — overshoot `|2a₁−L|−u_nL` is bounded by below-scale mass, so one nested
    restart per scale; n scales telescope exactly to u_nL.
Open gaps: step-3 nested-residual telescope (restart is genuinely parameter n−1, composes to u_nL);
verify the restart support is DISJOINT from a₁/crossing block (the exact property the anchored walk
lacked).
Cases to cover: deep interior only; base n=1; exact-zero cancellation.
Watch out for: (a) MUST NOT collapse to the R18 dead anchored walk — distinguishing feature is the
DISJOINT RESTART (a₁ consumed), not "continue the walk past the crossing." If the restart re-touches
a₁ or re-inflates (minpost/u_n ~2^{n-1}), it IS the 9th dead mechanism — STOP. (b) VALLEY-TIGHT
exactness. (c) If BOTH this and D&C fail their gate, the `min R(A)` target itself is the shared wall
→ next round must reframe off the reachable-value object entirely.

---

breakpoint-vertex: advance
Target: same whole P3 upper bound; certified core (WTC boundary closure, R-UV, R-COV', FGR, RL,
ESF-2, VALLEY-TIGHT) is INTACT and unchanged. Advance task is NARROW and low-risk, NOT a re-run of
the dead C2 gate.
Technique: object-fix by re-targeting — formally reduce the open residual from the caterpillar
`μ_{n+1}` to the certified true target `min R(A)`, unifying the field.
Skeleton (advance):
  1. State and certify `min R(A) ≤ μ_{n+1}` (caterpillars ⊆ trees; the caterpillar fold is one
     tree topology) — one-line consequence of RL, makes `min R(A)` the OFFICIAL residual.
  2. Confirm via R-UV/RL that a general tree value is Xiang-realizable in ≤ n cuts (extend the
     ESF-2 caterpillar realizability statement to trees, or cite the exact R-UV clause) — this is
     the pivotal correctness check that licenses both new approaches; certify it as a lemma if sound.
  3. Record: the deep-interior residual is now `min R(A) ≤ u_nL`, strictly easier than the (dead)
     caterpillar-contraction residual; hand off to tree-min-divide-conquer / signed-tree-invariant.
Open gaps: none new — this is a consolidation/certification advance that de-risks the two new
approaches by pinning the official target and its realizability.
Cases to cover: none (structural).
Watch out for: do NOT re-attempt any anchored-walk/caterpillar-contraction closing lever (9th dead
mechanism) — the advance is ONLY the re-targeting + realizability certification. If step 2's
tree-realizability turns out FALSE (only caterpillars are n-cut-realizable), that is a CRITICAL
finding: the two new approaches must then route through a bounded-gap bridge `μ_{n+1} ≤ min R(A)+Δ`
instead, and this must be flagged loudly for next round.

---

NOMINATED FOR RANKING (outline-reviewer): tree-min-divide-conquer (new), signed-tree-invariant
(new), breakpoint-vertex (advance).

Notes for the reviewer/builders:
- All three are UPPER. LOWER is HELD by explorer consensus (12 dead levers) — do not add a lower slug.
- Gate discipline (binding): both NEW approaches carry a MANDATORY exact-Fraction pre-build gate
  (n=4,5,6, `fractions.Fraction`, NEVER float). Compute `μ_{n+1}` via the FGR dist-recursion
  `μ_i=min(μ_{i-1},dist(a_i,R_{i-1}))`, NOT "min positive of the accumulated set" (explorer finding
  4 — the naive filter silently drops exact-0 cancellations). Compute `min R(A)` via memoized
  `treeVals` over index-subsets. Run on the HARD families (`A^{(n)}` inward-sliver,
  `{1/3,13/40,13/40,1/120,1/120}`, `{30,25,20,15,10}/100`), NOT random integers (which over-produce
  ties). KILL CRITERION for each: if the mechanism's produced value / u_n GROWS with n
  (covering-radius signature), STOP and ship no prose — record the refutation.
- The two NEW approaches are the two probes of the single `min R(A)` target (counting vs analytic).
  This is deliberate diversity within one target; if BOTH gates fail, next round must reframe OFF the
  reachable-value object (the target itself becomes the shared wall).
- Do NOT reuse any of the 9 dead upper mechanisms (covering radius ×2, density/COUNT, greedy band
  recursion, bounded-depth escape, mass-telescope, margin/extremal-tie, 2nd moment ×2, anchored
  walk) — each new approach names the specific dead mechanism it must avoid collapsing into.

build set: tree-min-divide-conquer, signed-tree-invariant, breakpoint-vertex
