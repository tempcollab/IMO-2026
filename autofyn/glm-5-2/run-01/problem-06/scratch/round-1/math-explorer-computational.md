## imo-2026-06 (computational-phenomenology lens)

### The problem (restated)
a_1>1 integer; a_{n+1} = smallest integer > a_n with gcd(a_{n+1}, a_i)>1 for EVERY i≤n. Prove ∃ T,L>0 with a_{n+T}=a_n+L for every n≥1. (Note: "for every positive integer n" — the claim is periodicity-from-the-start, NOT merely eventual. This matches the data: the pre-period is empty in every case observed.)

### Distinct openings surfaced
1. **Bounded-gaps + finite-state ⇒ periodic gap sequence.** Show d_n:=a_{n+1}-a_n is bounded (≤ some L), then the greedy's "state" (the active covering structure) lives in a finite set, so (d_n) is eventually periodic, giving a_{n+T}=a_n+Σ(d over one period)=a_n+L for n≥N. Then handle the "for every n" by showing the pre-period is empty (periodic from n=1).
2. **Kernel-prime-set S + residue greedy mod L.** Identify a finite "essential/kernel" prime set S (L=∏S squarefree); show every term is divisible by some p∈S and the residues {a_n mod L} form a finite set R closed under the greedy; periodicity of the residue traversal gives a_{n+T}=a_n+L.
3. **Common-prime dichotomy.** Split into (A) a single prime divides every term ⇒ T=1, L=that prime, AP trivially; (B) no common prime ⇒ build the kernel S and residue cycle. The even-a_1 case (T=1,L=2) is the cleanest sub-case (consecutive-integer coprimeness forces a_2=a_1+2).
4. **Induction on n with an explicit (T,L) constructed from a_1.** Define L and the residue set R from a_1 directly; prove a_{n+T}=a_n+L by induction, the greedy rule closing the induction via a shift-invariance of R mod L.

### Candidate technique(s)
- **Eventual periodicity mod m** (KB: "Order of an element / eventual periodicity of products of a sequence mod m"; "Linear recurrences: eventually periodic mod m"). The natural modulus is L=∏S.
- **Consecutive-integer coprimeness** gcd(k,k+1)=1 (KB: divisor analysis) — drives the even-a_1 case and the interruption mechanism.
- **Invariants / monovariants** (KB): the kernel prime set S is a monovariant (grows, then stabilizes); the "active residue set" is the invariant.
- **Pigeonhole on finite state** (KB): finite reachable states ⇒ eventual periodicity of the greedy.

### Cheap-kill candidates
- **Even a_1 ⇒ T=1, L=2 immediately**: gcd(a_1,a_1+1)=1 always, so a_2=a_1+2 (even), and inductively every term is even ⇒ 2 divides every term ⇒ a_{n+1}=a_n+2. This is a complete proof for a huge class of a_1 (all even). Rigorous and trivial.
- **Prime a_1 ⇒ T=1, L=a_1**: a_2=a_1+a_1=2a_1? No — empirically a_1=p prime gives T=1,L=p (e.g. a_1=7 → 7,14,21,...). Because a_2=2p (smallest >p divisible by p), a_3=3p,... all multiples of p. Clean sub-case.
- **a_1 = p^k (prime power) ⇒ T=1, L=p**: same logic (p divides a_1, and the only admissible numbers are multiples of p once all terms are multiples of p — needs the "pure power blocks intruders" fact).

### Knowledge-base entries to use
- "Order of an element, Fermat/Euler — eventual periodicity of products of a sequence mod m" (line 65)
- "Linear recurrences — sequences are eventually periodic mod m" (line 80)
- "Divisor analysis — consecutive-integer coprimeness gcd(k,k+1)=1" (line ~88)
- "Pigeonhole / extremal principle" + "Invariants & monovariants" (combinatorics section)
- (Not the Three-gap theorem — the gap structure here is finite-state, not Kronecker.)

### Analogous past problems (cruxes)
- **aimo-0079** (sequences-and-recurrences): "Reindex a sliding two-factor product so balancedness becomes a fixed-shift equality of per-term prime-count parity for all large arguments; pigeonhole over finitely many length-L window patterns to force two equal windows ⇒ periodicity." Analogous because it extracts periodicity from a prime-factor-parity condition over sliding windows — same flavor of "finite window patterns ⇒ eventual periodicity". The crux move (pigeonhole on length-L windows of a {0,1}-sequence) is adaptable to the residue-state sequence here.
- **aimo-0134** (sequences-and-recurrences): transfer eventual-constancy of a running average back to the original sequence via a difference identity. Tangentially analogous (eventual ⇒ pointwise) — could inspire the "pre-period empty" step.
- No crux in the corpus matches the greedy-gcd-covering structure directly; this problem appears novel relative to the bank. Do not force a closer match.

### Prior progress
None (round 1; workspace empty).

### Dead ends (do not retry)
None yet (no prior approaches). From this exploration: do NOT try to prove "the set P_n of all primes appearing stabilizes" — it does NOT (empirically P_n is unbounded: for a_1=35, primes 11,13,17,19,23,29,31,37,41,43,... keep appearing as free-riding factors of terms already divisible by 2,3,5,or 7). The stabilizing object is the *essential/kernel* prime set S, not P_n.

### Small-case / intuition notes (CONJECTURES — numeric evidence only, not proofs)

**Generated a_1=2..200 (1500 terms each) and odd composites up to 391 (8000–12000 terms). Period detected in EVERY case; the two stubborn cases (a_1=187=11·17, a_1=209=11·19) resolve at T=484,L=7854 and T=528,L=8778 respectively.**

**FACT 1 (conjecture, overwhelming evidence): The period holds FROM n=1 (a_1), i.e. the pre-period is EMPTY.** Verified for every a_1 in 2..59 and all tested odd composites: a_{n+T}=a_n+L for all n≥1, including n=1. E.g. a_1=15: a_1=15, a_9=45=15+30 (T=8,L=30). a_1=35: a_1=35, a_35=245=35+210 (T=34,L=210). a_1=77: a_1=77, a_19=231=77+154 (T=18,L=154). This is the load-bearing surprise: the theorem's "for every n" is literally true with transient 0.

**FACT 2 (conjecture): L is always squarefree and equals ∏(S) where S = primes dividing L (the "kernel").** Verified in all 30+ T>1 cases. S always contains 2 in the T>1 cases. Examples:
| a_1 | factorization | T | L | S=primes(L) |
|---|---|---|---|---|
| 15 | 3·5 | 8 | 30 | {2,3,5} |
| 35 | 5·7 | 34 | 210 | {2,3,5,7} |
| 65 | 5·13 | 58 | 390 | {2,3,5,13} |
| 77 | 7·11 | 18 | 154 | {2,7,11} |
| 91 | 7·13 | 20 | 182 | {2,7,13} |
| 95 | 5·19 | 82 | 570 | {2,3,5,19} |
| 105 | 3·5·7 | 58 | 210 | {2,3,5,7} |
| 135 | 3³·5 | 48 | 210 | {2,3,5,7} (7 NOT in a_1!) |
| 143 | 11·13 | 64 | 858 | {2,3,11,13} |
| 165 | 3·5·11 | 86 | 330 | {2,3,5,11} |
| 175 | 5²·7 | 274 | 2730 | {2,3,5,7,13} (13 NOT in a_1!) |
| 187 | 11·17 | 484 | 7854 | {2,3,7,11,17} (7 NOT in a_1!) |
| 209 | 11·19 | 528 | 8778 | {2,3,7,11,19} |
| 221 | 13·17 | 334 | 6630 | {2,3,5,13,17} |
| 323 | 17·19 | 94 | 1938 | {2,3,17,19} |
| 341 | 11·31 | 136 | 2046 | {2,3,11,31} |
| 391 | 17·23 | 110 | 2346 | {2,3,17,23} |

S is NOT simply primes(a_1): e.g. a_1=135 has S={2,3,5,7} (7 is extra); a_1=175 has S including 13 (extra); a_1=187 includes 7 (extra). The extra primes are forced by the interruption cascade — the proof must explain which primes enter S.

**FACT 3 (conjecture): T=1 ⟺ a single prime divides every term (a "common prime"); then L = that prime.** In every T=1 case the common prime is the smallest prime factor (spf) of a_1. T=1 occurs for: all even a_1 (L=2); all prime a_1 (L=a_1); all prime powers p^k (L=p); many odd composites p·q with p<q (e.g. 21=3·7→L=3, 55=5·11→L=5, 85=5·17→L=5, 119=7·17→L=7). 

**FACT 4 (the interruption mechanism — CONJECTURE, concrete examples):** For odd a_1=p·q, the AP a_1+(n-1)·p is either never interrupted (⇒ T=1, L=p) OR interrupted by a composite m < expected, using the larger prime q and the new prime 2.
- a_1=15=3·5: AP would be 15,18,21,...; **a_3=20 (not 21)** because 20=2²·5 < 21 and gcd(20,15)=5, gcd(20,18)=2. 2 enters via 18=2·3²; the larger prime 5 of a_1 supplies the multiple 20=4·5 sitting below 21=3·7. Sequence: 15,18,20,24,30,36,40,42,45,48,... (period 8, L=30 from n=1).
- a_1=21=3·7 (NO interruption): AP 21,24,27,30,...; the candidate 28=4·7 (=2²·7) is < 27? No — 28>27, and at a_4 (expected 30), 28 is already past; moreover 27=3³ is a pure power of 3, coprime to 28, blocking it. So the AP reaches the pure power 3³=27 safely, after which every term is a multiple of 3 and the AP locks. Sequence: 21,24,27,30,33,... (T=1, L=3).
- a_1=35=5·7: AP 35,40,45,...; **a_3=42 (not 45)** because 42=2·3·7 < 45, gcd(42,35)=7, gcd(42,40)=2. 2 enters via 40=2³·5; 7 supplies 42. Sequence: 35,40,42,45,50,60,70,75,80,84,90,100,105,...
- a_1=77=7·11: AP 77,84,91,...; **a_3=88 (not 91)** because 88=2³·11 < 91, gcd(88,77)=11, gcd(88,84)=2. Sequence: 77,84,88,98,110,112,126,132,140,154,...

**Interruption criterion (conjecture):** the AP a_1+(n-1)·p (p=spf) is interrupted iff, before the AP reaches the next pure power p^k (k≥2, p^k>a_1) — which is coprime to all non-p-multiples and would "lock" the AP — an admissible composite using q (the other prime) and 2 sneaks in below the expected AP term. a_1=p·q is interrupted iff some 2^a·q^b·(small) < the p^k that would lock. The exact criterion is intricate (e.g. 5·13 interrupted but 5·17 not; 7·11,7·13 interrupted but 7·17 not) — the proof likely does NOT need the exact criterion, only the dichotomy "lock or interrupt-into-finite-kernel".

**FACT 5 (conjecture): The residue set R = {a_n mod L : n in one period} is a proper subset of {r mod L : gcd(r,L)>1}, determined by the greedy on residues starting from a_1 mod L.** E.g. a_1=15: R={0,6,10,12,15,18,20,24} mod 30 (8 residues; note 15 is odd — no single prime divides all of R, confirming "no common prime" ⇔ T>1). a_1=35: |R|=34 residues mod 210. Same S={2,3,5,7}, L=210 can give different |R| for different a_1: a_1=35 (mod 210 = 35) → |R|=34; a_1=105 (mod 210=105) → |R|=58; a_1=135 (mod 210=135) → |R|=48. a_1=35 and a_1=245 (both ≡35 mod 210) → |R|=34 (SAME). So R depends on a_1 mod L, not on a_1's magnitude. Suggests the residue greedy is a finite deterministic walk on Z/LZ whose cycle is entered immediately (no tail) — consistent with FACT 1.

**FACT 6 (conjecture): "Passive primes" don't break periodicity.** New large primes keep appearing forever (for a_1=35, block 2 of the period introduces 29,31,37,41,43 as factors of 290,310,370,410,430,450,... which are all ≡ to S-divisible residues mod 210). These large primes are "passive": every term divisible by such a prime q is ALSO divisible by some kernel prime in S, so q imposes no new coverage obligation. This is why unbounded P_n coexists with exact periodicity.

### Facts a proof must establish (the load-bearing regularities)
1. **(Bounded gaps)** a_{n+1}-a_n is bounded (empirically ≤ L; max gap observed for a_1=187 is 22, for a_1=221 etc. small). Without this, no finite state.
2. **(Finite kernel S)** There is a finite set of primes S such that every term is divisible by some p∈S. (Equivalently: the "essential" covering primes stabilize — even though P_n is unbounded.) L=∏S.
3. **(Passive primes are harmless)** Any prime q∉S that divides some term a_n divides it together with some p∈S; hence q never creates a new coverage requirement. This is why the greedy state is captured by S alone.
4. **(Residue periodicity mod L)** The walk a_n mod L on the finite residue set R is periodic: ∃T with a_{n+T}≡a_n (mod L) for all n (and the right T is |R|, the cycle length).
5. **(Lift to equality, not just congruence)** From a_{n+T}≡a_n (mod L) and the gap bound, deduce a_{n+T}=a_n+L exactly (constant lift +1 per period) — not 0 or 2L. The bounded-gap + minimal-greedy should force the lift to be exactly L.
6. **(Pre-period empty / from n=1)** Strengthen "eventually" to "for every n≥1". Empirically always true; likely follows from the residue greedy being a single cycle with no tail (the state graph is a permutation on reachable states). This is the crux that elevates the problem to P6-difficulty.
7. **(Dichotomy T=1 vs T>1)** Either a common prime emerges (T=1, AP) or the kernel S has ≥2 primes with no single one covering all residues (T>1). Both yield a_{n+T}=a_n+L.

### Concrete data anchor (for the outliner's verification)
a_1=15 full first 15 terms: 15,18,20,24,30,36,40,42,45,48,50,54,60,66,70. Gaps: 3,2,4,6,6,4,2,3,3,2,4,6,6,4. Period-8 gap pattern (from a_2): 2,4,6,6,4,2,3,3 repeating. L=30=2·3·5. Residues mod 30 in visit order: 15,18,20,24,0,6,10,12 (then 15 again).
