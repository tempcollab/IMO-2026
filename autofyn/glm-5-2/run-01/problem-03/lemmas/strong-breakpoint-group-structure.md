# Lemma: strong-breakpoint-group-structure (S2)

**Statement.** Recall (`pl-breakpoint-minimum`) that a **strong breakpoint** is a refined
config in which every fragment (every split-product piece) ties an adjacent piece in the
sorted order. At a strong breakpoint of a refinement of `T_n=(2^n,\dots,2,1)`:

(i) every DYADIC fragment (value `2^k`) ties another dyadic fragment of the same value
(there are at least two copies of every dyadic value that survives into the spine);

(ii) every NON-dyadic fragment (value `\notin\{2^k\}`) cannot tie a tower piece (all tower
pieces are powers of 2), so it must tie ANOTHER non-dyadic fragment of the SAME value.
Consequently the non-dyadic fragments partition into adjacent-equal GROUPS of size `\ge 2`
in the sorted order.

**Corollary S2.** An EVEN-count non-dyadic group (size `2r`) fully cancels (it is `r`
adjacent-equal pairs, each contributing `0` by `spine-pair-cancellation`). An ODD-count group
(size `2r+1\ge 3`) leaves exactly ONE leftover of that value in the spine.

**Proof.** (i) A dyadic fragment of value `2^k` at a strong breakpoint ties an adjacent piece
of the same value `2^k` (a tie is an equality of adjacent sorted values); that adjacent piece
is itself dyadic. So dyadic values that appear do so at least twice, except those that survive
unpaired into the spine (odd count).

(ii) A non-dyadic fragment has value `v\notin\{2^k:k\ge 0\}`. Every tower piece has value in
`\{2^k\}`, so `v` cannot equal any tower piece. The strong-breakpoint hypothesis guarantees
the fragment ties an adjacent piece; that tie must therefore be to another non-dyadic fragment
of value `v`. Grouping adjacent-equal non-dyadic fragments gives groups of size `\ge 2`.

The Corollary follows from `spine-pair-cancellation` (S1): a group of size `2r` is `r`
adjacent-equal pairs (each contributing `0`); a group of size `2r+1` is `r` canceling pairs
plus one survivor. ∎

**Verified.** Constructed strong breakpoints of `T_n` for `n=2,3,4`: dyadic and non-dyadic
groups match the predicted structure; even groups cancel, odd groups leave one leftover.

**Importable by:** `tower-induction` (Route D), `tail-count` (the pair-cancellation
even-group sub-step), `gaps-leftover` (the spine-structure base case). The structural
input for `even-group-spine-lower-bound` (S3).

**Depends on:** `spine-pair-cancellation` (S1), `pl-breakpoint-minimum`.
