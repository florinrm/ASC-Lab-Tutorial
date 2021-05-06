from threading import Condition, current_thread, Thread

NO_THREADS = 8


class ReusableBarrierWithCond:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.waiting_threads = 0
        self.cond = Condition()

    def wait(self):
        with self.cond:
            self.waiting_threads += 1
            if self.waiting_threads == self.num_threads:
                # daca a ajuns ultimul thread la bariera, se va apela notify_all
                # prin care se vor scoate thread-urile din starea waiting
                print("Thread %s sets the flag on true, all threads pass the barrier" % current_thread().name)
                self.cond.notify_all()
            else:
                # thread-urile (cu exceptia ultimului, care va face trigger de notify_all
                # se vor afla in starea waiting, pana la apelul de notify_all
                print("Thread %s reached the barrier and waits" % current_thread().name)
                self.cond.wait()


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
    barrier = ReusableBarrierWithCond(NO_THREADS)
    for i in range(NO_THREADS):
        threads.append(MyThread(barrier))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()

