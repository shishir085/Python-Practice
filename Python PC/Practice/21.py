# for loop

lists=[1,6,9,4,6,4,2]
lists1=(1,6,9,4,6,4,2)

# for value in lists:
    # print(value)
# else:
    # print("end of list") 


#  /////////////////////////////

stri="crimsoncollege"

for char in stri:
    if (char=='n'):
        # print('n found')
        break
    # print(char)

# print("end of line")



# practice

list2=[1,4,9,16,25,36,49,64,81,100]
# for num in list2:
#     print(num)

idx=0
list3=(1,4,9,16,25,36,49,64,81,100,49)
x=49
for num in list3:
    if (num==x):
        print("found in ",idx," index") 
        break
    idx+=1