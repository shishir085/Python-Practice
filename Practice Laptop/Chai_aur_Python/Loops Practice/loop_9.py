# find the duplicate and print it
items=['apple','banana','orange','banana','apple','mango','mango']

unique_set=set()

for fruit in items:
    if fruit in unique_set:
        print("duplicate item is:", fruit)
        # break
    unique_set.add(fruit)






'''
for fruit in items:
    i=0
    if fruit==items[i]:
        print("duplicate fruit is: ",fruit)
        i+=1
        break
    else:
'''