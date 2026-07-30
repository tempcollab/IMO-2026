## imo-2026-06

- Distinct openings (finite-state / structural lens):
  1. **"Core prime set + signature-family" reduction.** Track, at step n, the set
     `S_n` of primes p such that infinitely-relevant hitting occurs through p (see caveat below —
     NOT simply "all primes dividing some a_i", see Dead ends / cheap-kill). If some finite S
     eventually has the property that *every* a_i (i ≥ N0) is divisible by at least one prime of
     S, then define, for i ≥ N0, the "S-signature" D(a_i) = {p ∈ S : p | a_i} (a nonempty subset
     of S). The family R_n = {D(a_i) : N0 ≤ i ≤ n} of *distinct* signatures seen so far is a
     monotone non-decreasing chain of subsets of the finite poset P(S)\{∅} (only 2^|S|-1
     elements), so by pure pigeonhole R_n must stabilize at some finite n = N1 to a fixed family
     R. This "R stabilizes" step is cheap and rigorous *given* S is known to work (see gap below).
  2. **Reduction to a periodic residue-selection process.** Once R has stabilized (step 1), for
     n ≥ N1 the admissibility condition "gcd(x,a_i)>1 for all i ≤ n" is implied (sufficient
     direction, easy) by "D(x) ∩ S hits every member of R". Whether D(x)∩S hits every member of R
     depends only on x mod L, L = lcm(S), via CRT — giving a FIXED nonempty "good residue set"
     G ⊆ Z/LZ. If in addition one can show this sufficient condition is also *necessary* for the
     actual minimal greedy choice (the real crux, see gap below), the tail of the sequence for
     n ≥ N1 is exactly "smallest x > a_n with x mod L ∈ G", a manifestly periodic process:
     T := |G| (number of good residues per period) and a_{n+T} = a_n + L for all n ≥ N1. This
     packages the whole theorem into two finite-state pigeonhole facts once S is granted.
  3. **State-graph / bijection framing (analogous to a reversible-walk argument).** Model the
     process as a walk on the finite state space of (current residue class mod L, which "good"
     residue in the cycle we are at) — a walk on a finite directed graph with out-degree 1 per
     node (deterministic next-good-residue map). Any infinite walk on a finite state graph with
     out-degree 1 per node must enter a cycle (pigeonhole on ≤ L states); combined with the
     already-periodic domain structure (Z/LZ), the cycle length equals T and shift equals L. This
     is really the same argument as opening 2, phrased as a "functional graph must cycle" fact —
     useful if the outliner wants a clean pigeonhole citation instead of direct verification.

- Candidate technique(s): pigeonhole on a monotone chain of subsets of a finite poset (forcing
  eventual stabilization of the "signature family"); CRT to reduce prime-signature membership to a
  residue condition mod a fixed L; "functional graph on finite state space must cycle" pigeonhole.

- Cheap-kill candidates: none that fully resolve the problem, but one important structural
  pruning: **the naive claim "the full set of primes ever dividing some a_i is eventually finite"
  is FALSE** (verified numerically below) — so any approach (including sibling explorers') that
  tries to prove finiteness of the *literal* set of primes used will hit a wall; the correct
  target is a smaller, load-bearing "core" set S (only the primes that matter for hitting future
  constraints), not the full prime support. This is a genuine gap-narrowing finding, not just a
  dead end to avoid — it redirects the finite-state argument.

- Knowledge-base entries to use: `knowledge_base.md` "Pigeonhole / extremal principle" entries
  (lines ~108, ~188) for the chain-stabilization / functional-graph-must-cycle steps; the
  "periodicity of a^n mod m / eventual periodicity of products of a sequence mod m" entry
  (lines ~65-80) is the closest existing KB pattern for "eventually periodic mod m" claims and is
  a good template for the CRT residue-reduction step (opening 2).

- Analogous past problems (cruxes):
  - `aimo-0514` (Planar National Park walk) — crux: encode state as "turn" so the one-step
    process is a *bijection* on a finite state set, forcing the whole (bi-infinite) orbit to be
    purely periodic, not just eventually periodic, via pigeonhole on finite states. Analogous in
    spirit to opening 3 (functional graph on finite states must cycle), though our process is not
    literally reversible so we only get *eventual* periodicity, matching the theorem's shape more
    loosely — good template for phrasing the pigeonhole cleanly.
  - `aimo-0982` (2^n-th digit rational⇒rational) — crux: reduce "eventually periodic" to tracking
    an *index* (here 2^n mod d) through CRT-splitting a modulus into 2-power and odd parts. Same
    high-level shape as opening 2's CRT step (residue of a_n mod L determines future signature),
    though the number-theoretic content differs.
  - `aimo-0077` (2009 cards flipping game) — crux: finite state space (≤2^2008 configs) forces a
    non-terminating process into a cycle, then minimality-in-the-cycle gives a contradiction.
    Useful as a second template for "finite state ⇒ must cycle," but the contradiction-via-
    minimality flavor doesn't map directly onto our problem (we WANT periodicity, not a
    contradiction from it).
  None of these is a tight structural match to the actual hard content (see gap below); they
  confirm the general pigeonhole-for-eventual-periodicity technique is standard but the
  problem-specific difficulty (identifying the correct finite "core" S, and proving no
  "large-prime coincidence" can undercut the greedy choice) is not present in any corpus entry
  found.

- Prior progress: none (first exploration of this problem; `results/imo-2026-06/` is empty
  scaffold only, confirmed by reading `current.md`).

- Dead ends (do not retry): "the full set of primes that ever appear in the sequence's
  factorizations is eventually finite" — checked numerically for a_1=35 up to n=3000: 281 distinct
  new primes appear (up to 1847), roughly one new prime every ~10 terms with no sign of stopping.
  So the literal prime-support of the sequence is very likely NOT eventually bounded, and any
  finite-state argument built on that literal claim is a dead end.

- Small-case / intuition notes (all labeled conjecture / numerical evidence only, using a fast
  bitmask-based greedy simulator, `math.gcd`/`sympy.primefactors`, verified against brute force on
  small n):
  - a_1 prime (2,3,5,7,...): trivial, T=1, L=a_1 (every subsequent term is just a_1 + a_1*k,
    since a_1 alone divides all future terms and remains the unique constraint) — sanity check
    only, not the interesting case.
  - a_1 = 6, 10, 12, 30 (already multiple small primes, e.g. 2·3, 2·5): degenerates immediately to
    an arithmetic progression with common difference = smallest prime factor already present
    (e.g. diff 2), because 2 alone already satisfies gcd>1 with everything — T=1 essentially.
  - a_1 = 15 (=3·5): genuinely non-trivial — diffs cycle with period **T=8**, sum of one period
    **L=30** = lcm(2,3,5): pattern of diffs [3,2,4,6,6,4,2,3] repeating. Verified this exact
    periodicity (a_{n+8}=a_n+30) holds for ALL n up to 3000 computed terms (strong numerical
    evidence, not proof) — **even though** the raw prime-support of the sequence keeps growing
    (288 distinct primes appear over those 3000 terms). This is the key structural finding: only
    2,3,5 ever matter for admissibility because **every single term over 2000+ computed terms is
    divisible by at least one of {2,3,5}** (checked directly: zero exceptions) — the extra large
    "one-off" primes appearing in factorizations (e.g. a term = 2·3·5·19···) are bystanders that
    never affect which future x's are admissible, since 2,3,5 alone already make every term hit
    every other term.
  - a_1 = 45 gives the identical period/shift (T=8, L=30) as a_1=15, consistent with both landing
    in the same "core = {2,3,5}" regime.
  - a_1 = 35 (=5·7): conjectured core is {2,3,5,7} (numerically, ever term of 2000+ computed terms
    is divisible by at least one of 2,3,5,7, with zero exceptions) — but I could not confirm exact
    long-run periodicity with high confidence in the time available (an earlier naive tail-match
    test spuriously reported T=34, L=210, but this used too short a window and is NOT trustworthy;
    do not cite the earlier T=34/L=210 for a_1=35 without re-verifying over a much longer range —
    only the a_1=15/45 case (T=8, L=30) was independently re-verified over 3000 terms and is
    solid numerical evidence).
  - a_1 = 105 (=3·5·7) also showed core primes reaching {2,3,5,7} eventually (2 gets pulled in),
    with candidate L=210, T unconfirmed at length — same caveat as above.
  - **The real crux for the outliner**, in this framing's terms: (a) prove existence of a finite
    "core" prime set S such that all sufficiently large a_i are divisible by some prime in S
    (this is NOT the same as "only finitely many primes ever appear" — it is a much weaker and
    more plausible claim, and is the correct target for the prime-bookkeeping/density explorers);
    (b) prove that, given such S, the greedy process's actual minimal choice at each step for
    n ≥ N1 coincides with the "smallest x with S-signature hitting R" choice — i.e. rule out that
    a smaller x could sneak in via a coincidental shared large prime with some specific a_i not
    covered by S. Part (b) is where the finite-state model's clean derivation of T, L given S
    would need a genuine argument (not just pigeonhole) — likely via a counting/gap bound showing
    such "lucky" x's, when they exist, are never smaller than the S-signature-based candidate, or
    do not disturb periodicity when they do occur. This is the shared true gap to flag to the
    outliner regardless of which framing (finite-state, prime-bookkeeping, density) is used.
