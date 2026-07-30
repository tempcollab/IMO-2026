# Dual-objective shift under an untouched dominant element (certified, round 5)

Source: `potential-averaging-bound.md`, "Promotable lemmas." Verified
correct by the proof-reviewer (short direct rank-shift argument, no
independent numeric check needed beyond inspection — this is algebraically
immediate).

**Statement.** If `B = {p_1} ∪ T'` where `p_1 ≥` every element of `T'` (so
`p_1` occupies rank 1 of `B`), then
```
oddrank(B) = p_1 + evenrank(T').
```

**Proof.** Every internal rank `i` of `T'` becomes global rank `i+1` in `B`;
odd global rank ⟺ even internal rank; summing the included (odd-global)
terms plus `p_1` itself gives the identity.

**Note.** This is the same mechanism already used (in equivalent form) in
the certified `geometric-configuration-facts.md` (Proposition A) and in
`generalized-domination-and-halving.md` (Lemma DOM's rank-shift-by-1 step);
it is certified here as a standalone, dependency-free statement (no
geometric structure, no domination hypothesis beyond `p_1` being an
already-established maximum) for direct reuse by any approach that recurses
on "leave the top piece untouched," without needing to re-derive it from a
larger construction each time.
