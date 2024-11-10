# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

math=int(input("enter maths:"))
english=int(input("enter eng:"))
kisw=int(input("enter kisw:"))
sci=int(input("enter sci:"))
sos=int(input("enter sos:"))

def calc_total_marks(m,e,s,sc,so):
    sum=m+e+s+sc+so
    return sum
total_marks=calc_total_marks(math,english,kisw,sci,sos)
print(f'total marks is {total_marks}')


# calculate average marks

def calculate_average(total_marks):
    average=total_marks/5
    return average
avg=calculate_average(total_marks)
print(f'average is{avg}')


def determine_grade(average):
    if average > 79:
        grade='A'
    elif 60 <= average <= 79:
        grade='B'
    elif 50 <= average < 60:
        grade='C'
    elif 40 <= average < 50:
        grade='D'
    else:
        grade='E'

        return grade
    f grade=find grade(avg)
