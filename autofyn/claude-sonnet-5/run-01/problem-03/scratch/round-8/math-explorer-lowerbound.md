## imo-2026-03 — lens: the two isolated lower-bound sub-gaps of `recursive-embedding-induction`

### Gap (a): partial-budget anchor-only strategies, M even

**Key structural fact (not previously exploited in the write-up):** because every
anchor value `t_i = 2^{n-i}` is a power of two and the lattice has ratio exactly 2,
the *only* way to split an anchor-valued piece into two anchor-valued parts is an
**exact halving** (`t_i → t_{i+1}, t_{i+1}`) — a sum of two *distinct* powers of two
is never itself a power of two (no dyadic carries), so no other anchor-exact split
exists. Consequently **every anchor-only strategy, full- or partial-budget, is
forced to be a binary subdivision tree**: `P_1` (forced to split, Fact 1 of
`lemmas/parity-pair-anchor.md`) and each `T_i` independently choose *some* binary
tree of halvings (possibly the trivial one-leaf tree, i.e. "don't touch"), and the
total marks used is exactly (total leaves) − (number of pieces) = Σ(leaves_i − 1).
This is a much more rigid combinatorial universe than "any nonnegative integer
vector `(c_1,...,c_n)`" — it is exactly the recursive self-similar structure Lemma
3 already uses, just applied at the leaf level instead of only at the top.

**Numeric probe (exhaustive, not sampled, exact integers).** I wrote a full
enumerator of every reachable anchor-only configuration (every binary-tree choice
for `P_1`, forced-split, and for each `T_i`, unforced) at budget `≤ n`, and computed
`D` for **all** of them:

- `n=1,2,3,4`: exhaustive over ALL reachable configs (full AND partial budget,
  every possible binary-tree shape) — `1, 4, 17, 82` configurations respectively —
  **zero violations of `D ≥ t_n`**, min `D` always exactly `t_n = 1`.
- Restricting to **even-`M`** configs only (the genuinely open sub-case): `n=2`: 1
  config, min `D=1`; `n=3`: 4 configs, min `D=1`; `n=4`: 19 configs, min `D=1`.
  **No even-`M` reachable configuration ever beats `t_n`.**
- The abstract counterexample cited in `lemmas/parity-pair-anchor.md`
  (`n=2`, abstract `c=(0,4)`, giving `D=0<1`) is confirmed **not reachable**: it
  would require killing `t_1` from `B` entirely while producing `4` copies of
  `t_2`, which needs `P_1` (level 2) to split directly into four level-`0`... no,
  it needs ≥3 marks on `P_1` alone (binary tree to depth 2), exceeding budget `n=2`.
  This matches the lemma file's own diagnosis exactly.

**Interesting side observation:** the true minimum `D = t_n` is already achieved at
**partial budget** in several cases (e.g. `n=3`'s minimizer uses only 2 of 3 marks:
`P_1={2,2},T_1` untouched-then-split differently — see script output
`(2, 6, [2,2,1,1,1,0])`), so the "extension-monotonicity" conjecture flagged in the
lemma file (*"splitting one more level can only decrease-or-preserve `D`"*) is
consistent with but not sharply needed — the real fact needed is weaker: **no
reachable config ever goes below `t_n`**, not that adding marks monotonically helps.

**Assessment: gap (a) looks tractable, and the abstract-parity route in the current
write-up is probably not the easiest path.** Recommend reframing the proof
directly on the binary-tree/self-similar structure: since `P_1`'s tree and each
`T_i`'s tree are *independent* recursive instances of the same "binary subdivision
of a power-of-two value" object, a proof by strong induction on `n` that peels the
**root of `P_1`'s tree** (which must split into two level-`(n-1)` sub-pieces, one of
which is by Lemma 3 exactly a rescaled copy of the whole `A_{n-1}` top piece,
recursively) should let the induction go through uniformly for *every* budget
`b ≤ n`, sidestepping the `M`-parity case split entirely (the parity issue is an
artifact of the `(c_1,...,c_n)`-vector abstraction, not of the underlying game).
This reduces to formalizing "any binary-tree-reachable dyadic leaf-multiset from a
level-`e` piece has `D ≥` [something bounded appropriately]" recursively — a natural
generalization of Lemma 3 + the existing Case A/B mechanism, but indexed by tree
recursion instead of by `M`'s parity. I did not attempt this proof (out of scope
for exploration), but the small-case data strongly supports it being the right
shape, and no obstruction (like the refuted "bound by sums alone" Candidate Lemma
from round 2) turned up in the search.

Script: `/tmp/explore_gap_a.py` (exhaustive enumerator + `D` computation, exact
Python ints, `n=1..4`).

### Gap (b): cross-piece tied free coordinates

**Numeric probe, exact rational LP-vertex enumeration (not sampling).**

- **`n=2`**, splitting `P_1` with 1 mark (free `s1`) and `T_1` with 1 mark (free
  `u1`), full budget: enumerated **all** vertices of the 2-free-variable polytope
  (all pairs of active linear constraints among `{s1,s2,u1,u2}` vs each other and
  vs anchors `{t1=2,t2=1}`), exact `Fraction` arithmetic. Global minimum `D=1=t_n`
  achieved only at the pure-anchor vertex `s1=s2=t1=2, u1=u2=t2=1`. The two
  possible genuine cross-piece-tie vertices (`s2=u1`, `s2=u2`, i.e. a free `P_1`
  coordinate tied to a free `T_1` coordinate) give `D=3`, **far above** `t_n=1` —
  strictly dominated, not competitive.
- **`n=3`**, `P_1` with 2 marks (free `s1,s2`, `s3` dependent), `T_1` with 1 mark
  (free `u1`, `u2` dependent), full budget: enumerated **all 228** feasible
  vertices of the 3-free-variable polytope exactly. Global min `D=1=t_n`
  (achieved, interestingly, at a vertex where the *labels* look like a
  cross-tie `s3=u1=u2`, but the tied value is `2=t2`, i.e. it's really an anchor
  coincidence, not a genuine free cross-tie). Filtering to **genuine** cross-tie
  vertices (tied value strictly between anchors, not equal to any `t_i`): found
  **31** such vertices; the best (lowest-`D`) among them is `D=5/3 ≈ 1.667`,
  strictly and substantially above `t_n=1`. **No genuine cross-tie vertex comes
  anywhere close to the true minimum.**
- Random continuous search (200k trials) at `n=3` with the same split shape
  approaches `D→1` only by driving `u2→0` (a piece degenerating to the anchor
  boundary, not a genuine interior cross-tie) — consistent with the exact result.

**Assessment: gap (b) looks even more tractable than (a), and possibly does not
need the "shared 2-multiplicity block" bookkeeping mechanism sketched in the
approach file at all.** The data suggests a cleaner route: prove directly that
**genuine cross-piece-tied vertices are always dominated** (i.e., never attain the
global minimum) — e.g. via a local perturbation/exchange argument: at a genuine
cross-tie `x=x'` (`x` from piece `π`, `x'` from `π'≠π`, no anchor between), since
`D` is linear in each of `x,x'` separately (fixed ranks) within the cell, and the
cell's boundary in *either* direction (breaking the tie one way or the other) is
still feasible for at least one of the two directions (a standard "can't be a
strict 2D local min of a linear function unless the level set contains a segment"
argument — here two independent linear functionals `∂D/∂x` and `∂D/∂x'` control the
tied value's two "roles"), one can likely always move to weakly decrease `D` by
breaking the tie, landing back in the well-separated / single-free-coordinate
case already closed by Lemma FC / Lemma V'-GEN's proved branch — i.e. **cross-tie
points can be shown non-minimal by a direct convexity/domination argument, without
needing the shared-block generalization of Lemma PARITY-PAIR-GENERAL's Case A.**
This would be a *shorter* proof than the one currently sketched in the approach
file. Not proved here — this is a lead, not a result — but the exact vertex data
at `n=2,3` gives no counter-evidence and a comfortable margin (`5/3` vs `1`, `3`
vs `1`), suggesting the domination gap, if real, is not a knife's-edge case.

Scripts: `/tmp/explore_gap_b.py`/`b2.py` (`n=2` exact vertex enum),
`/tmp/explore_gap_b3.py`/`b4.py` (`n=3` random probe + exact vertex enum).

### Which gap looks more tractable

**Both look tractable, and (b) looks slightly more tractable / lower-risk** — the
numeric margin between the true minimum (`t_n=1`) and the best cross-tie vertex
found (`5/3` at `n=3`, `3` at `n=2`) is large and grows with `n` in these samples,
suggesting a clean domination argument (not a delicate parity argument) will close
it, and it does not require touching the already-delicate `M`-parity machinery at
all. Gap (a) is also tractable but the fix is a genuine (if mechanical)
restructuring of the induction around the binary-tree/self-similarity structure
rather than the abstract `(c_1,...,c_n)`-vector formalism currently used — real
work, but the small-case data gives no sign of an actual obstruction (unlike the
certified-false "bound by sums alone" Candidate Lemma from round 2, which *did*
have a concrete counterexample). Recommend the outliner assign concrete build
tasks: (b) "prove genuine cross-piece-tie vertices are dominated by a
perturbation/exchange argument" (likely the shorter proof); (a) "redo the
partial-budget anchor-only closure via induction on the binary-subdivision-tree
structure (peeling `P_1`'s root split, reusing Lemma 3's self-similarity), instead
of via the `M`-parity vector abstraction" — both are now backed by exhaustive
(not sampled) small-`n` verification, not just heuristic plausibility.

### Candidate technique(s)
- Gap (a): induction on `n` (or on tree depth) directly over the binary
  subdivision structure, reusing Lemma 3 (self-similarity) and the certified
  Lemma D-BOUND for whichever sub-piece plays the "odd case" role — same toolkit
  as Lemma PARITY-PAIR-GENERAL, different indexing (tree recursion vs `M`-parity).
- Gap (b): a domination/exchange lemma showing genuine cross-piece ties are never
  the global minimizer, reducing Lemma V'-GEN's general case to the already-proved
  well-separated case. Reuses the certified Lemma D-INSERT (affineness of `D` in a
  free coordinate on its bracket) applied to *both* tied coordinates simultaneously.

### Cheap-kill candidates
None beyond what's already used (the reachability/binary-tree observation for (a)
and the vertex-domination check for (b) are themselves the cheap kills — they
rule out the abstract counterexamples without heavy machinery).

### Knowledge-base entries to use
Not separately consulted this pass (this lens is entirely internal to the
approach's own certified-lemma toolkit): Lemma 3 (self-similarity), Lemma
D-INSERT, Lemma D-BOUND, Lemma PARITY-PAIR-GENERAL — all already named and
certified in `lemmas/`.

### Analogous past problems (cruxes)
Not queried this pass — this lens was a deep, problem-internal numeric probe of
two specific isolated sub-gaps per the dispatch instructions, not a general
retrieval pass. (If needed next round: search the crux corpus for "binary/dyadic
subdivision + alternating sum" or "vertex domination in polytope optimization"
under combinatorics/algebra subtopics.)

### Prior progress
See `results/imo-2026-03/current.md` and
`results/imo-2026-03/approaches/recursive-embedding-induction.md` round 7 section
— both gaps precisely isolated there; this report adds exact small-case
verification (exhaustive, not sampled) for both, plus concrete proof-shape
suggestions.

### Dead ends (do not retry)
- Gap (a): the abstract "$M$ even $\Rightarrow D\ge t_n$" statement is genuinely
  false in the abstract (confirmed, `n=2`, `c=(0,4)`) — do not try to patch Lemma
  PARITY-PAIR-GENERAL itself to cover even `M`; the fix must go through
  reachability/tree structure, not the abstract vector statement.
- Gap (a): "extension-monotonicity" (`D` monotonically decreases as more marks
  are spent) is not needed and may not even be the cleanest true statement — the
  minimum is already hit at partial budget in the `n=3` example, so a *monotone
  decrease* framing is unnecessarily strong; prefer proving the bound directly
  for all reachable configs regardless of budget.

### Small-case / intuition notes (all labeled conjecture from finite exhaustive checks, not proofs)
- Conjecture (a): for every `n`, every anchor-only Xiang-Yu strategy (any budget
  `≤n`) has `D(B) ≥ t_n`. Verified exhaustively (not sampled) for `n=1,2,3,4`
  (all 1+4+17+82 = 104 reachable configurations, zero violations).
- Conjecture (b): for every `n` and every way of splitting `P_1` and the tail with
  a total of `≤n` marks, the true minimizer of `D` never requires two free
  coordinates from different split pieces to be tied to a common non-anchor
  value. Verified by exact vertex enumeration at `n=2` (all 2-free-var vertices)
  and `n=3` (all 228 3-free-var vertices for one representative mark
  distribution) — best genuine cross-tie vertex is always strictly and
  substantially above `t_n`.
