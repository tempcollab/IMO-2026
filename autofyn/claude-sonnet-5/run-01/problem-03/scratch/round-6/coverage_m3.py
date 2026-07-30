from fractions import Fraction as F
import itertools

c2 = F(4,7)

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def best_known_candidates(p1,p2,p3):
    S = p2+p3
    candidates = []
    # DOM: p1 >= S  -> value p1  (2 marks: split p1 into p2, r=p1-S... wait k=m-1=2 marks)
    if p1 >= S:
        candidates.append(('DOM', p1))
    # HALVE: p1 >= 2*p2 -> split p1 into two halves, value p1/2 + oddrank(tail)=p1/2+p2
    if p1 >= 2*p2:
        candidates.append(('HALVE', p1/2+p2))
    # TAIL-SNIP: split p3 (smallest) into two halves; m=3 odd -> value = oddrank(A)-p3/2
    val_ts = (p1+p3) - p3/2
    candidates.append(('TAIL-SNIP', val_ts))
    # SANDWICH: feasible if p1 < p2+p3 (=S); value = p2+p3 = S
    if p1 < S:
        candidates.append(('SANDWICH', S))
    return candidates

def scan():
    N = 40
    worst = None
    count_covered = 0
    count_total = 0
    fail_examples = []
    for i in range(1, N):
        for j in range(1, N-i):
            k = N-i-j
            if k < 1: continue
            p1,p2,p3 = F(i,N), F(j,N), F(k,N)
            vals = sorted([p1,p2,p3], reverse=True)
            p1,p2,p3 = vals
            if p1==p2 or p2==p3: continue  # skip ties for genericity
            count_total += 1
            cands = best_known_candidates(p1,p2,p3)
            best = min(v for _,v in cands)
            if best <= c2 + F(1,10**9):
                count_covered += 1
            else:
                fail_examples.append((p1,p2,p3,best,cands))
    print("total", count_total, "covered", count_covered, "uncovered", count_total-count_covered)
    print("sample uncovered:")
    for ex in fail_examples[:10]:
        print(ex)

scan()
