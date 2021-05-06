from random import randint, seed
from threading import Semaphore, Thread
from time import sleep

sem = Semaphore(value=3)


def access(nr):
    sem.acquire()
    print("Thread ", nr, " enters")
    sleep(randint(1, 4))
    print("Thread ", nr, " finishes")
    sem.release()


def main():
    thread_list = []
    seed()  # seed-ul este current system time pentru generatorul de nr random

    for i in range(10):
        thread = Thread(target=access(i))
        thread_list.append(thread)
        thread_list[-1].start()

    # asteptam terminarea thread-urilor
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    main()

