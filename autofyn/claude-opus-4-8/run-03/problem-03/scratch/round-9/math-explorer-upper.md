## imo-2026-03 — LENS: restricted-discrepancy / Subset-KK ratio bound (upper wall)

### Where the wall actually sits (verified against current files)
`breakpoint-vertex.md` R8 has reduced Prop UV (upper bound in the balanced valley
`a1<L/2, a2<β_nL`) via certified Reduction R-UV + Lemma RL/ESF-1/ESF-2 to one crisp
residual:

> **Subset-KK claim.** For every full-budget valley profile `A={a1≥...≥a_{n+1}}`
> (sum L) there is a nonempty subset `T` whose *descending-KK caterpillar value*
> (`v1=t1, v_j=|v_{j-1}-t_j|` in descending order over T) is `≤ u_nL = L/(2^{n+1}-1)`.

This is now a genuine **restricted discrepancy** problem: minimize over subsets T
(not the whole ground set) the descending-KK value, where "descending-KK" already
includes the abs-flip (two-sided), and the only remaining freedom is *which subset*.
Full-support descending KK (no skipping) is REFUTED (214/516 valley profiles exceed
u_nL, worst ratio 7.5×) — skipping (DELETE) is provably essential (Lemma RL/VS).
The one-sided "subtract from a1 only" family (ESF-1) is REFUTED by an explicit
rational n=2 witness `{9/20,7/25,27/100}`: ESF-1 floor 17/100 > u_2=1/7, while the
abs-flip pair `{a2,a3}` gives 1/100 ≤ u_2. So genuinely two-sided caterpillars over
a *chosen* subset are required, and no deterministic single-pass greedy policy works
(greedy-include-if-shrinking degenerates to full-support KK on non-skippable
instances, which is already refuted).

### Distinct viable openings for the Subset-KK claim
1. **Scale-recursion / peel-the-top-scale reduction (most promising).** Since the
   target profile is *close to* the extremal dyadic ladder `2^n,...,2,1` (scaled),
   try: peel off `a1` and recurse on the residual `n`-piece profile `{a2,...,a_{n+1}}`
   (sum `L-a1 > L/2`), which is itself a "smaller" instance — NOT literally an
   `(n-1)`-valley profile (Lemma VS already proves no *single*-move recursion admits
   an IH(n-1) certificate — this is why the naive DELETE/MATCH recursion fails), but
   a two-step compound move might: bisect the gap `a1` against a constructed subset
   sum `Σ_{i∈T} ai` chosen to land in the *next* dyadic scale band `(2^{n-2},2^{n-1}]`
   relative to `a1`, then recurse the *residual* (not `a1` itself) against the
   remaining pieces at the next scale down. This is a genuine ratio-target
   reformulation of Karmarkar-Karp differencing, not the raw KK statement — flag
   this as the top candidate to hand the builder, but it is NOT written out as a
   proof strategy here (still a scouted opening only).
2. **Complement/drop-one family + pigeonhole.** Instead of ESF-1 (drop only
   non-top elements) or full ESF-2 (drop nothing), consider the `n+1` subfamilies
   `T = A \ {a_i}` (drop exactly one element, any element not just non-top) and run
   descending-KK on each. This is a genuinely different subset family from what R8
   tried (ESF-1 anchors at a1 and only skips small elements toward a1; this drops
   one arbitrary element and keeps full-support KK on the rest). Worth a quick
   numerical check by the builder before committing — untested in the current
   record.
3. **Continued-fraction / Euclidean-algorithm framing.** The abs-flip caterpillar
   value on a descending sequence is structurally the same recursive step as the
   subtractive Euclidean algorithm (`v_j = |v_{j-1}-t_j|`). Reformulating the
   Subset-KK claim as "does a Euclidean-type reduction of the multiset against a
   dyadic modulus stay below `u_nL`" may connect to known bounds on the number of
   steps / remainder sizes in the subtractive Euclidean algorithm, and might yield
   a cleaner monovariant than raw case-splitting. Flag only — not developed.
4. **Direct LP/vertex specialization of Prop UV to Subset-KK.** Theorem VERT
   (already certified) says an optimal Xiang refinement lives at a polytope vertex
   with ≤ n+1 distinct values; combined with Lemma RL (only tree-realizable signed
   sums are reachable) one could try to characterize the extremal *valley* vertex
   profiles directly (not just the dyadic ladder) and show Subset-KK is tight
   exactly there — turning the general claim into finitely many boundary checks per
   n via VERT, mirroring how Lemma TB reduced the lower bound. This has NOT been
   tried for the upper valley (VERT was used for the lower bound machinery in §4A,
   not yet pushed into 4B beyond the reduction chain).

### aimo-0796 status (explicit check)
Confirmed by reading `past_problems_database.json`: aimo-0796 (IMO Iran problem,
"repeated smallest-gap-partition + increment" process) proves via induction
exactly the greedy append-to-smaller-side lemma: `|xi|<a for all i ⇒ ∃ partition
with |ΣI−ΣJ|<a`. This is EXACTLY the mechanism realized by ESF-1 (subtract toward
a1) and by the "greedy-subset-sum-toward-a1" route the field already ruled out.
The bound it gives is `< max|xi| = a1 < L/2`, i.e. ratio `a1/u_nL` up to
`β_n/u_n ≈ 2^{n-1}` off — confirmed by breakpoint-vertex's own accounting. A
"ratio-target reformulation" does NOT trivially fix this factor: the aimo-0796
lemma is genuinely a *one-sided* single-direction append (always add the new
element to the currently-smaller side), which is provably weaker than the
two-sided abs-flip family (ESF-2) already in use — so aimo-0796's technique alone
is a dead end for the ratio target; it can at best serve as a base-case building
block inside a scale-recursive argument (opening 1), not as the whole mechanism.

### DM-tree-achievable subset family / factor-2 deficit
Lemma RL rigorously proves `R(A)` (tree-realizable subset signed sums) is a
**strict** subset of all `{0,±1}` combinations — only differences, never sums of
two positive pieces, are reachable (machine-checked `m≤5`: `|R|=8<13` possible
`{0,±1}` patterns for `m=3`). This confirms the assigned lens's "factor-2
achievability deficit": a naive `2^{n+1}`-pattern pigeonhole argument is invalid
and cannot be salvaged by a counting trick alone — any correct argument must work
inside the tree-realizable family (ESF-2 already gives the full descending-KK
caterpillar family, which is proven to be a *subfamily* of tree-realizable values,
not the whole set — so there could in principle be even richer realizable
subfamilies beyond caterpillars, e.g. full binary trees of depth >1, that are not
yet exploited). **Open structural question, not yet explored by any approach**:
whether general (non-caterpillar) tree shapes over subsets give strictly more
reachable values than descending-KK caterpillars, and whether that extra room is
needed to close Subset-KK — worth a quick numeric probe by the builder.

### Cheap-kill candidates
- None found that dispatch Subset-KK outright. But a **useful cheap structural
  check** before heavy casework: verify (numerically, then structurally) whether
  restricting to *drop-one* subsets (opening 2 above) already suffices — this is
  a single, cheap family to rule in/out before the full scale-recursion machinery.
- Parity/size check: since `|T|` can range from 1 to `n+1` and the target ratio
  `u_n/L` shrinks like `2^{-n}`, a pure counting/pigeonhole over the `2^{n+1}`
  sign patterns is already proven insufficient (Lemma RL) — do not re-attempt a
  raw pigeonhole; any viable pigeonhole must be over the *tree-realizable* set,
  which is combinatorially subtler (no clean cardinality formula found yet).

### Knowledge-base entries
- No direct KK/discrepancy entry in `knowledge_base.md` (checked; only
  "Multiset partitions & power-sum matching (Prouhet–Tarry–Escott)" is tangential
  and not applicable — that's about matching power sums up to some order, not
  differencing/subset-sum discrepancy).
- Certified lemmas already in play and sufficient scaffolding for any of the four
  openings: `lemmas/leftover-realizability.md` (RL), `lemmas/valley-sharpness.md`
  (VS), `lemmas/subtraction-from-top-subfamily.md` (ESF-1),
  `lemmas/subset-caterpillar-subfamily.md` (ESF-2), `lemmas/elementary-reductions.md`
  (DM moves), `lemmas/cancelling-pair.md` (P), `lemmas/top-scale-dichotomy.md` (ONE).

### Analogous past problems (cruxes)
- **aimo-0796** (number_theory / induction-and-construction, but really a
  combinatorics-flavored process problem) — confirmed the exact technique already
  in use as ESF-1's ancestor; CONFIRMED insufficient for the ratio target (see
  above). Do not re-derive it as a fix; it is a documented dead end for the ratio
  bound specifically, though it may still supply a base-case building block.
- **aimo-0298** ("scale" / `D(x,y)=2^d` dyadic-gap problem) — already tried and
  REFUTED as `split-and-average` lever per current.md (round 7); confirmed here by
  reading the problem statement: it is about scale-multiplicity bounds in a set,
  not signed subset differencing, so its averaging mechanism genuinely does not
  transfer (independently corroborates the round-7 refutation).
- No crux in the corpus (filtered `combinatorics`/`number_theory` ×
  `pigeonhole`/`extremal-principle`/`processes-and-algorithms`/
  `size-bounding-and-descent`/`invariants-and-monovariants` × keywords
  `karmarkar`/`differencing`/`discrepancy`/`subset sum`/`scale`/`dyadic`/`binary
  representation`/`cascade`) resembles a genuine restricted (tree-only) signed
  subset-sum discrepancy problem with a ratio target. The closest hits
  (aimo-0796, aimo-0298) are both already flagged/refuted. **Verdict: no strong
  analogous crux exists** — this residual appears to be genuinely novel relative
  to the corpus, consistent with it being the hard core of an IMO-P3/P6-level
  problem.

### Prior progress
See `breakpoint-vertex.md` §4B.4 (round 8): Reduction UV', ESF-1, ESF-2 all
CERTIFIED-ready; Subset-KK claim stated cleanly and numerically confirmed on 387
valley profiles (worst ratio 0.31–0.74, i.e. comfortably true, never close to 1)
but with **no profile-independent proof**. This is the single sharpest form of the
upper wall across the whole field (shared with `subset-sum-pigeonhole` and
`smoothing-majorization` per current.md's own cross-references).

### Dead ends (do not retry)
- Naive `2^{n+1}`-subset `{0,±1}` pigeonhole (Lemma RL: invalid, strict subset).
- One-sided ESF-1 alone / greedy-subset-sum-toward-a1 (rigorous n=2 counterexample,
  ratio short by `2^{n-1}`).
- Full-support (no-DELETE) descending KK (machine-refuted, worst ratio 7.5×).
- Any single DELETE or single MATCH move + IH(n-1) certificate (Lemma VS: both
  thresholds `c(n)L`, `β_nL` fail exactly at the valley boundary).
- Deterministic single-pass greedy "include iff it shrinks the running value"
  (coincides with full-support KK once nothing is skippable ⇒ inherits the 7.5×
  refutation).
- `split-and-average` monovariant (aimo-0298 style) — refuted independently for
  D by the reviewer (round 7) and confirmed off-topic here.

### Small-case / intuition notes (conjecture, not proof)
- The extremal case is exactly the dyadic ladder scaled by `1/(2^{n+1}-1)`; there
  Subset-KK is tight (`=u_nL`) via the full descending cascade `2^n,2^{n-1},...,1`
  (no skipping needed) — this IS the equality case, consistent with the answer.
- Numeric evidence (387 profiles, n≤5) shows Subset-KK margin never approaches 1
  except at/near the dyadic extremal profile itself, suggesting the correct proof
  likely proceeds by a **continuity/perturbation-from-the-extremal-profile**
  argument or a genuine scale-recursion (opening 1) rather than a uniform
  worst-case combinatorial bound — i.e. the residual is "smooth," not adversarial,
  which favors an inductive/recursive construction over exhaustive casework.
