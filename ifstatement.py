# Take three inputs from a user, separately.
#  Print the largest of the numbers.
num1 =float(input ("Enter the first number: "))
num2 =float(input  ("Enter the second number: "))
num3 = float(input ("Enter the third number: "))
largest=max(num1,num2,num3)
print("the largest number is")
if num1>num2 and num1>num3:
    print(f"{num1}is the largest")

    if num2>num1 and num2>num3:
        print(f"{num2}is the largest")
    else:
        print(f"{num3}is the largest")

    

#     Hint: Determine what type of data is taken in as input.
# Take as input from a user the temperature if the temperature 
# is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” 
# otherwise display “Cold temperature”
# Take temperature as input
temperature =30

if temperature > 30:
    print("The temperature is too high")
elif temperature > 15:
    print("Normal temperature")
else:
    print("Cold temperature")

# 3.	Write a Python program that checks if a variable
#  x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100.
#  If both conditions are true, print "Conditions met"
# , otherwise print "Conditions not met"
x=int(input("enter number"))
y=int(input("enter number"))
if x<=10 <=20 and y >100:
    print("conditions met")
else:
    print("conditions not met")
# 4. Write a Python program that checks if a variable 
# password is equal to the string "secret123".
#  If it is, print "Access   granted", otherwise 
# print "Access denied"
# Check if password is correct
password = input("Enter password: ")
correct_password="secret123"
if password == correct_password:
    print("Access granted")
else:
    print("Access denied")

# 5. Write a Python program that checks if a variable
#  student_score is greater than 90. If true,
#  check if the attendance is greater than 80.
#  If both conditions are true, print 
# "Excellent student", otherwise print "Good score,
#  but attendance needs improvement
# Example values
student_score =float (input("enter student score:"))
attendance = int(input("enter student attendance:"))

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
else:
    print("poor score")

