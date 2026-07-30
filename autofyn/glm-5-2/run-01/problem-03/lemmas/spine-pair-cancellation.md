# Lemma: spine-pair-cancellation (S1)

**Statement.** Let `M=(a_1\ge a_2\ge\cdots\ge a_m)` be any sorted-descending multiset (dyadic
or not; any real values). If `a_i=a_{i+1}`, the pair `(a_i,a_{i+1})` contributes `0` to the
alternating sum `D(M)=a_1-a_2+a_3-\cdots`. Removing all adjacent-equal pairs (iteratively)
yields the **spine** `\operatorname{sp}(M)`: a strictly-decreasing sequence of DISTINCT
values, with

$$D(M) \;=\; D(\operatorname{sp}(M)).$$

The argument is **value-agnostic** — it uses no power-of-2 (dyadic) structure.

**Proof.** The pair `(a_i,a_{i+1})` at positions `i,i+1` contributes
`(-1)^{i+1}a_i+(-1)^{i+2}a_{i+1}=(-1)^{i+1}(a_i-a_{i+1})=0`. After removing the pair, every
surviving piece at old position `j>i+1` moves to new position `j-2`; its sign
`(-1)^{(j-2)+1}=(-1)^{j-1}=(-1)^{j+1}` (since `j-1\equiv j+1\pmod 2`) is UNCHANGED. So `D` is
preserved under each pair-removal. The iteration terminates (the multiset is finite, each
removal strictly decreases its size), reaching a strictly-decreasing spine with `D` preserved.
∎

**Verified.** 20 000 random configs with forced duplicates (mixed integer and rational values),
0 mismatches between `D(M)` and `D(\operatorname{sp}(M))`.

**Importable by:** `tower-induction` (the spine decomposition for the non-dyadic
generalization, Route D), `tail-count` (the pair-cancellation sub-step of the even-group
strong-breakpoint argument), `gaps-leftover` (the spine as the charging target). The
value-agnostic pair-cancellation is the common foundation for both the block/parity and the
PL/variational routes on the non-dyadic G1 wall.
