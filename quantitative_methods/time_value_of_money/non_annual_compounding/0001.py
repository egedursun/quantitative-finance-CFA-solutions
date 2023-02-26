"""
Continuing with the CD example, suppose your bank offers you a CD with a two-
year maturity, a stated annual interest rate of 8 percent compounded quarterly,
and a feature allowing reinvestment of the interest at the same interest rate. You
decide to invest $10,000. What will the CD be worth at maturity?
"""

# Set the variables
principal = 10000
interest_rate = 0.08
compounding_periods = 4 # quarterly compounding
investment_horizon = 2 # 2-year maturity

# Calculate the value of the CD at maturity
compounding_factor = 1 + (interest_rate / compounding_periods)
compounding_periods_investment_horizon = compounding_periods * investment_horizon
interest = principal * ((compounding_factor) ** compounding_periods_investment_horizon - 1)
future_value = principal * (compounding_factor ** compounding_periods_investment_horizon)

# Print the result
print("The value of the CD at maturity is: ${:,.2f}".format(future_value))
