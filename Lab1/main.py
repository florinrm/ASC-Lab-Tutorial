# functie goala (body gol)
def func():
    pass


def inc(n):
    n += 1


def edit_list(l):
    l.append([1, 2, 3, 4, 5])


def check_if_exists(id, d):
    for key in d.keys():
        if key == id:
            return True
    return False


def main():
    print('Choose one of the following options')
    print('1: Register a new employee')
    print('2: Search for an employee')
    print('3: Delete an employee')
    print('4: Quit')

    register = dict()

    n = int(input())
    while True:
        if n == 1:
            print('Type the ID')
            id_user = int(input())
            print('Type the name')
            name = input()

            if check_if_exists(id_user, register):
                print('ID %d already exists' % id_user)
            else:
                register[id_user] = name
        elif n == 2:
            print('Type the ID')
            id_user = int(input())
            if check_if_exists(id_user, register):
                print('Employee %d: %s' % (id_user, register[id_user]))
            else:
                print('Employee doesn\'t exist')
        elif n == 3:
            print('Type the ID')
            id_user = int(input())
            if check_if_exists(id_user, register):
                del register[id_user]
            else:
                print('Employee doesn\'t exist')
        elif n == 4:
            print('Quitting...')
            break
        else:
            print('Option not valid, choose a valid one please')

        print('Choose one of the following options')
        print('1: Register a new employee')
        print('2: Search for an employee')
        print('3: Delete an employee')
        print('4: Quit')
        n = int(input())

    p = 0
    inc(p)
    print(p)

    l = [1, 2, 3, 4]
    edit_list(l)
    print(l)


if __name__ == '__main__':
    main()
