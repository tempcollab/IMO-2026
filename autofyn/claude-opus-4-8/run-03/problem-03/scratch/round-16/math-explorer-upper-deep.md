## imo-2026-03 — UPPER wall, DEEP INTERIOR lens

- **Distinct openings surfaced** (all target the residual `Φ(A) = min_{∅≠T} descKK(T) ≤ u_nL` in
  the deep interior `a₁ < (L−u_nL)/2`, via certified R-COV'+FGR):
  1. **Multi-anchor / suffix-WTC** (dispatch Q2): apply certified Lemma WTC not just to the full
     profile (leader `a₁`) but to each suffix `{a_k,…,a_{n+1}}` (leader `a_k`), giving
     `Φ(A) ≤ min_k |2a_k − S_k|` (`S_k = a_k+…+a_{n+1}`). **TESTED NUMERICALLY, REFUTED** (see below).
  2. **WTC-per-arbitrary-subset ("Ψ")**: since WTC bounds `descKK(T) ≤ |2·max(T) − sum(T)|` for
     *every* nonempty `T` (not just suffixes), `Φ(A) ≤ Ψ(A) := min_{∅≠T} |2·max(T) − sum(T)|`.
     Algebraically `Ψ(A) = min_k min_{S⊆{a_{k+1},…,a_{n+1}}} |a_k − sum(S)|` — i.e. "some element
     equals a subset-sum of the elements below it, up to `u_n`" — a clean classical-looking
     subset-sum-near-target statement, structurally different from covering-radius/COUNT/mass-
     telescope. **TESTED NUMERICALLY, REFUTED** (see below) — this generalizes and subsumes (1).
  3. **Decimated/alternating-subsequence lever (new, speculative, NOT tested to conclusion):** at
     the counterexample that kills (1)/(2) (a smooth, near-geometric 7-piece deep profile), the
     TRUE minimizing subset is the **every-other-index** alternating subsequence
     `{a_1,a_3,a_5,a_7}` (indices 0,2,4,6), achieving `Φ/u_n ≈ 0.127` — far under budget — while
     `Ψ` (which only sees "leader + arbitrary subset of the strict tail") misses this because the
     alternating pattern's caterpillar telescopes almost to 0 precisely *because* consecutive
     included gaps are near-equal (smooth/near-geometric decay), which a generic-subset bound
     cannot see. This suggests the right lever is not "any subset via WTC" but a **targeted
     decimated subsequence chosen to match the local decay ratio** — structurally reminiscent of a
     three-distance/continued-fraction (Weyl equidistribution) mechanism: picking every `k`-th term
     of a near-geometric sequence to make a signed alternating sum land near 0. NOT developed into a
     proof; flagged as the single most promising untried opening.
  4. Corpus scouting for "subset-sum lands within ε of a target, all parts bounded by a fraction of
     the whole" turned up nothing directly transferable (see corpus section) — the closest hits are
     mod-p prefix-sum pigeonhole (aimo-0685, wrong setting: finite field, not real intervals).

- **Candidate technique(s):** targeted/decimated caterpillar subsequence selection exploiting local
  ratio structure (near-geometric decay) — untested; a three-gap/continued-fraction-style argument on
  consecutive ratios `a_{i+1}/a_i` is the closest classical analogue, not yet connected rigorously.

- **Cheap-kill candidates:**
  - `Ψ(A) ≤ u_nL` as a **uniform sufficient lever**: CHEAP-KILLED, REFUTED (exact witness below).
  - Multi-anchor/suffix-only WTC (`min_k |2a_k−S_k| ≤ u_nL`): CHEAP-KILLED, REFUTED, worse than Ψ
    (worst ratio 1.93/3.23/5.28 at n=3/4/5 in the deep interior — grows fast with n, clearly dead,
    not even a margin-tolerant candidate).
  - The TRUE target Φ itself: re-confirmed with a *stronger* adversarial search (Dirichlet random
    restarts with varying concentration, not naive uniform-simplex sampling — per the standing rule
    that naive random search under-samples adversarial minima) that the deep-interior margin is real
    and does NOT shrink with n: worst `Φ/u_n` found = 0.78 (n=3), 0.69 (n=4), 0.50 (n=5), 0.46 (n=6),
    0.34 (n=7) — i.e. the margin, if anything, *improves* with n. This corroborates and strengthens
    R15's `0.37–0.56` finding at n=4,5 and extends it to n=3,6,7. Good news for the outliner: the
    deep-interior claim is robustly true with a healthy, non-vanishing margin — the obstruction is
    purely finding a PROVABLE mechanism, not tightness.

- **Knowledge-base / lemma entries used:** certified Lemma WTC (`whole-tail-continuation.md`,
  reused/extended here to arbitrary subsets — extension itself dies, but WTC's core two-sided
  invariant is still the only rigorous per-subset bound available), Lemma FGR
  (`first-gap-recursion.md`), Reduction R-COV' (`covering-value-reduction.md`, sufficiency
  direction), Lemma CONF/MD2 (`confinement-reachable-set.md`, `multiset-doubling.md`) for context on
  why naive dispersion dies. `knowledge_base.md` pigeonhole/subset-sum entries did not surface
  anything beyond what's already been tried (no new named theorem found there for "subset sum near
  a target using only a fraction of the pieces").

- **Analogous past problems (cruxes):** searched `combinatorics` × `pigeonhole`,
  `size-bounding-and-descent`, `extremal-principle` for "subset sum near target" / "partial sum
  close to value" patterns. Best partial hit: **aimo-0685** (prefix-sum pigeonhole over `F_p` forcing
  a contiguous block-sum to vanish) — structurally NOT analogous (finite-field, exact-zero target,
  no "bounded by a fraction of the whole" structure); flagging it only to record it was checked and
  rejected, not recommended. **No genuinely analogous crux found** for the real-valued
  "subset-of-the-tail approximates a designated piece" statement that `Ψ(A)`'s algebraic form reduces
  to — this specific near-subset-sum flavor does not appear to be in the corpus under these subtopics.

- **Prior progress:** as recorded in `current.md`/`whole-tail-continuation.md` — boundary layer
  `a₁ ≥ (L−u_nL)/2` CLOSED EXACTLY by Lemma WTC (do not re-attack). Deep interior open since R7,
  isolated since R15.

- **Dead ends (do not retry), consolidated + 2 new ones this round:**
  - (pre-existing, per Rule/current.md) covering-radius one/two-cap, dispersion/density/COUNT-
    injectivity, greedy recursion, bounded-depth escape, mass-telescope discrepancy, margin/extremal-
    tie — all DEAD, confirmed, do not re-propose.
  - **NEW #1 (this round): multi-anchor suffix-WTC** (`Φ ≤ min_k |2a_k − S_k|`, only suffixes as
    candidate subsets) — REFUTED, worst ratio grows with n (1.93→5.28 at n=3..5), clearly the wrong
    shape of bound.
  - **NEW #2 (this round): WTC-per-arbitrary-subset / "Ψ"** (`Φ ≤ Ψ(A) = min_T |2max(T)−sum(T)|`
    over ALL nonempty subsets, not just suffixes) — REFUTED as a uniform sufficient lever. Exact
    witness at n=6: `A = (frac. approx of) [0.2032,0.1757,0.1613,0.1413,0.1283,0.1030,0.0874]`
    (deep: `a₁=0.2032 < boundary=0.4961`; valley: `a₂=0.1757<β_6=0.2520`), where `Ψ(A)/u_6 ≈ 1.585`
    (FAILS) even though the TRUE `Φ(A)/u_6 ≈ 0.127` (holds with huge margin). **Diagnosis**: `Ψ`
    only captures "leader `a_k` vs. subset of strictly smaller tail elements", which is too coarse
    for smooth/near-geometric profiles where the true minimizer is an *alternating decimated*
    subsequence spanning the WHOLE profile (both above and below the chosen leader in the sort
    order is irrelevant — the point is it needs ≥4 simultaneous signed terms in a specific
    alternating pattern, which no single-leader-vs-tail-subset bound can express). This is a
    genuinely distinct failure mode from the 6 previously-dead families — record as a 7th dead
    upper mechanism-attempt (any "single-leader vs.-remaining-subset" WTC generalization).
  - **IMPORTANT CORRECTION to the dispatch's framing**: the dispatch states dispersion/COUNT
    "only actually fail in the (now-closed) boundary layer." This is **not accurate** — the
    certified COUNT counterexample (`multiset-doubling.md`/`current.md` R11: the all-equal profile
    `a_i = 1/(n+1)`, `n≥3`) has `a₁ = 1/(n+1)`, which is **deep interior** for all n≥2 (e.g. n=4:
    `a₁=0.2 ≪ boundary≈0.484`), not boundary. So the dispersion/COUNT family's decisive failure
    witness lives squarely in the deep interior, not the boundary — the "only fails at the boundary"
    premise should be dropped. (It doesn't kill the deep-margin idea — Φ is genuinely small there,
    0 in fact via pairwise cancellation on the all-equal profile — but any dispatch reasoning that
    leans on "dispersion only fails near the boundary" is unsound and should not be repeated.)

- **Small-case / intuition notes (labeled conjecture where not exact):**
  - CONJECTURE (numerically very well supported, exact-fraction spot checks + Dirichlet-random
    adversarial search, 0 fails across n=3..7): the deep-interior margin `Φ/u_n` stays bounded away
    from 1, plausibly bounded by something like `0.3–0.8` uniformly, not degrading with n — this is a
    stronger and more precise form of R15's finding.
  - CONJECTURE: the true worst-case / hardest-to-prove deep-interior profiles are **smooth
    near-geometric decreasing sequences** (ratios `a_{i+1}/a_i` roughly constant and away from `1/2`
    — e.g. the n=6 witness above has ratios ≈0.86–0.91, i.e. much flatter than dyadic `1/2`), where
    the winning cancellation subset is a decimated/alternating pattern rather than a prefix, suffix,
    or "leader+tail-subset". Both the multiset-doubling all-equal witness (ratio 1, extreme flatness,
    trivial `Φ=0`) and this n=6 near-geometric-but-not-flat witness (ratio ≈0.9, `Φ` small but not
    trivially 0) suggest the mechanism should be parametrized by the *local decay ratio* rather than
    by any fixed subset-selection rule. This is the most promising concrete lead for a next-round
    outline/builder to pursue, but it is UNDEVELOPED (no lemma, no proof sketch) — purely a scouted
    opening per the explorer mandate.
