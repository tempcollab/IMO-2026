## Status
unsolved

## Approaches tried
- (round 1, new) Work directly with the gap sequence d_n = a_{n+1}−a_n over a finite alphabet; pigeonhole a repeated block, then force exact global periodicity via an aimo-0680-style divisibility-squeeze. Deliberately avoids characterizing E_∞ or the prime set.

## Current best
d_n ∈ {1,…,a_1} for all n (bounded gaps). No periodicity yet.

## Target
Prove there exist T, L with a_{n+T} = a_n + L for every positive integer n.

## Technique (spine)
Treat the *difference sequence* (d_n) as the primary object. It is over a finite alphabet (Step 1). Find a repeated finite block by pigeonhole, then upgrade "the block repeats along a subsequence" to "the block-structure is exactly periodic for all n" using the crux move of **aimo-0680** (a divisibility-squeeze: two quantities both divisible by a large modulus, with difference too small to be a nonzero multiple, forcing equality). This is a third, structurally distinct wall — it neither analyzes the compatible set nor builds a finite automaton state.

## Skeleton
1. **Finite alphabet for gaps.** d_n = a_{n+1} − a_n ≤ a_1 (least multiple of a_1 above a_n is compatible), and d_n ≥ 1. So (d_n) is a sequence over {1,…,a_1}. — rigorous.
2. **Responsibility structure (GAP R1).** Attach to each step n a bounded "reason" for the gap (which prime/residue forced a_{n+1} to be where it is). Show the pair (d_n, reason_n) lives in a finite set, and that the local future is determined by a bounded suffix of this data along an infinite set of indices.
3. **Repeated block by pigeonhole.** Over the finite alphabet, some finite block of (d_n,reason_n) of length W repeats at infinitely many positions; extract two positions x < x' with identical length-W data and matching residues mod L₀ := ∏(primes of a_1).
4. **Divisibility-squeeze to exact periodicity (GAP R2, imports aimo-0680).** Let Δ = a_{x'} − a_x. Using compatibility (every term shares a prime with a_1, and residues mod L₀ match), show a_{x'+j} − (a_{x+j}+Δ) is (i) divisible by a growing modulus tied to the witness spacing and (ii) bounded by the gap bound, hence forced to 0 for all j — i.e. a_{x'+j} = a_{x+j} + Δ for all j ≥ 0. This is the aimo-0680 "discrepancy smaller than its forced modulus ⇒ vanishes" mechanism, transplanted.
5. **To all n.** Take T = x'−x, L = Δ; if needed choose the minimal repeating block and re-anchor to n=1 (experimentally the identity holds from n=1). Combine several responsibility-classes' periods via T = lcm(…) exactly as aimo-0680 unifies orbit rows.

## Key lemmas (claim + mechanism)
- **Bounded gaps** — least multiple of a_1 above a_n is compatible. Rigorous.
- **Repeated block (R1)** — finite alphabet {1,…,a_1} × (bounded reasons) ⇒ pigeonhole gives an infinitely-recurring block. Mechanism sound; the risk is defining "reason" so the local future truly depends only on it.
- **Squeeze upgrade (R2)** — because the discrepancy between the shifted and actual continuation is divisible by the witness spacing (from matched residues mod L₀ propagated by the greedy rule) yet bounded by a_1 per step, it must vanish. This is the load-bearing borrowed move; its validity here hinges on producing a genuine divisibility of the discrepancy — the part NOT guaranteed by analogy and needing a real proof.

## Open gaps
- R1 (finite "reason" alphabet with local-future determinism) and R2 (constructing the actual divisibility that powers the squeeze). R2 is the make-or-break: aimo-0680 has a natural divisibility (f^{y}−f^{j} divisible by y−j from the orbit structure); the analogous divisibility here must be manufactured and is not obvious.

## Cases to cover
- Combining multiple responsibility-classes into one global period via lcm (as in aimo-0680).

## Watch out for
- The squeeze needs an HONEST divisibility relation; if none can be produced, this route degrades to "eventual periodicity along a subsequence" only — record that as a dead end rather than hand-waving the squeeze.
- Do not silently import the covering characterization; if R2 requires it, this collapses into enum-covering and loses its diversity value.
