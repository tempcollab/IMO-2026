# Approach: cross-intersecting-anchor

## Status
partial (skeleton, round 3 NEW)

## Framing (one line)
The stabilized minimal-hitting-set family `M'_∞` is **pairwise cross-intersecting** (a structural property of the greedy); by the certified closure lemma this freezes `M'` early, and the R-smooth terms act as **anchors** forcing every admissible `m` to hit all past `σ_i` via small primes — closing B1' by strong induction.

## Distinct route
This attacks B1' as a **structural property of the stabilized kernel** (`M'_∞` cross-intersecting + R-smooth subfamily generates it), NOT via spacing/v_p density (exhausted) and NOT via bare transversal duality (one-prime swap fails). The load-bearing ingredient is a property OF THE GREEDY's `M'_∞`, not of arbitrary hypergraphs.

## Skeleton
Target: the whole theorem. Prove B1' via the cross-intersecting anchor; then the CERTIFIED conditional spine (B1' ⟹ periodicity from `N`) gives `a_{n+T}=a_n+L` for `n≥N`; the B2 induction (sibling slug `b2-induction-step`) extends to `n≥1`. Trivial cases imported.

Setup (imports, all CERTIFIED): bounded-difference (`lemmas/bounded-difference.md`), universal-small-prime (`lemmas/universal-small-prime.md`), Theorem 1 (`lemmas/periodic-set-iteration.md`), small-prime-inclusion (`M'_n⊆M_n`, `B_n⊆A_n`), small-prime-minimum-in-window (`b_n≤a_n+R`), cross-intersecting-closure (`lemmas/cross-intersecting-closure.md`: if `M_n` cross-intersecting and new row hits `F_n` then `M_{n+1}=M_n`).

Notation: `R=rad(a_1)`, `P_R={primes≤R}`, `σ_i=supp(a_i)∩P_R`, `F'_n={distinct σ_i : i≤n}`, `M'_n`=minimal hitting sets of `F'_n` (⊆`2^{P_R}`), `B_n=∪_{h∈M'_n}{mult of m_h}`, `b_n=min(B_n∩(a_n,∞))`.

1. **One-sided inclusion (import).** `B_n⊆A_n`, so `a_{n+1}≤b_n≤a_n+R`. (CERTIFIED.)
2. **Freeze-early (import).** If `M'_n` is cross-intersecting and `σ(a_{n+1})` hits `F'_n` then `M'_{n+1}=M'_n` (closure lemma). Under B1', `σ(a_{n+1})⊇h_0∈M'_n` always (greedy lands in `B_n`), so the lemma applies verbatim.
3. **The anchor induction (B1').** Strong induction on `n`. Assume `a_i=b_i` for `i≤n`. Let `F'_smooth,n = {σ(a_j) : j≤n, supp(a_j)⊆P_R}` (R-smooth small-support family) and `M'_smooth,n` its minimal hitting sets.
   - **(Anchor key-lemma A)** `M'_smooth,n = M'_n` for all `n` past a bounded pre-anchor phase — i.e. the R-smooth subfamily already generates every minimal hitting set. **[GAP A — mechanism below]**
   - **(Anchor key-lemma B)** `M'_n` is pairwise cross-intersecting. **[GAP B — mechanism below]**
   - **Close.** Take any admissible `m∈A_n∩(a_n,a_n+R]`. For every R-smooth `a_j` (`j≤n`), `gcd(m,a_j)>1` and `a_j` has no large prime, so the shared prime is small: `σ(m)∩σ(a_j)≠∅`. Hence `σ(m)` hits `F'_smooth,n`; by (A) it contains `h∈M'_smooth,n=M'_n`. By (B) cross-intersecting, `h∩h_i≠∅` for every `h_i∈M'_n`; since each `σ_i⊇h_i`, `h∩σ_i≠∅`. So `σ(m)` hits all `F'_n`, i.e. `m∈B_n`. Thus `A_n∩(a_n,a_n+R]⊆B_n` (conjecture C), giving `a_{n+1}=b_n`. B1' holds at `n+1`; induction proceeds. ∎ (modulo gaps A, B, and pre-anchor)
4. **Pre-anchor fallback.** For the finitely many steps before (A)/(B) kick in (e.g. `n=1,2` for `a_1=135`), use the spacing fact + specific window arithmetic (the only large-prime multiple in the window has the wrong small primes). **[GAP C — finite casework, lower-stakes]**
5. **Certified spine.** Granting B1', `F'_n` stabilizes over finite `P_R` (pigeonhole) at `N`; `M'_∞`,`B`,`L=∏∪M'_∞` fixed; seed `a_N∈B` automatic; Theorem 1 ⇒ `a_{n+T}=a_n+L` for `n≥N`. (CERTIFIED, cite — do NOT re-prove.)
6. **B2 (from-`n=1`).** Defer to sibling slug `b2-induction-step` (seed `a_1∈B` is a theorem given B1'; induction step via the same cross-intersecting early freeze — `M'_n=M'_∞` early ⟹ `B_n=B` early ⟹ no prematurely-valid `B_n\B` candidate). **[GAP D — owned by b2-induction-step]**

## Key lemmas (claim + one-line mechanism)
- **(A) R-smooth subfamily generates `M'_n`.** Because every `h∈M'_n` (a minimal hitting set over `P_R`) is itself a subset of `P_R`, and `m_h=∏_{p∈h}p` is R-smooth and admissible (hits every `σ_i`), so `m_h`'s own R-smooth σ-witness... **mechanism open** — the gap is showing the R-smooth TERMS (not just kernels) realize every `σ*∈F'_n`. This is exactly conjecture (W) of the `w-descent-rsmooth` slug; the two slugs share this sub-gap (flagged coupling).
- **(B) `M'_∞` pairwise cross-intersecting.** Empirically 12/12 tested `a_1` (incl. 4-prime `a_1=210,1155`; `|M'_∞|` 1–7). Mechanism conjecture: the greedy's selection forces any two minimal hitting sets to share a prime because `a_1`'s own support `primes(a_1)⊆σ(a_1)` is hit by BOTH (every hitting set hits `σ(a_1)`, but that only gives pairwise intersection through `primes(a_1)` if `|primes(a_1)|=1`...). **Mechanism open.** A clean sufficient sub-claim: every `h∈M'_∞` contains a prime of `a_1` — then since all `h` hit `σ(a_1)⊇primes(a_1)`, two `h`'s need not share... actually cross-intersection is STRICTLY STRONGER than "each hits σ(a_1)". The crux is genuinely open; probe: is `M'_∞` cross-intersecting BECAUSE every `h` contains some `p∈primes(a_1)` AND the `primes(a_1)`-substructure is a clique? Test.
- **(Anchor close)** admissible `m` ⟹ hits every R-smooth `a_j` via a SMALL prime (since `a_j` has no large prime) ⟹ `σ(m)⊇h∈M'_n` ⟹ (cross-intersecting) `h` hits every `σ_i` ⟹ `m∈B_n`. This 3-line chain is the cheap kill ONCE (A)+(B) hold.

## Open gaps (builder fills)
- **[GAP A]** `M'_smooth,n = M'_n` past a bounded phase (= conjecture W: every `σ*∈F'_n` has an R-smooth term). Shared with `w-descent-rsmooth`.
- **[GAP B]** `M'_∞` always pairwise cross-intersecting. THE distinctive crux of this slug.
- **[GAP C]** Pre-anchor finite casework (spacing + arithmetic).
- **[GAP D]** B2 (deferred to `b2-induction-step`).

## Cases to cover
- Trivial: `a_1` even / `a_1=p^k` (imported, done).
- R-large regime (`R≥77`, 8/11 tested `a_1`): no `a_n` ever has a large prime ⟹ (A) trivial (every term R-smooth), B1' immediate. **Record as a clean sub-theorem** (verify threshold).
- R-small hard regime (`a_1∈{15,45,135}`, `R=15`): the real test of (A)+(B).

## Watch out for
- (B) is NOT implied by universal-small-prime (necessary ≠ sufficient; 1515/5000 arbitrary hypergraphs have large-only MHS — recorded dead end). The proof MUST use greedy-specific structure, not bare transversal theory.
- "every `h∈M'_∞` hits `σ(a_1)`" does NOT give cross-intersection (two sets can each hit `σ(a_1)` disjointly). Do not claim it.
- The cross-intersecting closure lemma only freezes `M'`; it does NOT itself prove `M'_∞` is cross-intersecting. (B) is the input, the lemma is the consequence.
- Coupling: (A) is shared with `w-descent-rsmooth`. If (A) fails, both slugs share that wall — but they attack it by DIFFERENT mechanisms (this slug via the anchor/cross-intersection route, the other via s-substitution descent), so the shared sub-gap is approached from two sides (acceptable diversity, not a single-gap trap).
