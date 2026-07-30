# imo-2026-03 — proof-outliner field (round 7)

Terrain read: upper explorer (recursive-split fix, O2→subset-sum, greedy cascade),
lower explorer (vertex-level restatement (★), Mechanism A, exhaustive T_3/T_4
vertex enum 0 counterexamples). Both walls are now narrow and concrete. The lower
wall gained a genuinely new object this round — the **vertex-level restatement
(★)** ("D=1 at a strong breakpoint ⟹ F=0"), which the face-level framings missed;
the upper wall gained a **load-bearing methodology fix** (recursive splits) that
removes the spurious "violations" and a clean constructive spine (greedy cascade).

Field = 3 approaches (2 lower, 1 upper) + HOLD notes on the converged lower
framings. Dead ends respected (O1, V(n) IH, 3-mark cascade, Max-bound,
Schur/majorization, even-packing-as-bypass, spine sign-pattern/multi-swap,
superincreasing-chain, mass-budget-as-sign-argument, non-tower Liu configs,
value-type classification). No two slugs share a single gap.

---

## imo-2026-03

### tail-count: ADVANCE
Target: `c(n) ≥ 2^n/D_n` for ALL n (the whole lower bound; the approach's overall
target is the whole problem `c(n)=2^n/D_n`, upper deferred to `majorization-upper`).
Technique: PL/variational + **vertex-level sign-assignment** (Mechanism A). Spine
= crux **(★) at every non-dyadic strong breakpoint (PL vertex) of `T_n`, `D>1`**,
proved via the single-survivor structure + the `t₊−f₋ > F` sign-forcing argument.
This is the strongest lower lead in 7 rounds — the vertex-level restatement is a
genuinely new object (the face-level framings missed "at most one non-dyadic
fragment survives at a vertex").
Skeleton:
  1. `pl-breakpoint-minimum` (certified) ⟹ global min of `D` over all ≤n-mark
     refinements of `T_n` is attained at a strong-breakpoint PL vertex.
  2. At a dyadic vertex, `D≥1` (`dyadic-refinement-lower-bound`, certified).
  3. **(★, the hard step)** At a non-dyadic strong breakpoint of `T_n`, `D>1`.
     a. **Single-survivor:** at a vertex, at most ONE non-dyadic fragment value
        survives on the spine. (Two surviving non-dyadic groups ⇒ `nfree≥2` ⇒ the
        config is a face, not a vertex; `D=1` on a face lives at a sub-vertex
        with `nfree≤1` — captured by the single-survivor case. Rigor needed.)
     b. **v-bracket:** the survivor `v` satisfies `1 < v < 2^{n−1}`. Mass budget
        `3v ≤ 2^n` (each non-dyadic survivor appears ≥3 times among top fragments,
        `mass-budget-breakpoint-inequality`) ⇒ `v ≤ 2^n/3 < 2^{n−1}`; and the
        known tower-valued fragments consume ≤ `2^n−4` of the top budget ⇒
        `v ≥ 4/3 > 1`. So `v` is NOT the smallest spine piece and sits strictly
        between surviving towers.
     c. **Decomposition:** `D = (F−T) + 2(t₊−f₋)` (spine-level, `t₊`=tower mass at
        `+`, `f₋`=fragment mass at `−`). At budget-tight vertices `T=3F−1`
        (certified), this gives `D = 1 − 2F + 2(t₊−f₋)`, so **`D>1 ⟺ t₊−f₋ > F`**.
     d. **HARD SUB-STEP (the sign-forcing proof):** prove `t₊−f₋ > F` from
        sort-order sign assignment + mass budget + **tower-vs-tower dyadic
        dominance** (ALLOWED — towers are distinct powers of 2) — but NOT
        fragment-vs-tower superincreasing (FORBIDDEN, round-6 rule). Two cases:
          - frag at `−` (13/15 vertices): `f₋=v`, need `t₊ > 2v`. The towers at
            `+` include the largest surviving tower (which exceeds `v`, since
            `v<2^{n−1}`) plus others; their sum exceeds `2v` by the mass budget
            `T≥3v−1` plus the sort-order forcing of large towers to `+`.
          - frag at `+` (2/15): `f₋=0`, need `t₊ > v`. Holds because the largest
            surviving tower alone exceeds `v`.
  4. Combine 1+2+3 ⟹ min `D ≥ 1` ⟹ `c(n) ≥ 2^n/D_n`.
Key lemmas (claim + one-line mechanism):
  - **Single-survivor** (at most one non-dyadic fragment survives at a vertex) —
    because two surviving non-dyadic groups would make the config a face
    (`nfree≥2`), and `D=1` on a face is attained at a sub-vertex (`nfree≤1`);
    vertex = `nfree≤1` by the PL-vertex definition.
  - **v-bracket** `1<v<2^{n−1}` — because `3v≤2^n` (mass budget) and tower-valued
    fragments consume ≤`2^n−4` of the top budget.
  - **`t₊−f₋>F`** — because sort-order forces the largest surviving tower
    (exceeds `v`) to the sign opposite `v`, and tower-vs-tower dyadic dominance
    (`2^k >` sum of smaller distinct powers) controls how tower mass splits across
    signs, giving enough `+`-tower mass to exceed `2v` (resp. `v`).
  - **(★) restatement** — `D=1` at a strong breakpoint ⟹ `F=0` (all surviving
    fragments dyadic); verified 0/15 non-dyadic vertices T_3+T_4 (min D=5/3).
Open gaps: sub-step (d) — the formal sign-forcing proof of `t₊−f₋>F` (the
universal condition, NOT the "largest tower at + > frag + smaller" dominance which
FAILS 2/15). Sub-step (a) — the "at most one survivor" rigor.
Cases to cover: frag-at-`−` (13/15) vs frag-at-`+` (2/15); budget-tight (12/15)
vs non-tight (3/15); cascade vs split-tower vs split-2tower vertex types.
Watch out:
  - Do NOT use fragment-vs-tower superincreasing (forbidden — fragments aren't
    tower pieces).
  - Do NOT use the circular spine sign-pattern/multi-swap framing (dead, round 5).
  - Do NOT mistake the mass-budget `T≥3F−1` (magnitudes) for a sign argument.
  - The "largest tower at + > frag + smaller towers" dominance FAILS 2/15 — use
    the universal `t₊−f₋ > F` instead.
  - Verify (★) at all 15 non-dyadic vertices with exact `Fraction` (the explorer's
    `mechanism_probe.py`); a single counterexample kills the route.
Imports (certified): `pl-breakpoint-minimum`, `dyadic-refinement-lower-bound`,
`mass-budget-breakpoint-inequality`, `telescoping-block-lemma`,
`mass-balance-lemma`, `spine-pair-cancellation`, `strong-breakpoint-group-structure`,
`gaps-leftover-identity`, `two-leftover-transport`, `even-group-spine-lower-bound`,
`block-contribution-formula`, `frontier-recursion`.

---

### vertex-enum-n3: NEW
Target: `c(3) = 8/15` **fully proven** (upper bound `c(3)≤8/15` already certified
via `v3-upper-bound`+`n2-max-bound`; this approach closes the n=3 LOWER bound by
finite exhaustive vertex enumeration). Overall target = the whole problem, with
`n≥4` lower bound left as the open gap (either extend the enumeration to n=4,5 —
finite but growing — or close the structural (★) for general n). This is a
genuinely different FRAMING from `tail-count`: it is **computational casework/
exhaustion for a fixed n** (KB "Casework / exhaustion"), NOT a general-n
structural lemma — and it delivers a certifiable milestone (`c(3)=8/15`) even
while the general-n wall stands.
Technique: Casework/exhaustion + PL breakpoint reduction. Finite exact
`Fraction` combinatorial computation over ALL strong-breakpoint vertices of `T_3`
by tie-structure set-partition (NOT a grid sample, NOT floating point).
Skeleton:
  1. Upper bound `c(3)≤8/15` certified (import `v3-upper-bound`, `n2-max-bound`).
  2. `pl-breakpoint-minimum` (certified) ⟹ min of `D` over ALL ≤3-mark
     refinements of `T_3` is attained at a strong-breakpoint PL vertex.
  3. **SOUNDNESS (hard step 1, load-bearing):** define the finite set `V_3` of
     ALL strong-breakpoint vertices of `T_3` = all tie-structure set-partitions
     of `{fragments} ∪ {4,2,1}` with `sum(full)=D_3=15`, covering ALL mixed
     mark-distributions (1, 2, 3 marks; cascade / split-tower / split-2tower /
     mixed types like "split top into 3 + split a tower"). Prove `V_3` is finite
     and COMPLETE: every refinement's minimum is realized at some vertex in
     `V_3` (no missed rational, no missed mark-distribution). This is the
     make-or-break soundness argument — a computational proof is legitimate ONLY
     if `V_3` is proven to exhaust the PL-vertex set.
  4. **COMPUTATION (hard step 2):** for each vertex in `V_3`, compute `D`
     exactly (`Fraction` arithmetic, no floats) and the block condition.
     Classify fragments by ORIGIN (fragment vs tower piece), NOT value-type
     (round-5/6 misclassification bug). Hard-validate `sum(full)=D_n` at every
     vertex (the explorer caught a sum bug producing spurious `D=0` configs).
  5. Verify `min D ≥ 1` across `V_3`. The explorer's partial enum (64 vertices
     T_3+T_4) found 0 vertices with `D<1`; `D=1` only at 7 dyadic vertices
     (`F=0`); all 15 non-dyadic vertices have `D>1` (min 5/3). The FULL n=3
     enum extends to all mixed mark-distributions.
  6. Conclude `min D(T_3) ≥ 1` ⟹ `c(3) ≥ 8/15`. Combined with step 1 ⟹
     `c(3) = 8/15` (both bounds, fully proven).
  7. **Open gap:** `n≥4`. Either extend the finite enumeration to `T_4`, `T_5`
     (finite but combinatorially growing — a computation, not a structural
     proof), OR close the structural (★) for general n (route: `tail-count`).
Key lemmas (claim + one-line mechanism):
  - **Completeness of `V_3`** — every PL vertex is a tie-structure set-partition
    with `sum=15`; the set of such partitions is finite and effectively
    enumerable (each vertex = a set-partition of fragments + tower-value/
    free-group assignment, solved linearly). Mechanism: `pl-breakpoint-minimum`
    reduces the min to vertices; vertices are exactly the tie-structure
    solutions of a finite linear system.
  - **Exact-Fraction soundness** — `D` is affine on each PL cell, so the vertex
    value IS the cell's min; computing at the vertex with exact arithmetic is
    rigorous (no rounding). Mechanism: PL affinity (`pl-breakpoint-minimum`).
  - **Origin-based classification** — a fragment CAN be a power of 2; classify
    by ORIGIN (fragment vs tower piece) so the block condition and `F`/`T`
    bookkeeping are correct. Mechanism: `mass-budget-breakpoint-inequality`
    (origin-based).
Open gaps: the COMPLETENESS proof of `V_3` (covers ALL mixed mark-distributions
— the explorer flagged the current enum misses e.g. "split top into 3 + split a
tower"). General `n≥4`.
Cases to cover: all mark-distributions (1, 2, 3 marks) × all refinement types
(cascade, split-tower, split-2tower, mixed) × all tie-structures (set-partitions
with sum=15).
Watch out:
  - This is a COMPUTATIONAL PROOF — legitimate ONLY if `V_3` is PROVEN complete
    (finite exhaustion over the PL-vertex set, not a grid sample). The explorer's
    partial 64-vertex result is verification, NOT proof — do not present it as
    proof.
  - Classify fragments by ORIGIN, not value-type (round-5/6 bug).
  - Hard-validate `sum(full)=D_n` at every vertex (the explorer's sum bug).
  - The enumeration grows combinatorially; `n=4,5` may be feasible but `n≥6`
    likely intractable — the general-n structural (★) is the real close.
Imports (certified): `pl-breakpoint-minimum`, `dyadic-refinement-lower-bound`,
`v3-upper-bound`, `n2-max-bound`, `spine-pair-cancellation`,
`mass-budget-breakpoint-inequality`, `block-contribution-formula`,
`telescoping-block-lemma`, `strong-breakpoint-group-structure`.

---

### majorization-upper: ADVANCE
Target: `c(n) ≤ 2^n/D_n` for ALL n (the whole upper bound; whole problem with
GAP-U2-compressed the open gap).
Technique: **Constructive/sequential greedy cascade** (Euclidean-algorithm
flavor) with a **monovariant** (KB "Invariants & monovariants"). Unified over
both the subset-sum regime (`a_1 ≤ 2^n/D_n`, ~75%) and the large-top regime
(`a_1 > 2^n/D_n`, ~25%). The O2 subset-sum reduction is folded as a FALLBACK
sub-claim for the regime where the greedy provably terminates cleanly. This is a
genuinely different framing from the existential subset-sum: it is sequential/
constructive, and its hard step (monovariant "remainder never stuck") is a
DIFFERENT quantity from subset-sum density — so it does not die with O2.
Skeleton:
  1. Closed cases (certified, import): `m≤n` ⟹ `D*=0` (`m-le-n-halving-D-zero`);
     repeated-value `m=n+1` ⟹ `D*=0` (`repeated-value-D-zero`); strictly-
     decreasing `m=n+1` with `a_{n+1}≤1/D_n` ⟹ `D=a_{n+1}≤1/D_n`
     (`halving-always-a-nplus1`). These close everything EXCEPT the compressed
     case.
  2. **GAP-U2-compressed:** strictly-decreasing `m=n+1`, `a_{n+1} > 1/D_n`.
     **Recursive-split model** (load-bearing methodology fix): each mark splits
     ANY current piece (including a previously-created fragment); `k` marks on
     one piece = partition into `k+1` arbitrary positive parts. The halving
     lemma + `block-contribution-formula` already handle fragments (they sort
     the whole refined multiset). The earlier round-6 "violations" were a
     search bug from non-recursive splits; the recursive model gives 0
     violations across thousands of configs n=2..6.
  3. **GREEDY CASCADE (primary spine):** split `a_1 → {a_2, a_1−a_2}` (1 mark,
     tie at `a_2`, the pair `a_2,a_2` cancels). Active remainder `r_1=a_1−a_2`.
     At step `k`, if `r_{k−1} ≥ a_{k+1}`, split `r_{k−1} → {a_{k+1},
     r_{k−1}−a_{k+1}}` (1 mark, tie at `a_{k+1}`, cancels). Continue ≤`n−1`
     steps. Each step pairs one more `a_i` (cancels it) and reduces the active
     remainder.
  4. **MONOVARIANT:** `r_k` strictly decreasing (each step subtracts
     `a_{k+1} ≥ a_{n+1} > 1/D_n`); the number of un-paired `a_i` strictly
     decreases. The process terminates in ≤`n−1` steps with a remainder
     `r ≤ a_{n+1}` (or 0). Mark budget ≤`n−1 ≤ n`. ✓
  5. **HARD STEP (the open core):** prove the greedy remainder never gets
     "stuck" in `(1/D_n, a_{k+1})` — i.e., either it reaches `≤ 1/D_n`
     (done: `D = r ≤ 1/D_n`) or it matches the next `a_i` (continue). Candidate
     tool: the **bounded-spread gap bound** — compression `a_i ≥ a_{n+1} >
     1/D_n`, `∑a_i=1` ⟹ spread `a_1/a_{n+1} < D_n − n` ⟹ consecutive gaps
     `a_{k+1}−a_{k+2} < (D_n/n)·a_{n+1}`. The explorer could NOT close this —
     flag as **GAP-Greedy**.
  6. **FALLBACK (O2 subset-sum, for `a_1 ≤ 2^n/D_n` regime):** find
     `S ⊆ {a_2,...,a_{n+1}}` with `sum(S) ∈ [a_1−1/D_n, a_1]`; split `a_1`
     into `S ∪ {leftover ≤ 1/D_n}`, halve the rest; `D = leftover ≤ 1/D_n`.
     This is a subset-sum density claim on `n` bounded-spread values with target
     window width `1/D_n`. Raw pigeonhole FAILS (`2^n < D_n − n` for `n≥3`); the
     density must come from the STRUCTURE of compressed configs. Flag as
     **GAP-SubsetSum**. This fallback applies ONLY where the greedy provably
     terminates cleanly; the large-top regime (`a_1 > 2^n/D_n`, ~25%) resists
     subset-sum-from-`a_1` (no subset of the rest reaches `a_1−1/D_n`) — the
     greedy MUST handle it.
  7. If **either** step 5 (greedy, both regimes) **or** step 6 (subset-sum,
     `≤ 2^n/D_n` regime) closes, GAP-U2-compressed is resolved ⟹
     `c(n) ≤ 2^n/D_n` for all n.
Key lemmas (claim + one-line mechanism):
  - **Recursive-split model correctness** — `k` marks on one piece = partition
    into `k+1` parts; the halving lemma + `block-contribution-formula` already
    handle fragments (they sort the whole refined multiset). Mechanism: the
    refinement is a multiset partition, re-sorted.
  - **Greedy monovariant** — `r_k` strictly decreasing, #un-paired strictly
    decreases ⟹ termination in ≤`n−1` steps. Mechanism: each step subtracts a
    positive `a_{k+1}` and pairs one more piece.
  - **"Remainder never stuck" (HARD, GAP-Greedy)** — bounded-spread gap bound
    from compression forces consecutive `a_i` gaps small enough that `r_k`
    cannot land in `(1/D_n, a_{k+1})`. Mechanism: gap bound + monovariant. NOT
    proved — the explorer could not close it.
  - **O2 subset-sum density (FALLBACK HARD, GAP-SubsetSum)** — for `n`
    bounded-spread values in `(1/D_n, a_1]` with `a_1 ≤ 2^n/D_n`, some subset
    sum hits `[a_1−1/D_n, min(a_1,1−a_1)]`. Mechanism: bounded-spread STRUCTURE
    (not raw count, since `2^n < D_n−n`). NOT proved.
Open gaps: step 5 (GAP-Greedy, "remainder never stuck") is the PRIMARY hard
step — it is a monovariant-termination argument, a DIFFERENT quantity from
subset-sum existence, so it does not die with O2. Step 6 (GAP-SubsetSum) is the
fallback for the `≤ 2^n/D_n` regime. The large-top regime (`a_1 > 2^n/D_n`) is
where the greedy must work alone (subset-sum impossible there).
Cases to cover: `a_1 ≤ 2^n/D_n` (subset-sum regime, ~75%) vs `a_1 > 2^n/D_n`
(large-top, ~25%); remainder `= 0` (`D=0`) vs remainder `≤ 1/D_n`
(`D=leftover`) vs remainder stuck (GAP-Greedy); `n=2` (exhaustive, 0 violations)
vs `n=3` (0 violations, worst ratio 0.88 at `(8,4,3,2)/17`) vs `n≥4`.
Watch out:
  - **Parity obstruction:** `2n+1` (odd) pieces ⟹ `D ≠ 0` with exactly `n`
    marks; the target is `D = small leftover ≤ 1/D_n`, NEVER `D=0` via exactly
    `n` marks (though `D=0` IS reachable with `< n` marks when structure
    allows). Design the strategy to leave a leftover `≤ 1/D_n`, not to fully
    cancel.
  - **Recursive-split model is MANDATORY** (non-recursive misses fragment-
    splitting, which is the actual O2 mechanism — the round-6 "violations" were
    this bug).
  - Worst non-tower ratio ~0.88 at `(8,4,3,2)/17`; deep compressed interior
    achieves `D=0` generically; difficulty concentrates at the TOWER BOUNDARY
    (`a_{n+1} → 1/D_n` from above).
  - Do NOT retry: O1 (dead — exact pairing impossible, IVT category error),
    V(n)←V(n−1) IH (phantom), 3-mark cascade (phantom), Max-bound (refuted by
    `(7,6,5,3)/21`), Schur/majorization (dead), even-packing-as-bypass
    (equivalent reframe — `D=1−2E` makes it logically equivalent, not a
    different mechanism), perturbation-to-halving-region (reduces to O1, dead).
Imports (certified): `halving-always-a-nplus1`, `m-le-n-halving-D-zero`,
`repeated-value-D-zero`, `spine-pair-cancellation`, `block-contribution-formula`,
`parallel-halving-saturates-tower`, `pl-breakpoint-minimum`,
`n2-upper-bound-complete`, `n2-max-bound`, `v3-upper-bound`,
`even-position-reframe` (diagnostic), `halving-underpacks-compressed`
(diagnostic), `closed-form-answer`.

---

## HOLD / retire notes (not built this round)

The lower field has CONVERGED: FIVE framings (`tail-count` PL/variational,
`tower-induction` block/spine, `gaps-leftover` charging, `lp-dual-certificate`
Farkas, `xor-overlap` correlation) are ALL GAP-C-equivalent at the crux (round-5
rule). After 5+ rounds this is strong evidence of a true hard wall. Per the
round-5 rule ("If all stall on the same lemma for 3 rounds, retire all but the
strongest mechanism"), the build set this round focuses on the TWO genuinely-
different lower mechanisms:
  - `tail-count` (Mechanism A — vertex-level sign-assignment, the NEW vertex-level
    restatement (★));
  - `vertex-enum-n3` (computational casework for fixed n — a different PROOF
    OBJECT, not a structural lemma).
The other three lower slugs (`tower-induction`, `gaps-leftover`,
`lp-dual-certificate`, `xor-overlap`) are HELD this round — do NOT build them;
the outline-reviewer should keep them ranked but stale. If (★) closes via
Mechanism A, the lower bound is DONE and these are moot; if (★) stalls, revisit
Mechanism B (gaps-leftover vertex charging) or Mechanism C (lp-dual infeasibility
at non-dyadic vertices) as fallback mechanisms next round.

`even-packing-upper` is a REFRAME (D=1−2E makes GAP-U2-packing logically
equivalent to GAP-U2-compressed — round-6 rule), NOT a bypass; HELD this round,
not built. `d-potential` and `self-similar` remain on HOLD (subsumed).

---

## Field handed to the outline-reviewer

  - `tail-count` — ADVANCE (Mechanism A, vertex-level sign-assignment (★))
  - `vertex-enum-n3` — NEW (finite exhaustive vertex enumeration, n=3 milestone)
  - `majorization-upper` — ADVANCE (greedy cascade + O2 subset-sum fallback)

Suggested build set: `tail-count`, `vertex-enum-n3`, `majorization-upper`
(three builders, parallel — each owns its own approach file). The lower field is
diversified by MECHANISM (structural sign-assignment vs computational
exhaustion); the upper field is a single slug with two sub-claims whose hard
steps are DIFFERENT quantities (monovariant "never stuck" vs subset-sum density),
respecting the round-6 "open at most ONE upper slug on the compressed sub-case"
rule. No two slugs share a single gap.
