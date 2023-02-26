"""
The British government once issued a type of security called a consol bond,
which promised to pay a level cash flow indefinitely. If a consol bond paid £100
per year in perpetuity, what would it be worth today if the required rate of
return were 5 percent?
"""

C = 100   # cash flow
r = 0.05  # discount rate
PV = C / r
print(f"The present value of the perpetuity is £{PV:.2f}")
