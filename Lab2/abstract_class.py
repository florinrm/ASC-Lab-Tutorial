from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def __init__(self, n):
        ABC.__init__(self)
        self.n = n

    def fulala(self):
        print('fulala')

    # daca bagam acest decorator, se forteaza implementarea metodei in subclasa (care sa nu fie abstracta)
    @abstractmethod
    def something(self):
        pass


class SubClass(AbstractClass):
    def __init__(self, a, b):
        AbstractClass.__init__(self, a)
        self.b = b

    def something(self):
        print('Ceva implementare')


def main():
    obj = SubClass(1, 2)
    obj.something()
    obj.fulala()


if __name__ == '__main__':
    main()
