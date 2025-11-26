meal_total = float(input("Enter the total amount of the meal: $"))

tip = round(meal_total * 0.18, 2)
tax = round(meal_total * 0.07, 2)
total_amount = round(meal_total + tip + tax, 2)

print("Tip (18%): $", tip)
print("Sales Tax (7%): $", tax)
print("Total Amount: $", total_amount)

