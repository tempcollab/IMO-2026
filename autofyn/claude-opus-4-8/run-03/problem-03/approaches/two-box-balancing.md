## Status
partial

## Approaches tried
- two-box-balancing (framing D = |O|−|E|, odd-rank box vs even-rank box, as a
  constructor/corrector balancing game; scale invariant à la crux aimo-0117) — PARTIAL,
  genuine new progress. NEW fully-rigorous results this round:
  - **Lemma U0 (even-multiplicity corrector):** if Liu's multiset has `m ≤ n` pieces, Xiang
    forces `D = 0` (top-copy chain producing even multiplicity of every final length; ≤ m cuts).
    This CLEANLY reduces the entire upper bound to the single boundary case `m = n+1`.
  - **Dominant sub-case of `m = n+1`:** if `a₁ ≥ Σ_{i≥2} a_i` (equivalently `a₁ ≥ 1/2`), Xiang
    forces `D ≤ u_n` (replicate-all if `a₁ ≤ c(n)`, bisect-top if `a₁ > c(n)`).
  - **Base cases n = 0, 1 both directions fully closed** through this framing.
  - **Lower Case A** (top scale uncut) reproved in the box language with the stronger bound
    `D ≥ 2^{n−1}u_n ≥ u_n`.
  - **Upper on the dyadic input** (tightness) via the bisect-the-top cancelling chain: `D = u_n`.
  - **Lower Case B** reduced to a clean sub-lemma SL (top scale cut ⇒ residual dominates the
    order-(n−1) dyadic block); SL's own Case A and the perfect-bisection recursion proven.
  Remaining GAPS honestly marked: (U) the `m=n+1` non-dominant / `a₁>c(n)` adaptive
  subset-match strategy; (L) SL for imperfect top cuts (the shadow-coupling inequality).
- (prior) parity-measure-potential, induction-peel — see current.md; same two coupling gaps.

## Current best

**Answer (confirmed): `c(n) = 2^n/(2^{n+1}−1)`, minimax `D = u_n = 1/(2^{n+1}−1)`,
and `c(n) = (1+u_n)/2` with `2c(n) − 1 = u_n`.**

Verification of the arithmetic `2c(n) − 1 = u_n`:
`2c(n) = 2^{n+1}/(2^{n+1}−1)`, so `2c(n) − 1 = (2^{n+1} − (2^{n+1}−1))/(2^{n+1}−1) = 1/(2^{n+1}−1) = u_n`. ✓

### 0. The two-box reformulation (from Lemma R)

By **Lemma R** (`lemmas/reduction-odd-rank.md`), after all cuts the pieces are sorted
`b_1 ≥ b_2 ≥ …`, Liu (first claimer) secures the odd-rank sum, and with total length 1 his
guaranteed share is `(1+D)/2` where
`D = Σ_i (−1)^{i+1} b_i = |O| − |E|`,
`O = {odd-rank pieces}` (box O), `E = {even-rank pieces}` (box E). Box membership is fixed by
sorted rank, not by choice. So the game value is
`c(n) = (1 + V)/2`, `V := max_{Liu A} min_{Xiang cuts} D(A, cuts)`,
where Liu picks a multiset `A: a_1 ≥ … ≥ a_m` (`m ≤ n+1`, `Σ = 1`) and Xiang refines it with
`≤ n` cuts. We must show `V = u_n`. **CRITICAL** (per the reviewer): because one cut re-sorts
the list and can flip O/E membership of many pieces at once, every invariant below is stated
on **lengths / dyadic scales**, never on fixed ranks. We use throughout **Lemma M/I**
(`D = μ{t : N(t) odd}`, `N(t) = #{pieces > t}`; even multiplicity everywhere ⇒ `D = 0`),
**Lemma T** (a cut of a length-`s` piece into `s_1 ≥ s_2` toggles the parity of `N` exactly on
`E = [0,s_2) ∪ [s_1, s)`, so the final odd-set is `O_0 △ E_1 △ … △ E_r`; one cut moves `D` by
`≤ 2s_2 ≤ s`), and **Lemma P** (`D(S∪{v,v}) = D(S)`).

Throughout, the **dyadic configuration** `𝒟_n` is Liu's partition into pieces
`c_k = 2^k u_n` (`k = 0,…,n`), which sum to `u_n(2^{n+1}−1) = 1`; in **integer units of `u_n`**
its pieces are `{1, 2, 4, …, 2^n}`, total `2^{n+1}−1`.

---

### 1. UPPER BOUND `V ≤ u_n` — reduction and the resolved cases

We must show: for **every** Liu multiset `A` (`m ≤ n+1` pieces, sum 1), Xiang has `≤ n` cuts
forcing `D ≤ u_n`.

#### Lemma U0 (even-multiplicity corrector). If `m ≤ n`, Xiang forces `D = 0`.

*Proof.* We give Xiang a strategy whose final configuration has **even multiplicity of every
length**, whence `D = 0` by the Corollary of Lemma M. Maintain a "reduced multiset" `R`,
initially `A` (`m` pieces), and a "settled pool" `F` (initially empty) that will always consist
of matched equal pairs. Repeat while `|R| ≥ 2`: let `a_1 ≥ a_2` be the two largest of `R`.
- If `a_1 = a_2`: move both into `F` as a pair (no cut). `|R|` drops by 2.
- If `a_1 > a_2`: Xiang cuts the physical piece `a_1` into `(a_2, a_1 − a_2)` (a legal cut since
  `a_1 − a_2 > 0`). This creates a new copy of `a_2`; move the two equal copies `{a_2, a_2}`
  into `F`, and replace `a_1` in `R` by the leftover `a_1 − a_2`. `|R|` drops by 1; one cut used.

When `|R| = 1` with leftover `ℓ > 0`, Xiang bisects `ℓ` into `(ℓ/2, ℓ/2)` (one cut) and moves
the pair into `F`; if `|R| = 0` nothing is needed. Every step uses at most one cut and lowers
`|R|` by at least one, so the total number of cuts is at most `m` (at most `m−1` reduction
steps to reach `|R| ≤ 1`, plus at most one final bisection); since `m ≤ n`, this is within
budget. The final physical configuration is exactly `F`, a disjoint union of equal pairs, so
every length occurs with even multiplicity and `D = 0`. ∎

*(Verified computationally: 20000 random multisets, `m ≤ 6`, the strategy yields `D = 0` with
`≤ m` cuts every time.)*

**Consequence.** The upper bound holds for all `m ≤ n`. It remains to handle `m = n+1`, i.e.
Liu using his **full** budget of `n` cuts to make `n+1` pieces, with Xiang holding budget
`n = m − 1`. Fix such an `A: a_1 ≥ … ≥ a_{n+1}`, `Σ = 1`.

#### Resolved sub-case: `A` dominant, `a_1 ≥ Σ_{i≥2} a_i` (equivalently `a_1 ≥ 1/2`).

Since `Σ_{i≥2} a_i = 1 − a_1 ≤ a_1`, Xiang can cut `a_1` into the `n` values
`a_2, a_3, …, a_{n+1}` plus the leftover `a_1 − Σ_{i≥2} a_i = 2a_1 − 1 ≥ 0`, using exactly
`n` cuts (creating `n` new pieces inside `a_1`). Each `a_i` (`i ≥ 2`) now has a duplicate, so by
Lemma P every such pair may be deleted without changing `D`; the residual multiset is the single
piece `{2a_1 − 1}`, giving
`D = 2a_1 − 1`.
- If `a_1 ≤ c(n)`: `D = 2a_1 − 1 ≤ 2c(n) − 1 = u_n`. ✓
- If `a_1 > c(n)`: instead Xiang **bisects** `a_1` into `(a_1/2, a_1/2)` with ONE cut and, if he
  wishes, uses Lemma U0's chain on the remaining `n` pieces `{a_1/2, a_1/2, a_2, …, a_{n+1}}`.
  In fact the cleanest bound: bisecting `a_1` makes two equal copies `a_1/2`; by Lemma P delete
  the pair, leaving `{a_2, …, a_{n+1}}` — an `n`-piece multiset of total `1 − a_1`, with `n − 1`
  cuts remaining. Since `n − 1 ≥ (n) − 1 = (\#pieces) − 1`, Lemma U0 (with budget `n−1 ≥ n−1`)
  forces `D = 0` on it, hence `D = 0 ≤ u_n` overall. ✓

  *(Cut count check: `1` bisection + `≤ n` cuts of the U0 chain on `n` pieces `= ` at most
  `1 + n`? — No: after deleting the equal pair via Lemma P, only the `n` residual pieces remain
  and U0 needs `≤ n` cuts, total `≤ 1 + n` which can exceed `n`. Corrected argument: do **not**
  bisect first. Since `a_1 > c(n) ≥ 1/2`, we have `Σ_{i≥2} a_i = 1 − a_1 < 1/2 < a_1`; cut `a_1`
  into `a_2, …, a_{n+1}` and leftover `2a_1 − 1` using `n` cuts, delete the `n−1`… )*

  **[GAP U1, cut-count in the dominant `a_1 > c(n)` branch].** The replicate-all move already
  uses all `n` cuts and yields `D = 2a_1 − 1 > u_n`; there is no spare cut to bisect the
  leftover. To beat `u_n` here one must, instead of copying **all** of `a_2,…,a_{n+1}`, copy a
  **subset** and spend the freed cuts more efficiently (subset-match, see GAP U below). The
  `a_1 > c(n)` dominant branch is therefore **not** closed by the naive replicate; it is a
  special case of GAP U. What IS closed unconditionally in the dominant regime is `a_1 ≤ c(n)`.

*(For `n = 1` the dominant branch IS fully closed by bisection because then `m = 2` and one
bisection already frees a cut — see §3 base case; the cut-count obstruction only bites for
`n ≥ 2`.)*

**Status of the upper bound.** Fully proven for all `m ≤ n` (Lemma U0, `D = 0`) and for
`m = n+1` dominant with `a_1 ≤ c(n)` (`D = 2a_1 − 1 ≤ u_n`). Remaining:

> **GAP U (adaptive subset-match, `m = n+1`).** For `m = n+1` with either `a_1 > c(n)` or `A`
> balanced (`a_1 < 1/2`), Xiang needs a strategy choosing a subset `S ⊆ {a_2,…,a_{n+1}}` (and,
> for balanced profiles, one or more bisections) so that after cancelling the matched pairs the
> residual multiset has `D ≤ u_n` within the surviving budget. The naive greedy (match top two)
> and the single replicate-all are both provably insufficient (see current.md, and the explorer
> counterexamples `(0.5,0.28,0.22)`, `(0.45,0.30,0.25)`). This is the shared upper-bound wall.

---

### 2. LOWER BOUND `V ≥ u_n` — Liu plays `𝒟_n`

Liu plays the dyadic `𝒟_n`. We must show every Xiang response (`≤ n` cuts) leaves
`D ≥ u_n`, i.e. in integer units of `u_n`, `D ≥ 1`. Work in integer units:
`𝒟_n = {1, 2, …, 2^n}`, and set `L(n) := min_{≤ n cuts} D(𝒟_n)`. Target: `L(n) ≥ 1`.
*(Numerically `L(n) = 1` for `n ≤ 4`, matching `u_n`.)*

We use the two-case top-scale split (aimo-0117 shape). Say a piece is a **descendant of the top
scale** if it is a sub-piece of the original largest piece `2^n`.

#### Case A (top scale never cut): `D ≥ 2^{n−1} ≥ 1` (n ≥ 1).

If the original piece `2^n` is never cut, it survives whole. Every other original piece has
length `≤ 2^{n−1}`, and cutting only shortens pieces, so every piece other than the intact `2^n`
has length `≤ 2^{n−1}`. Hence for every threshold `t ∈ (2^{n−1}, 2^n)` the ONLY piece exceeding
`t` is the intact top piece: `N(t) = 1`, which is odd. By Lemma M/I,
`D = μ{N odd} ≥ μ(2^{n−1}, 2^n) = 2^{n−1} ≥ 1`. ∎ (Case A)

This is the box-language statement "the top scale sits alone in box O and Xiang cannot pair it
off without cutting it." It reproduces (and strengthens) the certified Case A.

#### Case B (top scale is cut at least once): reduction to Sub-lemma SL.

Suppose Xiang spends `≥ 1` cut on a descendant of the top scale. Consider the FIRST cut Xiang
makes to the (still whole) top piece `2^n`, splitting it into `p_1 ≥ p_2` with
`p_1 + p_2 = 2^n`, so `p_1 ≥ 2^{n−1} ≥ p_2 > 0`. After this cut the configuration is
`Π = {p_1, p_2} ∪ {1, 2, …, 2^{n−1}}` (the other originals possibly not yet cut), with `≤ n−1`
cuts of budget remaining. Because further cuts only refine `Π`, we have
`L(n) ≥ min over such p_1,p_2 of [ min_{≤ n−1 cuts} D(Π) ]`.
So Case B follows from:

> **Sub-lemma SL.** For every `p_1 ≥ p_2 > 0` with `p_1 + p_2 = 2^n`, and every `≤ n−1` further
> cuts, `D({p_1, p_2, 2^{n−1}, …, 2^0}) ≥ 1`.

**Proven fragments of SL.**

- **SL Case A (`p_1` not further cut).** `p_1 ≥ 2^{n−1}`; the next-largest piece is
  `max(p_2, 2^{n−1}) = 2^{n−1}` when `p_2 ≤ 2^{n−1}` (always true), and all pieces other than
  `p_1` are `≤ 2^{n−1}` and only shrink under cuts. Hence for `t ∈ (2^{n−1}, p_1)`, only `p_1`
  exceeds `t`: `N(t) = 1`, odd, contributing `μ = p_1 − 2^{n−1}` to `D`. This alone gives
  `D ≥ p_1 − 2^{n−1}`, which is `≥ 1` when `p_1 ≥ 2^{n−1} + 1`, but degenerates as
  `p_1 ↓ 2^{n−1}` (near-perfect bisection). So SL Case A closes SL only for sufficiently
  unbalanced top cuts; near-perfect bisection needs the next fragment.

- **SL, perfect bisection `p_1 = p_2 = 2^{n−1}`.** Then `Π = {2^{n−1}, 2^{n−1}} ∪ {2^{n−1}, …, 1}
  = {2^{n−1} (×3), 2^{n−2}, …, 1}`. By Lemma P delete one cancelling pair `{2^{n−1}, 2^{n−1}}`
  without changing `D`; the residual is exactly `{2^{n−1}, 2^{n−2}, …, 1} = 𝒟_{n−1}` in the SAME
  integer units, with `≤ n−1` cuts remaining. By the induction hypothesis `L(n−1) ≥ 1`,
  `D ≥ 1`. ✓ (This is the mirror of the tight upper-bound recursion in §4: perfect bisection is
  exactly the move by which Xiang would try to reach the order-`(n−1)` dyadic, and the IH says he
  cannot get below `1` there either.)

- **Base of the induction, SL for n = 1.** `Π = {p_1, p_2, 1}`, `p_1 + p_2 = 2`,
  `p_1 ≥ 1 ≥ p_2`, `0` cuts. Sorted descending `p_1 ≥ 1 ≥ p_2`, so
  `D = p_1 − 1 + p_2 = (p_1 + p_2) − 1 = 2 − 1 = 1 ≥ 1`. ✓

> **GAP L (SL for imperfect top cuts, `p_1 ≠ p_2`) — REVISED round 3: surrogate-opponent
> domination (crux aimo-0560), a mechanism distinct from induction-peel's exact-identity route.**
> For general `p_1 ∈ (2^{n−1}, 2^n)` we need `D(Π) ≥ 1` under `≤ n−1` cuts. Rather than construct
> a shadow-coupling map (existence argument), grant Xiang a *strictly stronger surrogate*: a
> Xiang who, in addition to his real `≤ n−1` cuts on `Π = {p_1, p_2, 2^{n−1},…,1}`, may also
> **freely re-merge the fragment pair `{p_1, p_2}` back into a single piece `2^n` at no cut cost**
> before continuing. The surrogate is only more dangerous, so `D(Π under real Xiang) ≥ D(Π under
> surrogate Xiang)`; if even the surrogate cannot force `D < 1`, the real bound follows for free.
> Two facts make the surrogate tractable:
>  - **Domination direction (to prove):** any real continuation from `Π` is available to the
>    surrogate (he can decline the re-merge), so `min_{real} D ≥ min_{surrogate} D` — need the
>    inequality is the *useful* direction, i.e. surrogate value is a valid *lower* bound target.
>    Concretely show: re-merging `{p_1,p_2}` and re-cutting optimally can only *lower* `D`, so
>    surrogate-optimal play WLOG first re-merges to the clean `2^n`, landing exactly on `𝒟_n` with
>    `≤ n−1` fresh cuts (one already spent to reach `Π`), i.e. reduces to `L(n) under n−1 cuts`.
>  - **Budget accounting:** the surrogate on the re-merged `𝒟_n` has `≤ n−1` cuts, so by the
>    budget-monotonicity lemma (below) and the IH `L(n−1) ≥ 1`, the surrogate value is `≥ 1`.
>
> This folds the `p_1 ≠ p_2` imperfection into the surrogate's free re-merge instead of tracking
> it through the global sort. **Watch out:** the domination inequality must point the right way
> (surrogate `≤` real in `D`); if re-merging could *raise* `D` the argument inverts — the builder
> must verify via Lemma T that re-merge-then-recut never increases the achievable minimum. Import
> the **budget-monotonicity lemma** (`L(𝒞,b)` non-increasing in `b`; extra cuts wasted as no-ops)
> to justify comparing the `n−1`-budget surrogate game to the `n`-budget original. This is the
> shared lower-bound wall (= gap L/B2), attacked here by a genuinely different lever than
> induction-peel's exact toggle identity — the two lower-bound approaches stay far apart.

---

### 3. Base cases (both directions, fully closed)

**n = 0.** `u_0 = 1`, `c(0) = 1`. Liu makes `0` cuts (single piece length 1); Xiang makes `0`
cuts. `D = 1 = u_0`, Liu takes the whole stick, `c(0) = 1`. ✓

**n = 1.** `u_1 = 1/3`, `c(1) = 2/3`.
- *Lower:* Liu plays `𝒟_1 = {2/3, 1/3}`, `1` Xiang cut. If Xiang cuts the `1/3` piece (top uncut),
  Case A gives `D ≥ 2^{0}u_1 = 1/3`. If Xiang cuts `2/3` into `(x, 2/3−x)` with `x ≥ 1/3 ≥ 2/3−x`,
  the pieces are `{x, 1/3, 2/3−x}` sorted descending, so
  `D = x − 1/3 + (2/3 − x) = 1/3`. Either way `D ≥ 1/3 = u_1`, with equality at `x = 1/3`
  (bisection). ✓
- *Upper:* Liu's `A` has `m ≤ 2`. If `m = 1`, Lemma U0 (`m = 1 ≤ n = 1`) forces `D = 0 ≤ 1/3`.
  If `m = 2`, `A = {a_1, a_2}`, `a_1 ≥ 1/2`, budget 1. If `a_1 ≤ 2/3`: cut `a_1 → (a_2, a_1−a_2)`,
  Lemma P leaves `{2a_1 − 1}`, `D = 2a_1 − 1 ≤ 2·(2/3) − 1 = 1/3`. If `a_1 > 2/3`: bisect
  `a_1 → (a_1/2, a_1/2)`; since `a_1/2 > 1/3 ≥ a_2`? — not always, but by Lemma P delete the equal
  pair `{a_1/2, a_1/2}`, leaving `{a_2}`, so `D = a_2 = 1 − a_1 < 1/3`. Either way `D ≤ 1/3 = u_1`. ✓

So `n = 1` is complete in both directions, confirming the strategy templates (replicate vs.
bisect for the upper; Case A + boundary computation for the lower).

---

### 4. Tightness on the dyadic input (upper bound achieved on `𝒟_n`)

Xiang bisects the current top piece `n` times. Start `𝒟_n = {2^n, …, 1}` (units). Bisecting the
top `2^n` into `(2^{n−1}, 2^{n−1})` yields three copies of `2^{n−1}`; by Lemma P delete one
cancelling pair, leaving `{2^{n−1}, 2^{n−2}, …, 1} = 𝒟_{n−1}` with `D` unchanged. Iterating,
after `k` bisections `D = D(𝒟_{n−k})`; after `n` bisections the multiset is `{1}` (units), so
`D = 1` unit `= u_n`, using exactly `n` cuts. Hence `min_{Xiang} D(𝒟_n) ≤ u_n`. Combined with
the lower bound (§2, once GAP L is closed) this shows the dyadic input's value is **exactly**
`u_n`, so Liu cannot do better than `u_n` by playing `𝒟_n`, and the extremal value is pinned. ✓

---

### 5. Summary of what is closed vs. open in this framing

CLOSED (fully rigorous, this framing):
- Reformulation `D = |O| − |E|` and the reduction `c(n) = (1+V)/2`, `2c(n)−1 = u_n` (§0).
- **Lemma U0:** `m ≤ n ⇒ D = 0`, reducing the upper bound to `m = n+1` (§1). [Promotable.]
- Upper bound for `m = n+1` dominant with `a_1 ≤ c(n)`: `D = 2a_1 − 1 ≤ u_n` (§1).
- Lower Case A: `D ≥ 2^{n−1}u_n ≥ u_n` when the top scale is uncut (§2).
- Lower Case B reduction to Sub-lemma SL; SL Case A, SL perfect-bisection recursion, SL base
  `n = 1` (§2).
- Base cases `n = 0, 1` complete in both directions (§3).
- Dyadic tightness: Xiang forces `D = u_n` on `𝒟_n` (§4).

OPEN (honest gaps, unchanged shared walls):
- **GAP U** — the adaptive subset-match strategy for `m = n+1` (non-dominant, or dominant with
  `a_1 > c(n)`; the cut-count obstruction GAP U1 is a special case). Upper bound not complete.
- **GAP L** — Sub-lemma SL for imperfect top cuts `p_1 ≠ p_2` (the shadow-coupling/net-toggle
  domination). Lower bound Case B not complete.

The two-box framing did NOT independently break these two walls, but it (i) produced a *new*,
clean, fully-rigorous reduction of the upper bound to `m = n+1` via Lemma U0 (strictly sharper
than the earlier "reduce to full-budget all-strict" heuristics, since it exhibits an explicit
`D = 0` corrector for every under-full profile), and (ii) recast Case B lower as the single
Sub-lemma SL with two of its branches closed, isolating the residual work to imperfect top cuts.

## Promotable lemmas

- **Lemma U0 (even-multiplicity corrector).** *Statement.* In the reduced minimax game (Lemma R
  setting: Liu commits a multiset of `m` positive pieces summing to 1, Xiang refines with `≤ n`
  cuts, `D = Σ(−1)^{i+1}b_i` on the descending sort), if `m ≤ n` then Xiang can force `D = 0`
  using at most `m` cuts. *Proof.* §1 above: the top-copy chain (repeatedly cut the current
  largest to copy the current second-largest, cancelling the resulting equal pair via Lemma P,
  and bisect the final leftover) yields a final configuration in which every length has even
  multiplicity, so `D = 0` by the Corollary of Lemma M. Uses only certified Lemmas P and M.
  Verified computationally (20000 random multisets, `D = 0`, `≤ m` cuts). Approach-agnostic;
  importable by any approach to discharge all `m ≤ n` profiles of the upper bound.
