# Get the total for the meal from the user
meal_total = float(input("Enter the total amount of the meal: $"))

# Figure out the tip (18% of the meal)
tip = round(meal_total * 0.18, 2)

# Figure out the sales tax (7% of the meal)
tax = round(meal_total * 0.07, 2)

# Add everything together for the total
total_amount = round(meal_total + tip + tax, 2)

# Show the tip, tax, and total
print("Tip (18%): $", tip)
print("Sales Tax (7%): $", tax)
print("Total Amount: $", total_amount)

