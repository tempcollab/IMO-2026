## imo-2026-03 — lower-bound gap (b), multi-cluster generalization

- **Scope of this report**: I did NOT re-derive the whole proof; I scouted the
  structural obstruction to extending the single-cluster closure (Lemma
  TREE-BOUND-RESIDUAL / Lemma TWO-BLOCK) to two-or-more *simultaneous,
  independent* tie-clusters, per the dispatch. No proof attempted.

### The actual remaining claim

A vertex of the reachable polytope where **K≥2** disjoint subsets of split
pieces `S_1,...,S_K` are each tied at their *own* (mutually unrelated) value
`v_1,...,v_K`, each `v_l` playing the minority role in a 2-part split of every
piece in `S_l`. Need `D(B)≥t_n` for the merged configuration `B`.

### Distinct openings / how each mechanism would have to generalize

**1. TREE-BOUND-RESIDUAL's forest/induction route.**
The certified induction hypothesis is literally "at most one impure node in
the entire forest." Tracing through the inductive step (peel the top level,
split on whether the impurity is at the top or below):
- **Impurities distributed in disjoint subtrees** (e.g. one cluster's node
  sits below the top level, inside the `(m-1,r')` remainder, and the other
  cluster is elsewhere) peel apart cleanly: this is exactly a smaller
  instance of the *same* statement with `K-1` impurities inside the
  remainder, so an **outer induction on K, peeling one cluster's impure node
  off the forest first (find *some* impurity, apply the m-level peeling as
  before, land the rest inside the recursive `(m-1,r')` sub-forest)**
  reduces cleanly to the `K-1` case by strong induction on m — no new content
  needed for this branch.
- **The genuinely new sub-case**: two (or more) impurities land *at the same
  level simultaneously* — specifically, `p≥2` of the `r` top-level trees are
  each individually impure at once (this cannot be avoided by peeling: the
  induction's top-level step processes *all* `r` top trees together in one
  pass). This forces a **"p simultaneous impure cuts" version of Case C**:
  `B = [k' copies τ1] ∪ X ∪ {y_1,c_1} ∪ ... ∪ {y_p,c_p}`, `X` now fully pure
  (so `D(X)≥τ_m` by the *already-certified*, non-residual Lemma TREE-BOUND —
  a nice simplification: once you fix "exactly the top-level trees carry all
  the simultaneity," the deeper remainder is impurity-free). The existing
  proof closes `p=1` via **two applications of Lemma D-BOUND** (one for the
  `k'`-odd sub-case, one via a D-INSERT identity for `k'`-even). For general
  `p`, the natural fix is to insert the `p` pairs **one at a time, in
  decreasing order of companion size** `c_{(1)}>c_{(2)}>...>c_{(p)}`
  (largest first), each insertion a fresh D-INSERT step — i.e. a **new,
  genuinely un-proved "multi-pair insertion" lemma** generalizing the
  existing single-pair argument. This is the actual obstruction: not a
  logical contradiction, but a missing combinatorial lemma. My numeric probe
  (below) found no violation even when I adversarially forced companions
  `c_1≈c_2` (the case that would break a naive "D(Y)≥|c_1-c_2|" style bound,
  since then the top-block-vs-companion cancellation is near-zero and the
  slack has to come from elsewhere) — so the lemma is very likely provable,
  but the existing write-up's proof technique (two clean applications of
  D-BOUND) does not obviously survive verbatim to `p≥2`; it needs either an
  explicit induction on `p` via iterated D-INSERT, or a genuinely more
  general multi-threshold form of D-BOUND.

**2. TWO-BLOCK's two-largest-element route** looks structurally *more*
tractable to generalize, because its core machinery — the rank-shift
identity `D(L)=D(Y)+(-1)^{|Y|}D(Z)` for `Y={x>v}, Z={x≤v}` — composes
naturally across **nested thresholds**: if `v_1>v_2>...>v_K` are the
distinct cluster tie-values, then `Z` at threshold `v_1` itself splits again
at `v_2` into a new `Y',Z'`, and so on recursively. This telescopes into a
**K-fold iterated peel**, structurally the same one-step argument applied
K times from the largest threshold down, rather than a case-explosion. The
concrete new ingredient needed is a generalization of the Structural Lemma
(identifying the *two globally largest elements* of `B`) to identifying, at
each peeling level, the top elements *relative to that level's threshold*
— i.e. a "K-block" structural lemma pinning down `b_1,b_2` (or more
precisely the top elements of each `Y_l`) as a function of which cluster(s)
own indices `0` and `1` (the two dominant original pieces), generalized
across all K clusters' membership patterns. This is more casework
(`2^K`-ish flavor combinations of which cluster owns piece 0 / piece 1 /
neither) but each case reduces to the *same* single-block estimate already
proved, rather than needing a new insertion lemma. **This mechanism looks
like the more promising one to generalize** — the reduction is structural
(iterate an already-proved single-threshold fact) rather than needing a new
multi-element combinatorial identity.

**3. A third opening not yet tried by either approach**: instead of
generalizing the induction/estimate machinery, attempt a **WLOG reduction**
showing the true vertex-minimizer of `D` can never have `K≥2` simultaneous
independent clusters at once — i.e., show any 2-cluster configuration is
dominated by (or reduces to) an equivalent 1-cluster configuration with
`D` no larger, via an explicit exchange/merging argument on the two tie
values. This was mentioned as an alternative in the round-9 note but not
attempted. If achievable, it would sidestep needing *either* generalized
lemma — but no one has started building this reduction, and it's not
obviously easier than the direct generalization (the two clusters can be at
unrelated depths/subsets, so there's no obvious continuous path connecting
a 2-cluster config to a 1-cluster one without changing `D` along the way in
an uncontrolled way).

### Cheap-kill candidates
None obvious for ruling out K≥2 — the numerics are already clean (zero
violations up to 21,875 configs, and my own adversarial close-companion
probes found none either). No parity/pigeonhole shortcut identified; this
looks like it genuinely needs the extra lemma (route 1 or 2 above), not a
one-line kill.

### Knowledge-base / lemma inventory relevant here
- Lemma D-BOUND, Lemma D-INSERT (`lemmas/alternating-sum-toolkit.md`) — the
  atomic tools both routes are built from; a multi-pair or multi-threshold
  generalization would still cite these, not replace them.
- Lemma TREE-BOUND (`lemmas/tree-bound-anchor.md`) — needed as the "X is
  pure" base fact in the p-simultaneous-top-impurity sub-case (see above).
- Lemma TREE-BOUND-RESIDUAL and Lemma TWO-BLOCK themselves — both the
  starting points; neither addresses `K≥2` and neither builder flagged it in
  writing (confirmed again by direct re-reading of both files this round —
  TWO-BLOCK's Main Theorem's `S` is a set of pieces *all tied to the same
  v*, i.e. one cluster with multiple members, not multiple independent
  values; its own honest "Scope" section only flags the unrelated "doubly-
  tied ≥3-part piece" edge as open, not the multi-value case).

### Analogous past problems (cruxes)
Searched `combinatorics` subtopics `extremal-principle`, `games-and-
strategy`, `induction-and-construction` for "simultaneous/independent tie/
peel" keywords. Found no problem that is a genuine analogue of this specific
alternating-sum/multi-threshold structure. The closest *pattern* match is
the generic "peel off a self-contained top block/object, leaving a smaller
instance of the same shape for the induction hypothesis" move that recurs
across many cruxes (e.g. `aimo-0084`, `aimo-0439`, `aimo-0146`, `aimo-0438`)
— this is exactly the "outer induction on cluster count K, peel one cluster
off, recurse" strategy sketched in Opening 1/2 above, and its ubiquity in
the corpus is evidence the peeling-induction *shape* is the right one, but
none of these cruxes involve an analogous alternating-sum/threshold
identity, so there is no directly transplantable lemma. **Verdict: no strong
match; the peeling pattern is generically well-precedented, but nothing in
the corpus supplies the specific multi-pair-insertion or multi-threshold
lemma needed.**

### Prior progress
As recorded in `current.md`: gap (a) fully closed (Lemma TREE-BOUND); gap
(b) single-cluster case closed twice independently, round 9 (Lemma
TREE-BOUND-RESIDUAL, Lemma TWO-BLOCK), reviewer-certified. The K≥2
simultaneous-cluster case is the sole remaining gap in the entire lower
bound for `A_n`.

### Dead ends (do not retry)
- The round-9 plan's "compare residual configuration directly to its
  virtually-fully-split counterpart via a single domination inequality" is
  confirmed FALSE in general (159/600 violations, already recorded in
  TREE-BOUND-RESIDUAL's file) — do not resurrect this comparison mechanism
  for the multi-cluster case either; it fails even at K=1.
- Do not re-litigate the single-cluster closures themselves — both are
  independently reviewer-verified from scratch this round and last; the gap
  is precisely and only the K≥2 case.

### Small-case / intuition notes (numerical, NOT proof)
I ran my own from-scratch adversarial probe (`/tmp/multicluster_probe.py`,
independent of the builders' scripts): `(m,r)`-forests with `p=2`
simultaneous top-level impure trees, exhaustive over which anchor depths
`j_1,j_2∈{2,...,8}` (including `j_1=j_2`, the case where two companions are
*exactly* equal in magnitude — the scenario most likely to break a naive
"companions dominate and their difference supplies the margin" argument),
each combined with hundreds of random pure shapes for the rest of the
forest. **Minimum `D` found was always exactly `1=τ_m`, zero violations.**
This is consistent with (and independently reproduces) the round-9
reviewer's own multi-cluster stress test. Conjecture (not proof): the
`K≥2` bound holds with the *same* value `τ_m` as `K=1`, i.e. simultaneity
does not help the adversary at all — suggesting the correct generalized
lemma should give a clean, K-independent bound, not a bound that degrades
with `K` (a good sign for provability via either route above, since a
K-independent target is more likely to fall to a clean induction than one
requiring per-K bookkeeping).
