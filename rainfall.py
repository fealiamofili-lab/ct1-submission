# Ask the user how many years they want to track
years = int(input("Enter the number of years: "))

# Keep track of total rainfall and total number of months
total_rainfall = 0
total_months = 0

# Go through each year
for year in range(1, years + 1):
    print("Year", year)
    
    # Go through all 12 months
    for month in range(1, 13):
        rainfall = float(input("Enter rainfall for month " + str(month) + ": "))
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall
average_rainfall = total_rainfall / total_months

# Print results
print("Total months:", total_months)
print("Total rainfall:", total_rainfall)
print("Average rainfall per month:", average_rainfall)

