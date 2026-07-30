# proof-builder report — `defect-hall-deficiency`, round 15

## Verdict: dead end (Step 0 gate fails). Status set to `unsolved`
(dead end), not `partial`.

## What was checked

Per the outline-reviewer's added Step 0 caveat, I checked not merely
whether *some* bipartite-graph encoding of Xiang Yu's Case-C subset-match
problem has bounded Hall/König deficiency, but whether a Hall-type
matching in that graph actually **implies** the subset-match Lemma
SLACK-COVER needs. I ran this on all three mandated witnesses (uniform-
tail family `m=4,5,8,12`; `T=(0.20,0.15,0.12,0.08)`; and
`A=(1826,1563,1520,1514,765)/7188` from `current.md`), using exact
`fractions.Fraction` arithmetic.

## Result: decisive gate failure, general (not witness-specific)

Case C is defined by `p_1<\Sigma(A)/2`. This alone forces
`\Sigma(\mathrm{tail}(A))=\Sigma(A)-p_1>\Sigma(A)/2>p_1`, **strictly, in
every Case-C instance**. So the "does a covering subset of the tail
exist for `p_1`" question — the only thing a Hall/König-deficiency
argument can certify — is **always trivially true** (a two-line greedy
argument), before any graph is even drawn. Verified numerically on all
three witnesses (tail sums `1/2` vs `p_1<1/2`; `0.35>0.20`;
`5362/7188>1826/7188`).

This makes any bipartite encoding fail the faithfulness requirement, via
a clean dichotomy:
- **Permissive encoding** (edges = "any subset with `\Sigma(S)\le p_1`"):
  Hall's condition holds trivially, deficiency `\equiv0`. The theorem
  outputs only the already-known-easy "prefix-mesh" existence fact
  (independently derived and explicitly flagged as *not* the missing
  ingredient in `universal-adversary-strategy.md`'s Round 14 build). It
  carries zero information about which of the (generically many)
  covering subsets meets the actual value target.
- **Restricted encoding** (e.g. edges = contiguous-prefix matches only,
  mirroring the superseded Move 2/PARTIAL-DOM): bounded deficiency
  *within the class* does not imply the value target is met. Concrete,
  already-on-file counterexample re-verified exactly: on
  `A=(0.45,0.20,0.15,0.12,0.08)` (tail `(0.20,0.15,0.12,0.08)`), the
  Hall-saturating contiguous-prefix match (`p_1'=0.20\to\{0.15\}`)
  achieves `oddrank=7/25=0.28`, which **exceeds** the target
  `\Sigma(\mathrm{tail})/2=11/40=0.275`; only the non-contiguous subset
  `\{0.12,0.08\}` (sum exactly `0.20`) meets the target exactly. So
  "Hall-matching exists in `G`" does not imply "needed subset-match
  exists" for this `G` either.

Both natural encodings fail the implication the gate demands. The
underlying reason: the real difficulty is not a cardinality/reachability
question (which Hall/König address) but a numeric subset-sum/value
optimization (which specific subset's exact real value, combined with a
recursive value bound on the leftover via the certified Lemma
PAIR-VALUE / Lemma DOUBLE-INSERT-MATCH-VALUE, clears
`c(m-1)\Sigma(A)`) — a different combinatorial shape from an SDR/matching
question, confirming (now with a proof, not just a disanalogy note) the
outline-reviewer's flagged concern after checking crux `aimo-0341`
directly.

## Action taken

- **Did not proceed** to Steps 1–2 (general deficiency bound, value
  adaptation) — per the approach's own explicit instruction not to build
  on an unverified/failing premise.
- Updated `approaches/defect-hall-deficiency.md` in place: Status →
  `unsolved (dead end)`, full Step 0 derivation and both-encodings
  dichotomy written up in full, original skeleton kept below (marked
  superseded) for the historical record per repo convention.
- No changes to any other approach file or to `current.md` (reviewer-
  owned).

## Recommendation for next round

Do not re-attempt Hall/König-deficiency framings for Lemma SLACK-COVER —
existence of a covering subset is never the obstruction in Case C (proved
here in general, not just numerically). Any future attack on Lemma
SLACK-COVER must be a value-optimization argument (as
`universal-adversary-strategy`'s Round 15 joint-induction plan already is)
or a genuinely different mechanism that does not reduce to a
cardinality/existence claim.
