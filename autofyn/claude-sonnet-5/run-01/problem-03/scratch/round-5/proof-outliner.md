## imo-2026-03

recursive-embedding-induction: advance
Target: Full theorem — c(n) = 2^n/(2^{n+1}-1) is exactly Liu Bang's guaranteed
value, both directions, for every n. (This approach owns the lower-bound
half; upper bound over arbitrary configs is out of its scope, handled by
universal-adversary-strategy.)
Technique: Reduction via Lemma 1 (claiming-phase odd-rank value) + Lemma V'
(LP-vertex reduction to integer anchor vectors) + the D-REFORM/D-BOUND/
D-INSERT alternating-sum toolkit, closing the k=n tail-untouched sub-case
(Lemma L) by strong induction on n that peels off the top block.
Skeleton:
  1. (Certified) Lemma V' reduces Proposition K's k=n, tail-untouched
     sub-case to Lemma L: for integer vector a=(a_1,...,a_n), Σa_i=n+1,
     Σ a_i t_i = 2t_1 where t_i=2^{n-i}, the merged multiset has D≥t_n=1.
  2. NEW STEP — peel-the-top-block induction (this round's target):
     let c_1=a_1+1 be the multiplicity of the top value t_1 in the sorted
     merge. By Lemma D-INSERT, block 1 contributes ±t_1 to D if c_1 is odd,
     0 if c_1 is even, and shifts the starting parity for the remaining
     block. Strip block 1; the remainder is a multiset built from
     t_2,...,t_n with total extra multiplicity (n+1-c_1), and by Lemma 3's
     self-similarity, t_2,...,t_n = t_1/2 · (2^{n-2},...,1,1/2^{... }) is
     literally the level-(n-1) geometric tail rescaled by 1/2 — apply the
     induction hypothesis (Lemma L at n-1) to the remainder, using Lemma G1's
     exact recursion c(n)=2λ_n c(n-1) to translate scales. Case-split on
     parity of c_1 (odd: block-1 nets ±t_1, remainder needs D≥ -t_1+t_n or
     similar signed bound depending on which sign; even: block-1 nets 0,
     remainder alone must satisfy D≥t_n) and on whether a_1=0 (already
     covered by k<n cases) vs a_1≥1.
  3. Base case n=1: Lemma G0 (already certified, closes n=1 for every k).
  4. Conclude Lemma L for all n by induction; this closes k=n, tail-
     untouched, for the lower bound.
  5. (Separate, still-open beyond this round) k=n with tail also refined,
     and general k with 1<k<n — flagged as remaining sub-gaps of the same
     overall claim, targeted by geometric-dominance-construction in parallel
     using the same certified toolkit.
Key lemmas (claim + mechanism):
  - Lemma L (target of this round) — because peeling the top block reduces
    the (n+1)-part composition of 2^n to an (n)-part composition of 2^{n-1}
    on the self-similar half-scale tail, so the same claim recurses; the
    parity of the top block's multiplicity c_1 controls the sign contributed
    to D, giving a clean two-case induction instead of an unbounded case
    search over all a-vectors.
  - Lemma D-INSERT (certified) — exact single-insertion recursion for the
    alternating sum D under adding one more copy of a value to a sorted
    multiset; this is the mechanism that makes "peel the top block" tractable
    (it converts a global rank computation into a local block computation).
Open gaps: the parity case-split in Step 2 is not yet written out in full
(need to verify both odd-c_1 and even-c_1 sub-cases actually give a
sufficient inequality, not just a plausible one — the explorer flagged this
as untested); the extension of Lemma L beyond tail-untouched (k=n with tail
also split) is not attempted here.
Cases to cover: parity of c_1 (odd / even) x whether a_1=0; base case n=1.
Watch out for: the induction must apply Lemma L at n-1 to the *rescaled*
tail (factor 1/2 via Lemma 3), not to a differently-normalized object — get
the scaling exactly right when combining with Lemma G1's c(n)=2λ_n c(n-1);
also do not fall back to a sums-only bound (Rules: proven false by the
round-2 counterexample).

geometric-dominance-construction: advance
Target: Same full theorem, lower-bound half. This approach owns the general
"doubling family" claim (all 0≤k≤n, tail possibly refined), of which Lemma L
(owned in parallel by recursive-embedding-induction) is exactly the k=n
instance — confirmed identical this round by the lemmaL explorer via direct
substitution (C_n = {p_2,...,p_n,p_{n+1},p_{n+1}} = Lemma L's canonical
vector).
Technique: exchange/local-move argument directly on the (k+1)-part
composition vector of p_1 (the "doubling family" C_k), rather than an
abstract T-agnostic scalar bound (Claim ★'s route, now proven insufficient
for s≥3 by an exact counterexample this round, and a strengthened 3-scalar
version — max, oddrank, Σ(T) — also proven insufficient by this round's
explorer). Must use the tail's actual ratio-2 self-similar structure.
Skeleton:
  1. (Certified) Insertion Lemma, rank-shift-by-s, Claim ★ for s∈{1,2}
     closes k≤1 (with simultaneous tail-splitting, unconditional n≤2,
     conditional general n).
  2. NEW STEP — for general k, define the doubling family C_k and show by a
     single-unit exchange argument that moving one unit of multiplicity
     between adjacent a_i, a_{i+1} coordinates of ANY composition vector of
     p_1 (subject to the two linear constraints: total parts = k+1, total
     value = p_1) never increases oddrank(merge), with the canonical/doubling
     vector as the unique local (hence global, by connectivity of the
     exchange graph on this constraint polytope) minimum.
  3. Once the exchange argument establishes k=n's case is exactly Lemma L
     (already the target of recursive-embedding-induction — import that
     result once certified rather than re-deriving), extend the same
     exchange argument to k<n by allowing the tail to also carry some of the
     "leftover" multiplicity, again via local exchange, closing the doubling-
     family conjecture for every 0≤k≤n.
  4. Combine with the arbitrary-Xiang-Yu-response framing (Lemma 1's game
     value = odd-rank sum for the FIXED resulting multiset) to conclude the
     lower bound c(n) is achieved against Liu Bang's geometric construction
     A_n for every legal Xiang Yu play.
Key lemmas (claim + mechanism):
  - Doubling-family minimality (target) — because the exchange argument
    shows any deviation from the canonical vector can be "undone" by a
    single local move that strictly does not increase oddrank(merge) (a
    discrete convexity/rearrangement fact on the constrained polytope of
    integer composition vectors), so the polytope's unique combinatorial
    vertex reached by the doubling construction is the true minimizer.
Open gaps: the exchange-monotonicity claim in Step 2 is untested (the
lemmaL explorer flagged "verify computationally whether single-unit local
exchange actually monotonically decreases D... for n up to ~10" as the
fastest derisking check, not yet done); extending from k=n to general k<n
in Step 3 needs the tail-refined case of Lemma V', not yet verified to carry
over (flagged open in current.md gap 1).
Cases to cover: k=0,...,n; tail untouched vs. tail also refined.
Watch out for: do NOT retry the 2-scalar (max,oddrank) or 3-scalar
(max,oddrank,Σ) abstraction for s≥3 — both proven false this round by
explicit counterexamples (exact-Fraction, Λ/q ratios 1.0–1.9). Coordinate
tightly with recursive-embedding-induction: once either proves the k=n case
(Lemma L), the other should import it by reference rather than re-deriving,
per the CLAUDE.md shared-lemma-cache rule.

universal-adversary-strategy: advance
Target: Same full theorem, upper-bound half — for EVERY Liu Bang
configuration A (not just geometric), Xiang Yu has a strategy limiting Liu
Bang to ≤ c(n)·Σ(A), for general n.
Technique: strong induction jointly on (number of unprocessed pieces m,
remaining mark budget r), applying a cascading DOM→HALVE→DOM sequence to the
current top piece of whatever remains, using the newly-identified
boundary-slack fact that Lemma DOM's r=0 boundary case only costs k-1 marks
(not k).
Skeleton:
  1. (Certified) Lemma DOM: if p_1≥Σ(rest)=S, k marks suffice to force
     oddrank(B)=p_1 exactly (any tail shape). Lemma HALVE: if p_1≥2p_2, one
     mark suffices to force oddrank(B_0)=p_1/2+oddrank(tail'). Both close
     n=1 for arbitrary configs.
  2. NEW LEMMA — DOM-boundary-slack: in the r=0 sub-case of Lemma DOM (i.e.
     p_1 = S exactly, no leftover budget to "waste"), the same domination
     value is achieved using only k-1 marks — one mark cheaper than the
     generic case — because the last of the k splits becomes unnecessary
     when the remaining piece to split off already equals the target
     exactly (formalize the DOM construction's mark count as a function of
     whether the final residual is 0 or positive).
  3. NEW STEP — cascading recursion on (m,r): define the strategy
     recursively: on the current unprocessed tail (with its own budget r'),
     (a) if p_1≥S, apply DOM (using k marks, or k-1 if the boundary r=0
     case of Step 2 applies) and stop — the whole tail is dominated exactly;
     (b) else if p_1≥2p_2, apply HALVE using 1 mark, recurse into the new
     tail with budget r'-1; (c) else (neither DOM nor HALVE's hypothesis
     holds, e.g. near-tied top two pieces) — this round's explorer found
     cases where the optimal move skips p_1,p_2 and acts on a deeper piece
     instead; this sub-case needs its own lemma (not yet proven) bounding
     the achievable oddrank without touching the top.
  4. Prove by induction on m (number of pieces) — with r as a secondary
     resource tracked at each step, decreasing by exactly the marks spent —
     that this cascade always forces oddrank(B) ≤ c(n)·Σ(A), using Step 2's
     mark-saving fact to make the budget accounting exact rather than merely
     an inequality.
Key lemmas (claim + mechanism):
  - DOM-boundary-slack (new, needs proof) — because when p_1=S exactly, the
    DOM construction's final split step is forced to produce a
    zero-remainder piece, which can be folded into the previous split
    without using an extra mark (an off-by-one in the generic DOM
    construction's mark count).
  - Cascade sufficiency (target, hardest step) — because applying DOM/HALVE
    greedily top-down, recursing into whatever tail remains with whatever
    budget remains, provably never does worse than any other allocation of
    Xiang Yu's marks; the mechanism is a joint two-index well-founded
    induction (m,r), NOT induction on n alone (per rule from round 3).
Open gaps: case (c) in Step 3 (neither DOM nor HALVE fires) is the newest
and most concrete unresolved sub-case — the explorer's near-tied-top-two
numeric example shows the optimal move can skip the top entirely; this
needs its own construction/lemma before the cascade induction can close.
Cases to cover: p_1≥S; p_1≥2p_2 (but p_1<S); neither (near-tied case).
Watch out for: do not default to "induction on n" — must be the joint
(m,r) induction (memory rule from round 3); verify the DOM-boundary-slack
mark-saving fact rigorously (not just on the two numeric examples the
explorer found) before relying on it for the budget accounting.

potential-averaging-bound: new
Target: Same full theorem, upper-bound half — for every Liu Bang
configuration A and every n, Xiang Yu can force oddrank(B) ≤ c(n)·Σ(A),
proved via an averaging/potential argument instead of exact-minimizer
casework.
Technique: borrowed and adapted crux move from aimo-0198 (Liar's guessing
game) — "bound a greedy minimizer's outcome by the average of its two (or
more) available candidate strategies: min(strategy_1, strategy_2) ≤
(strategy_1 + strategy_2)/2." Applied here: Xiang Yu, as the party trying to
minimize oddrank(B), has at least two explicit, always-available candidate
plays at every recursive step (a cascading-DOM play and a cascading-HALVE
play, in the fully recursive/cascading forms from universal-adversary-
strategy, not the flat single-shot forms) — if the AVERAGE of the two
candidates' resulting oddrank already meets the target bound, Xiang Yu (who
picks the better of the two, hence does at least as well as the average)
automatically meets it too, without needing to determine analytically which
candidate is truly optimal in each regime.
Skeleton:
  1. Import Lemma DOM and Lemma HALVE (certified) in their cascading/
     recursive forms (as being developed by universal-adversary-strategy's
     Step 3 cascade, or independently re-derived here if that's not ready
     yet — this approach can proceed with the FLAT forms first as a
     simpler warm-up, then graduate to cascading forms).
  2. State the averaging inequality target: for every config A,
     (cascading-DOM-value(A) + cascading-HALVE-value(A)) / 2 ≤ c(n)·Σ(A).
  3. Prove this by induction on n, using the two candidates' own recursive
     identities (DOM: oddrank=p_1; HALVE: oddrank=p_1/2+oddrank(tail)) to
     express the average in closed form and bound it using the induction
     hypothesis on the (n-1)-piece tail.
  4. CAUTION (explorer-verified this round): the naive average of the FLAT
     (non-cascading) DOM and HALVE values does NOT always meet the bound in
     the region where neither hypothesis (p_1≥S nor p_1≥2p_2) fires — a
     first numeric spot-check found violations there. So Step 3 must use
     genuinely cascading/recursive versions of both candidates (each
     candidate itself recursing into the tail with its own remaining
     budget), not the single-shot flat identities alone; if even the
     cascading pair's average fails in some residual region, a third
     candidate strategy (targeting exactly the "near-tied top two" case
     that both universal-adversary-strategy and this round's explorer
     flagged) must be added to the averaging set (min over 3, not 2,
     candidates — average of the two closest to optimal, or a weighted
     combination).
  5. Conclude Xiang Yu's actual best response is ≤ the average of the
     available candidates ≤ c(n)·Σ(A), giving the upper bound for every n
     without needing to pin down region-by-region which of DOM/HALVE/other
     is exactly optimal.
Key lemmas (claim + mechanism):
  - Averaging bound (target) — because Xiang Yu is a minimizer over a set of
    strategies that includes both candidates, min ≤ average always holds by
    definition of minimum; this converts a hard "prove X is optimal in this
    regime" case-split into an easier "prove the average of two suboptimal-
    but-explicit strategies already clears the bar" additive argument — the
    crux move transferred from aimo-0198.
Open gaps: whether averaging cascading-DOM and cascading-HALVE (rather than
flat) suffices is untested; the near-tied-top-two region may need a third
candidate strategy not yet constructed. This is the most exploratory
approach in the field this round — treat its first build as a feasibility
probe (does the averaging inequality hold numerically at all for cascading
candidates, n=2..5?) before committing to a full proof.
Cases to cover: same regimes as universal-adversary-strategy (DOM-firing,
HALVE-firing, neither); if neither fires, this is exactly where a third
candidate is needed.
Watch out for: this is a genuinely different proof SHAPE (additive/
averaging vs. exact casework) from every other live approach — its value is
diversity even if it doesn't fully close the gap this round; do not
silently fall back to exact-minimizer casework, which would collapse it
into a copy of universal-adversary-strategy.
