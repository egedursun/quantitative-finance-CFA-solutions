"""
The manager of a Canadian pension fund knows that the fund must make a
lump-sum payment of C$5 million 10 years from now. She wants to invest an
amount today in a GIC so that it will grow to the required amount. The current
interest rate on GICs is 6 percent a year, compounded monthly. How much
should she invest today in the GIC?
"""

future_value = 5000000  # future value of the required payment
interest_rate = 0.06 / 12  # monthly interest rate
time_periods = 10 * 12  # number of months until maturity

present_value = future_value / ((1 + interest_rate) ** time_periods)
print(present_value)
