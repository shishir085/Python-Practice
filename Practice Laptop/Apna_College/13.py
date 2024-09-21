    # recusion 

def show(n):
    if(n==0):
        return
    # print(n)
    show(n-1)

show(5)

# factorial


def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)


factorial=fact(4)
# print(factorial)


# sum of first n natural numbers  using recursion


def sum(n):
    
    if(n==0):
        return 0
   
    
    return sum(n-1)+n

# print(sum(9))


# rec fn to print all el in a list

def rec_fn(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    rec_fn(list,index+1)

fruit=("apple","mango",'banana')
rec_fn(fruit)