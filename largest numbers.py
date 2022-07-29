n = int(input())
largest = 0
second_largest = 0
for _ in range(n):
    number = int(input())
    if number > largest:
        second_largest, largest = largest, number
    elif number > second_largest:
        second_largest = number
print(largest, second_largest, sep="\n")