# proof-builder — hitting-set-monovariant (round 2, imo-2026-06)

## Approach
`results/imo-2026-06/approaches/hitting-set-monovariant.md` — REVISED. Transversal-minimality / matching duality attack on crux B1' (`M_n=M'_n`).

## What I proved (rigorous, complete)

1. **Definitional reduction** (Lemma 1): `A_n=∪_{h∈M_n}{mult of m_h}`, identity via well-founded reduction to minimal hitting sets.
2. **Small-prime one-sided inclusion** (Lemma 4): `M'_n⊆M_n`, `B_n⊆A_n` always (small-prime minimal hitting sets are minimal for full supports because supports∩h = σ∩h for small-only h). The crux is the reverse inclusion.
3. **Cross-intersecting closure lemma** (Lemma 6): if `M_n` pairwise cross-intersecting and new row's support is a hitting set of `F_n`, then `M_{n+1}=M_n`. Full minimality-contradiction proof (both "old persist" and "no new" sub-claims). Unconditional — needs NO B1'. Stress-tested: 0 violations / 1581 random families. PROMOTABLE.
4. **Finite-universe stabilization** (Lemma 5): conditional on B1', `F'_n` over fixed finite `P_R` stabilizes by pigeonhole ⇒ `M'_∞`, `B`, `L=∏∪M'_∞` (kernel product) fixed, `B` is `L`-periodic.
5. **Seed automaticity** (Lemma 7): conditional on B1', `a_N∈B` for free (dissolves the round-1 B1(b) seed sub-gap).
6. **Periodicity from N**: conditional on B1'+Lemma 5+7, Theorem 1 (certified import) ⇒ `a_{n+T}=a_n+L` for `n≥N`.
7. **Trivial cases, certified imports** (bounded-diff, universal-small-prime, Theorem 1, `a_1` even / `a_1=p^k`).
8. **Equivalence of B1' with the round-1 free-rider-shortcut wall** — proved both directions: `M_n=M'_n` ⇔ no large-prime shortcut candidate in `(a_n,a_n+R]` below `min(B_n∩...)`. This is the cleanest equivalent form of B1 found.

## Gaps that remain (exact)

**[GAP B1' — THE crux]** `M_n=M'_n` (no minimal hitting set uses a prime `q>R`). Attempted the aimo-0030 (IMO-SL 2013) descent: minimal-counterexample `g∈M_n` with large `q`, witness row `a_j` hit only through `q` (carries small prime `p_j|a_1` not in `g`). The one-prime swap `g→(g\{q})∪{p_j}` FAILS: the other rows `g` hit only through `q` need not be divisible by `p_j`. Unlike aimo-0030's Claim 4 (replace ALL big primes at once by `p^n·∏small`, landing below the original), the hitting-set analogue has no canonical small-only comparable target. Matching/Hall-König duality does NOT apply (hypergraph transversal ≠ bipartite vertex cover; no min=max identity for general set-cover). The obstruction is REAL: a counterexample scan shows 1515/5000 arbitrary small-prime-bearing hypergraphs have a minimal hitting set using ONLY large primes — so "every row has a small prime" (Lemma 3) is necessary but NOT sufficient. The genuine lever must be greedy-specific (spacing / v_p cofinality), not bare transversal theory.

**Honest framing:** B1' is an EQUIVALENT REFORMULATION of the round-1 wall, not a bypass (matches the explorer's Q4 admission and the reviewer's warning). The transversal-duality mechanism formulates it cleanly and pinpoints the break, but does not prove it.

**[GAP B2 — secondary]** from-`n=1` (empty pre-period on the small lattice). Theorem 1's single-cycle removes internal pre-period but doesn't force `a_1,…,a_{N-1}` onto the same cycle. Empirically empty; no proof. Free in trivial cases.

## Spec concerns / coupling
- The crux B1' is SHARED by the whole field: `small-prime-window-lemma` (spacing) and `bounded-diff-finite-state` (v_p) attack the SAME claim with different mechanisms. My transversal-duality mechanism is genuinely independent of spacing (a spacing refutation wouldn't kill it, and vice versa) — the reviewer confirmed this independence — but it does NOT close the gap. If spacing+covering closes B1' next round, my approach's §4 [GAP] can be replaced by citing that result and the whole spine (§1-3, §5-7) goes through unchanged.
- Closure lemma is correctly demoted to early-stabilization shortcut (finite-universe backstop closes the theorem); do NOT re-raise the false monovariant `(|M_n|,Σ|h|,#disjoint-pairs)` — verified non-monotone on `a_1=385`.
- Modulus is the KERNEL product `L=∏∪M'_∞` (e.g. 30), NOT `∏∪F'_∞` (30030) — confirmed for all 6 test inputs.

## Empirics (Python/sympy, conjecture-grade)
- `M'_n = M_n` (full supports) at `n=60` for `a_1∈{15,35,77,91,135,385}`; `S=∪M'_∞⊆{primes≤R}` universally.
- Stabilized `M'_∞`: `a_1=15→{{2,3},{2,5},{3,5}},L=30`; `77→{{2,7},{2,11},{7,11}},L=154`; `91→{{2,7},{2,13},{7,13}},L=182`; `385` (n=60) `∪M={2,3,5,7,11,19}`, all ≤R=385.
- Closure lemma: 0/1581 violations. Descent obstruction: 1515/5000 small-bearing hypergraphs have a large-only minimal hitting set (B1' NOT a consequence of universal-small-prime).

## Self-assessed status
**partial.** All surrounding machinery rigorous (reduction, closure lemma, stabilization, seed, Theorem 1, trivial cases). The theorem is reduced to the single clean claim B1' + secondary B2, both honestly flagged. Two promotable lemmas proposed (cross-intersecting closure; small-prime inclusion).
