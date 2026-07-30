# proof-builder — frozen-invariant-reduce-mod-lcm (round 2)

## Verdict: ROUTE RETIRED

Slug `frozen-invariant-reduce-mod-lcm` was dispatched as a HIGH-RISK PROBE (the
field's only non-`M'_n`-stabilization attack on B1'). The retire-fast protocol
was triggered: the load-bearing monovariant `w_n` (aimo-0678 move (2)) was
empirically refuted, and the step-4 finite-state clincher was confirmed to
reimport B1' (the König obstruction). No proof was assembled.

## What was tested

### Test A — the monovariant `w_n = min{m>a_n : m∉B_n}` (step 2/3, the B1' lever)
Computed the greedy `a_1..a_N` (N=120–200) and `w_n` for `a_1 ∈ {15,35,77,91,105,135,175,385}`.

**Result (decisive):** `w_n` is NON-DECREASING in all 8 cases — the OPPOSITE of
the non-increasing direction the aimo-0678 lever requires. The gap
`u_n := w_n-a_n` is bounded (`∈ {1,2,3}`) but OSCILLATES (`1,2,1,1,…`;
`1,3,1,…`) — not monotone in either direction. The lever's entire purpose
(non-increasing `w_n` while `a_n` climbs ⇒ `a_n ≤ w_n ≤ w_0` ⇒ `a_n` bounded)
is inert: `w_n` tracks `a_n` upward and bounds nothing.

### Test B — finite-state determinism (step 4, the reduce-mod-lcm clincher)
For `a_1=15`, `L=30`: `(a_n mod 30) → (a_{n+1} mod 30)` is a deterministic
8-cycle from `n=0` (0 ambiguous keys). BUT this is Theorem 1 re-derived on the
*already-stabilized* small lattice — the genuine state is the full past hitting
family `M'_n`, finite only under B1'. Off the periodic regime the transition is
history-dependent (König scout's consistent-prefix tree: ≥20 continuations,
different `(T,L)`). So step 4 is conditional on step 3, which failed.

## Why the aimo-0678 crux does NOT transfer

The aimo-0678 monovariant `w_n = min{m≥a_n : m∤s_n}` is non-increasing there ONLY
because of TWO ingredients absent from our problem:
1. **A frozen invariant** `s_n = a_n+b_n`, conserved in the divisibility regime.
   Our greedy has no coupled second sequence, no conserved sum. The candidate
   `I_n = a_n mod L_*` fails (periodicity mod `R` is false; `L_*` is the kernel
   product, unknown a priori).
2. **An explicit gcd/lcm recurrence** `s_{n+1}=gcd+lcm` that lets one prove
   `a_n ∤ s_{n+1}` whenever `a_n ∤ s_n`, forcing `a_n ∈ W_{n+1}` hence
   `w_{n+1} ≤ a_n = w_n`. Our greedy `a_{n+1}=min{m>a_n : gcd(m,a_i)>1 ∀i≤n}`
   has no algebraic formula exposing the next state's divisibility structure;
   it is defined by "smallest admissible," not by gcd/lcm.

Without (1)+(2), the non-increasing proof has no analog, and the literal
`w_n = min{m>a_n : m∉B_n}` slides upward with `a_n`. Move (3) then reimports B1'
(finite state = `M'_n`, finite only under B1') and re-derives Theorem 1.

## Gaps / spec concerns
- None outstanding beyond the retire. The route is exhausted; its distinctive
  contribution is the NEGATIVE result (do not retry the monovariant shape).
- Spec note: the outline and outline-reviewer BOTH pre-flagged this as the
  highest-risk slug and prescribed retire-fast if `w_n` fails — the empirical
  test executed exactly as prescribed. The probe did its job.

## Recommendation to the reviewer / outliner
- CUT `frozen-invariant-reduce-mod-lcm` from the live population (or mark
  `retired-to-dead`). Keep the file as a low-Elo record so no agent re-dispatches
  the monovariant shape.
- The field's B1' attack should concentrate on the spacing/covering mechanism
  (`small-prime-window-lemma`) and the transversal-duality mechanism
  (`hitting-set-monovariant`). The aimo-0678 proof shape is genuinely different
  but does not transfer to a single-sequence greedy.

## Files
- Approach file: `/home/agentuser/repo/results/imo-2026-06/approaches/frozen-invariant-reduce-mod-lcm.md` (Status: unsolved, route retired)
- Empirical test scripts: `/tmp/test_frozen.py`, `/tmp/test_determ.py`, `/tmp/extra_check.py`
