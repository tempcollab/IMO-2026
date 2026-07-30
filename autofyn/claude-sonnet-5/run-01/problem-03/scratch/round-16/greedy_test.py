from fractions import Fraction as F

def oddrank(lst):
    s = sorted(lst, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def greedy_solve(A_desc, marks):
    """A_desc: sorted descending list of Fractions. marks: available real marks (int)."""
    m = len(A_desc)
    if m <= 1 or marks <= 0:
        return list(A_desc)
    p1 = A_desc[0]
    tail = list(A_desc[1:])  # descending
    Sigma_tail = sum(tail)
    if p1 >= Sigma_tail:
        # Full DOM match (contiguous, all of tail); ignore extra recursion into leftover r for simplicity
        r = p1 - Sigma_tail
        cost = len(tail) - (1 if r == 0 else 0)
        if cost > marks:
            # can't afford full match; fall back: just leave as is (should not happen at top-level budget m-1)
            return list(A_desc)
        pieces = []
        for t in tail:
            pieces += [t, t]
        if r > 0:
            pieces.append(r)
        return pieces
    else:
        # Case C: ascending greedy with running deficit
        tail_asc = list(reversed(tail))  # ascending
        d = p1
        matched = []
        idx = 0
        marks_before = marks
        while idx < len(tail_asc):
            t = tail_asc[idx]
            if d - t >= 0:
                matched.append(t)
                d -= t
                idx += 1
            else:
                break
        r = d
        remaining_tail_asc = tail_asc[idx:]
        pieces_count = len(matched) + (1 if r > 0 else 0)
        cost = max(pieces_count - 1, 0)
        if cost > marks:
            # not enough marks to even do the greedy match fully; truncate matched list
            # take as many matches as marks allow (cost = count-1 for matched-only, no leftover piece)
            # simplest: just match first `marks+? ` -- handle by capping matched count
            # we won't hit this at top-level since marks=m-1 generally suffices; but guard anyway
            take = marks + 1  # pieces_count <= marks+1
            matched = matched[:max(take-1,0)]
            r = p1 - sum(matched)
            remaining_tail_asc = tail_asc[len(matched):]
            pieces_count = len(matched) + (1 if r > 0 else 0)
            cost = max(pieces_count - 1, 0)
        marks_left = marks - cost
        remaining_tail_desc = list(reversed(remaining_tail_asc))
        refined_remainder = greedy_solve(remaining_tail_desc, marks_left) if remaining_tail_desc else []
        pieces = []
        for t in matched:
            pieces += [t, t]
        if r > 0:
            pieces.append(r)
        pieces += refined_remainder
        return pieces

def test(A, marks, target, label):
    A = [F(x) for x in A]
    A_sorted = sorted(A, reverse=True)
    Sigma = sum(A_sorted)
    result_pieces = greedy_solve(A_sorted, marks)
    val = oddrank(result_pieces)
    print(f"--- {label} ---")
    print("A =", A_sorted, "Sigma=", Sigma)
    print("marks=", marks)
    print("achieved oddrank =", val, "=", float(val))
    print("target =", target, "=", float(target))
    print("PASS" if val <= target else "FAIL", "margin=", target - val)
    print()

# Witness 1: T=(0.20,0.15,0.12,0.08), m=4
T = [F(20,100), F(15,100), F(12,100), F(8,100)]
Sigma = sum(T)
# c(3) = 2^3/(2^4-1) = 8/15
c3 = F(8,15)
target1 = c3*Sigma
test(T, 3, target1, "T=(0.20,0.15,0.12,0.08) m=4, target=c(3)*Sigma")

# Witness 2: A=(1826,1563,1520,1514,765)/7188, m=5
A2 = [F(1826,7188), F(1563,7188), F(1520,7188), F(1514,7188), F(765,7188)]
Sigma2 = sum(A2)
c4 = F(16,31)
target2 = c4*Sigma2
test(A2, 4, target2, "A=(1826,1563,1520,1514,765)/7188 m=5, target=c(4)*Sigma")

# Witness 3 (round15 m=6): A=(14,12,10,9,8,4), target 608/21, non-contig optimum 57/2
A3 = [F(14), F(12), F(10), F(9), F(8), F(4)]
Sigma3 = sum(A3)
c5 = F(2**5, 2**6-1)  # 32/63
target3 = F(608,21)
print("check target3 vs c5*Sigma3:", c5*Sigma3, target3)
test(A3, 5, target3, "A=(14,12,10,9,8,4) m=6, target=608/21")

print("=== Variant 2: singleton leftover gets halved if marks remain ===")

def greedy_solve2(A_desc, marks):
    m = len(A_desc)
    if m == 0 or marks <= 0:
        return list(A_desc)
    if m == 1:
        # split into two equal halves using 1 mark if available
        p1 = A_desc[0]
        return [p1/2, p1/2]
    p1 = A_desc[0]
    tail = list(A_desc[1:])
    Sigma_tail = sum(tail)
    if p1 >= Sigma_tail:
        r = p1 - Sigma_tail
        cost = len(tail) - (1 if r == 0 else 0)
        if cost > marks:
            return list(A_desc)
        pieces = []
        for t in tail:
            pieces += [t, t]
        if r > 0:
            pieces.append(r)
        return pieces
    else:
        tail_asc = list(reversed(tail))
        d = p1
        matched = []
        idx = 0
        while idx < len(tail_asc):
            t = tail_asc[idx]
            if d - t >= 0:
                matched.append(t)
                d -= t
                idx += 1
            else:
                break
        r = d
        remaining_tail_asc = tail_asc[idx:]
        pieces_count = len(matched) + (1 if r > 0 else 0)
        cost = max(pieces_count - 1, 0)
        if cost > marks:
            take = marks + 1
            matched = matched[:max(take-1,0)]
            r = p1 - sum(matched)
            remaining_tail_asc = tail_asc[len(matched):]
            pieces_count = len(matched) + (1 if r > 0 else 0)
            cost = max(pieces_count - 1, 0)
        marks_left = marks - cost
        remaining_tail_desc = list(reversed(remaining_tail_asc))
        refined_remainder = greedy_solve2(remaining_tail_desc, marks_left) if remaining_tail_desc else []
        pieces = []
        for t in matched:
            pieces += [t, t]
        if r > 0:
            pieces.append(r)
        pieces += refined_remainder
        return pieces

def test2(A, marks, target, label):
    A = [F(x) for x in A]
    A_sorted = sorted(A, reverse=True)
    Sigma = sum(A_sorted)
    result_pieces = greedy_solve2(A_sorted, marks)
    val = oddrank(result_pieces)
    print(f"--- {label} ---")
    print("A =", A_sorted, "Sigma=", Sigma)
    print("achieved pieces:", sorted(result_pieces, reverse=True))
    print("achieved oddrank =", val, "=", float(val))
    print("target =", target, "=", float(target))
    print("PASS" if val <= target else "FAIL", "margin=", target - val)
    print()

test2(T, 3, target1, "T=(0.20,0.15,0.12,0.08) m=4")
test2(A2, 4, target2, "A2 (m=5 hard witness)")
test2(A3, 5, target3, "A3=(14,12,10,9,8,4) m=6")

print("=== Variant 3: best-fit greedy (pick largest not-exceeding-d item each step, any order) ===")

def greedy_solve3(A_desc, marks):
    m = len(A_desc)
    if m == 0 or marks <= 0:
        return list(A_desc)
    if m == 1:
        p1 = A_desc[0]
        return [p1/2, p1/2]
    p1 = A_desc[0]
    tail = list(A_desc[1:])
    Sigma_tail = sum(tail)
    if p1 >= Sigma_tail:
        r = p1 - Sigma_tail
        cost = len(tail) - (1 if r == 0 else 0)
        if cost > marks:
            return list(A_desc)
        pieces = []
        for t in tail:
            pieces += [t, t]
        if r > 0:
            pieces.append(r)
        return pieces
    else:
        pool = list(tail)  # descending
        d = p1
        matched = []
        while True:
            # best-fit: largest element in pool that is <= d
            candidates = [t for t in pool if t <= d]
            if not candidates:
                break
            t = max(candidates)
            matched.append(t)
            pool.remove(t)
            d -= t
        r = d
        remaining_tail_desc = sorted(pool, reverse=True)
        pieces_count = len(matched) + (1 if r > 0 else 0)
        cost = max(pieces_count - 1, 0)
        if cost > marks:
            # cap matches (rare) - simple fallback, take fewer matches
            matched = matched[:max(marks,0)]
            r = p1 - sum(matched)
            used = set(matched)
            remaining_tail_desc = sorted([t for t in tail if t not in used or matched.count(t) < tail.count(t)], reverse=True)
            pieces_count = len(matched) + (1 if r > 0 else 0)
            cost = max(pieces_count - 1, 0)
        marks_left = marks - cost
        refined_remainder = greedy_solve3(remaining_tail_desc, marks_left) if remaining_tail_desc else []
        pieces = []
        for t in matched:
            pieces += [t, t]
        if r > 0:
            pieces.append(r)
        pieces += refined_remainder
        return pieces

def test3(A, marks, target, label):
    A = [F(x) for x in A]
    A_sorted = sorted(A, reverse=True)
    result_pieces = greedy_solve3(A_sorted, marks)
    val = oddrank(result_pieces)
    print(f"--- {label} ---")
    print("achieved pieces:", sorted(result_pieces, reverse=True))
    print("achieved oddrank =", val, "=", float(val), " target=", float(target))
    print("PASS" if val <= target else "FAIL", "margin=", target - val)
    print()

test3(T, 3, target1, "T=(0.20,0.15,0.12,0.08) m=4")
test3(A2, 4, target2, "A2 (m=5 hard witness)")
test3(A3, 5, target3, "A3=(14,12,10,9,8,4) m=6")
