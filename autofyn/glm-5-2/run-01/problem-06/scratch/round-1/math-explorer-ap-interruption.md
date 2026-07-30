## imo-2026-06

## Lens: greedy minimality and the AP-interruption mechanism

### Problem recap
a_1 > 1, a_{n+1} = smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for EVERY i ≤ n. Prove ∃ T, L > 0 with a_{n+T} = a_n + L for all n.

### Distinct openings (the route as a chain of lemmas)

**Lemma 1 (AP initiation):** a_2 = a_1 + p_min, where p_min = smallest prime factor of a_1.
- *Why plausible:* a_1 is divisible by p_min, so a_1 + p_min is the next multiple of p_min, hence gcd(a_1+p_min, a_1) ≥ p_min > 1. And no smaller m > a_1 can be a multiple of p_min. Any m in (a_1, a_1+p_min) is not a multiple of p_min; it can only hit a_1 via a different prime factor of a_1, but the next such multiple is ≥ a_1 + (next prime factor), which is ≥ a_1 + p_min.
- *Gap:* Need to verify no m in (a_1, a_1+p_min) hits a_1 via a non-p_min prime factor. Actually for a_1 = p·q (p<q), the number a_1 + q is a multiple of q but q > p so a_1+q > a_1+p. So a_1+p is indeed the smallest. VERIFIED computationally for all tested a_1.
- *Tools:* basic number theory, divisibility.

**Lemma 2 (AP continuation / interruption):** As long as ALL past terms are divisible by p_min, the AP a_n = a_1 + (n-1)·p_min continues (T=1, L=p_min). The AP is interrupted when a number m ∈ (a_n, a_n + p_min) (hence p_min ∤ m) hits all past terms via non-p_min primes.
- *Why plausible:* If all past terms share p_min, the next multiple of p_min hits them all via p_min. An interrupting m must use other primes.
- *Example (a_1=15=3·5):* AP step 3: 15, 18, [21 expected]. But 20 = 2²·5 ∈ (18,21) hits 15 via 5 and 18 via 2. Interruption! a_3 = 20 ≠ 21.
- *Example (a_1=143=11·13):* AP step 11: 143, 154, [165 expected]. 165 = 3·5·11 ∈ (154, 165), hits 143 via 11 and 154 via 11. No interruption at step 2, but 165 introduces prime 3 as a free rider.
- *Gap:* Characterizing WHEN interruption occurs. Key: a_1 must have ≥2 distinct prime factors (if a_1 = p^k, the AP never interrupts — VERIFIED: a_1=25,49,121,169 all give pure AP with step p).

**Lemma 3 (Bounded differences — THE KEY LEMMA, clean proof):** a_{n+1} - a_n ≤ R := rad(a_1) (product of distinct prime factors of a_1) for ALL n.
- *Proof:* Let P = set of prime factors of a_1. Every term a_i must satisfy gcd(a_i, a_1) > 1 (since a_i hits a_1), so every a_i is divisible by some p ∈ P. Consider m = ⌈(a_n+1)/R⌉ · R (the next multiple of R after a_n). Then m ≡ 0 (mod p) for every p ∈ P, so m is divisible by ALL primes in P. Since every past term a_i is divisible by some p ∈ P, and m is divisible by ALL p ∈ P, we have gcd(m, a_i) ≥ p > 1 for every i ≤ n. So m is a valid candidate. Therefore a_{n+1} ≤ m ≤ a_n + R. ∎
- *This is NON-CIRCULAR:* R = rad(a_1) is a fixed constant depending only on a_1. No dependence on the effective base or the greedy dynamics.
- *VERIFIED computationally:* 0 violations in 100 random tests (a_1 up to 8000).
- *Tools:* "Order of an element / Fermat-Euler" (periodicity mod m), "Divisor analysis" (rad, gcd structure), from knowledge_base.

**Lemma 4 (Finite effective prime set):** The "effective base" — the set of primes ≤ R that the greedy algorithm actually uses to determine choices — is finite (trivially, since primes ≤ R are finite) and stabilizes.
- *Why plausible:* The family of "small-prime-divisibility-sets" {primes p ≤ R : p | a_i} for past terms is a family of subsets of the finite set {primes ≤ R}. It is monotone (only grows as new terms are added) and finite, so it stabilizes after finitely many steps.
- *Gap:* This is a monovariant argument — the family only grows, and it's finite, so it stabilizes. But stabilization of the family doesn't immediately give periodicity (see Lemma 5).
- *Tools:* "Pigeonhole / extremal principle", "Invariants & monovariants" from knowledge_base.

**Lemma 5 (Finite-state periodicity — THE CRUX):** Once the small-prime-divisibility-set family stabilizes, the greedy choice a_{n+1} is eventually determined by (a_n mod L, the stable family), where L = product of all primes ≤ R. Since this state is finite, the sequence of states is eventually periodic, giving periodic diffs.
- *Why plausible:* The "small-prime-hitting candidates" (numbers whose small-prime-set hits every past term's small-prime-set) are periodic mod L and ALWAYS valid (hitting via small primes implies gcd > 1). The greedy m ≤ the smallest small-prime-hitting candidate > a_n (which is ≤ a_n + R by Lemma 3's proof). If the greedy always picks a small-prime-hitting candidate, the transition is deterministic on (a_n mod L, family), giving periodicity.
- *THE GAP (hardest step):* The greedy might pick a SMALLER candidate that is NOT small-prime-hitting, using a large prime q > R as a shortcut. This "deviation" depends on the actual value of a_n (not just a_n mod L), because the multiples of q in (a_n, a_n+R] depend on a_n's actual position. The crux is showing these deviations EVENTUALLY STOP — i.e., for large enough n, no large-prime shortcut is valid, and the greedy always picks a small-prime-hitting candidate.
- *Intuition for why deviations stop:* A non-small-prime-hitting candidate m misses some past term a_i via small primes. To be valid, m must hit a_i via a large prime q > R. As the family stabilizes and more past terms accumulate, the number of "missed" past terms grows. m can only have finitely many large prime factors (≤ log₂(a_n+R)), so it can't hit an unbounded number of missed past terms via large primes. Eventually, no non-small-prime-hitting candidate in the gap is valid.
- *CIRCULARITY RISK:* The argument "missed past terms grow" assumes the deviations don't change the small-prime family. But deviations introduce new terms whose small-prime-sets might not be in the stable family, re-extending the family. RESOLUTION: the family stabilizes to include ALL subsets of {primes ≤ R} that can appear, regardless of deviations. A deviation term a_{n+1} ≤ a_n + R has primes ≤ a_n + R, and its small-prime-set (primes ≤ R) is one of finitely many subsets. So deviations don't extend the family beyond the finite set of all subsets. The family stabilizes to a superset of all possible small-prime-subsets, regardless of deviations. No circularity.
- *Tools:* "Linear recurrences" (eventual periodicity mod m), "Invariants & monovariants" from knowledge_base. The aimo-0678 technique: "reduce mod lcm of bounded values, finite states → periodicity."

### Candidate "state" definition (the natural finite state)

The state at step n is: **(a_n mod L, F_n)** where:
- L = product of all primes ≤ R = rad(a_1) (the "small-prime modulus"),
- F_n = the family of small-prime-divisibility-sets of {a_1, ..., a_n}, i.e., F_n = {{p ≤ R : p | a_i} : 1 ≤ i ≤ n} ⊆ 2^{primes ≤ R}.

This state is finite: |a_n mod L| ≤ L choices, |F_n| ≤ 2^{2^{π(R)}} choices (bounded). Once F_n stabilizes to F, the state is (a_n mod L, F), which has at most L · 1 = L values. If the transition is deterministic on this state, periodicity follows with period ≤ L.

### The crux step flagged

**The single hardest step is Lemma 5's gap: proving that large-prime shortcuts eventually stop, so the greedy choice becomes determined by the finite state (a_n mod L, F).**

Three approaches the outliner could try:
1. **Direct argument:** Show that for large n, every non-small-prime-hitting candidate in (a_n, a_n+R] is invalid (misses some past term via both small and large primes). This requires bounding the "coverage" of large primes.
2. **Absorption argument:** Show that large-prime deviations are "absorbed" — they introduce terms whose small-prime-sets are already in F, so F doesn't change, and the deviation doesn't propagate.
3. **Bypass the gap entirely:** Find a different invariant or monovariant that directly gives periodicity without needing the greedy to be deterministic on the state. (E.g., show the diffs themselves are eventually periodic via a direct argument on the bounded-diff structure.)

### Cheap-kill candidates
- **Prime power case (a_1 = p^k):** The sequence is a pure AP with step p. T=1, L=p. Proof: every term must hit a_1 = p^k, so every term is divisible by p. The next multiple of p is a_n + p, which hits all past terms (all divisible by p). So a_{n+1} = a_n + p. TRIVIAL.
- **Even a_1 (2 | a_1):** Every term must hit a_1, so every term is even (divisible by 2). The next even number after a_n is a_n + 2, which hits all past terms via 2. So a_{n+1} = a_n + 2. T=1, L=2. TRIVIAL. (VERIFIED: a_1=6,30,210,2310 all give step 2.)
- **So the only interesting case is odd a_1 with ≥2 distinct prime factors.**

### Knowledge-base entries to use
- **Order of an element, Fermat/Euler** — periodicity of sequences mod m; the core of the finite-state argument.
- **Divisor analysis** — rad(a_1), gcd structure, consecutive-integer coprimality.
- **Pigeonhole / extremal principle** — finite states → eventual periodicity (the final step).
- **Invariants & monovariants** — the small-prime-divisibility-set family is a monovariant (only grows, finite, stabilizes).
- **Linear recurrences** — eventual periodicity mod m (analogous structure).

### Analogous past problems (cruxes)
- **aimo-0678** (France, gcd/lcm recurrence): The crux move is "bound one coordinate, reduce the other mod lcm of bounded values, show the pair (a_n, r_n) is finite and deterministic → eventually periodic." DIRECTLY analogous: here, the diffs are bounded (Lemma 3), residues mod L are finite, and the transition is (almost) deterministic. The aimo-0678 solution's second approach (reduce b_n mod M = lcm of all a_n values, show (a_n, b_n mod M) is finite and deterministic) is the template. The difference: here a_n is unbounded (grows), but the DIFFS are bounded, and the "state" is (a_n mod L, F), not (a_n, b_n mod M).
- **aimo-0477** (sequence with integer sum): The crux is "d_n = gcd(a_1, a_n) is nondecreasing and bounded by a_1, so stabilizes; then a_{n+1}/d divides a_n/d, giving descent." The "gcd chain stabilizes" technique is analogous to our "small-prime-divisibility-set family stabilizes." The difference: our stabilization is about the family of subsets, not a single gcd chain.
- **aimo-0611** (Zsigmondy + periodicity): Uses "x_n > product of all earlier terms → primitive prime exists" and "periodicity mod x_k → primitive prime contradiction." The periodicity-mod-m technique is relevant but the specific Zsigmondy argument is not (our sequence doesn't grow fast enough).

### Prior progress
None (empty workspace, round 1).

### Dead ends (do not retry)
- **"a_n + rad(a_1) is always valid":** FALSE. For a_1=15, a_3=20, a_3+15=35, gcd(35,18)=1. The correct statement is "the next MULTIPLE of rad(a_1) is always valid" (i.e., ⌈(a_n+1)/R⌉·R), NOT "a_n + R." These are different because a_n + R might not be a multiple of R.
- **"max diff ≤ 2·p_min":** FALSE for a_1=221=13·17 (maxdiff=34=2·17, not 2·13=26). The correct bound is rad(a_1) (Lemma 3).
- **"max diff ≤ 2·max_prime_factor(a_1)":** FALSE for a_1=175=5²·7 (maxdiff=21 > 2·7=14).
- **"effective base = {2} ∪ prime_factors(a_1)":** FALSE for a_1=143=11·13 (effective base is {2,3,11,13}, not {2,11,13}). The prime 3 enters as a free rider and becomes load-bearing.
- **"every term has ≥2 primes from {2}∪P":** FALSE for a_1=221 with base {2,13,17} (some terms have only 1 base prime, requiring prime 3 or 5 to join the base).

### Small-case / intuition notes (CONJECTURES, not proved)
- **Period and L values (verified computationally, not proved):**
  - a_1=15=3·5: T=8, L=30=2·3·5. Diffs period: [3,2,4,6,6,4,2,3].
  - a_1=77=7·11: T=18, L=154=2·7·11.
  - a_1=91=7·13: T=20, L=182=2·7·13.
  - a_1=143=11·13: T=64, L=858=2·3·11·13.
  - a_1=221=13·17: T=334, L=6630=2·3·5·13·17. (VERIFIED over 1500 terms.)
  - a_1=105=3·5·7: T=58, L=210=2·3·5·7.
- **Conjecture:** L = product of the "effective base" primes, which is always a subset of primes ≤ rad(a_1). The effective base includes 2 (for odd a_1), the prime factors of a_1, and possibly other small primes (3, 5, ...) that enter as free riders.
- **Conjecture:** The effective base stabilizes to a set S ⊆ {primes ≤ rad(a_1)} such that the "≥2-of-S" pattern (or more generally, the hitting-set pattern) is self-sustaining: every term has enough S-primes to hit all past terms, and no prime > rad(a_1) is needed.
- **Conjecture on L:** L = lcm of the effective base primes (verified: 30=2·3·5, 154=2·7·11, 858=2·3·11·13, 6630=2·3·5·13·17).
- **The effective base grows by absorbing small free-rider primes until the hitting pattern is self-sustaining.** For a_1=77=7·11, base {2,7,11} suffices (every term has ≥2). For a_1=143=11·13, base {2,11,13} doesn't suffice (some terms have only 1), so 3 joins → base {2,3,11,13}. For a_1=221=13·17, base {2,3,13,17} might not suffice, so 5 joins → base {2,3,5,13,17}.

### Concrete interrupting examples (with numbers)

**a_1=15=3·5, first interruption at n=3:**
- a_1=15, a_2=18=2·3² (AP step 3, but 2 enters as free rider)
- Gap (18, 21): 19=prime (misses 15), 20=2²·5 (hits 15 via 5, hits 18 via 2). a_3=20.
- After this, diffs become periodic: [3,2,4,6,6,4,2,3] with L=30, T=8.
- Every term mod 30: [15,18,20,24,0,6,10,12] — each divisible by ≥2 of {2,3,5}.
- All primes in sequence are UNBOUNDED (7,11,13,...,127 appear in first 200 terms), but they're free riders (always accompanied by ≥2 base primes).

**a_1=221=13·17, interruption and large-prime shortcut:**
- a_1=221, a_2=234=2·3²·13, a_3=238=2·7·17, a_4=255=3·5·17 (ODD — not even!)
- a_4=255 is chosen because even numbers 240-254 in (238,255) all miss 221=13·17 (not divisible by 13 or 17). The odd 255=3·5·17 hits 221 via 17, 234 via 3, 238 via 17.
- Max diff = 34 = 2·17 (occurs when going to an even multiple of 17 that's the only valid candidate).
- Period T=334, L=6630=2·3·5·13·17. The effective base is {2,3,5,13,17}.

### Summary for the outliner
The route has 5 lemmas. Lemmas 1-4 are clean (AP initiation, interruption, bounded diff via next-multiple-of-rad, finite effective base via monovariant). Lemma 5 (finite-state periodicity) is the crux: show the greedy choice is eventually determined by (a_n mod L, stable small-prime family). The bounded-diff lemma (Lemma 3) is the linchpin — it's clean, non-circular, and uses only the fact that the next multiple of rad(a_1) is always a valid candidate. The outliner should focus on Lemma 5's gap (large-prime shortcuts eventually stop) or find a bypass.
