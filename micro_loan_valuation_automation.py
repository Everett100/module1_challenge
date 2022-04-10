

loan_costs = [500, 600, 200, 1000, 450]

## calculate quantity, average & total price of loans.
total_number_loans = len(loan_costs)
loans_total = sum(loan_costs)
avrg_price = loans_total/total_number_loans
print(f" There is a total of {total_number_loans} loan, valued at $ {loans_total:.2f}")
print(f" The average loan price is ${avrg_price:.2f}")

## One small change for Git practice