# Sharing Data Between Processes Using Array and Value

import multiprocessing
import multiprocessing.process

def calc_square(number, result, v):
    v.value = 5.65
    for idx, n in enumerate(number):
        result[idx] = n*n
    

if __name__ == '__main__':
    arr = [1,2,3]

    result = multiprocessing.Array('i', 3) # i: integer, 3: as array contains 3 variables
    v = multiprocessing.Value('d', 0.0)

    p = multiprocessing.Process(target=calc_square, args=(arr, result, v))

    p.start()
    p.join()

    print(result[:])
    print(v.value)
    print("__done__")