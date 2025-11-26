# Ask user for the current time in hours (0-23)
current_time = int(input("Enter the current time (0-23): "))

# Ask user for how many hours until the alarm goes off
hours_to_wait = int(input("Enter how many hours until the alarm: "))

# Calculate the alarm time using a 24-hour clock
alarm_time = (current_time + hours_to_wait) % 24

# Show the time the alarm will go off
print("The alarm will go off at:", alarm_time)

