## imo-2026-03 (lens: go/no-go on TAIL-SNIP framing for Case C)

- Distinct openings:
  1. **STAY, reframed.** Per the sibling lens (`math-explorer-taildominant.md`,
     already in this round's `/tmp/round-13/`), the round-12 "tail locally
     dominant" gap was a strawman: tracing `A=(45,40,6,5,4)/100` shows the
     existing budget-1 recursion already reaches `Σ/2` exactly (snip fires
     3 levels down inside `tail(A)`'s own call on `(6,5,4)`), not via a
     naive pure-Move-1 IH. The real target is a clean, general claim: **"a
     single global snip, placed correctly somewhere in the recursion tree,
     always suffices to reach `Σ(A)/2` in Case C"** — an induction on
     `|A|` (strong/complete, not one-step peeling) tracking the *existence*
     of a good snip location, not a value inequality conditioned on a local
     predicate at the top level.
  2. **Potential/counting reframing** (untried so far): instead of casework
     on "is the tail locally dominant," define a potential
     `Φ(A) = Σ(A)/2 - solve_full(A,budget=1)` and show `Φ≥0` by strong
     induction using only the identity `solve(A,1) ≤ p_1/2 + solve(tail,1)`
     together with a base-case argument for when `tail` itself is small
     (`|tail|≤2`), rather than a global structural case split. This may
     collapse the "locally dominant chain" casework into one clean
     induction with a sharper IH (carry `budget∈{0,1}` explicitly as part
     of the statement, prove both `solve(A,0)≤f_0(A)` and `solve(A,1)≤Σ/2`
     jointly by mutual strong induction).
  3. **Exchange-argument/extremal framing**: the cascading family
     `p_i=(1/2-ε)R_i` (sibling's finding) hits the bound with margin
     exactly 0 for every `m` tested — this is very likely the *true*
     extremal configuration for Case C's induction step. A proof strategy
     built around showing this family is extremal (via an exchange/
     smoothing argument: any deviation from the cascade only helps Xiang
     Yu) could shortcut the general casework, analogous to how the
     already-certified lower-bound side used a fixed extremal `A_n`.

- Candidate technique(s): strong induction on `|A|` with an existential
  ("some snip location works") rather than universal-predicate IH; possibly
  paired with an exchange/smoothing argument isolating the cascading family
  as extremal.

- Cheap-kill candidates: none new found. Checked (independently, via the
  sibling's scripts' logic, not rerun from scratch due to time) that parity
  of `m` does not discriminate when budget=0 alone suffices (~99% failure
  both parities) — rules out a cheap parity-based case split as the fix.

- Knowledge-base / crux corpus query (combinatorics, `games-and-strategy`,
  `extremal-principle`, `invariants-and-monovariants`, `graph-theory-and-
  connectivity`): scanned ~2400 cruxes for potential-function, exchange-
  argument, duality-certificate, and Hall-matching technique text.
  **`aimo-0063`'s Hall-deficient-set-deletion** (iteratively delete a
  Hall-violating set + its neighborhood until survivors satisfy Hall,
  using a universal vertex to force nonempty terminal matching) is a
  genuine bipartite-matching/SDR tool — but Case C's gap, as now correctly
  reframed by the sibling lens, is *not* a matching/subset-selection
  question ("which donor covers which target") but a *where-in-the-
  recursion-tree* resource-placement question (one global snip, existence
  of a good location) — no natural bipartite structure was found to map
  it onto, confirming the sibling's conclusion that this bridge is
  unconnected. No stronger analog found in `games-and-strategy` (mostly
  discrete pairing/mirroring/invariant-parity games, a different shape)
  or `extremal-principle` (mostly worst-case-configuration arguments, closer
  in spirit to opening 3 above but none directly transferable). **No
  genuinely new framing from the corpus beats STAY.**

- Analogous past problems (cruxes): none found that transfer a ready-made
  technique; `aimo-0063` checked and ruled out as a direct fit (see above).
  `aimo-0117` (dyadic/geometric-domination), already flagged in memory from
  round 1, remains the most relevant prior analog but is already fully
  absorbed into the existing DOM/HALVE toolkit.

- Prior progress: see current.md / sibling report — WF-C5 certified;
  adversarial gate passes to `m≥18`+ and an explicit cascading extremal
  family (margin exactly 0); HALF-BOUND unproved but its counterexample
  candidate is refuted (not a real gap, just an inadequate proof strategy).

- Dead ends (do not retry): "pure Move-1-only halving suffices" (refuted);
  "budget=0 suffices when top-level A is not locally dominant" (refuted,
  ~99% failure, no simple top-level predicate works); treating the
  flagged `(45,40,6,5,4)` witness as an open counterexample (it is not —
  recompute before spending a round on it again).

- Small-case / intuition notes (conjectural): the cascading family
  `p_i=(1/2-ε)R_i` is almost certainly the true extremal family for Case
  C's inductive step (margin exactly 0, `m=4..15`); a proof strategy
  should be validated against it specifically, not just isolated witnesses.

**Verdict: STAY.** The TAIL-SNIP/Candidate-5 recursion framing is not
broken — round 12's flagged gap was a proof-strategy artifact, not a true
counterexample. No genuinely different combinatorial framing from the
corpus or from first principles outperforms it. The correct next step is
NOT a new top-level approach, but re-targeting the existing approach's
proof at the sharper, cleaner claim: strong induction on `|A|` proving
existence of a correctly-placed single snip (or a potential-function
argument as in opening 2), validated against the cascading extremal
family from opening 3 — this is a refinement within the same framing, not
a switch.
