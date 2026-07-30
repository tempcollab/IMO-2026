## imo-2026-03 — lens: GAP-P1 (loaded dyadic-shape IH for the peel induction, Case B residual)

### What's actually needed (restated precisely)
Peel identity (certified `lemmas/peel-difference-bound.md`): `D̃(F)=D̃(π_0)+D̃(F')−2λ(O_{π_0}∩O_{F'})`.
Case A closed; Case B closed on `{|D̃(π_0)−D̃(F')|≥1}` via the trivial overlap bound
`λ(O_{π_0}∩O_{F'})≤min(D̃(π_0),D̃(F'))`. The **only** open residual is the near-balance band
`{|D̃(π_0)−D̃(F')|<1}`, where the target reduces to a *tighter* overlap bound:
`2λ(O_{π_0}∩O_{F'}) ≤ D̃(π_0)+D̃(F')−1`. The plain scalar IH `D̃(F')≥1` cannot supply this (§7a
witness: `F'` with `D̃(F')=2.506` but `D̃(π_0⊎F')=0.146` — that `F'` is NOT a genuine dyadic
refinement, only an altsum-matching decoy). So the loaded quantity must be something that (a) a
real dyadic-refined `F'` provably carries, (b) a decoy multiset of the same total/altsum does NOT
carry, and (c) directly caps `λ(O_{π_0}∩O_{F'})`.

### Distinct openings for what the loaded quantity should be

1. **Vector/coupled-system IH across dyadic scales (the closest crux analogue, see below).**
   Instead of strengthening `D̃(F')≥1` to one bigger scalar inequality, strengthen it to a
   **tuple of simultaneously-inducted claims**, one per "residue"/scale-role, that feed each other
   under the peel recursion — mirroring how a single scalar claim about `Σ(−1)^{s(k)}` had to be
   split into THREE coupled claims (on `3i`, `3i−1`, `3i−2`) to close under bit-peeling. Here the
   natural coupling is across the *recursive* peel `F' = π_0' ⊎ F''` (one scale down): track not
   just `D̃(F')` but the **pair** `(D̃(F'), λ(O_{π_0'}∩O_{F''}))` — i.e. propagate the SAME
   overlap-type quantity you are trying to bound at level `n` down to level `n−1`, and prove the
   two overlap bounds close a joint recursion. This is a genuine "loaded shape" claim (not a
   restatement of `D̃≥1`) because it is a statement about *how* `F'` attains its discrepancy, not
   just its value.

2. **Top-part / anchor position as the loaded quantity.** Case A's clean closure came entirely
   from `π_0` being a single part with `O_{π_0}=(0,2^n)` — an interval containing all of `O_{F'}`.
   The residual is exactly where `π_0` has ≥2 parts AND `F'` is comparably "spread," so neither
   `O_{π_0}` nor `O_{F'}` dominates the other as an interval. Candidate loaded invariant: track
   `y_1(F')` (largest part of `F'`) relative to `θ/2 = 2^{n-2}` (i.e. whether `F'` is ITSELF
   "Case-A-like": one part near-dominant vs genuinely fragmented) and prove a two-level joint
   statement: if `F'`'s own top piece `π_1` (one scale further down) is uncut, the overlap bound
   sharpens by the same mechanism as Case A, recursively. This recurses Case A's proof one level
   down instead of restating `D̃(F')≥1`; worth testing whether the residual region is EXACTLY where
   both `π_0` and `π_0'` (F's top-two dyadic pieces) are simultaneously fragmented — if so the
   induction should load on "number of already-fragmented top scales," a monovariant that only
   takes finitely many values and bottoms out.

3. **Majorization / order-statistics domination (aimo-0287 crux, adapted).** Track that `F'`
   majorizes (in the standard prefix-sum-of-sorted-parts sense) a canonical extremal shape —
   candidates: the "all-uncut ladder" `{2^{n-1},…,1}` (Case-A equality attainer, §4) or the
   bisection-heavy shape from the certified upper-bound construction. A majorization-type loaded
   IH is attractive because majorization is exactly the kind of "shape, not value" property that
   distinguishes a real refinement from an altsum-matching decoy (the decoy witness in §7a has a
   near-flat/near-equal sorted profile, very UNLIKE any real dyadic refinement's profile, which is
   forced lumpy by the `2^{n-j}` weights). This needs checking against the R8/R9 "static profile ⇒
   equivalent to target" meta-warning (rule 26 in memory) — a majorization order over the FINAL
   multiset was one of the refuted merged-order framings, but majorization over the SPECIFIC
   sub-multiset `F'` compared to its OWN canonical shape (not a merged Y/Z profile) is a different,
   untried object; flag but do not assume it survives the meta-obstruction.

4. **Multiplicity/count vector `(a_0, a_1, …, a_n)` as the loaded state (budget-shape, not just
   budget total).** Invariant I already shows `M(0⁺)=(a_0+1)−|F'|≤1` depends on `a_0` and `b` only
   through their sum-vs-`n` relation. A genuinely loaded IH could carry the exact per-scale
   cut-counts `(a_1,…,a_n)` (not just their sum `b`) forward, since these directly determine the
   granularity of `F'`'s own recursive peel and hence how "spread" `O_{F'}` can possibly be. This
   is close to opening 1 but frames the load as a discrete combinatorial parameter (vector of
   integers with `Σ≤n`) rather than an analytic quantity — may be easier to induct on by strong
   induction on `Σa_j` (a bounded integer) instead of on `n`.

### Candidate technique(s)
- **Coupled/joint induction over recursively-linked sub-claims** (aimo-0377 pattern) — strengthen
  the scalar claim to a small system of claims that reference each other one peel-level down.
- **Two-level (or `k`-level) simultaneous peel**: instead of inducting `n → n−1` one scale at a
  time, do the inductive step on `n → n−2`, peeling `π_0` AND `π_0'` together and proving the
  residual directly in terms of the level-`(n−2)` object `F''`. This may dissolve the residual
  because Case A's mechanism (one scale dominates the rest) generalizes cleanly to "the TOP TWO
  scales jointly dominate the rest" — worth an explicit numeric check of whether
  `D̃(π_0⊎π_0') ≥ (2^n+2^{n-1}) − D̃(F'')` type identity holds and whether its analogue of (U1)
  closes the residual unconditionally, the way Case A did.
- **Majorization / rearrangement inequality** (aimo-0287) as a secondary candidate if opening 1/2
  stall.

### Cheap-kill candidates
- Before building any of the above, run the SAME §7a-style adversarial search but restricted to
  genuinely admissible `(π_0, F')` pairs where `F'`'s own top piece `π_0'` is FORCED to be uncut
  (`a_1=0`) — check whether the residual `{|D̃(π_0)−D̃(F')|<1}` even survives that restriction, or
  collapses entirely (which would validate opening 2/two-level-peel as sufficient on its own).
- Check parity: is `D̃(π_0⊎F')` always an integer at the tight/near-tight configs (it is, `ΣF` is
  odd throughout by the dyadic-ladder structure) — if the residual reduces to purely INTEGER
  configs, the certified **Parity Lemma** (`lemmas/parity-odd-total.md`, from the sibling
  `vertex-integrality-parity` approach) already gives `D̃(F)≥1` for free, no loaded invariant
  needed — but this only helps if the residual's *infimum* is attained on the integer lattice,
  which is exactly the unresolved GAP-IMR of that other approach. Worth explicitly checking
  whether GAP-P1's residual and GAP-IMR's residual are the SAME open set (if so, the two stuck
  approaches should be merged/cross-fed rather than developed independently).

### Knowledge-base entries to use
- KB "Pólya heuristics — induction loading / strengthening the hypothesis" (generic, names the
  move but has no specific dyadic content).
- No KB entry specific to dyadic/tree induction beyond the generic Erdős–Szekeres/coordinates
  entry (not directly relevant here — that's a 2-coordinate injectivity trick, not obviously
  transplantable, though the "map to a pair of coordinates, use injectivity + pigeonhole" flavor is
  loosely analogous to opening 1's "track a pair" idea; flagged as weak, not a strong match).

### Analogous past problems (cruxes)
- **aimo-0377** (number_theory, coloring-and-parity / modular-arithmetic-and-CRT) — STRONGEST
  match. Problem: prove `Σ_{i=1}^n (−1)^{s(3i)} > 0`. Crux: peeling the low bit of `k` splits a
  signed-parity sum into even/odd halves that recurse to smaller SAME-TYPE sums, but shifted by
  residue mod 3; the naive scalar claim doesn't close under this shift, so the induction is
  **strengthened to a coupled 3-claim system** (`f(3i)>0`, `f(3i−2)<0`, `f(3i−1)≤0`) that all
  three recurse into each other and close together. This is exactly the shape of GAP-P1: a scalar
  peel-induction (`D̃≥1`) that provably fails to close alone, needing a small system of
  co-inducted claims tied to the recursive (dyadic) structure. Directly informs opening 1.
- **aimo-0287** (algebra, invariants-and-monovariants via majorization) — moderate match. Uses a
  suffix-count majorization order to rule out a dominance relation between an optimal subset and
  an intermediate one. The *tool* (majorization as a shape-not-value invariant) is transplantable
  (opening 3); the problem's own combinatorics (subset sums summing to a target) is not close
  enough to call it a strong analogue — flagged as a technique-borrow only.
- **aimo-0438 / aimo-0965** (combinatorics, induction-and-construction) — weak match: both peel a
  boundary layer so the complement is a scaled congruent copy of the same region, i.e. clean
  self-similar peeling with NO loaded invariant needed (like this approach's own Case A). Useful
  only as a sanity check that "no load needed" is possible in self-similar peel proofs when the
  peeled piece dominates cleanly (as Case A found) — not applicable to the genuinely mixed
  residual.
- Nothing in the corpus solves a "peel-induction with a provably-insufficient scalar IH, needs a
  loaded dyadic-shape invariant" problem that matches GAP-P1's exact structure; aimo-0377 is the
  best available template for the *mechanism* (coupled system), not the specific quantity.

### Prior progress
Certified: peel (SD)/(PEEL) identity, (DIFF) difference bound, Case A closed unconditionally
(no value-IH), Invariant I (`M(0⁺)≤1`), Case B closed on 80.8% of sampled configs
(`|D̃(π_0)−D̃(F')|≥1`). All in `lemmas/peel-difference-bound.md` (certified round 9). The
residual `{|D̃(π_0)−D̃(F')|<1}` is the sole gap; §7a of the approach file gives a decisive
numeric refutation of the plain-value-IH sufficiency (`D̃(F')=2.506` but `D̃(F)=0.146` for a
non-dyadic decoy `F'`), and real dyadic refinements empirically hit `min D̃(F)=1` exactly on this
residual (`n=2..5`, `≥1.2·10^5` trials each, 0 violations) — so the target inequality is true,
just not yet proven.

### Dead ends (do not retry)
- **Plain scalar value-IH `D̃(F')≥1` alone** — proven insufficient (§7a decisive counterexample),
  do not resubmit as-is.
- **Prefix alternating-sum bound `Σ_{i≤2k}(−1)^{i−1}w_i≥0` for `F'`** — trivial/true but gives
  only `D̃(F)≥0` under insertion (too weak), rejected in §7b.
- **Scalar/top-reserve summaries of `F'`** — refuted in prior rounds (R3–R4 scalar summary; R7
  top-down reserve, `7306/4·10^5` violations) and independently the whole merged-order
  block/window/matching/tiling family (round 8 meta) and both directional sequential reserves
  (round 9, memory rule 23/25/26) — none of these transplant to "loaded IH on `F'`" either, since
  they are all restatements of the *static final-multiset* profile, whereas GAP-P1 needs
  something about `F'`'s *recursive origin*, a genuinely different object (per the approach
  file's own §7b argument for why it isn't yet excluded by the R8 meta).

### Small-case / intuition notes (conjecture, not proof)
- Numerically (n=3, exact `Fraction`, 2·10^5 trials) the decoy witness confirms real dyadic `F'`
  and near-equal-but-not-dyadic `F'` are numerically indistinguishable by `D̃(F')` alone but
  clearly distinguishable by their sorted-part profile: dyadic `F'`'s parts cluster at scale
  ratios `~2^{-j}` (lumpy geometric spread) vs the decoy's near-equal parts (`2.53, 2.25, 2.22`).
  This supports opening 3 (majorization/shape) and opening 4 (per-scale cut vector) as the most
  likely place the "extra bit" of information is hiding, more than opening 2 (single top-part
  position), since the decoy's failure mode isn't really about one dominant part — it's about
  overall flatness.
- **RAN the a_1=0 cheap-kill numerically (n=3, exact `Fraction`, 3·10^5 trials, random genuine
  dyadic refinements, Case A already excluded):** the residual band `{|D̃(π_0)−D̃(F')|<1}` has
  `109241` hits total; restricting to `F'`'s own top scale uncut (`a_1=0`, i.e. `π_0'` a single
  part) still leaves `97425` residual hits (**~89%, essentially NOT reduced**). Zero violations
  either way, `min D̃(F)=1` exactly in both slices. **Conclusion: opening 2 (single top-part /
  two-level-peel alone) is REFUTED as a sufficient reduction** — the residual is dominated by
  configs where `F'`'s top scale is ALREADY uncut, so forcing it uncut doesn't shrink the hard
  case; the missing information must come from deeper scales or from `π_0`'s own shape, not merely
  from whether `F'`'s immediate top piece is fragmented. This redirects weight toward **opening 1
  (coupled multi-scale system, aimo-0377-style)** and **opening 4 (full per-scale cut vector)**
  over opening 2. Script used: available on request (not saved to the workspace, reran cleanly
  with `random_partition` via exact-Fraction cut points on a `DENOM=10^4` grid to avoid float
  rounding artifacts — an earlier float/`limit_denominator` version spuriously showed `min D̃≈1−ε`
  as a "violation," which is a rounding artifact, not real; use exact Fraction arithmetic on this
  problem, never `limit_denominator`).
