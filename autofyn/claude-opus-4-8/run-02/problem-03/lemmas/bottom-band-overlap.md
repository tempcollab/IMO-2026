# Lemma: bottom-band overlap identity (value-threshold split of D̃)

Certified round 15 (from `bottom-band-peel-induction`, an otherwise-retired framing). Reviewer
re-derived from the certified SD/PEEL identity and reproduced with exact `Fraction`: 0 mismatches
over 30000 integer and fractional configs.

Notation: `N_P(t)=#{p∈P:p>t}`, `O_P={t>0:N_P(t) odd}`, `D̃(P)=λ(O_P)`.

## Statement

For any finite positive multiset `F` and any threshold `τ>0`, split by value
`F=F_{>τ}⊎F_{≤τ}`. Then
```
   λ(O_{F_{>τ}}∩O_{F_{≤τ}}) = D̃(F_{≤τ})·1[|F_{>τ}| odd],
```
and hence, via the certified SD identity `D̃(A⊎B)=D̃(A)+D̃(B)−2λ(O_A∩O_B)`,
```
   D̃(F) = D̃(F_{>τ}) + (−1)^{|F_{>τ}|} D̃(F_{≤τ}).
```

## Proof

Every part of `F_{≤τ}` is `≤τ`, so `N_{F_{≤τ}}(t)=0` for `t≥τ`, giving `O_{F_{≤τ}}⊆(0,τ)`. On
`(0,τ)` every part of `F_{>τ}` exceeds `t`, so `N_{F_{>τ}}(t)=|F_{>τ}|` is constant there; hence on
`(0,τ)`, `O_{F_{>τ}}` equals `(0,τ)` if `|F_{>τ}|` is odd and is empty if `|F_{>τ}|` is even.
Intersecting with `O_{F_{≤τ}}⊆(0,τ)` gives `λ(O_{F_{>τ}}∩O_{F_{≤τ}})=D̃(F_{≤τ})·1[|F_{>τ}| odd]`.
Substituting into SD yields the displayed value formula. ∎

## Remark (accounting tool, NOT a closer)

The even branch is additive; the odd branch is a difference and equals the certified DIFF/overlap
object the lower bound is stuck on — the bottom split is split-agnostic and does not escape GAP-P1.
Round-15 cheap-kill witnesses (verified): `F={2,2,1,1,1}` has `D̃=1` but the scale peel `G={2,2,1,1}`
has `D̃(G)=0` (so `D̃(G)≥2` fails on budget); `F={4,4,2,2,1,1,1}` has `D̃=1` but `F_{>1}={4,4,2,2}`
has `D̃=0` (surplus carried entirely by bottom fragments; `F_{>τ}` is not a feasible sub-instance).
Use only as an exact bottom-split accounting identity.
