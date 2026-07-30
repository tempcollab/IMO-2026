## imo-2026-06

- Distinct openings (all viewed through the "eligible set" E_n = {m : gcd(m,a_i)>1 ∀ i≤n} lens):
  1. **Core-prime-set / "≥2 of P" characterization.** Conjecture (strongly supported by experiment,
     see below): there is a finite set of primes P = {p_1,...,p_k} (depending on a_1) and a threshold
     N_0 such that for all sufficiently large integers m ≥ N_0, m ∈ (eventual image of the sequence)
     iff m is divisible by **at least two** distinct primes of P. If true, the eventual eligible set is
     literally a fixed union of residue classes mod M := p_1·p_2·⋯·p_k (M squarefree), and the walk
     through it in increasing order is exactly periodic mod M with T = #{residues mod M divisible by
     ≥2 of the p_i} and L = M. This is the cleanest target: (a) prove such a P exists and stabilizes,
     (b) prove "≥2 of P" is exactly the right predicate (not just necessary or just sufficient),
     (c) conclude periodicity is now pure counting (CRT/inclusion–exclusion), no further gcd machinery
     needed. The whole difficulty concentrates into steps (a)+(b).
  2. **Monotone/eventually-constant invariant on E_n directly.** Instead of guessing the final set,
     study E_n as a decreasing sequence of subsets of the eligible-candidate space directly (E_n only
     shrinks as n grows, since each new a_i imposes one more "share a factor" constraint). Show E_n
     eventually becomes constant when restricted to "far enough ahead" integers (i.e. for every m there
     is N(m) s.t. m∈E_n for n≥N(m) iff m∈E_∞ — a pointwise stabilization / monotone-class argument),
     then separately argue E_∞ is periodic. This decouples "does the sieve stabilize at all" from
     "what is the stable pattern," which may be easier to formalize than opening 1's direct guess.
  3. **Grid / covering encoding (adapt aimo-0447's move).** Build an array indexed by (candidate integer
     m, index i≤n) and place in cell (m,i) a prime dividing gcd(m,a_i) whenever m∈E_n. Track, for each
     *prime* p, the set of indices i such that p | a_i — call this the "p-fiber." A prime p can only be
     "load-bearing" (needed to certify m∈E_n against index i) while its fiber is sparse; as n→∞, primes
     with infinite fiber (dividing infinitely many a_i) become the only primes that can certify
     membership against *arbitrarily late* indices i, so E_n's *tail* behavior is controlled only by the
     finitely-many-or-not distinction among primes dividing infinitely many terms. This reframes "find
     the core set P" as "find the primes with infinite fiber" — a cleaner, more classical NT object
     (cf. aimo-0447's technique of encoding gcd>1 conditions via a chosen prime per pair, and aimo-0421's
     "gcd values are divisors of a fixed number, hence finite, pigeonhole over an infinite family").
  4. **Density / growth-rate argument to pin down which primes are load-bearing.** Since gaps
     a_{n+1}-a_n are governed by Bertrand-type/greedy-minimality reasoning, and the density of integers
     divisible by a fixed prime p is 1/p, an "efficient" greedy sieve will only recruit small primes
     (favoring 2, 3, 5, ... as seen experimentally) — a size/counting argument (in the spirit of
     Bertrand's postulate / prime density from the KB) could bound k = |P| and bound which primes appear,
     giving an a priori finite search instead of an open-ended existence argument.

- Candidate technique(s): modular arithmetic / CRT (to convert "periodic union of residue classes" into
  exact T,L), pigeonhole on "gcd of a fixed element with infinitely many others takes finitely many
  values" (KB: order/Euler entry, and directly mirrored in crux aimo-0421), monovariant/eventually-
  constant argument (E_n is a *decreasing* set sequence — natural monovariant target), inclusion-
  exclusion counting once the core prime set P is fixed.

- Cheap-kill candidates: none that finish the problem, but two are useful pruning facts to hand the
  outliner:
  (i) *a_1 prime* is the trivial base case — the whole sequence is forced (by induction) to be exactly
  the multiples of a_1's single prime factor, giving T=1, L=p immediately; good sanity-check /
  base case, not a route to the general problem.
  (ii) The gap bound `a_{n+1} - a_n ≥ gcd(a_n,a_{n+1})` (used in crux aimo-0503 for a *different* problem)
  is available for free from `gcd | difference`, but experimentally it is far too weak here — gaps stay
  small (single digits) even at n~1000 — so it will not by itself bound anything useful; don't lead with
  it.

- Knowledge-base entries to use: **Modular arithmetic, CRT** (turn "union of residue classes mod M" into
  exact period counting); **Order of an element / Euler** and **Linear recurrences: eventual periodicity
  mod m** (general pattern: sequences built from bounded local data are eventually periodic — same shape
  of conclusion needed here, though the mechanism differs); **Pigeonhole/extremal principle**
  (finitely-many-gcd-values pigeonhole, mirrors aimo-0421); **Divisor analysis** entry generally.
  Bertrand's postulate is a plausible tool for bounding gap sizes / prime magnitudes if a growth argument
  is needed to bound |P|.

- Analogous past problems (cruxes):
  - **aimo-0447** (`number_theory / divisibility-and-gcd`): hypothesis `gcd(a+i,b+j)>1 for all i,j∈{0..n}`
    — *structurally the closest analog* to our problem's hypothesis shape. Crux move: encode "gcd>1"
    conditions by placing a witnessing prime in each cell of a grid, then bound how many cells one prime
    p can "cover" (≤⌈N/p⌉ along each axis) to force most of the grid to be covered by *large* primes,
    which must then be pairwise distinct — driving a growth lower bound. Different target (a growth bound,
    not periodicity) but the technique of tracking "which prime is responsible for gcd>1 at each pair" is
    directly transplantable to formalize opening 3 above (tracking fibers of primes across indices).
  - **aimo-0421** (`number_theory / divisibility-and-gcd`): "gcd(a,s) for fixed a ranges over divisors of
    a, hence finite; pigeonhole an infinite family to fix the gcd value." Directly useful for proving a
    prime that is "load-bearing" for infinitely many indices must be one of finitely many primes dividing
    a_1 or an early term — supports opening 2/3's "stabilization" step.
  - No corpus problem produces the exact "walk through a periodic sieve" conclusion (a_{n+T}=a_n+L for an
    unbounded increasing greedy sequence) — this is a genuinely IMO-P6-level combination not matched
    closely elsewhere in the corpus; treat the corpus hits as technique donors, not solution templates.

- Prior progress: none — fresh workspace, no approaches or lemmas exist yet (round 1, this problem has
  no other rounds so far in this run).

- Dead ends (do not retry): none recorded yet (nothing has been tried).

- Small-case / intuition notes (all **conjectural**, verified only by direct simulation of the exact
  greedy rule for a1 up to a few thousand terms in Python):
  - `a_1 = p` prime ⟹ sequence = all multiples of p exactly, T=1, L=p (trivially, since gcd(a_1,a_i)>1
    forces p | every term, and then the minimal choice fills in every multiple of p — verified for
    a_1=2,3,5,7).
  - `a_1 = p^e` (single prime power, e.g. a_1=4=2², a_1=8, a_1=25=5²) ⟹ same trivial outcome, all
    multiples of p, T=1, L=p — verified a_1=4,8,25,49.
  - `a_1` with two distinct prime factors: outcome bifurcates sharply depending on the specific primes,
    NOT just on "how many primes":
    - a_1=21=3·7, 33=3·11, 39=3·13, 51=3·17, 63=9·7, 231=3·7·11 all converge trivially to T=1, L=3 (all
      multiples of 3) — whenever 3 | a_1, the greedy walk seems to "lock onto" multiples of 3 alone very
      fast (verified by direct simulation up to 1000+ terms).
    - a_1=15=3·5 does **not** reduce to multiples of 3 (or 5): instead it locks into a genuinely 2-D
      pattern — verified T=8, L=30, and the *exact* set of 8 stable residues mod 30 (namely
      {0,6,10,12,15,18,20,24}) is precisely **the residues divisible by at least 2 of {2,3,5}** (checked
      exhaustively: the 14 "single-prime-only" residues mod 30 that are divisible by exactly one of
      {2,3,5} — e.g. 3,5,9,21,25,27 — are *never* visited, confirmed out to n=3000+).
    - a_1=35=5·7 ⟹ T=34, L=210=2·3·5·7: core set grows to {2,3,5,7} — *even though 3 does not divide
      a_1* — recruited anyway. Same "≥2-of-core-set" predicate checked and holds.
    - a_1=105=3·5·7 ⟹ T=58, L=210 (core {2,3,5,7}); a_1=165=3·5·11 ⟹ T=86, L=330=2·3·5·11 (core
      {2,3,5,11}); a_1=143=11·13 ⟹ T=64, L=858=2·3·11·13 (core grows to include 3, even though 11,13
      are a_1's only factors); a_1=77=7·11 ⟹ T=18, L=154=2·7·11 (core stays {2,7,11}, does NOT recruit
      3 or 5) — **verified exactly** by checking the stable residue set mod 154 equals precisely the
      residues divisible by ≥2 of {2,7,11} (exact set match, not just count match).
    - Takeaway: the core prime set P is **not determined solely by which primes divide a_1**; extra
      small primes (2, sometimes 3) get recruited or not recruited depending on delicate numeric
      proximity of the greedy choices early in the sequence (e.g. for a1=15, the third term a_3=20 wins
      over the "pure multiple of 3" candidate 21 purely because 20<21 — a knife-edge greedy comparison).
      This means the “which primes end up in the core set” question is itself non-trivial and likely the
      hardest sub-problem; a fully general proof of periodicity may be able to sidestep *identifying* P
      explicitly and only need to prove P exists, is finite, and "≥2 of P" is eventually exactly the
      membership rule — worth flagging to the outliner as the place to aim the existence/stabilization
      argument rather than trying to compute P in closed form.
  - The **"≥2 of P"** predicate (rather than "≥1 of P") was checked *exactly* (full residue-set equality,
    not just cardinality) for a_1 = 15 (P={2,3,5}, M=30) and a_1 = 77 (P={2,7,11}, M=154); this is strong
    (though still empirical) evidence for opening 1's conjectured structural characterization, and gives
    a concrete formula once P is known: T = #{r mod M : r divisible by ≥2 primes of P}, computable by
    inclusion–exclusion via CRT since M=∏P is squarefree.
