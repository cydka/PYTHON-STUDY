
# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
# Once you learn functions,revisit this and write this code inside a function.

# Prompt the user to enter a number
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
