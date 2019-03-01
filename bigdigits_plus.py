import sys

zero = [' ***** ', '*     *', '*     *', '*     *', '*     *', '*     *', ' ***** ']
one =  ['   *   ', '  **   ', '   *   ', '   *   ', '   *   ', '   *   ', ' ***** ']
two =  [' ***** ', '*     *', '*     *', '     * ', '   *   ', ' *     ', '*******']
three =[' ***** ', '*     *', '      *', '    ** ', '      *', '*     *', ' ***** ']
four = ['    *  ', '   **  ', '  * *  ', ' *  *  ', '*******', '    *  ', '    *  ']
five = [' ***** ', '*      ', '*      ', ' ***** ', '      *', '*     *', ' ***** ']
six =  [' ***** ', '*      ', '*      ', '****** ', '*     *', '*     *', ' ***** ']
seven =[' ***** ', '*     *', '     * ', '    *  ', '   *   ', '   *   ', '   *   ']
eight =[' ***** ', '*     *', '*     *', ' ***** ', '*     *', '*     *', ' ***** ']
nine  =[' ***** ', '*     *', '*     *', ' ******', '      *', '      *', ' ***** ']
digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    nums = sys.argv[1]
    row = 0
    while row < 7:
        line = ''
        colume = 0
        while colume < len(nums):
            num = int(nums[colume])
            digit = digits[num]
            i = 0
            while i < 7:
                if digit[row][i] == ' ':
                    line += ' '
                else:
                    line += str(num)
                i += 1
            line += '  '
            colume += 1
        print(line)
        row += 1
except IndexError:
    print('usage: bigdigits.py <number>')
except ValueError:
    print('Please input a integer.')
