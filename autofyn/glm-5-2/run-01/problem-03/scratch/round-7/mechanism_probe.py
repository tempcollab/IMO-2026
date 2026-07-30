"""Probe the STRUCTURAL MECHANISM: at non-dyadic strong-breakpoint vertices,
WHY is D > 1? Test the conjectured mechanism:
  - surviving non-dyadic fragment value v satisfies 1 < v < 2^{n-1}
    (constrained by count>=3 and mass budget, so v is NOT the smallest spine piece
     and is below the largest tower)
  - the sort order places v BETWEEN towers, forcing it to a specific sign position
  - the dyadic dominance of the bracketing towers forces D > 1

Also test: is the block condition on the spine ALWAYS holding at non-dyadic vertices?
And: a direct parity/position-counting argument on the spine.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
from itertools import product
import sys
sys.path.insert(0,'/tmp/round-7')
from vertex_sign_clean import (enum_cascade, enum_split_tower, enum_split_two_tower,
                               spine_with_origins, alt_sum, is_pow2, analyze)

all_verts = []
all_verts += enum_cascade(3,4)+enum_cascade(3,3)+enum_cascade(3,2)
all_verts += enum_split_tower(3,2)+enum_split_tower(3,1)
all_verts += enum_split_two_tower(3,2,1)
all_verts += enum_cascade(4,4)+enum_cascade(4,3)+enum_cascade(4,5)+enum_cascade(4,2)
all_verts += enum_split_tower(4,3)+enum_split_tower(4,2)+enum_split_tower(4,1)
all_verts += enum_split_two_tower(4,3,2)+enum_split_two_tower(4,3,1)+enum_split_two_tower(4,2,1)

seen=set(); uniq=[]
for v in all_verts:
    key=(tuple(v['frags']),tuple(v['towers']))
    if key in seen: continue
    seen.add(key); uniq.append(v)

nondy = [v for v in uniq if v['F_mass'] > 0]
print(f"Non-dyadic vertices: {len(nondy)}")
print(f"All have block on spine = TRUE: {all(v['block'] for v in nondy)}")
print(f"All have D > 1: {all(v['D'] > 1 for v in nondy)}")
print(f"Min D at non-dyadic: {min(v['D'] for v in nondy)}")

# MECHANISM CHECK 1: surviving non-dyadic fragment value v.
# At a breakpoint, a surviving non-dyadic fragment appears odd count >= 3.
# Check: is every surviving non-dyadic fragment value v in (1, 2^{n-1})?
print(f"\n--- Surviving non-dyadic fragment values ---")
for v in sorted(nondy, key=lambda v: v['D']):
    n = int(v['label'].split('n=')[1].split()[0])
    top = F(2)**n
    largest_tow = F(2)**(n-1)
    # extract surviving F-values from spine
    f_vals = [val for val,o in v['spine'] if o=='F']
    for fv in f_vals:
        in_range = (F(1) < fv < largest_tow) or (fv == largest_tow) or (fv < F(1))
        print(f"  n={n} D={v['D']} frag_val={fv} in(1,2^(n-1))={F(1)<fv<largest_tow} "
              f"spine={[(str(x),o) for x,o in v['spine']]}")

# MECHANISM CHECK 2: position of surviving fragments in spine.
# Is every surviving F at a MINUS position (odd 0-based) at non-dyadic vertices
# where pattern fails? And does the sort order force this?
print(f"\n--- Position of surviving F in spine (non-dyadic vertices) ---")
for v in sorted(nondy, key=lambda v: v['D']):
    f_pos_in_spine = [i for i,(val,o) in enumerate(v['spine']) if o=='F']
    signs = ['+' if i%2==0 else '-' for i in f_pos_in_spine]
    print(f"  D={v['D']} F_pos={f_pos_in_spine} signs={signs} "
          f"spine={[(str(x),o,'+' if i%2==0 else '-') for i,(x,o) in enumerate(v['spine'])]}")

# MECHANISM CHECK 3: the mass-budget tightness vs D.
# At budget=0 (T = 3F-1), what is D? Is there a clean lower bound D >= F+... ?
print(f"\n--- Mass-budget tightness vs D ---")
for v in sorted(nondy, key=lambda v: v['D']):
    print(f"  D={v['D']} F={v['F_mass']} T={v['T_mass']} budget(T-3F+1)={v['budget']} "
          f"F-T={v['F_mass']-v['T_mass']} 2(t+-f-)={2*(v['t_plus']-v['f_minus'])} "
          f"decomp_check={(v['F_mass']-v['T_mass'])+2*(v['t_plus']-v['f_minus'])==v['D']}")

# MECHANISM CHECK 4: the KEY candidate — at a non-dyadic vertex, the spine is
# TOWER, FRAG, TOWER, ... interleaved (frag at -), and D = (sum towers at +) - frag + ...
# The towers at + are LARGER than the frag (sort order). By dyadic dominance,
# the largest tower at + exceeds the frag + all smaller towers. So D > 1?
print(f"\n--- Candidate: largest tower at + vs fragment + smaller towers ---")
for v in sorted(nondy, key=lambda v: v['D'])[:12]:
    sp = v['spine']
    # towers at + positions
    tp = [sp[i][0] for i in range(0,len(sp),2) if sp[i][1]=='T']
    # fragments (all, at whatever position)
    fv = [sp[i][0] for i in range(len(sp)) if sp[i][1]=='F']
    # towers at - positions
    tm = [sp[i][0] for i in range(1,len(sp),2) if sp[i][1]=='T']
    largest_tp = max(tp) if tp else F(0)
    frag_plus_smaller_tow = sum(fv) + sum(tm)
    print(f"  D={v['D']} largest_tower_at_+={largest_tp} "
          f"frag+smaller_towers_at_-={frag_plus_smaller_tow} "
          f"dominance={largest_tp > frag_plus_smaller_tow} "
          f"spine={[(str(x),o) for x,o in sp]}")
