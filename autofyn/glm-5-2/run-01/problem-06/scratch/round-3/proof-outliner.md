## imo-2026-06

State recap (cite, do NOT re-prove): conditional spine (B1' ⟹ `a_{n+T}=a_n+L` for `n≥N`) is CERTIFIED. Single crux B1'. Spacing/v_p/covering cluster EXHAUSTED (coupled, clean value-window refuted at `a_1=15`). Transversal-duality independent but unclosing. NEW lever (all 3 explorers): cross-intersecting `M'_∞` + R-smooth-anchor + clean reduction (W)⟹(C)⟹B1'; B2 seed now a theorem given B1'. Field below: 3 NEW + 1 COPY, plus 1 RETIRE; the 3 spacing/v_p slugs LEFT as certified spine (no re-advance — mechanism exhausted).

---

**cross-intersecting-anchor**: NEW
Target: the whole theorem (B1' via cross-intersecting `M'_∞` + R-smooth anchor; certified spine; B2 deferred to `b2-induction-step`).
Technique: strong induction on `n` (anchor) + cross-intersecting closure lemma (CERTIFIED) for the early freeze + pigeonhole (stabilization).
Skeleton:
  1. One-sided inclusion `B_n⊆A_n`, `a_{n+1}≤b_n≤a_n+R` (CERTIFIED imports).
  2. Freeze-early: cross-intersecting closure lemma (CERTIFIED) — if `M'_n` cross-intersecting and new `σ` hits `F'_n`, `M'_{n+1}=M'_n`.
  3. Anchor induction (B1'): admissible `m∈A_n∩(a_n,a_n+R]` ⟹ hits every R-smooth `a_j` via a SMALL prime (`a_j` has no large prime) ⟹ `σ(m)⊇h∈M'_smooth,n` ⟹ (cross-intersecting) `h` hits every `σ_i` ⟹ `m∈B_n`. So `A_n∩(a_n,a_n+R]⊆B_n` (conjecture C) ⟹ `a_{n+1}=b_n`.
  4. Certified spine: B1' ⟹ periodicity from `N` (cite).
  5. B2 deferred to `b2-induction-step`.
Key lemmas (claim + mechanism):
  - **(A) `M'_smooth,n = M'_n` past a bounded phase** (= conjecture W: every `σ*∈F'_n` has an R-smooth term) — because every `h∈M'_n` is itself R-smooth and admissible; mechanism open. SHARED with `w-descent-rsmooth` (flagged coupling).
  - **(B) `M'_∞` pairwise cross-intersecting** — empirically 12/12 `a_1` incl 4-prime cases; mechanism open (greedy-specific, NOT bare transversal theory — universal-small-prime is necessary-not-sufficient, 1515/5000 counterexamples recorded). THE distinctive crux.
  - Anchor close (3-line chain) is the cheap kill ONCE (A)+(B) hold.
Open gaps: [GAP A] (= W, shared), [GAP B] (THE crux), [GAP C] pre-anchor finite casework (spacing+arithmetic), [GAP D] B2 (deferred).
Cases: trivial (imported); R-large regime (≥77: purely R-smooth, (W) trivial — record sub-theorem); R-small hard regime (15,45,135: real test).
Watch out for: (B) NOT implied by universal-small-prime (do not claim); closure lemma freezes `M'` but does NOT prove cross-intersection (B is INPUT, not consequence); "every `h` hits `σ(a_1)`" ≠ cross-intersection.

---

**w-descent-rsmooth**: NEW
Target: the whole theorem via the clean reduction (W)⟹(C)⟹B1' + certified spine + B2 deferred.
Technique: minimal-counterexample descent on the support (aimo-0030 analog: strip large primes → R-smooth `s` with same `σ`) + late-arrival induction.
Skeleton:
  1. Clean reduction (W)⟹(C)⟹B1' (short rigorous proof): R-smooth `a_j` has no large prime ⟹ any `m∈A_n` sharing a factor shares a SMALL prime ⟹ `p∈σ(m)∩σ*` (contradiction if `σ(m)` missed `σ*`).
  2. Base case of (W): `σ*=σ(a_1)` — `a_1` itself is R-smooth (the "uncompensatable `σ(a_1)`-class" cheap kill, 70–80% of cases).
  3. s-substitution descent: for a `σ*`-term `a_j` with large prime `q>R`, set `s`=R-smooth part; `σ(s)=σ*`; `s` admissible for prior terms (VERIFIED 20/20, 12/12) — [GAP E: prove admissibility in general].
  4. Size gap + late-arrival: empirically `s≤a_{j-1}` ALWAYS (direct aimo-0030 window-landing is FALSE, 0/33). So `s` was a skipped admissible; iterate — skipping an R-smooth `s` of class `σ*` forces a strictly smaller admissible, producing a `σ*`-class all-small term within bounded delay (else infinite descent). [GAP F: the late-arrival mechanism — `a_1=135` shows delay 2].
  5. (W) proved (mod E,F) ⟹ step 1 gives B1'.
  6. Certified spine (cite). 7. B2 deferred.
Key lemmas:
  - **(W⟹C⟹B1')** — R-smooth `a_j` ⟹ shared prime is small ⟹ lands in `σ(m)∩σ*`.
  - **(s-substitution admissibility)** — `σ(s)=σ*` and (conjecturally) `σ*` hits `F'_{j-1}`; gap = rare subcase where `a_j` hits a past term only via a large prime.
  - **(Late-arrival)** — well-ordering of the greedy: a skipped R-smooth admissible forces a smaller admissible, bounded delay to a `σ*`-all-small term.
Open gaps: [GAP E] s-admissibility; [GAP F] late-arrival (THE crux); [GAP G] B2.
Cases: trivial; R-large (trivial (W)); R-small hard regime.
Watch out for: do NOT claim `s>a_{j-1}` (empirically false); "first term of each `σ*`-class is R-smooth" is FALSE (`a_1=135` class `{2,3}` first `138`); GAP A (=`M'_smooth=M'`) shared with `cross-intersecting-anchor` — two mechanisms on one sub-gap, acceptable.

---

**b2-induction-step**: NEW (B2-dedicated)
Target: B2 (the empty pre-period) given B1'; completes the whole theorem with a B1'-closing sibling.
Technique: seed theorem (cite) + single induction step via cross-intersecting early-freeze (path α) and/or "future-shared primes are small" (path β); `2∈S` resolves `n=1` for odd `a_1`.
Skeleton:
  1. Seed theorem `a_1∈B` (given B1'): universal-small-prime ⟹ `primes(a_1)` hits `F'_∞` ⟹ ⊇`h∈M'_∞` ⟹ `m_h|a_1`. Certify as `lemmas/a1-on-cycle.md`.
  2. `B⊆B_n` always ⟹ `min(B_n∩(a_n,∞))≤cyc_succ_B(a_n)`; failure = "prematurely valid SMALL-prime candidate" `m∈(a_n,cyc_succ_B(a_n))∩(B_n\B)`. [GAP H]
  3. Path α: cross-intersecting `M'_∞` (sibling GAP B) + closure lemma ⟹ `M'_n=M'_∞` early ⟹ `B_n=B` early ⟹ no premature candidate; finite pre-freeze casework. [GAP H-α, depends on sibling]
  4. Path β: `a_{n+1}∈B ⟺` every future `a_j` shares a SMALL prime with `a_{n+1}`; use σ-periodicity (future `σ`'s periodic with `T'`) to bound large-prime-sole-shared-factor cases. [GAP H-β, PROBE v_p-wall re-coupling]
  5. Path γ: `2∈S` for odd `a_1` (2-line proof, `2p`-witness) ⟹ `n=1` first jump resolved.
  6. Seed + induction step ⟹ `a_n∈B`, `a_{n+1}=cyc_succ_B(a_n)` ∀`n≥1` ⟹ Theorem 1 from `x_0=a_1`.
Key lemmas:
  - **Seed** — universal-small-prime makes `primes(a_1)` a hitting set of `F'_∞`, contains `h∈M'_∞`, `m_h|a_1`.
  - **`B⊆B_n`** — `h∈M'_∞` hits `F'_n`, contains `g∈M'_n`, `m_g|m_h`.
  - **`2∈S` for odd `a_1`** — `2p`-witness is even+admissible+`≤a_1+R`, greedy turns even by `a_2`.
Open gaps: [GAP H-α] (path α, depends on sibling GAP B), [GAP H-β] (path β, independent), [B1' dependency flag].
Cases: trivial (`N=1`); odd `a_1` (path γ for `n=1`, α/β for general `n`); even (trivial).
Watch out for: `B_n\B` candidates are SMALL-prime (spacing/v_p refutation does NOT directly transfer — but probe path β); path α NOT independent of `cross-intersecting-anchor` (shares GAP B); B2 may genuinely REQUIRE B1' (do not claim B2-closed-without-B1').

---

**b2-future-shared-primes**: COPY of `b2-induction-step`
Target: same as `b2-induction-step` (B2 given B1').
Distinct framing: pursue ONLY path β (the "future-shared primes are small" direct reformulation via σ-periodicity), as an INDEPENDENT twin — path α is coupled to `cross-intersecting-anchor`'s GAP B, so if GAP B fails path α dies; path β is the independent fallback. Two viable fillings of the same gap (GAP H), both worth pursuing in parallel.
Skeleton: identical to `b2-induction-step` steps 1,2,5,6, but step 3 REMOVED (no path α) and step 4 (path β) promoted to the primary mechanism — the σ-periodicity density argument that no future `a_j` shares only a large prime with `a_{n+1}`.
Key gap: [GAP H-β] — the σ-periodicity/density argument on future shared primes; PROBE whether it re-couples to the v_p wall (the candidates are small-prime here, so the large-prime spacing refutation does NOT directly transfer, but a density bound might).
Watch out for: σ-periodicity is CONDITIONAL on B1' (it is an induction tool); path β may secretly reduce to "no `B_n\B` element in a short value window" — check against the refuted (Cov) but note the candidate set differs.

---

**hitting-set-monovariant**: RETIRE
Reason: its distinctive mechanism (transversal-minimality / Hall-König / one-prime-swap descent) is a recorded dead end (one-prime swap fails; Hall/König inapplicable to hypergraph transversals; universal-small-prime necessary-not-sufficient, 1515/5000 counterexamples). The salvageable content — the cross-intersecting closure lemma + the definitional reduction + the certified conditional spine — is ALREADY certified in `lemmas/` and IMPORTED by the new `cross-intersecting-anchor` slug, which carries the new mechanism on the same route. Retiring avoids a misleading slug name ("monovariant" — the monovariant was dropped in round 2) and lets the ranker track the new mechanism at its own Elo.

---

**small-prime-window-lemma / bounded-diff-finite-state / periodic-set-iteration**: ADVANCE-NOOP (LEFT as certified spine)
Reason: the spacing/v_p/covering cluster is EXHAUSTED (dispatch state rule: re-advance ONLY if the mechanism is genuinely new). Their certified contributions (spacing fact, value-bound, σ-periodicity, v_p union-bound PARTIAL, Theorem 1) remain importable by the new slugs. `periodic-set-iteration` is the Theorem-1 carrier. Do NOT re-advance with the same mechanism; do NOT retire (they hold certified partial results). The new cross-intersecting / (W)-descent mechanisms route through FRESH slugs, not grafts onto these.

---

## Diversity / single-gap-trap check
- `cross-intersecting-anchor` crux = (B) `M'_∞` cross-intersecting (structural property of the stabilized kernel).
- `w-descent-rsmooth` crux = (F) late-arrival induction (per-term support descent).
- `b2-induction-step` / `b2-future-shared-primes` crux = (H) the B2 induction step (SMALL-prime premature candidates, different candidate set from B1).
These are THREE distinct mechanisms (stabilized-family structure / per-term descent / pre-period induction) on TWO distinct gaps (B1', B2). The shared sub-gap (A)=(W) is approached from two sides (anchor route vs descent route) — two mechanisms, not a single-gap trap. Path α of B2 shares (B) with the anchor slug — flagged; path β (the COPY twin) is the independent fallback.

## Recommended build set
build set: cross-intersecting-anchor, w-descent-rsmooth, b2-induction-step, b2-future-shared-primes
