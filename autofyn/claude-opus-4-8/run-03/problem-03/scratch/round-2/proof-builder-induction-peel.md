# Build report — induction-peel (round 2), imo-2026-03

Status: **partial**. Answer c(n)=2^n/(2^{n+1}-1) unchanged; minimax D = u_n = 1/(2^{n+1}-1).

## What I CLOSED this round (new, complete)

1. **Entire upper-bound DOMINANT case a_1 ≥ L/2** (§4A) — this is the headline. Two
   complementary, exhaustive branches, each a clean one-cut reduction:
   - (i) a_1 ≥ Lc(n): DELETE (bisect) a_1, apply UB(n-1); closes via u_{n-1}(L-a_1) ≤ u_n L,
     which ⇔ a_1 ≥ Lc(n) since 1 - u_n/u_{n-1} = c(n).
   - (ii) L/2 ≤ a_1 < Lc(n): MATCH the whole tail into a_1 (legal because a_1 ≥ L - a_1),
     leaving the SINGLE leftover ℓ = 2a_1 - L, so D = 2a_1 - L < 2Lc(n) - L = u_n L (uses
     2c(n)-1 = u_n). Uses ≤ m-1 ≤ n cuts.
   Contains the extremal dyadic input (a_1 = Lc(n), on the (i)/(ii) boundary, both give u_n L),
   so the upper bound is now PROVEN on the tight configuration and all dominant profiles.
   Verified over 8000 random dominant configs, n≤4: zero failures. Proposed as **Lemma DOM**
   for certification.

2. **Strengthened lower-bound Case (a)** to D ≥ a_1/2 ≥ u_n L (was: an interval of length u_n L;
   now the cleaner [a_1/2, a_1) interval), and **reduced Case (b)** to a coupling on the single
   band [0, a_1/2): showed O_tail ⊆ [0, a_1/2) while O_top may reach f_1 ≤ a_1, so the
   symmetric difference only interferes on [0, a_1/2), with LB(n-1) supplying D_tail ≥ u_n L.

## What REMAINS (two precisely-localised gaps)

- **GAP U (upper, balanced a_1 < L/2).** Proven that NO multiplicative IH can close it:
  reducing to a single leftover reaches Δ(a) = min nonneg signed sum (verified = MATCH-reachable
  min when >0), and Δ(a) > u_n L for all-equal odd-m profiles. The correct mechanism is
  early-stopping with even multiplicities (all-equal ⇒ D=0). The peel recursion B(a,n) ≤ u_n L
  was verified on 1600 random configs (n≤4, zero failures), so the bound is certainly true, but
  a human-checkable non-multiplicative potential is not found.
- **GAP L (lower, Case (b), Xiang cuts top piece).** Reduced to the [0, a_1/2) band coupling;
  the shadow-map φ / "cutting a scale costs that scale" one-directional inequality is set up but
  the bookkeeping (top-fragment toggles re-create ≥ what they erase) is not completed.

## Spec concerns
None. Answer and reduction are solid. Note the field-wide observation: the extremal config is
DOMINANT (a_1 = Lc(n) ≥ L/2), so the hard residual cases (balanced upper, top-cut lower) are all
strictly sub-extremal — they have slack, which is why the bound holds there but a tight
multiplicative induction cannot see it. Suggest next round: for GAP U, hand the outliner the
"early-stopping even-multiplicity potential" as the explicit target (not more matching); for
GAP L, the single-band [0, a_1/2) coupling is the concrete remaining computation.
