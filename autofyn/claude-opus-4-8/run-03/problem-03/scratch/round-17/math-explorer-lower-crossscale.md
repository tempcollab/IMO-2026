## imo-2026-03 — LOWER wall, CROSS-SCALE lens (R17)

### The exact cross-scale target (restated) and why scale-local levers collapse
Certified chain: Lemma MID (`D(S)=μ{g odd}`, `∫g=1`, `g=N_F−N_B` on `(0,2^{n-1})`) + Lemma CLIP
(τ=0 face `∫φ(g)=D(S)−1`, `φ(c)=1[c odd]−c`) + R16's own further reduction give the residual as
the **cross-scale inequality on the VALUE (g-level) side**:
```
Σ_{i≥1} μ{g ≥ 2i}  ≤  Σ_{i≥1} μ{g ≤ 1−2i}          (★)
```
(equivalent to `D(S)≥1`, via `D=1−2∫⌊g/2⌋` and the standard layer-cake split of `⌊g/2⌋`). Every
prior scale-local lever (9 dead: scalar-reserve/potential, transport/matching, prefix monovariant,
f-partition single-gap localisation, LP-dual/vertex-polytope, transform/generating-function,
merge-domination, split-average, per-DOMAIN-dyadic-band parity counting) attacked either (a) a
running/single-pass scalar in **time/domain order**, or (b) a **fixed-scale (in t) decomposition**
of the domain `(0,2^{n-1})` into dyadic sub-intervals `I_k=(2^{k-1},2^k)`. R16 showed the
domain-scale-local target `∫_{I_k}⌊g/2⌋ ≤ 0` is FALSE per band (top band positive on the
`F={12/5,14/5,14/5},B={1,2,2,2}` witness) — cancellation is cross-DOMAIN-band. (★) is a
different axis: it slices by the **value of g** (a level-set/layer-cake decomposition over the
WHOLE domain at once), not by position in `(0,L)`. This is confirmed genuinely distinct below.

### Distinct openings surfaced
1. **(i) Layer-cake / co-area value-side pairing.** Treat (★) itself as the object: pair the
   super-level measures `μ{g≥2i}` against the sub-level measures `μ{g≤1−2i}` via a per-level
   (in *g-value*, not domain-position) accounting that uses `∫g=1` and the dyadic-realizability
   of each level set (each `{g≥2i}` / `{g≤1-2i}` is provably a union of intervals compatible with
   BLK's finite-value-count and ONE-REC's per-scale-≤1-excess structure — a genuinely different
   slicing axis than R16's dead per-domain-band count).
2. **(ii) Symmetric-function/rearrangement on the multiset of block heights.** Treat the finite
   multiset of `(length_k, g_k)` pairs over maximal constant-`g` blocks (≤ n+2 distinct positive
   values per BLK) as a rearrangement/Chebyshev-sum target: is there a provable anti-correlation
   between block length and `|g_k|` (finer cuts needed for larger cancellation) that a
   majorization/SOS inequality could exploit treating all scales simultaneously? (Not gated
   numerically this round beyond a qualitative check — flagged as untested, see below.)
3. **(iii, NEW synthesis, not in the original two-direction list) Value-layer-cake × ONE-REC
   domain-scale product.** Combine (i)'s value-side slicing with the certified ONE-REC per-scale
   mass identity (`ΣG_j=2^j` for the tail piece originating at dyadic scale `j`, ≤1 excess
   fragment per scale): index each block not just by its `g`-level but by its **dyadic scale of
   origin** `j` (which ladder piece `2^j` it fragments). This gives a natural analogue of the
   aimo-0009 "self-referential index" `a_{a_i}` — the scale-of-origin plays the role of a second,
   structurally-determined index (not a free running scan), letting a per-(level, scale) cell
   bound sum to a fixed total exactly as in aimo-0009's `a_i+b_i≤n` pairing. This is the most
   promising untried combination — genuinely uses BOTH certified structural lemmas (BLK/ONE-REC)
   at once, which no dead lever did (each dead lever used at most one).

### WTC lower-analogue — re-confirmed DEAD (do not re-propose)
Re-verified the R16 explorer's algebraic argument (not just trusted it): WTC's `descKK` is
Karmarkar–Karp differencing in a FIXED order; `D(S)` is the alternating sum of the SORTED
descending merge. They coincide only in the single-dominant-element regime, which is exactly
where the (already-certified, already-insufficient) Lemma PEEL already applies as an *equality*
(`D(S)=f₁−D(S∖{f₁})`), strictly stronger than any WTC-style two-sided bracket could give. No
lower companion to WTC exists beyond what PEEL already supplies. **Confirmed dead — do not
re-propose "import WTC to the lower wall."**

### Cheap-kill / gate probes RUN (exact Fraction arithmetic, n=4,5,6)

**Gate 1 — global target (★) itself, sanity check.** Generated 900 random budget-respecting
`a=0` refinements (F = random partition of `2^n` into 3–6 fragments each `≤2^{n-1}`; B = random
refinement of the tail ladder `C_{n-1}` using the remaining cut budget), computed `g` exactly via
breakpoints, evaluated both sides of (★) for levels `i=1..6`.
**Result: 0 failures / 900 trials** (expected — (★) is exactly certified MID-core, already true).
Worst margin `RHS−LHS ≈ 0.0093` at `n=4` (near-tight, consistent with tight `D→1` configurations).

**Gate 2 — TERMWISE (per-level `i`) claim `μ{g≥2i} ≤ μ{g≤1−2i}` for EACH `i` separately.** This
is the natural "lazy" reduction of (★) to a scale-local (in g-VALUE) statement — if it held
termwise, (★) would follow trivially with no cross-scale content, meaning direction (i) would be
a repackaging, not new content. Ran 6000 (config, level) pairs across n=4,5,6.
**Result: 5 / 6000 FAILURES (0.08%), always at `i=1`** (e.g. n=4, `F={7.586,0.932,7.482},
B={1,2,4,4.241,0.844,2.915}` (scaled): `μ{g≥2}=3.241 > μ{g≤−1}=2.915`). **This is a decisive,
useful negative-and-positive result**: it PROVES the termwise reduction is false in general (so
(★) genuinely needs cross-level cancellation — confirming the dispatch's framing is right, not a
disguised triviality) while showing failures are rare and confined to `i=1`, meaning most of the
inequality's slack comes from `i≥2` compensating a small `i=1` deficit — a concrete quantitative
target for whichever mechanism (i)/(iii) the outliner builds ("the `i=1` band can run a small
deficit that is repaid by higher bands," i.e. genuinely cross-scale, not per-band-nonneg).

**Gate for (ii) (rearrangement/symmetric-function):** not run to a decisive numeric gate this
round — flagged as UNTESTED, lower priority; would need a concrete conjectural inequality (e.g.
Chebyshev sum on sorted `(length_k,|g_k|)`) before a cheap-Fraction gate is meaningful. Do not
build (ii) without first formulating and gating a specific conjectural inequality.

### Knowledge-base entries to use
- Fubini / layer-cake identity (already imported, underlies Lemma MID(b) and CLIP) — the natural
  tool for (★) itself.
- LP vertex fundamental theorem (already imported via VERT-LOW) — underlies BLK's finite-value
  structure that (iii) would need.
- No `knowledge_base.md` entry beyond these appears specific to level-set/co-area pairing or
  rearrangement/majorization; the KB's generic entries (symmetric functions, Newton's identities)
  are algebraic identity tools, not directly load-bearing here.

### Analogous past problems (cruxes) — genuine find this round
Searched `combinatorics`+`algebra`, subtopics `double-counting`, `size-bounding-and-descent`,
`inequalities-SOS-and-convexity`, `sequences-and-recurrences` for "tail-count"/"threshold"/
"level"/"pairing" techniques.
- **aimo-0127** (`double-counting`, "IMO-style" alternating min/max weighted-tree game) — crux:
  *"Rewrite a weighted total as a sum over weight thresholds of tail-counts (# items of weight ≥
  the threshold), so a per-threshold cap can be applied termwise."* This IS the layer-cake
  identity used exactly as direction (i)/(★) would need it (`ΣW = Σ_i a_i`, `a_i` = tail-count at
  level `i`, capped `a_i ≤ min(k,n−i)` from an independent structural bound, then the sum
  telescopes to the exact target). Directly analogous in FORM to (★): it shows the pattern
  "level-indexed tail-count sum, each capped by a *structural* (not scalar-scan) bound, summing
  exactly to the fixed total" is a real, provable pattern elsewhere — the missing ingredient here
  is finding OUR analogue of their per-level cap `a_i ≤ min(k, n−i)` (which came from a disjoint
  window/acyclicity argument, i.e. a genuinely combinatorial structural bound, not a potential).
- **aimo-0009** (IMO 2018-ish, `size-bounding-and-descent`+`double-counting`, sequence sum bound
  `Σa_i ≤ n²`) — crux: *"count the large excess by level: for each level count how many terms
  exceed it, and pair that per-level count against a matching small term so the two cancel to a
  fixed constant"* — concretely `a_i + b_i ≤ n` for `i≤t`, where `b_i` is itself a TAIL-COUNT at a
  SHIFTED level, and the shift/cap comes from a **self-referential** structural constraint
  (`a_{a_i} ≤ n+i−1`, the sequence indexing itself). This is the strongest structural analogue
  found: the "index-into-itself" self-referential coupling is exactly the flavor direction (iii)
  above proposes (scale-of-origin `j` acting as a second structurally-determined index, playing
  the role of `a_i` inside `a_{a_i}`), rather than a free-running scalar scan (the dead family).
  **Recommend the outliner read aimo-0009's finisher crux closely as a template for HOW to build
  a per-level cap from a structural (not potential) constraint** — but note every step must still
  be reproved from scratch for our `g`/BLK/ONE-REC objects; it is a hint, not a citation.
- Nothing else in `games-and-strategy`/`invariants-and-monovariants`/`coloring-and-parity` matched
  beyond generic same-subtopic parity games (aimo-0013/14/41/46/64/70/74/80/91/105/114 etc.) —
  same surface theme (parity, dyadic, level counts) but none combine tail-count-pairing with a
  self-referential structural cap the way aimo-0009 does; aimo-0127 and aimo-0009 are the two
  genuine matches.

### Prior progress
`results/imo-2026-03/current.md`: LOWER wall `partial`, NO live vehicle, 9 dead levers (per
dispatch). Certified lemmas MID, CLIP, BLK, ONE-REC, VERT-LOW all stand and are the substrate for
directions (i)/(iii) above. UPPER wall (breakpoint-vertex) is the separate live leader, untouched
by this lens.

### Dead ends (do not retry)
- All 9 dispatch-listed dead levers (scalar-reserve/potential, structured transport/matching,
  prefix/termwise monovariant, f-partition single-gap localisation, LP-dual/vertex-polytope/Farkas,
  generating-function/transform/roots-of-unity, merge/budget-domination, split-average, and R16's
  scale-local/per-DOMAIN-dyadic-band parity-counting).
- **WTC-lower-analogue**: re-confirmed dead this round (algebraic re-derivation, not just
  citation) — descKK ≠ D(S)'s alternating-merge functional except in the single-dominant regime
  already closed by certified equality-strength Lemma PEEL.
- **Termwise (per-g-level) reduction of (★)**: numerically REFUTED (5/6000 fails, all at i=1) —
  confirms (★) is genuinely cross-scale/cross-level, not a disguised per-level triviality; do not
  attempt to prove (★) via a per-i inequality alone (any real proof must let higher levels repay a
  possible i=1 deficit).

### Small-case / intuition notes (conjecture, not proof)
- The i=1 level is the only one that can run a deficit (5/6000 adversarial hits, always i=1) —
  suggests the "hard part" of (★) is entirely concentrated at the coarsest level (`g≥2` vs
  `g≤−1`), with all `i≥2` levels safely nonneg-contributing in every sampled case. If this
  concentration is provable in general (untested further this round), the target could reduce
  to a MUCH narrower two-level statement `μ{g≥2}−μ{g≤−1} ≤ Σ_{i≥2}(μ{g≤1−2i}−μ{g≥2i})`, i.e. deep
  levels always have surplus that can be "lent" to level 1 — a genuinely new, narrower conjecture
  worth a dedicated cheap-kill next round if the outliner wants a concrete sub-target.
- The layer-cake slicing (value-of-g axis) and R16's domain-band slicing (position-in-t axis) are
  provably NOT the same object (confirmed by the n=3 witness giving termwise-true here vs
  band-false there) — direction (i)/(iii) is a genuinely unexplored axis, not a repackaging.

### Ranked shortlist for the outliner (≤2 live cross-scale directions)
1. **(iii) Value-layer-cake × ONE-REC scale-of-origin synthesis** [PRIORITY]. Make-or-break:
   build a per-(g-level `i`, dyadic-origin-scale `j`) cell bound analogous to aimo-0009's
   `a_i+b_i≤n`, using BLK's finite-value bound + ONE-REC's `ΣG_j=2^j` per-scale mass identity as
   the *structural* (non-scalar, non-running) cap, summing to `∫g=1`. Gate result: (★) itself
   confirmed true/tight (0/900 fails, margin→0); termwise reduction REFUTED (rules out a lazy
   version, so real cross-scale content must be built) — the direction survives its own gates and
   is genuinely untried in this exact combined form.
2. **(i) Plain layer-cake/co-area pairing on (★)** (without the ONE-REC scale-of-origin index) —
   fallback if (iii)'s self-referential structure can't be found; same gates as above apply
   (termwise version refuted, aggregate confirmed true/tight). Weaker than (iii) because it lacks
   a concrete mechanism for WHY level-1 deficits get repaid by deeper levels — (iii) supplies a
   candidate mechanism (scale-of-origin indexing), (i) alone does not.

(ii) (rearrangement/symmetric-function on block-height multiset) is NOT included in the shortlist
— no concrete conjectural inequality was formulated or gated this round; flag it as a reserve idea
only if both (i)/(iii) stall, and insist any builder first state and gate a specific inequality
before writing proof text.
