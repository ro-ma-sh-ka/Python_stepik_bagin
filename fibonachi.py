n = int(input())
first_number = 0
second_number = 1
fibonachi = 1
for _ in range(1, n + 1):
    print(fibonachi, end=" ")
    fibonachi = first_number + second_number
    second_number, first_number = fibonachi, second_number