# Grade Classifier

students = [
    {"name": "Khushbu", "score": 92},
    {"name": "Aman", "score": 76},
    {"name": "Riya", "score": 64},
    {"name": "Rahul", "score": 48},
    {"name": "Sneha", "score": 85}
]


def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


# Sort students by score (highest to lowest)
sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

print("Student Grades:\n")

for student in sorted_students:
    grade = classify(student["score"])
    print(f"{student['name']} - Score: {student['score']} - Grade: {grade}")
