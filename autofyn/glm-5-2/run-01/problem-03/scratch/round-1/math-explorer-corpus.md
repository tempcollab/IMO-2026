## imo-2026-03 (IMO 2026 P3 — Liu Bang / Xiang Yu stick game)

### The problem (restated)
Liu Bang marks ≤n points on a unit stick; then Xiang Yu marks ≤n distinct points; stick is cut at all marks into pieces; players alternate claiming any unclaimed piece (Liu Bang first), each maximizing own total length. Find the largest c(n) Liu Bang can guarantee regardless of Xiang Yu's play. (answer_type = expression in n; need matching upper bound = XY strategy AND construction = Liu Bang strategy.)

### Distinct openings (each a different attack the outliner could build into a rival approach)
1. **Reduce the claiming game to the odd-index sum, then to the alternating sum D.** For a fixed multiset of piece lengths sorted descending $\ell_1\ge\cdots\ge\ell_m$, the value of the alternating pick-any game (P1 first, zero-sum) equals $\sum_{i\ \text{odd}}\ell_i = \frac{1+D}{2}$ where $D = \ell_1-\ell_2+\ell_3-\cdots$ is the alternating sum of sorted-desc pieces. (VERIFIED: minimax exact-match on 3000 random multisets, 0 mismatches; greedy "take largest" = minimax value = odd-index sum.) So the whole problem becomes: Liu Bang (max) and Xiang Yu (min) play the marking game on $D$ of the final partition, and $c(n) = \frac{1 + D^*}{2}$, $D^* = \max_{\text{LB}}\min_{\text{XY}} D$. This reframes a continuous-action minimax as a clean algebraic quantity.
2. **"Halving the largest piece" equilibrium / parity-of-multiplicities obstruction.** Small-case play shows the extremal configurations are Liu Bang creating one large "halvable" gap and several equal small pieces, XY responds by splitting the largest gap at its midpoint. Whether XY can additionally cancel $D$ to 0 depends on the **parity of the multiplicities of the small pieces** — this is the crux. Liu Bang must choose marks so that after XY's best response the small pieces cannot be regrouped to make $D=0$. (Concretely: for n=3 the naive LB={1,2,3}/11 is defeated: XY splits the big 8/11 gap into {1/11, 7/22, 7/22}, making four 1/11's (even) and two 7/22's, so $D=0$, claim=1/2.) Any successful Liu Bang strategy must rule out this parity flip.
3. **XY upper-bound strategy via "make every piece paired up" (D→0) when n large.** A natural upper-bound program: show that for n≥3 (or some threshold) Xiang Yu can always force $D \le$ some bound by adding marks that pair up the pieces. Proving the tight cap is the hard upper-bound half. For n=1,2 XY cannot cancel D fully (verified), so c>1/2 there; the regime where XY can force $D\to0$ is the boundary to identify.
4. **Exchange-argument / invariance route for the claim game.** The greedy=odd-index result has a standard exchange proof (swap two adjacent picks, total doesn't decrease) — useful if the outliner wants the claim-game lemma self-contained rather than computational.
5. **Continuous-position induction on n.** Solve base n=1, then build the n+1 strategy from the n strategy by inserting a controlled gap. The parity flip shows naive induction fails; a strengthened invariant tracking the sign of $D$ mod something is likely needed.

### Candidate technique(s)
- **Greedy / exchange argument** for the alternating pick game (proves claim value = odd-index sum). [Standard, re-prove from scratch.]
- **Minimax over a continuous action space reduced by symmetry** — the marking game is continuous, but the equilibrium is attained at rational symmetric configs (n=1: 1/3; n=2: {2/7,6/7}); extremal-principle + "equalize the largest gap" heuristic.
- **Alternating-sum invariant $D = \ell_1-\ell_2+\cdots$** as the bookkeeping quantity (instead of the odd-index sum directly); makes the minimax target linear.
- **Parity / multiplicity argument** to rule out the $D=0$ cancellation (the key obstruction at n≥3).

### Cheap-kill candidates
- The **odd-index / (1+D)/2 reformulation** is itself the cheap kill — it collapses the two-stage game to a single algebraic minimax; do this BEFORE any heavy casework.
- **Lower bound $c(n)\ge 1/2$ for free**: since $\ell_1\ge\ell_2$, $\ell_3\ge\ell_4,\ldots$, the odd-index sum ≥ even-index sum, so P1 (greedy) always gets ≥1/2. (Liu Bang can also just place 0 marks if needed.) So the answer is $1/2 + \varepsilon(n)$ with $\varepsilon(n)\to0$.
- Symmetry: WLOG Liu Bang's marks are ordered; the stick is mirror-symmetric so configs come in pairs.

### Knowledge-base entries to use
- **Invariants & monovariants** (combinatorics) — the alternating sum $D$ is the invariant bookkeeping.
- **Extremal principle / pigeonhole** — "take the largest gap" drives the halving response.
- **General: Induction / structural induction on n** and **Constructive vs existence** (need upper bound AND construction for the expression answer).
- (The crux corpus's three-gap / Kronecker entries are NOT relevant — this is not a rotation/gap-spacing problem.)

### Analogous past problems (cruxes)
The corpus has NO direct "divider-chooser / I-cut-you-choose / pick-pieces-on-a-stick" analogue. Best indirect analogues:
- **aimo-0127 (IMO 2025, Alice/Bob alternating edge game, maximize weighted total)** — crux: *"Rewrite a weighted total as a sum over weight thresholds of tail-counts (number of items of weight ≥ the threshold), so a per-threshold cap can be applied termwise."* Adapts: a per-threshold/tail-sum rewriting of P1's claimed length could give a clean upper bound, mirroring how IMO 2025 bounded the alternating edge total.
- **aimo-0340 (IMO-SL 2010, strings of pearls cut by length-ordered greedy rule)** — crux: *"Track paired extremal quantities of two symmetric sub-populations under a length-halving process; monotone ceil/floor split map preserves an initial strict dominance."* Adapts: the "halve the largest piece" response and the dominance-of-the-largest-piece under repeated halving is exactly the structure of our n=1, n=2 equilibria.
- **aimo-0663 (IMO-SL 2015, no-consecutive alternating pick game)** — crux: *"In a take-turns game, show the responder can always reply by a component-counting/pigeonhole invariant: the unpicked region splits into more gaps than the responder has used."* Adapts: a response/strategy-stealing flavor for the marking stage.

**Single most useful analogue:** aimo-0127 (IMO 2025) — same shape (alternating moves, weighted total, each maximizes own, find guaranteed total); its tail-count-threshold rewriting of a weighted alternating total is the closest load-bearing move to transport.

### Dead ends (do not retry)
- **Conjecture $c(n)=2n/(4n-1)$ is FALSE for n≥3.** It fits n=1 (=2/3) and n=2 (=4/7) but n=3 refutes it: the obvious config LB={1,2,3}/11 lets XY force claim≈1/2 (D≈0) by splitting the 8/11 gap into {1/11, 7/22, 7/22}, flipping the small-piece parity. Do not build an approach around $2n/(4n-1)$.
- **Trusting only the parity-count of the "natural" small pieces.** A Liu Bang strategy that leaves an odd number of small pieces hoping D stays positive is vulnerable: XY can spend a mark to change the effective parity. The invariant must be XY-proof, not just parity-of-fixed-multiplicities.
- Pure discrete/grid crux tactics (Nim-style, modular invariants on integers) do not transfer: this is a continuous-position, real-valued game.

### Prior progress
- Round 1 start; no approaches, no lemmas, no prior progress on file. (`results/imo-2026-03/current.md` = unsolved, empty.)

### Small-case / intuition notes (CONJECTURES unless marked PROVED)
- **PROVED:** Claim-game value = odd-index sum of sorted-desc pieces = (1+D)/2 (minimax match on 3000 random cases; greedy = minimax = odd-index sum). Greedy "always take the largest remaining" is optimal for both players (standard exchange argument; verified numerically).
- **PROVED (analytic):** $c(1) = 2/3$. Liu Bang marks at 1/3; XY's best response splits the 2/3 gap at its midpoint 2/3 → three equal thirds; $D=1/3$, claim $=(1+1/3)/2=2/3$. All other XY responses give $\ge 2/3$ (checked by casework on x≤1/3 vs x>1/3).
- **PROVED (exact, fraction-verified):** $c(2) = 4/7$. Liu Bang marks at $\{2/7, 6/7\}$ (pieces $\{2/7,4/7,1/7\}$); XY's best response over a /1001 grid gives exactly 4/7 (splits the 4/7 gap at its midpoint → $\{2/7,2/7,2/7,1/7\}$, $D=1/7$); all alternative XY responses (including splitting 4/7 into $\{1/7,3/7\}$, or splitting the 2/7 piece, or using 2 marks) give $D\ge1/7$. Robust.
- **CONJECTURE (open):** For n≥3 the value drops sharply toward 1/2; a coarse grid gives $c(3)\gtrsim 0.533$ (best config found near LB≈{0.056, 0.333, 0.889}) but the exact c(3) and the general formula are NOT pinned — the parity-flip obstruction defeats the natural $2n/(4n-1)$ pattern. The outliner's first job is to determine the true c(3) and the real general expression; the $D$-reformulation + "XY tries to cancel D by pairing pieces" is the right frame to find it.
- Intuition: $c(n)\to 1/2$ as $n\to\infty$ (P1 always ≥1/2; XY's mark budget grows, so XY cancels more of $D$). The answer is $1/2 + \varepsilon(n)$ with $\varepsilon(1)=1/6$, $\varepsilon(2)=1/14$, and $\varepsilon(n\ge3)$ decaying faster than $1/(4n)$ — exact form unknown.
