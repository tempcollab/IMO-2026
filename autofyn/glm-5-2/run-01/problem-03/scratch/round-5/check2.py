from fractions import Fraction as F

def D_of(pieces):
    s = F(0)
    for i,p in enumerate(pieces):
        if i % 2 == 0: s += p
        else: s -= p
    return s

def search(pieces_tuple, marks_left, best_so_far):
    pieces = sorted(pieces_tuple, reverse=True)
    d = D_of(pieces)
    if d < best_so_far[0]:
        best_so_far[0] = d
    if marks_left == 0 or best_so_far[0] == 0:
        return
    vals = set(pieces)
    n = len(pieces)
    for i in range(n):
        v = pieces[i]
        candidates = set()
        candidates.add(F(1,2) * v)
        for w in vals:
            if w < v:
                candidates.add(w)
                candidates.add(v - w)
        for q in candidates:
            if q <= 0 or q >= v:
                continue
            new = [q, v - q]
            rest = [pieces[j] for j in range(n) if j != i]
            merged = tuple(sorted(new + rest, reverse=True))
            search(merged, marks_left - 1, best_so_far)

# Test dominant tower-tail a1 > 2^n, and some non-tower-tail bottom-dominant
target = F(1, 31)
configs = [
    (17, 8, 4, 2, 1, "dom tower-tail a1=17"),
    (20, 8, 4, 2, 1, "dom tower-tail a1=20"),
    (24, 8, 4, 2, 1, "dom tower-tail a1=24"),
    (16, 9, 4, 2, 1, "tower perturbed (16,9,4,2,1)"),
    (16, 8, 5, 2, 1, "tower perturbed (16,8,5,2,1)"),
    (16, 8, 4, 3, 1, "tower perturbed (16,8,4,3,1)"),
    (10, 8, 4, 2, 1, "non-dom tower-tail a1=10"),
    (14, 9, 4, 2, 1, "non-tower-tail bottom-dom"),
    (7, 6, 5, 3, 1, "crux (7,6,5,3,1)"),
    (5, 5, 5, 1, "fewer pieces m=4"),
]
for a1,a2,a3,a4,a5,label in configs:
    cfg = (F(a1),F(a2),F(a3),F(a4),F(a5))
    S = sum(cfg)
    best = [F(10**9)]
    search(cfg, 4, best)
    d_star = best[0] / S
    print(f'{label}: S={S} D*={best[0]}/{S}={float(d_star):.6f} target={float(target):.6f} D*<=target:{d_star<=target} D*=0:{d_star==0}')
