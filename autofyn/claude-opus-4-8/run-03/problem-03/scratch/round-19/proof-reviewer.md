# Proof-reviewer — Round 19 (imo-2026-03)

## Approach: breakpoint-vertex (UPPER wall) — CONSOLIDATION / re-target round

**Verdict: CHANGES REQUESTED**  •  **True Status: partial**  •  Builder's recorded Status (partial): CORRECT.

### What was reviewed
A consolidation round that (1) officially re-targets the open deep-interior residual from the
caterpillar object `μ_{n+1} ≤ u_nL` to the certified true target `min 𝓡(A) ≤ u_nL` via Corollary
R-UV of certified Lemma RL, (2) records two mechanisms dead, (3) restates the open gap. No prose
closing the deep interior is shipped; none is claimed.

### 1. Correctness of the re-targeting — VERIFIED SOUND
- **R-UV is genuinely certified and correctly invoked.** The lemma file
  `lemmas/leftover-realizability.md` (CERTIFIED round 7) states Corollary R-UV: in the upper game
  (`m=n+1`, `≤n` cuts) Xiang forces `D ≤ u_nL` **as soon as** `min 𝓡(A) ≤ u_nL` — the *sufficiency*
  direction, via the disjoint-support invariant giving tree-realizability of any nonneg differencing
  value in `|T|−1` MATCHes + `m−|T|` DELETEs = `m−1 = n` cuts, ending `D({ρ})=ρ`. The builder cites
  it exactly, and correctly flags that the converse (R-COV') is uncertified and unused. No overclaim:
  a *sufficient* condition is all the upper bound needs.
- **`min 𝓡(A) ≤ μ_{n+1}` — VERIFIED.** Caterpillars are one tree topology, so the caterpillar
  reachable value-set is contained in the value-set of 𝓡(A); hence `min 𝓡(A) ≤ μ_{n+1}`. I confirmed
  numerically (exact Fraction): the containment holds on all three witnesses (0≤1, 0≤2, 2≤3). The
  re-target is therefore weakly easier AND, by R-UV, equally sufficient — a valid bookkeeping move,
  not new mathematics claimed as new.
- **Completeness identity `μ_{n+1} = min 𝓡(A)` is FALSE — INDEPENDENTLY REPRODUCED.** I recomputed
  min 𝓡(A) (full subset + all-differencing-tree search, exact Fraction) and μ (FGR dist-recursion):
  `(17,16,11,8,4)`: μ=1, minR=0; `(59,55,53,44,17)`: μ=2, minR=0; `(54,43,35,32,28)`: μ=3, minR=2.
  All match the builder exactly. So any future lever assuming that equality is unsound on arrival —
  exactly the landmine the re-target defuses. This is a genuine correctness safeguard.

### 2. Rigor — the open gap is honestly surfaced, no hand-waving
- The Status header, §3 Current best, and §4 Evidence all explicitly state the deep interior
  `a₁ < (L−u_nL)/2` is OPEN and the residual `min 𝓡(A) ≤ u_nL` is unproven. §4 numerics are labelled
  "EVIDENCE, not a proof." No step presents the open residual as closed. Overclaim check: PASS.
- The two dead mechanisms are recorded with sound structural reasons: (ii) a balanced FULL partition
  cannot drop pieces, so it cannot reach the anchor-EXCLUDING tail minimiser (`{13/40,13/40}` on the
  R18 witness) — consistent with the certified VALLEY-TIGHT/covering-radius death signature; (iii)
  band-restart ≡ descKK is anchored at `a₁`, the 9th dead anchored-walk under a new name, consistent
  with the round-18 class-level kill of anchored-walk contraction. Both are honest negative recordings.

### 3. Progress — real but low-content (correctly partial)
Adopting the certified correct target and refuting the μ=min𝓡 completeness confusion is a genuine
(if narrow) advance: it prevents a whole class of unsound "bound-the-big-object-transfer-by-completeness"
levers and correctly anchors the open residual as a NON-anchored global existence claim
(Steinitz / 1-D vector-balancing over the tree-realizable signed sums). It is NOT vacuous — but it
closes NO gap, so it is `partial`, not `advanced`/`solved`.

### The precise remaining gap (for next round)
Prove `min 𝓡(A) ≤ u_nL` for the deep interior `a₁ < (L−u_nL)/2` (hardest in the `u_n/2`-wide sliver
`a₁ ∈ (L/2−u_n, L/2−u_n/2)` where the ratio → 1). The true minimiser is generically an
anchor-EXCLUDING tail subset, so — per the standing R18 rule — the closing argument must be a
NON-anchored global existence bound over the whole tree-realizable signing set, not any single walk
or full-partition object. This slug's framing does not currently contain such an argument.

### Lemma certification
No new promotable lemma proposed this round (R-UV already certified round 7). Nothing to certify or
reject. Certified core (RL/R-UV, WTC, R-COV', FGR, ESF-2) INTACT and unchanged.

### Scores
- Correctness: 10/10 (every claim shipped is correct; independently reproduced).
- Completeness/rigor: 4/10 (honest, but the deep-interior residual remains open — as the builder states).
- Progress vs prior best: modest — a sound re-target + landmine-defusal + 2 recorded dead mechanisms;
  no gap closed.

**Routing: CHANGES REQUESTED — approach stays live (leader), close the deep-interior residual
`min 𝓡(A) ≤ u_nL` via a non-anchored existence argument, or hand to the outliner for a genuinely
different framing.**
