## imo-2026-03

**Answer (strongly conjectured, confirmed n=1 by hand + n=1..4 numerically):**
**c(n) = 2^n / (2^{n+1} − 1)** — c(1)=2/3, c(2)=4/7, c(3)=8/15, → 1/2⁺.

### Two reductions I verified this round (the spine every approach shares)
- **Greedy-claim Lemma G** (shared, → `lemmas/greedy-claim.md`): on a fixed multiset
  sorted descending, optimal alternating play gives Liu = odd-rank sum b_1+b_3+…. I
  brute-force-verified this equals the true minimax value on 2000 random multisets.
- **Discrepancy identity:** Liu = (1+D)/2, D = Σ(b_{2i−1}−b_{2i}) + [b_M if M odd].
  Since 2T_n − 1 = u := 1/(2^{n+1}−1) (the smallest dyadic piece), the whole problem is
  **equivalent to: minimax discrepancy D* = u** — Liu forces D ≥ u, Xiang forces D ≤ u.

### Numeric findings that reshape the plan (READ THIS)
- LOWER bound gap reduction holds **exactly and tight**: with Liu's dyadic partition
  (1:2:4:…:2^n), every ≤n Xiang response gives D/u ≥ 1 (min = 1.0, n=1..4).
- UPPER bound is the HARD gap. The explorers' proposed "Xiang bisects the n largest
  pieces" is **REFUTED** as a universal strategy (lets Liu reach 3/4 for non-geometric
  Liu partitions). Myopic "greedy minimize D one cut at a time" is **also refuted**
  (Liu 0.65 > 4/7 at n=2). **Xiang's optimal play is non-myopic/adaptive** — the n=1
  strategy is a threshold rule (bisect if p≤1/3, else pin the median). Do NOT let any
  builder reuse the bisection rule for the general upper bound.
- The value obeys a clean recursion **T_n = 2T_{n−1}/(2T_{n−1}+1)**, base T_0=1.

---

dyadic-discrepancy: new
Target: c(n) = 2^n/(2^{n+1}−1), both bounds + value.
Technique: greedy-claim Lemma G + discrepancy identity; explicit dyadic construction
  (lower) and explicit adaptive Xiang strategy (upper). Direct/constructive spine.
Skeleton:
  1. Position-independence: game depends only on final multiset — direct.
  2. Lemma G (shared): Liu = odd-rank sum — exchange/induction.
  3. Liu = (1+D)/2; answer ⟺ minimax D* = u.
  4. Lower: dyadic partition ⇒ D ≥ u for any ≤n Xiang cuts — domination (aimo-0117).
  5. Upper: adaptive Xiang strategy ⇒ D ≤ u for any Liu partition — equalize-pair/pin.
Key lemmas:
  - Liu = (1+D)/2 with D = Σ(b_{2i−1}−b_{2i})+[b_M odd] — because Σb=1 and Lemma G.
  - Dyadic D ≥ u — because g_k=2^k u exceeds Σ of all smaller pieces; Xiang has one cut
    too few (n cuts, n+1 pieces) to cancel every level, so ≥ u survives.
Open gaps: Lemma G optimality upper-half; GAP L (D≥u proof); GAP U (adaptive Xiang, THE
  hard one — bisection refuted).
Cases to cover: both bounds + value; Liu may use <n marks; Xiang <n marks; ties.
Watch out for: the refuted bisection rule; Lemma G tie handling; equality D*=u both ways.

induction-recursion: new
Target: c(n) = 2^n/(2^{n+1}−1) via induction on n.
Technique: prove c(n) = 2c(n−1)/(2c(n−1)+1) by a self-similar reduction of the n-game to
  the (n−1)-game; solve the recursion. Different wall from #1 (the size-reduction map,
  not endgame tier-counting).
Skeleton:
  1. Base n=0 (value 1), n=1 (2/3, hand).
  2. Lower half: Liu prepends a dominating top piece λ>1−λ over a scaled (n−1)-optimal
     instance; balance vs one Xiang cut ⇒ c(n) ≥ 2c(n−1)/(2c(n−1)+1).
  3. Upper half: Xiang spends one cut neutralizing Liu's top piece, reducing to an
     (n−1)-instance, apply IH ⇒ c(n) ≤ 2c(n−1)/(2c(n−1)+1).
  4. Solve recursion ⇒ 2^n/(2^{n+1}−1).
Key lemmas:
  - Recursion — because 1/T_n = 1 + 1/(2T_{n−1}) telescopes to 2 − 2^{−n} (verified).
  - Self-similar peel — top piece with λ>1−λ is claimed first, decoupling it so the
    residual is a scaled (n−1)-game.
Open gaps: both inductive halves; proving the top piece truly decouples (no cross-linking
  Xiang play); handling Xiang not spending the cut on the top piece.
Cases to cover: base cases; both halves; <n marks.
Watch out for: hand-waving "the rest is an (n−1)-instance" — must be exact over ALL Xiang
  responses; recursion is on the minimax value, not one strategy pair.

potential-certificate: new
Target: c(n) = 2^n/(2^{n+1}−1) via a single global weight/potential (minimax duality).
Technique: build w(ℓ) and potential Φ=Σw(piece) that upper-certifies Xiang and
  lower-certifies Liu at once — LP-duality/invariant framing, no explicit adversary play.
  Far from #1 and #2 (no construction-vs-adversary casework, no induction).
Skeleton:
  1. Shared base (Lemma G, discrepancy identity).
  2. Cut-budget: each Xiang split moves Φ by ≤ δ(w) (w concave) ⇒ n cuts = scalar budget.
  3. Odd-rank sum monotone in Φ ⇒ Φ-band bounds Liu both ways.
  4. Dyadic partition sits at the band edge (domination) ⇒ bounds meet at T_n.
Key lemmas:
  - Cut-budget bound — because w concave ⇒ w(x)+w(ℓ−x)−w(ℓ) bounded.
  - Φ↔odd-rank link — pairing consecutive ranks, each pair bounded by a w-difference.
Open gaps: EXISTENCE of a single w certifying both bounds (test on n=1,2 numerically
  first); sign/monotonicity consistency.
Cases to cover: construct explicit w; both bounds + value; n=1 median-pinning sanity.
Watch out for: may only certify the upper bound — then borrow #1's lower bound; sign
  errors silently invert the bound.

### Build-set recommendation
All three are new and far apart in framing (explicit strategies / induction-recursion /
global potential). Lemma G and the discrepancy identity are shared LEMMAS (isolate in
`lemmas/`), not shared framings, so a wrong Lemma-G proof doesn't sink the *routes*.
The hardest shared obstacle is the UPPER bound (non-myopic Xiang); the three approaches
attack it by genuinely different mechanisms (adaptive strategy / one-cut reduction /
dual certificate), so they should not die together on it.

Slugs created:
- **dyadic-discrepancy** — greedy lemma + gap identity; explicit dyadic construction
  (lower) and adaptive Xiang strategy (upper).
- **induction-recursion** — prove T_n = 2T_{n−1}/(2T_{n−1}+1) by self-similar n→n−1
  game reduction; solve for closed form.
- **potential-certificate** — one global weight w/potential Φ certifying both bounds via
  minimax duality, no explicit adversary play.
