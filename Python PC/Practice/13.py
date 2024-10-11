
# check if a list is palindorome or not
list1=[1,2,1]

list2cpy=list1.copy()
list2cpy.reverse()

print(list1)
print(list2cpy)
if(list1==list2cpy):
    print("it is palindrome")
else:

    print("it is not palindrome")
