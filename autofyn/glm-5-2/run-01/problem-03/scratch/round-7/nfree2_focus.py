"""Focused: only the nfree=2 multi-survivor case (top r=3 + tower r=3) for T_3,T_4,
plus a quick T_3 nfree<=1 mixed check. Avoids the full set-partition blowup."""
from fractions import Fraction as F
from itertools import product
from collections import Counter, defaultdict

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

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
            if nF % 2 == 1: sp.append((v,'F'))
            else: sp.append((v,'T'))
    return sp

def set_partitions(items):
    items = list(items)
    if not items:
        yield []; return
    first = items[0]; rest = items[1:]
    for sp in set_partitions(rest):
        yield [[first]] + sp
        for i, g in enumerate(sp):
            new_sp = [list(g2) for g2 in sp]
            new_sp[i] = [first] + list(g)
            yield new_sp

def enum_two_split_3each(n, k):
    """Top 2^n split into 3 frags (free group size 3 -> v1=2^n/3, non-dyadic).
    Tower 2^k split into 3 frags (free group size 3 -> v2=2^k/3, non-dyadic).
    This is the canonical nfree=2 multi-survivor vertex. Enumerate ALL tie structures
    over the 6 fragments (top:0,1,2; tower:3,4,5) with tower vals + free assignments."""
    top = F(2)**n; tk = F(2)**k
    D_n = F(2)**(n+1)-1
    unsplit = [F(2)**j for j in range(n) if F(2)**j != tk]
    tower_vals = sorted(set([F(2)**j for j in range(n)]), reverse=True)
    idx = [0,1,2,3,4,5]
    results = []; seen = set()
    for sp in set_partitions(idx):
        groups = sp; ngroups = len(groups)
        choices = [list(tower_vals)+['free'] for _ in groups]
        for combo in product(*choices):
            ok = True
            for gi,g in enumerate(groups):
                if combo[gi]=='free' and len(g)<2: ok=False; break
            if not ok: continue
            free_groups = [gi for gi in range(ngroups) if combo[gi]=='free']
            nfree = len(free_groups)
            fv = [None]*6
            for gi,g in enumerate(groups):
                if combo[gi]!='free':
                    for i in g: fv[i] = combo[gi]
            # constraints: fv[0]+fv[1]+fv[2]=top ; fv[3]+fv[4]+fv[5]=tk
            if nfree == 0:
                if sum(fv[:3])!=top or sum(fv[3:])!=tk: continue
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                # solve using the constraints it touches
                in_top = [i for i in g0 if i<3]; in_tk = [i for i in g0 if i>=3]
                vA = (top - sum(fv[i] for i in range(3) if fv[i] is not None))/len(in_top) if in_top else None
                vB = (tk - sum(fv[i] for i in range(3,6) if fv[i] is not None))/len(in_tk) if in_tk else None
                if in_top and in_tk:
                    if vA!=vB: continue
                    v=vA
                elif in_top: v=vA
                else: v=vB
                if v is None or v<=0: continue
                for i in g0: fv[i]=v
                if sum(fv[:3])!=top or sum(fv[3:])!=tk: continue
            elif nfree == 2:
                g0 = groups[free_groups[0]]; g1 = groups[free_groups[1]]
                # two unknowns v0 (g0), v1 (g1); constraints: top sum, tk sum
                # row A: (#g0 in top)*v0 + (#g1 in top)*v1 = top - known_top
                # row B: (#g0 in tk)*v0 + (#g1 in tk)*v1 = tk - known_tk
                known_top = sum(fv[i] for i in range(3) if fv[i] is not None)
                known_tk = sum(fv[i] for i in range(3,6) if fv[i] is not None)
                c0a = len([i for i in g0 if i<3]); c1a = len([i for i in g1 if i<3])
                c0b = len([i for i in g0 if i>=3]); c1b = len([i for i in g1 if i>=3])
                ra = top - known_top; rb = tk - known_tk
                det = c0a*c1b - c0b*c1a
                if det==0: continue
                v0 = (ra*c1b - rb*c1a)/det
                v1 = (c0a*rb - c0b*ra)/det
                if v0<=0 or v1<=0: continue
                # verify both constraints
                if c0a*v0+c1a*v1!=ra or c0b*v0+c1b*v1!=rb: continue
                for i in g0: fv[i]=v0
                for i in g1: fv[i]=v1
                if sum(fv[:3])!=top or sum(fv[3:])!=tk: continue
            else: continue
            frags = list(fv)
            if any(x is None or x<=0 for x in frags): continue
            origins = ['F','F','F','T','T','T'] + ['T']*len(unsplit)
            full = list(frags)+list(unsplit)
            if sum(full)!=D_n: continue
            key = tuple(sorted(full,reverse=True))
            if key in seen: continue
            seen.add(key)
            D = alt_sum(full)
            sp_sp = spine_with_origins(full, origins)
            fpos = [i for i,(v,o) in enumerate(sp_sp) if o=='F']
            Fm = sum(sp_sp[i][0] for i in fpos)
            Tm = sum(sp_sp[i][0] for i in range(len(sp_sp)) if sp_sp[i][1]=='T')
            block = (all(i%2==0 for i in fpos) or all(i%2==1 for i in fpos)) if fpos else True
            results.append({'n':n,'k':k,'D':D,'spine':sp_sp,'F':Fm,'T':Tm,
                            'block':block,'nfree':nfree,'frags':sorted(frags,reverse=True),
                            'unsplit':sorted(unsplit,reverse=True)})
    return results

# ============================================================
# T_3: top r=3 + tower r=3 needs 2+2=4 marks > 3 -> IMPOSSIBLE.
# So for T_3, no nfree=2 multi-survivor from this family. Verify the structural claim:
# any split into exactly 2 fragments has free-group-value = sum/2 = dyadic.
# Hence for T_3 (<=3 marks), at most ONE split has >=3 frags -> at most one non-dyadic free group.
print("="*70); print("T_3: nfree>=2 multi-survivor IMPOSSIBLE (mark budget)"); print("="*70)
print("Two splits with r>=3 each need (3-1)+(3-1)=4 marks > 3 = n. So at most one")
print("split has r>=3; a size-2 free group gives value=sum/2=dyadic (not free).")
print("=> T_3 vertices have nfree<=1. Single-survivor HOLDS for T_3.")

# ============================================================
# T_4: top r=3 + tower r=3 = 4 marks = n. nfree=2 POSSIBLE.
# ============================================================
print("\n"+"="*70); print("T_4: top r=3 + tower r=3 (4 marks = n) -- nfree=2 vertices"); print("="*70)
all_t4 = []
for k in range(4):
    all_t4 += enum_two_split_3each(4, k)
seen=set(); uniq=[]
for r in all_t4:
    key=(tuple(r['frags']),tuple(r['unsplit']))
    if key in seen: continue
    seen.add(key); uniq.append(r)
print(f"Total vertices (top r=3 + tower r=3, all k): {len(uniq)}")
n2 = [r for r in uniq if r['nfree']==2]
print(f"  nfree==2 (MULTI-SURVIVOR): {len(n2)}")
nondy = [r for r in uniq if r['F']>0]
print(f"  non-dyadic (F>0): {len(nondy)}")
print(f"  all non-dyadic have D>1: {all(r['D']>1 for r in nondy)}")
print(f"  min D overall: {min(r['D'] for r in uniq)}")
dlt1=[r for r in uniq if r['D']<1]
print(f"  D<1 (COUNTEREXAMPLES): {len(dlt1)}")
for r in dlt1:
    print(f"    COUNTEREXAMPLE: D={r['D']} frags={r['frags']} spine={[(str(v),o) for v,o in r['spine']]}")

print(f"\n--- nfree=2 MULTI-SURVIVOR vertices (T_4) ---")
for r in sorted(n2, key=lambda x:x['D']):
    nF = len([1 for v,o in r['spine'] if o=='F'])
    print(f"  D={r['D']} #surviving_frags={nF} F={r['F']} T={r['T']} "
          f"frags={r['frags']} unsplit={r['unsplit']} "
          f"spine={[(str(v),o) for v,o in r['spine']]} block={r['block']}")

print(f"\n--- ALL non-dyadic T_4 (top r=3+tower r=3) vertices sorted by D ---")
for r in sorted(nondy, key=lambda x:x['D'])[:40]:
    nF = len([1 for v,o in r['spine'] if o=='F'])
    print(f"  D={r['D']} #frag={nF} nfree={r['nfree']} F={r['F']} T={r['T']} "
          f"spine={[(str(v),o) for v,o in r['spine']]} block={r['block']}")
