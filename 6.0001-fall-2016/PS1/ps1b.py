annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the perfenct of your salary to save, as a decimal :"))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
monthly_salary = annual_salary/12

months = 0
while current_savings < portion_down_payment:
    current_savings += monthly_salary * portion_saved + current_savings*(0.04/12)
    months +=1 
    if months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
print(f"Number of months: {months}")