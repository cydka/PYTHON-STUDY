
# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.

# Define the list of products
prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

# Initialize a variable to store the total stock
total_stock = 0

# Loop through each product and add the stock to total_stock
for product in prods:
    total_stock += int(product[-1])  # Convert the last element to an integer and add to total_stock

# Display the total stock
print("Total stock:", total_stock)
