# Lemma MD2 (multiset doubling / subset enumeration) — CERTIFIED (round 11)

**Certification (round 11).** Reviewer-verified independently. `|M_i| = 2|M_{i-1}|` is immediate
from the disjoint-union construction; the leaf↔subset bijection (skip/reflect branch at each step)
is the same bijection underlying certified Lemma ESF-2 (subset-caterpillar), and the leaf value is
the descending-KK caterpillar of the include-set. Confinement to `[0, a_1]` is Lemma CONF at the
multiset level. Note only the **multiset** count `|M_i| = 2^i` is a theorem — the *distinct*-value
count `|R_{n+1}| = 2^{n+1}` is FALSE in the valley (all-equal counterexample, see below). Admitted.

**Statement.** Let `A = {a_1 ≥ … ≥ a_{n+1}}`. Define the reachable **multiset** `M_0 = {{0}}`,
`M_i = M_{i-1} ⊎ {{ |v − a_i| : v ∈ M_{i-1} }}` (each element contributes both itself and its
reflection `|·−a_i|`, with multiplicity). Then:
1. `|M_i| = 2^i` for all `0 ≤ i ≤ n+1`;
2. every element of `M_i` lies in `[0, a_1]` (Lemma CONF at the multiset level);
3. the support of `M_i` equals the reachable set `R_i`; `M_{n+1}` enumerates, with multiplicity,
   the descending-KK caterpillar value `v(T)` of each of the `2^{n+1}` subsets `T ⊆ {1,…,n+1}`
   (empty subset → `0`).

**Corollary (multiset pigeonhole).** Sorting the `2^{n+1}` values of `M_{n+1}` (all in `[0, a_1]`),
the `2^{n+1}-1` consecutive gaps sum to `≤ a_1 < L/2`, so some gap is `≤ a_1/(2^{n+1}-1) < u_n/2`.

**Proof.** (1) `M_i` is the disjoint union of a copy of `M_{i-1}` and its pointwise reflection, so
`|M_i| = 2|M_{i-1}| = 2^i`. (2) By Lemma CONF's induction, `v ∈ [0, a_1]` and `a_i ≤ a_1` give
`|v − a_i| ∈ [0, a_1]`. (3) At each step `i` the two branches ("keep `v`" = skip `a_i`, "reflect" =
include `a_i`) over `i = 1,…,n+1` form a bijection between the `2^{n+1}` leaves and the subsets `T`;
the first include from `0` sets the leader, subsequent includes fold in descending order, giving the
descending-KK caterpillar value of `T`. The corollary is the pigeonhole on the sorted list. ∎

**Scope — IMPORTANT limitation.** The corollary bounds a *gap* between two reachable values, which is
NOT itself reachable (the budget is exhausted realizing either endpoint), so it does NOT close the
Covering claim `cov(A) ≤ u_n`. The distinct-value pigeonhole (COUNT `|R_{n+1}| = 2^{n+1}`) is FALSE:
the all-equal profile `a_i = 1/(n+1)` (a genuine valley for `n ≥ 3`) has `R_i = {0, 1/(n+1)}` stable,
so `|R_{n+1}| = 2`. Thus MD2 is a structural enumeration fact, not a GAP→VALUE mechanism.
