## imo-2026-03 — lens: UPPER-BOUND crux, GAP U-VALLEY (vertex/VERT route)

### Setup recap (verified from files, not re-derived)
- Target: minimax $D=u_n=1/(2^{n+1}-1)$, $c(n)=2^n/(2^{n+1}-1)$.
- Certified: Lemma R (game→scalar minimax of $D$), Lemma M (measure identity), Lemma P
  (cancelling pair), Lemma PEEL, Lemma SPLIT, Lemma ONE, Lemma TB (top-band decomposition),
  Lemma DM (elementary reductions, = DELETE/MATCH move set), Lemma U0 (even-mult corrector).
- Upper bound closed everywhere except the **balanced valley**: $m=n+1$ pieces (full budget,
  by U0(c)/DM-corollary), $a_1<L/2$ **and** $a_2<\beta_nL$ ($\beta_n=2^{n-1}/(2^{n+1}-1)\to1/4$).
- `breakpoint-vertex`'s Theorem VERT (proven, self-contained on Lemma M + an LP-vertex/
  hyperplane-arrangement rank count) says: an optimal Xiang refinement is a polytope vertex, so
  its positive parts fall into $\le n+1$ **distinct values** — collapsing the continuum of cut
  positions to a finite tie-pattern search. Corollary VERT-C: peeling the even-multiplicity
  classes (Lemma P) leaves a **core** of $\le n+1$ *distinct* residual values.

### Key structural fact I verified (not previously stated explicitly in the files)
Lemma DM's two moves (DELETE $x$, MATCH $(x,y)\mapsto x-y$) are **exactly** the local
breakpoint types that Lemma PL1/Theorem VERT prove are optimal (self-bisection resp. a tie to an
existing value). So VERT is the abstract/global justification that a DM-move-sequence framing
*can* reach the true optimum — the open question is only which sequence, not whether the move
set is rich enough. Concretely: starting from $m=n+1$ pieces with budget $n$, **both DELETE and
MATCH reduce the effective piece-count by exactly 1 per mark** (DELETE: piece removed, its two
cancelling halves contribute 0; MATCH: two pieces removed, one difference-piece added, net −1).
Hence *any* legal sequence of $n$ non-degenerate DM moves takes $n+1$ pieces down to exactly
**one surviving "core" residual value** $\rho$, and (by Lemma P/PEEL) $D(\text{final}) = \rho$
(if the core is genuinely a single leftover) — matching breakpoint-vertex's GAP-U-fin remark
("simultaneous even-pairing vertex response ... one core leftover $\rho$"). **This is the exact
shape the uniform vertex bound must take**: prove $\min(\text{achievable }\rho)\le u_nL$ over the
balanced valley, where "achievable" means reachable by *some* order of DM moves.

### Fresh opening (untested by any approach so far) — subset-sum pigeonhole, with a verified caveat
The denominator $2^{n+1}-1$ is exactly the number of gaps between the $2^{n+1}$ subset sums of
$n+1$ numbers sorted in $[0,L]$: the classical pigeonhole bound for the number-partitioning
problem says two of the $2^{n+1}$ subset sums differ by $\le L/(2^{n+1}-1)=u_nL$. This numerology
match is suggestive that the *真正* crux is a subset-sum pigeonhole, not a greedy differencing
rule (which is all that's been tried and refuted so far — see Dead ends). **However I checked
this numerically and it does NOT transfer for free**: not every $\pm1$ subset-sign pattern (hence
not every subset-difference value) is *reachable* by a legal sequence of pairwise nonnegative
differencing operations (DELETE/MATCH). Brute-force check on 4 random reals: of the $2^{4-1}=8$
distinct $\pm$-sign magnitude classes, only $2^{4-2}=4$ are actually attainable by some
differencing tree — exactly half. (Code run: `rec()` recursive all-orders search vs. brute-force
$\pm1$ sign enumeration; mismatch confirmed on 5/5 random trials.) So **the naive full
subset-pigeonhole argument is not directly valid** — Xiang cannot realize an arbitrary subset
partition with $n$ cuts, only a restricted "binary-differencing-tree-realizable" family (this
restricted family is presumably exactly VERT's finite vertex family, i.e. tied to the
combinatorial type/tie-pattern of $P_\tau$). The correct fresh lever is therefore: **characterize
which subset-difference values are cut-achievable (this should coincide with the vertex tie
patterns of Theorem VERT) and run the pigeonhole argument restricted to that achievable family**,
or restrict to a cleverly chosen sub-collection of $O(2^{n+1})$ subsets that IS achievable and
still forces a gap $\le u_nL$. This is genuinely new territory — no built approach has tried a
subset-sum/pigeonhole argument at all (the refuted "mass-threshold subset-cover" lever, per
current.md, was a cruder single-threshold search, not a full sorted-subset-sum gap pigeonhole).

### Is the vertex set "bounded independent of the profile"?
Yes in *distinct-value count* ($\le n+1$, Theorem VERT, profile-independent) but **no** in the
naive sense of "a fixed finite list of formulas covering all $A$": the combinatorial *type*
$\tau$ (how many cuts go to each original piece) and the *tie pattern* (which fragments equal
which existing values) range over a set whose size grows with $n$ (number of integer
compositions of $\le n$ into $\le n+1$ parts, times tie-graph choices). For fixed $n$ this is
finite, so per-$n$ it is a finite check (as breakpoint-vertex states), but it does **not**
collapse to an $n$-independent closed form — the outliner should expect the induction-on-$n$
structure (as in smoothing-majorization §3) to persist; VERT finitizes *within* one inductive
step, it does not eliminate the need for the recursion.

### LP / piecewise-linear structure (as proven, PL1 + VERT)
Confirmed genuinely proven (I re-checked the algebra of PL1's derivative computation
$g'(s)=2f(s)+2f(\ell-s)-2\in\{-2,0,2\}$ — correct) and VERT's rank-counting argument (Step 4:
$\mathrm{rank}\le N-d\Rightarrow d\le M$) is a correct, self-contained polytope-vertex argument.
No flaw found. This part of breakpoint-vertex is solid infrastructure; the remaining work is all
in §4B's GAP U-fin, not in re-deriving VERT.

### How U0's simultaneous-corrector budget interacts with vertex enumeration
U0(b) shows *full* cancellation (D=0) needs budget $\ge m$; at $m=n+1$ pieces with only $n$ cuts,
Xiang is exactly **one mark short** of total cancellation — this is precisely why the balanced
valley is the unique hard case (every other regime either has $m\le n$, trivially $D=0$ by U0, or
has $a_1$ large enough that a single DELETE/whole-tail move already reaches the bound). The "one
mark short" deficit is exactly the "one core leftover $\rho$" in the DM-move counting above — U0
and the DM piece-count argument are two views of the same fact. This gives a clean informal
picture for the outliner: **GAP U-fin = bound the unavoidable single leftover value in an
(n+1)-element, n-move signed-cancellation game**, which is the number-partitioning discrepancy
problem at exactly one merge short of full collapse.

### Distinct openings (summary)
1. **Restricted subset-sum pigeonhole** (new, above): characterize the cut-achievable
   sign-patterns/subsets (tie to VERT's tie-graph structure) and run a pigeonhole over that
   restricted family to get gap $\le u_nL$. Numerology ($2^{n+1}-1$ gaps) strongly suggestive;
   naive full pigeonhole refuted numerically (only half of $\pm1$ patterns are tree-reachable).
2. **Explicit vertex-formula enumeration per inductive step** (as VERT literally licenses):
   for the $m=n+1$, $a_1<L/2$, $a_2<\beta_nL$ regime, write down the (finitely many, but
   $n$-growing) vertex/tie-pattern values of $D$ as explicit affine functions of $A$ and show the
   min over patterns is $\le u_nL$ — heavier but the "textbook" way to cash out VERT; not yet
   attempted (only 3 ad hoc greedy DM rules were tried, a tiny slice of the full pattern space).
3. **KK-differencing / number-partitioning literature analogy**: recognizing DM's MATCH move as
   literally the Karmarkar–Karp differencing heuristic explains WHY "always match top two" (the
   textbook KK rule) fails badly (4.23×) — KK's poor worst-case ratio on balanced/near-uniform
   instances is a *known* phenomenon in the partitioning literature, not a coincidence specific to
   this problem. This reframes GAP U-VALLEY as "prove the TRUE optimum (not the KK heuristic) of
   an $(n+1)$-number differencing game is $\le u_nL$" — pointing toward openings 1–2 rather than
   any fixed greedy rule.

### Cheap-kill candidates
- None found that close the whole valley. The "one mark short of U0(b)'s full cancellation"
  observation is a clean structural fact (reframes GAP U-fin exactly as stated above) but is not
  by itself a bound — it only says a single residual is unavoidable, not that it's small.
- Parity/pigeonhole on $2^{n+1}$ subset sums is the natural candidate but (per above) needs the
  achievability restriction resolved first; it is NOT a free cheap kill as stated.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (knowledge_base.md, Algebra & Polynomials): the exact
  archetype PL1/VERT already generalize (breakpoints at zeros of sinusoid arguments ↔ breakpoints
  at ties/zeros in PL1); no new content to pull, but confirms the technique is a recognized KB
  pattern, so the outliner can cite it as the generic justification for "vertex/breakpoint
  minimization" alongside VERT.
- No dedicated KB entry for subset-sum pigeonhole / number-partitioning discrepancy was found;
  this would be new content the outliner has to prove from scratch (per crux-corpus norms).

### Analogous past problems (cruxes)
Searched crux corpus (`domain=combinatorics`, subtopics `games-and-strategy`,
`extremal-principle`, `processes-and-algorithms`, `pigeonhole`) for stick/cut/partition/
differencing/adversary-game analogues. Found many surface-keyword hits (aimo-0012, aimo-0015,
aimo-0451, aimo-1002, etc.) but on inspection none combine (a) an adversarial two-player claiming
game, (b) an alternating odd/even-rank sum objective, and (c) a stick-cutting move structure —
i.e. **none are genuinely analogous** to this problem's specific game; they are surface keyword
matches only (partition-counting, coloring-parity, or matching-cycle arguments unrelated to a
minimax cutting game). No forced match; report **none** as a true crux analogue for this lens.
The closest *conceptual* (not corpus) analogue is the classical Karmarkar–Karp / number-
partitioning discrepancy bound (external literature, not in this corpus), flagged as opening 3
above.

### Dead ends (do not retry)
- **Mass-threshold / subset-cover** (parity-measure-potential, refuted with counterexample
  $(0.44,0.281,0.279)$): a *fixed-threshold* rule, distinct from the full sorted-subset-sum-gap
  pigeonhole of opening 1 above — do not conflate the two; the pigeonhole idea has NOT actually
  been tried and refuted, only the cruder threshold version has.
- **Greedy DM rules** (smoothing-majorization round 6): "always MATCH top two" (4.23×), "always
  DELETE $a_1$" (25.5×), "MATCH if $a_2\ge\beta_nL$ else DELETE" (10.7×) — all refuted by direct
  numerics; I re-derived analytically why "always DELETE $a_1$" fails (residual bound
  $u_{n-1}(L-a_1)$ grows as $a_1\to0$, exceeding $u_nL$ once $a_1$ small — matches the observed
  blow-up). Confirms these are genuinely bad, not artifacts.
- **Sequential/cascading single-piece bisection** (breakpoint-vertex GAP U-fin note): refuted,
  4.7× on $n=5$ near-uniform profile.

### Prior progress
Both live approaches (smoothing-majorization, breakpoint-vertex) independently reduce the upper
bound to the *same* balanced-valley residual bound, stated in equivalent forms:
$\rho\le u_nL$ (breakpoint-vertex, "surviving-core bound via SPLIT cross term") /
GAP U-VALLEY (smoothing-majorization, four-case induction, cases 3.1–3.3 closed by exact
identities). This is the shared wall for 2+ rounds now (round 6 both "advanced" but this
specific gap unmoved) — consistent with the orchestrator's "3+ round shared-gap ⇒ try a genuinely
different framing" trigger. My openings 1–3 above are candidate different framings (subset-sum/
partition-discrepancy, rather than induction-with-a-fixed-move-rule), worth putting on the table
as at least one new rival approach rather than another variant of the DM-induction framing.

### Small-case / intuition notes (conjectural, numeric only)
- Balanced valley numerics (smoothing-majorization) confirm target IS achievable, worst DM ratio
  observed $0.75\times u_nL$ (i.e. some legal move sequence attains $\le u_nL$ every time tested)
  — so the claim is true; the difficulty is purely in finding a *profile-independent proof*, not
  in the truth of the bound.
- My own check: reachable differencing-tree magnitudes for $n$ reals number $2^{n-2}$ (out of
  $2^{n-1}$ sign classes) in the 4-element test — i.e. roughly half of all subset-difference
  values are actually legally reachable. This ratio (and its dependence on $n$) is worth the next
  round computing exactly (conjecture: reachable set size is $2^{n-2}$ for $n$ elements, i.e.
  exactly half — untested beyond $n=4$, small sample).
