# imo-2026-06 — outline-reviewer report (round 2)

Gate verdict on the round-2 field of 7 entries. Two new slugs registered; two
retired; field ranked head-to-head (K=32). Build set at the bottom.

## Per-approach verdicts

### 1. `small-prime-window-lemma` — OPEN (new) → APPROVE / REGISTER
Cleanest single-claim reframing of the crux: B1 (kernel stabilize + coincidence
+ seed) collapses to ONE claim B1' = "no large-prime shortcut in the window
`(a_n, a_n+R]`," and once B1' holds the rest is genuinely free (pigeonhole
stabilization of `M'_n` over the definitional finite universe `P_R`, then
certified Theorem 1). The seed sub-gap dissolves correctly (the small-prime
greedy stays in `B` by Theorem 1). Mechanism is the **spacing fact** (a prime
`q>R` divides ≤1 integer of any length-`R` window — verified empirically) plus
a covering bound.

Issues to close while building (CHANGES-style, not blocking):
- Step 2(b)'s crude covering count `|J*|` vs `ω(m)` goes the wrong way (LHS
  `~ n`, RHS `~ log a_n`). The outline already admits this and prescribes the
  refinement: restrict to the **last period** of class-`σ*` terms near `a_n`,
  where spacing makes each large prime of `m` hit ≤1 of them (capacity `≤ω(m)`,
  demand `T_*`). The builder MUST actually prove `T_*` is bounded against
  `ω(m)` using `m ≤ a_n+R` — this is the genuine heart, unproven. Treat it as
  the load-bearing lemma, not a "then it follows."
- The lemma is named with a mechanism (spacing + last-period covering), which
  is sound as a strategy but unproven. Acceptable to build.
- B2 (step 6) is secondary and lives on the small lattice — fine.

Registered (cold-start 1500). Ranked. In build set.

### 2. `hitting-set-monovariant` — REVISE → APPROVE (revised)
The round-1 false monovariant `(|M_n|, Σ|h|, #disjoint-pairs)` is correctly
dropped (explorer stress-tested it: `|M|` rises `3→9` before falling; `#disjoint-
pairs` rises `3→12` on step 1 — non-monotone). The closure lemma (cross-
intersecting `M'_n` is stable forever) is VALID (2000 off-greedy tests, 0
violations; clean minimality-contradiction proof) and is correctly demoted to
an *early-stabilization shortcut*, not load-bearing (finite-universe backstop
closes the theorem). The recast 7-step chain is a real simplification: it
eliminates B1(b) (seed) and the monovariant, reducing the problem to B1' + B2.

Mechanism on B1' is **transversal-minimality / matching duality** — genuinely
different from spacing: it argues that the bounded-diff witness `R·⌈(a_n+1)/R⌉`
is a small-prime admissible hitting set, so by transversal duality no large prime
is ever essential for minimality.

Issues to close:
- Step 4's duality bridge is the unproved heart. The outline names the
  mechanism (Hall/König min-transversal = max-matching on rows×primes, or
  "smallest-product minimal transversal is small-prime-only") but the bridge
  from "an admissible small-prime candidate exists" to "EVERY minimal
  transversal is small-prime-only" is NOT established. The hitting-set explorer
  itself could not close it and admitted the route re-imports B1 (it is an
  equivalent reformulation, not a bypass). The builder must formulate the
  duality precisely or honestly report it as the same wall in different
  language.
- Watch: do NOT confuse "a small-prime hitting set exists" with "every
  minimal hitting set is small-prime-only." The latter is strictly stronger and
  is what B1' requires.

Ranked. In build set (different mechanism: duality).

### 3. `bounded-diff-finite-state` — ADVANCE → APPROVE (advance)
Certified spine intact (bounded-diff, universal-small-prime, Lemma 3, Theorem
1, trivial cases). The refuted Bertrand/competing-candidate attack is correctly
replaced by a `v_p`-multiplicity / size-counting move (König explorer's Opening
C).

Issues to close:
- The crude `v_p` count is INCONCLUSIVE and goes the wrong way (RHS `~ n·log
  n/R` eventually exceeds LHS `~ n` — wrong direction for a contradiction). The
  outline prescribes the same last-period refinement as `small-prime-window-
  lemma`. **See coupling verdict below** — this refinement may be the SAME
  load-bearing sub-move as the spacing route's, making this slug's "distinct
  mechanism" thinner than the outliner claims.
- The outline still references Lemma 3 = `F_n` stabilization, which the new-
  framing explorer showed OVER-COUNTS the modulus (`∏∪F_∞ = 30030` vs the true
  kernel product `∏∪M'_∞ = 30` for `a_1=15`). The builder must use `M'_n`
  (minimal hitting sets) as the stabilizing object and `L = ∏∪M'_∞` (kernel
  product), NOT `∏∪F_∞`. This is a correctness fix, not cosmetic.

Ranked (highest Elo after update). In build set.

### 4. `periodic-set-iteration` — ADVANCE → CHANGES REQUESTED / NOT IN BUILD SET THIS ROUND
The refuted profinite-compactness gamble is correctly dropped. But the
replacement step 4(a) IS B1' in periodic-set language, and its attack mechanism
is **the spacing fact + the same last-period covering bound** as
`small-prime-window-lemma` step 2(b) — the outline itself flags this coupling.

**Coupling verdict (the key call):** `periodic-set-iteration`'s distinctive
spine (the decreasing chain of periodic sets `A_n` + profinite-free reduction)
does NOT constitute an independent attack on B1'. The new-framing explorer
established that `A_n = ∪_{h∈M_n}{mult of m_h}` is an IDENTITY, so the chain
`A_n` is literally the hitting-set admissible set in different notation; its
"convergence to a fixed periodic `A`" IS the stabilization `M_n = M'_n`, which
IS B1'. The only distinctive content of step 4(a) — the spacing+covering move
on the window — is byte-identical to `small-prime-window-lemma`'s heart. **If
the spacing+covering move is refuted, both die together (single-gap trap).**

I verified the coupling is real, not just notational: at `n=40, a_1=15`, three
large past primes (17,19,23) touch only 2 of the 15 window integers — so
spacing ALONE is insufficient (confirmed), and the covering-bound refinement is
the genuine load-bearing move shared by both slugs.

Decision: do NOT spend a parallel builder here this round. Build
`small-prime-window-lemma` (the cleaner single-claim version) instead, and probe
`periodic-set-iteration`'s independence cheaply next round only if the
spacing+covering move survives the builder's attempt. Ranked (kept live, below
the cleaner twin).

### 5. `frozen-invariant-reduce-mod-lcm` — OPEN (new) → APPROVE WITH CAVEAT / PROBE
Genuinely different proof shape (does not route through `M'_n` stabilization +
Theorem 1 as spine): bounded coordinate `d_n≤R` (free); frozen invariant /
simplifying regime; min-of-failing-set monovariant `w_n = min{m>a_n : m∉B_n}`,
prove non-increasing ⇒ B1'; then reduce mod lcm of attainable state-values ⇒
finite-state pair ⇒ eventually periodic. This is the field's only non-`M'_n`
attack on B1'.

Issues (substantial — the outline is honest about them):
- Step 2 (frozen invariant identification) is UNIDENTIFIED — the genuine
  conceptual step. The candidate `I_n = a_n mod L_*` fails (periodicity mod `R`
  is FALSE, verified).
- Step 3 (the `w_n` monovariant, the B1' attack) is UNPROVEN and the outline
  concedes it may not transfer (greedy defined by "smallest admissible," not by
  gcd/lcm recurrence). The builder MUST test `w_n` empirically before trusting
  it.
- Step 4 (deterministic finite-state transition) is the SAME obstruction the
  König explorer found (residue mod M does not determine next residue without
  the small-prime state = B1'). The outline honestly flags this: step 4 is NOT
  a genuine bypass of B1' — it still needs step 3 to supply B1'. If step 3
  fails, RETIRE this slug; do not let it become a disguised fifth copy of the
  B1' wall.

Registered (cold-start 1500). Ranked. In build set as a PROBE — the builder
should test `w_n` empirically first and retire-fast if the monovariant does
not hold.

### 6. `compactness-konig-branch` — RETIRE → CUT (do not build, do not register further)
The König explorer's collapse proof is solid and doubly-fatal:
(i) finite branching (König) holds B1-free but "infinite path ⇒ eventually
periodic" needs a *deterministic finite* state, and residue mod M is NOT it
(verified: same residue `0 mod 15` yields next residue `10` vs `3` on two
greedy-continued paths — history-dependent, not a function of the node);
(ii) "unique infinite path" is false in the consistent-prefix tree (≥20
children at the root, all extending to infinite paths with DIFFERENT `(T,L)` —
`(8,30)`, `(1,3)`, `(1,5)`, long transients), and vacuous in the greedy-prefix
tree (single path, König trivial, periodicity still = B1).

The one salvageable idea (finite-state ⇒ eventually periodic via cyclic-
successor) IS `bounded-diff-finite-state`'s conditional spine. Retire: not in
build set, left in population as a low-Elo record so the dead route is
documented (it lost every comparison).

### 7. `bijection-from-n1` — RETIRE → CUT (do not build)
The distinctive injectivity bypass of B1 is confirmed collapsed (residue
transition not well-defined until the admissible set is periodic mod L, which
IS B1). Route exhausted. Residual contributions (bounded-diff, Theorem 1,
trivial cases, B2-is-separate diagnostic) are all recorded in `current.md` and
imported by the live slugs. Retire: not in build set, left as low-Elo record.

## Coupling verdict (single-gap trap check)

`periodic-set-iteration` and `small-prime-window-lemma` are **coupled**: both
share the load-bearing spacing+covering-bound sub-move on B1' (verified — the
spacing fact alone is insufficient at `n=40, a_1=15`; the covering refinement is
the genuine heart, and both outlines prescribe the IDENTICAL last-period
refinement "capacity ≤ ω(m), demand T_*"). `bounded-diff-finite-state`'s
`v_p`-counting move also bottoms out at the same last-period refinement
(its crude count goes the wrong way identically). So **three of the four
mechanisms converge on ONE unproved sub-move** (the last-period covering bound).
This is the round's single biggest risk: if that sub-move is refuted, three
slugs die together.

Mitigation: build ONE spacing-based slug (`small-prime-window-lemma`, the
cleanest) plus the genuinely-independent `hitting-set-monovariant` (duality)
plus the `frozen-invariant-reduce-mod-lcm` probe (different proof shape
entirely). Hold `periodic-set-iteration` out of the build set this round; if
the spacing+covering move survives, probe its (thin) distinctive content next
round. Tell the `bounded-diff-finite-state` builder to test whether its `v_p`
cofinality angle is genuinely independent of the last-period covering move
before committing to it — if not, this slug is also coupled and should adopt
the cleaner `M'_n` object (correctness fix above) and ride the same heart.

## Mechanism-diversity verdict

Four claimed mechanisms:
- (i) **spacing/covering** — `small-prime-window-lemma`, `periodic-set-
  iteration`, and (after refinement) `bounded-diff-finite-state`. These
  COLLAPSE to one mechanism (single-gap trap, per coupling verdict).
- (ii) **transversal-duality** — `hitting-set-monovariant`. Genuinely
  independent of spacing: a refutation of "spacing+covering" does not kill the
  matching/duality bridge (and vice versa). The bridge is unproven but the
  mechanism is distinct.
- (iv) **frozen-invariant / reduce-mod-lcm** — `frozen-invariant-reduce-mod-
  lcm`. Genuinely different proof shape (bounds a coordinate, reduces mod lcm
  of attainable values). Independent of (i) and (ii) — BUT step 4 re-imports
  the König finite-state obstruction, so it is conditional on step 3 supplying
  B1'. Independent as a *route*, not as a *bypass*.

**Confirmed: at least two genuinely independent mechanisms** (spacing/covering
vs duality), plus a third independent proof-shape (reduce-mod-lcm) as a probe.
The field is NOT a single-mechanism trap — but it is a 3-vs-1 imbalance,
which is why the spacing sub-move is the critical thing to test this round.

## Full ranking after update (Elo order, K=32, stale cleared)

| rank | slug | Elo | last outcome | notes |
|---|---|---|---|---|
| 1 | `bounded-diff-finite-state` | 1591.3 | advanced | certified spine; v_p advance; watch coupling + over-counting fix |
| 2 | `hitting-set-monovariant` | 1561.7 | — (revised) | clean 7-step; duality bridge = heart; drops false monovariant |
| 3 | `small-prime-window-lemma` | 1560.2 | — (new) | cleanest single-claim; spacing+covering = heart |
| 4 | `periodic-set-iteration` | 1513.1 | advanced | coupled to small-prime-window-lemma; held out this round |
| 5 | `frozen-invariant-reduce-mod-lcm` | 1482.0 | — (new) | highest-risk probe; retire-fast if w_n monovariant fails |
| 6 | `bijection-from-n1` | 1407.2 | partial | RETIRED (route exhausted) |
| 7 | `compactness-konig-branch` | 1384.4 | — | RETIRED (collapsed into bounded-diff-finite-state) |

## Build set (one proof-builder per slug)

`small-prime-window-lemma`, `hitting-set-monovariant`, `bounded-diff-finite-state`, `frozen-invariant-reduce-mod-lcm`

Builder directives:
- `small-prime-window-lemma`: attack the last-period covering bound (the heart);
  prove `T_*` bounded vs `ω(m)` with `m ≤ a_n+R`; use `L=∏∪M'_∞` (kernel
  product). This is the round's critical test of the shared spacing sub-move.
- `hitting-set-monovariant`: formulate the transversal-duality bridge precisely
  (Hall/König on rows×primes, or smallest-product minimal transversal) and
  bridge "exists a small-prime admissible candidate" → "EVERY minimal
  transversal is small-prime-only." Test empirically before committing.
- `bounded-diff-finite-state`: switch stabilizing object to `M'_n` (kernel
  product, NOT `∏∪F_∞`); test whether the `v_p` cofinality angle is
  independent of the last-period covering move — if not, it is coupled to
  small-prime-window-lemma and should ride the same heart.
- `frozen-invariant-reduce-mod-lcm`: PROBE — test `w_n` empirically first
(non-increasing? bounded above `a_n+R`?); if the monovariant fails, retire
fast and report; do not let it become a fifth copy of the B1' wall.
