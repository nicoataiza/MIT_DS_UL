annual_salary = int(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * 0.25
# savings can be 1000000-100 or +100
# only 36 months

# bisection search
start = 0
end = 10000
ctr = 0
rate = 0 
current_savings = 0
check = False
while not(portion_down_payment-100 <= current_savings <= portion_down_payment+100):
    current_savings = 0
    monthly_salary = annual_salary/12
    ctr += 1
    mid = ((start + end)//2)
    rate = mid*0.0001
    # savings
    for month in range(36):
        current_savings += monthly_salary * rate + current_savings*(0.04/12)
        month +=1 
        if month % 6 == 0:
            monthly_salary *= (1 + semi_annual_raise)
    if current_savings > portion_down_payment:
        end = mid
    else:
        start = mid
    if mid >= 9999 and not(portion_down_payment-100 <= current_savings <= portion_down_payment+100):
        check = True
        break
if check:
    print("It is not possible to pay the down payment in three years.")
else:
    print(f"Best savings: {round(rate,4)}")
    print(f"Steps in bisection search: {ctr}")