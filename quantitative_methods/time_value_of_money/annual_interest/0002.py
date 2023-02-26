"""
An institution offers you the following terms for a contract: For an investment
of ¥2,500,000, the institution promises to pay you a lump sum six years from
now at an 8 percent annual interest rate. What future amount can you expect?

FV = PV * (1 + r)^t
"""

present_value = 2500000
interest_rate = 0.08
years = 6

future_value = present_value * (1 + interest_rate) ** years

print(f"The future amount after {years} years is: ¥{future_value:,.2f}")
