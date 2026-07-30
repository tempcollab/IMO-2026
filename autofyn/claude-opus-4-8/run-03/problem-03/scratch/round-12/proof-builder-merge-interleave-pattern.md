# Build report — merge-interleave-pattern (LOWER wall), round 12

**Status: PARTIAL** (honest). Cheap-kill PASSED; vertex reduction proven; GAP-EXTR (general n) open.

## Cheap-kill result (MANDATED, run FIRST — decisive)
Exhaustive vertex/LP enumeration of the lower interleave polytope, all types × all words:
- **n=3** (5 F-types), **n=4** (21 F-types): **global min D = 1.000000, NO vertex with L_w < 1.**
- Minimisers are canonical one-fragment-per-gap layouts (n=3: F={4,3,1}, B={4,2,1}, D=1).
- **The refutation branch did NOT trigger** — no clumped sub-1 vertex. The approach is NOT refuted;
  cleared to write prose (per the reviewer's gate).
- First run used the WRONG objective (Σ odd-position values instead of the ALTERNATING sum
  v₁−v₂+v₃−…); gave min 8/16. Corrected to the alternating functional → min 1. (Recorded so nobody
  re-introduces the sign bug: D = Σ(−1)^{k+1}v_k, NOT Σ_{odd}v_k.)

## What is rigorously established (new, correct)
1. **Theorem VERT-LOW** — MID-core ⇔ every vertex of every P_T has L_T ≥ 1. Proof: Fundamental Theorem
   of LP (linear functional min on compact polytope at a vertex) + admissible refinements ⊆ ⋃_T P_T.
   Loss-free, rigorous, promotable.
2. **Block-structure lemma** — a vertex has ≤ n+3 distinct values (≤ n+2 positive; numerics n+1), by
   active-constraint rank against the n+1 group-sum equalities. Rigorous, promotable.
3. **Tight attainment** — explicit family B=C_{n-1}, F={2^{n-1},…,2,1,1} gives D=1 for all n (cancelling
   pairs + triple-1). Confirms minimax D=u_n, c(n)=2^n/(2^{n+1}−1). Promotable.

## Corrections to the outline (Spec concerns)
- **GAP-EXTR restated** per the reviewer: it is "min L_w ≥ 1 at every vertex," NOT "every vertex is
  canonical value 1" (D varies across words; Case (a) gives D=2^{n-1}). Done.
- **GAP-REACH dissolved:** ONE-REC per-scale single-excursion is an AUTOMATIC consequence of the group
  sums + positivity (two fragments > 2^{j-1} sum > 2^j), NOT a separate linear facet. So P_T is a
  polytope with only (E),(O),(C); the outline's "ONE-REC as linear polytope constraints" premise is
  moot — and, importantly, the outline's GAP-EXTR *mechanism* ("ONE-REC tightness at a vertex forces
  the spread") is UNSUPPORTED, since ONE-REC is not a binding constraint whose tightness could force
  anything. This is a real weakness in the proposed mechanism the reviewer should note.

## Honest gap
**GAP-EXTR for general n is loss-free equivalent to MID-core** — the vertex reduction reframes and
sharpens (finite explicit block-structured target, ≤ n+1 dyadic block-values) but does NOT close it.
Two shortcuts are REFUTED: integrality (non-integer vertices exist, all >1) and constant-value.
The route survived the cheap-kill and delivered a clean, reusable reduction + de-risking, but the
general-n vertex bound needs a genuinely new argument (induction over block levels / dyadic scales at
a vertex; NOT monovariant/transport/scalar-reserve, all dead).

## Verdict suggestion
CHANGES REQUESTED (partial, real progress: rigorous reduction + n≤4 confirmation + two dead shortcuts
eliminated + tight attainment). Keep live. Next round: attack GAP-EXTR by a dyadic-scale induction on
the block-structured vertex, or seed a structurally different lower reformulation (the field's lower
wall still terminates at MID-core — the convergence risk the reviewer flagged persists).
