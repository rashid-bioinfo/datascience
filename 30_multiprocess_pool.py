# Multiprocessing pool

from multiprocessing import Pool

def calc_square(n):
    return n*n

if __name__ == '__main__':
    arr = [1,2,3,4,5]

    # create multiprocessing pool
    p = Pool()
    # p.map(call_to_function, input)
    result = p.map(calc_square, arr)

    print(result)
    print("__done__")