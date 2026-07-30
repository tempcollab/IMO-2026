# proof-builder report — equalization-potential-bound (imo-2026-03, round 1)

## Verdict: dead end, reported honestly (Status: unsolved)

Resolved the outline-reviewer's circularity gate definitively and negatively.
Proved (Lemma D + Lemma E in the approach file) that no single, rank-only,
configuration-independent linear weight vector `w_i` can give a valid AND
tight upper bound for Xiang Yu's forced value `V(A)` at the conjectured
optimum, because:

1. The conjectured optimal ("geometric") configuration is a **strict
   interior point** of the ordered simplex `Δ_n = {p_1≥...≥p_{n+1}≥0, Σ=1}`
   for every `n` (Lemma E, proved via the standard vertex description
   `V_k=(1/k,...,1/k,0,...,0)`, `k=1,...,n+1`, of this polytope).
2. A linear functional cannot attain its maximum over a polytope at an
   interior point without being **constant** on the whole polytope (Lemma D,
   proved directly: perturb in the gradient direction, contradiction).
3. Chaining the required validity (`Σw_ip_i ≥ V(A)` everywhere) with the
   required tightness (`max_A Σw_ip_i = c(n) = V(p^*)`) forces the linear
   functional to attain its own max exactly at the interior point `p^*`,
   hence by (2) it must be the **trivial constant weighting**
   `w_i ≡ c(n)`, which is a tautological restatement of the theorem
   (validity of this trivial bound requires already knowing
   `V(A) ≤ c(n)` for all `A` — exactly the casework the theorem needs, not
   a shortcut around it).
4. Confirmed concretely at `n=1` by computing the exact value function
   `V(p_1,p_2) = min(p_1, p_2+p_1/2)` via full case analysis of Xiang Yu's
   one cut (which piece he splits and where) — genuinely piecewise-linear
   (min of two distinct lines, crossing at `p_1=2/3`), so no single linear
   `w` can equal it identically. Also exhibited the natural non-trivial
   candidate ("always bisect the top piece", `w=(1/2,1)`) as an **invalid**
   bound: it evaluates to `3/4 > c(1)=2/3` at `A=(1/2,1/2)`, verified by a
   quick script (Bash `python3 -c ...` with exact `Fraction` arithmetic).

This is a genuine, non-patchable structural obstruction (about the geometry
of the interior optimum vs. the polytope's vertices), not just a technical
gap — so per the outline's own instruction and CLAUDE.md's rigor rules, this
is reported as a dead end rather than papered over.

## What is NOT established

This approach contributes nothing toward actually proving
`c(n) = 2^n/(2^{n+1}-1)`; the upper-bound half of the theorem must be (and,
per the outline-reviewer, is being) carried by
`geometric-dominance-construction` and `recursive-embedding-induction`,
which do the necessary adversarial case analysis directly rather than
attempting to shortcut it via a global linear functional.

## File written
`/home/agentuser/repo/results/imo-2026-03/approaches/equalization-potential-bound.md`
— Status: unsolved, full derivation of the impossibility (Lemma D, Lemma E,
the n=1 exact computation, and the general-n argument), plus two promotable
lemmas (Lemma D and Lemma E, both fully proved and reusable for any future
LP-relaxation attempt on this or related problems) and the exact n=1 value
function `V(p_1,p_2)=min(p_1,p_2+p_1/2)` as a reusable sanity-check fact.

## Memory update
Appended two rules to `/tmp/memory/proof-builder.md` about recognizing this
interior-point/vertex obstruction early (check where the conjectured optimum
sits relative to the polytope, and check linearity of the true value
function at the smallest case) before investing further round-time in a
global-weighting/LP-relaxation outline.
