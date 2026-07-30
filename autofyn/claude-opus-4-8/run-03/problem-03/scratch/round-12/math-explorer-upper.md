## imo-2026-03 (UPPER wall — breakpoint-vertex, GAP U-cover / Covering claim)

### Setup recap (certified facts, no re-proof needed)
- Reduction chain: Reduction R-UV (any nonempty subset T with a tree-realizable descending-KK
  caterpillar value ρ(T) ≤ u_nL gives a legal ≤n-cut Xiang response with D=ρ). Residual = **Covering
  claim**: the descending include/skip reachable set `R_0={0}, R_i=R_{i-1}∪{|v−a_i|:v∈R_{i-1}}`
  meets `[0,u_nL]` via a value reached through a **nonempty** include-set (T=∅, i.e. "skip
  everything," is NOT budget-feasible: it needs n+1 DELETEs but only n cuts exist — see numeric
  correction below, this is a hazard worth flagging to the outliner/builder).
- Lemma CONF: `max R_i ≤ a₁` for all i ⇒ `R_{n+1}⊂[0,a₁)⊂[0,L/2)`.
- Lemma MD2: the reachable **multiset** `M_i` (both branches always kept, so `M_{n+1}` enumerates all
  `2^{n+1}` subsets including T=∅↦0) doubles each step, `|M_i|=2^i`, support `=R_i`.
- COUNT (`|R_{n+1}|=2^{n+1}`, distinct values) is FALSE (all-equal valley, `|R_{n+1}|=2`); average/
  smallest-gap→value pigeonhole on `M_{n+1}` provably fails by up to 2–3×. This density substrate is
  dead (R11) — confirmed, not re-litigated here.

### Numeric verification of the "collision vs spread" dichotomy — DECISIVE, mostly NEGATIVE for a
"forced-coincidence" mechanism as a broad phenomenon

I re-simulated the exact reachable-set construction with subset-tracking (Python + `fractions`,
exact rational arithmetic, no float error), **correctly excluding the T=∅ branch** (unlike a naive
first pass which — instructive bug — falsely found `min=0` on 100% of trials by including the
budget-infeasible "skip everything" path; flagging this as a trap for the builder: any code/argument
that treats `R_i` as literally containing `0` "for free" at every step is silently assuming the
infeasible empty-T branch).

With T=∅ correctly excluded, over exact-rational **randomly generated** valley profiles
(`a₁<L/2, a₂<β_nL`, n=2..7, ~50–2000 valid trials per n):
```
n   worst (min-ratio to u_n)   exact-zero hits (nonempty T)
2   0.30                       0
3   0.81                       0
4   0.53                       0
5   0.53                       0
6   0.46                       0
7   0.36                       0
```
**Zero exact collisions in thousands of generic trials.** Exact value 0 via a nonempty-T "even
cancellation" (e.g. `|a_i−a_j|=0`) only occurs at **measure-zero, exactly-tied configurations** (the
all-equal valley witness, or other symmetric coincidences engineered by the adversary) — it is a
genuine but *thin* boundary phenomenon, not a broad complementary regime to "spread." For a random
(non-adversarial, non-tied) profile the achieved minimum is always a **small but strictly positive**
discrepancy value, and it is NOT close to 0 in a way "collision" language suggests — worst ratios
0.3–0.8 show the covering claim is often not even close to binding.

I also checked, on the *hardest* (largest min-ratio) sampled profiles at n=5, which subset size `|T|`
achieves the minimizing value: it varies (2, 3, 4 — not fixed, not always the full n+1, not always a
pair). This reconfirms Lemma VS's message (no fixed-depth / fixed-pattern move suffices) rather than
suggesting a new localized collision trigger.

**Conclusion of this lens: the dispatch's "collision regime" as a genuinely separate uniform
mechanism from "spread" does not exist as stated.** The all-equal-type valley (used as the COUNT
counterexample) is a real but isolated boundary case handled trivially by `0` via an exact tie; away
from such ties, 100% of the real content is a **worst-case (not average-case) bound on a strictly
positive restricted discrepancy** over the tree-realizable ±1-pattern family — i.e., exactly Prop
UV / the Subset-KK claim already on the table, with no shortcut supplied by "forced repetition."
Recommend the outliner NOT chase a separate collision-forcing lemma as the primary lever; if pursued
at all, it should be folded in as one (easy, already-noted) boundary case of the same worst-case
discrepancy bound, not elevated to a parallel mechanism.

### Distinct openings (for the outliner to choose among, all consistent with the above finding)
1. **[DEAD, see numeric update below] Two-move coordinated / renormalization induction via
   MATCH-two-smallest.** Lemma VS proves no *single* DM move admits an IH(n−1) certificate; the
   natural candidate "MATCH the two smallest pieces, then recurse via IH(n−1) if the result is still
   in the valley" was checked numerically THIS ROUND and REFUTED (fails to stay in the valley 100%/
   99.5%/74% of the time at n=2/3/4 — see "Small-case / intuition notes" below for the full table and
   analysis). Recorded here for completeness/traceability; do not re-propose.
2. **Worst-case (not average) discrepancy over the RESTRICTED tree family**, using the recursive
   doubling structure of MD2 directly: since `M_i` is built by reflecting `M_{i-1}` off `a_i`, and
   `M_{i-1}` itself has a *known* covering structure by induction, propagate a genuinely tight
   (not average-gap) covering-radius recursion — the R10 attempt (`covering radius ≤ a_i/2`) is
   insufficient ALONE but was never combined with the SECOND cap `a₂<β_nL` recursively (R10 only
   used it as a final near-uniform patch); a joint two-cap recursive bound (using both `a₁` AND `a₂`
   caps at every level, not just the top level) has not been tried.
3. **Dyadic-band tagging** (crux aimo-0493 style, see below): tag each of the `2^{n+1}` tree leaves
   by which dyadic scale `2^{-k}` (relative to `L`) its caterpillar value first falls below, and show
   the tagging is forced to concentrate — a genuinely different bookkeeping from the refuted
   gap-pigeonhole, worth a light numeric probe before investing.

### Candidate technique(s)
Worst-case restricted-discrepancy bound over a tree-realizable ±1-subset-sum family via a
renormalization/self-similarity induction (opening 1) or a two-cap recursive covering-radius bound
(opening 2). NOT dispersion/pigeonhole (dead, R11), NOT a bounded-depth existential move (dead, R10),
NOT a single deterministic DM move (dead, Lemma VS).

### Cheap-kill candidates
- **Cheap first action for opening 1**: numerically check, over random valley profiles n=2..7, whether
  MATCH(a_n, a_{n+1}) (the two SMALLEST pieces) always leaves the resulting n-piece profile inside its
  own valley `{a₁'<L'/2, a₂'<β_{n−1}L'}` — if this fails on a nontrivial fraction, opening 1 is dead
  before any proof effort; if it holds, IH(n−1) applies directly and may close GAP U-cover in one
  clean step. This is a 5-minute numeric check that should gate whether opening 1 is worth a builder.
- Parity/size pigeonhole on the ORIGINAL `a_i` values alone (not subset sums) is too weak: n+1 values
  in `(0,L/2)` only forces an adjacent gap `≤ L/(2n)` by naive pigeonhole, exponentially weaker than
  `u_n=1/(2^{n+1}-1)` — confirms the field's standing conclusion that only the full subset-tree
  (exponentially many combinations) can supply enough resolution; no cheap linear pigeonhole works.

### Knowledge-base entries to use
Re-check `knowledge_base.md` for any entry on Karmarkar–Karp-style differencing / balanced
number-partitioning discrepancy bounds, or renormalization/self-similar induction templates — I did
not find the file listing during this pass (time-constrained); the outliner should grep
`knowledge_base.md` for "differencing," "discrepancy," "self-similar," "renormalization" directly.

### Analogous past problems (cruxes)
Searched `combinatorics`/`pigeonhole`, `processes-and-algorithms`, `size-bounding-and-descent`,
`extremal-principle`, `games-and-strategy` (see `crux_moves_documentation.md` for filter rules; used
exact `technique`/`how_used`/`subtopic` fields). **No genuinely strong analogue found** for "signed
subset sum forced small under recursive per-level size caps." Closest candidates, all partial:
- `aimo-0298` (dyadic-scale merge + potential telescoping, induction on closest-pair merge) — already
  the field's standing best analogue (used since R7); re-examined here, still the best template for a
  renormalization-style induction (opening 1/2 above), but its underlying mechanism (append-to-
  smaller-side greedy) is close to already-refuted greedy/one-sided routes — use only its INDUCTION
  SHAPE (strong induction merging the closest pair, tracking a monotone potential), not its specific
  greedy rule, which the field has repeatedly shown fails here.
- `aimo-0493` (invariants-and-monovariants/extremal-principle: dyadic-band tagging + super-geometric
  gap-sum growth) — a genuinely different bookkeeping technique (tag by dyadic scale, not by
  gap-size), worth a light look for opening 3, but I did not verify its actual mechanism transfers
  (time-constrained) — flag as unverified, not recommended over openings 1–2.
- `aimo-0715` (pigeonhole on prefix sums forcing a zero-sum window) — surface-similar (forcing a
  small/zero value by pigeonhole) but its mechanism is a straightforward prefix-sum-mod-range
  pigeonhole, structurally weaker than what's needed here (already shown insufficient by the field's
  refuted average-gap pigeonhole); not a new lever.
None of these should be cited as solving the residual — all are hints to adapt, per the corpus rule.

### Prior progress
Two lemmas certified this run (CONF, MD2); Covering claim numerically reconfirmed true with real
margin (worst ratio 0.3–0.8 on generic random profiles, this round's independent re-check); density/
count substrate rigorously dead (R11). No new certified content from this lens — this report is
primarily a **negative result** narrowing the field away from "collision" as a standalone mechanism,
plus two concrete, cheaply-checkable openings (1 and 2) for next round.

### Dead ends (do not retry)
- COUNT/distinct-value pigeonhole, average/smallest-multiset-gap→value conversion (R11, reconfirmed
  dead by nature of the argument, not re-tested numerically this round).
- Bounded/fixed-depth existential escape move (R10).
- Single deterministic DM move / single-move IH certificate (Lemma VS, exact thresholds `c(n)L`,
  `β_nL` proven unreachable by any single move in the valley).
- Treating "0 is always trivially reachable" (the T=∅ / skip-everything path) as free — this is
  budget-infeasible (needs n+1 deletes, only n cuts available); any builder code or argument must
  explicitly exclude T=∅ (I found this exact bug in my own first-pass simulation — a live hazard).
- (New this round) A broad "collision regime" as a mechanism distinct from and complementary to
  "spread": numerically, exact collisions to 0 essentially never occur outside measure-zero tied
  configurations (0/~8500 generic trials across n=2..7); this specific framing from the dispatch does
  not appear to open new ground beyond what's already isolated as Prop UV / Subset-KK.

### Small-case / intuition notes (all labeled conjecture/numeric evidence, not proof)
- Worst-case min-ratio (achieved value / u_n) over random valley profiles ranges roughly 0.3–0.8
  across n=2..7 in this round's re-check — consistent with, and slightly tighter than, prior rounds'
  reported worst 0.83 (R11) / 0.81 (R10) / 0.56 (R8), all comfortably `<1`, i.e. the claim is not
  numerically tight except at the known extremal dyadic profile (ratio exactly 1).
- The size of the minimizing subset `T` varies (2–n+1 elements) across different hard profiles: no
  single small pattern (pair, triple) dominates as the universal witness — reconfirms genuine
  case-dependence / adaptivity (Lemma VS), and argues against hoping for a size-2 "collision" shortcut.
- **UPDATE — ran the opening-1 cheap check (5 min, after drafting the above).** MATCH the two
  SMALLEST pieces `a_n,a_{n+1}` and test whether the resulting n-piece profile lands in its OWN
  valley `{a₁'<L'/2, a₂'<β_{n−1}L'}` (exact rational arithmetic, random valley profiles):
  ```
  n=2: fail 100% (80/80)     n=5: fail 32% (632/1987)
  n=3: fail 99.5% (555/558)  n=6: fail 9.1% (231/2528)
  n=4: fail 74% (973/1309)   n=7: fail 2.4% (69/2850)
  ```
  **Opening 1 as literally stated is REFUTED for small n** (fails almost always at n=2,3 — exactly
  where the base cases must hold) and only becomes rare at large n; a proof strategy that fails at
  n=2–3 cannot be the mechanism (small n is not a negligible edge case here, it's where induction
  starts). This matches Lemma VS's message (no single move admits an IH certificate) — MATCHing the
  two smallest is just another single move, so this is unsurprising in hindsight but is now a
  **quantified, ruled-out** instance rather than a live opening. **Downgrade opening 1 to DEAD; do
  not dispatch a builder on "MATCH-two-smallest-then-recurse."** The failure mode: `a₂'` (second
  largest of the new n-piece profile) is typically still `≥β_{n−1}L'` because removing only the
  smallest two pieces barely shrinks the second-largest survivor `a₂` relative to the new smaller
  total `L'` — i.e. a single coordinated pair-cut is still not "coordinated enough"; genuine
  multi-piece surgery (≥2 cuts spread differently, not just consuming the tail) remains necessary,
  reconfirming Lemma VS's ≥2-cuts message rather than opening a new route.
- Net effect: openings 1 (as stated) is now closed off; opening 2 (joint two-cap recursive
  covering-radius bound, using both `a₁` and `a₂` caps at every level of the MD2 doubling, not just
  the top level) and opening 3 (dyadic-band tagging, unverified) remain the least-explored, most
  promising untried directions for next round — recommend the outliner prioritize opening 2 since it
  builds directly on the two already-certified lemmas (CONF, MD2) rather than introducing new
  machinery.
