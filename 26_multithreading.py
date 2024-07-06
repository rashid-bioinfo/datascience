# Multithreading

import time
import threading

def square(number):
    print("calculate square of numbers")
    for n in number:
        time.sleep(0.2)
        print(n*n)


def cube(number):
    print("calculate cube of numbers")
    for n in number:
        time.sleep(0.2)
        print(n*n*n)   

array = [2,4,8,9]
t = time.time()
# square(array)
# cube(array)

t1 = threading.Thread(target=square, args=(array,))
t2 = threading.Thread(target=cube, args=(array,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"done in {time.time()-t}")

# print(out)
