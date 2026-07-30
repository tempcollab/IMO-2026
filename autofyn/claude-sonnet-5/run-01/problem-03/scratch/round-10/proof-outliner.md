## imo-2026-03

recursive-embedding-induction: revise
Target: For every n, against the geometric configuration A_n, every Xiang-Yu
response B (any budget, any split pattern) satisfies oddrank(B) ≥ c(n) =
2^n/(2^{n+1}-1) — i.e. A_n's value equals c(n) exactly (this is the whole
lower-bound half of the minimax, "c(n) ≥ 2^n/(2^{n+1}-1)", not a sub-lemma).
Technique: strong induction on the binary-subdivision-forest recursion
(already the spine of the certified Lemma TREE-BOUND / Lemma
TREE-BOUND-RESIDUAL), extending the induction hypothesis from "at most one
impure node in the whole forest" to "any finite number of impure nodes,
anywhere in the forest."
Skeleton:
  1. Restate Sub-lemma ODD's (TREE-BOUND-RESIDUAL's engine) induction
     hypothesis as: for every (m,r)-forest with ANY finite number of
     "impure" (non-anchor) leaves distributed arbitrarily through the
     forest, D(B) ≥ τ_m — dropping the "≤1 impurity" restriction entirely.
     This is a restatement, not new machinery — by multi-cluster explorer's
     structural read of the existing proof.
  2. Re-run the existing 3-case peeling step (impurity strictly below the
     top level / impurity aligned at the top level / impurity a top-level
     residual) verbatim, but now allow the "remainder" sub-forest X (the
     object the IH is applied to after peeling off the top level) to carry
     its own ≥1 impurities. Check line-by-line that no step of the existing
     proof actually used "at most one impurity in the whole forest" as
     opposed to "at most one impurity AT THIS LEVEL of peeling" — the
     explorer's read says it does not, but this must be verified rigorously,
     not just asserted, since it is the crux of the generalization.
  3. New case: p ≥ 2 impurities land at the SAME top level of the SAME
     forest pass simultaneously (this is the one case the existing proof's
     "at most one" scoping never had to handle, per multi-cluster explorer —
     it is not reachable by peeling one impurity off first). Formalize as
     B = [k' copies of τ1] ∪ X ∪ {y_1,c_1} ∪ ... ∪ {y_p,c_p}, X now fully
     pure (so D(X) ≥ τ_m by the ALREADY-CERTIFIED non-residual Lemma
     TREE-BOUND, unconditionally). Close via a "multi-pair insertion"
     generalization of D-INSERT: insert the p pairs one at a time in
     DECREASING order of companion size c_(1) > c_(2) > ... > c_(p) — each
     insertion is a single fresh application of the already-certified
     Lemma D-INSERT, so this is an induction on p (not new atomic
     machinery), reducing "p simultaneous impurities" to "p-1 simultaneous
     impurities plus one D-INSERT step," bottoming out at the already-closed
     p=1 case.
  4. Conclude the fully general Lemma PARITY-PAIR-GEN / Proposition K holds
     unconditionally for every n, every budget, every number of
     simultaneous tie-clusters — completing the lower bound
     "A_n's value = c(n)" in full, for every n.
Key lemmas (claim + mechanism):
  - Generalized Sub-lemma ODD (no impurity-count restriction) — because the
    peeling step's case analysis (top-level split into pure vs. impure
    trees, IH on the (m-1,r') remainder) never inspects how many impurities
    live inside that remainder; the IH is applied to the remainder as one
    opaque object regardless of its own impurity count.
  - Multi-pair insertion lemma (p simultaneous top-level impurities) —
    because inserting p pairs largest-companion-first is a literal
    induction on p using D-INSERT at each step, and the "pure X" base
    (D(X) ≥ τ_m) is already unconditionally certified via Lemma TREE-BOUND,
    so only the p pairs themselves need controlling, not the whole forest.
Open gaps: step 2's "no hidden use of the ≤1 restriction" verification;
step 3's multi-pair insertion lemma is the one genuinely new piece and is
NOT yet proved (only numerically evidenced, 21,875+ configs, zero
violations, per round-9 reviewer and round-10 multi-cluster explorer).
Cases to cover: p=2,3,... simultaneous top-level impurities (induction on p
should cover all p at once, but the base case p=1 and the inductive step
p→p+1 must both be checked explicitly); the boundary where companions tie
each other (c_(i) = c_(i+1)) — explorer's adversarial probe (forced
near-equal companions) found no violation but this exact edge must be
checked in the proof, not just numerically.
Watch out for: do NOT resurrect the round-9 "virtual fully-split domination"
comparison mechanism (proven FALSE, 159/600 violations) even as a component
of the multi-pair insertion step — the fix must be the direct D-INSERT
induction on p, not a comparison shortcut.

geometric-dominance-construction: revise
Target: Same as above (this is the lower bound's cross-verification twin) —
A_n's value = c(n) for every n, via the independent two-block/threshold
mechanism rather than forest-peeling.
Technique: iterated (nested) application of the already-certified Lemma
TWO-BLOCK across a decreasing sequence of distinct tie-values, one per
cluster.
Skeleton:
  1. Generalize Lemma TWO-BLOCK's Main Theorem from "one shared tie-value v
     across one subset S" to a finite decreasing sequence of tie-values
     v_1 > v_2 > ... > v_K (K disjoint clusters of pieces, pairwise disjoint
     index sets S_1,...,S_K, cluster l tied at v_l).
  2. Peel at threshold v_1: split the whole merged list L into Y_1 = {x >
     v_1} and Z_1 = {x ≤ v_1}. Since v_2 < v_1, every cluster-2..K
     companion lies inside Z_1, so Y_1 is determined purely by cluster 1's
     structure (plus whatever anchors exceed v_1) — apply the existing
     rank-shift identity D(L) = D(Y_1) + (-1)^{|Y_1|} D(Z_1) and the
     existing Structural Lemma to pin down Y_1's top elements exactly as in
     the K=1 case.
  3. Recurse: Z_1 is itself a merged list containing clusters 2..K tied at
     v_2,...,v_K — apply the (K-1)-cluster instance of the same theorem
     (induction on K) to Z_1 directly, i.e. threshold Z_1 at v_2, etc.
  4. New "K-block" structural lemma: identify, at each peeling level l, the
     top elements of Y_l as a function of which cluster (if any) owns each
     of the two globally-largest original pieces (index 0 and index 1 of
     A_n) — casework in "which cluster owns piece 0 / piece 1 / neither",
     roughly 2^K-ish combinations, but EACH case reduces to the identical
     single-block D-BOUND estimate already certified for K=1 (this is
     bookkeeping, not new atomic content, per altframing explorer's read).
  5. Combine all K levels: D(L) ≥ τ_n unconditionally by induction on K,
     base case K=1 already certified (Lemma TWO-BLOCK).
Key lemmas (claim + mechanism):
  - K-fold nested TWO-BLOCK — because thresholding at v_1 first isolates a
    piece of the list untouched by any lower cluster (v_2,...,v_K < v_1
    guarantees their companions can't cross above v_1), so the same
    rank-shift-by-|Y_1| identity used for K=1 applies verbatim, and the
    remainder Z_1 is exactly a (K-1)-cluster instance of the same problem.
  - K-block structural lemma (which cluster owns the two globally-largest
    pieces) — because the Structural Lemma's K=1 proof already does exactly
    this case analysis for one cluster; extending to K clusters is a
    2^K-ish enumeration of ownership patterns, each an instance of the
    already-proved single-cluster case.
Open gaps: the induction-on-K combination (step 3/5) and the K-block
structural lemma (step 4) are NOT yet written or proved — only the
mechanical roadmap is laid out here (per altframing explorer's structural
read of two-block-residue-close.md).
Cases to cover: K=2 first (write out fully, both cluster-ownership
sub-cases for pieces 0 and 1), then generalize to arbitrary K by induction;
must also handle the edge where a cluster's index set S_l straddles both
"contains piece 0 or 1" and "contains neither."
Watch out for: per round-10 outline-review guidance (implicit in the
altframing explorer's note), this round should be used primarily as a
CROSS-CHECK against recursive-embedding-induction's general theorem once it
exists, on the same concrete 2-4-cluster witnesses already stress-tested —
do not spend the whole round re-deriving a fully independent proof from
scratch a third time; if recursive-embedding-induction's general theorem
lands first, import it by reference and use TWO-BLOCK's K-fold extension as
verification only.

universal-adversary-strategy: revise
Target: c(n) ≤ 2^n/(2^{n+1}-1) for EVERY Liu Bang configuration A (not just
A_n) — the whole upper-bound half of the minimax, currently reduced to
Claim PTBI's Case C (p_1 < Σ(A)/2) for general piece-count m ≥ 4.
Technique: strong induction on m, replacing the failed "greedy largest-first
subset selection" mechanism with a genuine existence argument for a good
donor/subset match, per the PTBI explorer's two live openings.
Skeleton:
  1. State Case C's induction precisely: given A with m ≥ 4 pieces,
     p_1 < Σ(A)/2, budget m-1, show some sequence of ≤ m-1 marks produces B
     with oddrank(B) ≤ c(m-1)·Σ(A). Certified tools available: Lemma
     PAIR-VALUE (hypothesis-free value of an arbitrary tied-pair/subset
     match) and its SUBSET-DOM corollary; Lemma BLOCK-RECURSE; Lemma
     THRESHOLD-REDUCTION (already closes Cases A/B).
  2. FIRST attempt the Fact-0 reformulation (PTBI explorer's opening 2, not
     yet tried by any approach): since oddrank(A) = Σ(A) - evensum(A) and
     evensum is maximized over pairings of a FIXED multiset by the
     consecutive pairing (Fact 0, already proved), reframe Case C's target
     as: does there exist a budget-(m-1) sequence of splits whose RESULT's
     own consecutive-pairing evensum is ≥ (1-c(m-1))Σ(A)? This turns a
     discrete matching-existence question into a single scalar
     target-maximization question, potentially avoiding the Hall's-theorem
     formalization problem entirely. Test this reformulation numerically
     first (a cheap gate) before committing further effort, per the
     standing rule to derisk numerically before writing proofs.
  3. If Fact-0 reformulation does not yield a clean induction, fall back to
     a genuine existence argument for a good donor/subset match: NOT via
     textbook 1-1 SDR Hall's theorem (PTBI explorer found the object is a
     subset-sum/exact-cover structure, not literal 1-1 matching) but by
     adapting crux aimo-0063's "iterate Hall-deficient-set deletion": build
     the natural bipartite/hypergraph object (donors vs. candidate target
     subsets), and when a direct match doesn't exist, delete the
     Hall-violating side and recurse on the remainder — this crux move is
     directly analogous per the explorer's report and should be worked out
     concretely for this problem's specific subset-sum structure (not
     assumed to transfer without modification).
  4. Alternative induction shape (PTBI explorer's opening 3, untested):
     induct on m peeling off the PAIR (p_1,p_2) jointly rather than p_1
     alone, motivated by the m=5 witness's winning move (p_2 pairs with
     {p_4,p_5} while p_1,p_3 are independently halved) — try this as a
     second skeleton if steps 2-3 stall.
  5. Verify the resulting general construction against BOTH mandated hard
     m=5 witnesses (A=(12,6,5,4,2)/29 and the round-7 witnesses) and confirm
     it does not regress the now-fully-closed m=3 case.
Key lemmas (claim + mechanism):
  - Fact-0 rescoping of Case C — because evensum(B) for ANY reachable B is
    upper-bounded by the max-sum-of-mins over ALL pairings of B, so the
    existence question becomes "is there a reachable B whose natural
    consecutive-pairing evensum clears the threshold," which may admit a
    direct extremal/greedy argument on evensum itself even where subset
    selection resists greedy.
  - Hall-deficient-set-deletion existence argument (adapted from aimo-0063)
    — because when a direct simultaneous match of donors to target subsets
    fails Hall's condition, the standard fix is not to abandon matching but
    to strip the violating subset and its neighborhood and recurse on a
    strictly smaller instance, which composes naturally with the strong
    induction on m already in place.
Open gaps: the entire Case C existence argument remains open; both routes
(steps 2 and 3) are untested/unproved this round, though PTBI explorer's
300-trial exhaustive-search + simulated-annealing found zero counterexamples
to Claim PTBI at m≤6, so the target is very likely true.
Cases to cover: m=4 fully worked by hand first (smallest untested case)
before attempting general m; the boundary where multiple simultaneous
non-conflicting donor actions are needed (as in the m=5 witness) must be
handled by whichever mechanism is chosen, not special-cased away.
Watch out for: do NOT propose greedy largest-first subset selection again —
cheaply falsified this round (74% violation rate over 2000 trials,
reproduces only the suboptimal BLOCK-RECURSE value on the certified m=5
witness). Do NOT assume classical 1-1 SDR Hall's theorem applies directly
without first checking whether the bipartite object is genuinely a 1-1
matching or a subset/hyperedge structure (PTBI explorer's caveat) — verify
the formalization is correct before citing the theorem in a proof.
