a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 > b1 or a1 > b2:  # отрезки не совпадают
    print("пустое множество")
elif a2 == b1:  # а1b1 перед отрезком a2b2 и касаются друг друга
    print(a2)
elif a1 == b2:  # а2b2 перед отрезком a1b1 и касаются друг друга
    print(a1)
elif a2 >= a1 and b1 >= b2:  # a2b2 внутри  a1b1 или совпадают
    print(a2, b2)
elif a2 <= a1 and b2 >= b1:  # a1b1 внутри  a2b2 или совпадают
    print(a1, b1)
elif a2 > a1 and b2 > b1:  # a2b2 впереди a1b1
    print(a2, b1)
elif a1 > a2 and b1 > b2:  # a1b1 впереди a2b2
    print(a1, b2)