## imo-2026-03 — lens: Z's RECURSIVE DYADIC CUT-TREE ORIGIN (structural induction on Z's subtree splits)

Scope: the single open wall **GAP L** (lower bound, Case B). Target (certified reductions):
`D̃(F) ≥ 1`, `F = Y ⊎ Z`, `Y` = fragments of top dyadic piece `2^n`, `Z` = a `≤(n−1)`-cut
response to `S_{n−1}={1,…,2^{n−1}}`, `sum(Y)−sum(Z)=1`. Equivalently the bounded-mass
count-parity inequality `(△⋆) λ_{(0,θ)}{M odd} ≥ ∫_{(0,θ)}M = 1−β`, `M=N_Y−N_Z`, `θ=2^{n−1}`,
`β=(y₁−θ)⁺≤1`. Equivalently even-rank sum `E(F) ≤ 2^n−1`. The min is exactly 1, TRUE numerically
(re-verified: `0/2·10⁵` violations across `n≤5`), attained on a **continuum**, proof unwritten.

The cut-tree object (certified Structure Lemma, §5 of the leader): `F = ⊎_{j=0}^{n} π_j`, `π_j`
a partition of `2^{n−j}` into `a_j+1` parts, `Σa_j ≤ n`. Define `G_p := π_p ⊎ … ⊎ π_n` = a
`≤(n−p)`-cut response to `S_{n−p}`, living in `(0,2^{n−p}]`, with `G_p = π_p ⊎ G_{p+1}` and
`sum(π_p)−sum(G_{p+1}) = 1` **at every scale p**. So the "+1 mass" recurs at every level; the
budget `Σa_j≤n` is spent down this tree, one group per dyadic scale.

- **Distinct openings (this lens):**

  - **(A) Recursed-(△) depth induction.** Recurse the certified exact identity `(△)` at each
    threshold `θ_p=2^{n−p−1}`: `D̃(G_p)=β_p + λ_{(0,θ_p)}(O_{π_p} △ O_{G_{p+1}})`, IH `D̃(G_{p+1})≥1`.
    Invariant to carry: control the **overlap** `λ(O_{π_p} ∩ O_{G_{p+1}})` using that `π_p` is a
    partition of a *single* dyadic piece (its parity set `O_{π_p}` has one "big jump" structure at
    the sub-threshold). What it needs: a child invariant strong enough to bound the overlap.
    **Likely failure / caution:** the two natural strengthenings — top-down reserve (REFUTED R7) and
    its dual **bottom-up reserve** (I tested it this round: `63496/10⁵` violations, worst −6.5,
    **REFUTED**) — both die. Probe: overlap is large (up to ~2–3) and IH `D̃(Z)≥1` alone does not
    bound it, so this opening needs a genuinely new *shape* invariant on the parity SET (not a
    scalar/reserve). Smells partly circular unless the strengthened IH is about set geometry.

  - **(B/D) Extremal-vertex reduction → 2-adic rigidity — DUAL OF THE CERTIFIED UPPER BOUND
    (headline, untried).** `D̃` is piecewise-linear in the fragment positions; on each fixed
    **merged order-type cell** it is *linear*, so its minimum is attained at a vertex. Vertices are
    where merged values tie (`w_i=w_{i+1}`) or a fragment/cut hits a group boundary. At a **tie**,
    two equal parts `{v,v}` form an **Invisible Pair** (certified upper-bound lemma:
    `D̃(R∪{v,v})=D̃(R)`) — remove them, `D̃` unchanged, `sum(Y)−sum(Z)=1` preserved, config reduced.
    Iterating collapses each vertex toward the **pure dyadic-integer skeleton**, where the target
    `E(F)≤2^n−1` / `D̃≥1` is a **2-adic (binary distinct-subset-sum) rigidity** — *exactly* the
    fact the certified upper bound's Sharpness note uses ("every nonzero {−1,0,1} combination of
    `2^i` has `|Σε_i2^i|≥1`"). This mirrors the R7 upper-bound proof (reduce to extremal signed
    sum, then binary rigidity gives the constant 1) **in the opposite direction** — and the lower
    bound has NEVER imported the upper-bound machinery (Invisible-Pair + binary rigidity). Verified
    this round that near-tight `maxc≥2` cells (e.g. `n=3, Y=(4,4), Z=(2.716,2,1.284,1), D̃=1`) form
    a **flat face** `p∈(2,3)` whose two **vertices are integer configs** `(4,4,2,2,2,1)` and
    `(4,4,3,2,1,1)` — consistent with the reduction. What it needs: (i) prove cell-minima are at
    ties/skeleton vertices; (ii) the Invisible-Pair collapse stays inside a checkable class; (iii)
    2-adic ≥1 on the skeleton. **Failure mode:** the collapse preserves `D̃` but may leave the
    "fragments-of-dyadic-pieces" realizable class (removing an equal `Y`/`Z` pair can break the
    per-group partition structure), and equality lives on a continuum (flat optimum), so (i) is the
    real risk. Still the strongest lead: it is non-local by construction, reuses two certified
    tools, and is genuinely far from every refuted framing.

  - **(C) Per-scale count-parity ledger (aimo-0493 dyadic tagging).** The surplus is bottom-inclusive
    (§14: it can be entirely a near-0 band where `|Z|>|Y|` in part count). Tag each part by its
    origin dyadic scale and build a ledger of count-parity contributions per value-band; uncut
    anchors (groups with `a_j=0`) give clean rigid contributions, and the **budget bounds the number
    of "messy" cut groups to ≤ n** — so at most `n` scales perturb the clean anchor ledger. What it
    needs: the anchor contributions to dominate the ≤n perturbations globally (summed, not matched).
    **Failure mode:** origin-scale ≠ value-band (a fragment of a big piece can be tiny), so if the
    ledger is read on value-bands it collapses back to the raw profile `M` (REFUTED family). The
    budget must enter by bounding the *count of perturbing bands*, not the profile itself — the
    non-trivial content.

- **Candidate technique(s):** structural/strong induction on the cut-tree depth via the recursed
  exact identity `(△)`; **import of the certified upper-bound tools (Invisible-Pair Lemma + binary
  distinct-subset-sum rigidity) into the lower bound** through a piecewise-linear extremal/vertex
  reduction; 2-adic valuation / binary-digit-sum invariant carried through the ±-operation tree
  (aimo-0917). The "vertex reduction then 2-adic rigidity" is the through-line and the dual of R7.

- **Cheap-kill candidates:** (1) **Bottom-up reserve is DEAD** — I refuted it this round
  (`63496/10⁵`, dual of the R7-refuted top-down reserve); do not seed it. (2) Any per-anchor/per-run
  MATCHING is dead (§10, survival-domination fails 21%). (3) Any invariant read on the raw profile
  `M`/merged order is dead (R8 `(△△)`: pure measure-algebra restatements give only `D̃≥0`, off by
  ½). Before heavy work, cheap-check the (B/D) reduction on the two integer vertices of a flat cell:
  if `E(F)≤2^n−1` fails at an integer skeleton vertex the whole opening dies fast (it does not — the
  vertices I found satisfy it with equality).

- **Knowledge-base entries to use:** binary/2-adic distinct-subset-sum rigidity of `{1,2,…,2^n}`
  (the source of the constant 1; already load-bearing in `lemmas/upper-bound.md` Sharpness);
  piecewise-linear extremal principle (min of a linear functional over a polytope face is at a
  vertex); Legendre's formula / binary digit-sum `S_2` valuation (for opening B, via aimo-0917).
  Certified lemmas to import verbatim: `upper-bound.md` (Invisible-Pair Lemma, Realizability/Theorem
  R, binary sharpness), `termwise-lattice.md` (Lemma T closes `maxc≤1`, incl. every tight config),
  `merged-order-layer.md` (`(△△)`, Lemma H `maxc≤|Y|=a_0+1`), `greedy-claim.md`, `cut-flip.md`, plus
  the leader's proven-in-file `(△)`, `(△⋆)`, `(♠′)`, Structure Lemma.

- **Analogous past problems (cruxes):**
  - **aimo-0917 (IMO-SL 2020, invariants) — strongest match.** A game with `x+y` / `|x−y|` moves;
    the crux keeps a **2-adic valuation invariant** (`2^{s+1} ∤ N` where `N`=# balanced sign
    collections, `v_2(N)=S_2(n)` by Legendre) and splits `N=N_+ + N_-` so **an odd 2-adic valuation
    forces one branch to inherit it** — a non-local constant injected through a ±-operation tree.
    Directly models opening B: the signed-sum form `(♠′) D̃−1=2(Σ_{z odd-pos}z−Σ_{y even-pos}y)` is a
    ±-combination of fragments over the cut-tree, and the missing 1 is a 2-adic rigidity; this crux
    is the template for turning that rigidity into a tree-carried invariant. Adapt, don't cite.
  - **aimo-0493 (IMO-SL 2008, monovariants) — dyadic per-scale tagging.** "Tag each element by which
    dyadic threshold `2^k` separates its within-set gaps; one tag per scale; bound each scale
    separately." Template for opening C's per-scale count-parity ledger over `{1,…,2^{n+1}}` (note:
    same ground set `A={1,…,2^{n+1}}` and same `2^n` count as our `S`).
  - **aimo-1024 (USAMO 2022, induction) — middle-pivot recursion `T(k)=2T(k−1)+1`** matching the
    `2^{n+1}−1` dyadic recurrence; template for the depth-`p` structural induction skeleton (opening
    A), where one fresh object handles the split point and each half recurses.

- **Prior progress:** Upper bound fully proven & certified for all n (`lemmas/upper-bound.md`, R7).
  Lower bound complete except Case-B residual `maxc≥2`, reduced to `(△⋆)` / `E(F)≤2^n−1` (bounded
  mass ≤1). Leader `induction-recursion-telescope` owns `(△),(△⋆),(♠′),(△△)`, Lemma H, Structure
  Lemma. Tight core (`maxc≤1`, all equality configs) closed by Lemma T. `cut-sequence-potential` and
  `even-rank-doublecount` are RETHINK (their sequential/genfn engines proven equivalent to the target).

- **Dead ends (do NOT retry):** merged-order / measure-profile / sequential-cut / generating-function
  framing of the final multiset (R8, all proven equivalent to target, give only `D̃≥0`); scalar /
  aggregate-of-Z summary (R3–R4); per-anchor / per-run width-weighted matching (R7 §10, fails 21%);
  **top-down reserve** of Z (R7 §14) **and bottom-up reserve** of Z (refuted THIS round, `63496/10⁵`);
  one-sided confinement of `O_Z`; bounded-window nonneg-block tiling / crux-aimo-0626 (R8 §15,
  circular + no local certificate); any reduction of GAP L to a free-standing bounded-multiset
  inequality on Z with only `sum(Z)`+`altsum(Z)≥1` (probes 5–7, FALSE). The reduction-to-pure-integer-
  skeleton must handle the **flat optimum**: equality is attained on continuous order-type FACES, not
  isolated integer points — do not assert the minimizer is a unique integer config.

- **Small-case / intuition notes (conjecture unless noted):**
  - CONFIRMED numerically: target `D̃≥1` holds `0/2·10⁵` (`n≤5`); min = 1 attained.
  - CONFIRMED this round: the residual's tight cells are **flat linear faces** whose vertices are
    integer/dyadic configs (e.g. `n=3`: face `Y=(4,4), Z=(p,2,4−p,1)`, `p∈(2,3)`, `D̃≡1`; vertices
    `(4,4,2,2,2,1)` and `(4,4,3,2,1,1)`). Supports openings B/D: `D̃` is linear on order-type cells,
    so a vertex/extremal analysis is well-posed and the vertices reach the 2-adic skeleton.
  - CONJECTURE (opening B/D, the promising one): `min_{cell} D̃` is attained where the config
    collapses (via Invisible-Pair) to the pure dyadic skeleton `{1,…,2^n}` refined trivially, where
    `E(F)≤2^n−1` is the binary distinct-subset-sum fact — the same constant-1 mechanism the certified
    upper bound already uses. This is the untried DUAL of R7 and the recommended framing to seed.
  - The budget's non-local role is concretely: `Σa_j≤n` over `n+1` groups ⇒ at least one uncut
    anchor, and at most `n` "perturbing" cut-groups — the lever that any global (opening C) or
    extremal (opening B/D) argument must convert into the missing ½.
