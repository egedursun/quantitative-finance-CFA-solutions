"""
Consider a level perpetuity of £100 per year with its first payment beginning at
t  = 5. What is its present value today (at  t  = 0), given a 5 percent discount rate?
"""

A = 100
r = 0.05
n = 5

t4PV = A/r

print("Present Value at t=4 : ", round(t4PV, 2))

PV = t4PV * (1 + r)**(-(n-1))

print("Discounted at t=0 : ", round(PV, 2))



