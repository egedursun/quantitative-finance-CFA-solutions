"""
An Australian bank offers to pay you 6 percent compounded monthly. You decide
to invest A$1 million for one year. What is the future value of your investment
if interest payments are reinvested at 6 percent?
"""

principal = 1000000  # principal amount
interest_rate = 0.06 / 12  # monthly interest rate
time_periods = 12  # number of months

future_value = principal * (1 + interest_rate) ** time_periods
print("$", round(future_value))
