"""
Round 6: Mission A supplement + Mission B.

Mission A supplement: check ALL breakpoints (not just D=1) for D < 1.
  D = 2*S_+ - D_n is always odd (D_n odd). So D < 1 means D <= -1.
  Check: does any breakpoint of T_n have D <= -1?

Mission B: search for non-tower Liu configs with min D >= 1/D_n.
  For n=2,3,4, search integer configs and random reals.
  Compute min D using breakpoint-restricted optimization (grid + breakpoints).
"""
from fractions import Fraction as F
from itertools import combinations, product
import random
import math

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def tower(n):
    return [F(2)**(n-k) for k in range(n+1)]

def Dtower(n):
    return alt_sum(tower(n))

# ============================================================
# Mission A supplement: check ALL breakpoints of T_2, T_3 for D < 1
# ============================================================

print("=" * 70)
print("Mission A supplement: ALL breakpoints, check D < 1 (D <= -1)")
print("=" * 70)

# T_2 = (4, 2, 1). D_n = 7. Xiang uses <= 2 marks.
# Breakpoints: every fragment ties an adjacent piece.
# Enumerate all 2-mark refinements at breakpoints.

def check_all_breakpoints_T2():
    """T_2 = (4,2,1). 2 marks. Enumerate all breakpoint refinements."""
    T = [F(4), F(2), F(1)]
    D_n = 7
    min_D = None
    count = 0
    neg_count = 0

    # Case 1: both marks on piece 4 (cascade: 4->p+q, p->r+s)
    # Breakpoints: q ties 2 or 1; r or s ties 2 or 1 or the other fragment.
    for q in [F(1), F(2)]:  # q=1 (ties 1), q=2 (ties 2)
        p = F(4) - q
        # split p into r+s, r>=s. Breakpoints: s ties 1 or 2 or q.
        for s in [F(1), F(2), q]:
            if s <= 0 or s > p/2:
                continue
            r = p - s
            cfg = sorted([r, s, q, F(2), F(1)], reverse=True)
            D = alt_sum(cfg)
            count += 1
            if min_D is None or D < min_D:
                min_D = D
            if D < 1:
                neg_count += 1
                print(f"  D<1! cfg={cfg} D={D}")

    # Case 2: one mark on piece 4, one on piece 2
    for q1 in [F(1), F(2)]:  # split 4 into (4-q1)+q1, q1 ties 1 or 2
        for q2 in [F(1)]:  # split 2 into (2-q2)+q2, q2 ties 1
            cfg = sorted([F(4)-q1, q1, F(2)-q2, q2, F(1)], reverse=True)
            D = alt_sum(cfg)
            count += 1
            if min_D is None or D < min_D:
                min_D = D
            if D < 1:
                neg_count += 1
                print(f"  D<1! cfg={cfg} D={D}")

    # Case 3: both marks on piece 4 (parallel: 4->a+b, 4->c+d? No, only one piece 4)
    # Case 4: one mark on piece 4, one on piece 4's fragment
    # Already covered by cascade.

    # Case 5: 1 mark only (single split)
    for q in [F(1), F(2)]:
        cfg = sorted([F(4)-q, q, F(2), F(1)], reverse=True)
        D = alt_sum(cfg)
        count += 1
        if min_D is None or D < min_D:
            min_D = D
        if D < 1:
            neg_count += 1
            print(f"  D<1! cfg={cfg} D={D}")

    # Case 6: 0 marks
    D = alt_sum(T)
    count += 1
    if min_D is None or D < min_D:
        min_D = D

    print(f"  T_2: {count} breakpoint configs checked, min D = {min_D}, D<1 count = {neg_count}")
    return min_D, neg_count

check_all_breakpoints_T2()

# T_3 = (8,4,2,1). Check all breakpoints with <= 3 marks.
# This is a big enumeration. Let's use the grid approach from round-5 scripts
# but check ALL D values (not just D=1).

def check_all_breakpoints_T3():
    """T_3 = (8,4,2,1). 3 marks. Check all breakpoints."""
    D_n = 15
    min_D = None
    count = 0
    neg_count = 0
    d_values = set()

    # We enumerate breakpoints by checking configs where fragments tie tower pieces.
    # Use the cascade, split-larger, split-tower types from round-5 scripts.
    N = 4  # grid resolution

    # Type 1: cascade 8 -> (8-q1)+q1 -> (q1-q2)+q2 -> (q2-q3)+q3
    # Breakpoints: q1 in {1,2,4}, q2 in {1,2}, q3 in {1}
    # (q_i ties a tower piece or another fragment)
    for q1 in [F(k, N) for k in range(1, 4*N+1)]:
        if q1 <= 0 or q1 > 4:
            continue
        for q2 in [F(k, N) for k in range(1, int(2*q1*N)+1)]:
            if q2 <= 0 or q2 > q1/2:
                continue
            for q3 in [F(k, N) for k in range(1, int(2*q2*N)+1)]:
                if q3 <= 0 or q3 > q2/2:
                    continue
                frags = [F(8)-q1, q1-q2, q2-q3, q3]
                towers = [F(4), F(2), F(1)]
                cfg = sorted(frags + towers, reverse=True)
                D = alt_sum(cfg)
                count += 1
                d_values.add(D)
                if min_D is None or D < min_D:
                    min_D = D
                if D < 1:
                    neg_count += 1
                    if neg_count <= 5:
                        print(f"  D<1! cascade q1={q1} q2={q2} q3={q3} cfg={cfg} D={D}")

    # Type 2: split-larger 8 -> (8-q1)+q1, (8-q1) -> (8-q1-q2)+q2
    for q1 in [F(k, N) for k in range(1, 4*N+1)]:
        if q1 <= 0 or q1 > 4:
            continue
        for q2 in [F(k, N) for k in range(1, int((8-q1)*N/2)+1)]:
            if q2 <= 0 or q2 > (8-q1)/2:
                continue
            frags = [F(8)-q1-q2, q2, q1]
            towers = [F(4), F(2), F(1)]
            cfg = sorted(frags + towers, reverse=True)
            D = alt_sum(cfg)
            count += 1
            d_values.add(D)
            if min_D is None or D < min_D:
                min_D = D
            if D < 1:
                neg_count += 1
                if neg_count <= 5:
                    print(f"  D<1! split-larger q1={q1} q2={q2} cfg={cfg} D={D}")

    # Type 3: split-tower 8->(8-q1)+q1, 4->(4-q2)+q2
    for q1 in [F(k, N) for k in range(1, 4*N+1)]:
        if q1 <= 0 or q1 > 4:
            continue
        for q2 in [F(k, N) for k in range(1, 2*N+1)]:
            if q2 <= 0 or q2 > 2:
                continue
            frags_top = [F(8)-q1, q1]
            frags_t4 = [F(4)-q2, q2]
            towers = [F(2), F(1)]
            cfg = sorted(frags_top + frags_t4 + towers, reverse=True)
            D = alt_sum(cfg)
            count += 1
            d_values.add(D)
            if min_D is None or D < min_D:
                min_D = D
            if D < 1:
                neg_count += 1
                if neg_count <= 5:
                    print(f"  D<1! split-tower q1={q1} q2={q2} cfg={cfg} D={D}")

    # Type 4: 3 splits on tower pieces only (no top split)
    # 8->(8-q1)+q1, 4->(4-q2)+q2, 2->(2-q3)+q3
    for q1 in [F(k, N) for k in range(1, 4*N+1)]:
        if q1 <= 0 or q1 > 4: continue
        for q2 in [F(k, N) for k in range(1, 2*N+1)]:
            if q2 <= 0 or q2 > 2: continue
            for q3 in [F(k, N) for k in range(1, N+1)]:
                if q3 <= 0 or q3 > 1: continue
                frags = [F(8)-q1, q1, F(4)-q2, q2, F(2)-q3, q3, F(1)]
                cfg = sorted(frags, reverse=True)
                D = alt_sum(cfg)
                count += 1
                d_values.add(D)
                if min_D is None or D < min_D:
                    min_D = D
                if D < 1:
                    neg_count += 1
                    if neg_count <= 5:
                        print(f"  D<1! split-all-tower q1={q1} q2={q2} q3={q3} cfg={cfg} D={D}")

    print(f"  T_3: {count} configs checked (grid 1/{N}), min D = {min_D}, D<1 count = {neg_count}")
    print(f"  Distinct D values (sorted): {sorted(d_values)[:20]}{'...' if len(d_values)>20 else ''}")
    return min_D, neg_count

check_all_breakpoints_T3()
