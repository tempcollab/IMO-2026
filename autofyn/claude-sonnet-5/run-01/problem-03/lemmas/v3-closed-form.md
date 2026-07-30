# Lemma V3-CLOSED-FORM (certified, round 17)

**Status:** proved in full by hand; independently cross-checked against the
original recursive `V_3`/`L_2` definitions over 46,101 exact-`Fraction`
random trials restricted to `m=4` Case C's Region 3 (zero mismatches — see
`approaches/universal-adversary-strategy.md`'s round-17 build for the
verification script). Recommend certifying.

## Statement

For every sorted triple `x\ge y\ge z>0`, write `\sigma:=x+y+z`. Then
```
V_3(x,y,z) = \min\!\big(x/2+y,\; x/2+y/2+z\big)         if x\ge\tfrac47\sigma   (Case A)
           = x                                          if \sigma/2\le x<\tfrac47\sigma  (Case B)
           = \min\!\big(x+z/2,\; y+z\big)                if x<\sigma/2          (Case C)
```
i.e. **every branch of `V_3` is itself a min of at most two affine
functions of `(x,y,z)`** — in particular Case C, which in the definition
imported from `lemmas/ptbi-threshold-reduction.md` reads
`V_3=\min(x+z/2,\,y+L_2(x-y,z))` with `L_2` the (piecewise) `n=1` value, is
shown here to simplify to the affine-only form `\min(x+z/2,\,y+z)` — the
`L_2`-branch dependence disappears entirely once folded into the outer
`\min`.

## Proof

**Case A.** By definition `V_3=x/2+L_2(y,z)`. Since `y\ge z`, `M:=\max(y,z)
=y`, `m:=\min(y,z)=z`, and `L_2(y,z)=M` if `M\le2m` else `M/2+m`. Direct
check: `M\le2m\iff y\le2z\iff y\le y/2+z` (subtract `y/2` from both sides of
`y\le2z\iff y/2\le z`, i.e. `y\le y/2+z\iff y/2\le z\iff y\le2z` — same
condition). So on `y\le2z`, `M=y\le y/2+z`, i.e. `y` is the smaller of
`\{y,\,y/2+z\}`; on `y>2z`, `M/2+m=y/2+z<y`, i.e. `y/2+z` is the smaller.
Either way `L_2(y,z)=\min(y,\,y/2+z)` — a clean one-line closed form for
`L_2` once the larger argument is known. Hence `V_3=x/2+\min(y,y/2+z)=
\min(x/2+y,\;x/2+y/2+z)`.

**Case B.** Immediate from the imported definition (`V_3=x` is the raw DOM
value on this range, no recursion).

**Case C.** By the imported definition, `V_3=\min(x+z/2,\;y+L_2(x-y,z))`.
Write `u:=x-y\ge0` (since `x\ge y`), `v:=z`. The Case-C hypothesis `x<\sigma/2`
is equivalent to `x<y+z`, i.e. `x-y<z`, i.e. **`u<v`** — so inside Case C the
first argument of `L_2` is always the *smaller* of `(u,v)`: `M=v=z`,
`m=u=x-y`. Two sub-cases on `L_2`'s own threshold:

- *If `z\le2u`* (i.e. `M\le2m`): `L_2(u,v)=z` exactly, so
  `y+L_2(x-y,z)=y+z` exactly — not merely a bound, an equality. Hence
  `\min(x+z/2,\,y+L_2(x-y,z))=\min(x+z/2,\,y+z)` trivially (same two
  numbers).
- *If `z>2u`* (i.e. `M>2m`): `L_2(u,v)=z/2+u=z/2+(x-y)`, so
  `y+L_2(x-y,z)=y+z/2+x-y=x+z/2` exactly — again an equality, and it
  matches the *other* term of the outer min. So
  `\min(x+z/2,\,y+L_2(x-y,z))=\min(x+z/2,\,x+z/2)=x+z/2`. We must also
  check this equals `\min(x+z/2,y+z)`: since `z>2u\Rightarrow u<z/2
  \Rightarrow x-y<z/2\Rightarrow x+z/2<y+z`, so indeed
  `\min(x+z/2,y+z)=x+z/2`, matching.

In both sub-cases `\min(x+z/2,\,y+L_2(x-y,z)) = \min(x+z/2,\,y+z)` exactly
(not just `\le`), so `V_3=\min(x+z/2,\,y+z)` throughout Case C,
unconditionally on which of the two `L_2` sub-thresholds holds. `\blacksquare`

## Remark (reusability)

This lemma removes the need to ever invoke `L_2`'s own DOM/HALVE case split
directly when working with `V_3` — every one of `V_3`'s three top-level
branches is already a min of at most two *affine* functions of `(x,y,z)`,
making `V_3` (and hence any `V_3`-recursing strategy, restricted to a region
where its top-level branch is fixed) piecewise-linear with an explicit,
small, finite set of linear pieces. This is the tool used in round 17 to
get exact (non-loose) closed forms for `\mathrm{StratA}`, `\mathrm{StratB}`,
`\mathrm{StratC}_{23}` on `m=4` Case C's Region 3 — see
`approaches/universal-adversary-strategy.md`'s round-17 build and
`lemmas/m4-region-c-closure.md`.
