number = int(input())
if number < 0 or number > 36:
    print("ошибка ввода")
elif number == 0:
    print("зеленый")
elif (number % 2 == 0) and (1 <= number <= 10 or 19 <= number <= 28):
    print("черный")
elif (number % 2 != 0) and (1 <= number <= 10 or 19 <= number <= 28):
    print("красный")
elif (number % 2 == 0) and (11 <= number <= 18 or 29 <= number <= 36):
    print("красный")
elif (number % 2 != 0) and (11 <= number <= 18 or 29 <= number <= 36):
    print("черный")