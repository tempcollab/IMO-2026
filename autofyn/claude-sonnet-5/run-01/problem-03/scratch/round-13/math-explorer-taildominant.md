## imo-2026-03 (lens: tail-locally-dominant sub-case, Candidate 5 / Lemma HALF-BOUND)

- Distinct openings:
  1. **Re-derive the induction on the *recursion tree itself*, not on "Case C
     vs not."** Tracing the witness `A=(45,40,6,5,4)/100` (Fraction-exact,
     script `/tmp/round-13/probe3.py`) shows `solve_full(A,budget=1)=50=Σ/2`
     is achieved via **Move 1 at the top, and the single available snip
     (Move 3) fires three levels down**, inside `tail(A)=(40,6,5,4)`'s own
     recursive call on `(6,5,4)`. So the existing recursion *already*
     succeeds on this witness — the reported "pure Move-1-only" overshoot
     to `13/25` is a strawman comparison (forcing every level to use only
     Move 1), not evidence the recursion itself is broken. The real gap is
     that no one has yet written an inductive *proof* that some snip
     location always exists — only found it by brute-force search each time.
  2. **The snip is essentially always needed, not just in the flagged
     sub-case.** Budget=0 (Move 1/2 only) fails to reach `Σ/2` in ~99% of
     random Case-C instances tested (both even and odd `m`, script
     `/tmp/round-13/probe4.py`: 1187/1188 even-`m` trials failed, 1243/1248
     odd-`m` trials failed). So "exactly one global snip, applied at the
     right spot, always suffices" is the real load-bearing empirical claim
     — a much stronger and more surprising fact than "handle the rare
     locally-dominant tail case." Any proof plan should target this general
     claim, not carve out the locally-dominant tail as a special sub-case
     to patch.
  3. **Extremal/boundary framing:** the cascading family
     `p_i=(1/2-ε)·R_i` for every `i` (each element maximally locally
     dominant relative to its own remaining sum, at every recursion level
     simultaneously — the "worst possible" stacking of the flagged
     sub-case) hits the bound **exactly** (`margin=0` to machine/exact
     precision) for every `m=4..15` and every `ε` tested (script
     `/tmp/round-13/probe5.py`). This is the true extremal family, strictly
     harder than the single flagged witness, and a proof strategy should be
     validated against it, not just the one `m=5` witness.

- Candidate technique(s): an induction that tracks, for each recursive
  call `solve(A,budget)`, a bound of the shape `solve(A,budget) ≤ Σ(A)/2`
  when `budget≥1` (not conditioned on `A`'s own local Case-C status) —
  i.e. HALF-BOUND should probably be strengthened/generalized to *all*
  `(A,budget=1)` pairs reachable in the recursion (dropping the top-level-only
  Case-C hypothesis), proved by strong induction on `|A|` using Move 1's
  identity `solve(A,b) ≤ p_1/2+solve(tail(A),b)` together with a
  case split on whether `tail(A)` is itself "locally Case-C" — and when it
  is not, an explicit finite-depth argument that Move 2/3 close the gap
  (the depth of the "locally-dominant chain" is bounded by `|A|`, so a
  strong/complete induction on `|A|`, not merely peeling one element,
  is the right induction shape — ordinary induction peeling `p_1` only
  fails exactly because it doesn't let you "look ahead" into where the
  snip needs to land).

- Cheap-kill candidates: none found — checked parity (odd vs even `m`)
  as a possible discriminator for when budget=0 alone suffices: it does
  not discriminate (both parities fail budget=0 at ~99% rate). Checked
  whether the locally-dominant index is always unique/at a fixed position:
  no — in the witness, indices `{0,1,2,3}` (nearly all of the tuple) are
  simultaneously "locally dominant" by the `p_i>(R_i-p_i)/2` measure, yet
  one snip still suffices.

- Knowledge-base entries to use / relevant certified lemmas: BLOCK-RECURSE
  (leftover computation correctness, any depth — already used, still valid),
  THRESHOLD-REDUCTION (only needed for the final telescoping step, not this
  gap), TAIL-SNIP (the base move being budget-capped here), WF-C5 (already
  certified, not reusable for the value inequality itself). PARTIAL-DOM and
  PAIR-VALUE are candidates for an alternate closed-form value formula that
  might make the induction tractable without case-splitting on "locally
  dominant or not." ALL-BUT-MIN and MATCH-TAIL-PAIR (from round 9/10, tied
  to the Hall-matching framing) are probably NOT the right tool here — this
  gap is about *where in the recursion tree* to spend one global resource
  (a counting/allocation argument), not a donor/subset-matching existence
  question; I could not find a natural translation of "one snip suffices
  somewhere" into a Hall's-theorem statement. The `aimo-0063`
  Hall-deficient-set-deletion idea flagged in the current file remains
  unconnected — I did not find the bridge either.

- Analogous past problems (cruxes): did not have time this round to query
  the crux corpus directly (deferred to a lens with more coverage of that
  step); flagging this as a gap in my own coverage rather than asserting
  "none".

- Prior progress: Lemma WF-C5 (certified, well-foundedness only). Gate
  (existence of no counterexample, budget=1) independently reproduced
  clean up to `m=18` here (450+ fresh random trials, zero violations,
  worst margin exactly `0`) plus the m=4..15 cascading extremal family
  (exact `0` margin at every point, the true worst case). HALF-BOUND
  itself (the value inequality) remains unproved — this round adds
  numerical strengthening (larger `m`, an explicit worst-case family) but
  no new proof technique.

- Dead ends (do not retry): "pure Move-1-only halving always suffices" —
  already known false (overshoots by `p_m/2` since the recursion's actual
  base case returns the unhalved last element); confirmed again here,
  not a live idea. "Budget=0 (no snip) suffices whenever the top-level
  instance itself is not locally dominant / is Case C" — refuted broadly:
  budget=0 fails on ~99% of random Case-C instances regardless of any
  simple structural flag tested (parity, top-level dominance), so
  case-splitting the induction on a simple predicate at the *top* level
  will not work; the predicate needed (if any) must be about the whole
  recursion tree's structure, not one scalar test on `A`.

- Small-case / intuition notes (all conjectural, exact-Fraction-verified,
  no proof): (1) One global snip, correctly placed, suffices for every
  Case-C instance found so far, `m=4..18`, both random sampling and an
  explicit maximally-adversarial cascading family — strong evidence
  HALF-BOUND is true, no evidence found against it. (2) The witness
  `A=(45,40,6,5,4)/100` is NOT actually a counterexample to the current
  recursion (it achieves exactly `Σ/2`); it is a counterexample only to
  the naive "prove it via peeling + pure Move-1 IH" *proof strategy* —
  worth flagging clearly to the outliner so the next builder doesn't
  waste a round re-confirming the recursion "fails" on it. (3) The
  cascading family `p_i=(1/2-ε)R_i` is the right stress-test / likely
  extremal-configuration candidate for any future inductive proof to
  verify itself against, since it stacks the flagged sub-case at every
  level simultaneously and still hits the bound exactly.
