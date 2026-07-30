from fractions import Fraction as F

# m=5 witness
S = F(7188)
p1,p2,p3,p4,p5 = F(1826), F(1563), F(1520), F(1514), F(765)
assert p1+p2+p3+p4+p5 == S

def oddrank(pieces, total):
    # sort descending, sum pieces at odd positions (1-indexed)
    xs = sorted(pieces, reverse=True)
    tot = sum(xs)
    assert tot == total, (tot,total)
    s = sum(xs[i] for i in range(len(xs)) if i%2==0)
    return F(s, total)

# Construction A
r1 = p1 - p2   # 263
r3 = p3 - p4   # 6
half = F(p5 - r1, 2)  # (765-263)/2 = 251
piecesA = [p2,p2, p4,p4, r1,r1, half,half, r3]
print("A pieces:", piecesA, "sum:", sum(piecesA))
valA = oddrank(piecesA, S)
print("oddrank A =", valA, float(valA))

# Construction B
h1 = F(p1,2)  # 913
h2 = F(p2,2)  # 781.5
h5 = F(p5,2)  # 382.5
piecesB = [h1,h1, h2,h2, p3, p4, h5,h5, F(0)]
print("B pieces:", piecesB, "sum:", sum(piecesB))
valB = oddrank(piecesB, S)
print("oddrank B =", valB, float(valB))

# target c(4) = 16/31
c4 = F(16,31)
print("c4 =", c4, float(c4))
print("A <= c4?", valA <= c4)
print("B <= c4?", valB <= c4)
print("A == B?", valA == valB)

# 1199/2396 check
print("claimed value 1199/2396 =", float(F(1199,2396)))
