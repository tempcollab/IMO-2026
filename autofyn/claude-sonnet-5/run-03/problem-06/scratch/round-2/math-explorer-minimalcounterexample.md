## imo-2026-06

### Assigned lens
Scout whether the "minimal-counterexample / greedy-minimality-as-monovariant" idea sketched in
`covering-construction-induction.md` step 3(b) can be made into an actual argument (assume the
sequence is NOT eventually periodic, derive a contradiction from the greedy minimality rule
itself), as a genuinely different top-level mechanism from the shared No-Escape/CRT-covering wall
that `core-signature-pigeonhole`, `growth-bound-density`, and (in refuted form)
`monovariant-telescoping` all hit.

### What "No-Escape" precisely says (from `core-signature-pigeonhole.md`, the most rigorous file)
Fix $P=\{\text{primes}\le L_0\}$, $L_0=\mathrm{rad}(a_1)$ (a priori finite, from $a_1$ alone). After
signature stabilization ($N_1$, pigeonhole on $2^P$) and CRT, there's a sufficient target set $G$
with $a_{n+1}\le y_{n+1}:=\min\{x>a_n: x\bmod L_P\in G\}$ for $n\ge N_1$ (proved, no gap). The open
gap is: **no "escape"** ever occurs, i.e. no candidate $x$ with $a_n<x<y_{n+1}$ is validated only
because $\gcd(x,a_{i_0})>1$ is witnessed by a prime $q>L_0$ (a prime outside $P$) for some
$i_0\le n$, rather than by a prime of $P$. Given No-Escape, periodicity follows mechanically
(`lemmas/periodicity-given-no-escape.md`).

### Sharpest form of the minimal-counterexample argument I could build
Let $n_0\ge N_1$ be the **first** index where an escape occurs (assume one exists, for
contradiction). Structural facts that are actually available and *provable*, not conjectural:

1. **Fixed window.** By the unconditional gap bound (Lemma 2 in `core-signature-pigeonhole.md`,
   also `lemmas/gap-bound.md`), $x:=a_{n_0+1}\in(a_{n_0},a_{n_0}+L_0]$ — a window of length
   *exactly $L_0$, a global constant independent of $n_0$*. This holds for every step, escape or
   not; it is the strongest unconditional structural fact in the whole population and is
   under-exploited so far.
2. **At most one multiple of $q$ per window.** If the escape's witness prime $q>L_0$ divides $x$,
   then since $q>L_0=$ window length, $x$ is the *unique* multiple of $q$ in $(a_{n_0},a_{n_0}+L_0]$
   — escapes cannot be "redundant" within a single step; a given large prime pins down at most one
   candidate per window.
3. **Bound on $q$ in terms of the witness's age.** $q\mid(x-a_{i_0})$ and, telescoping the gap
   bound, $x-a_{i_0}=a_{n_0+1}-a_{i_0}\le(n_0+1-i_0)L_0$. So $q\le(n_0+1-i_0)L_0$: the escape
   prime is bounded **once you bound the "age" $n_0-i_0$ of the witnessing constraint**.
4. **The missing piece.** To turn this into a genuine contradiction from minimality of $n_0$ (the
   *first* escape), you would need: the witnessing index $i_0$ for the *first* escape must be
   *recent* (i.e. $n_0-i_0\le C$ for some constant $C$ depending only on $P,R$, not on $n_0$). I
   could **not establish this**, and have some numerical evidence it may be false as stated: see
   below. Without a recency bound, step 3 gives no finite bound on $q$, and the argument stalls
   exactly where the other three approaches stall — this IS effectively the same wall reached from
   a different angle, not a bypass of it. **I do not believe step 3(b) closes as a one-shot
   contradiction; it needs an extra ingredient (see "Concrete next steps" below), most likely a
   density/pigeonhole argument over *many* potential escapes rather than a single minimal one.**

### Cheap-kill / structural facts worth logging (new this round)
- The fixed-window fact (point 1 above) plus "≤1 multiple of $q$ per window" (point 2) is a clean,
  provable, and previously under-used structural constraint. It does not by itself close No-Escape,
  but any successful argument almost certainly routes through it (it is the only place the problem
  gives you a truly *bounded* quantity per step, independent of $n$).
- Computationally re-verified (stricter test than round 1's): across $a_1\in\{15,21,33,35,45,63,77,
  91,99,105,143,165,195,231,255,273,385,429,455,715,1001,1155,2145\}$, out to 400 terms each,
  **zero** escapes (in the strict Lemma-6 sense: a pair $(n{+}1,i_0)$ where $\gcd(a_{n+1},a_{i_0})$
  has *no* prime factor $\le L_0$). This both reproduces and broadens round 1's evidence.
- New distinguishing check this round: large primes $q>L_0$ **do** commonly appear as a factor of
  $\gcd(a_{n+1},a_i)$ (e.g. $a_1=15$: 550 such pairs in 300 terms, one example $\gcd(170,102)=34=
  2\cdot17$ with $17>15$) but **always alongside a small-prime witness too** (here $2\le L_0$) — so
  large primes recur constantly, just never as the *unique* witness. This sharpens (and confirms)
  the memory rule "frame the invariant around uniqueness of witness, not recurrence" — worth
  restating verbatim to the outliner since it is easy to conflate the two.
- Tested whether the "age" $n_0-i_0$ of a recurring $P$-signature $D^\*$ (i.e. gaps between
  consecutive indices sharing the same $D_n$) stays bounded as more terms are generated — this is
  exactly what would be needed to make step 4 above work. For $a_1=15,105,231$, out to 800 terms,
  the *maximum* observed recurrence gap for some signature classes was already 300–580, i.e. a
  sizeable fraction of the total run length, and did **not look like it was converging** to a fixed
  value as more terms were added (inconclusive — I could not push the naive $O(N^2)$-gcd simulator
  far enough in the time budget to confirm growth vs. a large-but-fixed bound; **the round-1 rule
  about needing a fast bitmask simulator for anything beyond quick sanity checks applies again
  here** — this measurement should be redone with a faster simulator before trusting it either
  way). **Conclusion: the "recency" ingredient needed to complete the minimal-counterexample
  argument is NOT obviously true and should not be assumed by a builder without first re-measuring
  with a faster simulator.**

### Candidate technique(s)
- Minimal-counterexample / extremal-principle-on-index framing, as instructed — but per above, it
  most likely needs to be a **density/pigeonhole argument over infinitely many potential escape
  events**, not a single first-escape contradiction. This is structurally close to a known IMO
  technique (see crux analog below): find an index class that recurs "densely enough" that a
  quantity is forced to repeat by pigeonhole, then use a divisibility-forces-vanishing step to
  upgrade "eventually/infinitely often" to "exactly, for all sufficiently large indices."
- The bounded-window fact (points 1–2 above) is a genuinely new lemma candidate,
  `windowed-witness-bound`, worth certifying on its own even though it doesn't close the gap yet:
  *for any $n$, any prime $q>L_0$ divides at most one integer in $(a_n,a_n+L_0]$.*

### Knowledge-base entries to use
- `knowledge_base.md` "Pigeonhole / extremal principle" (already used for signature stabilization;
  the same tool is the right one for a "densely recurring signature class" argument).
- "General Proof Methods" — induction's dual, "no minimal counterexample can exist" (§ near line
  185) — directly the technique family being probed here; worth re-reading before the outliner
  commits, since a naive single-minimal-counterexample framing risks being non-constructive in a
  way that doesn't actually use enough structure (as found above).
- CRT / modular reduction entries (already in use via `core-signature-pigeonhole`) remain relevant
  as the vehicle for the "density" version of the argument.

### Analogous past problems (cruxes)
- **`aimo-0680`** (IMO Shortlist 2015 N4/A-adjacent, "prove $f(n)-n$ is periodic given (i) $d\mid
  f^d(m)-m$ for all $d$, and (ii) cofinite image"): **the single best structural analog found.**
  Its proof shape is exactly the "genuinely different mechanism" the run needs: (1) partition the
  domain into finitely many classes ("rows" = orbits under $f$, here would be $P$-signature
  classes), (2) assume for contradiction some classes are NOT yet forced into arithmetic-progression
  behavior, (3) show the "leftover" classes must be asymptotically dense (via a counting argument
  against the classes already known periodic — using $\mathrm{lcm}$ of known periods, exactly the
  kind of $L_P$/CRT bookkeeping we already have), (4) pick the densest leftover class, get a
  difference quotient $\beta_d=(f^d(a_x)-a_x)/d$ that is a positive integer bounded independent of
  $d$ (forced by (i) + the density bound), pigeonhole to a fixed value on an infinite index set, and
  (5) the killer step: for two indices $y>j$ in that infinite set, both $f^y(a_x)-f^j(a_x)$ and
  $(y-j)T_x$ are divisible by $y-j$; their difference is bounded in absolute value but $y-j$ can be
  taken arbitrarily large, forcing the difference to be exactly $0$ — turning "true for infinitely
  many $d$" into "true for ALL $d$" for FREE. **This "bounded difference, divisible by an
  unboundedly large quantity ⟹ must vanish" trick is the single most transplantable idea I found
  this round** — it is exactly the kind of move that could upgrade our "$a_{n+1}\le y_{n+1}$ +
  escapes rare/bounded on some infinite subsequence" into "$a_{n+1}=y_{n+1}$ for ALL large $n$"
  *without* ever fully ruling out individual escapes, IF an analogous integer-divisibility identity
  can be manufactured for our recursion (our problem currently lacks a free identity like
  $d\mid f^d(m)-m$; deriving one — e.g. from the eventual periodicity of the $r_n=a_n\bmod L_P$ map
  once restricted to a single recurring residue class — is the concrete creative step needed to
  transplant this). **This is a genuinely different top-level mechanism from CRT-covering/No-Escape
  and should be given to the outliner as a real 4th/5th approach candidate**, not a variant of the
  existing three.
- `aimo-0611` (IMO SL 2014 N4, Zsigmondy-flavored: a term outgrowing the product of all earlier
  terms forces a brand-new prime factor) is the *opposite* phenomenon (forces large primes to
  appear) rather than what we need (large primes never uniquely necessary) — flagged as **not**
  directly transplantable, but useful negative context: it confirms new large primes appearing is
  expected/unavoidable (consistent with $Q$ being infinite, already known), so any approach must
  distinguish "large prime appears" from "large prime is load-bearing," matching the run's existing
  rule.
- `aimo-0077` (Germany TST 2010, extremal-principle: assume non-termination forces a state cycle,
  take the minimal-index object acted on within the cycle) — a genuine minimal-counterexample-on-a-
  cycle pattern, but it's a discrete combinatorics/card-flipping game, structurally too different
  (finite state space with no analog of our unbounded integer growth) to transplant directly; listed
  for completeness but judged a weaker analog than `aimo-0680`.

### Prior progress
No approach in the population has closed No-Escape; `core-signature-pigeonhole` remains the
furthest reduction (see `results/imo-2026-06/current.md`). This round's exploration did **not**
close it either — it sharpens the gap (fixed-window + single-multiple-per-window facts) and
supplies one concrete new top-level mechanism candidate (the aimo-0680-style density/vanishing
argument) but the "recency bound" needed for a literal one-shot minimal-counterexample contradiction
is unproven and may be false as stated (see numerical caveat above).

### Dead ends (do not retry)
- A **literal single-first-escape contradiction** (assume $n_0$ minimal, derive contradiction
  directly from step 3–4 above without further ingredients) does not obviously close: the bound on
  $q$ in point 3 needs a recency bound on $i_0$ that isn't established and whose truth is uncertain
  from the (inconclusive, needs faster simulator) numeric check. Don't hand a builder "assume the
  first escape and get an immediate contradiction" as if it's a known-clear path — flag it as
  needing the extra density ingredient from the start.
- Re-confirms: `monovariant-telescoping`'s $|Q|<\infty$ target (already ruled out by the reviewer)
  and any framing that tries to bound "primes recurring at all" rather than "primes as unique
  witnesses" — my new data (large primes recurring constantly but never uniquely) reinforces this
  is a dead framing, not just previously refuted by simulation coincidence.

### Small-case / intuition notes (all labeled conjecture except where marked proved)
- **Proved** (Lemma 2, reused here): $a_{n+1}-a_n\le L_0=\mathrm{rad}(a_1)$ for all $n$ — a fixed,
  n-independent window.
- **Proved** (immediate corollary, new this round): any prime $q>L_0$ divides at most one integer
  in any single window $(a_n,a_n+L_0]$.
- **Conjecture** (strong evidence, 23 values of $a_1$ up to 400 terms, zero counterexamples): no
  escape (unique large-prime witness) ever occurs — i.e. No-Escape is true.
- **Conjecture, weaker evidence, possibly false**: that the "age" of the witnessing index for a
  hypothetical escape can be bounded independent of $n$ — the recurrence-gap data (up to ~580 out of
  800 terms, not obviously converging) suggests this may NOT be true in general, which is exactly
  why a single minimal-counterexample knockout looks fragile and a density/infinite-subsequence
  argument (aimo-0680-style) looks like the more promising **genuinely new mechanism** to hand the
  outliner.

### Concrete next steps for the outliner
1. Register a new approach (distinct slug, e.g. `dense-signature-vanishing`) built around the
   aimo-0680 mechanism: partition indices by (eventually-stabilized) $P$-signature $D_n\in R$; for
   each $D\in R$ that recurs infinitely often, try to derive an integer-valued, boundedly-bounded
   difference quotient analogous to $\beta_d$ (the natural candidate: for $i<j$ with $D_i=D_j=D$,
   is $(a_j-a_i)$ forced into finitely many residues mod something, giving a pigeonholed constant
   gap on an infinite subsequence of that class?) and then apply the "unbounded divisor, bounded
   difference ⟹ vanishes" trick to upgrade to an exact statement for all large $n$ in that class.
   This is a real 4th mechanism, not a rephrasing of CRT-covering/No-Escape.
2. Certify the `windowed-witness-bound` lemma (fixed window + ≤1 multiple of any $q>L_0$ per
   window) as a standalone reusable fact regardless of which approach proceeds — it's cheap, fully
   proved, and likely load-bearing for whichever mechanism ultimately closes the gap.
3. Before any builder relies on a "recency of witness index" claim, re-run the signature-recurrence-
   gap measurement with a fast bitmask simulator (per the existing memory rule) out to several
   thousand terms to determine whether those gaps are bounded or genuinely growing — this directly
   determines whether the literal step-3(b) single-counterexample knockout is salvageable at all, or
   whether only the density/subsequence version (step 1 above) can work.
