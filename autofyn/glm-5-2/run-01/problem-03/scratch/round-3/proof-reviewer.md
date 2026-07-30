# proof-reviewer — Round 3 — IMO 2026 P3 (imo-2026-03)

Review of four built approaches. Each judged independently. Verdicts per slug at the
end. All four are CHANGES REQUESTED (partial) — none is a whole-problem solve, none
is a dead end. Real progress on the G1/G2 walls, with the open cruxes precisely
characterized. 6 NEW lemmas certified (19 total in the cache); 2 proposed lemmas
rejected as standalone (conditional reductions, recorded as such).

## Cross-cutting verification

All load-bearing computations re-derived independently with `Fraction`-exact
arithmetic (`/tmp/round-3/verify_two_split.py`, `verify_two_split_1b.py`,
`verify_spine.py`, `verify_gaps_maxbound.py`):

- **Two-split formulas** (Cases 1a, 1b, 2, 4, a=b): 0 mismatches vs direct
  recomputation for `n = 3,…,7`. `D ≥ D(T_{n−2})`: 0 violations `n = 3,…,7`.
- **Spine pair-cancellation (S1)**: 0 mismatches over 20 000 random configs.
- **Even-group spine dominance (S3)**: min `D = 1` over all 127 nonempty
  strictly-decreasing distinct-power-of-2 spines of `{1,…,64}`; 0 violations on
  constructed even-group strong breakpoints of `T_3, T_4`.
- **Gaps+leftover identity (G1)**: 0 mismatches over 20 000 configs, both parities.
- **Pairing bound (G2)**: 0 violations over 20 000 configs.
- **Max-bound conjecture `D* ≤ M/2^n`** (n=2, brute-force breakpoint+grid Xiang
  optimization over 200 random configs): 0 violations; tower `T_2` attains ratio
  1.0 (the tight case); worst non-tower ratio 0.67. Supports the conjecture but
  NOT a proof of the crux.

---

## 1. `tail-count` — CHANGES REQUESTED (partial)

### What's proved this round (correct, verified)
- **Two-split sub-case (§7, top-fragment-split type):** `D ≥ D(T_{n−2}) ≥ 1` for
  every 2-mark refinement where both splits act on the top's fragments, all `n`.
  The four-case block-contribution analysis (Cases 1–4) is verified
  `Fraction`-exact `n = 3,…,7`; the parity constraint `c = 4 ⟹ M ≤ n−2` is a valid
  deduction (`M ≡ n mod 2`, `M ≤ n−1` ⟹ `M ≤ n−2`). The load-bearing identity
  `D = D(T_n) − (c_M·2^M + c_m·2^m)/3` (Sub-case 1a) and
  `D = (2^n + (−1)^n − c·2^m)/3` (Sub-case 1b) both reproduce direct computation.
- **Even-group pair-cancellation + spine (§8):** `D ≥ 1` for even-group strong
  breakpoints, all `n`. Adjacent-equal pairs cancel (sign-agnostic); spine = distinct
  powers of 2; geometric dominance `2^{k_1} > Σ smaller = 2^{k_1}−1` gives `D ≥ 1`;
  nonempty via odd-total-mass. This is the SAME result as `tower-induction`'s S3
  (derived independently here from the PL/variational side). Correct.
- **Plateau-connectivity / V-shape (§9):** the V-shape obstruction (local
  rebalancing FAILS, `8→5+3` then `5→2.5+2.5` gives `D=2` > `D=1` at the tie
  `q=1`) is correctly verified `Fraction`-exact. The global-exchange gap is
  honestly characterized.

### Gaps found
- **(G1, the main wall) Non-dyadic multi-split `k ≥ 3`:** OPEN. The
  plateau-connectivity global exchange (prove the min-level set contains a dyadic
  config for `k ≥ 3`) is unproved. Verified `n ≤ 6`, not proved. This is the
  correct honest status.
- **Two-split lemma — Type C (second split on a tower piece):** verified
  `n = 3,…,7` but NOT proved. The lemma's scope is honestly restricted to
  top-fragment-split.
- **Two-split lemma — Type 4 (r-tower-tie) case enumeration:** the lemma claims
  "Cases 1–4 cover all breakpoint types where the ties involve tower pieces or
  fragment-fragment equalities," but Type 4 breakpoints (`q = 2^a` tower-tie,
  `r = 2^c` tower-tie, `s = 2^n − 2^a − 2^c` non-tower) are NOT explicitly
  addressed in the case analysis. They DO reduce to Case 1 by config-structure
  symmetry (the config `{non-tower, tower, tower} ∪ T_{n−1}` is the same multiset
  regardless of which fragment is the non-tower one), and they're verified (0
  violations, 245 Type-4 breakpoints `n = 3,…,7`), but the proof doesn't make the
  symmetry explicit. This is a minor rigor/exposition defect, not a fatal flaw —
  the formula is structurally symmetric and the conclusion holds.
- **(U) Upper bound general `n`:** deferred to `majorization-upper` (correctly).

### Lemma certifications
- **`two-split-lower-bound`** — **CERTIFY** with caveats. Formulas verified
  `Fraction`-exact (0 mismatches `n = 3,…,7`); `D ≥ D(T_{n−2})` verified (0
  violations). The parity-constrained geometric bound is correct. Caveats
  (noted in the lemma file's scope): (a) Type C (second split on a tower piece)
  is verified but NOT proved — scope restricted to top-fragment-split, as the
  builder honestly states; (b) the case-enumeration exhaustiveness claim is
  slightly overclaimed — Type 4 (r-tower-tie) breakpoints are not explicitly
  addressed but reduce to Case 1 by config-structure symmetry (verified, not
  separately proved). The lemma is a rigorous partial result within its stated
  scope; importers must respect the scope restriction.

### Route for next round
Attack G1 (k ≥ 3 non-dyadic multi-split) via the plateau-connectivity global
exchange. The 2-split sub-case (now certified) and the even-group sub-result
(too narrow) don't compose. The V-shape shows local rebalancing fails; a
multi-coordinate deformation preserving `D = D*` is needed. Alternatively, a
direct `D ≥ 1` argument at odd-count non-dyadic breakpoints (the shared wall
with `tower-induction`'s G2-odd) — the spine-sign-bookkeeping candidate.

---

## 2. `tower-induction` — CHANGES REQUESTED (partial)

### What's proved this round (correct, verified)
- **Lemma S1 (spine-pair-cancellation):** value-agnostic, correct. Removing
  adjacent-equal pairs preserves `D` (pair contributes 0; subsequent positions
  shift by 2, signs unchanged). The spine may not be unique but `D(spine) = D(M)`
  is invariant. 0 mismatches over 20 000 random configs.
- **Lemma S2 (strong-breakpoint group structure):** correct. At a strong
  breakpoint, non-dyadic fragments (value `≠ 2^k`) cannot tie tower pieces, so
  they form adjacent-equal groups of size `≥ 2`; even groups fully cancel, odd
  groups leave one leftover. Part (i) wording ("every dyadic fragment ties
  another dyadic fragment") is slightly imprecise (a dyadic fragment could tie
  an unsplit tower piece of the same value — but that tower piece is also
  "dyadic" by value, so the claim holds; the key conclusion about even/odd
  cancellation is correct).
- **Lemma S3 (even-group spine dominance):** correct. Geometric bound: `D ≥ 2^{k_1} − (2^{k_1}−1) = 1` (largest power exceeds sum of all smaller distinct
  powers). Nonempty via odd-total-mass (`D_n` odd, removed pairs even-mass).
  Verified: min `D = 1` over all 127 nonempty distinct-power-of-2 spines. This
  CLOSES the even-group strong-breakpoint sub-case of G1 for all `n` — an
  INDEPENDENT proof from `tail-count`'s §8 (here via spine decomposition; there
  via PL/variational pair-cancellation). Two independent proofs of the same
  sub-result.

### Gaps found
- **(G2-odd) Odd-count non-dyadic leftovers:** OPEN. When a non-dyadic group has
  odd count `≥ 3`, one leftover survives into the spine; its sign is a GLOBAL
  position-parity property (witnesses `{4.75,4,0.25}` `D=1` both at `+`;
  `{4,7/3,2}` `D=11/3` at `−`). The frontier recursion does NOT extend (block-
  contiguity is load-bearing on balanced splits producing equal adjacent
  fragments). Odd-group MINIMIZERS exist at `D=1`, so the bound must be tight to
  1. This is the shared G1 wall (block/spine side).
- **Strong-breakpoint scope:** S3 only covers STRONG breakpoints (every fragment
  ties an adjacent piece). The `pl-breakpoint-minimum` lemma only guarantees a
  (weak) breakpoint (per split, some tie exists). Non-strong breakpoints (a lone
  untied fragment, e.g. `{5,4,2,2,1,1}` for `T_3`, `D=1`) can also be minimizers
  and are NOT covered by S3. This is honestly acknowledged (§8 boundary).
- **(U1, U2) Upper bound general `n`:** unchanged, fallback only.

### Lemma certifications
- **`spine-pair-cancellation` (S1)** — **CERTIFY.** Value-agnostic, fully proved,
  0 mismatches. Foundational for any spine-based argument.
- **`strong-breakpoint-group-structure` (S2)** — **CERTIFY.** Correct (minor
  wording imprecision in part (i) noted, but the key even/odd cancellation
  conclusion holds). Depends on `spine-pair-cancellation`, `pl-breakpoint-minimum`.
- **`even-group-spine-lower-bound` (S3)** — **CERTIFY.** Geometric bound correct,
  nonempty via odd-total-mass, correctly scoped to even-group strong breakpoints.
  Closes the even-group sub-case of G1 for all `n`. Depends on S1, S2,
  `pl-breakpoint-minimum`.

### Route for next round
The odd-count leftover sign-bookkeeping is the open core. The candidate mechanism
(tying each leftover's sign to its splitting-tree origin) is undeveloped. The
shared wall with `tail-count`'s plateau-connectivity suggests a combined attack:
the spine decomposition + a global exchange that routes odd-count configs to
even-count or dyadic ones. A direct case analysis on the 1-leftover and
2-leftover spines (the tractable base cases) is the natural first step.

---

## 3. `gaps-leftover` — CHANGES REQUESTED (partial)

### What's proved this round (correct, verified)
- **Lemma G1 (gaps+leftover identity):** pure telescoping, correct for both
  parities (phantom-zero padding for even `m`). 0 mismatches over 20 000 configs.
  Trivial but clean; the value is in the proof object it invites (charging against
  the tower skeleton), not the statement.
- **Lemma G2 (pairing/leftover bound):** `D ≥ p_m` (odd `m`), `D ≥ 0` (even `m`).
  Trivial consequence of G1 + sortedness. 0 violations. Closes the `p_m ≥ 1`
  sub-region of the tower lower bound.
- **Top-split inductive decomposition (G3, reduction):** correctly identifies
  that `D(F ∪ R) ≠ D(F) + D(R)` (interleaving changes signs), and reduces the
  lower bound to an interleaving lemma conditional on `W(n−1)`. Honest reduction,
  not a standalone bound (correctly NOT submitted for certification).
- **Scope-gap handling (§3):** the even-`m` / fewer-marks cases are correctly
  reduced to certified lemmas (case A → `tower-top-unsplit`; B-i →
  `single-split-top-lower-bound`; B-ii-dyadic → `dyadic-refinement-lower-bound`).
  The uniform padded identity makes the charging target well-defined for both
  parities. The minimizer-at-even-`m` phenomenon (numerically observed) is
  honestly acknowledged.

### Gaps found
- **(G1 crux) Deficit-covering inequality:** OPEN. When `p_m < 1`, the gaps
  `Σ(p_{2k−1}−p_{2k})` must cover `1 − p_m`. The charging/matching argument
  (charge leftover to smallest tower level, charge each gap to a tower level,
  use dyadic dominance) is NOT proved. Verified `n = 3,4` (60k+ trials, 0
  violations; deficits covered exactly at minimizers). This is the genuinely-new
  machinery this framing was opened to provide, and it has not closed.
- **The "1 is conserved" picture** is a CONJECTURE supported by numerics, not a
  proof. Correctly flagged as GAP.
- **No upper-bound progress** (correctly deferred to `majorization-upper`).

### Lemma certifications
- **`gaps-leftover-identity` (G1)** — **CERTIFY.** Pure telescoping, both
  parities, 0 mismatches. Created lemma file (builder had not).
- **`pairing-leftover-bound` (G2)** — **CERTIFY.** Trivial consequence of G1,
  closes the `p_m ≥ 1` sub-region. Created lemma file (builder had not).
- G3 (top-split decomposition) — correctly NOT submitted (conditional reduction).
- G4 (dominance margin) — correctly NOT submitted (definitional, implicit in
  `frontier-recursion`).

### Route for next round
The deficit-covering crux is the hard step. The interleaving lemma (G3) pinpoints
where the obstruction enters: `F`-fragments at even global positions must be
chargeable to `R`-mass at odd positions plus the margin `1`. A concrete first step:
prove the crux for the 2-fragment `F` case (one top split + rest refined) by
direct case analysis on where the two fragments land, using the certified
`single-split-top-lower-bound` as the base. The V-shape obstruction (from
`tail-count`) warns that naive monotone charging fails; the charging must be
adaptive to the interleaving.

---

## 4. `majorization-upper` — CHANGES REQUESTED (partial)

### What's proved this round (correct, verified)
- **MB-Dom (dominant case `a_1 ≥ 2a_2`):** the halving induction is correct.
  Halving `a_1` into `{a_1/2, a_1/2}`: since `a_1/2 ≥ a_2`, the two halves sit at
  positions 1, 2 and cancel; the rest starts at position 3 (odd, same parity as
  rest-local position 1), so `D(total) = D(rest)`. Rest max `a_2 ≤ M/2`. Apply
  `W(n−1)` (piece-count-free): `D(rest) ≤ a_2/2^{n−1} ≤ M/2^n`. Parity preserved
  under recursive marking (rest-fragments stay `≤ a_2 ≤ a_1/2 =` the halves, so
  halves remain at positions 1, 2). Mark budget `1 + (n−1) = n`. ✓ The logic is
  sound; the base `n = 0` (`D ≤ a_1 = M`) is trivial and correct.
- **MB-Pair (non-dominant `a_1 < 2a_2`, `a_3 ≤ a_1/2`):** the pairing move
  `a_1 → {a_2, a_1−a_2}` is correct. Two copies of `a_2` at positions 1, 2 cancel.
  Rest' max `max(a_1−a_2, a_3) ≤ M/2` (both: `a_1−a_2 < a_1/2` from
  `a_1 < 2a_2 ⟺ a_2 > a_1/2 ⟺ a_1−a_2 < a_1/2`; `a_3 ≤ a_1/2` by hypothesis).
  Apply `W(n−1)`: `D(rest') ≤ M/2^n`. Parity preserved (`a_2 > a_1/2 ≥` rest'-max).
  The `m=2` case (no `a_3`, rest' = single fragment `a_1−a_2 < M/2`) is handled
  via scaling. ✓ The strictness argument is convoluted but not load-bearing (the
  upper bound only needs `≤`, not strict).
- **Max-bound conjecture verification:** 0 violations `n = 2,3,4` (2860+ configs);
  tight uniquely at the tower. The Schur/majorization route is correctly DROPPED
  (decisive counterexamples: `(1)` is most-majorizing yet `D* = 0`; non-tower
  configs majorize `T_3` yet have smaller `D*`).

### Gaps found
- **(The crux) `a_1 < 2a_2 ∧ a_3 > a_1/2`:** OPEN. After the pairing move, rest'
  max `= a_3 > M/2`, so `W(n−1)` gives `D(rest') ≤ a_3/2^{n−1}`, which overshoots
  `M/2^n` by the factor `2a_3/a_1 > 1`. The slack (rest' is non-tower, far from
  `T_{n−1}`, so the true `D*` is strictly below the Max-bound) is real but
  invisible to the worst-case IH. The two-variable IH `f(M, M_2, n)` is a
  candidate, not a proof.
- **MB-Dom and MB-Pair are CONDITIONAL on the Max-bound IH `W(n−1)`** — which is
  the Max-bound conjecture itself (proved only for base `n = 0,1,2`; open crux
  for `n ≥ 3`). Per the round-1 reviewer rule (never certify a lemma as
  standalone if its proof depends on an unproved IH), these are REJECTED as
  standalone certifiable lemmas. They are recorded as clean *reductions*
  (analogous to round-2 `U2`/`U3`). The lemma files have been marked
  "REDUCTION (NOT a standalone certified lemma)" to prevent misuse.
- **"Parity preserved under recursive marking" (MB-Dom):** the argument is correct
  but deserves scrutiny. The two halves (`a_1/2`) remain the largest pieces
  throughout because Xiang's subsequent splits produce fragments `≤ a_2 ≤ a_1/2`.
  Edge case `a_1/2 = a_2` (dominant boundary): three pieces tied at `a_1/2`; any
  ordering gives the same `D` (tie-agnostic). ✓ Verified 0 parity mismatches over
  155 836 random dominant configs.
- **MB-Pair "rest' max ≤ M/2" claim:** verified correct (both candidates
  `a_1−a_2 < a_1/2` and `a_3 ≤ a_1/2` by hypothesis; `a_4 ≤ a_3 ≤ M/2`, etc.).
  The bound `D(rest') ≤ max(rest')/2^{n−1} ≤ (M/2)/2^{n−1} = M/2^n` is valid.
  ✓

### Lemma certifications
- **`max-bound-dominant` (MB-Dom)** — **REJECT as standalone certifiable lemma.**
  Conditional on the unproved Max-bound conjecture `W(n−1)`. Recorded as a clean
  reduction (file marked "REDUCTION"). Analogous to round-2 `U2`.
- **`max-bound-pairing-small-third` (MB-Pair)** — **REJECT as standalone
  certifiable lemma.** Conditional on `W(n−1)`. Recorded as a clean reduction
  (file marked "REDUCTION"). Analogous to round-2 `U3`.

### Route for next round
The crux `a_1 < 2a_2 ∧ a_3 > a_1/2` is the single open sub-case. The two-variable
IH `f(M, M_2, n)` is the candidate but undeveloped. The adaptive optimal move
(explorer's trace) is sometimes pair, sometimes halve, depending on where
`a_1/2` sits relative to `a_2, a_3` — no single rule works. A concrete first
step: prove the Max-bound for the 3-large-piece crux at `n = 3` directly (it's
tractable by breakpoint enumeration, like `n = 2`), establishing the next base
case; then attempt the two-variable IH induction from `n = 3`. The residual-
integral language (`D = ∫(N mod 2)dt`) is the fallback for the crux.

---

## Summary of verdicts

| Slug | Verdict | Status | Key gap |
|------|---------|--------|---------|
| `tail-count` | CHANGES REQUESTED | partial | G1 (k≥3 non-dyadic multi-split plateau-connectivity); two-split Type C |
| `tower-induction` | CHANGES REQUESTED | partial | G2-odd (odd-count non-dyadic leftover sign-bookkeeping) |
| `gaps-leftover` | CHANGES REQUESTED | partial | G1 crux (deficit-covering when `p_m < 1`) |
| `majorization-upper` | CHANGES REQUESTED | partial | Max-bound crux (`a_1<2a_2 ∧ a_3>a_1/2`); MB-Dom/MB-Pair are reductions, not standalone |

**No APPROVE.** The problem remains `partial`. The answer `c(n) = 2^n/(2^{n+1}−1)`
is still conjectured (verified `n=1..4`), not proved for general `n`. The two
walls are: (lower) non-dyadic multi-split lower bound (G1, attacked from three
framings — PL/variational, block/spine, gaps/leftover — all converging on the
same odd-count/deficit-covering crux); (upper) the Max-bound crux (three
near-equal large pieces, single-gap-trap-safe unified conjecture). 6 NEW lemmas
certified (19 total); 2 proposed lemmas rejected as standalone (conditional
reductions, files marked).

The even-group strong-breakpoint sub-case of G1 is now closed by TWO independent
proofs (`tail-count` §8 via PL pair-cancellation; `tower-induction` S3 via spine
decomposition) — a verified milestone. The 2-split top-fragment sub-case is
closed (certified `two-split-lower-bound`). The `p_m ≥ 1` sub-region is closed
(certified `pairing-leftover-bound`). The Max-bound dominant + non-dominant-small-
third cases are clean reductions (conditional on the Max-bound IH).
