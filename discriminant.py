def solve(a, b, c):
    from math import sqrt
    D = pow(b, 2) - 4 * a * c
    if D == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        D1 = (-b + sqrt(D)) / (2 * a)
        D2 = (-b - sqrt(D)) / (2 * a)
        return min(D1, D2), max(D1, D2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)