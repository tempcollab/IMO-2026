from fractions import Fraction as F
import random

def partial_dom_leftover(A):
    A = tuple(sorted(A, reverse=True))
    p1 = A[0]; tail = A[1:]
    S = F(0); jstar = 0
    for j in range(1, len(tail)+1):
        Snew = S + tail[j-1]
        if p1 >= Snew:
            jstar = j; S = Snew
        else:
            break
    r = p1 - S
    leftover = list(tail[jstar:])
    if r > 0:
        leftover.append(r)
    leftover = tuple(sorted(leftover, reverse=True))
    return jstar, S, leftover

random.seed(2)
trials=0; case_c_fail=0
worst_ratio = None
for m in range(3, 12):
    for _ in range(2000):
        vals = [random.random()**2 for _ in range(m)]
        s = sum(vals); vals=[v/s for v in vals]
        vals.sort(reverse=True)
        if vals[0] >= 0.5:
            continue
        Af = [F(v).limit_denominator(500) for v in vals]
        s2 = sum(Af); Af=[a/s2 for a in Af]
        if Af[0] >= F(1,2):
            continue
        trials += 1
        jstar, S, leftover = partial_dom_leftover(Af)
        if len(leftover)==0:
            continue
        Sigma_left = sum(leftover)
        top_left = leftover[0]
        if Sigma_left == 0:
            continue
        ratio = top_left / Sigma_left  # want < 1/2 for Case C to hold
        if ratio >= F(1,2):
            case_c_fail += 1
            if worst_ratio is None or ratio>worst_ratio:
                worst_ratio = ratio
                worst_example = (Af, jstar, leftover, ratio)

print("trials:", trials, "case_c_fail (leftover NOT Case C):", case_c_fail)
if case_c_fail:
    print("worst ratio found:", worst_ratio, float(worst_ratio))
    print("example:", worst_example)
