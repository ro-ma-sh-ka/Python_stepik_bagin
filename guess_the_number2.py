from random import *

left, right = 1, int(input())
n_pass = right
counter, middle = 0, 0

while middle != n_pass:
    middle = (left + right) // 2
    if middle > n_pass:
        right = middle - 1
    elif middle < n_pass:
        left = middle + 1
    counter += 1

print(counter)