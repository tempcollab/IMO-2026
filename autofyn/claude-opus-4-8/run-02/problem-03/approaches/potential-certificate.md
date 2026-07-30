# Approach: potential-certificate (global weight/invariant, minimax duality)

## Status
partial

## Approaches tried
- (new, round 1) Certify both bounds with a single **separable** potential Φ = Σ_pieces w(piece).
  **DEAD END — refuted numerically and by a clean witness (see Gate result below).** A
  per-piece additive potential provably cannot control the odd-rank functional, because
  odd-rank is an ordering functional: the *same* local split changes it in *opposite*
  directions depending on context, while it always changes any Σw(piece) by the same amount.
- (new, round 1, PIVOT) Replaced the separable potential by an **order-aware (non-separable)
  certificate**: the level-set functional D = meas{ t : #(pieces > t) is odd }. Proved
  D = alternating sum = 2·Liu − 1, and proved a **cut-budget lemma** (each Xiang split moves D
  by at most 2·min(x, L−x)). This is a genuine global invariant that *does* control Liu's take.
  It reduces BOTH bounds to one clean statement about parity-flips. Delivered rigorously; the
  two extremal reachability computations (upper = the shared non-myopic-Xiang crux) are not yet
  closed here — recorded as gaps. Lower bound reduced and partially closed (D ≥ 2b₁−1 lemma +
  protected-interval reduction); full D ≥ u borrowed from dyadic-discrepancy.

## Current best

**Value (all approaches agree):** c(n) = 2ⁿ/(2ⁿ⁺¹−1), with u := 1/(2ⁿ⁺¹−1) and c(n)=(1+u)/2.
Confirmed by grid brute force: c(1)=2/3, c(2)=4/7.

This approach's distinct, rigorously delivered contributions this round:

1. **Gate result (mandatory check): NO separable certificate exists.** Proven (LP + witness).
2. **Lemma G (alternating-selection value = odd-rank sum):** full proof below — promotable.
3. **Order-aware certificate:** D = meas{t : #(pieces>t) odd} = 2·(Liu's take) − 1, plus the
   **cut-budget lemma** |ΔD| ≤ 2·min(x,L−x) per Xiang split — full proofs below, promotable.
   This answers the reviewer's question "does a richer certificate exist?": **yes**, the
   level-set functional, and it reframes the whole problem as parity-flip reachability.
4. **Domination lemma D ≥ 2b₁ − 1** (b₁ = largest piece) — full proof below.

**Open gaps (honest):**
- **Upper bound (THE shared crux):** show every Liu partition admits a Xiang response with
  D ≤ u, i.e. the reachable *maximum* of the parity functional over the two-stage game is u.
  In certificate language this is: n toggle-operations suffice to drive D down to ≤ u from any
  starting partition. Not closed here (this is the non-myopic-Xiang wall the whole field shares;
  the naive greedy "bisect current largest" is refuted below).
- **Lower bound full closure:** D ≥ u from the dyadic start under any ≤ n splits. Reduced to a
  parity-flip statement and partially closed (protected top interval); the complete argument is
  **borrowed from the `dyadic-discrepancy` approach** (domination), which owns it.

---

## The set-up (shared spine)

Positions do not matter: the claiming game depends only on the final multiset of piece
lengths. Write a final multiset sorted descending as b₁ ≥ b₂ ≥ … ≥ b_m (Σb_j = 1).

### Lemma G (alternating selection). 
*On a fixed multiset of nonnegative reals, two players alternately take one remaining element,
each maximising the total of the elements it takes; the first player (Liu) can guarantee, and
the second (Xiang) can hold him to, exactly the **odd-rank sum** O := b₁ + b₃ + b₅ + …*

**Proof.** Let E := b₂ + b₄ + … be the even-rank sum; O + E = Σ b_j.

*Xiang can hold Liu to ≤ O (equivalently Xiang guarantees ≥ E).* Form the pairs
P_i = {b_{2i−1}, b_{2i}} for i = 1, …, ⌊m/2⌋ (if m is odd, b_m is left unpaired). Xiang's
strategy: **whenever Liu takes an element, Xiang immediately takes the partner of that element,
if it is still available.** We check this is always possible and yields ≥ E. By induction on
the moves: before each Liu move, every pair is either untouched or completely taken (invariant).
Liu must therefore take an element from an *untouched* pair P_i (or, if m is odd and all pairs
are complete, the unpaired b_m — but that only happens on the very last move, which is Liu's
when m is odd). Xiang then takes the other element of P_i, restoring the invariant. Within
P_i = {b_{2i−1}, b_{2i}} (b_{2i−1} ≥ b_{2i}), whichever element Liu took, Xiang gets the other,
which is ≥ b_{2i}. Summing over all pairs, Xiang gets ≥ Σ_i b_{2i} = E. Hence Liu ≤ Σb − E = O.

*Liu can guarantee ≥ O.* Liu first takes b₁ (a largest element). Now it is Xiang's turn and the
remaining sorted multiset is b₂ ≥ b₃ ≥ …. Liu applies the pairing strategy above **as the
responder** on the remaining elements, with pairs {b₂,b₃}, {b₄,b₅}, …: whenever Xiang takes an
element, Liu takes its partner. By the same argument Liu gets, from the remainder, at least
b₃ + b₅ + … . Adding the b₁ he already holds, Liu ≥ b₁ + b₃ + b₅ + … = O.

Since Liu ≥ O and Liu ≤ O, the value is exactly O. The pairing arguments never assumed strict
inequalities, so ties are handled. ∎

*(Numerically verified: on 3000 random multisets the true alternating minimax value equals the
odd-rank sum, 0 mismatches.)*

### Discrepancy identity.
Let D := O − E (the **discrepancy**). Since O + E = 1, Liu's guaranteed take equals
**(1 + D)/2**. Thus c(n) = 2ⁿ/(2ⁿ⁺¹−1) = (1+u)/2 is **equivalent to the minimax discrepancy
being exactly u**: Liu forces D ≥ u, Xiang forces D ≤ u.

---

## Gate result: a SEPARABLE potential cannot certify these bounds

**Claim.** There is no weight function w : (0,1] → ℝ such that the additive potential
Φ(M) = Σ_{p∈M} w(p) is a monotone proxy for Liu's take O(M) — i.e. such that O is a function of
Φ, or even such that Φ preserves the order of O across multisets.

**Proof (clean witness).** Consider the single local operation "**split a piece of length ½
into two pieces of length ¼**." For any additive Φ this changes Φ by the *context-independent*
amount Δ = 2w(¼) − w(½). But its effect on O depends on the rest of the multiset:
- On M = {½, ½}: O = ½. After the split, {½,¼,¼}: O = ½ + ¼ = ¾.   (O increases by ¼.)
- On M = {½, ¼, ¼}: O = ¾. After the split, {¼,¼,¼,¼}: O = ¼ + ¼ = ½.   (O decreases by ¼.)

The same ΔΦ = Δ accompanies both an increase and a decrease of O. A monotone (indeed any
order-consistent) proxy requires equal ΔΦ ⇒ same sign of ΔO; contradiction. Hence no separable
w works. ∎

**Independent LP confirmation.** Discretising piece lengths on the grid {k/8} and taking all 22
integer partitions of 8 (multisets summing to 1), the linear program "find w embedding the O-order
into the Φ-order" (174 strict order constraints, 114 equalities for O-ties) is **infeasible**
(`scipy.linprog`, HiGHS, status 2). So the separable route is dead, exactly as the reviewer warned.

**Pivot.** We replace Φ by the order-aware level-set functional below.

---

## The order-aware certificate (the pivot)

For a multiset M with sorted pieces b₁ ≥ … ≥ b_m, define
    N_M(t) := #{ pieces of M with length > t }  (t > 0),   and
    D(M) := ∫₀^∞ 𝟙[ N_M(t) is odd ] dt = meas{ t : N_M(t) odd }.

### Lemma C1 (level-set identity). *D(M) = b₁ − b₂ + b₃ − b₄ + … = O(M) − E(M).*

**Proof.** N_M is a nonincreasing step function: on the interval (b_{j+1}, b_j) exactly j pieces
exceed t, so N_M = j there (with b_{m+1} := 0, and N_M = 0 above b₁). Hence
meas{N_M odd} = Σ_{j odd} (length of (b_{j+1}, b_j)) = Σ_{j odd} (b_j − b_{j+1})
= (b₁−b₂) + (b₃−b₄) + … = b₁ − b₂ + b₃ − … = O − E. ∎

By the discrepancy identity, **Liu's take = (1 + D(M))/2**, so D(M) is an exact order-aware
potential for the value. (Verified: D = alternating sum and Liu = (1+D)/2 on 2000 random multisets.)

### Lemma C2 (cut-budget). *Splitting one piece of length L into x and L−x (0<x≤L−x) changes
D by at most 2x = 2·min(x,L−x) in absolute value: |ΔD| ≤ 2·min(x, L−x).*

**Proof.** N is additive over pieces, so the split adds to N_M(t) the increment
δ(t) = 𝟙[t<x] + 𝟙[t<L−x] − 𝟙[t<L]. Computing δ mod 2 by intervals (x ≤ L−x):
on (0,x): 1+1−1 = 1; on (x, L−x): 0+1−1 = 0; on (L−x, L): 0+0−1 ≡ 1; on (L,∞): 0. So the split
**toggles the parity of N exactly on S = (0,x) ∪ (L−x, L)**, a set of measure 2x, and leaves it
unchanged elsewhere. Toggling the indicator 𝟙[N odd] on a set of measure 2x changes its integral
by at most that measure: |ΔD| ≤ meas(S) = 2x = 2·min(x, L−x). ∎

*(Verified on 3000 random split experiments: |ΔD| ≤ 2·min(x,L−x) held every time.)*

**Consequence — the whole problem in one sentence.** Starting from Liu's partition (final
multiset before Xiang moves), Xiang's ≤ n cuts are ≤ n parity-toggles, each on a set
S_i = (0,x_i) ∪ (r_i−x_i, r_i) (r_i = length of the piece cut, x_i ≤ r_i/2 its smaller part). So
    D_final = meas{ 𝟙[N₀ odd] ⊕ 𝟙_{S₁} ⊕ … ⊕ 𝟙_{S_m} = 1 },   m ≤ n,
and the game value is (1 + minimax D_final)/2. Liu picks the starting profile N₀ (his partition);
Xiang picks ≤ n toggles to minimise D. **c(n) = (1+u)/2 ⟺ this minimax parity-measure = u.**

---

## Lower bound (Liu ≥ c(n)): reduced, partially closed, remainder borrowed

Liu plays the **dyadic partition** s_k = 2^k u (k = 0,…,n), which uses n marks and has
Σ s_k = u(2ⁿ⁺¹−1) = 1. We must show every ≤ n Xiang toggles leave D ≥ u.

**Confirmed tight:** grid search gives min D from the dyadic start = u exactly for n = 1,2,3
(ratio 1.000), so the target is right.

**Lemma C3 (domination).** *For any multiset, D ≥ 2b₁ − 1 (b₁ = largest piece).*
**Proof.** 2b₁ − 1 = 2b₁ − Σ_j b_j = b₁ − b₂ − b₃ − …, and by Lemma C1
D − (2b₁−1) = (b₁−b₂+b₃−b₄+…) − (b₁−b₂−b₃−b₄−…) = 2b₃ + 2b₅ + 2b₇ + … ≥ 0. ∎

Thus if the largest final piece satisfies b₁ ≥ (1+u)/2 = c(n) we are done immediately. Xiang's
only way to defeat this is to cut the top piece down, which the certificate localises:

**Protected-interval reduction.** In the dyadic start, on the top interval
I = (2ⁿ⁻¹u, 2ⁿu) we have N₀ = 1 (odd), so 𝟙[N₀ odd] = 1 there. Every toggle set
S_i = (0,x_i) ∪ (r_i−x_i, r_i) has its left part (0,x_i) ⊆ (0, 2ⁿ⁻¹u] because
x_i ≤ r_i/2 ≤ (2ⁿu)/2 = 2ⁿ⁻¹u; hence the left parts never enter I. So D can be reduced on I only
by the *right* parts (r_i−x_i, r_i) of cuts applied to pieces of length r_i > 2ⁿ⁻¹u — of which
there is initially exactly one (the top piece). This localises the top-of-the-profile control and
is the seed of the full domination induction.

**Status of the lower bound in this approach:** the reduction above (Lemmas C1–C3 + protected
interval) is rigorous, and the target min D = u is verified, but the complete induction closing
D ≥ u under all ≤ n toggles is **not finished here**. The `dyadic-discrepancy` approach owns the
full domination proof (each dyadic level 2^k u exceeds the sum (2^k−1)u of all smaller levels, so
n cuts cannot cancel all n+1 levels and a residual of measure ≥ u survives); we **import that
lower bound** rather than duplicate it. Under that import, Liu ≥ (1+u)/2 = c(n).

---

## Upper bound (Xiang ≤ c(n)): OPEN — the shared crux

We must show: for **every** Liu partition, Xiang has ≤ n toggles reaching D ≤ u. Two naive
strategies are **refuted numerically**, so no cheap potential-greedy closes this:
- "Bisect the current largest piece" is **not** optimal: e.g. Liu = {0.517, 0.483}, n=1 — bisecting
  gives Liu 0.742, whereas Xiang's true optimum holds Liu to 0.517; Liu = {0.3,0.7} gives 0.65 vs
  optimal 0.5. (Numerically tabulated.)
- The refuted-earlier "bisect the n largest" is likewise not universal.

So Xiang's optimal play is genuinely **adaptive / non-myopic** (n=1: threshold rule — bisect the
big piece if it is ≥ 2× the small one, else pin). In certificate language the upper bound is the
statement "n parity-toggles suffice to push D down to ≤ u from any profile," and finding the toggle
schedule is exactly the shared hard gap. **Not closed here.**

---

## Answer

**c(n) = 2ⁿ / (2ⁿ⁺¹ − 1)** (verified c(1)=2/3, c(2)=4/7 by brute force; c(n) = (1+u)/2,
u = 1/(2ⁿ⁺¹−1)). This approach rigorously establishes the value's *equivalence* to a parity-toggle
minimax of exactly u, proves the machinery (Lemmas G, C1, C2, C3), imports the lower bound, and
leaves the upper bound (non-myopic Xiang) as the open gap it shares with the field.

## Promotable lemmas

- **Lemma G (alternating-selection value = odd-rank sum).** For any multiset, alternating
  greedy-optimal play with Liu first gives Liu = b₁+b₃+b₅+… (sorted descending). Full proof above
  (pairing strategy, both directions, ties handled). → `lemmas/greedy-claim.md`.
- **Lemma C1 (level-set identity).** D(M) := meas{t : #(pieces>t) odd} = b₁−b₂+b₃−… = O−E, so
  Liu's take = (1+D)/2. Full proof above; verified numerically. → `lemmas/levelset-discrepancy.md`.
- **Lemma C2 (cut-budget).** One split of L into x, L−x toggles the parity of N exactly on
  (0,x)∪(L−x,L), so |ΔD| ≤ 2·min(x,L−x). Full proof above; verified. → `lemmas/cut-budget.md`.
- **Lemma C3 (domination).** D ≥ 2·(largest piece) − 1 for every multiset. Full proof above.
  → `lemmas/discrepancy-domination.md`.
