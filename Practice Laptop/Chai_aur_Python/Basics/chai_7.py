# dict
chai_types={
    'masala':'spicy',
    'ginger':'zesty',
    'green':'mild'
}


print(chai_types.get("ginger"))

print(chai_types['green'])


chai_types['green']='fresh'
print(chai_types)
'''
for chai in chai_types:
    print(chai,':',chai_types[chai])
'''

for key,value in chai_types.items():
    print(key,':',value)

if 'masala'  in chai_types:
    print('i have masala chai')

print(len(chai_types))

chai_types['earl grey']="citrus"
print(chai_types)

chai_types.pop("ginger")
print(chai_types)

chai_types.popitem()
print(chai_types)
del chai_types['green']
print(chai_types)

chai_types_copy=chai_types.copy()


