# Decorators
import time

def time_it(func):
    def wraper(*args, **kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()
        # func.__name__ returns the name of function
        print(f"{func.__name__} executed in {end-start} milsec")
        return results
    
    return wraper

@time_it
def square(number):
    results = []
    for item in number:
        results.append(item*item)
    return results

@time_it
def cube(number):
    results = []
    for item in number:
        results.append(item*item*item)
    return results

array = range(1,100000)
square(array)
cube(array)
# print(out)
