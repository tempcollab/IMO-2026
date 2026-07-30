## imo-2026-03 — UPPER wall, sliver lens (a₁ ∈ (L/2−u_n, L/2−u_n/2))

- **Distinct openings surfaced:**
  1. **Two-anchor {a₁,a_k} cancellation** (the dispatch's headline candidate) — tested exhaustively,
     exact `Fraction`, on the worst-case sliver family (A^{(n)} perturbed by shifting mass a₁→a₂ by
     δ ∈ {u_n/10, u_n/50, u_n/100}, landing exactly in the sliver band). **REFUTED, decisively and
     with growing looseness in n.** `min_k |a₁−a_k| / u_nL` = 3.33 / 3.51 (n=3), 7.32/7.50 (n=4),
     15.31/15.49 (n=5), 31.30/31.48 (n=6) — roughly doubling with each unit increase of n (≈2^{n-1}
     scaling). This is WORSE than doing nothing (WTC's own `|2a₁−L|` ratio is 0.90–1.18 in the same
     regime) — a single-tail-element anchor paired with a₁ is a strictly bad idea in the sliver, not
     a marginal shortfall.
  2. **Extending to {a₁,a₂,a₃} (3-element prefix caterpillar, one step past WTC's first move)** —
     also tested exactly: ratio 0.68–0.86 (n=3) but 3.56–3.74 (n=4), 7.55–7.73 (n=5), 15.55–15.73
     (n=6) — again growing roughly geometrically with n. A *fixed-length* prefix extension of WTC by
     one or two extra terms does NOT stay bounded; it only works by luck at n=3.
  3. **Arbitrary 2-element pair {a_i,a_j} anywhere in the profile (not tied to a₁ at all)** — this is
     the closest thing to a genuine "two-piece cancellation" and it is worth flagging as a DISTINCT
     idea from (1)/(2) since it decouples from a₁. On the *A^{(n)}-derived* sliver perturbations it
     accidentally works (ratio 0.94–0.98, achieved by the untouched tail pair (a_{n-1},a_n) = (3,2)/
     denom, whose difference 1/(2^{n+1}+1) is inherited unperturbed from A^{(n)} and is < u_nL by
     construction of that specific family). BUT a targeted adversarial search (200k random sliver
     profiles per n, uniform sampling not restricted to A^{(n)}-perturbations) finds sliver profiles
     where `min over ALL pairs |a_i−a_j| / u_nL` reaches 2.68 (n=4), 3.12 (n=5), 3.98 (n=6) —
     growing with n. So the "some pair is close" phenomenon is an ARTIFACT of the specific tight
     family, not a general sliver fact. **REFUTED as a universal exact mechanism.**
  4. On one such adversarial-pair witness (n=4, `a=(0.4708,0.2623,0.1759,0.0888,0.0021)`), the TRUE
     minimizer Φ is achieved by the 4-element (size-n) subset `{a₂,a₃,a₄,a₅}` — excluding a₁
     entirely, ratio Φ/u_n = 0.0092 (deeply below u_n, but only reachable via a subset of size n, not
     2 or 3). This matches R17's `{30,25,20,15,10}/100` finding (4-element cancellation needed) and
     shows the minimizing subset SIZE is not bounded uniformly — it can be as large as n even inside
     the sliver.

- **Candidate technique(s):** none of the small-fixed-arity (size ≤3) two/three-piece cancellation
  ideas survive exact testing in the sliver. The only mechanism that reaches Φ ≤ u_nL there is either
  (a) the full-tail WTC caterpillar (already certified, insufficient once |2a₁−L| > u_nL, which is
  exactly the sliver's defining feature) or (b) a subset whose SIZE grows with n / with the profile
  structure — i.e. genuinely unbounded-order cancellation, the same wall R15/R17 already isolated.
  I found NO exact bounded-arity substitute. This confirms — does not open — the standing R15/R17
  diagnosis.

- **Cheap-kill candidates:** the two done above (min-pair-diff adversarial search, min-{a₁,a_k}
  exact check) ARE the cheap kills for this lens; both kill the two-anchor idea outright before any
  proof attempt. No further cheap kill found that revives it.

- **Knowledge-base entries to use:** none new beyond what's already certified (Lemma WTC / whole-tail-
  continuation, Lemma FGR / first-gap-recursion, R-COV'). No knowledge_base.md generic entry (pigeonhole,
  extremal principle, etc.) suggested a bounded 2-anchor mechanism that these tests hadn't already
  covered; the problem's own structure (exponentially small target `u_n` against linearly many pieces)
  is the obstruction, matching the certified GAP-TELE refutation reasoning already on file.

- **Analogous past problems (cruxes):** did not query the corpus fresh this round (out of scope for
  this narrowly-dispatched numeric lens — the prior explorer rounds already searched combinatorial-
  game / subset-sum-discrepancy corpus entries without finding a bounded-arity analogue); no new
  candidate found. Recommend a future explorer specifically search the corpus for "signed subset sum
  discrepancy / Steinitz-type" results if a genuinely new idea is wanted, since the growing-with-n
  pattern found here (ratios doubling each step) smells like a Steinitz-lemma / vector-balancing
  obstruction rather than a finite casework one.

- **Prior progress:** unchanged from R17 — boundary layer `a₁ ≥ L/2 − u_n/2` closed exactly by
  certified Lemma WTC; deep interior open, now further confirmed (this round) that the sliver
  sub-band closest to the boundary has NO bounded-size (2- or 3-element) exact mechanism either.

- **Dead ends (do not retry):**
  - The dispatch's headline idea, `Φ ≤ |a₁ − a_k|` for a single well-chosen tail element `a_k`
    ("two-anchor a₁ + a_k"): REFUTED, ratio grows ~2^{n/2} with n (exact `Fraction`, 4 values of n).
  - Fixed-length prefix extension of WTC by 1–2 extra terms (`{a₁,a₂,a₃}`): REFUTED, same growth.
  - "Some arbitrary pair in the profile is always u_nL-close" (a generic 2-anchor-anywhere claim):
    REFUTED by adversarial search (ratio 2.68→3.98, n=4..6, growing); the cases where it *does* work
    are special to the A^{(n)}-tight-family tail structure, not general.
  - (Carried from breakpoint-vertex R17, do not re-attempt): full-tree 2nd moment, deep-interior
    margin/smoothing (G1/G2), gated-first ensemble average — all 8 previously dead upper mechanisms
    plus these 3 new negative findings make the count effectively higher for "bounded-arity" ideas
    specifically.

- **Small-case / intuition notes (conjecture, not proof):** the exact data across n=4,5,6 for both
  refuted candidates shows worst-case ratio scaling that looks geometric in n (roughly doubling per
  unit n for the {a₁,a_k} test: 3.3→7.3→15.3→31.3, i.e. ≈2^{n-1}·u_nL-ish growth relative to a fixed
  small-arity target). This strongly suggests the sliver genuinely needs an argument whose "reach"
  (number of pieces/terms combined) scales with n, not a constant-size trick — consistent with, and
  now sharper evidence for, the standing diagnosis that the deep/sliver residual is an unbounded
  multi-piece cancellation (Steinitz/subset-sum-discrepancy flavor), not a two-piece one. I recommend
  the outliner NOT pursue any O(1)-arity two-anchor mechanism for the sliver going forward; if a
  bounded mechanism is wanted, it must be bounded relative to n (e.g. O(log(1/u_n)) = O(n) pieces),
  matching the R17 4-element example and the size-n minimizer found here.
