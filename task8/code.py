


print("===== EXAMINATION RESULT SYSTEM =====")


name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))


max_marks = int(input("Enter maximum marks per subject: "))
pass_marks = int(input("Enter minimum passing marks: "))
grace_limit = int(input("Enter maximum grace marks per subject: "))


if (n <= 0 or max_marks <= 0 or
    pass_marks < 0 or pass_marks > max_marks or
    grace_limit < 0):
    print("Invalid examination rules!")

else:
    total_marks = 0
    total_maximum = n * max_marks
    all_pass = True
    grace_used = 0

    subject_results = []

    for i in range(n):
        print("\nSubject", i + 1)

        subject = input("Enter subject name: ")
        marks = int(input("Enter obtained marks: "))

       
        if marks < 0 or marks > max_marks:
            print("Invalid marks! Enter marks within the limit.")
            all_pass = False
            break

        final_marks = marks
        grace = 0

        
        if marks < pass_marks:
            required = pass_marks - marks

            if required <= grace_limit:
                grace = required
                final_marks = min(
                    marks + grace,
                    max_marks
                )

        
        if final_marks >= pass_marks:
            status = "PASS"
        else:
            status = "FAIL"
            all_pass = False

        total_marks += final_marks
        grace_used += grace

        subject_results.append(
            (subject, marks, grace, final_marks, status)
        )

    if len(subject_results) == n:

        percentage = (total_marks / total_maximum) * 100

       
        if not all_pass:
            classification = "FAIL"
        elif percentage >= 75:
            classification = "DISTINCTION"
        elif percentage >= 60:
            classification = "FIRST CLASS"
        elif percentage >= 50:
            classification = "SECOND CLASS"
        else:
            classification = "PASS"

       
        print("\n===== FINAL EXAMINATION RESULT =====")
        print("Student Name:", name)

        print("\nSubject-wise Results:")
        print("-----------------------------------------------")
        print("Subject | Original | Grace | Final | Status")
        print("-----------------------------------------------")

        for subject, original, grace, final, status in subject_results:
            print(subject, "|", original, "|",
                  grace, "|", final, "|", status)

        print("-----------------------------------------------")
        print("Total Marks:", total_marks, "/", total_maximum)
        print("Grace Marks Used:", grace_used)
        print("Percentage:", round(percentage, 2), "%")
        print("Final Classification:", classification)

        print("\n===== RESULT COMPLETED =====")

