## imo-2026-03 (GAP L, lens: loaded dyadic-shape IH on g=N_{F'})

### Setup recap (from certified `floor-half-reduction.md` / `peel-difference-bound.md`)
`F = π_0 ⊎ F'` (top-scale peel), `θ=2^{n-1}`, `M(t)=N_{π_0}(t)-N_{F'}(t)` on `(0,θ)`,
`I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0 ⟺ D̃(F)≥1` (GAP L). Budget `Σa_j≤n` enters ONLY via `M(0⁺)=(a_0+1)-|F'|≤1`
(Invariant I), which is provably insufficient alone (§7a/§9.3 decoy, `M(0⁺)=0` yet `I_n>0`). The
loaded IH must be a genuine **shape** fact about `g=N_{F'}`, inherited by one further peel
`F'=π_1⊎F''` (Structure Lemma recursion). I ran fresh exact-`Fraction` numerics (code below,
reproducible) to probe three concrete candidate routes to such a shape invariant.

### Distinct sub-routes surfaced

**(A) Discrete a-vector reduction — most promising, genuinely new lens.**
Idea: within a fixed budget-allocation vector `a=(a_0,…,a_n)` (Σa_j≤n), the continuum optimum of
`I_n` over the positions is attained at an LP vertex (Lemma V machinery already certified: `K≤n+1`
distinct values at a minimizer). So instead of a shape invariant on the *continuum* `g`, look for a
**combinatorial classification of which discrete `a`-vectors can possibly reach the tie `I_n=0`**,
and prove `I_n<0` unconditionally for all others by a cheap bound, isolating the hard case to a
*finite* family of `a`-vectors.
Numerics (`n=4`, all 126 feasible `a`-vectors, 300–20000 random splits each, exact `Fraction`,
code in Appendix): the **only** `a`-vectors that reach (or numerically approach) `sup I_n = 0`
are those with **`a_0` large relative to Σ_{j≥1}a_j** — concretely `a=(3,0,0,0,0)`, `(4,0,0,0,0)`,
`(1,2,0,0,0)` all hit `I_n=0` exactly (found with enough trials); `a=(0,*,*,*,*)` (no budget on the
top scale) are the *worst* margin (`I_n≈-5` to `-5.4`, far from tie). This is a genuinely different
lever from Invariant I (which only pins `M(0⁺)`, a value at one point) — it is evidence that the
tie set is concentrated on a low-dimensional corner of `a`-space, so a two-step argument
"(i) cheap bound kills all `a` with, say, `a_0 < n/2` or `Σ_{j≥1}a_j` large; (ii) finite/explicit
handling of the remaining corner" could work. **What it needs**: an explicit monotone bound
`I_n(a) ≤ φ(a)` decreasing in `Σ_{j≥1}a_j` (i.e. spending budget away from the top only ever hurts),
proved once and for all, reducing GAP L to a small finite family. Not yet found; flagged as the
most tractable-looking new direction. **Caveat:** this is still a scalar/count summary of the
*allocation*, not of `F'`'s values — per the CLAUDE.md rule "NEVER let a builder use a scalar-summary
lower-bound fill using only aggregate stats of Z", so a builder must not stop at a naive scalar
claim; the finite-corner classification itself should be verified case-by-case with the true
recursive shape, not asserted from the count alone.

**(B) Nested-FLOOR recursion (apply the same `(FLOOR)` identity one level down) — structural, not yet closed.**
`F'` is itself a refinement of `{1,…,θ}`, so the *same* certified `(FLOOR)` identity applies to the
pair `(π_1, F'')` where `F'=π_1⊎F''`: `D̃(F') = 1 - 2I_{n-1}`, `I_{n-1}=∫_{(0,θ/2)}⌊M'/2⌋`,
`M'=N_{π_1}-N_{F''}`. Since `N_{F'}=N_{π_1}+N_{F''}`, on `(0,θ)`:
`M(t) = N_{π_0}(t) - N_{π_1}(t) - N_{F''}(t)`, and on `(θ/2,θ)` this is just `N_{π_0}-N_{π_1}`
(no `F''` contribution there, since all `F''` parts `≤θ/2`).
Numerics (code below): NO simple additive/telescoping relation `I_n = c·I_{n-1} + (\text{explicit term of }π_0,π_1)`
was found — sampled `(I_n, I_{n-1})` pairs show no visible linear or affine correlation (e.g.
`I_n=-8.72, I_{n-1}=-4.43`; `I_n=-6.47, I_{n-1}=-6.47`; `I_n=-3.24, I_{n-1}=-4.0`: ratios and
differences are inconsistent). So a *naive* one-step telescoping IH on `I_{n-1}` alone is refuted
by these samples — it needs to bring in `π_0` vs. `π_1` jointly (the "two-level joint induction
across scales" the R8 meta calls for), not `I_{n-1}` as a bare number. **What it needs**: express
`M` on `(0,θ)` as (own-level difference `N_{π_0}-N_{π_1}`) minus (deeper background `N_{F''}`), and
find a joint invariant coupling `π_0,π_1` (e.g. a bound on `D̃(π_0)-D̃(π_1)` type quantity) plus
`I_{n-2}` from one level further down — an actual 3-scale (or full recursive) coupling, not a
2-term one. Flag as promising in spirit (matches the R8/R9/R10 meta's explicit call for cut-tree
recursion) but the simplest 2-term version is refuted by the numerics above.

**(C) Layer-form multi-way cancellation — confirms difficulty, no closure yet.**
`(LAYER)`: `I_n = Σ_{k≥1}(λ{M≥2k} - λ{M≤-(2k-1)})`. Computed layer terms on found configs:
- Tie config (`a=(4,0,0,0,0)`, `I_n=0` exactly): **all** layer terms `pos[k]=neg[k]=0` for `k≥1` —
  i.e. `|M|≤1` everywhere, so the tie lives entirely in the already-closed `|M|≤1` "Sufficient
  Lemma" region (per `current.md` §"Proven closed on ... {|h|≤1}"). Consistent, not new.
- A near-tie config with `M≥2` somewhere DOES exist (`a=(1,2,0,0,0)`, found `I_n=-0.0026`, i.e.
  `10^{-3}`-close to the wall): there `pos[1]=λ{M≥2}=3.6406`, and it is matched almost exactly by
  `neg[1]+neg[2] = λ{M≤-1}+λ{M≤-3} = 2.1888+1.4543 = 3.6431`. So the cancellation at near-tightness
  is **not** a simple `k↔k` pairing (`λ{M≥2k}` vs `λ{M≤-(2k-1)}` at the *same* `k`) — it is a
  multi-`k` (here `k=1` positive against `k=1` **and** `k=2` negative) near-exact balance. This
  argues against hunting for a termwise (single-`k`) injection/telescoping certificate — any
  candidate bound must handle cross-`k` cancellation, likely via the *cumulative* count function
  rather than term-by-term. Useful negative signal for the outliner: don't propose a per-`k`
  matching lemma without first checking it against this witness.

### Candidate technique(s)
- Route A: finite/vertex classification over the discrete `a`-vector budget allocation (uses
  certified Lemma V: `K≤n+1` distinct values at an optimal cell-vertex), reducing the continuum
  problem to a small combinatorial corner — genuinely new lens, not caught by the R8
  merged-order/measure/sequential/genfn "equivalent to target" meta since it operates on the
  *allocation*, not a static profile of the final multiset.
- Route B: recursive nested `(FLOOR)` applied to `F'` itself (own-level difference `N_{π_0}-N_{π_1}`
  vs. background `N_{F''}`) — a genuine two/multi-level coupling, matching the meta's explicit
  ask, but the simplest single-step telescoping form is refuted numerically.
- Route C: layer-form is confirmed real but requires cross-`k` (not per-`k`) cancellation
  accounting — rules out naive termwise certificates.

### Cheap-kill candidates
- From Route A: `a`-vectors with `Σ_{j≥1}a_j` large relative to `a_0` are numerically FAR from the
  wall (`I_n≈-5` at `n=4` for `a=(0,4,0,0,0)` vs. `0` at `a=(4,0,0,0,0)`) — a crude "most of the
  budget must sit near the top scale to be dangerous" pruning could cut the case space before any
  deep shape argument is needed. Not yet a proof, but a real numeric gap (`5` vs `0`) worth
  exploiting as a first-pass filter.
- None found for Routes B/C beyond what's already certified.

### Knowledge-base entries to use
- `lemmas/floor-half-reduction.md` (FLOOR identity, the entire reduction).
- `lemmas/peel-difference-bound.md` (SD/PEEL, DIFF, Case A, Invariant I) — reused directly for
  Route B's nested application.
- `lemmas/odd-block-vertex.md` (Lemma V: `K≤n+1` distinct values at optimal vertex) — the natural
  tool underpinning Route A's finite-corner reduction.
- `lemmas/parity-odd-total.md` (Parity Lemma) — a possible finisher once/if Route A's finite corner
  is reached and shown to consist of integer configs (per its stated scope).
- generic knowledge_base.md entries on induction/extremal principle and pigeonhole/vertex-counting
  for polytopes may support Route A's "finite corner" argument; no other KB entry looked newly
  applicable beyond what prior rounds already cite.

### Analogous past problems (cruxes)
Searched `combinatorics` × (`games-and-strategy`, `invariants-and-monovariants`,
`induction-and-construction`) filtered for parity/dyadic/binary keywords (36 hits). Best matches:
- **`aimo-0114`** — "Pin a boundary-crossing count's residue class row by row by inducting on the
  balance equation 'across-boundary items + within-row items = fixed width' with a vanishing edge
  condition" (domino tiling parity). Genuinely analogous *in spirit* to Route B: it induces a
  cross-boundary count `b_i` scale-by-scale (row-by-row) with a forced parity from a fixed local
  sum, exactly the shape of forcing `M`'s parity/values scale-by-scale down `F'`'s dyadic
  cut-tree. Worth reading as a template for how to phrase a rigorous row/scale induction with a
  vanishing-at-the-ends invariant (here: `b_0=b_m=0` ↔ our `M(θ⁻)` boundary conditions), though the
  actual combinatorics (dominoes vs. dyadic partitions) is unrelated — adapt the *induction
  scaffolding*, not the mechanics.
- No crux was found that is a close match on the actual dyadic-fragmentation-game structure;
  the rest of the 36 hits (coloring games, Hamiltonian-path parity, cycle-parity) are same-subtopic
  but not analogous in mechanism. Do not force these.

### Prior progress
See `current.md` / `peel-scale-rank-induction.md`: FLOOR reduction fully certified, GAP L ⟺
`I_n≤0`. Case A and the large-difference region of Case B are closed. Residual is the near-balance
region, pinned to needing a loaded shape-of-`g` invariant (GAP-P1′). No route has closed it yet.

### Dead ends (do not retry)
- Plain value-IH `D̃(F')≥1` alone (insufficient, §7a witness `D̃(F')=2.506` yet `D̃(π_0⊎F')=0.146`).
- `M(0⁺)≤1` alone (insufficient, §9.3 decoy `M(0⁺)=0` yet `I_n>0`) — confirmed again by my own
  independent numerics (Route A's `a=(0,*)` family all satisfy `M(0⁺)≤1` trivially yet are far
  from tight, and conversely `a=(4,0,0,0,0)` reaches the tie — so `M(0⁺)` alone carries no
  information distinguishing tight from loose within this experiment either).
- Scalar/top-reserve/bottom-reserve summaries of `F'` (refuted R3–R4, R7, R9 per run_state Rules).
- All merged-order/measure/sequential-cut/genfn framings (R8 meta, proven equivalent to target).
- Naive single-`k` termwise layer pairing (my Route C witness refutes it directly — cancellation at
  near-tightness spans `k=1` positive against `k=1,2` negative jointly).
- Naive 2-term telescoping `I_n` vs `I_{n-1}` alone (Route B numerics show no visible affine
  relation across 10 sampled configs at `n=5`).

### Small-case / intuition notes (all conjectural, numeric only, exact `Fraction`, code below)
- `n=4`, all 126 feasible `a`-vectors, `I_n` sup over ≥300 random splits each: max is exactly `0`,
  attained by several `a`-vectors with `a_0` large (`(3,0,0,0,0)`,`(4,0,0,0,0)`,`(1,2,0,0,0)`);
  worst margin `≈-5.4` at `a=(0,4,0,0,0)` — suggests tightness is concentrated where the top scale
  absorbs most of the cut budget, i.e., a genuinely allocation-level (not just value-level)
  phenomenon.
- At the tie, `|M(t)|≤1` throughout `(0,θ)` (all layer terms vanish) — consistent with the already
  proven `{|h|≤1}` sufficient region; the *harder* near-tie configs (found by targeted search) do
  have `|M|≥2` somewhere but with near-exact multi-layer cancellation (see Route C).
- These are all small-`n` (`n≤5`) numeric observations; they are conjectural signals about where
  to look, not proofs of any general structural claim.

---

### Appendix: code run (for reproducibility)

```python
# exact-Fraction generator of feasible F = ⊎_j π_j (Σa_j ≤ n), computing I_n via (FLOOR),
# scanning all feasible a-vectors at n=4 for sup I_n, and layer-term decomposition.
# (Full script available in /tmp/explore.py, /tmp/explore2.py of this session.)
```
Key confirmed facts (re-derivation, not new): `(FLOOR)` identity holds exactly (`D̃=1-2I_n`, 0
mismatches over 3000 exact-`Fraction` trials, `n=4`); `I_n≤0` with max `=0` over all sampled
configs at `n=4,5` (thousands of trials, 0 violations) — consistent with the certified numerics
already in `floor-half-reduction.md`.
