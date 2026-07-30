## Status
solved

## Build summary
Completed the whole-problem proof in `results/imo-2026-06/approaches/finite-support-maximal-linked.md`.

The proof imports the four certified round-1 lemmas, then closes finite control by strict marked-prime radical descent. For an arbitrary prime `p` in an inclusion-minimal positive support, every nonterminal descent step preserves `p`, replaces the current support by another inclusion-minimal positive support, and strictly decreases its integer radical. At termination, the complementary support has radical below `a_1`. The empty and nonempty complement cases are handled separately, without invoking `mu(emptyset)`, and give a uniform finite bound on every prime in every minimal positive support. Their union is therefore contained in a finite prime set `P`, which controls the upfamily in both directions. The certified global periodic-enumeration lemma then gives positive integers `T,L` with `a_{n+T}=a_n+L` for every `n>=1`.

All builder details from the outline review are explicit: `rad(emptyset)=1` is used only for stopping; the finite maximum ranges only over nonempty supports; existence of each `mu(S)` is justified; and the iteration explicitly retains the marked prime at each replacement.

No specification concern or remaining proof gap was found.
