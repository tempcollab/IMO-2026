# Outline review — imo-2026-06 (round 1)

## Problem
Prove ∃ T,L>0 with `a_{n+T} = a_n + L` for every n≥1, where `a_{n+1}` is the least integer > `a_n` sharing a nontrivial gcd with every past term. IMO 2026 P6, difficulty 9.

## The shared crux (the "B1 river")
Every route must cross, avoid, or hand-wave one step: **the active/kernel prime set S is finite (and bounded, conjecturally `S ⊆ {primes ≤ R = rad(a_1)}`).** I verified empirically:
- Bounded-diff lemma `a_{n+1}-a_n ≤ rad(a_1)` holds in all tested cases (a_1 ∈ {6,10,15,21,35,77}); max diff ≤ R always. CLEAN — certify it as a shared lemma.
- The set of primes dividing some `a_n` is **NOT finite** (a_1=15 accumulates 12+ distinct primes by term 60, up to 37). So "all primes appearing" is the wrong object; the *kernel* `S = primes(L)` (e.g. {2,3,5} for a_1=15, where L=30) is the stabilizing object. This matches the outliner's warning.
- L is a multiple of R in multi-prime cases (15→30, 77→154); period holds from n=1 in every tested case (empty pre-period).

The B1 step is genuinely open in every approach that needs it. The honest routes flag it; the gambles try to avoid it.

## Shared lemma of cross-route value
`periodic-set-iteration`'s **Theorem 1** (iterating least-greater-than on a fixed periodic set is a single cycle from the start — cyclic successor on sorted residues is a transitive bijection) is the clean "lift = L / from-n=1" mechanism that `bounded-diff-finite-state`, `hitting-set-monovariant`, and `bijection-from-n1` all need for their final steps. Its proof is short and concrete. **The builder of periodic-set-iteration should prove and certify Theorem 1 in `lemmas/` first** so all routes can import it. Likewise the bounded-diff lemma `≤ rad(a_1)` should be certified (the builder of bounded-diff-finite-state owns it).

---

## Per-approach verdict

### bounded-diff-finite-state — KEEP (APPROVE)
The most direct, honest attack on B1. Skeleton is sound: each step follows from the previous; the bounded-diff lemma is clean and verified. The B1 mechanism (competing-candidate: the next multiple of any kernel prime `p ≤ R` after `a_n` is ≤ `a_n+p ≤ a_n+R`, beating any large-prime candidate via a Bertrand-style dyadic comparison) is a concrete, plausible number-theoretic argument — the best-stated crux mechanism in the field. Sub-gaps (large-prime shortcuts stop; lift = L; injectivity for from-n=1) are correctly nested under B1. The modulus caution (use L=∏S, NOT ∏_{p≤R}p — verified FALSE for a_1=15) is correct and important.
**Gaps the builder must close:** step 2 (B1 — make the competing-candidate + Bertrand argument rigorous, including the "2 is forced for odd a_1" cascade); step 3 (large-prime shortcuts stop — watch the circularity, resolved because F is bounded by 2^S); step 6 (injectivity for from-n=1, or a direct from-n=1 argument).

### hitting-set-monovariant — KEEP (APPROVE)
Genuinely distinct mechanism from bounded-diff: the primary object is the combinatorial family `M_n` of minimal hitting sets, not a residue automaton. The **cross-intersecting closure lemma (step 3) is clean and the best structural insight in the field** — once `M_n` is pairwise cross-intersecting, it is self-sustaining forever (new term's support contains a current `h` meeting every `h'`, so nothing removed/added). This is a real, provable lemma. The monovariant crux (step 4) honestly admits it needs B1 to make the poset finite (`Σ|h|` alone is not well-founded without bounded active primes) — correct self-diagnosis. Handles both attractors (singleton collapse `{{p}}` → T=1, and cross-intersecting closure → T>1).
**Gaps:** step 4 (the well-founded measure — the heart; needs both the measure AND B1 to bound its range); step 6 (each residue once per period); step 7 (from-n=1).
**Concern:** shares the B1 wall with bounded-diff-finite-state. If B1 is fundamentally hard, both stall. Mitigated by the three gambles.

### periodic-set-iteration — KEEP (APPROVE, lower priority)
The factorization is the field's best structural idea: separate (I) a pure combinatorial theorem on periodic-set iteration (CLEAN, short, shared value) from (II) the number-theoretic convergence of `A_n`. Theorem 1 is concrete and provable. The distinctive gamble — profinite compactness on the chain of residue-class descriptions to extract a finite periodic quotient WITHOUT bounding S — is a legitimate research direction, **but currently hand-wavy**: the skeleton itself notes "the orbit is NOT contained in `A_∞=∩A_n`," which breaks the natural compactness framing, and admits the move is a "research gamble." The fallback (B1) makes it a re-skin of bounded-diff if the gamble fails — acceptable, since Theorem 1 is then its real contribution.
**Gaps the builder must close:** prove Theorem 1 rigorously (short — do this first, certify it); make the compactness escape concrete (define the clopen sets in Ẑ precisely, state the extraction theorem) OR concede and use B1. Step 6 (from-n=1) is free once Theorem 1 + a fixed periodic set are established.

### compactness-konig-branch — KEEP (APPROVE, lowest priority; high collapse risk)
The highest-variance route. It aims to AVOID B1 entirely via König's lemma with a LOCAL rad(a_1) branching bound. The skeleton is **admirably honest about its own weakness**: step 3 admits "finite branching of residues is not enough; the node must carry enough state to determine the future" and that this "brings back a finite-family bound (2^{π(R)}) — but then this route secretly re-imports a finite-state argument." The distinctive escape (compactness gives a periodic path even without deterministic state) is under-specified, and step 7 flags a **circularity risk** ("compactness gives an infinite path; finite-state gives eventual periodicity; uniqueness gives the greedy path equals it — read carefully for circularity").
**Verdict:** not doomed — it is a complete attempt at the whole claim with a genuinely non-constructive framing. But the "avoid B1" goal is the likely-failing part; if finite branching of a rich-enough state secretly requires B1, it collapses to bounded-diff-finite-state. Keep live as a long shot; do NOT prioritize until the builder shows finite branching avoids B1.

### bijection-from-n1 — KEEP (APPROVE, lower priority)
Distinctive spine: prove the transition `T` on reachable residues is injective ⇒ bijection ⇒ single cycle ⇒ from-n=1 is FREE (no "eventually then strengthen"). The from-n=1 payoff is real and elegant. **But the skeleton is honest that the crux is currently a non-proof:** the proposed mechanism (cyclic successor monotone on a shift-invariant admissible set) requires the admissible set to be periodic = B1, and the "direct greedy-minimality + symmetry" alternative is sketched but admitted to be a non-proof. The self-diagnosis is exactly right: "if injectivity secretly requires 'admissible set is periodic' (= B1), this route is NOT genuinely distinct — it repackages bounded-diff-finite-state."
**Gap the builder must test:** a DIRECT injectivity argument NOT passing through periodicity of the admissible set. If none exists, the route collapses. The lift step has a subtlety to reconcile (proper-subset cycle vs. full-set cycle — the skeleton flags this; a cycle of the cyclic-successor map sums to L regardless, so it is consistent, but confirm).
**Verdict:** legitimate distinct framing (injectivity is a different shape of difficulty), worth a builder probing directly. Lower priority than the B1-crossers.

---

## Diversity assessment
The field is genuinely far apart in framing — the outliner did its job:
- Two B1-crossers with DIFFERENT mechanisms (competing-candidate/pigeonhole vs. combinatorial monovariant on hitting sets).
- Three distinct gambles that hedge the B1 wall: factorization + profinite compactness; König's lemma + local bound; direct injectivity.

**Shared-wall risk:** bounded-diff-finite-state and hitting-set-monovariant both bottom out on B1. If B1 proves fundamentally hard, both stall together. The build set below sends only ONE of them this round (disciplined per "don't send two builders at the same wall"), keeping the other live in the pool.

---

## Registered slugs (all five kept live)
bounded-diff-finite-state, hitting-set-monovariant, periodic-set-iteration, compactness-konig-branch, bijection-from-n1. No COPY requests this round.

## Ranking table (after head-to-head, K=32, all cold-start 1500 → separated by crux-directness)

| Rank | Slug | Elo | Rationale |
|------|------|-----|-----------|
| 1 | bounded-diff-finite-state | 1560 | Most direct attack on B1; clean bounded-diff lemma; concrete competing-candidate+Bertrand mechanism; honest sub-gaps. |
| 2 | hitting-set-monovariant | 1530 | Clean cross-intersecting closure lemma; well-founded measure is the crux (more speculative than competing-candidate); shares B1 wall. |
| 3 | periodic-set-iteration | 1500 | Theorem 1 is concrete shared value; compactness escape is a legitimate but hand-wavy gamble; falls back to B1. |
| 4 | bijection-from-n1 | 1470 | Injectivity is a genuine distinct crux, but currently a non-proof; admitted likely collapse to bounded-diff. |
| 5 | compactness-konig-branch | 1440 | Highest variance; self-admitted likely collapse to bounded-diff; circularity risk in step 7. |

Pairwise: bounded-diff > all; hitting-set > periodic/bijection/konig; periodic > bijection/konig; bijection > konig.

## Build set rationale
Three builders, DIVERSE framings (no two at the B1 wall together):
- **bounded-diff-finite-state** — the strongest, most direct B1-crosser; advance it to close B1 (competing-candidate+Bertrand) and certify the bounded-diff lemma. Primary hope.
- **periodic-set-iteration** — distinct factorization; builder proves Theorem 1 (shared-lemma value for ALL routes) and attempts the compactness escape OR concedes B1.
- **bijection-from-n1** — genuinely distinct injectivity framing; builder tests whether a DIRECT injectivity argument (not via admissible-set periodicity) exists. Probes a different wall.

hitting-set-monovariant (shares B1 wall with the leader) and compactness-konig-branch (highest collapse risk) stay live in the pool un-built this round; the next round's ranking will pull one in if a B1-crossing or injectivity line stalls.

build set: bounded-diff-finite-state, periodic-set-iteration, bijection-from-n1
