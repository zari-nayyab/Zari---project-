principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
interest = (principal * rate * time) / 100
total_amount = principal + interest
print("Interest:", round(interest, 2))
print("Total Amount:", round(total_amount, 2))
