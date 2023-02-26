"""
A pension fund manager estimates that his corporate sponsor will make a
$10 million contribution five years from now. The rate of return on plan assets
has been estimated at 9 percent per year. The pension fund manager wants to
calculate the future value of this contribution 15 years from now, which is the
date at which the funds will be distributed to retirees. What is that future value?

fv = pv * (1 + r) ** n
"""

# Set the variables
future_contribution = 10000000  # $10 million
years_to_contribution = 5
years_to_distribution = 15
rate_of_return = 0.09

# Calculate the future value
pv = future_contribution
n = years_to_distribution - years_to_contribution
r = rate_of_return
fv = pv * (1 + r) ** n

# Print the result
print("The future value of the contribution is: $", round(fv, 2))
