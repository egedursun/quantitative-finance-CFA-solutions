"""
Suppose your company’s defined contribution retirement plan allows you to
invest up to €20,000 per year. You plan to invest €20,000 per year in a stock
index fund for the next 30 years. Historically, this fund has earned 9 percent per
year on average. Assuming that you actually earn 9 percent a year, how much
money will you have available for retirement after making the last payment?
"""

principal = 20000  # annual contribution amount
interest_rate = 0.09  # annual interest rate
time_periods = 30  # number of years

future_value = principal * (((1 + interest_rate) ** time_periods - 1) / interest_rate)
print(future_value)
