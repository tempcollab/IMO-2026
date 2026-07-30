# outline-reviewer rules

ALWAYS: for imo-2026-03, sanity-check strategy claims with a small recursive grid-search of the n=2 cut-and-choose game (cheap, ~seconds, exposed nothing false in round 1 but confirmed ladder value 4/7 and the C(2) cap) (round 1)
ALWAYS: when an outline proposes a strengthened induction hypothesis to fix one case, require the builder to re-prove ALL cases at the strengthened strength — changing the IH is a whole-induction restructure, not a local patch (dyadic-recursion Case D, round 1)
NEVER: accept "recurse on the sub-ladder" style steps without checking the sub-object actually matches the induction's hypothesis class (untouched rungs of a cut dyadic ladder are an arbitrary rung subset, not a smaller dyadic ladder — dyadic-recursion Step 3, round 1)
ALWAYS: for multi-Match chain constructions, check intermediate legality, not just final feasibility — here final x2 >= 0 luckily implies every running remainder r_k = tail + x2 >= a_{k+1}, a one-line fact the outline left implicit; require the builder to state it (Case 3a MultiMatch, round 2)
ALWAYS: when executing a copy_approach, write the twin's body file yourself immediately (source prose + divergence) — the outliner doesn't create it and the builder needs it to exist at dispatch (discrepancy-halving-bands, round 2)
NEVER: treat "not every signed sum is Match-reachable" claims as pedantry — reachable residuals are capped by the current max piece, so ternary-realizability lemmas MUST carry a smallness hypothesis or they are false (|5+3-1|=7>5 example, round 2)
