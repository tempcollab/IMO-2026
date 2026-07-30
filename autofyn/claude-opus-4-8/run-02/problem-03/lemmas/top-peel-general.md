# Lemma: general top-peel of D̃ (MAXPEEL) and its arbitrary-blue red-peel corollary (I3′)

Notation: for a finite positive multiset `P`, `N_P(t)=#{p∈P: p>t}` and by the certified
**Lemma G** (level-measure / alternating-sum form)
`D̃(P)=∫_0^∞ 1[N_P(t) odd]\,dt = Σ_i(−1)^{i−1}w_i` (`w` sorted descending, tie-invariant).
`Δ(A,B):=½(D̃(A⊎B)−ΣA+ΣB)`.

## Statement

**(MAXPEEL) General top-peel.** For ANY finite positive multiset `P` with maximum `y=max(P)`,
```
    D̃(P) = y − D̃(P∖{y}).
```

**(I3′) Arbitrary-blue red-peel (corollary).** Let `R` be a finite positive multiset with
`y=max R`, and `Z` any finite positive multiset with every part `< y` (in particular any blue
with all parts `≤ θ:=2^{m−1} < y`). Then `y` is the global maximum of `R⊎Z` and
```
    D̃(R⊎Z) = y − D̃((R∖{y})⊎Z),
    equivalently   Δ(R,Z) = y − ΣR + ΣZ − Δ(R∖{y}, Z).
```

## Proof

**(MAXPEEL).** Write the descending sort of `P` as `y=w_1 ≥ w_2 ≥ … ≥ w_k`. Then
`P∖{y}` has descending sort `w_2 ≥ … ≥ w_k`, so by Lemma G
`D̃(P∖{y}) = Σ_{i≥2}(−1)^{i}w_i = −Σ_{i≥2}(−1)^{i−1}w_i = w_1 − D̃(P)`.
Hence `D̃(P) = w_1 − D̃(P∖{y}) = y − D̃(P∖{y})`. ∎

(Measure-form proof, equivalent: for `y=max(P)`, `N_P=0` on `(y,∞)`, and on `(0,y)`,
`N_P = N_{P∖{y}} + 1`, so `1[N_P odd] = 1 − 1[N_{P∖{y}} odd]` there, and integrating over `(0,y)`
gives `D̃(P)=y−D̃(P∖{y})` since `D̃(P∖{y})=∫_{(0,y)}1[N_{P∖{y}} odd]`.)

**(I3′).** Since every part of `Z` is `< y = max R`, `y` is the global maximum of `R⊎Z` and
`(R⊎Z)∖{y} = (R∖{y})⊎Z`. Apply (MAXPEEL) to `P=R⊎Z`:
`D̃(R⊎Z)=y−D̃((R∖{y})⊎Z)`. The `Δ`-form follows by adding the two `Δ`-definitions:
`Δ(R,Z)+Δ(R∖{y},Z)=½(D̃(R⊎Z)+D̃((R∖{y})⊎Z))−½(2ΣR−y)+ΣZ = ½·y −ΣR+½y+ΣZ = y−ΣR+ΣZ`
(using `D̃(R⊎Z)+D̃((R∖{y})⊎Z)=y`). ∎

## Scope / relation to certified (I3)

This strictly generalizes the certified red-peel `(I3)` of `base-slice-star.md`, which assumed
blue `= L_m` (the full uncut ladder). (I3′) needs only that every blue part is smaller than the
peeled red `y`; MAXPEEL needs nothing at all (any multiset, peel its global max). Both are
immediate consequences of Lemma G's alternating-sum form. Useful to reduce any blue-`=F'` lower
bound to the all-red-`≤θ` regime by peeling each red `> θ` in turn without changing scale.

**Caveat (do NOT over-read).** MAXPEEL/(I3′) reduce `ΣR` but do NOT reduce the dyadic scale `m`
and do NOT close the b-lift: after peeling all large reds, closing `D̃(π_0⊎F')≥1` still requires
controlling the split-top-rung overlap `λ(O_{ρ_1}∩O_{R⊎Z'})` (the certified GAP-P1 wall). These
lemmas are bookkeeping tools, not a closer.

## Verification (exact `Fraction`)

- MAXPEEL: `0` fails / `5·10³` random multisets.
- (I3′): `0` fails / `2048` tested configs (random `m∈{2,3,4}`, blue parts `≤θ`, `y=maxR>θ`).
- Reviewer re-derived both from Lemma G's alternating-sum form and reproduced the numerics.

Certified round 14 (proof-reviewer). Source approaches: `absorb-rescale-induction` (MAXPEEL),
`split-rung-mutual-induction` (I3′). Supersedes both banked forms as a single master lemma.
