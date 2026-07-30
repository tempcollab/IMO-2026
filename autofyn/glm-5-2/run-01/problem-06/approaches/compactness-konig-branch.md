# Approach: compactness-konig-branch

## Status
partial

## Approaches tried
- (none — round 1 seed)

## Current best
**Bounded-difference lemma (CLEAN, imported):** `a_{n+1} - a_n ≤ R := rad(a_1)` for all n. This bounds the sequence's local growth, which is the entry point for a compactness/descent argument.

**Empirical anchor:** the period holds FROM n=1 in every tested case (pre-period empty). This suggests the right object is a single infinite branch through a finitely-branching tree of consistent residue histories — a König's-lemma / compactness move.

## Proof skeleton

Target: ∃ T,L>0 with `a_{n+T} = a_n + L` for every n ≥ 1.

Technique (spine): **non-constructive existence via König's lemma on the tree of consistent finite residue-histories.** Distinct from all other routes: it NEVER bounds the active-prime set explicitly (no B1 step) and never names a monovariant. It argues that an infinite consistent residue-history exists (compactness), and that any infinite path in a finitely-branching tree is eventually periodic (a graph-theoretic fact), yielding the result. The crux becomes "finite branching of the history tree," which requires a DIFFERENT bound (a local one, via the rad(a_1) gap) rather than a global kernel bound.

1. **Bounded differences (imported).** `a_{n+1} - a_n ≤ R`. [GAP: none — clean lemma.]

2. **Reformulate as a residue-history tree.** Fix a modulus `M = R` (to be refined). Define the *history tree* `T`: a node at depth n is a tuple `(r_1, …, r_n)` with `r_i = a_i mod M`, such that there EXISTS a valid sequence `b_1, b_2, …, b_n` with `b_1 ≡ a_1`, `b_{i+1}` the greedy-least valid continuation of `(b_1,…,b_i)`, and `b_i ≡ r_i (mod M)`. The root is `(a_1 mod M)`. Children extend by one step. The actual sequence `(a_n)` defines one infinite path. [GAP: the tree is well-defined; the modulus M = R may need refinement to a larger fixed modulus once the kernel is implicitly captured — but the compactness route aims to AVOID pinning the kernel, so we work mod R and accept that residues may repeat with different "states".]

3. **Finite branching (THE CRUX of this route — a LOCAL bound, not B1).** Show each node has finitely many children. Mechanism: the next residue `r_{n+1} = a_{n+1} mod M` is constrained by `a_{n+1} ∈ (a_n, a_n + R]`, so `r_{n+1} ∈ {r_n + 1, …, r_n + R} mod M` — at most R choices for the residue. BUT two different actual values `a_{n+1}` with the same residue mod M could correspond to different future behavior (if they use different large primes). So finite branching of RESIDUES is not enough; the node must carry enough state to make the future deterministic. [GAP: define the node state so that (a) it is finite-branching and (b) it determines future transitions. Candidate: node = (residue mod M, the family of small-supports of past terms restricted to primes ≤ R). This brings back a finite-family bound (2^{π(R)} subsets) — finite, so OK. But then this route secretly re-imports a finite-state argument. The DISTINCTIVE escape: argue that even WITHOUT a fully-deterministic state, the set of POSSIBLE infinite paths is compact, so AT LEAST ONE periodic path exists — and then argue the greedy picks it.]

4. **König's lemma ⇒ an infinite path.** If T is finitely-branching and has nodes of arbitrary depth (the real sequence gives this), then T has an infinite path. [GAP: finite branching (step 3).]

5. **Infinite path in finitely-branching tree ⇒ eventually periodic.** Any infinite path in a finitely-branching tree with finitely many node-types visits some node-type infinitely often; between two visits to the same node-type, the path is a finite loop; hence the path is eventually periodic. (This is the standard "finite directed graph ⇒ eventually periodic walk" fact.) So the residue sequence is eventually periodic mod M. [GAP: needs the node-types finite — same as step 3's state.]

6. **From periodic residues mod M to `a_{n+T} = a_n + L`.** Eventually `a_{n+T} ≡ a_n (mod M)` with constant lift; bounded diffs give the lift is a constant `L`, and `M | L`. Minimality of the greedy forces the lift to be the minimal period-compatible value. [GAP: pin down L precisely and prove lift = L not kL — same lift step as other routes. Also: M = R here, so L is a multiple of R, consistent with empirical `L = k·R`.]

7. **From-n=1 (the distinctive strength of compactness, IF it works).** Argue by the TREE structure: if the infinite path is a single cycle (the node-type visited repeatedly is the root-type), then periodicity holds from n=1. Mechanism: compactness gives existence of a periodic path; if we can show the greedy is DETERMINISTIC (unique path), then the existing periodic path IS the greedy path, and from-n=1 follows. [GAP: determinism of the greedy path in the tree — i.e. each node has exactly ONE child that extends to an infinite path. This is the crux of the from-n=1 step and possibly the whole route. Mechanism: if two children extended infinitely, both would be valid greedy continuations, contradicting the greedy's uniqueness (a_{n+1} is the LEAST valid, hence unique). So the greedy path is the UNIQUE infinite path. Then if any periodic path exists, it must be the greedy path — and from-n=1 follows IF the periodic path is a single cycle from the root.]

## Key lemmas (claim + one-line mechanism)
- **Bounded diffs ≤ rad(a_1)** — imported.
- **History tree is finitely branching** — because next residue ∈ a window of size R mod M (local bound); the hard part is making the node-state finite without re-importing B1.
- **Infinite path ⇒ eventually periodic** — finite directed graph ⇒ eventually periodic walk (standard).
- **Greedy path is the UNIQUE infinite path** — because the greedy picks the unique least valid continuation, so at each node exactly one child is the greedy child; hence the (unique) periodic path, if it exists, IS the greedy path.
- **Periodic path is a single cycle from the root** — (the deepest gap) needs the root to lie on the cycle, not in a tail.

## Open gaps (builder fills)
- Step 3: finite branching with a state rich enough to determine the future, WITHOUT re-importing the full B1 kernel bound. (This is the gamble: can compactness avoid B1? If not, this route collapses to bounded-diff-finite-state.)
- Step 6: lift from congruence mod M to equality with the right L.
- Step 7: uniqueness of the infinite greedy path + the cycle contains the root (from-n=1).

## Cases to cover
- Trivial (even / prime-power a_1): tree degenerates to a single residue class, T=1, L=p.
- Hard case: full tree argument.

## Watch out for
- The compactness route GAMLES on avoiding the B1 (active-prime) bound. If finite branching secretly requires B1, this route collapses to `bounded-diff-finite-state`. Flag this explicitly — do not pretend compactness magically avoids B1.
- König's lemma needs FINITE branching; infinite branching gives no conclusion. The residue-window alone (R choices) may not suffice because the future depends on which large primes were used. The node-state must be enriched, and that enrichment is where B1 may sneak back in.
- The "unique infinite path ⇒ it is the periodic one" move (step 7) requires that a periodic path EXISTS — which is what we're trying to prove. The argument is: compactness gives an infinite path; finite-state gives it is eventually periodic; uniqueness gives the greedy path equals it. Read carefully for circularity.
- This route is the highest-variance: it could yield the cleanest proof (if compactness + uniqueness close) or collapse entirely (if B1 is unavoidable).
