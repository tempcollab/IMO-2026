"""
Test the XOR/overlap decomposition (genuinely 5th framing).

Key identity: N(t) = N_F(t) + N_R(t), where
  N_F(t) = #{top-fragments >= t}  (top piece 2^n split into fragments, total mass 2^n)
  N_R(t) = #{below-top pieces >= t} (refinement of T_{n-1} with <= n-1 marks, total mass 2^n-1)

(a+b) mod 2 = (a mod 2) + (b mod 2) - 2*(a mod 2)*(b mod 2)

So D(global) = D_F + D_R - 2*C, where
  D_F = int(N_F mod 2) dt = standalone alternating sum of top-fragments
  D_R = int(N_R mod 2) dt = standalone alternating sum of below-top pieces
  C   = int (N_F mod 2)*(N_R mod 2) dt = overlap of odd-parity regions.

Induction on n: R is a <= (n-1)-mark refinement of T_{n-1}, so D_R >= 1 by IH.
Need: D_F + D_R - 2C >= 1  <=>  D_F >= 2C - (D_R - 1).
Since D_R >= 1, sufficient: D_F >= 2C, i.e. the top-fragment odd-parity measure
>= 2x the overlap of the two odd-parity regions.

Test: is D_F >= 2C always? Or the weaker D_F + D_R - 2C >= 1?
"""
from fractions import Fraction as F

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**k)*v for k,v in enumerate(s))

def Nfunc(pieces, t):
    """#{pieces >= t} for a real threshold t (Fraction)."""
    return sum(1 for p in pieces if p >= t)

def D_integral(pieces):
    """D = integral of (N mod 2) dt, computed exactly via breakpoints.
    N(t) is a step function changing at each piece value.
    Integrate over [0, max]. Partition [0, max] by piece values."""
    s = sorted(set([F(0)] + [p for p in pieces]), reverse=False)
    mx = max(pieces)
    total = F(0)
    for i in range(len(s)-1):
        lo, hi = s[i], s[i+1]
        mid = (lo+hi)/2
        N = Nfunc(pieces, mid)
        if N % 2 == 1:
            total += (hi - lo)
    return total

def overlap_C(top_frags, below_pieces):
    """C = int (N_F mod 2)*(N_R mod 2) dt over [0, max]."""
    allvals = sorted(set([F(0)] + list(top_frags) + list(below_pieces)), reverse=False)
    total = F(0)
    for i in range(len(allvals)-1):
        lo, hi = allvals[i], allvals[i+1]
        mid = (lo+hi)/2
        NF = Nfunc(top_frags, mid)
        NR = Nfunc(below_pieces, mid)
        if NF % 2 == 1 and NR % 2 == 1:
            total += (hi - lo)
    return total

def tower(n):
    return [F(2**k) for k in range(n,-1,-1)]

# Verify the XOR identity on random refinements of T_n
import random
random.seed(42)

def random_refine(T, nmarks):
    """Apply nmarks random splits to tower T."""
    pieces = list(T)
    for _ in range(nmarks):
        if len(pieces) <= 1: break
        # pick a piece to split (weighted toward larger)
        idx = random.randrange(len(pieces))
        V = pieces[idx]
        # random cut position
        f = V * F(random.randint(1, 8), 16)  # between 0 and V
        if f <= 0 or f >= V: continue
        pieces = pieces[:idx] + [f, V-f] + pieces[idx+1:]
    return sorted(pieces, reverse=True)

print("Verifying XOR identity D = D_F + D_R - 2*C on random refinements of T_3, T_4, T_5:")
for n in [3,4,5]:
    T = tower(n)
    top = T[0]; below = T[1:]
    fails = 0
    Cvals, DFvals, DRvals, Dvals = [], [], [], []
    for trial in range(2000):
        # split top into r fragments (use 1..n marks on top), rest on below
        ntop_marks = random.randint(1, n)
        nbelow_marks = random.randint(0, n - ntop_marks)
        top_frags = random_refine([top], ntop_marks)
        below_pieces = random_refine(below, nbelow_marks)
        global_pieces = top_frags + below_pieces
        Dg = D_of(global_pieces)
        DF = D_integral(top_frags)
        DR = D_integral(below_pieces)
        C = overlap_C(top_frags, below_pieces)
        if Dg != DF + DR - 2*C:
            fails += 1
        Cvals.append(C); DFvals.append(DF); DRvals.append(DR); Dvals.append(Dg)
    print(f"  T_{n}: {fails} identity failures / 2000. min D={min(Dvals)}, min D_F={min(DFvals)}, min D_R={min(DRvals)}, max C={max(Cvals)}")

print()
print("Key test: is D_F >= 2*C always? (sufficient condition for the bound given IH D_R>=1)")
for n in [3,4,5]:
    T = tower(n); top=T[0]; below=T[1:]
    fails = 0; tight=0; worst=None
    for trial in range(5000):
        ntop_marks = random.randint(1, n)
        nbelow_marks = random.randint(0, n - ntop_marks)
        top_frags = random_refine([top], ntop_marks)
        below_pieces = random_refine(below, nbelow_marks)
        DF = D_integral(top_frags)
        C = overlap_C(top_frags, below_pieces)
        if DF < 2*C:
            fails += 1
            if worst is None or (2*C - DF) > worst[0]:
                worst = (2*C - DF, DF, C, top_frags, below_pieces)
    print(f"  T_{n}: D_F < 2C in {fails}/5000 cases.", end="")
    if worst:
        print(f" worst deficit D_F-2C = {-worst[0]} (D_F={worst[1]}, C={worst[2]})")
        print(f"    top_frags={worst[3]}, below={worst[4][:6]}...")
    else:
        print(" (never violated)")

print()
print("Check the actual needed condition: D_F + D_R - 2C >= 1 (the real target). This = D(global) >= 1, already known.")
print("But the INDUCTIVE question: assuming D_R >= 1 (IH), is D_F + 1 - 2C >= 1 i.e. D_F >= 2C?")
print("And without IH: what is min of D_R over refinements of T_{n-1} (standalone)? Should be >= 1.")
for n in [3,4,5,6]:
    T = tower(n); below=T[1:]
    mn = None
    for trial in range(3000):
        nbelow_marks = random.randint(0, n-1)
        below_pieces = random_refine(below, nbelow_marks)
        DR = D_integral(below_pieces)
        if mn is None or DR < mn: mn = DR
    print(f"  T_{n} below-top (=T_{n-1} ref): min D_R = {mn} (should be >= 1)")
