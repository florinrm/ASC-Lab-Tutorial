from threading import Thread
from math import ceil

lst = []
NO_THREADS = 8


# varianta 1 - extindem clasa Thread si suprascriem metoda run
class MyThread(Thread):
    def __init__(self, index):
        Thread.__init__(self)
        self.index = index

    def run(self):
        start = self.index * ceil(len(lst) / NO_THREADS)
        end = min(len(lst), ((self.index + 1) * ceil(len(lst) / NO_THREADS)))

        for i in range(start, end):
            lst[i] += 1


def increment(index):
    start = index * ceil(len(lst) / NO_THREADS)
    end = min(len(lst), ((index + 1) * ceil(len(lst) / NO_THREADS)))

    for i in range(start, end):
        lst[i] += 1


def main():
    global lst

    # varianta 1
    print('Varianta 1')
    lst = [x for x in range(1, 21)]
    print(lst)

    threads = []
    for i in range(0, NO_THREADS):
        threads.append(MyThread(i))
        threads[-1].start()

    for t in threads:
        t.join()
    print(lst)

    # varianta 2
    print('Varianta 2')
    lst = [x for x in range(1, 21)]
    print(lst)

    threads = []
    for i in range(0, NO_THREADS):
        threads.append(Thread(target=increment(i)))
        threads[-1].start()

    for t in threads:
        t.join()
    print(lst)


if __name__ == '__main__':
    main()
