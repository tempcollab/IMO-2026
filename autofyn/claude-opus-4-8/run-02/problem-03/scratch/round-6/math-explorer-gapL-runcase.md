## imo-2026-03 — GAP L residual (maxc≥2 "run" sub-case)

### Distinct openings

1. **Anchor-domination via the Structure Lemma, two-level induction on Z's own
   Case-A/B split (the report's own proposed route).** `Z` (a `≤(n−1)`-cut response to
   `S_{n−1}={1,…,2^{n−1}}`) itself decomposes at its OWN threshold `θ/2=2^{n−2}` into
   `Z = Y'^{(0)} ⊎ Z'` (Structure Lemma, certified in `induction-recursion-telescope.md §5`),
   where `Y'^{(0)}` = fragments of `Z`'s top piece `θ=2^{n−1}` and `Z'` is a
   `≤(n−2)`-cut response to `S_{n−2}`. The natural attack: strengthen the IH `P(n−1)`
   from the bare scalar `altsum(Z)≥1` to a **carry-forward local statement** — e.g.
   "for every threshold `τ`, the restriction of `Z`'s merged-order signed sum below `τ`
   already banks at least (some anchor-indexed reserve)" — so that when `Y`'s top run
   consumes width against `Z` above `θ/2`, the induction can hand down the exact
   compensating surplus from `Z`'s own top anchor (or, recursively, from `Z'`'s). This
   is a genuine "disjunctive invariant with a reserve buffer" pattern (cf. CLAUDE.md /
   memory rule about aimo-0340, already used on the GAP-U wall) — **transplant that
   template to GAP L**: the IH must carry more than a scalar, it must carry a
   per-scale/per-level certificate that survives interleaving with `Y`.

2. **Attack the tie/boundary structure directly.** Numerically (see Probes below) the
   configs that are *closest* to violating (min `D̃` over `maxc≥2`) are **exactly the
   ones where `Y`'s top fragment `y₁` ties `Z`'s top uncut anchor `θ` (or a `Z`-cut
   fragment)** — i.e. sit on the boundary of the already-closed region
   `{y₁≥2^{n−1}+1}` (Half-total single-crosser Lemma, certified). This suggests
   reformulating the residual not as "maxc≥2" per se but as **"how far below `θ` can
   `y₁` be pushed while still having a run,"** and bounding `θ−y₁` against the run's
   negative contribution — a more surgical version of the existing `(◇◇)` bound that
   might close the residual with an explicit slack estimate rather than an abstract
   two-level induction.

3. **Strengthen Lemma T itself to a weighted/discounted version.** Instead of the
   sharp dichotomy `ψ(c)≥0 ⇔ c≤1`, note `ψ(c)` for `c≥2` is bounded (`ψ(c)≤1−c`, so it
   grows only linearly in `c`, and `maxc` is itself bounded by the number of Y-fragments
   `a+1≤n`). A weaker but possibly sufficient claim: bound the *total* negative area
   `Σ_{c_i≥2}(c_i−1[odd])Δw_i` directly via a **counting argument on how many disjoint
   "runs" can occur** (each run of length `≥2` costs Y at least 2 fragments locally,
   and the cut budget `a≤n−b` caps the total number/size of runs) versus the surplus
   `Z`'s `b`-cut budget can generate. This turns the geometric/measure argument into a
   combinatorial budget-counting one — closer in spirit to a direct pigeonhole/budget
   bound than the recursive induction, and may be easier to formalize than the full
   two-level induction.

### Candidate technique(s)
- Two-level (nested) strong induction on `n`, with the IH on `Z` strengthened to carry
  a per-scale reserve (reserve-buffer / disjunctive-invariant pattern).
- Alternatively, a direct combinatorial budget count on runs vs. anchors (pigeonhole on
  cut-budget `a+b≤n`), bypassing the recursive induction.
- Both routes must go **through** the Structure Lemma (certified, `§5` of
  `induction-recursion-telescope.md`) — a scalar/count summary of `Z` is refuted (do
  not resurrect).

### Cheap-kill candidates
- None found — every numeric probe (including a corrected, previously-buggy R5 script,
  see below) confirms `D̃≥1` holds on `maxc≥2` configs; no counterexample.
- One structural check worth flagging to the builder (not a kill, a **precision
  requirement**): `maxc` as defined (prefix imbalance in the merged descending list) is
  **order-dependent at exact ties** between a `Y`-value and a `Z`-value. Example found
  (`n=4`, `a=3`, `Y=(8,3,3,2)`, `Z=(8,2,2,2,1)`, both from a legitimate `≤4`-cut Case-B
  config with `a+b=4=n`): the raw multiset alternating sum is exactly `1`
  (`8−8+3−3+2−2+2−2+1=1`), but if the tie `8Y` vs `8Z` is broken with `Y` first, the
  merged prefix imbalance reaches `c=2` (a genuine `Δw=1`-wide run from `t∈(2,3)`, not a
  measure-zero artifact) — i.e. this is a bona fide `maxc=2` config attaining `D̃=1`
  EXACTLY, which at face value contradicts the round-4 numeric claim "every tight
  config has `maxc≤1`" / "`maxc≥2` residual has strict slack `≈1.017`". Resolution:
  this is a genuine boundary point where the exact tie (`y₁=θ` exactly) is what
  supplies the compensating surplus; perturbing either value slightly moves it either
  into the already-closed region `y₁≥θ+1` or strictly above `D̃=1` — so it is not a
  counterexample to the theorem `D̃≥1`, but it DOES show the "maxc≥2 residual is
  strictly separated from equality" claim needs the word "generic" (distinct values)
  or must explicitly handle exact ties by continuity. **Tell the builder:** define
  `maxc` with a canonical tie-break (e.g., always break `Y`-before-`Z` ties, or work
  with the value-only alternating sum and prove the bound is tie-break-invariant) and
  treat `y₁=θ` exactly as part of the ALREADY-CLOSED boundary case, not the open
  residual — do not let a builder claim a uniform `>1.017` gap on all of `maxc≥2`; the
  true infimum on that region (properly defined) is `1`, approached but not exceeded
  by continuity from the closed region. This is a precision fix, not a new gap.

### Knowledge-base entries to use
- No `knowledge_base.md` generic entry is a close match for this specific dyadic
  cut-tree / merged-order argument (checked: the KB's general theorems are broad
  olympiad tools, not tailored to this construction). The load-bearing tools are the
  problem's own certified lemmas: Lemma G / Level-Measure identity, Cut-Flip/Domination
  (`lemmas/greedy-claim.md`, `lemmas/cut-flip.md`), Termwise Lattice Lemma T
  (`lemmas/termwise-lattice.md`), and the (uncertified but proved-in-approach-file)
  Structure Lemma + difference-function Sufficient Lemma
  (`approaches/induction-recursion-telescope.md §5`, `induction-recursion.md §5C`).

### Analogous past problems (cruxes)
Searched `combinatorics` domain, subtopics `invariants-and-monovariants`,
`coloring-and-parity`, `games-and-strategy`, `telescoping-and-summation`, plus keyword
scan for "dyadic/recursive/anchor/interleav/merged order/prefix imbalance". Findings:
- **aimo-0493** (`invariants-and-monovariants`/`extremal-principle`): "Tag each element
  by which dyadic threshold `2^k` separates two of its within-set gaps, producing one
  tag per scale `k`" and "compare each candidate to the set's minimum inside the dyadic
  band matching its gap ... gaps grow geometrically." This is the closest **structural**
  analogy: a per-scale (dyadic-level) certificate assigned recursively, which is exactly
  the shape opening (1) above needs (a per-level reserve indexed by `2^{k}`, not a
  single scalar). Worth reading in full if the outliner commits to the reserve-buffer
  induction.
- **aimo-0019** (`games-and-strategy`/`invariants-and-monovariants`): "bound a family of
  dyadic-length pieces of pairwise distinct sizes by twice the largest, via the
  geometric sum of distinct negative powers of two" — a cut/paint game with dyadic ink
  quantities; thematically close (dyadic adversarial game) but the actual crux move
  (geometric-sum domination by the largest piece) is already essentially what Lemma T /
  Case A domination uses, not new for the residual.
- No genuinely matching "merged-order signed-sum / prefix-imbalance / ballot-type"
  crux was found for this exact construction; the several "interleaving" cruxes found
  (aimo-0250, aimo-0720, aimo-0916) are about interleaving two *sequences* for a
  construction/majority argument, not about bounding a signed alternating sum along a
  merged order — judged NOT genuinely analogous, do not force the match.

### Prior progress
- Lemma T (certified) closes the entire `maxc≤1` region unconditionally: `D̃≥1` whenever
  the merged prefix imbalance never reaches 2.
- Structure Lemma (proved in `induction-recursion-telescope.md §5`, not yet in
  `lemmas/`, good promotion candidate): the recursive `Z=⊎_j Y^{(j)}` cut-tree
  decomposition, giving the anchors needed for the residual.
- Fragment-count obstruction (R4, certified fact in `induction-recursion.md §5C R4`):
  for `b≥2`, `h(0⁺)≤1−2b≤−3`, so `|h|≤1`/exchange-based routes cannot finish — this
  is why the residual needs the recursive structure, not a one-shot exchange.
- Open sub-claim `(GAP-LB′-run)`: T-run deficit `≤` anchor surplus, precisely stated in
  `induction-recursion-telescope.md §6`. It IS precisely formulable (as an inequality
  between two sums over prefixes of the merged order, both restricted by sign of
  `c_i−1` resp. `c_i`), and is plausible: it held with 0 violations over 4·10^5 random
  configs (R4) and over an additional ~50 targeted Nelder-Mead optimizer searches (this
  round, `n=3,4,5`, various `a,b` and cut-count schedules) — every found infimum for
  `maxc≥2` was `≥1` with the true optimum apparently `=1` (attained only at the tie
  boundary described above).

### Dead ends (do not retry)
- Scalar/aggregate summaries of `Z` (e.g. `D̃ ≥ sum(Y)−sum(Z)` unconditionally, or any
  fill using only `altsum(Z)` / `D_bot` without location info): PROVEN FALSE, 3
  counterexamples (R3–R4).
- One-sided confinement of `O_Z` to a "high" region: REFUTED even at `n=1` (cutting
  the `2` into `x,2−x` reaches an odd-set arbitrarily close to `0`).
- Exchange/`|h|≤1` route (`induction-recursion` twin): proved structurally unable to
  close `b≥2` configs (Fragment-count obstruction, R4) — confirmed correct on
  re-inspection this round (the derivation `h(0⁺)=(a+1)−(n+b)≤1−2b` is airtight given
  the budget `a+b≤n`); do not re-attempt this as the primary route for the residual,
  though its Sufficient Lemma `(R2)` remains valid and reusable for whatever sub-cases
  do satisfy `|h|≤1`.
- Treating "maxc≥2 has a uniform strict slack `>1`" as already-proved: it is **not** —
  the tie-boundary example above shows the infimum is exactly `1`, approached; any
  builder claiming a strict numeric slack bound (e.g. `≥1.017` universally) is
  overclaiming based on a finite random sample, not a proof. The correct target
  statement is the non-strict `D̃≥1` (with equality only at measure-zero tie
  configurations continuous with the closed region), matching Lemma T's own
  equality-robustness.

### Small-case / intuition notes (conjectural unless stated as proved above)
- Re-ran the R5 probe script `/tmp/round-5/probe_runcase.py`: **it contains a bug** —
  it calls `gen_Z(n-1, b, rng)` for the bottom-block generator, but the bottom block
  should have `n` pieces `{1,…,2^{n-1}}` (indices `0..n-1`), not `n-1` pieces; this
  silently drops `Z`'s own top anchor `2^{n-1}` from the simulation. Uncorrected, this
  gave spurious `Dtilde` values as low as `−14.78` for `maxc≥2` (looks like a
  counterexample!). Re-running with the fix (`gen_Z(n, b, rng)`, 200k trials, `n=5`)
  gives **0 violations of `D̃≥1`** and `min D̃≈1.22` among sampled `maxc≥2` configs
  (random, non-optimized — consistent with the builder's own optimizer-based `≈1.017`).
  **Flag this bug to the outliner/builder**: any future numeric work reusing
  `probe_runcase.py` verbatim must first apply this one-line fix, or its "violations"
  are artifacts, not real counterexamples.
- Targeted Nelder-Mead search (this round, `/tmp/opt_check.py`, `/tmp/opt_check2.py`,
  `/tmp/opt_check3.py`) forcing `maxc≥2` via a penalty term found infima of exactly
  `D̃=1.00000` for several `(n,a,cutcounts)` configurations at `n=3,4,5` — in every case
  inspected, the minimizer sits at an exact-tie boundary (`Y`'s fragment value equal to
  a `Z`-anchor or `Z`-cut-fragment value), consistent with "the residual's true
  infimum is `1`, attained only at boundary ties with the already-closed region," not a
  counterexample and not evidence of slack strictly `>1` either. This conjecturally
  confirms `(GAP-LB′-run)` is tight (an equality-robust inequality, matching Lemma T's
  own character) rather than strict, which should guide the two-level induction to
  prove a **non-strict** `≤`/`≥`, with equality tracked precisely (useful for
  eventually merging with Lemma T into one unconditional certified lemma).
