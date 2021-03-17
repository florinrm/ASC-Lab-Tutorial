from threading import Semaphore, Lock, Thread, current_thread

NO_THREADS = 8


class ReentrantBarrierWithSemaphore:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        # folosim liste, deoarece daca am folosi doar variabile simple, resetarea din phase
        # nu va fi vizibila
        self.count_threads1 = [0]
        self.count_threads2 = [0]
        self.sem1 = Semaphore(0)  # punem zero, ca ele sa se blocheze la acquire
        self.sem2 = Semaphore(0)
        self.lock = Lock()

    def wait(self):
        self.phase(self.sem1, self.count_threads1)
        self.phase(self.sem2, self.count_threads2)

    def phase(self, sem, count_threads):
        with self.lock:
            count_threads[0] += 1
        if count_threads[0] == self.num_threads:
            for _ in range(self.num_threads):
                sem.release()  # creste count-ul din semafor, astfel thread-urile se deblocheaza unul cate unul
            count_threads[0] = 0  # resetam contorul, pentru ca bariera sa fie refolosita
        sem.acquire()  # daca semaforul e pe 0, thread-ul se blocheaza


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
    barrier = ReentrantBarrierWithSemaphore(NO_THREADS)
    for i in range(NO_THREADS):
        threads.append(MyThread(barrier))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
