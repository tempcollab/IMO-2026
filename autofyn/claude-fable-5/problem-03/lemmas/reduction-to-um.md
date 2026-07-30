# Lemma: reduction-to-um (Target U ⟸ Claim U(n+1))

*Proposed by the discrepancy-halving builder, round 3. **CERTIFIED by the proof-reviewer, round 4**: padding (T4), tied-pair bookkeeping (T3 applied once per retired pair), and cut legality (every cut at an interior point of an existing physical piece, hence a fresh distinct mark; ≤ n cuts total; zeros never cut since Bisect/Match require positive arguments) re-checked line by line. Content extracted verbatim from `approaches/discrepancy-halving.md` §§0–1 and 3. Imports the certified `lemmas/greedy-claiming.md` and `lemmas/threshold-identity.md`.*

## Statement

Define, for a finite multiset S of nonnegative reals sorted descending, Δ(S) := p₁ − p₂ + p₃ − ⋯ (alternating sum). Let

**Claim U(m):** *for every multiset A of m ≥ 1 nonnegative reals with sum T, a sequence of at most m − 1 Bisect/Match/FreeRetire moves (defined below) reaches an active multiset A_end with Δ(A_end) ≤ β := T/(2^m − 1).*

Then **U(n+1) implies the upper bound c(n) ≤ (1 + u)/2 = 2^n/(2^{n+1} − 1)**, u := 1/(2^{n+1} − 1). (Combined with the certified `lemmas/ladder-resists.md`, U(n+1) therefore pins c(n) = 2^n/(2^{n+1}−1).)

## The move process

Xiang acts on an *active multiset* A of piece lengths; each move uses ≤ 1 cut and *retires* pieces never touched again:

- **Bisect(L)** [1 cut], L > 0 active: cut L at its midpoint; retire the exactly-tied pair (L/2, L/2); A ← A ∖ {L}.
- **Match(L, S)** [1 cut], L > S > 0 both active: cut L at distance S from an end into (S, L−S); retire the exactly-tied pair {new sub-piece S, old piece S}; A ← A ∖ {L, S} ∪ {L−S}.
- **FreeRetire(L, L)** [0 cuts], two equal active pieces: retire both; A ← A ∖ {L, L}.

## Proof of the reduction

By **Corollary R** (`lemmas/greedy-claiming.md`), c(n) = sup_a inf_x odd(S(a,x)) with a = Liu's partition of 1 into ≤ n+1 positive parts, x = Xiang's reply (≤ n cuts at interior points, all marks distinct), S(a,x) the final multiset. By the **discrepancy identity** (T1 of `lemmas/threshold-identity.md`), odd(S) = (1 + Δ(S))/2 when ΣS = 1. So it suffices to show: for every a, some legal x has Δ(S(a,x)) ≤ u.

Fix a and pad it with zero entries to exactly m = n+1 entries (harmless: zero-padding changes neither odd nor Δ, by T4 of `threshold-identity`; zeros are bookkeeping only and are never cut). Run any move sequence provided by U(n+1) (T = 1, β = u, budget m − 1 = n cuts). Legality as a Xiang reply: every cut is placed at an interior point of an existing physical piece (Bisect: the midpoint, 0 < L/2 < L; Match: distance S from an end, 0 < S < L), hence is a new mark distinct from all previous marks; at most n cuts are used. Zero entries are never the argument of a cut (Bisect and Match require positive arguments).

Let A_end be the final active multiset. The final piece multiset of the stick is S = (all retired tied pairs) ∪ A_end, and by **tied-pair invariance** (T3 of `threshold-identity`), applied once per retired pair,

Δ(S) = Δ(A_end) ≤ u.

Hence inf_x odd(S(a,x)) ≤ (1 + u)/2 for every a, i.e. c(n) ≤ (1+u)/2 = 2^n/(2^{n+1}−1). ∎

## Remarks
- Xiang may use fewer than n cuts; stopping early is legal (the game allows ≤ n marks).
- If Liu uses fewer than n+1 pieces the padding supplies the missing entries; the physical stick is unchanged.
- The reduction is tight: on the dyadic ladder, `ladder-resists` shows no reply gets Δ < u, matching U(n+1)'s bound exactly.
