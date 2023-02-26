"""
An insurance company has issued a Guaranteed Investment Contract (GIC)
that promises to pay $100,000 in six years with an 8 percent return rate. What
amount of money must the insurer invest today at 8 percent for six years to
make the promised payment?
"""

future_value = 100000  # future value of the promised payment
interest_rate = 0.08  # annual interest rate
time_periods = 6  # number of years

present_value = future_value / ((1 + interest_rate) ** time_periods)
print(present_value)
