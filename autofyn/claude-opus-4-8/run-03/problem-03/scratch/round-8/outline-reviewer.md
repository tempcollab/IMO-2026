# Outline review — imo-2026-03, round 8

Answer CONFIRMED c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1). Two sharpened walls:
LOWER GAP MID-core (Σc_iw_i≥0 on the ±1 walk) and UPPER Prop UV (min 𝓡(A)≤u_nL in the valley).
Shared walk reduction (D(S)=Σ_{i odd}w_i, ∫g=ΣF−ΣB=1) re-verified numerically on the explorer's
n=3 example (D=2.2, ∫g=1.0, D−∫g=1.2) — the reduction the lower approaches rest on is sound.

## parity-measure-potential (advance) — APPROVE → BUILD
Best lower vehicle; owns certified MID. Skeleton is honest: steps 1–3 (reduction + walk encoding +
recast to Σc_iw_i≥0, c_i even) are certified/algebraic; the ONLY open gap is step 4, the
aggregate-compensation induction on Δ(i)=Σ_{j≤i}c_jw_j via Lemma ONE recursed. The outline correctly
flags the two traps (pure-integral version FALSE via g≡2; termwise S_i≤1[i odd] FALSE via S_4=2) and
targets the correct AGGREGATE form. Mechanism for step 4 is stated (peel top dyadic scale, next
forced B-crossing repays overshoot, terminal S_m=|F|−|B|<0) — a real mechanism, not a bare label,
though unproven. Sound to build.
Issue to close while building: the "next ladder-forced B-crossing repays" claim must be made a
quantitative per-scale inequality (debit above τ ≤ credit reachable below τ), not an appeal to
intuition — this is the genuine content and must be proved profile-independently for |F|≥3.

## breakpoint-vertex (advance) — APPROVE → BUILD
Best upper vehicle; VERT/RL/VS/R-UV all certified and reviewer-confirmed profile-independent (not
spot-checks). Reduction to Prop UV (min 𝓡(A)≤u_nL over the finite VERT tie-pattern family) is exact.
Open gap Prop UV is correctly isolated. The outline respects the recorded constraints (RL forbids the
naive 2^{n+1} pigeonhole; DELETE is essential; ≥2 coordinated cuts forced by VS). Sound to build.
Issue to close while building: Prop UV is still ONLY numerically verified (387 profiles R7 + fresh
n=3,4 brute force this round, worst ratio ~0.56–0.66). The builder must produce a profile-independent
bound over the vertex family — a spot-check is NOT a proof (rules R3/R4). The dyadic-cascade
telescoping (2^n−2^{n−1}−…−1=1=u_nL) is the model to generalize.

## ballot-matching (new) — CHANGES REQUESTED → REGISTER, HOLD from build
Technique (weighted transport + Hall from the ladder) is plausible and the skeleton imports the
certified reduction correctly. But it attacks the IDENTICAL target inequality Σc_iw_i≥0 as
parity-measure, and the "mechanism" is not genuinely independent: a Hall/transport feasibility
condition for a later-credit matching on the line ("debit above τ ≤ credit below τ") is, by LP
duality, the SAME prefix-sum inequality as parity-measure's running-deficit monovariant Δ(i)≥bound.
The explorer confirmed GAP-HALL ≡ GAP MID-core, and the outliner's own honesty flag invites pruning
if too close. It IS too close — building it alongside parity-measure would advance two levers that
collapse to the same wall (the exact redundancy to avoid). Registered as a live reserve (Elo ~1460);
if parity-measure's step-4 induction stalls next round, the matching-certificate reformulation is a
legitimate alternate write-up to activate. Not doomed — held, not cut.

## valley-differencing-construction (new) — CHANGES REQUESTED → REGISTER, HOLD from build
Constructive framing (explicit DELETE-repair + sorted-difference chain) is genuinely a different
PROOF STYLE from breakpoint-vertex's existence/enumeration, and a fully explicit strategy would be
the cleaner proof — real value in the population. But as written it is not yet buildable:
- GAP-DELETE-RULE: Step 1 is self-contradictory ("keep a_j iff a_j≤r_current; DELETE it otherwise is
  WRONG … the correct rule is … keep every piece while r>0 and DELETE only the terminal tail"). The
  DELETE rule is admittedly "stated loosely" — it must be pinned to a single deterministic,
  budget-legal recipe before the chain is even well-defined.
- GAP-CHAIN: the telescoping bound ρ≤u_nL is a lemma named WITHOUT a working mechanism. aimo-0796
  gives only ρ<a₂ (off by up to 2^{n−1}, acknowledged), and the replacement is asserted via a
  monotonicity claim ("pushing a₂<β_nL can only DECREASE the leftover relative to the dyadic tight
  case"). That monotonicity is unjustified and echoes a refuted intuition — R3 showed the minimax V
  is NOT monotone along balanced→dyadic paths (interior valleys), so a "can only decrease toward
  dyadic" argument cannot be waved through. A genuine telescoping induction on survivor count must be
  supplied, not a monotonicity assertion.
Additionally, the explorer flagged that the construction (route ii) shares its make-or-break sub-step
with the pigeonhole/VERT object — so building it alongside breakpoint-vertex would also risk two
upper levers on the same wall. Registered as a live reserve (Elo ~1507); it is the pre-positioned
genuinely-different upper framing to ACTIVATE if breakpoint-vertex's Prop UV stalls again. Not
doomed — held, not cut.

## Diversity / field note
The field is correctly split one-lever-per-wall this round. The recurring risk (flagged R4, R6, R7)
is real: every lower approach reduces to Σc_iw_i≥0 and every upper approach to min 𝓡(A)≤u_nL. That
is inherent to the problem's two-wall structure now, not a framing accident — the reductions are
certified. The right response is depth on each wall's single best vehicle plus a pre-positioned
different-MECHANISM reserve per wall (ballot-matching for lower, valley-differencing for upper),
which is exactly the current population. If EITHER built vehicle stalls on its wall next round,
activate that wall's reserve rather than adding a third bookkeeping variant.

build set: parity-measure-potential, breakpoint-vertex
