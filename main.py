print("Welcome to the gross monthly income calculator ")
payment = int(input("Please input your hourly wage : "))

week_n = int(input("Please input the amount of hours you work in a week : "))

annual_pay = payment*week_n*52

gross_mon = annual_pay/12

print("Your gross monthly income is : ", gross_mon)



