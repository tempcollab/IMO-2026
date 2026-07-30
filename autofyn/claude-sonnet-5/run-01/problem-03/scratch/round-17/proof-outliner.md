# Round 17 outline field — IMO-2026-03

Standings checked via `mcp__approach-ranker__sample_approaches` (k=10, 12
total approaches on file). Top of field: `universal-adversary-strategy`
(Elo 1712.8, stale, last_outcome "advanced" — round 16 closed Region 1+2 of
`m=4` Case C, Region 3 open). `recursive-embedding-induction` (Elo 1677.1)
is the certified-complete lower-bound approach; nothing changed for it this
round, advance unchanged, no build needed. All other approaches (Elo
1350–1635) are either dead-end/RETHINK-retired mechanisms
(`case-c-slack-covering`, `defect-hall-deficiency`,
`case-c-secondary-extremality`, `relaxed-adversary-transfer`,
`majorization-smoothing`) or superseded partial results
(`geometric-dominance-construction`, subsumed by
`recursive-embedding-induction`'s unrestricted closure). None of these are
touched this round.

**Build set this round: `universal-adversary-strategy` only.** No second
slug is opened for Region 3 itself (would be the single-gap trap CLAUDE.md
forbids — a second lens on the *same* wall). The vertex/extreme-point idea
(§2 below) is offered as a genuinely different-framing candidate per the
plateau-breaking rule, but scoped as a feasibility check the outline-reviewer
should decide whether to register and dispatch this round or hold for next
round once `universal-adversary-strategy`'s Region-3 push lands — see the
reviewer question at the end of §2.

---

## 1. `universal-adversary-strategy` (revise) — target: close Region 3 of `m=4` Case C

**Status:** `partial` (unchanged coming in). Region 1 and Region 2 of the
5-strategy `m=4` Case C split are fully closed and certified
(`lemmas/m4-region-a-region-b.md`). Region 3 (`t_1<\tfrac4{15}\Sigma$ and the
tail `(t_1,t_2,t_3)` is itself in `V_3`'s Case C) is open.

**Approaches tried (this slug, cumulative — see `current.md` for full
history).** Loose Strategy-B bound: proved algebraically insufficient in
Region 3 (round 16). Strategy C_{23} alone: this round's explorer proved
it is **not** universal on Region 3 (24% of a 17,992-trial random sample
violate the target using `StratC_{23}` alone; smallest exact witness
`A=(937,457,390,142)`). Full 5-strategy `\min`: zero violations found in
every test to date (≈44,000+ trials this round alone, plus a 60-restart
`differential_evolution` adversarial search whose only zero-margin point is
the already-known extremal `A\propto(6,4,3,2)`, sitting exactly on the
Region 1/Region 3 boundary, not in Region 3's interior) — strong evidence
the existing menu (no 6th strategy needed) is exactly sufficient, but no
proof yet.

**Two candidate simplifications from the explorer, both spot-checked by me
this round — one refuted, one narrowed.**

1. *"Region 1's loose `StratA` bound automatically covers Region 3too"* —
   **REFUTED, not just unconfirmed.** Region 1's proof shows
   `\mathrm{StratA}\le\tfrac47\Sigma-\tfrac{t_1}7`, an affine function
   **strictly decreasing** in `t_1`, equal to `c(3)\Sigma` exactly at
   `t_1=\tfrac4{15}\Sigma`. Since it is strictly decreasing, for
   `t_1<\tfrac4{15}\Sigma` (all of Region 3) this same loose bound is
   **strictly greater than** `c(3)\Sigma`, not less — the bound gets worse,
   not better, as `t_1` shrinks below the Region-1 threshold. So the loose
   `V3`-BOUND-based bound on `StratA` can never by itself certify any point
   in Region 3's interior; whenever `StratA` numerically rescues a Region-3
   trial (round-17 explorer found this happens for a large share of the
   4,355 `C23`-failures), it must be because `StratA`'s **true, exact**
   value is below the loose bound in that regime — i.e. using the exact
   three-branch form of `V_3(t_2,t_3,p_1-t_1)` rather than the blanket
   `\le\tfrac47\sigma` inequality. (The explorer's own writeup already
   flagged this as "worth double-checking… matches what we see
   numerically: StratA meets target on some but not all of Region 3" — my
   spot check confirms the mechanism precisely: the loose bound is
   *never* sufficient in Region 3's open interior, so any Region-3a/3b
   split by "does the loose bound already work" is empty on the 3a side.)

2. *"`StratB=StratC_{23}` identically on (part of) Region 3"* —
   **REFUTED as a general identity, confirmed to be a coincidence at
   symmetric points only.** I checked both of the round-17 explorer's own
   witnesses with exact `Fraction` arithmetic:
   - `A=(10,10,10,9)`: `StratB=39/2`, `StratC_{23}=39/2` — **equal**
     (matches the explorer's report).
   - `A=(937,457,390,142)` (Region 3, `C_{23}`-alone failure witness):
     `StratB=1993/2=996.5`, `StratC_{23}=1079` — **not equal**
     (`StratB` is the one that rescues this point; target `=5136/5=1027.2`,
     and `996.5\le1027.2$ with real margin, while `1079>1027.2`). So the
     equality at `(10,10,10,9)` (and at `(8,4,3,2)`) is a coincidence of
     those specific highly-symmetric configurations (where the base
     triples of `StratB`'s and `StratC_{23}`'s recursive `V_3` calls
     happen to land in Case-C branches that evaluate to the same number),
     not a general algebraic identity over Region 3. A proof cannot use
     "`StratB=StratC_{23}`" as a shortcut.

**Revised concrete plan for this slug (gaps marked `[GAP]` for the
builder).**

Since neither shortcut survives, the closure must track the **exact**
(not loose) value of whichever strategy wins, case-by-case, inside Region 3.
The natural structure (confirmed by both witnesses above and the round-16
worked example `A=(x,x,x,0.9x)`) is:

- Region 3's own hypotheses force the tail `(t_1,t_2,t_3)` into `V_3`'s
  Case C, so `V_3(t_1,t_2,t_3)=\min(t_1+t_3/2,\ t_2+L_2(t_1-t_2,t_3))`
  (two branches, no ambiguity — this part is already fully derived, not a
  gap).
- `[GAP 1]` Prove a genuine (non-loose) upper bound for `StratB=
  p_1/2+V_3(t_1,t_2,t_3)` using the *exact* two-branch form above (not the
  blanket `\le\tfrac47S_{\mathrm{tail}}` inequality), i.e. bound
  `p_1/2+\min(t_1+t_3/2,\ t_2+L_2(t_1-t_2,t_3))` directly against
  `c(3)\Sigma` using Region 3's three defining inequalities
  (`p_1<\Sigma/2`, `t_1<\tfrac4{15}\Sigma`, `t_1<S_{\mathrm{tail}}/2`) plus
  whichever extra structural facts about `t_2,t_3` are needed. This is the
  branch that rescues witness `A=(937,457,390,142)` and should be tried
  first since it is one recursion level shallower than `StratC_{23}`
  (no case split needed on a second, `StratC`-specific base triple).
- `[GAP 2]` For the residual sub-region where `[GAP 1]`'s bound is not
  enough (if any — must be checked, not assumed empty), prove the analogous
  exact bound for `StratC_{23}=t_3+V_3(p_1,t_1,t_2-t_3)`, tracking which of
  `V_3`'s three branches (A/B/C) the base triple `(p_1,t_1,t_2-t_3)` lands
  in — confirmed this round (both worked witnesses) that the base can land
  in Case B (the `A=(937,...)` witness: base `(937,457,248)`, Case B, value
  `=937` exactly, contributing to why `C_{23}` alone fails there) **or**
  Case C (the `(10,10,10,9)` and `(8,4,3,2)` witnesses) — both branches of
  the base triple are genuinely reachable inside Region 3 and must both be
  handled, not assumed away.
- `[GAP 3]` Determine whether `StratC_{12}`/`StratC_{13}` are ever needed
  inside Region 3, or whether (as round 17's explorer found empirically —
  no counterexample where either is the unique winner in Region 3) `StratA`
  ∪ `StratB` ∪ `StratC_{23}`'s exact bounds suffice to close Region 3 in
  full. If `[GAP 1]`+`[GAP 2]` together are shown to cover all of Region 3
  with a clean case split (e.g. by which of `V_3`'s branches the relevant
  base triple lands in, giving a small, explicit finite sub-case count —
  not open-ended), `StratC_{12}`/`StratC_{13}` can be dropped from the
  Region-3 proof entirely (they remain in the menu for Regions 1/2 and for
  whatever role they play, if any, outside `m=4` — out of scope here).
- Concrete reusable assets for the builder: witness
  `A=(937,457,390,142)` (`StratC_{23}` alone fails, `StratB` rescues,
  base of `StratC_{23}` lands in `V_3`-Case-B); witness `A=(8,4,3,2)`
  (all 5 strategies tie exactly at margin `1/255\cdot\Sigma`, base of
  `StratC_{23}` lands in `V_3`-Case-C); witness `A=(10,10,10,9)`
  (`StratB=StratC_{23}` coincidentally, both in `V_3`-Case-C); and the
  fixed-tail family `A=(p_1,4,3,2)` showing the unique global tight point
  over *all* of Case C is `p_1=6` (Region 1's boundary), not an interior
  Region-3 point — useful for sanity-checking any candidate closed form
  (it must attain equality only at `p_1=6`, strict slack everywhere else on
  that family).

**What this round should NOT attempt:** general `m\ge5` — untouched again
this round by design, per the round-16 review's own next-step note; the
5-strategy menu here is `m=4`-specific and does not generalize without
separately resolving Lemma SLACK-COVER's necessity at `m\ge6` (already
proved necessary there, round 15).

**If the builder cannot close all of `[GAP 1]`–`[GAP 3]` this round:**
report exactly which sub-case(s) remain, with the sharpest available exact
witness for each — do not round up to "Region 3 is closed" without a
completed case-exhaustive argument (verified equality/margin at every
witness is evidence, not proof, per CLAUDE.md's rigor rules already
enforced on this slug for 5+ rounds running).

---

## 2. New candidate slug (scouting-scoped only): vertex/extreme-point reduction on `A`

**Not added to this round's build set — offered to the outline-reviewer as
a plateau-breaking candidate, with an explicit recommendation to scope it
narrowly if registered.**

**Why it's worth considering at all.** `universal-adversary-strategy` has
now spent rounds 12–17 (6 rounds) inside one framing — fix `A`, search over
Xiang-Yu response strategies/case-splits — and Region 3 is the third
consecutive round-level "one more sub-case" gap in that same framing
(HALF-BOUND's sub-case → SLACK-COVER's existence question → now Region 3's
exact-branch tracking). Per CLAUDE.md's plateau rule, that is a legitimate
trigger to put a genuinely different framing on the table, not just another
bypass inside the same casework. The round-17 `m5-fresh` explorer's
proposal — reduce "for every configuration `A`" to "for finitely many
extremal vertex configurations of `A`," via the observation that `V_m(A)`
is piecewise-linear in `A` on each fixed-strategy/fixed-branch cell, so the
defect `c(m-1)\Sigma(A)-V_m(A)` is piecewise-linear too and its infimum
over each cell sits at a vertex — genuinely quantifies over *which
configurations* need checking, not over *which response* wins, a different
axis from every mechanism tried so far (fixed-shape pairing, scalar
averaging, Hall/König covering, greedy scan-order, and the current
5-strategy-menu casework itself).

**Why it's still too underbaked to build in full, and how to scope it if
opened.** The explorer is explicit and I agree: no affineness-per-cell
proof was attempted, no vertex-count induction was attempted, and the
biggest risk is real — if the number of cells/vertices grows
combinatorially with `m`, this collapses into "more casework," the exact
fate CLAUDE.md's own history log records for `minimax-mixed-duality` and
`case-c-secondary-extremality`. Per CLAUDE.md's instruction to avoid
premature full builds, if the outline-reviewer registers this slug this
round, its build should be capped to a **feasibility check only**, not a
general-`m` proof attempt:

1. Formalize "`m=4` Case C, Region 1 ∪ Region 2" (already fully closed by
   hand algebra) as a small number of explicit polyhedral cells (one per
   strategy-branch combination already used in the certified proof).
2. Verify directly (not assume) that `A\mapsto V_4(A)` restricted to each
   such cell is genuinely affine, by re-deriving it from the already-proved
   Region 1/Region 2 formulas (`\mathrm{StratA}=t_1+V_3(t_2,t_3,p_1-t_1)`
   with `V_3` in its Case-C branch, etc.) — this is a re-statement of
   already-proved content in vertex-reduction language, not new math, and
   should be quick to confirm or refute.
3. Confirm the known extremal vertex `A\propto(6,4,3,2)` is recovered as
   *the* vertex of the Region-1/Region-3-boundary cell by the general
   vertex-reduction lemma, not just by the ad hoc monotonicity argument
   already in the file.
4. **Explicitly stop there.** Do not attempt Region 3's cells (still open
   in the sibling approach) or any `m\ge5` cell count in this first build.
   Report back whether step 2's affineness holds cleanly and whether the
   cell/vertex count for `m=4` looks small and explicit (good sign) or
   already unwieldy (bad sign, matching the risk flag).

**Recommendation to the outline-reviewer:** register this as a new slug
(e.g. `vertex-reduction-on-adversary`) with the four-step scope above as
its only mandate this round, OR hold it for round 18 if the reviewer judges
`universal-adversary-strategy`'s Region-3 push (§1) is likely to close this
round and a second slug isn't needed yet — both are defensible; I flag the
tradeoff rather than force it, since the plateau is real (3 rounds of
same-framing sub-case gaps) but Region 3 also looks closer to closed than
open (zero violations in ~44,000 trials, one precisely bounded residual
question) so the urgency of diversifying is moderate, not acute. If
registered, it must NOT be graded against Region 3 closure — its only job
this round is the feasibility check in steps 1–4, explicitly not a
competing attempt at the same gap.
