## Compensation Move (M2)

**Statement.** Suppose Mulan holds an (unlabelled) triangle (t,u,w) with t+u+w = nθ (n≥2
integer), t < θ, and no current angle equal to θ. Then:

1. Not both of u,w are ≥ (n-1)θ. (Proof: if both were, u+w ≥ 2(n-1)θ; but also
   u+w = nθ-t > (n-1)θ and u+w < nθ; combining gives 2(n-1)θ < nθ, i.e. n<2, contradicting
   n≥2.) Call the one that is < (n-1)θ "keep-small", the other "s".
2. Mulan splits vertex s at x₁ = θ-t (valid: 0<x₁ since t<θ; x₁<s since
   s+t = nθ-keep-small > θ). Applying the Master Cut Formula with a=s, b=t, c=keep-small
   gives
     Child_A = (t, θ-t, (n-1)θ),   Child_B = (keep-small, s-θ+t, θ).
   Child_B always contains θ exactly.
   - If n=2: (n-1)θ=θ, so Child_A also contains θ — both branches lose for Shan-Yu, the
     game ends in this one move.
   - If n≥3: Child_A has no angle equal to θ (t≠θ given; θ-t=0 impossible since t>0;
     (n-1)θ=θ would force n=2, excluded), so it is the safe continuation. Designate
     Target := (n-1)θ ≥ 2θ, Shield := t, Growing := θ-t; General Chip Move (M1) is now
     applicable.

**Proof.** Direct computation via the Master Cut Formula, verified by substitution (see
derivation above). ∎

**Verification.** Re-derived independently by the reviewer; checked with the full
independent Python simulation of the entire forward algorithm (3600 random trials,
n=2..19), 0 failures.

**Source.** Certified from `results/imo-2026-04/approaches/chip-double-force.md` (round 2).
