chai="lemon,ginger,mint,masala"

# print(chai.split(", "))   # into list 

'''
chiya='masala chiya'
print(chiya.find("chiya"))

chai1="masala chai chai chai chai"
print(chai1.count("chai"))
'''

'''
chai_type="Masala"
quantity=2
order="i ordered {} cups of {} chai"
print(order.format(quantity,chai_type))


a='apple'
a1=2
b="banana"
b2=3
bought='i ordered {} of {} kgs and {} of {} dozens.'
print(bought.format(a,a1,b,b2))

'''
for el in chai:
    print(el , end=" ")


chai_type=['lemon','masala','ginger']

print(" ".join(chai_type))  #convert into string from list
print("-".join(chai_type))  #convert into string from list


data="c:\\user\\pwd"
data1=r"c:\user\pwd"   #raw

print(data)
print(data1)