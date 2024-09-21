# file input/ output in python

f=open("14.txt","r")
data=f.read()

# print(data)
# print(type(data))

f.close()



f=open("14.txt","r")
# data1=f.read()
# print(data1)

# data2=f.readline()
# print(data2)

# data3=f.read(5)
# print(data3)


f.close()




f=open("14.txt","w")


write1=f.write("i want to learn js tomorrow. 123134")

# print(write1)

f.close()


f=open("14.txt","a")


write1=f.write("\n then i will move to react js")

# print(write1)

f.close()






