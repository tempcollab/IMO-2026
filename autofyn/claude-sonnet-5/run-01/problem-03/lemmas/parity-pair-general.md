# Lemma PARITY-PAIR-GENERAL and Lemma ZERO-DROP (new, round 7)

Source: `recursive-embedding-induction.md`, round 7 build (target: Lemma
PARITY-PAIR-GEN / Step 1, "Lemma PARITY-PAIR-ANCHOR"). Both lemmas below are
strict generalizations of already-certified facts
(`lemmas/parity-pair-lemma-L.md`) and are proved directly from the same
certified block formula — no unproved machinery is introduced.

## Setting

Fix `n ≥ 1`. Let `t_i := 2^{n-i}` for `i = 1,...,n` (`t_1 = 2^{n-1} >
t_2 > ... > t_n = 1`). For a finite sorted-descending list `Y`, `D(Y)` is the
alternating sum `Σ_j (-1)^{j+1} y_j` (1-indexed).

## Lemma ZERO-DROP

**Statement.** For any finite multiset `Y` of nonnegative reals and any
`k ≥ 0`, `D(Y ∪ \{0 \text{ (mult. } k)\}) = D(Y)`.

**Proof.** Sort `Y ∪ \{0^k\}` descending: every `0` sorts strictly after
every positive element of `Y` (or, if `Y` is empty/entirely `0`, the claim is
trivial `0=0`), so the `k` zero entries occupy exactly the last `k` sorted
positions; every non-zero element of `Y` occupies the *same* position it
would occupy in `Y` alone, since removing purely-trailing entries changes no
earlier position. Hence the alternating sum's positive-element terms are
identical, and each of the `k` trailing zero terms contributes
`(-1)^{j+1}\cdot 0 = 0` regardless of `j`. So `D(Y\cup\{0^k\}) = D(Y) + 0 =
D(Y)`. ∎

*(Consequence used below: appending or discarding zero-valued pieces never
changes `D`, so any argument about the value of `D` may freely add or ignore
degenerate zero-length cut results.)*

## Lemma PARITY-PAIR-GENERAL

**Statement.** For every `n ≥ 1` and every choice of nonnegative integers
`c_1,...,c_n ≥ 0` (no requirement that `c_i ≥ 1`; some or even all but one
may be `0`), with `M := Σ_{i=1}^n c_i`, if `M` is **odd** then
```
D(C) ≥ t_n = 1,
```
where `C` is the sorted-descending list consisting of `c_i` copies of `t_i`
for each `i = 1,...,n`.

This **strictly generalizes** the certified Lemma PARITY-PAIR
(`lemmas/parity-pair-lemma-L.md`), which is exactly the special case
`c_i ≥ 1` for every `i` (there written `c_i = a_i+1`, `a_i ≥ 0`; in that
special case `M = n + Σa_i`, so "`M` odd" is literally the same condition
as that lemma's "`n+m` odd").

**Proof.** By the same **strong induction on `n`** as the certified proof of
Lemma PARITY-PAIR, using the certified block formula (verbatim from
`parity-pair-lemma-L.md`, which holds for arbitrary `c_i ≥ 0` — its
derivation is a direct telescoping computation that never used `c_i ≥ 1`):
writing `C_0 := 0`, `C_i := c_1+\cdots+c_i`,
```
D(C) = Σ_{i : c_i \text{ odd}} (-1)^{C_{i-1}} t_i.
```
(If `c_i = 0` for some `i`, that index simply contributes nothing to the
sum, exactly as if "there is no block `i`" — the formula needs no
modification.)

*Base case `n=1`.* `M = c_1` odd (in particular `c_1 ≥ 1`). Single block:
`D = (-1)^0 t_1 = t_1 = t_n`. Equality.

*Inductive step, `n ≥ 2`.* Let the "remainder" be levels `2,\dots,n`,
re-parametrized as their own level-`(n-1)` instance: `t'_j := t_{j+1}`,
`c'_j := c_{j+1}` for `j=1,\dots,n-1`, with `M' := M - c_1 = Σ_{j\ge2} c_j`,
and let `D'` denote `D` computed for this fresh `(n-1)`-level list (using the
same block formula, freshly indexed from `1`).

- **Case A (`c_1` even, including `c_1 = 0`).** By the block formula, index
  `i=1` does not contribute to `D(C)` (either because `c_1=0`, so there is
  no block `1` at all, or because `c_1` is even and positive, so the block
  formula's own sum simply omits it either way — "`c_1` odd" fails in both
  sub-cases). For every `i \ge 2` appearing in the sum, `C_{i-1} = c_1 +
  C'_{i-2}` where `C'_{j} := c_2+\cdots+c_{j+1}` is the remainder's own
  partial sum; since `c_1` is even, `(-1)^{C_{i-1}} = (-1)^{C'_{i-2}}`,
  i.e. every remainder term's sign is unchanged from its fresh-indexed
  value. Hence `D(C) = D'` exactly (this holds whether `c_1=0` or `c_1>0`
  even — in the `c_1=0` sub-case the "shift" is by `0`, trivially
  sign-preserving). Since `M = M' + c_1` with `c_1` even and `M` odd, `M'` is
  odd, so the induction hypothesis (applied at level `n-1`, with `M'`
  possibly arising from a `c'_j` vector containing zeros — exactly what the
  inductive statement is designed to allow) gives `D' \ge t'_{n-1} = t_n`.
  Hence `D(C) = D' \ge t_n`.
- **Case B (`c_1` odd, so `c_1 \ge 1`).** Block `1` contributes
  `(-1)^{C_0} t_1 = t_1` (sign `+`, since `C_0=0`). For `i \ge 2`,
  `C_{i-1} = c_1 + C'_{i-2}` with `c_1` odd, so `(-1)^{C_{i-1}} =
  -(-1)^{C'_{i-2}}`: every remainder term's sign is flipped relative to its
  fresh-indexed value, i.e. `D(C) = t_1 - D'`. The induction hypothesis does
  **not** apply to `D'` here (`M' = M - c_1` is even in this case), so
  instead bound `D'` via the already-certified Lemma D-BOUND
  (`lemmas/alternating-sum-toolkit.md`, `0 \le D(Y) \le \max(Y)`, valid for
  any finite nonnegative sorted list including the empty list by convention
  `D(\emptyset)=0`): the remainder list only contains values from
  `\{t_2,\dots,t_n\}`, so `\max(\text{remainder}) \le t_2` (with the
  convention that an empty remainder has `D'=0 \le t_2` trivially). Hence
  `D(C) = t_1 - D' \ge t_1 - t_2 = t_2` (using `t_1-t_2 = 2^{n-1}-2^{n-2} =
  2^{n-2} = t_2`, valid since `n \ge 2`), and `t_2 = 2^{n-2} \ge 2^0 = t_n`
  since `n \ge 2`.

Both cases give `D(C) \ge t_n`. ∎

**Independent computational verification (exact integer arithmetic,
exhaustive, not sampled).** A from-scratch Python script
(`/tmp/verify_ppg.py`) exhaustively enumerated **every** vector
`(c_1,\dots,c_n) \in \{0,1,2,3,4\}^n` for `n=1,\dots,7` (`97{,}648` vectors
with `M \ge 1` total across all `n`), computed `D` directly by sorting and
summing signs (not via the block formula — an independent recomputation),
and checked the claim on every vector with `M` odd. **Zero violations.**
This directly stress-tests the new content (vectors with one or more
`c_i = 0` for `i < n`, which the original certified Lemma PARITY-PAIR's
statement does not cover), e.g. `n=4`, `c=(0,0,3,2)` (`M=5` odd):
`C = \{2,2,2,1,1\}`, `D = 2-2+2-1+1 = 2 \ge t_4=1`. ✓.

## What this closes

Lemma PARITY-PAIR-GENERAL subsumes Lemma PARITY-PAIR (and hence Lemma L) as
the special case `c_i \ge 1 \,\forall i`. Its new content — allowing
`c_i = 0` for indices `i < n` — is exactly what is needed by
`lemmas/parity-pair-anchor.md` (round 7, `recursive-embedding-induction`) to
handle Xiang-Yu strategies that split the tail as well as `p_1`, since a
tail piece that is itself split may vanish entirely from the merged anchor
multiset (see that file for the full argument and its precise remaining
scope).

## Status
**Certified.** Proof is complete, self-contained, and matches the technique
of the already-certified Lemma PARITY-PAIR exactly (same case split, same
citation of Lemma D-BOUND), generalized only by removing the unnecessary
`c_i \ge 1` restriction — independently verified exhaustively as above.
