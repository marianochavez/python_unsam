# print headers
headers = '   '
for num in range(10):
    headers += f'{num:>4d}'
print(headers)
# print separators
separators = print(f'{"_"*len(headers)}')
# print table
for n, num_1 in enumerate(range(10)):
    num_table = f'{n:<2d}:'
    for num_2 in range(10):
        num_table += f'{num_1*num_2:4d}'
    print(num_table)

"""
      0   1   2   3   4   5   6   7   8   9
___________________________________________
0 :   0   0   0   0   0   0   0   0   0   0
1 :   0   1   2   3   4   5   6   7   8   9
2 :   0   2   4   6   8  10  12  14  16  18
3 :   0   3   6   9  12  15  18  21  24  27
4 :   0   4   8  12  16  20  24  28  32  36
5 :   0   5  10  15  20  25  30  35  40  45
6 :   0   6  12  18  24  30  36  42  48  54
7 :   0   7  14  21  28  35  42  49  56  63
8 :   0   8  16  24  32  40  48  56  64  72
9 :   0   9  18  27  36  45  54  63  72  81
"""
