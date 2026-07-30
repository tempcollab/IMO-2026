## imo-2026-03 — LOWER-wall lens (routes A: WTC-analogue, B: direct integrality accounting)

### Setup recap
GAP MID-core (certified Lemma MID): with `g = N_F − N_B` on `(0, 2^{n-1})`, `∫g = 1`, prove
`μ{g odd} ≥ 1` for `|F| ≥ 3`. Equivalently (certified VERT-LOW+BLK) GAP-EXTR: min alternating
value `L_T ≥ 1` at every vertex of the interleave-word polytope. Also equivalently, in
`induction-peel`'s framing, this is **GAP L2 = {critical band of (L⋆), width exactly
`w ∈ (2^{n-1}-1, 2^{n-1})`} ∪ {Case II, `|F|≥3`}** — the "Gap-Interleaving exchange step." All
three approach files (merge-interleave, induction-peel, parity-measure-potential) converge on
this ONE residual under different names — confirming (again) it is a single shared wall, not
three.

### Route (A): WTC-analogue for the lower wall — VERDICT: not a new lever, collapses to already-certified (and insufficient) machinery

**Test performed (worked out by hand, not numerically — this is an algebraic fact, cheap to
check).** WTC's `descKK` is the *Karmarkar–Karp differencing* recursion `v_k = |v_{k-1} − a_k|`
applied to a sequence in a FIXED given order. `D(S)` (the lower-wall quantity) is instead the
*alternating sum* `Σ(−1)^{i+1}b_i` of the SORTED descending merge — a different functional in
general. Concretely, on `(10,1,1)`: `descKK = |{|10-1|-1}| = 8`, but the alternating sum
`10-1+1 = 10`. They diverge whenever `v_{k-1} ≥ a_k` for several consecutive steps (descKK keeps
subtracting, effectively giving *all* later terms a `−` sign, not an alternating one) — i.e.
descKK and the alternating sum coincide only in the "one term dominates the rest" regime, exactly
where WTC is already tight (`a₁ ≥ L/2` branch, = certified `whole-tail-peel`).

Worse: for `D(S)` itself, the **exact** peeling identity is already certified and is *strictly
stronger* than anything WTC's two-sided bracket could give: **Lemma PEEL**
(`strict-max-peel.md`, used verbatim in `induction-peel.md` §3): for a unique max `f₁`,
`D(S) = f₁ − D(S∖{f₁})` — an EQUALITY, not an inequality. WTC's `a₁ − P_k ≤ v_k ≤ |a₁ − P_k|` is a
two-sided *inequality* bracket for a *different, weaker-information* recursion; importing it to
bound `D` directly would at best re-derive a weaker form of PEEL, which is already known to be
insufficient — PEEL is exactly what reduces Case (I) to `(L⋆): D(S') ≤ f₁ − 1`, and that reduction
is *already done*; the open residual is precisely the regime where PEEL/WTC-type single-dominant-
term reasoning is powerless (`|F| ≥ 3`, no unique dominant piece, "critical band" width exactly
`1` in `w`). WTC itself is explicitly vacuous in the structurally analogous UPPER-wall deep
interior for the same reason (`|2a₁−L| > u_nL` when no piece dominates).

**Conclusion:** the two open walls fail for the *same structural reason* — absence of a single
dominant element to peel/differences against — and WTC is a single-dominant-element tool. There is
no "lower companion" to extract: the lower side of WTC's own bracket (`a₁ − P_k ≤ v_k`) already
*is* exploited (it's the equality branch, = whole-tail-peel/PEEL). Route (A) is a dead-on-arrival
reframing of already-certified (and already-insufficient) machinery, not a genuinely new lever.
Do not re-propose "import WTC to the lower wall" as a distinct approach; if anything is salvaged,
it is the observation above (both walls collapse to the identical no-dominant-element residual),
which the outliner should use to justify unifying the two open gaps as literally the same
research target (a `|F|≥3` / balanced-regime aggregate cancellation bound), not to re-attempt
peeling.

### Route (B): direct integrality/parity accounting on g — VERDICT: correct target, but the "new" lever must avoid re-deriving the 8 dead objects

Confirmed (from Lemma MID's own text and `parity-measure-potential`/R9 ONE-REC record): the
**pure**-integral claim "`g` integer, `∫g=1` ⇒ `μ{g odd}≥1`" is FALSE in general (witness: `g≡2`
on half the domain, `0` elsewhere, suitably scaled — an even-valued plateau contributes `0` to
`μ{g odd}` while carrying nonzero mass). So *some* extra structural input from the dyadic
ladder is unavoidable — already known, already the stated open direction since R7/R9. The
question for this lens is only: **is there an accounting mechanism that uses this structure
without being one of the 8 dead objects** (potential/reserve, matching, prefix monovariant,
f-partition localisation, LP-dual, transform, merge-domination, split-average)?

Candidates surveyed, with verdicts:
1. **Level-set / total-variation accounting.** Since `g` changes by exactly `±1` at every
   breakpoint (down at each F-value, up at each B-value — this is literally restating `N_S=N_F+N_B`,
   the content of Lemma MID(a)), the walk's *parity* at time `t` is determined purely by the
   *count* of breakpoints crossed so far (mod 2) — which is exactly `N_S(t) mod 2`. Any attempt to
   track this walk termwise (in breakpoint order) IS the "prefix/termwise monovariant on the
   signed walk" — explicitly the 3rd dead lever. So a level-set argument that processes
   breakpoints in TIME order is not new; it must process them in some OTHER order (e.g. by
   dyadic scale, not by position) to be distinct.
2. **Scale-by-scale (ONE-REC) accounting, not a running scalar.** Certified Lemma ONE-REC gives,
   for every truncation level `ℓ`, that `B_{≤ℓ}` is itself a bona fide refinement of `C_ℓ` with at
   most one excess fragment per scale. This is *structural*, not a scalar reserve — but every
   attempt to turn it into a proof so far (parity-measure's `ρ_k` cumulative surplus, R9;
   merge-interleave's "dyadic-scale induction on the vertex," flagged but undes-risked at R14) has
   either been refuted (ρ_k) or not actually attempted (the merge-interleave flag is only a name,
   no mechanism was built). **This is the one candidate NOT yet ruled out** — but note it was
   *proposed* twice (R9, R14) without ever being carried through with a concrete non-scalar
   mechanism; if attempted again it must explicitly avoid degenerating into (i) a running-scalar
   potential (dead #1) or (ii) an LP/vertex enumeration by scale (which is just VERT-LOW/BLK
   again, dead #5 in disguise).
3. **A genuine self-similar reduction: MID-core(n) ⟹ instance of MID-core(n−1).** Distinct from
   merge/budget-domination (dead #7, which merges *within* F and was refuted both empirically —
   9–15% failure — and structurally — the merged fragment generically lands back in Case I, the
   *other* open gap). An alternative surgery: instead of merging two F-fragments, **peel off the
   *bottom* dyadic scale of `B`** (the piece(s) of size `~1`, i.e. `G_0` in ONE-REC's notation) and
   ask whether `(F, B_{≤n-2})` — treating `G_{n-1}` (the piece(s) near `2^{n-1}`) as absorbed into a
   redefined "top" — is a genuine `(n−1)`-instance. This is NOT literally the same surgery as
   merge-interleave's dead LP-dual/vertex-polytope framing (which fixes `n` and enumerates
   vertices) nor induction-peel's dead merge (which combines two F-pieces). It has not been tried
   under this exact form and is worth flagging to the outliner as a genuinely distinct structural
   induction, though its outcome (does the surgery preserve `D`, or introduce an uncontrolled
   cross-term analogous to SPLIT's `μ(O_F∩O_B)`?) is unknown and would need to be checked as a
   MANDATED cheap-kill before investing further (test: does `D(S) − D(bottom-peeled S)` have a
   clean formula? almost certainly it reduces, via Lemma SPLIT, to the SAME cross term
   `μ(O_F∩O_B)` that MID was built to eliminate — so this is at HIGH risk of being dead lever (7)
   or (2) wearing a different scale).

**Honest assessment of (B):** the correct target is right (needs the dyadic ladder, confirmed
false without it), but essentially every concrete mechanism anyone has proposed under this
umbrella (scalar reserve, structured matching, LP-dual, merge, split-average, transform) is
already dead. The one line not yet actually attempted with a worked mechanism is **candidate 2**
(ONE-REC as a genuinely non-scalar per-scale STRUCTURAL constraint feeding a vertex/block-count
argument on the ALREADY-CERTIFIED Lemma BLK's "≤ n+2 distinct positive values at a vertex" —
i.e., use BLK's finite value-count directly with a counting/pigeonhole argument on how many of
those ≤ n+2 distinct dyadic-block values can be "unpaired" (contribute to `μ{g odd}` /oddness) —
rather than an LP/vertex ENUMERATION (dead #5) or a running potential (dead #1). This is subtly
different from both: it is a *counting bound* on the block structure itself (how many blocks can
have odd multiplicity given the dyadic group sums are fixed powers of 2), not a linear-algebra
vertex search and not a scalar carried forward move-by-move.

### Recommendation to the outliner
- Route (A) (WTC-analogue): **do not pursue as a standalone approach** — it either re-derives the
  already-certified, already-insufficient Lemma PEEL, or is vacuous in exactly the residual regime
  (no dominant element), mirroring WTC's own vacuity in the UPPER wall's deep interior. Worth
  keeping ONE sentence in the outline noting both walls' open residuals are the *same*
  no-dominant-element phenomenon (possibly worth a single unified approach attacking both walls at
  once via that observation), but not worth a dedicated slug.
- Route (B): the more promising terrain, but narrow it to the untried sub-lever — a **counting/
  pigeonhole bound on Lemma BLK's ≤ n+2 distinct dyadic-block values at a vertex** (how many
  blocks can have odd size given fixed dyadic group sums Σgroup_j = 2^j), explicitly NOT an LP
  vertex enumeration and NOT a running scalar. Flag the self-similar bottom-peel surgery
  (candidate 3) only as a secondary idea, with the explicit warning that it is at high risk of
  reproducing the dead SPLIT cross-term / merge-domination failure and MUST be gated by a cheap
  numerical check (does the peel introduce an uncontrolled cross-term?) before any proof effort.

### Cheap-kill candidates
- For candidate 2/BLK-counting: at a fixed vertex with ≤ n+2 distinct positive dyadic-block
  values, compute (numerically, small n) the parity/multiplicity pattern of blocks across all
  n=3,4,5 vertices already enumerated by merge-interleave's cheap-kill (LP solve) and check
  whether "number of odd-size blocks" or "position of the unique odd-total block" obeys a clean
  extractable inequality (e.g. is it always ≥1 and does the alternating value depend monotonically
  on it?) — reuse the existing n=3,4,5 vertex data rather than re-enumerating.
- For candidate 3 (bottom-peel self-similar surgery): before any proof writing, symbolically
  compute `D(S) − D(S with G_0 or G_{n-1} peeled)` on a few explicit F,B examples and check if it
  reduces to a clean small correction or reimports `μ(O_F∩O_B)`.

### Knowledge-base entries to use
No knowledge_base.md entry beyond what's already imported (Fubini/layer-cake, LP vertex
fundamental theorem, pigeonhole) appears newly relevant to this narrow lens; the load is carried
by the problem's own certified lemma stack (MID, ONE-REC, BLK, VERT-LOW, PEEL, WTC).

### Analogous past problems (cruxes)
- Searched combinatorics `coloring-and-parity` / `invariants-and-monovariants` /
  `extremal-principle` for "odd", "parity", "step function", "measure", "dyadic". The closest hit
  is **aimo-0019** (IMO 2013-ish "paintful game" / ink-pot covering game): crux move "bound a
  family of dyadic-length pieces of pairwise distinct sizes by twice the largest, via the
  geometric sum of distinct negative powers of two," backed by an **amortized linear potential**
  (ink spent on `[0,x_r] ≤ 3x_r`). This is thematically close (dyadic pieces, at-most-one-per-scale
  structure very like certified Lemma ONE/ONE-REC) but its closing mechanism is a running
  amortized potential/charging argument — i.e., exactly dead lever (1) (scalar-reserve/potential)
  in a different costume. It confirms rather than refutes the pattern: the "obvious" way to handle
  dyadic at-most-one-per-scale structure is a potential, and that route is already dead here.
  **Not a genuinely new mechanism to import**, but useful negative confirmation.
- No other corpus entry found that resembles "measure of an odd-level-set of an integer step
  function ≥ its integral" closely enough to be a genuine crux match; nothing else surfaced beyond
  generic dyadic/parity games (aimo-0013, aimo-0014, aimo-0041, aimo-0046) which are same-subtopic
  but not analogous in mechanism.

### Prior progress
See `results/imo-2026-03/current.md`. Both walls are open; the lower wall's residual (GAP MID-core
/ GAP-EXTR / GAP L2) is confirmed identical across all three live framings (parity-measure,
merge-interleave, induction-peel). 8 lower levers dead (listed in dispatch). 30 lemmas certified,
including the newest (WTC, round 15, upper wall only).

### Dead ends (do not retry)
All 8 listed in the dispatch, plus (per this lens's analysis) two additional non-viable framings
now identified:
- **WTC-style two-sided differencing bracket applied to `D(S)` directly** — either reduces to
  already-certified, already-insufficient Lemma PEEL, or is vacuous exactly where MID-core is
  open (no dominant element) — same failure mode as WTC's own upper-wall deep-interior gap.
- **aimo-0019-style amortized linear potential on the breakpoint scale** — same shape as dead
  lever (1) (scalar-reserve/potential); the corpus analogue's own mechanism is a potential, so it
  offers no escape from that already-refuted family.

### Small-case / intuition notes (conjecture, not proof)
- Both walls' open residuals structurally coincide in being "no single element/scale dominates"
  regimes — this is not new information but is reinforced by this lens's algebraic check of
  WTC vs. PEEL. Suggests the TRUE missing tool is fundamentally a *multi-scale simultaneous*
  argument (matching the dyadic ladder's self-similarity across ALL scales at once, e.g. via
  BLK's finite block-count), not a single-step peel/differencing/potential — consistent with why
  every single-mechanism attempt (8 of them) has failed identically.
