


print("========================================")
print("   MULTI-CURRENCY TRAVEL BUDGET SYSTEM")
print("========================================")


budget = float(input("Enter travel budget in INR: "))


fee_rate = 2


n = int(input("Enter number of expenses: "))

total_expenses = 0
category_totals = {}
expenses = []


for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    currency = input("Enter currency code: ").upper()

    amount = float(input("Enter expense amount: "))
    exchange_rate = float(input("Enter exchange rate to INR: "))

   
    if amount < 0 or exchange_rate <= 0:
        print("Invalid amount or exchange rate!")
        exit()

    
    converted_amount = amount * exchange_rate

    
    conversion_fee = converted_amount * fee_rate / 100

    
    final_amount = converted_amount + conversion_fee

   
    total_expenses += final_amount

   
    if category in category_totals:
        category_totals[category] += final_amount
    else:
        category_totals[category] = final_amount

    
    expenses.append([
        category, currency, amount,
        exchange_rate, converted_amount,
        conversion_fee, final_amount
    ])


largest_category = max(category_totals, key=category_totals.get)
largest_amount = category_totals[largest_category]


balance = budget - total_expenses

=======================")
print("           TRAVEL EXPENSE REPORT")
print("==============================================")

print("{:<15} {:<8} {:>10} {:>12}".format(
    "Category", "Currency", "Amount", "Total INR"
))

print("-" * 55)

for e in expenses:
    print("{:<15} {:<8} {:>10.2f} {:>12.2f}".format(
        e[0], e[1], e[2], e[6]
    ))

print("-" * 55)

print("Conversion Fee Rate:", fee_rate, "%")
print("Total Travel Expenses: Rs.", round(total_expenses, 2))
print("Planned Budget: Rs.", round(budget, 2))


if total_expenses > budget:
    print("Budget Status: OVER BUDGET")
    print("Exceeded Amount: Rs.", round(abs(balance), 2))
else:
    print("Budget Status: WITHIN BUDGET")
    print("Remaining Balance: Rs.", round(balance, 2))


print("\nLargest Expense Category:", largest_category)
print("Largest Category Amount: Rs.", round(largest_amount, 2))

print("\nThank you for using Travel Budget System!")
print("==============================================")

