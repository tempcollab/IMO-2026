# Build report — dyadic-discrepancy-euclid (GAP U), round 7

## Headline
**The entire upper bound `D*≤u_n` (i.e. `c(n)≤2ⁿ/(2^{n+1}−1)`) is now COMPLETELY proven**, all `n`,
all Liu plays — not just the assigned residual (iii-b) `ℓ₁<Σ/2`. The whole GAP U wall is closed by
this slug. File: `results/imo-2026-03/approaches/dyadic-discrepancy-euclid.md`.

## What I closed
The round-6 approach had reduced the entire upper bound to ONE open step — the Reachability Lemma
(§D): is the minimizing signed-subset sum `m*` realizable as a single legal coin? I proved it.

- **Theorem R (Abs-Difference Reachability), fully proven (§D).** For any finite multiset `U` of
  positive reals, `min Reach(U) = m*_±(U) = min_{ε∈{±1}^U}|Σ ε_i x_i|`, and the minimizer is realized
  by pinning `U` to one coin in `|U|−1` pins. **Mechanism = sign-pairing strong induction:** take a
  `+`/`−` pair `(p,q)` from any minimizer; contract it to the coin `c=|x_p−x_q|` (one pin); prove the
  contracted multiset's min signed sum equals the original's (contracted `±1` patterns correspond
  exactly to original patterns with `ε_p=−ε_q`, and the minimizer is feasible there). This *replaces*
  the round-6 "peel-the-smallest" IH, which genuinely stalled (needed reachable values above the
  subproblem's own min, e.g. `24∈Reach({44,20})`). The pairing peel keeps the minimum invariant, so
  the naive IH suffices.

- **Op-budget resolved (§E), the reviewer's load-bearing warning.** The play uses **exactly `n` cuts**:
  `n+1−s` bisects (delete unused pieces) + `s−1` pins (the abs-difference tree on the support). The
  chain length is `s−1≤n`; there is no iterated `a mod b` with quotient `>1`, so the "subtractive
  Euclidean chain overruns `k` ops" fear never materialises. Budget was never binding — reachability
  was the real crux, exactly as flagged.

- **Fewer-marks case (§F), trivial.** If Liu marks `a<n` points (`a+1≤n` pieces), Xiang bisects every
  piece (`a+1≤n` cuts) → all invisible pairs → `D=0≤u_n`. This is the clean resolution of the
  piece-count-vs-`n` mismatch (subset sums of `<n+1` pieces only give `u_{p-1}>u_n`; the fix is to
  bisect to `D=0`, not to chase the deep pigeonhole). Only `a=n` needs the §E construction.

Result: §B (subset-sum pigeonhole, `m*≤u_kΣ`, universal, proven round 6) + §D (Theorem R) + §E
(exactly `n` ops) + §F (fewer marks) ⇒ upper bound for ALL cases and all `n` in one page, on the
certified RT spine.

## Verification (exact arithmetic)
- `/tmp/thmR.py`: pairing-induction tree root `= m*` on `0/2000` random `Fraction` instances (`n≤5`);
  op-count `≤n` on `0/2000`; `m*≤u_nΣ` on `0/2000`.
- `/tmp/rtest.py`: `min Reach(U)=m*_±(U)` on `0/300` integer multisets, `s≤6`.
- Fewer-marks: strong search confirms `min_Xiang D≪u_n` for `a<n`; §F proves `D=0` outright.

## What remains open (the whole problem, NOT this slug)
Only the **lower bound Case B / GAP L** (`maxc≥2` T-run) is unproven; it is a different wall owned by
`induction-recursion-telescope`. Imported, not re-attempted. Hence this slug's Status is `partial`
for the *whole problem*, but its own target (GAP U) is fully closed. Once GAP L closes, the problem is
solved.

## Spec concerns
None on the upper bound. Note: this slug now SUPERSEDES the twin `dyadic-discrepancy`'s `ψ(k,β)`
pin-top-2 induction for GAP U — the subset-sum + Theorem-R route is strictly more complete (all cases
at once, no near-miss branch needed). The reviewer may wish to consolidate the GAP-U wall onto this
argument.

## Lemmas proposed for certification
1. **Theorem R (Abs-Difference Reachability)** — `min Reach(U)=min ±1 signed sum`, minimizer realizable
   as one coin in `|U|−1` pins. Proof: §D (sign-pairing induction). Clean, self-contained, exact-verified.
2. **Upper-bound completion (§E–§G)** — for all `n`, all Liu plays, Xiang holds `D≤u_nΣ`; hence
   `c(n)≤2ⁿ/(2^{n+1}−1)`. Depends on RT (certified) + Lemmas A,B,C + Theorem R + §F. Ready to certify
   the entire GAP U wall.
