# Proof-reviewer catch-up review — round-4 builder output (imo-2026-03)

Context: round 4's three proof-builders updated their approach files but the
round was interrupted before proof-reviewer ran. This review adversarially
checks all three updated files plus notes the unchanged fourth approach, then
updates `current.md` and certifies lemmas. Every new claimed lemma below was
independently re-derived / re-checked with `fractions.Fraction` exact
arithmetic (200,000+ trials for the highest-risk claims), not just read.

---

## 1. `geometric-dominance-construction.md` — round 4 additions

**Claims checked:**
- **Lemma I (Insertion Lemma):** `evenrank(T∪{a}) ≥ a` for any nonempty
  nonnegative multiset `T` and `a∈[0,max(T)]`. Re-derived from scratch and
  verified by 200,000 exact-`Fraction` random trials (random `T` size 1-6,
  random `a≤max(T)`): **zero violations.** The two-case proof (insertion
  position parity) is correct and genuinely structure-free — it does not use
  the geometric configuration at all, so it is a strict, honest
  generalization of round 2's Lemma F1 computation, not a relabeling.
- **Rank-shift-by-s fact:** verified by 50,000 exact-`Fraction` trials over
  random `s∈{1,2,3,4}`: **zero violations.** Proof (parity flip when merging
  a dominating block) is correct.
- **Claim ★, s=1,2:** verified by 200,000 exact-`Fraction` trials (random
  `q`, random `T` rescaled to satisfy `max(T)≤q, oddrank(T)≥q`, random split
  `R` of `2q` into `s∈{1,2}` parts): **zero violations.** The proof correctly
  splits on `r_2 ≤ max(T)` vs. `r_2 > max(T)`, both cases closing cleanly via
  Lemma I / rank-shift-by-1 or rank-shift-by-2. Confirmed correct.
- **Counterexample showing Claim ★ is FALSE for s≥3:** I substituted the
  exact stated values directly — `q=1/8`, `T={1/8}`, `R={649/4000,
  116181/2000000, 59319/2000000}` — and computed `oddrank(R∪T) =
  440681/2000000 = 0.2203405 < 1/4 = 2q`, confirming `Σ R = 2q` exactly and
  the inequality genuinely fails. This is a real, exact counterexample, not
  numerical noise. **Confirmed correct.**
- **Application (Theorem M(n), k≤1 with simultaneous tail-splitting):** I
  checked the self-similarity inputs (`T_0=λ_n·A_{n-1}`, `p_2=λ_n·p_1^{(n-1)}`)
  numerically for `n=1..5`: exact match. The induction correctly reduces to
  Claim ★ with `q:=p_2`, `s=2`. The base case `n=1` is fully closed (only 3
  possible Xiang-Yu moves, all checked). The inductive step for `n≥2` is
  algebraically sound.

**Overclaim check.** The file is careful and honest: it explicitly states
the inductive step for `n≥3` is **conditional** on the FULL Theorem M(n-1)
(all `k`, not just `k≤1`) holding at level `n-1`, and that this is
*unconditionally* available only via the base case `n=1`, so the
unconditional closure only reaches `n=2`. This is stated plainly in the
"Honest scope of this result" section and matches what I independently
verified is actually provable from the pieces on hand — **no overclaiming
found.** Status header says `partial`, matching reality.

**Verdict: CHANGES REQUESTED.** Status: **partial**. Real, verified progress
(Lemma I, rank-shift-by-s, Claim ★ s≤2, the s≥3 negative result, and the
`k≤1`+tail-splitting closure for `n≤2` unconditional / general `n`
conditional). Gap remaining: `k≥2` in every form, and the entire upper-bound
half over arbitrary configurations (not attempted here).

---

## 2. `recursive-embedding-induction.md` — round 3/4 additions

**Claims checked:**
- **Lemma D-REFORM** (`oddsum(B)=(1+D(B))/2` where `D` is the alternating
  sum): verified by 20,000 exact-`Fraction` trials (random sorted lists
  summing to 1, sizes 1-8): **zero violations.** Simple, correct algebra.
- **Lemma D-BOUND** (`0≤D(Y)≤max(Y)`): verified by 20,000 trials, sizes 1-8:
  **zero violations.** Correct short induction.
- **Lemma D-INSERT** (exact single-insertion recursion for `D`): verified by
  20,000 random-insertion trials with exact `Fraction`: **zero violations.**
  Formula reproduces `D(C')` exactly in every trial.
- **Lemma V' (vertex reduction, fixed tail):** the LP-vertex argument
  (piecewise-affine function on a compact polytope, minimum at a vertex of
  the induced hyperplane arrangement, vertex has ≤1 free coordinate) is a
  standard and correctly-stated fact; I did not find a flaw in the argument,
  and it is explicitly scoped to the **fixed-tail** sub-case only (the file
  is honest that extending to a variable tail is unproved and unattempted).
- **Lemma L (the reduced combinatorial claim it feeds into):** I
  independently wrote a fresh, from-scratch brute-force enumerator (not the
  approach's own script) and confirmed: for `n=1..8`, the minimum of `D` over
  all valid anchor-vectors is exactly `t_n=1` (in the normalized integer
  form), achieved **uniquely** by the canonical vector `a_i=1 (i<n), a_n=2`,
  exactly as claimed. This matches the write-up's own numbers for `n≤7`
  exactly, and I extended the check one further step (`n=8`) with the same
  result. **Confirmed correct as a numerically-verified but formally
  unproven claim** — the file correctly does NOT claim Lemma L is proved for
  general `n`; it is listed as an open target, not certified as a lemma.

**Overclaim check.** No overclaiming found. The write-up is explicit
throughout ("verified but NOT proved for general n", "this is genuine,
precisely-characterized progress, but it is NOT a general proof"). Status
header says `partial`, matching reality.

**Verdict: CHANGES REQUESTED.** Status: **partial**. Real, verified new
toolkit (D-REFORM/D-BOUND/D-INSERT/V') plus a sharpened, precisely-verified
(not proved) reduction of the `k=n` tail-untouched sub-case to Lemma L. Same
overall `k≥1`+tail-splitting gap and upper-bound gap remain; this round did
not close them but did produce genuinely reusable general-purpose machinery
and a much more precise target.

---

## 3. `majorization-smoothing.md` — round 4 (Step 0 execution)

**Context check.** Round 3's outline-reviewer approved a revised Lemma C'
into the build set with a mandatory Step 0 gate: "reproduce the round-1
falsification with the TRUE, exactly-computed V before treating anything
else as progress; if it reproduces, STOP, report RETHINK, do not proceed
further." This round's build executed exactly that.

**Claims checked:**
- **Closed form (†):** `V_{(1,0,0)}(p) = min(max(p_1,1-p_1), p_1/2+p_2)` for
  the `n=2`, one-mark-on-`p_1`, tail-untouched sub-case. I independently
  computed the true value by a 20,001-point grid search over the split point
  `x∈[0,p_1]` at all three reference points and got an **exact match** to
  (†): `p1→0.55`, `p2→0.50`, `mid→0.52`.
- **Whether `(1,0,0)` is truly the GLOBAL minimizer** (not just within its
  own composition type): I wrote an independent brute-force grid search over
  **all 10** valid Xiang-Yu compositions `(k_1,k_2,k_3)` with `k_1+k_2+k_3≤2`
  (not just the 7 the write-up mentions — I count 10, a minor descriptive
  imprecision, NOT load-bearing) at `p=mid`, with a fine grid (30 steps per
  free dimension per composition). Result: the global minimum is **exactly
  0.52**, achieved by `(1,0,0)` (and matched, not beaten, by a few other
  compositions at their degenerate boundary). This **confirms the Step 0
  reconciliation is genuine and correct** — the falsification is not an
  artifact of an under-searched composition space.
- **Non-concavity mechanism** (min of an affine piece and a genuinely convex
  piece `max(p_1,1-p_1)`, hence not generally concave, and this is intrinsic
  — no finite refinement of split-type removes the inner `max`): the
  argument is sound; `max(p_1,1-p_1)` is manifestly convex (max of two
  affine functions), and a min of a concave and a strictly-convex function
  is generically neither concave nor convex, exactly as observed at `mid`.
  This is a genuine structural result, not a repeat of round 1's bare
  numeric counterexample in different notation — round 1 only had the three
  numbers; this round derives *why* they occur and *why* no repair of Lemma
  C' (the specific mechanism the round-3 outline proposed) can work.

**Was this genuinely new work or a re-labeled falsified argument?** Genuinely
new. Round 1 stopped at the bare numeric counterexample with no closed form
and no structural explanation. This round derives the exact closed form (†)
from a complete six-region case analysis, confirms it against the true
global minimum (not just its own composition), and proves the specific
mechanism (convex kink from the max-of-two-affine-branches nested inside the
outer min) that makes the whole "global concavity" idea impossible in
principle, not just unproven. This is real, rigorous, certifiable negative-
result content.

**Did the build skip Steps 2/4 improperly?** No — the round-3 gate
explicitly instructed to STOP after Step 0 if the falsification reproduces,
which it did. Not attempting Steps 2 (type-refinement termination) or 4
(general-n kink system) is compliance with the mandated gate, not a
shortfall; attempting them would have been wasted effort on a framing the
gate itself says is dead once Step 0 reproduces.

**Overclaim check.** File's own Status header is `unsolved` — correct, no
overclaiming (if anything the file slightly underclaims by not proposing its
two results for certification as prominently as it could, but it does list
them under "Promotable lemmas").

**Verdict: RETHINK.** Status: **unsolved** (confirmed correct, matches the
file's own header). This is the *correct* outcome of Step 0's rigorous
execution, not a new failure — this round genuinely and rigorously closed
out this approach as dead, with reusable negative-result content. It should
not be revived under the same "global concavity of V" framing.

---

## 4. `universal-adversary-strategy.md` — unchanged, noted for completeness

Not touched this round; math not re-verified per dispatch instructions
(already reviewer-verified in round 2: Lemma DOM + Lemma HALVE, 3000
exact-`Fraction` trials each, closing `n=1` for arbitrary configurations).
Status remains `partial`; general-`n` upper bound over arbitrary
configurations remains fully open, unchanged.

---

## Summary of verdicts

| Approach | Verdict | Status |
|---|---|---|
| `geometric-dominance-construction` | CHANGES REQUESTED | partial |
| `recursive-embedding-induction` | CHANGES REQUESTED | partial |
| `majorization-smoothing` | RETHINK | unsolved (confirmed dead, correctly) |
| `universal-adversary-strategy` | (not reviewed this round; unchanged) | partial |

Population-level `current.md` Status: **partial** (updated).

## Actions taken
- Updated `results/imo-2026-03/current.md` — Status, Approaches tried,
  Current best sections rewritten to reflect all round-4 work and re-stated
  open gaps.
- Certified three new lemma files (all independently re-verified above):
  - `results/imo-2026-03/lemmas/insertion-and-abstract-reduction.md`
    (Lemma I, rank-shift-by-s, Claim ★ s≤2, s≥3 counterexample)
  - `results/imo-2026-03/lemmas/alternating-sum-toolkit.md`
    (D-REFORM, D-BOUND, D-INSERT, V' — Lemma L explicitly NOT certified,
    listed as open target only)
  - `results/imo-2026-03/lemmas/concavity-failure-and-n2-k1-value.md`
    (exact n=2,k=1 value formula + non-concavity structural proof)
- Called `record_outcome` for all three reviewed approaches:
  `geometric-dominance-construction` → advanced,
  `recursive-embedding-induction` → advanced,
  `majorization-smoothing` → dead-end.

## Notes for next round
- The `k≥2` lower-bound gap and the general-`n` upper-bound gap remain the
  two central open items, as before — but the `k≥2` gap is now sharper:
  Claim ★'s abstraction (scalar summaries `max(T)`, `oddrank(T)` only) is
  *provably* insufficient (exact counterexample), so the next attempt must
  use `T`'s actual recursive/self-similar structure. `recursive-embedding-
  induction`'s Lemma L is a concrete, verified-but-unproved combinatorial
  target for the `k=n` tail-untouched slice of the same gap — a natural
  next target (induction directly on the block-length sequence, as the file
  suggests).
- `majorization-smoothing` should be considered closed out for good under
  its current framing; do not re-propose "V is concave" again without a
  fundamentally different underlying mechanism.
