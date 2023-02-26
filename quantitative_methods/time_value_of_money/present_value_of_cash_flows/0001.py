"""
Suppose you are considering purchasing a financial asset that promises to pay
€1,000 per year for five years, with the first payment one year from now. The
required rate of return is 12 percent per year. How much should you pay for
this asset?
"""

annual_payment = 1000  # annual payment for 5 years
interest_rate = 0.12  # required rate of return
time_periods = 5  # number of years

present_value = (annual_payment * (1 - (1 / (1 + interest_rate) ** time_periods))/(interest_rate))
print(round(present_value, 2))




