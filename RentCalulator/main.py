rent = float(input("Enter Your flat rent = "))
food = float(input("Enter the amount of food ordered = "))
electricity_spend = float(input("Enter the amount for electricity spend = "))
charge_per_unit = float(input("Enter the charge per unit = "))
person = int(input("Enter the numbers persons living in flat = "))

if person > 0:
    total_electricity_bill = electricity_spend * charge_per_unit
    total_expense = food+ rent + total_electricity_bill
    amount_per_person = total_expense/person
    print("Total Expense = ",total_expense)
    print("Each one has to pay = ",round(amount_per_person, 2))
else:
    print("Nos of person must be greater then 0")