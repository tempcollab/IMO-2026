# Lemma V3-BOUND (certified, round 16)

**Status:** proved in full, independently re-verified by the proof-reviewer
(round 16). Recommend certifying.

## Statement

For every sorted triple `(x\ge y\ge z>0)`, writing `\sigma_3:=x+y+z`, the
certified `m=3` theorem `V_3` (the exact optimal Xiang-Yu value against a
3-piece Liu-Bang configuration, using `\le2` marks — proved case-by-case in
`lemmas/ptbi-threshold-reduction.md` Cases A/B and round 9's "`m=3` solved in
full" Case C closure) satisfies, unconditionally (no case restriction):
```
V_3(x,y,z) \le c(2)\,\sigma_3 = \tfrac47(x+y+z).
```

## Proof

Recall `V_3`'s three branches:
```
V_3(x,y,z) = x/2+L_2(y,z)          if x \ge c(2)\sigma_3 = 4/7\,\sigma_3   (Case A)
           = x                     if \sigma_3/2 \le x < 4/7\,\sigma_3     (Case B)
           = \min(x+z/2,\ y+L_2(x-y,z))   if x<\sigma_3/2                  (Case C)
```
where `L_2(u,v) = \max(u,v)` if `\max\le2\min`, else `\max/2+\min` (the fully
closed `n=1` theorem).

- **Case B:** `x<4/7\,\sigma_3` is the defining range, so `V_3=x<4/7\,\sigma_3`
  directly.
- **Case A:** by `lemmas/ptbi-threshold-reduction.md`'s Case-A argument
  applied at `m=3` (IH budget `1` on the pair `(y,z)`), `g(x):=x/2+c(1)
  (\sigma_3-x)` is strictly decreasing (slope `1/2-c(1)=1/2-2/3=-1/6<0`) and
  `g(4/7\,\sigma_3)=4/7\,\sigma_3`. Since `L_2(y,z)\le c(1)(y+z)=2/3(y+z)`
  (the `n=1` theorem's own bound), `V_3=x/2+L_2(y,z)\le g(x)\le g(4/7\,
  \sigma_3)=4/7\,\sigma_3` for `x\ge4/7\,\sigma_3`.
- **Case C:** exactly the content proved in round 9 ("`m=3`'s general upper
  bound is now solved in full, unconditionally over every configuration"):
  `\min(\mathrm{TAIL\text{-}SNIP},\mathrm{BLOCK\text{-}RECURSE}_1)\le c(2)
  \sigma_3=4/7\,\sigma_3` throughout `x<\sigma_3/2`, with equality
  approached (attained) at `(x,y,z)\propto(3,2,2)`. `\blacksquare`

## Independent verification (round 16, proof-reviewer)

Re-implemented `V_3`/`L_2` from scratch in exact `fractions.Fraction`
arithmetic (matching the three branches above verbatim) and ran 200,000
random-integer trials: zero violations of `V_3(x,y,z)\le c(2)(x+y+z)`.

## Scope / reuse note

This is a *loose* corollary of the already fully-certified `m=3` theorem —
it discards `V_3`'s exact case-by-case value in favor of one clean
unconditional bound, `c(2)\sigma_3`. Useful as a black box whenever a future
construction recurses into `V_3` and only needs the loose bound rather than
the exact value (as used by the round-16 `m=4` Case C Region 1/Region 2
closure, see `lemmas/m4-region-a-region-b.md`).
