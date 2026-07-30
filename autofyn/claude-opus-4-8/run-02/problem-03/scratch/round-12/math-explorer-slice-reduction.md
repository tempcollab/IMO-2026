## imo-2026-03 — LENS: GAP-P1′-b (slice-max reduction of general b to the extremal base b=0)

Scope: whether/how "prove (★)/I_n≤0 at b=0 (F'=uncut ladder L) ⇒ I_n≤0 for all feasible b" can be
made rigorous. I did NOT touch the base case itself (GAP-P1′-a) — that is the leader's other gap.

### HEADLINE (route c, decisive — a numerical FACT the outliner must have)
**b=0 is NOT the unique/strict worst case. The `I_n` slice-maximum is CONSTANT = 0 across every
b = 0,1,…,n−1.** Full integer enumeration of the whole feasible family (Structure-Lemma allocations,
all partitions), exact arithmetic:
- n=3: min D̃ per slice = **1, 1, 1**, 7 for b=0,1,2,3. (Ties I_n=0 at b=0,1,2; b=3=n is Case A.)
- n=4: min D̃ per slice = **1, 1, 1, 1**, 9 for b=0,1,2,3,4. (Ties I_n=0 at b=0,1,2,3; b=4=n is Case A.)
  Tie witnesses: b=1 `F=(8,8,4,4,3,2,1,1)`, b=2 `F=(8,8,4,4,3,2,1,1)` alloc `(1,1,1,0,0)`,
  b=3 `F=(8,8,4,4,2,2,1,1,1)`. (b=2 tie `{8,8,5,4,2,2,1,1}` from the R11 refutation reproduced too.)

**Consequence — the §10.7 premise is REFUTED.** The approach file's slice-maxima
"`−3.69, −0.55, −0.281, −0.295, 0` for b=4..0" (peel-scale §10.7) are WRONG (undersampled): they
claim strictly-negative maxima at b=1,2,3, but the true slice-max there is exactly **0** (min D̃=1,
attained by integer configs above). Only the terminal slice b=n (=Case A, a_0=0, already closed
unconditionally in §4) is strictly negative. So:
- Any "slice-max strictly decreasing in b" or "b=0 is the strict extremum" argument is **impossible**.
- A b→0 reduction is necessarily **max-preserving with zero slack at every tie**; it is exactly as
  hard as the full theorem at each of the (many) exact-tie configs. b=0's only genuine value is
  **structural** (F'=L is a fixed known object), not extremal.

### Distinct openings (this lens)
- **(a) Co-varying descent toward b=0 (merge one F'-cut + repartition π_0, budget-preserved).**
  The move: pick a scale π_j (j≥1) with a_j≥1, merge two of its parts (b→b−1); simultaneously give
  the freed cut to π_0 (a_0→a_0+1, repartition freely). Budget a_0+b is conserved, feasibility kept.
  I tested existence of a **D̃-non-increasing** such move on ALL n=4 configs with b≥1:
  **1395 / 1396 admit one**; the single failure is an **exact tie** `π_0={8,8}`,
  `F'={5,2,1}∪{4}∪{2}∪{1}`, D̃=1 (the b=2 tie). So a co-varying descent is a **near-total
  monovariant whose only obstructions are the characterizable tie family** (the D̃=1 "zigzag"
  configs). This is the most viable route in the lens: a two-part plan — descent handles the
  generic ≥99.9% (D̃ strictly >1, room to descend), and the exact-tie family is handled directly
  (it is a known, finite-shape family; see §10.2's red/blue alternation description). VIABLE but
  the tie carve-out is real work; the hard step is proving the descent D̃-non-increasing in general
  (I only verified existence of a good move per config, not a clean invariant selecting it).
- **(b) Direct extremal / vertex argument (max I_n over the feasible polytope at a vertex).**
  I_n is piecewise-linear in the cut positions; on a fixed merged-order cell it is linear, so its
  max sits at a cell-vertex = a degenerate (parts-collide) config. But **max I_n = min D̃**, and
  "min D̃ is attained at an integer/degenerate config" is **exactly the DEAD GAP-IMR
  integer-minimizer framing** (R10: proven equivalent-difficulty to the target; cross-scale mass
  transfer blocked by the hard sums Σπ_j=2^{n−j}). Route (b) is NOT genuinely distinct from the
  dead route — do not seed it. (The KB "Piecewise-concavity smoothing" entry is the philosophy
  here, but f is non-concave (R2), so no global smoothing-to-vertex certificate exists.)
- **(c) Is some interior b worse? — NO.** Answered above: slice-max is flat =0 for b<n, strictly
  negative only at b=n. No interior b beats b=0; they tie. This kills the "worst-case-hunting"
  angle but also kills any slack-based reduction.

### Candidate technique(s)
- Co-varying **exchange/monovariant** with an explicit **tie-set carve-out** (route a). NOT a
  pointwise π_0-fixed monovariant (refuted R11, ~30% fail) — π_0 must absorb the freed cut.
- The tie family should be handled via the certified **ladder-interleaving identity** (§10.2,
  `lemmas/ladder-interleaving-identity.md`): at ties, red/blue alternate perfectly after the lead
  red, both sides of (★) are 0.

### Cheap-kill candidates
- **Expose the §10.7 numerical error** (done here): the reported strictly-negative slice-maxima are
  wrong; there are integer ties at all b<n. The outliner should not build any argument that assumes
  strict b-slack. One-line integer enumeration reproduces it (`/tmp/probe_slice.py`).
- Before any descent argument, note b=n is Case A (already closed §4) — exclude it, don't re-handle.

### Knowledge-base entries to use
- **Invariants & monovariants** (line 117 / 191) — for the co-varying descent, but only with the
  tie carve-out (a clean global monovariant does NOT exist here, per the tie-slice flatness).
- **Piecewise-concavity smoothing** (lines 20–32) — relevant in spirit to route (b) but **do not
  rely on it**: f is non-concave (R2) and route (b) = dead GAP-IMR.
- **Standard inequalities / extremal equality cases** (line 33) — the tie family is the equality case.

### Analogous past problems (cruxes)
- `aimo-0117` (games-and-strategy, "largest value exceeds sum of all others") — the ladder L's
  dominance `2^{n−i} > Σ_{i'>i} 2^{n−i'}` underlies the tie-family carve-out; banked, round-1 rule.
  Relevant to the tie-handling half of route (a), not the descent half.
- No corpus crux matches the *co-varying* deformation directly; the monovariant family is refuted
  in its pointwise form, so a borrowed monovariant crux would mislead. Do not force one.

### Prior progress (this lens's gap)
- GAP-P1′-b is OPEN. The pointwise π_0-fixed monovariant on I_n is FALSE (R11, ~30% increase adding
  a cut to F'). No correct monotone-in-b argument exists. The base case b=0 is itself still open
  (GAP-P1′-a), so even a perfect reduction is not yet useful standalone.

### Dead ends (do not retry)
- **"b=0 is the strict/unique worst case" / "slice-max strictly decreasing in b"** — REFUTED here:
  ties I_n=0 at every b<n (n=3,4 full enumeration). The §10.7 slice-maxima are undersampled.
- **Pointwise π_0-FIXED per-cut monovariant on I_n** — REFUTED R11 (~30% violations, all n).
- **Vertex/LP extremal argument (route b)** — = the DEAD GAP-IMR integer-minimizer framing (R10),
  blocked by hard sums Σπ_j=2^{n−j}. Not distinct; do not seed.
- **Naive "merge F' toward L" with π_0 held fixed** — merging can RAISE D̃ (`{4,2,½,½}`: 2→3,
  run_state), so an un-coupled merge is not D̃-monotone; the merge MUST be coupled to a π_0 split.
- **Scalar b-cutoff / φ(b) pruning** — DEAD R11 (ties at b=2,3; b has no separating power).

### Small-case / intuition notes (labeled conjecture)
- **CONJECTURE (strong, n=3,4 exact):** min D̃ = 1 on every slice b=0,…,n−1, and =2^n−(something)>1
  only at b=n (Case A). I.e. the tie set spans all sub-Case-A slices. This is the real reason the
  slice framing gives no leverage.
- **CONJECTURE (route a, n=4 exact):** every non-tie config (D̃>1) admits a budget-preserving
  coupled (merge-in-F' + split-π_0) move that does not increase D̃; the only single-step
  obstructions are exact-tie (D̃=1) configs. If confirmed at larger n and the tie family is
  carved out, route (a) is a genuine descent to b=0 — the one live opening from this lens.
- **Meta-recommendation for the outliner:** because the slice-max is flat across b, `b` is the
  WRONG induction/reduction variable; `n` (the peel) is right. GAP-P1′-b as a "reduce to the
  extremal slice" is largely a mirage — either (i) pursue route (a)'s co-varying descent WITH an
  explicit tie carve-out, or (ii) drop the slice framing and fold b=0 back into the pure n-peel
  induction (GAP-P1 / loaded IH), treating b=0 only as a self-contained sanity anchor, not as a
  reduction target that buys slack.
