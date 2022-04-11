import csv
from itertools import count
from pathlib import Path

##--------------------------------------------------

loan_costs = [500, 600, 200, 1000, 450]

## calculate quantity, average & total price of loans.
total_number_loans = len(loan_costs)
loans_total = sum(loan_costs)
avrg_price = loans_total/total_number_loans
print(f" - There is a total of {total_number_loans} loan, valued at $ {loans_total:.2f}")
print(f" - The average loan price is ${avrg_price:.2f}")

## --------------------------------------------------
print("-----------------------------------------------")

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

## Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
loan_price = loan.get("loan_price")
hurdle_rate = .20

#Use the formula for Present Value to calculate a "fair value" of the loan with 20% Hurdle rate, compouded monthly
fair_value = future_value / (1 + (hurdle_rate / 12)) ** remaining_months
print(f" - The fair value of the this loan is: ${fair_value:.2f}")

print(f" - For this loan: the fair value = {fair_value:.2f}; Future Value = ${future_value:.2f} ; Remaining months are :{remaining_months}; Hurdle rate is :{hurdle_rate*100:.0f}%; The loan price is ${loan_price}")

# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if fair_value >= loan_price:
        print(" - The loan is worth at least the cost to buy it")
else:
        print(" - the loan is too expensive and not worth the price.")

## ---------------------------------------------------------
print("-----------------------------------------------")

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
        present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
        print(f"The present value of the new loan is: {present_value:.2f}")
        return present_value

annual_discount_rate = 0.20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)

    
print("-----------------------------------------------")

##-----------------------------------------------------

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

count = 0
for loan_price in loans:
    if loan_price["loan_price"] <= 500:
        inexpensive_loans.append(loan_price)
        count = count + 1
        
                
# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

print(f" Following is a list of ({count})Inexpensive Loans..... {inexpensive_loans}")

