

print("===== EMPLOYEE PAYROLL SYSTEM =====")


name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")


basic = float(input("Enter Basic Salary: "))
allowances = float(input("Enter Allowances: "))
overtime = float(input("Enter Overtime Amount: "))
incentives = float(input("Enter Incentives: "))


if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid Input! Salary amounts cannot be negative.")

else:
   
    gross_salary = basic + allowances + overtime + incentives

   
    if gross_salary <= 20000:
        deduction_rate = 0

    elif gross_salary <= 40000:
        deduction_rate = 5

    elif gross_salary <= 60000:
        deduction_rate = 10

    else:
        deduction_rate = 15

  
    deduction = gross_salary * deduction_rate / 100

   
    net_salary = gross_salary - deduction

  
    print("\n========== SALARY STATEMENT ==========")

    print("Employee Name:", name)
    print("Employee ID:", emp_id)

    print("--------------------------------------")
    print("Basic Salary       : Rs.", basic)
    print("Allowances         : Rs.", allowances)
    print("Overtime Amount    : Rs.", overtime)
    print("Incentives         : Rs.", incentives)

    print("--------------------------------------")
    print("Gross Salary       : Rs.", gross_salary)
    print("Deduction Rate     :", deduction_rate, "%")
    print("Total Deduction    : Rs.", deduction)

    print("--------------------------------------")
    print("Net Salary         : Rs.", net_salary)
    print("======================================")

