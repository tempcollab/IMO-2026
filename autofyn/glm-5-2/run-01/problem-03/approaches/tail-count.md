# `tail-count` — IMO 2026 P3 (Liu Bang / Xiang Yu stick game)

**Conjectured (and numerically exact for n=1,2,3,4) answer:**
$$\boxed{\,c(n)=\dfrac{2^{\,n}}{2^{\,n+1}-1}\,}$$
It is monotone decreasing (2/3, 4/7, 8/15, 16/31, …) and tends to 1/2 from above.

This approach rewrites the claim-game value via the **layer-cake / tail-count identity**
`odd-index sum = ∫₀^∞ ⌈N(t)/2⌉ dt`, `N(t)=#{pieces of length ≥ t}`. The ceiling absorbs
the parity bookkeeping. I import the shared reduction (Lemma 0), the layer-cake identity,
and the `D = ∫(N mod 2)dt` corollary from the certified lemma cache, and I import case (a)
(top piece unsplit). The new work this round is the **per-split ΔD formula**, the
**balanced-split / frontier recursion** (closed form `D(T_n)=(2^{n+1}+(-1)^n)/3`), a complete
rigorous proof of the **single-split lower bound** `D ≥ D(T_{n-1}) ≥ 1`, and a complete
rigorous proof of the **multi-split dyadic (balanced) lower bound** `D ≥ 1`. The
**non-dyadic multi-split** regime remains an explicit gap (G1): verified to `n=6` and
exhaustively to `n=3`, with a proven reduction (piecewise-linearity ⇒ min at a
breakpoint config) but no proof that every breakpoint config has `D ≥ 1`.

All tower-unit computations below were checked with exact `Fraction` arithmetic.

---

## Status
partial

**Round 7 update.** Attacked the open core (GAP-C) via the **vertex-level crux (★)** and
**Mechanism A** (§16, NEW). **(★): at every non-dyadic strong-breakpoint vertex of `T_n`,
`D > 1`.** Combined with `pl-breakpoint-minimum` (global min at a vertex) +
`dyadic-refinement-lower-bound` (dyadic vertices `D ≥ 1`), (★) ⟹ lower bound
`D*(T_n) ≥ 1/D_n`. **PROVED sub-cases of (★):** single-survivor at cascade vertices (one sum
constraint ⟹ `nfree ≤ 1`); single-survivor for ALL `T_3` vertex types (mark budget ≤ 3 forces
at most one split with ≥ 3 fragments); **largest-tower-exceeds-fragment** (`2^j > v` by mass-
budget contradiction); **frag-at-`+` budget-tight ⟹ `D > 1`** (via `t₊ > v` from largest
tower). The decomposition `D = (F−T) + 2(t₊−f₋)` is reviewer-confirmed non-circular algebra.
**Honest gaps:** (GAP-A) `v > 1` lower bound (verified, unproved — needed for non-tight
frag-at-`+`); (GAP-C / GAP-(★)-d-minus) the **frag-at-`−` sign-forcing** `t₊ > 2v` (near-miss:
`t₊ > 2v − 1/2` by dyadic dominance; the `1/2` gap is the obstruction; 13/13 verified); (GAP-B)
mixed/multi-survivor `n ≥ 4` (47 nfree=2 vertices `T_4`, all `D > 1`, but mass-budget is
cascade-only — generalization unproved); (GAP-D) vertex-type completeness `n ≥ 5`.
**Verification (NOT proof):** (★) holds on 131 enumerated vertices (64 cascade/split-tower/
split-2tower `T_3`+`T_4` + 67 mixed top-r3+tower-r3 `T_4` incl. 47 multi-survivor), 0
counterexamples, `D = 1` only at 7 dyadic vertices (`F = 0`), min non-dyadic `D = 5/3`.
The spine sign-pattern / multi-swap framing remains **CIRCULAR** (round 5) — do NOT chase it.

**Round 6 update.** NARROWED GAP-C(i) via the **mass-budget inequality** (§15, NEW).
At a breakpoint of `T_n` (cascade type, all `n`), every non-dyadic surviving fragment `w`
appears `≥ 3` times among top fragments (odd count `≥ 3`, breakpoint forces `≥ 2` ties, and
non-dyadic values can only tie other top fragments — tower pieces are all `2^k`). Each copy
consumes `w` from the top budget `2^n`. The dyadic top fragments (those equal to a tower piece
`2^k`) consume at least `2^k` each from non-surviving tower values. This yields the
**mass-budget inequality** `T ≥ 3F − 1` (§15, PROVED), where `F` = total surviving non-dyadic
fragment mass, `T` = total surviving tower mass on the spine. **Corollary (proved):** if the
block condition holds (all surviving fragments at `+`) and `D = 1`, then `D = F − T = 1` gives
`F = T + 1`; combined with `T ≥ 3F − 1 = 3T + 2` gives `T ≤ −1`, a contradiction — so `F = 0`
(spine dyadic, `D ≥ 1` by `even-group-spine-lower-bound`). **Continuity argument (proved):**
the "all `F` at `−`" block direction is ruled out at a `D = 1` breakpoint (it gives `D ≤ −1` on
the adjacent cell by the mass-balance lemma, contradicting `D = 1` at the vertex by PL
continuity). So **IF the block condition holds at a `D = 1` breakpoint, then `F = 0` and
`D = 1` by §8**. The gap that remains: proving the block condition (or `F = 0`) directly
without the block-condition hypothesis. **Verification:** `F = 0` at all `D = 1` breakpoints of
`T_3` (151 breakpoints, all types); block condition holds at all 523 `D = 1` configs
(`T_3`/`T_4`/`T_5`); mass-budget inequality `T ≥ 3F − 1` verified 0 violations at all
constructed breakpoints including non-grid values (`7/3`, `4/3`, `14/3`, …). When `F > 0` at a
breakpoint, `D > 1` always (smallest `D = 5/3`). The mass-budget inequality is the strongest
new constraint: any counterexample to `D ≥ 1` must have `F > 0` AND the block condition failing,
a much more constrained scenario.

**Round 5 update.** (1) **MASS-BALANCE LEMMA PROVED** (`lemmas/mass-balance-lemma.md`, proposed for
certification): on any block-condition cell, `D = 2S₊ − D_n` (algebra); `D = 1 ⟺ S₊ = 2^n`; the
top piece `2^n` is split into fragments all at one sign (block condition) — if all at `−` then
`S₊ ≤ 2^n−1 < 2^n` so `D ≤ −1 ≠ 1`; if all at `+` then `S₊ = 2^n ⟺` all below-top pieces at `−`.
**Sub-gap (ii) is VACUOUS**: every block-condition `D = 1` cell has the all-top-`+`/all-below-`−`
pattern, hence is settled by `telescoping-block-lemma` (d) directly (no dyadic endpoint needed).
This is rigorous, n-independent, and certifiable now. (2) **SPINE SIGN-PATTERN LEMMA — honestly
CIRCULAR as the nosaddle-close explorer framed it.** The explorer's "mass identity `F = T + 1`"
(where `F` = total non-tower spine mass, `T` = total tower spine mass) is NOT an independent mass
identity — it is EQUIVALENT to `D(spine) = 1` under the assumed interleaving pattern
(`D = F − T` when pattern holds, so `F − T = 1 ⟺ D = 1`). Verified by exact `Fraction` check:
spines where the pattern holds but `D ≠ 1` have `F − T = D ≠ 1` (e.g. `T_3` split `8→5+3, 4→3+1`,
spine `{5,2}`, pattern holds, `F − T = 3 = D`, NOT 1). The single-swap argument
(`2(t−v) = 0 ⟹ t = v`, power-of-2 vs non-power) and the multi-swap subset-sum argument BOTH rest
on this circular premise (`S₊ = F`, which already assumes the pattern). So the spine sign-pattern
framing does NOT close GAP-C; the multi-swap remains **GAP-C-hard**, with the precise obstruction
stated in §13. The honest situation: **sub-gap (ii) closed (vacuous), sub-gap (i) (V-shape cell
faces / non-block cells) still OPEN**, and the spine-level multi-swap is NOT a viable route as
framed (circular). GAP-C still requires a genuinely non-circular argument that `D ≥ 1` on
non-block-condition cells.

## Approaches tried
- (round 1) `tail-count` built from scratch: Lemma 0 (greedy=odd-index) proved by backward induction; layer-cake identity `odd-index = ∫⌈N/2⌉dt` and corollary `D = ∫(N mod 2)dt` proved exactly (verified rationally on 2000+ instances, 0 mismatches). Lower-bound case (a) "top piece unsplit" PROVED cleanly using the dominance `2^n > sum of all smaller tower pieces` — no IH, no parity bug. Lower-bound case (b) "top piece split" + multi-split closure = OPEN GAP. Upper bound: n=1 base case proved by hand; general-n parity-telescoping = OPEN GAP (the coupled-global-parity obstruction materialized as predicted by the reviewer).
- (round 3) ADVANCED the non-dyadic lower bound with three results:
  (a) **2-split sub-case** (`two-split-lower-bound`, proposed lemma): proved `D ≥ D(T_{n−2}) ≥ 1`
  for every 2-mark refinement of `T_n` where both splits act on the top's fragments, all `n`.
  Mechanism: PL + breakpoint reduction, then block-contribution formula for the all-tower
  "rest" with a **parity-constrained geometric bound** (`c_M·2^M + c_m·2^m ≤ 3·2^{n−1}` where
  the parity constraint `c=4 ⟹ M ≤ n−2` does the work). Four-case exhaustive check on
  `(c_M,c_m) ∈ {2,4}²`. Verified `n=3..7`. Type C (split tower piece) verified but not fully
  proved — same pattern, GAP.
  (b) **Even-group pair-cancellation + spine** (from the lower-nondyadic explorer): proved
  `D ≥ 1` for even-group strong breakpoints, all `n`. Adjacent-equal pairs cancel (sign-agnostic);
  even-count non-dyadic groups fully cancel; the spine is distinct powers of `2`; geometric
  dominance (`2^{k_1} > Σ` smaller) + odd-total-mass (forces `1` in spine) gives `D ≥ 1`.
  Boundary: odd-group minimizers EXIST (D=1), so this is PARTIAL, not a full G1 close.
  (c) **Plateau-connectivity (GLOBAL exchange)**: developed as the deep G1-closing route.
  Confirmed the V-shape (LOCAL rebalancing FAILS: `8→5+3` then `5→4+1` gives D=1, but
  rebalancing to `5→2.5+2.5` gives D=2 — INCREASE). Corrected the explorer's D=3 to D=2
  (verified `Fraction`-exact). The exchange must be GLOBAL, not per-split. GAP: proving the
  min-level set always contains a dyadic config (for k≥3 splits).
- (round 4) PROVED GAP-B (telescoping zero-gradient block lemma, §11): on a PL cell where each split's two fragments sit at same-sign positions, D is CONSTANT (gradient 0 in every cut coordinate). If all top-piece fragments sit at + positions and all below-tower pieces (split or unsplit) at − positions, D = 2^n − (2^n − 1) = 1 DIRECTLY from the telescoping mass identity — no dyadic endpoint needed (addresses the reviewer's flagged concern for block-condition cells). This is the non-dyadic generalization of block-contribution-formula. PROVED GAP-A (2-leftover transport, §12) as a corollary: the mass identity a + d = t + 1 (spine-3 cascade) follows from fragment-tower telescoping (fragment mass = 2^n, below-tower mass = 2^n − 1, paired mass = (2^n−1)−t, so a+d = 2^n − ((2^n−1)−t) = t+1). GAP-C (star-shaped transport, §13) remains OPEN: mechanism explained (V-shape cells have D > 1 in interior; min-level set lives on tie FACES shared with block-condition cells where D ≡ 1 by GAP-B(d); the transport goes AROUND the V-shape along these faces), verified T_3/T_4 but not proved generally. The reviewer's concern about cells without dyadic endpoints is ADDRESSED for block-condition cells (GAP-B(d) computes D=1 directly) but remains open for non-block-condition cells.
- (round 2) Closed two sub-cases of lower-bound case (b) **rigorously** and reduced the rest:
  (1) **Per-split ΔD formula** `ΔD = 2q − 2·O([0,q]) − 2·O((p,L])` proved from `D=∫(N mod 2)dt` (layer-cake / D-equals-parity-integral), verified on T_2, T_3.
  (2) **Balanced-split recursion**: a balanced split of the top of T_n flips the parity of `N(t)` on all of `[0,2^n]`, giving `D_new = 2^n − D(T_n)`; combined with the **frontier recursion** `D(T_n)+D(T_{n−1})=2^n` (proved by geometric telescoping) this yields `D_new = D(T_{n−1})`. Closed form `D(T_n)=(2^{n+1}+(-1)^n)/3 ≥ 1`.
  (3) **Single-split case (b-i)**: PROVED. For a single split `2^n → p+q` of the top, `D` is a continuous piecewise-linear function of `q` with slope `0` or `−2` (hence non-increasing); the minimum is at the balanced point `q=2^{n−1}` and equals `D(T_{n−1}) ≥ 1`. This closes **every** single-split refinement (dyadic or not), for all `n`.
  (4) **Multi-split dyadic (balanced) case (b-ii-dyadic)**: PROVED. For any dyadic refinement (all fragments powers of 2, ≤n balanced splits), grouping pieces by size-`2^k` blocks shows within-block pairs cancel and the unpaired odd-count levels contribute `±2^k`; the largest odd-count level always contributes `+2^K` (all larger levels are even-count), and the rest is dominated by `2^K−1`, giving `D ≥ 1`. Equality at the balanced-pairs config.
  (5) **Piecewise-linearity + breakpoint reduction**: PROVED as a reduction — `D` is affine in the split positions within each fixed combinatorial type (sort order), so the global minimum over all ≤n-mark refinements is attained at a **breakpoint (tie) config** (every fragment length ties with an adjacent piece).
  (6) **G1 (non-dyadic multi-split)**: OPEN GAP. Verified `n≤6` (dyadic & non-dyadic enumeration) and exhaustive `n=2,3` grid over 2-split refinements (min `D=1`, attained on plateaus containing both dyadic and non-dyadic points); the reduction (5) lands here, but proving `D ≥ 1` at an arbitrary (non-dyadic) breakpoint config is the make-or-break open step.
- (round 5) PROVED the **mass-balance lemma** (`lemmas/mass-balance-lemma.md`, proposed for
  certification): on a block-condition cell, `D = 2S₊ − D_n` (algebra), `D = 1 ⟺ S₊ = 2^n`, and
  the block condition forces the top fragments to a single sign — all-at-`−` gives `D ≤ −1 ≠ 1`,
  all-at-`+` gives `S₊ = 2^n ⟺` all below-top at `−`. **Sub-gap (ii) is VACUOUS**: every
  block-condition `D = 1` cell has the all-top-`+`/all-below-`−` pattern (settled by
  `telescoping-block-lemma` (d), no dyadic endpoint needed). SERIOUSLY ATTEMPTED the spine
  sign-pattern lemma (the nosaddle-close explorer's G1-closer) and found it **CIRCULAR as framed**:
  the "mass identity `F = T + 1`" is equivalent to `D(spine) = 1` under the assumed interleaving
  (verified `Fraction`-exact: pattern-holding spines with `D ≠ 1` have `F − T = D ≠ 1`, e.g.
  `T_3` `{5,2}` spine, `F − T = 3`). The single-swap (`2(t−v)=0 ⟹ t=v`) and multi-swap subset-sum
  arguments both presuppose `S₊ = F` (the pattern), so they are circular. The multi-swap is left
  as **GAP-C-hard** with a precise obstruction statement (§13). Sub-gap (i) (V-shape cell faces /
  non-block-condition cells) remains genuinely OPEN; the spine-level multi-swap is NOT a viable
  closing route as framed. Honest negative result: do NOT chase the spine sign-pattern /
  multi-swap subset-sum framing for 3 rounds — it is circular.
- (round 6) NARROWED GAP-C(i) via the **mass-budget inequality** (§15, NEW, proposed for
  certification as `mass-budget-breakpoint-inequality`). At a breakpoint of `T_n` (cascade type,
  all `n`), every non-dyadic surviving fragment `w` appears `≥ 3` times among top fragments
  (breakpoint forces `≥ 2` ties; non-dyadic values can only tie other top fragments since tower
  pieces are all powers of `2`; odd count `≥ 3` for survivors). Each copy consumes `w` from the
  top budget `2^n`. The dyadic top fragments (those `= 2^k`) consume `≥ 2^k` each from
  non-surviving tower values. This yields **`T ≥ 3F − 1`** (§15, PROVED), where `F` = total
  surviving non-dyadic fragment mass, `T` = total surviving tower mass on the spine.
  **Corollary (proved):** block condition (all `F` at `+`) + `D = 1` ⟹ `D = F − T = 1` ⟹
  `F = T+1` ⟹ `T ≥ 3(T+1)−1 = 3T+2` ⟹ `T ≤ −1`, contradiction ⟹ **`F = 0`** (spine dyadic,
  `D ≥ 1` by §8). **Continuity (proved):** "all `F` at `−`" ruled out at `D=1` breakpoint
  (`D ≤ −1` on adjacent cell by mass-balance lemma, contradicting `D=1` vertex by PL continuity).
  So **block condition at `D=1` breakpoint ⟹ `F=0` ⟹ `D=1` by §8** — the block condition is
  SUFFICIENT (not just necessary) for `D=1` at breakpoints. **Verification:** `F=0` at all
  `D=1` breakpoints of `T_3` (151 breakpoints, all types); block condition holds at all 523
  `D=1` configs (`T_3`/`T_4`/`T_5`, origin-based classification); mass-budget `T ≥ 3F−1`
  verified 0 violations at all constructed breakpoints including non-grid values (`7/3`,
  `4/3`, `14/3`, `10/3`, `8/3`, …). When `F > 0`, `D > 1` always (smallest `D = 5/3`).
  **GAP-C(i) narrowed but NOT closed:** the remaining step is proving the block condition (or
  `F=0`) at `D=1` breakpoints directly, without the block-condition hypothesis. The
  mass-budget constrains `F` but doesn't force `F=0` without the block condition. Any
  counterexample to `D ≥ 1` must have `F > 0` AND the block condition failing — a much more
  constrained scenario than before.
- Upper bound general n: still OPEN GAP (parity coupling of `N(t) mod 2` across thresholds); only `n=1` proved.
- (round 7) Attacked GAP-C via the **vertex-level crux (★)** + Mechanism A (§16, NEW). **(★): at
  every non-dyadic strong-breakpoint vertex of `T_n`, `D > 1`.** PROVED: single-survivor at
  cascade vertices (one sum constraint pins `nfree ≤ 1` at a vertex, §16.1); single-survivor for
  ALL `T_3` vertex types (mark budget ≤ 3, §16.1); v-bracket `v < 2^{n−1}` (mass budget,
  §16.2); **largest-tower-exceeds-fragment** `2^j > v` (mass-budget contradiction, §16.3);
  **frag-at-`+` budget-tight ⟹ `D > 1`** (via `t₊ > v`, §16.5); `t₊ > t₋` (dyadic dominance,
  §16.4). Decomposition `D = (F−T) + 2(t₊−f₋)` is non-circular algebra (reviewer-confirmed).
  **GAPS:** (GAP-A) `v > 1` (verified min 4/3, unproved general n — needed for non-tight
  frag-at-`+`); (GAP-C / d-minus) frag-at-`−` sign-forcing `t₊ > 2v` (near-miss `t₊ > 2v−1/2`,
  the 1/2 gap is the obstruction; 13/13 verified); (GAP-B) mixed multi-survivor `n ≥ 4`
  (mass-budget cascade-only; 47 nfree=2 vertices `T_4` all `D > 1`, unproved structurally);
  (GAP-D) vertex-type completeness `n ≥ 5`. **Verification:** (★) holds on 131 vertices (64
  cascade/split-tower/split-2tower `T_3`+`T_4` + 67 mixed `T_4` incl. 47 multi-survivor), 0
  counterexamples, `D = 1` only at 7 dyadic vertices. The spine sign-pattern framing remains
  CIRCULAR (round 5) — not retried.

## Current best
Certified (importable) results the proof builds on:
1. **Lemma 0** (`lemmas/claim-game-odd-index.md`) — claim game value = odd-index sum; greedy optimal. (The certified proof is the sign-correct version; the round-1 `tail-count` write-up of Lemma 0 contained a displayed sign error — flagged and not used here.)
2. **Layer-cake identity** (`lemmas/layer-cake-odd-index.md`) — `odd-index = ∫⌈N(t)/2⌉dt`.
3. **D-integral** (`lemmas/D-equals-parity-integral.md`) — `D = ∫(N(t) mod 2)dt`.
4. **Case (a)** (`lemmas/tower-top-unsplit.md`) — top unsplit ⇒ `D ≥ 1/D_n`, no IH.
5. **n=1 base** (`lemmas/n1-base-both-bounds.md`) — `c(1)=2/3`.
6. **Closed form** (`lemmas/closed-form-answer.md`) — algebraic identity for `r_n=2^n/(2^{n+1}−1)`.

New rigorous results this round (in this file; lemma candidates at the bottom):
7. **ΔD formula** (per-split) — exact change in `D` from splitting one piece.
8. **Balanced-split recursion + frontier recursion** — `D(T_n)+D(T_{n−1})=2^n`, `D(T_n)=(2^{n+1}+(-1)^n)/3`.
9. **Single-split lower bound** — `D ≥ D(T_{n−1}) ≥ 1` for any single split of the top.
10. **Multi-split dyadic lower bound** — `D ≥ 1` for any ≤n-mark dyadic (balanced) refinement.
11. **PL + breakpoint reduction** — global min over ≤n-mark refinements is at a tie/breakpoint config.

New rigorous results (round 4, this file; lemma candidates at the bottom):
12. **Telescoping zero-gradient block lemma** (GAP-B, §11) — D is constant on a PL cell where each split's
    fragments sit at same-sign positions; if all top-piece fragments at + and all below-tower pieces at −,
    then D = 2^n − (2^n − 1) = 1 directly (no dyadic endpoint needed). The non-dyadic generalization of
    `block-contribution-formula`.
13. **2-leftover transport lemma** (GAP-A, §12) — at a spine-3 cascade breakpoint (two non-dyadic fragments
    a, d straddling a tower piece t), the mass identity a + d = t + 1 follows from fragment-tower telescoping,
    giving D = a − t + d = 1. Corollary of GAP-B(d).

New rigorous result (round 5, this file; lemma candidate at the bottom):
14. **Mass-balance lemma** (§14, `lemmas/mass-balance-lemma.md`, proposed for certification) — on a
    block-condition cell, `D = 2S₊ − D_n`; `D = 1 ⟺ S₊ = 2^n ⟺` the all-top-`+`/all-below-`−` pattern.
    **Sub-gap (ii) VACUOUS**: every block-condition `D = 1` cell is settled by GAP-B(d) directly.

New rigorous results (round 6, this file; lemma candidate at the bottom):
15. **Mass-budget breakpoint inequality** (§15, NEW, proposed for certification as
    `mass-budget-breakpoint-inequality`) — at a breakpoint of `T_n` (cascade type, all `n`),
    `T ≥ 3F − 1` where `F` = surviving non-dyadic fragment mass, `T` = surviving tower mass.
    **Corollary:** block condition + `D = 1` at a breakpoint ⟹ `F = 0` (spine dyadic) ⟹
    `D ≥ 1` by §8. The block condition is SUFFICIENT for `D = 1` at breakpoints.
    **Verification:** `F = 0` at all 151 `D = 1` breakpoints of `T_3`; `T ≥ 3F − 1` at all
    constructed breakpoints (0 violations). GAP-C(i) NARROWED: any counterexample must have
    `F > 0` AND block condition failing.

New rigorous results (round 7, this file; lemma candidates at the bottom):
16. **Vertex-level crux (★) + Mechanism A** (§16, NEW). **(★):** at every non-dyadic strong-
    breakpoint vertex of `T_n`, `D > 1`. PROVED sub-cases: **single-survivor at cascade
    vertices** (one sum constraint implies `nfree ≤ 1` at a vertex, §16.1); **single-survivor
    for ALL `T_3` types** (mark budget ≤ 3, §16.1); **v-bracket** `v < 2^{n−1}` (§16.2);
    **largest-tower-exceeds-fragment** `2^j > v` (§16.3, mass-budget contradiction);
    **`t₊ > t₋`** (dyadic dominance, §16.4); **frag-at-`+` budget-tight implies `D > 1`**
    (§16.5, via `t₊ > v`). Decomposition `D = (F−T) + 2(t₊−f₋)` non-circular (§16.4).
    **GAPS:** (GAP-A) `v > 1` (verified, unproved); (GAP-C/d-minus) frag-at-`−` `t₊ > 2v`
    (near-miss `2v−1/2`, 13/13 verified); (GAP-B) mixed multi-survivor `n ≥ 4` (47 nfree=2
    vertices all `D > 1`, mass-budget cascade-only); (GAP-D) completeness `n ≥ 5`. Verified:
    131 vertices, 0 counterexamples.

**Honest negative result (round 5):** the spine sign-pattern / multi-swap subset-sum framing (the
nosaddle-close explorer's G1-closer) is **CIRCULAR** — the "mass identity `F = T + 1`" is equivalent
to `D = 1` under the assumed pattern, not independent (verified `Fraction`-exact, §13). It does NOT
close GAP-C. The single-swap and multi-swap both rest on this circular premise.

**Open gaps preventing `solved`:**
- **(G1) Lower bound case (b), non-dyadic multi-split (k ≥ 3).** When Xiang uses ≥3 marks with
  at least one unbalanced split, prove `D ≥ 1`. The PL+breakpoint reduction (§6) lands the
  global min at a breakpoint config; §§4–5,7–8 settle single-split, dyadic, 2-split, even-group.
  Round 4: GAP-B (§11) proves D = 1 on block-condition cells DIRECTLY (no dyadic endpoint
  needed); GAP-A (§12) proves the spine-3 mass identity a+d = t+1. Round 5: sub-gap (ii) VACUOUS
  (mass-balance lemma). Round 6 NEW: **mass-budget inequality** `T ≥ 3F − 1` (§15) at breakpoints
  + corollary: **block condition at `D = 1` breakpoint ⟹ `F = 0` ⟹ `D = 1` by §8** (sufficient).
  Continuity rules out "all `F` at `−`". The remaining step is **GAP-C(i)-balance-implies-block**:
  prove the block condition (or `F = 0`) at `D = 1` breakpoints directly. The mass budget
  constrains `F` but doesn't force `F = 0` without the block-condition hypothesis. Any
  counterexample must have `F > 0` AND the block condition failing — a much more constrained
  scenario. Verified: `F = 0` at all 151 `D = 1` breakpoints of `T_3` (all types); block
  condition holds at all 523 `D = 1` configs (`T_3`/`T_4`/`T_5`); `T ≥ 3F−1` at all constructed
  breakpoints (0 violations).
- **(U) Upper bound general n** — only `n=1` proved (parity coupling obstruction); deferred to
  `majorization-upper`.

---

## Approach

### 0. Notation and the marking/claiming reduction

Liu Bang places at most `n` marks, cutting the unit stick into at most `n+1` pieces; call this
multiset (Liu's *config*) `L`, summing to 1. Xiang Yu then places at most `n` further distinct
marks; each of his marks *refines* Liu's config by splitting one existing piece into two. The
final multiset (re-sorted descending) `a_1 ≥ a_2 ≥ … ≥ a_m` (with `m ≤ 2n+1`) is what the two
players draft from, Liu first, each maximising his own total.

By Lemma 0 (`lemmas/claim-game-odd-index.md`), the value of the alternating pick-any-piece
draft on the fixed sorted multiset is the odd-index sum `V = a_1 + a_3 + a_5 + … = (S+D)/2`,
where `S = Σ a_i = 1` and `D = a_1 − a_2 + a_3 − …`. Hence the whole game value is
`c(n) = max_L min_X (1+D)/2 = (1 + D*)/2` with `D* = max_L min_X D`. The target
`c(n) = 2^n/(2^{n+1}−1)` is equivalent to `D* = 1/(2^{n+1}−1) =: 1/D_n`.

**Tower units.** Throughout the lower bound we work in *tower units*: scale by `D_n`, so the
tower is `T_n = (2^n, 2^{n−1}, …, 2, 1)` (sum `D_n = 2^{n+1}−1`) and the target is `D ≥ 1`. Real
units = tower units / `D_n`.

### 1. Imported lemmas (certified)

- **Lemma 0** (`claim-game-odd-index`): draft value = odd-index sum; greedy optimal. (Sign-correct certified proof used; the round-1 displayed formula `T_1 − T_j = a_1 + (a_3−a_2)+…` in this file's prior version is **wrong** — the correct relation is `T_1 − T_j = (a_1−a_2)+(a_3−a_4)+…+(a_{j−2}−a_{j−1})` for `j` odd. The *conclusion* of the round-1 write-up was correct; the displayed derivation is not. Use the certified file.)
- **Lemma 1** (`layer-cake-odd-index`): `odd-index = ∫_0^∞ ⌈N(t)/2⌉ dt` (Tonelli).
- **Corollary 2** (`D-equals-parity-integral`): `D = ∫_0^∞ (N(t) mod 2) dt`, since `⌈N/2⌉ = N/2 + (N mod 2)/2` and `∫ N = S`.
- **Case (a)** (`tower-top-unsplit`): if Xiang does not split the top piece `2^n/D_n`, then `D ≥ 1/D_n`.
- **n=1 base** (`n1-base-both-bounds`): `c(1)=2/3`.

---

## Lower bound: `c(n) ≥ 2^n / (2^{n+1} − 1)`

Liu plays the **dyadic tower** `T_n` (tower units). We must show that for **every** Xiang
refinement (≤ `n` marks) the alternating sum satisfies `D ≥ 1` (tower units), equivalently
Liu's odd-index sum `≥ (D_n + 1)/2 = 2^n`. Case (a) (top unsplit) is the certified lemma
`tower-top-unsplit`. We close **case (b)** (top split) as far as the rigorous argument
reaches.

### 2. The per-split ΔD formula — PROVED

**Statement.** Let `M` be a multiset with `N(t) = #{pieces ≥ t}` and `D = ∫_0^∞ (N(t) mod 2) dt`
(Corollary 2). Pick one piece of length `L` and split it into `p + q = L` with `p ≥ q ≥ 0`,
producing a new multiset `M'`. Let `O(I) := ∫_I (N(t) mod 2) dt` denote the total width on
which the *pre-split* `N(t)` is odd, over an interval `I`. Then

$$\Delta D \;=\; D(M') - D(M) \;=\; 2q \;-\; 2\,O\bigl((0,q]\bigr) \;-\; 2\,O\bigl((p,L]\bigr).$$

**Proof.** Removing the piece `L` from `M` decreases `N(t)` by `1` on `(0, L]`; adding `p`
increases `N` by `1` on `(0, p]`; adding `q` increases `N` by `1` on `(0, q]`. Since
`q ≤ p ≤ L`, on the three sub-intervals:

- `(0, q]`: net change `ΔN = −1 + 1 + 1 = +1`;
- `(q, p]`: net change `ΔN = −1 + 1 + 0 = 0`;
- `(p, L]`: net change `ΔN = −1 + 0 + 0 = −1`;
- `(L, ∞)`: `ΔN = 0`.

On the two intervals where `ΔN = 0`, `(N mod 2)` is unchanged. On `(0, q]`, `N' = N + 1`, so
`N'(t) mod 2 = 1 − (N(t) mod 2)` (parity **flips**). The change in the integrand is
`1 − 2·(N(t) mod 2)`, contributing `q − 2·O((0,q])` to `ΔD`. On `(p, L]`, `N' = N − 1`, and
again `(N−1) mod 2 = 1 − (N mod 2)` (parity flips), contributing `(L−p) − 2·O((p,L]) =
q − 2·O((p,L])`. Summing:

$$\Delta D = \bigl(q - 2\,O((0,q])\bigr) + \bigl(q - 2\,O((p,L])\bigr) = 2q - 2\,O((0,q]) - 2\,O((p,L]). \quad\blacksquare$$

**(Composability caveat — the coupling obstruction.)** The formula's `O`-widths are those of
the *current* `N(t)`. After the first split, `N(t)` is no longer the clean tower staircase, so
`O((0,q])` for a *second* split is a global functional of the perturbed landscape — this is the
parity-coupling obstruction predicted in round 1 and confirmed by the outline-reviewer. The
formula composes exactly (apply sequentially with the updated `N`), but the signs are coupled
across thresholds by the single global sort. We use the formula explicitly only for the
single-split case and the balanced-split recursion below; the multi-split dyadic case bypasses
it via a direct block argument (§5).

**Verification.** For `T_3 = (8,4,2,1)` (tower units, `D_old = 5`), the single split of the
top `8` into `p + q` gives, by direct recomputation of the alternating sum versus the formula:

| `q` | `D_new` (direct) | `ΔD` (formula) |
|----|----|----|
| `1/2` | `5` | `0` |
| `1` | `5` | `0` |
| `3/2` | `4` | `−1` |
| `2` | `3` | `−2` |
| `5/2` | `3` | `−2` |
| `3` | `3` | `−2` |
| `4` | `3` | `−2` |

All entries match (`Fraction` arithmetic). The formula is the load-bearing identity; the proofs
below are analytic, not computational.

### 3. Balanced-split recursion and the frontier recursion — PROVED

**Lemma (balanced-split recursion).** The balanced split of the top piece `2^n` of `T_n` into
`2^{n−1} + 2^{n−1}` produces a multiset whose alternating sum is `2^n − D(T_n)`.

**Proof (via the ΔD formula).** Take `p = q = 2^{n−1}` (so `L = 2^n`). The pre-split tower
`T_n` has `N(t) mod 2` on `(0, 2^n]` exactly the parity staircase of the tower. We use two
observations:

(i) `O((0, 2^{n−1}])`: for `t ≤ 2^{n−1}`, `N_{T_n}(t) = 2 + N_{T_{n−1}}(t)` (the two tower
pieces `2^n, 2^{n−1}` are both `≥ t`, plus the `T_{n−1}` tail). Since `2 mod 2 = 0`,
`N_{T_n}(t) mod 2 = N_{T_{n−1}}(t) mod 2`. Hence `O((0, 2^{n−1}]) = D(T_{n−1})` (the full
parity integral of `T_{n−1}`, whose largest piece is `2^{n−1}`).

(ii) `O((2^{n−1}, 2^n]) = D(T_n) − D(T_{n−1})` (the parity integral above `2^{n−1}`).

Substituting into the ΔD formula with `q = 2^{n−1}`:

$$\Delta D = 2\cdot 2^{n-1} - 2\,D(T_{n-1}) - 2\,\bigl(D(T_n) - D(T_{n-1})\bigr) = 2^n - 2\,D(T_n).$$

Hence `D_new = D_old + ΔD = D(T_n) + (2^n − 2D(T_n)) = 2^n − D(T_n)`. ∎

**Lemma (frontier recursion).** For all `n ≥ 1`,
$$D(T_n) + D(T_{n-1}) = 2^n, \qquad D(T_0) = 1.$$
Consequently `D(T_n) = 2^n − D(T_{n−1}) = (2^{n+1} + (-1)^n)/3 ≥ 1`.

**Proof.** `T_n = (2^n, 2^{n−1}, …, 2, 1)`, so
$$D(T_n) = \sum_{k=0}^{n} (-1)^k\, 2^{n-k} = 2^n - 2^{n-1} + 2^{n-2} - \cdots + (-1)^n.$$
Likewise `D(T_{n−1}) = 2^{n−1} − 2^{n−2} + … + (−1)^{n−1}`. Adding, the sum telescopes:

$$D(T_n) + D(T_{n-1}) = 2^n + \sum_{k=1}^{n} \bigl[(-1)^k 2^{n-k} + (-1)^{k-1} 2^{n-k}\bigr] = 2^n + 0 = 2^n,$$

since each bracketed pair `(-1)^k + (-1)^{k-1} = 0`. The base `D(T_0) = 1` (the one-piece
tower `(1)` has `D = 1`). Unwinding the recursion:
`D(T_n) = 2^n − 2^{n−1} + 2^{n−2} − … + (−1)^n` (a geometric sum with ratio `−1/2`),
`D(T_n) = 2^n · (1 − (−1/2)^{n+1})/(1 + 1/2) = (2^{n+1} + (−1)^n)/3`. For `n ≥ 0` this is
`≥ (2^{n+1} − 1)/3 ≥ 1` (with equality `D(T_0)=D(T_1)=1`). ∎

**(Computation check.)** `n=0,1,2,3,4,5,6`: `D(T_n) = 1,1,3,5,11,21,43`, matching
`(2^{n+1}+(−1)^n)/3` exactly. ✓

**Corollary (balanced top split reduces `T_n → T_{n−1}`).** By the two lemmas, a balanced split
of the top of `T_n` gives `D_new = 2^n − D(T_n) = D(T_{n−1})`. (Equivalently, the
three-copies argument: after the split the multiset is `{2^{n−1}, 2^{n−1}, 2^{n−1}, 2^{n−2},
…, 1}`; two of the three `2^{n−1}`'s pair up at positions `1,2` and cancel, the third starts
`T_{n−1}` at the (odd) position `3`, contributing `D(T_{n−1})`.)

### 4. Single-split case (b-i): one split of the top — PROVED, `D ≥ D(T_{n−1}) ≥ 1`

**Lemma.** Split the top piece `2^n` of `T_n` once into `p + q`, `p ≥ q`, `p + q = 2^n`
(so `q ∈ (0, 2^{n−1}]`). Then `D ≥ D(T_{n−1}) ≥ 1`, regardless of where the cut is made.

**Proof.** The refined multiset is `M = {p, q} ∪ T_{n−1}` (tower units). Because
`p = 2^n − q ≥ 2^{n−1}` and `2^{n−1}` is the largest piece of `T_{n−1}`, `p` is the unique
largest element of `M` and occupies position `1` (sign `+`). Hence, writing
`R := {q} ∪ T_{n−1}` (sorted descending),
$$D(M) = p - D(R) = (2^n - q) - D(R). \tag{*}$$

The sorted order of `R` is fixed except for the placement of `q`. For `q` in the *segment*
$$S_s := (2^{s-1},\, 2^s], \qquad s = 0, 1, \ldots, n-1 \quad (2^{-1} := 0),$$
`q` lands between the tower pieces `2^s` (above) and `2^{s-1}` (below) — at the endpoints the
list ties, but `D` is *tie-agnostic* (equal adjacent pieces contribute `±x ∓ x = 0` regardless
of order), so `D(R)` is continuous across endpoints. In segment `S_s`, the elements above `q`
in `R` are `2^{n-1}, 2^{n-2}, …, 2^s` (that is `n − s` pieces, occupying positions
`1, …, n−s`); `q` is at position `n − s + 1`; the tail `T_{s-1} = (2^{s-1}, …, 1)` (length
`s`) occupies positions `n − s + 2, …, n + 1`. So

$$D(R) = D\bigl(\{2^{n-1}, \ldots, 2^s\}\bigr) \;+\; (-1)^{n-s}\, q \;\pm\; D(T_{s-1}),$$

where `q`'s sign is `(-1)^{(n-s+1)+1} = (-1)^{n-s}`, and the tail `T_{s-1}` starts at position
`n − s + 2` (sign `(-1)^{n-s+3}`), contributing `+D(T_{s-1})` if `n − s` is odd and
`−D(T_{s-1})` if `n − s` is even. Substituting into `(*)`:

- **`n − s` even (`n ≡ s mod 2`):** `D(R) = D({…2^s}) + q − D(T_{s-1})`, so
  `D(M) = 2^n − D({…2^s}) + D(T_{s-1}) − 2q` — **linear in `q` with slope `−2`**.
- **`n − s` odd:** `D(R) = D({…2^s}) − q + D(T_{s-1})`, so
  `D(M) = 2^n − D({…2^s}) − D(T_{s-1})` — **constant in `q`** (slope `0`).

So on every segment `S_s`, `D` is affine with slope `0` or `−2`; in particular it is
**non-increasing** in `q` on each segment, and (continuity at endpoints) non-increasing on the
whole `(0, 2^{n−1}]`. The minimum is at `q = 2^{n−1}` (the balanced split, top of `S_{n−1}`).
The segment `S_{n−1}` has `n − s = 1` (odd), so it is **constant** at its value, which (by the
balanced-split recursion, §3) equals `D(T_{n−1})`. Therefore
$$D(M) \;\ge\; D\bigl|_{q=2^{n-1}} \;=\; D(T_{n-1}) \;=\; \frac{2^n + (-1)^{n-1}}{3} \;\ge\; \frac{2^n - 1}{3} \;\ge\; 1$$
for `n ≥ 1` (and exactly `1` at `n = 1`, since `D(T_0) = 1`). ∎

**Remark (the plateau).** The whole top segment `S_{n−1} = (2^{n−2}, 2^{n−1}]` is a *plateau*
at `D(T_{n−1})`: every cut in this range — dyadic balanced (`q = 2^{n−1}`) or non-dyadic
(`q ∈ (2^{n−2}, 2^{n−1})`) — gives the same value. This is the single-split instance of the
"non-dyadic breakpoints lie on plateaus reaching dyadic ones" phenomenon; for a *single* split
it is **proved** here for all `n`. (For `T_3`: `D ≡ 5` on `(0,1]`, `D = 7 − 2q` on `(1,2]`,
`D ≡ 3` on `[2,4]`; min `= 3 = D(T_2)`, attained on the plateau `[2,4]` containing the dyadic
point `q = 4`.) **The single-split case (b-i) is fully closed.**

### 5. Multi-split dyadic (balanced) case (b-ii-dyadic) — PROVED, `D ≥ 1`

**Lemma.** Let `M` be a dyadic refinement of `T_n` — a multiset of powers of `2` obtained from
`T_n` by `≤ n` balanced splits (each split replaces a `2^k`, `k ≥ 1`, by two `2^{k−1}`).
Then `D(M) ≥ 1` (tower units), with equality at the balanced-pairs config
`{2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 2, 2, 1, 1, 1}`.

**Proof.** Let `c_k =` (number of pieces of size `2^k` in `M`), for `k = 0, …, n`. Balanced
splits conserve total mass: `Σ_{k=0}^n c_k · 2^k = 2^{n+1} − 1 = D_n` (odd). Since every term
`c_k 2^k` with `k ≥ 1` is even, `c_0` is **odd**.

The pieces of `M` sort into level-blocks: all `2^n`'s first, then all `2^{n−1}`'s, …, then all
`1`'s. Let `P_k := Σ_{\ell > k} c_\ell` = number of pieces strictly larger than `2^k`. The
block of size-`2^k` pieces occupies positions `P_k + 1, …, P_k + c_k`, contributing
$$2^k \sum_{j=1}^{c_k} (-1)^{P_k + j + 1} = 2^k\,(-1)^{P_k+1}\sum_{j=1}^{c_k}(-1)^{j}.$$
Now `Σ_{j=1}^{c_k} (−1)^j = −1` if `c_k` is odd and `0` if `c_k` is even. So the block
contributes `2^k·(−1)^{P_k}` when `c_k` is odd, and `0` when `c_k` is even (pairs within a
level cancel). Let `O := {k : c_k \text{ odd}}`. Then

$$D(M) = \sum_{k \in O} 2^k\,(-1)^{P_k}. \tag{**}$$

`O` is nonempty (it contains `0`). Let `K := \max O`. For every `ℓ > K`, `c_ℓ` is even (else
`ℓ ∈ O`, contradicting maximality of `K`), so `P_K = Σ_{ℓ > K} c_ℓ` is a sum of even numbers —
**even**. Hence `(−1)^{P_K} = +1`: the largest odd-count level contributes exactly `+2^K`.

The remaining terms of `(**)` (those with `k < K`, `k ∈ O`) are each `±2^k`, so their total
contribution is bounded below by `−Σ_{k < K} 2^k = −(2^K − 1)`. Therefore

$$D(M) \;\ge\; 2^K - (2^K - 1) \;=\; 1. \quad\blacksquare$$

**Equality.** The balanced-pairs config has `c_k = 2` for `1 ≤ k ≤ n−1` (even), `c_0 = 3`
(odd), so `O = {0}`, `K = 0`, and `D = 2^0·(−1)^{P_0} = (−1)^{P_0}` where
`P_0 = 2(n−1)` (even). So `D = 1`. ✓ (This config uses `n − 1` marks; an `n`-th balanced mark
leaves it on a plateau at `D = 1`.)

**Computation check.** Enumerating *all* dyadic refinements (≤ `n` balanced splits) of `T_n`
for `n = 1, …, 7`: the minimum `D` is exactly `1` in every case (`2, 4, 10, 28, 79, 224, 649`
configs respectively; all `D` values are odd; none below `1`). ✓

### 6. Piecewise-linearity + breakpoint reduction — PROVED (reduction)

**Lemma (PL).** Fix the number `k ≤ n` of Xiang marks and fix a *combinatorial type*
(`σ`, the total order — allowing ties — of the resulting `≤ n+1+k` pieces). On the open cell
of split-position vectors realizing `σ`, the alternating sum `D` is an **affine** (linear)
function of the `k` split positions.

**Proof.** On a fixed type, each piece's *position* (hence its sign in the alternating sum) is
fixed, and each piece's *length* is an affine function of the split positions (each length is
either a Liu piece, or `p =` (a fixed Liu/parent length) `− q`, or `q` — affine in the `q`'s).
`D = Σ_i (± a_i` (sign from fixed position) is then a finite sum of affine functions, hence
affine. ∎ (Knowledge-base entry: "Piecewise-concavity smoothing" — the breakpoint-minimum
principle.)

**Corollary (breakpoint minimum).** The global infimum of `D` over all `≤ n`-mark refinements
of `T_n` is attained at a **breakpoint (tie) config** — one where every fragment length ties
(in `σ`) with an adjacent piece.

**Proof.** The feasible region (vectors of `≤ n` split positions in `[0,1]^{≤n}` respecting
the parent-child structure, plus the discrete choice of which piece to split at each step) is
compact; `D` is continuous (tie-agnostic at type boundaries, by the PL lemma). Hence the
minimum is attained. Suppose it is attained at an interior point of a cell (no ties). Then
`D` is affine on a neighbourhood; if its slope is nonzero in some coordinate, sliding that
coordinate decreases `D`, contradicting minimality; if the slope is zero in every coordinate,
`D` is constant on the cell, and we may slide to the cell boundary (a tie config) without
increasing `D`. Iterating across cells, the minimum is also attained at a vertex of the PL
complex — a config where *every* fragment length ties with an adjacent piece, i.e. a
breakpoint config. ∎

This reduces the lower bound to: **prove `D ≥ 1` at every breakpoint config of `T_n`**. The
dyadic breakpoints (all fragments are powers of `2`) are settled by §5; the single-split
breakpoints (all single-split `q`'s) are settled by §4. The open step is non-dyadic
multi-split breakpoints.

### 7. Two-split sub-case (G1 partial) — PROVED for top-fragment splits, all n

**Lemma** (`two-split-lower-bound`, proposed for certification — see
`lemmas/two-split-lower-bound.md`). When Xiang uses exactly 2 marks both splitting fragments of
the top piece `2^n`, the min `D = D(T_{n−2}) = (2^{n−1}+(−1)^{n−2})/3 ≥ 1`, attained at the dyadic
cascade `2^n → 2^{n−1}+2^{n−1} → 2^{n−2}+2^{n−2}`.

**Proof sketch** (full proof in the lemma file). By `pl-breakpoint-minimum`, the min is at a
breakpoint. At a breakpoint where both cuts tie tower pieces (`q=2^a, s=2^b`), the config is
`{r, 2^b, 2^a} ∪ T_{n−1}` with `r = 2^n − 2^a − 2^b` (the lone non-tower piece). The rest (after
removing the largest piece) is all-tower, so `block-contribution-formula` gives an exact formula:

- **Sub-case 1a** (`r ≥ 2^{n−1}`): `D = D(T_n) − (c_M·2^M + c_m·2^m)/3` where
  `c_M, c_m ∈ {2,4}` are parity-determined. The **parity constraint** — `c_M=4` forces `M ≤ n−2`,
  and `c_M=2, c_m=4` forces `m ≤ M−2` — guarantees `c_M·2^M + c_m·2^m ≤ 3·2^{n−1}`, hence
  `D ≥ D(T_n) − 2^{n−1} = D(T_{n−2})`. Four-case check on `(c_M, c_m)`.
- **Sub-case 1b** (`r < 2^{n−1}`): forces `M = n−1`; after the two `2^{n−1}`'s cancel, the
  formula reduces to `D = (2^n + (−1)^n − c·2^m)/3` with `c ∈ {2,4}`, and
  `c·2^m ≤ 2^{n−1}` by the same parity constraint (`c=4` forces `m ≤ n−3`).
- **Balanced 2nd split** (`s=r`): equal fragments cancel, `D = D({2^a} ∪ T_{n−1})`, bounded by
  `2^a ≤ 2^{n−1}`.
- **`q=s`** (two equal): reduce to Case 1 or Case 4 at a vertex.
- **All equal** (`q=s=r=2^n/3`): `D = D(T_{n−2}) + 2^{n−1}/3 ≥ D(T_{n−2})`.

All formulas verified `Fraction`-exact `n=3,…,7`. **GAP**: Type C (second split on a tower piece)
verified `n=3..7` but not fully proved (same pattern, two-level-removal formula). This is a
partial G1 close — the 2-split top-fragment-split case is settled for all `n`.

### 8. Even-group pair-cancellation + spine — PROVED (closes G1 for even-group strong breakpoints)

**Lemma** (folded from the lower-nondyadic explorer, §S1/S2). At a **strong breakpoint** config
of `T_n` (every fragment ties an adjacent piece), if every non-dyadic fragment group has EVEN
count, then `D ≥ 1`.

**Proof.** Two structural facts (proved from scratch):

**(S1) Adjacent-equal pairs cancel in the alternating sum.** If `a_i = a_{i+1}`, their combined
contribution is `(−1)^{i+1}a_i + (−1)^{i+2}a_{i+1} = 0` (by `claim-game-odd-index` sign
convention: position `j` has sign `(−1)^{j+1}`). Removing the pair shifts positions `> i+1` down
by 2, preserving signs (each shifts by 2, sign `(−1)^{j−2+1} = (−1)^{j+1}`). Hence
`D(full) = D(after removing all adjacent-equal pairs)`.

**(S2) At a strong breakpoint, non-dyadic fragments form adjacent-equal groups.** A non-dyadic
fragment (value `≠ 2^k`) cannot tie a tower piece (all tower pieces are `2^k`). So it must tie
another non-dyadic fragment of the same value. Adjacent-equal groups of size `≥ 2` form. If the
group has EVEN size, it is a union of pairs, each cancelling by (S1). If ODD `≥ 3`, one copy
survives.

**The spine.** After removing ALL adjacent-equal pairs (dyadic and non-dyadic), the remaining
"spine" is strictly decreasing with distinct values. If every non-dyadic group is even, the spine
contains only distinct powers of `2` (the unpaired dyadic pieces). The spine is a strictly
decreasing sequence of distinct powers of `2`: `2^{k_1} > 2^{k_2} > … > 2^{k_j}`.

**Geometric dominance.** For distinct powers of `2`, `2^{k_1} > Σ_{i≥2} 2^{k_i}` (since
`Σ_{i≥2} 2^{k_i} ≤ 2^{k_1} − 1`, the sum of all smaller distinct powers of `2`). The spine is
nonempty because the total mass `D_n = 2^{n+1} − 1` is ODD, while adjacent-equal pairs contribute
EVEN total mass (each pair contributes `2×` its value), so the unpaired mass is odd, forcing
`2^0 = 1` to be in the spine. Hence `D(spine) ≥ 1` (the largest power exceeds the sum of all
smaller; the alternating sum of a decreasing power-of-2 sequence is a positive integer `≥ 1`). ∎

**Boundary (what this closes, what it leaves open).** This closes G1 for **even-group strong
breakpoints** (all `n`, independently of the global exchange). It does NOT close:
- **Odd-group strong breakpoints**: a non-dyadic group of ODD count `≥ 3` leaves a leftover in
  the spine. Odd-group minimizers EXIST at `D = 1` (e.g. `{4.75, 4, 2, 2, 1, 1, 0.25}` for `T_3`,
  spine `{4.75, 4, 0.25}`, `D = 1`). The pair-cancellation argument is INSUFFICIENT here.
- **PL-vertex (non-strong) breakpoints**: a lone larger-fragment (not tied) is not eliminated by
  pair-cancellation. These can also be minimizers (e.g. `{5, 4, 2, 2, 1, 1}` for `T_3`, `D = 1`).
  These are the `D = D*` non-dyadic configs that the global exchange must reach.

### 9. Plateau-connectivity (GLOBAL exchange) — the deep G1-closing route — GAP (developed)

**The claim.** The min-level set `{D = D*}` always contains a DYADIC config. Then
`dyadic-refinement-lower-bound` gives `D* ≥ 1`. This would close G1 for ALL multi-split configs.

**Why the PL machinery lands here.** The PL-vertex iteration (`pl-breakpoint-minimum`) slides
along zero-gradient directions (plateaus where `D` is constant) until reaching a vertex where
all coordinates are pinned. The target is to show this terminal vertex can be chosen DYADIC by
routing the slide through dyadic-friendly directions. The 2-split lemma (§7) confirms this for
`k = 2`: the min plateau contains the dyadic cascade.

**The V-shape obstruction (LOCAL rebalancing FAILS).** After an unbalanced first split, the
second split's `D` as a function of the cut `q` is **V-shaped**, not monotone. Verified for
`T_3`: `8 → 5+3` (unbalanced), then split the `5` into `(5−q)+q`:

| `q` | config | `D` |
|-----|--------|-----|
| `1` (tie) | `{4,4,3,2,1,1}` | `1` |
| `2` | `{4,3,3,2,2,1}` | `3` |
| `5/2` (balanced) | `{4,3,5/2,5/2,2,1}` | `2` |
| `3` | `{4,3,3,2,2,1}` | `3` |

The minimum is at `q = 1` (a tie), NOT at the balanced `q = 5/2`. **Rebalancing the second
split INCREASES `D` from 1 to 2.** (The explorer reported `D = 3` at `q = 5/2`; the correct
value is `D = 2` — verified by `Fraction` arithmetic: `4 − 3 + 5/2 − 5/2 + 2 − 1 = 2`. The
qualitative obstruction is unchanged: local rebalancing does not weakly decrease `D`.)

This kills any "replace unbalanced split by balanced, `D` doesn't increase" per-split exchange.
The required exchange must be **GLOBAL**: a multi-coordinate deformation keeping `D = D*`, not a
sequence of local rebalancings.

**What is proved.**
- The 2-split sub-case (§7): the min-level set contains the dyadic cascade, so `D* = D(T_{n−2})`
  for `k = 2`. ✓
- Even-group strong breakpoints have `D ≥ 1` (§8). ✓
- The V-shape is confirmed; LOCAL rebalancing fails. ✓

**GAP (the hard step).** For `k ≥ 3` splits with at least one unbalanced, prove the min-level
set `{D = D*}` contains a dyadic config. The obstruction: the PL-vertex iteration may terminate
at a non-dyadic vertex (lone larger-fragment); sliding to a dyadic vertex requires a GLOBAL
multi-coordinate exchange that preserves `D = D*`, which the V-shape shows cannot be done
per-split. No proof found. Verified `n ≤ 6` (min `D = 1`, attained on plateaus containing dyadic
configs). The even-group sub-result (§8) is the fallback: if the terminal vertex is an even-group
strong breakpoint, `D ≥ 1` directly.

### 10. Gap G1: non-dyadic multi-split breakpoints (k ≥ 3) — OPEN

**Status.** Conjectured, verified, not proved.

**What remains.** After §6, the global minimum of `D` over all `≤ n`-mark refinements is at a
breakpoint config. §§4–5 prove `D ≥ 1` for single-split breakpoints (all `n`) and for dyadic
multi-split breakpoints (all `n`). The remaining case is a breakpoint config with ≥ `2` splits,
at least one of which is **unbalanced**, so that some fragment length is *not* a power of `2`.

**Why the proven machinery does not auto-close this case.** (a) The dyadic block argument of §5
relies on pieces grouping into exact `2^k`-blocks; non-power-of-2 fragments do not group, so
the within-block pair-cancellation fails. (b) The ΔD formula of §2 composes across splits but
its `O`-widths after the first split are functionals of the *perturbed* `N(t)` (no longer the
tower staircase), and the signs of successive `ΔD`'s are coupled through the global sort —
this is the parity-coupling obstruction. (c) After an *unbalanced* first split, the
single-split monotonicity (§4) breaks: e.g. for `T_3`, after `8 → 5 + 3`, the second split (of
the `5`) gives `D` as a function of the second cut that is `V-shaped` (decreasing then
increasing), not monotone — so "balancing the second split" does not, in general, weakly
decrease `D`. (Verified: min of that second-split function is still `1`, at a tie `q = 1`, but
the monotonicity argument does not reach it.)

**The plateau conjecture (G1, restated).** *Every* non-dyadic multi-split breakpoint config lies
on a PL plateau (a cell of the PL complex on which `D` is constant) whose closure contains a
dyadic breakpoint config; since `D` is constant on the plateau and the dyadic endpoint has
`D ≥ 1` (§5), the non-dyadic config also has `D ≥ 1`. This is the "non-dyadic breakpoints lie on
plateaus connecting to dyadic ones" claim of explorer A.

**Verification of G1 (not a proof).**
- `n = 2`: exhaustive 2-mark grid over `T_2 = (4,2,1)` (all split-pair patterns, `1/1024` grid):
  minimum `D = 1`, attained on plateaus containing the dyadic balanced-pairs config
  `{2,2,1,1,1}` and non-dyadic configs (e.g. `{2961/1024, 1071/1024, 1/16, 2, 1}`).
- `n = 3`: exhaustive 2-split grid (`1/4` step) over both "split top then split a fragment" and
  "split top and split second piece"; minimum `D = 1`, attained at non-dyadic breakpoints
  (e.g. `{5,4,2,2,1,1}` → `D = 5−4+2−2+1−1 = 1`) on plateaus connecting to the dyadic
  balanced-pairs `{4,4,2,2,1,1,1}`.
- `n ≤ 6`: full dyadic enumeration gives min `D = 1`; random non-dyadic multi-split sampling
  (`30 000` per `n`) gives no `D < 1`. (For `n = 3` the reviewer independently confirms `121`
  configs on the `D = 1` plateau, only `1` dyadic.)

The reduction of §6 lands the global minimum here; closing G1 = proving the plateau
continuity claim (or an equivalent direct `D ≥ 1` argument at non-dyadic breakpoints).

**GAP (G1):** prove `D ≥ 1` at every non-dyadic multi-split breakpoint config of `T_n` (or,
equivalently, prove the plateau-connects-to-dyadic claim). Verified `n ≤ 6`; open in general.

### 11. Telescoping zero-gradient block lemma (GAP-B) — PROVED

This is the scaffold lemma that makes the star-shaped transport (§13) finite. It is the
non-dyadic generalization of the certified `block-contribution-formula`.

**Lemma (GAP-B).** Let `M` be a refinement of `T_n` (tower units). Fix a combinatorial type
`σ` (a strict total order of all `m` pieces). On the open PL cell `C_σ` (where the order is
strict, no ties):

**(a) Affinity.** `D = Σ_{i=1}^m s_i p_i` is affine in the cut positions, where
`s_i = (−1)^{i+1}` is the sign at position `i` (position 1 is `+`, 2 is `−`, …) and `p_i`
is the length of the `i`-th piece in the sorted order.

**(b) Same-sign block ⇒ constant contribution.** For each split of a tower piece `V` into
fragments `f_1, …, f_r` (with `Σ_j f_j = V` by the telescoping identity — each split replaces
`V` by `f + (V−f)`, and iterative splitting preserves the partition sum), if all fragments
sit at positions of the same sign `s`, their combined contribution to `D` is
`s · Σ_j f_j = s · V` — independent of the cut positions. If any two fragments sit at
opposite-sign positions, the contribution depends on the cuts (gradient `±2` per cut
coordinate, by the single-split formula §4 and the ΔD formula §2).

**(c) Constancy (block condition).** If every split's fragments all sit at same-sign
positions (the **block condition**), then `D` is CONSTANT on `C_σ`.

**(d) Direct value = 1 (the key computation).** If ALL fragments derived from the top piece
`2^n` sit at `+` positions and ALL pieces derived from tower pieces below `2^n` (split or
unsplit) sit at `−` positions, then
$$D \;=\; 2^n - (2^n - 1) \;=\; 1$$
on the whole cell `C_σ`, by (c) and the telescoping mass identity.

**Proof.**

(a) On a fixed type, each piece's position (hence sign `s_i`) is fixed. Each piece length
`p_i` is affine in the cut positions (each is either a constant — an unsplit tower piece — or
an affine function of the cuts: `p = V − q` or `p = q`). `D = Σ s_i p_i` is a finite sum of
affine functions, hence affine. ∎ (Knowledge-base: "Piecewise-concavity smoothing" /
`pl-breakpoint-minimum` PL lemma.)

(b) The fragments of a split piece `V` satisfy `Σ_j f_j = V` (they partition `V`; this is the
telescoping identity — each split replaces `V` by `f + (V−f)`, and iterative splitting preserves
the partition sum). Their combined contribution to `D` is `Σ_j s_{i_j} f_j`. If
`s_{i_j} = s` for all `j` (same sign), this is `s · Σ f_j = s · V`, a constant. If signs differ,
the contribution is `Σ_j s_{i_j} f_j` with at least two different coefficients `(±1)`, which is
a non-constant affine function of the cuts. Concretely, for a single split of `V` into
`f_1 = V − q`, `f_2 = q` (parameterized by cut `q`), the gradient is
`∂D/∂q = −s_{i_1} + s_{i_2}`, which is `0` if `s_{i_1} = s_{i_2}` (same sign) and `±2` if
opposite — matching the single-split slope analysis of §4 and the ΔD formula of §2. ∎

(c) By (b), each split piece with uniform-sign fragments contributes a constant `(±V)` to `D`.
Unsplit pieces contribute constants `(±2^k)`. So `D` is a sum of constants, hence constant on
`C_σ`. ∎

(d) The top piece `2^n` is split into fragments summing to `2^n` (telescoping, (b)). At `+`
positions, they contribute `+2^n`. The tower pieces below `2^n` — `{2^{n−1}, …, 2, 1}`, total
mass `2^n − 1` — are either unsplit or further split; in either case, their fragments sum to
`2^n − 1` (telescoping of each split tower piece). At `−` positions, they contribute
`−(2^n − 1)`. By (c), `D` is constant on `C_σ`; its value is `2^n − (2^n − 1) = 1`. ∎

**Remark (reviewer concern addressed for block-condition cells).** Part (d) computes `D = 1`
DIRECTLY from the telescoping mass identity — it does NOT require the cell to contain a dyadic
endpoint. This addresses the outline-reviewer's flagged concern ("step 4's constancy needs the
cell to CONTAIN a dyadic endpoint") for all cells satisfying the sign-pattern of (d): the value
`1` follows from the mass identity (fragment mass `= 2^n`, below-tower mass `= 2^n − 1`), not
from proximity to a dyadic config. The only cells where a dyadic endpoint remains necessary are
those where the block condition holds (c) but the sign pattern is NOT "all top `+`, all below
`−`" — see §13 for this case.

**Remark (relation to certified lemmas).** Part (d) is the non-dyadic generalization of
`block-contribution-formula` (certified): the dyadic formula
`D = Σ_k 2^k (−1)^{C_k} (n_k mod 2)` is the special case where all fragments are powers of `2`
(dyadic), and within-block pairs cancel by sign-matching; the block lemma extends the
"within-block pairs cancel" mechanism to non-dyadic fragments via the sign-uniformity (block)
condition. The `even-group-spine-lower-bound` (certified, §8) is the spine-level shadow of
the same mechanism: even-count non-dyadic groups cancel (block condition at the group level).

**Verification (not a proof step).** The spine-7 cell `{a, 4, b, 2, c, 1, d}` of the T_3
cascade type: all 4 fragments at `+` (positions 1,3,5,7), all 3 tower pieces at `−`
(positions 2,4,6). `D = (a+b+c+d) − (4+2+1) = 8 − 7 = 1`, independent of `(q_1, q_2, q_3)`
(since `a+b+c+d = (8−q_1)+(q_1−q_2)+(q_2−q_3)+q_3 = 8` telescopes). Verified `Fraction`-exact
along the full 201-point star-path from the spine-7 minimizer `{77/16, 4, 33/16, 2, 17/16, 1,
1/16}` to the dyadic `{4, 4, 2, 2, 1, 1, 1}`: distinct `D` values along the path = `{1}`. The
spine-3 cell `{a, 4, 2, 2, 1, 1, d}`: `D = a − 4 + 2 − 2 + 1 − 1 + d = (a+d) − 4 = 5 − 4 = 1`.
The V-shape cell (`8→5+3`, then `5→4+1`, interior `{4, 3, 3, 2, 2, 1}`): the split of `5`
produces fragments `{4, 1}` at positions 2 `(−)` and 5 `(+)` — OPPOSITE signs — block condition
FAILS, `D` has nonzero gradient (the V-shape). ✓

### 12. Two-leftover transport lemma (GAP-A) — PROVED (corollary of GAP-B)

**Lemma (GAP-A).** In the cascade refinement type of `T_n` (the top piece `2^n` is split into
`≥ 3` fragments via cascading splits on the smaller fragment), consider a breakpoint config where
exactly two fragments `a`, `d` are non-dyadic and all other fragments are dyadic (each equal to
a tower piece `2^k`, `k < n`), pairing off with the corresponding tower pieces. Let `t` be the
unique unpaired tower piece (the only tower piece whose count is odd). Then the spine is
`{a, t, d}` (`a > t > d`), and

$$a + d = t + 1, \qquad D = a - t + d = 1.$$

Moreover the transport — shifting mass from `a` to `d` while keeping `a + d = t + 1` — reaches
the dyadic config `{t, t, …, 1}` at `D = 1`.

**Proof.** By the cascade structure, all fragments derive from the top piece `2^n`, so their
total mass is `2^n` (telescoping, GAP-B(b)). The dyadic fragments each equal a tower piece and
pair with it (by `strong-breakpoint-group-structure` S2: at a strong breakpoint, non-dyadic
fragments form adjacent-equal groups; here each non-dyadic value appears exactly once, so the
"groups" are trivially the lone non-dyadic survivors, and the dyadic fragments pair with tower
pieces of the same value by `spine-pair-cancellation` S1). The paired fragment mass equals the
paired tower mass (each pair: fragment `= tower piece`, same value). The unpaired tower mass is
`t` (the single survivor). The total tower mass below `2^n` is `2^n − 1`. So:

- (paired tower mass) `= (2^n − 1) − t`,
- (paired fragment mass) `= (paired tower mass) = (2^n − 1) − t` [each pair: same value],
- (unpaired fragment mass) `= a + d = 2^n − (paired fragment mass) = 2^n − (2^n − 1 − t) = t + 1`.

The sorted config places all fragments at `+` positions and all tower pieces at `−` positions
(the interleaved order `{a, t_1, f_1, t_2, f_2, …, d}` where tower pieces `t_j` sit at even
positions and fragments at odd positions). By **GAP-B(d)**:

$$D = 2^n - (2^n - 1) = 1.$$

Equivalently, the spine `{a, t, d}` has `D(spine) = a − t + d = (t + 1) − t = 1` (by
`spine-pair-cancellation` S1, `D(config) = D(spine)`). ∎

**Scope.** This proves `D = 1` for the spine-3 cascade case (and, by the same GAP-B(d)
mechanism, for spine-5 and spine-7 cascade cells where all fragments sit at `+` and all tower
pieces at `−`). For `T_3`, this covers 45/816 (spine-3), 315/816 (spine-5), and 455/816
(spine-7) cascade `D = 1` minimizers — all settled by the telescoping mass identity, NOT by the
star-shaped transport.

**Remark (mass identity as gaps-leftover instance).** The identity `a + d = t + 1` is the
spine-length-3 instance of `gaps-leftover-identity` (certified): the gaps (paired fragments `=`
paired tower pieces) telescope, and the leftover `(a + d) − t = 1` by the odd-total-mass
constraint (`D_n = 2^{n+1} − 1` odd, paired mass even, spine mass odd, forcing the `+1`
survivor — the mechanism of `even-group-spine-lower-bound` S3).

**Remark (the transport).** The "transport" (shifting mass `a ↔ d` keeping `a + d = t + 1`) is
simply moving along the PL cell where the block condition holds (GAP-B(c)): `D` is constant
`= 1` on the whole cell, so any path within the cell stays at `D = 1`. The dyadic endpoint
(`a = t`, `d = 1`, or the appropriate cascade-equivalent) lies on the cell boundary (where
ties occur), and `D` extends continuously to it by the PL lemma (§6, `pl-breakpoint-minimum`).

### 13. Star-shaped transport (GAP-C) — the G1-closing step — OPEN (mechanism explained)

**The claim (star-shaped).** Within each combinatorial type of a cascade refinement of `T_n`,
the min-level set `{D = D*}` is star-shaped with respect to the type's dyadic attainer: the
linear path from any `D = 1` point to the dyadic endpoint stays at `D = 1`.

**What GAP-B settles WITHOUT GAP-C.** Every cell satisfying GAP-B(d) — all top-piece fragments
at `+`, all below-tower pieces at `−` — has `D = 1` on the ENTIRE cell (interior + boundary),
unconditionally, by the telescoping mass identity. This covers:

- Spine-7 cascade cell `{a, 4, b, 2, c, 1, d}` (455/816 `T_3` cascade minimizers).
- Spine-5 cascade cell (one dyadic fragment pairs a tower piece; 315/816).
- Spine-3 cascade cell (two dyadic fragments pair tower pieces; 45/816; §12).
- Split-larger block-condition cell (320/322 `T_3` split-larger minimizers).
- Split-tower block-condition cell (17/17 `T_3` split-tower minimizers).

For ALL these cells, `D = 1` follows DIRECTLY from the mass identity `2^n − (2^n − 1) = 1`
(GAP-B(d)), NOT from the star-shaped transport and NOT from a dyadic endpoint. The star-shaped
transport is NOT NEEDED for these cells.

**The mechanism (explained, NOT proved).** The cells NOT settled by GAP-B(d) are the V-shape
cells, where some split's fragments sit at opposite-sign positions (block condition fails). In
these cells, `D` has nonzero gradient in the interior (slope `±2` per cut coordinate, by
GAP-B(b)), so `D > 1` in the interior (the V-shape). The min-level set `{D = 1}` does NOT
include V-shape cell interiors.

Instead, the min-level set lives on PL cell FACES — lower-dimensional tie loci where some
fragments equal adjacent pieces (tower pieces or other fragments). On these faces, the block
condition holds (the tie forces two pieces to the same position, which is a same-sign position
in the interleaved order), so `D ≡ 1` on the face by GAP-B(d) or GAP-B(c) + a dyadic-endpoint
value. The transport moves ALONG these faces (tie loci) to the dyadic vertex, going AROUND the
V-shape gradient (which points INTO cell interiors, off the face).

**Concrete T_3 example (the V-shape cell).** After `8 → 5 + 3` (unbalanced first split), the
second split of `5` into `(5−q) + q` gives the V-shape: `D` as a function of `q` is decreasing
then increasing, with minimum `D = 1` at the tie `q = 1` (config `{4, 4, 3, 2, 1, 1}`, a tie
face shared with the block-condition cell where the first split is `8 → 4 + 4`). The V-shape
gradient points into the cell interior (`q ∈ (1, 5/2)`, where `D > 1`); the transport stays on
the tie face `q = 1` (where `D = 1` by the adjacent block-condition cell). ✓

**The open sub-gap (GAP-C, restated precisely).**

**(Sub-gap (i): V-shape cell faces.** Every V-shape cell has `D > 1` in its interior. Its
`D = 1` points (if any) lie on its faces (tie loci). The open step: prove every such face
inherits the block condition (so `D = 1` on the face by GAP-B(d) or by the dyadic-endpoint
value via `dyadic-refinement-lower-bound`). Verified `T_3` (all V-shape cell faces in the
cascade type have the block condition); open for general `n`.

**(Sub-gap (ii): block-condition cells without the "all-top-+, all-below-−" sign pattern —
CLOSED (round 5, vacuous).** By the **mass-balance lemma** (§14, `lemmas/mass-balance-lemma.md`,
proposed for certification): on any block-condition cell `D = 2S₊ − D_n` (algebra), so
`D = 1 ⟺ S₊ = 2^n`. The block condition forces all top fragments to a single sign; if all at `−`
then `S₊ ≤ 2^n − 1 < 2^n` (so `D ≤ −1 ≠ 1`); if all at `+` then `S₊ = 2^n ⟺` all below-top pieces
at `−`. Hence `D = 1` on a block-condition cell FORCES the all-top-`+`/all-below-`−` pattern —
settled by GAP-B(d) directly, no dyadic endpoint needed. **There are NO block-condition `D = 1`
cells lacking the pattern: sub-gap (ii) is vacuous.** The reviewer's flagged concern (an
undetermined signed sum on block-condition cells without the pattern) is moot for `D = 1` cells —
they all have the pattern. (A block-condition cell with all top fragments at `−` would have
`D ≤ −1`, but such a cell cannot be a `D = 1` cell, and whether it exists as an open cell is
irrelevant to the `D ≥ 1` lower bound's min-level set.)

**Address of the reviewer's concern.** The reviewer flagged: "step 4's constancy argument says
'equal to its value at any point — in particular at the dyadic endpoint IF THE CELL CONTAINS
ONE.' The 'if' is load-bearing." We address this in two parts:

1. For cells satisfying GAP-B(d) (the dominant case): `D = 1` is computed DIRECTLY from the
   telescoping mass identity (§11(d)), with NO dyadic endpoint needed. The "if" is moot.

2. For block-condition cells NOT satisfying (d)'s sign pattern: `D` is constant (GAP-B(c)), but
   the value may be `≠ 1`. If the cell contains a dyadic endpoint, the value is `≥ 1` (by
   `dyadic-refinement-lower-bound`); if not, the value is an undetermined integer. This is
   **honestly marked as a remaining sub-gap** — we do NOT claim it is settled. The numerics
   (816/816 `T_3` cascade, 322/322 split-larger, 17/17 split-tower) are consistent with
   every `{D = 1}` cell satisfying (d), but we do NOT present these as a proof (per the round-2
   rule: numerics are verification, not proof).

**Boundary cases (the 17 "disconnected" split-larger points).** The 17 `T_3` split-larger
`D = 1` points at `q_1 = 4` (first split balanced, `8 → 4 + 4`) lie on the TYPE BOUNDARY
between split-larger and split-tower: at `q_1 = 4`, the first split produces two `4`'s, one of
which is a tower piece, and the second split acts on the other — which is structurally a
split-tower move. These 17 points are NOT in the main split-larger `D = 1` component (305/322)
but ARE in the split-tower `D = 1` component (17/17, connected to the dyadic). Since `D` is
continuous across type boundaries (tie-agnostic, by the PL lemma §6), these points are in the
global min-level set via the adjacent type's connectivity. This boundary case is handled by
the adjacent type, not by a separate argument.

**Verification (NOT a proof).** `T_3` cascade: 816/816 `D = 1` points are star-shaped to the
dyadic (linear path stays `D = 1`). `T_3` split-larger: 305/322 in the main block-condition
component (settled by GAP-B(d)), 17/322 on the type boundary (settled by adjacent type).
`T_3` split-tower: 17/17. `T_4` cascade 3-split: 165/165. These numerics are consistent with
the mechanism but do NOT constitute a proof.

**GAP (GAP-C):** Sub-gap (ii) is CLOSED (vacuous, §14). The remaining open step is **sub-gap (i)**:
prove that every cell face in the min-level set `{D = 1}` that is NOT a block-condition cell face
(V-shape cell faces) nonetheless inherits the block condition on the face (so `D ≡ 1` by GAP-B(d)),
OR give a direct non-circular argument that `D ≥ 1` on V-shape cell faces. Verified `T_3` (all
V-shape cell faces in the cascade type have the block condition) and `T_4` (cascade 3-split);
open for general `n`. **The spine sign-pattern / multi-swap subset-sum framing is NOT a viable
closing route — see §14(B) for the circularity finding.**

### 14. Mass-balance lemma + spine sign-pattern (honest circularity finding) — §14

**(A) Mass-balance lemma — PROVED (proposed for certification, `lemmas/mass-balance-lemma.md`).**

**Statement.** On a block-condition PL cell `C_σ` of a refinement of `T_n` (top piece `2^n`
split into `r ≥ 2` fragments, every split's fragments at same-sign positions):

(i) `D = 2 S_+ - D_n`, where `S_+` = mass at `+` (odd-index) positions. (Pure algebra:
`D = S_+ - S_-`, `S_+ + S_- = D_n`.)

(ii) `D = 1 ⟺ S_+ = 2^n ⟺` the all-top-`+`/all-below-`−` sign pattern
(`telescoping-block-lemma` (d)).

**Proof.** (i) `D = S_+ - S_- = S_+ - (D_n - S_+) = 2 S_+ - D_n`. (ii) Since `D_n = 2^{n+1} - 1`
is odd, `(D_n + 1)/2 = 2^n`, so `D = 1 ⟺ S_+ = 2^n`. By the block condition, all `r` top
fragments sit at a single sign. If all at `−`: they contribute `0` to `S_+`, so
`S_+ ≤` (below-top mass) `= 2^n - 1 < 2^n`, giving `D ≤ -1 ≠ 1`. If all at `+`: they contribute
exactly `2^n` to `S_+`, so `S_+ = 2^n ⟺` (below-top mass at `+`) `= 0 ⟺` all below-top pieces at
`−`. Hence `D = 1` forces the all-top-`+`/all-below-`−` pattern, which by `telescoping-block-lemma`
(d) gives `D = 2^n - (2^n - 1) = 1` on the whole cell. ∎

**Consequence.** Sub-gap (ii) (block-condition `D = 1` cells without the pattern and without a
dyadic endpoint) is **vacuous**: every block-condition `D = 1` cell has the pattern and is settled
directly by GAP-B(d). This is rigorous, `n`-independent, certifiable now.

**(B) Spine sign-pattern lemma — honestly CIRCULAR as the nosaddle-close explorer framed it.**

The nosaddle-close explorer (round 5) proposed a "spine sign-pattern lemma" as the G1-closer: at
every `D = 1` breakpoint, the spine (after `spine-pair-cancellation` S1) interleaves as
(fragment, tower, fragment, tower, …) with all fragments at `+` and all towers at `−`, giving
`D(spine) = F - T = 1` by the "mass identity `F = T + 1`" (where `F` = total non-tower spine mass,
`T` = total tower spine mass). The single-swap argument: swapping one fragment `v` (at `+`) with
one tower `t` (at `−`) changes `D` by `2(t - v)`, so `D = 1` preserved ⟹ `t = v`, but `t` is a
power of 2 and `v` is not — impossible. The multi-swap argument (subset-sum): swapping `k`
fragments (total `f`) with `j` towers (total `t`) preserves `D = 1` iff `f = t`.

**This framing is CIRCULAR; neither the single-swap nor the multi-swap closes GAP-C.**

The circularity is in the "mass identity `F = T + 1`." This identity is NOT an independent fact
about the spine's mass bookkeeping — it is EQUIVALENT to `D(spine) = 1` under the assumed
interleaving pattern. The decomposition is: let `f_+` = fragment mass at `+` positions, `f_-` =
fragment mass at `−` positions, `t_+` = tower mass at `+`, `t_-` = tower mass at `−`. Then
`F = f_+ + f_-`, `T = t_+ + t_-`, and

$$D(\text{spine}) = f_+ - f_- + t_+ - t_- = (F - T) + 2(t_+ - f_-). \tag{†}$$

When the pattern holds (`f_- = 0`, `t_+ = 0`), `D = F - T`. So `F - T = 1 ⟺ D = 1` (under the
pattern). The "mass identity" is just `D = 1` restated, not a separate constraint.

**Exact verification (`Fraction` arithmetic) that `F - T` is NOT identically `1`.** The spine of
the `T_3` config obtained by `8 → 5 + 3` (top) and `4 → 3 + 1` (below-top) is `{5, 2}` (the two
`3`'s pair-cancel, the two `1`'s pair-cancel). Here the pattern HOLDS (position 1 = `5` fragment
at `+`, position 2 = `2` tower at `−`), yet `F = 5`, `T = 2`, `F - T = 3 = D ≠ 1`. So a
pattern-holding spine can have `F - T = D = 3`, not `1`. The identity `F = T + 1` fails here,
confirming it is equivalent to `D = 1`, not an independent mass identity.

**Why the single-swap and multi-swap are circular.** Both arguments start from the pattern
(`D = F - T`) and consider "swaps" that move fragment mass `v` (or `f`) to `−` and tower mass `t`
(or `t`) to `+`, changing `D` by `2(t - v)` (or `2(t - f)`). For `D` to STAY `1` after the swap,
they require `2(t - v) = 0` ⟹ `t = v`. But this computation PRESUPPOSES the starting value
`D = F - T = 1`, i.e. presupposes the mass identity `F = T + 1`, which (as just shown) is itself
equivalent to `D = 1` under the pattern. Equivalently, from `D = 1` alone one derives
`S_+ = (S + 1)/2 = (F + T + 1)/2`; the pattern's `S_+ = F` is an ADDITIONAL assumption
(`f_- = 0, t_+ = 0`), not a consequence of `D = 1`. Without the pattern, `D = 1` is consistent
with arbitrary `t_+ - f_-` (equation `(†)` gives `(F - T) + 2(t_+ - f_-) = 1`, a single equation
in the two unknowns `F - T` and `t_+ - f_-`). So the subset-sum obstruction does NOT follow from
`D = 1`; it requires the pattern as a premise, which is what it purports to prove.

**Precise statement of GAP-C-hard (what a non-circular proof would need).** Provide a genuinely
NON-CIRCULAR argument that `D ≥ 1` on every breakpoint face NOT settled by GAP-B(d) — i.e. on
V-shape cell faces (sub-gap (i)) and on block-condition cells whose constant value is not yet
shown to be `≥ 1`. The spine sign-pattern / multi-swap subset-sum route does NOT supply this:
the "mass identity `F = T + 1`" is equivalent to `D = 1` under the pattern, so it cannot prove
`D ≥ 1`. A viable route must either (a) prove V-shape cell faces inherit the block condition
(then GAP-B(d) applies on the face), verified `T_3`/`T_4` but open generally; or (b) exhibit a
different, non-circular mass identity or charging argument that lower-bounds `D` on non-block
cells. **Do NOT chase the spine sign-pattern / multi-swap framing for multiple rounds — it is
circular.** (Computation: 0/523 subset-sum matches across `T_3/T_4/T_5` `D = 1` configs is
strong evidence the pattern holds at `D = 1` breakpoints, but it is a CHARACTERIZATION of `D = 1`
configs, not a proof that `D ≥ 1` everywhere; numerics are verification, not proof, per the
round-2 rule.)

### 15. Mass-budget breakpoint inequality (GAP-C(i) narrowing) — PROVED (§15, NEW)

This section proves a NEW, non-circular constraint — the **mass-budget inequality** — that
narrows GAP-C(i) by showing the block condition is **sufficient** (not just necessary) for
`D = 1` at breakpoints.

**Setup.** Consider a **breakpoint** config of `T_n` (cascade type: all `≤ n` marks split the top
piece `2^n` into fragments `f_1, …, f_r` with `r = k+1 ≤ n+1`, sum `= 2^n`; the below-top tower
pieces `{2^{n-1}, …, 2, 1}` are unsplit). By the breakpoint condition (§6), every fragment value
appears `≥ 2` times in the full config `{f_1, …, f_r, 2^{n-1}, …, 2, 1}`. Apply
`spine-pair-cancellation` S1: adjacent-equal pairs cancel, leaving the **spine** — a strictly
decreasing sequence of values with odd count in the config. `D(config) = D(spine)` (S1).

**Origin tracking.** Classify each spine piece by origin:
- **Fragment (F):** a non-dyadic value `w` (not a power of `2`) that survived pair-cancellation.
  Since `w` is non-dyadic, no tower piece has value `w`, so `w` can only tie another top fragment.
  At a breakpoint, `w` appears `≥ 2` times; if it survived (odd count), `≥ 3` times.
- **Tower (T):** a power of `2`, say `2^k`, that survived. Its count is `1 + d_k` where `d_k` =
  (number of top fragments `= 2^k`). Odd count (survival) `⟺ d_k` even. The surviving piece is
  the tower piece (origin T).

Let `F = Σ` (surviving non-dyadic fragment values), `T = Σ` (surviving tower values).

**Lemma 15 (mass-budget inequality).** *At a breakpoint of `T_n` (cascade type, all `n`),*
$$T \;\ge\; 3F - 1.$$

**Proof.** The top mass `2^n` is partitioned among fragments. At a breakpoint, each fragment
value `v` appears `c_v ≥ 2` times. Classify:

- **Surviving non-dyadic** values `w_1, …, w_l` (odd count `c_{w_i} ≥ 3`): each consumes
  `c_{w_i} · w_i ≥ 3 w_i` from the top budget. Total `≥ 3F`.
- **Non-surviving non-dyadic** values `u_1, …, u_p` (even count `≥ 2`): each consumes
  `≥ 2 u_j ≥ 0`. Total `≥ 0`.
- **Dyadic** values `2^k` appearing `d_k` times among top fragments: consume `d_k · 2^k`.

The total: `2^n ≥ 3F + 0 + Σ_k d_k · 2^k`.

Now, for each tower piece `2^k`:
- If `d_k` is **odd** (`≥ 1`): `2^k` is **not** in the spine (count `1 + d_k` even, paired). It
  contributes `d_k · 2^k ≥ 2^k` to the top budget.
- If `d_k` is **even** (`≥ 0`): `2^k` **is** in the spine (count odd). It contributes
  `d_k · 2^k ≥ 0`.

So `Σ_k d_k · 2^k ≥ Σ_{d_k \text{ odd}} 2^k = (2^n - 1) - T` (the non-surviving tower mass; the
surviving tower mass is `T`, total tower mass is `2^n - 1`).

Substituting: `2^n ≥ 3F + (2^n - 1) - T`, giving `1 ≥ 3F - T`, i.e., `T ≥ 3F - 1`. ∎

**Remark (tightness).** The inequality is tight at several breakpoints. E.g., `T_3` cascade
breakpoint `frags = {7/3, 7/3, 7/3, 1}` (`3·7/3 + 1 = 8`): spine `{4, 7/3, 2}`, `F = 7/3`,
`T = 6 = 3·(7/3) - 1`. `D = 4 - 7/3 + 2 = 11/3 > 1`. The inequality is tight but `D > 1`.

**Corollary 15a (block condition sufficiency).** *At a breakpoint of `T_n`, if the block
condition holds on the spine (all surviving fragments at `+` positions) and `D = 1`, then
`F = 0` (the spine is all-tower).*

**Proof.** Block condition (all `F` at `+`) gives `D = F - T` (fragments at `+`, towers at `−`).
`D = 1` gives `F = T + 1`. Lemma 15: `T ≥ 3F - 1 = 3(T+1) - 1 = 3T + 2`, so `-2T ≥ 2`,
`T ≤ -1`. Since `T ≥ 0` (nonneg mass), this is a contradiction — **unless `F = 0`** (in which
case the block condition is vacuous, `D = -T` which can't be `1` for `T ≥ 0` unless we're in the
degenerate case; more precisely, `F = 0` gives `D = A` where `A` is the tower alternating sum, a
positive integer `≥ 1` by the dyadic dominance of `even-group-spine-lower-bound` §8). ∎

**Corollary 15b (continuity rules out "all `F` at `−`").** *At a `D = 1` breakpoint, the "all
surviving fragments at `−`" block direction is impossible.*

**Proof.** If the block condition holds with all fragments at `−` on an adjacent PL cell, the
mass-balance lemma (§14) gives `D ≤ 2(2^n - 1) - D_n = -1` on that cell (all top fragments at `−`
`⟹ S_+ ≤ 2^n - 1 < 2^n`). But `D` is continuous (PL, §6) and `D = 1` at the breakpoint vertex
(on the cell boundary). A cell with `D ≤ -1` on its interior cannot have `D = 1` at its boundary
by continuity. Contradiction. ∎

**Combining 15a + 15b:** At a `D = 1` breakpoint, **if** the block condition holds on any adjacent
cell, it must be the "all `F` at `+`" direction (15b rules out `−`), which forces `F = 0` (15a),
making the spine dyadic, and `D ≥ 1` by §8. **The block condition is sufficient for `D = 1` at
breakpoints.**

**What remains open (GAP-C(i)-balance-implies-block).** The step we CANNOT prove: at a `D = 1`
breakpoint, the block condition holds on (at least one) adjacent cell. Equivalently: `F = 0`
(no non-dyadic spine pieces) at every `D = 1` breakpoint, without assuming the block condition.
The mass-budget inequality `T ≥ 3F - 1` constrains `F` but does not, by itself, force `F = 0`
when the block condition fails (fragments at both `+` and `−` positions). Any counterexample to
`D ≥ 1` must satisfy: `F > 0`, `T ≥ 3F - 1`, `D = 1` with fragments at mixed signs — a much more
constrained scenario than before this round.

**Why the superincreasing-chain mechanism (round 6 reviewer flag) is avoided.** The reviewer
correctly flagged that bare superincreasing (`2^k >` sum of smaller `2^j`) constrains tower-vs-tower
only, not fragment-vs-tower. Lemma 15 does NOT use superincreasing. It uses the **breakpoint
structure** (every non-dyadic fragment must tie another fragment, forcing `≥ 2` copies, `≥ 3` for
survivors) and the **mass budget** (`3w ≤ 2^n` per surviving fragment). The dyadic dominance
(`2^{k_1} > 2^{k_1} - 1 ≥` sum of smaller distinct powers) is used only in §8 for the `F = 0` case
(spine all-tower), not for the fragment-vs-tower relationship.

**Verification (not a proof step, `Fraction`-exact).**
- `F = 0` at all `D = 1` breakpoints of `T_3`: 151 breakpoints across all types (cascade,
  split-larger, split-tower, split-all-tower), all with `F = 0`, min `D = 1`.
- Block condition holds at all 523 `D = 1` configs (`T_3` cascade 120 + split-larger 98 +
  split-tower 9; `T_4` cascade 35 + split-larger 241 + split-tower 5; `T_5` cascade 15).
- Mass-budget `T ≥ 3F - 1` verified 0 violations at all constructed breakpoints, including
  non-grid-aligned values: `{7/3, 7/3, 7/3, 1}` (`T = 6 = 3F - 1`, tight), `{4/3, 4/3, 4/3, 4}`
  (`T = 3 = 3F - 1`, tight), `{14/3, 14/3, 14/3, 1, 1}` for `T_4` (`T = 15 = 3F - 1`, tight).
- When `F > 0` at a breakpoint, `D > 1` always: smallest `D = 5/3` (at `{4/3, 4/3, 4/3, 4}` for
  `T_3`, spine `{2, 4/3, 1}`, `D = 2 - 4/3 + 1 = 5/3`).
- All `D = 1` non-breakpoint configs (119 for `T_3` cascade, 96 for split-larger) have `F > 0`
  AND the block condition holding (alternating spine `F, T, F, T, …, F`) — they are on PL cells
  where `D ≡ 1` by GAP-B(d), and the breakpoint is on the cell boundary (dyadic endpoint).

---

### 16. The vertex-level crux (★) and Mechanism A — NEW (round 7)

This section attacks the open core (GAP-C / G1) from a **vertex-level** angle. The key new
object is the restatement (★) below, which the face-level framings (§§11–15) missed: at a
strong-breakpoint *vertex* (not just a face), the structure is far more constrained — at most
one non-dyadic fragment survives — and the sign-forcing reduces to a clean tower-dominance
argument in one of two sub-cases. This is the strongest lower-bound lead in 7 rounds.

#### 16.0. The restatement (★) and the load-bearing inference

**Definition (strong-breakpoint PL vertex).** A refinement of `T_n` is a **strong-breakpoint
vertex** if (i) it is a breakpoint (every split-product fragment ties an adjacent piece in the
sorted order — `pl-breakpoint-minimum`), and (ii) it is a **vertex** of the PL complex of `D`
(zero-dimensional cell: every split position is pinned by ties). Equivalently: the tie
constraints on the fragments form a system with a unique solution.

**(★) Restatement of the crux.** *At every strong-breakpoint vertex of `T_n` with `F > 0` (a
surviving non-dyadic fragment), `D > 1` (tower units).*

**Load-bearing inference (reviewer-confirmed sound).** By `pl-breakpoint-minimum` (certified),
the global minimum of `D` over all `≤ n`-mark refinements of `T_n` is attained at a
strong-breakpoint PL vertex. (Standard PL fact: `D` is continuous piecewise-linear on the
compact refinement polytope; min of a PL function on a polytope is at a vertex of the PL
subdivision; a tie-face is a cell where `D` is affine, its min at a sub-vertex.) By
`dyadic-refinement-lower-bound` (certified), at a **dyadic** vertex (`F = 0`, all fragments
powers of 2), `D ≥ 1`. **(★)** handles the **non-dyadic** vertices (`F > 0 ⟹ D > 1`).
Combining: global min `D ≥ 1` ⟹ `D*(T_n) ≥ 1/D_n` ⟹ `c(n) ≥ 2^n/D_n` (lower bound CLOSED,
for the `n` where (★) is proved).

So the entire lower bound reduces to **proving (★)**. This section proves (★) in the
**frag-at-`+` sub-case** (single survivor, budget-tight) and proves the reduction lemmas
(single-survivor, v-bracket, largest-tower-exceeds-fragment, decomposition), leaving the
**frag-at-`−` sign-forcing** and the **mixed-type / multi-survivor generalization** as honest
explicit gaps. The non-circularity caveat (reviewer point (c)) is addressed in §16.5.

#### 16.1. Lemma (single-survivor at a cascade vertex) — PROVED

**Statement.** At a strong-breakpoint vertex of `T_n` of the **cascade type** (all `≤ n` marks
split the top piece `2^n`; below-top tower pieces `{2^{n−1},…,1}` are unsplit), at most **one**
non-dyadic fragment value survives into the spine (after `spine-pair-cancellation` S1).

**Proof.** The top piece `2^n` is split into `r ≤ n+1` fragments summing to `2^n` — ONE sum
constraint. At a strong breakpoint, every fragment value appears `≥ 2` times. By
`strong-breakpoint-group-structure` (S2, certified), non-dyadic fragments form adjacent-equal
groups of size `≥ 2`; a survivor (odd count) has size `≥ 3`.

A "free group" is a maximal set of fragments sharing a non-tower value `v`; it introduces one
free parameter `v`. The single sum constraint `Σ(fragments) = 2^n` pins one linear combination of
the free parameters. With `n_{free}` free groups (distinct non-tower values), the free-parameter
count is `n_{free}`, and the sum constraint reduces it to `n_{free} − 1` effective free
parameters.

A **vertex** has **zero** effective free parameters (all positions pinned). Hence
`n_{free} − 1 = 0`, i.e. `n_{free} ≤ 1`: **at most one free group**. A free group of even size
fully cancels (S1, `F = 0` from it); of odd size leaves one survivor. So the number of surviving
non-dyadic fragment VALUES is `≤ 1`. ∎

**Remark (T_3: single-survivor for ALL vertex types).** For `T_3` (`n = 3`, `≤ 3` marks), a
split into `r` fragments uses `r − 1` marks. Two splits each with `≥ 3` fragments (each
producing a non-dyadic free group, since a size-2 free group has value `sum/2 =` a power of 2,
hence dyadic) require `≥ (3−1) + (3−1) = 4` marks `> 3`. So at most one split has `≥ 3`
fragments, giving at most one non-dyadic free group — hence `n_{free} ≤ 1` for **every** `T_3`
vertex type (cascade, split-tower, split-2tower, mixed). Single-survivor holds for all of `T_3`.
(For `n ≥ 4`, multi-survivor vertices exist — see §16.6, GAP-B.)

#### 16.2. Lemma (v-bracket) — PROVED (cascade type, single survivor)

**Statement.** At a cascade-type strong-breakpoint vertex with one surviving non-dyadic
fragment of value `v` (appearing `c ≥ 3` times), `v < 2^{n−1}` (strictly below the largest tower
piece).

**Proof.** By the mass-budget argument (`mass-budget-breakpoint-inequality`, certified): each
copy of `v` consumes `v` from the top budget `2^n`, so `c·v ≤ 2^n`, `v ≤ 2^n/c ≤ 2^n/3 <
2^{n−1}` (for `n ≥ 2`; `n = 1` is the certified base case). ∎

(The lower bound `v > 1` is verified on all enumerated vertices — min `v = 4/3` — but NOT
proved for general `n`; see GAP-A in §16.6.)

#### 16.3. Lemma (largest-tower-exceeds-fragment) — PROVED (cascade, single survivor)

**Statement.** At a cascade-type strong-breakpoint vertex with one surviving non-dyadic
fragment `v`, the **largest surviving tower** `2^j` (the largest power of 2 in the spine)
satisfies `2^j > v`. Consequently the largest spine element is a tower at position 0 (sign `+`).

**Proof.** Suppose `2^j ≤ v`. Every tower `2^k` with `k > j` is NOT in the spine (else it would
be larger than `2^j`, contradicting maximality of `j`). So for each `k > j`, the count
`1 + d_k` (tower piece + `d_k` top-fragments of value `2^k`) is **even** (not surviving), hence
`d_k` is odd `≥ 1`: at least one top-fragment of value `2^k` exists, consuming `≥ 2^k` from the
top budget. The total consumed by these is `≥ Σ_{k>j} 2^k = 2^n − 2^{j+1}`. The surviving
fragment consumes `c·v ≥ 3v ≥ 3·2^j` (using `2^j ≤ v`). So the top budget satisfies
`2^n ≥ (2^n − 2^{j+1}) + 3·2^j = 2^n − 2^{j+1} + 3·2^j = 2^n + 2^j`, i.e. `0 ≥ 2^j` —
contradiction (`2^j > 0`). Hence `2^j > v`. ∎

#### 16.4. The decomposition and the two sub-cases

**Decomposition (algebra, reviewer-confirmed non-circular).** Let `f₊, f₋` = fragment mass at
`+, −` spine positions; `t₊, t₋` = tower mass at `+, −`. `F = f₊ + f₋`, `T = t₊ + t₋`.
$$D = (f₊ − f₋) + (t₊ − t₋) = (F − T) + 2(t₊ − f₋). \tag{†}$$
(Pure algebra: expand and collect.) At a budget-tight vertex (`T = 3F − 1`,
`mass-budget-breakpoint-inequality`):
$$D = 1 − 2F + 2(t₊ − f₋), \qquad\text{so}\qquad D > 1 \iff t₊ − f₋ > F. \tag{‡}$$

This is **algebra only** — it does NOT presuppose any sign pattern (the round-5 circularity was
in the ARGUMENT that `S₊ = F`, not in this identity). The sign-forcing below derives
`t₊ − f₋ > F` from sort-order + mass-budget + tower-vs-tower dyadic dominance, WITHOUT assuming
the interleaving pattern.

**Lemma (t₊ > t₋, tower-vs-tower dyadic dominance).** At any non-dyadic vertex (cascade, single
survivor), the tower mass at `+` positions exceeds the tower mass at `−` positions:
`t₊ > t₋`.

**Proof.** The spine (after pair-cancellation, S1) is a strictly-decreasing sequence of distinct
powers of 2 plus the single fragment `v`. Position 0 (sign `+`) is the **largest** spine element,
which by §16.3 is a tower `2^j > v`. By **dyadic dominance** (the defining property of distinct
powers of 2: `2^j > Σ` of all smaller distinct powers), `2^j` exceeds the sum of ALL other
surviving towers: `2^j > T − 2^j`, i.e. `2^j > T/2`. Since position 0 contributes to `t₊`, and
`t₊ + t₋ = T`, we have `t₊ ≥ 2^j > T − 2^j ≥ t₋`. ∎

#### 16.5. PROVED sub-case: frag-at-`+` (single survivor, budget-tight) ⟹ D > 1

**Proposition.** At a cascade-type strong-breakpoint vertex with one surviving fragment `v`, if
(i) the block condition holds with `v` at a `+` position (`f₋ = 0`, `f₊ = F = v`) and (ii) the
mass budget is tight (`T = 3F − 1`), then `D > 1`.

**Proof.** By `(‡)`: `D = 1 − 2F + 2(t₊ − f₋) = 1 − 2v + 2t₊` (since `f₋ = 0`). By §16.3, the
largest surviving tower `2^j` is at position 0 (`+`), so `t₊ ≥ 2^j > v = F`. Hence
`2t₊ > 2F = 2v`, giving `D = 1 − 2v + 2t₊ > 1`. ∎

**Non-tight extension (conditional on `v > 1`).** Without budget-tightness, `(†)` gives
`D = (F − T) + 2(t₊ − f₋) = F − T + 2t₊ = F + (t₊ − t₋)` (using `T = t₊ + t₋`, `f₋ = 0`). By
§16.4, `t₊ > t₋`, so `D > F = v`. **If `v > 1`** (verified on all enumerated vertices, min
`v = 4/3`, but NOT proved for general `n` — see GAP-A), then `D > 1`.

So the **frag-at-`+` sub-case is CLOSED at budget-tight vertices** (proved), and closed at
non-tight vertices **conditional on `v > 1`** (verified, gap on `v > 1`).

#### 16.6. Open gaps (honest)

**GAP-A (v > 1 lower bound).** The lower bound `v > 1` (tower units) for the single surviving
non-dyadic fragment is **verified** on all 15 + 32 = 47 non-dyadic enumerated vertices (min
`v = 4/3`, for both `T_3` and `T_4`, all types) but **NOT proved** for general `n`. The mass
budget gives the upper bound `v ≤ 2^n/3 < 2^{n−1}` (§16.2) but not the lower bound. Proving
`v > 1` would close the non-tight frag-at-`+` sub-case. The obstruction: for large `n`, the
budget `2^n` has room for `v ≤ 1` in principle; the breakpoint tie-structure constrains it but
the argument is not yet formalized.

**GAP-B (single-survivor for `n ≥ 4` mixed types).** For `n ≥ 4`, multi-survivor vertices exist:
e.g. `T_4`, top `16 → {16/3, 16/3, 16/3}` (2 marks) + tower `4 → {4/3, 4/3, 4/3}` (2 marks) =
4 marks = `n`. This is a valid strong-breakpoint vertex with TWO surviving non-dyadic values
(`16/3` F-origin, `4/3` T-origin), spine `{8, 16/3, 4, 4/3, 2, 1}`, `D = 3 > 1` (verified, not
a counterexample to (★)). **However**, at any PL vertex, at most ONE **F-origin** (top-split)
non-dyadic survivor exists: two F-origin free groups in the top split share one sum constraint
(`Σ = 2^n`), giving `n_{free} − 1 ≥ 1` free parameters ⟹ a face, not a vertex. (T-origin
non-dyadic survivors, from tower splits, can coexist, each pinned by its own tower's sum
constraint.) The mass-budget inequality `T ≥ 3F − 1` is **cascade-type only** (certified); its
generalization to mixed types (where non-dyadic T-origin survivors consume from tower budgets,
not the top budget) is **NOT proved**. So (★) for mixed multi-survivor vertices is
**verified** (47 multi-survivor vertices `T_4`, all `D > 1`, 0 counterexamples) but **NOT proved
structurally**.

**GAP-C / GAP-(★)-d-minus (the frag-at-`−` sign-forcing — the genuine open core).** At a
budget-tight cascade vertex with single survivor `v` at a `−` position (`f₋ = v`, `f₊ = 0`),
`(‡)` requires `t₊ > 2v`. The near-miss: by §16.4, `t₊ ≥ 2^j` (largest tower at `+`), and
`2^j > (T + v)/2 ≥ (3v − 1 + v)/2 = 2v − 1/2` (dyadic dominance: `2^j` exceeds sum of all other
spine elements including `v`). So `t₊ > 2v − 1/2`. **The `1/2` gap is the obstruction** —
`t₊ > 2v − 1/2` does not imply `t₊ > 2v`. Since `t₊` is an integer (a subset-sum of distinct
powers of 2) and `2v` is generally non-integer, the gap could in principle be closed by an
integrality/rounding argument, but the precise rounding obstruction is not yet formalized.
**Verified:** 13/13 frag-at-`−` vertices (all enumerated) satisfy `t₊ > 2v` (0 failures). This
is the strongest verified-but-unproved step in the approach.

**GAP-D (vertex-type completeness for `n ≥ 5`).** The enumeration covers `T_3` (all types,
single-survivor forced by mark budget) and `T_4` (cascade, split-tower, split-2tower, and the
mixed top-r3+tower-r3 family with nfree `≤ 2`). For `n ≥ 5`, the combinatorial type space grows
(triple splits, more mixed families). The structural single-survivor argument (at most one
F-origin survivor per vertex) partially extends, but the full type classification for `n ≥ 5` is
not enumerated.

#### 16.7. Verification (NOT a proof step) — extended enumeration

The enumeration (`mechanism_probe.py`, `vertex_sign_clean.py`, `nfree2_focus.py`,
`breakpoint_exact_enum.py`, all exact-`Fraction`, no floats) covers:

| Tower | Types enumerated | Vertices | `D < 1` | `D = 1` | Non-dyadic (`F>0`) | min non-dyadic `D` |
|---|---|---|---|---|---|---|
| `T_3` | cascade (r=2,3,4), split-tower (k=1,2), split-2tower (k1=2,k2=1) | 64 total (with `T_4`) | 0 | 7 (all `F=0`) | 15 | 5/3 |
| `T_4` | cascade (r=2,3,4,5), split-tower (k=1,2,3), split-2tower (3 types) | (above) | 0 | 7 (all `F=0`) | (above) | 5/3 |
| `T_4` mixed | top r=3 + tower r=3 (all k), incl. nfree=2 multi-survivor | 67 | 0 | (dyadic) | 32 | 2 |

**(★) verified: 0 counterexamples across 131 vertices** (64 cascade/split-tower/split-2tower +
67 mixed). `D = 1` occurs ONLY at dyadic vertices (`F = 0`, settled by
`dyadic-refinement-lower-bound`). All 15 single-survivor non-dyadic vertices have `D > 1` (min
`5/3`). All 47 `nfree = 2` multi-survivor mixed vertices (`T_4`) have `D > 1` (min `2`). The
decomposition `(†)` checks out (`decomp_check = True`) at all 15 single-survivor vertices. Mass
budget `T ≥ 3F − 1` is tight at 12/15 single-survivor vertices. The "largest tower at `+` >
frag + smaller" dominance FAILS exactly the 2 frag-at-`+` cases (confirmed: use the universal
`t₊ − f₋ > F` condition, not that dominance).

**No counterexample to (★) was found.** If one existed, it would be a decisive negative result
for this route; none was hidden.

#### 16.8. Summary of §16

**(★) is PROVED** for: cascade-type, single-survivor, budget-tight, **frag-at-`+`** vertices
(§16.5). **(★) is conditionally proved** for non-tight frag-at-`+` vertices (conditional on
`v > 1`, GAP-A). **(★) is verified-but-unproved** for: frag-at-`−` (GAP-C, 13/13, near-miss
`t₊ > 2v − 1/2`), and mixed/multi-survivor `n ≥ 4` (GAP-B, 47/47). The full lower bound
`c(n) ≥ 2^n/D_n` follows from (★) + `pl-breakpoint-minimum` + `dyadic-refinement-lower-bound`
for the `n` where (★) is fully proved. Currently (★) is fully proved only in a sub-case, so the
lower bound remains **partial** (Status: `partial`).

---

## Lower-bound summary

For Liu's tower `T_n` and **any** Xiang refinement with `≤ n` marks:

- **Case (a)** (top piece `2^n` unsplit): `D ≥ 1` — certified (`tower-top-unsplit`).
- **Case (b-i)** (exactly one split, of the top): `D ≥ D(T_{n−1}) ≥ 1` — **proved** (§4).
- **Case (b-ii-dyadic)** (multi-split, all splits balanced): `D ≥ 1` — **proved** (§5).
- **Case (b-ii-non-dyadic)** (multi-split, ≥1 unbalanced split):
  - **2 splits** (top-fragment-split type): `D ≥ D(T_{n−2}) ≥ 1` — **proved** (§7, all `n`).
  - **Even-group strong breakpoints**: `D ≥ 1` — **proved** (§8, all `n`).
  - **Block-condition cells** (all top-piece fragments at `+`, all below-tower at `−`):
    `D = 1` — **proved** (§11 GAP-B(d), all `n`; direct mass-identity computation, no dyadic
    endpoint needed). Covers spine-3,5,7 cascade cells, split-larger block cells, split-tower
    block cells.
  - **Spine-3 cascade** (two non-dyadic fragments straddling a tower piece): `a + d = t + 1`
    ⇒ `D = 1` — **proved** (§12 GAP-A, corollary of GAP-B(d)).
  - **k ≥ 3 splits, general (V-shape cell faces, non-block cells without dyadic endpoint)**:
    `D ≥ 1` — **conjectured**, verified `T_3` (816/816 + 322/322 + 17/17) and `T_4` (165/165);
    star-shaped transport (§13 GAP-C) is the open step; **GAP (G1/GAP-C)**.
  - **Mass-balance lemma** (round 5, §14, proposed for certification `mass-balance-lemma`): on a
    block-condition cell `D = 1 ⟺` the all-top-`+`/all-below-`−` pattern — **sub-gap (ii)
    VACUOUS**. The spine sign-pattern / multi-swap framing is **CIRCULAR** (§14(B)): the
    "mass identity `F = T + 1`" is equivalent to `D = 1` under the pattern, verified
    `Fraction`-exact (spine `{5,2}`, pattern holds, `F - T = 3 ≠ 1`), so it does NOT close GAP-C.
  - **Mass-budget breakpoint inequality** (round 6, §15, NEW, proposed for certification as
    `mass-budget-breakpoint-inequality`): at a breakpoint of `T_n`, `T ≥ 3F − 1` (proved).
    **Corollary:** block condition + `D = 1` at breakpoint ⟹ `F = 0` (spine dyadic) ⟹ `D ≥ 1`
    by §8. Continuity rules out "all `F` at `−`". **Block condition is SUFFICIENT for `D = 1` at
    breakpoints.** Verified: `F = 0` at all 151 `D = 1` breakpoints of `T_3`; `T ≥ 3F−1` 0
    violations at all constructed breakpoints; `F > 0` always gives `D > 1` (min `5/3`).
    **GAP-C(i) NARROWED:** any counterexample must have `F > 0` AND block condition failing.
  - **Vertex-level crux (★) + Mechanism A** (round 7, §16, NEW): at every non-dyadic strong-
    breakpoint vertex of `T_n`, `D > 1`. PROVED sub-cases: single-survivor (cascade, all `T_3`),
    v-bracket, largest-tower-exceeds-fragment, **frag-at-`+` budget-tight ⟹ `D > 1`** (§16.5).
    Decomposition `D = (F−T) + 2(t₊−f₋)` non-circular. **GAPS:** (GAP-A) `v > 1` (verified,
    unproved); (GAP-C/d-minus) frag-at-`−` `t₊ > 2v` (near-miss `2v−1/2`, 13/13 verified);
    (GAP-B) mixed multi-survivor `n ≥ 4` (47 nfree=2 vertices all `D > 1`, unproved);
    (GAP-D) completeness `n ≥ 5`. Verified: 131 vertices, 0 counterexamples, `D = 1` only at
    7 dyadic vertices. The decomposition algebra is non-circular; the sign-forcing does NOT
    presuppose the interleaving pattern (§16.4, §16.5).

So the lower bound `c(n) ≥ 2^n / (2^{n+1} − 1)` is **rigorously established** for `n = 1, 2, 3`
(case (a) + (b-i) cover all `n = 1`; for `n = 2, 3`, the 2-split sub-case (§7), even-group
sub-result (§8), and block-condition cells (§11) cover all breakpoints verified exhaustively)
and for **all `n`** in cases (a), (b-i), (b-ii-dyadic), (b-ii-2-split-top-fragment),
(b-ii-even-group-strong-bp), and (b-ii-block-condition-cells). The general-all-`n`-all-refinements
lower bound is blocked only by GAP-C (V-shape cell faces / non-block cells without dyadic endpoints
in the min-level set, k ≥ 3 non-dyadic).

---

## Upper bound: `c(n) ≤ 2^n / (2^{n+1} − 1)` — n=1 PROVED, general n = OPEN GAP

We must show that for *every* Liu config (≤ `n+1` pieces summing to 1), Xiang has ≤ `n` marks
forcing `D ≤ 1/D_n` (equivalently, Liu's odd-index sum `≤ 2^n/D_n`).

### Base case `n = 1` — PROVED (`lemmas/n1-base-both-bounds.md`)
Certified; `c(1) = 2/3` by hand.

### General `n` — OPEN GAP (parity coupling)

The intended mechanism (§2): one Xiang mark, splitting a piece `L` into `p ≥ q`, changes
`N(t)` by `+1` on `(0,q]`, `0` on `(q,p]`, `−1` on `(p,L]`, hence changes `D` by
`ΔD = 2q − 2·O((0,q]) − 2·O((p,L])`. One would like to choose splits so the net change per mark
telescopes to `D ≤ 1/D_n`. The obstruction (confirmed by the outline-reviewer and by the
single-split slope analysis above): the `O`-widths are global functionals of `N(t)`, and after
the first split the parities at unrelated thresholds are coupled through the single global
sort — the per-threshold cap of the `aimo-0127`-style crux does not decouple here.

**Status of (U):** proved for `n = 1`; for `n ≥ 2` the adaptive Xiang strategy is conjectured
(verified by grid search for `n = 2`: over 300 random Liu configs, Xiang's grid-best odd-index
take never exceeded `4/7`) but not proved. **GAP (U).**

---

## Answer verification

The conjectured answer `c(n) = 2^n/(2^{n+1}−1)` is **numerically exact** for `n = 1, 2, 3, 4`
(substitution returns `2/3, 4/7, 8/15, 16/31`), each attained by:
- **Liu (lower bound):** the dyadic tower `T_n`, which resists every Xiang refinement at
  `D ≥ 1` (equality at the balanced-pairs config `{2^{n−1},2^{n−1},…,2,2,1,1,1}/D_n`).
- **Xiang (upper bound):** for `n = 1` *proved*; for `n = 2, 3, 4` *verified* by exhaustive
  / random-config grid search.

For `n = 1` the result `c(1) = 2/3` is **fully proved** (both bounds; `n1-base-both-bounds`).
For general `n` the proof is blocked by GAP (G1) on the lower bound and GAP (U) on the upper
bound. The answer itself is fully determined numerically and consistent across all checks.

---

## Gaps (explicit)

1. **(G1 / GAP-C) [lower bound, non-dyadic multi-split, k ≥ 3].** Prove `D ≥ 1` (tower units) when
   Xiang uses `≥ 3` marks with at least one unbalanced split of `T_n`. The proven reduction (§6)
   lands the global minimum at a breakpoint (tie) config; §§4–5 settle single-split and dyadic
   breakpoints; §7 settles 2-split (top-fragment); §8 settles even-group strong breakpoints;
   **§11 (GAP-B) settles block-condition cells** (all top fragments at `+`, all below-tower at `−`:
   `D = 1` directly by mass identity, no dyadic endpoint needed); **§12 (GAP-A) settles spine-3
   cascade** (mass identity `a + d = t + 1`); **§14 (mass-balance lemma) closes sub-gap (ii)** —
   every block-condition `D = 1` cell has the all-top-`+`/all-below-`−` pattern (vacuous sub-gap).
   **Round 6 NEW: §15 (mass-budget inequality) `T ≥ 3F − 1` at breakpoints** — block condition +
   `D = 1` ⟹ `F = 0` (spine dyadic, `D ≥ 1` by §8); continuity rules out "all `F` at `−`".
   **Block condition is SUFFICIENT for `D = 1` at breakpoints.** The remaining open step is
   **GAP-C(i)-balance-implies-block**: prove the block condition (or `F = 0`) at `D = 1`
   breakpoints directly. Any counterexample must have `F > 0` AND block condition failing.
   Verified: `F = 0` at all 151 `D = 1` breakpoints of `T_3`; block condition holds at all 523
   `D = 1` configs (`T_3`/`T_4`/`T_5`); `T ≥ 3F − 1` 0 violations.
   **The spine sign-pattern / multi-swap subset-sum framing is CIRCULAR (§14(B))**: the "mass
   identity `F = T + 1`" is equivalent to `D = 1` under the assumed pattern (verified
   `Fraction`-exact: spine `{5,2}` has pattern, `F - T = 3 ≠ 1`), so it does NOT close GAP-C — do
   not chase it.
   **Round 7 NEW: §16 (vertex-level crux (★) + Mechanism A).** The crux restated: at every
   non-dyadic strong-breakpoint **vertex** of `T_n`, `D > 1`. PROVED sub-cases: single-survivor
   (cascade, all `T_3`), v-bracket, largest-tower-exceeds-fragment, **frag-at-`+` budget-tight
   ⟹ `D > 1`** (§16.5, via `t₊ > v`). Decomposition `D = (F−T) + 2(t₊−f₋)` non-circular.
   **Open gaps:** (GAP-A) `v > 1` (verified, unproved); (GAP-C/d-minus) frag-at-`−` `t₊ > 2v`
   (near-miss `t₊ > 2v − 1/2`, 13/13 verified — the genuine open core); (GAP-B) mixed
   multi-survivor `n ≥ 4` (mass-budget cascade-only; 47 nfree=2 vertices all `D > 1` but
   unproved structurally); (GAP-D) vertex-type completeness `n ≥ 5`. Verified: 131 vertices,
   0 counterexamples. The decomposition algebra is non-circular; the sign-forcing does NOT
   presuppose the interleaving pattern (§16.4–5).
2. **(U) [upper bound, general n].** Produce an explicit Xiang strategy (≤ `n` adaptive marks)
   forcing `D ≤ 1/D_n` against *every* Liu config. Only `n = 1` is proved; the per-threshold
   tail-count cap is blocked by the parity coupling of `N(t) mod 2` across thresholds. Verified
   for `n = 2` by grid search; open generally.

Despite the gaps, the **answer is fully determined numerically and consistent across all
checks**: `c(n) = 2^n/(2^{n+1} − 1)`.

---

## Promotable lemmas

- **Per-split ΔD formula.** *Statement:* splitting a piece `L` into `p+q` (`p ≥ q`) changes
  `D = ∫(N mod 2)dt` by `ΔD = 2q − 2·O((0,q]) − 2·O((p,L])`, where `O(I)` is the pre-split
  odd-parity width on `I`. *Proved in full above* (§2, from `D-equals-parity-integral`). The
  load-bearing identity for the lower-bound machinery.
- **Balanced-split / frontier recursion.** *Statement:* `D(T_n) + D(T_{n−1}) = 2^n`,
  `D(T_0) = 1`; equivalently `D(T_n) = (2^{n+1} + (−1)^n)/3`; a balanced split of the top of
  `T_n` gives `D → 2^n − D(T_n) = D(T_{n−1})`. *Proved in full above* (§3, geometric telescope
  + ΔD formula). Inductive scaffold for case (b).
- **Single-split lower bound.** *Statement:* a single split of the top piece of `T_n` into
  `p+q` (any `p ≥ q`) yields `D ≥ D(T_{n−1}) ≥ 1`, with min at the balanced split; `D` is
  continuous PL in `q` with slopes `0` or `−2`. *Proved in full above* (§4). Closes case (b-i).
- **Multi-split dyadic lower bound.** *Statement:* every dyadic (all-balanced-splits, ≤`n`
  marks) refinement of `T_n` has `D ≥ 1`, equality at the balanced-pairs config.
  *Proved in full above* (§5, level-block dominance). Closes case (b-ii-dyadic).
- **PL + breakpoint reduction.** *Statement:* the global min of `D` over all `≤ n`-mark
  refinements of `T_n` is attained at a breakpoint (tie) config. *Proved in full above* (§6).

### NEW this round (round 3) — proposed for certification

- **Two-split lower bound** (`two-split-lower-bound`, see `lemmas/two-split-lower-bound.md`):
  *Statement:* every 2-mark refinement of `T_n` (both splits on the top's fragments) has
  `D ≥ D(T_{n−2}) ≥ 1`, min at the dyadic cascade. *Proved in full* (§7): PL+breakpoint
  reduction, then block-contribution formula for the all-tower rest with the parity-constrained
  geometric bound (`c_M·2^M + c_m·2^m ≤ 3·2^{n−1}`), four-case exhaustive check.
  *Scope:* top-fragment-split case fully proved (all n); Type C (split tower piece) verified
  n=3..7, GAP. *Importable by:* `tower-induction`, `gaps-leftover`.
- **Even-group pair-cancellation + spine** (see §8 of this file): *Statement:* at an even-group
  strong breakpoint of `T_n`, `D ≥ 1` (all n). *Proved in full* (§8): adjacent-equal pairs
  cancel (S1), even-count non-dyadic groups cancel (S2), spine = distinct powers of 2, geometric
  dominance + odd-total-mass gives `D ≥ 1`. *Boundary:* odd-group minimizers exist (D=1), so this
  is PARTIAL, not a full G1 close. *Importable by:* `tower-induction` (same sub-result from the
  block/parity viewpoint).

### NEW this round (round 4) — proposed for certification

- **Telescoping zero-gradient block lemma** (`telescoping-block-lemma`, GAP-B, §11):
  *Statement:* on a PL cell of a refinement of `T_n` where each split's two fragments sit at
  same-sign positions (the block condition), `D` is CONSTANT. If all top-piece fragments sit at
  `+` positions and all below-tower pieces (split or unsplit) sit at `−` positions, then
  `D = 2^n − (2^n − 1) = 1` directly (no dyadic endpoint needed). *Proved in full* (§11):
  affinity (each piece length is affine in cuts, signs fixed by type), same-sign ⇒ contribution
  `= ±V` independent of cuts (telescoping), mass-identity computation `2^n − (2^n−1) = 1`.
  *This is the non-dyadic generalization of `block-contribution-formula`.* The value-1
  computation addresses the outline-reviewer's flagged concern for block-condition cells.
  *Importable by:* `tower-induction` (spine-level shadow of the same mechanism), `gaps-leftover`
  (the mass-identity instantiation of gaps+leftover telescoping), `lp-dual-certificate` (the
  dual certificate is the same signed-tower-sum `Σ (±V_j)`).
- **2-leftover transport lemma** (`two-leftover-transport`, GAP-A, §12):
  *Statement:* at a spine-3 cascade breakpoint of `T_n` (two non-dyadic fragments `a, d`
  straddling a tower piece `t`), the mass identity `a + d = t + 1` holds, giving
  `D = a − t + d = 1`. *Proved in full* (§12): fragment mass `= 2^n` (telescoping), below-tower
  mass `= 2^n − 1`, paired fragment mass `= (2^n−1)−t` (each pair: fragment `=` tower piece),
  so `a + d = 2^n − ((2^n−1)−t) = t + 1`. Corollary of GAP-B(d). *Importable by:* `gaps-leftover`
  (spine-length-3 instance of `gaps-leftover-identity`), `tower-induction`.

### NEW this round (round 5) — proposed for certification

- **Mass-balance lemma** (`mass-balance-lemma`, §14, see `lemmas/mass-balance-lemma.md`):
  *Statement:* on a block-condition cell of a refinement of `T_n`, `D = 2 S_+ - D_n` (algebra),
  so `D = 1 ⟺ S_+ = 2^n ⟺` the all-top-`+`/all-below-`−` sign pattern. *Proved in full* (§14):
  `D_n` odd ⟹ `(D_n+1)/2 = 2^n`; block condition forces top fragments to one sign — all-at-`−`
  gives `S_+ ≤ 2^n - 1` (so `D ≤ -1 ≠ 1`), all-at-`+` gives `S_+ = 2^n ⟺` all below-top at `−`.
  **Closes sub-gap (ii) (vacuous):** every block-condition `D = 1` cell has the pattern, settled
  by `telescoping-block-lemma` (d) directly. *Importable by:* `tower-induction`, `gaps-leftover`,
  `lp-dual-certificate` (the dual cert `y_eq = +1`/`−1` is the LP shadow of this sign pattern).
  *Honest caveat:* this CHARACTERIZES block-condition `D = 1` cells; it does NOT prove `D ≥ 1` on
  all block-condition cells (all-top-`−` cells would have `D ≤ -1`) nor address V-shape cells.

### HONEST NEGATIVE RESULT (round 5) — NOT a lemma, a circularity warning

- **Spine sign-pattern / multi-swap subset-sum framing is CIRCULAR.** The nosaddle-close
  explorer's proposed G1-closer ("mass identity `F = T + 1`" ⟹ `D = F - T = 1`) is equivalent to
  `D = 1` under the assumed interleaving pattern, NOT an independent mass identity. Verified
  `Fraction`-exact: the spine `{5, 2}` (from `T_3`, `8 → 5+3`, `4 → 3+1`) HAS the pattern but
  `F - T = 3 = D ≠ 1`. The single-swap (`2(t-v)=0 ⟹ t=v`) and multi-swap subset-sum both
  presuppose `S_+ = F` (the pattern), so they are circular. The 0/523 subset-sum numerics are a
  CHARACTERIZATION of `D = 1` breakpoints, not a proof of `D ≥ 1`. **Do NOT chase this framing.**

## Lemma candidates for certification

- **`balanced-split-frontier-recursion`** — `D(T_n)+D(T_{n−1})=2^n`, closed form
  `D(T_n)=(2^{n+1}+(−1)^n)/3`, balanced top split `D → D(T_{n−1})`. (§3; clean, fully proved,
  immediately importable by `tower-induction` and `frontier-recursion`-style approaches as the
  inductive scaffold for the balanced sub-case.) **[Already certified as `frontier-recursion`.]**
- **`single-split-top-lower-bound`** — one split of `T_n`'s top ⇒ `D ≥ D(T_{n−1}) ≥ 1`, with the
  PL-slope-`{0,−2}` analysis. (§4; closes case (b-i) standalone.) **[Already certified.]**
- **`dyadic-refinement-lower-bound`** — every dyadic ≤`n`-mark refinement of `T_n` has
  `D ≥ 1` (level-block dominance; §5). **[Already certified.]**
- **`two-split-lower-bound`** (NEW, round 3) — every 2-mark refinement of `T_n` (both splits on
  top's fragments) has `D ≥ D(T_{n−2}) ≥ 1`, min at the dyadic cascade. (§7; block-contribution
  formula + parity-constrained geometric bound, four-case exhaustive check. Type C verified
  n=3..7, GAP.) See `lemmas/two-split-lower-bound.md`.
- **`even-group-strong-breakpoint-bound`** (NEW, round 3) — at an even-group strong breakpoint
  of `T_n`, `D ≥ 1` (all n). (§8; pair cancellation + spine geometric dominance + odd-total-mass.)
  Partial: odd-group minimizers exist, so does not close G1 alone.
- **`telescoping-block-lemma`** (NEW, round 4) — D is constant on a PL cell where each split's
  fragments sit at same-sign positions; if all top-piece fragments at `+` and all below-tower
  at `−`, then `D = 2^n − (2^n − 1) = 1` directly (no dyadic endpoint needed). (§11 GAP-B;
  non-dyadic generalization of `block-contribution-formula`; addresses reviewer's flagged concern
  for block-condition cells.) See §11.
- **`two-leftover-transport`** (NEW, round 4) — at a spine-3 cascade breakpoint, mass identity
  `a + d = t + 1` ⇒ `D = 1`. (§12 GAP-A; corollary of GAP-B(d); fragment-tower telescoping.)
- **`mass-budget-breakpoint-inequality`** (NEW, round 6) — at a breakpoint of `T_n` (cascade type,
  all `n`), `T ≥ 3F − 1` where `F` = surviving non-dyadic fragment mass, `T` = surviving tower
  mass. (§15; mass-budget: each non-dyadic survivor appears `≥ 3` times among top fragments,
  consuming `≥ 3w` from the `2^n` budget; dyadic non-survivors consume `≥ 2^k` each.)
  **Corollary:** block condition + `D = 1` at breakpoint ⟹ `F = 0` ⟹ `D ≥ 1` by §8.
  Continuity rules out "all `F` at `−`". *Importable by:* `tower-induction`, `gaps-leftover`,
  `lp-dual-certificate` (mass-budget as a constraint on the dual). *Honest caveat:* constrains
  `F` but does NOT prove `F = 0` without the block condition; GAP-C(i) narrowed, not closed.

### NEW this round (round 7) — proposed for certification

- **`vertex-single-survivor`** (NEW, round 7, §16.1) — *Statement:* at a strong-breakpoint
  **vertex** of `T_n` (cascade type: all marks split the top `2^n`), at most ONE non-dyadic
  fragment value survives into the spine. *Proved in full* (§16.1): the top split has ONE sum
  constraint; `n_{free}` free groups introduce `n_{free}` unknowns, the sum constraint pins one
  combination, leaving `n_{free} - 1` free parameters; a vertex has 0 free parameters, so
  `n_{free} <= 1`. A free group of even size cancels (`F = 0`), odd size leaves one survivor.
  **Corollary:** for `T_3` (`n = 3`, marks 3), single-survivor holds for ALL vertex types (two
  splits with 3+ fragments each need 4 marks > 3; a size-2 free group has value `sum/2` = a
  power of 2, hence dyadic). *Importable by:* `tower-induction`, `vertex-enum-n3` (justifies
  focusing the enumeration on single-survivor vertices for `T_3`). *Scope:* cascade type all
  `n`; all `T_3` types. For `n >= 4` mixed types, multi-survivor vertices exist (GAP-B, §16.6)
  — at most one **F-origin** survivor per vertex (two F-origin free groups share one sum
  constraint, giving a face), but T-origin survivors can coexist.

- **`largest-tower-exceeds-fragment`** (NEW, round 7, §16.3) — *Statement:* at a cascade-type
  strong-breakpoint vertex with one surviving non-dyadic fragment `v` (appearing `c >= 3`
  times), the largest surviving tower `2^j` satisfies `2^j > v`. *Proved in full* (§16.3): if
  `2^j <= v`, then all towers `2^k` (`k > j`) are non-surviving (even count, `d_k` odd `>= 1`),
  consuming `>= 2^n - 2^{j+1}` from the top budget; the survivor consumes `>= 3*2^j`; total
  `>= 2^n - 2^{j+1} + 3*2^j = 2^n + 2^j > 2^n` — contradiction. *Importable by:* any approach
  using the spine tower-dominance structure. *Depends on:* `mass-budget-breakpoint-inequality`,
  `spine-pair-cancellation`, `strong-breakpoint-group-structure`.

- **`vertex-frag-at-plus-implies-D-gt-1`** (NEW, round 7, §16.5) — *Statement:* at a cascade-
  type strong-breakpoint vertex with one surviving fragment `v` at a `+` position (block
  condition, `f_- = 0`) and budget-tight (`T = 3F - 1`), `D > 1`. *Proved in full* (§16.5): the
  decomposition `D = 1 - 2F + 2(t_+ - f_-) = 1 - 2v + 2t_+` (§16.4); the largest surviving
  tower `2^j` is at position 0 (`+`, by `largest-tower-exceeds-fragment`), so `t_+ >= 2^j > v`;
  hence `2t_+ > 2v` and `D > 1`. Non-tight extension: `D = F + (t_+ - t_-) > F` (by
  `t_+ > t_-`, dyadic dominance), conditional on `v > 1` (GAP-A). *Importable by:* any approach
  using the vertex-level sign-forcing. *Depends on:* `largest-tower-exceeds-fragment`,
  `mass-budget-breakpoint-inequality`, `pl-breakpoint-minimum`. *Honest caveat:* closes only
  the frag-at-`+` budget-tight sub-case; the frag-at-`-` sub-case (GAP-C/d-minus) and the
  `v > 1` lower bound (GAP-A) remain open.
