# Grade to point mapping
grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "F": 0
}

total_units = 0
total_weighted_points = 0

print("Enter the grade and course unit for 6 courses:")

for i in range(1, 7):
    grade = input(f"Course {i} grade (A-F): ").upper()
    unit = int(input(f"Course {i} unit: "))

    if grade in grade_points:
        total_units += unit
        total_weighted_points += grade_points[grade] * unit
    else:
        print("Invalid grade entered. Please use A-F.")
        exit()

gpa = total_weighted_points / total_units
print(f"\nYour GPA is: {gpa:.2f}")