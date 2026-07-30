## imo-2026-03

Answer (all approaches target this end to end): **c(n) = 2^n / (2^{n+1} − 1)**
(u := 1/(2^{n+1}−1); Liu total = (1 + D)/2 where D = odd-rank sum − even-rank sum;
minimax D = u). Three rival approaches, kept far apart in route. All share one
infrastructure lemma (Reduction Lemma R, greedy = odd-rank sum) — a short exchange
argument; if certified once it becomes a shared lemma importable by the other two.

VERIFIED this round (numerics/derivation): (i) identity D = measure{ t : #{pieces>t}
odd } holds on 20000 random multisets; (ii) dyadic pieces u·(1,2,…,2^n) give D_0 =
u·(2^{n−1}+2^{n−3}+…) and Xiang's optimal response drives D to exactly 1u for n=1,2,3;
(iii) recursion 1/D(n) = 2/D(n−1)+1 reproduces 2^n/(2^{n+1}−1), matching n=1..4.

---

induction-peel: new
Target: c(n) = 2^n/(2^{n+1}−1), both bounds, by strong induction on n.
Technique: strong induction via the recursion D(n) = D(n−1)/(2 + D(n−1)), D(0)=1;
peel off the largest piece + one cut to reduce the n-game to the (n−1)-game.
Skeleton: Reduction Lemma R → Liu=(1+D)/2 → base n=0,1 → lower bound: dyadic +
superincreasing peel of top piece 2^n (dominates sum of rest) → upper bound: adaptive
Xiang cut on a_1 reducing to CLAIM(n−1) → combine.
Key lemmas: recursion 1/D(n)=2/D(n−1)+1 (verified numerically); superincreasing
2^k > 2^0+…+2^{k−1} forces one uncancelled odd block ≥ u unless Xiang spends a top cut.
Open gaps: R (exchange arg); A1 (lower-bound peel: cost of attacking top = drop to n−1
budget); A2 (upper-bound peel: WHERE to cut a_1 adaptively so residual is a legit
CLAIM(n−1) instance — the hard part).
Cases to cover: lone dominant top piece vs. near-equal top two (adaptive cut differs).
Watch out for: "bisect the largest" is a DEAD END (fails Liu=(0.6,0.4), n=1); the peel
cut must depend on the ratio a_1 : (a_2+rest).

parity-measure-potential: new
Target: c(n) = 2^n/(2^{n+1}−1), both bounds, with NO induction on n.
Technique: the global identity D = measure{ t : N(t) odd } (N(t)=#pieces>t) plus a
parity-toggle calculus — one cut splitting s into s_1≥s_2 toggles parity of N on
exactly [0,s_2) and [s_1,s), two windows each of length s_2.
Skeleton: Reduction Lemma R → identity D = measure{N odd} (VERIFIED) → toggle calculus
→ lower bound: superincreasing caps how much odd-measure n toggles can cancel, residue
= u → upper bound: n adaptive toggles pair ranks (b_{2i−1}=b_{2i}) covering all but u
of the odd set → combine.
Key lemmas: D = measure{N(t) odd} (VERIFIED on 20000 multisets); a cut's leverage is
≤ 2·s_2 (smaller fragment); superincreasing ⇒ ≥1 cut needed per doubling scale.
Open gaps: R; B0/B1 (write up identity + toggle intervals — mechanical); B2 (KEY,
lower: odd-measure cancellation capped at u); B3 (KEY, upper: covering the odd set by
n toggles with residue ≤ u).
Cases to cover: Xiang using fewer than n cuts; overlapping toggle windows.
Watch out for: toggle windows can overlap and re-flip parity — the covering argument
must count net measure, not gross.

explicit-pairing-strategy: new
Target: c(n) = 2^n/(2^{n+1}−1), both bounds, via explicit strategies + combinatorial
matching (no induction, no measure integral).
Technique: explicit Liu dyadic construction and explicit adaptive Xiang
"recursive-doubling / Huffman-style greedy-merge" response; each bound proven by an
explicit injection/companion-pairing of final pieces into adjacent ranks.
Skeleton: Reduction Lemma R → Liu dyadic + Xiang greedy-merge (both explicit) → lower
bound: injection Xiang-pieces → strictly larger Liu-pieces, unmatched mass ≥ u → upper
bound: greedy-merge uses ≤ n cuts and each cut's fragment is the even-rank companion of
an odd-rank piece, Σ gaps ≤ u → combine; verify n=1,2 by substitution.
Key lemmas: superincreasing dyadic ⇒ top-dominates-tail at every scale (lower bound
injection); greedy-merge companion pairing makes ranks (2i−1,2i) near-equal twins.
Open gaps: R; C1 (KEY, lower: odd−even ≥ u for any splitting of dyadic); C2 (KEY,
upper: greedy-merge stays ≤ n cuts AND forces D ≤ u for EVERY Liu partition — adaptive
cut choice, companion-pairing residue ≤ u).
Cases to cover: near-equal top two (pair for free) vs. lone dominant top (must split);
Xiang running out of cuts before pairing everything.
Watch out for: DEAD ENDS "always bisect largest" and "always split smallest" both fail
globally — the merge must adaptively match the larger fragment down to the next piece.

---

Field rationale (diversity): the three routes share only Reduction Lemma R and the
D-reformulation; their engines are disjoint — (A) recursion on n, (B) a measure-theoretic
global identity, (C) explicit strategies + combinatorial injection — so they will NOT
die on the same wall. The common hard difficulty (the adaptive Xiang upper bound) is
attacked three different ways: A2 as a peel-recursion, B3 as a parity-covering, C2 as a
companion-pairing. If one framing's upper-bound gap proves refuted, the others are
independent. Crux borrowed: aimo-0117 dyadic-domination invariant (largest value exceeds
sum of the rest) underlies the superincreasing construction in all three.

build set: induction-peel, parity-measure-potential, explicit-pairing-strategy
