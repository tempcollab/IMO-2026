"""Investigate the D=0 dyadic vertex and any D<1 vertex."""
from fractions import Fraction as F
from collections import Counter, defaultdict
from itertools import product
import sys
sys.path.insert(0, '/tmp/round-7')
from vertex_sign_diagnostic import (enum_cascade_vertices, enum_split_tower_vertices,
                                     analyze_vertex, spine_with_origins, alt_sum, is_pow2)

all_verts = []
all_verts += enum_cascade_vertices(3, 4)
all_verts += enum_cascade_vertices(3, 3)
all_verts += enum_cascade_vertices(3, 2)
all_verts += enum_split_tower_vertices(3, 2)
all_verts += enum_split_tower_vertices(3, 1)
all_verts += enum_cascade_vertices(4, 4)
all_verts += enum_cascade_vertices(4, 3)
all_verts += enum_cascade_vertices(4, 5)
all_verts += enum_split_tower_vertices(4, 3)
all_verts += enum_split_tower_vertices(4, 2)
all_verts += enum_split_tower_vertices(4, 1)

seen = set()
uniq = []
for v in all_verts:
    key = (tuple(v['frags']), tuple(v['towers']))
    if key in seen: continue
    seen.add(key)
    uniq.append(v)

print("Vertices with D <= 1 (all):")
for v in sorted(uniq, key=lambda v: v['D']):
    if v['D'] <= 1:
        sp_str = [(str(val), o, ('+' if i%2==0 else '-')) for i,(val,o) in enumerate(v['spine'])]
        print(f"  D={v['D']} frags={v['frags']} towers={v['towers']} "
              f"F={v['F_mass']} T={v['T_mass']} block={v['block']} pattern={v['pattern']} "
              f"label={v['label']} spine={sp_str}")
        # reconstruct full config and recompute D directly
        full = list(v['frags']) + list(v['towers'])
        Ddirect = alt_sum(full)
        print(f"    full={sorted(full,reverse=True)} D_direct={Ddirect}")
