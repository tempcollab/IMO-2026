## imo-2026-06

**Lens: shadow-sequence / look-ahead cofinality route to B1'.**

### Distinct openings

Five distinct openings surfaced on the shadow-sequence framing, each a different attack the outliner could build into a rival approach:

1. **Anchor induction (the main opening).** Define the self-referential shadow `b_n`: `b_1=a_1`, `b_{n+1}=min(B_n ∩ (b_n,∞))` where `B_n = ∪_{h∈M'_n}{mult of m_h}` is the small-prime admissible set built from `b`'s OWN small supports `σ'_i = supp(b_i) ∩ P_R`. (Equivalently: `b_{n+1} = min{m>b_n : σ(m)∩σ'_i≠∅ ∀i≤n}`.) B1' is exactly `a_n=b_n`. The **anchor mechanism**: every R-smooth term `a_j` (all prime factors ≤R) forces any admissible `m` to hit it via a SMALL prime (since `a_j` has no large primes). The R-smooth terms' `σ`'s generate a subfamily `F'_smooth`; every admissible `m` has `σ(m) ⊇ some h∈M'_smooth`. **If every `h∈M'_smooth` hits every `σ_i`** (the "anchor condition"), then `m∈B_n` and B1' holds by strong induction. Verified: anchor works from `n=1` for `a_1=15`, from `n=3` for `a_1=135`. The induction closes once the anchor kicks in; the closure lemma (`lemmas/cross-intersecting-closure.md`) keeps `M'` frozen.

2. **`M'_∞` universal cross-intersecting (structural property).** Empirically `M'_∞` is cross-intersecting for ALL 12 tested `a_1` (including 4-prime cases `a_1=210, 1155`; `|M'_∞|` ranges 1–7, always cross-intersecting). This is the KEY unproved structural fact: if `M'_∞` is always cross-intersecting, then (by the closure lemma) `M'` freezes as soon as it becomes cross-intersecting (typically `n=2–3`), and the anchor induction closes cleanly. The greedy's selection rule imposes structure on the `σ`'s that prevents disjoint minimal hitting sets. **This is the single most promising concrete target for a builder.**

3. **Pre-anchor fallback (spacing + arithmetic).** For the finitely many steps before the anchor kicks in (e.g. `n=1,2` for `a_1=135`), the spacing fact (`q>R` divides ≤1 window integer) plus the specific arithmetic of the window prevents shortcuts. At `a_1=135, n=1`: the only candidate `m=139` (between `a_1=138` and `b_2=140`) is prime and inadmissible. At `n=5, q=23`: `m=161=7·23` has `σ={7}` which misses `a_0=135`'s `σ={3,5}` → "not A". The mechanism: the R-smooth term `a_0=135` (with only primes 3,5) forces `m` to have 3 or 5, but the specific large-prime multiple in the window has the WRONG small primes. Hard to generalize but finitely many steps per `a_1`.

4. **`A_n \ B_n` global emptiness near `a_n` (conjecture (C), strengthened).** Computed: `A_n \ B_n` is EMPTY in `(a_n, a_n+10R]` for ALL tested `n` and `a_1` (searched up to `200R` for `a_1=15`, `100R` for `a_1=77`; 0 elements found). This is FAR stronger than B1' (which only needs the minima to coincide) and stronger than conjecture (C) from prior rounds (which only covers `(a_n, a_n+R]`). The `A_n\B_n` set is either empty near `a_n` or starts very far away — suggesting B1' is not a delicate balance but a structural identity `A_n≈B_n` near `a_n`.

5. **Counterfactual divergence (no self-correction).** Artificially inserting a shortcut value (e.g. `21` instead of `18` at step 2 for `a_1=15`) causes the greedy to DIVERGE permanently — no recovery to the shadow path within 15+ steps. Inserting a value ON the correct path (e.g. `20` instead of `18`) causes immediate convergence. This means: there is no "look-ahead cofinality" that forces recovery — B1' must hold for a DIRECT reason (no shortcut exists), not because shortcuts are self-correcting. The look-ahead argument as described in the prompt does NOT work: a large prime `q` used at step `n` does not create a future obstruction (the greedy simply diverges to a different valid sequence). **The look-ahead/cofinality framing is a dead end; the anchor mechanism is the live opening.**

### Candidate technique(s)

- **Strong induction on `n` with the anchor as the induction step** (the main technique). The R-smooth terms act as invariants that force `σ(a_{n+1})` to be a hitting set of `F'_smooth`, which (once the anchor kicks in) implies `a_{n+1}∈B_n`.
- **Cross-intersecting closure lemma** (already certified, `lemmas/cross-intersecting-closure.md`): if `M'_n` is cross-intersecting and the new `σ` is a hitting set, `M'` freezes. The anchor induction uses this to keep `M'` frozen.
- **Spacing fact** (certified, `lemmas/spacing-fact.md`): for the pre-anchor fallback, `q>R` divides ≤1 window integer.
- **Pigeonhole/extremal** (KB): `F'_n` stabilizes over finite `P_R`; `M'_∞` is cross-intersecting (empirically, needs proof).

### Cheap-kill candidates

- **The anchor is a cheap kill for the post-stabilization regime.** Once `M'_∞` is cross-intersecting (empirically always true) and frozen, B1' follows in 3 lines: admissible → hits R-smooth terms via small primes → `σ⊇h∈M'_∞=M'_n` → `h` hits all `σ_i` → `∈B_n`. The only non-trivial ingredient is proving `M'_∞` is always cross-intersecting.
- **Global `A\B` emptiness** (conjecture (C), strengthened): `A_n\B_n` empty in `(a_n, a_n+100R]` — if provable by a density/pigeonhole argument, B1' collapses. But the density route was already refuted (`sieve error ~a_n > signal ~n·δ`), so this is a target for a DIFFERENT density argument (not `v_p`-based).

### Knowledge-base entries to use

- **Pigeonhole/extremal principle** (KB "Combinatorics"): `F'_n` stabilizes over finite `P_R`; `M'_∞` cross-intersecting.
- **Induction (strong)** (KB "General Proof Methods"): the anchor induction on `n`.
- **Modular arithmetic/CRT** (KB "Number Theory"): the `σ`-periodicity structure (already in `lemmas/sigma-periodicity.md`).
- **Invariants/monovariants** (KB "Combinatorics"): the R-smooth terms are an invariant anchor (their `σ`'s never change once established).

### Analogous past problems (cruxes)

- **`aimo-0184`** (Bulgaria): greedy-minimal sequence `a_n = smallest x>a_{n-1}` with a floor-sum condition. Crux: "match a greedily-minimal recursion `x=1+S(x)` to a candidate set by plugging the count identity into `S` at a candidate: a target leaves exactly +1 slack while a non-target makes `S(x)=x` (forcing `x=x+1`)." This is structurally analogous to B1': the shadow `b_n` is the "candidate set" (the small-prime-admissible greedy), and the real greedy matches it because no shortcut candidate satisfies the full constraint. The key parallel: in `aimo-0184`, the identity `Σ floor(...) = x` for non-targets forces `x=x+1`, a contradiction; here, the anchor forces `σ(m)⊇h∈M'_∞` which hits all `σ`'s, so `m∈B_n` — the shortcut "absorbs" into `B_n`.
- **`aimo-0224`** (Peru): coprimality pattern encoded via prime assignments to subsets. Crux: "encode coprimality as disjointness of subsets." Tangentially related (our `σ`'s encode gcd structure), but the problem is about construction, not greedy matching. Weak analogy.
- **`aimo-0208`**: admissible set closed under `x²+kxy+y²`. Crux: "exhibit a proper subset closed under the operation" (`dℤ` when `gcd(m,n)=d>1`). Weakly analogous: `B_n⊆A_n` is like `dℤ⊆ℤ` — the small-prime structure is a "proper subset" of the full admissible structure.

### Prior progress

- **B1' pinpointed** (round 2): `a_{n+1}=min(B_n∩(a_n,∞))` for all `n`, equivalently `M_n=M'_n`. Conditional spine (B1' ⟹ periodicity from `N`) is CERTIFIED. Three coupled mechanisms (spacing, `v_p`/density, covering) all bottom out at "demand ~n vs capacity ~a_n~(L/T)·n with L≥2."
- **Conjecture (C)** recorded: `A_n∩(a_n,a_n+R]⊆B_n`, 0 violations over 480+ pairs. This exploration strengthens (C): `A_n\B_n` is empty in `(a_n, a_n+100R]` (not just `R`).
- **The self-referential shadow `b_n`**: computed `a_n=b_n` for `a_1∈{15,35,77,91,105,135,187,221,385}`, `N=100` each, with 0 divergence (max gap `a_n-b_n=0` in every case). This is a NEW computation confirming B1' from the shadow-sequence perspective.

### Dead ends (do not retry)

- **Look-ahead / cofinality argument**: a large prime `q>R` used at step `n` does NOT create a future obstruction. Counterfactual test: inserting a shortcut value (e.g. 21 for `a_1=15`) causes permanent divergence with NO recovery. The greedy simply follows a different valid sequence. The "q must divide some future `a_j`" argument does not yield a contradiction — `q` can recur sparsely without causing problems.
- **Bertrand/competing-candidate** (round 1): a single-kernel-prime multiple is not a universal admissible candidate.
- **Residue-mod-M-only finite-state bypass** (round 1): residue does not determine next residue.
- **Profinite compactness** (round 1): yields profinite point, not finite-period set.
- **Injectivity-on-residues** (round 1): transition not well-defined without B1.
- **Frozen-invariant monovariant** (round 2, retired): `w_n` is non-decreasing (wrong direction); no frozen invariant exists.
- **`v_p` union-bound beyond `n_0`** (round 2): sieve error `~a_n` outpaces signal `~n·δ`. NOT independent of spacing wall.
- **Clean value-window (Cov) sufficiency** (round 2, refuted): `σ*`-terms too sparse in length-`(q_min-R)` windows; 9927 violations at `a_1=15`.
- **Transversal-minimality / Hall-König duality** (round 2): one-prime swap fails; Hall/König doesn't apply to hypergraph transversals; universal-small-prime necessary but not sufficient (1515/5000 counterexamples).

### Small-case / intuition notes (all CONJECTURE, labeled as such)

- **`a_n=b_n` always** (conjecture): verified for 9 `a_1` values, 100 terms each, 0 divergence. The self-referential shadow exactly matches the real greedy.
- **`M'_∞` always cross-intersecting** (conjecture): verified for 12 `a_1` values (including 4-prime `a_1=210, 1155`), always cross-intersecting. If provable, the anchor induction closes.
- **Anchor kicks in after ≤3 R-smooth terms** (conjecture): for `a_1=15`, anchor works from `n=1`; for `a_1=135`, from `n=3`. The R-smooth family stabilizes to `M'_∞` after 2–4 terms.
- **Large-prime free-riders are harmless** (conjecture): for `a_1=15`, 30% of terms (n≥23) carry large primes (17,19,23,29,31,37), but their `σ`'s are ALREADY in `F'_∞` — the large prime is a free-rider that doesn't change the hitting-set structure.
- **`A_n\B_n` is globally empty near `a_n`** (conjecture, stronger than (C)): 0 elements in `(a_n, a_n+100R]` for all tested `n, a_1`. The shortcut set is either empty near `a_n` or starts very far away.
- **For `R≥77`, all terms are R-smooth** (conjecture): `a_1∈{77,91,105,187,221,385}` have 0 large-prime terms in 100 steps. B1' is trivially true (A_n=B_n) when all terms are R-smooth. The hard case is small R (R=15 for `a_1=15,135`).
