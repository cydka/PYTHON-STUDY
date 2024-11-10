
# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

# Set correct credentials
correct_email = "admin@mail.com"
correct_password = "Admin@123"

# Set the maximum number of attempts
attempts = 3

# Loop to allow up to 3 attempts
while attempts > 0:
    # Take email and password as input
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Check if credentials are correct
    if email == correct_email and password == correct_password:
        print("Login is Successful")
        break
    else:
        attempts -= 1
        print(f"Invalid username or password. You have {attempts} attempts left.")
        
    # If no attempts are left, notify the user of being blocked
    if attempts == 0:
        print("You have been blocked.")
