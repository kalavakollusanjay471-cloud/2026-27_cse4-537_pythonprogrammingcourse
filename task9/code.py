

print("===== ATTENDANCE RECOVERY SYSTEM =====")


name = input("Enter student name: ")

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))

eligibility = float(input("Enter required attendance percentage: "))


if (total_classes <= 0 or attended_classes < 0 or
    attended_classes > total_classes or
    eligibility <= 0 or eligibility > 100):

    print("Invalid input! Please enter valid values.")

else:
    
    current_percentage = (
        attended_classes / total_classes
    ) * 100

    print("\n===== CURRENT ATTENDANCE =====")
    print("Student Name:", name)
    print("Total Classes:", total_classes)
    print("Attended Classes:", attended_classes)
    print("Current Attendance:",
          round(current_percentage, 2), "%")

    print("Eligibility Requirement:", eligibility, "%")

    
    if current_percentage >= eligibility:
        print("\nStatus: ELIGIBLE")
        print("No additional classes required.")

        minimum_classes = 0

    else:
        print("\nStatus: NOT ELIGIBLE")

       
        minimum_classes = 0

        while (
            (attended_classes + minimum_classes) /
            (total_classes + minimum_classes) * 100
        ) < eligibility:
            minimum_classes += 1

        print("Minimum consecutive classes to attend:",
              minimum_classes)

   
    print("\n===== FUTURE ATTENDANCE SCENARIOS =====")

    future_classes = int(
        input("Enter number of upcoming classes: ")
    )

    if future_classes < 0:
        print("Invalid number of future classes.")

    else:
        scenarios = {
            "Attend all classes": future_classes,
            "Attend 75% classes": int(future_classes * 0.75),
            "Attend 50% classes": int(future_classes * 0.50),
            "Attend no classes": 0
        }

        for scenario, future_attended in scenarios.items():

            new_attended = attended_classes + future_attended
            new_total = total_classes + future_classes

            percentage = (new_attended / new_total) * 100

            print("\n", scenario)
            print("Classes Attended:", future_attended)
            print("Final Attendance:",
                  round(percentage, 2), "%")

            if percentage >= eligibility:
                print("Status: ELIGIBLE")
            else:
                print("Status: NOT ELIGIBLE")

    print("\n===== ATTENDANCE REPORT COMPLETED =====")

