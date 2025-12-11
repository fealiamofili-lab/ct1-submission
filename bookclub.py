# Ask the user how many books they bought this month
books = int(input("Enter the number of books you purchased this month: "))

# Decide points based on the number of books
if books == 0:
    points = 0
elif books == 2:
    points = 5
elif books == 4:
    points = 15
elif books == 6:
    points = 30
elif books >= 8:
    points = 60
else:
    points = 0  # For any other number not listed

# Show the points the customer earned
print("You earned", points, "points this month.")
