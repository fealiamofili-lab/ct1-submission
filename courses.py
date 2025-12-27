# Dictionary for room numbers for each course
course_rooms = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

# Dictionary for instructors for each course
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Dictionary for meeting times for each course
course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Function to display course information
def display_course_info(course_number):
    try:
        # Look up the room, instructor, and meeting time
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        time = course_times[course_number]

        # Print the information
        print("Course Number:", course_number)
        print("Room Number:", room)
        print("Instructor:", instructor)
        print("Meeting Time:", time)

    except KeyError:
        # Handle invalid course numbers
        print("Invalid course number. Please try again.")

# Main program
def main():
    # Ask the user for a course number
    course_number = input("Enter the course number (e.g., CSC101): ").upper()
    # Display the course information
    display_course_info(course_number)

# Run the program
main()
