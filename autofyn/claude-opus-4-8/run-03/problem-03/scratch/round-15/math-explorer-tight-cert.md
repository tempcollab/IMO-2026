## imo-2026-03 (lens: exact zero-margin certificate for the UPPER wall only, valley regime)

- Distinct openings surfaced:
  1. **Integrality-degenerate witness on A^(n).** Computed the FULL tree-realizable reachable set
     (all differencing trees over all nonempty subsets, not just the descending caterpillar; a
     strict superset check of Lemma FGR's object) exactly for A^(n)={2^n,…,4,3,2}/(2^{n+1}+1) at
     n=2,3,4,5. Confirmed (matches certified VALLEY-TIGHT): min positive reachable value is exactly
     1 (unnormalized), 0 is NOT reachable. **New finding**: the minimizing witness is always the
     TRIVIAL 2-element pairwise difference |4−3|=1 between the two fixed values "4" and "3" that
     sit in the tail of every A^(n) (n=2: mask={index0,1}={4,3}; n=3: {4,3} at shifted indices;
     n=4,5 same pattern — the top piece 2^n and everything else in the tail is UNUSED by the
     witness). So Φ(A^(n)) is realized by a single MATCH move on two specific tail pieces, and it
     equals 1 simply because 1 is the smallest possible nonzero value on an ALL-INTEGER profile
     (integrality floor) — NOT because of any deep recursive/tree structure. Since the tail
     {…,4,3,2} is literally IDENTICAL (as raw integers) for every n, Φ_raw(A^(n))=1 for every n
     is essentially by construction; only the normalizing denominator (2^{n+1}+1) grows, which is
     what drives the ratio Φ/u_n→1. **This means the extremal family's tightness has a cheap,
     non-generalizable cause (integrality of a fixed small pairwise gap), not a structural dual
     object.** A "tight certificate" built by generalizing the (4,3)-pairwise-gap idea will NOT
     transfer to generic valley profiles (see cheap-kill below) — this is an important negative
     for the outliner: don't chase a "pairwise/adjacent-gap" certificate.
  2. **Peel-the-top-piece self-similarity is trivial, not structural.** A^(n) minus its top piece
     2^n equals EXACTLY the raw (unnormalized) integer profile {2^{n-1},…,4,3,2} = the raw A^(n−1)
     tail. So there IS a literal peel A^(n) = {2^n} ∪ A^(n−1)_raw. But since the witness for Φ never
     touches the top piece (opening 1 above), peeling contributes NOTHING to the certificate — the
     minimizer is entirely inside the untouched tail. This rules out (for THIS family) any
     induction of the form "peel top piece, recurse Xiang's tight response on the rest and combine
     via u_n=u_{n-1}/(2+u_{n-1})" — the recursion is vacuous on the extremal family because the top
     piece plays no role in achieving Φ here. If an inductive proof is attempted, it must derive its
     force from a DIFFERENT (non-extremal, or worst-case-over-all-valley) argument, not by mimicking
     what happens on A^(n) itself.
  3. **The TRUE worst-case valley maximizer is NOT A^(n) and is much more complex.** R14's own
     adversarial numerics (recorded in breakpoint-vertex.md, "GATE FINDING 3") found the actual
     tied maximizer at n=4, {16,8,4,3,2}/33-type points, has the minimizing value Φ=1/33 achieved
     SIMULTANEOUSLY by 14 distinct signed-subset patterns (both the whole-tail difference |2a1−1|
     AND several short interior differences), and at n=3 a different local maximizer has the min
     achieved by a near-tie of |a2−a3| and the whole-tail difference. So the actual extremal face is
     high-dimensional and n-varying — A^(n) is a valid ASYMPTOTIC witness for the ratio→1 claim but
     is evidently NOT itself the genuine LP maximizer structure; it just happens to also reach the
     ratio 1 in the limit via the cheap integrality argument above. **A dual/complementary-slackness
     certificate built by reverse-engineering A^(n)'s (trivial) minimizer will miss the real tied
     face** that the true worst-case profile exhibits (multiple simultaneous binding signed-subset
     constraints, incl. the whole-tail difference |2a1−L|). Any LP-duality certificate must be built
     to be tight on THAT multi-constraint face, not on the shallow A^(n) witness.
  4. **A cleaner "second" dual candidate: the whole-tail difference itself.** Since |2a1−L| is one
     of the binding constraints at the true n=4 maximizer, and the DOMINANT regime a1≥L/2 is ALREADY
     closed exactly by D=2a1−L (certified whole-tail-peel lemma), the valley (a1<L/2) is precisely
     the region where 2a1−L<0, i.e. the whole-tail signed difference is negative and hence not
     directly the leftover value but its absolute value |2a1−L|=L−2a1 is still a legitimate
     tree-realizable candidate (drop everything but the "whole tail vs a1" split). This IS one of
     the 14 tied patterns at the true n=4 maximizer. This suggests the correct dual object may be a
     PIECEWISE one: near the valley/dominant boundary (a1 close to L/2, which is exactly where the
     A^(n) family and the true maximizer both concentrate — a1/L→1/2⁻ as n→∞ in both), the
     whole-tail difference L−2a1 is itself of order u_n and could be the primary binding term, with
     interior-difference terms providing the "backup" needed away from the boundary. This is a
     genuinely different opening from (1)-(3): treat the valley bound as a CONTINUATION of the
     dominant-regime exact formula D=2a1−L across the boundary a1=L/2, i.e. try to show
     Φ(A) ≤ f(a1, a2, …) where f interpolates continuously and equals L−2a1 plus a correction from
     the next-largest pieces, rather than search for a single clean pairwise/subset certificate.

- Candidate technique(s): none of the standard families (all six dead upper families are still
  dead here). The only genuinely new angle surfaced is (4) — treating the valley bound as an
  analytic continuation / boundary-matching of the certified whole-tail-peel formula D=2a1−L across
  a1=L/2, using the fact that BOTH the constructed asymptotic witness (A^(n)) and the true
  numerically-found maximizer concentrate near a1→L/2⁻. This is speculative and UNVERIFIED beyond
  the observation that |2a1−L| is one of the 14 tied minimizing patterns at n=4 — it is not a proof
  sketch, just a place to look.

- Cheap-kill candidates:
  - **Pairwise/adjacent-gap certificate: REFUTED by direct computation (this round).** On the
    valley profile {30,25,20,15,10}/100 (n=4, valid valley: a1=0.30<0.5, a2=0.25<β4=8/31≈0.258),
    the minimum ADJACENT gap is 1/20=0.05 ≫ u4=1/31≈0.032 — the trivial pairwise-difference bound
    is already too weak on a perfectly ordinary (non-adversarial) valley profile with n=4. A deeper
    check of the FULL tree-realizable reachable set on the same profile (all subsets, all
    difference trees, exact integers {30,25,20,15,10}) shows 0 IS reachable there (full
    cancellation via a ≥4-element tree), so Φ=0≤u4 still holds — but NOT via any pairwise gap; it
    needs a genuine multi-element cancellation. This directly confirms opening (1)'s warning: do
    NOT let the outliner chase "smallest gap between two Liu pieces ≤ u_n" as a general lever — it
    is false in general and the A^(n) family's shallow witness is a special/degenerate case, not
    the template for a proof.
  - A parity/integrality argument (min positive value of an all-integer reachable set is ≥1) is
    the ENTIRE reason A^(n) is tight — this is a cheap fact worth stating explicitly to the outliner
    so nobody re-derives it as if it were deep: for any INTEGER-valued Liu profile the "floor" on
    the smallest achievable nonzero leftover is exactly 1, and Prop UV for such integer profiles is
    then just "does some subset achieve exactly 1 (or 0)", a much easier discrete question than the
    general real-valued Prop UV. The general problem is over reals, so this floor is not directly
    usable, but it is why the constructed witness looks "trivial."

- Knowledge-base entries to use: none new beyond what's already imported (Lemma FGR, R-COV',
  VALLEY-TIGHT, VS, whole-tail-peel — all already certified and in use by breakpoint-vertex.md).
  Did not find a new knowledge_base.md entry that changes this picture; the relevant discrepancy /
  three-distance-theorem style entries were already ruled out by the mass-telescope refutation
  (R13) and covering-radius refutations (R10/R12).

- Analogous past problems (cruxes): did not run a fresh corpus query this round (time budget went
  to the exact-computation probe per the dispatch's explicit ask); the R13/R14 explorer rounds
  already searched discrepancy/three-distance/equidistribution subtopics without finding a
  transferable crux (recorded in run_state.md). Recommend: if the outliner wants a corpus pass, the
  most promising untried subtopic given finding (4) above would be "boundary/continuity of
  extremal-game value functions" or "LP duality with a degenerate/high-multiplicity tied optimum" —
  not discrepancy per se.

- Prior progress: Certified reduction R-UV/FGR/R-COV' stands (Φ = μ_{n+1} = min_i dist(a_i,R_{i-1})
  over nonempty T, sufficiency direction only). Certified VALLEY-TIGHT: Φ/u_n→1 on A^(n), so no
  margin exists. Certified VS: no single DM move suffices in the valley (≥2 coordinated cuts always
  needed). This round's NEW (unproven, not yet certified) findings: (a) A^(n)'s witness is a
  trivial 2-element pairwise MATCH using only the fixed tail values {4,3}, top piece unused —
  explains WHY the ratio→1 but shows the mechanism does not generalize; (b) pairwise/adjacent-gap
  bound is directly refuted on an explicit ordinary n=4 valley profile ({30,25,20,15,10}/100, gap
  0.05 > u4≈0.032); (c) the TRUE worst-case valley maximizer (already found by R14's adversarial
  search, reused here) is a genuinely different, high-dimensional tied-face profile where the
  whole-tail difference |2a1−L| is one of ~14 simultaneously-binding tree values — this is the
  object a correct dual certificate needs to be tight against, not A^(n).

- Dead ends (do not retry): everything in run_state.md's standing NEVER-rules (covering-radius
  one/two-cap, dispersion/density/COUNT, greedy recursion, bounded-depth escape, mass-telescope,
  margin/extremal-tie) — unchanged, still dead. NEW this round: pairwise/adjacent-gap-of-Liu's-
  pieces as a general sufficient certificate is REFUTED by the explicit {30,25,20,15,10}/100 n=4
  counterexample (gap 0.05 > u4, yet Φ=0 only via a genuine 4-element cancellation tree) — do not
  propose "two close pieces" as the mechanism.

- Small-case / intuition notes (all labeled conjecture/empirical unless stated as computed exactly):
  - Computed EXACTLY (not conjecture): Φ(A^(n)) unnormalized = 1 for n=2,3,4,5, witness always the
    pair (4,3) in the fixed tail, top piece 2^n unused. Ratio Φ/u_n = (2^{n+1}−1)/(2^{n+1}+1).
  - Computed EXACTLY: on {30,25,20,15,10}/100 (n=4 valley profile), descending-caterpillar min
    positive value is 1/20 (=0.05), but the FULL tree-realizable set (unrestricted subset/tree)
    contains 0, i.e. Φ=0 there — achieved only via a ≥4-piece cancellation, not any pairwise or
    3-piece combination found by the sequential process starting from a 2-element pair. This is
    consistent with Prop UV (0≤u4) but is NOT explained by any shallow mechanism.
  - Conjecture (from R14's own adversarial search, re-confirmed by reading, not re-run here): the
    genuine worst-case valley profile has a1 approaching L/2⁻ as n grows (mirroring A^(n)'s
    a1=2^n/(2^{n+1}+1)→1/2⁻), and simultaneously ties several signed-subset values including the
    whole-tail difference — suggesting the boundary a1→L/2 is where the hard case concentrates for
    all n, i.e. the valley's difficulty is fundamentally a boundary-layer phenomenon adjacent to the
    already-solved dominant regime, not a "deep in the interior of the valley" phenomenon. If true,
    this would justify opening (4) (continuation/boundary-matching of the whole-tail-peel formula)
    as the most promising untried route — but this is NOT verified beyond the single n=4 tied-face
    observation already on record; it should be treated as a hypothesis for the outliner to test
    numerically before committing a builder to it.
