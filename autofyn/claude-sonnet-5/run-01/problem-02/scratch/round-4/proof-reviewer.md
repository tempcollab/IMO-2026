# Proof review — round 4 — imo-2026-02

Reviewed all three built approaches independently and adversarially. Re-derived every load-bearing
symbolic claim from scratch with sympy (not trusting builder self-reports), and did an independent
20,000-sample numeric sweep plus an analytic argument for the rotation-sign-convention question the
dispatch flagged as highest priority.

## 1. `coordinate-groebner-elimination` — claimed Status: solved

**Verdict: CHANGES REQUESTED** (true Status: **partial**, not solved — overclaim caught and corrected).

What I independently re-verified as correct:
- `e1 = tK·(|AC|²/4)·g1(tL,...)`, `e2 = tL·(|AB|²/4)·g2(tK,...)` — rebuilt `e1,e2` from the file's own
  literal `cross`/`dot` definitions and confirmed both factorizations reduce to exactly 0 (symbolic,
  mod `ca²+sa²=1`).
- The full cofactor identity `2Z²·myexpr = (Z·P1)·g1 + (Z·QA+QB)·g2` — reran the file's own Appendix
  script from scratch (executed, not just read) and separately re-derived it independently (polynomial
  division in `tL` then `tK`, tracked all residual denominators); confirmed the identity holds as a
  **fully symbolic identity** modulo `ca²+sa²=1` (`sp.simplify` on the fully-expanded, fully-reduced
  difference gives exactly `0`, not just at sampled points). This part of the file is genuinely correct.
- `K_y = tK·X` and the barycentric argument `K_y = μq/2 > 0` (hence `X>0`) — correct, standard.

**The gap that sinks "solved":** the file's Setup section picks a specific rotation-sign convention
for `K,L` (`K = tK·(p·ca+q·sa, q·ca−p·sa)`, i.e. rotating ray `BA` by `−α` not `+α`) and states this
"is the branch matching the position hypotheses... confirmed by direct numerical construction below."
The section it points to is literally headed **"Existence / consistency check (numerical, corroborating
but not part of the logical proof)"** — the file's own words disclaim this as not a proof. I checked:
the underlying fact (that `−α`, not `+α`, is forced by `K` being interior to `△BMC`) **is true** — I
verified it two ways: (a) an analytic argument (K interior to `△BMC` ⟹ same side of line `AB` as `C`
⟹ `cross(A−B,K−B)` has the same sign as `cross(A−B,C−B) = −qa < 0` ⟹ forces the `−α` branch), and
(b) a 20,000-sample numeric sweep (random triangles + random interior points of `△BMC`, comparing the
true point against the formula's prediction using the true unsigned angle `α`): **zero failures**, max
error `1.4e-15`. So the fact is correct — but this file does not contain a proof of it, only the
numeric-existence check it itself disclaims. The sibling file `synthetic-angle-chase-aklastar.md`
closes this exact gap rigorously via an "interior-point side test" lemma (which I independently
verified symbolically); this file does not.

**A second, more serious gap this file does not even mention:** hypotheses (ii) `∠LBK=∠LNC` and (iii)
`∠LCK=∠BMK` are *unsigned* angle equalities. Encoding them as `e1=0`,`e2=0` via the
`cross(X,Y)·dot(W,Z) − cross(W,Z)·dot(X,Y)` construction only captures the directed-angle relation
`θ1≡θ2 (mod π)` — specifically the branch `θ1=θ2`, not the reflected branch `θ1=−θ2`/`θ1=θ2+π`, which
would require the sign-negated polynomial. This file's `e1,e2` are the *identical* construction used
by `synthetic-angle-chase-aklastar.md`, whose builder explicitly flags this branch-selection question
as the **sole remaining open gap**, checked only at 5 numeric configurations (not proved). This file's
"solved" claim does not raise this issue at all — a serious omission, since the identical construction
is used and the identical ambiguity applies.

Given both gaps, "solved" is a clear overclaim. True Status: **partial**. Real progress stands (the
full cofactor identity, independently reverified as exact — this is new and correct this round), but
two real gaps remain, one of which (the branch-selection issue for (ii)/(iii)) isn't even acknowledged.

## 2. `synthetic-angle-chase-aklastar` — self-reported Status: partial

**Verdict: CHANGES REQUESTED** (Status **partial** confirmed correct; the self-report is accurate,
neither over- nor under-claiming).

Independently re-verified:
- `myexpr·Z = 2(q−T_K X)A1 + 2(T_L X'−q)B1` — rebuilt from the file's own definitions and confirmed
  it holds as an **unconditional** polynomial identity (no `c²+s²=1` needed), matching the file exactly.
- `cross(A−B, K−B) = −T_K·s·|AB|²` and `cross(A−C, L−C) = T_L·s·|AC|²` under the stated parametrization
  — both reproduced symbolically, matching the file's claims exactly.
- The "interior-point side test" lemma (K interior to `△BMC` ⟹ `C`-side of line `AB` ⟹ forces `−α`,
  not `+α`) — this is a genuine, rigorous, non-numeric proof of exactly the fact `coordinate-groebner-
  elimination` left unproven. This is real progress and correctly promoted (see below).
- `sin α > 0`: correctly excludes **both** `α=0` and `α=π` via `K∉` the full line `AB` (not just the
  weaker "not on ray `BA`" argument flagged as insufficient by the round-4 outline-reviewer) — the fix
  requested by the outline was made correctly.

The one remaining, honestly-flagged gap (directed-angle branch selection for (ii),(iii), i.e. which of
`θ1=θ2` vs. the reflected relation matches the position hypotheses) is real and correctly identified as
not yet closed — only checked at 5 numeric configurations. **Additional note not caught by the
builder:** all 5 sampled configurations in the file's table share the identical value `α=0.05` (only
`a,p,q` vary) — so despite the write-up's framing ("five triangles of substantially different shape"),
the check has not varied `α` at all, which is exactly the parameter that could plausibly flip the
branch (e.g. near `α→0` or `α→π`). This makes the numeric evidence narrower than presented, though it
does not change the Status (already correctly `partial`, not claimed solved).

## 3. `inversion-at-a-collinearity` — self-reported Status: partial

**Verdict: CHANGES REQUESTED** (Status **partial** confirmed correct; self-report accurate).

- Lemma 0 (local re-derivation of "`A,K,L,A*` concyclic ⟺ `OM=ON`" for `AB≠AC`, replacing the stale
  citation into the sibling file) — independently checked (perpendicular-bisector midpoint computation)
  and correct.
- Lemmas 1–3 (inversion distance formula, similar-triangle correspondence, cross-ratio/concyclicity
  preservation) — previously certified, unchanged, still sound.
- The structural diagnosis that hypotheses (ii),(iii) cannot be translated via Lemma 2 centered at `A`
  (neither leg of the relevant angles passes through `A`) is a genuine, correctly-reasoned obstruction
  of this specific framing (single inversion at `A`), not merely "not yet found" — legitimate progress
  in narrowing the problem, even though it does not close it.
- The meta-observation that the isosceles branch-selection question (for this approach's own `A*`
  route) is moot for the *overall* problem's proof, because the sibling's cofactor identity treats
  `AB=AC` uniformly and needs no branch selection — logically sound, correctly scoped (explicitly not
  claimed to resolve this approach's *own* remaining branch-selection gap, only that it's not required
  elsewhere).

Still substantially incomplete (large open translation gap for (ii),(iii)); correctly kept live for
population diversity per CLAUDE.md's single-gap-trap guidance, since it is the only approach not
resting on the coordinate route's algebra.

## current.md

Updated `results/imo-2026-02/current.md`: Status remains **partial**. Recorded the round's real
advance (the `Z>0`/`D1>0` gap from rounds 2–3 is now fully and rigorously retired via
`synthetic-angle-chase-aklastar`'s interior-point side test) and the new common bottleneck exposed this
round: the directed-angle branch-selection question for hypotheses (ii),(iii), which both coordinate
approaches share (one addresses it honestly as open, the other omits it — now flagged explicitly).
Documented the `coordinate-groebner-elimination` overclaim (solved → partial) explicitly.

## Lemmas certified this round

- `results/imo-2026-02/lemmas/interior-point-side-test.md` — certified (general lemma: interior points
  of a triangle with two vertices on a line lie strictly on the third vertex's side; application to
  fixing the K,L rotation-sign convention). Sourced from `synthetic-angle-chase-aklastar.md`,
  independently reverified symbolically.
- `results/imo-2026-02/lemmas/cofactor-identity-myexpr.md` — certified (the unconditional polynomial
  identity `myexpr·Z = 2(q−T_KX)A1 + 2(T_LX'−q)B1`, no `c²+s²=1` needed). Independently reverified by
  full symbolic expansion from scratch. Explicitly scoped: this lemma is pure algebra and does **not**
  by itself certify the parametrization's geometric coverage or the (ii)/(iii) branch-selection
  question — noted in the lemma file to prevent future overclaiming from citing it as settling more
  than it does.

Rejected (not certified as separate lemmas this round): `coordinate-groebner-elimination`'s own
"Z>0 on the geometrically valid locus" and "fully-polynomial cofactor identity" promotable-lemma
proposals — the cofactor identity is subsumed by the newly-certified `cofactor-identity-myexpr.md`
(same fact, cleaner normalization, already reviewer-verified); the "Z>0" lemma as stated in that file
implicitly assumes the (unproven-in-that-file) rotation-sign coverage claim to even make its
computation meaningful (it uses `K_y = t_K·X` as given, which presupposes the parametrization already
represents the real `K`) — superseded by `interior-point-side-test.md`, which proves the needed fact
without this gap.

## Ranker outcomes recorded

- `coordinate-groebner-elimination`: `partial` (overclaim caught; two real gaps: unproven-in-file
  rotation-sign convention, and the unaddressed (ii)/(iii) directed-angle branch-selection issue).
- `synthetic-angle-chase-aklastar`: `advanced` (Z>0 gap fully and rigorously closed this round;
  remaining gap precisely isolated and honestly self-reported).
- `inversion-at-a-collinearity`: `partial` (self-assessment confirmed accurate; genuine but
  incomplete structural progress, valuable diversity).

## Overall

No approach reaches `solved` this round. The population's central wall from rounds 2–3 (`Z≠0`/`D1≠0`)
is now genuinely and rigorously retired by `synthetic-angle-chase-aklastar`. A new, sharper common
bottleneck has emerged and is now explicit in `current.md`: the directed-angle branch-selection
question for hypotheses (ii),(iii) — i.e., proving (not just numerically checking) that the specific
polynomials `e1,e2` (as opposed to their sign-flipped alternatives) correctly encode the unsigned angle
equalities given the position hypotheses ("K inside ∠LBA", "L inside ∠ACK", etc.). This should be the
explicit focus for the next round's explorers/outliner — likely via using the position hypotheses
(currently unused for this purpose) to pin the branch directly, analogous to how the interior-point
side test pinned the K,L rotation-sign convention this round.
