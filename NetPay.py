import EmployeeClass as employee
import PayrollDeductionClass as deduction

Jimmy_Smith = employee.employee("Jimmy Smith", 58475, "Information Systems", "Developer", 6800)

print(f"Name, ID Number, Department, Job Title, Monthly Salary")
print(f"{Jimmy_Smith.get_name()}, {Jimmy_Smith.get_ID_number()}, {Jimmy_Smith.get_department()}, {Jimmy_Smith.get_job_title()}, {Jimmy_Smith.get_monthly_salary()}")

first = deduction.payroll_deduction("food court", "8/14/2022", 22.5, 39119)
second = deduction.payroll_deduction("gift contribution", "8/12/2022", 25.0, 58475)
third = deduction.payroll_deduction("food court", "8/17/2022", 15.25, 21547)
fourth = deduction.payroll_deduction("vending machine", "8/22/2022", 3.0, 58475)
fifth = deduction.payroll_deduction("vending machine", "8/5/2022", 2.75, 58475)
print()
print(f"Description, Date, Charge, EmployeeID")
print(f"{first.get_Description()}, {first.get_Date()}, {first.get_Charge()}, {first.get_EmployeeID()}")
print(f"{second.get_Description()}, {second.get_Date()}, {second.get_Charge()}, {second.get_EmployeeID()}")
print(f"{third.get_Description()}, {third.get_Date()}, {third.get_Charge()}, {third.get_EmployeeID()}")
print(f"{fourth.get_Description()}, {fourth.get_Date()}, {fourth.get_Charge()}, {fourth.get_EmployeeID()}")
print(f"{fifth.get_Description()}, {fifth.get_Date()}, {fifth.get_Charge()}, {fifth.get_EmployeeID()}")
print()

print(f"*** Employee Pay ***")
print(f"Name: {Jimmy_Smith.get_name()}")
print(f"ID Number: {Jimmy_Smith.get_ID_number()}")
print(f"Department: {Jimmy_Smith.get_department()}")
print(f"Gross Pay: ${Jimmy_Smith.get_monthly_salary()}")
print(f"Net Pay: ${Jimmy_Smith.get_monthly_salary() - (second.get_Charge()) - (fourth.get_Charge()) - (fifth.get_Charge())}")


