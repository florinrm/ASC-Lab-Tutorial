from threading import Thread, Barrier

NO_THREADS = 8
barrier = Barrier(NO_THREADS)


class MyThread(Thread):
    def __init__(self, index):
        Thread.__init__(self)
        self.index = index

    def run(self):
        print("Before the barrier in thread no. %d" % self.index)
        barrier.wait()
        print("After the barrier in thread no.%d" % self.index)


def main():
    threads = []

    for i in range(0, NO_THREADS):
        threads.append(MyThread(i))
        threads[-1].start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
