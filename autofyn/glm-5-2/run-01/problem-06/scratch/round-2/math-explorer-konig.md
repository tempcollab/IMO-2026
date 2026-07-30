## imo-2026-06 — König/compactness route (`compactness-konig-branch`)

Scout's job: determine whether the König's-lemma / compactness route genuinely bypasses the shared crux B1 (kernel stabilization), or collapses into `bounded-diff-finite-state`. Verdict up front, then the five answers.

### Verdict: the route COLLAPSES into `bounded-diff-finite-state`; it does not bypass B1. Two independent reasons, both fatal and both verified empirically.

---

### Answer 1 — Can finite branching be achieved WITHOUT re-importing B1? NO (collapse).

Two separate requirements are conflated in the skeleton, and only the first survives without B1:

- **(a) Finite branching (for König's lemma).** This holds cheaply and WITHOUT B1. At a node, the next value lies in `(a_n, a_n+R]` (bounded-diff lemma, certified), so the next residue mod any `M` lies in `{r_n+1,…,r_n+R} mod M` — at most `R` children. König's lemma applies. This part is genuinely B1-free.
- **(b) Finite node-TYPES with deterministic transitions (for "infinite path ⇒ eventually periodic").** This is where the route dies. The standard fact the skeleton invokes in step 5 is NOT "infinite path in a finitely-branching tree ⇒ eventually periodic"; it is "infinite walk in a **finite directed graph whose transitions are a function of the current vertex** ⇒ eventually periodic." The residue-tree's vertices are residues mod `M`, but the transition is **history-dependent, not a function of the residue**.

Empirical proof that residue does NOT determine the next residue (a_1=15, M=R=15):
- Real greedy path reaches residue `0 mod 15` at `a_5=30`; the next residue is `10` (`a_6=40`).
- Alternative greedy-continued path `[15,21,24,27,30,…]` reaches residue `0 mod 15` at `b_4=30`; the next residue is `3` (`b_5=33`).
- **Same residue (0 mod 15), different next residue (10 vs 3).** The residue alone does not determine the future.

So the residue sequence of an arbitrary infinite path through the residue-tree is NOT forced to be eventually periodic just from `M` being finite. To make the transition a function of the node (so that finite node-types ⇒ eventually periodic), the node must carry the full state: **residue + small-prime-support family of past terms restricted to primes ≤ R**. That state is exactly `F_n = {supp(a_i) ∩ S_0 : i ≤ n}` over `S_0 ⊆ {primes ≤ R}` — which is `bounded-diff-finite-state`'s **Lemma 3** (certified). The state space is `(residue mod M) × 2^{2^{S_0}}`, finite, but this IS the bounded-diff-finite-state machinery verbatim. The König route, to close step 5 honestly, re-imports Lemma 3 = the B1 support-family stabilization. **Distinct? No — it is a relabeling.** The only B1-free piece (residue-window finite branching) is insufficient on its own; the piece that closes the argument is B1's machinery.

---

### Answer 2 — Is "greedy path = unique infinite path" sound? NO (two senses, both fail).

The skeleton's step 7 hinges on "at each node, exactly one child extends to an infinite path." This is unsound in BOTH interpretations of the tree:

**(i) Greedy-prefix tree** (node = residue-history of THE greedy sequence from a fixed b_1≡a_1). The greedy is deterministic: given b_1, every b_{n+1} is the unique least admissible. So the tree is a **single path**. König's lemma is vacuous (an infinite path exists trivially), and "unique infinite path" is trivially true but tells us nothing — we still must prove that single path is eventually periodic, which needs the finite state of Answer 1 (= B1). The argument is circular: uniqueness is free but useless; the hard work is periodicity, which is B1.

**(ii) Consistent-prefix tree** (node = residue-history of ANY greedy-continued sequence with b_1≡a_1 mod M, allowing b_2 to be any admissible value, not just the greedy least; subsequent steps greedy). Here the tree branches and König applies. But **uniqueness is FALSE**: many children extend to infinite valid greedy-continued sequences, and many of those are periodic with DIFFERENT periods and lifts. Empirically (a_1=15, M=15), all of these are valid infinite paths through the consistent tree:

| prefix (b_1,b_2) | resulting period (T,L) |
|---|---|
| (15,18) — the REAL greedy | (8, 30) |
| (15,20) | (8, 30) — same period, different path |
| (15,21) | (1, 3) |
| (15,25) | (1, 5) |
| (15,30) | (1, 3) |
| (15,33) | (1, 3) |
| (15,35) | no short period found in 60 terms (complex transient) |

So the consistent tree contains **multiple distinct periodic infinite paths with different (T,L)** — `(8,30)`, `(1,3)`, `(1,5)`, and long-transient paths. The real greedy `(8,30)` is just one among many. There is no sense in which "the greedy path is the unique infinite path." The deterministic greedy picks the unique least AT EACH STEP for a FIXED b_1, but the tree ranges over b_1 (and over non-greedy first choices), so uniqueness of the infinite path is false. The skeleton conflates "the greedy is deterministic for fixed b_1" (true) with "the tree has a unique infinite path" (false).

The tension resolves against the route: the greedy-prefix tree makes König vacuous; the consistent-prefix tree makes uniqueness false. Neither supports step 7.

---

### Answer 3 — Does "infinite path ⇒ eventually periodic" yield `a_{n+T}=a_n+L` or just congruence? Just congruence, and only weakly.

Even granting (counterfactually, per Answer 1) a finite deterministic state, the standard "finite directed graph ⇒ eventually periodic walk" fact yields `a_{n+T} ≡ a_n (mod M)` eventually — a **congruence of residues**, not equality with a constant lift. To promote congruence to `a_{n+T}=a_n+L` (equality with constant `L`) requires:
- the **bounded-diff lemma** (the lift `a_{n+T}-a_n` is bounded, hence eventually constant among finitely many values), AND
- the **cyclic-successor-on-a-periodic-set theorem** (certified, `lemmas/periodic-set-iteration.md`), which requires the orbit to live on a FIXED periodic SET `A` (not merely have periodic residues) and gives lift exactly `L`, single cycle, no pre-period.

Both are shared with every other route; the König route does not close the lift for free. Moreover, "periodic residues mod M" + "bounded diffs" does NOT suffice: the residues mod 15 of the real greedy are periodic with `T=8` (because `15 | 30 = L`), but this periodicity of residues is a CONSEQUENCE of the value-periodicity `a_{n+8}=a_n+30`, not a substitute for it. The lift `30` is not determined by the residue mod `15` (it is `2·rad(15)`, the kernel product, not a function of the modulus `R`). So the lift step is inherited, not closed.

---

### Answer 4 — Does compactness give from-n=1 for free? NO (B2 restated).

Compactness (König) gives the EXISTENCE of SOME infinite path that is (counterfactually) eventually periodic. Proving that this periodic path is the REAL greedy path AND starts at the root `a_1` is exactly the content of B2 (empty pre-period). The skeleton's step 7 mechanism — "if the infinite path is a single cycle whose node-type is the root-type, then periodicity holds from n=1" — requires proving the root lies on the cycle, not in a tail. That is:
- in the greedy-prefix tree: the single path IS from the root by definition, but periodicity of that path is unproved (= B1, Answer 1). "From-n=1" is then a corollary of B1, not of compactness.
- in the consistent-prefix tree: the periodic path need not pass through the root at all (the `(1,3)` paths start `(15,21,…)` — they DO share the root `15`, but with a different period; a generic periodic path in the consistent tree could start at any `b_1≡a_1 mod M`, not necessarily `a_1` itself).

There is no real argument that compactness places the root on the cycle. This is B2 restated, not a free corollary. The round-1 proof-reviewer already noted B2 is a separate gap (per the `bijection-from-n1` diagnostic); compactness does not dissolve it.

---

### Answer 5 — Empirical residue-history tree depth and branching (a_1=15, M=15).

- Real greedy sequence (60 terms): period `T=8`, `L=30`, **from n=1** (verified: `a[8]=45=a[1]+30`, `a[0+8]=a[0]+30`). Diffs `[3,2,4,6,6,4,2,3]` repeating, max diff `6 ≤ R=15`.
- Residues mod 15 (first 40): `[0,3,5,9,0,6,10,12,0,3,5,9,0,6,10,12,…]` — periodic with `T=8`, but ONLY because `15 | 30`; the residue periodicity is a shadow of value-periodicity, not an independent certificate.
- **Branching of the consistent-prefix tree at the root:** admissible continuations of `[15]` in `(15,60)` = 20 values (18,20,21,24,25,27,30,33,35,36,39,40,42,45,48,50,51,54,55,57). Each extends to an infinite valid greedy-continued sequence (bounded-diff guarantees no stuck). So the root has ≥20 children, ALL extending to infinite paths. **The "unique infinite path" picture fails empirically and dramatically.**
- Same residue, different future (decisive): residue `0 mod 15` at value `30` yields next residue `10` (real greedy, past `[15,18,20,24,30]`) vs. next residue `3` (path `[15,21,24,27,30]`, past `[15,21,24,27]`). The transition is history-dependent.
- Alternative periodic paths through the consistent tree: `(15,21,…)→(T=1,L=3)`, `(15,25,…)→(T=1,L=5)`, `(15,30,…)→(T=1,L=3)`, `(15,20,…)→(T=8,L=30)` — distinct from the real greedy and from each other.

The "unique infinite path" picture does NOT hold empirically. The consistent tree is a thicket of rival periodic paths; the greedy is one leaf, not a distinguished spine.

---

### Distinct openings (for the outliner)

- **Opening A (cheap, negative): use this route's failure as a diagnostic.** The verified fact "residue mod M does not determine the next residue" (Answer 1/5 data) is a reusable negative lemma: NO route that works purely mod a fixed modulus `M` can prove periodicity without enriching the state to the support family. This kills any future "residue-only" bypass and sharpens B1 as the genuine obstruction. Record it.
- **Opening B (positive, borrowed): the support-family IS the finite state — embrace it directly.** The König route's only salvageable contribution is that the state `(residue mod L_0, support-family F_∞)` is finite and the transition on it is eventually a single cycle (via the certified cyclic-successor theorem). That is exactly `bounded-diff-finite-state`'s conditional spine. The outliner should NOT pursue a separate König approach; it should fold the one salvageable idea (finite-state ⇒ eventually periodic) INTO `bounded-diff-finite-state` and attack B1 directly with a new mechanism.
- **Opening C (genuinely different framing, NOT König): direct attack on the free-rider-shortcut sub-gap.** The empirical fact that free-rider primes `> R` (17,19,23,29,31,37 for a_1=15) ALWAYS appear alongside a kernel prime, never as the sole shortcut below the small-prime candidate, suggests a `v_p`-counting or size argument: a candidate `m ∈ (a_n, a_n+R]` carrying a free-rider `q>R` can hit only the past terms divisible by `q` (a set not cofinal in the support family), so it cannot be the greedy least. This is the real crux; it is NOT a compactness move.

### Candidate technique(s)
- König's lemma / finite-branching tree (applies, but only gives an infinite path — insufficient).
- "Finite directed graph ⇒ eventually periodic walk" (the move the route NEEDS, but it requires a deterministic finite state = B1's support family; not genuinely available without B1).
- No genuine compactness bypass of B1 exists on this problem.

### Cheap-kill candidates
- The empirical demonstration "same residue, different next residue" (a_1=15, residue 0 mod 15 → next 10 vs 3) is a one-line structural refutation of any residue-only finite-state claim. Use it to prune any future residue-mod-M bypass.

### Knowledge-base entries to use
- `Pigeonhole / extremal principle` (the "monotone sequence in a finite poset stabilizes" = Lemma 3, already certified).
- `Invariants & monovariants` (the bounded-diff lemma is a local bound, not a monovariant; do not mislabel).
- `Induction / infinite descent` (the support-family stabilization is a finite-poset descent).
- No KB entry for König's lemma or compactness exists; the corpus has no compactness crux for sequence-periodicity problems (see below).

### Analogous past problems (cruxes)
- **None genuinely analogous.** The crux corpus has NO König's-lemma / compactness / finite-branching-tree crux for sequence-periodicity problems. The closest retrievals:
  - `aimo-0077` (combinatorics, extremal-principle): "finite state space ⇒ non-ending game repeats a state ⇒ periodic cycle." This is the standard finite-state-⇒-periodic move, which the König route NEEDS but can only get via B1's support family — i.e., it confirms the collapse, not a bypass.
  - `aimo-0126` (combinatorics, invariants): permutation cycles on `Z/2025` with bounded steps ⇒ net displacement zero per cycle. Finite-state cycle argument; same flavor, no compactness bypass.
  - `aimo-0171` (number theory, modular arithmetic): "iteratively jump to the nearest later index closing a zero-residue window; step bounded by period." A walk-with-bounded-steps argument, but on a FINITE cyclic group, not an infinite König tree.
  None is a genuine analog to "infinite path in an infinite finitely-branching tree ⇒ eventual periodicity of a greedy integer sequence." Do not force a match.

### Prior progress
- Certified lemmas `bounded-difference`, `universal-small-prime`, `periodic-set-iteration` (cyclic-successor theorem) all stand and are imported by this route.
- The route's skeleton (round 1 seed) correctly flagged steps 3 and 7 as the gamble. This scout confirms both fail: step 3 collapses to bounded-diff-finite-state's Lemma 3; step 7's uniqueness is false (consistent tree) or vacuous (greedy tree).
- Round-1 proof-reviewer already refuted the profinite-compactness bypass (in `periodic-set-iteration`) and the injectivity bypass (in `bijection-from-n1`); this König route is a third bypass attempt that fails for the same root reason (no finite deterministic state without B1).

### Dead ends (do not retry)
- **Residue-mod-M finite branching as a B1 bypass.** Refuted: residue does not determine the next residue (empirical counterexample above). Finite branching (König) holds, but finite node-types-with-deterministic-transitions does not, without the support family.
- **"Greedy path = unique infinite path" (step 7).** Refuted in both tree interpretations: greedy-prefix tree is a single path (König vacuous, uniqueness trivial, periodicity still = B1); consistent-prefix tree has many periodic infinite paths with different (T,L) (uniqueness false).
- **Profinite compactness in `Ẑ` (already refuted round 1, `periodic-set-iteration` Step 3).** `Â_∞` is closed-not-open, need not contain a genuine integer, orbit not contained. Do not re-raise.
- **Injectivity-on-residues bypass (already collapsed round 1, `bijection-from-n1`).** Transition not well-defined until admissible set is periodic mod L = B1.

### Small-case / intuition notes (conjecture, labeled as such)
- a_1=15: real greedy has (T=8, L=30), periodic from n=1. Consistent tree has rival paths with (T=1,L=3), (T=1,L=5), (T=8,L=30), and a long-transient path from (15,35). The real greedy is NOT distinguished by uniqueness.
- The modulus that works is `L=30=2·rad(15)` (kernel product), NOT `R=15` and NOT `∏_{p≤15}p=30030`. Residue periodicity mod 15 is a consequence, not a cause.
- Conjecture (unproved, shared): B1+B2 hold in every tested case. No new evidence from the König angle.

### Recommended next step
**Do not advance `compactness-konig-branch` as a distinct approach.** Send it back to the outliner with the verdict: collapses into `bounded-diff-finite-state` (the only finite deterministic state is the support family = Lemma 3 = B1's machinery). The route's one salvageable idea — "finite state ⇒ eventually periodic via the cyclic-successor theorem" — is already present in `bounded-diff-finite-state`'s conditional spine. Instead, the outliner should open a genuinely different framing that attacks the free-rider-shortcut sub-gap (B1) directly: a `v_p`-counting / size argument showing a free-rider prime `q>R` in a candidate `m ∈ (a_n, a_n+R]` cannot be the sole shortcut below the small-prime candidate, because `q` hits only a non-cofinal slice of the support family. That is the real crux, and it is not a compactness move.
