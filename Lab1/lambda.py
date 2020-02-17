def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # ciobaneste
    l1 = []
    for e in l:
        if e % 2 == 0:
            l1.append(e)

    l2 = []
    for e in l:
        l2.append(e + 2)

    print(l1)
    print(l2)

    l1.clear()
    l2.clear()

    # now some Vietnam flashbacks
    # lambda functions
    l1 = list(filter(lambda x: x % 2 == 0, l))
    l2 = list(map(lambda x: x + 2, l))

    print(l1)
    print(l2)

    l1.clear()
    l2.clear()

    # list comprehensions
    l1 = [x for x in l if x % 2 == 0]
    l2 = [(x + 2) for x in l]

    print(l1)
    print(l2)

if __name__ == '__main__':
    main()
    