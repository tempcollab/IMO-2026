# Proof-builder report — bounded-window-distinctness (imo-2026-06, round 9)

**Status: partial** (route dead as a closer; no solve flip). File updated:
`results/imo-2026-06/approaches/bounded-window-distinctness.md`.

## What I was asked
Fill step 4 (window localization) of the value-difference distinctness route abstractly (Window Purity +
linear growth, NOT numerically, per the round-8 reviewer's two explicit warnings): cluster the infinite
connector pool Q(r_0) into a bounded value-window so distinctness-by-difference caps it.

## What I did
I executed the requested abstract argument for step 4. It does not close the gap; instead it **decides step 4
in the negative** with a crisp new theorem, sharpening my round-8 Proposition R:

- **(R2′) [new, round 9]** *If the new-large-prime-carrying witnesses lie in any bounded value-band
  [a_1, V), then Q(r_0) is finite.* Proof (pure term-finiteness, no numerics): those witnesses index at most
  V − a_1 distinct term-values, hence finitely many terms; Q(r_0) = ⋃ over them of the finite sets Q_i is then
  a finite union of finite sets. Contrapositive: Q(r_0) infinite ⟹ the contributing witnesses are unbounded
  in value.

**Consequence.** Distinctness-by-Difference (Step 3, my certified-in-file local lemma: a prime q > N divides
≤ 1 element of any value-window of length N) only bites inside a bounded window. By (R2′), confining the
new-prime witnesses to a bounded window is *equivalent* to Q(r_0) being finite — i.e. to the negation of the
very hypothesis ¬(FIN-Q) we must refute. The engine can only act where its own conclusion is already assumed.
This is an **impossibility argument for the distinctness closer**, argued abstractly (as required), and it
respects the reviewer's warning: (R2′) is stated purely in value bands a_i < V, never same-CLASS (mod M).

## Outcome vs. the two reviewer warnings
- Warning 1 (no numeric pre-check possible — CSP holds on every seed, no star ever inhabited): respected —
  the whole argument is abstract; I ran no seed hunt.
- Warning 2 (don't conflate same-CLASS unbounded differences with same-VALUE-WINDOW <N differences):
  respected — (R2′) and Step 3 are value-band statements only.

## Deliverables / salvage
- **Promotable (re-confirmed gap-free):** Distinctness-by-Difference (local) — for any I in a value-window of
  length N and prime q > N, q divides ≤ 1 element of I; #distinct primes >N dividing some element ≤ |I|.
  Self-contained, elementary, reusable.
- **Negative certification (sharpened):** Proposition R + new (R2′) — value-difference distinctness cannot
  refute ¬(FIN-Q); bars re-fielding value-difference counting/distinctness against ¬(FIN-Q).

## Recommendation to the orchestrator/outliner
Route verdict: **RETHINK** for this slug (no closing mechanism remains; step 4 is provably unachievable for
this mechanism, now with a crisp contrapositive, not a heuristic). Per the round-8 reviewer's diversity note,
round 9's outliner should NOT add a 4th reformulation of ¬(FIN-Q); the untried lever is the growth-RATE /
recruitment framing ("each new distinct connector q_k must appear as a factor of some term within a bounded
window, costing one slot per a_1-length window") — which is exactly the surface where (R2′) says a *counting
of slots against window length* could bite, but that is a density/recruitment argument, not a value-difference
count, so it belongs to a new slug, not this one.
