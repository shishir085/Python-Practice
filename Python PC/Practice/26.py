num=[1,5,6,74,5,4,56,5,5]

def lis(lists):
    print(len(lists))
    print(lists[4],end=" ")
    print(lists[5],)

# lis(num)


#  factorial using function 

def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact*=i
        i=i+1

    print(fact)
    
# fact(4)

#  usd to nepali converter

def convert(usd):
    npr=usd*132
    print(usd,"USD","=",npr,"NPR")

# convert(2)
 


# input a number and print odd string else even string

num_1=int(input('enter a number'))

def fn(n):
    if n%2==1:
        return "odd"
    elif n%2==0:
        return "even"
    

data=fn(num_1)
print(data)