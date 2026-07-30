## imo-2026-03 — LENS: multi-cut / structured global re-choice for the b-lift (GAP-P1′-b)

### Summary verdict up front
I tested the two most natural "hold-π₀-fixed, do a GLOBAL (not single) move on F'" candidates
numerically and both are **REFUTED**, for the same underlying reason as the already-dead single-cut
routes (R11 rule 34, R12 coupled-cut-descent): **any monovariant that holds π₀ literally fixed while
touching F' is doomed**, regardless of whether the move is one cut or all of F's cuts done
simultaneously. This is a genuinely new (if negative) data point: it rules out the "obvious" way to
read "multi-cut" (do more cuts of the same kind, still π₀-fixed) and pins the obstruction down more
precisely than before — the fix, if one exists, must co-vary π₀'s own shape together with F', not just
extend the move's cardinality. I also confirm (more finely than R11's single data point at n=4) exactly
where the true worst case lives: the single corner **a₀=n, b=0** (all budget spent fragmenting π₀,
F' fully uncut) — consistent with, and sharpening, the "extremal slice is b=0" finding.

### Distinct openings
1. **"Merge-all-of-F'-back-to-the-full-ladder-at-once", π₀ fixed.** Precisely: given feasible
   `(π₀, F')` with `F'` a genuine dyadic refinement, replace `F'` by the fully uncut ladder
   `L = {2^{n-1},…,1}` (all scales un-split simultaneously — a *global*, not single-cut, move), keep
   `π₀` untouched, and ask whether `D̃(π₀⊎F') ≥ D̃(π₀⊎L)`. **REFUTED numerically**: 2073/3000 (n=2),
   970/3000 (n=3), 1263/3000 (n=4), 1114/3000 (n=5) failures (exact `Fraction`, random feasible
   configs). E.g. n=2: `π₀={4}`, `F'={2068/4181, 6292/4181, 2/4181}` gives `D̃(F)=12498/4181≈2.99`
   but `D̃(π₀⊎L)=3` — here the inequality direction that would be *useful* (F' cut version has
   discrepancy **at least** as large as the ladder version) fails; other witnesses show it failing in
   the other direction too. This is exactly the same failure mode as R11's π₀-fixed single-move
   refutation (rule 34, ~30% fail) and R12's coupled-cut-descent (n=5 witness) — generalizing the move
   to "all cuts of F' at once" does **not** rescue it, because the flaw is holding π₀ fixed, not the
   move's granularity. **This is a clean new negative to bank: do not re-seed ANY π₀-fixed global
   merge of F', single-cut or multi-cut — the failure is structural in "π₀ fixed", not in cut count.**

2. **Slice-max(b) monotonicity at FIXED a₀ (a refined version of the GAP-P1′-b reduction-to-base
   claim).** I sampled `max_{π₀,F'} I_n` over configs with a₀ (π₀'s own fragmentation) held fixed and
   `b` (F''s cut budget) varying, `a₀+b≤n`. Result (n=4, random sampling, 6000 trials/cell, not
   provably the true max — see caveat):
   ```
   a0=0: b=0..4  maxI ≈ -4.50,-4.50,-3.59,-3.57,-3.57   (flat / mildly increasing)
   a0=1: b=0..3  maxI ≈ -2.50,-0.51,-0.53,-0.51          (NOT monotone in b; small bumps)
   a0=2: b=0..2  maxI ≈ -0.50,-0.50,-0.49
   a0=3: b=0..1  maxI ≈ -0.50,-0.05
   a0=4: b=0      maxI ≈ +0.02  (≈0, the true tie corner a0=n,b=0)
   ```
   The true extremal corner is **exactly `a0=n, b=0`** (matches the already-proven base slice). But
   slice-max is **not cleanly monotone in b at fixed a0** (small non-monotone bumps, e.g. a0=1:
   b=2 slightly worse than b=1 and b=3) — though all values stay comfortably below 0 once a0<n. This
   means the naive "monotone in b" reduction-to-base claim is at best true only in a weak/asymptotic
   sense near the true corner, not as a clean pointwise-in-b statement; a rigorous slice-max argument
   would need to handle a0<n uniformly (they're all far from 0) and treat `a0=n` (all budget on π₀,
   `F'` forced toward the ladder as `b→0`) as the delicate boundary — i.e. **the real content is a
   two-parameter (a0, b) argument, not a one-parameter descent in b alone.** This refines, but does not
   resolve, the coupled-cut-descent post-mortem's warning that "reachability isn't the obstacle,
   locality of the move is" — the obstruction is real and appears in a second independent test.

3. **A genuine two-parameter joint induction generalizing the (P_m)/(Q_m) ladder machinery to
   split (cut) blue objects, not just the full ladder.** The proven base-slice machinery
   (`base-slice-star.md`) works by inducting on ladder length `m` with red `R` against the **full**
   ladder `L_m`, using three peel identities (I1)-(I3) that all crucially exploit that the ladder's
   top rung is a **single part** `θ` (so removing/peeling it toggles parity on one clean interval
   `[·,θ)`). **Diagnosis of exactly why this does not survive to general F' (the concrete technical
   obstruction, not previously stated this precisely):** if the blue top rung is itself split into
   `a_j+1 ≥ 2` parts (as in a general F'), (I1)'s core step `N_P = N_{P'} + 1[t<θ]` (a single
   indicator) becomes `N_P = N_{P'} + Σ_i 1[t < c_i]` for the `a_j+1` split values `c_i` summing to
   `θ` — several possibly-overlapping indicators, not one clean interval, so parity toggles a
   *multi-interval, count-dependent* pattern rather than a single flip. A generalized peel identity
   would have to track not just a scalar `Δ_m(R)` but something like the *whole level function* of the
   split rung — i.e., it would have to re-derive the FLOOR/(★-id) machinery recursively at the
   sub-level, which is circular unless done very carefully. **Candidate concrete move:** define a
   TWO-parameter statement `(P_{m,k})` (ladder length `m`, remaining split-budget `k` for blue),
   proved by induction on `m` first splitting on "is blue's top rung split (k≥1 there) or not
   (k=0)": if not split, reduce to `(P_{m-1,k})`/`(Q_{m-1,k})` exactly as now; if split, peel the
   red parts against each of the `a_j+1` blue sub-parts in descending merged order and bound the
   resulting cross term by a NEW sub-lemma. **This is a real, previously-unattempted mechanism** —
   distinct from all banned routes (it's not a single-cut descent, not WM/HLP, not scalar
   Q≥S_π) because it never separates the base case from the lift: it's ONE induction whose `k=0`
   slice literally IS `(P_m)`/`(Q_m)` already proven. Risk: the "NEW sub-lemma" bounding the cross
   term when blue's rung is split is exactly the technical content that opening-1's failure suggests
   is hard (any answer that ignores π₀'s co-varying shape will likely fail the same way). Medium-high
   risk, but concrete and machinery-adjacent (reuses (I1)-(I4), Lemma 0, and the certified base case
   as the anchor `k=0` rather than as an external fact to "lift").

4. **(POS)/(Q) layer bookkeeping as the loaded IH (carried over from R13 explorer, still live and
   lower risk than 1-2 above).** `positive-layer-localization.md`'s `P ≤ Σ_{k≤K0} y_{2k}` is a clean
   half-result depending only on π₀. A numeric bound on `Q` (F''s negative layers) inherited under one
   further peel of F' would close `I_n=P-Q≤0` without needing majorization or any π₀-fixed move at all
   — this sidesteps both of opening 1/2's dead ends entirely since it never compares two different F'
   configs, only bounds Q intrinsically. Worth prioritizing over 1/2 given today's negative results.

### Candidate technique(s)
- A genuinely two-parameter (ladder-length `m`, blue-split-budget `k`) mutual induction generalizing
  the certified (P_m)/(Q_m)/(LB_m)/Lipschitz machinery (opening 3) — reuses all certified sub-lemmas,
  anchors at the already-proven `k=0` case, never separates base from lift.
- (POS)/(Q) intrinsic layer bound on F' alone (opening 4), avoiding any two-configuration comparison.
- Karamata/HLP-style smoothing (aimo-0146 template) remains a *possible* finishing device for a
  relaxed-LP version of the problem, but per the crux's own structure ("relaxed bound exceeds target,
  then re-impose exact discrete structure to kill the gap") this is essentially the already-DEAD
  GAP-IMR/integer-minimizer framing in different clothes — do not re-seed without a genuinely new
  angle on why THIS relaxation's equality case is dyadically infeasible.

### Cheap-kill candidates
- Before committing any π₀-fixed comparison of two F' configs (single-cut OR multi-cut, "merge to
  ladder" or any variant): run it against the n=2 witness `π₀={4}`, `F'={2068/4181,6292/4181,
  2/4181}` above (2 lines of Fraction arithmetic) — it already breaks the "merge F' fully to L, π₀
  fixed" direction cleanly and is a fast filter.
- For opening 3: before building out the two-parameter induction in full, check whether the
  cross-term bound is even TRUE at the smallest nontrivial split (`m=2`, blue's top rung split into
  exactly 2 parts, `k=1`) by brute-force Fraction search — this is a ≤30-minute numeric gate that
  would catch a false generalization before investing builder time.

### Knowledge-base entries to use
- `lemmas/base-slice-star.md` (the (P_m)/(Q_m)/(LB_m) machinery + Lipschitz collapse (I4) — the
  reusable engine for opening 3).
- `lemmas/floor-half-reduction.md`, `lemmas/ladder-interleaving-identity.md` (both fully general in
  F', unaffected by this round's findings).
- `lemmas/positive-layer-localization.md` (opening 4's starting point).
- knowledge_base.md's exchange/smoothing entries — relevant only as a cautionary template (see
  aimo-0146 below), not as a ready-made tool.

### Analogous past problems (cruxes)
- **aimo-0146** (combinatorics, extremal-principle/invariants-and-monovariants; APMO-style `S(G)=
  Σmin(deg u,deg v)` maximization, 2017 edges): crux move is "smooth a monotone bounded sequence
  toward extremal profiles via exchange, get a RELAXED bound that exceeds the true target by a fixed
  gap, then re-impose the exact discrete structure to kill the gap and confirm the relaxed equality
  case is infeasible." This is structurally the template underlying opening 4-of-R13 (Karamata
  smoothing to the tie family) and is exactly analogous in SHAPE to the already-DEAD GAP-IMR route
  (R9-R10, both dead: relaxed continuum optimum ≠ integer optimum, cross-scale rounding blocked). I
  do not think it offers fresh leverage here beyond what's already tried and killed — flagging it only
  so the outliner doesn't re-invent it as if it were new.
- No new corpus match found for the specific "generalize a peel/ladder induction to split blue rungs"
  mechanism of opening 3 — this appears to be a genuinely bespoke construction for this problem's
  dyadic structure, not a template borrowed from the corpus.

### Prior progress
- Base slice (b=0): FULLY PROVEN (`base-slice-star.md`). Not reattempted.
- FLOOR + (★-id): both fully general in F', already the reduction in force.
- All prior b-lift mechanisms (single-cut co-varying descent R12, full-WM-IH inheritance R13, (NEG)
  bound R13, scalar b-cutoff R11) remain dead; this round adds two more dead variants (opening 1) that
  are natural "multi-cut" readings of the same family — the family of "hold π₀ fixed, transform F'"
  moves is now thoroughly exhausted and should not be revisited in ANY form.

### Dead ends (do not retry)
- **"Merge all of F' back to the full ladder simultaneously, π₀ fixed" (this round): REFUTED.**
  970-2073 / 3000 failures across n=2..5, exact `Fraction`. Witness above. Do not re-seed any
  π₀-fixed global/multi-cut comparison of F' to L or to any other F'' — the flaw is "π₀ fixed," not
  cut-count; this closes off the entire family of moves that hold π₀ literally constant while
  varying F', for any number of simultaneous cuts.
- (Carried over, still dead) single-cut co-varying b→b−1 descent (R12), full-WM-IH inheritance under
  one peel (R13), (NEG) Q≥S_π (R13), scalar b-cutoff (R11).

### Small-case / intuition notes (conjectural / numeric evidence only)
- The true worst-case corner across the whole feasible family is exactly `a0=n, b=0` (all
  fragmentation budget on π₀, F' fully uncut) — confirmed at finer granularity (varying a0 and b
  independently, n=4) than R11's single data point; this is fully consistent with the already-PROVEN
  base-slice theorem being the tight extremal object, not just an extremal slice.
- Slice-max in `b` at fixed `a0` is close to flat/mildly non-monotone (small bumps, e.g. a0=1's
  b=0,1,2,3 give -2.50,-0.51,-0.53,-0.51) but never comes close to 0 except at the single corner
  `a0=n,b=0` — suggesting whatever argument closes the general case will need to treat "a0=n" (or
  near it) as a genuine special/boundary regime and everything else as comfortably slack, rather than
  a uniform one-parameter monovariant in `b` alone. This is weak, sampling-based evidence (not an LP
  optimum), so treat the "flat/non-monotone" claim as suggestive only, not established.
