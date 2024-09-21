# grade calculator

user_marks=float(input("enter your marks obtained: "))

if user_marks>=90 and user_marks<=100:
    print("you obtained A grade")
elif user_marks>=80 and user_marks<90:
    print("you obtained B grade")
elif user_marks>=70 and user_marks<80:
    print("you obtained C grade")
elif user_marks>=60 and user_marks<70:
    print("you obtained D grade")
elif user_marks<60:
    print("you obtained F grade")
else:
    print("Invalid Parameter")


