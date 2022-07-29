n = int(input())
largest = 0
smallest = 9
while n != 0:
    if n % 10 > largest:
        largest = n % 10
    if n % 10 < smallest:
        smallest = n % 10
    n //= 10
print("Максимальная цифра равна", largest)
print("Минимальная цифра равна", smallest)