vertical_1, horizontal_1, vertical_2, horizontal_2 = int(input()), int(input()), int(input()), int(input())
if vertical_1 - vertical_2 > 1 or vertical_2 - vertical_1 > 1 or horizontal_1 - horizontal_2 > 1 or horizontal_2 - horizontal_1 > 1:
    print("NO")
else:
    print("YES")