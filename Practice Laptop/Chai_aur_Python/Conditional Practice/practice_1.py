# solve conditional problem

user_age=int(input("ener your age: "))
if user_age<13:
    print("child")
elif user_age>=13 and user_age<=19:
    print('teenager')
elif user_age>=20 and user_age<=50:
    print("adult")
elif user_age>60:
    print("senior")
else:
    pass
