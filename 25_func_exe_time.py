# To calculate function execution time

import time

def square(number):
    start = time.time()
    results = []
    for item in number:
        results.append(item*item)

    end = time.time()

    print(f"Excution time for square function is {(end-start)*1000} mil sec")
    return results

def cube(number):

    start = time.time()
    results = []
    for item in number:
        results.append(item*item*item)
    
    end = time.time()
    print(f"Excution time for sube function is {(end-start)*1000} mil sec")
    return results

array = range(1,100000)
square(array)
cube(array)
# print(out)
