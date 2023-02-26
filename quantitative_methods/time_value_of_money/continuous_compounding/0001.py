"""
Suppose a $10,000 investment will earn 8 percent compounded continuously
for two years. Compute the future value.
"""

import math

principal = 10000  # principal amount
interest_rate = 0.08  # annual interest rate
time_periods = 2  # number of years

future_value = principal * math.exp(interest_rate * time_periods)
print(future_value)
