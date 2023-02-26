"""
You are retiring today and must choose to take your retirement benefits either as
a lump sum or as an annuity. Your company’s benefits officer presents you with
two alternatives: an immediate lump sum of $2 million or an annuity with 20
payments of $200,000 a year with the first payment starting today. The interest
rate at your bank is 7 percent per year compounded annually. Which option has
the greater present value? (Ignore any tax differences between the two options.)
"""

lump_sum = 2000000  # immediate lump sum payment
interest_rate = 0.07  # interest rate
annuity_payment = 200000  # annual annuity payment
num_payments = 20  # number of annuity payments

lump_sum_pv = lump_sum  # present value of lump sum is equal to the lump sum

annuity_pv = 0  # initialize present value of annuity payments

for n in range(1, num_payments):
    annuity_pv += annuity_payment / (1 + interest_rate) ** n

print("A. Total Payments in the Future: $", round(annuity_pv, 2)+200_000)
print("B. Lump Sum Payment: $ 2000000")
print("Option A / Annuity is a better option.")

