tea_types=['Black','Green','Masala','White']

for tea in tea_types:
    print(tea,end=",")



tea_types.append('Oolong')

if "Oolong" in  tea_types:
    print("\nOolong tea is available")
else:
    print("\nOolong tea is not available")

'''
tea_types.pop()

for tea in tea_types:
    print(tea,end=",")

'''

tea_types.remove('Green')

tea_types.insert(1,"Green")
# print(tea_types)


tea_types_copy=tea_types.copy()
'''

tea_types_copy.append("Lemon")
print(tea_types_copy)
print(tea_types)

'''

squared_num=[x**2 for x in range(1,10)]
print(squared_num) 