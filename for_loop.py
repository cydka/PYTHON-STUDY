fruits=['apple','banana','cherry','avocado']
for fruit in fruits:
    print(fruits)
    # if fruit=='banana':
    #     print(fruit)

    # range function is used to create a list of numbers 
    # from certain number to certain number
    x=[1,2,3,4,5,6,7,8,9,10]
    y=list(range(1,11))
    num=list(range(1,1000))

    print(num)
    # iterate thru numbers btwn 20 t0 100

    c=list(range(20,101))
    for num in c:
        print(num)
# iterate thru number btwn 20 to 100 but only display even numbers
numbers=list(range(20,101))
even_numbers=[]

for i in numbers:
      if i%2==0:
           even_numbers.append(i)
           print(even_numbers)
# break is used to stop loop
ls1 = list(range(20,50))
res = []
for i in ls1:
    # if i % 2 ==0:
    #     res.append 
    if i == 30:
        break
    if i%2==0:
        res.append(i)
else:
    pass
