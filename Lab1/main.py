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



if __name__ == '__main__':
    main()
    