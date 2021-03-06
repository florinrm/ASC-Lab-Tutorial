from threading import Thread, RLock, Lock
from math import ceil

lst = []
NO_THREADS = 8
rlock = RLock()


def decrement(index):
    start = index * ceil(len(lst) / NO_THREADS)
    end = min(len(lst), ((index + 1) * ceil(len(lst) / NO_THREADS)))

    for i in range(start, end):
        if lst[i] > 0:
            rlock.acquire()
            lst[i] -= 1
            decrement(index)
            rlock.release()


def main():
    global lst

    # varianta 2
    lst = [x for x in range(1, 21)]
    print(lst)

    threads = []
    for i in range(0, NO_THREADS):
        threads.append(Thread(target=decrement(i)))
        threads[-1].start()

    for t in threads:
        t.join()
    print(lst)


if __name__ == '__main__':
    main()
