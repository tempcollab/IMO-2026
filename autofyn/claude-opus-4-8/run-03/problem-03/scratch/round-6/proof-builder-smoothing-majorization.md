# Build report — smoothing-majorization (imo-2026-03), round 6

Status: **partial** (real new content, one honest labeled GAP remains).

## What I closed (rigorous, new)

1. **Rebuilt the approach off a new lever.** Discarded the refuted (SMOOTH) global-concavity
   monotonicity AND the round-5 D-DICHOTOMY single-leftover plan (I refuted the latter: reducing to
   ONE piece via nested differences gives ratio up to 28x u_n on balanced profiles — a single
   forced leftover does NOT bound D). Replaced both with a **finite DELETE/MATCH reduction game**.

2. **Lemma DM (proposed, `lemmas/elementary-reductions.md`).** Xiang has two exact D-tracking moves,
   each one mark, each an instance of certified Lemma P:
   - DELETE x (bisect): D(S) -> D(S\{x});
   - MATCH (x,y), x>y: D(S) -> D((S\{x,y}) ∪ {x-y}).
   This recasts the whole upper bound as a finite reachability game — no subset enumeration, no mass
   threshold, no convexity of V. Fully rigorous given Lemma P. Also gives a clean self-contained
   proof of the m<=n corrector (DELETE all pieces => D=0), subsuming Lemma U0. For the UPPER bound
   we only need these moves LEGAL+SUFFICIENT (not optimal), so VERT is NOT required here.

3. **UB(n) strong induction, four disjoint exhaustive cases; three closed:**
   - a1 >= c(n)L: DELETE a1, then UB(n-1) on tail; exact identity u_{n-1}(1-c(n))=u_n. RIGOROUS.
   - L/2 <= a1 < c(n)L: certified whole-tail-peel, D=2a1-L<=u_nL. RIGOROUS.
   - a1 < L/2 AND a2 >= beta_n L (beta_n=2^{n-1}/(2^{n+1}-1)): MATCH top two, then UB(n-1) on the
     n-piece residual (sum L-2a2); exact identity u_{n-1}(1-2beta_n)=u_n. RIGOROUS.
   - Base cases UB(0), UB(1) fully closed (UB(1) has no balanced case).
   All threshold identities verified exactly with fractions for 2<=n<=7.

## What remains (honest GAP)

- **GAP U-VALLEY:** balanced full-budget profiles with a1<L/2 AND a2<beta_n L (beta_n -> 1/4). This
  is the sole uncovered case. Numerically the DELETE/MATCH optimum still hits D<=u_nL here (worst
  ratio 0.75 over n<=5), so the target is TRUE and reachable in the move set — but I have NO
  profile-independent move choice. I confirmed every simple deterministic rule FAILS in the valley:
  always-MATCH-top-two 4.23x, always-DELETE-a1 25.5x, the two-rule hybrid 10.7x. So the optimal
  sequence is genuinely adaptive (interior valleys), consistent with the standing "V not concave"
  finding. Closing it needs an adaptive potential OR the breakpoint-vertex VERT finitization plus a
  uniform vertex bound.

- **GAP L (imported):** lower-bound Case B; owned by induction-peel / parity-measure; unchanged.

## Spec / diversity concerns

- This approach is now genuinely far from subset-cover and from smoothing/concavity: it is a finite
  move-reduction game. Its non-valley cases share the DELETE/whole-tail machinery with the field but
  the framing (exact 2-move reduction game) is distinct.
- GAP U-VALLEY is the SAME wall as breakpoint-vertex §4B and the other upper-wall attacks. My new
  contribution narrows the balanced regime to exactly {a2 < beta_n L}; the field should now target
  that narrow valley specifically. A natural next step: feed the DELETE/MATCH game + VERT together
  (VERT says min over responses = min over DELETE/MATCH vertices, finitizing GAP U-VALLEY).

## Files written
- results/imo-2026-03/approaches/smoothing-majorization.md (rebuilt; Status partial)
- results/imo-2026-03/lemmas/elementary-reductions.md (Lemma DM proposal for certification)
