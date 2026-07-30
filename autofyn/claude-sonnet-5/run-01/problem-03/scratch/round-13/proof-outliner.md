## imo-2026-03

Context (do not re-derive): The entire LOWER BOUND (`A_n` achieves
`c(n)=2^n/(2^{n+1}-1)` for every `n`) is fully proved and certified
(Lemma TREE-BOUND-MULTICLUSTER, round 10). `m=1,2,3`-piece cases of the
UPPER BOUND (Claim PTBI, "no config beats `A_n`") are fully closed.
**The single remaining gap in the whole problem is Claim PTBI's Case C
(`p_1<Σ(A)/2`) for general piece-count `m≥4`.** Candidate 5
(budget-capped TAIL-SNIP recursion, `solve(A,budget)`, well-founded per
certified Lemma WF-C5) passes an extensive adversarial gate with no
counterexample. This round's three explorers all confirm: the round-12
"tail locally dominant" witness `A=(0.45,0.40,0.06,0.05,0.04)` is NOT a
counterexample (the recursion already reaches `Σ/2` exactly, snip firing
3 levels down) — it only refutes the naive "pure Move-1 telescoping"
*proof strategy*, not the recursion itself. New finding: HALF-BOUND
(`solve_full(A)≤Σ(A)/2` throughout Case C) empirically holds as an exact
**identity** (`solve_full(A)=Σ(A)/2`), confirmed on 7000+ exact-`Fraction`
trials including the explicit worst-case cascading family
`p_i=(1/2-ε)R_i` for every `i` (margin exactly 0, `m` up to 20). No move
propagates the bound alone; the `min` over Move 1/2/3 genuinely switches
winner by configuration. Verdict from all 3 explorers: **STAY in this
framing** — no alternative combinatorial framing (Hall-matching,
duality, potential-averaging) found any leverage; the fix is a properly
targeted strong induction on `|A|` with an existential (not
scalar-predicate) inductive hypothesis, not a new top-level approach.

---

universal-adversary-strategy: revise
Target: Claim PTBI's Case C for general `m≥4` — for every sorted
`A=(p_1\ge\cdots\ge p_m)` with `p_1<\Sigma(A)/2`, no Liu-Bang
configuration beats `c(m-1)\Sigma(A)`; equivalently (via already-certified
Lemma THRESHOLD-REDUCTION, since `c(k)>1/2` for all finite `k`), it
suffices to prove Lemma HALF-BOUND: `\mathrm{solve\_full}(A)\le\Sigma(A)/2`.
Technique: strong induction on `m=|A|`, tracking `\mathrm{solve}(A,b)` for
`b\in\{0,1\}` jointly, with the key case split not on a *scalar* predicate
of `A` alone but on whether **`\mathrm{tail}(A)` is itself Case-C relative
to its own sum** (`p_2<\Sigma(\mathrm{tail}(A))/2`) — i.e. whether the
"locally dominant" pathology recurs one level down. This directly targets
the exact obstruction all three explorers independently confirmed: no
single move (Move 1 alone or Move 2 alone) propagates HALF-BOUND, but the
obstruction is *localized* to whichever level of the recursion first hits
a locally-dominant tail, and below that level a fresh sub-instance
restarts the same dichotomy (this is why strong, not one-step, induction
on `|A|` is required — round-13-inductive lens's finding that leftover is
frequently NOT Case-C-for-itself, and that budget-0 recursion on such a
leftover frequently overshoots, is exactly the signal that budget must be
spent *at the level where the pathology recurs*, not necessarily at the
top).
Skeleton:
  1. Base cases `m=1,2,3`: Case C is vacuous for `m=1,2` (sorted-descending
     forces `p_1\ge\Sigma/2` always) — one-line arithmetic check. `m=3`
     Case C is already fully closed unconditionally (round 9,
     BLOCK-RECURSE_1/TAIL-SNIP algebra) — import that result as the base
     case rather than re-deriving; it already gives `\mathrm{solve\_full}
     (A)\le c(2)\Sigma(A)`, and HALF-BOUND itself for `m=3` can be checked
     directly on the finite algebra already on file (builder confirms it
     is consistent, does not need re-proof from scratch).
  2. Inductive step, `m\ge4`, `A` in Case C. Case split on `\mathrm{tail}
     (A)=(p_2,\ldots,p_m)`:
     - **Case (a): `\mathrm{tail}(A)` is Case-C relative to itself**
       (`p_2<\Sigma(\mathrm{tail}(A))/2`). By the strong IH (size `m-1<m`,
       budget 1), `\mathrm{solve}(\mathrm{tail}(A),1)\le
       \Sigma(\mathrm{tail}(A))/2`. Apply Move 1 (already-certified
       identity `\mathrm{solve}(A,1)\le p_1/2+\mathrm{solve}(\mathrm{tail}
       (A),1)`): `\mathrm{solve}(A,1)\le p_1/2+(\Sigma(A)-p_1)/2=
       \Sigma(A)/2`. **Closed — by Move 1 + IH only, no budget spent
       below this level.**
     - **Case (b): `\mathrm{tail}(A)` is NOT Case-C relative to itself**
       (`p_2\ge\Sigma(\mathrm{tail}(A))/2`, i.e. `p_2` alone dominates the
       rest of the tail). Here Move 1 cannot be used (the IH does not
       apply to `\mathrm{tail}(A)` in the needed form). Instead apply
       Move 2 (partial-dom) directly at the top level of `A`: since
       `p_1<\Sigma(A)/2` and `p_2\ge\Sigma(\mathrm{tail}(A))/2`, a short
       algebraic argument (Key Lemma CASE-B-MATCH below) shows the
       Move-2 prefix match `j^*` against `p_1` inside `\mathrm{tail}(A)`
       satisfies one of two outcomes: (i) an exact tie (`S_{j^*}=p_1`,
       leftover empty) — then `\mathrm{solve}(A,\cdot)=S_{j^*}=p_1=
       \Sigma(A)/2` is forced directly by `p_1<\Sigma(A)/2` combined with
       the matching identity `\Sigma(\mathrm{leftover})=\Sigma(A)-2S_{j^*}`
       (empty leftover forces `S_{j^*}=\Sigma(A)/2>p_1`, contradiction
       unless `S_{j^*}=p_1=\Sigma(A)/2` — needs care, flagged as a genuine
       sub-step for the builder, not hand-waved); or (ii) a nonempty
       leftover `L` with `\Sigma(L)=\Sigma(A)-2S_{j^*}` and `|L|<m` — apply
       the strong IH to `L` **at budget 0** if `L` is Case-C for itself
       (`\mathrm{top}(L)<\Sigma(L)/2`), or spend the single Move-3 tail-snip
       mark (well-founded per certified Lemma WF-C5) to convert `L` into a
       shape where it is, before invoking the budget-0 IH on the
       tail-snipped `L'` (`|L'|<m` still, since `|L|<m` strictly).
  3. Assemble: every branch of the case split terminates (strong induction
     on strictly decreasing `|A|`, well-founded per certified Lemma WF-C5,
     reused not re-derived) at either a direct Move-1+IH closure (Case a)
     or a Move-2(+Move-3)+IH closure (Case b), each giving
     `\mathrm{solve}(A,1)\le\Sigma(A)/2`. Combine with Lemma
     THRESHOLD-REDUCTION (`c(k-1)=c(k)/(2(1-c(k))`, already certified) and
     `c(m-1)>1/2` to conclude `\mathrm{solve\_full}(A)\le c(m-1)\Sigma(A)`,
     closing Case C for all `m\ge4` and hence all of Claim PTBI, hence the
     whole upper bound, hence the whole problem (Status → solved).
Key lemmas (claim + mechanism):
  - **Lemma HALF-BOUND** (`\mathrm{solve\_full}(A)\le\Sigma(A)/2` in Case
    C) — because the exact "excess" identity
    `e(A,b):=\mathrm{solve}(A,b)-\Sigma(A)/2` satisfies `e(A,b)=\min` of
    each move's excess **exactly** (Move 1's excess is exactly
    `e(\mathrm{tail}(A),b)` since `\Sigma(A)/2=p_1/2+\Sigma(\mathrm{tail}
    (A))/2`; Move 2's excess is exactly `e(\mathrm{leftover},b-1)` — or 0
    if leftover is empty and the tie is exact — since
    `\Sigma(\mathrm{leftover})=\Sigma(A)-2S_{j^*}` is an exact identity;
    Move 3's excess is exactly `e(A',b-1)` since tail-snip preserves
    `\Sigma`), reducing the whole claim to showing this min-recursion never
    goes negative, which the case split above establishes by structural
    induction rather than a single scalar invariant (round-13
    math-explorer-inductive's reformulation — reuse this exact identity as
    the organizing tool, it is algebra, not conjecture, and was verified
    exactly on all tested instances).
  - **Lemma CASE-B-MATCH** (new, needs full proof) — when `p_2\ge
    \Sigma(\mathrm{tail}(A))/2` and `p_1<\Sigma(A)/2`, the Move-2 prefix
    match against `p_1` inside `\mathrm{tail}(A)` produces a leftover
    strictly smaller than `A` whose own top element is bounded in a way
    that lets the IH (at budget 0, possibly after one Move-3 snip) close
    it — because `p_2` dominating its own tail forces `j^*\in\{0,1\}`
    (the prefix match can include at most `p_2` itself before overshooting
    `p_1$, since `p_2\ge\Sigma(\mathrm{tail}(A))/2\ge p_1/2$ is not
    automatically `\ge p_1`, so the builder must case-split further on
    `p_1` vs `p_2` here — flagged explicitly, do not paper over).
Open gaps: Lemma CASE-B-MATCH is the one genuinely new piece of algebra
this skeleton needs, not yet proved — everything else (Move 1 identity,
matching identity, WF-C5, THRESHOLD-REDUCTION) is already certified.
Builder should validate any proposed Case-B-MATCH argument against the
cascading extremal family `p_i=(1/2-\epsilon)R_i` (round-13 finding: exact
margin `0`) before claiming closure — a proof that doesn't reduce to
equality on this family is almost certainly missing a case.
Cases to cover: Case (a) tail-Case-C, Case (b) tail-dominant — further
sub-split of (b) on `p_1` vs `p_2` (both `\ge` and `<`) is required and
currently unaddressed; do not let the builder treat (b) as a single case.
Watch out for: (1) the round-12 witness `A=(0.45,0.40,0.06,0.05,0.04)` is
NOT a counterexample — do not waste builder time "refuting" the
recursion on it, the correct target is a *proof* it already succeeds
(snip 3 levels down inside tail's own recursive call), not a search for
where it fails. (2) Any sub-argument implying `e(A,1)<0` strictly should
be treated as a red flag / likely algebra error (cheap self-check from
math-explorer-inductive — 7000+ trials found excess is never negative,
only exactly `0` or positive).

universal-adversary-strategy-exact-tie: copy-of universal-adversary-strategy
Target: identical top-level claim (Claim PTBI Case C, general `m\ge4`),
same file lineage/certified-lemma base as the primary slug, but pursuing
a **genuinely different mechanism** for the same open gap — worth running
in parallel per CLAUDE.md's copy rule, since both routes are independently
viable and neither has failed yet.
Technique: prove the sharper **identity** `\mathrm{solve\_full}(A)=
\Sigma(A)/2$ (not merely `\le`) directly via an **exact-cover / exact-tie
existence argument**, reframing the `e`-recursion (Lemma above) as "does
the recursion always reach a leaf, or an exact Move-2 tie
(`S_{j^*}=p_1$ exactly), with excess `0`" — a Boolean existence claim
per configuration rather than an inequality needing slack-bookkeeping.
Skeleton:
  1. Reformulate via the exact `e`-recursion (same identity as above,
     shared with the primary slug — do not re-derive, cite it).
  2. Observe the only strictly-positive leaf of the min-recursion is the
     singleton base case (`e(\text{singleton})=p_1/2>0`); every other
     terminal state is an exact tie giving `e=0` exactly. So HALF-BOUND-
     as-identity reduces to: **for every Case-C `A`, there exists a
     sequence of Moves 1/2/3 (using the single available budget unit at
     most once) that reaches an exact tie before it is forced down to a
     singleton.**
  3. Attempt to prove this existence claim by strong induction on `|A|`,
     tracking a REACHABLE-TIE invariant: define `T(A)` = set of values
     reachable as a partial-sum of some subset of `A\setminus\{p_1\}$
     (or of a once-tail-snipped variant of `A$). Claim: `p_1\in T(A)$ for
     every Case-C `A$ (i.e. some subset of the rest of the pieces sums
     exactly to `p_1$), OR a single tail-snip makes it so. This is the
     Hall/exact-cover-flavored existence question the round-12 plan
     originally flagged `aimo-0063`'s Hall-deficient-set-deletion
     technique for — attempt the adaptation here explicitly (both
     round-13 lenses looked for the bridge and did not find it; this slug
     should either complete the bridge or produce a clean negative result
     ruling it out, rather than leaving it unconnected a third time).
  4. If the subset-sum-exact-match claim is FALSE in general (plausible —
     generic reals rarely have exact subset-sum coincidences), this
     approach must explain why the tail-snip move (which can synthesize
     an exact tie by splitting the last element into two equal halves,
     each a legitimate new "donor") always suffices to manufacture one —
     i.e. the real claim is about a *relaxed* exact-cover where one
     designated element can be freely bisected, which changes the
     combinatorics enough that Hall's classical theorem may not apply
     as-is; flag this explicitly as a risk in the file, do not silently
     assume classical Hall transfers.
Key lemmas (claim + mechanism):
  - **Lemma EXACT-TIE-EXISTS** (new, central, needs full proof) — because
    the recursion's only source of positive excess is the untouched final
    singleton, and Case C plus the "prefix-sum sequence of a sorted
    positive vector densely covers `[0,\Sigma-p_1]$ up to one gap of size
    `\le p_1$" structural fact (standard from the sorted-descending
    ordering) should make an exact or synthetically-manufactured tie
    generically reachable — this is conjectural and is the whole content
    of the gap, not yet reduced to a known theorem.
Open gaps: Lemma EXACT-TIE-EXISTS is entirely open; this is a genuinely
different bet from the primary slug's case-split induction (identity vs.
inequality, exact-cover-existence vs. structural case-split) — if this
route fails, it should produce a clean negative result (an explicit
Case-C `A` with no reachable exact tie under any move sequence) rather
than silently duplicating the primary slug's mechanism, per the
minimax-mixed-duality/case-c-secondary-extremality convergence-failure
lesson already on file.
Cases to cover: none enumerated yet (this is the existence-claim route,
cases to be discovered by the builder's search).
Watch out for: do not let this collapse into re-deriving the primary
slug's Case (a)/(b) split under a different name — if the builder's
"exact tie" construction turns out to just BE the primary slug's Move-2
leftover argument, merge/import rather than duplicate (per round 11's
"secondary statistic" convergence-failure precedent).

recursive-embedding-induction: advance (unchanged, no further target)
Target: (already fully discharged) the entire lower bound `c(n)\ge
2^n/(2^{n+1}-1)$ via `A_n$, closed in full at round 10
(Lemma TREE-BOUND-MULTICLUSTER). No open gap remains in this approach's
scope. Not nominated for build this round — kept live in the population
as the certified record, per "do not re-attempt a closed gap."
Technique: n/a (closed).
Skeleton: n/a.
Key lemmas: n/a (all certified, see `lemmas/tree-bound*.md`).
Open gaps: none in scope.
Cases to cover: none.
Watch out for: do not dispatch a builder here — there is nothing left to
prove in this approach's target; any further work belongs to
universal-adversary-strategy's Case C gap.

geometric-dominance-construction: advance (unchanged, no further target)
Target: (already fully discharged, narrower independent cross-check of
the same lower-bound closure). No open gap remains in scope.
Technique: n/a (closed / superseded in generality by sibling).
Skeleton: n/a.
Key lemmas: n/a (certified, `lemmas/multi-cluster-two-block.md`).
Open gaps: none in scope.
Cases to cover: none.
Watch out for: do not dispatch a builder here either — same reasoning as
recursive-embedding-induction above.

Left alone (do not touch, per standing rules): `relaxed-adversary-transfer`
(DEAD, clean structural dead end, round 7), `minimax-mixed-duality`
(RETIRED, round 8, 2x RETHINK), `case-c-secondary-extremality` (RETHINK,
round 11, no independent leverage — value-equivalent to primary approach),
`majorization-smoothing` (DEAD x3, structural non-concavity proof),
`potential-averaging-bound` (partial but flagged near-duplicative if not
resolved — no new evidence this round to revive), `equalization-potential-
bound` (stagnant since round 1, conditional impossibility, not touched).
No new evidence surfaced this round for any of these; per the standing
rule, do not resurrect without one.
