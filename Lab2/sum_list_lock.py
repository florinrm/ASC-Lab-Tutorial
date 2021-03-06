from threading import Thread, Lock
from math import ceil

lst = []
NO_THREADS = 8
total_sum = 0
lock = Lock()


class MyThread(Thread):
    def __init__(self, index):
        Thread.__init__(self)
        self.index = index

    def run(self):
        global total_sum
        start = self.index * ceil(len(lst) / NO_THREADS)
        end = min(len(lst), ((self.index + 1) * ceil(len(lst) / NO_THREADS)))

        for i in range(start, end):
            lock.acquire()
            total_sum += lst[i]
            lock.release()


def main():
    global lst

    lst = [x for x in range(1, 101)]

    threads = []
    for i in range(0, NO_THREADS):
        threads.append(MyThread(i))
        threads[-1].start()

    for t in threads:
        t.join()
    print(total_sum)


if __name__ == '__main__':
    main()
