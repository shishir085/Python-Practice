# timing function execution

# /write a decorator that measures the time a fn takes to execute

import time

def timer1(func):
    start=time.time()
    def wrapper(*args,**kwargs):# for getting unlimited arguments
        res=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return res

    return wrapper


@timer1
def examplefn(n):
    time.sleep(n)

examplefn(2)