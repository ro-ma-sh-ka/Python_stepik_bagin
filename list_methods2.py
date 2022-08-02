numbers = [8, 9, 10, 11]

# Заменил второй элемент списка на 17;
numbers.pop(1)
numbers.insert(1, 17)

# Добавил числа 4, 5 и 6 в конец списка;
for i in range(3):
    numbers.insert(100, 4 + i)

# Удалил первый элемент списка;
numbers.pop(0)

# Удвоил список;
numbers.extend(numbers)

# Вставил число 25 по индексу 3;
numbers.insert(3, 25)

# Вывел список, с помощью функции print()
print(numbers)