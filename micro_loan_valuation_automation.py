import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]

## calculate quantity, average & total price of loans.
total_number_loans = len(loan_costs)
loans_total = sum(loan_costs)
avrg_price = loans_total/total_number_loans
print(f" - There is a total of {total_number_loans} loan, valued at $ {loans_total:.2f}")
print(f" - The average loan price is ${avrg_price:.2f}")

## --------------------------------------------------

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

print(f" - For this loan: the fair value = {fair_value:.2f}; Future Value = ${future_value:.2f} ; Remaining months are :{remaining_months}; Hurdle rate is :% {hurdle_rate*100}; The loan price is ${loan_price}")

# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if fair_value >= loan_price:
        print(" - ! The loan is worth at least the cost to buy it")
else:
        print(" - the loan is too expensive and not worth the price.")
