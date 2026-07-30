from fractions import Fraction as F
from collections import Counter, defaultdict

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def spine_with_origins(pieces, origins):
    val_origins = defaultdict(list)
    for v, o in zip(pieces, origins):
        val_origins[v].append(o)
    sp = []
    for v in sorted(val_origins.keys(), reverse=True):
        cnt = len(val_origins[v])
        if cnt % 2 == 1:
            origins_list = val_origins[v]
            nF = origins_list.count('F')
            sp.append((v, 'F' if nF % 2 == 1 else 'T'))
    return sp

# Directly construct breakpoints by solving tie equations.
# T_3 cascade: frags = [8-q1, q1-q2, q2-q3, q3], towers = [4,2,1]
# At a breakpoint, every fragment value appears >= 2 in the full config.
# Enumerate all possible tie patterns: each fragment either equals a tower piece
# or equals another fragment.

# For each fragment, it can tie: tower 4, tower 2, tower 1, or another fragment.
# Generate all assignments and solve.

import itertools

def check_breakpoint_config(frags, towers, label):
    all_p = list(frags) + list(towers)
    counts = Counter(all_p)
    is_bp = all(counts[v] >= 2 for v in frags)
    if not is_bp:
        return None
    D = alt_sum(all_p)
    origins = ['F']*len(frags) + ['T']*len(towers)
    sp = spine_with_origins(all_p, origins)
    Fm = sum(v for v,o in sp if o=='F')
    Tm = sum(v for v,o in sp if o=='T')
    return (D, Fm, Tm, sp, all_p)

# T_3 cascade: frags = [8-q1, q1-q2, q2-q3, q3]
# Each frag ties something. Options: tie tower (4,2,1) or tie another frag.
# We enumerate all possible tie structures.

# Approach: each fragment value must appear >= 2 times.
# The fragments are f0=8-q1, f1=q1-q2, f2=q2-q3, f3=q3.
# f0+f1+f2+f3 = 8. Each fi > 0.
# The full config is {f0,f1,f2,f3,4,2,1}.
# Each fi must have count >= 2 in this multiset.

# A fragment fi can tie:
# - Tower 4 (fi=4), Tower 2 (fi=2), Tower 1 (fi=1)
# - Another fragment fj (fi=fj)

# Enumerate all possible "tie types" for (f0,f1,f2,f3):
# Each fi is either = a tower piece (4,2,1) or = another fj.
# This gives a system of equations.

print("T_3 cascade: directly constructed breakpoints")
print("="*70)

# Case 1: all frags are dyadic (tie tower pieces)
# f0=4,f1=2,f2=1,f3=1: 4+2+1+1=8 ✓. Config {4,4,2,2,1,1,1}. 
r = check_breakpoint_config([F(4),F(2),F(1),F(1)], [F(4),F(2),F(1)], "dyadic")
if r: print(f"  Dyadic: D={r[0]} F={r[1]} T={r[2]} spine={[(str(v),o) for v,o in r[3]]}")

# Case 2: one non-dyadic value appears 3 times among frags, one frag is dyadic
# frags = {w,w,w,v} where v is dyadic, 3w+v=8
for v_label, v_val in [("1",F(1)),("2",F(2)),("4",F(4))]:
    w = (F(8) - v_val) / 3
    if w <= 0 or w == v_val: continue
    frags = [w, w, w, v_val]
    r = check_breakpoint_config(frags, [F(4),F(2),F(1)], f"w3+{v_label}")
    if r:
        # Check mass budget
        print(f"  3x{w}+{v_val}: D={r[0]} F={r[1]} T={r[2]} 3F-1={3*r[1]-1} T>=3F-1? {r[2]>=3*r[1]-1} "
              f"spine={[(str(v),o) for v,o in r[3]]}")

# Case 3: two pairs of equal non-dyadic frags: {w,w,u,u}, 2w+2u=8, w!=u, both non-dyadic
# w+u=4. Enumerate w values.
print("  Two pairs {w,w,u,u}, w+u=4:")
for wn in range(1, 32):
    w = F(wn, 8)
    u = F(4) - w
    if w <= 0 or u <= 0 or w == u: continue
    # Check non-dyadic (not power of 2)
    frags = [w, w, u, u]
    r = check_breakpoint_config(frags, [F(4),F(2),F(1)], f"pairs({w},{u})")
    if r:
        print(f"    w={w} u={u}: D={r[0]} F={r[1]} T={r[2]} 3F-1={3*r[1]-1} T>=3F-1? {r[2]>=3*r[1]-1} "
              f"spine={[(str(v),o) for v,o in r[3]]}")

# Case 4: one pair {w,w} and two dyadic frags
print("  One pair {w,w} + two dyadic, 2w+v1+v2=8:")
for v1_label, v1 in [("1",F(1)),("2",F(2)),("4",F(4))]:
    for v2_label, v2 in [("1",F(1)),("2",F(2)),("4",F(4))]:
        w = (F(8) - v1 - v2) / 2
        if w <= 0 or w == v1 or w == v2: continue
        if v1 > v2: continue  # avoid duplicates
        frags = [w, w, v1, v2]
        r = check_breakpoint_config(frags, [F(4),F(2),F(1)], f"pair({w})+{v1_label}+{v2_label}")
        if r:
            print(f"    w={w} v1={v1} v2={v2}: D={r[0]} F={r[1]} T={r[2]} 3F-1={3*r[1]-1} "
                  f"T>=3F-1? {r[2]>=3*r[1]-1} spine={[(str(v),o) for v,o in r[3]]}")

# Case 5: all 4 frags equal (w,w,w,w), 4w=8, w=2 (dyadic). Skip.

# Case 6: 3 copies of w + 1 frag that ties another frag
# frags = {w,w,w,u} where u ties something. u must appear >= 2.
# u must tie a tower piece or another frag. Since w appears 3 times and u once,
# u must tie a tower piece (u = 4, 2, or 1).
# Already covered in Case 2.

print("\n" + "="*70)
print("T_4 cascade: directly constructed breakpoints")
print("="*70)
# T_4: frags = [16-q1, q1-q2, q2-q3, q3-q4, q4] (5 frags), towers = [8,4,2,1]
# 5 frags sum to 16.

# Dyadic: all frags are powers of 2 tying towers
r = check_breakpoint_config([F(8),F(4),F(2),F(1),F(1)], [F(8),F(4),F(2),F(1)], "dyadic")
if r: print(f"  Dyadic: D={r[0]} F={r[1]} T={r[2]} spine={[(str(v),o) for v,o in r[3]]}")

# 3 copies of w + 2 dyadic: 3w + v1 + v2 = 16
for v1 in [F(1),F(2),F(4),F(8)]:
    for v2 in [F(1),F(2),F(4),F(8)]:
        if v1 > v2: continue
        w = (F(16) - v1 - v2) / 3
        if w <= 0 or w == v1 or w == v2: continue
        frags = [w,w,w,v1,v2]
        r = check_breakpoint_config(frags, [F(8),F(4),F(2),F(1)], f"3x{w}+{v1}+{v2}")
        if r:
            print(f"  3x{w}+{v1}+{v2}: D={r[0]} F={r[1]} T={r[2]} 3F-1={3*r[1]-1} "
                  f"T>=3F-1? {r[2]>=3*r[1]-1} spine={[(str(v),o) for v,o in r[3]]}")

# 2 pairs: {w,w,u,u}, 2w+2u=16, w+u=8
print("  Two pairs {w,w,u,u}, w+u=8:")
for wn in range(1, 64):
    w = F(wn, 8)
    u = F(8) - w
    if w <= 0 or u <= 0 or w == u: continue
    frags = [w, w, u, u, F(0)]  # need 5 frags! Not 4. Skip if 5th needed.
    # Actually 5 frags: 2w+2u+v3 = 16. Need v3 too.
    # This is getting complex. Skip for now.
    pass

# 1 pair {w,w} + 3 dyadic: 2w+v1+v2+v3=16
print("  One pair {w,w} + 3 dyadic:")
from itertools import combinations_with_replacement
for v1,v2,v3 in combinations_with_replacement([F(1),F(2),F(4),F(8)], 3):
    w = (F(16) - v1 - v2 - v3) / 2
    if w <= 0 or w in [v1,v2,v3]: continue
    frags = [w,w,v1,v2,v3]
    r = check_breakpoint_config(frags, [F(8),F(4),F(2),F(1)], f"pair({w})+{v1}+{v2}+{v3}")
    if r:
        print(f"    w={w} v=({v1},{v2},{v3}): D={r[0]} F={r[1]} T={r[2]} 3F-1={3*r[1]-1} "
              f"T>=3F-1? {r[2]>=3*r[1]-1}")

print("\n" + "="*70)
print("SUMMARY: At ALL constructed breakpoints, check D>=1 and T>=3F-1")
print("="*70)
