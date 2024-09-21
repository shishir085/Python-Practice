# password strength checker

user_pass=len(input("enter password:"))

if user_pass<6:
    print("Weak password")

elif user_pass<=10:
    print("medium password")

elif user_pass>10:
    print("strong password")