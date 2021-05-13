from sys import argv


'''
In PyCharm puteti seta argumentele din linia de comanda
dand pe Edit Configurations (fix unde se ruleaza, in dreapta sus, 
unde scrie numele scriptului curent de Python)
'''
def main():
    print(argv[0]) # numele executabilului, ca in C
    print(argv[1])


if __name__ == '__main__':
    main()