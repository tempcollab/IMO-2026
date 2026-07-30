# Build report — density-bounded-recruitment (imo-2026-06), round 1

## Status: partial

## What I did
Reframed the density lane into its productive form and **reduced the entire problem to a single clean crux**, proving the full endgame rigorously around it.

- Proved (full): Step 1 (all terms pairwise non-coprime, so every term ∈ E_∞); Step 2 (every term has a prime ≤ a_1, colors finite); Step 3 (gaps ≤ a_1); Step 4 (sequence = increasing enumeration of E_∞∩[a_1,∞)); Step 5 (periodicity + `a_{n+T}=a_n+L` for every n) **conditional on the Structural Lemma**.
- The whole problem now rests on ONE statement:
  **Structural Lemma:** every two terms share a prime factor ≤ a_1 (colors pairwise intersect) ⇔ no prime > a_1 is ever load-bearing.
- Endgame delivers a valid (non-minimal) `(T,L)` with `L=∏(small primes present)`; verified numerically `a_{n+T}=a_n+L` and `enum==seq` for a_1∈{15,35}; no disjoint-color pair on 20 seeds.

## Key finding for the orchestrator (diversity/gap)
The outline's stated density mechanism ("finitely many primes divide infinitely many terms") is **provably FALSE**: since E_∞ is periodic, every prime meets it in positive density, so infinitely many primes divide infinitely many terms. Asymptotic density therefore cannot be the tool. The true crux is a **per-pair magnitude** statement (Structural Lemma), NOT an asymptotic one. This is the same crux as enum-covering's Lemma F, restated as pairwise-color-intersection.

## Relation to enum-covering
Same isolated crux (finiteness / no large relevant prime), reached by a genuinely different, cleaner formulation: **"every two terms share a small prime."** This is a crisper, checkable target than "minimal covering sets ⊆ R" and may be the better statement for the field to attack. Recommend both approaches now aim at this exact pairwise statement.

## Spec concerns
- None on the problem statement. One methodological note: density (my assigned lane) does not close the crux; the productive content of the lane turned out to be the *magnitude* reduction (primes ≤ a_1 suffice), which I delivered. If the orchestrator wants a distinct-from-enum-covering attack on the crux, the Structural Lemma likely needs a greedy-minimality / ordering argument (how the sieve forbids a disjoint-color term from ever being selected), not density — a candidate for next round's outliner.

## Promotable lemmas (fully proved, reviewer may certify)
Steps 1–4 (pairwise non-coprime; prime ≤ a_1 in every term; bounded gaps; enumeration-of-E_∞) and Step 5 (periodicity from pairwise-intersecting colors). All are independent of the open Structural Lemma except Step 5's hypothesis.
