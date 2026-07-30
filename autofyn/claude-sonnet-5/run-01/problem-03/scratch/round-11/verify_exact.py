from fractions import Fraction as F

p1,p2,p3,p4,p5 = F(1826,7188),F(1563,7188),F(1520,7188),F(1514,7188),F(765,7188)

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

r1 = p1-p2
r3 = p3-p4
# match construction leaves
match_leaves = [p2,p2, p4,p4, r1,r1... ]
