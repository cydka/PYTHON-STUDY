
# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

# Prompt the user to enter a phone number
phone_number = input("Enter a phone number: ")

# Validate and convert the phone number to the +254 format
if phone_number.startswith("+254"):
    valid_number = phone_number
elif phone_number.startswith("07"):
    valid_number = "+254" + phone_number[1:]
elif phone_number.startswith("7"):
    valid_number = "+254" + phone_number
elif phone_number.startswith("254"):
    valid_number = "+" + phone_number
elif phone_number.startswith("01"):
    valid_number = "+254" + phone_number[1:]
elif phone_number.startswith("1"):
    valid_number = "+254" + phone_number
else:
    valid_number = "Invalid phone number format"

# Display the converted phone number
print(valid_number)
