## imo-2026-03 — lens: lower-bound top-piece-cut coupling gap (GAP L / GAP B2)

### Setup recap (confirmed correct)
Liu's dyadic construction in units of `u = 1/(2^{n+1}-1)`: pieces `1,2,4,...,2^n` (sum
`2^{n+1}-1`). Need: for ANY ≤n Xiang cuts, `D ≥ 1` (unnormalized). Case A (top piece `P=2^n`
never cut) is fully proved via Lemma I: `N(t)=1` on `[2^n-1,2^n)`. Case B (Xiang cuts `P`
at least once) is open in both live approaches, with identical diagnosis: `P`'s fragments
(mass `2^n`) dominate the tail `1,...,2^{n-1}` (mass `2^n-1`) in the global sort, so the
residual after "using up" a cut on `P` is not a clean order-(n-1) instance.

**I verified this numerically** (continuous random-cut search, `explore.py`/`explore2.py`,
150k-200k trials): min D over ALL cut strategies (including ones that force-cut the top
piece first, at arbitrary fraction, not just bisection) is exactly `1` for n=1,2,3 to
machine precision. Two useful new facts from this experiment:
- **The claim is true and tight** — Gap L is not a dead end to route around, it is a real
  theorem waiting for a proof.
- **The minimizer is NOT unique.** Forcing the first cut on `P` at fraction `0.71` (n=2)
  or `0.83` (n=3) — not bisection (`0.5`) — still lets the rest of the game reach `D=1`.
  So the extremal set is a whole flat region of strategies, not an isolated equilibrium.
  This matters: an *inequality*-style argument (showing `D ≥ 1` from structural bounds)
  is more promising than trying to pin down "the" unique optimal continuation, since many
  continuations are optimal.

### Distinct openings

1. **Strengthen the induction hypothesis to general superincreasing sequences with gap
   `g`** (`a_j - Σ_{i<j}a_i = g` for all j), by induction on piece-count rather than on `n`
   fixing cut budget separately. I checked directly whether this repairs Case B: after
   Xiang cuts `P=a_m` into `p1≥p2`, does `{a_1,...,a_{m-1}}∪{p1,p2}` remain superincreasing
   (so the IH reapplies one level down)? It needs `p1 ≥ (a_1+...+a_{m-1}) + p2 + g'`; since
   `p1+p2=a_m=Σ_{i<m}a_i+g`, this forces `p2` to be tiny — false in general (bisection gives
   `p1≈p2≈a_m/2`, comparable to `a_{m-1}`). **This confirms the obstruction is real, not an
   artifact of a weak induction statement** — any fix must handle genuinely non-superincreasing
   residuals. Do not waste a round just re-trying a stronger IH of this same shape.

2. **"n cuts vs n+1 protected bands" pigeonhole / charging argument.** There are n+1 dyadic
   "scale bands" `[2^{k}-1,2^k)` (well, the odd/even alternating bands from the un-cut
   config), and only n cuts. Idea: charge each Xiang cut against "killing" at most one
   band's odd-parity, so by pigeonhole at least one band (heuristically the smallest, width
   `u`) must survive odd. **Risk / why this needs care:** by Lemma T, a single cut's toggle
   set is `[0,s_2)∪[s_1,s)`, which is NOT confined to one dyadic band — a cut near the top
   can have `s_2` comparable to several lower bands at once, toggling all of them
   simultaneously. So the naive pigeonhole (1 cut ↔ 1 band) is false as stated; the correct
   charging scheme must account for a cut's toggle measure being spread over multiple
   bands, likely by tracking toggle *measure* (not band count) and showing total toggled
   measure across the odd-set is bounded by a telescoping sum ≤ (total − u). This is
   probably the most promising route to actually CLOSE the gap, but is real work, not free.

3. **Piece-count parity as a cheap complementary invariant (not sufficient alone).** By the
   Corollary to Lemma I, `D=0` requires every distinct value to have even multiplicity,
   which requires an EVEN total piece count. Starting from `n+1` pieces, after `k≤n` cuts
   the count is `n+1+k`. If Xiang uses all `n` cuts, count `=2n+1` is odd ⇒ `D>0` strictly
   (cannot be a perfect pairing) — but Xiang can instead use `k<n` cuts with the right
   parity to make the count even, so this alone does NOT force `D≥u`, only `D>0` in the
   full-budget branch. Cheap sanity check / partial pruning, not a closer.

4. **Shadow-game / coupling-map route** (crux-inspired, see below): instead of trying to
   make the residual literally an order-(n-1) dyadic instance, construct an explicit
   value-level MAP `φ` (an involution or piecewise-linear correspondence) from "Case B"
   configurations (top cut at least once) to "clean" order-(n-1) dyadic configurations,
   and prove a ONE-DIRECTIONAL inequality transfer: `D(actual residual) ≥ D(φ(residual))`
   using Lemma T's toggle bookkeeping, then apply Case A/IH to `φ(residual)`. This only
   needs an inequality, not an exact correspondence — matches the numerical finding above
   (flat extremal set) that exact matching is unnecessary.

5. **Amortized-potential route (a la aimo-0019, see below).** Track a potential
   `Φ_k = D(current config) ` after `k` cuts and show `Φ_k ≥ u_n · (something like a
   fixed fraction of remaining structure)`, proved by an amortized induction where each
   cut is "charged" against the piece/scale it destroys, bounding cumulative loss by a
   linear function of cuts used (cf. the "ink used ≤ 3x_r" invariant in aimo-0019). This
   reframes gap L as a resource-accounting problem instead of a case-split, which may be
   more robust to the top-cut interference than trying to force a clean recursive split.

### Candidate technique(s)
Measure/parity bookkeeping (Lemma I/T, already proved) + either (a) a genuine multi-band
charging/potential argument (opening 2/5) or (b) an explicit coupling map with one-directional
inequality transfer (opening 4). Straight induction-on-n with a stronger structural
hypothesis (opening 1) is verified to be a dead end in its natural form.

### Cheap-kill candidates
- Piece-count parity (opening 3): quick sanity check, rules out `D=0` in the full-budget
  branch, but not sufficient to reach `D≥u`.
- None of the "special symmetric cut" reductions (always-bisect, always-pair-top-two) are
  cheap kills for the LOWER bound side — they're strategies for the wrong player (those
  are Xiang's candidate strategies for the UPPER bound, already shown insufficient there).

### Knowledge-base entries to use
- `knowledge_base.md` "Invariants & monovariants" and "Induction" sections (generic) — no
  problem-specific dyadic-game entry exists yet in the KB; this problem's core lemmas
  (R, I/M, T, P) are already extracted as the reusable machinery and live in
  `results/imo-2026-03/lemmas/`.

### Analogous past problems (cruxes)
Searched combinatorics domain, subtopics `games-and-strategy`, `invariants-and-monovariants`,
`processes-and-algorithms`, filtered by keywords (stick/cut/interval/split/partition/dyadic).
- **aimo-0019** (IMO 2013-flavor "paint game"; player A supplies `1/2^m` ink units, B paints
  dyadic intervals). Crux: *"Maintain a linear potential bounding cumulative resource by a
  constant times progress, proved by amortized induction that charges each frontier
  advance against the pieces it absorbs"* and *"bound a family of dyadic-length pieces of
  pairwise distinct sizes by twice the largest via the geometric sum of distinct negative
  powers of two."* Genuinely analogous: same dyadic/geometric structure, same flavor of
  "opponent's resource-limited moves vs. an amortized potential" argument. This is the
  strongest match for opening 5 (amortized potential route) — worth reading in full if the
  outliner pursues that route.
- **aimo-0663** (combinatorial game on `[n]`, no-two-consecutive picks). Crux: *"reuse a
  winning strategy known only for one specific opponent-opening on a different opening by
  running a shadow game coupled to the real one via a position map, verifying only a
  ONE-DIRECTIONAL legality implication per player."* Analogous in spirit to opening 4: a
  coupling/shadow-instance argument that only needs a one-directional inequality, not a
  full equivalence — directly matches what's needed to couple the top-cut residual to a
  clean order-(n-1) instance without proving exact equality of configurations.
- **aimo-0117** (dyadic/geometric two-sided sequence in a stone-game so the largest term
  strictly exceeds the sum of all others) — same superincreasing idea as Liu's
  construction, but the solution there is for a different game structure (box-filling);
  read only if opening 1's "superincreasing gap" framing is revisited — but note opening 1
  is verified to break at top-bisection, so low priority.
- Nothing in the corpus is an exact match for "alternating-sum-of-sorted-parts game with a
  fixed cut budget"; the above three are the closest available, matches in *technique
  shape* (dyadic geometric bounding, amortized potential, one-directional coupling), not in
  literal problem content.

### Prior progress
See current.md: Lemmas R, I, T, P certified; lower Case A proved; upper bound reduced to
the all-strict full-budget case with greedy proven insufficient (separate gap, not this
lens). Gap L (this lens) is the sole remaining lower-bound obstruction.

### Dead ends (do not retry)
- Naive strengthening of the superincreasing induction hypothesis to survive an arbitrary
  top-cut (opening 1 above) — checked directly this round: bisection produces a residual
  that is NOT superincreasing relative to the tail, so the same-shape IH cannot be
  reapplied without a genuinely different argument. Do not re-attempt this exact
  strengthening; any viable induction must abandon "superincreasing is preserved" as an
  invariant.
- Naive "1 cut kills 1 band" pigeonhole (part of opening 2) is FALSE as stated because a
  single cut's toggle set `[0,s_2)∪[s_1,s)` can span multiple dyadic bands at once
  (Lemma T). Any pigeonhole/charging argument must track toggled *measure*, not band
  *count*.

### Small-case / intuition notes (conjectural / numerical, not proofs)
- Confirmed numerically (continuous random-cut search, not exhaustive but 150k-200k
  trials per case, machine precision) that min D = 1 exactly for the dyadic n=1,2,3
  configurations under an unrestricted Xiang, including when the first cut is forced onto
  the top piece at an arbitrary (non-bisecting) fraction. This is strong evidence (not a
  proof) that Gap L is TRUE and that the extremal set of Xiang strategies achieving D=1 is
  a whole flat family (bisection is one but not the only member), which favors an
  inequality/potential-style proof over trying to characterize a unique optimal line.
- The recursive-bisection strategy (cut top, cancel against the next-largest tail piece,
  repeat) that the upper-bound side already uses to show D ≤ u ON THE DYADIC INPUT is
  literally a Xiang strategy that cuts the top piece every round; the missing direction is
  showing NO Xiang strategy can do BETTER than this (i.e. push D below u). So gap L is
  exactly "prove the recursive-bisection value is optimal (a genuine minimum, not just an
  achievable value)" — this reframing may be useful to hand the outliner: it's a *matching
  upper-bound-on-Xiang's-power* statement, dual to the already-proved achievability.
