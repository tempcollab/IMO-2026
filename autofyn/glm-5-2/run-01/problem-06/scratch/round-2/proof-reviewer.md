# proof-reviewer — round 2, imo-2026-06 (IMO 2026 P6)

Problem: `a_1>1`; `a_{n+1}` = smallest integer `> a_n` with `gcd(a_{n+1},a_i)>1` for EVERY `i≤n`. Prove ∃ `T,L>0` with `a_{n+T}=a_n+L` for all `n≥1`. (`task: proof_only`, `answer_type: none`.)

I independently re-derived the load-bearing steps in Python/sympy. Verifications run:
- `a_1=15` greedy sequence (40 terms) computed; `M'_∞={{2,3},{2,5},{3,5}}`, kernel product `L=30`, period `T=8`, **small-prime greedy == true greedy exactly** (B1' holds empirically).
- Conjecture (C) `A_n∩(a_n,a_n+R]⊆B_n`: **0 violations** over 19 windows for `a_1=15` (each window length 1–5, 0 shortcuts).
- Window structure: `b_n-a_n-1 ∈ {1,…,5}` for `a_1=15`, consistent with the value-window (Cov) sparsity refutation (short windows rarely contain a `σ*`-term).
- Seed-automaticity argument re-derived by hand (see conditional-spine audit below).
- Kernel product vs over-count: confirmed `L=30=∏∪M'_∞`, NOT `30030=∏∪F'_∞` for `a_1=15`.
- `v_p` threshold ballpark: Σ`1/q` over primes `17..p_600` ≈ 1.14, product has ~1500–2000 digits — consistent with `n_0∼10^{2000}`.

---

## Conditional-spine audit (the round's main value) — B1' ⟹ periodicity from `N`

This is the central cross-verification the dispatch asked for. **The conditional spine is CERTIFIED CORRECT.** Granting B1' (`a_{n+1}=min(B_n∩(a_n,∞))` for all `n`, window form), the rest goes through with NO remaining gap except B2:

1. **Stabilization (Lemma 6/5/3 across slugs).** `F'_n⊆2^{P_R}` monotone, `P_R` finite ⟹ stabilizes at `N` (pigeonhole). `M'_n=:M'_∞` fixed; `B_n=:B` fixed; `B` is `L`-periodic, `L=∏_{p∈∪M'_∞}p` (kernel product, verified). ✓
2. **Seed `a_N∈B` is automatic (Lemma 7/small-prime-window Lemma 7).** B1' at step `N-1` gives `a_N=min(B_{N-1}∩(a_{N-1},∞))∈B_{N-1}`, so `σ(a_N)⊇h` for some `h∈M'_{N-1}` hitting `F'_{N-1}`. Trivially `σ(a_N)` hits `σ_N=σ(a_N)` (a_N carries a small prime by universal-small-prime). Hence `σ(a_N)` hits `F'_N`, so `a_N∈B_N=B`. No circularity (B1' is assumed for all n, including `N-1`). ✓ This **dissolves the old B1(b) seed sub-gap for free**, confirming the round-1 reviewer's seed concern is resolved under B1'.
3. **Theorem 1 (certified) applies**: greedy `= f_B` on fixed `L`-periodic `B` from index `N`, `a_N∈B` ⟹ `a_{n+T}=a_n+L` for `n≥N`. ✓

So **B1' ⟹ periodicity from `N`** is rigorous. The only remaining gap given B1' is **B2** (extend to `n≥1`). The spine's scope is correctly stated by all three partial slugs. **This is the round's main value and it is confirmed.**

**One rigor flag (non-fatal).** Both `small-prime-window-lemma` (§3) and `hitting-set-monovariant` (§3) claim B1' (window form) is **equivalent** to `M_n=M'_n` (no large prime in any minimal hitting set of full supports). This is **overstated**: `M_n=M'_n ⟹ A_n=B_n ⟹ B1'` (window) holds, but the converse does not — a large prime `q` in some `g∈M_n` shows `A_n⊋B_n`, but the extra `A_n\B_n` elements need not lie in the window `(a_n,b_n)⊆(a_n,a_n+R]`, so B1' (window) can in principle hold while `M_n≠M'_n`. The correct relation is **`M_n=M'_n` is a sufficient (stronger) condition for B1'**, not equivalent. This does not break the conditional spine (which assumes the weaker window B1'), but the "equivalence" phrasing should be downgraded to "sufficiency" next round. Flagged; does not change any verdict.

---

## Coupling diagnosis — verified

- **spacing (`small-prime-window-lemma`) and `v_p` (`bounded-diff-finite-state`) ARE coupled.** Both are density/covering arguments that bottom out at "demand `~n` (the `σ*`-class size) vs capacity `~a_n ~ (L/T)·n` (sieve period / candidate size), with `L≥2`." Both builders **honestly admit** this coupling (bounded-diff: "the `v_p` mechanism is NOT independent of the spacing route's wall"; small-prime-window: "three slugs share this heart, if (Cov) is genuinely unprovable by spacing, all three die together"). The outline-reviewer's coupling directive is upheld. ✓
- **`hitting-set-monovariant`'s transversal-duality is GENUINELY INDEPENDENT in mechanism.** It is a combinatorial reformulation (minimal transversal of a hypergraph), not a density/covering argument. A spacing/density refutation would NOT kill it. The builder correctly shows the one-prime swap fails, Hall/König does not apply to hypergraph transversals (only to bipartite vertex covers), and a counterexample scan (1515/5000 small-prime-bearing hypergraphs have a large-only minimal hitting set) confirms universal-small-prime is necessary but not sufficient for B1'. So the transversal framing is independent in mechanism but does NOT close the gap — bare hypergraph transversal theory cannot prove B1'; a greedy-specific ingredient is needed. The independence claim is **correct**; the non-closing is honest. ✓

---

## Conjecture (C) check — confirmed cleanest next-round target

`(C)`: `A_n∩(a_n,a_n+R]⊆B_n` for every `n` — every admissible window integer is small-prime-admissible. Re-run on `a_1=15` (19 windows): **0 violations**, consistent with the builder's 0/480+ claim. (C) is **strictly stronger than B1'**: B1' only requires the minima to coincide (no `A\B` element in `(a_n,b_n)⊆(a_n,a_n+R]`); (C) excludes `A\B` elements from the whole window. (C) ⟹ B1' trivially. If (C) is provable, B1' collapses (and the seed argument gives B2's mechanism via the same small-lattice). The `v_p` framework (Lemma 5 σ-periodicity + Lemma 6 union-bound) is the closest attempt; the sieve-error obstruction (`~a_n` outpaces `~n·δ` since `δ<1<L`) is precisely why it falls short. **(C) is the cleanest next-round target.** Flag it for the outliner.

---

## Approach 1: `small-prime-window-lemma` — verdict: CHANGES REQUESTED (Status: partial)

**Correctness.** Every proved layer is valid:
- Lemma 1 (`B_n⊆A_n`, `a_{n+1}≤b_n`): definitional, correct.
- Lemma 2 (`b_n≤a_n+R`, the next multiple of `R` is small-prime-admissible via `primes(a_1)⊆σ(M)` and universal-small-prime): correct, verified.
- Lemma 3 (spacing: `q>R` divides ≤1 integer of `W_n`): trivially correct (two multiples of `q` differ by ≥`q`>`R`).
- Lemma 4 + Cor 5 (value bound / unkillable window): `m≡a_j≡0 mod q`, `m>a_n≥a_j` ⟹ `m-a_j≥q` ⟹ `a_j≤m-q≤a_n+R-q`; hence `σ*`-terms in `(a_n+R-q_min,a_n]` escape. Algebra re-derived and correct. Necessary-condition only (honestly labeled).
- Lemma 6 (stabilization over `P_R`, `B` fixed, `L`=kernel product): correct, verified `L=30` for `a_1=15`.
- Lemma 7 (seed automatic under B1'): correct (see spine audit).
- Theorem 8 (periodicity from `N_0` conditional on B1'): correct (imports Theorem 1).

**Honest gaps.** [GAP B1' (Cov) — covering sufficiency] is the heart, unproved. The clean value-window version is **empirically refuted** (9927 violations at `a_1=15`; window structure verified short, length 1–5, so sparsity of `σ*`-terms in the value window is expected). [GAP B2] separate, open. No overclaim: Status `partial` correct; the refutation is recorded, not papered over. The coupling to the other spacing/v_p routes is honestly admitted.

**Scores.** Correctness 8/10; Completeness 5/10 (B1' sufficiency + B2 open; clean value-window refuted); Progress 8/10 (clean reduction to single claim B1', necessary-condition lemma, conditional spine + seed dissolution — round's cleanest formulation).

---

## Approach 2: `hitting-set-monovariant` — verdict: CHANGES REQUESTED (Status: partial)

**Correctness.** Every proved layer is valid:
- Lemma 1 (admissible-set identity via minimal hitting sets): correct identity (well-founded reduction to minimal hitting sets).
- Lemma 4 (one-sided inclusion `M'_n⊆M_n`): correct (`h` small-only ⟹ `supp(a_i)∩h=σ_i∩h`).
- **Lemma 6 (cross-intersecting closure)** — the distinctive promotable result: if `M_n` pairwise cross-intersecting and new row's support is a hitting set of `F_n`, then `M_{n+1}=M_n`. Proof re-derived: old sets persist (`h'∩S_{n+1}⊇h'∩h_0≠∅`); no new minimal (`g∈M_{n+1}⊇h_g∈M_n`, `h_g` hits new row via `h_g∩h_0`, minimality forces `g=h_g`). Correct. Stress-tested 0/1581. Unconditional (no B1'). Genuinely reusable.
- Lemma 5 (stabilization, conditional on B1'), Lemma 7 (seed, conditional), Theorem (periodicity from `N`): correct (shared spine).
- The **false round-1 monovariant** `(|M_n|,Σ|h|,#disjoint-pairs)` is correctly **dropped** (verified non-monotone: `a_1=385`, `|M|` rises 3→9). Good — no dead weight carried.

**Honest gap.** [GAP B1'] — the transversal-minimality / matching-duality descent breaks at the one-prime swap (`g\{q}∪{p_j}` need not hit other `q`-essential rows); Hall/König does not apply to hypergraph transversals; the counterexample scan (1515/5000) confirms universal-small-prime is necessary but not sufficient. The builder honestly frames B1' as an EQUIVALENT REFORMULATION of the round-1 wall, not a bypass (matches the explorer's admission). The "equivalence" phrasing is slightly overclaimed (it's sufficiency, see spine audit), but this is non-fatal.

**Independence.** The transversal-duality mechanism is genuinely independent of spacing/density (a density refutation wouldn't kill it), but it does NOT close B1' — the gap persists. Honest.

**Scores.** Correctness 8/10; Completeness 5/10 (B1'+B2 open; descent break located); Progress 7/10 (clean combinatorial reformulation, cross-intersecting closure lemma, false monovariant dropped).

---

## Approach 3: `bounded-diff-finite-state` — verdict: CHANGES REQUESTED (Status: partial)

**Correctness.** Every proved layer is valid:
- Lemmas 1–4 (bounded-diff, universal-small-prime, `M'_n` stabilization with kernel-product correction, small-prime greedy bounded): correct, verified (`L=30` for `a_1=15`, not `30030`).
- **Lemma 5 (σ-periodicity, conditional on B1')**: `σ_i` periodic with `T'=lcm(T,{p≤R:p∤L})`; `σ*`-class = union of APs with common difference `L'=(T'/T)·L`; `gcd(L',q)=1` for `q>R` (all prime factors of `L'` are ≤`R`). Re-derived: for `p|L`, `p`-divisibility is `T`-periodic; for `p∤L`, residue advances by `L mod p` (a generator), cycling in `p` blocks of `T`. Correct.
- **Lemma 6 (`v_p` union-bound — PARTIAL)**: induction; covered `σ*`-terms ≤ `|J*|·Σ1/q + O(c*·|Q|)`; coverage requires `1≤Σ1/q+o(1)`; contrapositive gives B1' at step `n+1` when `Σ1/q<1`. Threshold `n_0(a_1)` via `Φ_R(M)~log log log M`; `n_0(15)~10^{2000}` — ballpark verified (~600 primes, product ~10^{1500–2000}). A genuine PARTIAL result.

**Honest gaps.** [GAP B1' beyond `n_0`] — the refined density/sieve argument fails: uncovered `σ*`-terms have positive density `δ>0` but their first occurrence has index up to `(∏q)·T'≤(a_n+R)·T'∼n·L' >n` (since `L'≥L≥2`), i.e. a FUTURE term, not a past term. The sieve error `O(∏q)~a_n` outpaces the signal `~n·δ` because `δ<1<L`. Precisely located, structurally honest. [GAP B2] separate.

**Minor rigor flag (non-fatal).** Lemma 6's induction step only handles `n≥N` (stabilization index); the pre-stabilization steps `1<n<N` are described as "plus the bounded pre-stabilization regime" — a finite-per-`a_1` check that is not rigorously uniform in `a_1`. This is a small gap in the lemma's claimed scope (`B1' for all n≤n_0`), but since Lemma 6 is already PARTIAL and the pre-stabilization regime is finite, it does not change the verdict. Flag for the builder to close next round (verify B1' for `n<N` uniformly, or restrict the lemma's scope to `N≤n≤n_0`).

**Coupling.** The builder **honestly admits** the `v_p` mechanism is NOT independent of the spacing route's wall (both bottom out at "demand ~n vs capacity ~a_n"). The outline-reviewer's coupling directive is upheld.

**Empirical conjecture (C).** Recorded as the stronger-than-B1' clean formulation; 0 violations verified for `a_1=15`. Correctly flagged as the next-round target.

**Scores.** Correctness 7/10 (Lemma 6 pre-stabilization scope loose); Completeness 5/10 (B1' beyond `n_0` + B2 open); Progress 8/10 (σ-periodicity + `v_p` partial result + conjecture (C) — the round's most developed attack on B1').

---

## Approach 4: `frozen-invariant-reduce-mod-lcm` — verdict: RETHINK (Status: unsolved)

**Correctness.** The route was a HIGH-RISK PROBE (the field's only non-`M'_n`-stabilization attack on B1'). The retire-fast protocol was correctly triggered:
- **Test A (monovariant `w_n=min{m>a_n:m∉B_n}`)**: empirically refuted — `w_n` is NON-DECREASING in all 8 tested `a_1` (the OPPOSITE of the non-increasing direction the aimo-0678 lever requires); the gap `u_n=w_n-a_n` is bounded but OSCILLATES (`{1,2,1,1,…}`). The lever's purpose (non-increasing while `a_n` climbs ⟹ `a_n` bounded) is inert.
- **Test B (finite-state determinism)**: `(a_n mod 30)→(a_{n+1} mod 30)` is a deterministic 8-cycle, BUT this is Theorem 1 re-derived on the *already-stabilized* small lattice — conditional on B1', not a bypass. Off the periodic regime the transition is history-dependent (≥20 continuations).
- **Why the aimo-0678 shape does not transfer**: the non-increasing proof there uses BOTH a frozen invariant `s_n=a_n+b_n` (conserved) AND an explicit gcd/lcm recurrence `s_{n+1}=gcd+lcm`. Neither exists in our single-sequence greedy (no coupled sequence, no conserved quantity, no algebraic formula for the next state). The diagnosis is sound.

**Status.** `unsolved` is correct — no correct progress specific to this approach; the certified results it re-confirmed are owned by other routes. The distinctive contribution is the NEGATIVE result (do not retry the monovariant shape). Route retired. The builder honestly recommends cutting it from the live population.

**Scores.** Correctness 6/10 (negative result is sound); Completeness 2/10 (route exhausted); Progress 3/10 (negative diagnostic only, but valuable for not retrying).

---

## Certified lemmas (this round)

Promotable-lemma certification (full bar: sorry-free, statement correct, no stronger than proved):

- **Cross-intersecting closure lemma** (hitting-set-monovariant, Lemma 6) — **CERTIFY**. Correct, unconditional, stress-tested 0/1581, reusable by any hitting-set approach. Distinctive promotable result of the round. → `results/imo-2026-06/lemmas/cross-intersecting-closure.md`.
- **Spacing fact** (small-prime-window, Lemma 3) — **CERTIFY**. Trivially correct (`q>R` divides ≤1 integer of a length-`R` window), reusable. → `results/imo-2026-06/lemmas/spacing-fact.md`.
- **Value-bound / unkillable-window lemma** (small-prime-window, Lemma 4+Cor 5) — **CERTIFY**. Necessary condition, algebra verified, correctly labeled necessary-only. → `results/imo-2026-06/lemmas/value-bound-unkillable-window.md`.
- **Small-prime-minimum-in-window** (small-prime-window, Lemma 2) — **CERTIFY (marginal)**. Correct (`b_n≤a_n+R` via the bounded-diff witness repurposed); overlaps with `bounded-difference.md` but states a distinct fact about `b_n`. → `results/imo-2026-06/lemmas/small-prime-minimum-in-window.md`.
- **σ-periodicity lemma** (bounded-diff, Lemma 5) — **CERTIFY (conditional on B1')**. Correct, the structural input for any density argument on B1'. Scope clearly conditional. → `results/imo-2026-06/lemmas/sigma-periodicity.md`.
- **`v_p` union-bound lemma** (bounded-diff, Lemma 6, PARTIAL) — **CERTIFY (PARTIAL scope)**. Statement correct; proof rigorous for `N≤n≤n_0(a_1)`. **Flag the pre-stabilization scope gap** (`1<n<N` not uniformly covered) in the lemma file. Practically weak (astronomical `n_0`, doesn't close the gap) but correctly stated. → `results/imo-2026-06/lemmas/vp-union-bound.md`.
- **Small-prime one-sided inclusion** (hitting-set, Lemma 4) — **CERTIFY (marginal)**. Correct (`M'_n⊆M_n`), small but reusable. → `results/imo-2026-06/lemmas/small-prime-inclusion.md`.
- frozen-invariant: **none** (negative diagnostic only, correctly not proposed).

---

## Final consolidated line

**The conditional spine (B1' ⟹ periodicity from `N`) is CERTIFIED.** Granting B1' (the single window-admissibility crux: `a_{n+1}=min(B_n∩(a_n,∞))` for all `n`), the seed `a_N∈B` is automatic, stabilization is free (pigeonhole over `P_R`), and Theorem 1 gives `a_{n+T}=a_n+L` for `n≥N` with `L`=kernel product. The ONLY remaining gap given B1' is B2 (from-`n=1`, empirically universal, unproved). Three mechanisms (spacing/v_p/covering) are coupled and the clean value-window version is empirically refuted; the transversal-duality mechanism is genuinely independent in mechanism but does not close the gap; the frozen-invariant monovariant route is retired (refuted). **Conjecture (C)** (`A_n∩(a_n,a_n+R]⊆B_n`, 0 violations) is the cleanest next-round target — strictly stronger than B1', its proof would collapse B1' (and via the seed mechanism, B2). No approach is solved; all four verdicts are non-APPROVE.

---

## Verdicts

1. `small-prime-window-lemma` — **CHANGES REQUESTED** (Status: partial). Clean reduction to B1', necessary-condition lemma, conditional spine certified; (Cov) sufficiency open, value-window refuted.
2. `hitting-set-monovariant` — **CHANGES REQUESTED** (Status: partial). Cross-intersecting closure lemma, clean combinatorial reformulation; transversal-duality descent breaks at one-prime swap, B1' open.
3. `bounded-diff-finite-state` — **CHANGES REQUESTED** (Status: partial). σ-periodicity + `v_p` partial result (B1' up to `n_0`) + conjecture (C); B1' beyond `n_0` open (sieve-error obstruction), coupled to spacing wall; Lemma 6 pre-stabilization scope gap flagged.
4. `frozen-invariant-reduce-mod-lcm` — **RETHINK** (Status: unsolved). Monovariant `w_n` refuted (non-decreasing, oscillating); aimo-0678 shape does not transfer; route retired.
