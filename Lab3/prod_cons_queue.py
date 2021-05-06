import random
from queue import Queue
from threading import Thread

BUFF_SIZE = 10
NO_PROD = 10
NO_CONS = 40


class Producer(Thread):
    def __init__(self, prod_id, queue):
        Thread.__init__(self)
        self.prod_id = prod_id
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.full():
                n = random.randint(1, 100)
                print("Producer %d puts %d in queue" % (self.prod_id, n))
                self.queue.put(n)


class Consumer(Thread):
    def __init__(self, cons_id, queue):
        Thread.__init__(self)
        self.cons_id = cons_id
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                n = self.queue.get()
                print("Consumer %d takes %d from queue" % (self.cons_id, n))

def main():
    queue = Queue(BUFF_SIZE)
    threads = []

    for i in range(NO_PROD):
        threads.append(Producer(i, queue))

    for i in range(NO_CONS):
        threads.append(Consumer(i, queue))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
