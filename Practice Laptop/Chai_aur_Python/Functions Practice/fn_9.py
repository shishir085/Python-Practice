'''
def print_even_numbers(limit):
    for i in range(2, limit + 1, 2):
        print(i)

print_even_numbers(20)

'''


# def even_generator(limit):
#     for i in range(2,limit+1,2):
#       return i
# even_generator(99)    


# def evengenerator(num):
#     for i in range(2,num+1,2):
#     #    print (i)
#       yield i
 
# evengenerator(99)


def evengenerator (limit):
    for i in range(2,limit+1,2):
        yield i

for num in evengenerator(10):
    print(num)


