# In order to see how much time multiprocessing pool can save as compared to serial processing

import time
from multiprocessing import Pool

def calc_square(n):
    sum = 0
    for x in range(10000):
        sum += x*x
    return sum

if __name__ == '__main__':

    # arr = []
    # for i in range(100000+1):
    #     arr.append(i)

    # time.time() takes the current time
    print("Parallel compouting results:")
    t1 = time.time()
    result = []
    p = Pool()
    result = p.map(calc_square, range(10000))
    p.close()
    p.join()
    
    print(f"time taken: {time.time() - t1}")

    print("=============")
    print("Serial Computing results:")
    
    t2 = time.time() 
    result = []
    for i in range(10000):
        result.append(calc_square(i))
    # print(result)
    print(f"time taken: {(time.time() - t2)}")
    
    print("__done__")
    


