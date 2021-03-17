from threading import Semaphore, Lock, Thread, current_thread

NO_THREADS = 8


class SimpleBarrierWithSemaphore:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.count_threads = 0
        self.sem = Semaphore(0)  # punem zero, ca ele sa se blocheze la acquire
        self.lock = Lock()

    def wait(self):
        with self.lock:
            self.count_threads += 1
        if self.count_threads == self.num_threads:
            for _ in range(self.num_threads):
                self.sem.release()  # creste count-ul din semafor, astfel thread-urile se deblocheaza unul cate unul
        self.sem.acquire()  # daca semaforul e pe 0, thread-ul se blocheaza


class MyThread(Thread):
    def __init__(self, barrier):
        Thread.__init__(self)
        self.barrier = barrier

    def run(self):
        print("Before barrier in thread %s" % current_thread().name)
        self.barrier.wait()
        print("After barrier in thread %s" % current_thread().name)


def main():
    threads = []
    barrier = SimpleBarrierWithSemaphore(NO_THREADS)
    for i in range(NO_THREADS):
        threads.append(MyThread(barrier))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
