# Outline review — IMO 2026 P6 (`imo-2026-06`), round 3

Reviewer gate. I read the field the outliner put up (`/tmp/round-3/proof-outliner.md`), the 3 new skeletons, the certified lemmas, the live slugs, and ran empirical sanity checks (`python3`) on the load-bearing claims before judging. Findings below.

## Headline

The outliner's flagship new approach **`cross-intersecting-anchor`** is built on a FALSE empirical premise: its distinctive crux (B) "`M'_∞` pairwise cross-intersecting, 12/12 a_1" is empirically FALSE for `a_1=135, 105, 385` (incl. the outline's own "R-small hard regime, real test" case `a_1=135`, where `{2,5}∩{3,7}=∅`). This kills the distinctive mechanism AND the B2 path α that depends on it. The surviving B1' route in that slug reduces to (A)=(W), which is the SAME wall `w-descent-rsmooth` attacks — so `cross-intersecting-anchor` adds no diversity and is CUT (RETHINK, not registered, not built). The COPY twin `b2-future-shared-primes` is also declined (path α is dead, not merely coupled, so the twin would converge with a path-β-only `b2-induction-step`).

Two new approaches survive: `w-descent-rsmooth` (APPROVE-registered) and `b2-induction-step` (APPROVE-registered, with mandatory changes — drop dead path α, fix the 2∈S proof).

## Per-approach verdicts

### cross-intersecting-anchor — RETHINK (CUT, not registered, not built)
The distinctive crux (B) is empirically FALSE. I computed `M'_∞` and checked pairwise cross-intersection for 8 `a_1`:
- `a_1=135` (R=15): `M'_∞={{2,3},{2,5},{3,5},{3,7}}`; `{2,5}∩{3,7}=∅` ⟹ NOT cross-intersecting.
- `a_1=105`: `M'_∞` has `{2,5}` and `{3,7,11,13}` disjoint ⟹ NOT cross-intersecting.
- `a_1=385`: `M'_∞` has `{2,3,5}` and `{7,11,13}` disjoint ⟹ NOT cross-intersecting.

The outline's claim "empirically 12/12 incl 4-prime cases" is incorrect (it was checked only on small-`|M'_∞|` cases where cross-intersection is trivially forced). Since `a_1=135` is the outline's OWN designated hard-regime test case, the distinctive crux is dead, not merely "mechanism open".

Additional flaws in the skeleton:
- **Step 3 close logic is circular/backwards.** It writes "By (B) cross-intersecting, `h∩h_i≠∅` for every `h_i∈M'_n`; since each `σ_i⊇h_i`, `h∩σ_i≠∅`." But `h_i∈M'_n` is a minimal HITTING SET of `F'_n`, so `h_i∩σ_i≠∅`, NOT `σ_i⊇h_i`. The containment is backwards. In fact the close does NOT need (B) at all: once `(A)` gives `σ(m)⊇h∈M'_smooth,n=M'_n`, then `h` is itself a hitting set of `F'_n` (every `h∈M'_n` hits every `σ_i`), so `σ(m)⊇h` already hits `F'_n`, i.e. `m∈B_n`. The (B) invocation in step 3 is spurious. (B) is only the INPUT to the early-freeze (step 2) and to B2 path α — both now dead.
- **The "strong induction" framing is vacuous.** B1' at `n+1` requires `(A)` at `n+1`, which IS (W) — the very claim being proved. The induction hypothesis ("`a_i=b_i` for `i≤n`") does not produce R-smooth terms, so it does not advance `(A)`. The "induction" is a static implication `(A)⟹B1'` at each `n`, with no inductive mechanism for `(A)` itself.
- **`(A)`=(W) is shared with `w-descent-rsmooth`** (the outline admits this). With (B) dead, `cross-intersecting-anchor`'s ONLY remaining B1' route is `(A)=(W)⟹B1'`, which is exactly `w-descent-rsmooth`'s clean reduction — but with NO mechanism for proving (W) (the s-substitution + late-arrival machinery is the other slug's distinctive contribution). So `cross-intersecting-anchor` is strictly weaker than `w-descent-rsmooth` and offers no distinct framing. This is the single-gap-trap signature: two slugs on one wall, one with a real mechanism, one without.

Send back to the outliner for a genuinely different framing of B1' (not a (W)-variant), or drop it. Do NOT register; do NOT build.

### w-descent-rsmooth — APPROVE (registered, NEW)
The clean reduction `(W)⟹(C)⟹B1'` (step 1) is rigorous and short: an R-smooth `a_j` has no large prime, so any `m∈A_n` sharing a factor with `a_j` shares a SMALL prime, landing `p∈σ(m)∩σ*` — contradiction if `σ(m)` missed `σ*`. The s-substitution + late-arrival descent is a genuinely distinct mechanism (per-term support descent, aimo-0030 analog) attacking (W) from a different side than the cross-intersection/anchor route. `(W)`-eventually is empirically TRUE (8/8 tested `a_1`: every σ*-class that ever appears has an R-smooth term somewhere). GAP F (late-arrival) is honestly flagged as the crux; the outline correctly does NOT claim the false strong form ("first term of each class is R-smooth" is FALSE for `a_1=135` class `{2,3}`, first term `138`).

Mandatory builder clarifications (CHANGES-REQUESTED level, fix while building):
- **`(W)`-at-step-n vs `(W)`-eventually.** The clean reduction needs `(W)` AT STEP `n`: every `σ*∈F'_n` has an R-smooth term among `a_1..a_n`. This is FALSE at `n=2,3` for `a_1=135` (class `{2,3}` appears at `a_2=138=2·3·23`; its R-smooth term `a_4=144=2^4·3^2` arrives at delay 2). So the reduction gives B1' only for `n ≥ (arrival delay)`; the early-delay cases (`n=2,3` for `a_1=135`) MUST be handled explicitly. This is NOT "GAP C lower-stakes finite casework" — it is the other face of GAP F (the late-arrival mechanism must produce the R-smooth term within bounded delay AND cover the pre-arrival window). I verified B1'(window) holds empirically at `n=2` for `a_1=135` (`a_3=140∈B_2`; all admissible `m∈(138,153]` are in `B_2`), so the early cases are PROVABLE, but the outline under-scopes them. The builder must state `(W)` as "(W)-eventually + bounded early-delay casework" and cover the delay window.
- Verify the R-large-regime threshold (`R≥?` ⟹ every term R-smooth ⟹ (W) trivial) as a clean sub-theorem.

### b2-induction-step — APPROVE with CHANGES REQUESTED (registered, NEW)
The rigorous core is sound: seed `a_1∈B` (step 1: universal-small-prime ⟹ `primes(a_1)` hits `F'_∞` ⟹ `⊇h∈M'_∞` ⟹ `m_h|a_1`) is a clean theorem given B1'; `B⊆B_n` (step 2: `h∈M'_∞` hits `F'_n⊆F'_∞` ⟹ `⊇g∈M'_n` ⟹ `m_g|m_h`) is rigorous; the reduction to "no prematurely-valid SMALL-prime `B_n\B` candidate" is correct and the candidate set is genuinely different from B1's large-prime `A_n\B_n` shortcuts (spacing/v_p refutation does not transfer directly). This is the only slug dedicated to B2 — good diversity of gap-coverage.

Mandatory changes (the builder must close these):
- **Path α is DEAD — drop it.** Path α depends on (B) cross-intersecting `M'_∞`, which is empirically FALSE (see above). Do not pursue path α; do not re-state it as a live option. The slug becomes path β + path γ only.
- **Path γ's `2∈S` proof is WRONG as stated.** The outline argues "once an even term exists, `2` is a hitting prime of `F'_∞`". This conflates "2 appears in some `σ(a_j)`" with "{2} is a hitting set" (FALSE: `a_1=15` has `σ(a_1)={3,5}`, no 2) and with "2 lies in some minimal hitting set `h∈M'_∞`" (the actual `2∈S` claim). I verified the CLAIM `2∈S` is empirically TRUE for all 8 tested `a_1` (incl. 135/105/385), and that `a_2=a_1+p_0` is even (`p_0`=smallest prime of `a_1`) for every odd `a_1` — so the turning-even-by-`a_2` sub-fact is correct and easy (consecutive-multiple arithmetic). But the bridge "even term ⟹ 2 lies in a minimal hitting set of `F'_∞`" needs a real mechanism (why does the greedy's structure force 2 into `M'_∞`, not merely into some `σ(a_j)`?). The builder must prove this, not hand-wave.
- **Path β must probe v_p re-coupling.** Path β uses σ-periodicity (which is itself CONDITIONAL on B1') to bound "future `a_j` shares only a large prime with `a_{n+1}`" cases. The candidate set (`B_n\B`, small-prime) differs from B1's, so the 9927-violation spacing refutation does not directly transfer — but a density/periodicity bound on future-shared large primes might re-couple to the same `~n` demand vs `~a_n` capacity wall that killed `bounded-diff-finite-state`. The builder must explicitly check whether path β's density estimate reduces to the refuted (Cov) window claim or to the v_p sieve-error obstruction; if it does, path β dies too and B2 must await a different mechanism.

### b2-future-shared-primes (COPY) — NO COPY
The outliner asked to copy `b2-induction-step` → `b2-future-shared-primes` (twin pursuing ONLY path β, as independent fallback to path α). The copy rationale was "path α coupled to (B); path β independent; pursue both in parallel." But (B) is empirically FALSE, so path α is DEAD, not merely coupled/risky. With path α dropped from `b2-induction-step`, the "twin" (path β only) and the revised original (path β + path γ only) would CONVERGE — both effectively just do path β. A copy that converges with its source on day one is not a useful twin (the ranker's copy mechanism is for two genuinely divergent fillings of a shared gap). Decline the copy; instead revise `b2-induction-step` to drop path α (above). If path β later proves viable AND a second mechanism for GAP H emerges, a copy can be reconsidered then.

### hitting-set-monovariant — RETIRED (frozen)
Agree with the outliner. The distinctive mechanism (transversal-minimality / one-prime-swap / Hall-König) is a recorded dead end; the salvageable content (cross-intersecting closure lemma, definitional reduction, conditional spine) is already certified in `lemmas/` and imported by the live slugs. Marked the approach file `unsolved (RETIRED)` with reason; ranker entry frozen (not in build set). The certified lemmas remain importable.

### small-prime-window-lemma / bounded-diff-finite-state / periodic-set-iteration — LEFT as certified spine (ADVANCE-NOOP)
Agree. The spacing/v_p/covering cluster is EXHAUSTED (clean value-window (Cov) refuted at 9927 violations; v_p sieve-error structural beyond `n_0`; coupled to one wall). Their certified results (spacing fact, value-bound, σ-periodicity, v_p union-bound PARTIAL, Theorem 1) remain importable by `w-descent-rsmooth` and `b2-induction-step`. `periodic-set-iteration` is the Theorem-1 carrier. Do NOT re-advance with the same mechanism; do NOT retire (certified partial results). Stale flags cleared via this round's ranking update.

### compactness-konig-branch / bijection-from-n1 / frozen-invariant-reduce-mod-lcm — LEFT (frozen in population)
Not in the outliner's round-3 field. `compactness-konig-branch` never built (null outcome, speculative — König's-lemma gamble); `bijection-from-n1` route collapsed (injectivity bypass broken, residual B2-diagnostic only); `frozen-invariant-reduce-mod-lcm` retired (dead-end). Left as-is; stale flags cleared. Not in build set.

## Coupling / single-gap-trap status

- **The (W) wall is the field's shared wall for B1'.** After cutting `cross-intersecting-anchor`, ONLY `w-descent-rsmooth` attacks B1' with a live mechanism (s-substitution + late-arrival on (W)). `bounded-diff-finite-state` / `small-prime-window-lemma` / `periodic-set-iteration` are exhausted (their B1 attack is coupled to the refuted spacing/v_p/covering wall). So B1' has a single live attacker. This is THIN but honest — the alternative (keeping a (W)-variant without a (W)-mechanism) would be a false diversity. The orchestrator should instruct next round's outliner to put ≥1 genuinely different B1' framing on the table (NOT a (W)-variant, NOT a spacing/v_p variant) — e.g. a direct greedy-walk / modular-arithmetic / induction-on-the-orbit argument that does not route through "every σ*-class has an R-smooth term".
- **B2 is independently covered** by `b2-induction-step` (path β + path γ), on a DIFFERENT gap from B1' — good diversity of gap-coverage. But path β carries a real v_p-re-coupling risk (flagged above); if path β dies, B2 has no live attacker either.
- **No single-gap-trap within the live field** (two live attackers on two distinct gaps B1', B2). The trap was averted by CUTTING `cross-intersecting-anchor` (which would have been a second (W)-variant pretending to be diverse).

## Empirical verification performed (python3, sympy)

- (B) cross-intersecting `M'_∞`: FALSE for `a_1=135` (`{2,5}∩{3,7}=∅`), `105`, `385`. TRUE only for small-`|M'_∞|` cases (15,45,77,91,210). This refutes the outline's "12/12" claim.
- (W)-at-step-n: FALSE at `n=2,3` for `a_1=135` (class `{2,3}` R-smooth term arrives at `a_4=144`, delay 2).
- (W)-eventually: TRUE for all 8 tested `a_1` (every σ*-class has an R-smooth term somewhere in the first 400 terms).
- B1'(window) at `n=2` for `a_1=135`: holds (`a_3=140∈B_2`; all admissible `m∈(138,153]` lie in `B_2`) — confirms the early-delay cases are provable.
- `2∈S`: TRUE for all 8 tested `a_1`; `a_2=a_1+p_0` even for all odd `a_1` (turning-even-by-`a_2` confirmed). The `2∈S` CLAIM is true; only the outline's PROOF is flawed.

## Full ranked field (Elo after update, best-first)

| rank | slug | Elo | last_outcome | status |
|------|------|-----|-------------|--------|
| 1 | bounded-diff-finite-state | 1616 | advanced | LEFT (spine, exhausted) |
| 2 | small-prime-window-lemma | 1558 | partial | LEFT (spine, exhausted) |
| 3 | periodic-set-iteration | 1549 | advanced | LEFT (spine, Theorem-1 carrier) |
| 4 | w-descent-rsmooth | 1548 | NEW | APPROVE-registered, BUILD |
| 5 | b2-induction-step | 1542 | NEW | APPROVE-registered, BUILD (with changes) |
| 6 | hitting-set-monovariant | 1526 | partial | RETIRED (frozen) |
| 7 | frozen-invariant-reduce-mod-lcm | 1430 | dead-end | LEFT (frozen) |
| 8 | bijection-from-n1 | 1390 | partial | LEFT (frozen) |
| 9 | compactness-konig-branch | 1341 | null | LEFT (frozen, never built) |

(cross-intersecting-anchor is NOT in the table — RETHINK, not registered.)

## Build set

Two builders, one per APPROVED approach. `cross-intersecting-anchor` is cut (RETHINK → back to outliner for a genuinely different B1' framing); `b2-future-shared-primes` copy declined.

build set: w-descent-rsmooth, b2-induction-step
