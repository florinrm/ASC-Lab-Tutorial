import time
from concurrent.futures.thread import ThreadPoolExecutor
from threading import current_thread

l = [x for x in range(1, 10001)]


def add_with_ten(n):
    print("Thread %s adds with ten" % current_thread().name)
    return n + 10


def mul_function(x, y):
    print("Thread %s multiplies" % current_thread().name)
    print('Task (%d multiply %d) started' % (x, y))
    time.sleep(2)
    print('Task (%d multiply %d) completed' % (x, y))
    return x * y


def main():
    # cu map - aplicata pe o structura iterabila (lista)
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(add_with_ten, l)
        print(list(results))

    # cu submit
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(mul_function, 3, 4)
        future2 = executor.submit(mul_function, 8, 8)
        print(future.result(), future2.result())


if __name__ == '__main__':
    main()
