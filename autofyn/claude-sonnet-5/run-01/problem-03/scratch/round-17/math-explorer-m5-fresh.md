# Round 17 — math-explorer (lens: general m≥5, fresh framing)

## Task
Scout for a genuinely NEW mechanism for Case C (`p_1 < Σ(A)/2`) of Claim PTBI's
upper-bound induction, general `m≥5`, that does not rely on: (a) fixed-shape
top-level pair templates, (b) non-constructive scalar averaging/pigeonhole,
(c) Hall/König deficiency covering, (d) deterministic greedy scan-order
exchange arguments. **Verdict up front: no new mechanism was found that
clears the bar of "genuinely different, not a repackaging of an already-dead
line." One meta-level idea (below, "WLOG-reduce the adversary's config A via
smoothing," §3) is untested by any prior round and is worth a slug, but it is
a *direction*, not a worked-out technique — flag it to the outliner as a
candidate, not as ready machinery.**

## 1. Crux corpus search (read `crux_moves_documentation.md` first, then queried directly)

Queried `past_crux_moves_database.json` (2434 cruxes) by keyword and by
`subtopic` (`games-and-strategy`: 40 hits across number_theory/combinatorics;
`probabilistic-method`: 5 hits; plus keyword scans for `envy`, `cake`,
`fair division`, `duality`, `matching`, `charge`, `extreme point`,
`convexity`, `smoothing`, `majorization`, `rearrangement`).

**No cake-cutting / envy-free-division cruxes exist in the corpus** (0 hits
for `envy`, `cake`; the one `fair division` hit, `aimo-0106`, is an unrelated
"assume positive, construct the forbidden object" impossibility proof, not a
division mechanism). The corpus's `games-and-strategy` entries are
overwhelmingly **pairing/mirroring/involution strategies** (respond to move
`i` by playing a fixed partner of `i`) — structurally identical to the
already-dead "fixed-shape top-level pairs" and "deterministic greedy
scan-order" lines explicitly ruled out for this task.

Three subtler leads, checked and **all found to reduce to already-dead
lines**, not new ones:
- `aimo-0198` ("`min(A,B) ≤ (A+B)/2`, bound a greedy minimizer by averaging
  its two options") and `aimo-0956` ("set a mixing probability so the two
  weakest cases become equal") — both are **mixed-strategy / scalar-averaging
  arguments**, i.e. exactly the mechanism already killed twice in this run
  (`case-c-slack-covering`, RETHINK round 14, algebraic refutation for every
  `m≥4`; `minimax-mixed-duality`, RETHINK round 9, converged to the same
  discrete casework it was trying to avoid). No new leverage.
- `aimo-0146` ("exchange-smoothing weight toward the heaviest-weight
  entries", "charge each edge to its lower-degree endpoint") — a
  smoothing/charging argument for a *different* problem shape (a linear
  functional of a sorted degree sequence). Its charging idea is closer to
  Hall/König-style covering (already killed, round 15) than to anything new.
- `aimo-0656` ("a form linear in each variable over a box has its optimum at
  a corner") — this is the **vertex/extreme-point reduction principle**,
  which is *not* dead in this run (nothing has explicitly tried it as a
  general induction tool) but is also not a discrete "mechanism" by itself —
  see §3, where I use it as the seed of the one fresh idea I'm flagging.

**Conclusion of the corpus search:** every crux move that looked promising by
name collapses on inspection into (a) pairing/mirroring (dead: fixed-shape
template), (b) scalar mixed-strategy averaging (dead twice already), or (c)
Hall-style charging/covering (dead). The corpus does not contain a load-bearing
move from a genuinely different domain (LP duality over a continuum, cake
division, derandomization) that transfers here. This is a real negative
result, not a failure to search hard enough — I checked every subtopic
plausibly relevant (`games-and-strategy`, `probabilistic-method`,
`extremal-principle` overlap via `convexity`/`smoothing`/`rearrangement`
keyword scans) across all three domains.

## 2. Numerical experiments (m=4 sanity re-check, exact `Fraction`)

Before trusting any new numeric exploration, I re-implemented the certified
`m=4` 5-strategy menu (`V4 = min(StratA, StratB, StratC_12, StratC_13,
StratC_23)`, recursing into the certified `V3`) completely from scratch in
`/tmp/round-17/solve_menu2.py`. First pass (`solve_menu.py`) had a bug — I
called `V3` on unsorted argument triples inside the `StratA`/`StratC_ij`
branches, since `V3` assumes its inputs pre-sorted descending — and this
produced a **spurious violation**, `A=(992,670,325,158)`: buggy `V4=1150 >
target=1144`. This is a good adversarial self-check: after sorting the
triples correctly (`solve_menu2.py`), the same witness gives `V4=1074 ≤
1144`, no violation, and a 200,000-trial random Case-C sweep at `m=4` found
**zero violations**, worst margin ratio `41/61755·Σ > 0`, and both named
witnesses (`A=(6,4,3,2)` → `8=8` exactly; `A=(1859,931,619,611)` →
`2014≤2144`) reproduce exactly. This **independently re-confirms** (not just
re-runs) current.md's round-16 zero-violation claim for the certified
5-strategy menu, and flags for the record: any future round building a
general-`m` recursive solver must sort every recursive-call argument triple
by descending value before invoking `V3`/`V_{m-1}` — an easy silent bug that
manifests as a false counterexample, exactly the shape of trap this run's own
history (round 12→13 mark-accounting bug) has hit before.

I did not build a full general-`m≥5` recursive solver (the honest move-menu
for `m≥5` is not yet defined/certified beyond the `m=6` ad hoc
contiguous-vs-non-contiguous witness in round 15) — doing so properly is
builder-scale work, not scouting-scale, and risks exactly the kind of
accounting bug just illustrated if done hastily. I flag this as a concrete,
bounded task for the next builder round rather than attempting it here.

## 3. The one fresh idea worth flagging: WLOG-reduce the adversary's config `A`, not just Xiang Yu's response

**Observation on quantifier structure.** Every mechanism tried in this run so
far — the 5-strategy menu, Hall/König covering, scalar averaging, mixed
strategies, greedy scan-order — fixes an arbitrary Liu Bang configuration `A`
and searches for/bounds Xiang Yu's *response*. None has tried to first
**WLOG-reduce which configurations `A` need to be checked at all**, the way
`recursive-embedding-induction` closed the *lower* bound: that side didn't
directly analyze "does the adversary's best response beat `c(n)` for every
`B`" as a raw universal statement either — it built one specific extremal
family `A_n` and proved *that* family achieves `c(n)`, with the matching
upper-bound half (this approach's job) still needing "no other `A` beats
`c(n))`." The idea: use a **smoothing/exchange argument directly on `A`**
(not on the response) to show that Liu Bang's worst-case `A` for fixed `m` can
be taken WLOG from a small, explicit finite family — mirroring `aimo-0146`'s
"exchange-smoothing toward the heaviest-weight entries" and `aimo-0656`'s
"linear-in-a-box optimum sits at a corner," but applied to the *adversary's*
choice variable instead of the response.

**Why this is structurally different, not a repackaging.** `V_m(A)` (the true
game value, min over Xiang Yu's responses) is, within any fixed "cell" where
one specific response-strategy realizes the min and one specific case-branch
of every recursive sub-call is active (exactly the kind of cell round 16's
Region 1/Region 2/Region 3 partition of `m=4` Case C already carves out
implicitly), a **piecewise-linear function of `A`** — every strategy formula
in the current menu (`StratA`, `StratB`, `StratC_{ij}`, and `V3`'s own three
branches) is an explicit affine combination of `A`'s coordinates within its
domain of validity. If this holds in general (needs proof for general `m`,
not yet done), then `c(m-1)Σ(A) - V_m(A)` is piecewise-linear on the Case-C
cone, and **its infimum over each cell is attained at a vertex/extreme ray of
that cell** — a *finite* set of configurations per cell, not the whole
continuum. Round 16's Region 1 closure already implicitly used exactly this
fact (proving `StratA`'s bound is *affine, strictly decreasing* in `t_1`,
hence minimized at the region's boundary vertex `t_1=4/15Σ`, where it exactly
meets `c(3)Σ` at the single point `A∝(6,4,3,2)`) — but this was done as
ad hoc case-specific algebra, not stated or used as a **general, reusable
vertex-reduction lemma** applicable uniformly for every `m`.

**What a slug pursuing this would need to do, concretely (not attempted here,
scouting only):**
1. Prove (or find a counterexample to) the general claim: for fixed `m` and a
   fixed choice of (i) which strategy in the menu realizes `V_m(A)`, and (ii)
   which branch of every nested `V_{m-1}`/`V3`/.../`L_2` call is active, the
   function `A ↦ V_m(A)` is affine on the corresponding polyhedral cell.
2. If so, formalize "worst case over a cell is at a vertex" as a general
   lemma (this is exactly `aimo-0656`'s crux move, `argmax` of a
   linear-in-a-box functional is a corner — imported, not reinvented) and use
   it to reduce "prove the bound for every `A` in Case C" to "prove the bound
   at finitely many named extremal vertex configurations per `m`" — a finite
   check, potentially inductively bounded in count as `m` grows (the number
   of cells/vertices is presumably some explicit function of `m`, itself
   provable by strong induction — this is the genuinely new content, and the
   place this could still fail: if the vertex count blows up combinatorially
   with `m` faster than the induction can absorb, this collapses back into
   full casework, no better than the status quo).
3. Cross-check whether the finitely many extremal vertices, once identified
   for `m=4` (i.e. is `A∝(6,4,3,2)` really the *unique* worst vertex of Case
   C's Region 1/2/3 decomposition, or are there others not yet found because
   Region 3 itself is unclosed?) form a recognizable pattern across `m`
   (analogous to the `A_n` geometric family that closed the lower bound) —
   this is a concrete, checkable numeric task for a follow-up explorer: run a
   `scipy.optimize.differential_evolution` search for the worst-case `A` at
   `m=5,6` under the best currently-available proxy value (e.g. round 15's
   `m=6` full non-contiguous-menu solver) and see if the located extrema have
   small rational coordinates suggestive of a vertex of a low-dimensional
   cell (the way `(6,4,3,2)` and `(3,2,2)`-proportional points did at
   `m=3,4`), rather than generic irrational-looking optima.

**Risk flag, stated honestly.** This idea has NOT been tested at all this
round (no vertex-count induction was attempted, no general affineness proof
was checked) — it is a structural observation plus a concrete task list, not
verified machinery. It could fail exactly the way `minimax-mixed-duality`
failed (reduces back to "here is more casework," offering no shortcut) if the
number of cells/vertices grows too fast with `m`. But it is genuinely
different in *quantifier structure* from every mechanism explicitly ruled out
for this task (it fixes no template on the response, uses no scalar
averaging, no covering/matching existence question, no scan-order) — it
instead asks "which finitely many `A` are worst," a question none of the
prior ~15 rounds asked directly. Worth one outliner slug, explicitly scoped
to Step 1 above (test affineness-per-cell and vertex reduction at `m=4` on
the *already fully understood* Region 1/2 boundary as a sanity check) before
committing to general `m`.

## Summary verdict

- Crux corpus: **no new mechanism found**; every superficially-promising lead
  (pairing/mirroring, mixed-strategy/probabilistic, exchange-smoothing/
  charging) traces back to one of the four explicitly-dead lines.
- Numerics: re-confirmed (independently, catching and fixing my own
  sort-order bug along the way) that the certified `m=4` 5-strategy menu has
  zero known violations — no new counterexample surfaced, no new pattern in
  "what the true optimal Xiang-Yu response looks like" beyond what round 16
  already documented (Region 3's `StratC_{23}` needing its base triple's own
  Case-C branch, not just DOM).
- One fresh, untested direction worth a slug: **vertex/extreme-point
  reduction on the adversary's configuration `A` itself** (§3), imported from
  crux `aimo-0656`'s "linear-in-a-box optimum is a corner" move, generalizing
  what round 16's Region 1 closure already did ad hoc. This is a genuinely
  different framing (quantifies over which `A` need checking, not over which
  response wins) from the four ruled-out mechanisms, but is high-risk
  (plausible collapse into unbounded casework) and completely unworked —
  report it to the outliner as a candidate to scope narrowly (test on the
  already-solved `m=3`/`m=4` Region 1/2 boundary first), not as ready-to-build
  machinery.

## Files
- `/tmp/round-17/solve_menu.py` — first (buggy) from-scratch reimplementation
  of the certified `m=4` menu; kept for the record as an example of the
  sort-order trap.
- `/tmp/round-17/solve_menu2.py` — corrected version; reproduces all
  current.md witnesses exactly and found zero violations in 200,000 random
  Case-C trials.
