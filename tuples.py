# create a tuple
marks=(100,300,250,160,450,600)
# print(type(marks))

print(marks[5])


# printinto a list
marks=list(marks)
print(type(marks))


# print back to tuple
marks=tuple(marks)
print(type(marks))
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days[2])
print(len(days))
days=(list(days))
days[3]="Thur"
days=tuple(days)
print(days)

my_tuple=("age",14,'location',"kiambu",[100,300,500])
my_tuple[4][1]=1000
print(type(my_tuple))
