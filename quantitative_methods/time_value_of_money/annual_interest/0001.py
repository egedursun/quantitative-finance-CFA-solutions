"""
You are the lucky winner of your state’s lottery of $5 million after taxes. You
invest your winnings in a five-year certificate of deposit (CD) at a local financial
institution. The CD promises to pay 7 percent per year compounded annually.
This institution also lets you reinvest the interest at that rate for the duration of
the CD. How much will you have at the end of five years if your money remains
invested at 7 percent for five years with no withdrawals?

A = P * (1 + r/n)^(n*t)
"""

principal = 5000000
rate = 0.07
years = 5

final_amount = principal

for i in range(years):
    interest = final_amount * rate
    final_amount += interest
    print(f"Year {i+1}: ${final_amount:,.2f}")

print(f"\nFinal amount after {years} years: ${final_amount:,.2f}")
