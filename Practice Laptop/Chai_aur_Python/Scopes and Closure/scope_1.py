username="chaiaurcode"
def func():
    # username="chai"
    print(username)

# print(username)
# func()


x=99
def func2(y):
    z=x+y
    return z

res=func2(1)
# print(res)


def func3():
    global x
    x=12

# func3()
# print(x)

def f1():
    x=88
    def f2():
        print(x)
    f2()

f1()







