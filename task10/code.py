


print("===== ATM TRANSACTION SYSTEM =====")


balance = float(input("Enter initial account balance: "))
withdrawal_limit = float(input("Enter maximum withdrawal limit: "))
n = int(input("Enter number of transactions: "))


if balance < 0 or withdrawal_limit <= 0 or n <= 0:
    print("Invalid account details!")

else:
   
    total_deposits = 0
    total_withdrawals = 0
    successful = 0
    rejected = 0

   
    for i in range(n):

        print("\nTransaction", i + 1)

        transaction_type = input(
            "Enter transaction type (D/W): "
        ).upper()

        amount = float(input("Enter transaction amount: "))

       
        if amount <= 0:
            print("Transaction Rejected: Invalid amount")
            rejected += 1

        elif transaction_type == "D":

            balance += amount
            total_deposits += amount
            successful += 1

            print("Deposit Successful")
            print("Updated Balance:", round(balance, 2))

        elif transaction_type == "W":

            if amount > withdrawal_limit:
                print("Transaction Rejected: "
                      "Withdrawal limit exceeded")
                rejected += 1

            elif amount > balance:
                print("Transaction Rejected: "
                      "Insufficient balance")
                rejected += 1

            else:
                balance -= amount
                total_withdrawals += amount
                successful += 1

                print("Withdrawal Successful")
                print("Updated Balance:", round(balance, 2))

        else:
            print("Transaction Rejected: Invalid transaction type")
            rejected += 1

   
    print("\n===== ATM TRANSACTION SUMMARY =====")

    print("Total Deposits:", round(total_deposits, 2))
    print("Total Withdrawals:", round(total_withdrawals, 2))
    print("Successful Transactions:", successful)
    print("Rejected Transactions:", rejected)
    print("Final Account Balance:", round(balance, 2))

    print("\n===== THANK YOU FOR USING ATM =====")

