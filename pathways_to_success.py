# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    calculate_present_value = future_value / ( 1 + annual_discount_rate/12)**remaining_months
    return (calculate_present_value)
       

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
annual_discount_rate = .2
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)



print(f"The present value of the loan is: {present_value}")