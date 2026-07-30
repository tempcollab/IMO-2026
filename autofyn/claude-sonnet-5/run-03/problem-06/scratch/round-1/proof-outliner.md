## imo-2026-06

core-signature-pigeonhole: new
Target: prove a_{n+T}=a_n+L for explicit T,L via CRT/finite-state pigeonhole on prime "signatures."
Technique: Let S = primes(a_1) (finite, known immediately — no existence proof needed). Every a_i
is divisible by some prime of S (from gcd(a_i,a_1)>1). Track D_i = S ∩ primes(a_i); the family of
distinct D_i's stabilizes by pigeonhole on a monotone chain in the finite poset P(S)\{∅}. This
gives a fixed nonempty "good residue set" G mod L=lcm(S) via CRT, sufficient for admissibility.
Skeleton: (1) S=primes(a_1), D_i nonempty ∀i. (2) chain R_n stabilizes (pigeonhole, 2^k-1 states).
(3) CRT: G ⊆ Z/LZ of residues hitting every D∈R, nonempty. (4) sufficiency: x≡r∈G(mod L) ⟹
gcd(x,a_i)>1 ∀i≤n. (5) KEY GAP: necessity ("No-Escape Lemma") — true greedy min equals
min{x>a_n: x mod L∈G}, i.e. no smaller x can cheat via a lucky prime outside S. (6) given (5),
tail is periodic residue-selection on Z/LZ: T=|G|, shift L, mechanical.
Key lemmas: chain-stabilization (pure pigeonhole, essentially free); No-Escape Lemma (open, hard).
Open gaps: step 5 is the entire remaining difficulty. Also must fold in finitely many i<N1 cleanly.
Cases to cover: a_1 prime power (trivial sanity check, S={p}, T=1,L=p); general k≥2 substantive.
Watch out for: S=primes(a_1) alone may be too coarse — true minimal period empirically uses a
larger modulus (e.g. a_1=15 uses L=30=lcm(2,3,5), not 15) since primes not dividing a_1 (like 2)
get pulled in; this approach may only capture a periodic SUPERstructure, not the exact minimal
(T,L), and the builder must check/extend S if so.

growth-bound-density: new
Target: same whole theorem, via bounding gaps first (density/sieve), THEN extracting finite-state
periodicity — a different route than signature-family pigeonhole.
Technique: Jacobsthal/sieve-style density bound + aimo-0447-style grid-counting, dual direction
(bound how soon a valid next term appears, not how large numbers must be).
Skeleton: (1) S=primes(a_1), D_i nonempty ∀i (shared fact with sibling). (2) density lemma: an
interval of length L0=∏S always contains a multiple of L0. (3) PROVEN (not just conjectured): any
x≡0 mod L0 is divisible by every prime of S, hence automatically meets D_i for every i (D_i⊆S
nonempty) — giving the fully rigorous unconditional bound a_{n+1}-a_n ≤ L0 for ALL n, no gap here.
(4) KEY GAP: build state σ_n=(a_n mod M, S-profiles of last L0 terms) and show it's a genuine
finite deterministic state (i.e. a bounded lookback window truly determines the whole future —
this is a windowed restatement of the No-Escape Lemma, not an avoidance of it). (5) pigeonhole on
finite functional graph ⟹ cycle ⟹ T,L via matched repeated states.
Key lemmas: a_{n+1}-a_n ≤ L0 (step 3) is FULLY RIGOROUS and should be certified as a standalone
lemma in results/imo-2026-06/lemmas/ once verified — reusable by every other approach (e.g. as the
"gaps are bounded" input to core-signature-pigeonhole or covering-construction-induction).
Open gaps: step 4 (finite window suffices) — same underlying difficulty as sibling's No-Escape
Lemma, reformulated.
Cases to cover: a_1 prime power trivial (L0=p, T=1 immediately).
Watch out for: state space in step 4 could be huge — argument must stay an abstract pigeonhole
existence claim, not a literal enumeration attempt by the builder.

monovariant-telescoping: new
Target: same whole theorem, via a genuinely different top-level object: track, per prime p|a_1,
the depth e_p(n)=v_p(gcd(a_1,a_n)), look for a monovariant forcing eventual stabilization of each
prime's "role" (permanently active w/ periodic usage, or abandoned), then CRT-combine into (T,L).
Technique: monovariant / eventually-constant-sequence argument, in the style of aimo-0477's
v_p-monotonicity trick, but applied to gcd-with-a_1 depth rather than a ratio-sum.
Skeleton: (1) define e_p(n) per prime of a_1; note it need not be monotone raw, so track a
weighted sum Φ(n)=Σ v_p(gcd(a_1,a_n))·w_p as the candidate monovariant (weights/direction TBD —
open). (2) KEY GAP (Eventual Prime-Role Dichotomy): each prime of a_1 eventually either drops out
forever or settles into periodic usage — monotonicity/boundedness of Φ would force this but the
right Φ has not been found. (3) bootstrap to periodicity via CRT given (2) (mechanical). (4)
extend dichotomy to primes NOT dividing a_1 (e.g. 2 pulled into a_1=15's pattern) — strictly harder
than (2), proposed to import growth-bound-density's a_{n+1}-a_n≤L0 lemma to bound which new primes
can ever become permanently active.
Key lemmas: none yet established rigorously; this is the least worked-out, most exploratory
approach in the field, kept for framing diversity (per-prime dynamics vs. global signature
combinatorics) in case the pigeonhole-style siblings stall.
Open gaps: steps 1-2 (no monovariant found yet), step 4 (extension to non-a_1 primes).
Cases to cover: a_1 prime power trivial.
Watch out for: conflating "p divides a_n" with "p is the specific prime explaining
gcd(a_1,a_n)>1" — easy bookkeeping error that breaks the whole monovariant definition.

covering-construction-induction: new
Target: same whole theorem, via explicit construction of a candidate covering system from a_1
directly, then either (a) inductive refinement or (b) proof-by-minimal-counterexample using
minimality of the greedy rule itself, to force the true sequence to conform.
Technique: explicit covering-congruence-style construction + minimal-counterexample / greedy-
minimality contradiction (distinct proof SHAPE from the pigeonhole-existence siblings, even though
it targets the same underlying difficulty).
Skeleton: (1) S=primes(a_1), coarse guess G*_0 = residues mod L*=∏S divisible by some prime of S
(handles i=1 exactly, unconditionally — trivial). (2) KEY GAP, two sub-strategies given to
builder: (a) refine G by processing a_2,a_3,... one at a time, intersecting in extra conditions —
termination of refinement is exactly as hard as the No-Escape Lemma (relocates, doesn't avoid, the
difficulty); (b) NEW idea — assume for contradiction the tail is never eventually periodic, and
derive a contradiction from the greedy rule's own minimality (what smaller value did it skip, and
why is that already forced-admissible) — a genuinely different proof shape, not yet executed.
(3) conclusion given either sub-strategy closing; verify against explorer data (a_1=15→T=8,L=30;
a_1=105→T=58,L=210).
Key lemmas: coarse guess handles i=1 unconditionally (trivial); refinement-terminates OR
contradiction-from-minimality (both open, same core difficulty as siblings, different attack shape).
Open gaps: all of step 2 — explicitly flagged as reducing to the SAME "no lucky-prime-escape"
wall as core-signature-pigeonhole and growth-bound-density. Per CLAUDE.md's shared-gap-plateau
rule: if next round all three report the identical unresolved gap with no new mechanism, the
following round's outliner should open a genuinely different top-level framing (e.g. analytic/
probabilistic density, or a wholly different combinatorial encoding) rather than refining further.
Cases to cover: a_1 prime power trivial (G*_0 already exact, no refinement needed).
Watch out for: conflating the easy sufficiency direction with the hard "greedy actually achieves
this" direction — same risk as the other approaches, called out explicitly here too.

Registration note: mcp__approach-ranker__register_approach was not available in this session's
tool list (only sample_approaches was exposed); the four approach files above were written to
results/imo-2026-06/approaches/ but could not be registered via MCP this round. Whoever runs next
(or the harness) should register them, or the outline-reviewer/orchestrator should invoke
registration before ranking.

Slugs created this round:
- core-signature-pigeonhole — S=primes(a_1) + signature-family pigeonhole + CRT residue set;
  strongest/most standard route, single clearly-isolated "No-Escape Lemma" gap.
- growth-bound-density — bounds gaps first via a fully rigorous a_{n+1}-a_n≤L0 lemma (worth
  certifying standalone), then finite-state pigeonhole on a bounded lookback window.
- monovariant-telescoping — per-prime depth/monovariant framing (aimo-0477-style), most
  exploratory/least worked-out, kept for genuine framing diversity.
- covering-construction-induction — explicit covering-system construction + minimal-counterexample
  contradiction strategy, a different proof shape attacking the same core difficulty.
