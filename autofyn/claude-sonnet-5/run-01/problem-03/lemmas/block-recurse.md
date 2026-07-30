# Lemma BLOCK-RECURSE (recursive generalization of PARTIAL-DOM / PARTIAL-DOM-RESIDUAL)

**Status:** proposed by the round-8 explorer (numerically verified,
`m=3..9`, thousands of exact-`Fraction` trials, zero failures, plus exact
ties at the geometric extremal configs `n=1..7`), **proved in full below**
by the round-8 builder (`universal-adversary-strategy`). Recommend
certifying.

## Statement

Let `A = (p_1 ≥ p_2 ≥ ⋯ ≥ p_m)` be any sorted list of positive reals,
`T = (t_1,\ldots,t_k) := (p_2,\ldots,p_m)` (`k=m-1`), `S_j := t_1+\cdots+t_j`
for `0\le j\le k`. Fix `1\le j\le k` with
```
p_1 \ge S_j   and   r := p_1 - S_j < t_j.
```
(These are exactly Lemma PARTIAL-DOM's hypotheses, certified in
`lemmas/partial-dom.md`, applied at this `j` — `j` need not be maximal.)
Using exactly `j` marks, split `p_1` into the `j+1` parts
`t_1,\ldots,t_j,r`; merge with the full tail `T` to form the intermediate
multiset. Write `U := (t_{j+1},\ldots,t_k)` (the *unmatched* tail) and
`L_0 := \{r\}\cup U`, so `\Sigma(L_0) = p_1 + \Sigma(T) - 2S_j`.

Then, for **any** further refinement `W` of `L_0` obtained by repeatedly
splitting elements of `L_0` into positive parts (any depth, any number of
splits, in particular the result of applying an arbitrary Xiang-Yu-style
recursive strategy to `L_0` as its own independent sub-instance), the final
merged multiset `B := \{t_1,t_1,\ldots,t_j,t_j\}\cup W` satisfies, exactly:
```
oddrank(B) = S_j + oddrank(W).
```
This holds **unconditionally** in the choice of `W` — no hypothesis on `W`
beyond "`W` is some refinement of `L_0`" is needed. If the recursive
response to `L_0` uses `b` further marks, the total mark count is `j+b`.

## Proof

**Step 0 (monotonicity of the max under splitting).** If `w` is obtained
from a positive real `v` by repeated splitting (each split replaces one
positive value by two positive parts summing to it), every value appearing
in the resulting multiset is `\le v`: a single split replaces `v` by two
parts each `< v` (both positive, summing to `v`), and this property is
preserved under further splitting of those parts (each subsequent split
again only produces parts `\le` the value being split). By induction on the
number of splits, every element of any refinement of a multiset `L_0` is
`\le \max(L_0)`.

**Step 1 (leftover is dominated by the block, always).** By Step 0 applied
to each element of `L_0=\{r\}\cup U`, every element of `W` is
`\le \max(L_0) = \max(r, t_{j+1})`. By hypothesis `r < t_j`, and by
sortedness `t_{j+1}\le t_j`, so `\max(r,t_{j+1}) \le t_j`. Hence
```
\max(W) \le t_j = \min\{t_1,\ldots,t_j\}.
```

**Step 2 (sorted order of `B`, tie-insensitive).** Write
`\text{Block} := \{t_1,t_1,t_2,t_2,\ldots,t_j,t_j\}` (`2j` elements, each
`\ge t_j`). By Step 1, every element of `W` is `\le t_j \le` every element
of `\text{Block}`. Consequently, in any sorted (descending) arrangement of
`B = \text{Block}\cup W`, the `2j` elements of `\text{Block}` occupy ranks
`1,\ldots,2j` and the elements of `W` occupy ranks `2j+1,\ldots,2j+|W|`,
**with `W`'s own internal sorted order preserved inside that block of
ranks**. (If there is an exact tie `t_j = \max(W)`, the assignment of which
specific tied copies sit at which of the boundary ranks is ambiguous, but
`oddrank` is a function of the multiset of values only — a sum over a fixed
set of rank-positions of numbers that are literally the same real number
does not depend on which formal copy is placed at which position, only on
how many of the boundary ranks are odd, and that count is determined
purely by `j` and `|W|`, not by the tie-break. So the "Block occupies ranks
`1..2j`" description below is a valid representative sorted order and gives
the correct value regardless of any exact ties at the boundary.)

**Step 3 (contribution of the block).** As in Lemma DOM's proof (Step 1)
and Lemma PARTIAL-DOM's construction: for each `i=1,\ldots,j`, the pair of
copies of `t_i` occupies ranks `2i-1` (odd) and `2i` (even), so the block
contributes exactly `t_1+t_2+\cdots+t_j = S_j` to `oddrank(B)`, regardless
of the internal tie-break order among equal values (each pair contributes
its common value once, to the odd-ranked copy, whichever specific copy that
formally is).

**Step 4 (contribution of `W`).** `W`'s elements occupy global ranks
`2j+1,\ldots,2j+|W|`; local rank `\rho$ of `W` (in `W`'s own sorted order)
maps to global rank `2j+\rho`. Since `2j` is even, global parity equals
local parity: local odd ranks of `W` map to global odd ranks, and vice
versa. Hence `W`'s contribution to `oddrank(B)` is exactly `oddrank(W)`
(computed in `W`'s own sorted order, unaffected by anything outside `W`).

**Step 5 (total).** Summing Steps 3 and 4:
```
oddrank(B) = S_j + oddrank(W).
```
This did not use any property of `W` beyond Step 1 (`\max(W)\le t_j`),
which Step 0 establishes for *every* refinement of `L_0`, at *any* depth.
Hence the identity holds for the result of an arbitrary recursive strategy
applied to `L_0`, not merely a single further split — proving the claim.
∎

## Budget conservation (recursion-depth induction)

**Claim.** If the top-level instance has size `m` and is given budget
`m-1`, and BLOCK-RECURSE is applied with parameter `j` (costing `j` marks
on `p_1`), then the recursive sub-instance `L_0` (of size `m-j`, since
`|L_0| = 1+|U| = 1+(k-j) = 1+(m-1-j) = m-j`) is given exactly the
correct budget `(m-j)-1 = m-1-j` — i.e. total marks used telescopes
exactly to `m-1`, never exceeding budget, by induction on recursion depth.

**Proof.** Base case (depth `0`, no further recursion): the sub-instance
`L_0` of size `m-j` is handled by *some* base construction (e.g. "do
nothing", `0` marks, always valid and within any budget `\ge 0`), and
`j + 0 = j \le m-1$ (since `j\le k=m-1`), within budget. Inductive step: if
the sub-instance `L_0` (size `m-j`, budget `m-1-j`) is itself handled by
recursively applying BLOCK-RECURSE (or any other budget-`\le(m-j)-1`
construction, by the inductive hypothesis on strictly smaller size), it
uses `\le (m-j)-1 = m-1-j` marks by assumption, so the top-level total is
`\le j + (m-1-j) = m-1`. By strong induction on size, every finite
recursion depth telescopes to a total of `\le m-1` marks. `∎`

## Recovering PARTIAL-DOM and PARTIAL-DOM-RESIDUAL

Taking `W = L_0` itself (no further refinement, `0` extra marks) recovers
exactly Lemma PARTIAL-DOM's formula `oddrank(B)=S_j+oddrank(L_0)`. Taking
`W` = one further Lemma-SPLIT application to `r` inside `L_0` recovers
exactly Lemma PARTIAL-DOM-RESIDUAL. BLOCK-RECURSE strictly generalizes both
by allowing `W` to be the result of *any* further (possibly deeply
recursive) refinement of `L_0`, proving the identity holds uniformly at
every depth — this is the mechanism needed to set up a strong induction on
piece-count for the general upper bound (Claim PTBI).
