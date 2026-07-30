"""
Round 7: Extend enumeration to NFREE>=2 VERTICES (mixed types) for T_3 and T_4.
The existing vertex_sign_clean.py / breakpoint_exact_enum.py SKIP nfree>=2 (treat as faces).
But for split types with >=2 independent sum constraints, nfree=2 can give a genuine VERTEX
(2 unknowns, 2 equations -> 0 free params). This addresses reviewer caveat (b): verify (★)
on the FULL vertex type set, including mixed/multi-survivor vertices.

Mixed type: top 2^n split into r1 fragments (r1-1 marks) + tower 2^k split into r2 fragments
(r2-1 marks), with r1-1 + r2-1 <= n. Free groups within each split's fragments, each non-dyadic,
determined by the split's sum constraint. If BOTH splits have a non-dyadic free group (size>=3,
since size-2 free -> value = sum/2 = dyadic), we get nfree=2 with TWO surviving fragments.

We enumerate ALL such mixed vertices for T_3 (n=3, <=3 marks) and T_4 (n=4, <=4 marks),
compute D exactly (Fraction), check (★): D>1 at non-dyadic vertices, D>=1 overall.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter, defaultdict

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def is_pow2(x):
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            n = int(x); return n > 0 and (n & (n-1)) == 0
        num, den = x.numerator, x.denominator
        return (num & (num-1)) == 0 and (den & (den-1)) == 0
    return False

def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first = items[0]
    rest = items[1:]
    for sp in set_partitions(rest):
        yield [[first]] + sp
        for i, g in enumerate(sp):
            new_sp = [list(g2) for g2 in sp]
            new_sp[i] = [first] + list(g)
            yield new_sp

def spine_with_origins(pieces, origins):
    val_count = Counter(pieces)
    val_origins = defaultdict(list)
    for v, o in zip(pieces, origins):
        val_origins[v].append(o)
    sp = []
    for v in sorted(val_count.keys(), reverse=True):
        cnt = val_count[v]
        if cnt % 2 == 1:
            olist = val_origins[v]
            nF = olist.count('F')
            if nF % 2 == 1:
                sp.append((v, 'F'))
            else:
                sp.append((v, 'T'))
    return sp

def analyze_mixed(n, splits):
    """splits = list of (piece_value, r, origin_label) where piece_value is the sum
    (2^n for top, 2^k for tower), r = number of fragments, origin = 'F' (top) or 'T' (tower).
    Unsplit towers = all 2^j for j in 0..n-1 not in the split tower set.
    Enumerate tie structures across ALL fragments jointly (a fragment from the top CAN tie
    a fragment from a tower split if they share the same value)."""
    top = F(2)**n
    D_n = F(2)**(n+1) - 1
    # collect all fragments and their sum constraints
    # each split contributes r fragments; fragment indices global; each split has a sum constraint
    frag_idx = []
    constraints = []  # (list_of_indices, target_sum)
    origin_labels = []
    cur = 0
    for (pval, r, olab) in splits:
        idx = list(range(cur, cur+r))
        frag_idx.extend(idx)
        constraints.append((idx, pval))
        origin_labels.extend([olab]*r)
        cur += r
    nfrags = cur
    # unsplit towers: 2^j for j in 0..n-1, excluding tower pieces that were split
    split_tower_vals = set(pval for (pval,r,olab) in splits if olab=='T')
    unsplit = [F(2)**j for j in range(n) if F(2)**j not in split_tower_vals]
    tower_vals = sorted(set([F(2)**j for j in range(n)]), reverse=True)

    results = []
    idx_all = list(range(nfrags))
    seen = set()
    for sp in set_partitions(idx_all):
        groups = sp
        ngroups = len(groups)
        choices = [list(tower_vals) + ['free'] for _ in groups]
        for combo in product(*choices):
            # free group must have size >= 2
            ok = True
            for gi, g in enumerate(groups):
                if combo[gi] == 'free' and len(g) < 2:
                    ok = False; break
            if not ok: continue
            free_groups = [gi for gi in range(ngroups) if combo[gi]=='free']
            nfree = len(free_groups)
            if nfree == 0:
                # all assigned tower values; check each split sum constraint
                fv = [None]*nfrags
                for gi,g in enumerate(groups):
                    if combo[gi] != 'free':
                        for i in g: fv[i] = combo[gi]
                ok2 = True
                for (idxs, tgt) in constraints:
                    if sum(fv[i] for i in idxs) != tgt:
                        ok2 = False; break
                if not ok2: continue
                frags = [fv[i] for i in range(nfrags)]
            elif nfree == 1:
                fv = [None]*nfrags
                for gi,g in enumerate(groups):
                    if combo[gi] != 'free':
                        for i in g: fv[i] = combo[gi]
                g0 = groups[free_groups[0]]
                # the free group may span multiple sum constraints; each constraint it touches
                # must determine the SAME v
                v_candidates = []
                for (idxs, tgt) in constraints:
                    free_in = [i for i in g0 if i in idxs]
                    if free_in:
                        known = sum(fv[i] for i in idxs if fv[i] is not None)
                        v_candidates.append((tgt - known, len(free_in)))
                # all (tgt-known)/len(free_in) must be equal
                vs = set()
                for (rem, sz) in v_candidates:
                    if rem <= 0: vs.add(None)
                    else: vs.add(F(rem)/sz)
                if len(vs) != 1: continue
                v = next(iter(vs))
                if v is None or v <= 0: continue
                for i in g0: fv[i] = v
                frags = [fv[i] for i in range(nfrags)]
            elif nfree == 2:
                # TWO free groups. For a VERTEX, each free group's value must be determined
                # by the sum constraints. A free group may span multiple constraints; the
                # system is: for each constraint, sum of (free frags in it)*their_v + known = tgt.
                # With 2 unknowns v1, v2 and >=2 independent constraints, we solve.
                fv = [None]*nfrags
                for gi,g in enumerate(groups):
                    if combo[gi] != 'free':
                        for i in g: fv[i] = combo[gi]
                g0 = groups[free_groups[0]]
                g1 = groups[free_groups[1]]
                # Build linear system: for each constraint, sum of free-in-constraint v's + known = tgt
                # unknowns: v0 (for g0), v1 (for g1)
                rows = []
                for (idxs, tgt) in constraints:
                    c0 = len([i for i in g0 if i in idxs])
                    c1 = len([i for i in g1 if i in idxs])
                    known = sum(fv[i] for i in idxs if fv[i] is not None)
                    rows.append((c0, c1, F(tgt) - known))
                # Solve the 2x2 system (pick two independent rows)
                solved = False
                v0 = v1 = None
                for a in range(len(rows)):
                    for b in range(a+1, len(rows)):
                        (c0a,c1a,ra),(c0b,c1b,rb) = rows[a], rows[b]
                        det = c0a*c1b - c0b*c1a
                        if det == 0: continue
                        v0 = (ra*c1b - rb*c1a)/det
                        v1 = (c0a*rb - c0b*ra)/det
                        # check consistency with ALL rows
                        ok3 = True
                        for (c0,c1,r) in rows:
                            if c0*v0 + c1*v1 != r:
                                ok3 = False; break
                        if ok3 and v0 > 0 and v1 > 0:
                            solved = True; break
                    if solved: break
                if not solved: continue
                for i in g0: fv[i] = v0
                for i in g1: fv[i] = v1
                frags = [fv[i] for i in range(nfrags)]
            else:
                continue  # nfree>=3: face, skip (D=1 points on sub-faces)
            if any(f is None or f <= 0 for f in frags): continue
            # origins: top split frags = 'F', tower split frags = 'T', unsplit = 'T'
            origins = list(origin_labels) + ['T']*len(unsplit)
            full = list(frags) + list(unsplit)
            if sum(full) != D_n: continue
            key = tuple(sorted(full, reverse=True))
            if key in seen: continue
            seen.add(key)
            D = alt_sum(full)
            sp_spine = spine_with_origins(full, origins)
            fpos = [i for i,(v,o) in enumerate(sp_spine) if o=='F']
            F_mass = sum(sp_spine[i][0] for i in fpos)
            T_mass = sum(sp_spine[i][0] for i in range(len(sp_spine)) if sp_spine[i][1]=='T')
            block = (all(i%2==0 for i in fpos) or all(i%2==1 for i in fpos)) if fpos else True
            results.append({
                'n':n,'splits':splits,'frags':sorted(frags,reverse=True),
                'unsplit':sorted(unsplit,reverse=True),'D':D,'spine':sp_spine,
                'F_mass':F_mass,'T_mass':T_mass,'block':block,'nfree':nfree,
                'fv':[(str(x), 'F' if origin_labels[i]=='F' else 'T') for i,x in enumerate(frags)]})
    return results

# ============================================================
# T_3 (n=3): enumerate ALL mixed types with <=3 marks
#   mark budget = 3. splits: each split uses r-1 marks.
#   Possible distributions (r1-1)+(r2-1)+... <= 3:
#     - single split r=4 (3 marks): cascade [covered, nfree<=1]
#     - single split r=3 (2 marks): [covered]
#     - single split r=2 (1 mark): [covered]
#     - two splits: r1=3(2mk)+r2=2(1mk)=3mk; r1=2+r2=2=2mk; r1=3+r2=3=4mk>3 (excluded)
#     - three splits: 2+2+2=3mk
#   For nfree>=2 (two non-dyadic free groups), need two splits each with a non-dyadic
#   free group (size>=3 -> r>=3). For T_3: r1=3+r2=3=4mk>3 -> IMPOSSIBLE.
#   So T_3 has NO nfree>=2 non-dyadic vertices. Verify this:
# ============================================================
print("="*70)
print("T_3 mixed types (n=3, <=3 marks): checking nfree>=2 possibility")
print("="*70)
t3_results = []
# two splits: top r=3 (2mk) + tower r=2 (1mk)
for k in range(3):  # tower 2^k for k=0,1,2
    t3_results += analyze_mixed(3, [(F(8),3,'F'),(F(2)**k,2,'T')])
# top r=2 + tower r=3 ... but tower r=3 (2mk) + top r=2 (1mk) = 3mk
for k in range(3):
    t3_results += analyze_mixed(3, [(F(8),2,'F'),(F(2)**k,3,'T')])
# three splits 2+2+2 (1+1+1=3mk): top + 2 towers
for k1 in range(3):
    for k2 in range(k1+1,3):
        t3_results += analyze_mixed(3, [(F(8),2,'F'),(F(2)**k1,2,'T'),(F(2)**k2,2,'T')])
# top r=2 + one tower r=2 (2mk total): covered above subset; also top r=3 + tower r=2 done

nfree2_t3 = [r for r in t3_results if r['nfree']==2]
print(f"T_3 mixed vertices found: {len(t3_results)}")
print(f"  nfree>=2 vertices: {len(nfree2_t3)}")
print(f"  (Expect 0: two splits with r>=3 each need 4 marks > 3 for T_3)")
nondy_t3 = [r for r in t3_results if r['F_mass']>0]
print(f"  non-dyadic vertices (F>0): {len(nondy_t3)}")
print(f"  all have D>1: {all(r['D']>1 for r in nondy_t3)}")
if nondy_t3:
    print(f"  min D at non-dyadic: {min(r['D'] for r in nondy_t3)}")
    for r in sorted(nondy_t3, key=lambda x:x['D'])[:10]:
        print(f"    D={r['D']} F={r['F_mass']} T={r['T_mass']} nfree={r['nfree']} "
              f"spine={[(str(v),o) for v,o in r['spine']]} block={r['block']}")

# ============================================================
# T_4 (n=4): enumerate mixed types including nfree>=2
#   <=4 marks. Two splits r=3+r=3 = 4mk: POSSIBLE -> nfree=2 vertices exist!
# ============================================================
print("\n"+"="*70)
print("T_4 mixed types (n=4, <=4 marks): INCLUDING nfree=2 multi-survivor")
print("="*70)
t4_results = []
# top r=3 (2mk) + tower r=3 (2mk) = 4mk -- THE KEY nfree=2 case
for k in range(4):  # tower 2^k, k=0,1,2,3
    t4_results += analyze_mixed(4, [(F(16),3,'F'),(F(2)**k,3,'T')])
# top r=4 (3mk) + tower r=2 (1mk) = 4mk
for k in range(4):
    t4_results += analyze_mixed(4, [(F(16),4,'F'),(F(2)**k,2,'T')])
# top r=2 + tower r=3 (1+2=3mk)
for k in range(4):
    t4_results += analyze_mixed(4, [(F(16),2,'F'),(F(2)**k,3,'T')])
# top r=3 + tower r=2 (2+1=3mk)
for k in range(4):
    t4_results += analyze_mixed(4, [(F(16),3,'F'),(F(2)**k,2,'T')])
# two splits 2+2 (1+1=2mk)
for k in range(4):
    t4_results += analyze_mixed(4, [(F(16),2,'F'),(F(2)**k,2,'T')])
# three splits: top r=2 + tower r=2 + tower r=2 (3mk)
for k1 in range(4):
    for k2 in range(k1+1,4):
        t4_results += analyze_mixed(4, [(F(16),2,'F'),(F(2)**k1,2,'T'),(F(2)**k2,2,'T')])
# four splits 2+2+2+2 (4mk): top + 3 towers
for k1 in range(4):
    for k2 in range(k1+1,4):
        for k3 in range(k2+1,4):
            t4_results += analyze_mixed(4, [(F(16),2,'F'),(F(2)**k1,2,'T'),
                                            (F(2)**k2,2,'T'),(F(2)**k3,2,'T')])
# top r=3 (2mk) + two tower splits r=2+r=2 (1+1=2mk) -> 4mk
for k1 in range(4):
    for k2 in range(4):
        if k1==k2: continue
        t4_results += analyze_mixed(4, [(F(16),3,'F'),(F(2)**k1,2,'T'),(F(2)**k2,2,'T')])

# dedupe
seen=set(); t4_uniq=[]
for r in t4_results:
    key=(tuple(r['frags']),tuple(r['unsplit']))
    if key in seen: continue
    seen.add(key); t4_uniq.append(r)
t4_results = t4_uniq

print(f"T_4 mixed vertices found: {len(t4_results)}")
nfree2_t4 = [r for r in t4_results if r['nfree']==2]
print(f"  nfree==2 vertices (MULTI-SURVIVOR): {len(nfree2_t4)}")
nondy_t4 = [r for r in t4_results if r['F_mass']>0]
print(f"  non-dyadic vertices (F>0): {len(nondy_t4)}")
print(f"  all have D>1: {all(r['D']>1 for r in nondy_t4)}")
print(f"  min D overall: {min(r['D'] for r in t4_results)}")
d_lt1 = [r for r in t4_results if r['D']<1]
print(f"  D<1 (COUNTEREXAMPLES to (★)): {len(d_lt1)}")
for r in d_lt1:
    print(f"    COUNTEREXAMPLE: D={r['D']} frags={r['frags']} spine={[(str(v),o) for v,o in r['spine']]}")

print(f"\n--- nfree=2 multi-survivor vertices (T_4) ---")
for r in sorted(nfree2_t4, key=lambda x:x['D']):
    print(f"  D={r['D']} F={r['F_mass']} T={r['T_mass']} nfree={r['nfree']} "
          f"frags={r['frags']} unsplit={r['unsplit']} "
          f"spine={[(str(v),o) for v,o in r['spine']]} block={r['block']}")

print(f"\n--- ALL non-dyadic T_4 mixed vertices (sorted by D) ---")
for r in sorted(nondy_t4, key=lambda x:x['D'])[:30]:
    print(f"  D={r['D']} F={r['F_mass']} T={r['T_mass']} nfree={r['nfree']} "
          f"spine={[(str(v),o) for v,o in r['spine']]} block={r['block']}")
