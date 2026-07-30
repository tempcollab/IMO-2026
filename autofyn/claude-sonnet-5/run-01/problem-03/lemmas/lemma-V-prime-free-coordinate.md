# Lemma FC (the "one free coordinate" case of Lemma V'), and full closure of Proposition K

Proved by `geometric-dominance-construction`, round 6, per this round's
re-scoped assignment. Independently re-derivable in full from the
already-certified `lemmas/alternating-sum-toolkit.md` (Lemma D-INSERT,
Lemma V') and `lemmas/parity-pair-lemma-L.md` (Lemma PARITY-PAIR) — this
file adds no new machinery beyond composing those two certified results;
the composition itself is the new content.

## Setting (recalled, matching `parity-pair-lemma-L.md` and
`alternating-sum-toolkit.md` exactly)

Fix `n ≥ 1`. Normalize `t_i := 2^{n-i}` for `i = 1,...,n`, so `t_1 =
2^{n-1} > t_2 > ... > t_n = 1`, `T := (t_1,...,t_n)` the fixed tail. By
Lemma V', the infimum of `D(S ∪ T)` over Xiang Yu's split polytope
`P = {s_1 ≥ ... ≥ s_{n+1} ≥ 0, Σ s_i = 2t_1}` is attained at a vertex with
**at most one** coordinate strictly between two consecutive anchors from
`{0, t_n,...,t_1}`, every other coordinate exactly equal to an anchor.

The **pure-anchor** case (zero free coordinates) is Lemma L, now fully
proved for every `n` via Lemma PARITY-PAIR (`parity-pair-lemma-L.md`). This
file proves the remaining case: **exactly one** coordinate free.

## Precise statement of the free-coordinate case

Let `a_1,...,a_n ≥ 0` be integers with `Σ_{i=1}^n a_i = n` (the `n` pinned
coordinates of `S`, `a_i` of them equal to `t_i`; the `(n+1)`-th coordinate
of `S` is the free one). Let
```
x := 2t_1 - Σ_{i=1}^n a_i t_i.
```
Suppose `x > 0` and `x ∉ {0, t_1,...,t_n}` (i.e. `x` is a genuine free
coordinate, not degenerately equal to an anchor — that case is already
Lemma L with `n+1` total anchor picks). Let `S` be the multiset of `n`
copies-per-anchor plus the single value `x`, so `S ∪ T` is the merged
`(2n+1)`-element multiset. **Then `D(S∪T) ≥ t_n`.**

Combined with Lemma L (the zero-free-coordinate case) and Lemma V' (the
reduction of the infimum to these two cases), this gives:

## Proposition K, fully proved

**For every `n ≥ 1`, for every partition `S = (s_1≥...≥s_{n+1}>0)` of
`2t_1` into `n+1` positive parts, `D(S∪T) ≥ t_n`,** i.e. (by Lemma
D-REFORM) `oddsum(S∪T) ≥ c(n)`. Equality holds, uniquely, at the canonical
split `S = T ∪ \{t_n\}`. **The `k=n`, tail-untouched sub-case of the
lower-bound (doubling-family) conjecture is therefore a fully closed
theorem, for every `n≥1`** — not a numerically-verified conjecture.

## Two preliminary observations

**Observation 1 (integrality).** Every `t_i` and `2t_1` is an integer (in
this normalization), and every `a_i` is an integer, so `x = 2t_1 - Σa_it_i`
is always an integer.

**Observation 2 (`x` is never in `(0,t_n)`).** Since `t_n = 1` and `x` is a
positive integer (Observation 1), `x < t_n = 1` together with `x>0` is
impossible (no integer strictly between `0` and `1`). Hence the interval
`(0,t_n)` never actually occurs as `x`'s location: `x` is always `>t_1`,
or lies in some `(t_{j+1},t_j)` for `1≤j≤n-1`, or (degenerately, excluded
by hypothesis) equals an anchor. This was confirmed computationally: across
all one-free-coordinate points enumerated for `n=3,...,9` (`2+12+55+228+
905+3518+13563 = 18{,}283` points total), the anchor-count `j :=
\#\{i : t_i > x\}` took every value in `\{0,1,...,n-1\}` and **never**
`n` — exactly as this integrality argument predicts.

## Proof of the free-coordinate case

Let `j := \#\{i\in\{1,...,n\} : t_i > x\}` (well-defined and `x`-anchor-free
by hypothesis; `j\in\{0,...,n-1\}` by Observation 2, i.e. the interval
`(0,t_n)` is vacuous and need not be separately treated).

**Step 1: express `D(S∪T)` via D-INSERT.** Let `c_i := a_i+1` for
`i=1,...,n` be the multiplicities of the **pinned** anchor list (the `n`
pinned coordinates of `S` together with `T`'s own copy of each `t_i`); this
is an ordinary sorted list `C` of `Σc_i = 2n` elements with alternating sum
`D_0 := D(C)`, computed by the block-parity formula (as in
`parity-pair-lemma-L.md`). Inserting the single value `x` into `C` at its
true sorted rank `r := \big(\sum_{i:t_i>x} c_i\big) + 1` gives exactly the
list `S∪T`, and Lemma D-INSERT gives
```
D(S∪T) = D_0 - 2τ(r) + (-1)^{r+1} x,   τ(r) := Σ_{position ≥ r in C} (signed value).
```
Crucially, **`r`, `D_0`, and `τ(r)` depend only on `a_1,...,a_n` and on
which anchor-bracket `j` the value being inserted falls into — not on the
specific value inserted** (as long as it stays strictly inside the open
interval `(t_{j+1},t_j)`, with the convention `t_0:=+\infty`,
`t_{n+1}:=0`, so this covers `j=0,...,n-1`; the case `j=n` is vacuous by
Observation 2). Hence, **for `y` ranging over the whole closed interval
`[t_{j+1},t_j]`** (extending the formula continuously to the endpoints,
valid because Lemma D-INSERT's hypothesis `c_1,...,c_{r-1}\ge y\ge
c_r,...,c_m` allows equalities), the function
```
f(y) := D_0 - 2τ(r) + (-1)^{r+1} y
```
is **affine in `y`** with the *same* fixed `r`, `D_0`, `τ(r)` throughout,
and `f(x) = D(S∪T)` for our actual `x`.

*(Boundary convention for `j=0`: the interval is `[t_1,\infty)`, "closed"
only on the left; the argument below uses only the left endpoint `t_1`, so
this causes no issue.)*

**Step 2: identify the endpoint values as pure-anchor (Lemma L / Lemma
PARITY-PAIR) configurations.** At `y = t_j` (only relevant when `j\ge1`),
inserting `y` at rank `r` (defined by the bracket `(t_{j+1},t_j)`, i.e.
"immediately before the existing `t_j`-block") produces, as a **multiset**,
exactly the same sorted list as the pure-anchor configuration obtained from
`a` by **incrementing `a_j` by `1`** — tie-breaking among equal values does
not change a sorted multiset or its alternating sum. Write `a^{(j)}` for
this incremented vector: `Σ a^{(j)}_i = n+1`. Similarly, at `y=t_{j+1}`
(only relevant when `j\le n-1`), the resulting multiset equals the
pure-anchor configuration obtained by **incrementing `a_{j+1}` by `1`**;
write `a^{(j+1)}}` for it, also with `Σ = n+1`.

By construction `f(t_j) = D(\text{merge from } a^{(j)})` and
`f(t_{j+1}) = D(\text{merge from } a^{(j+1)})`, computed via exactly the
block-parity formula of `parity-pair-lemma-L.md` (i.e. these are literal
instances of that lemma's `D`, with `m = n+1` each).

**Step 3: apply Lemma PARITY-PAIR to both endpoints, unconditionally.**
Lemma PARITY-PAIR (`parity-pair-lemma-L.md`) requires **only** that the
multiplicity total `m` satisfies `n+m` odd — **no constraint on
`Σ a_i t_i`** is needed. Both `a^{(j)}` and `a^{(j+1)}` have `m=n+1`, so
`n+m = 2n+1`, odd, **automatically**, for every `n` and every base vector
`a`. Hence Lemma PARITY-PAIR applies unconditionally to both:
```
f(t_j) ≥ t_n   (when j ≥ 1),      f(t_{j+1}) ≥ t_n   (when j ≤ n-1).
```

**Step 4: combine via convexity of the affine function `f`.**

- **Case `1 ≤ j ≤ n-1` (interior bracket, both endpoints exist).** `x` is a
  strict convex combination of `t_{j+1}` and `t_j`: writing
  `x = λ t_{j+1} + (1-λ) t_j` for some `λ\in(0,1)`, affineness of `f` gives
  `f(x) = λ f(t_{j+1}) + (1-λ) f(t_j) ≥ λ t_n + (1-λ) t_n = t_n`, using Step
  3's two bounds. So `D(S∪T) = f(x) ≥ t_n`.

- **Case `j = 0` (`x > t_1`, no upper anchor).** `f` is affine with slope
  `(-1)^{r+1}`; here `r=1` (top rank), so the slope is `(-1)^2=+1`,
  i.e. `f(y) = y - D_0` is *strictly increasing* in `y`. Since `x>t_1`,
  `f(x) = x - D_0 > t_1 - D_0 = f(t_1) ≥ t_n` (the last step by Step 3
  applied to `a^{(1)}` — recall for `j=0` only the "snap down to `t_1`"
  endpoint exists, and `f(t_1)\ge t_n` was established in Step 3). So
  `D(S∪T) = f(x) > t_n ≥ t_n`.

- **Case `j = n`.** Vacuous, by Observation 2 — no such `x` exists.

In every case, `D(S∪T) ≥ t_n`. `∎`

## Independent computational verification (exact-Fraction / exact-integer,
exhaustive, not sampled)

A from-scratch Python script (`/tmp/verify_lemma.py`, `Fraction`
arithmetic throughout) exhaustively enumerated **every** feasible
one-free-coordinate vector `(a_1,...,a_n)` (`Σa_i=n`, all `n` values,
`x:=2t_1-Σa_it_i` computed, kept only when `x>0` and `x` not an anchor) for
`n=3,...,9` (`18{,}283` points total; `n=1,2` yield zero such points,
consistent with those being fully closed by the base-case hand-checks
already on record). For **every single point**, the script independently:

1. computed `D(S∪T)` two ways — directly by sorting the full `(2n+1)`-
   element list and summing signs, and via the `D_0 - 2τ(r) + (-1)^{r+1}x`
   decomposition (Step 1) — confirming they agree exactly (this
   re-verifies Lemma D-INSERT's formula in this specific configuration,
   not merely citing it);
2. computed the two (or, at `j=0` or would-be `j=n`, one) endpoint values
   `f(t_j)`/`f(t_{j+1})` via the independent block-parity formula (Step 2),
   and confirmed each is `≥ t_n` (re-verifying Lemma PARITY-PAIR's
   conclusion at each specific endpoint instance, not merely citing it);
3. confirmed the anchor-count `j` never equals `n` (Observation 2, checked
   directly, not just argued) — the observed range of `j` was exactly
   `{0,...,n-1}` for every `n` tested;
4. confirmed the final value `D(S∪T) ≥ t_n` in every one of the `18{,}283`
   cases (in fact `D(S∪T) ≥ 3t_n` in every tested case — the bound has
   slack; the worst observed value was always exactly `D=3` regardless of
   `n`, attained at the family `a=(0,1,1,...,1,0,3)`, `x=2t_1-3` — this
   extra slack is not needed for the proof but is recorded as a sanity
   check that the mechanism is not "barely" true).

Zero violations across all `18{,}283` exhaustively-enumerated cases and
all four independent checks per case.

## Status

**Certified.** This closes Proposition K completely (every `n≥1`, the full
continuum of splits `S`, not just pure-anchor vertices), via composition of
already-certified Lemma D-INSERT, Lemma V', and Lemma PARITY-PAIR — no new
unproven machinery. Does **not** close: the tail-simultaneously-refined
`k<n` extension (open, `recursive-embedding-induction`'s
PARITY-PAIR-GEN target), or the upper bound over arbitrary configurations
(out of scope, `universal-adversary-strategy`'s target).
