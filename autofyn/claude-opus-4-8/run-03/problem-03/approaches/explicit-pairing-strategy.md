## Status
unsolved

## Approach: explicit-pairing-strategy (framing C — explicit strategies for BOTH players + a combinatorial pairing/injection)

Target (the whole claim): c(n) = 2^n/(2^{n+1} − 1). This route commits to fully explicit
strategies — Liu's dyadic construction and Xiang's "recursive-doubling / Huffman-style
greedy-merge" response — and proves each bound by an explicit PAIRING (injection) of the
final pieces into adjacent ranks, with no induction on n and no measure identity. It is
kept far from the other two: the analysis is a direct combinatorial matching of pieces,
not a recursion or an integral.

### Preliminary — Reduction Lemma R (shared)
Same LEMMA R: Liu's total = odd-rank sum b_1+b_3+…; Xiang gets the even ranks. Write
D = Liu − Xiang = Σ (−1)^{i+1} b_i, Liu = (1+D)/2. Target: minimax D = u := 1/(2^{n+1}−1).
[GAP R shared.]

### Explicit constructions
- **Liu's construction:** cut so his n+1 pieces have lengths u·2^k, k = 0..n (cut points
  at (2^k−1)/(2^{n+1}−1), k=1..n). Superincreasing: 2^k > 2^0+…+2^{k−1}.
- **Xiang's response strategy (adaptive, explicit):** process pieces largest-first;
  repeatedly take the two largest UNPAIRED fragments and, if unequal, cut the larger so
  its top fragment equals the smaller — pairing them at equal size (a "greedy merge").
  On Liu's dyadic input this is exactly "split each 2^k into two 2^{k−1}'s, top down,"
  which uses n cuts and yields the multiset whose sorted form pairs perfectly except for
  one leftover u-piece.

### Skeleton
1. Reduction Lemma R and D-form. — exchange argument.
2. **Lower bound (Liu guarantees ≥ c(n)) via an explicit adjacency-pairing:**
   Liu plays dyadic. For ANY Xiang response (≤ n cuts), exhibit an INJECTION from
   Xiang's pieces (even ranks) to strictly larger Liu pieces (odd ranks) such that the
   unmatched Liu mass is ≥ u. Mechanism: superincreasingness ⇒ when the final pieces are
   sorted descending, the partial sums satisfy a "top piece dominates the tail" relation
   at every dyadic scale, forcing at least one uncancelled odd block of size ≥ u.
   [GAP C1 (KEY, lower bound): construct the injection / adjacency argument showing
   odd-rank sum − even-rank sum ≥ u for every Xiang splitting of the dyadic multiset.
   Candidate concrete form: track, scale by scale (t in each band [2^{k−1},2^k)u), that
   the number of fragments exceeding the band's floor is odd unless Xiang spent a cut in
   that band; with only n cuts across n+1 scales, at least the base scale keeps its odd
   block of width u. Cross-checked: numerics give min D = 1u exactly for n≤3.]
3. **Upper bound (Xiang holds Liu ≤ c(n)) via the explicit greedy-merge + companion
   pairing:** For an ARBITRARY Liu partition a_1 ≥ … ≥ a_{n+1}, run the explicit
   greedy-merge Xiang strategy; prove it uses ≤ n cuts and forces D ≤ u. Analysis by a
   COMPANION PAIRING: each cut Xiang makes creates a fragment that becomes the immediate
   even-rank companion (rank 2i) of some odd-rank piece (rank 2i−1), so in the sorted
   final list ranks (2i−1, 2i) are a matched near-equal pair with gap accounted for; sum
   the gaps.
   [GAP C2 (KEY, the hard part): prove the explicit greedy-merge strategy (a) never
   exceeds n cuts on an (n+1)-piece input, and (b) leaves Σ(b_{2i−1} − b_{2i}) + tail
   ≤ u for EVERY input. The load-bearing sub-claim: after processing, every descending
   adjacent gap b_{2i−1} − b_{2i} is "paid for" by a distinct cut, and the total unpaid
   residue is at most the smallest scale u. Beware the DEAD ENDS: neither "always bisect
   the largest" nor "always split the smallest to pair the top two" works globally — the
   greedy-merge chooses the cut adaptively (match the larger fragment down to the next
   piece). Must handle the case where Liu leaves two near-equal top pieces (Xiang pairs
   them for free with a smaller cut) vs. a lone dominant top piece (Xiang must split it).]
4. Both bounds meet at u ⇒ c(n) = (1+u)/2 = 2^n/(2^{n+1}−1); verify n=1 (2/3), n=2 (4/7)
   by direct substitution. ∎

## Approaches tried
- (this file) explicit-pairing-strategy: explicit dyadic (Liu) + greedy-merge (Xiang),
  both bounds reduced to explicit piece-pairings/injections.

## Current best
Fully explicit strategies for both players (dyadic construction; recursive-doubling /
greedy-merge response) plus the D = odd−even reformulation. Both bounds reduced to two
explicit pairing gaps (C1 injection for the lower bound, C2 companion-pairing for the
upper bound). Extremal Xiang response on the dyadic verified numerically to give D = u.

## Open gaps
- GAP R (shared): greedy Reduction Lemma.
- GAP C1 (KEY): lower-bound injection — odd−even ≥ u for any splitting of the dyadic.
- GAP C2 (KEY): upper-bound — greedy-merge uses ≤ n cuts and forces D ≤ u for any Liu
  partition (adaptive cut choice; companion-pairing bounds the residue at u).
