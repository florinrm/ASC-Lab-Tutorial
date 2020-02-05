def func():
    pass

def main():
    # reading input
    # reading a phrase (string)
    line = input()
    words = line.split() # obtaining a list of words
    print(words)
    print(line.split(','))

    # reading integers
    a = int(input()) # input returns a string, gotta convert in int
    b = int(input())
    print("a + b = " + str(a + b))

    # lists
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l)
    l.pop() # se sterge ultimul element
    print(l)
    l.append(69)
    print(l)




if __name__ == '__main__':
    main()
    