n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + i):
        if j <= i:
            print(j, end='')
        else:
            print(i - (j - i), end='')
    print()