


print("===== CAMPUS EVENT FINANCIAL PLANNING =====")


venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))


catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))


participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter available sponsorship amount: "))


if (venue < 0 or equipment < 0 or transport < 0 or
    catering < 0 or certificate < 0 or
    participants <= 0 or sponsorship < 0):

    print("Invalid input! Enter valid positive values.")

else:
   
    fixed_cost = venue + equipment + transport

    variable_cost = catering + certificate

    total_variable_cost = variable_cost * participants

   
    total_cost = fixed_cost + total_variable_cost

    
    required_amount = max(0, total_cost - sponsorship)

   
    contribution = required_amount / participants

    
    if contribution > variable_cost:
        break_even = fixed_cost / (contribution - variable_cost)
        break_even = int(break_even) + (
            break_even % 1 > 0
        )
    else:
        break_even = None

  
    print("\n===== EVENT FINANCIAL REPORT =====")

    print("Venue Cost:", venue)
    print("Equipment Cost:", equipment)
    print("Transport Cost:", transport)
    print("Catering Cost:", catering * participants)
    print("Certificate Cost:", certificate * participants)

    print("--------------------------------")
    print("Fixed Cost:", fixed_cost)
    print("Variable Cost:", total_variable_cost)
    print("Total Event Cost:", total_cost)

    print("Sponsorship Amount:", sponsorship)
    print("Sponsorship Shortfall:", required_amount)

    print("Participant Contribution:",
          round(contribution, 2))

    if break_even is not None:
        print("Minimum Registrations to Break Even:",
              break_even)
    else:
        print("Break-even cannot be achieved with this contribution.")

    print("\n===== EVENT PLANNING COMPLETED =====")

