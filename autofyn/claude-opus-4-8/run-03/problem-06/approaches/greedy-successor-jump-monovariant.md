## Status
unsolved (new approach — round 10)

## Framing (genuinely new: greedy-successor process potential, aimo-0678 transplant)

Every prior lane uses only that a_i is *some* element of E_∞ (a static covering term); the ONLY
certified fact using the greedy SMALLEST choice is Window Purity, and it is used passively. This lane
makes the **greedy successor rule itself** — a_{n+1} = smallest integer > a_n compatible with every
predecessor — the engine, via a **min-of-a-failing-set process potential with a freeze/jump phase
dichotomy**, exactly the mechanism that proves aimo-0678 (IMO 2015 SL N4) eventually periodic. The
contradiction target is the **certified gap bound a_{n+1}−a_n ≤ a_1**: if recruiting a new
load-bearing large prime forces the least available compatible integer to jump by more than a_1,
periodicity failure is impossible. This is far from the four exhausted static faces — it is a
dynamical monovariant on the actual process, not a covering-set reformulation.

## Skeleton (whole theorem)

1. **Setup.** Import certified `enumeration-of-E-infinity.md` (sequence = increasing enumeration of
   E_∞∩[a_1,∞)), `periodic-set-enumeration.md`, `csp-implies-theorem.md`, the **gap bound
   a_{n+1}−a_n ≤ a_1** (Current best), and `window-purity.md` (every integer in (a_n,a_{n+1}) is
   non-covering). Suffices to prove (CSP) ≡ (FIN-Q). *[imported, gap-free]*

2. **Assume failure ¬(FIN-Q).** Then (certified `finite-connector-pool-periodicity.md`) an inhabited
   bad class r_0 has an INFINITE large-connector pool: distinct large primes q_1<q_2<… each first
   become load-bearing (essential connector for some non-covering set, `essential-connector-
   equivalence.md`) at strictly increasing "activation" indices n_1<n_2<…

3. **Process potential.** Define the phase potential at each step from the greedy rule. Candidate:
   Φ_n := the least integer m>a_n that is compatible with a_1,…,a_n **using only small primes**
   (support ⊆ [2,P_max]); by Window Purity the actual successor a_{n+1} ≤ a_n + a_1, and every skipped
   integer in (a_n,a_{n+1}) fails compatibility against some predecessor. Split the process into:
   - **FREEZE phase:** steps where a_{n+1} is small-compatible (no new large prime is load-bearing) —
     here Φ behaves predictably / is controlled by the finite small-prime state mod L_0.
   - **JUMP phase:** a step n_k where activating a *new* large prime q_k is *forced* to keep the
     successor within the a_1-window. *[GAP 1 — define Φ so the phase split is clean and Φ is a genuine
     monovariant / bounded quantity, à la aimo-0678's non-increasing w_n]*

4. **Jump inequality (the crux mechanism).** At a JUMP step n_k, the color (predecessor a_i) that
   only q_k can re-hit means: to place a compatible successor within (a_{n_k}, a_{n_k}+a_1], the greedy
   rule must land on a **multiple of q_k**. Multiples of q_k are spaced q_k > P_max apart; if q_k > a_1
   the window (a_{n_k}, a_{n_k}+a_1] contains at most one multiple of q_k (certified `distinctness-by-
   difference.md`). Show this forces either (a) a SMALLER prime already covers that color (⟹ q_k not
   essential, contradiction), or (b) the least compatible integer exceeds a_{n_k}+a_1, contradicting
   the certified gap bound. *[GAP 2 — the load-bearing step: convert "new essential large prime" into a
   forced window overflow]*

5. **Monovariant / termination.** Aggregate: each JUMP consumes a resource that the FREEZE phase
   cannot replenish (aimo-0678: w_n non-increasing, finitely many jumps ⟹ bounded ⟹ finite state).
   Conclude only finitely many q_k activate ⟹ (FIN-Q) ⟹ theorem. *[GAP 3 — the aggregation: rule out
   infinitely many jumps, via a bounded/monotone Φ]*

## Key lemmas (claim + mechanism)

- **Gap bound a_{n+1}−a_n ≤ a_1.** — because a_1 shares a factor with every term (a_1's own primes),
  so a_n + (a_1-multiple) is always eligible within one a_1-window. Certified (Current best). Gap-free.
- **Window Purity.** — every integer in (a_n,a_{n+1}) is ∉E_∞, hence non-covering — from ENUM. Certified.
- **Large prime spacing.** — a prime q>window-length divides ≤1 integer per length-q window; certified
  `distinctness-by-difference.md`. This is the arithmetic that puts a new essential q in tension with the
  a_1-gap bound.
- **Jump forces overflow OR redundancy (THE GAP, GAP 2):** — because an essential large prime q_k is
  the *sole* connector to a color, a compatible successor hitting that color within the a_1-window must
  be a q_k-multiple, but consecutive q_k-multiples are q_k>a_1 apart ⟹ generically no q_k-multiple lands
  in-window ⟹ the color must actually be covered by a small prime (q_k redundant). Making "generically"
  rigorous (over all n, accounting for phase alignment) is the gap.
- **Finitely many jumps ⟹ periodicity.** — once no new large prime activates, the connector pool is
  finite ⟹ `finite-connector-pool-periodicity.md` gives the theorem. Certified (imported).

## Open gaps
- **GAP 1:** construct the correct process potential Φ_n whose FREEZE/JUMP dichotomy is clean and which
  is provably bounded or monotone (aimo-0678's w_n = min{m≥a_n : m∤s_n} analog). The invariant-sum s_n
  that makes aimo-0678 work has NO ready-made analog here — the candidate is a sum over active
  predecessors or the small-prime state mod L_0.
- **GAP 2 (crux-equivalent):** the jump inequality — a newly essential large prime q_k cannot be
  accommodated within the certified a_1-gap without either overflowing the window (contradiction) or
  being redundant (contradiction). This is where the greedy SMALLEST choice must do real work.
- **GAP 3:** aggregate finitely-many-jumps from the monovariant.

## Cases to cover
- q_k ≤ a_1 vs q_k > a_1 (spacing argument only bites for q_k > a_1; but load-bearing large primes are
  > P_max, and P_max can be < a_1 — cover q_k ∈ (P_max, a_1] separately, possibly via the small-prime
  state directly).
- Phase alignment: a q_k-multiple *could* land in-window for special n; must handle all n, not generic.
- The witnesses a_i ∈ W(r_0) are NOT confined off the a_1-lattice (recruitment-lens finding) — the
  argument must NOT assume witness terms live in a bounded window.

## Watch out for
- Do NOT let GAP 2 degrade into the per-window occupancy count (`minimal-linking-prime-extremal`,
  Lemma B) — that bounds a RATE, not a total, and is certified insufficient. The escape is that the
  greedy SMALLEST choice + gap bound gives a per-step CONSTRAINT (the successor must exist in-window),
  not just an occupancy statistic. Keep the argument local-per-step and tied to minimality.
- Do NOT reintroduce the bounded-value-band confinement (`distinctness-by-difference` as CLOSER) —
  (R2′) proved that vacuous. Here `distinctness-by-difference` is used only as the local spacing fact
  feeding the in-window tension, not to confine the pool.
- If Φ has no bounded/monotone form (GAP 1 fails), the phase split is cosmetic — flag honestly; the
  novelty is the process potential, and without a genuine monovariant this collapses to the wall.
