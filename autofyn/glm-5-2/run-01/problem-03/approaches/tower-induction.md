# imo-2026-03 — approach `tower-induction`

Dyadic tower resists refinement (lower bound) + the **frontier recursion** as the
lower-bound engine + the **spine sign-bookkeeping** extension toward non-dyadic
fragments (Route D) + a dominance case split (upper bound, fallback). Main line.

**Conjectured answer (verified n=1,2,3,4):**

$$c(n) \;=\; \frac{2^{n}}{2^{\,n+1}-1} \;=\; \frac{1}{2-2^{-n}}.$$

| n | c(n) | decimal |
|---|------|---------|
| 1 | 2/3  | 0.6667  |
| 2 | 4/7  | 0.5714  |
| 3 | 8/15 | 0.5333  |
| 4 | 16/31| 0.5161  |

Verification: `(1+1/D_n)/2 = (D_n+1)/(2D_n) = 2^{n+1}/(2D_n) = 2^n/D_n` with
`D_n=2^{n+1}-1` (checked exactly for n=1,2,3,4 by substitution; certified lemma
`closed-form-answer.md`).

Throughout, **tower units** mean we rescale so the tower is `(2^n,2^{n-1},...,1)` with
total `D_n=2^{n+1}-1`; one tower unit `= 1/D_n` in real (stick-length) units. The
target `D \ge 1/D_n` (real) is `D \ge 1` (tower units), and `c=2^n/D_n` (real) is
"odd-index `= 2^n`" (tower units).

---

## Status

partial

## Approaches tried

- `tower-induction` (round 1) — Lemma 0 (greedy = odd-index) proved in full; lower-bound base n=1 and case (a) [top unsplit] proved in full via a clean `D = A - D(R')` identity that needs no IH; case (b) [top split] reduced to an interleaving crux, the equal-split sub-case closed by IH, the general sub-case left as an explicit gap; upper bound n=1 base proved in full, general induction set up, non-dominant case and the dominant recurrence left as explicit gaps.
- `tower-induction` (round 2) — **frontier recursion installed as the lower-bound engine.** Replaced the dead self-similar IH (wrong-direction parity bug, round 1) with the parity-block formula: for any *balanced* (dyadic) refinement of `T_n`, the alternating sum `D` depends only on the split-parity vector `e=(e_1,\dots,e_n)` and obeys the two recursions `D_n(e,e_n=0)=2^n-D_{n-1}(e)` (top unsplit) and `D_n(e,e_n=1)=D_{n-1}(e)` (top balanced-split). Induction gives **`1 \le D_n(e) \le 2^n-1` for every parity vector**, hence **every balanced-split refinement of `T_n` has `D\ge 1` (tower units)**, with equality at the fully-cascaded all-1's config. This RIGOROUSLY closes the all-balanced-splits sub-case of case (b) for all `n` (no IH, no numerics-as-proof). The unbalanced-split sub-case (Xiang splits `2^k\to p+q` with `p\ne q`) is the remaining **G2 gap** (shared wall with `tail-count`'s non-dyadic-breakpoint gap). Upper bound: `n=1` proven; general `n` OPEN and kept as a fallback (the primary upper-bound attack is `majorization-upper`); the dominant factorization and the three-regime picture are stated honestly with the below-threshold gap flagged.
- `tower-induction` (round 3) — **spine sign-bookkeeping extension (Route D).** Generalized the pair-cancellation idea (sign-AGNOSTIC, value-independent) to a spine decomposition valid for ANY refined config (dyadic or not): remove all adjacent-equal pairs; the remaining **spine** is strictly-decreasing DISTINCT values (powers of 2 + possibly non-dyadic leftovers), and `D(\text{config})=D(\text{spine})` (Lemma S1, proved). At a **strong breakpoint** (every fragment ties an adjacent piece — the structural condition certified via `pl-breakpoint-minimum`), non-dyadic fragments cannot tie a tower piece (tower pieces are powers of 2) so they form adjacent-equal GROUPS (Lemma S2, proved). Even-count non-dyadic groups fully cancel, so the spine is purely distinct powers of 2; the geometric bound (largest power `2^{k_1}` strictly exceeds the sum `2^{k_1}-1` of all smaller distinct powers) PLUS the nonempty argument (total mass `D_n` is ODD while removed pairs contribute EVEN mass, so the spine mass is odd `\ge 1`, hence nonempty) give **`D(\text{spine})\ge 1`** (Lemma S3, proved). **This closes G1 for even-group strong breakpoints** — a clean, certifiable, INDEPENDENT sub-result derived from the block/spine viewpoint (the block/parity counterpart of tail-count's even-group pair-cancellation, derived here from the sign-agnostic spine decomposition). The **odd-count case is the honest GAP (G2-odd)**: a non-dyadic leftover's sign depends on its GLOBAL position in the spine (witness `{4.75,4,0.25}` `D=1` with both leftovers at `+`; witness `{4,7/3,2}` `D=11/3` with the leftover at `-`), so no uniform "leftover contributes `+`" rule exists. The frontier recursion `D_n(\bar e,0)=2^n-D_{n-1}`, `D_n(\bar e,1)=D_{n-1}` does NOT extend to non-dyadic splits: its clean cancel/flip dichotomy is load-bearing on the balanced split producing TWO EQUAL fragments at adjacent positions (1,2) that cancel, whereas an unbalanced split produces UNEQUAL fragments that interleave with tower pieces and break block-contiguity; the single-split escape uses PL analysis (one variable, certified `single-split-top-lower-bound`), but multi-split compounds (the V-shape, round-2 rule). The odd-count spine bound tied to the splitting-tree origin of each leftover is the candidate mechanism but is NOT evident; left as the open G2-odd. Upper bound unchanged (fallback; primary attack is `majorization-upper`).

## Current best

Proved and certified (importable from `results/imo-2026-03/lemmas/` — 13 lemmas):
1. **Lemma 0** (`claim-game-odd-index.md`) — claim game value = odd-index sum; greedy optimal.
2. **Lower bound case (a)** (`tower-top-unsplit.md`) — tower resists refinement with top unsplit, all `n`, no IH.
3. **n=1 base** (`n1-base-both-bounds.md`) — `c(1)=2/3`.
4. **Layer-cake / D-integral / closed form** — certified.
5. **Block-contribution formula** (`block-contribution-formula.md`) — dyadic `D=\sum_k 2^k(-1)^{C_k}(n_k\bmod 2)`.
6. **Frontier recursion** (`frontier-recursion.md`) — `D_n(\bar e,0)=2^n-D_{n-1}(\bar e)`, `D_n(\bar e,1)=D_{n-1}(\bar e)`, `D_0=1`.
7. **Dyadic-refinement lower bound** (`dyadic-refinement-lower-bound.md`) — `1\le D\le 2^n-1` for every balanced refinement of `T_n`, all `n`. Closes all-balanced-splits sub-case of case (b).
8. **Single-split top lower bound** (`single-split-top-lower-bound.md`) — `D\ge D(T_{n-1})\ge 1`, all `n`. Closes case (b-i).
9. **PL breakpoint minimum** (`pl-breakpoint-minimum.md`) — global min of `D` at a breakpoint (tie) config.
10. **Parallel-halving saturates tower / n=2 upper bound** — certified.

Proved in THIS round (this file, candidates for certification):
11. **Lemma S1 (pair-cancellation, sign-agnostic)** — for ANY refined config, removing all adjacent-equal pairs preserves `D`; the remaining **spine** is strictly-decreasing and `D(\text{config})=D(\text{spine})`.
12. **Lemma S2 (strong-breakpoint group structure)** — at a strong breakpoint, non-dyadic fragments form adjacent-equal groups (size `\ge 2`); even-count groups fully cancel into the spine.
13. **Lemma S3 (even-group spine dominance)** — if every non-dyadic group is even, the spine is a nonempty strictly-decreasing sequence of distinct powers of 2, and `D(\text{spine})\ge 1` (geometric bound `2^{k_1}>2^{k_1}-1\ge` sum of all smaller; nonempty via odd-total-mass). **Closes G1 for even-group strong breakpoints**, all `n`.

Open gaps:
- **G2-odd (lower bound, non-dyadic odd-count leftovers):** when a non-dyadic group has odd count `\ge 3`, one leftover survives into the spine. Its sign (position parity in the spine) is GLOBAL (witnesses: `{4.75,4,0.25}` `D=1`, both leftovers at `+`; `{4,7/3,2}` `D=11/3`, leftover at `-`). The frontier recursion does NOT extend (block-contiguity load-bearing). Odd-count MINIMIZERS exist (`D=1`, e.g. `{4.75,4,2,2,1,1,0.25}`), so the bound must be tight to 1. A sign-bookkeeping argument tied to the splitting-tree origin of each leftover is the candidate mechanism but is NOT proved. **This is the block/parity counterpart of tail-count's plateau wall (same G1, opposite machinery).**
- **U1, U2 (upper bound, general `n`):** dominant-case recurrence does not factor through `c(n-1)`; below-threshold regime (cases C/B2) for `n\ge 3` open. Deferred to `majorization-upper`.

## Full proof

Not complete (gaps G2-odd, U1, U2 below). The proved portions are written out rigorously.

---

### Lemma 0 (claim game = odd-index sum; greedy is optimal)

Imported verbatim from the certified lemma `claim-game-odd-index.md` (proved by
backward induction on `|S|`, every parity case settled). We use only its **corollary**:

$$c(n) \;=\; \frac{1+D^*}{2}, \qquad D^* \;=\; \max_{\text{Liu }\le n\text{ marks}}\;\min_{\text{Xiang }\le n\text{ marks}}\; D(\text{sorted refined multiset}),$$

where `D=a_1-a_2+a_3-\cdots` is the alternating (signed) sum of the sorted-descending
final multiset. The target `c(n)=2^n/D_n` is `D^*=1/D_n`. Xiang's marks refine Liu's
pieces (split each into subpieces) and re-sort descending.

---

### Lower bound: Liu plays the dyadic tower

**Liu's strategy.** Liu marks at cumulative sums `(2^k-1)/D_n` for `k=1,\dots,n`,
producing the **tower**

$$T_n \;=\; (2^n,\,2^{n-1},\,\dots,\,2,\,1)\,/\,D_n, \qquad D_n = 2^{n+1}-1.$$

Structural facts: (i) `2^n > 2^n-1 =` (sum of all smaller tower pieces) — the *only*
dominance fact used by case (a); (ii) the rest `(2^{n-1},\dots,1)` rescaled to total 1 is
exactly `T_{n-1}` with denominator `D_{n-1}=2^n-1` — self-similarity; (iii) every piece is
a power of 2 — the entry point of the frontier machinery.

**Theorem L (lower bound).** *For the tower `T_n`, every Xiang refinement using `\le n`
marks leaves `D\ge 1/D_n` (Liu's take `\ge 2^n/D_n`).*

We prove the base case, case (a) (top unsplit), the all-balanced-splits sub-case of case
(b), the single-split sub-case of case (b), and the **even-group strong-breakpoint
sub-case** of the non-dyadic multi-split case (b-ii), all in full. The **odd-count
non-dyadic** sub-case is the open gap G2-odd.

#### Base `n=1`

Certified (`n1-base-both-bounds.md`): `c(1)=2/3`. ∎ base.

#### Case (a): Xiang leaves the top piece unsplit

Certified (`tower-top-unsplit.md`): uses only `D(R')\le\text{total}(R')=(2^n-1)/D_n` and
`D(M)=A-D(R')` (top piece `A=2^n/D_n` strictly largest, occupies position 1), giving
`D(M)\ge A-\text{total}(R')=1/D_n` for all `n` at once, no IH. ∎ case (a)

#### Case (b-i): Xiang makes exactly one split of the top

Certified (`single-split-top-lower-bound.md`): `D` is continuous PL in the cut `q` with
slopes in `\{0,-2\}` (non-increasing), the minimum is on the plateau
`q\in[2^{n-2},2^{n-1}]` at value `D(T_{n-1})\ge 1` (`frontier-recursion` closed form),
all `n`, dyadic AND non-dyadic single splits. ∎ case (b-i)

#### Case (b-ii-dyadic): all balanced splits — the frontier machinery

Closed in full for all `n` by the frontier recursion (Lemmas F-block, F-rec, F-min —
certified `block-contribution-formula`, `frontier-recursion`,
`dyadic-refinement-lower-bound`). We record the statements for reference; full proofs are
in the certified lemma files.

**Lemma F-block (block-contribution formula, certified).** *Let `M` be a dyadic
(balanced-split) refinement of `T_n`. Let `n_k` = number of pieces of value `2^k`
(`k=0,\dots,n`) and `C_k:=\sum_{j>k}n_j`. Then `D(M)=\sum_{k=0}^{n} 2^k(-1)^{C_k}(n_k\bmod 2)`.
In particular `D(M)` depends only on the split-parity vector `e_k:=c_k\bmod 2` (`e_0=0`
fixed).*

**Lemma F-rec (frontier recursion, certified).** *`D_n(\bar e,0)=2^n-D_{n-1}(\bar e)`,
`D_n(\bar e,1)=D_{n-1}(\bar e)`, `D_0=1`. The unsplit-tower identity `D(T_m)=2^m-D(T_{m-1})`
is the case `e\equiv 0`; the closed form `D(T_m)=(2^{m+1}+(-1)^m)/3\ge 1` follows.*

**Lemma F-min (min-balanced-frontier `=1`, certified).** *For every parity vector
`e\in\{0,1\}^n` (`n\ge 1`), `1\le D_n(e)\le 2^n-1`. Hence every balanced-split refinement
`M` of `T_n` has `D(M)\ge 1=1/D_n` (tower units), with equality at the fully-cascaded
all-1's refinement `e=(1,\dots,1)`.*

**Conclusion of the balanced sub-case.** If Xiang refines `T_n` using only balanced
splits, Lemma F-min gives `D\ge 1/D_n`. ∎ case (b-ii-dyadic)

---

#### Case (b-ii), non-dyadic multi-split — spine sign-bookkeeping (Route D, NEW round 3)

We develop a **spine decomposition** that applies to ANY refined config (dyadic or not),
and prove `D\ge 1` for the structural class of **even-group strong breakpoints**. The
odd-count case is the honest GAP (G2-odd).

**Setup.** Xiang makes at least one **unbalanced** split `2^k\to p+q` with `p\ne q`
(`p+q=2^k`, `p>q`). The resulting multiset is no longer dyadic, so the block formula
(Lemma F-block) does not apply directly. The certified reduction
(`pl-breakpoint-minimum`) constrains Xiang's optimum to a **breakpoint (tie) config** — a
vertex of the PL structure of `D` in the split positions. We attack the breakpoint configs
via the spine.

---

**Lemma S1 (pair-cancellation, sign-agnostic).** *Let `M=(a_1\ge a_2\ge\cdots\ge a_m)` be
any sorted-descending multiset (dyadic or not). If `a_i=a_{i+1}` for some `i`, the pair
`(a_i,a_{i+1})` contributes*

$$(-1)^{i+1}a_i + (-1)^{i+2}a_{i+1} \;=\; (-1)^{i+1}(a_i - a_{i+1}) \;=\; 0.$$

*Removing the pair `(a_i,a_{i+1})` from `M` shifts every later piece's position by `2`,
leaving its sign `(-1)^{(\text{new pos})+1}=(-1)^{(\text{old pos})+1+2}=(-1)^{(\text{old
pos})+1}` UNCHANGED. Hence the alternating sum of the pair-removed multiset equals that of
`M`. Iterating until NO adjacent-equal pair remains yields the **spine**
`\operatorname{sp}(M)`: a strictly-decreasing sequence of DISTINCT values (some powers of
2, possibly some non-dyadic leftovers), with*

$$D(M) \;=\; D(\operatorname{sp}(M)).$$

*Proof.* The pair's contribution is zero as shown. After removal, every surviving piece at
old position `j>i+1` moves to new position `j-2`; its sign
`(-1)^{(j-2)+1}=(-1)^{j-1}=(-1)^{j+1}` (since `j-1\equiv j+1\pmod 2`) is unchanged.
Iterating (the process terminates: the multiset is finite, and each removal strictly
decreases its size), we reach a strictly-decreasing spine with `D` preserved. ∎

(Computational countercheck: 20 000 random configs with forced duplicates, 0 mismatches
between `D(M)` and `D(\operatorname{sp}(M))`.)

**Remark.** Lemma S1 is value-AGNOSTIC — it needs no power-of-2 structure. This is the
entry point that generalizes the block formula's "within-block pairs cancel" (which
requires dyadic contiguity) to arbitrary configs.

---

**Lemma S2 (strong-breakpoint group structure).** *Recall (`pl-breakpoint-minimum`) that a
**strong breakpoint** is a refined config in which every fragment (every split-product
piece) ties an adjacent piece in the sorted order. At a strong breakpoint of a refinement
of `T_n`:*

*(i) every DYADIC fragment (a power of 2) ties another dyadic fragment of the same value
(there are at least two copies of every value that appears, since the tower starts with
one copy of each `2^k` and a fragment of value `2^k` either is an unsplit tower piece
paired with an extracted copy, or is one of a balanced-split pair);*

*(ii) every NON-dyadic fragment (value `\ne 2^k`) cannot tie a tower piece (all tower
pieces are powers of 2 and the fragment's value is not), so it must tie ANOTHER non-dyadic
fragment of the SAME value. Consequently the non-dyadic fragments partition into
adjacent-equal GROUPS of size `\ge 2` in the sorted order.*

*Proof.* (i) A dyadic fragment of value `2^k` at a strong breakpoint ties an adjacent
piece of the same value `2^k`; that adjacent piece is itself dyadic. (ii) A non-dyadic
fragment has value `v\notin\{2^k\}`; every tower piece has value in `\{2^k\}`, so `v`
cannot equal any tower piece, hence the fragment's adjacent tie (guaranteed by the strong-
breakpoint hypothesis) must be to another non-dyadic fragment of value `v`. Grouping
adjacent-equal non-dyadic fragments gives groups of size `\ge 2`. ∎

**Corollary S2.** *At a strong breakpoint, an EVEN-count non-dyadic group (size `2r`)
fully cancels: it is `r` adjacent-equal pairs, each contributing `0` by Lemma S1. An
ODD-count group (size `2r+1\ge 3`) leaves exactly ONE leftover of value `v` in the spine.*

---

**Lemma S3 (even-group spine dominance).** *Let `M` be a strong-breakpoint refinement of
`T_n` in which every non-dyadic group has EVEN count. Then the spine
`\operatorname{sp}(M)` is a nonempty strictly-decreasing sequence of distinct powers of
2, and*

$$D(M) \;=\; D(\operatorname{sp}(M)) \;\ge\; 1 \qquad(\text{tower units } = 1/D_n
\text{ real}).$$

*Proof.* **Spine is distinct powers of 2.** By Corollary S2, every even-count non-dyadic
group cancels fully. By Lemma S2(i), the dyadic fragments pair off (each value `2^k` that
survives into the spine is unpaired — appears an odd number of times). The remaining
spine values are exactly the values `2^k` appearing an odd number of times in `M`, each
once — a strictly-decreasing sequence of distinct powers of 2. Write them
`2^{k_1}>2^{k_2}>\cdots>2^{k_s}` with `k_1>k_2>\cdots>k_s\ge 0`.

**Geometric bound.** The alternating sum is
`D=2^{k_1}-2^{k_2}+2^{k_3}-\cdots+(-1)^{s+1}2^{k_s}`. The negative terms are a subset of
`\{2^{k_2},2^{k_3},\dots,2^{k_s}\}`, whose sum is at most the sum of ALL distinct powers
of 2 strictly below `2^{k_1}`, i.e. at most `2^{k_1}-1` (geometric series
`1+2+\cdots+2^{k_1-1}=2^{k_1}-1`). The positive terms beyond the first are also a subset
of the smaller powers, so they only help. Hence

$$D \;\ge\; 2^{k_1} - (2^{k_1}-1) \;=\; 1.$$

More carefully: `D = 2^{k_1} - \bigl[(\text{sum of negative terms}) - (\text{sum of
positive smaller terms})\bigr]`. The bracketed quantity is the alternating sum of the
smaller powers starting with a minus, which is at most the sum of all smaller powers (each
term is bounded by the running total in absolute value, or simply:
`|D(\text{smaller})|\le\sum\text{smaller}\le 2^{k_1}-1`). Thus `D\ge 2^{k_1}-(2^{k_1}-1)=1`.

**Nonempty.** The total mass of `M` is `D_n=2^{n+1}-1` (ODD). Each removed adjacent-equal
pair contributes mass `2v` (EVEN). So the spine's total mass is `D_n-(\text{even})`,
which is ODD, hence `\ge 1` — the spine is nonempty. (Equivalently: a nonempty sequence
of distinct powers of 2 has odd sum iff `2^0=1` is among them, so the spine contains the
value `1`.) ∎

(Computational countercheck: all `2^{7}-1=127` nonempty strictly-decreasing subsequences of
`{1,2,\dots,64}` have `D\ge 1`, min `=1` at the spine `\{2,1\}` or `\{1\}`.)

**Conclusion of the even-group strong-breakpoint sub-case.** If Xiang's optimum (a
breakpoint config per `pl-breakpoint-minimum`) is a strong breakpoint with all non-dyadic
groups even, Lemma S3 gives `D\ge 1/D_n`. ∎ (even-group strong-breakpoint sub-case)

---

**GAP G2-odd (odd-count non-dyadic leftovers).** When some non-dyadic group has odd
count `\ge 3`, exactly one leftover of that value survives into the spine. The spine is
now a strictly-decreasing mix of powers of 2 and non-dyadic leftovers, and the geometric
dominance of Lemma S3 FAILS (a leftover need not exceed the sum of smaller powers; e.g.
the leftover `4.75<2\cdot 4=8`). The sign of a leftover's contribution is its position
parity in the spine, which is a GLOBAL property:

- **Witness A (both leftovers at `+`, `D=1`, a MINIMIZER):** `T_3`, splits
  `8\to 4.75+3.25`, `3.25\to 2+1.25`, `1.25\to 1+0.25`. Config
  `\{4.75,4,2,2,1,1,0.25\}`. Pairs `\{2,2\},\{1,1\}` cancel; spine
  `\{4.75,4,0.25\}`. `D=4.75-4+0.25=1`. Both leftovers (`4.75` at pos 1, `0.25` at pos 3)
  are at `+` positions; they straddle the tower piece `4` and sum to `5>4`, surplus
  `=1`.
- **Witness B (leftover at `-`, `D=11/3>1`):** spine `\{4,7/3,2\}`. The leftover `7/3`
  sits between tower pieces `4,2` at `-` (pos 2); `D=4-7/3+2=11/3`.
- **Odd-group MINIMIZERS exist** (321 of them for `T_3` 3-split at `D=1`, per
  `math-explorer-lower-nondyadic`): the pair-cancellation / spine-geometric argument is
  INSUFFICIENT to close G1 — odd-count configs can be the global minimizer.

**Why the frontier recursion does not extend.** The recursion
`D_n(\bar e,0)=2^n-D_{n-1}(\bar e)`, `D_n(\bar e,1)=D_{n-1}(\bar e)` is load-bearing on
the **balanced** split `2^n\to 2^{n-1}+2^{n-1}` producing TWO EQUAL fragments at adjacent
positions `(1,2)` that cancel (the `e_n=1` branch), or leaving `2^n` alone at position 1
with the rest's signs flipping (the `e_n=0` branch). An **unbalanced** split
`2^n\to p+q` (`p>q`) produces UNEQUAL fragments: `p` occupies position 1 alone, while `q`
interleaves with the tower pieces `\{2^{n-1},\dots,1\}` at a position depending on `q`'s
value — there is no clean "cancel or flip" dichotomy, and the block-contiguity (all
pieces of value `2^k` forming one contiguous block, required by `block-contribution-formula`)
is destroyed. The single-split escape works because `D` is PL in ONE variable `q`
(`single-split-top-lower-bound`), but multi-split compounds: the second split's `D` is
V-shaped (not monotone) after an unbalanced first split (round-2 rule, witness `T_3`
`8\to 5+3` then `5\to(5-q)+q`: `q=1\Rightarrow D=1`, `q=2\Rightarrow D=3`,
`q=2.5\Rightarrow D=2`; rebalancing INCREASES `D`).

**Candidate mechanism (NOT proved).** The non-dyadic leftovers arise from
splitting-tree "ends" (the largest fragment of a split chain, and the cascading residual).
In Witness A, the two leftovers `4.75+0.25=5` straddle tower `4` (since the chain
`8\to 4.75+3.25\to\dots\to 1+0.25` extracts `2+1=3` from `8`, leaving `5` split as
`4.75+0.25`). A sign-bookkeeping argument tying each leftover's sign to its splitting-tree
origin (which fragment spawned which leftover, and the parity of the tower pieces
extracted in between) is the natural block/parity counterpart of tail-count's
plateau-connectivity route, but it is NOT evident — the global parity coupling is exactly
the obstruction. **This is left as the open G2-odd gap.**

---

**Lower-bound conclusion.** `c(n)\ge 2^n/D_n` is proved for: `n=1` (full, certified);
case (a) top-unsplit (all `n`, certified); case (b-i) single-split (all `n`, certified);
the all-balanced-splits sub-case of case (b) (all `n`, certified F-min); and the
**even-group strong-breakpoint** sub-case of the non-dyadic multi-split case (b-ii) (all
`n`, Lemma S3, this round). The remaining gap is **G2-odd**: non-dyadic refinements with
odd-count non-dyadic groups, where the leftover sign-bookkeeping is unproved (verified
`n\le 6`, 0 violations, but NOT proved). This is the same wall `tail-count` hits from the
PL/variational side; the two slugs converge here from opposite machinery (block/spine vs
PL/plateau).

---

### Upper bound: Xiang caps Liu at `2^n/D_n` (FALLBACK; GAP beyond `n=1`)

This section is kept honest and is NOT the primary upper-bound attack (that is
`majorization-upper` this round). `n=1` is proved; general `n` is open.

**Theorem U (upper bound, target).** *For every Liu config (`\le n+1` pieces summing to
1), Xiang has `\le n` marks forcing `D\le 1/D_n` (Liu's take `\le 2^n/D_n`).*

#### Base `n=1` (full, certified)

`c(1)=2/3` (`n1-base-both-bounds.md`). ∎

#### Three-regime picture (explorer B; verified, structural, NOT a proof for `n\ge 2`)

Let `L=a_1` be Liu's largest piece, `a_2` the second-largest, `R=1-L` the rest total,
`D_{n-1}=2^n-1`.

| Regime | Condition | Xiang's first move | After 1 mark | Status |
|---|---|---|---|---|
| **A (full dominant)** | `L\ge 2a_2` AND `L\ge 2^n/D_n` | halve `L` | `D=D(\text{rest})`, `R\le D_{n-1}/D_n` | closes by IH |
| **C (R-too-big)** | `L\ge 2a_2` AND `L<2^n/D_n` | halve `L` | `D=D(\text{rest})`, `R>D_{n-1}/D_n` | **overshoots** |
| **B (non-dominant)** | `L<2a_2` | pair: split `L\to a_2+(L-a_2)` | `D=D(\text{rest}')`, `R'=1-2a_2` | B1 closes if `a_2\ge 2^{n-1}/D_n`; **B2 overshoots** |

The dominant factorization (regime A) is arithmetically exact: under `L\ge 2a_2` the two
halves `L/2,L/2` each `\ge a_2`, occupy positions 1,2 and cancel, so `D(\text{total})
=D(\text{rest})`; under `L\ge 2^n/D_n`, `R=1-L\le(2^n-1)/D_n=D_{n-1}/D_n`, so by the IH
on the `(n-1)`-game (rest rescaled to total 1), `D(\text{rest})\le R\cdot
(1/D_{n-1})\le 1/D_n`. The identity `(2^n-1)/D_{n-1}=1` closes it.

#### Open gaps (upper bound, general `n`)

- **U1 (dominant recurrence).** The factorization closes regime A *conditional on the IH
  for `n-1`*, but the recurrence on the value does not factor cleanly through
  `c(n-1)=2^{n-1}/D_{n-1}`. **Open.**
- **U2 (below-threshold regime, cases C and B2, `n\ge 3`).** When `L<2^n/D_n`, after one
  mark the rest is also below-threshold in the `(n-1)`-game, so the recursion NEVER
  reaches regime A. The IH `D\le R/D_{n-1}` overshoots. A strengthened two-variable IH is
  needed. **Open.** (Deferred to `majorization-upper`.)

**Upper-bound conclusion.** `c(n)\le 2^n/D_n` is proved only for `n=1`. The general
induction is the open wall U1+U2; this slug keeps it as an honest fallback and does not
rival `majorization-upper`.

---

## Gaps

1. **G2-odd (lower bound, non-dyadic odd-count leftovers).** At a strong breakpoint with
   an odd-count non-dyadic group, one leftover survives into the spine. The leftover's
   sign is its global position parity (witnesses: `{4.75,4,0.25}` `D=1` both at `+`;
   `{4,7/3,2}` `D=11/3` at `-`). The frontier recursion does NOT extend (block-contiguity
   load-bearing; the V-shape defeats local rebalancing). Odd-group MINIMIZERS exist
   (`D=1`), so the bound must be tight to 1. A sign-bookkeeping argument tied to the
   splitting-tree origin of each leftover is the candidate mechanism, NOT proved. Shared
   wall with `tail-count`'s non-dyadic-breakpoint gap (opposite machinery). The
   even-group sub-case (Lemma S3) is closed; the odd-count sub-case is the open core of
   G1.

2. **U1 (upper bound, dominant recurrence, `n\ge 2`).** The regime-A factorization is
   exact but conditional on the `(n-1)`-IH; the value recurrence does not factor through
   `c(n-1)`.

3. **U2 (upper bound, below-threshold regime C/B2, `n\ge 3`).** The IH overshoots; a
   strengthened two-variable IH or a majorization argument is required. Deferred to
   `majorization-upper`.

---

## Promotable lemmas

- **Lemma S1 (pair-cancellation, sign-agnostic).** For any sorted-descending multiset
  `M` (dyadic or not), removing all adjacent-equal pairs preserves `D`; the resulting
  strictly-decreasing **spine** satisfies `D(M)=D(\operatorname{sp}(M))`. Value-agnostic
  (needs no power-of-2 structure). Fully proved above (Location: this file, "Lemma S1").
  Candidate for `results/imo-2026-03/lemmas/spine-pair-cancellation.md`.

- **Lemma S2 (strong-breakpoint group structure).** At a strong breakpoint refinement of
  `T_n`, non-dyadic fragments form adjacent-equal groups of size `\ge 2`; even-count
  groups fully cancel (Corollary S2). Fully proved above (Location: this file, "Lemma S2").
  Candidate for `results/imo-2026-03/lemmas/strong-breakpoint-group-structure.md`.

- **Lemma S3 (even-group spine dominance).** At a strong-breakpoint refinement of `T_n`
  with all non-dyadic groups even, the spine is a nonempty strictly-decreasing sequence
  of distinct powers of 2 and `D(\operatorname{sp})\ge 1` (geometric bound `2^{k_1}>2^{k_1}-1\ge`
  sum of smaller; nonempty via odd-total-mass `D_n`). Closes G1 for even-group strong
  breakpoints, all `n`. Fully proved above (Location: this file, "Lemma S3"). Candidate
  for `results/imo-2026-03/lemmas/even-group-spine-lower-bound.md`.

- **Lemma F-block, Lemma F-rec, Lemma F-min** — already certified (round 2); re-listed
  for reference.
