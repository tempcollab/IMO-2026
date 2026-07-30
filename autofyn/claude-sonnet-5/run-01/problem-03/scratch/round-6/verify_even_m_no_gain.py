from fractions import Fraction as F
import random

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

random.seed(2)
fails=0
checked=0
for _ in range(5000):
    m = random.choice([4,6])
    tail_n = m-1
    tail = sorted((F(random.randint(1,10000),1) for _ in range(tail_n)), reverse=True)
    if len(set(tail)) < tail_n: continue
    p2, pm = tail[0], tail[-1]
    p1 = p2 + F(random.randint(1,10000),1)  # p1 > p2, arbitrary, must be >= p2
    A = [p1]+tail
    x = p2 - F(1,10**6)  # x just below p2 (near-boundary approx, since true sup not attained)
    # only test the LIMIT claim qualitatively: as x -> p2^-, oddrank(B) -> oddrank(A)
    y = p1-x
    if y<=0: continue
    B = [x,y]+tail
    got = oddrank(B)
    orig = oddrank(A)
    checked+=1
    diff = got-orig
    if abs(diff) > F(1,1000):
        fails+=1
        print("large diff", A, got, orig, diff)
print("checked",checked,"fails(large diff)",fails)
