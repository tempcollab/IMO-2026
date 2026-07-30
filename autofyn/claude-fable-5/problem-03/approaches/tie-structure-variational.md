# Approach: tie-structure-variational

## Status
partial

## Approaches tried
- (round 1, outline) Skeleton laid down; nothing certified. Anchors: at the dyadic optimum, Xiang's numerically-optimal replies are all tie-creating ("mirror ladder", "bisect top", "shave to match") and three structurally different replies attain the same value 4/7 at n=2 — evidence that optima live on tie strata.
- (round 1, build) **GAP T closed** — replaced the iterative "slide to nearest boundary" argument (cycling risk flagged by the outline-reviewer) with a **static LP/vertex argument**: Xiang's value function is affine on the cells of the tie-hyperplane arrangement, so a minimizer exists at an arrangement vertex, where the cuts are pinned by independent tie equations. No sliding, no monovariant, no cycling — the lemma is now fully rigorous (§3 below). Also proved: the greedy-claiming lemma + Stackelberg reduction (written to `lemmas/greedy-claiming.md`), a layer-cake parity identity for the odd-rank sum (§4), the exact mirror-ladder computation V(a*) ≤ c(n) for all n (§5), and a complete end-to-end solve of n = 1 through the catalog pipeline, giving c(1) = 2/3 rigorously (§6).
- (round 2, outline revision) **Old outer-sup route retired** per the §8 kill criterion, half-fired: GAP M(a) is moot (import `lemmas/ladder-resists.md`, certified) and GAP M(b) is confirmed same-wall duplication of the induction siblings' casework. GAP C in its old form (catalog over Liu partitions for general n) is abandoned with it. The slug is **re-targeted** at the field's single remaining gap — Claim U(m) — via a static pinned-catalog analysis of the *fixed-multiset subgame*; see "Route v2" at the end of this file. The certified infrastructure (V1–V4, Lemma G, layer-cake) all carries over.
- (round 1, build) Two routes attempted and **failed** on the remaining gaps, recorded so they are not retried: (a) *parity-XOR induction on the top rung* for the ladder lower bound: Δ = ∫(π_top ⊕ π_low) and the XOR cancellation is exactly what Xiang's mirror reply exploits, so no termwise bound of the form Δ ≥ Δ_low − (something small) survives; the bound Δ ≥ |Δ_top − Δ_low| is true but |Δ_top − Δ_low| ≥ 1 unit has no real-valued proof (it would need integrality). (b) *Integrality of pinned replies*: FALSE — cutting a rung of size 4 units into three equal sub-pieces 4/3 is a legal pinned (vertex) reply with non-integral sub-pieces; any argument assuming pinned sub-pieces are integer multiples of the unit is unsound.

## Current best

Rigorously established this round (details in the numbered sections below):

1. **Lemma G + Corollary R** (`lemmas/greedy-claiming.md`): the claiming phase has exact value = odd-rank sum for Liu Bang, and c(n) = sup_a inf_x odd(S(a,x)) over size multisets only.
2. **Tie-Structure Lemma (V1–V3, §3)**: for every Liu partition a, Xiang's infimum is attained, and it is attained at a reply in which all sub-pieces are positive and the M ≤ n cut positions are pinned by M linearly independent equations, each of the form "two sub-pieces are equal" or "a sub-piece equals an uncut Liu piece". Hence V(a) is a minimum over a **finite catalog** of affine functionals of a (Corollary V4). This was GAP T; it is closed, in a stronger (static) form than outlined.
3. **Layer-cake parity identity (§4)**: Liu's value = 1/2 + Δ/2 where Δ = Lebesgue measure of {t > 0 : #(pieces ≥ t) is odd}. Free consequence: Liu always gets ≥ 1/2.
4. **Mirror-ladder computation (§5)**: against the dyadic ladder a*, Xiang's mirror reply yields exactly 2^n/(2^{n+1}−1); hence V(a*) ≤ c(n) — the construction cannot give more than the conjectured value.
5. **n = 1 solved end-to-end (§6)**: the pipeline (V1–V4 catalog + outer maximization) yields c(1) = 2/3 with full rigor — both bounds — validating the framing on the smallest case.

**Open gaps (named, precise):**
- **GAP C** (catalog organization): Corollary V4 gives a finite catalog for each fixed n, but no explicit, recursively organized enumeration of the feasible pinned types for general n. Without it, Steps §7a/§7b cannot be executed for general n.
- **GAP M(a)** (ladder lower bound): every pinned reply against a* has value ≥ 2^n/(2^{n+1}−1), i.e. V(a*) ≥ c(n). Open.
- **GAP M(b)** (outer bound): V(a) ≤ c(n) for every a. Open here; note this overlaps the induction sibling's Cases A–D, and per the kill criterion this slug must NOT duplicate that casework — see §8 for the honest overlap assessment.

---

# The build (round 1)

Throughout, **units**: u := 1/(2^{n+1}−1), and the target value is c(n) := 2^n·u = 2^n/(2^{n+1}−1). "odd(S)" denotes the odd-rank sum of a finite multiset S of nonnegative reals sorted in decreasing order (well-defined under ties: permuting equal values permutes equal summands). Final answer claimed: **c(n) = 2^n/(2^{n+1}−1)** (verified below at n = 1 rigorously and consistent with the exact mirror-ladder value for all n; not yet proved for general n).

## §1. Imported infrastructure

**Lemma G (greedy claiming)** and **Corollary R (multiset/Stackelberg reduction)** — proved in full in `results/imo-2026-03/lemmas/greedy-claiming.md` (written by this builder this round; pending certification). Statement of R, which fixes all notation:

$$c(n) = \sup_{a}\ \inf_{x}\ \mathrm{odd}(S(a,x)),$$

where a = (a₁ ≥ … ≥ a_k > 0), k ≤ n+1, Σa_j = 1 is Liu's partition; a reply x consists of cut counts m_j ≥ 0 with Σ_j m_j ≤ n and positions 0 < x_{j,1} < … < x_{j,m_j} < a_j inside piece j; S(a,x) is the multiset of all resulting sub-piece sizes.

Also imported from that file: **zero-padding is harmless** — adding size-0 entries to a multiset changes odd(·) by nothing (positive entries keep their ranks; zeros contribute 0 regardless of parity).

## §2. Compactification (Lemma V1)

Fix a. For a cut-count vector m = (m₁,…,m_k) with M := Σ m_j, define the compact convex polytope

$$D_m := \prod_{j=1}^{k}\ \{\,0 \le x_{j,1} \le \dots \le x_{j,m_j} \le a_j\,\} \subset \mathbb{R}^M,$$

and the **size functions**: for each piece j, s_{j,0}(x) = x_{j,1}, s_{j,i}(x) = x_{j,i+1} − x_{j,i} (1 ≤ i ≤ m_j−1), s_{j,m_j}(x) = a_j − x_{j,m_j}; if m_j = 0 the single size function is the constant s_{j,0} ≡ a_j. There are P := Σ_j (m_j + 1) size functions, each affine in x, and D_m = {x : s_α(x) ≥ 0 for all α}. Let f(x) := odd(S(x)) where S(x) is the multiset of all P values (zeros allowed).

**Lemma V1.** (a) f is continuous on D_m. (b) With V(a) := min over cut-count vectors m with Σ m_j = n of min_{D_m} f, we have inf over all legal replies x (all cut counts ≤ n) of odd(S(a,x)) = V(a), and the minimum is attained.

*Proof.* (a) The r-th largest entry of a vector u ∈ ℝ^P is s_r(u) = max_{|I|=r} min_{i∈I} u_i, a maximum of minima of coordinates, hence 1-Lipschitz for the sup-norm; f is the sum of the odd-indexed such functions composed with the affine map x ↦ (s_α(x))_α, hence continuous (indeed piecewise affine and Lipschitz).

(b) Two directions. (⊇) Every point x ∈ D_m determines a *legal* reply with the same value: delete every degenerate cut (a cut coincident with another cut or with a piece endpoint corresponds to a size-0 sub-piece); the resulting multiset is S(x) minus some zero entries, so by zero-padding harmlessness its odd(·) equals f(x); the remaining cuts are strictly increasing and interior, hence legal with ≤ M ≤ n cuts. So min_m min_{D_m} f ≥ inf over legal replies. (⊆) Every legal reply with M′ ≤ n cuts appears as a point of D_m for the composition m obtained by adding n − M′ extra cuts at position 0 in piece 1 (a boundary point of D_m), again with equal value by zero-padding. So the inf over legal replies ≥ min_m min_{D_m} f. Both minima exist: finitely many m; each D_m compact, f continuous. ∎

## §3. The Tie-Structure Lemma (GAP T — closed)

Fix a and m as above; M = Σ m_j. Consider the finite family of affine functions on ℝ^M:

$$\mathcal{A} := \{\, s_\alpha - s_\beta \,:\, \alpha \ne \beta \,\} \cup \{\, s_\alpha \,:\, \alpha \,\},$$

and let 𝒜* ⊂ 𝒜 be those members that are not identically zero and not a nonzero constant. (A member is a nonzero constant only when it compares two uncut pieces of different sizes, or is an uncut piece itself; it is identically zero only when it compares two uncut pieces of equal size.) The **arrangement** is the finite union of hyperplanes {g = 0}, g ∈ 𝒜*.

**Lemma V2 (vertex form of tie-structure).** min_{D_m} f is attained at a point x* at which there are M linearly independent active equations, each of one of the forms
 (i) s_α(x*) = 0 for some sub-piece α of a cut piece;
 (ii) s_α(x*) = s_β(x*) for two distinct sub-pieces of cut pieces (in the same piece or in different pieces);
 (iii) s_α(x*) = a_l for a sub-piece α of a cut piece and an uncut piece l.

*Proof.* **Step 1 (cells).** Let U₁,…,U_q be the connected components of ℝ^M \ ∪_{g∈𝒜*}{g = 0}, and let C_i := cl(U_i) ∩ D_m. Each C_i is a compact convex polytope (an intersection of finitely many closed half-spaces — the sign conditions ±g ≥ 0 that define cl(U_i), which are constant-sign on the open component — with the compact polytope D_m). The C_i cover D_m: the union of the cl(U_i) is closed and contains the dense set ℝ^M \ ∪{g=0}, hence is all of ℝ^M.

**Step 2 (f is affine on each cell).** On U_i, every g ∈ 𝒜* has a constant strict sign, and the members of 𝒜 \ 𝒜* have constant sign trivially. Hence for every pair α, β the relation between s_α(x) and s_β(x) (<, =, >) is the same for all x ∈ U_i: a constant weak order on the P size functions. Choose any permutation σ of {1,…,P} consistent with this weak order (largest first). Then for all x ∈ U_i, (s_{σ(1)}(x), …, s_{σ(P)}(x)) is the sorted list of S(x), so

$$f(x) = \sum_{r \text{ odd}} s_{\sigma(r)}(x),$$

an affine function of x (independent of how ties inside the weak order were broken, since tied positions carry equal values). By continuity of f (Lemma V1a) the same affine formula holds on C_i = cl(U_i) ∩ D_m.

**Step 3 (LP vertex principle).** f attains its minimum over D_m on some cell C_i (finitely many cells covering a compact set), and an affine function on a compact convex polytope attains its minimum at an extreme point (fundamental theorem of linear programming: the minimum over a polytope of an affine functional is attained at a vertex; knowledge base, "Extremal principle"). Let x* be such a vertex of C_i achieving min_{D_m} f.

**Step 4 (reading off the active equations).** C_i ⊂ ℝ^M is defined by the affine inequalities: s_α ≥ 0 (all α), and ±g ≥ 0 for g ∈ 𝒜* (with signs given by U_i). A vertex of a polyhedron in ℝ^M is a face of dimension 0, i.e. a point where the active constraints (those holding with equality) contain M with linearly independent linear parts. Each active constraint is of the form s_α(x*) = 0 or s_α(x*) = s_β(x*). Classify: if both α, β are uncut pieces, the function is constant — either never zero (excluded from 𝒜*) or identically zero (excluded from 𝒜*), so this form does not occur among active members of 𝒜*; if exactly one of them is an uncut piece l, the equation reads s_α(x*) = a_l — form (iii); if both are sub-pieces of cut pieces — form (ii). And s_α(x*) = 0 with α an uncut piece is impossible (a_l > 0), so any active s_α = 0 is form (i). ∎

**Lemma V3 (nondegenerate pinned minimizer).** There exist a cut-count vector m with M := Σ m_j ≤ n and a minimizer x* ∈ D_m with f(x*) = V(a) such that **all P sub-pieces are strictly positive** and the cut positions satisfy M linearly independent active equations of forms (ii)–(iii) only.

*Proof.* Among all cut-count vectors m′ with Σ m′_j ≤ n and min_{D_{m′}} f = V(a) (a nonempty finite set by Lemma V1b — note min_{D_{m′}} f for Σ m′_j < n also occurs as a boundary value inside a larger D_m, and directly: D_{m′} is itself a legal reply space), choose m with Σ m_j =: M minimal. Apply Lemma V2 to this m to get a vertex minimizer x* with M independent active equations of forms (i)–(iii). Suppose some equation of form (i) is active, i.e. some sub-piece s_{j,i}(x*) = 0. Deleting the corresponding cut (one of the coincident marks, or the mark sitting at the piece endpoint) produces a point x′ ∈ D_{m''} with Σ m″_j = M − 1 whose multiset is S(x*) minus one zero entry, so f(x′) = f(x*) = V(a) by zero-padding harmlessness — contradicting the minimality of M. Hence no form-(i) equation is active at x*; in particular every s_α(x*) > 0 (an inactive constraint s_α ≥ 0 is strict), and the M independent active equations are all of forms (ii)–(iii). ∎

**Remark (why this closes GAP T, cycle-free).** The outline proposed an iterative slide-to-nearest-tie with a ties-count monovariant; the outline-reviewer flagged re-sorting/cycling. Lemmas V2–V3 obtain a *stronger* conclusion (all M cuts simultaneously pinned by an independent tie system, not merely each cut adjacent to one tie) with no iteration at all: the minimizer is a vertex of one cell of a fixed hyperplane arrangement. Nothing moves, so nothing can cycle.

**Corollary V4 (finite catalog in principle).** Call a **pinned type** τ the combinatorial data: (m; a set E of M equations of forms (ii)–(iii) with linearly independent linear parts; the weak order of the P size values). For fixed τ, the M equations in the M unknowns x have a unique solution x_τ, and both x_τ and the value f_τ := f(x_τ) are affine functions of (a₁,…,a_k) with coefficients determined by τ alone (solve the linear system; the right-hand sides are ℤ-combinations of the a_j; then f_τ is the odd-rank sum read off the weak order). Say τ is *feasible at a* if x_τ ∈ D_{m} and the size values at x_τ realize the weak order of τ. Then by Lemma V3,

$$V(a) = \min\{\, f_\tau(a) \,:\, \tau \text{ feasible at } a \,\},$$

a minimum over a finite (n-dependent) set of affine functionals. ∎

*What is still missing here is not finiteness but organization:* an explicit, recursively structured enumeration of the feasible types for general n, tight enough to run the outer optimization. That is **GAP C** (see §8).

## §4. Layer-cake parity identity (free reformulation)

**Lemma D.** Let S be a finite multiset of nonnegative reals with sum T, and for t > 0 let N(t) := #{s ∈ S : s ≥ t}. Then

$$\mathrm{odd}(S) = \frac{T}{2} + \frac{\Delta(S)}{2}, \qquad \Delta(S) := \lambda\big(\{t > 0 : N(t) \text{ is odd}\}\big),$$

where λ is Lebesgue measure. In particular odd(S) ≥ T/2 always.

*Proof.* Sort S as s₁ ≥ … ≥ s_P ≥ 0. For t > 0 the elements ≥ t are exactly those of ranks 1,…,N(t); hence #{r odd : s_r ≥ t} = ⌈N(t)/2⌉. By the layer-cake formula for each term, s_r = λ((0, s_r]) = ∫₀^∞ 1[s_r ≥ t] dt, so

$$\mathrm{odd}(S) = \int_0^\infty \#\{r \text{ odd}: s_r \ge t\}\,dt = \int_0^\infty \Big\lceil \tfrac{N(t)}{2} \Big\rceil dt, \qquad T = \int_0^\infty N(t)\,dt,$$

both integrals finite (integrands vanish for t > s₁ and are bounded by P). Since ⌈N/2⌉ − N/2 = ½·1[N odd] pointwise, subtracting gives odd(S) − T/2 = ½ ∫ 1[N(t) odd] dt = Δ(S)/2. ∎

(Verified computationally on 200 random rational multisets in exact arithmetic — a check, not a proof step; the proof above stands alone.)

**Consequence for the problem** (with T = 1): Liu's value against reply x is ½ + Δ(S(a,x))/2, so the target claims become: *(upper)* for every a, Xiang has replies making Δ arbitrarily close to (or equal to) u; *(lower)* every ≤ n-cut refinement of the dyadic ladder has Δ ≥ u. This Δ coincides with the discrepancy of the sibling approach `discrepancy-halving` (Liu − Xiang); the derivation here is independent and the ⌈N/2⌉ form is what the variational analysis of §3 naturally measures (parity of N(t) flips exactly at un-tied values — ties are parity-transparent).

## §5. The dyadic ladder and the mirror reply: V(a*) ≤ c(n)

**Definition.** The dyadic ladder is a* := (2^n u, 2^{n−1} u, …, 2u, u), i.e. a_j = 2^{n+1−j} u for j = 1,…,n+1. It is a legal Liu partition: n+1 positive parts summing to (2^{n+1} − 1)u = 1, using exactly n marks.

**Proposition M (mirror-ladder value).** Against a*, the Xiang reply "cut the top rung 2^n u into sub-pieces 2^{n−1}u, 2^{n−2}u, …, 2u, u, u" (n cuts, n+1 sub-pieces) is legal and yields Liu exactly 2^n u = c(n). Hence V(a*) ≤ c(n): the conjectured value is an upper bound for what the ladder guarantees.

*Proof.* Legality and count: the sub-pieces are n+1 positive reals with sum (2^{n−1} + ⋯ + 2 + 1)u + u = (2^n − 1)u + u = 2^n u, the size of the top rung, so they are produced by n interior cuts of that rung.

*Case n = 1:* the ladder is (2u, u); the reply cuts 2u into (u, u); final multiset {u, u, u}; odd-rank sum = 2u = c(1) = 2/3. ✓

*Case n ≥ 2:* the final multiset consists of the untouched rungs {2^{n−1}u, …, 2u, u} together with the sub-pieces {2^{n−1}u, …, 2u, u, u}; in units, that is the multiset with **two** copies of 2^k for each k = 1, …, n−1 and **three** copies of 1. Sanity: cardinality 2(n−1) + 3 = 2n+1 ✓; sum 2(2^n − 2) + 3 = 2^{n+1} − 1 ✓. Sort decreasingly: for k = n−1 down to 1, the two copies of 2^k occupy ranks 2(n−1−k)+1 and 2(n−1−k)+2 (proof: exactly the values 2^{n−1},…,2^{k+1}, i.e. 2(n−1−k) entries, are strictly larger); the three copies of 1 occupy ranks 2n−1, 2n, 2n+1. The odd ranks are therefore: one copy of each 2^k (k = 1,…,n−1) — ranks 2(n−1−k)+1 — and two copies of 1 — ranks 2n−1 and 2n+1. Liu's odd-rank sum in units:

$$\sum_{k=1}^{n-1} 2^k + 2 = (2^n - 2) + 2 = 2^n.$$

So Liu receives exactly 2^n u = c(n). (Checked in exact rational arithmetic for n = 1,…,8 — a check only.) Since V(a*) is the infimum over Xiang's replies and this reply is legal, V(a*) ≤ c(n). ∎

Via Lemma D this reply achieves Δ = u exactly: N(t) is odd only for t ∈ (0, u] (there N = 2n+1; on (2^k u, 2^{k+1}u] for k ≥ 1... more simply, above u all values come in the pairs listed plus one levelled triple whose first two members change N by 2 at a time except across the value 1). We do not rely on this remark.

**Tie anatomy of the mirror reply** (motivation for the equalizer conjecture, not used as a proof step): all n cuts are pinned — n−1 sub-pieces satisfy form-(iii) ties (equal to the uncut rungs 2^{n−1}u,…,2u,u) and the last two satisfy one form-(iii) tie (= u) and one form-(ii) tie (the two u sub-pieces equal); the ladder is characterized by the exact identities a₁ = 2a₂ and a₁ = (1 − a₁) + a_{n+1}, which make "bisect the top" and "mirror the ladder" tie at the same value — the equalizing structure the outer optimization (GAP M(b)) should certify.

## §6. n = 1 solved end-to-end through the pipeline: c(1) = 2/3

This section runs §1–§3 to completion for n = 1, with no numerics. Liu's partition: a = (a₁, a₂), a₁ ≥ a₂ ≥ 0, a₁ + a₂ = 1 (a₂ = 0 means Liu made no cut; then piece 2 does not exist). Xiang has at most one cut. We enumerate the pinned replies of Lemma V3 exhaustively — for M ≤ 1 the catalog is tiny, and V1–V3 guarantee it suffices to consider exactly these:

- **M = 0** (no cut): S = {a₁, a₂}, value odd = a₁.
- **M = 1, cut in piece 1** (sub-pieces s and a₁ − s, one pinning equation required):
  - form (ii): s = a₁ − s, i.e. s = a₁/2. S = {a₁/2, a₁/2, a₂}. A 3-element multiset has odd ranks 1 and 3, so odd = max + min = a₁/2 + a₂ = 1 − a₁/2 (whichever of a₁/2, a₂ is larger, the sum of largest and smallest is a₁/2 + a₂).
  - form (iii): s = a₂ or a₁ − s = a₂ (same reply up to reflection; feasible iff a₂ ≤ a₁... indeed a₂ ≤ a₁ always, and a₂ > 0). S = {a₁ − a₂, a₂, a₂}; odd = max + min = (a₁ − a₂) + a₂ = a₁ if a₁ − a₂ ≥ a₂; otherwise sorted (a₂, a₂, a₁ − a₂) gives odd = a₂ + (a₁ − a₂) = a₁. Either way, value a₁.
  - (Form (i) equations are excluded by Lemma V3; they reproduce the M = 0 value a₁ anyway.)
- **M = 1, cut in piece 2** (exists only if a₂ > 0; sub-pieces s, a₂ − s):
  - form (ii): s = a₂/2. S = {a₁, a₂/2, a₂/2}; since a₁ ≥ a₂ > a₂/2, odd = max + min = a₁ + a₂/2 ≥ a₁.
  - form (iii): s = a₁ requires a₁ ≤ a₂, hence a₁ = a₂ = 1/2 and s = 1/2 = a₂ — then the other sub-piece is 0, which is a form-(i) degeneracy excluded by V3 (its value equals the M = 0 value a₁).

By Lemma V3, V(a) is the minimum of the listed pinned values:

$$V(a) = \min\big(a_1,\ 1 - \tfrac{a_1}{2},\ a_1 + \tfrac{a_2}{2}\big) = \min\big(a_1,\ 1 - \tfrac{a_1}{2}\big).$$

(The k = 1 case a = (1) is the sub-case a₂ = 0: V = min(1, 1/2) = 1/2.)

**Outer maximization.** For a₁ ∈ [1/2, 2/3]: 1 − a₁/2 ≥ 1 − 1/3 = 2/3 ≥ a₁, so V(a) = a₁ ≤ 2/3, with equality iff a₁ = 2/3. For a₁ ∈ [2/3, 1]: V(a) = min(a₁, 1 − a₁/2) ≤ 1 − a₁/2 ≤ 2/3, with equality iff a₁ = 2/3. Hence

$$c(1) = \max_a V(a) = \tfrac{2}{3}, \text{ attained uniquely at } a = (\tfrac23, \tfrac13),$$

and 2/3 = 2¹/(2² − 1) verifies the claimed formula at n = 1: the **lower bound** (Liu plays (2/3, 1/3); every Xiang reply gives ≥ 2/3, because by V1–V3 the infimum equals the catalog minimum, which is min(2/3, 1 − 1/3) = 2/3) and the **upper bound** (any a: V(a) ≤ 2/3) are both fully proved. ∎

This validates the pipeline: the tie-structure lemma plus catalog enumeration plus outer maximization is a complete and rigorous method at n = 1. (A brute-force numeric sweep over cut placements matched min(a₁, 1 − a₁/2) at 8 values of a₁ — a check only.)

## §7. What a complete general-n proof along this route requires

**§7a (lower bound, GAP M(a)).** By V1–V3, V(a*) ≥ c(n) reduces to: *every pinned reply against the ladder has odd-rank value ≥ 2^n u.* Pinned replies against a* are strongly constrained (each cut participates in an independent tie system anchored at the rung values 2^k u), but the tie systems can force non-integral sub-pieces (the 4 → 4/3+4/3+4/3 example above), so no integrality shortcut exists; an argument on the structure of the tie graph (components anchored at rungs vs. free equal-blocks) is needed. **Open.**

**§7b (upper bound, GAP M(b)).** By V4 it suffices to exhibit, for each non-ladder a, a feasible pinned type τ with f_τ(a) ≤ c(n), and to organize the smoothing rung-by-rung (if a₁ > 2a₂ bisecting the top beats c(n); if a₁ < the mirror-anchored threshold, a mirror-type entry beats it; recurse down). **Open**, and dangerously close to the induction sibling's Cases A–D — see §8.

## §8. Honest overlap assessment (the kill criterion)

The outline-reviewer's condition: if the catalog explodes into the induction approach's casework, declare this slug a dead end rather than duplicate. Round-1 verdict: **not yet a dead end, but the risk is confirmed for GAP M(b)**. The genuinely variational asset produced this round is the Tie-Structure Lemma (V2/V3): it is *static, exact, and applies to every Liu partition*, and it is precisely the tool the siblings lack for their lower-bound gaps (dyadic-recursion's G1 and discrepancy-halving's GAP L both need "only structured Xiang replies matter against the ladder" — V3 supplies exactly that, reviewer-checkable and importable). If next round's work on §7a still bottoms out on the same accounting wall as G1/GAP L, and §7b remains only executable as the induction's A–D casework, this slug should be folded into the siblings (donating V2/V3 and Lemma D) and retired. Recommendation to the outline-reviewer: treat V2/V3 and Lemma D as field-level infrastructure regardless of this slug's fate.

## Cases to cover (unchanged plan items for the remaining gaps)
- Liu using k < n+1 parts in §7b (spare Xiang cuts: handled in principle by V1's compactification — extra cuts at boundary cost nothing).
- Equal Liu pieces (aᵢ = aᵢ₊₁): expected to die early in §7b via a match-and-shave pinned entry forcing ≈ 1/2; not yet written.
- Hybrid pinned types with cuts in several pieces (§7a): the tie graph may connect sub-pieces across pieces; must be covered by the eventual catalog organization.

## Promotable lemmas

1. **greedy-claiming** (Lemma G + Corollary R) — proved in full in `results/imo-2026-03/lemmas/greedy-claiming.md` (this round, this builder). Ready for certification; all three approaches import it.
2. **Tie-Structure Lemma (V1–V3 + Corollary V4)** — proved in full in §2–§3 of this file. Statement worth caching: *for every Liu partition a, Xiang's optimal reply may be taken with all sub-pieces positive and all cut positions pinned by Σm_j linearly independent equations of the forms "sub-piece = sub-piece" or "sub-piece = uncut piece"; hence V(a) is a minimum of finitely many affine functionals of a.* Directly importable by the siblings for their lower-bound gaps (G1, GAP L).
3. **Layer-cake parity identity (Lemma D)** — proved in full in §4. *odd(S) = T/2 + ½·λ{t : N(t) odd}.* Equivalent to (and an independent derivation of) the discrepancy identity used by `discrepancy-halving`; suggest certifying once for the field.
4. **Mirror-ladder value (Proposition M)** — proved in full in §5: the dyadic ladder concedes exactly c(n) to the mirror reply, so V(a*) ≤ c(n) for all n ≥ 1.

---

# Route v2 (round-2 revision, outliner) — static pinned-catalog proof of U(m)

**Target (whole problem):** c(n) = 2^n/(2^{n+1}−1). Lower bound: import `lemmas/ladder-resists.md` (certified). Upper bound: import the reduction Target U ⟸ U(n+1) (being certified by the discrepancy-halving builder as `lemmas/reduction-to-um.md`), then prove **Claim U(m)** — for any multiset A = {a₁ ≥ … ≥ a_m ≥ 0}, T = ΣA, β = T/(2^m−1), Xiang can reach Δ ≤ β with ≤ m−1 cuts — by a **static LP/vertex argument on the fixed-multiset subgame**, not by move-process induction. This is the field's only non-move-process framing.

## Skeleton

1. **Subgame setup.** Fix m and A. Xiang's reply space = allocations of ≤ m−1 cuts with real positions inside pieces; Δ(final multiset) is piecewise-linear in the cut positions (same cell decomposition as certified V2).
2. **Pinning (port of V2/V3).** The minimum of Δ over the reply polytope is attained at a reply where every cut is pinned by tie equations — each sub-piece tied to another sub-piece or an uncut piece. V3's cut-count-minimality argument transfers verbatim; cite `lemmas/tie-structure.md`.
3. **Ternary structure theorem (make-or-break).** Classify pinned optima: the tie-graph components are anchored at the values a₁,…,a_m; show every pinned optimal reply is equivalent to a ternary matching structure — each piece carries a coefficient c_i ∈ {−1, 0, +1} (fully matched into ties across pieces = ±1 canceling; deleted by internal self-ties/bisection = 0; residual carrier) and the pinned value is |Σ c_i a_i|. Mechanism: a tie component's sub-pieces are equal by value, so its Δ-contribution telescopes. (Round-2 numerics, outliner: min over admissible c of |Σca| ≤ 0.80β on 8600+ random Case-3 instances; exhaustive move search attains the ternary optimum on 120/120 instances — the classification is numerically watertight.)
4. **Catalog bound.** Prove min over admissible c (≥1 nonzero; mixed signs if ≥2; realizable) of |Σ c_i a_i| ≤ β — NOT by per-region casework but by an averaging/exchange or LP-duality argument over the finite type family, exploiting the middle-regime slack (only Cases 1/2 of U(m) are tight, and those are already proved by moves and importable from `lemmas/um-easy-cases.md` once certified).
5. **Combine.** U(m) for all m ⟹ upper bound ⟹ c(n) = 2^n/(2^{n+1}−1); verify at n = 1 (§6 already does this end-to-end).

## Open gaps (v2)
- **GAP S (structure theorem, step 3).** The classification of pinned subgame optima into ternary matching structures.
- **GAP B (catalog bound, step 4).** The averaging/duality proof that some admissible c has |Σca| ≤ β outside the already-proved boundary cases.

## Kill criterion (v2)
If by end of next build this route has reproduced the move-induction's Case 1/2/3 analysis instead of the structure theorem + averaging, fold the slug for good (its lemmas are already donated to `lemmas/`). The alt-upper explorer's warning is on record: per-region certificate hunting is the same wall in convex-analysis clothing — the only reason this slug lives is steps 3–4 as stated.

## Watch out for
- Non-integral pinned sub-pieces (the 4 → 4/3+4/3+4/3 example): the structure theorem must not assume sub-pieces are copies of whole piece values — components can be anchored at fractional tie values; the ternary claim is about *whole-piece* coefficients after telescoping, not about sub-piece integrality.
- Zero pieces and exact ties among the a_i (route through the compactification V1 conventions).
