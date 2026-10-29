


MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Student name: ")
    aggregate = float(input("Aggregate percentage: "))

    subjects = list(map(
        int, input("Enter marks in 3 subjects: ").split()
    ))

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income (Rs.): "))

    
    eligible = (
        aggregate >= MIN_AGGREGATE
        and len(subjects) == 3
        and all(mark >= MIN_SUBJECT_MARK for mark in subjects)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME
    )

    student = {
        "name": name,
        "aggregate": aggregate,
        "subjects": subjects,
        "attendance": attendance,
        "income": income,
        "eligible": eligible
    }

    students.append(student)


print("\n--- Eligibility Results ---")

for student in students:
    status = "Eligible" if student["eligible"] else "Not Eligible"
    print(f"{student['name']}: {status}")


eligible_students = [
    student for student in students if student["eligible"]
]


eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)


print("\n--- Scholarship Ranking ---")

if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"{rank}. {student['name']} | "
            f"Aggregate: {student['aggregate']:.2f}% | "
            f"Attendance: {student['attendance']:.2f}% | "
            f"Income: Rs.{student['income']:.0f}"
        )
else:
    print("No eligible students found.")

