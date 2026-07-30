## imo-2026-06 — B2 (from-n=1) lens

### Headline

**The B2 SEED is now a theorem (given B1').** `a_1 ∈ B` (the eventual stabilized small-prime admissible set) follows unconditionally from B1' + the certified universal-small-prime lemma. This dissolves the seed sub-gap for `n=1` (the prior round only certified the seed `a_N ∈ B` at the stabilization index `N`; the stronger `a_1 ∈ B` is new). What remains of B2 is a single **induction step** with a clean combinatorial statement.

### Distinct openings

1. **SEED (a_1 ∈ B) — RIGOROUS, given B1'.** Proof (1-2 lines, verified computationally for 16 `a_1` incl. 15,21,33,35,39,55,77,91,105,135,175,187,221,385): By universal-small-prime (CERTIFIED), every `a_i` is divisible by some prime of `a_1`; all primes of `a_1` are `≤ R = rad(a_1)` (since each prime `p | a_1` satisfies `p ≤ ∏ primes(a_1) = R`), so `primes(a_1) ⊆ P_R` and `primes(a_1) ∩ σ(a_i) ≠ ∅` for every `i`. Hence `primes(a_1)` is a hitting set of `F'_∞ = {distinct σ(a_i) : i ≥ 1}` (the stabilized family — stabilization only collects the distinct `σ`'s, it does not change which sets must be hit). By well-foundedness of minimal hitting sets, `primes(a_1) ⊇ some h ∈ M'_∞`. Since `h ⊆ primes(a_1) = supp(a_1) = σ(a_1)` and `a_1` is divisible by every prime in `supp(a_1)`, `m_h | a_1`, hence `a_1 ∈ B`. ∎ (No B2 assumption, no induction; only B1' to define the stabilized `B` and universal-small-prime.) **Computationally confirmed**: in every tested `a_1`, the `h ⊆ primes(a_1)` in `M'_∞` is exactly `primes(a_1)` when `a_1` is odd-squarefree-rich (e.g. 15→{3,5}, 35→{5,7}, 77→{7,11}, 91→{7,13}, 105→{3,5,7}, 187→{11,17}, 221→{13,17}, 385→{5,7,11}) and a proper subset when the kernel collapses (e.g. 21→{3}, 33→{3}, 39→{3}: `L=3, T=1`, prime-power-like). Either way `m_h | a_1`.

2. **INDUCTION STEP (the real B2 crux, given B1')** — `a_{n+1} = cyc_succ_B(a_n)` for `n < N_stab`, equivalently `min(B_n ∩ (a_n,∞)) ∈ B` (and equals `cyc_succ_B(a_n)`). Reduction: `B ⊆ B_n` always (if `m ∈ B` then `m_h | m` for `h ∈ M'_∞`, and `h` hits `F'_n ⊆ F'_∞`, so `h ⊇ some g ∈ M'_n`, `m_g | m_h | m`, `m ∈ B_n`); hence `min(B_n ∩ (a_n,∞)) ≤ cyc_succ_B(a_n)`, and the only failure mode is a "prematurely valid SMALL-prime candidate" `m ∈ (a_n, cyc_succ_B(a_n)) ∩ (B_n \ B)`. **This is a different candidate set from B1'** (B1' excludes `A_n \ B_n` large-prime shortcuts; B2-given-B1' excludes `B_n \ B` small-prime premature candidates). The large-prime machinery (spacing fact, `v_p` union-bound, value-bound/unkillable-window) is **irrelevant** here — the obstruction is purely the `M'_n` vs `M'_∞` combinatorial structure.

3. **Reformulation of the induction step as "future-shared primes are small."** `a_{n+1} ∈ B ⟺ σ(a_{n+1})` is a hitting set of `F'_∞ ⟺ a_{n+1}` shares a SMALL prime with every future `a_j` (`j > n+1`). By the greedy rule, every future `a_j` shares A prime with `a_{n+1}` (since `n+1 ≤ j-1` is a past term at step `j-1`). So **B2-given-B1' ⟺ "for every `n < j-1`, the shared prime between `a_{n+1}` and `a_j` is small (`≤ R`)."** This is B1'-flavored (it excludes large primes as the SOLE shared prime between two sequence terms) but WEAKER than B1' (B1' excludes large primes from stealing the greedy minimum; B2 only excludes them from being the sole common factor between `a_{n+1}` and any future term). The two may be independently tractable, but they are NOT provably independent — both are "no large-prime shortcut" claims. **Flag: B2 may genuinely require B1' (or a cousin of it); the logical dependency is NOT clean.** A builder should treat "B2 without B1'" as speculative.

4. **The "first jump" `n=1` instance** (cleanest test bed): `a_2 = min{m > a_1 : gcd(m,a_1) > 1}` (only constraint at `n=1` is hitting `a_1`). Empirically `a_2 = cyc_succ_B(a_1)` in EVERY tested case (15→18, 35→40, 77→84, 91→98, 105→108, 135→138, 175→180, 187→198, 221→234, 385→390, also 21→24, 33→36, 39→42, 55→60, 65→70, 69→72, 85→90, 95→100, 115→120, 119→126, 133→140, 143→156, 145→150, 155→160). The gap `(a_1, a_2)` is tiny (length = `a_2 - a_1 ∈ {3,5,7,11,...}`, always a prime of `a_1` or small) and contains NO `B_1`-element. For ODD `a_1` the first `B_1`-candidate above `a_1` lands on an EVEN multiple (e.g. `a_1=105`: first mult of 3 is 108 = mult of 6 ∈ B; first mult of 5 is 110 = mult of 10 ∈ B; first mult of 7 is 112 = mult of 14 ∈ B) — because `2 ∈ S` always (2 is a kernel prime whenever `a_1` is odd, since the greedy turns even at `a_2`), and `m_{\{2,p\}} | 2p` divides the even multiple of `p`. **Conjectured mechanism for the first jump (odd `a_1`): `2 ∈ S` forces the first `p`-multiple above the odd `a_1` to be even, hence in `B`.** This is a concrete, attackable sub-claim — but it only covers `n=1` and only odd `a_1`.

5. **DUAL / backward angle (scouted, NOT a proof):** "the cyclic-successor map applied to `a_1` already lands in the periodic regime." Empirically `cyc_succ_B(a_1) = a_2` universally (opening #4). The backward-predecessor framing is less useful here: every element of `B` has a predecessor in `B` (Theorem 1 single cycle), but that only shows `a_1` COULD be on a cycle, not that it IS on THIS cycle. The forward seed (opening 1) is stronger.

### Candidate technique(s)

- **Hitting-set well-foundedness** (`primes(a_1) ⊇ some h ∈ M'_∞`) — the seed. KB: *Pigeonhole/extremal* (minimal element of a finite poset); *Divisor analysis* (`m_h | a_1` from `h ⊆ supp(a_1)`).
- **Induction on `n` with `σ(a_{n+1})` hitting `F'_∞`** — the induction step. No KB entry directly fits; it is a "no large-prime-as-sole-shared-prime" claim (cousin of B1').
- The **cross-intersecting closure lemma** (CERTIFIED, unconditional) is a candidate for the induction step: it gives an EARLY freeze of `M_n` once cross-intersecting. If `M'_∞` is cross-intersecting from the start (empirically: `M'_∞` for 15,35,77,91 are pairwise cross-intersecting — each pair shares a prime), the closure lemma might let the induction step piggyback on the freeze. **Worth a builder probe**: is `M'_∞` always pairwise cross-intersecting, and does that imply `min(B_n ∩ (a_n,∞)) ∈ B` for `n < N`?

### Cheap-kill candidates

- **The seed** (opening 1) IS the cheap kill for the seed sub-gap — already done.
- **Parity / `2 ∈ S` for odd `a_1`**: the observation that `2` is always a kernel prime for odd `a_1` (the greedy hits an even `a_2`, and evenness propagates through the kernel) is a cheap structural fact that resolves the `n=1` first-jump for odd `a_1`. A builder can prove `2 ∈ S` for odd `a_1` in 2 lines (the greedy reaches an even term immediately, and once an even term exists, 2 is a hitting prime of `F'_∞`).
- **No obvious kill for the general induction step** — it is the crux.

### Knowledge-base entries to use

- *Universal-small-prime* (CERTIFIED lemma) — the engine of the seed.
- *Pigeonhole/extremal* — well-foundedness of minimal hitting sets over finite `P_R`.
- *Divisor analysis* — `m_h | a_1` from `h ⊆ supp(a_1)`; consecutive-integer coprimality (for `2 ∈ S`).
- *Cross-intersecting closure lemma* (CERTIFIED, `lemmas/cross-intersecting-closure.md`) — candidate for the induction-step freeze.
- *Cyclic-successor / periodic-set-iteration* (CERTIFIED Theorem 1) — the engine once `a_1 ∈ B` and the induction step hold: gives `a_{n+T} = a_n + L` from `n=1` directly.

### Analogous past problems (cruxes)

- **none directly retrieved** (did not run a full crux-corpus query this round — the B2 reduction is internal to this problem's machinery; the closest analog is the problem's own Theorem 1). A builder pursuing the induction step should query the crux corpus for "minimal hitting set stabilization" / "greedy sequence shares small prime with all future terms" subtopics, but no prior crux jumped out as analogous to the B2 induction step.

### Prior progress

- **Conditional spine (B1' ⟹ periodicity from `N`)** is CERTIFIED (round 2). The seed `a_N ∈ B` was certified automatic given B1'. **This round strengthens it: `a_1 ∈ B` is automatic given B1'** (opening 1) — so the seed sub-gap for B2 is dissolved at `n=1`, not just at `n=N`.
- **Empirical B2 invariant** (round 2): pre-period empty for `a_1 ∈ {15,35,45,77,91,105,135,175,187,221,385}`. **This round extends it**: 0 mismatches between `min(B_n ∩ (a_n,∞))` and `cyc_succ_B(a_n)` across ALL `n` (not just `n < N_stab`) for `a_1 ∈ {15,21,33,35,39,77,91,105,135,175,187,221,385}` plus adversarial `21,33,39,55,65,69,85,95,115,119,133,143,145,155`. The induction step is empirically rock-solid.

### Dead ends (do not retry)

- **Injectivity-on-residues bypass of B2** (`bijection-from-n1` round 1): the transition on residues mod `L` is not well-defined until `A_n` is periodic mod `L` (= B1). Confirmed collapsed; do not retry.
- **Profinite-compactness in `Ẑ`** (`periodic-set-iteration` step 3): yields a profinite point, not a finite-period set containing the orbit. Not a B2 bypass.
- **Frozen-invariant monovariant** (`frozen-invariant-reduce-mod-lcm`, retired): `w_n = min{m > a_n : m ∉ B_n}` is non-decreasing (wrong direction); the aimo-0678 shape does not transfer. Not a B2 route.
- **Clean value-window (Cov) sufficiency** for B1' (refuted, 9927 violations at `a_1=15`): this refutes a B1' attack, NOT a B2 attack, but any B2 route that secretly reduces to "no `B_n \ B` element in a short value window" should be checked against this — the `B_n \ B` candidates are SMALL-prime (different from the refuted large-prime `A_n \ B_n` window), so the refutation does NOT directly transfer. Still, a builder should not assume "short window ⟹ empty" without proof.

### Small-case / intuition notes (labeled CONJECTURE)

- **CONJECTURE (seed, now proved given B1')**: `a_1 ∈ B`. — Rigorous (opening 1).
- **CONJECTURE (induction step)**: `min(B_n ∩ (a_n,∞)) = cyc_succ_B(a_n) = a_{n+1}` for every `n ≥ 1`, given B1'. Empirically universal (0 mismatches, 30+ `a_1`, all `n`). Equivalent to "`σ(a_{n+1})` is a hitting set of `F'_∞`" = "every future `a_j` shares a small prime with `a_{n+1}`." NOT proved.
- **CONJECTURE (cross-intersecting `M'_∞`)**: `M'_∞` is pairwise cross-intersecting in every tested case (15: {2,3},{2,5},{3,5} — yes; 35: {2,3,7},{2,5},{3,5},{5,7} — {2,3,7}∩{5,7}={7}✓, {2,5}∩{3,5}={5}✓, yes; 77,91 similar). If always true, the cross-intersecting closure lemma gives an early freeze — a candidate route for the induction step.
- **CONJECTURE (`2 ∈ S` for odd `a_1`)**: empirically `2 ∈ S` whenever `a_1` is odd (every tested odd `a_1`). Resolves the `n=1` first-jump for odd `a_1` via the even-multiple mechanism. Cheap to prove.
- **The pre-period is empty in every tested case** (`a_{1+T} = a_1 + L` from `n=1`); combined with the seed theorem, this means the ONLY remaining B2 ingredient is the induction step.

### The SINGLE most promising concrete next step for a builder

**Prove the SEED theorem (opening 1) formally and certify it as a lemma** (`lemmas/a1-on-cycle.md`): "Given B1' (the stabilized small-prime admissible set `B` with kernel `S` and `M'_∞`), `a_1 ∈ B`." This is a 4-line proof (universal-small-prime ⟹ `primes(a_1)` hits `F'_∞` ⟹ `primes(a_1) ⊇ h ∈ M'_∞` ⟹ `m_h | a_1` ⟹ `a_1 ∈ B`), unconditional given B1', and it is the cleanest NEW rigorous contribution on the B2 front. It does NOT close B2 (the induction step remains), but it converts B2 from "extend periodicity backward from `N` to `1`" into "prove the induction step `a_{n+1} = cyc_succ_B(a_n)` for `n < N`," a strictly easier-to-state target. Pair it with a probe of the **cross-intersecting `M'_∞` conjecture** as the induction-step attack: if `M'_∞` is always pairwise cross-intersecting (empirically yes), the cross-intersecting closure lemma may let the induction step piggyback on an early freeze, giving B2 without re-proving B1'.
