def func():
    pass

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
            id = int(input())
            print('Type the name')
            name = input()

            if check_if_exists(id, register):
                print('ID %d already exists' %(id))
            else:
                register[id] = name
        elif n == 2:
            print('Type the ID')
            id = int(input())
            if check_if_exists(id, register):
                print('Employee %d: %s' %(id, register[id]))
            else:
                print('Employee doesn\'t exist')
        elif n == 3:
            print('Type the ID')
            id = int(input())
            if check_if_exists(id, register):
                del register[id]
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

if __name__ == '__main__':
    main()
    