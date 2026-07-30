## imo-2026-03 (UPPER wall, deep interior a₁ < (L−u_nL)/2)

- **Exact deep-interior target.** Certified reduction stack: Lemma RL (leftover-realizability)
  characterizes 𝓡(A) = tree-realizable signed subset sums; Reduction R-UV (sufficiency) says
  Xiang forces D ≤ u_nL as soon as min 𝓡(A) ≤ u_nL. Lemma FGR gives the concrete sufficient
  object μ_{n+1} = min_i dist(a_i, R_{i−1}) (the "descending include/skip" family — a FIXED
  left-to-right differencing order over subsets T ⊆ {1,…,n+1}, i.e. 2^{n+1} leaves of the
  recursion R_0={0}, R_i = R_{i−1} ∪ {|v−a_i| : v∈R_{i−1}}); Reduction R-COV' (sufficiency
  certified) says μ_{n+1} ≤ u_nL ⟹ D ≤ u_nL. Target: **some nonempty T (in this fixed-order
  family) gives descKK(T) ≤ u_nL** — either exactly 0 (trivial, always admissible) or the
  smallest positive leaf value ≤ u_nL. Available UNUSED hypothesis: a₁ < (L−u_nL)/2 (WTC is
  vacuous here since |2a₁−L| = L−2a₁ > u_nL).

- **Distinct openings surfaced (this lens):**
  1. Naive **uniform second-moment over ALL 2^{n+1} leaves** of the fixed-order subset family:
     if mean(V²) over nonempty leaves ≤ (u_nL)², then min|V| ≤ u_nL trivially (min ≤ mean).
  2. **Best-of-size-class averaging**: for each subset size k, average V² over all C(n+1,k)
     size-k subsets (still fixed descending order); claim ∃k with mean ≤ (u_nL)² — a
     non-constructive "the right size exists" argument, exploiting that argmin |T| varies with
     the profile (2,3,5,4 at n=4,5,6,7 on generic witnesses — genuinely spread-out, matching the
     orchestrator's diagnosis that no single-size/constructive family suffices).
  3. (Flagged, NOT tested — out of budget) Second moment over the **full tree-realizable
     family** 𝓡(A) (Lemma RL — all binary differencing trees, not just the fixed left-to-right
     order), which is exponentially larger (Catalan-many structures) and might concentrate
     better since it isn't confined to one specific processing order.

- **Candidate technique(s):** probabilistic/averaging (2nd moment / Markov's `min ≤ mean`)
  over a tree-realizable ensemble — margin-tolerant, non-constructive, distinct from all 7 dead
  upper mechanisms (none of them used an averaging/expectation argument; all were
  constructive-selection, covering-radius, or single-anchor differencing).

- **Cheap-kill gates run (exact `Fraction`, sympy-free but exact rational arithmetic) — BOTH
  FAIL, decisively:**
  - **Gate 1 (uniform 2nd moment, all leaves).** On "genuinely hard" deep-interior profiles
    (random distinct integers rescaled to L=1, a₁ < (L−u_nL)/2, filtered to have **no**
    nonempty-T exact-zero — i.e. the honestly-hard case, not the trivial-zero shortcut):
    ```
    n=3: mean(V²)/(u_nL)² = 8.68     (true min-ratio 0.209)
    n=4: mean(V²)/(u_nL)² = 33.06    (true min-ratio 0.201)
    n=5: mean(V²)/(u_nL)² = 52.95    (true min-ratio 0.069)
    n=6: mean(V²)/(u_nL)² = 73.13–103.6  (true min-ratio 0.098–0.332)
    ```
    Ratio **grows with n**, reaching 2 orders of magnitude — the uniform-average population is
    dominated by large-value leaves (most leaves are close to a₁-scale); the true small witness
    is a rare needle the crude average cannot see. **KILLED.**
  - **Gate 2 (best per-size-class 2nd moment).** Same hard profiles, take min over subset-size
    k of mean(V² | size k):
    ```
    n=3: best-k mean(V²)/(u_nL)² = 4.92   (k=3)
    n=4: best-k mean(V²)/(u_nL)² = 0.305  (k=5)  -- PASSES here
    n=5: best-k mean(V²)/(u_nL)² = 9.83   (k=5)
    n=6: best-k mean(V²)/(u_nL)² = 13.21  (k=6)
    ```
    Passes only 1 of 4 tested n (n=4); fails at n=3,5,6 by factors 5×–13×, with no visible
    trend to shrink with n. **KILLED** (not robust — an inconsistent, cherry-picked pass is not
    a theorem).
  - Both gates used exact `Fraction` arithmetic, no floating point, on adversarially-generic
    (non-collision) deep-interior witnesses — this is a fast, clean kill, not a numerical
    artifact.

- **Why the argmin structure defeats both averages:** direct inspection of the actual
  minimizing T on 4 generic hard witnesses (n=4..7) gives |T| = 2, 3, 5, 4 respectively — sizes
  scattered with no monotone or size-independent pattern, and the achieving VALUE is ~2–3 orders
  of magnitude below the population mean at that size. The witness is a rare event in every
  size class tested, not a typical one — consistent with the orchestrator's diagnosis that the
  true minimizer is a "spread-out subset of all sizes that no single-leader/constructed-subset
  bound expresses," but it ALSO defeats the coarse-grained averaging that would normally be the
  non-constructive fallback for "spread-out, no explicit construction" claims.

- **Respecting Lemma RL / tree-realizability:** both gated ensembles (uniform-over-leaves,
  per-size-class) are built entirely from the certified FGR fixed-order recursion R_i =
  R_{i−1} ∪ {|v−a_i|}; every leaf corresponds to a genuine nonempty T with its descending-KK
  value, i.e. a bona fide element of 𝓡(A) (a sub-family of RL's full tree-realizable set,
  matching R-COV's certified sufficiency object exactly) — no arbitrary ±1 pattern was used.
  The untested Opening 3 (average over the FULL RL family, not just fixed left-to-right order)
  would still need to respect RL's tree-realizability constraint by construction (each
  differencing tree over any T is itself an admissible RL object) — flagged as the one
  remaining genuinely broader ensemble, not yet gated.

- **The a₁ < (L−u_nL)/2 hypothesis:** used only to select the "hard/deep" test profiles above
  (filtering by this exact inequality); no way was found in this pass to feed it QUANTITATIVELY
  into either averaging gate beyond selection — e.g. it does not obviously reduce the variance
  of the leaf-value distribution. This mirrors the boundary-layer WTC mechanism (which used a₁
  directly via |2a₁−L|) but a direct analogue for a variance/second-moment bound was not found;
  this is an open modeling gap for whoever picks up Opening 3.

- **Knowledge-base entries:** `knowledge_base.md` was checked for probabilistic-method /
  second-moment / discrepancy entries; none found (searched "second moment", "probabilist",
  "random", "averaging", "expectation", "discrepancy", "three-distance" — zero hits). No KB
  entry directly supports this direction; it would be a self-contained argument.

- **Crux corpus analogues.** Filtered `combinatorics`/`probabilistic-method` (only 4 cruxes
  total in the whole corpus): `aimo-0160` (average incidence count over rotations, pick
  above-average rotation — a genuine "min/max ≤ mean" existence move, but for a rotation
  group action, not subset sums), `aimo-0198` (adversarial encoding, unrelated), `aimo-0693`
  (average degree = E/V, unrelated), `aimo-0956` (graph recast, unrelated). **None are
  genuinely analogous** to a signed-subset-sum discrepancy claim — the structural mismatch is
  that `aimo-0160`'s ensemble (rotations of a fixed finite group) is genuinely uniform/symmetric
  with no "rare needle" problem, whereas here the true witness is a low-probability event under
  the natural (uniform or per-size) measure, exactly why the gates above failed. Also checked
  `size-bounding-and-descent`/`invariants-and-monovariants`/`pigeonhole` cruxes containing
  "subset sum"/"partial sum"/"signed sum" keywords (~40 hits) — closest in flavor is
  `aimo-0715` ("greedily choose each sign to pull the running partial sum back toward zero,
  then induct to confine each partial sum") — but this is a GREEDY/constructive sign choice,
  which is exactly the family already dead here (R9 greedy-recursion, R16 constructive
  subset-selection). No probabilistic/averaging crux was found that overcomes a "rare needle"
  structure; **judge: no genuinely analogous crux exists in the corpus for this specific
  target.**

- **Small-case / intuition notes (conjecture, from the numeric probes):** the true minimizing
  subset is a rare, structurally special witness (small value at an atypical size, with no
  consistent size across profiles) — this is consistent with 7 rounds of failed constructive
  and now 2 rounds of failed averaging attempts, and suggests the correct proof mechanism is
  neither "construct it" nor "average and win" but some THIRD kind of non-constructive argument
  — e.g. an extremal/exchange argument directly on the profile (show the WORST profile for
  μ_{n+1} is dyadically structured, analogous to how VALLEY-TIGHT pinned the boundary-layer
  extremal family) rather than a probabilistic ensemble over subsets. This is speculative and
  not gated.

- **Dead ends (do not retry, confirmed by direct check against Rules, not just cited):**
  covering-radius (one/two-cap), dispersion/density/COUNT, greedy recursion, bounded-depth
  escape, mass-telescope discrepancy, margin/extremal-tie, WTC-extensions / single-anchor or
  constructive subset-selection (all 7, per Rules — verified consistent with the lemma files
  read this round, no re-attack). **NEW (this round): naive uniform 2nd-moment averaging over
  the fixed-order subset family, and best-per-size-class 2nd-moment averaging — both KILLED by
  exact-Fraction gate** (ratios 5×–100×+ above target, non-monotone/inconsistent across n).

- **Ranked shortlist for the outliner (≤2 live directions):**
  1. **[WEAK/UNTESTED] Second moment over the FULL tree-realizable family 𝓡(A)** (all binary
     differencing trees over all nonempty T, not just the fixed left-to-right order) —
     genuinely distinct object from the gated fixed-order family (RL's family is a strict
     superset, per Lemma RL's own strictness result), potentially concentrates better since it
     has vastly more elements (Catalan(|T|-1) trees per subset vs 1). Make-or-break: does
     mean(V²) over 𝓡(A) (or a natural sub-ensemble of it) fall below (u_nL)² robustly across n,
     unlike the fixed-order family? NOT YET GATED (exponential enumeration cost not attempted
     this round) — the outliner should mandate this exact-Fraction gate before any build.
  2. **[SPECULATIVE] Extremal/worst-profile characterization of μ_{n+1}** analogous to
     VALLEY-TIGHT: instead of averaging over subsets for a FIXED profile, fix the (adversarial)
     worst profile structurally (conjecture: dyadic/near-dyadic, similar to A^{(n)}) and prove
     the bound there + a smoothing/majorization argument that no other profile is worse — this
     is NOT a probabilistic ensemble at all, it is the "prove it's tight and pin the extremizer"
     recipe that worked for the boundary layer (WTC) and for VALLEY-TIGHT itself, redirected at
     the deep interior where a margin now exists (so exact tightness is not required, only a
     bound). Both directions are genuinely different from each other and from the 7+2 dead
     mechanisms; direction 1 is the one the dispatch explicitly asked to scout and it failed at
     the "obvious" ensemble — the outliner should decide whether to gate the harder full-RL
     ensemble (1) or pivot fully to the extremal recipe (2).
