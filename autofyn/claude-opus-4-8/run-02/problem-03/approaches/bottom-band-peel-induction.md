# Approach: bottom-band-peel-induction (GAP-P1′-b, far-apart bottom split)

## Status
unsolved  (RETHINK / retire — the cheap-kill HARD GATE FAILED: the bottom split is
split-agnostic exactly as both explorers warned; the framing cannot close the b-lift. This
round is a rigorous structural NEGATIVE, documented below so the field does not retry it.)

## Spec note
The outline-reviewer imposed a HARD CHEAP-KILL GATE before any proof effort: numerically test,
over thousands of exact-`Fraction` feasible Case-B configs, whether the bottom-band overlap
`λ(O_{F_{>τ}}∩O_{F_{≤τ}})` is genuinely parity-controllable by the peel, i.e. whether the
reduction's key inequality actually closes via the induction hypothesis. It does not. I ran the
gate first (exact `Fraction`, integer and fractional feasible configs, n=2..6) and it blew up on
all three sub-routes (bottom-SCALE peel, bottom-VALUE-BAND peel, and the parity/near-0 routing).
Per the reviewer's own instruction ("If the cheap-kill blows up, STOP, record the exact witness
and the negative honestly … do NOT force a proof"), I stop and record the negative. No proof is
overclaimed.

## Setup (certified, imported)
`F = ⊎_{j=0}^{n} π_j` is a simultaneous refinement of the dyadic ladder `{2^0,…,2^n}`
(Structure Lemma); scale `j` is a partition `π_j` of `2^{n−j}` into `a_j+1` parts, with the cut
budget `Σ_{j=0}^n a_j ≤ n`. `ΣF = 2^{n+1}−1` (odd). For a positive multiset `P`,
`N_P(t)=#{p∈P:p>t}`, `O_P={t>0:N_P(t) odd}`, `D̃(P)=λ(O_P)=Σ_i(−1)^{i−1}w_i` (certified
Lemma G). The b-lift target is `D̃(F) ≥ 1` for **all feasible real configs** (equivalently
`D̃(π_0⊎F') ≥ 1` for any real `π_0`, `Σ=2^n`, `≤n+1` parts, and any dyadic refinement `F'` of the
sub-ladder; base slice `F'=L` is certified in `base-slice-star.md`).

Tools used in the gate (all certified):
- **SD/PEEL identity** (`peel-difference-bound.md` (1)): for any split `F=A⊎B`,
  `D̃(F)=D̃(A)+D̃(B)−2λ(O_A∩O_B)`.
- **DIFF bound** (`peel-difference-bound.md` (2)): `D̃(A⊎B) ≥ |D̃(A)−D̃(B)|`.
- **Universal bound** `D̃(P) ≤ ΣP`.
- **Parity Lemma** (`parity-odd-total.md`): integer multiset + odd total ⇒ `D̃` odd ⇒ `D̃≥1`.

## Structural fact behind the bottom split (correct, but not enough)
For a **value** threshold `τ`, split `F=F_{>τ} ⊎ F_{≤τ}` (`F_{>τ}=` parts `>τ`). Every part of
`F_{≤τ}` is `≤τ`, so `O_{F_{≤τ}} ⊆ (0,τ)`. On `(0,τ)` every part of `F_{>τ}` exceeds `t`, so
`N_{F_{>τ}}(t)=|F_{>τ}|` is constant. Hence on `(0,τ)`, `O_{F_{>τ}}` is either all of `(0,τ)`
(if `|F_{>τ}|` odd) or empty (if `|F_{>τ}|` even), giving the exact overlap value

```
   λ(O_{F_{>τ}}∩O_{F_{≤τ}}) = D̃(F_{≤τ})·1[|F_{>τ}| odd] .
```

Substituting into SD/PEEL:
```
   |F_{>τ}| even :  D̃(F) = D̃(F_{>τ}) + D̃(F_{≤τ})           (bottom band ADDS)
   |F_{>τ}| odd  :  D̃(F) = D̃(F_{>τ}) − D̃(F_{≤τ})           (bottom band SUBTRACTS)
```
Both hold for **real** configs (verified: `0` mismatches over the samples below). This is the
"cleaner overlap" the outline hoped for. But the odd branch is a **difference**, i.e. it is the
certified DIFF/overlap term itself — the same object the whole field is stuck on. The bottom
split does NOT escape it. Below are the three exact ways it dies.

## Cheap-kill result 1 — bottom-SCALE peel via DIFF is DEAD (needs `D̃(G)≥2`, which fails)
Natural scale split: `F = G ⊎ π_n`, `G=⊎_{j=0}^{n−1}π_j` (a refinement of `{2,…,2^n}`,
`ΣG=2^{n+1}−2`), `π_n` = a partition of `1`. The clean hope: `G/2` is a refinement of
`{1,…,2^{n−1}}` with total `2^n−1 = 2^{(n−1)+1}−1`, so by the induction hypothesis (the whole
theorem at `n−1`) `D̃(G/2)≥1`, whence `D̃(G)=2D̃(G/2)≥2`; since `D̃(π_n)≤Σπ_n=1`, the DIFF bound
gives `D̃(F) ≥ D̃(G)−D̃(π_n) ≥ 2−1 = 1`.

**This fails: `G/2` is not a bona-fide `(n−1)`-feasible instance** (the reviewer's mandated
Step-3 check). The cut budget of `G` on scales `0..n−1` can be up to `Σ_{j<n}a_j ≤ n`, but an
`(n−1)`-instance allows only `≤ n−1` cuts. When the whole budget sits on the top scales, `G/2`
uses one cut too many and the IH does not apply — and indeed `D̃(G)` drops below `2`.

Exact `Fraction` witness (n=2): `π_0={2,1,1}`, `π_1={2}`, `π_2={1}`, so
`F={2,2,1,1,1}` with `D̃(F)=2−2+1−1+1=1` (true). Here `G={2,2,1,1}` with
`D̃(G)=2−2+1−1=0`, and `D̃(π_2)=1`, so the DIFF bound yields only
`D̃(F) ≥ D̃(G)−D̃(π_2) = 0−1 = −1` — vacuous. (`G/2={1,1,½,½}` uses budget `2 > n−1 = 1`,
so the IH is unavailable and `D̃(G/2)=0`.) Verified over integer feasible configs `n=2..6`:
`D̃(G)<2` occurs routinely (e.g. `D̃(G)=0` for the above). Over fractional feasible configs
`D̃(G)<2` also occurs (14/513 at n=3). **Bottom-scale DIFF peel: DEAD.**

## Cheap-kill result 2 — bottom-VALUE-BAND peel has no inductive engine
At a value threshold `τ` the odd branch needs `D̃(F_{>τ}) − D̃(F_{≤τ}) ≥ 1`. This is true (it
equals `D̃(F)`), but to *prove* it one needs `D̃(F_{>τ}) ≥ 1` from an IH **plus** a separate
handle on `D̃(F_{≤τ})`. Neither is available:

- `F_{>τ}` is a **value truncation**, not a dyadic-ladder refinement, so it is not a smaller
  feasible instance and **no IH gives `D̃(F_{>τ})≥1`**. Exact `Fraction` witness (n=3):
  `F={4,4,2,2,1,1,1}` (π_0={4,4}, π_1={2,2}, π_2={1,1}, π_3={1}), `D̃(F)=1`. At `τ=1`:
  `F_{>1}={4,4,2,2}` with `D̃(F_{>1}) = 4−4+2−2 = 0` — not `≥1`. (`|F_{>1}|=4` even, so the
  bottom band ADDS: `D̃(F)=0+D̃({1,1,1})=0+1=1`, and the ENTIRE surplus is carried by the
  bottom unit fragments, none by the top.)
- The residual `D̃(F_{≤τ})` in the odd branch is unbounded below `1` for real configs, so the IH
  `D̃(F_{>τ})≥1` (even if it held) would be short by exactly `D̃(F_{≤τ})` — the certified
  DIFF/overlap gap. Split-agnostic, as both explorers proved.

**Bottom-value-band peel: no engine.**

## Cheap-kill result 3 — the parity / near-0 routing dies on real configs
The framing's `+1` injector was the Parity Lemma applied in the near-0 count-parity band. This
works ONLY under integer normalization and CANNOT be reached for the real-valued theorem:

- The near-0 contribution below the smallest part `z_min` is exactly `z_min·1[|F| odd]`. Under
  integer normalization `z_min ≥ 1`, so the band can carry a full unit — this is the R7/R8
  "surplus concentrates near 0" phenomenon (confirmed in result 2: at integer scale the whole
  `+1` sat on the unit fragments `{1,1,1}`). But for **real** configs `z_min → 0`, so the near-0
  band carries `→ 0`. Exact `Fraction`: over fractional feasible configs the near-0 band is
  `< 0.01` in ≈40% of trials (212/513 at n=3, 55/151 at n=4, 22/49 at n=5). Concrete real
  witness: `π_2` cut as `{1.5,0.5}` gives `F={4,4,2,2,1.5,1,0.5}`, `D̃(F)=1`, but the near-0 band
  below `z_min=0.5` contributes only `0.5` — shrinking the smallest fragment sends it to `0`. The
  surplus is NOT concentrated near 0 for reals.
- The Parity Lemma (`parity-odd-total.md`) requires **integer** parts; it is silent on real
  configs. Reaching integers legitimately requires the Integer-Minimizer Reduction **GAP-IMR**,
  which was **PROVEN equivalent-difficulty to the whole target** in round 10
  (`vertex-integrality-parity`, RETHINK) — so parity supplies no free lunch here.

**Parity/near-0 routing: unreachable for the real theorem.**

## Verdict
The cheap-kill HARD GATE failed on every sub-route. The bottom-band overlap term
`λ(O_{F_{>τ}}∩O_{F_{≤τ}}) = D̃(F_{≤τ})·1[|F_{>τ}| odd]` is exact but split-agnostic: its odd
branch is the certified DIFF/overlap wall verbatim, `F_{>τ}` is not a feasible sub-instance
(no IH), the scale split needs `D̃(G)≥2` which fails on the budget, and the `+1`-via-parity
injector exists only for integer configs (unreachable without the equivalent-difficulty
GAP-IMR). This confirms the game-explorer's finding that ALL splits hit the overlap term and the
outline-reviewer's warning that a bottom split does not automatically escape the wall. **Retire
this framing** (RETHINK); it should not be rebuilt. The one exact structural gain worth banking
is the bottom-band overlap identity below.

## Approaches tried
- **bottom-band-peel-induction (R15, NEW)** — RETHINK / retire. Cheap-kill HARD GATE failed on
  all three sub-routes: (1) bottom-SCALE DIFF peel needs `D̃(G)≥2`, refuted by the budget
  (witness `F={2,2,1,1,1}`, `D̃(G)=0`); (2) bottom-VALUE-BAND peel reduces the odd branch to the
  certified DIFF/overlap term and `F_{>τ}` is not a feasible sub-instance (witness
  `F={4,4,2,2,1,1,1}`, `D̃(F_{>1})=0`); (3) parity/near-0 injector only exists for integer
  configs, `z_min→0` kills the near-0 concentration on reals, and integer reduction (GAP-IMR) is
  proven equivalent-difficulty (R10). Bottom-band overlap identity banked as the one exact gain.

## Current best
The exact **bottom-band overlap identity** (proved fully this round, real-valued):
for any value threshold `τ`, splitting `F=F_{>τ}⊎F_{≤τ}`,
```
   λ(O_{F_{>τ}}∩O_{F_{≤τ}}) = D̃(F_{≤τ})·1[|F_{>τ}| odd],
   hence  D̃(F) = D̃(F_{>τ}) + (−1)^{|F_{>τ}|} D̃(F_{≤τ}).
```
This is a clean, correct specialization of the certified SD/PEEL identity to a bottom split, but
its odd branch is exactly the certified DIFF/overlap wall (split-agnostic), so it does not close
the b-lift. No progress on GAP-P1′-b; the framing is retired.

## Promotable lemmas
**Bottom-band overlap identity.** For any finite positive multiset `F`, any `τ>0`, split
`F=F_{>τ}⊎F_{≤τ}` by value. Then `O_{F_{≤τ}}⊆(0,τ)` and `N_{F_{>τ}}≡|F_{>τ}|` on `(0,τ)`, so
`λ(O_{F_{>τ}}∩O_{F_{≤τ}}) = D̃(F_{≤τ})·1[|F_{>τ}| odd]`, giving
`D̃(F) = D̃(F_{>τ}) + (−1)^{|F_{>τ}|}D̃(F_{≤τ})`. Proved in full above from the certified SD/PEEL
identity; verified `0` mismatches over integer and fractional feasible configs `n=2..6`
(exact `Fraction`). Reusable as an exact bottom-split accounting tool (NOT a closer — its odd
branch is the certified overlap term). Reviewer may certify into `lemmas/` if useful.
