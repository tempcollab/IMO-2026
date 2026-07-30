# Proof-builder report — covering-small-part-descent (round 9)

Problem: imo-2026-06 (IMO 2026 P6, greedy-gcd sequence eventual periodicity). answer_type: none.
Status: **partial** (advanced). Elo 1660 top live carrier, kept in lane (crisp value target, value descent).

## What I did
Leaned on the essential-witness value pressure the reviewer directed (each essential witness B_p is a
term ≥ a_1), NOT on re-deriving Window Purity (which the reviewer flagged adds no leverage here — I did
not touch it). Delivered two gap-free lemmas that recast the crux (6b/CSP) into its crispest
value/arithmetic form.

## New gap-free results
- **Lemma 13 (Essential-connector equivalence, (EC)).** CSP fails ⟺ some **large** prime q is an
  *essential connector* for some non-covering prime set A — i.e. every A-avoiding term (primes ∩ A = ∅)
  is divisible by q; equivalently A non-covering but A∪{q} covering. Hence CSP ⟺ **(EC): for every
  non-covering A and large q, some A-avoiding term is not divisible by q.** Both directions proved:
  (⟹) from Lemma 10 (a minimal cover C' with large q, take A=C'\{q}) + REAL 𝒯⊆𝒞; (⟸) A∪{q} covering,
  contains a minimal cover C''⊄A so q∈C'', CSP fails by Lemma 10. Companion (W-inf): the A-avoiding
  terms W_A are infinite (multiply a witness by a fresh prime r∉A, REAL c) and all ≡ 0 (mod q).
- **Lemma 14 (Essentiality propagation).** In any failing config (A,q), every A-avoiding term B has
  primes(B)\{q} non-covering (else realize that covering set by REAL c to get a q-coprime A-avoiding
  term — contradiction). So (primes(B)\{q}, q) is again a failing config with the SAME q.

## Why this is genuine progress
(EC) is the value form of the crux — a pure term-divisibility statement — distinct in phrasing from the
sibling's set-theoretic ℰ-small-only, exactly this lane's mandate. It's the sharpest handle yet: it
converts "no minimal cover carries a large prime" into "no large prime divides every A-avoiding term."
Lemma 14 identifies precisely why the naive value lever (realize primes(B)\{q}) fails — the failing
case blocks it — which is a useful pruning fact.

## Honest gap (unchanged in kind)
Lemma 14 preserves q: the config self-reproduces with q, rad, and set-size all recurring. No well-founded
monovariant exists on essential-connector configs (A,q). So the value/essential-witness mechanism stalls
at the same wall it has since round 5. To close (EC) one must force SOME A-avoiding term coprime to q —
a genuinely new lever, not available from realizability alone. I did not overclaim: Status stays partial.

## Barred-dead closures respected
Did not re-field: global Σ1/p² capacity; pure covering/Helly (Prop D); symmetric bad-partner ascent;
the (q*,k) active rewrite; and (per reviewer) did not lean on RED_n or Window Purity.

## Promotable (recommend certifying)
1. Lemma 13 — Essential-connector equivalence + (W-inf). Gap-free.
2. Lemma 14 — Essentiality propagation. Gap-free.
(Plus previously-proposed Lemmas 10, 12 still standing.)

File: results/imo-2026-06/approaches/covering-small-part-descent.md (Lemmas 13, 14 added; meta sections
updated). Suggested route: CHANGES REQUESTED (real advance, gap remains).
