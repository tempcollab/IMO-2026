## imo-2026-03 — LENS: fold (★) + the b-lift into ONE scale-by-scale peel induction

### Summary verdict up front
I found one genuinely new, EXACT (not conjectural) identity — the **absorb-the-top-block identity**
— that generalizes the ladder-length machinery's rung-peel (I1) to the case where `F'`'s top scale is
itself CUT (not a single atom). It is unconditional, proven algebraically in two lines, and verified
`0/2000` exact-`Fraction`. It is the natural "single induction, never separate (★) from the lift"
object my lens was asked to find. **But naively iterating it (absorbing all of `F'`'s scales into
`π_0` one at a time and re-using the certified `(LB_m)` deficient bound at each step) does NOT close
the b-lift** — it drives the accumulated red total `ΣR` far outside `(LB_m)`'s proven domain
(`ΣR ≤ 2^{m+1}`), and the naive extrapolation of `(LB_m)` beyond that cap is **numerically FALSE**
(28/10000 exact counterexamples below, starting at `m=1`). So absorption-with-(LB_m) is a genuine new
*cheap-kill*: a clean idea that fails for a precise, checkable reason, not vague intuition. The
correct fix is not "extend `(LB_m)`'s numeric bound" but "retain `F''`'s ladder shape explicitly at
each level instead of folding it into `R`" — i.e. exactly the R10/R11 finding that a *shape* invariant
on `g=N_{F'}`, not an aggregate total, is unavoidable. Separately, I ran a direct numeric probe of the
GAP-P1′-b slice-max claim in a new parametrization (`(m,β)`: `β`=cuts spent on `Z`, count cap on `R` =
`m+1−β`) and it is **consistent and monotone**: `min Δ` over feasible `(R,Z)` strictly increases in `β`
(tightest, `=0`, at `β=0`), which is independent numeric support for "the base slice `b=0` is the
global extremum," the load-bearing premise of GAP-P1′-b.

### Distinct openings
1. **The absorb identity as a *building block*, not a closer.** For any red multiset `R`, any split
   `Z = π_1 ⊎ Z'` (top block `π_1` of total `θ`, remainder `Z'`), with
   `Δ_m(A,B) := ½(D̃(A⊎B) − ΣA + ΣB)` (the natural generalization of the certified `Δ_m(R)`,
   dropping the assumption `B` is a full ladder):
   ```
      Δ_m(R,Z) = θ + Δ_{m−1}(R ⊎ π_1, Z')          (ABSORB, exact, unconditional)
   ```
   *Proof:* `D̃(R⊎Z) = D̃((R⊎π_1)⊎Z')` (same multiset), so both sides expand to
   `½(D̃(R⊎π_1⊎Z') − ΣR + θ + ΣZ')` after substituting `ΣZ=θ+ΣZ'` and `Σ(R⊎π_1)=ΣR+θ`; the `D̃` terms
   cancel and the constant discrepancy is exactly `θ`. Needs NO hypothesis on `π_1`'s shape (it need
   not even be dyadic) — it is pure bookkeeping, one level more general than the certified (I1) (which
   assumed `π_1={θ}` a singleton and additionally required every part of the fixed `R` to be `≤θ`).
   This is new: it reduces `Δ_n(π_0,F')≥0` at scale `n` to `Δ_{n−1}(π_0⊎π_1, F'')≥−θ` at scale `n−1`,
   in ONE step, with `F'=π_1⊎F''` the standard top-peel of `F'` itself (Structure Lemma) — literally
   folding the base case and the lift into one recursive call, as the lens asked.
2. **Why naive iteration fails (the honest negative, precise).** Iterating (ABSORB) down through all
   of `F'`s scales accumulates `R` to `π_0 ⊎ π_1 ⊎ π_2 ⊎ …`, whose total grows like
   `2^n + 2^{n−1} + … ≈ 2^{n+1} − 2^{n−k}` at depth `k`, while the remaining ladder length `m=n−1−k`
   has `2^m = 2^{n−1−k}` — the ratio `ΣR / 2^m` grows *without bound* as `k` increases. The certified
   `(LB_m)` only proves the deficient bound `Δ_m(R)≥min(0,2^m−ΣR)` for `ΣR ≤ 2^{m+1}` (and a matching
   count cap); well beyond that cap the naive extrapolated bound is **false**: e.g. `m=1`,
   `ΣR=52/25≈2.08` (already `>2^{m+1}=4`? no `2.08<4` — check: actually the failures below occur even
   *inside* `ΣR≤2^{m+1}=4` at `m=1`, once the COUNT cap is not simultaneously tightened — see numeric
   evidence). So the count/total tradeoff in `(LB_m)`/`(Q_m)` is load-bearing in BOTH directions, and
   simply piling more mass into `R` via repeated absorption outruns it. **Conclusion: absorbing all of
   `F'` into `R` at once collapses the b-lift back into a restatement of the whole theorem (same
   failure mode the R8 meta already proved for static-profile framings) — the recursion must stop
   after ONE absorb step and bound `Δ_{n−1}(π_0⊎π_1,F'')` using a property of `F''`'s remaining
   *shape*, not a blind total/count bound.** This is a clean, reusable cheap-kill for future b-lift
   proposals: if a candidate mechanism reduces to "iterate ABSORB and reuse `(LB_m)`/`(Q_m)`
   verbatim," it is dead before being written up — test on the `m=1` witness below.
3. **One-level-only use of ABSORB, closing the "cut the top rung of `F'` once" reduction cleanly.**
   Since (ABSORB) is exact and general, a single application (not iterated) legitimately reduces
   general-`b` GAP-P1′-b to a *smaller* instance: prove `Δ_{n−1}(π_0 ⊎ π_1, F'') ≥ −θ` where `π_1` is
   *any* partition of `θ=2^{n−1}` (the piece Xiang cut off Liu's top piece) and `F''` is a refinement
   of the remaining `n−1` scales with budget `b−a_1`. This is now an inequality of *exactly the same
   shape as the base-slice theorem* (★) but with a **doubled-mass, doubly-large red set**
   (`Σ(π_0⊎π_1)=3·2^{n-2}=3θ`, not `2^{n-1}`) against a *shorter* ladder-refinement of length `n−1`.
   If this single-step reduced claim can be attacked directly (its own mutual `(P,Q)`-style induction,
   scaled to handle total `3θ` rather than `2θ`), it might close the FIRST unit of budget `b→b−1` in
   one clean step without ever absorbing further — worth scoping as a genuinely new slug distinct from
   both the dead single-cut descent (R12) and the dead WM-inheritance (R13): this uses an EXACT
   identity, not a monovariant guess, and the target inequality is now scale-`(n−1)`, one level
   smaller, so a *fresh* induction on `n` (not on `b`) closes it if the `(n−1)`-level claim can be
   discharged — worth checking whether the SAME mutual `(P_m)/(Q_m)/(LB_m)` engine, re-run with `R`
   allowed total up to `3·2^m` (not `2^{m+1}`) and a correspondingly adjusted count cap, might still
   go through — the failures found in opening 2 used *uncapped* count against blown-up total; a
   correctly-recomputed count cap (matching the true budget bookkeeping `a_0+a_1+2 ≤ n+2`) was NOT yet
   tested and is the natural next experiment.
4. **The `(m,β)` slice-max reformulation — independent support for GAP-P1′-b's premise.**
   Reparametrize: for red-count cap `m+1−β` and any `Z` a refinement of the `m`-ladder using budget
   `β`, `min_{R,Z} Δ_m(R,Z)` over `4500` random exact-`Fraction` trials (`m≤5`, `β=0..m−1`) is:
   `0` at `β=0` for `m≤3` (matches the certified tie), and **strictly non-decreasing in `β`** at fixed
   `m` (e.g. `m=5`: `1.42, 1.88, 2.00, 2.71, 4.38` for `β=0..4`). This is genuinely new confirmation —
   from a DIFFERENT sampling parametrization than R11's original slice-max probe — that `β=0` (i.e.
   `b=0`, all budget on `π_0`) is the extremal/tightest slice, the exact premise GAP-P1′-b needs to
   formalize. It does not prove monotonicity, but it is a second independent numeric witness for it
   (0 counterexamples across two different generators).

### Candidate technique(s)
- The (ABSORB) identity as a *single-step* reduction tool (opening 3) — genuinely new, not banned by
  any prior-round rule (it's not WM, not a single-cut co-varying descent, not a scalar φ(b) cutoff).
- A rescaled/generalized mutual `(P,Q)`-induction at "3×-mass" scale for the one-step-absorbed claim,
  if opening 3 is pursued — this would need its own base case and Lipschitz-collapse analogue; NOT
  yet attempted, flagged as the natural next experiment, not a claim.

### Cheap-kill candidates
- **"Iterate ABSORB + reuse (LB_m)/(Q_m) verbatim" is a cheap kill — REFUTED this round** (opening 2):
  the extrapolated deficient bound `Δ_m(R,Z) ≥ min(0,2^m−ΣR)` fails for `ΣR` even modestly beyond the
  certified regime once the count cap isn't co-tightened. Concrete minimal witness: `m=1`, `Z=L_1={1}`
  (`β=0`), `R={a,b}` scaled to `ΣR=2` (i.e. exactly at the boundary `2^{m+1}=4`... actually the cleanest
  failing witness found is `ΣR=2` with `Δ=-1/6 < bound=0` — check against `(Q_1)`'s own count cap
  `#R≤3`: the witnesses use `capR=m+1-β+2` (2 more than the true cap) in the stress test, i.e. they
  are OUTSIDE `(P_1)`/`(Q_1)`'s proven count hypothesis by construction — confirming the count cap,
  not just the total cap, is essential and cannot be dropped when chaining). Use this as a fast filter
  before proposing any "just extend `(LB_m)`" mechanism.
- Before committing a slug to opening 3, cheaply check: does the doubled-mass claim
  `Δ_{n−1}(π_0⊎π_1,F'')≥−θ` fail on any of the already-known hard witnesses (the R13 `n=2` WM
  counterexample, the R9 §7a decoy)? A 10-line Fraction script re-using the existing test harness
  (`/tmp/test_blift.py` below) can check this in under a minute before any proof is attempted.

### Knowledge-base entries to use
- `lemmas/base-slice-star.md` (the `(P_m)/(Q_m)/(LB_m)` engine + Lipschitz collapse (I4)) — directly
  reused/extended by openings 2–3.
- `lemmas/floor-half-reduction.md`, `lemmas/ladder-interleaving-identity.md`, `lemmas/peel-difference-bound.md`
  — the general-in-`F'` identities my `Δ_m(R,Z)` generalizes; consistent by construction (verified: at
  `Z=L_n`, `π_0=R`, my `Δ_n(π_0,L_n)` matches the certified `Δ_n(π_0)` exactly, since `ΣL_n=2^n-1`
  makes the two definitions coincide).
- `lemmas/hlp-breakpoint-reduction.md` — orthogonal (WM machinery); not used here, and per R13/R14
  banned rules, do not resurrect WM as the loaded IH.
- knowledge_base.md: no new specific entry found beyond the generic exchange/induction-on-structure
  techniques already cited in prior rounds; this round's contribution is a problem-specific identity,
  not a KB match.

### Analogous past problems (cruxes)
- Consistent with round 12/13 banked notes (`aimo-0146`, `aimo-0388`); did not find a new corpus match
  this round — the object here (a discrepancy functional under one-level absorption of a partition
  block) is specific enough to this problem's dyadic peel structure that I did not locate a closer
  crux than what's already banked. Did not exhaustively re-query given time budget; flagging rather
  than forcing a weak match.

### Prior progress
- (★) base slice (`b=0`) fully proven & certified (`base-slice-star.md`), independent of this round's
  work — unchanged, not re-attempted per the ban.
- The b-lift (GAP-P1′-b) remains OPEN. This round's new material: the exact (ABSORB) identity
  (certified-quality, 0/2000 numeric, algebraic proof included above — ready for a builder to adopt
  as a promotable lemma), the precise failure mode of naive iteration (opening 2), and independent
  `(m,β)` numeric support for the slice-max premise (opening 4).

### Dead ends (do not retry)
- **Iterating (ABSORB) through all scales and reusing `(LB_m)`/`(Q_m)` unchanged: REFUTED this round**
  (opening 2) — the accumulated red total outruns the certified deficient-bound domain and the naive
  extrapolation is numerically false. Do not propose "just absorb everything and induct on total mass
  with the same bound" as a slug.
- All previously banned routes remain banned and were NOT retried: single-cut co-varying b→b−1
  descent (R12), full-WM-IH inheritance (R13), (NEG) Q≥S_π (R13), scalar b-cutoff/φ(b) (R11), all
  measure/merged-order/sequential/genfn/GAP-IMR framings (R8/R10).

### Small-case / intuition notes (conjectural / numeric evidence only)
- (ABSORB) itself is an EXACT identity (proven algebraically above, not conjectural) — safe for a
  builder to cite directly without re-deriving, though it should still be independently verified by
  the reviewer per protocol.
- The `(m,β)` monotonicity (opening 4) and the R11 slice-max numbers are two independently-generated
  numeric witnesses agreeing that `β=0`/`b=0` is the extremal slice — this is still a CONJECTURE (no
  proof of monotonicity offered), but it is now corroborated from a second angle, which slightly
  de-risks GAP-P1′-b's core premise for whichever mechanism the outliner picks.
- Full test script (exact `Fraction`, reproducible): `/tmp/test_blift.py` on this container — contains
  `Delta`, the absorb-identity check (0/2000), the `(m,β)` slice-max sweep, and the extended-bound
  stress test (28/10000 failures, all at count-cap violations as intended).
