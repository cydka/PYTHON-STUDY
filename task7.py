
# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
marks=int(input("enter student marks"))

if 0<= marks <= 100:
    if marks>79:
        grade="A"
    elif 60 <= marks <= 79:
        grade="B"
    elif 50 <= marks <= 59:
        grade="C"
    elif 40 <= marks <= 49:
        grade="D"
    else:
        grade="E"
        print(grade)
# else:
#     print("invalid marks")
