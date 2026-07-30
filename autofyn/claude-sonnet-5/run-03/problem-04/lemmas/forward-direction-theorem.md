## Forward Direction Theorem

**Statement.** For every integer n≥2 (θ=180°/n) and every starting triangle (a,b,c) with
a+b+c=nθ, Mulan has an explicit strategy — built only from the General Chip Move (M1) and
Compensation Move (M2) — that forces a win (some angle exactly θ) in a finite (O(n)) number
of moves, regardless of how Shan-Yu replies at each step.

**Algorithm.**
1. If some starting angle already equals θ: Mulan has already won.
2. Else if some starting angle t<θ: apply M2 to (t,u,w). This ends the game (n=2) or
   produces Target=(n-1)θ, Shield=t, Growing=θ-t (n≥3); go to 4.
3. Else (all three angles >θ, forced since step 1/2 excluded ≤θ): designate any one angle
   as Target and the other two as Shield/Growing (arbitrary fixed choice). Apply M1
   repeatedly; Target strictly decreases by θ each application. Either it hits exactly
   Target=2θ (terminal win), or the current Target drops below θ for the first time
   without ever landing on exactly θ (since Target=θ can only arise from a prior
   Target=2θ, which is caught as terminal first) — in the latter case treat the current
   triple as fresh and go to step 2/M2 (step 4).
4. If Target=(n-1)θ arose from an M2 application: apply M1 repeatedly; since Target is an
   exact multiple of θ it decreases through (n-2)θ,...,3θ,2θ without ever passing through a
   non-multiple value, terminating (win) after exactly n-2 further M1 applications.

Throughout, Shield is a fixed real value ≠θ from the moment it is designated (either it was
one of the three original angles known to be >θ, or it is a value <θ produced by M2), and
Growing is a real value that only increases (from a value that is either >θ, if never
touched, or in (0,θ) initially after an M2 hand-off, thereafter always >θ after one
increase) — in either case Growing≠θ throughout, and this is proved rigorously (an increase
of exactly θ from a positive value that is never itself θ cannot land on θ).

**Proof.** Full case analysis given in `results/imo-2026-04/approaches/chip-double-force.md`,
"Current best" section, "Full algorithm and termination."

**Verification.** Independently reproduced by the reviewer: reimplemented the literal
algorithm in Python and ran it for n=2..19, 200 random starting triangles per n (3600 total
trials); 0 failures, every trial terminates with an exact win, matching every algebraic
identity claimed (Discard-branch always contains θ; Keep-branch/Child_A never contains θ
except at the designed terminal steps).

**Source.** Certified from `results/imo-2026-04/approaches/chip-double-force.md` (round 2).
