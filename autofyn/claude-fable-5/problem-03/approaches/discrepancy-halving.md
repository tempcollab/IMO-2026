# Approach: discrepancy-halving

## Status
solved

## Approaches tried
- (round 1, outline) Skeleton laid down; nothing certified. Anchors: the identity Liu = 1/2 + Δ/2 (below) is elementary algebra; c(1)=2/3 hand-proved; c(2)=4/7, c(3)=8/15 numeric.
- (round 1, build) **Lower bound (GAP L) fully closed** — new mechanism: threshold identity Δ = |{t : N(t) odd}| + consecutive-pairing + a tree/mass argument on the pairing multigraph over rungs. No per-rung bookkeeping, no integrality; global flow/matching form as required. — **worked** (certified round 2 as `lemmas/ladder-resists.md`).
- (round 1, build) Upper bound (GAP U): the naive halving invariant was replaced (per the outline review) by the correct scale-invariant claim **U(m)**: any m-piece multiset with m−1 cuts can be driven to Δ ≤ ΣA/(2^m − 1). Proved the two boundary cases (top piece ≥ 2^{m−1}β: bisect; second piece ≥ 2^{m−2}β: match); middle case left open. The plain "match-or-bisect" greedy provably fails the sharp constant on (5,3,3,2)/13, so the middle case needed a non-greedy mechanism. — **partial**.
- (round 2, fold bookkeeping) dyadic-recursion-induction folded (C(m) slack invariant not easier — greedy violates C(3) on (5,3,3,2)/13).
- (round 3, build) **GAP U fully closed — U(m) proved in complete generality, all cases at once**, superseding the Case 1/2/3 analysis. Mechanism: (i) **Balancing Lemma** — if all m pieces exceed β = T/(2^m−1), the 2^m subset sums would be pairwise > β apart if no balanced disjoint pair (P, N) existed, forcing a range > (2^m−1)β = T, a contradiction; so a split with |ΣP − ΣN| ≤ β always exists. (ii) **Two-pile walk realizability** — any such split is realizable by Match/FreeRetire moves within the m−1 cut budget: walk toward zero, and the only reachable "stuck" state (positives left, negatives exhausted, running sum q > 0) automatically has q < |ΣP − ΣN| ≤ β, so Xiang stops and bisects the remainder. (iii) Trivial branch: some piece ≤ β — keep it, bisect the rest. The planned ternary/dense-sparse dichotomy of the outline was not needed: the pigeonhole argument replaces both branches. Verified end-to-end numerically: 32,000 random instances m = 1..8 (ties, zeros, ladders, adversarial shapes) — move-by-move simulation with legality checks, cut budget ≤ m−1 and Δ ≤ β every time; exact-arithmetic checks on the tight ladder and all known hard instances. — **worked; approach complete**.

## Current best

**The problem is fully solved by this approach: c(n) = 2^n/(2^{n+1}−1), both bounds proved.** Lower bound: certified `lemmas/ladder-resists.md`. Upper bound: Claim U(m) proved below in full generality (no open cases); applied with m = n+1 it caps every Liu partition at (1+u)/2 = 2^n/(2^{n+1}−1), u = 1/(2^{n+1}−1). No gaps remain.

## Full proof

**Answer: c(n) = 2^n/(2^{n+1}−1).** (For `answer_type: expression`; verified at n = 1: 2/3 matches the hand proof; n = 2: 4/7 matches the round-1 grid search.)

### 0. Imported certified infrastructure

We import, as black boxes, the reviewer-certified lemmas of this workspace:

- **Lemma G and Corollary R** (`lemmas/greedy-claiming.md`): the claiming phase on a final multiset S has value exactly odd(S) (odd-rank sum) for Liu Bang, and c(n) = sup_a inf_x odd(S(a,x)), where a ranges over partitions of 1 into ≤ n+1 positive parts and x over Xiang's legal replies (≤ n cuts at interior points of Liu's pieces, all marks distinct). Only the multiset of piece sizes matters.
- **Threshold-identity lemma** (`lemmas/threshold-identity.md`), items used below:
  - (T1) *Discrepancy identity:* odd(S) = (ΣS + Δ(S))/2, where Δ(S) := p₁ − p₂ + p₃ − ⋯ is the alternating sum of the sorted (descending) multiset.
  - (T3) *Tied-pair invariance:* Δ(S ∪ {x,x}) = Δ(S) for any x ≥ 0; a final multiset of exactly-tied pairs plus one residual piece x has Δ = x; only tied pairs, Δ = 0.
  - (T4) *Zero-padding:* adjoining 0-entries changes neither odd(S) nor Δ(S).
- **Theorem L** (`lemmas/ladder-resists.md`): the entire lower bound — Liu Bang's dyadic ladder (2^n, 2^{n−1}, …, 2, 1)·u, u = 1/(2^{n+1}−1), satisfies Δ(S) ≥ u for every legal Xiang reply, hence **c(n) ≥ 2^n/(2^{n+1}−1)**; and Xiang's mirror reply attains Δ = u exactly.

By (T1), for ΣS = 1 Liu's value on S is (1 + Δ(S))/2, so

c(n) = 1/2 + (1/2)·sup_a inf_x Δ(S(a,x)),

and the target c(n) = 2^n/(2^{n+1}−1) is equivalent to sup_a inf_x Δ = u := 1/(2^{n+1}−1), since (1+u)/2 = 2^n/(2^{n+1}−1). Theorem L gives "≥". It remains to prove the upper bound:

**Target U.** For every Liu partition a₁ ≥ … ≥ a_k > 0 (k ≤ n+1, Σ = 1), Xiang has a legal reply with Δ(S) ≤ u.

### 1. Reduction to a multiset move process

Pad a with zeros to exactly m = n+1 entries; by (T4) this changes no value, and a strategy will never cut a zero entry (zeros are bookkeeping only — they correspond to no piece of the physical stick, and leaving them "active" adds 0-entries to S, harmless by (T4)).

Xiang builds his reply as a sequence of **moves** on an *active multiset* A (initially the padded partition, |A| = n+1). Each move uses at most one cut and *retires* pieces that are never touched again:

- **Bisect(L)** [1 cut], L > 0 active: cut L at its midpoint into (L/2, L/2); retire this exactly-tied pair; A ← A ∖ {L}.
- **Match(L, S)** [1 cut], L > S > 0 active: cut L at distance S from an end, into (S, L−S); retire the exactly-tied pair {new sub-piece of size S, the old piece S}; A ← A ∖ {L, S} ∪ {L−S}.
- **FreeRetire(L, L)** [0 cuts], two equal active pieces: retire both; A ← A ∖ {L, L}.

Every cut is at an interior point of an existing physical piece, hence a new mark distinct from all previous marks — each move is legal, and a sequence of ≤ n moves-with-cuts is a legal Xiang reply. If Xiang stops with active multiset A_end, the final multiset is S = (all retired tied pairs) ∪ A_end, and by (T3),

Δ(S) = Δ(A_end).

(This reduction paragraph is unchanged from rounds 1–2 and was checked by the round-1 review; it is extracted as the proposed lemma `lemmas/reduction-to-um.md`.)

Therefore Target U follows from the purely combinatorial claim, applied with m = n+1, T = 1 (then β = u, budget m−1 = n):

**Claim U(m).** *Let A be any multiset of m ≥ 1 nonnegative reals, T = ΣA, β := T/(2^m − 1). Using at most m − 1 cuts, the moves above can reach an active multiset A_end with Δ(A_end) ≤ β.*

(U(m) is exactly tight: on the ladder A = (2^{m−1}, …, 2, 1)β, Theorem L's argument scaled to total T shows no reply beats Δ = β.)

### 2. Proof of Claim U(m) — in full generality

If T = 0 all entries are 0; stop immediately: Δ(A) = 0 = β. Assume T > 0, so β > 0. Sort A as a₁ ≥ … ≥ a_m ≥ 0. Two exhaustive branches.

**Branch 1: some aᵢ ≤ β.** Fix such an aᵢ. Bisect every *other* positive entry — at most m − 1 of them, so at most m − 1 cuts — and leave aᵢ (and all zero entries) active. Then A_end = {aᵢ} ∪ {zeros}, and by (T3)+(T4), Δ(final) = Δ(A_end) = aᵢ ≤ β. ✔

**Branch 2: every aᵢ > β.** (In particular all entries are positive.) We use two new lemmas.

---

**Lemma B (balancing pigeonhole).** *Let a₁, …, a_m > β > 0 with a₁ + ⋯ + a_m = T = (2^m − 1)β. Then there exist disjoint nonempty index sets P, N ⊆ {1, …, m} with |Σ_{i∈P} aᵢ − Σ_{i∈N} aᵢ| ≤ β.*

*Proof.* Suppose not: for **every** pair of disjoint nonempty index sets P, N,

|Σ_P a − Σ_N a| > β.  (⋆)

Consider the 2^m subset sums f(S) := Σ_{i∈S} aᵢ, S ⊆ {1,…,m}, all lying in [0, T] (f is monotone in S; f(∅) = 0, f({1,…,m}) = T). We claim they are pairwise more than β apart. Let S ≠ S′ and put P := S ∖ S′, N := S′ ∖ S; since S ≠ S′, P and N are not both empty, and

f(S) − f(S′) = Σ_P a − Σ_N a.

Three exhaustive cases:
- N = ∅ (so P ≠ ∅): f(S) − f(S′) = Σ_P a > |P|·β ≥ β, since every piece exceeds β.
- P = ∅ (so N ≠ ∅): symmetrically f(S′) − f(S) > β.
- P, N both nonempty: |f(S) − f(S′)| > β by (⋆).

So the 2^m values f(S) are pairwise > β apart; in particular they are distinct. Sort them v₀ < v₁ < ⋯ < v_{2^m−1}. Then

v_{2^m−1} − v₀ = Σ_{j=0}^{2^m−2} (v_{j+1} − vⱼ) > (2^m − 1)β = T.

But v₀ ≥ 0 and v_{2^m−1} ≤ T, so v_{2^m−1} − v₀ ≤ T — a contradiction. ∎

---

**Lemma W (two-pile walk realizability).** *Let A be an active multiset of m positive pieces and let P, N ⊆ A be disjoint nonempty sub-multisets with s := |ΣP − ΣN| ≤ β. Then a sequence of Bisect/Match/FreeRetire moves with at most m − 1 cuts reaches A_end with Δ(A_end) ≤ β.*

*Proof.* WLOG ΣP − ΣN = s ≥ 0 (else swap P and N). Write Z := A ∖ (P ∪ N) (the unused pieces). Xiang runs the following **walk**, maintaining:

- the multisets P′ ⊆ P, N′ ⊆ N of not-yet-consumed pieces;
- the running signed sum q := Σ(consumed pieces of P) − Σ(consumed pieces of N);
- the invariant: *all consumed pieces have been converted into retired exactly-tied pairs, plus — iff q ≠ 0 — one active piece of length |q|, called the* carrier.

Initially P′ = P, N′ = N, q = 0, no carrier; the invariant holds vacuously. One step of the walk (each step consumes exactly one piece):

- **If q = 0:** take any x ∈ P′ (rule below guarantees P′ ≠ ∅ whenever the walk continues); *designate* x as the carrier — no move is made, 0 cuts. New q = x > 0. Invariant holds.
- **If q > 0:** the carrier is an active piece of length q. Take any y ∈ N′ (if N′ = ∅, **stop** — analyzed below).
  - If y < q: Match(carrier, y) — cut the carrier into (y, q − y), retire the tied pair {sub-piece y, piece y}; new carrier q − y. 1 cut. New q = q − y > 0.
  - If y > q: Match(y, carrier) — cut y into (q, y − q), retire the tied pair {sub-piece q, old carrier}; new carrier y − q. 1 cut. New q = q − y < 0, and the carrier length is |q|. ✔
  - If y = q: FreeRetire(carrier, y). 0 cuts. New q = 0, no carrier.
  In all three sub-cases the new piece y enters q with coefficient −1 and the invariant is preserved. (Match legality: both arguments are active and the strict inequality holds in the sub-case used; equality is routed through FreeRetire.)
- **If q < 0:** symmetric with x ∈ P′ (x enters with coefficient +1; if x < |q| Match(carrier, x); if x > |q| Match(x, carrier); if x = |q| FreeRetire). New q = q + x.

Each step consumes one piece of P ∪ N, so the walk halts after at most |P| + |N| steps, in one of the terminal situations analyzed next. Throughout, by construction, q = Σ(consumed P) − Σ(consumed N) exactly.

*The walk never demands a piece from an empty pile except benignly.* Check the three conceivable "empty pile" states (all pieces are positive, and Σ N = ΣP − s ≤ ΣP):

1. **q < 0 with P′ = ∅:** then Σ(consumed N) = Σ(consumed P) + |q| = ΣP + |q| > ΣP ≥ ΣN ≥ Σ(consumed N). Contradiction — this state is unreachable.
2. **q = 0 with P′ = ∅ but N′ ≠ ∅:** then Σ(consumed N) = Σ(consumed P) = ΣP = ΣN + s ≥ ΣN; but N′ ≠ ∅ and pieces are positive force Σ(consumed N) < ΣN. Contradiction — unreachable. (Hence at q = 0, either P′ ≠ ∅ and the walk continues, or P′ = N′ = ∅ and it ends.)
3. **q > 0 with N′ = ∅:** this is the one reachable stop. Here q = Σ(consumed P) − ΣN, so the unconsumed mass of P is ΣP − Σ(consumed P) = (ΣN + s) − (ΣN + q) = s − q. If P′ ≠ ∅ this mass is positive, so **0 < q < s ≤ β**. Xiang stops the walk.

Terminal positions and endgame:
- *Everything consumed* (P′ = N′ = ∅): q = ΣP − ΣN = s. If s > 0 the active leftover of the walk is the carrier, of length s ≤ β; if s = 0 there is none.
- *Stopped in state 3:* the active leftover is the carrier, of length q < β, plus the unconsumed pieces P′.

In either case Xiang finishes by **bisecting every unconsumed piece** (all pieces of P′ and of Z; each is an original positive piece, so Bisect is legal), one cut each. Now A_end = {carrier} (or ∅), so by (T3), Δ(final) = Δ(A_end) ≤ β. ✔

*Cut count.* Each consumed piece is consumed by exactly one of: a fresh designation (0 cuts), a Match (1 cut), a FreeRetire (0 cuts); and the first consumed piece is a fresh designation. Hence the walk uses at most (#consumed − 1) cuts. The endgame bisects exactly the unconsumed pieces: (m − #consumed) cuts. Total ≤ m − 1. ∎

---

*Conclusion of Branch 2.* By Lemma B there are disjoint nonempty P, N with |ΣP − ΣN| ≤ β; by Lemma W, Xiang reaches Δ ≤ β within m − 1 cuts. ✔

Branches 1 and 2 are exhaustive (either some piece is ≤ β or all exceed β), so **Claim U(m) is proved for every m ≥ 1**. ∎

*(Sanity anchors, all re-verified this round in exact arithmetic: the ladder (8,4,2,1)β lands in Branch 1 with aᵢ = β exactly, Δ = β — tight, as it must be, since Theorem L forbids anything smaller there. The greedy-killer (5,3,3,2)·(T/13): Branch 2, P = {5}, N = {3,2}, walk = Match(5,3) → carrier 2, FreeRetire(2,2), then Bisect(3): 2 cuts ≤ 3, Δ = 0. A 32,000-instance move-by-move simulation over m = 1..8, with legality and budget assertions, produced no violation. These computations are checks only; the proof above does not rely on them.)*

### 3. Assembly and the final answer

Let a₁ ≥ … ≥ a_k > 0 (k ≤ n+1) be any Liu partition of 1. Pad with zeros to m = n+1 entries (T = 1, β = 1/(2^{n+1}−1) = u). By Claim U(n+1), Xiang has a move sequence with at most n cuts reaching Δ(final) ≤ u; by the Section-1 reduction this is a legal reply x with Δ(S(a,x)) ≤ u. Hence by (T1),

inf_x odd(S(a,x)) ≤ (1 + u)/2 for every a, so c(n) ≤ (1+u)/2 = 2^n/(2^{n+1}−1).

Combined with Theorem L (`lemmas/ladder-resists.md`): c(n) ≥ 2^n/(2^{n+1}−1). Therefore

**c(n) = 2^n / (2^{n+1} − 1).**

*Verification of the answer.* n = 1: formula gives 2/3 — matches the certified end-to-end n = 1 analysis (tie-structure file, round 1) and the hand proof: Liu cuts (2/3, 1/3)·... precisely, ladder (2u, u), u = 1/3: Liu guarantees (1+1/3)/2 = 2/3, and U(2) caps any partition at Δ ≤ 1/3. n = 2: 4/7 — matches the round-1 grid search recorded by the outline-reviewer. Substituting back: (1 + 1/(2^{n+1}−1))/2 = (2^{n+1}/(2^{n+1}−1))/2 = 2^n/(2^{n+1}−1) ✓ consistent throughout. ∎

---

## Superseded material (kept for the record)

The round-1 partial case analysis of U(m) (Case 1: a₁ ≥ 2^{m−1}β via Bisect; Case 2: a₂ ≥ 2^{m−2}β, a₁ > a₂ via Match; plus this round's closures of the a₁ = a₂ tie branch via FreeRetire + zero-pad + U(m−1), and of Case 3a: a₁ ≥ (2^{m−1}−1)β via full MultiMatch) is now **superseded** by the general proof in Section 2, but remains correct and is written out in the proposed lemma file `lemmas/um-easy-cases.md` as independent corroboration of the constant.

## Cases covered / hygiene
- Liu with fewer than n+1 pieces: zero-padding (T4), zeros never cut.
- Xiang with fewer than n cuts: allowed (budgets are "≤"; stopping early is always legal).
- Exact ties everywhere: Match's strict inequality is enforced — equalities route through FreeRetire (Lemma W's three sub-cases are exhaustive: y < q, y > q, y = q).
- Zero pieces: only in Branch 1 / padding; never cut; harmless by (T4).
- T = 0 degenerate instance: handled explicitly.
- All cut positions are interior points of existing pieces, distinct from all previous marks — legality is argued in Section 1, not assumed.
- No integrality or parity-of-units arguments anywhere; all lengths are arbitrary nonnegative reals.
- Both branches of U(m) and all three sub-cases of each walk step are exhaustive and disjoint.

## Promotable lemmas
- **um-proof** (Claim U(m), Section 2 above — Lemma B + Lemma W + Branch 1): *any multiset of m nonnegative reals with sum T can be driven, by at most m−1 Bisect/Match/FreeRetire cuts, to Δ ≤ T/(2^m−1).* Proved in full above; written as proposed file `lemmas/um-proof.md`. This is the entire upper bound of the problem; siblings can import it as a black box.
- **reduction-to-um** (Section 1 above): c(n) ≤ (1 + 1/(2^{n+1}−1))/2 follows from U(n+1) — padding, the move process, tied-pair bookkeeping, legality of the reply. Written as proposed file `lemmas/reduction-to-um.md`.
- **um-easy-cases** (superseded but independently useful): Cases 1, 2 (incl. the a₁ = a₂ tie branch), 3a, and U(m ≤ 3) by direct moves. Written as proposed file `lemmas/um-easy-cases.md`.
