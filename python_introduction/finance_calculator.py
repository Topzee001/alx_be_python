monthly_income = input("Enter your monthly income: ")

monthly_expenses = input("Enter your monthly expenses: ")

monthly_savings = int(monthly_income) - int(monthly_expenses)

annual_interest = 0.05
months = 12 # Calculate the projected savings for one year

Projected_savings = monthly_savings * 12 + (monthly_savings * annual_interest * months)

print("Your monthly savings are:", monthly_savings)
print("Projected savings after one year, with interest, is: $", Projected_savings)