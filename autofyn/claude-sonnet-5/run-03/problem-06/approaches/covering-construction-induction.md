## Status
unsolved

## Approaches tried
(none yet — first pass)

## Current best
Empty.

## Approach

**Target:** the whole theorem, via a genuinely different route from the pigeonhole-existence
approaches: instead of proving an abstract finite state space exists and invoking pigeonhole, this
approach TRIES TO GUESS/CONSTRUCT the explicit eventual pattern (a specific covering system: a
finite list of (prime, residue) pairs covering Z) directly from a_1, and then proves by strong
induction / minimal-counterexample that the actual greedy sequence must conform to it from some
point on — i.e. an explicit-construction-then-verify proof, the standard shape required for
"find all n" / "construct + verify" style olympiad answers, applied here to constructing (T, L)
rather than assuming their existence abstractly.

**Technique:** explicit construction (à la covering congruences / Erdős-style covering systems)
+ proof by minimal counterexample (assume the greedy sequence deviates from the constructed
pattern at the EARLIEST possible point, derive a contradiction with either minimality of the greedy
rule or with the covering property).

**Skeleton:**

1. **Construct the candidate covering system.** From S = primes(a_1) = {p_1,...,p_k} (k ≥ 1),
   define the candidate modulus L* and residue set G* exactly as in `core-signature-pigeonhole`
   steps 1–3 (L* = ∏ p_i, G* = residues mod L* that are "S-complete enough"), BUT here we do not
   derive G* abstractly via pigeonhole on an unknown-length prefix — instead we EXPLICITLY compute
   it from a_1 alone as an a priori guess: define G*_0 := { r mod L* : r ≡ 0 mod p_i for at least
   one p_i for EVERY subset that ever needs covering } — concretely, START with the guess that the
   eventual pattern is simply "x divisible by at least one prime of S" (the coarsest possible
   covering system built from S), i.e. G*_0 = { r mod L* : gcd(r, L*) > 1 } ∪ {0}. This is only a
   FIRST APPROXIMATION (may need refinement — see step 3) but gives an explicit, checkable
   candidate T_0 = |G*_0|, computable directly from a_1 by brute enumeration over Z/L*Z. — direct
   construction, no existence argument needed for this coarse guess.

2. **Verify the coarse guess handles the a_1-constraint exactly (not just sufficiently).** By
   construction every r ∈ G*_0 is divisible by some prime of S, hence any x ≡ r (mod L*) has
   gcd(x, a_1) > 1 automatically — this handles i=1 for ALL n, unconditionally, by definition of
   S = primes(a_1). — trivial from the construction.

3. **KEY GAP — refine construction / prove minimality-forced conformance for i ≥ 2.** The coarse
   guess G*_0 does NOT yet account for constraints from a_2, a_3, .... Two sub-strategies to give
   the builder:
   (a) *Refinement-by-induction*: process constraints i = 2, 3, ... one at a time; at each step,
   if the current candidate covering system (L, G) already ensures gcd(x,a_i)>1 for x ≡ r ∈ G
   automatically (because a_i's own S-signature already meets every "gap" in G), keep (L,G)
   unchanged; otherwise REFINE by intersecting G with the extra condition "x shares a prime with
   a_i" reduced mod lcm(L, primes(a_i) ∩ [relevant small primes]) — this can only make L grow and G
   shrink (as a fraction of L), so termination of the refinement process (i.e. that only FINITELY
   many refinements ever occur) is exactly as hard as the No-Escape Lemma in the sibling approach —
   this sub-strategy does not avoid the core difficulty, it relocates it into "does the refinement
   process terminate," a genuinely equivalent-strength open question.
   (b) *Minimal-counterexample strategy (the genuinely new idea in this approach)*: Suppose, for
   contradiction, that the true greedy sequence deviates from ANY finite covering-system pattern
   infinitely often (i.e. no eventual (T,L) exists). Since the problem is a claimed theorem, use
   the MINIMALITY of the greedy choice itself as the source of contradiction: if a_{n+1} were
   forced (by some deviation) to be strictly larger than the "coarse-guess" prediction infinitely
   often, examine what SMALLER value the greedy rule skipped over and show it must already be
   admissible by an earlier-established invariant, contradicting minimality of the true greedy
   pick. This converts "prove periodicity" into "derive a contradiction from a hypothetical
   non-periodic tail using the greedy rule's own minimality as the monovariant" — structurally
   different from steps 1-3(a) because it never needs to fully characterize G in closed form; it
   only needs ONE clean contradiction from non-periodicity. This is the most promising genuinely
   NEW idea in this approach but is currently just a proof STRATEGY, not a proof — the actual
   contradiction argument (what exactly goes wrong if the tail is not eventually periodic) has not
   been found and is the open gap.

4. **Conclusion given step 3.** Whichever sub-strategy closes, the output is an explicit (L, T)
   (or at least existence via the contradiction route) with a_{n+T} = a_n + L for n large. State
   the explicit L, T formula from the surviving construction and verify against the explorers'
   computed examples (a_1=15 → T=8,L=30; a_1=105 → T=58,L=210) as a sanity check once a candidate
   formula/algorithm exists.

**Key lemmas (claim + mechanism):**
- Coarse guess handles i=1 unconditionally (step 2) — trivial from S = primes(a_1).
- Refinement terminates in finitely many steps (step 3a) OR minimal-counterexample yields a
  contradiction (step 3b) — NEITHER is established; this is the same underlying difficulty as the
  sibling approaches' No-Escape Lemma, approached from the "explicit construction + refine" or
  "assume non-periodic tail, contradict minimality" angle instead of "pigeonhole on signature
  family." Genuinely worth pursuing in parallel since a contradiction-style argument (3b) may be
  easier to close than a constructive closed form (3a) even though both attack the same wall.

**Open gaps:** All of step 3 — this approach is explicitly flagged as attacking the SAME core
difficulty as `core-signature-pigeonhole` and `growth-bound-density` (they all reduce to some form
of "no lucky large-prime escape can happen infinitely often relative to a finite covering
pattern"), but via a different proof SHAPE (explicit refinement / minimal-counterexample rather
than abstract pigeonhole). Per the run's rule against single-gap traps: if after one round all
three of these approaches report the identical unresolved gap with no new mechanism, the next
round's outliner should treat this as a genuine 3-round-shared-wall signal and seek a totally
different top-level framing (e.g. an analytic/probabilistic density argument, or reformulating
the whole problem in terms of a different combinatorial object entirely) rather than continuing to
refine any of these three.

**Cases to cover:** a_1 prime power: coarse guess G*_0 is already exact (T=1, L=p) since S={p} and
"divisible by p" is already the full constraint — no refinement ever needed, immediate sanity
check that the construction is non-vacuous.

**Watch out for:** conflating "sufficient" (step 2's easy direction) with "the greedy actually
achieves this minimum" (step 3's hard direction) — every approach in this population risks this
same confusion; the outline explicitly separates them here to make the gap impossible to
hand-wave past.
