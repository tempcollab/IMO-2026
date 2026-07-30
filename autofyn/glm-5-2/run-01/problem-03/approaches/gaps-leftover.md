# gaps-leftover — IMO 2026 P3 (lower bound via per-pair-gap + leftover charging)

Round 3, NEW. A genuinely-different lower-bound framing: after Xiang refines the
tower `T_n` into `m` sorted pieces `p_1 ≥ … ≥ p_m`, the alternating sum
`D` telescopes into **per-pair gaps plus a leftover**. The lower bound
`D ≥ 1` (tower units) becomes "the `n` per-turn advantages plus one leftover
piece cover the target `1` (= the smallest tower piece)." The proof object is
a **charging/matching** argument against the tower's self-similar dyadic sizes —
third-party to the PL/variational (`tail-count`) and block/parity
(`tower-induction`) machinery on the same G1 wall.

## Status
partial

## Approaches tried
- (round 3) gaps+leftover identity + pairing bound + top-split inductive
  decomposition + scope-gap handling — PROVED the identity (both parities) and
  the pairing/leftover bound `D ≥ p_m` (m odd); PROVED the top-split
  decomposition reducing the lower bound to an interleaving lemma (conditional
  reduction, not a standalone bound); handled the outline-reviewer's scope gap
  (fewer-marks / even-`m` cases) by reducing the structured sub-cases to the
  certified lemmas and stating the charging target uniformly via the padded
  identity. Numerically verified `D ≥ 1` for `n=3,4` (60k+ random refinements
  each, 0 violations; identity confirmed both parities; minimizers at even `m`
  occur — scope gap is genuine). OPEN GAP: the charging/matching argument that
  proves the **gaps cover the deficit `1 − p_m`** when `p_m < 1` — the crux of
  G1 (non-dyadic multi-split). Honest partial: the framing stands, the
  reduction is clean, the crux is unproved.

## Current best
Two PROVEN results and one clean reduction (all below), plus the honest
characterization of the open G1 crux as a **deficit-covering** inequality.

The furthest rigorous progress:

**(I) Gaps+leftover identity (both parities)** — §1. For `m` sorted pieces,
`D = Σ_{k=1}^{⌊m/2⌋}(p_{2k−1}−p_{2k}) + [m odd]·p_m`. Proven by telescoping
the alternating sum; equivalently pad an even list with a phantom `0` piece to
recover the odd-length form. Each gap `p_{2k−1}−p_{2k} ≥ 0`.

**(II) Pairing / leftover bound** — §2. `D ≥ p_m` when `m` is odd and `D ≥ 0`
when `m` is even (equivalently Liu's odd-index take `≥ (T + p_m)/2` for odd `m`,
`≥ T/2` for even `m`, where `T = D_n`). Proven from the per-pair inequality
`p_{2k−1} ≥ p_{2k}`.

**(III) Scope-gap handling** — §3. The identity holds for every `m`; the
structured small-mark-count sub-cases reduce to certified lemmas (case A:
`tower-top-unsplit`; case B-i: `single-split-top-lower-bound`; case B-ii-dyadic:
`dyadic-refinement-lower-bound`); the charging target is stated **uniformly**
over both parities via the padded identity, so the open G1 crux is the single
inequality `Σ gaps + leftover ≥ 1` for every top-split, ≥ 2-mark refinement of
`T_n`, **regardless of `m`'s parity**.

**(IV) Top-split inductive decomposition (reduction, conditional on IH)** — §4.
If Xiang splits the top piece `2^n` into fragments `F` (sum `2^n = D_{n−1}+1`)
and refines `T_{n−1}` into `R` with the remaining `≤ n−1` marks, then
`D(T_n\text{'s refinement}) = D(F ∪ R)` and (by IH on `T_{n−1}`) `D(R) ≥ 1`.
The bound `D(F ∪ R) ≥ 1` reduces to an **interleaving lemma** (GAP): the mass
of top-fragments landing in even positions must be chargeable to `R`-mass in
odd positions. The reduction itself is proven; the interleaving lemma is the
open G1 crux in this framing's language.

**(V) The "1" as dominance margin (structural insight, not a standalone lemma)**
— §5. The `1` is exactly the **dominance margin** of the top piece:
`2^n − (2^n − 1) = 1`, i.e. the top tower piece exceeds the total of all smaller
tower pieces by exactly `1`. This is the conserved quantity the numerics see
flowing into gaps-or-leftover; it is the natural charging target. (Characterization
PROVED; the conservation `Σ gaps + leftover ≥ 1` itself is the open GAP.)

**Open gap (G1 crux, this framing):** prove
`Σ_{k}(p_{2k−1}−p_{2k}) + [m odd]·p_m ≥ 1` for every top-split, ≥ 2-mark
refinement of `T_n` (both parities of `m`). When `p_m ≥ 1` the pairing bound
closes it (§2); the deficit regime `p_m < 1` (some fragment smaller than the
smallest tower piece) is where the gaps must cover `1 − p_m` and where the
charging argument is required and unproved. Verified `n=3,4` (60k+ trials each,
0 violations; at minimizers the gaps cover the deficit *exactly*, supporting the
"1 is conserved" conjecture — but a proof is not known here).

## Full proof
Not yet complete. The lower bound is established unconditionally for cases A,
B-i, B-ii-dyadic (cited certified lemmas) and reduced cleanly for G1; the G1
crux (deficit-covering) is an explicit gap. The upper bound is owned by
`majorization-upper` (cited); `n=1` from `n1-base-both-bounds`. Hence `c(n) =
2^n/(2^{n+1}−1)` is not yet proved by this approach.

---

## Detailed development

### 0. Setup and imports

We work in **tower units**: `T_n = (2^n, 2^{n−1}, …, 2, 1)`, total
`D_n = 2^{n+1}−1`. The target lower bound is `D ≥ 1` (tower units), equivalently
Liu's odd-index take `≥ 2^n` (since `(D_n + D)/2 ≥ (D_n+1)/2 = 2^n`), i.e. the
real-unit guarantee `c(n) ≥ 2^n/D_n`.

Liu plays the tower `T_n` (Liu's `n` marks produce the `n+1` tower pieces; this
is WLOG Liu's optimal strategy by the certified lower-bound lemmas). Xiang
places `≤ n` marks, refining `T_n` into `m` pieces `p_1 ≥ … ≥ p_m`, `m ≤ 2n+1`,
total `D_n`. By Lemma 0 (`claim-game-odd-index`, certified), Liu's guaranteed
take is the odd-index sum, and `D := p_1 − p_2 + p_3 − …` satisfies
`Liu = (D_n + D)/2`. Thus `Liu ≥ 2^n ⟺ D ≥ 1`.

**Imported certified lemmas** (from `results/imo-2026-03/lemmas/`):
- `claim-game-odd-index` (Lemma 0): greedy optimal; Liu's take = odd-index sum;
  `D = 2·(Liu) − T`.
- `tower-top-unsplit` (case A): top piece unsplit ⇒ `D ≥ 1`, all `n`.
- `single-split-top-lower-bound` (case B-i): one mark splitting the top ⇒
  `D ≥ D(T_{n−1}) ≥ 1`, all `n`.
- `dyadic-refinement-lower-bound` (case B-ii-dyadic): all balanced splits ⇒
  `D ≥ 1`, all `n`.
- `frontier-recursion`: `D(T_n) = (2^{n+1}+(−1)^n)/3 ≥ 1`; balanced top split
  `T_n → T_{n−1}`; `D_n = 2·D_{n−1} + 1`.
- `closed-form-answer`: `r_n = 2^n/(2^{n+1}−1)` is the candidate closed form.
- `n1-base-both-bounds`: `c(1) = 2/3`.
- `pl-breakpoint-minimum`: Xiang's optimum over refinements is at a
  breakpoint (used to justify that the charging target is attained at a
  structured config, though the bound itself must still be proven).

### 1. The gaps+leftover identity (PROVEN, both parities)

**Lemma G1 (gaps+leftover identity).** Let `p_1 ≥ p_2 ≥ … ≥ p_m` be a
nonincreasing list of nonnegative reals. Let `D = p_1 − p_2 + p_3 − p_4 + …` be
the alternating sum (sign `+` on odd indices). Then

$$D \;=\; \sum_{k=1}^{\lfloor m/2\rfloor}\bigl(p_{2k-1}-p_{2k}\bigr) \;+\; \mathbf{1}_{m\ \text{odd}}\cdot p_m.$$

In particular each summand `p_{2k−1}−p_{2k} ≥ 0` (sorted), and the "leftover"
`p_m` (when `m` is odd) is `≥ 0`, so `D ≥ 0` always.

**Proof.** This is a telescoping of the alternating sum, partitioned into
consecutive disjoint pairs.

- *`m` odd, `m = 2ℓ+1`.* Group the terms as
  `(p_1−p_2) + (p_3−p_4) + … + (p_{2ℓ−1}−p_{2ℓ}) + p_{2ℓ+1}`. Every index
  `1,…,2ℓ+1` appears exactly once with the correct sign: indices `2k−1` carry
  `+`, indices `2k` carry `−`, and the final odd index `2ℓ+1` is the lone
  unpaired `+` term. Hence `D = Σ_{k=1}^{ℓ}(p_{2k−1}−p_{2k}) + p_{2ℓ+1}`. ∎

- *`m` even, `m = 2ℓ`.* Group as `(p_1−p_2) + … + (p_{2ℓ−1}−p_{2ℓ})`; every
  index is paired, no leftover. So `D = Σ_{k=1}^{ℓ}(p_{2k−1}−p_{2k})`.

  *Equivalent odd-form (padding):* append a phantom piece `p_{2ℓ+1} := 0` to
  obtain an odd-length list `p_1,…,p_{2ℓ},0`. The alternating sum is unchanged
  (adding a trailing `0` contributes `0`), and the odd-form identity gives
  `D = Σ_{k=1}^{ℓ}(p_{2k−1}−p_{2k}) + 0`, matching the even form. Thus the
  single odd-form formula with leftover `p_m` (taken to be `0` when `m` is even
  via padding) covers both parities. ∎

**Numerical confirmation:** the identity `D == Σ gaps + [m odd]·p_m` holds with
0 failures over 30 000 random refinements of `T_3` and `T_4` each, for both
parities of `m` (`/tmp/round-3/gaps_leftover_check.py`). ∎

This identity is purely algebraic; its diversity from the PL-integral
(`D = ∫(N(t) mod 2)dt`, `D-equals-parity-integral`) and block-formula
(`D = Σ_k 2^k(−1)^{C_k}(n_k mod 2)`, `block-contribution-formula`) lies in the
**proof object it invites** — a charging of each gap and the leftover against
the tower skeleton — not in the statement (which is, algebraically, the same
`D ≥ 1`).

### 2. The pairing / leftover bound (PROVEN)

**Lemma G2 (pairing bound).** With the notation of Lemma G1,
- if `m` is odd, `D ≥ p_m` (equivalently Liu's odd-index take `≥ (T + p_m)/2`);
- if `m` is even, `D ≥ 0` (Liu's odd-index take `≥ T/2`),
where `T = Σ_i p_i = D_n` is the (constant) total.

**Proof.** Since the list is sorted, `p_{2k−1} ≥ p_{2k}` for every `k`, hence
every gap `g_k := p_{2k−1}−p_{2k} ≥ 0`.

- *`m` odd (`m = 2ℓ+1`):* by Lemma G1, `D = Σ_{k=1}^{ℓ} g_k + p_{2ℓ+1} ≥ p_{2ℓ+1}
  = p_m` (each `g_k ≥ 0`). Equivalently,
  `Liu = (T+D)/2 ≥ (T + p_m)/2`. ∎
- *`m` even (`m = 2ℓ`):* by Lemma G1 (even form), `D = Σ_{k=1}^{ℓ} g_k ≥ 0`.
  Equivalently `Liu ≥ T/2`. ∎

A more direct derivation of the equivalent "Liu ≥ `(T+p_m)/2`" form: in each
consecutive pair `(p_{2k−1}, p_{2k})`, the odd-index member `p_{2k−1} ≥
(p_{2k−1}+p_{2k})/2` (pair-mass halving), and (for odd `m`) the unpaired
leftover `p_m` is taken fully by Liu. Summing: `Liu ≥ Σ_k(p_{2k−1}+p_{2k})/2 +
[m\text{ odd}]·p_m = (T − [m odd]·p_m)/2 + [m odd]·p_m = T/2 + [m odd]·p_m/2`. ∎

**Consequence (immediate lower-bound sub-result).** If `m` is odd and
`p_m ≥ 1` (the smallest piece is at least the smallest tower piece), then
`D ≥ 1` by Lemma G2. In particular, every refinement whose smallest piece
exceeds or meets `1` is settled. This closes a clean (if partial) sub-region of
the refinement space. ∎

**Where Lemma G2 is insufficient.** When `p_m < 1` — i.e. some Xiang fragment is
*smaller than the smallest tower piece* — the pairing bound yields only
`D ≥ p_m < 1`. Such fragments arise from splitting any tower piece and creating
a sub-`1` fragment (e.g. split `2` into `1.5 + 0.5`). The **deficit**
`1 − p_m` must then be covered by the gaps `Σ g_k`. This is exactly the regime
where the charging/matching argument is needed (the G1 crux, §6). Numerically
(`/tmp/round-3/gaps_leftover_check.py`, stress run): when `p_m < 1`, the gaps
cover the deficit *exactly* at minimizers (`Σ g_k + p_m = 1.000`), supporting
the "1 is conserved" picture — but this conservation is the unproved step.

### 3. Scope-gap handling (outline-reviewer's mandatory fix)

The outline-reviewer flagged that the odd-`m` identity (§1, `m = 2n+1`) covers
only Xiang's using-exactly-`n`-marks refinements, and that the lower bound must
hold for **every** `≤ n`-mark refinement — including fewer marks (`m` smaller)
and even `m`. We handle this as follows.

**Case partition (exhaustive, disjoint).** Xiang's refinement of `T_n` either

- **(A)** leaves the top piece `2^n` unsplit — *any* number of marks, *any*
  parity of `m*; or
- **(B)** splits the top piece `2^n` (≥ 1 Xiang mark on the top piece). Within
  (B):
  - **(B-i)** exactly one Xiang mark total, on the top;
  - **(B-ii)** ≥ 2 Xiang marks, top split. Within (B-ii):
    - **(B-ii-dyadic)** every split is balanced (each split halves its piece);
    - **(B-ii-nondyadic)** at least one split is unbalanced — **this is G1**.

**Reduction of the structured sub-cases to certified lemmas (no new proof
needed):**

- **(A)** — `tower-top-unsplit` (certified): `D ≥ 1/D_n` (real units) `= 1`
  (tower units), for all `n`, regardless of the number of marks Xiang spends on
  the rest and regardless of `m`'s parity. The intact top piece `2^n` strictly
  exceeds the total `(2^n − 1)` of the rest, so it occupies position 1 and
  `D = 2^n − D(R') ≥ 2^n − (2^n − 1) = 1`. ✓ (This handles all even-`m` and
  small-`m` refinements that avoid the top piece — exactly the "fewer marks"
  cases the reviewer worried about, so long as the top is untouched.)

- **(B-i)** — `single-split-top-lower-bound` (certified): one mark splitting the
  top gives `D ≥ D(T_{n−1}) ≥ 1`, all `n` (the global min is the plateau
  `q ∈ [2^{n−2}, 2^{n−1}]` where the refinement is a balanced top split
  reducing to `T_{n−1}`; the PL slope is in `{0,−2}`). Here `m = n + 2` (one
  extra piece from the single split): parity is `n + 2` mod 2 = `n` mod 2 — so
  both parities occur and are covered by this certified lemma. ✓

- **(B-ii-dyadic)** — `dyadic-refinement-lower-bound` (certified, via
  `frontier-recursion`): `1 ≤ D ≤ 2^n − 1` for every balanced-split refinement,
  all `n`. Equality `D = 1` at the all-`1`s cascade. Here `m` ranges over
  `n+1+k` for `k` balanced splits, `1 ≤ k ≤ n`; both parities occur and are
  covered. ✓

**The open sub-case (B-ii-nondyadic) is exactly G1**, and within it `m` ranges
over `n+1+k` for `k ∈ {2,…,n}` marks, so `m ∈ {n+3,…,2n+1}` — **both parities
occur**. The gaps+leftover identity (§1) is stated **uniformly** for both
parities (via the padding convention, leftover `= 0` when `m` even), so the
charging target is the single inequality

$$\sum_{k=1}^{\lfloor m/2\rfloor}(p_{2k-1}-p_{2k}) \;+\; [\text{$m$ odd}]\cdot p_m \;\ge\; 1, \qquad m \in \{n+3,\ldots,2n+1\},$$

for every top-split, ≥ 2-mark, non-dyadic refinement of `T_n`. No parity is
excluded; the scope gap is closed by (i) the uniform padded identity and (ii)
the reduction of every structured sub-case to a certified lemma. The
**unproved** content is the inequality itself (§6). ∎

(Note: the minimizer of `D` over `≤ n`-mark refinements is *not* always at
exactly `n` marks — e.g. for `n = 2` the min `D = 1` is attained at both 1-mark
and 2-mark configs; for `n = 3,4` our numerics find minimizers at even `m`
(`m = 6` at `n = 3`, `m = 8` at `n = 4`). So the even-`m` regime is not a
vacuous formality — it contains genuine minimizers. The uniform padded identity
is what makes the charging target well-defined there.)

### 4. Top-split inductive decomposition (reduction, conditional on IH)

To organize the G1 crux, we record a clean decomposition that pinpoints
*where* the interleaving obstruction enters. It is a **reduction** (conditional
on the inductive hypothesis `W(n−1): D ≥ 1` for every `≤ (n−1)`-mark refinement
of `T_{n−1}`), recorded as a reduction rather than a standalone bound — in the
spirit of the certified-but-conditional reductions `U2`/`U3` of
`majorization-upper`.

**Lemma G3 (top-split decomposition — reduction).** *Assume* the inductive
hypothesis `W(n−1)`: for every `≤ (n−1)`-mark refinement `R` of `T_{n−1}`,
`D(R) ≥ 1` (tower units of `T_{n−1}`, equivalently the same `1` as for `T_n`
since the smallest tower piece is `1` in both). Consider a refinement of `T_n`
in which Xiang splits the top piece `2^n` into fragments
`F = (f_1,…,f_{k+1})` (`k ≥ 1` marks on top, `Σ f_i = 2^n`) and refines
`T_{n−1}` with the remaining `≤ n − k ≤ n − 1` marks into a multiset `R`.
Then:
- the refined multiset is `F ∪ R` (a single interleaved sorted list), total
  `2^n + (2^n − 1) = D_n`;
- `D(F ∪ R)` is the alternating sum of this interleaved list, **not**
  `D(F) + D(R)` (interleaving changes the signs of `R`'s pieces);
- by IH, `D(R) ≥ 1` and `Σ F = 2^n = D_{n−1} + 1` (the top piece exceeds the
  total of `T_{n−1}` by exactly `1`).

The lower bound `D(F ∪ R) ≥ 1` reduces (under IH) to an **interleaving lemma**:
the mass of `F`-fragments landing at even global positions must be chargeable
to `R`-mass at odd global positions plus the "dominance margin" `1`. (Precise
form in §6.)

**Proof of the decomposition (the reduction part).** That the refined multiset
is `F ∪ R` with total `D_n` is immediate: `T_n = {2^n} ∪ T_{n−1}`,
`Σ T_n = 2^n + D_{n−1} = (D_{n−1}+1) + D_{n−1} = 2·D_{n−1}+1 = D_n`. Xiang's
marks on the top piece produce `F` (`Σ F = 2^n`); his remaining marks refine
`T_{n−1}` into `R` (`Σ R = D_{n−1}`). The two sub-multisets are then
concatenated and globally re-sorted; the global alternating sum
`D(F ∪ R) = Σ_i (−1)^{i+1} p_i` where `p_i` is the global sorted order — this
is in general **not** `D(F) + D(R)` because `R`'s pieces do not occupy
contiguous global positions (they interleave with `F`'s fragments), so their
signs in the global alternating sum differ from their signs in `D(R)`'s
isolated alternating sum. By IH (applied to `T_{n−1}` with `≤ n−1` marks) we
have `D(R) ≥ 1`. The remaining obligation — proving `D(F ∪ R) ≥ 1` — is
therefore *not* a consequence of `D(R) ≥ 1` alone; it requires controlling the
sign distortion from interleaving. ∎ (reduction complete; interleaving lemma =
GAP)

The "dominance margin" `1` entering the reduction is the structural fact

$$2^n - D_{n-1} \;=\; 2^n - (2^n - 1) \;=\; 1,$$

i.e. the top tower piece exceeds the total of all smaller tower pieces by
exactly `1` — equivalently `D_n = 2·D_{n−1} + 1` (`frontier-recursion`). This
`1` is the conserved quantity the numerics of §2 see flowing into
gaps-or-leftover.

### 5. The "1" as dominance margin (structural characterization)

**Lemma G4 (the target "1" is the top-dominance margin).** In tower units, the
target `1` of the lower bound `D ≥ 1` equals the dominance margin of the top
tower piece:

$$1 \;=\; 2^n - \sum_{j=0}^{n-1} 2^j \;=\; 2^n - (2^n - 1) \;=\; 2^n - D_{n-1}.$$

Moreover `D_n = 2·D_{n−1} + 1`, so the margin `1` is the additive constant of
the tower's self-similar recursion.

**Proof.** `D_{n−1} = 2^n − 1` (geometric sum), so
`2^n − D_{n−1} = 2^n − (2^n−1) = 1`. And
`D_n = 2^{n+1}−1 = 2(2^n−1) + 1 = 2·D_{n−1} + 1` (`frontier-recursion`,
certified). ∎

This identifies the natural charging target: the `1` is *exactly the excess of
the top piece over the whole rest*. When Xiang splits the top piece, this
excess is what must be "absorbed" by the gaps and the leftover. The
conservation picture (`1 → Σ gaps + leftover`) observed numerically is the
statement that this absorption always succeeds — which **is** the lower bound.
Lemma G4 is a characterization, not a proof of conservation.

### 6. The charging/matching crux (G1 — OPEN GAP)

**Target (G1, this framing).** Prove that for every top-split, ≥ 2-mark,
non-dyadic refinement of `T_n` (the sub-case (B-ii-nondyadic), `m ∈
{n+3,…,2n+1}`, both parities),

$$\boxed{\;\sum_{k=1}^{\lfloor m/2\rfloor}(p_{2k-1}-p_{2k}) \;+\; [\text{$m$ odd}]\cdot p_m \;\ge\; 1\;}$$

using only the tower's self-similar dyadic sizes `{2^n,…,2,1}` and the
dominance margin `1 = 2^n − D_{n−1}`.

**Equivalent reformulation (Xiang-take form).** Since `D = D_n − 2·(\text{Xiang's
even-index take})`, `D ≥ 1 ⟺` Xiang's even-index take `≤ (D_n − 1)/2 =
(2^{n+1}−2)/2 = 2^n − 1 = D_{n−1}`. So the crux is equivalently:

> *After any top-split, ≥ 2-mark, non-dyadic refinement of `T_n`, the total
>  mass captured by Xiang (the even-index pieces) is at most `D_{n−1}` — the
>  total of all tower pieces below the top.*

The "1" deficit is then `1 = 2^n − D_{n−1}`: Liu must retain at least the
top piece's worth `2^n`, i.e. Xiang must lose at least the margin `1` relative
to an even split.

**What is PROVED (genuine sub-results of this framing):**

1. *If `p_m ≥ 1` (smallest piece ≥ smallest tower piece):* the pairing bound
   (Lemma G2) gives `D ≥ p_m ≥ 1`. ✓ (closes the `p_m ≥ 1` sub-region.)
2. *If `m` is even:* `D = Σ gaps` (no leftover); the target is `Σ gaps ≥ 1`.
   (No sub-region is closed here in general; the even-`m` minimizers of our
   numerics had `p_m ≥ 1` — i.e. the smallest piece was an intact tower piece —
   so they were closed by sub-result 1. But even-`m` minimizers with
   `p_m < 1` are not ruled out by anything proven here.)
3. *Base `n = 1` (top-only split):* `T_1 = {2,1}`, one split of the top
   `2 → f_1 + f_2` (`f_1 ≥ f_2`, `f_1+f_2 = 2`), rest `{1}`. If `f_2 ≥ 1` then
   `f_1 = f_2 = 1` (sum 2, sorted), `D = 1 − 1 + 1 = 1`. If `f_2 < 1` the sorted
   list is `(f_1, 1, f_2)` and `D = f_1 − 1 + f_2 = (f_1+f_2) − 1 = 2 − 1 = 1`.
   So `D = 1` **always** at `n = 1` for the top-only split. ✓ (This matches
   `n1-base-both-bounds`; recorded here in the gaps+leftover language.)

**What is OPEN (the G1 crux):** the deficit regime `p_m < 1`, where the gaps
must cover `1 − p_m`. The natural charging argument would:

(i) charge the leftover `p_m` to the smallest tower level `1`;
(ii) charge each per-pair gap `g_k = p_{2k−1} − p_{2k}` to a tower level
     `{2^n, 2^{n−1}, …, 2}` so that the total charge `≥ 1`;
(iii) prove the charging is feasible using the tower's dyadic dominance
     (`2^j > Σ_{i<j} 2^i`) and the dominance margin `2^n − D_{n−1} = 1`.

The obstruction (flagged by the explorer and confirmed by the `tail-count` /
`tower-induction` framings): the global sorted order **interleaves**
`F`-fragments with `R`-pieces, so a per-pair gap is not in general a
"tower-level gap"; the matching must be **adaptive** to the interleaving, and
no clean per-level or per-fragment rule is visible (the V-shape
`8 → 5+3` then `5 → 4+1` gives `D = 1`, but rebalancing `5 → 2.5+2.5` gives
`D = 3` — an *increase* — so "balance reduces `D`" is false and a naive
monotone charging fails). The interleaving lemma of §4 (Lemma G3) is the
precise open statement.

**Honest assessment.** The charging/matching argument is the genuinely-new
machinery this framing was opened to provide, and it has not closed here. The
framing's *clean sub-results* — the gaps+leftover identity (Lemma G1), the
pairing bound (Lemma G2), the top-split decomposition (Lemma G3, reduction),
the dominance-margin characterization (Lemma G4), and the `p_m ≥ 1` sub-region
closure — are PROVEN and independent of the PL/block machinery; the G1 crux
(deficit-covering when `p_m < 1`) is an explicit GAP. This is an honest partial:
the framing stands as a rival population member, the scope gap is handled, but
the lower bound is not complete.

### 7. Numerical verification (`/tmp/round-3/gaps_leftover_check.py`)

- `n = 3`, 30 000 random `≤ 3`-mark refinements of `T_3`: min `D = 1.000000`,
  0 violations; identity holds both parities (0 failures); pairing bound holds
  (0 failures). A minimizing config (even `m = 6`): `{4.49, 4, 2.01, 2, 1.49,
  1}` (top split + one interior split, smallest piece `1` = intact tower level
  → closed by sub-result 1).
- `n = 4`, 30 000 random `≤ 4`-mark refinements of `T_4`: min `D = 1.000000`,
  0 violations; identity & pairing bound hold.
- *Stress (small-leftover regime, `p_m < 1`)* — `n = 3`: min `D = 1.000000`
  among configs with `p_m < 1`, at `p_m = 0.154`, `m = 7` (odd), gaps `= 0.846`,
  `gaps + leftover = 1.000` (deficit covered exactly). `n = 4`: min `D =
  1.0018` among `p_m < 1` configs (deficit covered with equality at the true
  minimizer). This supports the "1 is conserved" picture but is **not** a proof
  (rigor rule).

These are sanity checks, not proof steps; the written proof above stands on
its own.

### 8. Upper bound

Owned by `majorization-upper` (cited): the Max-bound halving induction
`D* ≤ M/2^n` unifies G1-upper/G2; `n = 1` from `n1-base-both-bounds`
(certified); `n = 2` from `n2-upper-bound-complete` (certified). This approach
does not advance the upper bound. The final answer (if both bounds close) is
`c(n) = 2^n/(2^{n+1}−1)` (`closed-form-answer`, algebraic).

## Promotable lemmas

1. **`gaps-leftover-identity`** (Lemma G1, §1) — for sorted `p_1 ≥ … ≥ p_m`,
   `D = Σ_{k=1}^{⌊m/2⌋}(p_{2k−1}−p_{2k}) + [m odd]·p_m` (both parities, via
   phantom-zero padding). Pure telescoping; holds for any sorted multiset, not
   just tower refinements. Proven in full above. Importable by any approach
   that wants the gaps+leftover decomposition of the alternating sum.

2. **`pairing-leftover-bound`** (Lemma G2, §2) — for sorted `p_1 ≥ … ≥ p_m`,
   `D ≥ p_m` (m odd) / `D ≥ 0` (m even); equivalently Liu's odd-index take
   `≥ (T + p_m)/2` (m odd) / `≥ T/2` (m even). Proven in full above. Closes the
   `p_m ≥ 1` sub-region of the lower bound for the tower.

(Lemmas G3, G4 are reductions / characterizations rather than standalone proven
bounds; G3 is conditional on IH `W(n−1)` and is therefore proposed as a
*reduction* (like `majorization-upper`'s `U2`/`U3`) rather than a certifiable
lemma, and G4 is a definitional identity already implicit in
`frontier-recursion`. Neither is submitted for certification.)
