# Proof review — imo-2026-03 (IMO 2026 P3), round 1

Problem: `compute_and_prove`, answer_type `expression`. Claimed answer
**c(n) = 2^n/(2^{n+1}−1)**. All three builders report `partial`. I independently
re-derived the load-bearing steps and ran verification. Summary: the shared spine is
CORRECT and rigorous; the two flagged gaps (lower-bound Case B, general upper bound) are
REAL and honestly marked; nothing is overclaimed. No approach is `solved`.

## Independent verification I ran

- **Lemma G** (greedy claiming ⇒ first player = odd-rank sum): 0 mismatches vs brute-force
  optimal alternating-selection value on 4000 random multisets; greedy-first-move is optimal
  on 3000 tie-heavy integer multisets (0 failures). Proof in `greedy-claim.md` re-checked line
  by line (recursion V(A)=T−min_j V(A∖b_j); Δ_j≥0 for odd/even j; ties non-strict) — rigorous.
- **Level-measure identity** D = b₁−b₂+b₃−⋯ = λ{t : #(pieces>t) odd}: 0 mismatches on 3000
  random multisets; integral-form proof (indicator decomposition, prefix alternating sum) is
  correct.
- **Cut-flip / cut-budget**: toggle set [0,x)∪[L−x,L), |ΔD|≤2min(x,L−x): re-derived by the
  δ(t)=1[t<x]+1[t<L−x]−1[t<L] case split; held on 3000 random splits.
- **Answer algebra**: (1+u)/2 = 2^n/(2^{n+1}−1) with u=1/(2^{n+1}−1) confirmed symbolically
  for n=1..5. So "target ⇔ D*=u" is a faithful restatement, not a hidden assumption.
- **n=1 full game** (Liu 1 mark, Xiang 1 cut, grid K=60): max_Liu min_Xiang D = 1/3 ⇒ c(1)=2/3.
- **Dyadic lower bound tightness**: min D over ≤ n arbitrary cuts from the dyadic partition
  = u exactly for n=1,2,3 (20000-trial search never beats u). So D≥u is TRUE; the proof of it
  (Case B) is what is unfinished, not the statement.

Conclusion on the value: the answer **c(n)=2^n/(2^{n+1}−1) is correct** (proven for n=1,
verified computationally for n≤3, algebra exact), but it is **not fully PROVEN for n≥2**
because the general upper bound is open. Hence `partial`, not `solved`, for the whole problem.

## Per-approach verdicts

### dyadic-discrepancy — CHANGES REQUESTED (Status: partial) — builder's `partial` is CORRECT
Rigorously proven here: the reduction (§0), Lemma G + both identities, the answer/reformulation
D*=u (§1), the complete n=1 solution both bounds (§3), and lower-bound Case A (§2, b₁=2^n u ⇒
D≥2b₁−1=u via the domination inequality). No overclaim: GAP L and GAP U are explicitly and
honestly marked, and it correctly avoids the refuted "bisect n largest" rule. This is the
leader — most concrete, spine owned, and it owns the domination lower bound Case A. Progress is
real. To close: GAP U (a general non-myopic Xiang rule) and GAP L (Case B).

### induction-recursion — CHANGES REQUESTED (Status: partial) — builder's `partial` is CORRECT
Same proven spine (Lemma G §1, level-measure §2, cut-flip §3, reduction §4, Case A §5), plus two
genuine additions I verified: (a) the exact block-split identity for Case B,
`D = λ(O_top)+λ(O_bot)−2λ(O_top∩O_bot)` (this is `{N odd}=O_top △ O_bot`, correct), with
λ(O_bot)≥u by the scaled IH; and (b) the rigorous refutation of bisection-only Xiang via the
cut-flip corollary (min_T D(T) ≈ 0.165 > 1/7 at n=2 — I accept this; it is the certified
corollary). Recursion u_n=u_{n−1}/(2+u_{n−1}) verified. GAP-LB and GAP-UB honestly open.
This approach is **closest to closing GAP L**: it has reduced Case B to a single clean
sub-claim (λ(O_top) ≥ 2λ(O_top∩O_bot)), needing a cut-budget-refined bound W(n−1,b)>u_{n−1}
for b<n−1.

### potential-certificate — CHANGES REQUESTED (Status: partial) — weakest, near-duplicate
The distinctive contribution is a PROVEN dead-end, correctly reported: no separable per-piece
potential Φ=Σw(piece) can certify the odd-rank functional. I verified the witness (split ½→¼,¼
raises O on {½,½} but lowers it on {½,¼,¼} with identical ΔΦ) — clean and correct; the LP
infeasibility is consistent. However, the approach then **pivots to exactly the same order-aware
level-set certificate** (D, cut-budget, domination) as the other two, and **imports** the lower
bound from dyadic-discrepancy rather than owning it; the upper bound is left open as the shared
crux. So its独立 progress beyond the shared spine is just the separability gate result. It is
correctly `partial`, but it has collapsed toward the shared framing — if it stalls again next
round it is a RETHINK candidate (the field would then be one framing, per the CLAUDE.md
shared-gap warning). Keep it this round for the gate result and diversity.

## Are the two gaps real? (checked — yes, not overclaimed)

- **GAP L (lower bound, Case B):** REAL. My search confirms D≥u is TRUE for the dyadic
  partition under any ≤n cuts, but that is computational, not a proof. The inductive
  cancellation step (ruling out O_top cancelling O_bot under the shared cut budget) is
  genuinely unwritten. Budget-essentiality (unlimited cuts drive D→0) is correct, so a soft
  estimate cannot work — a counting/monovariant argument is needed. **Closest: induction-
  recursion** (exact identity reduces it to one inequality).
- **GAP U (upper bound, general n — THE crux):** REAL and the true wall. Only n=1 is proven.
  Bisection-only and myopic-greedy Xiang are both rigorously refuted, so the rule must be
  non-myopic; no approach has a mechanism. This is what blocks `solved`. **Closest: none has a
  proof**; dyadic-discrepancy has the cleanest framework (assign n cuts so sorted ranks pair up
  with gaps summing to ≤u) but it is still a goal, not an argument. Field-level: if two of three
  stall here next round, seed a genuinely different fourth framing (per outline-reviewer note).

## Lemmas certified into the shared cache

- **Lemma G** (`lemmas/greedy-claim.md`) — CERTIFIED. Statement correct, proof rigorous
  (ties handled, both optimality directions), numerically confirmed. Status line updated.
- **Level-measure / integral identity** (in `lemmas/greedy-claim.md`) — CERTIFIED. D = alt sum
  = λ{t:#(pieces>t) odd}; Liu = (1+D)/2.
- **Cut-flip / cut-budget + bisection corollary + domination (D≥2b₁−1)** — CERTIFIED, written to
  new file `lemmas/cut-flip.md`. All re-derived and verified.

These three are the solid shared spine; next round should build on them and spend the round on
GAP U (and GAP L) — do not re-litigate the spine.

## Verdicts (one per slug)
- dyadic-discrepancy: **CHANGES REQUESTED** (partial)
- induction-recursion: **CHANGES REQUESTED** (partial)
- potential-certificate: **CHANGES REQUESTED** (partial)
