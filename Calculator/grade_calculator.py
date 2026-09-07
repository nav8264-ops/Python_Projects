"""Marks/Grade Calculator"""

def calculate_grade(percentage):
    # Determine the grade based on percentage
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def process_student_marks(marks_list, max_per_subject=100):
    # Calculate total marks, percentage, and grade
    total_marks = sum(marks_list)
    total_possible = len(marks_list) * max_per_subject # Total possible marks based on number of subjects
    percentage = (total_marks / total_possible) * 100
    grade = calculate_grade(percentage)

    # Condition: Check if passed all subjects
    has_failed_subject = any(mark < 40 for mark in marks_list)
    status = "FAILED (Subject criteria not met)" if has_failed_subject else "PASSED"
    return total_marks, total_possible, percentage, grade, status

subjects = ["Math", "Science", "English", "History", "Computer"]
student_marks = []

print("=== Student Marks Entry ===")
for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= score <= 100:
                student_marks.append(score)  # Adding score to the list
                break
            else:
                print("Invalid score! Must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid numeric value.")

# Process the results using the function
# To Calculate total, percentage, grade, and final status based on the marks entered by the user
total, total_possible, percent, letter_grade, final_status = process_student_marks(student_marks)

# Display Summary
print("\n" + "=" * 30)
print("       GRADE REPORT       ")
print("=" * 30)
for idx, subject in enumerate(subjects):  # enumerate to get index and subject name
    print(f"{subject:10}: {student_marks[idx]} / 100")

print("-" * 30)
print(f"Total Marks : {total:.1f} / {total_possible}")
print(f"Percentage  : {percent:.2f}%")
print(f"Grade       : {letter_grade}")
print(f"Status      : {final_status}")
print("=" * 30)
