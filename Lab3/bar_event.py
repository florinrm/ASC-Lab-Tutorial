from threading import Event, Lock, current_thread, Thread

NO_THREADS = 8


class SimpleBarrierWithEvent:
    def __init__(self, num_threads):
        self.num_threads = num_threads  # numarul de thread-uri pentru bariera
        self.waiting_threads = 0  # numarul de thread-uri in asteptare
        self.event = Event()
        self.lock = Lock()  # lock folosit pentru incrementarea numarului de thread-uri care ajung la bariera

    def wait(self):
        with self.lock:
            self.waiting_threads += 1
        if self.waiting_threads == self.num_threads:
            # daca a ajuns ultimul thread la bariera, se va seta flag-ul pe true
            # iar restul thread-urilor vor iesi din starea waiting
            print("Thread %s sets the flag on true, all threads pass the barrier" % current_thread().name)
            self.event.set()
        print("Thread %s reached the barrier and waits" % current_thread().name)
        self.event.wait()  # nu se va bloca executia thread-ului care seteaza flag-ul pe true


class MyThread(Thread):
    def __init__(self, barrier):
        Thread.__init__(self)
        self.barrier = barrier

    def run(self):
        # print("Before barrier in thread %s" % current_thread().name)
        self.barrier.wait()
        # print("After barrier in thread %s" % current_thread().name)


def main():
    threads = []
    barrier = SimpleBarrierWithEvent(NO_THREADS)
    for i in range(NO_THREADS):
        threads.append(MyThread(barrier))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
