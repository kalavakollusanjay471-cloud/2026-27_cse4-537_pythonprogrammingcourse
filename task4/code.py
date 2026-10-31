

print("===== RAILWAY FARE CALCULATOR =====")


distance = float(input("Enter journey distance (km): "))


n = int(input("Enter number of passengers: "))


print("\nSelect Travel Class:")
print("1. Sleeper")
print("2. AC 3-Tier")
print("3. AC 2-Tier")

choice = int(input("Enter your choice: "))


if choice == 1:
    class_name = "Sleeper"
    rate = 1.5
    reservation = 20
elif choice == 2:
    class_name = "AC 3-Tier"
    rate = 3.0
    reservation = 40
elif choice == 3:
    class_name = "AC 2-Tier"
    rate = 4.5
    reservation = 50
else:
    print("Invalid class selection!")
    exit()

total_fare = 0


for i in range(1, n + 1):

    print("\nPassenger", i)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

   
    basic_fare = distance * rate

   
    if age < 5:
        concession = 100
    elif age <= 11:
        concession = 50
    elif age >= 60:
        concession = 40
    else:
        concession = 0

    fare = basic_fare - (basic_fare * concession / 100)

   
    if age < 5:
        final_fare = 0
    else:
        final_fare = fare + reservation

    print("\nPassenger Name:", name)
    print("Age:", age)
    print("Travel Class:", class_name)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Concession:", concession, "%")
    print("Reservation Fee: Rs.",
          reservation if age >= 5 else 0)
    print("Ticket Fare: Rs.", round(final_fare, 2))

    total_fare += final_fare

print("\n===== RESERVATION SUMMARY =====")
print("Total Passengers:", n)
print("Total Ticket Fare: Rs.", round(total_fare, 2))


cancel = input("\nDo you want to cancel the tickets? (yes/no): ")

if cancel.lower() == "yes":

    penalty_rate = 20

    penalty = total_fare * penalty_rate / 100
    refund = total_fare - penalty

    print("\n===== CANCELLATION DETAILS =====")
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund Amount: Rs.", round(refund, 2))

else:
    print("Tickets successfully reserved!")

print("\nThank you for using Railway Reservation System!")

