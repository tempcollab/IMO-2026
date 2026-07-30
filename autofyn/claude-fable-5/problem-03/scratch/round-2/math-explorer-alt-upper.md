## imo-2026-03 (lens: upper-bound routes bypassing Claim U(m))

### Distinct openings (alternatives to the discrepancy-halving move-process induction)

1. **Concavity / local-KKT route (new, from the certified Tie-Structure catalog V1–V4).**
   Corollary V4 (certified in `lemmas/tie-structure.md`) says V(a) := Xiang's optimal value
   against partition a equals `min_τ f_τ(a)` over a *finite* set of pinned types τ, each
   f_τ **affine in a**. A min of finitely many affine functions is concave. I verified this
   numerically: sampled random pairs of 3-part partitions a,b (n=2, budget 2 cuts), computed
   V at a, b, and the midpoint via exhaustive move-search — concavity `V(mid) ≥ (V(a)+V(b))/2`
   held on 5/5 random trials (labeled conjecture, small sample). If V is concave on the whole
   simplex of Liu partitions, then proving `sup_a V(a) = c(n)` attained at the ladder a* reduces
   to a **local first-order (KKT) certificate at the single point a=a\*** — no global induction
   over all a needed. I checked this is not vacuous: at a=a\* (ladder), the "bisect-top" pinned
   value a₁/2+c(n−1)(1−a₁) and the "match-second" pinned value a₂+c(n−1)(1−2a₂) both equal c(n)
   exactly there (since ladder's a₁=c(n) and a₂=c(n)/2 exactly — checked algebraically), i.e.
   multiple affine pieces are tied at a\*, which is exactly what a KKT subdifferential argument
   needs.
   **Caveat (important):** this elegance is deceptive. The *true* V(a) is a min over only the
   FEASIBLE pinned types at a, and establishing that V really is the pointwise min of a
   *specific small explicit family* valid **everywhere** (not just locally near a\*) is exactly
   GAP C / GAP M(b) in `tie-structure-variational.md` — and each "candidate certificate" f_τ
   valid on a whole region is precisely a Xiang *strategy* achieving ≤ c(n) there, i.e. exactly
   what Cases A/B/C/D (or U(m)'s Cases 1/2) already are. **Verdict: this is the same wall
   wearing convex-analysis language — it does not bypass Case D/Case-3, it only says "if you
   already had enough certificates, concavity would make the outer sup easy"; the missing
   certificate in the flat/middle regime is the unresolved content, identical in substance.**
   Still worth recording for the outliner as a *packaging*, since a local KKT check at exactly
   one point (a\*) is a genuinely different final step than a global induction, IF the field
   ever obtains the missing middle-regime certificate by other means — it could shortcut "prove
   for all a" to "prove tightness only at the ladder."

2. **Case D / Claim C(m) in `dyadic-recursion-induction.md` — a different (non-scale-invariant, single-variable) invariant.**
   C(m): partition into ≤ m+1 parts, m cuts ⟹ Liu ≤ max(a₁, 1/2 + a₁/2^{m+1}). This depends
   on a₁ **alone** (not a₂, unlike U(m)'s Case 1/2 split which needs both a₁ and a₂ thresholds).
   I numerically stress-tested it (corrected exhaustive move-search over Bisect/Match/FreeRetire
   sequences, fixed a bug in my first pass — see note below) on random 3–4 piece partitions and
   on the known hard case (5,3,3,2)/13: C(m) held with visible slack every time (e.g. on
   (5,3,3,2)/13 with m=3: bound 0.524 vs actual optimum 0.5 — comfortable margin, unlike U(m)'s
   β=1/15 which is tight only at the ladder). **This is evidence C(m) is true but NOT tight
   in the middle regime, meaning a proof of it (if found) would need less delicate case
   analysis than U(m)'s sharp β bound.**
   However: attempting to derive C(m) inductively via "bisect the top, recurse with C(m−1) on
   the tail" does **not** telescope cleanly to the claimed max(a₁, ½+a₁/2^{m+1}) form (the
   recursive bound involves a₂ of the tail, reintroducing exactly the two-variable case split
   the file's own Case A/B mechanism needs) — I could not find an argument that proves C(m)
   without re-deriving something equivalent to Case A–D. **Conclusion: Case D/C(m) is very
   likely the *same* underlying difficulty (the "no piece dominates, no two pieces already
   tied" regime) restated with a looser, more forgiving invariant — a real but not
   obviously-easier alternative; worth trying because of the slack, but do not expect it to
   sidestep the core obstruction.**

3. **Probabilistic-method framing (genuinely unexplored by any current approach).**
   Instead of an explicit deterministic strategy (move-process induction or pinned-type
   catalog), define a *randomized* Xiang strategy (e.g. random matching of comparable-sized
   pieces, or random choice among several deterministic tie-breaking rules on the flat/middle
   instances) and show `E[Δ] ≤ u`; existence of *some* realization with `Δ ≤ E[Δ] ≤ u` then
   follows by the first-moment method (KB: "Probabilistic method", listed as a combinatorics
   subtopic in the crux corpus). This is a genuinely different top-level mechanism (existence
   via averaging rather than case analysis or induction) and has NOT been tried by any of the
   three approaches. I did not attempt to construct the randomization (out of scope per lens
   instructions — "note the idea, don't develop it"), but flag it as unexplored territory that
   could specifically target the flat/middle regime (many comparable pieces = many candidate
   matchings to average over).

4. **Direct bijective / merge-sort inversion-counting reframing.** The threshold identity
   (Δ = measure of t with N(t) odd, certified in `lemmas/threshold-identity.md`) suggests
   recasting Xiang's task as: choose cuts to make the "level function" N(t) even almost
   everywhere. This is structurally close to a bin-packing / capacity argument. The crux
   corpus's `aimo-0012` (ISL/IMO — "smallest k such that any a_i∈[0,1] summing to n can be
   packed into k bins of capacity 1, answer 2n−1") uses a greedy-merge/pigeonhole mechanism
   ("repeatedly find a mergeable adjacent pair", "closed part past a fixed capacity
   threshold") that is thematically resonant (dyadic/threshold capacity counting) but I judge
   it **not a genuine crux match** — that problem is a static bin-packing question with no
   adversarial second player and no dyadic doubling; the resemblance is superficial (both
   involve a tight construction ratio and greedy merging), not a transferable proof technique.
   Flagging so the outliner doesn't chase a false lead, but noting the "greedy-merge-until-
   capacity-threshold" idea as a loose inspiration only.

### Candidate technique(s)
- LP/convex-analysis duality (concavity of V as min-of-affines + KKT at a single point) —
  packaging only, same underlying gap (see finding 1).
- Single-variable (a₁-only) induction via Claim C(m) — a real but likely equally-hard
  alternative invariant (finding 2).
- Probabilistic method / first-moment argument for existence of a good reply — genuinely
  unexplored (finding 3).

### Cheap-kill candidates
None obvious that dispatch a proof outright, but a useful pruning check for any future
middle-case attempt: on the flat/middle regime (a₁ < 2^{m−1}β, a₂ < 2^{m−2}β), verify whether
some *two* pieces are automatically forced within a factor of 2 of each other (pigeonhole on
m pieces all below 2^{m−1}β — by pigeonhole on dyadic scale bands 2^{-k}β, k=0,…,m−1, since
there are m pieces and only m−1 remaining "big" bands below 2^{m-1}β, two pieces must fall in
the same dyadic band, hence within a factor 2 of each other) — this pigeonhole observation
(not yet in any approach file) might be the missing structural fact that licenses a Match
move producing further ties recursively, i.e. a genuine cheap first step for the Case-3/Case-D
regime. Flagging this explicitly as a candidate the outliner should have builders try, since it
is elementary (pigeonhole, KB "Pigeonhole / extremal principle") and I have not seen it written
in any of the three approach files.

### Knowledge-base entries to use
- "Pigeonhole / extremal principle" (KB combinatorics section) — for the dyadic-band pigeonhole
  cheap-kill above.
- "Probabilistic method" is not explicitly in `knowledge_base.md`'s combinatorics list (only
  appears as a crux-corpus subtopic) — if the outliner pursues finding 3, it should be added to
  the KB as a named technique once used.
- "Extremal principle" / "Invariants & monovariants" (KB) — underlies both U(m) and C(m)
  framings already in use; no new entry needed for those.
- LP/duality: KB doesn't have a named "LP duality for concave minimax" entry; the
  tie-structure approach already cites "Extremal principle" (fundamental theorem of LP, vertex
  of polytope) for its own V2 lemma — the concavity idea (finding 1) would reuse the same
  citation for the dual/concave direction.

### Analogous past problems (cruxes)
- **aimo-0012** (ISL/IMO-style, Poland, "partition a_i∈[0,1] summing to n into k=2n−1 groups
  each ≤1") — thematically close (tight ratio + greedy merge-until-threshold) but judged **not
  a strong crux match**: no adversarial second player, no dyadic/geometric doubling structure,
  and the mechanism (merge two small items into one bin) doesn't map onto our alternating
  claiming game. Mention only as loose inspiration for finding 4, not a transferable proof.
- **aimo-0117** (Dutch, dyadic-ladder-values-in-boxes game) — the crux "assign values as a
  two-sided geometric/dyadic sequence so the largest exceeds the sum of all others" mirrors our
  ladder's super-increasing property (2^k > 2^{k-1}+...+1), but it's a different game (box
  capacity, not stick-cutting/claiming) — again a structural echo, not a reusable proof step.
- No other crux in `games-and-strategy` (39 entries checked, domain=combinatorics) resembles
  the specific alternating-claiming-after-cutting structure of this problem. **Overall
  verdict: nothing in the corpus is a genuine analog of the whole game; the closest matches
  are dyadic/threshold-flavored but structurally different games.**

### Prior progress
- Lower bound c(n) ≥ 2^n/(2^{n+1}−1): fully proved, certified (`lemmas/ladder-resists.md`).
  I did NOT re-verify this (out of lens scope — dispatch note says lower bound is certified);
  I did independently re-run its extremal instance (ladder n=3) through a corrected exhaustive
  move-search and got min Δ = 1/15 exactly, matching Theorem L's claimed bound (sanity check,
  not a re-proof).
- Upper bound reduced to Claim U(m) Case 3 (middle) + a₁=a₂ tie sub-case of Case 2 — this
  remains, in my assessment, the single real obstruction; findings 1–2 above both reduce to it
  in different clothing.

### Dead ends (do not retry)
- Plain greedy match-or-bisect for U(m) — fails on (5,3,3,2)/13 (already recorded; I
  independently reproduced this with a corrected exhaustive move simulator: optimal Δ=0 there,
  greedy leaves 1/13).
- Parity-XOR induction on the top rung, integrality of pinned replies — already recorded dead
  ends in `current.md`; not revisited.
- **New dead-end note (from my own numerics):** my first-pass "Match" move simulator had a bug
  (double-counting the retired partner instead of dropping it), which spuriously suggested
  Δ=0 was reachable on the ladder with only n cuts — a false alarm that would have contradicted
  the certified Theorem L. After fixing the bug, the ladder's guaranteed minimum recovers
  exactly u=1/15 for n=3. **Lesson for any builder writing/verifying a move-based numeric
  check: the Match move must REMOVE both L and S from active and add back ONLY the remainder
  L−S (the old S and new S-copy are retired as a pair and must not reappear in the active
  list), not add back both the remainder and a duplicate of S.** This is an easy bug to
  reintroduce; flag it for proof-builders doing their own numeric verification of U(m)/Case D.

### Small-case / intuition notes (conjectural)
- Concavity of V(a) as a function of Liu's partition a holds numerically on all sampled
  instances (n=2, 5/5 trials, small sample) — conjecture, consistent with the fact that V is a
  min of finitely many affine functionals wherever the catalog framework applies, but I have
  not established this holds *globally* (only that it's plausible).
- Claim C(m) (dyadic-recursion's Case D invariant) held with comfortable slack on all ~10
  random/adversarial instances tested (including the known hard case), never approaching
  tightness away from the ladder itself — suggestive that C(m) is true and perhaps provable
  by a cruder argument than the sharp β-invariant, but I found no such argument in the time
  available; its natural induction reintroduces a₂-dependence, i.e. likely the same core
  difficulty.
- The dyadic-band pigeonhole observation (cheap-kill above) — every set of m pieces each below
  2^{m−1}β must have two pieces in the same dyadic band `[2^{-k-1}·2^{m-1}β, 2^{-k}·2^{m-1}β)`
  for some k ≤ m−2 by pigeonhole (m pieces, m−1 bands) — is elementary and, to my knowledge,
  not yet used by any approach; it guarantees a "near-tie" pair to Match on even in the
  flattest instances, which is exactly the structural handle Case 3/Case D currently lacks.
  This is my strongest concrete lead for the round, offered as a candidate first move for
  whichever slug attacks the middle case next, independent of which of U(m)/C(m)/concavity
  framing is chosen.
