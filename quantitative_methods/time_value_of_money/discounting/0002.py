"""
Suppose you own a liquid financial asset that will pay you $100,000 in 10 years
from today. Your daughter plans to attend college four years from today, and
you want to know what the asset’s present value will be at that time. Given an
8 percent discount rate, what will the asset be worth four years from today?
"""

future_value = 100000  # future value of the asset
interest_rate = 0.08  # annual discount rate
time_periods = 10  # number of years until maturity
years_until_college = 4  # number of years until college

present_value = future_value / ((1 + interest_rate) ** (time_periods - years_until_college))
print(present_value)
