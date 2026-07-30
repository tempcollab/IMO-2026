## imo-2026-03 — lens: Xiang Yu's defense / the UPPER BOUND

### Setup reduction (foundational, shared with all lenses)
The claiming phase ("alternately claim any unclaimed piece, each maximizing own
total") reduces to a pure combinatorial fact: **greedy take-the-largest-remaining
is optimal for both players** in an alternating "pick a number from a shrinking
multiset to maximize your own running sum" game (standard exchange/induction
argument — swapping a non-greedy pick for the greedy one never decreases your
total and never helps the opponent; NOT yet in `knowledge_base.md`, needs its
own short proof, but is completely standard). Given this, once all ≤2n marks are
placed, sort the resulting ≤2n+1 piece-lengths descending L_1≥L_2≥…≥L_m; Liu
Bang (first) ends up with L_1+L_3+L_5+…, Xiang Yu with L_2+L_4+…. **The whole
game collapses to a static optimization**: Liu Bang picks ≤n points (creating
≤n+1 intervals), Xiang Yu — seeing them — picks ≤n more points (subdividing
those intervals) to minimize the odd-rank sum. Flag this reduction lemma as a
prerequisite gap common to every approach; it should be proved once and shared.

### Numerical exploration (this round's main contribution)
I ran nested numerical optimization (Nelder–Mead inner minimization over Xiang
Yu's points, outer search over Liu Bang's points) in Python to find the true
value of c(n) for n=1,2,3, since a natural first guess is wrong (see Dead ends).

- **n=1** (hand-verified exactly, not just numerically): with Liu Bang's single
  mark at p, writing the 3 resulting pieces, Liu Bang's total = 1 − median.
  Case analysis (splitting the two sub-segments Xiang Yu can cut) gives Xiang
  Yu's best response value = (1+p)/2 for p≤1/3 and 1−p for p≥1/3; maximizing
  over p gives **p*=1/3, c(1) = 2/3**, exactly, attained (e.g. Xiang Yu cutting
  the remaining 2/3 into two 1/3's, or not cutting at all — both give exactly
  2/3; Xiang Yu is indifferent among several optimal replies).
- **n=2**: outer/inner numerical search converges to **c(2) ≈ 4/7 ≈ 0.5714**,
  attained by Liu Bang marking near **1/7, 3/7** (pieces of relative size
  1:2:4 in sevenths). Confirmed by refined local search (Nelder–Mead,
  restarts=200): the geometric config's inner-min holds firmly at 4/7 while
  many other configs (equal-fifths, random) top out lower.
- **n=3**: same search gives **c(3) ≈ 8/15 ≈ 0.5333**, attained by Liu Bang
  marking near **1/15, 3/15, 7/15** (pieces of relative size 1:2:4:8 in
  fifteenths). A "linear" competitor (odd multiples of 1/11) was numerically
  dominated (inner-min only 1/2, worse than 8/15), confirming the geometric
  pattern beats the naive equal-spacing pattern.

**Conjecture (numerically supported, not proved): c(n) = 2ⁿ/(2ⁿ⁺¹ − 1).**
Matches n=1 exactly (rigorously) and n=2,3 to high numerical precision.

### The extremal construction and WHY it's tight (mechanism for the upper bound)
Liu Bang's candidate-optimal marks: cumulative partial sums of powers of two,
i.e. at (2^i−1)/(2^{n+1}−1) for i=1..n, producing n+1 pieces of lengths
1,2,4,…,2ⁿ (units of 1/(2^{n+1}−1)). Xiang Yu's matching best response (found
by the optimizer, verified by hand for n=2): **bisect the n LARGEST of the n+1
pieces (one cut each), leave the single SMALLEST piece untouched.** Each
bisected piece of size 2^i becomes two pieces of size 2^{i-1}, i.e. matches the
next tier down. The final multiset is: 3 copies of the unit piece 2^0 (one
original untouched + two halves of the bisected 2^1-piece), and exactly 2
copies of each of 2^1,…,2^{n-1}. In sorted-descending order every tier of 2
equal pieces splits exactly 1-1 between the two players (two consecutive ranks
= one odd, one even); only the BOTTOM tier has an ODD count (3 copies), and
there Liu Bang — moving first — wins 2 of the 3. Summing: Liu Bang gets
½·(everything above the bottom tier) + ⅔·(the bottom tier) = 2ⁿ out of
2ⁿ⁺¹−1. **This is the mechanism that should drive the upper-bound proof**: an
odd "leftover" tier is unavoidable because Xiang Yu has exactly one cut fewer
than needed to bisect every one of Liu Bang's n+1 pieces, and Liu Bang's edge
is exactly the first-mover's win of that single 3-way (or generally odd-way)
tie.

### Distinct openings for the upper bound
1. **Direct adversary strategy + rank-parity counting** (the mechanism above):
   generalize "bisect all but the smallest piece" to an arbitrary Liu Bang
   marking (not just the geometric one), and show the resulting odd-rank sum
   is ≤ 2ⁿ/(2ⁿ⁺¹−1) for ANY input configuration, via an inequality on how
   bisecting redistributes rank-mass (each bisected piece contributes ≤ half
   to Liu Bang, with the "loss" bounded by an odd-tier/pigeonhole term).
2. **Induction on n with a self-similar halving reduction**: bisecting the
   largest piece and recursing looks like it reduces an n-piece problem to an
   (n−1)-piece problem on "half the mass" — worth checking if c(n) satisfies a
   clean recursion in terms of c(n−1) (I did not find one algebraically clean
   in the time available; f(n)=2ⁿ/(2⁙⁺¹−1) doesn't obviously satisfy a simple
   f(n) = g(f(n-1)) — flag for the outliner to check more carefully, may need
   working with 1−f(n) or a different recursive quantity/potential).
3. **Majorization / smoothing argument**: treat Xiang Yu's problem as, given
   the fixed vector of Liu Bang's n+1 piece lengths (summing to 1) and a
   budget of n more cuts to distribute among them, find the allocation
   minimizing the odd-rank sum; conjecture the minimizer is "bisect the n
   largest, leave smallest whole" by an exchange/majorization argument (swap
   any other allocation for this one without increasing Liu Bang's total).
   This targets a general Xiang-Yu-optimality proof, not just the extremal
   Liu Bang input.

### Cheap-kill candidates
- **First check**: verify whether "equalize to 2n+1 equal pieces of size
  1/(2n+1)" is really optimal for Xiang Yu — **it is NOT** (see Dead ends
  below); this rules out (n+1)/(2n+1) immediately and should save the outliner
  time.
- Parity/pigeonhole: count Liu Bang's n+1 pieces vs Xiang Yu's n cuts — Xiang
  Yu is always exactly one cut short of bisecting every piece, which is the
  structural reason an odd leftover tier is forced. This one-cut-short
  counting argument is a genuine cheap structural fact worth stating early.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (Combinatorics section) — for the "one
  cut short → odd leftover tier" counting argument.
- **Invariants & monovariants** — potential function tracking "total mass
  still contested / unequalized" across Xiang Yu's cuts.
- **Constructive / incremental** — building the geometric extremal
  configuration as an explicit family indexed by n.
- **Problem-Solving Heuristics: solve a simpler case first / specialize** —
  exactly how the n=1 case was cracked by hand; template for n=2,3 by-hand
  verification the outliner should replicate rigorously (not just trust my
  numerics) before committing.
- No entry in the KB currently states "greedy take-largest is optimal in the
  alternating claim game" — this foundational lemma needs its own short
  from-scratch proof (exchange argument), citing **General Proof Methods:
  Direct proof / induction**.

### Analogous past problems (crux corpus)
Searched `combinatorics` domain, subtopic `games-and-strategy` (39 entries) and
broader keyword search (bisect/halving/equalize/alternat/stick/interval) across
all domains. **No genuinely close analog found.** The games-and-strategy
entries are almost all pairing/mirroring/invariant strategies for discrete
combinatorial games (graph coloring, token games, placement games on boards) —
none involve continuous interval-cutting or a "claim the largest remaining
number" auction structure. Closest in spirit but not truly analogous:
- `aimo-0225` — game value determined by 2-adic valuation of a halving
  quantity (P/N status flips with parity of valuation): thematically close to
  the "odd leftover tier from repeated bisection" mechanism found here, worth
  a look for technique inspiration (dyadic/halving potential functions), but
  the problem itself (a token/counter game) is not analogous in structure.
- `aimo-0663` — pigeonhole on the number of contiguous gaps vs moves used, to
  guarantee a legal reply always exists: same *flavor* of counting argument
  (comparing available "slots" to remaining budget) as the "one cut short"
  observation here, but again a different underlying game.
None should be treated as a template to adapt directly; the outliner should
build the upper-bound proof from the direct construction/mechanism above
rather than force-fit a crux.

### Prior progress
None — `results/imo-2026-03/` is empty (fresh problem, round 1).

### Dead ends (do not retry)
- **"Xiang Yu equalizes into 2n+1 pieces of size 1/(2n+1) each" ⟹ Liu Bang
  gets (n+1)/(2n+1).** This is the naive generalization of a tempting
  n=1 coincidence and is WRONG for n≥2 — numerically disproved: for n=2,
  Liu Bang marking at 1/5,2/5 with Xiang Yu equalizing to five 1/5-pieces
  gives exactly 3/5, but Xiang Yu has a strictly better reply (bisect the
  large remaining piece + drop a near-zero sliver elsewhere) that forces Liu
  Bang down to 0.50, and against the TRUE optimal Liu Bang marking (near
  1/7,3/7) the ceiling is only 4/7≈0.571, not 3/5=0.6. **Do not present
  (n+1)/(2n+1) as the answer.** The correct-looking candidate is
  2ⁿ/(2ⁿ⁺¹−1).

### Small-case / intuition notes (labeled conjecture except n=1)
- n=1: **c(1) = 2/3**, proved by hand (case analysis above) — this can be
  taken as solid, not just conjectural.
- n=2: **c(2) ≈ 4/7**, numeric (Nelder–Mead, multiple restarts, refined grid),
  matches 2ⁿ/(2ⁿ⁺¹−1) to 4+ decimal places; the extremal marking is pieces of
  ratio 1:2:4 (marks at ~1/7, ~3/7), and I verified the exact value 4/7 by
  hand for that specific construction (bisect-two-largest response gives
  exactly 4/7 via the tier-counting argument above).
- n=3: **c(3) ≈ 8/15**, numeric, matches 2ⁿ/(2ⁿ⁺¹−1); extremal marking ratio
  1:2:4:8 (marks at ~1/15, 3/15, 7/15).
- Working conjecture for the whole problem: **c(n) = 2ⁿ/(2ⁿ⁺¹−1)**, with
  Liu Bang's optimal construction = cumulative powers-of-two partial sums, and
  Xiang Yu's optimal reply = bisect the n largest of Liu Bang's n+1 pieces and
  leave the smallest alone. This needs (a) a general upper-bound proof that
  no Liu Bang marking beats this value against optimal Xiang Yu play (my
  assigned focus — mechanism sketched above, not proved), and (b) a general
  lower-bound proof that Liu Bang's geometric marking guarantees this value
  against ANY Xiang Yu response (not just the bisection one) — that's a
  companion piece for a different explorer/approach.
