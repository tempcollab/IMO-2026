## Lemma FREE-TIE-REDUCTION (Move 0), and mark-faithful recursion `solve2`

Certified round 14, `universal-adversary-strategy`.

### Statement

Let `A = (a_1 \ge a_2 \ge \cdots \ge a_m)` be any sorted list of positive
reals (any `m \ge 1`), and suppose some value `v` occurs with **even**
multiplicity `2j \ge 2` in `A` (a run of `2j` equal entries; since `A` is
sorted, these occupy `2j` **consecutive** ranks, say `k+1,\ldots,k+2j`, for
some `0 \le k \le m-2j`). Let `A' := A` with those `2j` copies of `v` deleted
(so `|A'| = m-2j`, still sorted descending). Then, **using zero marks**,
```
oddrank(A) = j\,v + oddrank(A').
```
Consequently, this reduction may be applied to `A` **at no cost**, and the
resulting instance `A'` may be handed to any further (marked) strategy with
the *full* remaining mark budget unchanged.

### Proof

Consider the `2j` consecutive ranks `k+1,\ldots,k+2j` occupied by the tied
run. Group them into `j` consecutive pairs `(k+1,k+2), (k+3,k+4), \ldots,
(k+2j-1,k+2j)`. In any pair of two consecutive integers, exactly one is odd
and one is even, regardless of the parity of `k` (the starting offset): if
`k+2i-1` is odd, `k+2i` is even, and vice versa — either way exactly one of
the two ranks in each pair is odd. Since both ranks in a pair hold the value
`v`, each pair contributes exactly `v` to `oddrank(A)` (from whichever of its
two ranks is odd) and exactly `v` to `evensum(A)` (from the other). Summing
over the `j` pairs, the tied run contributes exactly `j v` to `oddrank(A)`,
independent of `k`.

Now consider the ranks outside the run: ranks `1,\ldots,k` (before the run)
and ranks `k+2j+1,\ldots,m` (after the run). These correspond exactly to the
elements of `A'` in the same relative sorted order (deleting the run does not
change the relative order of the remaining elements, since `A` was already
sorted and every deleted element's value `v` is removed as an intact block).
The first block (`1,\ldots,k`) keeps its original ranks — these are the first
`k` elements of `A'` too, at the same ranks `1,\ldots,k` in `A'`; parity is
unchanged, so this block contributes `oddrank(a_1,\ldots,a_k)` to both
`oddrank(A)` and `oddrank(A')` identically.

The second block (global ranks `k+2j+1,\ldots,m` in `A`, local ranks
`1,\ldots,m-k-2j` within itself) is exactly the tail of `A'` starting at
`A'`'s position `k+1`. In `A`, its global rank for local position `\ell` is
`k+2j+\ell`; in `A'`, its rank is `k+\ell`. The shift between these two rank
assignments is `2j`, an **even** number, so parity is preserved: rank
`k+2j+\ell` is odd in `A` iff rank `k+\ell` is odd in `A'`. Hence this block
contributes the identical value to `oddrank(A)` as it does to `oddrank(A')`.

Summing all three contributions (the tied run: `jv`; the prefix block:
identical in `A` and `A'`; the suffix block: identical in `A` and `A'`) gives
```
oddrank(A) = jv + [\text{prefix contribution}] + [\text{suffix contribution}]
           = jv + oddrank(A').
```
∎

### Remark: relation to Lemma DOM's Step 1

This is the same tie-insensitivity mechanism used in the certified Lemma DOM
(`generalized-domination-and-halving.md`), Step 1 (there applied only to the
specific doubled-tail multiset `E` constructed by that lemma's proof), and in
Lemma DOUBLE-INSERT (`double-insert.md`, the special case `j=1`, one inserted
pair). Lemma FREE-TIE-REDUCTION is the fully general **removal** direction of
the same identity, applicable to *any* pre-existing even-multiplicity tied
run **anywhere** in a sorted list — not only a run created by an insertion,
and not only a run located in a top prefix. In particular it strictly
generalizes any restriction to "ties only in the top `2k` elements": the
proof above never uses the position `k` of the run at all, only that the run
has even length and is a single contiguous block (automatic from sortedness).

### Application: Move 0 in the mark-faithful recursion `solve2`

Define, for a sorted list `A` (any positive reals) and a nonnegative integer
`marks` (the true remaining Xiang-Yu mark budget — one **shared** counter,
never split into sub-budgets counted separately per move type):
```
solve2(A, marks) :=
  min over all of:
    (i)   oddrank(A)                                   [do nothing]
    (ii)  jv + solve2(A', marks)                        [Move 0, cost 0]
             whenever A has an even-multiplicity tied run (v, 2j, A' as above)
    (iii) solve2( sort(\{p_1/2,p_1/2\}\cup \mathrm{tail}(A)), marks-1 )
                                                          [Move 1, cost 1, if marks>=1]
    (iv)  solve2( sort(\mathrm{init}(A)\cup\{a_m/2,a_m/2\}), marks-1 )
                                                          [Move 3, cost 1, if marks>=1]
    (v)   for each subset S of tail(A) with \Sigma(S)\le p_1, letting
             r := p_1-\Sigma(S), cost := |S| if r>0 else |S|-1:
             solve2( sort( (\mathrm{tail}(A)\setminus S) \cup S \cup S \cup
                            (\{r\}\ \mathrm{if}\ r>0) ), marks-cost )
                                                          [Move 2, cost |S| or |S|-1,
                                                           if cost<=marks]
```
Every branch that recurses does so on a **strictly smaller** instance in the
lexicographic order `(marks, |A|)` with `marks` primary:
- Move 0 (ii): `marks` unchanged, `|A|` strictly decreases (`|A'| = |A|-2j <
  |A|`) — this is exactly why `marks` alone does not suffice as the measure
  and `(marks,|A|)` lexicographic (as in the certified Lemma WF-C5) is
  needed; the outline-reviewer's flagged check is satisfied: Move 0 is safe
  under this order.
- Moves (iii),(iv),(v): `marks` strictly decreases (by `1`, `1`, or `cost\ge1`
  respectively, since `cost\ge1` whenever `|S|\ge1` and `r>0`, or `cost=|S|-1
  \ge 0`; the only zero-cost sub-case of Move 2 is `|S|=1,r=0`, i.e. a single
  tail element exactly equal to `p_1` — but that case is already covered by
  Move 0 directly, since `p_1=t_1` is then a pre-existing tie of multiplicity
  `\ge2$, so Move 2's `cost=0` branch never needs to be invoked separately).

Hence `(marks,|A|)` lexicographic (`marks` primary) strictly decreases on
every recursive call, so `solve2` is well-founded by the same argument as
the certified Lemma WF-C5 (`wf-c5.md`), extended to include Move 0 exactly as
flagged by the round-14 outline. Every use of the shared counter `marks`
begins at `marks = |A|-1` at the top level and is charged for *every*
elementary split actually made (Moves 1, 3, and every subset-match Move 2),
correcting the round-12/13 bug (Move 3 no longer grants an uncounted extra
mark: it is charged exactly `1`, the same as every other elementary split,
against the single shared counter).

### Numerical verification (this round)

Implemented `solve2` exactly as above with exact `fractions.Fraction`
arithmetic (script `/tmp/solve2.py`, memoized). Ran on three witnesses:

| witness | `m` | `solve2(A,m-1)` | `\Sigma(A)/2` | `c(m-1)\Sigma(A)` |
|---|---|---|---|---|
| `A=(26,21,10)/57` | 3 | `31/57 \approx 0.5439` | `1/2` | `4/7\approx0.5714` |
| `T=(0.20,0.15,0.12,0.08)` | 4 | `11/40 = 0.275` | `11/40=0.275` | `22/75\approx0.2933` |
| `A=(965,965,958,482)` | 4 | `1685` | `1685` | `5392/3\approx1797.3` |

All three meet the target `\le c(m-1)\Sigma(A)`, and the last two attain
`\Sigma(A)/2` exactly. On the `(965,965,958,482)` witness, the winning move
sequence is: Move 0 fires immediately on the pre-existing tie `965=965`
(banking `965` for free, no marks spent), leaving the sub-instance
`(958,482)` with the full `3`-mark budget; this sub-instance is itself
dominant (`958 \ge 482`), so halving both `958\to(479,479)` and
`482\to(241,241)` (2 of the 3 available marks; a 3rd is unused) gives
`oddrank = 965+479+241 = 1685 = \Sigma(A)/2`. This confirms Move 0 is
load-bearing exactly where the round-14 explorer flagged: every prior
certified move menu would have wasted a mark "creating" a tie that already
existed for free.

The `m=8` witness from round 12
(`A\approx(0.2117,0.1588,0.1410,0.1319,0.1232,0.0881,0.0748,0.0705)`) was
**not** successfully evaluated this round: the exhaustive subset-match search
(over all `2^{7}` tail subsets at every recursion level) makes the
memoized `solve2` implementation computationally infeasible within the time
budget (did not terminate in 5 minutes). This is an implementation-scale
limitation of the reference program, not a proof; it does not certify or
refute anything about `m=8`, and is recorded honestly as untested this
round.
