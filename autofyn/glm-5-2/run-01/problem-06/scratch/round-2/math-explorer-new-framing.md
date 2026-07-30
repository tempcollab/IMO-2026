# imo-2026-06 — round-2 exploration: genuinely-different framing of B1

Scout route: challenge the B1 wall (kernel stabilization) by reframing, with DATA. All computations are conjecture-grade evidence, not proof.

## Terrain per framing

### (A) Difference-sequence direct (d_n = a_{n+1}-a_n ∈ [1,R], prove d_n eventually periodic via a finite state)
- DATA: d_n is bounded (≤ R, certified) and in fact MUCH smaller than R in practice (a_1=385, R=385, but maxdiff=14 over 5000 terms). The diff sequence for a_1=15 is periodic with the same T=8, L=30 from n=1.
- The "state that determines d_{n+1}" is the family of past small-prime supports (or the minimal-hitting-set family M_n). This state is finite ONLY IF the relevant primes are bounded — which is B1. The diff-sequence approach does not escape: to prove the state is finite you must prove large primes never enter the determining state, i.e. B1'.
- VERDICT: **REIMPORTS B1.** The finite-state for d_n is exactly the stabilized M_n; proving it finite is the wall. (Confirmed: d_n periodic from n=1 in every tested case, but the proof of periodicity reduces to B1'.)

### (B) "Large free-riders are along for the ride" — does the true greedy equal the small-prime-only greedy?
- DATA (KEY): For a_1 ∈ {15,35,77,91,105,135,175,187,221,385,95,143,65}, the TRUE greedy a_{n+1}=min(A_n∩(a_n,∞)) is IDENTICAL to the small-prime-only greedy a^{sp}_{n+1}=min(B_n∩(a_n,∞)) where B_n uses only σ_i=supp(a_i)∩{p≤R}. Verified for 300–1500 terms (a_1=15: 1500 terms, zero divergence). **Large primes (>R) NEVER provide a shortcut candidate below the small-prime minimum.**
- This IS B1 restated as a single clean claim (call it **B1'**): min(A_n∩(a_n,a_n+R]) = min(B_n∩(a_n,a_n+R]) for all n. It does not dissolve the wall, but it ISOLATES it: B1 is exactly "no large prime q>R dividing some past a_i yields a candidate m in (a_n, f_B(a_n)) that is admissible." The "seed a_N ∈ B" sub-gap and the "two-prime-set" confusion dissolve: with the right object (M_n, see below) there is only ONE claim.
- VERDICT: **ISOLATES B1 (does not dissolve, but cleans it to a single window-admissibility lemma).** This is the round's most useful reconnaissance: the field's "B1 = stabilize kernel S + coincidence + seed" collapses to the single statement B1'.

### (C) Block / Euclidean (a_n = R·q_n + s_n)
- a_n is divisible by SOME prime of a_1 (universal-small-prime), not all; a_n mod R is not special. Periodicity mod R is FALSE (certified: a_1=15, a_1≡a_5≡0 mod 15 but a_2≡3, a_6≡6 mod 15). The modulus must be L=∏S (kernel product), strictly larger than R. So the Euclidean decomposition mod R does not carry the period.
- VERDICT: **REIMPORTS B1.** The block decomposition needs L=∏S, which is the kernel — the wall.

### (D) Covering-system / CRT framing
- A_n = ∪_{h∈M_n}{multiples of m_h} is a union of residue classes mod M_n=rad(∏_{i≤n}a_i). The obstruction is precisely "the extra forbidden residues coming from large free-rider primes are a finite set mod L." This is B1' in CRT language: the greedy sees the same admissible residues as the small-prime lattice. No new mechanism.
- VERDICT: **REIMPORTS B1** (same wall, CRT dress).

### (E) aimo-0678 monovariant + reduce-mod-lcm (from crux corpus — the genuinely different MECHANISM)
- **BEST ANALOG: aimo-0678** (France): recurrence a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)-1; prove (a_n) eventually periodic. Crux = 3 moves: (1) find a frozen invariant / regime where recurrence simplifies; (2) construct a min-of-a-failing-set integer monovariant w_n=min{m≥a_n : m∤s_n}, prove NON-INCREASING ⇒ boundedness; (3) **once bounded, reduce the other coordinate mod lcm of attainable values ⇒ finite state ⇒ eventually periodic.** Move (3) is the clincher and is genuinely different from "stabilize S then apply Theorem 1": it bounds a COORDINATE (not the prime set) and reduces mod an lcm of attainable values.
- For our problem: the bounded coordinate is d_n (≤ R, already certified). The finite-state step would be: once M_n (small-prime minimal hitting sets) is stable, the greedy is a deterministic map on residues mod L=∏∪M_∞, finite ⇒ periodic. This is exactly Theorem 1's content — BUT the aimo-0678 move (3) arrives at it via "reduce mod lcm of attainable diff-values" rather than "exhibit the periodic set," a different proof shape. The gap is the SAME (B1'): move (3) needs the state finite, which needs large primes excluded.
- VERDICT: the finite-state clincher is a different PROOF SHAPE but still needs B1'. **Partial reimport; the monovariant move (2) is the unexploited lever** — see recommendation.

## Critical structural discoveries (DATA)

1. **The right stabilizing object is M_n (minimal hitting sets), NOT F_n (full small-prime support family).** F_n keeps GROWING: for a_1=15, the last new small-prime support appears at n=1141, |F|=28, ∪F={2,3,5,7,11,13} (all primes ≤R). The "stabilized" small-prime admissible set B_∞ would be 30030-periodic. BUT the true greedy has period L=30 (verified 1492 terms). Resolution: the extra small primes 7,11,13 appear ONLY in redundant support classes (each contains a kernel prime ∈{2,3,5}), so they impose no new constraint. The minimal hitting sets M_∞ = {{2,3},{2,5},{3,5}} (the 2-subsets of {2,3,5}), and the period is L=∏∪M_∞=30, NOT ∏∪F_∞=30030. **The `hitting-set-monovariant` route (un-built in round 1) had the RIGHT object; the `bounded-diff-finite-state` Lemma 3 (F_n stabilizes) is a red herring that over-counts the modulus.**

2. **The admissible set A_n = ∪_{h∈M_n}{multiples of m_h} is EXACT** (definitional identity), where M_n = minimal hitting sets of {supp(a_i):i≤n}. There is NO "shortcut" gap with this object: the greedy IS literally min(A_n∩(a_n,∞)). The ONLY question is whether M_n stabilizes. With M_n of FULL supports, large primes can in principle enter; with M_n of SMALL supports (σ_i=supp(a_i)∩{≤R}), the universe is automatically 2^{≤R} (bounded, stabilizes by Lemma 3) — BUT then A_n is the small-prime admissible set, and equality with the true greedy is B1'.

3. **Empirical kernel S = ∪M_∞ is always ⊆ {primes ≤ R}** (verified all 13 tested a_1: S factors of L are all ≤ rad(a_1)). 2 is ALWAYS recruited (every tested non-collapse case has 2∈S). M_∞ is either a singleton {{p}} (collapse, T=1, L=p) or the (k−1)-subsets of a k-set S (cross-intersecting). The singleton-collapse cases: a_1∈{21,33,55,63,69,85,119,231,273} all give T=1, L=smallest prime of a_1.

4. **From-n=1 (B2) holds in EVERY tested case** (empty pre-period for all 13 a_1, including stubborn a_1=187 T=484, a_1=221 T=334, a_1=175 T=274). Strong conjecture; no counterexample.

5. **Spacing fact (NEW mechanism, not tried round 1):** a large prime q>R divides AT MOST ONE integer in any window of length R (multiples of q are spaced q>R apart). So in (a_n, a_n+R], each large past-prime q "occupies" ≤1 slot. At n=40 (a_1=15): 3 large primes in past, only 2 window integers touched by them. The large-prime "shortcut threat" is SPARSE in the window — but nonzero, so spacing alone does NOT prove B1'; it is a necessary ingredient.

6. **Shift-invariance induction (framing E') is a DEAD END.** I tested whether a_{k+T} and a_k have the same prime support (needed for an L-shift-invariant admissible set). They do NOT: a_6=36={2,3}, a_14=66={2,3,11}; a_8=42={2,3,7}, a_16=72={2,3}. Even at the small-prime level, supports are NOT shift-periodic (66 picks up small prime 11). So the admissible set is NOT L-shift-invariant; an induction on support shift-invariance fails. The values a_{n+T}=a_n+L ARE periodic, but via M_n stabilization, not via support shift-invariance. (Recorded so the outliner does not retry this.)

## The single most promising NEW framing to open

**"Small-prime-lattice + window-admissibility lemma (B1')"** — a CLEAN REFRAMING of the crux, not a bypass.

The round-1 field framed B1 as "stabilize the kernel prime set S ⊇ primes(a_1), then the greedy is the cyclic successor on the S-admissible set, plus the seed a_N∈A sub-gap, plus the from-n=1 sub-gap." This bundles three things and uses the WRONG object (F_n) for the modulus, producing the false 30030-vs-30 tension. The clean reframe:

- **Use M_n (minimal hitting sets of SMALL supports σ_i=supp(a_i)∩{≤R}) as the object from the start.** M_n ⊆ 2^{{primes≤R}} is automatically bounded and stabilizes to M_∞ (this is just Lemma 3 + reduction to minimal hitting sets; certified machinery). The modulus is L=∏∪M_∞ (the KERNEL product, e.g. 30 not 30030), and A^{(S)}=∪_{h∈M_∞}{mult of m_h} is L-periodic. Theorem 1 ⇒ periodicity from n=N (stabilization index). **This part needs NO new proof — it is certified machinery + the (correct) observation that the modulus is the kernel product, not the full small-prime product.**

- **The wall, cleanly: B1' = "the true greedy coincides with the small-prime greedy" = "for every n, no large prime q>R yields a shortcut admissible candidate in (a_n, f_{B_n}(a_n))."** This is ONE claim (not three). The seed sub-gap dissolves: once the greedy is the small-prime greedy, the seed a_N∈A is automatic (the small-prime greedy stays in B by Theorem 1). B2 (from-n=1) remains as a separate clean sub-gap on the small lattice.

- **New mechanism to attack B1' (the spacing + covering bound):** in the window (a_n, a_n+R] of length R, each large prime q>R occupies ≤1 slot (spacing fact). A shortcut candidate m must (i) be divisible by some large prime q of a past term a_{i*} in a support class σ* that m small-misses, AND (ii) hit ALL other past terms. The lever: the number of past terms in the small-missed class σ* that are NOT multiples of any of m's large primes must be ≥1 (so m fails admissibility). This needs a covering bound: show |J*| (past terms in σ*) exceeds the covering capacity of m's ≤log_R(a_n+R) large primes. My crude count was INCONCLUSIVE (RHS ~ n·log n/R, LHS ~ n — RHS eventually exceeds LHS, wrong direction for a contradiction). So the counting needs refinement (e.g. restrict to the LAST period of class-σ* terms, which are few and close to a_n — a large prime of m can hit at most one of them by spacing). **This is the concrete open mechanism for the builder to attack; it is genuinely different from the refuted Bertrand/competing-candidate move (which compared dyadic ranges) and from the refuted profinite/injectivity moves.**

## Concrete slug suggestion(s)

### Slug 1 (RECOMMENDED, genuinely new framing): `small-prime-window-lemma`
Spine (2–3 hard steps):
1. **Reduction to the small-prime lattice (clean, uses certified machinery).** Define σ_i=supp(a_i)∩{≤R}, M_n=minimal hitting sets of {σ_i:i≤n} (⊆2^{{≤R}}, bounded). M_n stabilizes to M_∞ (Lemma 3). The small-prime admissible set A^{(S)}=∪_{h∈M_∞}{mult of m_h} is L=∏∪M_∞-periodic. The true admissible set A_n ⊇ A^{(S)} (small hit ⟹ hit). Note L is the KERNEL product (e.g. 30), NOT ∏∪F_∞ (e.g. 30030) — this is the correction to round-1's over-counting. [No gap beyond certified Lemma 3.]
2. **Window-admissibility lemma B1' (THE crux, new mechanism).** Prove: ∀n, min(A_n∩(a_n,∞)) = min(A^{(S)}_n∩(a_n,∞)) where A^{(S)}_n uses M_n (still-stabilizing). Equivalently: no m∈(a_n, f_{A^{(S)}_n}(a_n)) is admissible. Attack via the SPACING fact (each large prime q>R occupies ≤1 window slot) + a covering bound on the small-missed support class (refine the count to the last period of class-σ* terms near a_n, where spacing makes each large prime of m hit ≤1 of them). [GAP — the heart; new mechanism, not a rehash of refuted moves.]
3. **Periodicity (Theorem 1, certified).** Once B1' holds, the greedy = cyclic successor on A^{(S)} (after M_n stabilizes), giving a_{n+T}=a_n+L for n≥N, T=|A^{(S)}∩[0,L)|. [No gap — import `lemmas/periodic-set-iteration.md`.]
4. **From-n=1 (B2, separate).** Show the pre-period is empty on the small lattice: for n<N, no "prematurely valid" small-prime candidate steals the greedy. Empirically always true. [GAP — secondary, clean.]

Why it does NOT share the B1 wall (as framed in round 1): round-1's B1 was "stabilize the full prime kernel S (⊆{≤R}) then prove coincidence + seed." This slug (i) uses the AUTOMATICALLY-bounded small hitting-set family (no "is S finite?" question — it is, by Lemma 3), (ii) collapses the three sub-gaps (stabilization/seed/coincidence) into the single window-lemma B1', (iii) attacks B1' with the spacing fact (a window-density argument), which is a DIFFERENT mechanism from Bertrand (dyadic, refuted), profinite compactness (refuted), and injectivity (refuted). The wall is still B1' but it is now ONE clean claim attacked by a new mechanism.

### Slug 2 (build the un-built round-1 route with the corrected object): `hitting-set-monovariant` (REVISED)
The round-1 `hitting-set-monovariant` skeleton had the RIGHT object (M_n) but was never built, and its step 4 (monovariant ⇒ cross-intersecting) loops back to "bound active primes." REVISE it to use the small-prime M_n (automatically bounded) so step 4's "bound active primes" is FREE, and the ONLY remaining step is the cross-intersecting-closure monovariant (step 3 of that skeleton, the self-sustaining closure lemma) + B1'. This is the aimo-0678 move (2) (monovariant) adapted: the monovariant is "number of disjoint pairs in M_n" or "(|M_n|, Σ|h|) in well-order," now well-founded because M_n⊆2^{{≤R}} is finite for free. The crux becomes: show M_n reaches a cross-intersecting state (every pair of minimal hitting sets meets), at which point it is stable forever (self-sustaining closure). This is a FINITE-state descent, genuinely different from "stabilize S." Combined with B1' (or absorbing B1' by noting that the small-prime M_n is the object and large primes never enter minimal hitting sets because a small hitting set always exists with smaller product — a candidate argument for the builder to test).

## Dead ends (do not retry)
- **Shift-invariance induction (framing E'):** supports of a_{n+T} and a_n are NOT equal (a_6=36={2,3} vs a_14=66={2,3,11}; even small supports differ). The admissible set is NOT L-shift-invariant. An induction on support shift-invariance is invalid. (Tested, dead.)
- **F_n (full small-prime support family) as the modulus object:** over-counts the modulus (30030 vs the true 30); the extra small primes are redundant. Use M_n (minimal hitting sets) instead. (Diagnostic, not a "retry" — a correction.)
- Bertrand/competing-candidate (refuted round 1), profinite-compactness bypass (refuted round 1), injectivity/residue-transition bypass (refuted round 1) — all confirmed dead.

## Prior progress (current best, unchanged but clarified)
Certified machinery: bounded-diff (a_{n+1}-a_n≤R), universal-small-prime, Theorem 1 (cyclic successor ⇒ x_{k+T}=x_k+L from k=0), trivial cases (a_1 even→T=1,L=2; a_1=p^k→T=1,L=p). The problem reduces to B1' (single clean claim, this round's clarification) + B2 (from-n=1). All partial.

## Analogous past problems (cruxes)
- **aimo-0678 (BEST analog):** recurrence via gcd/lcm, prove eventually periodic. Crux = (a) frozen invariant in the simplifying regime; (b) min-of-a-failing-set integer monovariant, non-increasing ⇒ boundedness; (c) reduce mod lcm of attainable values ⇒ finite state ⇒ periodic. Move (c) is the finite-state clincher with a different proof shape than Theorem 1; move (b) is the unexploited monovariant lever for B1'/M_n stabilization. WHY analogous: both are "greedy-ish integer recurrence, prove eventually periodic" where the crux is bounding a coordinate/state, not identifying a prime set.
- **aimo-0930 (secondary):** p-sequence a_{n+1}=a_n+d_p(a_n); periodicity via multiplicative order of 2 mod p (orbit mod m periodic ⇒ sum over one period constant ⇒ lift). Same spirit as Theorem 1 (orbit on a finite residue set is a single cycle) but the "order" angle is a different mechanism if a modulus can be identified early. Less directly applicable (periodicity mod R is false here).
- No other corpus problem resembles ours closely; aimo-0678 is the genuine analog.

## Small-case / intuition notes (conjecture, not proof)
- B1' (no large-prime shortcut) holds in ALL 13 tested a_1 (300–1500 terms). CONJECTURE.
- B2 (empty pre-period) holds in ALL tested a_1. CONJECTURE.
- S=∪M_∞ ⊆ {primes≤R} in all tested cases; 2 always recruited (non-collapse cases). CONJECTURE.
- M_∞ is either singleton {{p}} (collapse) or (k−1)-subsets of a k-set (cross-intersecting). CONJECTURE.
- The kernel product L=∏S is the period; it is NOT ∏∪F_∞ (which over-counts redundant small primes). VERIFIED for a_1=15 (30 vs 30030).
- a_1=385 (R=385) has NOT settled in 5000 terms (period > 1500); the kernel S for 385 is large/recruits many small primes — the hardest test case; the outliner should not assume small T.
