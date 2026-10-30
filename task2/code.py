


print("===== HOSPITAL BILLING SYSTEM =====")


name = input("Enter patient name: ")
age = int(input("Enter patient age: "))


consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))


if age <= 0:
    print("Invalid age!")

elif consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
   
    total_bill = consultation + diagnostic + treatment

   
    print("\nSelect Patient Category:")
    print("1. General Patient")
    print("2. Senior Citizen")
    print("3. BPL Patient")
    print("4. Emergency Patient")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        category = "General Patient"
        discount = 0

    elif choice == 2:
        category = "Senior Citizen"
        discount = 10

    elif choice == 3:
        category = "BPL Patient"
        discount = 20

    elif choice == 4:
        category = "Emergency Patient"
        discount = 5

    else:
        print("Invalid patient category!")
        exit()

  
    concession = total_bill * discount / 100

   
    final_amount = total_bill - concession

 
    print("\n===== FINAL HOSPITAL BILL =====")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Patient Category:", category)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Bill: Rs.", total_bill)
    print("Concession:", discount, "%")
    print("Concession Amount: Rs.", concession)
    print("Final Payable Amount: Rs.", final_amount)

