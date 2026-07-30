# math-explorer — Case (b): Xiang splits the tower's top piece

**Lens:** Close the lower-bound case (b) — prove D >= 1/D_n (tower units: D >= 1) when
Xiang splits the top piece 2^n of T_n, for arbitrary (unbalanced, multi-) fragmentation.

All computation below uses **tower units** (tower T_n = (2^n, ..., 2, 1), total D_n =
2^{n+1}-1; target D >= 1). Real units = tower units / D_n.

---

## (a) Exact effect of one split on N(t) and D

### The split's effect on N(t)

Split a piece of length L into p >= q (p + q = L). The change in N(t) = #{pieces >= t}
is:

  delta_N(t) = +1 on [0, q],   0 on (q, p],   -1 on (p, L].

Intuition: the new smaller piece q contributes +1 to the tail count below q (two new
pieces vs. one old); the removed range (p, L] loses the old piece's contribution (-1);
the middle range is unchanged.

### The split's effect on D = integral(N(t) mod 2) dt

Since N mod 2 is **nonlinear**, the change in D is NOT integral(delta_N mod 2). Both the
+1 on [0,q] and the -1 on (p,L] **flip the parity** of N there. Computing exactly:

  delta_D = integral_{[0,q]} (1 - 2*(N mod 2)) dt  +  integral_{(p,L]} (1 - 2*(N mod 2)) dt

The integrand is +1 where N is **even** (parity even->odd, gaining for D) and -1 where N
is **odd** (parity odd->even, losing from D). Define O(I) = total width where N is odd on
interval I. Then:

  **delta_D = 2q - 2*O([0,q]) - 2*O((p,L])**

**Verified** for all splits of the top of T_3 against direct alt-sum recomputation (0
mismatches). This is the load-bearing formula.

### The parity-coupling obstruction, made precise

The same split flips parities on **two disjoint ranges** ([0,q] and (p,L]) whose
odd-widths O are determined by the **global** N(t) structure, not by the split locally.
Xiang controls q (and hence p), but O([0,q]) and O((p,L]) depend on where q and p fall
relative to the tower's step-function breakpoints (2^0, 2^1, ..., 2^n). This is the
coupling: the split's benefit depends on the parity landscape over a long range of t.

### Special case: balanced split of the top (q = p = 2^{n-1})

Here [0, q] = [0, 2^{n-1}] covers all tower intervals j = 0, ..., n-1, and (p, L] =
(2^{n-1}, 2^n] is the top interval (j = n, N = 1, odd, width 2^{n-1}). The parity flips
on the **entire** range [0, 2^n]. This gives the clean identity:

  **D_new = 2^n - D_old = D(T_{n-1})**

(Verified for n = 1, ..., 6.) Mechanism: the new multiset is {2^{n-1}, 2^{n-1},
2^{n-1}, 2^{n-2}, ..., 1} — three copies of 2^{n-1} plus T_{n-1}. The first two copies
pair up at positions 1, 2 (cancel in D). The third copy starts T_{n-1} at position 3
(odd). So D = 0 + D(T_{n-1}).

### Is the balanced split the minimizer?

For a **single** split of the top, D is piecewise-linear (constant or linear) in q within
each combinatorial type (fixed sorted order). For T_3: D = 5 (constant) for q in (0, 1];
D = 7-2q (linear decreasing) for q in (1, 2]; D = 3 (constant) for q in [2, 4]. The
balanced point q = 4 is **on the plateau** of the minimum — it is as good as any q in
[2,4] but not uniquely optimal. No unbalanced single split beats it.

For **two** splits, balanced is strictly better: balanced cascade (8->4+4, 4->2+2)
gives D = 1, while unbalanced (8->5+3, 4->3+1) gives D = 3.

---

## (b) Most promising route to close case (b) — ranked

### Route 1 (MOST PROMISING): Variational minimum at breakpoint + frontier recursion

**The argument shape:**

1. **Piecewise-linearity.** D is piecewise-linear (constant or linear with slope in
   {-2, 0, +2}) in each split position q, within a fixed combinatorial type (sorted
   order). Verified analytically for T_3 single-split (three types: constant, linear,
   constant). The breakpoints are at tower-piece values (where the fragment q crosses a
   tower piece in sort order).

2. **Minimum at a breakpoint.** A piecewise-linear function on a compact feasible region
   attains its minimum at a breakpoint (where the type changes) or on a plateau touching
   a breakpoint. So WLOG the global minimum of D over all <= n-mark refinements is at a
   config where every split is at a breakpoint — i.e., every fragment **ties** with an
   adjacent piece in the sorted order.

3. **Frontier recursion.** Among **dyadic** breakpoint configs (all pieces are powers of
   2), the only way to split 2^k into two powers of 2 is 2^{k-1} + 2^{k-1} (since
   2^a + 2^b = 2^k forces a = b = k-1). So dyadic breakpoint configs are exactly the
   **frontiers** (balanced-split configs). Computation confirms: **all frontiers give
   D >= 1** for n = 3, 4, 5, 6, with minimum D = 1 at the tight frontier {2, 3, ..., n}.
   The frontier D values satisfy: min D among frontiers with topmost unexpanded level m
   is exactly D(T_m), and D(T_m) = 2^m - D(T_{m-1}) (recursion), with D(T_0) = D(T_1) = 1.

**Where it gets stuck:** Step 2 constrains the minimizer to a **breakpoint** config, but
NOT necessarily a **dyadic** one. Non-dyadic breakpoints exist: for n=3 on a 1/8 grid,
121 configs achieve D = 1, of which only 1 is dyadic (the frontier {4,4,2,2,1,1,1}). The
other 120 have non-dyadic fragments (e.g., {39/8, 4, 2, 2, 1, 1, 1/8}) that tie with
adjacent tower pieces at breakpoints but are not powers of 2. The argument must show
D >= 1 at ALL breakpoint configs, not just dyadic ones.

**How to push past the stuck point:** The variational argument plus the exact delta_D
formula give a path. At a breakpoint, the fragment q equals an adjacent piece r. The
delta_D formula becomes 2r - 2*O([0,r]) - 2*O((L-r, L]). If we can show that for ANY
tower-piece value r that the fragment ties with, this delta_D (accumulated over all
splits) cannot push D below 1, the bound follows. The frontier analysis proves it for
dyadic breakpoints; the non-dyadic breakpoints need a separate (possibly simpler)
argument — they live on plateaus where D is already at the frontier value.

**Sub-steps for a builder:**
- (i) Formalize piecewise-linearity of D in split positions (provable by tracking how
  the sorted order changes as q varies).
- (ii) Prove the minimum is at a breakpoint config (compactness + PL structure).
- (iii) Prove the frontier recursion: D(T_m) = 2^m - D(T_{m-1}), D(T_0) = D(T_1) = 1, and
  min-over-frontiers = D(T_m) for topmost unexpanded level m.
- (iv) Handle non-dyadic breakpoints: show they lie on plateaus connecting to dyadic
  breakpoints, so D at a non-dyadic breakpoint = D at a nearby dyadic breakpoint >= 1.

### Route 2: N(t)/parity-integral per-split telescoping (tail-count's forte)

Using the exact formula delta_D = 2q - 2*O([0,q]) - 2*O((p,L]), one seeks a per-split
lower bound on D that telescopes over <= n splits. The balanced split gives D -> D(T_{n-1}),
a clean one-step reduction. The hope: show that for ANY split (not just balanced), the
resulting D is >= the balanced-split D (i.e., balanced is worst-case), then telescope
D >= D(T_{n-1}) >= ... >= D(T_1) = 1.

**Where it gets stuck:** The formula shows delta_D depends on O([0,q]) and O((p,L]),
which are global quantities. For the single top split, delta_D is constant (most
negative) on a plateau q in [2^{n-1}-delta, 2^{n-1}], so balanced is AS GOOD as any
split in that range — but proving this for ARBITRARY splits of ARBITRARY pieces
(not just the top) requires controlling the parity landscape after prior splits have
changed N(t). The parity coupling compounds: after the first split, N(t) is no longer
the clean tower step function, and O([0,q]) for the second split is harder to compute.

**Feasibility:** Medium for the top-split-only case (the plateau structure is clean);
hard for multi-split due to the compounding parity landscape. The `tail-count`
approach is best placed here because it already has the N(t) machinery.

### Route 3: Binary-tree / frontier (see section (c) below)

Has strong structural legs but the non-monotonicity of expansion (expanding the wrong
level INCREASES D) blocks a simple monotone induction. Most useful as a SCAFFOLD for
Route 1's frontier recursion.

### Route 4: Pairing / charging

D = (a1 - a2) + (a3 - a4) + ... + (trailing odd piece). The equality config has all pairs
cancel and trailing = 1 (the bottom piece). The tower-induction identity D = 1 + 2*(O_R' -
E_F) (rest-mass in odd slots vs fragment-mass in even slots) is a reformulation, not a
shortcut. A direct charging argument (pair each even-position fragment against an
odd-position rest piece of >= length) would need a matching/exchange argument. Hall's
theorem could certify the matching if the tower's dominance structure provides the
expansion property. This is the LEAST explored route; feasibility unclear without a
concrete matching construction.

---

## (c) Verdict on the binary-tree / frontier framing

**LEGS — strong structural scaffold, but not a standalone proof.**

**What works:**
- D_n = 2^{n+1} - 1 = number of nodes in a complete binary tree of depth n. Tower pieces
  2^k are the level sizes (level k has 2^k nodes). This is an exact match, not a metaphor.
- A balanced split 2^k -> 2^{k-1} + 2^{k-1} is exactly **expanding a level into its two
  child levels**. The equality config is a frontier (antichain of partial expansions).
- The frontier D values follow a **clean recursion**: min D among frontiers with topmost
  unexpanded level m is D(T_m) = 2^m - D(T_{m-1}), with base D(T_0) = D(T_1) = 1. This is
  the parity-flip recursion D -> 2^n - D specialized to the tower.
- After balanced top split, the config reduces to T_{n-1} (two extra copies pair up and
  cancel). This gives a clean inductive scaffold.
- All frontiers give D >= 1 (verified n = 3..6).

**What blocks a standalone proof:**
- **Non-monotonicity.** Expanding a level does NOT always decrease D. For n=4, expanding
  level 3 alone (split 8 -> 4+4) INCREASES D from 11 to 13. The benefit of a split
  depends on what OTHER splits have been made. So the tree structure does not give a
  monotone process; one cannot simply say "each expansion reduces D."
- **Unbalanced splits.** Xiang may split 2^k into p + q with p != q, which is NOT a tree
  expansion. The only way to split 2^k into two powers of 2 is the balanced split, so
  the tree framing covers only dyadic (balanced) configs. An exchange/convexity argument
  is needed to reduce unbalanced to balanced — and the data shows unbalanced single
  splits are AS GOOD (plateau) but not BETTER, while unbalanced multi-splits are STRICTLY
  WORSE for Xiang. This asymmetry (single = plateau, multi = strict) makes the reduction
  non-trivial.
- **Kraft/Huffman inequality.** I explored whether a Kraft-type inequality
  (sum 2^{-code_length} <= 1) could bound D. The tower pieces sum to D_n = 2^{n+1}-1, and
  a "prefix-free code" interpretation would need the alternating sum to relate to code
  lengths. I could not find a clean connection; the alternating sum D does not factor as
  a Kraft sum. This sub-idea does NOT have legs.

**Bottom line:** The binary-tree framing's main contribution is the **frontier recursion**
(D(T_m) = 2^m - D(T_{m-1}), min-over-frontiers = D(T_m)) and the **balanced-top-split
reduction** (D -> D(T_{n-1})). These are clean scaffolds for Route 1's induction. The
framing alone cannot close case (b) because of non-monotonicity and unbalanced splits,
but it provides the inductive backbone that Route 1 can build on.

---

## (d) New lemma worth proposing to the shared cache

### Lemma (balanced-top-split recursion)

**Statement.** Let T_n = (2^n, 2^{n-1}, ..., 2, 1) (tower units). The balanced split of
the top piece 2^n into 2^{n-1} + 2^{n-1} produces the multiset {2^{n-1}, 2^{n-1},
2^{n-1}, 2^{n-2}, ..., 2, 1}, whose alternating sum is D(T_{n-1}). Equivalently,
D -> 2^n - D(T_n) = D(T_{n-1}), via the full parity flip on [0, 2^n].

**Proof.** The balanced split (q = p = 2^{n-1}) flips the parity of N(t) on the entire
range [0, 2^n] (the +1 on [0, 2^{n-1}] covers intervals 0..n-1; the -1 on
(2^{n-1}, 2^n] covers interval n). After the flip, D_new = (total width where new N is
odd) = (2^n - D_old) on [0, 2^n] and 0 above (the new max piece is 2^{n-1} < 2^n).
Concretely: the three copies of 2^{n-1} sort as positions 1, 2, 3; positions 1-2 pair and
cancel (contribute 0), position 3 starts T_{n-1} at an odd index. So D_new = D(T_{n-1}).
The identity D(T_m) = 2^m - D(T_{m-1}) with D(T_0) = D(T_1) = 1 gives D(T_m) =
2^{m-1} - 2^{m-3} + ... (alternating). Verified for m = 1, ..., 6.

**Use.** This is the inductive scaffold for the lower bound case (b): after balanced top
split, the problem reduces from T_n to T_{n-1}. Currently embedded in `tower-induction`
as sub-case (b-i) (conditionally closed on IH); worth extracting as a standalone
certified lemma so the recursion D(T_m) = 2^m - D(T_{m-1}) is importable.

### Lemma (frontier minimum = D(T_m))

**Statement.** Among all balanced-split frontiers of T_n (configs obtained by expanding
a subset of levels {1, ..., n}, each expansion splitting 2^k -> 2^{k-1} + 2^{k-1}), the
minimum alternating sum among those with topmost unexpanded level m is D(T_m). In
particular, all frontiers satisfy D >= D(T_1) = 1.

**Proof sketch (verified n = 3..6, not yet rigorously proved).** The balanced-top-split
recursion shows that expanding the topmost level m reduces D from D(T_m) to D(T_{m-1}).
Expanding a non-topmost level can increase D (non-monotonicity), but the minimum over
all expansion patterns with a given topmost unexpanded level is achieved by expanding
all levels above m (cascading down), giving D(T_m). The tight frontier {2, ..., n} (all
levels expanded except 0 and 1) gives D = D(T_1) = 1.

**Status.** Verified computationally for n = 3..6. Needs rigorous proof of the
"expanding all above m is optimal" claim — this is the exchange/monotonicity step that
is currently missing.

---

## (e) Recommendation to the outliner

**Advance `tail-count`** (highest Elo 1540, has the N(t)/parity-integral machinery
best placed to execute Route 1's per-split delta_D formula and the variational argument).
Tell its builder: (1) formalize the piecewise-linearity of D in split positions and the
breakpoint-minimum argument; (2) use the delta_D = 2q - 2*O([0,q]) - 2*O((p,L]) formula to
show balanced-split is worst-case (plateau minimum) for the top; (3) close the gap between
breakpoint configs and frontiers (non-dyadic breakpoints lie on plateaus connecting to
dyadic ones).

**Open a NEW approach slug `frontier-recursion`** that builds on the binary-tree
recursion D(T_n) -> D(T_{n-1}) via balanced top split and the frontier minimum pattern
(min D = D(T_m) for topmost unexpanded level m). This approach would: prove the
balanced-top-split recursion and frontier-minimum lemma as standalone results, then
attempt to close case (b) by showing the variational minimum reduces to a frontier
(breakpoint => plateau => dyadic => frontier => D >= 1). This is genuinely different
from `tail-count` (which uses the integral/parity language) and from `tower-induction`
(which uses the sorted-list/self-similar IH) — it uses the binary-tree/frontier
structure and the parity-flip recursion as its engine, a framing no existing approach
has. The key risk: the non-dyadic breakpoint gap (step iv of Route 1).
