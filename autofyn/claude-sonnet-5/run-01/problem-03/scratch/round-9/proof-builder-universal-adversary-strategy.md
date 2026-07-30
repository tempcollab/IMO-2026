# Round 9 build report — `universal-adversary-strategy`

## Target 1 (quick win): `m=3` Case C residual region — CLOSED IN FULL

Found and fixed a computational error in the round-8 write-up: BLOCK-RECURSE
`j=1`'s recursion target had been mislabeled `L=(p_2,r)` instead of the
correct `L_0=\{r,p_3\}` (per Lemma BLOCK-RECURSE's own statement, the
unmatched tail beyond the `j=1` prefix). This had made one worked example
(`(0.4,0.35,0.25)`) look like BLOCK-RECURSE failed (`0.575`) when the
correct value is `0.525` (succeeds, and in fact exactly equals TAIL-SNIP).

With the corrected closed form, `BLOCK-RECURSE_1(A) = 1-p_1` when
`p_3\le2(p_1-p_2)` and `= p_1+p_3/2` (exactly TAIL-SNIP) otherwise. A direct
2-case algebraic argument (splitting on `p_3\lessgtr2/7`) shows
`\min(\text{TAIL-SNIP},\text{BLOCK-RECURSE}_1)\le4/7` throughout **all** of
Case C (`p_1<\Sigma/2`), not just the previously-targeted sub-region
(`p_3>\Sigma/7`) — the argument needed no extra hypothesis beyond Case C
itself. Equality is attained exactly at the extremal point
`(p_1,p_2,p_3)=(3/7,2/7,2/7)` (both candidates give exactly `4/7`).
Independently verified: 200,000 exact-`Fraction` random trials over
`p_1<1/2`, zero violations, max found `≈0.571276` approaching but never
exceeding `4/7≈0.571429`.

**Result: `m=3`'s general upper bound is now fully solved, unconditionally
over every configuration** (combining with round 8's Cases A/B for
`p_1\ge\Sigma/2`).

## Target 2 (main): Lemma PAIR-VALUE (SUBSET-DOM without contiguity)

Verified the falsifying witness `A=(12,6,5,4,2)/29`, `m=5`, budget 4 first:
confirmed the existing menu tops out at `15/29≈0.5172 > c(4)=16/31≈0.5161`,
while `oddrank=1/2` is achievable by matching `p_2` to `{p_4,p_5}` (skipping
`p_3`) plus halving `p_1` and `p_3` — a non-prefix subset match BLOCK-RECURSE
cannot express.

Rather than a direct Hall's-theorem-based patch to BLOCK-RECURSE's
contiguity argument, found and proved a strictly more general fact:
**Lemma PAIR-VALUE** — if a multiset decomposes into any number of exactly
tied pairs (arbitrary values, *arbitrary relative position*, no domination
or contiguity assumption at all) plus an unpaired remainder, then
`oddrank = sum(pair values) + oddrank(remainder)`, unconditionally. Proved
by induction (remove one adjacent tied pair at a time; the resulting even
rank-shift preserves parity for everything else — a one-line argument).
Independently verified by 40,000 exact-`Fraction` random trials (wide and
narrow value ranges, to stress-test both generic interleaving and forced
value coincidences), zero mismatches.

This **strictly generalizes** Lemma DOUBLE-INSERT (`k=1`) and Lemma
BLOCK-RECURSE (`k` pairs, with the extra domination hypothesis that forces
contiguity — now shown unnecessary). Its SUBSET-DOM corollary extends
"split one piece to reproduce a subset of the others' values" from sorted
prefixes to **arbitrary subsets**, with the same clean value identity and
no extra hypothesis. Applied to the falsifying witness: matching `p_2` to
`{p_4,p_5}` exactly (1 mark, `r=0` boundary saving), halving `p_1` (1 mark)
and `p_3` (1 mark) — 3 marks total, all elements paired — gives exactly
`oddrank(B) = p_1/2+p_3/2+p_4+p_5 = 29/58 = 1/2 < 16/31 = c(4)`, closing the
witness (independently reproduced by direct computation on the full
8-element sorted multiset).

**Honest scope.** This resolves the round-9 plan's flagged technical risk
("BLOCK-RECURSE's contiguity does not automatically transfer to arbitrary
subsets") by showing contiguity was never actually load-bearing — not by
finding a workaround. It concretely closes the one falsifying witness. It
does **not** establish a general theorem that some donor/target-subset
choice always closes Case C for every `m≥4` — that would need Hall's
marriage theorem to handle simultaneous, non-conflicting multi-donor
matching, a genuinely separate existence question not attempted in general
this round. `m≥4`'s general Case C induction remains open.

## Files changed

- `/home/agentuser/repo/results/imo-2026-03/approaches/universal-adversary-strategy.md`
  — corrected the round-8 computational error; added the full round-9
  Target 1 closure and Target 2 (Lemma PAIR-VALUE) write-up; updated
  "Full proof" summary and "Promotable lemmas".
- `/home/agentuser/repo/results/imo-2026-03/lemmas/pair-value.md` — new
  certified lemma (Lemma PAIR-VALUE, full proof, numerical verification,
  SUBSET-DOM corollary, worked witness check).

## Recommended verdict

CHANGES REQUESTED (real progress on both targets; `m=3` fully solved as a
sub-result, `m≥4` Case C still open — the approach as a whole remains
`partial` since the general-`m` upper bound induction is not complete).
