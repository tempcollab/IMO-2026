# Lemma: spacing fact (large primes in a short window)

## Status
CERTIFIED (round 2, proof-reviewer). Proved in `approaches/small-prime-window-lemma.md` §4/Lemma 3.

## Statement
Let `R ≥ 1` and `W = (x, x+R]` be a window of length `R`. Every prime `q > R` divides at most one integer of `W`.

## Proof
Two distinct multiples of `q` differ by at least `q`. The window `W` has length `R < q`, so it cannot contain two distinct multiples of `q`. ∎

## Scope / reusability
The structural input for any spacing-based attack on `imo-2026-06`'s crux B1'. Genuinely weak on its own — at `a_1=35, n=221`, large past primes collectively touch `15` of the `35` window slots — but it is the rigorous foundation for the value-bound / unkillable-window lemma.
