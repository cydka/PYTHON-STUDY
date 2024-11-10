
# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.
# Set the correct password
# correct_password = "admin@123"
# attempts = 4

# # Loop to check password input
# while attempts > 0:
#     # Prompt the user to enter the password
#     password = input("Enter password: ")
    
#     # Check if the entered password is correct
#     if password == correct_password:
#         print("Access granted")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect password. You have {attempts} attempts left.")
        
#     # If no attempts are left, block the account
#     if attempts == 0:
#         print("Account is blocked.")

attempts=4
correct_password="admin@123"

for i in range(attempts):
    password=input("enter password:")
    if password== correct_password:
        display="Access granted"
        break
    else:
        remaining_attempts=attempts-(i+1)
        print(f"incorrect password.You have {remaining_attempts} attempts remaining")
        if remaining_attempts==0:
            display="account blocked"
print(display)