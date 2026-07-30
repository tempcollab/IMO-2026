# Approach: xor-overlap (5th lower-bound framing)

**Target (whole problem, lower bound half).** Prove `D(M) ≥ 1` (tower units) for every
`≤ n`-mark Xiang refinement `M` of the dyadic tower `T_n = (2^n, 2^{n-1}, …, 2, 1)`, for all
`n ≥ 1`. Equivalently `c(n) ≥ 2^n/D_n` where `D_n = 2^{n+1} − 1`. (Combined with the
certified upper bound for `n ≤ 3` this would yield `c(3) = 8/15`; the upper bound for
general `n` is the separate concern of `majorization-upper`.)

This approach is a genuinely-5th framing of the lower-bound wall: it attacks via an
**exact overlap/correlation decomposition** of the `D`-integral, *not* global-position
parity, PL/variational geometry, block/spine cancellation, gaps-leftover charging, or LP
duality. The four converged framings (`tail-count`, `tower-induction`, `gaps-leftover`,
`lp-dual-certificate`) all bottom out on the same global-sort obstruction; this framing
isolates a different object (the overlap `C` of two *separately structured* parity
functions) and reduces `G1(n) → G1(n−1) + overlap-bound`.

---

## Status
partial

## Approaches tried
- **Round 5 (NEW).** Built the XOR-overlap framing from scratch. Proved and proposed for
  certification the **XOR identity** `D(M) = D_F + D_R − 2C` (lemma file
  `lemmas/xor-overlap-identity.md`), a bilinearity-of-parity decomposition of the
  `D`-integral. Proved the **tight base case `n = 1`** (`D_F = 2C` exactly, `D = 1`).
  Set up the **strong induction `G1(n) → G1(n−1) + overlap bound`**: `R` is a
  `≤ (n−1)`-mark refinement of `T_{n−1}`, so `D_R ≥ 1` by the inductive hypothesis;
  closing needs the **overlap bound `C ≤ (D_F + D_R − 1)/2`** (GAP-X). Attempted the
  overlap bound via (a) trivial measure/Cauchy-Schwarz bounds, (b) per-fragment charging,
  (c) the dyadic-structure of the unsplit-`R` odd region, (d) a recursive expansion; all
  routes give only the trivial `D ≥ 0` or reduce to already-closed sub-cases, EXCEPT the
  genuinely-open non-dyadic-`R` case which is **honestly G1(n−1)-equivalent** (not a
  shortcut). GAP-X remains open; no false claim of closure. Verified the identity exact
  (3000 random refinements, 0 failures) and the base case (exact `Fraction`, all `f ∈
  (1,2)`); numerics correctly labeled verification-not-proof.

## Current best
The **exact XOR identity** `D(M) = D_F + D_R − 2C` is PROVED (proposed lemma, certifiable
on its own merits — pure algebra on top of the certified `D-equals-parity-integral`).
The **tight base `n = 1`** is proved (`D_F = 2C`, `D = 1` for every split of the top
piece). The **inductive reduction** `G1(n) ⟹ (case (a): certified `tower-top-unsplit`)
∪ (case (b): `G1(n−1)` + GAP-X)` is set up correctly. The single open gap is **GAP-X**
below: a bound on the overlap `C = |Ω_F ∩ Ω_R|` of the two odd-parity regions that is
stronger than the trivial `C ≤ min(D_F, D_R)` and `C ≤ √(D_F D_R)` (Cauchy-Schwarz), both
of which give only `D ≥ 0`. GAP-X is, as a *standalone sufficient* statement, equivalent in
difficulty to `G1` itself (the bound `C ≤ (D_F + D_R − 1)/2` is `D ≥ 1` restated); the
framing's value is the *decoupled object* `C` and the clean induction `G1(n) →
G1(n−1) + overlap`, NOT a difficulty reduction.

## Full proof
*Not complete — GAP-X (below) is open. The rigorous portion follows.*

### 0. Conventions and imported facts

Work in **tower units**: the stick has length `D_n = 2^{n+1} − 1`, the tower is
`T_n = (2^n, 2^{n-1}, …, 2, 1)`, and the lower bound to prove is `D(M) ≥ 1` for every
`≤ n`-mark refinement `M` of `T_n` (this rescales to `D(M) ≥ 1/D_n` on the unit stick, i.e.
`c(n) ≥ 2^n/D_n`; the rescaling is the one used in every certified lemma and is
immaterial).

**Imported (certified).**
- `claim-game-odd-index` (Lemma 0): in the alternating draft on a sorted multiset, the
  first mover (Liu) takes the odd-index sum `= (S + D)/2`. So Liu guarantees `(S + D)/2`,
  and `D(M) ≥ 1` ⟺ Liu guarantees `(D_n + 1)/2 = 2^n` ⟺ the lower bound. The target is
  *exactly* `D(M) ≥ 1`.
- `D-equals-parity-integral`: `D(P) = ∫_0^∞ (N_P(t) mod 2) dt` for any sorted multiset `P`,
  with `N_P(t) = #{i : p_i ≥ t}`.
- `tower-top-unsplit` (case (a)): if Xiang leaves the top piece `2^n` unsplit, then
  `D(M) ≥ 1` for all `n`, with **no** induction hypothesis (uses `2^n > 2^n − 1`).
- `frontier-recursion`: `D(T_n) = 2^n − D(T_{n−1}) = (2^{n+1} + (−1)^n)/3 ≥ 1`, the
  recurrence used in the consistency check.

### 1. The XOR-overlap identity (PROVED — proposed lemma)

**Proposed lemma (`lemmas/xor-overlap-identity.md`).** Let `M` be a refinement of `T_n`
partitioned as `M = F ⊎ R`, where `F` is the refinement of the top piece `2^n`
(`Σ f_i = 2^n`, `k ≥ 1` fragments — `k = 1` means the top is unsplit) and `R` is the
refinement of the below-top tower `T_{n−1}` (`Σ r_j = 2^n − 1`). With `D_F = D(F)`,
`D_R = D(R)`, and
`C = ∫_0^∞ (N_F(t) mod 2)(N_R(t) mod 2) dt = |Ω_F ∩ Ω_R|`, one has

$$D(M) \;=\; D_F \;+\; D_R \;-\; 2\,C. \tag{XOR}$$

**Proof (summary; full proof in the lemma file).** The pieces of `M` are the disjoint
union of `F`'s and `R`'s pieces, so `N_M(t) = N_F(t) + N_R(t)` for every `t`. For
nonnegative integers `a, b` the parity identity
`(a + b) mod 2 = (a mod 2) + (b mod 2) − 2 (a mod 2)(b mod 2)`
holds (check the four `(a mod 2, b mod 2)` cases; it is `a ⊕ b = a' + b' − 2a'b'` in
`{0,1}`). Substituting `a = N_F(t), b = N_R(t)` and integrating (Tonelli, finite support)
gives `D(M) = ∫(N_F mod 2)dt + ∫(N_R mod 2)dt − 2∫(N_F mod 2)(N_R mod 2)dt = D_F + D_R − 2C`,
the first two integrals being `D_F, D_R` by the certified `D-equals-parity-integral`
(the integral is intrinsic to each sub-multiset, independent of any merging). ∎

(Verified exact: 0 failures over 3000 random refinements of `T_2,…,T_5`, exact
`Fraction` arithmetic; consistency check `F = {2^n}, R = T_{n−1}` recovers
`D(M) = 2^n − D(T_{n−1}) = D(T_n)` ✓. Numerics are verification, not proof — the proof
above stands on its own.)

**Reformulation.** With `Ω_F = {t : N_F(t) odd}`, `Ω_R = {t : N_R(t) odd}`, identity
(XOR) reads `D(M) = 2|Ω_F ∪ Ω_R| − |Ω_F| − |Ω_R| = D_F + D_R − 2|Ω_F ∩ Ω_R|`. Hence

$$D(M) \ge 1 \;\;\Longleftrightarrow\;\; |\Omega_F \cup \Omega_R| \;\ge\; \tfrac{D_F + D_R + 1}{2}
\;\;\Longleftrightarrow\;\; C \;\le\; \tfrac{D_F + D_R - 1}{2}. \tag{XOR-bound}$$

The two odd-parity regions must be *almost disjoint*: their overlap is at most half their
total measure minus `1/2`.

### 2. Tight base case `n = 1` (PROVED)

For `n = 1`, `T_1 = (2, 1)`, `D_1 = 3`. Xiang has `≤ 1` mark.

- **Sub-case (a): top `2` unsplit.** `M = {2, 1}`, `D = 2 − 1 = 1 ≥ 1`. ✓ (This is
  `tower-top-unsplit` at `n = 1`, certified.)
- **Sub-case (b): top `2` split by the one mark.** `F = (f, 2 − f)` with
  `f ≥ 2 − f`, i.e. `f ∈ [1, 2]` (the case `f = 2` is the unsplit limit, already
  covered; take `f ∈ [1, 2)` for a genuine split). `R` refines `T_0 = (1)` with `≤ 0`
  marks, so `R = {1}` (the single below-top piece, unsplit — `T_0` admits no refinement).

Compute the three objects directly from their definitions.

- `D_F = D({f, 2−f}) = f − (2 − f) = 2f − 2`.
- `D_R = D({1}) = 1`.
- `Ω_F`: `N_F(t)` counts fragments `≥ t`. With `f ≥ 1 > 2 − f ≥ 0`:
  - `t ∈ [0, 2 − f)`: both fragments `≥ t`, `N_F = 2` (even) → not in `Ω_F`;
  - `t ∈ [2 − f, f)`: only `f ≥ t`, `N_F = 1` (odd) → in `Ω_F`;
  - `t ≥ f`: `N_F = 0` → not in `Ω_F`.
  So `Ω_F = [2 − f, f)`, `|Ω_F| = f − (2 − f) = 2f − 2 = D_F`. ✓
- `Ω_R`: `N_R(t) = 1` for `t ∈ [0, 1)`, `0` for `t ≥ 1`; so `Ω_R = [0, 1)`,
  `|Ω_R| = 1 = D_R`. ✓
- `C = |Ω_F ∩ Ω_R| = |[2 − f, f) ∩ [0, 1)|`. For `f ∈ [1, 2)`, `2 − f ∈ (0, 1]` and
  `f ≥ 1`, so `[2 − f, f) ∩ [0, 1) = [2 − f, 1)` (empty when `f = 1`, i.e. `2 − f = 1`,
  giving the degenerate equal-split `F = {1, 1}`; otherwise a single interval of length
  `1 − (2 − f) = f − 1`). Thus `C = f − 1`.

Hence `D_F = 2f − 2 = 2(f − 1) = 2C` **exactly**, and by (XOR)

$$D(M) \;=\; D_F + D_R - 2C \;=\; 2C + 1 - 2C \;=\; 1. \qquad\checkmark$$

The base case is **tight**: equality `D = 1` holds for *every* split `f ∈ [1, 2)`, and
the cancellation `D_F = 2C` is exact (no slack at the base — the entire margin comes from
`D_R = 1`, the contribution of the unsplit below-top piece). ∎

(Verified with exact `Fraction` arithmetic for `f ∈ {1.1, 1.2, …, 1.9}` and at the
degenerate `f = 1`; all give `D = 1`, `D_F = 2C` exactly.)

### 3. Inductive setup (PROVED, conditional on GAP-X)

Let `G1(n)` be the statement: *every `≤ n`-mark refinement `M` of `T_n` has `D(M) ≥ 1`.*
We prove `G1(n)` by **strong induction on `n`**, assuming `G1(n'')` for all `n'' < n`.
Base `n = 1` is §2. (The certified `tower-top-unsplit` and the `n = 1` certified
`n1-base-both-bounds` also supply `n = 1`; §2 is the XOR-specific base.)

**Inductive step.** Let `M` be a `≤ n`-mark refinement of `T_n`. Partition it as
`M = F ⊎ R` where `F` is the refinement of the top piece `2^n` and `R` the refinement of
`T_{n−1}` (§1).

- **Mark accounting.** If the top is split into `k ≥ 2` fragments, that uses `k − 1 ≥ 1`
  marks on the top piece, leaving at most `n − (k − 1) ≤ n − 1` marks for the refinement
  of `T_{n−1}`. So `R` is a refinement of `T_{n−1}` using **`≤ n − 1` marks**. By the strong
  inductive hypothesis `G1(n − 1)`, the standalone alternating sum of `R` satisfies
  `D_R = D(R) ≥ 1`. (If the top is unsplit, `k = 1`, we are in case (a), closed by
  `tower-top-unsplit` — no induction needed.)

- **Case (a) (top unsplit, `k = 1`):** `D(M) ≥ 1` by `tower-top-unsplit` (certified,
  no IH). ✓

- **Case (b) (top split, `k ≥ 2`):** apply (XOR):
  `D(M) = D_F + D_R − 2C ≥ D_F + 1 − 2C`, using `D_R ≥ 1` from the IH.
  To conclude `D(M) ≥ 1`, it suffices to prove the **overlap bound**

  $$\boxed{\;C \;\le\; \frac{D_F + D_R - 1}{2}.\;} \tag{GAP-X}$$

  (Then `D(M) ≥ D_F + D_R − (D_F + D_R − 1) = 1`.) Note GAP-X uses the *actual* `D_R`
  (not just `D_R ≥ 1`); the weaker sufficient condition `C ≤ D_F/2` (obtained by replacing
  `D_R` with `1` in GAP-X) is **false** (see §4).

Thus `G1(n)` reduces to `G1(n − 1)` + GAP-X. The reduction is well-formed: `R`'s
refinement of `T_{n−1}` with `≤ n − 1` marks is exactly the input class of `G1(n − 1)`.

### 4. The overlap bound GAP-X — attempted routes (OPEN)

We record four serious attempts; none closes GAP-X. Each is documented with the precise
obstruction, so the next round can pick the most promising.

#### 4.1. Trivial measure / Cauchy-Schwarz bounds (give only `D ≥ 0`)

`Ω_F, Ω_R` are measurable subsets of `[0, 2^n)`, `Ω_R ⊂ [0, 2^{n−1}]`. Generic
inequalities:

- **Sub-measure:** `C = |Ω_F ∩ Ω_R| ≤ min(|Ω_F|, |Ω_R|) = min(D_F, D_R)`.
- **Cauchy-Schwarz** (for `{0,1}`-valued `1_{Ω_F}, 1_{Ω_R}`, with `1_{Ω}^2 = 1_{Ω}`):
  `C = ∫ 1_{Ω_F} 1_{Ω_R} ≤ √(∫1_{Ω_F} · ∫1_{Ω_R}) = √(D_F D_R)`.

Combining (XOR) with `C ≤ √(D_F D_R)`:
`D(M) ≥ D_F + D_R − 2√(D_F D_R) = (√D_F − √D_R)^2 ≥ 0`.
The trivial bound recovers `D ≥ 0` — the certified `pairing-leftover-bound` (Lemma G2)
trivial lower bound — and nothing more. The `1` in `D ≥ 1` is *not* captured by these
generic inequalities: they hold for arbitrary measurable sets, ignoring the tower
structure entirely. (And `C ≤ min(D_F, D_R)` gives `D(M) ≥ max(D_F, D_R) − min(D_F, D_R)`,
again `≥ 0` only.)

#### 4.2. The sufficient condition `D_F ≥ 2C` FAILS at minimizers

Replacing `D_R` by its lower bound `1` in GAP-X gives the *sufficient* (not necessary)
condition `C ≤ D_F/2`, i.e. `D_F ≥ 2C`. This is appealing because `D_F` is a function of
`F` alone (decoupled from `R`). It is, however, **false**:

- Numerically (exact `Fraction`, breakpoint/tie configs of `T_4`): `D_F ≥ 2C` fails in
  **543 of 2196** breakpoint top-split pairs; worst deficit `D_F − 2C = −6` at
  `F = {9, 3, 3, 1}`, `R = {8, 2, 2, 1, 1, 1}` (a `T_4` minimizer neighborhood).
- At genuine `D = 1` minimizers, `D_F < 2C` is *common*; the deficit is exactly
  compensated by `D_R > 1` (the below-top refinement has standalone `D_R` strictly above
  the inductive floor). The `1` margin is **not** absorbed locally by the top split; it
  requires the below-top tower structure.

So the decoupled sufficient condition is too strong; only the *exact* bound GAP-X (which
uses the real `D_R`) can work, and the exact bound is `D ≥ 1` restated (circular as a
*standalone* fact — its value is the inductive framing, not a self-contained shortcut).

#### 4.3. Dyadic structure of `Ω_R` for unsplit / dyadic `R` (covers only an already-closed sub-case)

When `R` is the **unsplit tower** `T_{n−1} = (2^{n-1}, …, 2, 1)`, the odd-parity region
`Ω_R` is a union of **dyadic** intervals. Specifically `N_R(t)` on `(ℓ_{i+1}, ℓ_i]`
(the `i`-th gap of the descending tower, `ℓ_i = 2^{n-1-i+1} = 2^{n-i}`) equals `i`, so
`Ω_R = ∪_{i odd} (2^{n-i-1}, 2^{n-i}]`, a disjoint union of dyadic intervals of the form
`(2^j, 2^{j+1}]`. The same holds when `R` is any **dyadic** (all-balanced-splits)
refinement of `T_{n−1}` (by `block-contribution-formula`, the parity structure is
dyadic). In this regime one may hope to bound `C` by a *pigeonhole on dyadic intervals*:
`Ω_F` (a union of `≤ k` intervals from splitting `2^n`, total `D_F`) overlaps the
`⌈(n−1)/2⌉` dyadic intervals of `Ω_R`.

**However**, this dyadic structure of `Ω_R` is *lost* once `R` is a non-dyadic refinement
(the G1-hard case for `R`): only ~37%/29%/24% of randomly-refined `R` have purely-dyadic
`Ω_R` for `T_2/T_3/T_4` (verified); e.g. `R = {5/8, 15/8, 3/2, 2, 1}` (a refinement of
`T_2`-mass `3`) has `Ω_R = [0, 5/8] ∪ [1, 3/2] ∪ [15/8, 2]`, **not** dyadic. So a
"dyadic-misalignment lemma" on `C` covers *only* the sub-case where `R` is unsplit /
dyadic-refined — which is **already closed** by the certified
`dyadic-refinement-lower-bound` (Lemma: `1 ≤ D ≤ 2^n − 1` for every balanced-split
refinement of `T_n`, all `n`). It yields no progress on the genuinely-open non-dyadic
`R` regime. (Recorded as a *reproduction* of a known result via the XOR framing —
demonstrating the framing is non-circular and reproduces certified sub-cases — but not a
new closure.)

#### 4.4. Per-fragment charging of the overlap

Decompose `Ω_F = ⊔_{i odd} (f_{i+1}, f_i]` (the `i`-th gap of `F`'s descending sort,
`f_{k+1} := 0`), so `D_F = Σ_{i odd} (f_i − f_{i+1})` and
`C = Σ_{i odd} |(f_{i+1}, f_i] ∩ Ω_R|`. Each per-gap contribution `C_i ≤ f_i − f_{i+1}`
(the gap length), giving `C ≤ D_F` (the trivial sub-measure bound, §4.1). Charging each
gap *against a tower level* (cf. `gaps-leftover`'s charging against the tower skeleton,
but now on **regions** not positions) would require, per gap, a tower piece of
*comparable length* lying in the same threshold band — exactly the global-interleaving
obstruction the four converged framings hit. The per-gap charge does not compose: the
position parity of a fragment is a global functional of the entire sorted multiset, so a
local per-gap rule cannot reach the `1`. (Symptom: the V-shape — after `8 → 5 + 3`, the
second split is V-shaped and rebalancing *increases* `D`.)

#### 4.5. Recursive expansion (telescopes only at terminals)

One may expand `R` itself via (XOR): split `T_{n−1}`'s top `2^{n−1}` into `F'` and recurse
on `T_{n−2}`. This builds a binary decomposition tree indexed by tower levels; each
*internal* node contributes a `-2·(node overlap)` term, each *leaf* where the top is
unsplit contributes a case-(a) margin `1` (the dominance `2^k − (2^k − 1) = 1`). The `D`
of the full refinement is `(sum of leaf margins) − 2·(sum of internal overlaps)`. Closing
`D ≥ 1` would require the internal overlaps to telescope against the leaf margins; the
cross-level overlap terms couple adjacent levels and do **not** telescope in any obvious
way (verified structurally; no clean cancellation found). This is a candidate for a future
round but is not a proof.

### 5. GAP-X — precise statement and honest status

> **GAP-X (open).** For every `n ≥ 2`, every split `F` of the top piece `2^n`
> (`Σ f_i = 2^n`, `k ≥ 2` fragments), and every `≤ (n−1)`-mark refinement `R` of
> `T_{n−1}`, with `D_F, D_R, C` as in §1,
>
> $$C \;=\; |\Omega_F \cap \Omega_R| \;\le\; \frac{D_F + D_R - 1}{2}.$$

**Honest status.** As a *standalone sufficient* statement, GAP-X is **equivalent in
difficulty to `G1` itself**: by (XOR-bound), GAP-X is exactly `D(M) ≥ 1`, i.e. `G1(n)`.
The value of the XOR framing is therefore *not* a difficulty reduction — it is a
**genuinely-different attack surface** (a correlation of two *separately*-structured
parity functions, one dyadic — `Ω_F` — and one — `Ω_R` — inherited from `T_{n−1}`,
coupled only through the product `C`), together with a clean inductive reduction
`G1(n) → G1(n−1) + GAP-X` and a provably tight base case. This is the same logical
status as `lp-dual-certificate`'s GAP-LP2 (honestly G1-equivalent by LP strong duality):
a rival *proof mechanism* for the same wall, kept far from the four converged framings.

**Diversity check (vs the four converged framings).**
- vs `tail-count` (PL/variational): GAP-X is a measure bound on a correlation, *not* a
  PL-geometry / breakpoint-transport statement (no V-shape, no star-shaped level set).
- vs `tower-induction` (block/spine): GAP-X is a real overlap of two parity *regions*,
  not an adjacent-equal-pair cancellation or a spine sign-bookkeeping.
- vs `gaps-leftover` (charging): GAP-X couples two *regions*, not pairs of *positions*;
  no per-pair gap charging against tower levels.
- vs `lp-dual-certificate` (LP/Farkas): `C` is a *dynamic* overlap depending on both `F`
  and `R`, with a clean inductive reduction; the LP dual objective
  `Σ_t y_eq[t]·2^{n−t}` is a *static* certificate with no induction on `n`.

### 6. Summary of what is proved

1. **XOR identity** `D(M) = D_F + D_R − 2C` (proposed lemma, certifiable).
2. **Tight base `n = 1`** (`D_F = 2C` exactly, `D = 1` for every top split).
3. **Inductive reduction** `G1(n) → G1(n−1) + GAP-X` (mark accounting +
   `tower-top-unsplit` for case (a)).
4. **Non-circularity reproduction**: the dyadic-`R` sub-case is reachable by the XOR
   framing (and reduces to the certified `dyadic-refinement-lower-bound`).
5. **Open**: GAP-X (the overlap bound). Honestly G1-equivalent; not a shortcut.

## Promotable lemmas
- **XOR-overlap identity** (`lemmas/xor-overlap-identity.md`): `D(M) = D_F + D_R − 2C`
  for the top-split / below-top partition of any `T_n` refinement, via bilinearity of
  the `D`-integral parity product. PROVED in full (Step 1 count-split, Step 2 pointwise
  parity identity with four-case check, Step 3 Tonelli integration invoking the
  certified `D-equals-parity-integral`). Consistency check on the unsplit tower recovers
  `D(T_n) = 2^n − D(T_{n−1})`. Proposed for certification; importable by any approach
  wanting a correlation/overlap decomposition of `D`.
