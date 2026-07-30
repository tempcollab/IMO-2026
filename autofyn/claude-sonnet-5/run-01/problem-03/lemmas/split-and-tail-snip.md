# Lemma DOM-boundary-slack, Lemma SPLIT, Lemma TAIL-SNIP (certified, round 5)

Source: `universal-adversary-strategy.md`, round 5. Independently
re-verified by the proof-reviewer: Lemma SPLIT against 11,000+ random
exact-`Fraction` trials (zero mismatches, both parity cases and both
boundary sizes of `R`); Lemma TAIL-SNIP's refuting counterexample
recomputed exactly (`A=(4649/10000,3042/10000,2309/10000)`, TAIL-SNIP value
`11607/20000 = 0.58035 > c(2)=4/7≈0.5714`, confirmed exact).

## Lemma DOM-boundary-slack

**Statement.** In Lemma DOM's setting (`A=(p_1≥...≥p_m)`, tail
`T=(p_2,...,p_m)`, `S=Σ(T)`), if `p_1 = S` exactly (the `r=0` boundary of
Lemma DOM), Xiang Yu can force `oddrank(B)=p_1` using only `k-1` marks
(`k=m-1`), not `k`. *Proof.* Split `p_1` directly into the `k` positive parts
`t_1,...,t_k` (forced, since they must sum to `p_1=S=Σt_i`); producing `k`
labelled parts from one piece costs `k-1` marks. Apply Lemma DOM's Step 1
(`oddrank(E)=S=p_1`). ∎

## Lemma SPLIT (general single-position halving)

**Statement.** For sorted `a_1≥...≥a_m`, index `i` with `a_i/2 ≥ a_{i+1}`
(vacuous if `i=m`), splitting `a_i` into two copies of `a_i/2` and writing
`R=(a_{i+1},...,a_m)`:
```
i odd:  oddrank(B) - oddrank(A) = -a_i/2 + 2·oddrank(R) - Σ(R)
i even: oddrank(B) - oddrank(A) =  a_i/2 + Σ(R) - 2·oddrank(R)
```
*Proof.* Rank-shift bookkeeping (the new pair occupies ranks `i,i+1`; `R`'s
elements shift by `i+1`, flipping parity iff `i` is even). Full derivation
in the approach file; independently verified by the proof-reviewer, 11,000+
random exact-`Fraction` trials, zero mismatches. Strictly generalizes the
already-certified Lemma HALVE (the `i=1` case reproduces it exactly).

## Lemma TAIL-SNIP (corollary of Lemma SPLIT, `i=m`)

**Statement.** Splitting the smallest element `a_m` of any sorted positive
list (no hypothesis needed) changes `oddrank` by exactly `-a_m/2` if `m` is
odd (strict decrease) or `+a_m/2` if `m` is even (strict increase).

**Certified negative result.** Lemma TAIL-SNIP alone does **not** close the
"neither DOM's nor HALVE's hypothesis fires" regime: exact counterexample
`A = (4649/10000, 3042/10000, 2309/10000)` (`n=2`, `m=3` odd, neither `p_1≥S`
nor `p_1≥2p_2` holds), TAIL-SNIP value `= oddrank(A) - a_3/2 = 11607/20000 =
0.58035 > c(2) = 4/7 ≈ 0.5714` — confirmed exact by the proof-reviewer. A
grid search over the true 2-mark optimum on this instance found the correct
response splits **two** pieces (`p_1` and `p_2`) simultaneously at
non-half ratios, not the single smallest piece — i.e. no single-piece move
(DOM, HALVE, or TAIL-SNIP) suffices in this regime; a coordinated
multi-piece move is required. Do not re-attempt a single-piece fix for this
regime without checking against this exact witness.
