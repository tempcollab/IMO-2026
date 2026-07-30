# Lemma (Distinctness-by-Difference, local)

**Certified** (proof-reviewer, round 9). Source: `bounded-window-distinctness` Step 3. A clean elementary
value-difference fact, salvaged from a route otherwise proven dead as a closer (see scope).

## Statement
Let N≥1 and let I⊆ℤ be a set of integers all lying in a value-window of length N (max I − min I < N). If a
prime q>N divides two distinct elements A,B∈I, then q∣(A−B), yet 0<|A−B|<N<q forces q∤(A−B) — a
contradiction. Hence **a prime q>N divides at most one element of I.** Consequently the number of distinct
primes q>N dividing at least one element of I is at most |I|.

## Proof
q∣A and q∣B ⟹ q∣(A−B). If A≠B then |A−B| is a nonzero integer with |A−B|≤max I−min I<N<q, so 0<|A−B|<q,
whence q∤(A−B), contradicting q∣(A−B). So q divides at most one element. Assigning each prime q>N (that
divides some element) the unique element it divides gives an injection into I; hence ≤|I| such primes. ∎

## Scope / route status
TRUE and reusable, but the route that invoked it (value-difference distinctness against ¬(FIN-Q)) is
**dead as a closer**: the confinement it needs — clustering the new-large-prime-carrying witnesses into a
single bounded value-window — is provably *equivalent* to the connector pool Q(r_0) being finite
(`bounded-window-distinctness` (R2′): the large-prime-carrying witnesses in a fixed value-band [a_1,V)
are finitely many terms, so their pool is finite; contrapositive, Q(r_0) infinite ⟹ witnesses unbounded
in value). Thus distinctness can only bite where its conclusion is already assumed; the bound is local and
grows as O(N). Do NOT re-field value-difference counting against ¬(FIN-Q). The lemma itself is a valid
local tool for any *bounded-window* argument. Gap-free.
