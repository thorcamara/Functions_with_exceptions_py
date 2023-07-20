def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERROR: please, type a valid Integer.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31m\nUser chose not to enter this number.\033[m')
            return 0
        else:
            return n


def readFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERROR: please, type a valid Float.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mUser chose not to enter this number.\033[m')
            return 0
        else:
            return n


n1 = readInt('Type a Integer: ')
n2 = readFloat('Type a Float: ')
print(f'The \033[1;34mInteger\033[m number entered was \033[1;32m{n1}\033[m and the \033[1;34mFloat\033[m was \033[1;32m{n2}\033[m.')
