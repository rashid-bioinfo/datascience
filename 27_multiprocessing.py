import time
import multiprocessing

results = []

def calc_sqaure(number):
    global results
    for n in number:
        results.append(n*n)
    
    print(f"results (within function): {results}")

if __name__ == '__main__':
    arr = [1,2,3,4,5]

    p1 = multiprocessing.Process(target=calc_sqaure, args=(arr,))

    p1.start()

    p1.join()

    print(f"results (global): {results}")
    print("Done")