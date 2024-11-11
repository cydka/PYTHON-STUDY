# offers a concise way to create a new list from another
# create list of even numbers between 20 and 100
even_numbers=[i for i in range(20,100)if i%2==0]
# for i in range(20,101):
    # if i%2==0:
        # even_numbers.append(i)
print(even_numbers)

# store in a list square of numbers between 1 and 20

square_numbers=[i**2 for i in range(1,21)]

print(square_numbers)
