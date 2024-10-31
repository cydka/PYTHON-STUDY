# Write a program that displays a numbers 1 to 50 inside a list.
# Generate a list of numbers from 1 to 50
numbers = list(range(1, 51))
print(numbers)

# From 1 above display the ones divisible by 7 or 5 inside a list.
numbers = list(range(1, 51))
divisible_numbers=[]
for num in numbers:
    if num %7==0 or num %5==0:
        divisible_numbers.append(num)
        print(divisible_numbers)

# Find sum and average of values in the range between 10 to 40.
numbers = list(range(10,41))
total_sum = sum(numbers)


# Put in a list the first 10 odd numbers between 10 to 50. 
# Generate a list of odd numbers between 10 and 50


# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.

