def draw_triangle():
    for i in range(8):
        print(' ' * (7 - i), '*' * i, '*', '*' * i, sep='')

# основная программа
draw_triangle()  # вызов функции