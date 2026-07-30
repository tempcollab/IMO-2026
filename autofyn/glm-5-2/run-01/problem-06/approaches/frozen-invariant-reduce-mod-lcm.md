# frozen-invariant-reduce-mod-lcm — approach file (round 2)

## Status
unsolved (ROUTE RETIRED — the aimo-0678 monovariant lever does not transfer to a single-sequence greedy; see Approaches tried)

## Approaches tried
- **round 2: transfer the aimo-0678 crux shape (frozen invariant + min-of-failing-set monovariant + reduce-mod-lcm ⇒ finite-state ⇒ periodic).** — DEAD-END, retired fast per protocol. Empirical test of the load-bearing monovariant `w_n = min{m>a_n : m∉B_n}` over `a_1 ∈ {15,35,77,91,105,135,175,385}` shows `w_n` is **non-decreasing** (it tracks `a_n` upward, gap `w_n-a_n ∈ {1,2,3}`) in ALL eight cases — the OPPOSITE of the non-increasing direction the aimo-0678 lever requires. The reformulation `u_n := w_n-a_n` is bounded but OSCILLATES (e.g. `a_1=15`: `1,2,1,1,…`; `a_1=105`: `1,3,1,…`) — not monotone. The finite-state determinism test (step 4) confirmed the König obstruction: on the greedy orbit `(a_n mod 30) → (a_{n+1} mod 30)` is a deterministic 8-cycle (period `T=8` from `n=0`), but this is precisely Theorem 1 re-derived on the *already-stabilized* small lattice — it is NOT a bypass of B1', and off the periodic regime the transition is history-dependent (the state that determines `a_{n+1}` is the full past small-support family / hitting-set family `M'_n`, finite only under B1'). So step 4 is conditional on step 3, which failed. **Retire this slug; do not let it become a fifth copy of the B1' wall.**

## Current best
No correct progress SPECIFIC to this approach. The certified results it re-confirmed (B1' holds empirically for all 8 tested `a_1`; the greedy residue orbit mod `L` is a single cycle from `n=1`) are already recorded in `current.md` and owned by the spacing/duality routes. This approach's distinctive contribution is the NEGATIVE result: the aimo-0678 monovariant mechanism does not transfer to a greedy defined by "smallest admissible," because such a greedy has no frozen invariant (no coupled second sequence, no conserved sum, no explicit gcd/lcm recurrence giving divisibility structure of a "next state") to power the non-increasing proof.

### Open gap (the reason the route is dead, recorded so no agent retries this shape)
The aimo-0678 monovariant `w_n = min{m≥a_n : m∤s_n}` is non-increasing there ONLY because (a) there is a frozen invariant `s_n = a_n+b_n` conserved in the divisibility regime, and (b) the explicit recurrence `s_{n+1}=gcd(a_n,b_n)+lcm(a_n,b_n)` lets one prove `a_n ∤ s_{n+1}` whenever `a_n ∤ s_n`, forcing `a_n ∈ W_{n+1}` and hence `w_{n+1} ≤ a_n = w_n`. Neither ingredient exists in our problem: the greedy `a_{n+1} = min{m>a_n : gcd(m,a_i)>1 ∀i≤n}` has no coupled sequence, no conserved quantity, and no algebraic formula exposing the divisibility structure of the next state. The literal analog `w_n = min{m>a_n : m∉B_n}` is non-decreasing because the first non-small-prime-admissible integer above `a_n` sits at distance `1–3` from `a_n` and slides upward with `a_n`; it bounds nothing about `a_n` itself. The lever's entire purpose (non-increasing while `a_n` increases ⇒ `a_n` bounded) is absent.

## Full proof
(Not present — Status is `unsolved`. The route was retired by empirical refutation of its load-bearing monovariant before any proof could be assembled.)

## Promotable lemmas
None. (The negative monovariant test is a diagnostic, not a reusable lemma; it is recorded here to prevent re-dispatch.)

---

## Appendix: empirical evidence (diagnostic, not proof)

### Test A — monovariant `w_n = min{m>a_n : m∉B_n}` (B1'-attack lever, step 2/3)
Computed the greedy `a_1..a_N` (N=120–200) and, for each `n`, `w_n = min{m>a_n : m shares no small prime ≤R with some a_i, i<n}`. Results:

| `a_1` | `R=rad(a_1)` | `len` | B1' violations | `w_n` non-decreasing? | `w_n` non-increasing? | `w_n-a_n` values |
|---|---|---|---|---|---|---|
| 15 | 15 | 200 | 0 | True | **False** | {1,2} |
| 35 | 35 | 200 | 0 | True | **False** | {1} |
| 77 | 77 | 200 | 0 | True | **False** | {1,2} |
| 91 | 91 | 200 | 0 | True | **False** | {1,2} |
| 105 | 105 | 200 | 0 | True | **False** | {1,3} |
| 135 | 15 | 200 | 0 | True | **False** | {1,2} |
| 175 | 35 | 200 | 0 | True | **False** | {1,2} |
| 385 | 385 | 150 | 0 | True | **False** | {1,2} |

The gap `u_n := w_n-a_n` is bounded (`≤3`) but oscillates (`1,2,1,1,…`, `1,3,1,…`) — not monotone in either direction. The aimo-0678 lever (non-increasing `w_n` while `a_n` climbs ⇒ `a_n ≤ w_n ≤ w_0` ⇒ `a_n` bounded) is inert here: `w_n` climbs with `a_n` and bounds nothing.

### Test B — finite-state determinism (step 4, the reduce-mod-lcm clincher)
For `a_1=15`, `L=30` (kernel product per current.md):

| state key | ambiguous? (# keys with >1 next residue) |
|---|---|
| `(a_n mod 30)` alone | **0/8** — deterministic ON the greedy orbit |
| `(a_n mod 30, σ_small(a_n))` | 0/39 |
| `(a_n mod 30, σ_small(a_n), σ_small(a_{n-1}))` | 0/85 |

The residue orbit is a single 8-cycle from `n=0`. This looks like a clean finite-state map — BUT it is deterministic *only because B1' holds and `M'_n` has already stabilized*; the transition `(a_n mod L) ↦ (a_{n+1} mod L)` on the periodic regime IS the cyclic successor of Theorem 1, not an independent bypass of B1'. The state that genuinely determines `a_{n+1}` is the full past small-support hitting family `M'_n`, which is finite ONLY under B1' (large primes excluded); off the periodic regime (e.g. in the consistent-prefix tree explored by the round-2 König scout) the same residue admits ≥20 infinite continuations with different `(T,L)`. So step 4 is conditional on step 3, which Test A refuted.

### Conclusion of the probe
The aimo-0678 crux shape is genuinely different in *proof shape* but does not transfer in *mechanism*:
- **Move (1) frozen invariant:** no analog. No coupled sequence, no conserved sum. The candidate `I_n = a_n mod L_*` fails (periodicity mod `R` is false; `L_*` is the kernel product, unknown a priori).
- **Move (2) min-of-failing-set monovariant:** REFUTED. `w_n` is non-decreasing, not non-increasing; the gap is bounded-but-oscillating. The non-increasing proof in aimo-0678 uses both the frozen invariant AND the explicit gcd/lcm recurrence — neither exists here.
- **Move (3) reduce-mod-lcm ⇒ finite-state ⇒ periodic:** conditional on (2); reimports B1' (the finite state is `M'_n`, finite only under B1') and re-derives Theorem 1, not a bypass.

ROUTE RETIRED. The field's only non-`M'_n`-stabilization attack on B1' is dead; B1' should be attacked via the spacing/covering mechanism (`small-prime-window-lemma`) or the transversal-duality mechanism (`hitting-set-monovariant`), not via a monovariant.
