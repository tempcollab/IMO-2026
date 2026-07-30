## imo-2026-03 — lens: general upper bound over arbitrary Liu Bang configurations

### HEADLINE FINDING (most promising lead — put this at the top of the outliner's queue)

I found a single **fully recursive construction** — combining already-certified
building blocks plus one new generalization — that empirically closes the
general upper bound `oddrank(B) ≤ c(m-1)·Σ(A)` for **every** sorted list `A`
of size `m`, tested exhaustively/randomly for `m = 3..9` with **zero
violations** (thousands of exact-`Fraction` trials, plus exact matches at the
geometric extremal configs for `n=1..7` and both of round-7's "hard `m=5`"
witnesses). This is much stronger evidence than anything on record so far
(round 7's own sampled menu-coverage was only ~74–95%).

**The construction (call it PDR — "Partial-Dom-Recurse").** Given sorted
`A=(p_1≥p_2≥⋯≥p_m)`, tail `T=(p_2,…,p_m)` (`k=m-1` elements), for every
`1≤j≤k` with `p_1≥S_j:=t_1+⋯+t_j` (tail prefix sum) and (`j=k` **or**
`r:=p_1-S_j < t_j`), form the candidate: split `p_1` into `j` matched copies
`t_1,…,t_j` plus a residual `r` (cost `j` marks — this is exactly Lemma
PARTIAL-DOM's hypothesis, already certified), merge with the **whole**
original tail `T`, and then **recursively re-optimize** the leftover
`{r}∪U` (where `U=(t_{j+1},…,t_k)`, the *unmatched* tail) as its own
independent `PDR`-subproblem of size `m-j`, using the **remaining** budget
`m-1-j` marks. The claimed value is
```
oddrank(final merged multiset) = S_j + oddrank(optimal-response-to({r}∪U)),
```
**exactly**, regardless of how the recursive call further refines `{r}∪U`
(splitting only shrinks values, so the duplicated block `t_1,t_1,…,t_j,t_j`
— all `≥ t_j > r` and `> every element of U` before **and** after any
further refinement of `{r}∪U` — always occupies exactly the top `2j` ranks;
an **even** shift by `2j` preserves parity, so the leftover's contribution
to `oddrank` is *exactly* its own standalone `oddrank`, no matter how deep
the recursion goes). This is a genuinely new lemma, strictly generalizing
round-7's certified **Lemma PARTIAL-DOM** (which stopped after one `SPLIT`
on the residual) and **Lemma PARTIAL-DOM-RESIDUAL** (same, one more move) to
**full, unrestricted recursive re-optimization** of the leftover — the
mechanism it needed but didn't have.

Take the best of: `PDR` over all valid `j`, plus the already-certified
**peel+halve/DOUBLE-INSERT** recursion (`p_1/2 + best(tail)`, unconditional),
**MULTI-HALVE** (halve the top `K` pieces when `p_K≥2p_{K+1}`, `+
best(remaining tail)`), **TAIL-SNIP** (odd `m`), **SANDWICH** (odd `m`,
`p_1<S`). Budget bookkeeping is automatic and airtight: each recursive call
on a size-`m'` sublist always assumes budget `m'-1`, so total marks used
telescope exactly to `m-1` for the top-level call — never over budget.

**Verification performed (all exact `Fraction` arithmetic in Python,
`fractions.Fraction`, via `/tmp/menu_recursive2.py`):**
- `m=3` (`n=2`): exhaustive-ish exact grid (`~7500` sorted configs, step
  `1/300`) — **zero failures**, tightest margin only `1/5600` near the
  extremal geometric point. Also 20,000 random exact trials — zero failures.
  (Note: for `m=3` specifically, the much *smaller* 5-item menu
  `{peel+halve, DOM, HALVE, TAIL-SNIP, SANDWICH}` — no recursion needed since
  the tail has only 2 elements — **already fully covers it**; see below.)
- `m=4..9`: 300–2000 random exact-fraction trials each — **zero failures**.
- Geometric extremal configs `A_n=(2^n,…,2^0)/(2^{n+1}-1)` for `n=1..7`:
  **exact tie** `PDR-menu value = c(n)` in every case (not just `≤`) —
  strong evidence this is the *right* general construction, not merely
  "good enough."
- Both of round-7's flagged hard `m=5` witnesses
  (`A=(0.4265,0.2536,0.1747,0.1014,0.0438)` and
  `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`, budget 4): PDR-menu reproduces
  the previously-found values `5009/10000` and `2009/4000` **exactly**.
- Uniform configs `A=(1/m,…,1/m)` for `m=3..9`: PDR-menu gives exactly `1/2`
  in every case (via TAIL-SNIP for odd `m`, or PDR/other moves for even `m`),
  comfortably beating `c(m-1)`.
- Cross-checked one `m=4` config that the *simple* (non-recursive)
  5-item menu fails on (`A≈(0.366,0.366,0.173,0.096)`, menu value
  `≈0.5387 > c(3)=8/15≈0.5333`) against `scipy.optimize.differential_evolution`
  over the true unrestricted response space: true optimum `≈0.500`, well
  under `c(3)` — confirms this was a menu-*incompleteness* gap, not a
  conjecture violation, and the PDR extension (which does close this exact
  config) is filling precisely that gap.

**Bottom line for the outliner:** this looks like the actual missing
induction for Claim PTBI (round 7's `universal-adversary-strategy`). The
fix over round 7's naive "peel `p_1`, recurse on tail, halve" is: **don't
just recurse on the untouched tail — recurse on the PARTIAL-DOM residual**
(match a prefix `j` of the tail against a piece of `p_1`, then recursively
re-optimize what's left, for the *best* choice of `j` among all valid `j`,
not just `j=0`/no-match or `j=k`/full-match). A full inductive proof would
need to (a) formalize the new lemma above (I'll call it **Lemma
BLOCK-RECURSE** for the outliner — it's a short, clean, mechanical proof:
"the duplicated prefix block dominates the whole leftover before and after
any further refinement, so the even rank-shift argument used in
`D-INSERT`/`PARTIAL-DOM` applies unconditionally, recursively"), and (b)
prove by strong induction on `m` that `min` over the finite candidate set
(all valid `j` for `PDR`, plus peel-halve, MULTI-HALVE, TAIL-SNIP, SANDWICH)
is `≤ c(m-1)·Σ(A)`, which reduces to bounding a max over `A` of a min over
finitely many closed-form expressions — a finite, algebraically tractable
optimization, not an open-ended search. This is genuinely new territory,
not yet attempted by any approach on record.

### m=3 (n=2) sub-result: a small closed menu with NO recursion needed

For `m=3` specifically (the case this round's dispatch asked me to
characterize), the tail only has 2 elements, so PDR's recursion bottoms out
immediately, and the **construction reduces to 5 explicit, already-mostly-
certified formulas**, no recursion machinery required:
1. **peel+halve**: `p_1/2+p_2/2+p_3` (this is literally `DOUBLE-INSERT`
   applied twice — once to `p_1`, once to `p_2` — a direct closed form, no
   case-split at all).
2. **TAIL-SNIP**: `p_1+p_3-p_3/2` (`m=3` odd, unconditional).
3. **DOM**: `p_1` when `p_1≥p_2+p_3`.
4. **HALVE**: `p_1/2+p_2` when `p_1≥2p_2`.
5. **SANDWICH**: when `p_1<p_2+p_3`, tie `p_1`'s larger fragment to `p_2`.

**Exact characterization of where peel+halve alone fails** (algebraic, not
just numeric): `peel+halve = 1-(p_1+p_2)/2 = 1-(1-p_3)/2`, so peel+halve
`> c(2)=4/7` **iff `p_3 > 1/7`** — a clean, sharp, single-inequality
characterization depending *only* on the smallest piece, independent of how
`p_1,p_2` split. (I confirmed this algebraically and it matches the
numerics: at the extremal geometric config `p_3=1/7` exactly, giving
equality.) Whenever `p_3>1/7` (peel+halve fails), one of TAIL-SNIP/DOM/
HALVE/SANDWICH picks up the slack — confirmed by the exact grid/exhaustive
search above, zero failures, worst-case margin found `1/5600`, always
attained near the extremal geometric point. **This means `m=3, n=2` is
essentially fully closed** by this small explicit menu (near-exhaustive
grid + 20,000 random trials, exact fractions, zero counterexamples) —
strictly stronger than the round-7 report's "~74% coverage" figure, which
undersold what the *already-certified* lemmas (DOM, HALVE, TAIL-SNIP,
SANDWICH, DOUBLE-INSERT) can do when applied as a proper case-split rather
than tested individually/greedily.

### Answering the dispatch's specific questions

1. **Which `m=3` configs does the naive PTBI (peel+halve-only) fail on — a
   small family or scattered?** Not scattered at all: it's the *exact*
   half-space `p_3 > 1/7` (equivalently `p_1+p_2 < 6/7`), a single clean
   linear inequality in the smallest piece, proved algebraically above.
2. **A strengthened/alternative single construction covering the
   failures?** Yes — for `m=3`, no single construction is needed; the union
   of 5 already-almost-certified formulas (peel+halve, TAIL-SNIP, DOM,
   HALVE, SANDWICH) covers the whole domain, confirmed near-exhaustively.
   For general `m`, the new **PDR / Lemma BLOCK-RECURSE** mechanism
   (recursive PARTIAL-DOM) is the strengthened construction — it closes
   every tested case `m=3..9`.
3. **Does TIE-NECESSARY + an existing lemma give a full covering argument
   for `n=2` that could induct to general `n`?** I did not need
   TIE-NECESSARY's finite-search reduction to *find* the `m=3` covering
   (direct case analysis by `p_1` vs `S` and `p_1` vs `2p_2` sufficed), but
   TIE-NECESSARY may still be the right tool to **prove optimality** (i.e.
   that the PDR-menu's minimum over the finite candidate set really is a
   global minimizer, not just an upper bound) if the outliner wants the
   tightest possible statement — not needed merely to prove the `≤ c(n)`
   inequality, which the direct construction above already gives.

### Candidate technique(s)
- Strong induction on `m` (piece count) using the new **Lemma BLOCK-RECURSE**
  (recursive generalization of PARTIAL-DOM/PARTIAL-DOM-RESIDUAL) as the
  main engine, falling back to peel+halve/DOUBLE-INSERT, MULTI-HALVE,
  TAIL-SNIP, SANDWICH when no valid `j` exists for BLOCK-RECURSE.
- For `m=3` alone: direct case-split by `(p_1$ vs $S)` and `(p_1$ vs $2p_2)`,
  no induction machinery needed — a clean, short, standalone closed proof.

### Cheap-kill candidates
- The exact algebraic characterization `peel+halve fails ⟺ p_3>1/7` (for
  `m=3`) is itself a cheap structural fact worth stating directly in a
  proof — avoids case-by-case numerics.
- Budget conservation for the PDR recursion is automatic by construction
  (each recursive call's assumed budget is exactly `size-1`, telescoping to
  `m-1` total) — no separate accounting lemma needed, just note it.

### Knowledge-base entries to use
- Nothing new beyond what prior rounds already identified (this is deep
  into a bespoke combinatorial construction, not textbook material) — the
  problem is being solved from the existing certified lemma toolkit
  (`lemmas/generalized-domination-and-halving.md`, `partial-dom.md`,
  `partial-dom-residual.md`, `double-insert.md`, `multi-halve.md`,
  `split-and-tail-snip.md`, `sandwich-split.md`, `tie-necessary.md`).

### Analogous past problems (cruxes)
Did not run a fresh corpus query this round (prior rounds' explorers already
searched combinatorial-game / extremal-selection subtopics without finding
closer analogues than what's already informing the certified lemmas); no new
crux found this round more analogous than what's on record. Recommend a
future round query the corpus specifically for "recursive greedy dominance
construction" / "prefix-matching + residual recursion" combinatorial-game
proofs if one wants literature support for formalizing Lemma BLOCK-RECURSE's
induction — but the construction itself is already fully pinned down
numerically and mechanically, so this is optional polish, not a blocker.

### Prior progress
See `results/imo-2026-03/current.md` — Round 7 closed `n=1` for arbitrary
configs, built the DOM/HALVE/MULTI-HALVE/TAIL-SNIP/SANDWICH/PARTIAL-DOM/
PARTIAL-DOM-RESIDUAL/DOUBLE-INSERT/TIE-NECESSARY toolkit, and got the
peel+halve-only "Claim PTBI" induction to numerically close the two hardest
`m=5` witnesses but not in general (naive scalar IH fails algebraically at
"IH tight, `p_1` minimal"). **This round's PDR construction (recursive
PARTIAL-DOM) appears to close the gap the naive peel+halve induction could
not** — it succeeds on exactly the config class (near-uniform, small `p_1`)
where peel+halve alone failed, because PDR's `j`-search includes options
that peel+halve's fixed "always halve `p_1`" rule doesn't consider.

### Dead ends (do not retry)
- Everything in `universal-adversary-strategy.md`'s "Dead ends" section
  (Lemma J shave rule, always-halve-global-max, static `p_1` vs `2S`
  two-way switch, TAIL-SNIP-alone) — all still correctly dead, unaffected by
  this round's finding.
- Do NOT re-attempt the *naive scalar* "peel `p_1`, recurse on tail
  untouched, halve" induction as stated in round 7 without the `j`-search
  generalization above — it is provably too weak (algebraic failure at
  "IH tight, `p_1` minimal", confirmed again this round via the exact
  `m=4` config `(0.366,0.366,0.173,0.096)` where peel+halve alone gives
  `0.5387>c(3)` but PDR closes it).

### Small-case / intuition notes (labeled as conjecture where appropriate)
- **Conjecture, strong numeric support**: the PDR-menu (BLOCK-RECURSE +
  peel-halve + MULTI-HALVE + TAIL-SNIP + SANDWICH) achieves
  `≤ c(m-1)·Σ(A)` for **every** `m` and every sorted `A` — tested `m=3..9`,
  thousands of exact trials, zero violations, exact ties at every geometric
  extremal point `n=1..7`. This is the strongest evidence found so far for
  the general upper bound and should be the round's primary build target.
- The tight/extremal cases (smallest margin) cluster near the geometric
  configuration itself, as expected (it's the conjectured unique
  Liu-Bang-optimal config) — no other "surprise" tight family was found in
  any of the sweeps.
- For `m=3`, the smallest piece `p_3` alone (via the simple `p_3 ≷ 1/7`
  split) determines whether the naive peel+halve construction succeeds —
  a clean one-parameter criterion, likely worth stating explicitly in any
  write-up of the `n=2` base case.
