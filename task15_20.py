# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable.
def calculate_gross_salary(basic_salary, benefits):
    gross=basic_salary + benefits
    return gross
basic_salary = float(input("Enter the basic salary: "))
benefits = float(input("Enter the benefits amount: "))
gross_salary = calculate_gross_salary(basic_salary, benefits)
print(f"Gross Salary: {gross_salary}")


def calculate_nhif(gross_salary):
    if gross_salary<= 5999:
        nhif = 150
    elif 6000 <= gross_salary<= 7999:
        nhif = 300
    elif 8000 <= gross_salary <= 11999:
        nhif = 400
    elif 12000 <= gross_salary <= 14999:
        nhif = 500
    elif 15000 <= gross_salary <= 19999:
        nhif = 600
    elif 20000 <= gross_salary <= 24999:
        nhif = 750
    elif 25000 <= gross_salary <= 29999:
        nhif = 850
    elif 30000 <= gross_salary <= 34999:
        nhif = 900
    elif 35000 <= gross_salary <= 39999:
        nhif = 950
    elif 40000 <= gross_salary <= 44999:
        nhif = 1000
    elif 45000 <= gross_salary <= 49999:
        nhif = 1100
    elif 50000 <= gross_salary <= 59999:
        nhif = 1200
    elif 60000 <= gross_salary <= 69999:
        nhif = 1300
    elif 70000 <= gross_salary <= 79999:
        nhif = 1400
    elif 80000 <= gross_salary <= 89999:
        nhif = 1500
    elif 90000 <= gross_salary <= 99999:
        nhif = 1600
    else:
        nhif = 1700
    return nhif
nhif_deduction = calculate_nhif(gross_salary)
print(f"NHIF Deduction: {nhif_deduction}")



# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 

# Write a normal program but use functions if you feel comfortable.
def calculate_nssf(gross_salary):
  nssf_base = min(gross_salary, 18000)
  nssf_deduction = 0.06 * nssf_base 
  return nssf_deduction
nssf_deduction = calculate_nssf(gross_salary)
print(f"NSSF Deduction: {nssf_deduction:}")


