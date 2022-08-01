from math import ceil, floor
n = int(input())
for i in range(1, ceil(n / 2) + 1):
    for _ in range(1, i + 1):
        print('*', end='')
    print()
for i in range(floor(n / 2), 0, -1):
    for _ in range(i, 0, -1):
        print('*', end='')
    print()