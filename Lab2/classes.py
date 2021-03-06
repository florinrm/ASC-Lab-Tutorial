class A:
    def __init__(self, n):
        self.n = n
        print('A')

    def print(self):
        print('n = ' + str(self.n))


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('B')

    def print(self):
        print('(a, b) = (%d, %d)' % (self.a, self.b))


class C(A, B):
    def __init__(self, a, b, c):
        B.__init__(self, b, c)
        A.__init__(self, a)
        print('C')

    def print(self):
        A.print(self) # print din clasa A
        B.print(self) # print din clasa B

def main():
    obj = C(1, 2, 3)
    print(obj.n)
    print(obj.a)
    obj.print()


if __name__ == '__main__':
    main()
