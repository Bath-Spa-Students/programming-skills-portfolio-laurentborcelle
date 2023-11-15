# Get the number of courses and total marks from the user
num_courses = int(input("Enter the number of courses: "))
total_marks = int(input("Enter the total marks for all courses (or 500 if you want to use the default): "))

# Initialize a variable to store the sum of course marks
total_score = 0

# Get course marks from the user and calculate the total score
for i in range(num_courses):
    course_mark = float(input(f"Enter the mark for course {i + 1}: "))
    total_score += course_mark

# Calculate the average of course marks
average = total_score / num_courses

# Calculate the percentage based on the total marks
percentage = (total_score / total_marks) * 100

# Print the average and percentage
print(f"Average of course marks: {average}")
print(f"Percentage: {percentage}%")
