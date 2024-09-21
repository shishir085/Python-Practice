# reverse string using a loop

string=input("enter a string : ") 
reversed_str=''

for letter in string:
    reversed_str=letter+reversed_str
print(reversed_str)


