# factorial of a number using while loop

num=int(input("enter a number: "))
fact=1
while num>0:
    fact*=num
    num-=1
print("factorial is",fact)