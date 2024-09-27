import time

def cache(func):
    cachevalue={}
    print(cachevalue)
    def wrapper(*args):
        if args in cachevalue:
            return cachevalue[args]
        res=func(*args)
        cachevalue[args]=res
        return res
    return wrapper

@cache
def add(a,b):
    time.sleep(4)
    return a+b

print(add(3,6))
print(add(4,6))
