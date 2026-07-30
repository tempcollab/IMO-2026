## Status
unsolved (dead end — Step 0 gate fails; recorded honestly, not patched
around)

## Approaches tried
- **Round 15 build.** Ran the mandatory Step 0 numeric/representational
  feasibility gate (outline-reviewer's added caveat: check not just that
  *some* bipartite graph has bounded deficiency, but that a Hall-type
  matching in the chosen graph actually *implies* the needed subset-match)
  on the uniform-tail family, the `T=(0.20,0.15,0.12,0.08)` witness, and
  `A=(1826,1563,1520,1514,765)/7188`. **Result: the gate fails —
  decisively and structurally, not just on these witnesses. This is a
  genuine dead end for the whole defect-Hall/König framing, reported
  honestly per this slug's own do-not-repeat instruction. Full argument
  below.**

### Step 0 — the representational-faithfulness check

**What Hall's theorem / König deficiency actually characterizes** (per
`knowledge_base.md`'s "Hall's marriage theorem / SDR" entry): given a
bipartite graph with parts `X,Y` and neighborhoods `N(\cdot)`, a matching
saturating `X` exists iff `|N(S)|\ge|S|` for every `S\subseteq X`; the
defect form bounds the size of the largest unmatched subset of `X` by
`\mathrm{def}(X)=\max_{S\subseteq X}(|S|-|N(S)|)`. This is a **cardinality
/ reachability** statement: it tells you *how many* left-vertices can be
simultaneously assigned *distinct* right-vertices under a fixed adjacency
relation. It says nothing about the **numeric value** carried by whichever
right-vertices end up matched.

**What Lemma SLACK-COVER actually needs** (restated precisely in
`universal-adversary-strategy.md`'s Round 14/15 sections, and re-derived
here from scratch, not merely quoted): given sorted Case-C `A=(p_1,\dots,
p_m)`, tail `T=\mathrm{tail}(A)`, find *some* subset `S\subseteq T` with
`\Sigma(S)\le p_1`, cost `\mathrm{cost}(S)=|S|-[\Sigma(S)=p_1]\le marks`,
such that `\Sigma(S)+\mathrm{solve2}(\mathrm{leftover},marks-\mathrm{cost}
(S))\le c(m-1)\Sigma(A)`, where `\mathrm{leftover}` is `T\setminus S` with
the residual `r=p_1-\Sigma(S)` inserted. This is a statement about the
**value** of a subset (via the exact identity of the already-certified
Lemma DOUBLE-INSERT-MATCH-VALUE / Lemma PAIR-VALUE, `lemmas/pair-value.md`,
`lemmas/double-insert-match-value.md`) combined with a recursive value
bound on the leftover — not a cardinality/existence statement at all.

**Structural fact, general to every Case-C instance, not witness-specific
(checked here, but true unconditionally by Case C's own defining
inequality).** Case C is defined by `p_1<\Sigma(A)/2`. Hence
`\Sigma(T)=\Sigma(A)-p_1>\Sigma(A)-\Sigma(A)/2=\Sigma(A)/2>p_1`, **strictly,
always**. So "does some subset of `T` cover `p_1`" (i.e. does *any*
covering `S` with `\Sigma(S)\ge p_1`, or the weaker `\Sigma(S)\le p_1`
with small residual, exist) is **never in doubt** in Case C — a trivial
greedy argument (take tail elements one at a time, largest first, until
the running sum reaches or passes `p_1`; this must happen before
exhausting `T`, since `\Sigma(T)>p_1`) always succeeds. Verified explicitly
by exact `fractions.Fraction` computation on all three mandated witnesses:
- **Uniform-tail family** (`\Sigma(A)=1`, `p_1=1/2`, tail of `m-1` equal
  elements summing to `1/2`): `\Sigma(T)=1/2=p_1` at the exact limiting
  boundary, and `>p_1` strictly for every genuine Case-C instance
  approaching it (`p_1<1/2` strictly, so `\Sigma(T)>1/2>p_1`), checked
  for `m=4,5,8,12`.
- `T=(0.20,0.15,0.12,0.08)` (as a Case-C sub-instance in its own right,
  target `p_1'=0.20`, its own tail `(0.15,0.12,0.08)`): `\Sigma(\mathrm{tail})
  =0.35>0.20=p_1'`. Exhaustive check of all `2^3=8` subsets confirms
  multiple covering subsets exist (e.g. `\{0.15\}` alone already exceeds
  nothing but is close; `\{0.12,0.08\}` sums to exactly `0.20=p_1'`,
  `r=0`) — existence is not merely true but multiply witnessed.
- `A=(1826,1563,1520,1514,765)/7188` (`m=5`): tail sum
  `=(1563+1520+1514+765)/7188=5362/7188$, `p_1=1826/7188`;
  `5362>1826$ — covering existence trivial (e.g. `\{1563\}` alone already
  exceeds nothing needed; `\{1563,1520\}=3083>1826$ already overshoots,
  and smaller single elements plus residual trivially cover it).

So on **every** graph encoding one could reasonably draw for this
"covering" question (left = `\{p_1\}` or a discretization of it, right =
tail elements or subsets, edges = "usable towards the target"), the
Hall condition is satisfied and the deficiency is **zero** — not merely
bounded, but identically `0`, in every Case-C instance, unconditionally.
This is not a near-miss numeric pass; it is a vacuous pass, and that
vacuity is the failure.

### Why a vacuous pass kills the framing (the representational-faithfulness
failure the outline-reviewer flagged)

A defect-Hall argument is only informative when the *deficiency* is the
binding constraint — i.e. when whether *some* legal assignment exists is
itself in doubt, and the theorem's contribution is to certify existence
(or to quantify how far short of full saturation one must fall). Here
that existence question is answered "yes, always, by a two-line greedy
argument from the Case-C inequality alone" — **before any graph is even
drawn**. Consequently:

- If the encoding graph is **permissive** (edges = "any subset with
  `\Sigma(S)\le p_1`," i.e. essentially the complete relevant relation):
  Hall's condition holds trivially (deficiency `0`) in every instance, so
  the theorem outputs "a covering subset exists" — a true but **already
  known, already-easy fact** (this is exactly the "prefix-mesh bound"
  `universal-adversary-strategy`'s Round 14 build independently derived
  and explicitly flagged as *not* the missing ingredient: "the open
  question is not 'is some affordable subset close to `p_1`' … it is
  'does an affordable subset exist whose resulting recursive value …
  meets the target'"). A zero-deficiency Hall certificate carries **no
  information whatsoever** about which of the (generically many)
  covering subsets achieves the required value bound. This is the
  precise sense in which the encoding is representationally unfaithful:
  a Hall-saturating matching in this graph does **not** imply the needed
  *value-good* subset-match — it implies only the already-trivial
  existence fact.
- If the encoding graph is instead **restricted** to some structurally
  meaningful sub-class of moves (e.g. edges = "contiguous prefix of the
  sorted tail," mirroring the old, already-superseded Move 2/PARTIAL-DOM),
  bounded (even zero) deficiency *within that restricted class* still does
  **not** imply the value target is met, by a concrete, already-on-file
  counterexample: on `A=(0.45,0.20,0.15,0.12,0.08)` (tail
  `T=(0.20,0.15,0.12,0.08)`), the contiguous-prefix class is
  Hall-saturated (a legal prefix match — matching `p_1'=0.20` to the
  prefix `\{0.15\}`, residual `0.05` — exists and is found), yet its
  value is `\mathrm{oddrank}=0.28`, which **exceeds** the target
  `\Sigma(T)/2=0.275` (this is exactly the round-13/14-certified finding,
  independently re-verified here by direct computation with
  `fractions.Fraction`: `Fraction(7,25)=0.28>Fraction(11,40)=0.275`). Only
  the *non-contiguous* subset `\{0.12,0.08\}` (sum `=0.20$ exactly,
  `r=0`) meets the target, `\mathrm{oddrank}=0.275` exactly. So a
  Hall-certificate of bounded deficiency in the restricted-class graph
  is **satisfied by a match that fails the actual requirement** — the
  implication "Hall-matching exists in `G`" `\Rightarrow` "needed
  subset-match exists" is **false** for this choice of `G` too.

Both horns are checked and both fail the faithfulness requirement: either
the graph is too permissive (deficiency trivially `0`, theorem vacuous —
gives no leverage on which subset to pick) or too restrictive (deficiency
bounded within the class, but a Hall-witness in that class can be exactly
the wrong choice, value-wise). There is no encoding in between that
escapes this dichotomy, because the underlying difficulty is not a
**cardinality/reachability** fact (which subsets of `T` are "reachable"
or "usable" — this is never the obstruction, by the Case-C inequality
above) but a **numeric optimization over which specific subset's exact
real value, combined with a recursive value on the leftover, clears a
target** — a fundamentally different combinatorial shape (subset-sum /
knapsack-value optimization) from an SDR/matching-cardinality question.
This is exactly the disanalogy the outline-reviewer flagged when
checking crux `aimo-0341` directly (that crux's mechanism is a genuine
1-1 assignment/SDR structure on a product grid, not a many-to-one
subset-value optimization), now confirmed not just as "a different
flavor" but as a **provable failure of the needed implication direction**
in both natural encodings.

### Explicit self-check against this slug's own risk list

- Per the do-not-repeat item "an unbounded deficiency on either known
  hard witness kills this approach immediately": the deficiency is not
  unbounded, it is **zero** — an even more decisive failure mode than the
  one anticipated (the risk was framed as "too hard to bound," the actual
  failure is "trivially bounded to the point of vacuity, or bounded-but-
  wrong-witness-selected"), and it is reported as such rather than
  reframed to look like a pass.
- No general deficiency-bound proof (Step 1) or value-adaptation (Step 2)
  was attempted, per the explicit instruction not to proceed past a
  failing Step 0 on an unverified premise.

## Current best
Nothing carried forward as progress on Lemma SLACK-COVER itself — this
approach contributes a **negative result**: the defect-Hall/König-
deficiency framing is representationally unfaithful for this problem's
actual open question (Case-C subset-match value optimization), for both
of the two natural bipartite encodings, and should not be reattempted in
this form. The one reusable fact is the general structural observation
(new, but elementary — worth keeping so no future round re-derives it by
numeric search): **in every Case-C instance, `\Sigma(\mathrm{tail}(A))>p_1`
strictly, so any subset-covering/existence question for `p_1` against the
tail is automatically trivial; the entire content of Lemma SLACK-COVER is
the value-optimization question of *which* covering subset to use, never
an existence question** — consistent with, and now given a clean general
proof of, `universal-adversary-strategy`'s Round 14 build's own
witness-specific diagnosis ("the open question is not 'is some affordable
subset close to `p_1`' … it is … value-aware").

## Approach skeleton (Round 15 open — superseded by the Step 0 failure
above; kept for the record, not to be built on)

## Approach skeleton (Round 15 open)

**Target (the whole problem, restated).** For each positive integer `n`,
determine the largest `c=c(n)` such that Liu Bang (first mover, `n`
marks) can guarantee total length `\ge c` regardless of Xiang Yu's `n`
marks and the ensuing draft, and prove both:
(a) **Upper bound:** no Liu Bang strategy beats `c(n)` (Xiang Yu has a
response holding him to exactly `c(n)`), and
(b) **Lower bound / construction:** Liu Bang has an explicit strategy
`A_n` guaranteeing `\ge c(n)`.

Per the field's current state (see `current.md`, Rounds 9–14 and
`recursive-embedding-induction.md`), the **lower bound (b) is already
fully closed** (Lemma TREE-BOUND-MULTICLUSTER, Round 10, independently
re-verified) — that construction and its value are not reopened here.
The **entire remaining content of the whole problem is the upper bound
(a)**, specifically Xiang Yu's adversary strategy value on Case C
configurations (`p_1<\Sigma(A)/2`, `m\ge4`) matching `c(m-1)\Sigma(A)`,
which is exactly the recursive `(marks,|A|)` game `solve2` (defined in
`universal-adversary-strategy.md`) is built to compute, and whose sole
open gap is Lemma SLACK-COVER (existence of a subset-match, jointly with
its recursive value, meeting the target).

**Why this is a genuinely different proof shape from the live field
(not a relabeling).** This approach does not use `solve2`'s move-menu
recursion, Lemma PAIR-VALUE/BLOCK-RECURSE's mark-cost accounting, or any
linear/averaging certificate (all three variants of that mechanism —
`case-c-slack-covering`, `potential-averaging-bound`,
`equalization-potential-bound` — are independently refuted or
conditional). Instead it casts Xiang Yu's matching problem as an
explicit **bipartite graph existence question** and attacks it with
**König/Hall deficiency** (defect form of Hall's marriage theorem,
`knowledge_base.md`'s "Hall's marriage theorem / SDR" entry), adapting —
not citing — the technique from crux `aimo-0341` (peel the
maximum-deficiency subset, apply plain Hall to the remainder, handle the
leftover by hand). This targets Case C's Lemma SLACK-COVER gap from a
different theorem than anything tried so far, per this round's
plateau-break mandate.

**Step 0 (mandatory numeric feasibility gate, before any general proof
effort).** Define the candidate bipartite matching graph precisely for
Case C: left vertices = "targets to be tied" (the top block `p_1`, or
more generally each block requiring a match in the recursive
construction), right vertices = candidate tail elements/subsets
available to match them, edges = "this tail subset can serve as (part
of) a valid tie for this target within the mark budget." Compute the
Hall deficiency `\mathrm{def}(X)=\max_{S\subseteq X}(|S|-|N(S)|)` of this
graph **explicitly** on the two known hard witnesses already on file:
- the uniform-tail family (the exact refutation witness from
  `case-c-slack-covering`, Round 14, where one-level averaging fails for
  every `m\ge4`), and
- `T=(0.20,0.15,0.12,0.08)$ (the `m=4` witness requiring a genuine
  non-contiguous match, per the Round 15 `math-explorer-termination`
  report — small enough for exhaustive `2^3`-subset hand computation).

If the deficiency is **not** uniformly bounded (grows with `m` or with
the depth of recursion) on either witness, this framing is dead on
arrival and must be reported as such — do not proceed to a general
deficiency-bound proof on an unverified premise. This gate must be run
and its outcome reported honestly before any further step, exactly as
`case-c-slack-covering`'s and `relaxed-adversary-transfer`'s gates were.

**Step 1 (gap — deficiency bound, if Step 0 passes).** Prove the
matching graph's deficiency is bounded by an explicit, small quantity
(ideally a constant, or `O(1)` independent of `m`) using the sorted
order of `A` (tail elements `t_i\le p_1`, `A` descending — the same
structural fact the certified contiguous Move 2/Lemma DOM-boundary-slack
already exploits) — a direct combinatorial neighborhood-structure
argument, not a global averaging inequality. **This is a gap**: no such
bound has been derived or checked yet.

**Step 2 (gap — from deficiency to a value bound, the genuinely new
content).** Standard defect Hall bounds a *cardinality* of unmatched
vertices; the quantity that actually matters here is the leftover's
contribution to `oddrank`, a weighted, order-sensitive quantity, not a
plain count. Adapting `aimo-0341`'s "build the missing/leftover part
coordinate-by-coordinate" step to a *value* statement (not an existence
statement) is genuinely new work — **this is the crux of the whole
approach and is not yet done.** The target: combine the bounded
leftover (from Step 1) with the already-certified value machinery
(`lemmas/pair-value.md`, `lemmas/double-insert-match-value.md`,
`lemmas/wf-c5.md` — reused, not re-derived) to show the deficient
leftover's recursive value is absorbed by whatever slack margin the
correct (non-averaged) `c(m-1)\Sigma(A)` bound leaves, closing Lemma
SLACK-COVER. **This is a gap.**

**Step 3 (assembly, if Steps 1–2 close).** Combine with the already-fully-
proved lower bound (`recursive-embedding-induction.md`, Lemma
TREE-BOUND-MULTICLUSTER) to obtain the complete two-sided determination
of `c(n)` for every `n`, with the explicit closed form for `c(n)` stated
and verified (per CLAUDE.md's rigor rule for `compute_and_prove`
problems) exactly as `universal-adversary-strategy.md`'s own verdict
section already sets up (Lemma THRESHOLD-REDUCTION's recursion
`c(k-1)=c(k)/(2(1-c(k)))`; only Case C's upper bound is missing).

**Explicit risks / do-not-repeat, carried over from the Round 15
fresh-framing scouting report:**
- If Step 2's "build the leftover by hand" ends up reconstructing the
  same tie/rank-parity casework `solve2`'s Move 0–3 menu already
  encodes, this collapses into a relabeling of
  `universal-adversary-strategy` — must be checked explicitly at the
  first build gate, not assumed away, and reported honestly if so.
- Do not attempt this via a global linear/averaging deficiency estimate
  — that is the same mechanism already refuted three times
  (`case-c-slack-covering`, `potential-averaging-bound`,
  `equalization-potential-bound`); the deficiency bound (Step 1) must
  come from a direct structural/sorted-order argument.
- Do not skip Step 0: an unbounded deficiency on either known hard
  witness kills this approach immediately and must be reported as a
  dead end, not patched around.
