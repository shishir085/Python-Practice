# keep asking the user until they enter a num between 1 and 10

num=int(input("enter a number between 1 and 10: "))
while True:
    if 1<=num<=10:
        print("num between 1 and 10 is : ",num)
        break
    else:
        num=int(input("enter a number between 1 and 10: "))
    