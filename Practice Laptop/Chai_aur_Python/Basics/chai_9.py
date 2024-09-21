# tuples in py
# immutable

tea_types=('black','green','oolong')

print(tea_types)

print(tea_types[2])

print(len(tea_types))

more_tea=('herbal','masala')

all_tea=more_tea+tea_types
print(all_tea)


if "green"in all_tea:
    print("i have green tea")

more_tea1=('herbal','earl gray','herbal')
print(more_tea1.count('herbal'))

