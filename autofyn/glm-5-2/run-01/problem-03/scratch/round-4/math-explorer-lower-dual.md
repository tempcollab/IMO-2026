## imo-2026-03  (LOWER-bound 4th-framing scout — LP / Farkas duality lens)

Scouting a GENUINELY orthogonal 4th framing for the open lower wall (odd-count
non-dyadic leftover / deficit-covering `Σ gaps + leftover ≥ 1` when `p_m < 1`).
Tower units throughout; target `D ≥ 1`. All numerics below are EVIDENCE/conjecture
unless labeled PROVED (the LP-dual existence per type is numerically verified, not a
theorem). Scripts: `/tmp/round-4/lp_dual_probe.py`, `/tmp/round-4/cert_feasibility.py`.

### Distinct openings (the four candidate 4th framings, assessed)

**[WINNER] LP / minimax DUALITY (Farkas separating-hyperplane).** Xiang's
refinement-min of `D` is, **per combinatorial type**, an EXACT linear program
(not a relaxation): variables `p_k` (piece lengths, sorted desc), objective
`D = Σ_k (-1)^k p_k`, constraints = (i) **bin-sum equalities**
`Σ_{k: b(k)=t} p_k = 2^{n-t}` for each tower piece `t` (the bin assignment
`b(k)` = which tower piece spawned piece `k`), (ii) sort order `p_k ≥ p_{k+1}`,
(iii) `p_k ≥ 0`. *Why exact, not a relaxation:* any composition of a tower
piece of size `L` into `r ≥ 1` positive parts is a valid split tree (split off
pieces one at a time), so for a fixed `(bin assignment, sort order)` the
bin-partition LP IS the refinement LP restricted to that type cell. The LP DUAL
gives a **certificate** that `D ≥ (dual objective)` over the whole cell — a
genuine lower bound on Xiang's min that does NOT evaluate `D`'s sign pattern at
all. This is the separating-hyperplane / Farkas form of the charging argument,
made **global** (one LP per type, solved simultaneously, not a greedy per-pair
charge). **Escape from the convergence trap:** the three existing framings all
bound `D` directly and stall on the **leftover's global position-sign** (a primal
property). The LP-dual never computes any leftover's sign — it asks whether
"`D ≥ 1`" is a *linear consequence* of the bin-sum + sort constraints. The
obstruction killing the three framings (V-shape: LOCAL rebalancing fails) is a
LOCAL obstruction; LP duality is GLOBAL, so it sidesteps it by construction.

**KEY numerical finding (verified, not proved):** for EVERY sampled combinatorial
type of `T_2, T_3, T_4` (400/250/600 random refinements, incl. all odd-`m`
types — the wall regime), the LP primal min over the cell is `≥ 1`, and the dual
optimum (strong duality) is `≥ 1` with **minimum exactly 1** over the "tight"
types (where Xiang reaches the wall). The dual marginals (shadow prices on the
bin-sum equalities) are **sign-patterns on bins**: `(1,-1,-1,-1)` (objective
`2^n − (2^n−1) = 1`, the dominance margin G4!), `(0,0,1,-1)`, `(1,-1,1,-1)`
(objective 5, looser), etc. — always `y_eq[t] ∈ {+1,−1,0}` with
`Σ_t y_eq[t]·2^{n−t} ≥ 1`. The objective-1 certificates are precisely the
dominance-margin pattern `+1` on the top bin `2^n`, `−1` on enough smaller bins
that `Σ = 2^n − (2^n − 1) = 1`. So the G4 "dominance margin" insight is REALIZED
HERE AS A RIGOROUS FARKAS CERTIFICATE, not the conjectural "1 is conserved"
charging of gaps-leftover.

**[NOT orthogonal — reject] Integral / measure transport (lens 2).** `D = ∫(N(t) mod 2) dt`
is already the tail-count framing's functional. A "convex/monotone functional of
`N(t)` lower-bounding `D`" is either `D` itself (round-3 explorer confirmed `D`
is NOT monotone/convex — the V-shape) or a weaker functional `≤ D` that must
still be proved `≥ 1` — i.e. a proof of `D ≥ 1` in disguise. No escape; same
wall, same machinery (layer-cake/D-integral).

**[NOT orthogonal — reject] Sign-reversing / parity-pairing injection on odd
groups (lens 3).** A sign-reversing involution pairing odd-group leftovers
across the spine is a refinement of spine pair-cancellation (tower-induction S1)
+ gaps-leftover charging (framing 3). The obstruction IS that the leftover's
sign is GLOBAL position-parity — an involution would have to control global
position parity, which is exactly the wall. Technique upgrade within framing
2/3, not a new framing.

**[DEAD] Alternative Liu config (lens 4).** Verified (P2, n=3): the tower `T_3`
is the UNIQUE best Liu config — among 60 random non-tower 4-piece configs
summing to `D_3=15`, the best achieves `min_X D = 1.61 > 1`, i.e. WORSE for Liu.
Extends the round-3 n=2 saddle finding. No non-tower config reaches the tight
`D = 1`, so a different skeleton cannot give the same value `2^n/D_n`. Lens-4
route change is dead for a tight bound.

### Candidate technique(s) — for the WINNER (LP/Farkas)
- **LP strong duality / Farkas lemma** (the separating-hyperplane certificate:
  `D ≥ 1` as a linear consequence of bin-sum + sort constraints).
- **Dual reconstruction as a nonneg flow:** stationarity reads
  `y_eq[b(k)] = (−1)^k + y_ub[k] − y_ub[k−1]`, `y_ub ≥ 0`, `y_ub[−1]=y_ub[m−1]=0`.
  So `y_ub` is a **nonneg "mountain"** on the position chain whose discrete
  derivative reconstructs `y_eq[b(k)] − (−1)^k`. The proof obligation per type:
  exhibit such a nonneg `y_ub` (with consistent `y_eq` per bin) s.t.
  `Σ_t y_eq[t]·2^{n−t} ≥ 1`. This is linear-algebra feasibility, NOT
  sign-bookkeeping.
- Composes with certified `pl-breakpoint-minimum` (lands the global min at a
  breakpoint/tie config = a type-cell vertex; the LP certifies each vertex).

### Concrete first sub-step a builder could attempt
1. Formalize the per-type LP exactly (variables `p_k`, bin-sum equalities, sort
   `p_k ≥ p_{k+1}`, `p ≥ 0`; objective `D`). Confirm `min-cell-D ≥ 1` is what we
   need (it is: the global min is the min over type cells, by `pl-breakpoint-minimum`).
2. Prove dual-feasibility for the **clean types** (each bin's pieces all share
   the same position parity): then `y_ub = 0` trivially, `y_eq[b(k)] = (−1)^k`,
   objective `= Σ_t (±2^{n−t})`; show this is `≥ 1` by the tower's dyadic
   dominance (the largest bin `2^n` exceeds the sum `2^n−1` of all smaller —
   the SAME dominance used in `tower-top-unsplit` and `even-group-spine-lower-bound`,
   here in dual form).
3. For **interleaved types** (a bin's pieces split across parities — the wall
   regime), characterize when the uniform `y_eq = (1,−1,…,−1)` cert is feasible
   (boundary condition: top-bin holds exactly `(m+1)/2` pieces for odd `m` —
   PROVED algebraically in `cert_feasibility.py` P1d), and when a fallback
   sign-pattern is needed; the fallbacks are still `±1/0` sign-patterns with
   objective `≥ 1`. The open step is a structural lemma that a feasible
   sign-pattern **always exists** for tower-refinement types — inspectable
   directly from the marginal data (the numerics list the few patterns).

### Cheap-kill candidates (structural pruning before heavy LP work)
- The dual objective is always `Σ_t y_eq[t]·2^{n−t}` with `y_eq[t] ∈ {+1,−1,0}`;
  the minimum positive value of such a signed tower sum is `1` (since the
  smallest tower piece is `1` and signs are `±`). So ANY feasible sign-cert with
  nonneg objective gives `≥ 1` for FREE. The only thing to rule out is
  objective `≤ 0` — and the numerics show it never happens. The cheap kill:
  prove feasibility always admits a **nonneg-objective** sign-pattern (then
  `≥ 1` is automatic by integrality of the tower values). This reframes the
  wall as "the dual never goes nonpositive" — a much weaker claim than "D ≥ 1 at
  every breakpoint," and it is exactly the Farkas negation of "a type cell with
  `D < 1` exists."
- Parity/size pigeonhole: the boundary condition `#(top-bin pieces) = (m+1)/2`
  for the uniform cert (P1d, proved) is a pigeonhole-style combinatorial
  condition on the bin assignment — checkable per type without solving any LP.

### Knowledge-base entries to use
- `pl-breakpoint-minimum` (certified) — lands global min at a type-cell vertex.
- `gaps-leftover-identity` (G1, certified) — the primal `D` decomposition; the
  LP-dual is its Farkas dual, so the two framings are COMPLEMENTARY (dual cert
  vs. primal charge), and the LP-dual can IMPORT G1's identity as the primal
  face of its certificate.
- `tower-top-unsplit`, `even-group-spine-lower-bound` (certified) — the
  dominance-margin `2^n > 2^n−1` in dual/sign-pattern form.
- (If `knowledge_base.md` has an entry for LP duality / Farkas / separating
  hyperplane / minimax LP — consult it; the crux corpus query below checks for
  `games-and-strategy` + `linear-algebra-method` cruxes.)

### Analogous past problems (cruxes)
- Filter `combinatorics` / `games-and-strategy` and `linear-algebra-method`
  subtopics; the candidate analogue is any stick-cutting / cake-division game
  solved by a minimax-duality / LP-dual certificate (the dual variables =
  "shadow prices" on the pieces). I did not retrieve a specific `problem_id`
  this round (no grep run on the corpus — recommend the outliner query
  `past_crux_moves_database.json` for `subtopic="games-and-strategy"` +
  `technique_tags` containing "duality"/"LP"/"minimax"). Report "none
  confirmed" — do not force a wrong match; the LP-dual framing is
  problem-specific enough that a forced analogue would mislead.

### Prior progress (the wall, precisely)
Three framings converge on: **odd-count non-dyadic leftover / deficit-covering
`Σ gaps + leftover ≥ 1` when `p_m < 1`**. Even-group strong breakpoints CLOSED
(2 independent proofs). 2-split top-fragment CLOSED. Single-split + dyadic
CLOSED. The wall is the odd-count case, where a leftover's sign is GLOBAL
position-parity (witnesses `{4.75,4,0.25}` `D=1` both `+`; `{4,7/3,2}` `D=11/3`
leftover `−`). Odd-group minimizers EXIST at `D=1`, so the bound is tight to 1.

### Dead ends (do not retry)
- `majorization`/Schur-convexity (round 3, decisive counterexample `(1)` most-majorizing
  `D*=0`) — dead for upper bound; irrelevant to lower.
- Naive "balance a later split weakly decreases `D`" — FALSE (V-shape, round 2).
- `gaps-leftover` greedy per-pair charging — stalls on the interleaving
  obstruction (G3); the LP-dual is the GLOBAL version of this, NOT a retry.
- Single uniform cert `y_eq=(1,−1,…,−1)` — only 0–3% of odd types admit it
  (boundary condition `#top-bin = (m+1)/2` fails for most); a FAMILY of
  sign-patterns is needed. Do not promise a single separating hyperplane.

### Small-case / intuition notes (CONJECTURE, not proof)
- **LP primal min over every type cell is `≥ 1`** (verified n=2,3,4, 0 violations
  over 1000+ sampled types incl. all odd-`m` wall types). Strong duality ⇒ a
  dual sign-cert with objective `≥ 1` exists for every tower-refinement type.
  This is the conjecture the 4th framing would prove.
- The dual objective is always a **signed tower sum** `Σ_t ε_t·2^{n−t}`,
  `ε_t ∈ {+1,−1,0}`; its minimum positive value is `1`. So the wall reduces to
  "the dual is never forced nonpositive" — a cleaner, weaker target than the
  direct "D ≥ 1 at every breakpoint."
- The dominance margin `1 = 2^n − D_{n−1}` (G4) is the **objective-1
  certificate** `y_eq=(1,−1,…,−1)`; it is dual-feasible exactly when the
  top-bin holds `(m+1)/2` pieces (odd `m`). When it is NOT feasible, the
  fallback certs have LARGER objective (3, 5, 7, …) — the wall types (objective
  exactly 1) are the binding minority. This matches the primal picture (odd-group
  minimizers at `D=1` are the tight minority).
- **Caveat (honest):** the round-3 alt-framing dismissed "F4 LP saddle" as
  circular for the lower bound. That dismissal was about the **claim-game dual**
  (weights `w` on pieces, which IS circular: "every feasible `w` gives
  `Σw_i p_i ≥ v_n`" = "odd-index ≥ v_n"). The LP-dual here is DIFFERENT — it is
  the dual of **Xiang's refinement-min LP** (weights on bin-sum + sort
  constraints), certifying a lower bound on Xiang's min from the CONSTRAINT
  STRUCTURE, not by re-deriving the odd-index sum. The round-3 dismissal does NOT
  apply; verify this non-circularity by noting the dual objective
  `2^n − (2^n − 1) = 1` uses only tower bin VALUES, never the sorted positions.

### Bottom line
The LP/Farkas-duality framing is the most promising 4th framing. It is
genuinely orthogonal in MACHINERY (global LP feasibility / separating
hyperplane, vs. direct `D`-bounding / greedy charging), it BYPASSES the
leftover's global sign (the exact primal obstruction the three framings share),
and its certificate is always a signed tower sum `≥ 1` (with the dominance
margin `1` as the tight case). The honest risk: a single uniform certificate
does NOT exist (only 0–3% of odd types admit it); a FAMILY of sign-patterns is
required, and a structural "feasible sign-pattern always exists" lemma is the
real theorem to prove — but that lemma is a linear-algebra feasibility
question, not sign-bookkeeping, so it is a different wall than the one currently
stuck. Recommend the outliner open ONE new lower-bound slug on this framing
(LP-dual), keeping `gaps-leftover` (its primal face) and `tail-count`/`tower-induction`
as the direct-bound rivals.
