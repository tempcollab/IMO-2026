## General Chip Move (M1)

**Statement.** Suppose Mulan holds a triangle with three *designated* roles: Target (angle
T), Shield (angle S), Growing (angle G), with T+S+G = nθ (n a positive integer ≥2, θ the
fixed target angle), T > θ, and no current angle equal to θ. Mulan cuts the Target vertex at
the point where x = θ, measured so that (using the Master Cut Formula with a=T, b=G, c=S):

  Discard-branch = (G, θ, T+S-θ)   — always contains angle θ exactly.
  Keep-branch    = (S, T-θ, G+θ).

- If T ≠ 2θ: the Keep-branch has no angle equal to θ (S ≠ θ by induction, T-θ ≠ θ since
  T≠2θ, G+θ ≠ θ since G>0), so it is a genuine safe continuation with new roles
  Target'=T-θ, Shield'=S, Growing'=G+θ.
- If T = 2θ: the Keep-branch becomes (S, θ, G+θ), which also contains θ. Both branches
  contain θ; the game ends here with Mulan winning, regardless of which branch Shan-Yu
  picks (the discard-branch is an immediate win; the keep-branch is a triangle that, on
  the very next check, already has an angle equal to θ).

**Proof.** Direct substitution into the Master Cut Formula; case split on T=2θ vs T≠2θ as
above. ∎

**Verification.** Re-derived independently by the reviewer; checked with a full independent
Python simulation of the entire forward algorithm (3600 random trials, n=2..19), 0 failures.

**Source.** Certified from `results/imo-2026-04/approaches/chip-double-force.md` (round 2).
