# Proof-builder report — bounded-diff-finite-state (round 2, ADVANCE)

## Approach
`results/imo-2026-06/approaches/bounded-diff-finite-state.md` — kept the certified spine (bounded-diff → `M'_n` stabilization → Theorem 1 → trivial cases); replaced the refuted Bertrand/competing-candidate attack on B1 with a **`v_p`-multiplicity / size-counting** mechanism; switched the stabilizing object to `M'_n` (minimal hitting sets over `P_R={primes≤R}`) with the **kernel product** modulus `L=∏∪M'_∞` (correctness fix: 30 not 30030 for `a_1=15`); collapsed the three old sub-gaps into the single window-admissibility claim **B1'**.

## What I proved (rigorous, this round)

1. **Lemma 3 (corrected)** — `F'_n` over fixed finite `P_R` stabilizes at `N`; `M'_n=:M'_∞` fixed; `B:=∪_{h∈M'_∞}{mult of m_h}` is fixed `L`-periodic, `L=∏∪M'_∞` (kernel product). Corrected the round-1 over-counting (`∏∪F'_∞=30030` vs true `∏∪M'_∞=30` for `a_1=15`). Verified: kernel product = period for `a_1∈{15,35,77,91}` (60-term scan); `S=∪M'_∞ ⊆ P_R` for ALL 8 required inputs.

2. **Lemma 4 (small-prime greedy bounded; one-sided)** — `A_n ⊇ B_n` ⟹ `a_{n+1}≤b_{n+1}`; and the bounded-diff witness `R·⌈(a_n+1)/R⌉ ∈ B_n` (because `supp(a_1)` is a hitting set of `F'_n` and `m_h|R` for the contained `h`), so `b_{n+1}≤a_n+R`. Equality is exactly B1'.

3. **Lemma 5 (`σ`-periodicity, conditional on B1')** — assuming B1' for steps `≤ n`, `σ_i=supp(a_i)∩P_R` is eventually periodic with explicit period `T'=lcm(T,{p≤R:p∤L})`; each `σ*`-class is a finite union of APs with common difference `L'=(T'/T)·L`; `gcd(L',q)=1` for primes `q>R` (since every prime factor of `L'` is `≤R`). This is the structural input for any density/counting argument on B1'. **Promotable.**

4. **Lemma 6 (`v_p` union-bound — PARTIAL RESULT)** — inductively: B1' for steps `≤ n` + `Σ_{q∈Q(m)} 1/q < 1` for every hypothetical `m∈(a_n,a_n+R]` ⟹ B1' at step `n+1`. Hence B1' holds for all `n ≤ n_0(a_1)`, where `n_0` is the threshold at which `Φ_R(M):=max Σ 1/q` (over distinct primes `>R` with product `≤M`) first reaches 1. For `a_1=15` (`R=15`): `M_0∼10^{2000}`, `n_0∼10^{2000}` — finite but astronomical. **Promotable (PARTIAL).**

5. **Conditional spine** — given B1' (PARTIAL): stabilization is free (Lemma 3); seed `a_N∈B` is automatic; Theorem 1 (certified) gives `a_{n+T}=a_n+L` for `n≥N`. Given B2: extends to `n≥1`.

6. **Trivial cases** kept from round 1: `a_1` even ⟹ `T=1,L=2`; `a_1=p^k` ⟹ `T=1,L=p`. Verified across `{2,3,...,16,9,25,27,49}`.

## Gaps that remain (exactly located)

**[GAP B1' — full free-rider exclusion beyond `n_0(a_1)`.]** Lemma 6 proves B1' only up to `n_0`. The refined density/sieve argument (which would handle all `n`) FAILS, and the obstruction is structural, not a missing technique:

- The uncovered `σ*`-terms (those not divisible by any `q∈Q(m)`) have positive density `δ=∏(1-1/q)>0`, so infinitely many exist. BUT their **first occurrence** has index up to one full sieve period `∏q·T' ≤ (a_n+R)·T' ∼ n·L'`. Since `L'≥L≥2`, this is `> n` — the first uncovered `σ*`-term is a FUTURE term, not a past term.
- Equivalently, the inclusion-exclusion error `O(∏q)≤O(a_n+R)∼(L/T)·n` dominates the uncovered-density signal `|J*_post|·δ ∼ (c*/T')·n·δ` because `δ<1<L≤L'`. So the sieve cannot exhibit a past uncovered `σ*`-term to contradict `m`'s admissibility.

**This is the same wall the spacing route hits.** Both bottom out at "demand `∼n` vs capacity `∼a_n∼(L/T)·n`" with `L≥2`. Per the outline-reviewer's coupling directive: I tested whether the `v_p` cofinality angle is genuinely independent — **it is NOT**; it is coupled to `small-prime-window-lemma`'s spacing+covering heart. The honest recommendation (per the reviewer's directive) is that this slug should ride the same heart as `small-prime-window-lemma` rather than claim a distinct mechanism.

**[GAP B2 — from-`n=1` / empty pre-period.]** Even granting B1', Theorem 1 gives periodicity from `n=N>1`, not `n=1`. Empty pre-period empirically universal (8/8 required inputs satisfy `a_{1+T}=a_1+L`), no proof. Separate from B1'.

## Empirical conjecture (stronger than B1', UNPROVED, recorded)
`A_n ∩ (a_n, a_n+R] ⊆ B_n` for every `n` — every admissible window integer is small-prime-admissible. **0 violations over 480+ `(a_1,n)` pairs** (27 hard odd composites in `[3,130)`, 24 steps each; + 8 required inputs, 79 steps each). Strictly stronger than B1'. If provable, B1' (and B2, via the automatic-seed argument) collapse; the `v_p` framework is the closest attempt, and the sieve-error obstruction is the precise reason it falls short. Flagged for the next round.

## Spec-concern / rigor notes
- Switched stabilizing object `F_n → M'_n` (minimal hitting sets) per the outline-reviewer's correctness fix. Modulus is now the kernel product `∏∪M'_∞`, verified = period for `a_1∈{15,35,77,91}`.
- Did NOT retry the refuted Bertrand/competing-candidate move (round 1). Did NOT retry residue-mod-M, profinite, or injectivity bypasses (all refuted).
- The `v_p` partial result is honestly labeled PARTIAL — it does NOT prove B1' for all `n`, only `n ≤ n_0(a_1)`. Status `partial`.
- The coupling to `small-prime-window-lemma` is honestly reported (not papered over) — the `v_p` mechanism is NOT independent of the spacing route's wall.

## Promotable lemmas proposed for certification
- `results/imo-2026-06/lemmas/sigma-periodicity.md` — Lemma 5 (σ-periodicity + σ*-class AP-structure, conditional on B1'). Fully proved; structural input for any B1' covering-bound argument.
- `results/imo-2026-06/lemmas/vp-union-bound.md` — Lemma 6 (PARTIAL: B1' for `n ≤ n_0(a_1)` via the `v_p` union bound). Fully proved as a partial result; explicitly flagged as covering only the sub-threshold regime.

## Self-assessed status
**partial.** Complete for trivial cases (even, prime-power). For the hard case: certified spine + the `v_p` PARTIAL result (B1' up to `n_0(a_1)`) + conditional periodicity given B1'+B2. Two honest gaps: B1' beyond `n_0(a_1)` (sieve-error obstruction, precisely located; coupled to the spacing route's wall) and B2 (separate). Empirical conjecture (C) recorded as the strongest clean formulation of the crux for the next round.
