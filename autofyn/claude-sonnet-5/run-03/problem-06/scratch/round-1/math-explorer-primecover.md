## imo-2026-06

- **Distinct openings** (all under the "prime-cover / bookkeeping" lens):
  1. **Growth-rate / gap-bound opening.** Use a Zaremba/covering-grid-style bound (see
     the crux `aimo-0447` below) to show `a_{n+1}-a_n` cannot grow too fast — i.e.
     `a_n = O(n·polylog n)` or similar — which forces the number of *distinct* prime
     factors of `a_{n+1}` to be `O(log a_n) = O(log n)`, far smaller than the `n`
     gcd-constraints it must satisfy. Pigeonhole then forces many of the `i ≤ n` to be
     "served" by the *same* prime factor of `a_{n+1}` — i.e. a genuine covering-system
     structure emerges among a bounded number of primes. This is the natural route to
     "only finitely many primes ever matter."
  2. **Finite-prime-pool opening.** Directly attempt to show: there is a finite set of
     primes `P` such that every sufficiently large term is divisible by at least one
     member of `P`, and (key extra fact, NOT just "divides all terms" — see below)
     each `p ∈ P` divides a set of indices that is eventually periodic mod some `M_p`
     (arithmetic-progression-like). Combine via CRT into one global period `L =
     lcm(M_p)` and `T` from the pattern length. Empirical caution below: the "prime
     pool" is not simply "primes dividing every term from some point on" — see
     small-case notes; it's subtler (a covering-system pattern, not a single common
     divisor).
  3. **Difference/telescoping opening (bridge to aimo-0477's technique).** Track
     `gcd(a_1, a_n)` (or `gcd` with any early fixed term) as `n` grows: show it is
     eventually monotonic (non-decreasing, bounded by `a_1`) hence eventually
     constant, by an argument parallel to the ISL 2010ish problem `aimo-0477`
     (v_p-monotonicity per prime). This could give a foothold: once
     `gcd(a_1,a_n)` stabilizes at `d`, all sufficiently large terms share the factor
     `d` with `a_1`, shrinking the "who must be covered" bookkeeping.
  4. **Direct covering-system construction/uniqueness opening.** Treat the "primes
     used from some point on" as building a genuine **covering system** of the
     integers by residue classes mod small primes (à la Erdős's classical covering
     congruences), and argue the greedy process is *forced* to eventually settle into
     exactly such a system because it's the greedy (lexicographically smallest)
     choice — i.e. show uniqueness/stability of the covering pattern using
     minimality of the greedy rule (any deviation would have been chosen earlier).

- **Candidate technique(s):** prime factorization / v_p bookkeeping, pigeonhole on
  "which prime serves which constraint," covering systems / CRT combination of
  residue classes, growth-rate bounds on gcd-chains (grid/counting argument), and
  (secondarily) the v_p-monotonicity trick from `aimo-0477`.

- **Cheap-kill candidates:**
  - **Degenerate case first:** if `a_1` is a prime power `p^k` (e.g. `a_1=2,3`), EVERY
    later term must share a factor with `a_1`, and since `a_1`'s only prime is `p`,
    every term is forced divisible by `p`. Then the greedy rule collapses to "smallest
    multiple of `p` greater than the previous term," giving `T=1, L=p` trivially —
    confirmed by computation (`a_1=2` gives all evens, `a_1=3` gives all multiples of
    3, etc.). **This case is trivial and should not be over-invested in**; the real
    content is when `a_1` (or the early terms) have ≥2 distinct prime factors so no
    single prime is forced on all terms.
  - **Pigeonhole on prime-factor count vs. constraint count**: cheap structural fact —
    if `a_{n+1} - a_n` stays bounded (plausible from small-case data, gaps look like
    small constants, e.g. 2,3,4,6 in the size-15 example) then `a_{n+1}` has at most
    `O(log a_{n+1})` distinct prime factors, but must satisfy `n` gcd constraints; for
    large `n` this is way fewer primes than constraints, forcing heavy prime-reuse —
    this pigeonhole is probably the crux structural fact underlying the whole proof
    and costs little to state early.

- **Knowledge-base entries to use:** "Modular arithmetic, CRT" (combining residue
  classes mod several primes into one mod `lcm`), "Order of an element,
  Fermat/Euler: periodicity of products of a sequence mod m" (directly the flavor of
  conclusion we want), "Divisor analysis: gcd structure, consecutive-integer
  coprimality, bounding a finite search by size," "Pigeonhole / extremal principle."
  No entry in `knowledge_base.md` currently states a covering-system theorem by name
  — if the outliner needs one, it will have to be proved from scratch (Erdős covering
  congruences are not yet in the KB).

- **Analogous past problems (cruxes):**
  1. **`aimo-0447`** (crux domain=number_theory, subtopic=divisibility-and-gcd) — “Prove
     there is `c>0` such that if `gcd(a+i,b+j)>1` for all `i,j∈{0,...,n}` then
     `min{a,b} > (cn)^{n/2}`.” **Strongly analogous**: it is precisely a bound on how
     large numbers must be to satisfy a grid of pairwise gcd`>1` constraints, proved
     by placing a prime in each cell of an `N×N` grid and counting how few large
     primes can cover the grid (essentially the same "prime pool is scarce / bounded
     number of primes must do heavy lifting" argument our problem needs). Its crux
     move — *build an `n×n`(or here, `n×1`) grid of forced-shared-primes and count how
     many cells small primes can cover, forcing large primes or heavy reuse* — is the
     direct ancestor of Opening 1 above. Worth adapting the counting-argument
     machinery (not the exact bound, since our setting is `a_{n+1}` vs. ALL of
     `a_1..a_n`, a triangular/linear version rather than a square grid, but the
     "primes ≤X cover only O(N/p) cells each" counting idea transfers).
  2. **`aimo-0477`** (ISL, Mongolia; subtopic=divisibility-and-gcd/telescoping) —
     "sequence where a sum-of-ratios is eventually integer ⟹ eventually constant."
     **Partially analogous**: the technique of tracking `gcd(a_1,a_n)` (or here
     `δ_n = gcd(a_1,a_n,a_{n+1})`) and showing it is eventually monotonic via a `v_p`
     case analysis, then concluding stabilization, is a reusable pattern for Opening 3
     — but the underlying hypothesis (an integer sum of ratios) is different enough
     that this is a *technique* borrow, not a structural analogy of the whole
     problem.
  3. **`aimo-0421`** (a competition problem about infinite sets and gcd patterns) —
     the crux "if a prime `p` divides infinitely many elements of `S`, pick an element
     outside `S_p` and pigeonhole on the finitely many possible gcds" / "if every
     prime divides only finitely many elements of `S`, only finitely many elements
     fail to be coprime to a fixed pair" is a nice **general finiteness lemma** about
     infinite integer sets and primes, but the actual claim proved (existence of a
     "balanced triangle" of gcds) is not close to our problem's conclusion —
     **weaker analogy**, useful mainly as a reminder of the standard "prime `p`
     divides only finitely/infinitely many terms" dichotomy technique, not as a
     structural template.

- **Prior progress:** none — round 1, first exploration, `results/imo-2026-06/` is
  empty scaffolding (`current.md` Status: unsolved, no approaches, no lemmas).

- **Dead ends (do not retry):** none recorded yet (nothing has been tried). One
  thing to flag as a *likely-wrong simplification*: don't assume the "prime pool"
  consists of primes that divide **every** sufficiently large term — empirically
  false (see notes below); the correct invariant is a **covering-system pattern**
  over the pool, not a single common divisor.

- **Small-case / intuition notes (all conjectural, from direct computation):**
  - Computed the greedy sequence for `a_1 ∈ {2,3,4,6,9,10,12,15,21,33,35,45,65,77,
    105,143}` up to a few hundred–3000 terms (Python, exact gcd/greedy simulation).
  - **Trivial cases**: whenever `a_1` is a prime power (`2,3,4,6=2·3` behaves like
    2 forced... actually `a_1=6` still gives immediate period `T=1,L=2` since the
    greedy rule locks onto "next even number"), `21,33` (multiples of 3), the sequence
    becomes an arithmetic progression from term 1 with `T=1` (period is immediate,
    no "eventually" needed). These are the least interesting cases.
  - **Genuinely eventual-periodicity cases** (period only kicks in after transient):
    `a_1=15 → T=8, L=30`; `a_1=45 → T=8, L=30`; `a_1=35 → T=34, L=210`;
    `a_1=105 → T=58, L=210`; `a_1=65 → T=58, L=390`; `a_1=143 → T=64, L=858`;
    `a_1=77 → T=18, L=154`.
  - **Conjecture A**: `L` is always a multiple of the primes needed to "cover" all
    residues within one period, and empirically factors as products of 2, 3, and the
    prime factors of `a_1` — BUT NOT ALWAYS: `a_1=77=7·11` gives `L=154=2·7·11`
    (no factor of 3!), showing the pool isn't simply "2,3,and primes of a_1" — it's
    determined by the actual greedy dynamics, so this is a red herring; don't let the
    outliner assume a fixed formula for `L`.
  - **Conjecture B** (checked directly): NO single prime divides all sufficiently
    large terms in any of the "genuinely eventual" cases tested (computed the set of
    common prime factors over the last 200 terms of a 3000-term run — empty in every
    non-trivial case except the prime-power-`a_1` trivial cases). This DISPROVES the
    naive "the sequence eventually lives entirely on one prime" model and supports
    the **covering-system** picture instead: different terms in a period are covered
    by different primes from the finite pool, no single prime dominates.
  - **Conjecture C**: average gap size `L/T` seems to grow with the number of
    distinct primes in the pool (3.6–13.4 in samples), consistent with Opening 1's
    picture that as constraints accumulate you need either more distinct small
    primes or bigger gaps — worth the outliner treating `L/T` and pool-size as linked
    quantities rather than independent unknowns.
  - All of the above are **empirical/conjectural** — no proof yet that periodicity
    even occurs in general (it's the theorem to prove), only that it does in every
    sample tried, consistent with the target statement.
</content>
