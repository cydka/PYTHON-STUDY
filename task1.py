# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a func
# Prompt the user to enter the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = 0.5 * base * height
print(area)



# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a fun

# Prompt the user to enter a number
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

if number % 4 == 0:
    print("divisible by 4")


