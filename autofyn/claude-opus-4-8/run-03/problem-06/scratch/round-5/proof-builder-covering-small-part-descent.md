# Build report — covering-small-part-descent (round 5)

**Status: partial** (advanced; one of the two open sub-gaps now closed).

## What I did
Advanced the value-ascent carrier. Steps 1–5 were already certified. I **closed sub-step (6a)**
(the "unbounded bad-term family" gap that stalled the field for 3+ rounds) with a short, rigorous
argument built only on the certified Realizability lemma.

### New result — Lemma 6 (bad-signature geometric family), Step 6, COMPLETE
If `m` is a bad term, then for every prime `r ∣ m` and every `k ≥ 0`, `m·r^k` is again a bad term,
with `S(m·r^k) = S(m)` and the SAME witness. Hence one bad term forces infinitely many, unbounded
above, all with a fixed non-covering signature.

Proof (one paragraph): `m` a term ⇒ `primes(m)` covering (Realizability, `𝒯⊆𝒞`). For `r∣m`,
`primes(m·r^k) = primes(m)` ⊇ covering set and `m·r^k ≥ a_1`, so by Realizability (every integer
`≥ a_1` whose prime set contains a covering set is a term) `m·r^k` is a term. Its small part equals
`S(m)`, non-covering with the same witness `B`, so `m·r^k` is bad. `r≥2` ⇒ strictly increasing.

This **bypasses the symmetric-ascent obstruction entirely** — it does not use Step 5's single
upward step, so the round-4 blocker ("the partner of `m_1` may be `m_0` again; no fresh larger bad
term; can't exclude a largest bad term") is moot. The finite-signature pigeonhole becomes trivial:
every family member shares one signature.

## What remains open — (6b) alone (the sharpened crux)
Even with an unbounded bad-term family there is no contradiction yet. The residual gap is now the
crisp statement **"no term has a non-covering small part"** (= CSP), which by the Prop D barrier
MUST use greedy value, not covering combinatorics alone; and by Lemmas C1–C3 the global Σ1/p²
capacity count is provably insufficient (caps a positive fraction, never zero). I checked and
recorded that the **aimo-0016 "infinitely-often ⇒ always" template does not transplant**: our finite
signature alphabet carries no per-term-index local recurrence (only unbounded multiplicative gaps
`m·r^k`), so its downward-induction / windowed-sum transport step has no analogue.

## Cross-approach payoff
Lemma 6 makes **automatic** the hypothesis that the two sibling framings' Step-5 pigeonhole needs
and previously could not assume: "some residue class in `R_bad` is inhabited by infinitely many bad
terms" (the family `m·r^k mod L_0` cycles finitely many residues). Recommend the reviewer certify
Lemma 6 into `lemmas/` so `bad-residue-witness-index` and `minimal-linking-prime-extremal` can
import it.

## Verification
Computational (a_1∈{15,35,231}, 400 terms): CSP holds (0 bad terms); `S(m·r)=S(m)`; `m·r` is a term.

## Files
- Wrote: `results/imo-2026-06/approaches/covering-small-part-descent.md` (Steps 6–7 rewritten;
  Status/Approaches/Current best/Promotable updated; Lemma 6 added as promotable).

## Recommendation to orchestrator
Route: **CHANGES REQUESTED** (real progress, gap remains). The single shared wall is now precisely
(6b) for all three live framings; Lemma 6 removed (6a) from the shared crux and unblocked the
siblings' pigeonhole. If (6b) persists next round, the reviewer's contingency (seed a framing
attacking the greedy DYNAMICS of the actual successor `a_{n+1}` directly) is the right escalation.
