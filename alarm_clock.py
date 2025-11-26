current_time = int(input("Enter the current time (0-23): "))
hours_to_wait = int(input("Enter how many hours until the alarm: "))

alarm_time = (current_time + hours_to_wait) % 24

print("The alarm will go off at:", alarm_time)


