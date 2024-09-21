
"""
print(0.1+0.1+0.1)
print(0.1+0.1+0.1-0.3)
print((0.1+0.1+0.1)-0.3)
"""

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1') -Decimal('0.3'))

# set

set1={1,2,3,4}
set2={2,5,6}

print(set1.union(set2))  
print(set1.intersection(set2))


print(set1 & set2)  #and
print(set1 | set2)  #or 

print(4 is 4)    #compares internally and datatype
print('4' is 4)