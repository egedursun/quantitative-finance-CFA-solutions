"""
A German pension fund manager anticipates that benefits of
 €1 million per year must be paid to retirees. Retirements
 will not occur until 10 years from now at time  t  = 10.
 Once benefits begin to be paid, they will extend until
 t  = 39 for a total of 30 payments. What is the present
 value of the pension liability if the appropriate annual
 discount rate for plan liabilities is 5 percent compounded
 annually?
"""

pmt = 1_000_000
r = 0.05
n = 30

t9V = pmt * ((1 - (1 / (1 + r)**n))/r)

PV = t9V * ((1 + r)**(-9))

print("t=9 value -> ", "$", round(t9V, 2))
print("t=0 value (Discounted) -> $", round(PV, 2))
