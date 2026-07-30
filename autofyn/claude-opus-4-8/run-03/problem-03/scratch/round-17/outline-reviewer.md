# Outline review — imo-2026-03 (R17)

Field: 3 slugs — scale-origin-layercake (LOWER, new, priority), breakpoint-vertex (UPPER, advance),
block-rearrangement (LOWER, new, reserve). One vehicle per wall built; the second lower slug held.

Note: neither new-slug body file exists yet (`approaches/scale-origin-layercake.md`,
`approaches/block-rearrangement.md` MISSING — the outliner did not seed them). The full skeletons live
in `/tmp/round-17/proof-outliner.md`; the built builder creates its own file from that skeleton.
Ranking metadata for both is now registered.

---

## scale-origin-layercake (LOWER, new) — APPROVE, build STRICTLY gate-bound (PRIORITY)

Verdict: APPROVE as the LOWER wall's first live vehicle since R11, but the build is a GATED PROBE —
no prose before the make-or-break passes. This is the correct move on an empty wall (my R15 rule:
seed a genuinely-new-OBJECT probe as a bounded gate; it returns either a vehicle or a cleanly-recorded
dead family, both worth one builder).

Why it is NOT a re-entry of a dead lever (checked against all 9):
- Slices by g-VALUE (super/sub-level sets {g≥2i}, {g≤1−2i}), NOT by domain position. R16's 9th-dead
  lever sliced by DOMAIN dyadic band I_k; the explorer's n=3 witness proves the two axes are provably
  distinct (termwise-true on the value axis where the band target ∫_{I_k}⌊g/2⌋≤0 is false). Not the
  9th lever.
- The cap is per-(i,j) STRUCTURAL (from ONE-REC's 2^j per-scale mass), not a running/foresight scalar
  (dead R9/R10), not a transport/matching (dead R11), not LP-dual/vertex (dead R12/R14), not a
  transform (dead R15), not merge-domination (dead R15). It is the FIRST lower lever to use BLK and
  ONE-REC jointly — every dead lever used at most one. Genuinely new.
- Step 1 correctly imports D=1−2∫⌊g/2⌋ as an IDENTITY and explicitly refuses to re-certify it as
  "Lemma FLR" (respects the R16 rule: FLR = CLIP τ=0 rescaled, certification rejected). Good.

Substrate confirmed (explorer's exact-Fraction gates, consistent with certified MID): (★) is true and
tight (0/900, worst margin ≈0.0093); the TERMWISE-per-i reduction is FALSE (5/6000, always i=1) — so
the target genuinely needs cross-level cancellation (i≥2 repays an i=1 deficit). This is exactly what
makes the direction non-trivial rather than a disguised triviality.

THE LOAD-BEARING GAP (step 3, the per-cell cap C(i,j)) is UNFORMULATED. The outliner did not write a
concrete inequality — the entire content is finding one. This is the "reframing not reduction" trap
that killed 9 levers, so I could not run the gate myself (there is nothing concrete to test yet).
Therefore the build is bound HARD to the outliner's make-or-break:
  1. The builder must FIRST commit a concrete, genuinely LOCAL per-(i,j) inequality C(i,j) proved from
     ONE-REC's 2^j mass — NOT a global restatement of (★) split into cells.
  2. Gate it exact-`Fraction`, 0 exceptions, ≥1000 adversarial a=0 refinements per n=4,5,6, INCLUDING
     the i=1-termwise-FAILING witnesses (e.g. the explorer's n=4 F={7.586,0.932,7.482},
     B={1,2,4,4.241,0.844,2.915} scaled). The gate must confirm the cap absorbs the i=1 deficit via
     the i≥2 scale-credit — i.e. holds cell-by-cell where the naive per-level claim fails. This is the
     genuine discriminator: if the only cap that sums to (★) is (★) trivially split, it inherits the
     i=1 termwise failure and the gate KILLS it.
  3. KILL CONDITION (mandatory): if no local C(i,j) survives the i=1-failing witnesses, this collapses
     to plain layer-cake = MID-core restated → record as the 10th dead lower lever and STOP. Do NOT
     ship a dressed tautology.
Do NOT gate (★) itself (certified true) — gate the CAP. Cover |F|≥3 only (|F|=2, 0≤g≤1 closed by MID).

## breakpoint-vertex (UPPER, advance) — APPROVE, build gate-bound (leader, only live upper vehicle)

Verdict: APPROVE the advance. Live leader (Elo 1826), boundary layer CLOSED exactly (Lemma WTC, R15);
sole open region is the deep interior a₁<(L−u_nL)/2, which carries genuine non-shrinking margin
(Φ/u_n worst 0.34–0.56) so a NON-tight bound is admissible there (VALLEY-TIGHT's no-margin ban applies
only to the closed boundary layer — respected). The primary extremal/worst-profile recipe is NOT
margin-based, NOT covering-radius, NOT a WTC-extension, NOT constructive-subset-selection, NOT
averaging — distinct from all 7 dead upper mechanisms.

Two real concerns, both already handled by the outliner's gates — build is bound to them:
- H1 (which vertex maximizes μ_{n+1} on the deep-interior polytope) is UNKNOWN. The upper explorer's
  own diagnosis is that the true small witness is a "rare needle" and the inner argmin |T| is scattered
  (2,3,5,4). That is the inner-min over SUBSETS for a fixed profile — a different object from the outer
  argmax over PROFILES that G1 probes — so it does not by itself refute H1, but it IS a warning that the
  extremizer may be structureless. GATE G1 (exact-`Fraction` argmax of μ_{n+1} at n=4,5,6) is the
  cheap decisive test: if the argmax is a generic spread with no near-dyadic pattern, H1 has no target
  → PIVOT (do not force a near-dyadic fit — my R16 note: the true minimizer is genuinely spread).
- SMOOTH-MONO (H2): my R3 rule warns minimax value is NOT monotone along balanced→dyadic paths
  (interior valleys). The move here is toward the deep-interior extremizer (not toward dyadic) and on
  μ_{n+1} (not V), but the non-monotonicity risk is real — GATE G2 (0 exceptions on ≥500 deep-interior
  profiles per n) is mandatory before prose; re-choose the move or pivot if it decreases μ_{n+1}.
- The CONDITIONAL PROBE (full-tree second moment over 𝓡(A)) is correctly demoted to gated-FIRST and is
  expected to die by the same rare-needle structure that killed both fixed-order second-moment gates
  (ratios 5×–100×, growing with n). Build its prose ONLY if mean(V²)/(u_nL)²<1 robustly with no
  n-growth; otherwise record dead, do not ship. Fine as structured — no effort wasted.

Do NOT re-close the boundary layer or re-use any WTC-extension / single-anchor / constructive-selection
bound (all dead R16). Note the all-equal COUNT counterexample lives in the deep interior, so a naive
dispersion/count fallback is not automatically safe despite the margin.

## block-rearrangement (LOWER, new) — REGISTERED, HELD from build (reserve / breadth)

Verdict: register for population diversity (far-apart lower option — Chebyshev/majorization on the block
multiset vs scale-origin's co-area pairing), but HOLD from the build set this round. Rationale:
- No concrete inequality exists (steps 2–3 entirely open); it is a pure research seed.
- The load-bearing length↔|g| anti-correlation hypothesis is UNTESTED and explicitly flagged
  possibly-false by the explorer (a single long high-|g| block kills the ordering). The explorer
  refused to put it in its shortlist.
- Focus one lower builder on the priority (scale-origin-layercake); keep block-rearrangement as the
  far-apart backup if scale-origin's cap gate fails next round (my R7/R8 rule: diversity in the
  population, focus in the build set — do not build 4). If promoted later, its own make-or-break
  (formulate + exact-`Fraction`-gate the specific inequality before any prose) is mandatory.

---

## Diversity / plateau note for the orchestrator

The two BUILT vehicles are on different walls and genuinely far apart (value-side co-area cap vs
deep-interior extremal/smoothing), so the field is not collapsing to one framing this round. But BOTH
are gated probes whose load-bearing step is unformulated (lower cap C(i,j) not written; upper H1
extremizer unknown) — realistic outcome is one or two more cleanly-recorded dead families, not
necessarily a closed gap. The LOWER wall in particular has now burned 9 levers; if scale-origin's cap
gate fails, next round should treat the wall as needing a genuinely different GLOBAL reformulation
(block-rearrangement is the registered far-apart candidate) rather than another value/scale bookkeeping
variant.

Ranking (post-update): breakpoint-vertex 1826 (leader, live, built) > parity-measure-potential 1625
(stale, family dead) > scale-origin-layercake 1569 (new, live, built) > merge-interleave 1531 (dead) >
odd-block-counting 1514 (dead) > block-rearrangement 1498 (reserve, held) > gen-func-transform 1483
(dead) > ballot-matching 1404 (dead).

build set: scale-origin-layercake, breakpoint-vertex
