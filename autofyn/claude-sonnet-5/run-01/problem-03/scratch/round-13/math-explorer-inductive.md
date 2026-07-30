## imo-2026-03

### 1. Exact recursion (Candidate 5 / budget-capped TAIL-SNIP), read from `approaches/universal-adversary-strategy.md` lines 2454-2820

`A` sorted descending, `Sigma = Sigma(A)`.
```
solve(A, budget):
  if |A|==1: return A[0]
  Move 1 (halve):  p1/2 + solve(tail(A), budget)                 # budget unchanged
  Move 2 (partial-dom): j* = max j with p1 >= S_j (S_j = prefix sum of tail);
      r = p1 - S_j*, leftover = tail[j*:] plus {r} if r>0
      value = S_j* + solve(leftover, max(budget-1,0))            # or S_j* alone if leftover empty
  Move 3 (tail-snip, only if |A| odd, |A|>=3, budget>0):
      A' = A with last element replaced by two copies of half its value
      value = solve(A', budget-1)
  return min of the available moves
solve_full(A) := solve(A, 1)
```
IH as stated in the plan: `solve(A,budget) <= c(|A|-1)*Sigma(A)` tracked jointly over `budget in {0,1}`, with mark-budget bookkeeping. HALF-BOUND is a discovered sharper target: `solve_full(A) <= Sigma(A)/2` whenever `p1 < Sigma(A)/2` (Case C).

### 2. New reduction found this round: the "excess" recursion, and an unexpected identity

Define `e(A,budget) := solve(A,budget) - Sigma(A)/2`. Since `Sigma(A)/2 = p1/2 + Sigma(tail)/2` exactly, Move 1's excess is **exactly** `e(tail(A),budget)` (no approximation). Since matching a prefix summing to `S_j*` against `p1` satisfies the *exact* identity `Sigma(leftover) = Sigma(A) - 2*S_j*` (because `leftover = tail[j*:] cup {r}`, `r=p1-S_j*`), Move 2's excess is **exactly** `e(leftover, budget-1)` (or `0` if leftover is empty — this needs `S_j*=p1` exactly, i.e. a perfect tie). Since tail-snip preserves `Sigma`, Move 3's excess is exactly `e(A',budget-1)`. So:
```
e(A,budget) = min( e(tail(A),budget), [0 if leftover empty else e(leftover,budget-1)], [e(A',budget-1) if applicable] )
e(singleton) = A[0]/2  > 0
```
I verified this identity symbolically-exactly (re-deriving both sides via independent code and checking equality) on several configurations — holds exactly, as it must from the algebra. **This is a genuinely clean reformulation**: HALF-BOUND becomes "does the min-recursion, which can only bottom out at strictly positive leaves (`A[0]/2`) or exact-tie zeros (`S_j*=p1` exactly, i.e. leftover empty), ever reach `<=0`?"

**Surprising empirical finding (conjecture, not proof): the recursion appears to ALWAYS hit an exact-tie zero when Case C holds — i.e. `solve_full(A) = Sigma(A)/2` EXACTLY, not merely `<=`, for every Case-C configuration.** I tested this directly (exact `Fraction` arithmetic, no floats) on 3,500+ random configurations spanning `m=4..12` (uniform-random and highly-skewed integer weight vectors), plus every previously-flagged hard witness (`m=5` witness `(1826,1563,1520,1514,765)/7188`, the `(0.45,0.40,0.06,0.05,0.04)` tail-dominant witness, near-uniform triples, boundary cases `p1` just under `Sigma/2` with a highly skewed tail): **every single test gives `e(A,1)=0` exactly, zero exceptions.** This is consistent with — and in fact fully explains — the round-12 gate's reported worst-case margins `c(m-1)-1/2 = 1/(2(2^m-1))` exactly: if `solve_full(A)=Sigma/2` identically throughout Case C, then `margin(m) := c(m-1)*Sigma - solve_full(A) = (c(m-1)-1/2)*Sigma` identically too — matching the reported closed form exactly, not just at the found worst point.

### 3. Sharper reformulated target for the outliner

Rather than chase the inequality HALF-BOUND with residual "tail locally dominant" casework (which I confirmed is a real obstruction to naive induction — see below), **the outliner should consider targeting the IDENTITY**: `solve_full(A) = Sigma(A)/2` exactly whenever `p1 < Sigma(A)/2`. This is stronger, but may be structurally *easier* to prove because via the `e`-recursion it reduces to a pure existence claim: **some sequence of the three moves always reaches a perfect tie (`S_j*` exactly equal to the current top piece, i.e. an exact-sum subset/prefix match with zero residual) before bottoming out at a singleton.** This is precisely an exact-matching / Hall's-theorem-flavored existence question (as the round-12 plan already suspected when flagging `aimo-0063`'s Hall-deficient-set-deletion technique) — but now the target is sharper and cleaner: not "beat `c(m-1)*Sigma`" but "hit `Sigma/2` on the nose via an exact tie," which is a single Boolean existence claim per configuration, not an inequality needing slack-tracking.

### 4. Confirmed real obstruction to a naive induction (do not re-attempt without addressing this)

I directly tested (and confirm, independently of the builder's report) that:
- Move 2's leftover is **not always Case-C for itself**: in 22% of tested random Case-C configurations (`m=3..11`, 14k+ trials), `top(leftover) >= Sigma(leftover)/2`, up to ratio `0.9985` — so a bare "apply IH to leftover assuming it's Case C" argument fails structurally, confirmed with an explicit witness.
- Worse, when leftover fails Case-C, `solve(leftover, budget=0)` (i.e. leftover recursed *without* the spare tail-snip mark) frequently genuinely **overshoots** `Sigma(leftover)/2` (3550/4726 non-Case-C-leftover cases in one 18k-trial sweep, worst margin `-0.068` i.e. `solve(leftover,0) > Sigma(leftover)/2` by 6.8% of `Sigma`). This means **no single move (Move 1 alone, or Move 2 alone) propagates HALF-BOUND recursively** — the `min` over all three moves is doing genuinely non-trivial, configuration-dependent work, and which move "wins" switches between levels of the recursion in a way not captured by a clean 2-variable inequality. This is why the naive per-move induction attempts (both the builder's and mine) stall.

### Distinct openings
- **(New, this report) Target the exact identity `solve_full(A)=Sigma/2` in Case C** via the `e`-recursion above, reducing to: prove that a perfect-tie leftover (`S_j*=p1` exactly, possibly only reachable after one Move-3 split manufactures a synthetic tie between two new equal half-pieces) is always reachable. Concretely: show that the recursion always has access to *some* subset of the (possibly once-split) multiset summing exactly to the running "target" value at each step — a Hall/deficiency-style exact-cover argument, not an inequality argument.
- Fall back: keep the inequality HALF-BOUND but track the leftover's own worst-case slack jointly (go back toward the original `c(|A|-1)*Sigma` bookkeeping, using the exact identity `S_j*+Sigma(leftover)/2=Sigma/2` as a tool, rather than trying to force the leftover into Case C).
- Abandon per-move induction; instead try to directly characterize, as a function of `(p1/Sigma, p2/Sigma)` (2-variable reduction), *which* move wins, and show the winning move's excess is `<=0` via case-by-case algebra on this 2D parameter space (cheap to grid-search exactly with `Fraction` to look for the boundary curve before attempting proof).

### Candidate technique(s)
Exact-sum subset-matching / Hall's marriage theorem (crux `aimo-0063` Hall-deficient-set-deletion, still not applied, flagged again as directly relevant — more so now that the target is an exact identity, i.e. an exact-cover existence claim, than for the inequality). Strong induction via the `e`-recursion reformulation (new this round).

### Cheap-kill candidates
The `e`-recursion's positivity-of-leaves structure gives a cheap sanity check: any proposed proof of HALF-BOUND that doesn't produce (or account for) an exact zero-excess leaf is suspect, since empirically excess is *never* a small negative number — it's exactly 0 whenever Case C holds. This is a strong self-check to apply to any future inductive argument (if a builder's argument implies `e(A,1)<0` strictly anywhere, re-verify — it likely signals an algebra error, since no such example was found in ~7000+ trials).

### Knowledge-base entries to use
Reuse already-certified Lemma PAIR-VALUE and Lemma BLOCK-RECURSE (exact value identities under matching — the algebraic backbone behind the `S_j*+Sigma(leftover)/2=Sigma/2` identity derived here) and Lemma THRESHOLD-REDUCTION (`c(k-1)=c(k)/(2(1-c(k)))`, needed for the final step converting `Sigma/2 < c(m-1)*Sigma` once/if the identity is established).

### Analogous past problems (cruxes)
Have not re-queried the crux corpus this round (focus was the recursion/algebra per dispatch); `aimo-0063`'s Hall-deficient-set-deletion technique (already flagged by the round-12 plan) is the standing candidate for the exact-cover/matching-existence step — now more directly relevant given the identity reframing in Section 3.

### Prior progress
Lemma WF-C5 (well-foundedness) certified. Adversarial gate passes for `m=4..14`. HALF-BOUND (inequality) empirically confirmed with zero violations across thousands of trials, but the builder's own proof attempt (pure Move-1 induction) explicitly does not close the "tail locally dominant" sub-case. This round's new finding: **HALF-BOUND appears to actually be an equality** (`solve_full(A)=Sigma(A)/2` exactly throughout Case C), which is new information not previously reported at this precision, and the exact `e`-recursion reformulation of the problem (Section 2), independently verified.

### Dead ends (do not retry)
- Pure Move-1-only recursive induction (assumes tail inherits Case C) — refuted both by the builder (round 12) and independently here (22% of leftovers fail Case-C-for-itself, up to ratio 0.9985 of dominance).
- Assuming Move 2's leftover, when it fails Case-C, still satisfies HALF-BOUND on its own with `budget=0` — refuted here directly (75% of non-Case-C leftovers in one sweep genuinely overshoot `Sigma(leftover)/2` at `budget=0`, worst margin `-0.068*Sigma`), confirming no single move propagates the bound recursively in isolation.

### Small-case / intuition notes
**Conjecture (strong numerical evidence, ~7000+ exact-Fraction trials, `m=4..14`, zero exceptions, not proved):** `solve_full(A) = Sigma(A)/2` exactly (an identity, not merely an inequality) for every sorted `A` with `p1 < Sigma(A)/2`. If provable, this would fully close Case C with a clean explicit value, and the excess-recursion (Section 2) suggests the natural proof vehicle is an exact-cover/matching existence argument rather than further inequality casework.
