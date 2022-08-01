n, s = int(input()), input()
for c in s:
    if ord(c) - n < 97:
        print(chr(ord(c) - n + 26), end='')
    else:
        print(chr(ord(c) - n), end='')