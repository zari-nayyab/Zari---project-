quantity = int(input("Enter quantity: "))
price_per_item = float(input("Enter price per item: "))
total_bill = quantity * price_per_item
print("You bought", quantity, "items and total cost is", round(total_bill, 2), "Rs")
