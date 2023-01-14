annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the perfenct of your salary to save, as a decimal :"))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
monthly_salary = annual_salary/12

months = 0
while current_savings < portion_down_payment:
    current_savings += monthly_salary * portion_saved + current_savings*(0.04/12)
    months +=1 
print(f"Number of months: {months}")