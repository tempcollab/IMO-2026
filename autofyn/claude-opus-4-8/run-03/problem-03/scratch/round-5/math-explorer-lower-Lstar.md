## imo-2026-03

### Scope of this lens
Assigned: scout whether (L⋆) — `D(S') ≤ f₁ − 1` (Case I of the lower bound, both live approaches'
shared wall) — is provable by **induction on piece count** using Lemma PEEL / Lemma SPLIT, map the
exact statement/base/step, find where it breaks, and separately settle GAP L2 (Case II, top
shredded into all-≤2^{n-1} fragments). No full proof attempted; this is terrain-mapping backed by
numerical experiments (Python, `sorted`-alternating-sum `D`, random cut simulation, n≤4).

### Precise restatement of (L⋆)
`S'` arises as: the top piece `2^n` is cut (≥1 cut) into `f₁ ∈ (2^{n-1}, 2^n)` (the unique piece
of the whole multiset `S` exceeding `2^{n-1}`) plus `k` further fragments `A` (using `k−1` more
cuts, `k≥1`) with `A` a refinement of a single virtual piece of mass `w := 2^n − f₁ < 2^{n-1}`;
plus `B`, a refinement of the tail `C_{n-1}={2^{n-1},…,1}` using the remaining `n−k` cuts. So
`S' = A ⊔ B`, all pieces ≤ `2^{n-1}`, `mass(S') = 2^{n+1}-1-f₁ = (2^n-1)+w`, built with exactly
`n−1` total cuts. Target: `D(S') ≤ f₁-1 = (2^n-1) - w`.

### KEY FINDING — the inequality splits into a trivial regime and a narrow critical band
Numerically verified (n=3,4; thousands of random completions, zero violations of (L⋆) anywhere):
- **Trivial regime `w ≤ 2^{n-1}-1` (i.e. `f₁ ≥ 2^{n-1}+1`):** the crude bound `D(S') ≤ max(S') ≤
  2^{n-1}` (every piece of S' is ≤ 2^{n-1} by construction) already gives `D(S') ≤ 2^{n-1} ≤
  f₁-1` **directly** — no cross-term/cancellation argument needed at all. This is because
  `f₁-1 ≥ 2^{n-1} ⟺ w ≤ 2^{n-1}-1`. **This closes the vast majority of the range for free** and
  should be stated as a one-line sub-case before any heavier machinery.
- **Critical band `w ∈ (2^{n-1}-1, 2^{n-1})`, i.e. `f₁ ∈ (2^{n-1}, 2^{n-1}+1)`** (width exactly
  1!): here `f₁-1 < 2^{n-1}`, so the trivial bound fails and the cross-term (Lemma SPLIT) must be
  carried. This is the ONLY regime where (L⋆) is non-trivial and tight.

This band-narrowing was **not present** in either live approach's writeup — both state (L⋆) as
one monolithic inequality over all `f₁ ∈ (2^{n-1},2^n)`. Telling the outliner to split the case
this way removes ~all the "loose" content and focuses effort exactly where it's needed.

### Inside the critical band: numerics pin down the exact mechanism
For n=3 (tail `C_2=[4,2,1]`, budget 2 cuts on `S'`), sweeping `w ∈ {3.0,...,3.999}`: the maximum
of `D(S')` over **all** Xiang completions (tail cut or not) exactly equals the maximum obtained
by the restricted family **"leave the tail C_{n-1} completely uncut, spend all `n-1` cuts
splitting the w-piece"** — matched to 4-5 significant digits at every sampled point in the band
(e.g. w=3.5: both give exactly 3.5 = f₁-1; w=3.9: both give exactly 3.1 = f₁-1). Outside the band
(w=1,2 for n=3) tail-cutting strictly beats tail-uncut (e.g. w=1: full search 3.99 vs tail-uncut
3.0), but there the bound has huge slack (bound=6.0) so it doesn't matter.

**The extremal construction (tail uncut) has closed form.** Splitting `w` into exactly `n`
fragments `g_1>...>g_n` with `g_i ∈ (t_{i+1}, t_i)` where `t_i = 2^{n-i}` are the tail values
(so each fragment sits in the open gap strictly between two consecutive tail values, using `n-1`
cuts) gives merged sorted order `t_1,g_1,t_2,g_2,...,t_n,g_n`, hence exactly
```
D(A ∪ C_{n-1}) = (t_1 - g_1) + (t_2 - g_2) + ... + (t_n - g_n) = (2^n-1) - w = f₁ - 1.
```
Feasibility (the g_i bands have total width `Σ(t_i-t_{i+1}) = 2^{n-1}` — exactly matching the
required range `w < 2^{n-1}`) confirmed by direct construction and numerically (found by random
search independently, e.g. n=3, w=3.2 gave fragments `2.05,1.11,0.037` sitting in gaps
`(2,4),(1,2),(0,1)` respectively). **This is the exact mirror/dual of the GAP L2 extremal
construction** noted in induction-peel.md (`g_k` slightly **exceeding** each `t_k`, giving
`D=Σg_k-Σt_i=1`) — here the fragments sit **below** each `t_i` instead of above. Both constructions
are provably tight (verified: GAP L2 min D found = 1.00007 over 400k random n=3 Case-II
completions, matching the `≥1` bound; L1 max D found in the critical band matches `f₁-1` to 4
decimal places at every tested point).

### Is plain induction on piece count (via PEEL/SPLIT alone) viable?
**Not as a single clean step** — here's exactly where it breaks:
- Applying Lemma SPLIT to `S'=A⊔B` gives `D(S')=D(A)+D(B)-2μ(O_A∩O_B)`. The crude bound
  `D(A)≤w`, `D(B)≤2^{n-1}` (each trivial, single-max bound) gives `D(S')≤w+2^{n-1}`, which
  **exceeds** the target `f₁-1=(2^n-1)-w` exactly in the critical band (checked: at `w`
  approaching `2^{n-1}`, `w+2^{n-1}→2^n` while target `→2^{n-1}-1`, a huge gap). So **dropping
  the cross term is fatally lossy near the band** — confirms current.md's diagnosis, now with the
  exact quantitative gap measured.
- A genuine induction "on piece count of `A`" (holding tail fixed uncut, inducting on the number
  of cuts spent on `w`) **is numerically well supported as a base+step structure**:
  - **Base `k=1`** (A left as single piece `w`, inserted into sorted `C_{n-1}`): checked
    numerically for n=4 across the whole range `w∈(0,2^{n-1})` — `D({w}∪C_{n-1})` stays well
    below `(2^n-1)-w` everywhere (large margin, e.g. `w=1.03`: D=5.97 vs bound=13.97), i.e. the
    base case is easy and not tight (tightness only appears at `k=n`, using the full cut budget).
  - **Inductive step (k → k+1, one more cut on A)** is where the real content lives: need to show
    that each additional cut on `A` can raise `D` by *at most* the exact telescoping amount needed
    to reach, but never exceed, the `(2^n-1)-w` ceiling. This is a genuinely new "how much can one
    more cut increase D" lemma — NOT already certified (Lemma T bounds `|ΔD|≤2s₂` per cut,
    but that per-cut bound, summed over `k` cuts, is again too loose — it would allow `D` to grow
    unboundedly with more cuts, when in fact the interleaving construction shows the max is
    achieved at exactly `k=n` cuts and cannot exceed a hard ceiling for any `k`). **This is the
    actual gap to fill**, and it is NOT solved by citing PEEL/SPLIT alone — a new
    "one-more-cut-cannot-overshoot-the-gap-ceiling" argument (perhaps an exchange/rearrangement
    argument: any fragment placed outside a `(t_{i+1},t_i)` gap, or a second fragment placed in
    the same gap, can be shown to strictly decrease `D` relative to the canonical one-per-gap
    layout) is needed. This is plausible (an exchange argument on adjacent values is a standard
    olympiad move) but **not yet proved** — flag as the residual technical gap inside (L⋆).
- The needed auxiliary invariant for the induction is **not "mass" or "piece count" alone** but
  the **gap structure**: which of the `n` open intervals `(t_{i+1},t_i)` (and `(0,t_n)`, `(t_1,∞)`)
  already contain a fragment of `A`. A clean strengthened IH would carry, as invariant, "the
  multiset of occupied/unoccupied gaps," reducing the step to a single-fragment insertion-or-split
  argument. This is exactly the kind of invariant `induction on piece count` needs but that neither
  PEEL nor SPLIT alone supplies — they're the right *identities* but a bespoke gap-occupancy
  argument on top of them is the missing piece.

### Where it will break for the outliner to watch for
- Do NOT let the builder drop the cross term "even a little" in the critical band — the numeric
  margin there is exactly zero at the band's right edge (w→2^{n-1}), so any lossy step fails.
- The "leave tail uncut is extremal" claim is **only true inside the critical band**; outside it,
  it is FALSE (tail-cutting strictly beats it) but harmless because the bound has slack there. A
  proof must either (a) prove the trivial bound for `w≤2^{n-1}-1` and a separate, tight argument
  only for the band, or (b) find one uniform argument valid everywhere (harder, likely wasteful).
  Route (a) is recommended.

### GAP L2 (Case II — top shredded, all pieces ≤2^{n-1})
Numerically confirmed (n=3, 400k random completions with ≥2 cuts on the top so ≥3 top fragments,
tail arbitrarily also cut): `min D = 1.00007` (matches target `D≥1` tightly), achieved essentially
at the "tail uncut, top fragments each slightly exceeding the paired tail value" construction
(`g_k` interleaved just **above** `t_k` — the mirror of L1's "just below" construction; this is
exactly the telescoping identity already written out in induction-peel.md's round-3-correction
note, `D=Σg_k - Σt_i = 2^n-(2^n-1)=1`). **GAP L2 and (L⋆)/GAP L1 are structurally the same
combinatorial object** — an "interleave free mass `w` into the fixed sequence `C_{n-1}`" problem,
differing only in which side of each gap the fragment sits (below for L1's upper bound on `D(S')`
when `w<2^{n-1}`; above for L2's lower bound on `D` when `w=2^n`, i.e. `n+1` fragments straddling
all `n` gaps plus overflowing past `t_1`). **Recommend to the outliner: state one unified
"gap-interleaving lemma"** parametrized by whether fragments sit above or below each tail value,
and derive both L1 and L2 as its two instantiations, rather than treating them as separate proofs.
This halves the remaining work if it can be made rigorous.

### Cheap-kill / simplification to hand to the outliner
1. **Split (L⋆) into `w≤2^{n-1}-1` (trivial, one line) and the critical band `w∈(2^{n-1}-1,
   2^{n-1})` (the only real content).** This alone removes most of the case's apparent difficulty.
2. Target a single **"gap-occupancy" induction** on the number of cuts spent on the free mass
   `w` (or, dually, on the top fragments in Case II), with invariant = which of the `n` canonical
   gaps `(t_{i+1},t_i)` are occupied — not a generic "piece count" bound via crude PEEL/SPLIT.
3. Unify L1 and L2 as two instances of one interleaving lemma (above vs below insertion).

### Candidate technique(s)
Exact combinatorial "insertion into a fixed geometric ladder" argument (exchange/rearrangement on
adjacent fragment-vs-tail-value pairs), built on top of the already-certified Lemma M (measure
identity) and Lemma T (toggle calculus) — NOT a new appeal to generic real-analysis smoothing.
Lemma SPLIT is the right decomposition tool but its crude two-term bound must be sharpened via
this gap-occupancy structure, not used as-is.

### Knowledge-base entries relevant
`lemmas/measure-identity.md` (Lemma M/I, `D=μ{N odd}` — the workhorse for computing D of the
merged interleaved sequence exactly), `lemmas/strict-max-peel.md` (Lemma PEEL — already used to
derive (L⋆) itself, not needed further inside it), `lemmas/split-cross-term.md` (Lemma SPLIT —
needed but its naive use is the diagnosed failure point), `lemmas/top-scale-dichotomy.md` (Lemma
ONE — established the `w<2^{n-1}` regime in the first place). No new knowledge_base.md generic
theorem obviously applies beyond what's already imported; this is a bespoke finite combinatorial
lemma about geometric sequences and interleaving, closest in spirit to rearrangement-inequality /
exchange-argument technique (standard olympiad tool, not separately named in knowledge_base.md).

### Analogous past problems (crux corpus)
Did not find a close analogue in the time available for this focused numerical/structural dive —
the "interleave free mass into a fixed geometric ladder to compute an alternating sum exactly" is
quite specific to this problem's D-functional; a targeted corpus search under combinatorics /
extremal or exchange-argument subtopics would be needed by the outliner if it wants a template for
the exchange-argument style step, but nothing here should be forced as a match.

### Prior progress recap (unchanged, both approaches at the same wall)
Both `induction-peel.md` and `parity-measure-potential.md` have (correctly) reduced Case I to
exactly (L⋆) via Lemma PEEL, and both list Case II (=GAP L2) as the companion open piece.
Upper bound is separately closed for `a₁≥L/2` in both approaches (§4A / whole-tail-peel Branch 2);
GAP U (balanced `a₁<L/2`) is untouched by this lens (out of scope — assigned to lower bound only).

### Dead ends (do not retry)
- Dropping the SPLIT cross term (`D(S')≤D(A)+D(B)`) — quantitatively confirmed to overshoot by
  as much as `2^{n-1}` near the critical band's right edge; already flagged in current.md, now
  measured precisely.
- Treating (L⋆) as valid uniformly via a single mass-only bound (à la the refuted GAP U
  subset-cover lever) — same failure mode as GAP U: D depends on internal structure (gap
  occupancy), not mass, once inside the critical band.

### Small-case / intuition notes (labeled conjecture where not proved)
- CONJECTURE (strong numeric support, n=3,4, tens of thousands of trials): (L⋆) splits cleanly
  into a trivial half (`w≤2^{n-1}-1`) and a tight critical band of width exactly 1 in `f₁`.
- CONJECTURE (numeric, matched to 4-5 sig figs at every tested band point): inside the critical
  band, leaving `C_{n-1}` uncut and inserting `n` fragments one per gap is exactly extremal for
  both L1 (below-gap insertion) and L2 (above-gap insertion, matches earlier construction note).
- Not proved: the inductive step "one more cut on the free mass cannot push D past the ceiling"
  — this is the genuine remaining mathematical content of (L⋆), and by the L1/L2 duality, likely
  also the content that would close GAP L2 if solved once in unified form.
