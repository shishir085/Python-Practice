tea_shop={
    "chai":{"masala":"spicy","ginger":"zesty"},
    "tea":{"green":'mild','black':'strong'}
}

print(tea_shop)

print(tea_shop["chai"]['masala'])
'''
square_num=[x**2 for x in range(1,11)]
print(square_num)

squared_num={x:x**2 for x in range(1,11)}
print(squared_num)

'''

tea_shop.clear()
print(tea_shop)

# constructing a dictionary

keys=['masala','ginger','lemon']

default_value="delicious"

new_dict=dict.fromkeys(keys,default_value)
print(new_dict)