"""
Given a 5 percent discount rate, find the present value of a four-year ordinary
annuity of £100 per year starting in Year 1 as the difference between the following
two level perpetuities:

Perpetuity 1 £100 per year starting in Year 1 (first payment at  t  = 1)
Perpetuity 2 £100 per year starting in Year 5 (first payment at  t  = 5)
"""

A = 100
r = 0.05
n = 4

pv0_perp1 = A / r

pv4_perp2 = A / r
pv0_perp2 = pv4_perp2 / ((1 + r)**n)

pv0_annuity = pv0_perp1 - pv0_perp2
print("Difference P1 and P2: ", round(pv0_annuity, 2))
