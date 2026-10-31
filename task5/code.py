

print("===================================")
print("       RETAIL BILLING SYSTEM")
print("===================================")


tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "groceries": 2,
    "others": 12
}


n = int(input("Enter number of products: "))

products = []
subtotal_total = 0
tax_total = 0


for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ").lower()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

   
    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        exit()

   
    tax_rate = tax_rates.get(category, tax_rates["others"])

   
    subtotal = price * quantity

   
    tax = subtotal * tax_rate / 100

    
    item_total = subtotal + tax

    subtotal_total += subtotal
    tax_total += tax

    products.append([
        name, category, price, quantity,
        subtotal, tax_rate, tax, item_total
    ])


grand_total = subtotal_total + tax_total


if grand_total > 5000:
    discount_rate = 10
elif grand_total > 3000:
    discount_rate = 7
elif grand_total > 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = grand_total * discount_rate / 100


maximum_discount = 1000
if discount > maximum_discount:
    discount = maximum_discount


final_amount = grand_total - discount


print("\n==============================================")
print("              RETAIL INVOICE")
print("==============================================")

print("\nProduct Details:")
print("-" * 70)

print("{:<15} {:<12} {:>8} {:>6} {:>9}".format(
    "Product", "Category", "Price", "Qty", "Subtotal"
))

print("-" * 70)

for p in products:
    print("{:<15} {:<12} {:>8.2f} {:>6} {:>9.2f}".format(
        p[0], p[1], p[2], p[3], p[4]
    ))

print("-" * 70)

print("Subtotal Amount: Rs.", round(subtotal_total, 2))
print("Total Tax:       Rs.", round(tax_total, 2))
print("Amount Before Discount: Rs.", round(grand_total, 2))
print("Discount Rate:", discount_rate, "%")
print("Discount Amount: Rs.", round(discount, 2))
print("Maximum Discount: Rs.", maximum_discount)

print("----------------------------------------------")
print("FINAL PAYABLE AMOUNT: Rs.", round(final_amount, 2))
print("==============================================")

print("Thank you for shopping!")

