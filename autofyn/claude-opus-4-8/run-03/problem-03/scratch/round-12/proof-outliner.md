## imo-2026-03

Field this round: TWO far-apart LOWER mechanisms (LP-vertex vs majorization), ONE UPPER advance
(two-cap covering-radius recursion), and the retirement of the dead ballot-matching vehicle. The
two lower slugs are genuinely far apart in mechanism (vertex-of-a-polytope rank argument vs
majorization+exchange), not near-variants — they will not die on the same gap. Answer is CONFIRMED
`c(n)=2^n/(2^{n+1}−1)`, minimax `D=u_n=1/(2^{n+1}−1)`; both walls are the two open cruxes.

---

merge-interleave-pattern: revise
Target: minimax `D=u_n` (whole claim); the distinct contribution is the LOWER bound — every ≤n-cut
  refinement `S` of `C_n` has `D(S)≥1`, i.e. MID-core `μ{g odd}≥1` for `|F|≥3`.
Technique: LP-VERTEX / active-constraint-rank (import breakpoint-vertex's Theorem VERT onto a DIFFERENT
  polytope — the lower reachable-word interleave polytope). For a fixed reachable word `w`,
  `D(S)=Σ_{i odd}w_i` is LINEAR in the gap-lengths, so its min sits at a vertex; characterize vertices.
  Genuinely far from the three dead lower families (scalar-reserve, transport/matching, monovariant):
  it is a polytope-vertex rank argument, not a mass transport or scalar potential.
Skeleton:
  1. Import R/M/TB/MID/OSR/CLIP/ONE-REC — residual is the balanced band `F⊔B`, `|F|≥3`, all `≤2^{n-1}`,
     with `D(S)=Σ_{i odd}w_i`, `∫g=1` — by certified lemmas.
  2. Encode descending merge as word `w∈{F,B}^m`; `D=L_w=Σ_{i odd}w_i` linear in gap-lengths for fixed `w`.
  3. Reachable-value polytope `P_w`: sum constraints (`ΣF=2^n`, `B` refines `C_{n-1}`), cut-budget
     `(|F|−1)+c_B≤n−1`, ONE-REC per-scale single-excursion — all LINEAR ⇒ compact polytope.
  4. Min of linear `L_w` over `P_w` is at a vertex — by the affine-min-at-extreme-point step of Theorem VERT.
  5. GAP-EXTR: every vertex of `P_w` is a canonical one-F-fragment-per-gap interleave, value telescopes
     to exactly 1 — by the ONE-REC + budget active-constraint rank count.
  6. Base `n≤2` by certified brute force.
Key lemmas (claim + mechanism):
  - GAP-EXTR — every vertex is a one-F-per-gap layout with `D=1`, because at a vertex the ONE-REC
    per-scale single-excursion constraints and the cut-budget are simultaneously tight; a vertex clumping
    two F-fragments in one dyadic gap leaves another gap empty, forcing an inactive ONE-REC slack the rank
    count forbids ⇒ the F-fragments spread one-per-gap, where `D=Σt_k−Σg_k=(2^n−1)−(2^n−2)=1`. This is the
    vertex-analogue of the "spread" the refuted transport (HALL-ENDPOINT) could not force — LP rank forces it.
  - GAP-REACH — ONE-REC per-scale single-excursion as LINEAR polytope constraints, from the sum + ladder.
Open gaps: GAP-REACH (polytope constraints rigorous), GAP-EXTR (vertex characterization). Builder fills these.
Cases to cover: reachable words `w` (finite per n); base `n≤2`.
Watch out: MANDATED CHEAP-KILL FIRST — enumerate vertices of the lower polytope for n=3,4 (exact
  enumeration or scipy LP per fixed `w`) and verify ALL are canonical interleaves BEFORE any prose. A
  clumped vertex kills this exactly like HALL-ENDPOINT (spread to non-adjacent scales). ~30 lines, decisive.
  Do NOT re-derive the word identities (certified). Keep distinct from breakpoint-vertex (different polytope,
  different wall — not the same gap).

---

f-partition-majorization: new
Target: minimax `D=u_n` (whole claim); LOWER bound MID-core `D(S)≥1` for `|F|≥3` via majorization.
Technique: MAJORIZATION / rearrangement — compare the ordered `F`-value profile to the FIXED
  superincreasing dyadic ladder `B=C_{n-1}` (Karamata-style, Schur-appropriate on the odd-rank
  functional), PLUS a B-refinement monotonicity lemma. Asymmetric treatment of F vs B — genuinely far
  from the LP-vertex route and from all three dead families.
Skeleton:
  1. Reduce to MID-core (import R/M/TB/MID/OSR).
  2. MAJ (`c_B=0` slice): with `B` the fixed dyadic ladder, `D=Σ_{i odd}w_i` over F-insertions is
     minimised by the canonical one-F-per-gap layout (value 1); any other F-profile majorises it — by the
     superincreasing ladder gaps making the odd-rank functional Schur-appropriate (ONE-REC keeps ≤1
     excursion/scale).
  3. GAP B-MONO: `∀` fixed admissible `F`, `min_B D(F,B) ≥ 1` — by a single-scale exchange showing the
     minimising `B` is uncut or a canonical ladder-aligned cut, where MAJ applies (B-cut perturbs `μ{g odd}`
     only within the one dyadic gap the new fragment enters — local support).
  4. Combine `D(F,B)≥min_B≥1`. Base `n≤2`.
Key lemmas (claim + mechanism):
  - MAJ — canonical one-F-per-gap layout minimises `D`, value telescopes to `1`; because superincreasing
    ladder gaps make moving F-mass to a coarser gap only add odd-measure.
  - GAP B-MONO (make-or-break, genuinely NEW, unrefuted) — `min_B D(F,B)≥1 ∀F`; because a B-cut's effect on
    `μ{g odd}` has support in a single dyadic gap, so the min-B is at one aligned configuration where MAJ closes it.
Open gaps: MAJ (c_B=0 slice), GAP B-MONO (B-cut monotonicity localising the min-B).
Cases to cover: `c_B=0` slice; `c_B>0` general; base `n≤2`.
Watch out: `c_B=0` is PROVEN NOT WLOG (explorer: 42.8% of B-cuts strictly lower `D` at n=5) — GAP B-MONO is
  MANDATORY. RISK FLAG for reviewer: `min_B D(F,B)≥1 ∀F` is close to MID-core restated; the decomposition
  only has teeth if the exchange step genuinely localises the minimising `B` to ONE aligned configuration —
  if it cannot, this collapses to full MID-core and should be retired. NO corpus majorization analogue
  (report honestly; `aimo-0287` local exchange is a flavour hint only). Cheap-kill FIRST: exhaustive
  (multi-cut, not one-cut) adversarial B-search per fixed F, n=4,5, confirming `min_B D≥1` before prose.

---

breakpoint-vertex: advance
Target: minimax `D=u_n` (whole claim); UPPER bound — Xiang forces `D≤u_nL` in the balanced valley
  (`a₁<L/2`, `a₂<β_nL`), i.e. the Covering claim: a nonempty-T tree-realizable descending-KK value `≤u_nL`.
Technique: JOINT TWO-CAP recursive covering-radius bound on the reachable set — a GLOBAL set invariant
  (over all of `R_i`), NOT a single-pass policy (those are refuted). Builds directly on the two lemmas
  certified R11: CONF (`max R_i≤a₁`) and MD2 (reachable MULTISET `|M_i|=2^i`, support `R_i`, all in `[0,a₁)`).
Skeleton:
  1. Import CONF (`R_{n+1}⊂[0,a₁)`) and MD2 (multiset doubling).
  2. Define the covering radius `c_i := sup_{x∈[0,a₁]} dist(x, R_i)` — a GLOBAL invariant of the whole set.
  3. GAP TWO-CAP (make-or-break): a contraction recursion `c_i ≤ f(c_{i-1}, a_i)` using BOTH caps —
     `a_i≤a₂<β_nL` for `i≥2` (second cap, used at EVERY level, not just the top as in the refuted R10
     `a_i/2` bound) AND CONF — telescoping to `c_{n+1} ≤ u_nL`.
  4. Convert covering radius → a NONEMPTY-T reachable value `≤u_nL`: the `2^{n+1}−1` nonempty-T values plus
     `0` cover `[0,a₁]` within `c_{n+1}`; force a nonempty-T value within `u_nL` of `0`, OR an exact `0` via
     nonempty even cancellation. Handle the T=∅ exclusion EXPLICITLY (skip-everything needs n+1 deletes, only
     n cuts — infeasible).
  5. Base `n≤2` by direct computation; combine with the certified `a₁≥L/2` closure for the whole upper bound.
Key lemmas (claim + mechanism):
  - GAP TWO-CAP — `c_i` contracts geometrically to `u_nL`; because reflecting `R_{i-1}` off the SMALL piece
    `a_i≤a₂<β_nL` (MD2's doubling step) refines the gaps near `a_i` at every level, and the second cap keeps
    `a_i` small enough that the refinement genuinely halves (not saturates at `a_{n+1}/2` as the one-cap R10
    bound did). The extremal dyadic profile telescopes to exactly `u_n`, confirming tightness.
Open gaps: GAP TWO-CAP (the contraction inequality) and the T=∅-safe covering→nonempty-value conversion (step 4).
Cases to cover: valley `a₁<L/2 ∧ a₂<β_nL` (residual); `a₁≥L/2` already certified; base `n≤2`.
Watch out: R9 REFUTED single-pass greedy recursions (band-landing recursion / flip-if-helps / drop-one,
  overshoot ≤11.4×) — this MUST be a global set invariant, not a policy. R11 REFUTED the collision-regime as a
  broad mechanism (exact 0 is measure-zero) — do NOT lean on forced collisions; the content is a worst-case
  bound on a strictly-positive covering radius, with exact-0 folded in as one easy tied boundary case. MUST
  exclude T=∅. Numeric-GATE the exact recursion inequality (`c_i≤f(c_{i-1},a_i)`) on random valley profiles
  n=2..7 BEFORE prose. Dyadic-band-tagging (crux aimo-0493, opening 3) is a noted alternative but stays OFF
  the table this round — same upper object, would be a single-gap-trap double-up; revisit only if two-cap dies.

---

ballot-matching: retire
Verdict: RETHINK (R11) — the structured debit→credit transport/Hall MECHANISM is provably DEAD
  (HALL-ENDPOINT fails 49%; GAP-TERMINAL premise `S_m<0` FALSE, tight case `S_m≥0`; only feasible transport
  = complete-bipartite = target itself). Combined with the dead scalar-reserve family (R10), NO structured
  transport/matching lever survives for MID-core. This vehicle has no re-plan that escapes the refutation —
  its defining mechanism (a structured assignment certificate) is exactly what was killed. RETIRE; the LOWER
  wall's two live vehicles this round are the genuinely-new merge-interleave-pattern (LP-vertex) and
  f-partition-majorization (majorization+exchange), which are NOT transport/matching. Do not rebuild
  ballot-matching. (Also do not rebuild parity-measure-potential — top Elo 1752 but its entire scalar-reserve
  family is dead.)
