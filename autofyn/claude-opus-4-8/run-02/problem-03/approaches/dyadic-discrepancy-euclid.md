# Approach: dyadic-discrepancy-euclid (GAP U via signed-subset discrepancy + abs-difference reachability)

## Status
partial

(**Upper bound `D* ≤ u_n`, i.e. `c(n) ≤ 2ⁿ/(2^{n+1}−1)`, is now COMPLETELY proven, all `n`, all
Liu plays** — the entire GAP U wall, not just sub-case (iii-b). The residual `ℓ₁<Σ/2` and every
other case are subsumed by one clean argument below. The only remaining open piece of the *whole
problem* is the LOWER bound Case B / GAP L, which is a different wall owned by the
`induction-recursion-telescope` slug and is imported here, not re-attempted.)

## Approaches tried
- (inherited spine, from `dyadic-discrepancy`) Reduction to the static discrepancy game; Lemma G
  (greedy-claim); level-measure identity `D=λ{t:N(t) odd}`; Cut-Flip; Invisible-Pair (IP); the two
  exact removal ops (bisect / generalized pin) + free-delete; the **Residual-Total Theorem (RT)** —
  CERTIFIED, imported.
- **Round 4, this slug — accumulator schedule.** Closed Case (iii) sub-region A `{Σ/2≤ℓ₁<c(k)Σ}`
  fully (residual `2ℓ₁−Σ`, certified `lemmas/pivot-lemma.md`). Sub-region B `{ℓ₁<Σ/2}` left open.
- **Round 6, this slug — repoint to signed-subset / subset-sum pigeonhole.** Proved §A (reachable
  totals are signed-subset sums) and §B (Subset-Sum Pigeonhole: `m*(x)≤u_kΣ` universally). Left the
  **Reachability Lemma §D** open (whether the minimizing signed sum is realizable as one legal coin).
- **Round 7, this slug — CLOSED §D and the whole upper bound.** Two new results finish everything:
  1. **Theorem R (Abs-Difference Reachability), fully proven (§D).** For any finite multiset `U` of
     positive reals, the minimum value obtainable by pinning `U` down to a single coin equals the
     minimum non-zero signed-subset sum `m*_±(U)=min_{ε∈{±1}^U}|Σ ε_i x_i|`. Proof: a
     **sign-pairing induction** — pick a `+`/`−` pair from any minimizer, contract it to the coin
     `|x_p−x_q|` (one pin), and observe the contracted problem's minimum equals the original's.
     This supersedes the round-6 "peel-the-smallest" IH (which genuinely stalled) with a peel that
     keeps the minimum invariant. Verified exactly: tree root `= m*` on `0/2000` `Fraction` instances,
     `n≤5`; op-count never exceeds `n`.
  2. **Fewer-marks case is trivial (§F).** If Liu uses `a<n` marks (`a+1≤n` pieces), Xiang bisects
     *every* piece (`a+1≤n` cuts), turning the whole multiset into invisible pairs, so `D=0≤u_n`.
  Outcome: **the upper bound closes for ALL `n` and ALL Liu plays in one page** (§B+§D+§F, on the
  certified RT spine). Genuinely far from the twin's `ψ(k,β)` potential induction: this is a static
  subset-sum pigeonhole plus a constructive abs-difference tree, no induction on the answer level.

## Current best

**The entire upper bound is proven.** For every `n` and every Liu play, Xiang has a `≤n`-cut response
with `D≤u_nΣ` (`Σ=1`), hence `c(n)=(1+D*)/2≤(1+u_n)/2=2ⁿ/(2^{n+1}−1)`. Combined with the certified
lower bound (Case A) and the still-open lower-bound Case B (GAP L, `induction-recursion-telescope`),
the answer `c(n)=2ⁿ/(2^{n+1}−1)` is established modulo the single lower-bound Case-B gap that lives in
a *different* slug. **This slug's own target — GAP U — is fully closed.**

---

## Imported certified spine (proofs in `dyadic-discrepancy.md` §0–§4.5, `lemmas/`)

**Reduction (§0).** Liu's guaranteed total `= (1+D*)/2`, where `D*=max_Liu min_Xiang D` and `D` is the
first-player advantage of the alternating selection game on the final piece multiset. Thus
`c(n)≤2ⁿ/(2^{n+1}−1) ⇔ D*≤u_n`, with `u_n=1/(2^{n+1}−1)`.

**Lemma G / level-measure (`lemmas/greedy-claim.md`, CERTIFIED).**
`D(A)=Σ(−1)^{i+1}b_i=λ{t≥0:N_A(t)odd}` where `N_A(t)=#\{pieces>t\}`; hence `0≤D(A)≤b₁≤(total of A)`.

**Invisible-Pair (IP, §4.5, CERTIFIED).** For any multiset `R` and `v>0`, `D(R∪{v,v})=D(R)` (two equal
pieces add `2·1[t<v]`, an even amount, to `N(t)` everywhere).

**Removal ops (§4.5), each `≤1` cut.** On an effective multiset `ℓ₁≥…≥ℓ_m>0`:
- **(Bisect `ℓ_i`)** cut `ℓ_i` into two equal halves; the halves are an invisible pair, so `ℓ_i` is
  deleted; total drops by `ℓ_i`; piece count `−1`; `D` unchanged relative to the rest.
- **(Pin `ℓ_j` into `ℓ_i`, `ℓ_i>ℓ_j`)** cut `ℓ_i` into `\{ℓ_j,ℓ_i−ℓ_j\}`; the created `ℓ_j` and the
  standing `ℓ_j` are an invisible pair (deleted); `\{ℓ_i,ℓ_j\}↦\{ℓ_i−ℓ_j\}`; total `−2ℓ_j`.
- **(Free-delete)** remove an equal pair `\{v,v\}` at cost `0` cuts (IP).
Each op preserves the invariant "final `D` = discrepancy of the current effective multiset."

**Residual-Total Theorem (RT, §4.5, CERTIFIED).** Since `D≤(total)` (Lemma G), if from total `Σ` Xiang
can, using `≤N` cuts, reach an effective multiset of total `≤t`, then `D≤t`. In particular, reaching an
effective total `≤u_nΣ` with `≤n` cuts yields `D≤u_nΣ`.

The rest of this file proves, from scratch, that such a play always exists.

---

## §A. Reachable effective totals are signed-subset sums

**Lemma A.** Every effective multiset reachable from `M=\{x_1,…,x_p\}` by ops (Bisect, Pin,
Free-delete) consists of *coins*, each of the form `Σ_{i∈U}ε_i x_i` over a subset `U⊆\{1,…,p\}`, with
`ε_i∈\{±1\}`, and the supports `U` of distinct surviving coins are pairwise disjoint. Consequently the
effective total is `Σ_i ε_i x_i` for some `ε∈\{−1,0,1\}^p` (`ε_i=0` on deleted / paired indices), and
each coin value equals its own (positive) signed sum.

*Proof.* Attach to every effective piece a formal signed sum over the original indices equal to its
length, with the original pieces having support `\{i\}` and coefficient `+1`. This holds initially. A
Bisect zeroes the coefficients of a piece's support (the piece is removed). A Pin of coin
`b=Σβ_i x_i` into coin `a=Σα_i x_i` (`a>b`, disjoint supports) produces the coin
`a−b=Σ(α_i−β_i)x_i`; disjointness makes each `α_i−β_i∈\{−1,0,1\}`, and the deleted invisible pair
carries coefficient `0`. Free-delete removes an equal pair. Throughout, the surviving coins have
pairwise disjoint supports (a pin merges two disjoint-support coins into one; deletion only removes).
Each coin value is a length `>0` and equals `Σ_{i∈U}ε_i x_i` for the current signs; summing over the
disjoint-support coins gives an overall `ε∈\{−1,0,1\}^p`. ∎

Write `Reach(U)` for the set of coin-values obtainable by pinning the multiset `U` down to a single
coin (a binary "absolute-difference tree" with leaves `U`: each internal node is `|left−right|`). By
Lemma A every element of `Reach(U)` is a `\{±1\}`-signed sum of `U`.

---

## §B. Subset-Sum Pigeonhole — the discrepancy half of the upper bound

**Lemma B (Subset-Sum Pigeonhole).** Let `x_1,…,x_{k+1}>0` have sum `Σ`. Then there is
`ε∈\{−1,0,+1\}^{k+1}`, `ε≠0`, with
`|Σ ε_i x_i| ≤ u_kΣ`, where `u_k=1/(2^{k+1}−1)`. Equivalently
`m*(x):=\min\{|Σε_i x_i|:ε≠0\}≤u_kΣ`.

*Proof.* Consider the `2^{k+1}` subset sums `σ_S=Σ_{i∈S}x_i`, `S⊆\{1,…,k+1\}`. Each lies in `[0,Σ]`.
Partition `[0,Σ]` into `2^{k+1}−1` consecutive sub-intervals each of length
`Σ/(2^{k+1}−1)=u_kΣ` (an exact partition, since `(2^{k+1}−1)·u_kΣ=Σ`). We have `2^{k+1}` points in
`2^{k+1}−1` boxes; by the **Pigeonhole Principle** (`knowledge_base.md`, "Pigeonhole / box principle")
two distinct subsets `S≠T` share a box, so `|σ_S−σ_T|≤u_kΣ`. Now
`σ_S−σ_T=Σ_{i∈S\setminus T}x_i−Σ_{i∈T\setminus S}x_i=Σ_i ε_i x_i`, with `ε_i=+1` on `S\setminus T`,
`−1` on `T\setminus S`, `0` else. Since `S≠T`, `S△T≠∅`, so `ε≠0`. Hence `|Σε_i x_i|≤u_kΣ`. ∎

**Remarks.** Lemma B uses no case hypothesis, so it applies to Cases (i),(ii),(iii-a),(iii-b) alike —
in particular the super-balanced residual `ℓ₁<Σ/2` that defeated every fixed schedule. It is *not* the
refuted "reachable-mesh" bound (which fails on the gaps of the set of *reachable values*, gaps up to
`2u_k` just outside the window); the pigeonhole here is on the `2^{k+1}` *subset sums*, always
`2^{k+1}` points in `[0,Σ]` — a different, elementary object. The bound is sharp: at the dyadic
extremal `x_i=2^{k−i}u_k` (`Σ=1`) the smallest non-zero signed sum is exactly `u_k`
(`2^k u_k−2^{k−1}u_k−⋯−u_k=u_k`).

**Support of the minimizer.** Let `ε*` attain `m*(x)`, and let `U₀=\{i:ε*_i≠0\}` be its support. On
`U₀` all coefficients are `±1`. Then `m*(x)=m*_±(U₀):=\min_{ε∈\{±1\}^{U₀}}|Σ_{i∈U₀}ε_i x_i|`. Indeed
`m*(x)=|Σ_{i∈U₀}ε*_i x_i|≥m*_±(U₀)`; conversely every `\{±1\}` pattern on `U₀` extends (by zeros) to a
non-zero `\{−1,0,1\}` pattern on all of `x`, so `m*_±(U₀)≥m*(x)`. Hence equality.

---

## §C. The minimizer uses only pieces `≥ m*`

**Lemma C.** `m*(x)≤\min_i x_i`; in particular `m*(x)≤\min\{x_i:i∈U₀\}`.

*Proof.* Each singleton pattern `e_j` (coefficient `+1` on `j`, else `0`) is non-zero with value
`x_j`, so `m*(x)≤x_j` for every `j`. ∎

---

## §D. Theorem R — Abs-Difference Reachability (the former open step, NOW PROVEN)

> **Theorem R.** For every finite multiset `U` of positive reals,
> `\min Reach(U)=m*_±(U):=\min_{ε∈\{±1\}^U}\big|Σ_{i∈U}ε_i x_i\big|.`
> Equivalently, the minimum non-zero signed sum of `U` is realizable as a single coin, i.e. by pinning
> `U` down to one piece using `|U|−1` pins (some possibly replaced by free-deletes).

*Proof.* Write `s=|U|`.

**(≥) Every reachable value is a `±1` signed sum.** By induction on `s`: a leaf is `x_i` (`+1` sign);
an internal node `|L−R|` with `L,R` reachable from disjoint sub-supports equals `±(L−R)`, and by the
IH `L,R` are `±1` signed sums of their supports, so `|L−R|` is a `±1` signed sum of `U`. Hence
`\min Reach(U)≥m*_±(U)`.

**(≤) The minimum signed sum is realizable.** Strong induction on `s`.

- **`s=1`:** `Reach(\{x_1\})=\{x_1\}=\{m*_±\}`. ✓
- **`s=2`, `U=\{x_1≥x_2\}`:** signed sums are `x_1+x_2` and `x_1−x_2`; the minimum is `x_1−x_2`, and
  `Reach(U)=\{x_1−x_2\}`. ✓
- **`s≥2` (step).** Fix a minimizer `ε*` of `m*_±(U)`; after a global sign flip assume
  `Σ_i ε*_i x_i = m:=m*_±(U)≥0`. **The minimizer is mixed** (has at least one `+1` and one `−1`):
  if all `ε*_i=+1` then `m=Σx_i` (the total `T`), but flipping the smallest element `μ` gives value
  `|T−2μ|`, and `0<μ<T` (as `s≥2`) forces `|T−2μ|<T`, contradicting minimality; and all `ε*_i=−1`
  gives `Σ=−T<0`, contradicting the orientation `m≥0`. So pick indices `p,q` with `ε*_p=+1`,
  `ε*_q=−1`.

  Contract this pair: form the coin `c:=|x_p−x_q|` by one pin (cut the larger into `\{smaller, c\}`,
  delete the equal pair), and set `U'':=(U\setminus\{x_p,x_q\})∪\{c\}` (size `s−1`). Every
  abs-difference tree on `U''` lifts to one on `U` by expanding the leaf `c` into the node
  `|x_p−x_q|`, so
  `\min Reach(U)≤\min Reach(U'')`.   (★)

  Now I claim `m*_±(U'')=m*_±(U)`. A `\{±1\}` pattern `δ` on `U''` has value
  `|δ_c c+Σ_{i≠p,q}δ_i x_i|`. Writing (WLOG `x_p≥x_q`) `c=x_p−x_q`, we get
  `δ_c c=δ_c x_p+(−δ_c)x_q`, i.e. `δ` corresponds bijectively to an original pattern `ε` on `U` with
  `ε_p=δ_c`, `ε_q=−δ_c` — that is, `ε_p=−ε_q` (opposite signs on `p,q`), all other signs free. Hence
  `m*_±(U'')=\min\{|Σ_i ε_i x_i|:ε∈\{±1\}^U,\ ε_p=−ε_q\}.`
  The minimizer `ε*` has `ε*_p=+1=−ε*_q`, so it is feasible in this constrained minimum, giving
  `m*_±(U'')≤m`. And restricting the minimum to a subset of patterns cannot lower it below the global
  minimum, so `m*_±(U'')≥m*_±(U)=m`. Therefore `m*_±(U'')=m`.

  If `c=0` (i.e. `x_p=x_q`): the pair is an invisible equal pair, free-delete it and recurse on
  `U\setminus\{x_p,x_q\}` (size `s−2`); the deleted pair contributes `0` to the signed sum, so
  `m*_±(U\setminus\{x_p,x_q\})=m`, and by the IH its minimum is realizable, hence so is `m` for `U`
  (attach the free-deleted pair). ✓

  Otherwise `c>0`, so `U''` is a multiset of `s−1` positive reals. By the IH,
  `\min Reach(U'')=m*_±(U'')=m`. With (★), `\min Reach(U)≤m`. Combined with the `(≥)` direction
  `\min Reach(U)≥m*_±(U)=m`, we get `\min Reach(U)=m`. ✓

This completes the induction and the proof of Theorem R. ∎

**Numerical confirmation (exact `Fraction`, `/tmp/thmR.py`).** For `2000` random multisets of `n+1`
integer pieces (`n≤5`), the tree produced by the pairing induction has root exactly equal to the
brute-force `m*` in `0/2000` mismatches; and the resulting play uses `≤n` ops in `0/2000` overruns.

---

## §E. Op-budget accounting — exactly `n` ops, never binding

Facing Liu's `n+1` pieces `x_1,…,x_{n+1}` (Liu used all `n` marks), Xiang computes a global minimizer
`ε*` with support `U₀` (`|U₀|=s`, `1≤s≤n+1`), and plays:

1. **Bisect** each of the `n+1−s` pieces outside `U₀`: `n+1−s` cuts, each deleting its piece (IP).
2. **Realize `m*` as one coin** by the Theorem R tree on `U₀`: a binary tree on `s` leaves has `s−1`
   internal nodes, i.e. `s−1` pins (each `≤1` cut; a `0`-valued node is a free-delete costing `0`).

Total cuts `=(n+1−s)+(s−1)=n`, **exactly the budget**, independent of `s` and the pin order. (There is
no iterated `a mod b` with quotient `>1`: each original piece is consumed once; the descent is a
*single* signed combination, so the reviewer's Euclidean-chain-overrun worry never materialises — the
chain length is `s−1≤n`.) After the play the effective multiset is the single coin of value
`m*(x)`; by Lemma A / IP all bisected halves and pinned equal-pairs are invisible, so
`D=D(\{m*\})=m*(x)≤u_nΣ` by Lemma B. By RT, `D≤u_nΣ`.

Thus **every Liu play with exactly `n` marks (`n+1` pieces) is answered with `D≤u_nΣ`, all `n`.** This
subsumes Cases (i),(ii),(iii-a) and closes the residual (iii-b) `ℓ₁<Σ/2` uniformly — the pin-top-2
potential and the Pivot Lemma become special cases, not prerequisites.

---

## §F. Liu plays with fewer than `n` marks — trivial

If Liu marks `a<n` points, the stick is cut into `a+1` pieces, and `a+1≤n`. Xiang **bisects every
piece** (one cut each, `a+1≤n` cuts total). The final multiset is `\{x_1/2,x_1/2,…,x_{a+1}/2,x_{a+1}/2\}`:
every value occurs an even number of times, so `N(t)=\#\{pieces>t\}` is even for every `t`, whence
`D=λ\{t:N(t)odd\}=0≤u_nΣ`. (Formally, this is `a+1` disjoint invisible pairs, `D=0` by IP.) ∎

---

## §G. Conclusion of the upper bound

Combining §E (Liu uses all `n` marks) and §F (Liu uses fewer), **for every `n` and every Liu play,
Xiang has a `≤n`-cut response with `D≤u_nΣ`.** Hence `D*=max_Liu min_Xiang D≤u_n`, and by the
Reduction (§0),
`c(n)=(1+D*)/2≤(1+u_n)/2=\dfrac{2^n}{2^{n+1}−1}.`

**Verification of the constant.** `(1+u_n)/2` with `u_n=1/(2^{n+1}−1)`:
`(1+1/(2^{n+1}−1))/2=((2^{n+1}−1+1)/(2^{n+1}−1))/2=(2^{n+1}/(2^{n+1}−1))/2=2^n/(2^{n+1}−1)`. ✓
Values: `n=1→2/3`, `n=2→4/7`, `n=3→8/15` — matching the certified answer and the `n=1,2` brute-force.
Tightness: the dyadic Liu partition `x_i=2^{n−i}u_n` attains `m*=u_n` (Remark in §B), so the bound is
achieved, consistent with the lower bound.

This closes the **entire GAP U wall** (upper bound), all `n`, all Liu plays. ∎ (upper bound)

---

## Remaining open piece of the whole problem (NOT this slug's mechanism)

The full determination `c(n)=2ⁿ/(2^{n+1}−1)` also needs the **lower bound** `D*≥u_n`: Liu's dyadic
partition forces `D≥u_n` against every `≤n`-cut Xiang response. Case A (top dyadic piece uncut) is
certified; **Case B / GAP L residual (`maxc≥2` T-run)** is still open and is owned by the
`induction-recursion-telescope` slug (reserve-carry induction on `Z`'s dyadic cut-tree). It is imported
here, not re-attempted — hence this slug's Status is `partial` for the *whole* problem even though its
own target (GAP U) is fully closed.

---

## Spec concerns

1. **Op-budget was never binding (§E):** every single-coin signed-subset play uses exactly `n` ops
   (`n+1−s` bisects + `s−1` pins); the abs-difference chain has length `s−1≤n`. The reviewer's
   "iterated subtractive descent may overrun `k` ops" is resolved — the descent is one signed
   combination, not an iterated modulus.
2. **The one-shot consecutive-gap pigeonhole `c(k)Σ/(2k)` is the WRONG pigeonhole** (it exceeds `u_kΣ`
   for `k≥3`, ratio `2^{k−1}/k`). The correct pigeonhole is on the `2^{k+1}` subset sums (§B), giving
   `u_kΣ` exactly. This is why the "find a small consecutive gap" base was insufficient and why §D
   (reachability of the *global* minimizer) was the real crux.
3. **The reduction is universal, not confined to region B.** §B+§D+§F close *all* cases and all `n` in
   one stroke — a genuinely different framing from the twin's `ψ(k,β)` induction (static subset-sum +
   constructive tree, no induction on the answer level).

---

## Empirical support (exact arithmetic where noted)

- Theorem R (`/tmp/thmR.py`, exact `Fraction`): pairing-induction tree root `= m*` on `0/2000`
  mismatches, `n≤5`; op-count `≤n` on `0/2000`; `m*≤u_nΣ` on `0/2000`.
- `min Reach(U)=m*_±(U)` on `0/300` random integer multisets, `s≤6` (`/tmp/rtest.py`).
- Fewer-marks case: strong random search gives `min_Xiang D≪u_n` for `a<n` (e.g. `n=4`, pieces
  `[0.766,0.15,0.084]`, min `D≈0.0089<u_4≈0.0323`); §F proves `D=0` directly.
- Round-6 data: `m*(x)≤u_kΣ` with `0/12000` violations, all `k∈\{2,3,4,5\}` (`/tmp/round-6/rt_search.py`).

---

## Promotable lemmas

- **Theorem R (Abs-Difference Reachability), NEW, fully proven this round.** *Statement:* for any
  finite multiset `U` of positive reals, `\min Reach(U)=\min_{ε∈\{±1\}^U}|Σ ε_i x_i|`, and the
  minimizer is realizable as a single coin by `|U|−1` pins. *Proof:* sign-pairing strong induction
  (§D). Reusable by any GAP-U approach as the realizability input, replacing the round-6 open §D.
- **Signed-subset reduction (Lemma A), fully proven (round 6, re-stated §A).** Every reachable
  effective total is `Σε_i x_i`, `ε∈\{−1,0,1\}`, a sum of disjoint-support `\{±1\}` coins.
- **Subset-Sum Pigeonhole (Lemma B), fully proven (round 6, §B), UNIVERSAL.** `m*(x)≤u_kΣ`.
- **Upper-bound completion (§E–§G), NEW.** For all `n` and all Liu plays, Xiang holds `D≤u_nΣ`; hence
  `c(n)≤2ⁿ/(2^{n+1}−1)`. Depends only on RT (certified) + Lemmas A,B,C + Theorem R + the fewer-marks
  bisect argument (§F). Ready to certify the whole GAP U wall.
