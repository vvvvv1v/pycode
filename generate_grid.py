import random

def get_int(msg, minimum, default):
    while True:
        try:        
            string = input(msg)
            if not string and default is not None:
                return default
            number = int(string) 
            if number < minimum:
                print('must be >=', minimum)
            else:
                return number
        except ValueError as err:
            print(err)

rows = get_int('rows: ', 1, None)
columes = get_int('columes: ', 1, None)
minimum = get_int('minimum (or Enter for 0): ', -1000000, 0)

default = 1000
if default <= minimum:
    default = 2 * minimum
maximum = get_int('maximum (or Enter for ' + str(default) + '): ', minimum, default)

row = 0
while row < rows:
    line = ''
    colume = 0
    while colume < columes:
        number = random.randint(minimum, maximum)
        string = str(number)
        while len(string) < 10:
            string += ' '
        line += string
        colume += 1
    print(line)
    row += 1
