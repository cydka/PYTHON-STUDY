# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.
# Prompt the user to enter four unique numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Determine the largest number without using max()
if num1 > num2 and num1 > num3 and num1 > num4:
    largest = num1
elif num2 > num1 and num2 > num3 and num2 > num4:
    largest = num2
elif num3 > num1 and num3 > num2 and num3 > num4:
    largest = num3
else:
    largest = num4

# Display the largest number
print("The largest number is:", largest)
