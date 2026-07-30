## imo-2026-03 — LENS: overlap term λ(O_{π0}∩O_{F'}) via F''s recursive dyadic cut-tree

### Setup recap (from certified lemmas, no re-derivation)
Top-scale peel `F=π0⊎F'`, `F'=⊎_{j=1}^n π_j` itself a simultaneous dyadic refinement (budget
`b=Σ_{j≥1}a_j ≤ n−a_0`). Certified SD/PEEL (`peel-difference-bound.md`):
`D̃(F)=D̃(π0)+D̃(F')−2λ(O_{π0}∩O_{F'})`. Need `D̃(F)≥1` i.e. an UPPER bound
`λ(O_{π0}∩O_{F'}) ≤ (D̃(π0)+D̃(F')−1)/2`. Equivalently (FLOOR/layer form,
`floor-half-reduction.md`+`positive-layer-localization.md`): `I_n=P−Q≤0`, `P` (π0-driven positive
layers) already UPPER-bounded by `Σ y_{2k}` (POS lemma); need `Q ≥ P`, `Q` governed entirely by
`N_{F'}`, i.e. by F''s own recursive cut-tree.

### Distinct openings surfaced this round

**(a) Scale-XOR decomposition of `O_{F'}` (the natural inclusion–exclusion move).**
By the general SD identity applied repeatedly inside `F'`: `1[N_{F'}(t) odd] = ⊕_{j=1}^n
1[N_{πj}(t) odd]` — i.e. `O_{F'}` is the XOR (across F''s own n scales) of each single-scale
odd-set. This is EXACTLY the certified `(⊞)` reformulation from R8 (`scale-parity-xor.md`),
restricted to F' instead of the whole `F`. **Tested numerically**: the natural union/subadditive
consequence `λ(O_{π0}∩O_{F'}) ≤ Σ_{j=1}^n λ(O_{π0}∩O_{πj})` holds pointwise (trivial: if the XOR
is odd, ≥1 term is 1) — verified 0/3000 exact-`Fraction` trials, n=4. But **this bound is too
weak to close the target**: `(D̃(π0)+D̃(F')−1)/2 − Σ_j λ(O_{π0}∩O_{πj}) < 0` on 1125/3000 trials
(worst deficit ≈ −7.6), i.e. the per-scale union bound massively overcounts whenever several
scales are simultaneously active — exactly the "non-additive across scales" failure mode R8
already proved for the flat `(⊞)` genfn engine. **This confirms (a) re-encodes the R8-dead
wall**: any additive/union combination across F''s scales loses the cross-scale cancellation
that the true parity XOR exploits. Do not build this as posed; it is a cheap-kill, not an opening
(reported here as a NEGATIVE finding, verified fresh for the overlap-specific object, not just
inherited from the old ban).

**(b) Asymmetric recursive peel of `F'` alone (single-scale-at-a-time), holding π0 fixed as ONE
set (not expanded).** Peel `F'=π_1⊎F''` and apply SD/PEEL a second time inside the overlap:
`λ(O_{π0}∩O_{F'}) = λ(O_{π0}∩O_{π1}) + λ(O_{π0}∩O_{F''}) − 2λ(O_{π0}∩O_{π1}∩O_{F''})`. This is
structurally the SAME move `split-rung-mutual-induction` made (R14, killed — its clean form
`(I1′)` FALSE 3931/4000). The honest identity produces a TRIPLE intersection term at every
recursion step, an infinite regress of higher-order overlaps rather than a closing bound — I
recommend **not** re-opening this exact recursion (banned per Rules: "clean sign-flip split-rung
identity `(I1′)` FALSE"); flagging only to confirm it is the same wall from this lens too, not a
fresh route.

**(c) Branching/entropy potential `B(t) := #{j∈[1,n] : N_{πj}(t) odd}` (the count of F''s
sub-scales that are "odd-active" at level t).** By definition `t∈O_{F'} ⟺ B(t)` is odd — so `Q`
(the negative layers) is governed by the PARITY of `B`, not its magnitude. This is a genuinely
different quantity from a scalar/count summary of Z (which the Rules ban — R3/R4/R9 "NEVER use
scalar-summary lower-bound / count summary of Z") because it is a FUNCTION of `t`, tracking
which/how-many scales conspire at each level, not a single aggregate number. Two concrete
sub-directions worth scouting further (NOT attempted here beyond terrain-mapping, per role limits):
  - a weighted branching sum (e.g. `Σ_j 2^{j-n}·1[N_{πj}(t) odd]`, weighting deeper/smaller
    scales more) as a proxy potential correlating with where `Q`'s mass concentrates — motivated
    by the R7/R8 finding "surplus lives in the near-0 count-parity band" (deep scales dominate
    near t→0⁺).
  - a DUAL to the certified POS lemma: POS shows `P ≤ Σ_{k=1}^{K0} y_{2k}` using only π0's
    even-ranked VALUES (not counts). Is there an analogous LOWER bound `Q ≥` (some explicit sum
    over F''s parts, e.g. its own even/odd-ranked values at each scale, mirroring Lemma OB's
    odd-block alternating-value decomposition `odd-block-vertex.md`)? This has NOT been tried in
    this exact "NEG lemma dual to POS" framing — it is the natural missing counterpart and stays
    strictly within F''s own recursive structure (not a comparison to π0 at all until the final
    match-up `Q≥P`), which may sidestep both (a)'s non-additivity and (b)'s triple-overlap regress
    since it never needs an exact overlap FORMULA, only two independent one-sided bounds `P≤…`,
    `Q≥…` that are then compared termwise.

**Cheap numeric check performed:** confirms (a) is dead (union bound provably too weak, fresh
verification). (b) inherits R14's exact refutation. (c) is UNTESTED — the natural next probe
(for the outliner/builder, not done here) is: compute `Q` explicitly and compare against a
candidate closed form built from F''s parts values at even/odd multiplicity ranks (Lemma-OB style),
analogous to how POS used π0's even-ranked VALUES `y_{2k}` rather than a count.

### Candidate technique(s)
- Two-sided independent bounding (POS-style upper bound on `P` already certified; need a
  genuinely NEW *lower* bound on `Q` built from F''s own value-ranked structure, i.e. a "NEG
  lemma" dual to `positive-layer-localization.md`, likely via Lemma OB's alternating-value
  decomposition applied recursively to `F'`'s own dyadic sub-partitions) — the most promising
  untried opening.
- Explicitly AVOID any construction that (i) sums/unions overlaps additively across F''s scales
  (dead, (a) above, fresh numeric confirmation) or (ii) peels F' one scale at a time producing a
  clean local closed-form overlap identity (dead, (b), R14).

### Cheap-kill candidates
- Before building a "NEG lemma" dual-to-POS: numerically test the natural guess `Q ≥
  Σ_{k} z_{2k-1}` (odd-ranked values of F', by analogy with POS's even-ranked values of π0) on a
  few hundred random feasible configs BEFORE writing any proof — cheap to falsify, exactly the
  discipline that killed (NEG) `Q≥S_π` last round (R14 meta) and (I1′) split-rung.
- Parity/size pigeonhole: `B(t)` is bounded above by `n−a_0` (number of scales with a cut,
  ≤ total budget `b`); any candidate `Q`-lower-bound that only uses `b` as a scalar is already
  known insufficient (R10: `M(0⁺)≤1` alone insufficient) — a valid NEG lemma MUST use F''s
  ranked VALUES at each scale, not merely counts.

### Knowledge-base entries to use
- `knowledge_base.md` "Double counting" (generic double-count/two-ways framing) — motivates
  trying an exact two-sided count of the overlap, but nothing scale-tree-specific is present in
  the KB; the KB has no dedicated entropy/branching-potential entry for recursive dyadic
  structures. No other KB entries are more relevant than what prior rounds already used
  (Lemma G / level-measure, already certified in-repo).

### Analogous past problems (cruxes)
Searched combinatorics (double-counting, coloring-and-parity, invariants-and-monovariants,
extremal-principle) filtered by dyadic/2-adic/recursive/overlap/inclusion-exclusion keywords.
- **aimo-0966** (combinatorics, generating-functions/double-counting): "sieve a family by
  inclusion–exclusion over a set of markers so each member is counted with net multiplicity one."
  Structurally closest in SPIRIT (a clean net-multiplicity-one I/E identity turns an alternating
  sum into 1) but the mechanism (binomial-power padding `(x+y)^{c(P)}=1`, bijective coefficient
  extraction) does not transplant — there is no natural "padding" variable here since F''s scales
  are already forced by the fixed dyadic sizes, not a free choice. Worth a glance only as
  inspiration for "engineer an identity=1 via a padding trick," not a direct crux.
  - **aimo-0917** (combinatorics, games-and-strategy/invariants): "split the invariant's count
  over the two possible responses as `N=N_++N_-`, so an odd-valuation total forces at least one
  branch to inherit that valuation." Already checked and ruled out for this exact wall in R11
  (memory rule 33): the transplant fails because GAP L has NO adversarial branch choice left to
  exploit once collapsed via Lemma G to a static universal inequality — re-confirmed here, not
  re-tested.
  - No crux in the corpus does a genuine "asymmetric recursive overlap of a fixed top object
  against a recursively-refined lower object" — this is a bespoke structure of imo-2026-03's own
  Structure Lemma; **no strong analogue found**, report honestly rather than force a match.

### Prior progress
GAP L fully reduced (certified) to `I_n=P−Q≤0`; `P≤Σy_{2k}` (POS, certified); the base slice
`b=0` (`F'=L`) is fully proven (★). The sole open wall is a lower bound on `Q` from F''s own
recursive dyadic cut-tree — see current.md / run_state.md for full history.

### Dead ends (do not retry — consolidating Rules + this round's fresh checks)
- Scale-XOR union/subadditive bound across F''s scales (this round, fresh numeric confirmation,
  1125/3000 fails, n=4) — re-encodes R8's `(⊞)`/genfn wall.
- Single-scale-at-a-time peel of F' producing a clean local overlap identity — R14's `(I1′)`,
  FALSE 3931/4000.
- All π0-fixed comparison (single or multi-cut), ABSORB-as-engine, scalar/telescoping/sign
  bounds, merged-order/measure/sequential/genfn/GAP-IMR framings, φ(b) b-pruning — per Rules,
  not re-scouted here.

### Small-case / intuition notes (conjecture only)
- The numeric evidence (this round + R7/R8's "surplus concentrates near t→0⁺") suggests `Q`'s
  mass is dominated by F''s DEEPEST active scales (small parts near 0), where many sub-scale
  odd-indicators coincide — consistent with a VALUE-weighted (not count-weighted) dual to POS
  being the right shape, since deep scales contribute small values but potentially many of them.
  This is a hypothesis for the outliner to test structurally, not a proven fact.
